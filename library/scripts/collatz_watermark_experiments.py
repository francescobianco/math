#!/usr/bin/env python3
"""Measurements for a watermark/authentication use of the Collatz phase word.

The thesis tested here: the *structure* that makes the phase word useless as a
cipher keystream (forbidden words, forcing rules, local rigidity) is exactly
what makes it a good *fragile watermark* — tampering breaks the grammar and is
detected. We measure:

  E1  tamper-evidence: probability a single symbol substitution creates a
      forbidden window (ternary mod-3 grammar at window lengths 6,7,8).
  E2  capacity: fraction of positions whose preceding 5-context FORCES the
      next symbol (watermark-bearing, zero payload) vs FREE (payload), and the
      residual per-symbol entropy of the free positions.
  E3  burst tampering: detection vs number of edited symbols.
  E5  streaming attacks: per-seam detection of splice (cut-and-paste a valid
      foreign block), reorder (swap two adjacent blocks), replay (insert a
      foreign block) — the structural edits a real-time stream faces.
  E4  keyability: does scanning the phase word along a secret arithmetic
      progression n = r (mod m) change the forbidden-hexagram set? (key space
      of the "secret grammar".)

Usage:  python3 collatz_watermark_experiments.py [log2_N]   (default 20)
"""

import random
import sys


def sigma_full(limit):
    """Total stopping time sigma_C(n) for the full map (n/2 | 3n+1), n<limit,
    memoized: walk until the orbit drops below n (where sigma is already
    known).  sigma_C(1)=0."""
    sig = [0] * limit
    for n in range(2, limit):
        m, steps = n, 0
        while True:
            m = (3 * m + 1) if (m & 1) else (m >> 1)
            steps += 1
            if m < n:           # m < n <= limit, so sig[m] is set
                break
        sig[n] = steps + sig[m]
    return sig


def phase_word(limit):
    sig = sigma_full(limit)
    return [sig[n] % 3 for n in range(1, limit)]


def windows_of_length(word, L):
    """Set of length-L subwords as tuples."""
    seen = set()
    n = len(word)
    for i in range(n - L + 1):
        seen.add(tuple(word[i:i + L]))
    return seen


# ----------------------------------------------------------------------
def E1_E3_tamper(word, alphabet=(0, 1, 2), trials=50000, seed=1):
    print("=" * 70)
    print("E1/E3 — tamper-evidence of the forbidden-word grammar")
    print("=" * 70)
    rng = random.Random(seed)
    n = len(word)
    occ = {L: windows_of_length(word, L) for L in (6, 7, 8)}
    for L in (6, 7, 8):
        total = len(alphabet) ** L
        print(f"  length {L}: {total - len(occ[L])} forbidden of {total}")

    def detects(w, pos, L):
        """does any length-L window covering pos become forbidden?"""
        lo = max(0, pos - L + 1)
        hi = min(len(w) - L, pos)
        S = occ[L]
        for i in range(lo, hi + 1):
            if tuple(w[i:i + L]) not in S:
                return True
        return False

    print("\nSingle-substitution detection probability:")
    for L in (6, 7, 8):
        hit = 0
        for _ in range(trials):
            pos = rng.randrange(L - 1, n - L)
            old = word[pos]
            new = rng.choice([s for s in alphabet if s != old])
            # local copy only around pos
            seg_lo = max(0, pos - L + 1)
            seg = word[seg_lo:pos + L]
            seg[pos - seg_lo] = new
            S = occ[L]
            found = any(tuple(seg[i:i + L]) not in S
                        for i in range(len(seg) - L + 1))
            hit += found
        print(f"  window length {L}: P(detected) = {hit/trials:.4f}")

    print("\nBurst detection (window length 8), k random substitutions in a"
          " block of 32:")
    L = 8
    S = occ[L]
    for k in (1, 2, 3, 5, 8):
        hit = 0
        bt = trials // 10
        for _ in range(bt):
            start = rng.randrange(0, n - 64)
            seg = word[start:start + 64]
            for _e in range(k):
                p = rng.randrange(16, 48)
                seg[p] = rng.choice([s for s in alphabet if s != seg[p]])
            found = any(tuple(seg[i:i + L]) not in S
                        for i in range(len(seg) - L + 1))
            hit += found
        print(f"  k = {k}: P(detected) = {hit/bt:.4f}")


# ----------------------------------------------------------------------
def E5_streaming(word, alphabet=(0, 1, 2), trials=20000, seed=2):
    """Stream-native attacks: splice (cut-and-paste a VALID foreign block),
    reorder (swap two adjacent valid blocks), replay (insert a foreign block).
    The interior of a pasted valid block never trips; only the seams can — so
    this measures per-seam detectability of structural edits to a stream."""
    print()
    print("=" * 70)
    print("E5 — streaming attacks: splice / reorder / replay (per-seam)")
    print("=" * 70)
    rng = random.Random(seed)
    n = len(word)
    occ = {L: windows_of_length(word, L) for L in (6, 8)}

    def has_forb(seg, L, S):
        return any(tuple(seg[i:i + L]) not in S
                   for i in range(len(seg) - L + 1))

    print("\nSplice (paste a valid foreign block of length B):")
    print(f"  {'B':>4} {'L=6':>8} {'L=8':>8}")
    for B in (4, 8, 16, 32):
        row = []
        for L in (6, 8):
            S = occ[L]
            hit = 0
            for _ in range(trials):
                p = rng.randrange(64, n - 64 - B)
                q = rng.randrange(0, n - B)
                seg = word[p - (L - 1):p + B + (L - 1)][:]
                for k in range(B):
                    seg[(L - 1) + k] = word[q + k]
                hit += has_forb(seg, L, S)
            row.append(hit / trials)
        print(f"  {B:>4} {row[0]:>8.4f} {row[1]:>8.4f}")

    print("\nReorder (swap two adjacent valid blocks of length B):")
    print(f"  {'B':>4} {'L=6':>8} {'L=8':>8}")
    for B in (4, 8, 16):
        row = []
        for L in (6, 8):
            S = occ[L]
            hit = 0
            for _ in range(trials):
                p = rng.randrange(64, n - 64 - 2 * B)
                seg = word[p - (L - 1):p + 2 * B + (L - 1)][:]
                a = seg[L - 1:L - 1 + B][:]
                b = seg[L - 1 + B:L - 1 + 2 * B][:]
                seg[L - 1:L - 1 + B] = b
                seg[L - 1 + B:L - 1 + 2 * B] = a
                hit += has_forb(seg, L, S)
            row.append(hit / trials)
        print(f"  {B:>4} {row[0]:>8.4f} {row[1]:>8.4f}")

    print("\nReplay / insertion of a foreign block of length M (L=8):")
    L = 8
    S = occ[L]
    for M in (6, 12, 24, 48):
        hit = 0
        for _ in range(trials):
            p = rng.randrange(64, n - 64 - M)
            q = rng.randrange(0, n - M)
            seg = word[p - (L - 1):p + M + (L - 1)][:]
            for k in range(M):
                seg[(L - 1) + k] = word[q + k]
            hit += has_forb(seg, L, S)
        print(f"  insert len {M:>3}: P(detected) = {hit/trials:.4f}")


# ----------------------------------------------------------------------
def E2_capacity(word, ctx=5, alphabet=(0, 1, 2)):
    print()
    print("=" * 70)
    print(f"E2 — capacity: forced vs free positions (context length {ctx})")
    print("=" * 70)
    n = len(word)
    # children seen for each context
    from collections import defaultdict
    children = defaultdict(set)
    counts = defaultdict(lambda: defaultdict(int))
    for i in range(n - ctx):
        c = tuple(word[i:i + ctx])
        nxt = word[i + ctx]
        children[c].add(nxt)
        counts[c][nxt] += 1
    forcing = {c for c, ch in children.items() if len(ch) == 1}
    twochild = {c for c, ch in children.items() if len(ch) == 2}
    print(f"  distinct {ctx}-contexts occurring: {len(children)}")
    print(f"  forcing (1 child):  {len(forcing)}")
    print(f"  2-child:            {len(twochild)}")
    print(f"  full (3 children):  {len(children) - len(forcing) - len(twochild)}")

    # position-weighted: fraction of symbols that are forced / 2-way / free
    import math
    tot = 0
    forced_pos = 0
    ent = 0.0
    for i in range(n - ctx):
        c = tuple(word[i:i + ctx])
        tot += 1
        ch = children[c]
        if len(ch) == 1:
            forced_pos += 1
        # empirical conditional entropy of next symbol
        cc = counts[c]
        s = sum(cc.values())
        h = -sum((v / s) * math.log2(v / s) for v in cc.values())
        ent += h
    print(f"\n  position-weighted forced fraction: {forced_pos/tot:.4f}")
    print(f"  mean conditional entropy H(next | {ctx}-context): "
          f"{ent/tot:.4f} bits  (max {math.log2(3):.4f})")
    print(f"  => payload capacity ~ {ent/tot:.3f} bits per symbol, watermark "
          f"carried by the {forced_pos/tot:.1%} forced positions")


# ----------------------------------------------------------------------
def E4_keyability(word, m_values=(2, 3, 4, 5), L=6, alphabet=(0, 1, 2)):
    print()
    print("=" * 70)
    print("E4 — keyability: forbidden hexagram set along secret scans"
          " n = r (mod m)")
    print("=" * 70)
    n = len(word)
    base = windows_of_length(word, L)
    full = set()
    sets = {}
    for m in m_values:
        for r in range(m):
            sub = word[r::m]
            occ = windows_of_length(sub, L)
            forb = frozenset(t for t in _all_words(L, alphabet)
                             if t not in occ)
            sets[(m, r)] = forb
    distinct = set(sets.values())
    print(f"  scans tested: {len(sets)}")
    print(f"  distinct forbidden-hexagram sets: {len(distinct)}")
    sizes = sorted(len(s) for s in sets.values())
    print(f"  forbidden-set sizes: min {sizes[0]}, median "
          f"{sizes[len(sizes)//2]}, max {sizes[-1]}")
    # how different are two scans? mean symmetric-difference between distinct sets
    dl = list(distinct)
    if len(dl) > 1:
        import itertools
        diffs = [len(a ^ b) for a, b in itertools.combinations(dl, 2)]
        print(f"  mean |A symdiff B| over distinct sets: "
              f"{sum(diffs)/len(diffs):.1f}")
    # identity scan (m=1) baseline
    print(f"  baseline (full word, no scan): {len(base) and (len(alphabet)**L - len(base))} forbidden")


def _all_words(L, alphabet):
    if L == 0:
        yield ()
        return
    for w in _all_words(L - 1, alphabet):
        for a in alphabet:
            yield w + (a,)


if __name__ == '__main__':
    log2N = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    limit = 1 << log2N
    print(f"building phase word for n < 2^{log2N} = {limit} ...")
    word = phase_word(limit)
    print(f"phase word length: {len(word)}\n")
    E1_E3_tamper(word)
    E5_streaming(word)
    E2_capacity(word)
    E4_keyability(word)