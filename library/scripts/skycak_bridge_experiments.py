#!/usr/bin/env python3
"""Numerical experiments bridging Skycak's continuous 3n+1 extension and
the phase program of `the-phases-of-collatz.md`.

Experiment A — basin census of Skycak's f(x) = (4x+1)/4 - (2x+1)/4 cos(pi x):
capture fraction on random seeds, which attracting 2-cycle captures them
((1,2) integer cycle vs the ghost cycle ~(1.193, 2.139)), the phase
(parity of arrival time) of the captured seeds, and the gauge test
f + c*sin(pi x) to see whether the ghost cycle and the capture fraction
survive a repainting of the canvas.

Experiment B — the phase language of Skycak's accelerated map
T(n) = (3n+1)/2 / n/2 (terminal cycle (1,2), period two): the binary phase
word phi2(n) = sigma_T(n) mod 2, its subword complexity p(L) vs 2^L, the
first forbidden length, persistence of the missing words under sample
growth, and rotation/reversal closure.

Experiment C — the dial between two means: escape census of the generalized
extension F_{a,1} across the window 3 <= a <= 4, where the arithmetic-mean
(area) criterion of Skycak's paper predicts the crossover at a = 3 and the
geometric-mean (multiplicative drift) criterion predicts it at a = 4. The
integer maps T_{a,1} (a odd) cannot sample the window; the continuous family
can.

Usage:  python3 skycak_bridge_experiments.py [log2_N]   (default 22)
"""

import math
import random
import sys


# ----------------------------------------------------------------------
# Experiment A: Skycak's continuous extension
# ----------------------------------------------------------------------

def skycak_f(x, c=0.0):
    return (4 * x + 1) / 4 - (2 * x + 1) / 4 * math.cos(math.pi * x) \
        + c * math.sin(math.pi * x)


def classify_orbit(x, c=0.0, iters=2000, bail=1e12):
    """Return (label, arrival_parity). Labels: 'int' for the (1,2) cycle,
    'ghost' for the ~(1.193,2.139) cycle, 'escape', 'other'."""
    for t in range(iters):
        if x > bail or x < 0 or math.isinf(x) or math.isnan(x):
            return 'escape', None
        # near the integer cycle (1,2)?
        if abs(x - 1.0) < 1e-9:
            return 'int', t % 2
        if abs(x - 2.0) < 1e-9:
            return 'int', (t + 1) % 2
        x = skycak_f(x, c)
    # not bailed: identify the residual 2-cycle, if any
    a, b = x, skycak_f(x, c)
    if abs(skycak_f(b, c) - a) < 1e-6:
        lo, hi = min(a, b), max(a, b)
        if abs(lo - 1.0) < 1e-3 and abs(hi - 2.0) < 1e-3:
            return 'int', None
        if abs(lo - 1.19) < 0.05 and abs(hi - 2.14) < 0.05:
            return 'ghost', None
        return 'other', None
    return 'other', None


def find_ghost_cycle(c=0.0):
    """Locate the non-integer attracting 2-cycle by iterating from 1.2."""
    x = 1.2
    for _ in range(5000):
        x = skycak_f(x, c)
    a, b = x, skycak_f(x, c)
    return (min(a, b), max(a, b))


def experiment_A(n_seeds=20000, seed=1):
    print("=" * 70)
    print("EXPERIMENT A — basin census of Skycak's f on [1, 100]")
    print("=" * 70)
    rng = random.Random(seed)
    for c in (0.0, 0.3, 1.0):
        counts = {'int': 0, 'ghost': 0, 'escape': 0, 'other': 0}
        parity = {0: 0, 1: 0}
        for _ in range(n_seeds):
            x = rng.uniform(1, 100)
            label, par = classify_orbit(x, c)
            counts[label] += 1
            if par is not None:
                parity[par] += 1
        ghost = find_ghost_cycle(c)
        ga, gb = ghost
        # multiplier of the ghost cycle, by finite differences
        h = 1e-7
        mult = ((skycak_f(ga + h, c) - skycak_f(ga - h, c)) / (2 * h)) * \
               ((skycak_f(gb + h, c) - skycak_f(gb - h, c)) / (2 * h))
        print(f"\ncanvas c = {c}")
        print(f"  captured by (1,2):      {counts['int']:6d}  "
              f"({100*counts['int']/n_seeds:.1f}%)")
        print(f"  captured by ghost:      {counts['ghost']:6d}  "
              f"({100*counts['ghost']/n_seeds:.1f}%)")
        print(f"  escape to infinity:     {counts['escape']:6d}  "
              f"({100*counts['escape']/n_seeds:.1f}%)")
        print(f"  other/undecided:        {counts['other']:6d}")
        print(f"  arrival parity split (even/odd ticks): "
              f"{parity[0]} / {parity[1]}")
        print(f"  residual 2-cycle from seed 1.2: "
              f"({ga:.6f}, {gb:.6f}), multiplier {mult:+.4f}")


# ----------------------------------------------------------------------
# Experiment B: phase language of the accelerated map, mod 2
# ----------------------------------------------------------------------

def sigma_shortcut(limit):
    """sigma_T(n) for the accelerated map T(n) = (3n+1)/2 | n/2, n < limit.
    sigma(1) = 0; T(1) = 2, T(2) = 1."""
    sig = [0] * limit
    sig[1] = 0
    for n in range(2, limit):
        m, steps = n, 0
        while m >= n:
            m = (3 * m + 1) // 2 if m & 1 else m >> 1
            steps += 1
        sig[n] = steps + sig[m]
    return sig


def experiment_B(log2N=22, maxL=20):
    limit = 1 << log2N
    print()
    print("=" * 70)
    print(f"EXPERIMENT B — phase word of the accelerated map, "
          f"phi2(n) = sigma_T(n) mod 2, n < 2^{log2N}")
    print("=" * 70)
    sig = sigma_shortcut(limit)
    word = bytes(s & 1 for s in sig[1:])

    def complexity(w, L):
        seen = set()
        v = int.from_bytes(b'\x00', 'big')  # placeholder
        mask = (1 << L) - 1
        v = 0
        for i, ch in enumerate(w):
            v = ((v << 1) | ch) & mask
            if i >= L - 1:
                seen.add(v)
        return seen

    print(f"\n{'L':>3} {'p(L)':>10} {'2^L':>10}   missing")
    first_forbidden = None
    missing_sets = {}
    for L in range(2, maxL + 1):
        seen = complexity(word, L)
        total = 1 << L
        miss = total - len(seen)
        print(f"{L:>3} {len(seen):>10} {total:>10}   {miss}")
        if miss and first_forbidden is None:
            first_forbidden = L
            missing_sets[L] = set(range(total)) - seen
    if first_forbidden is None:
        print(f"\nNo forbidden words up to length {maxL}: the binary phase "
              f"language is full at every tested length.")
        return

    L = first_forbidden
    missing = missing_sets[L]
    print(f"\nFirst forbidden length: {L}  ({len(missing)} missing words)")

    # persistence: same set on the quarter range?
    quarter = word[: len(word) // 4]
    seen_q = complexity(quarter, L)
    missing_q = set(range(1 << L)) - seen_q
    print(f"missing at quarter range: {len(missing_q)}; "
          f"stable subset: {len(missing & missing_q)} of {len(missing)}")

    def decode(v):
        return format(v, f'0{L}b')

    # closure tests: complement (binary analogue of letter rotation), reversal
    full = (1 << L) - 1
    comp_closed = all((m ^ full) in missing for m in missing)
    rev_closed = all(int(decode(m)[::-1], 2) in missing for m in missing)
    print(f"closed under complement (letter rotation mod 2): {comp_closed}")
    print(f"closed under reversal: {rev_closed}")
    sample = sorted(missing)[:24]
    print("missing words (first 24):")
    print('  ' + ' '.join(decode(m) for m in sample))


# ----------------------------------------------------------------------
# Experiment C: the dial between two means
# ----------------------------------------------------------------------

def F_ab(a, b, x):
    return ((a + 1) * x + b) / 4 - ((a - 1) * x + b) / 4 * math.cos(math.pi * x)


def experiment_C(n_seeds=400, iters=400, seed=7):
    print()
    print("=" * 70)
    print("EXPERIMENT C — escape census of F_{a,1} across the window (3, 4)")
    print("=" * 70)
    rng = random.Random(seed)
    print(f"\n{'a':>5} {'settled(<10)':>13} {'escaped(>1e8)':>14} "
          f"{'median final':>14}")
    for a10 in range(28, 45, 2):
        a = a10 / 10
        finals, esc, settled = [], 0, 0
        for _ in range(n_seeds):
            x = rng.uniform(1, 500)
            for _t in range(iters):
                x = F_ab(a, 1.0, x)
                if x > 1e8:
                    break
            if x > 1e8:
                esc += 1
            elif x < 10:
                settled += 1
            finals.append(min(x, 1e8))
        finals.sort()
        print(f"{a:>5.1f} {settled:>13d} {esc:>14d} "
              f"{finals[n_seeds // 2]:>14.4g}")


if __name__ == '__main__':
    log2N = int(sys.argv[1]) if len(sys.argv) > 1 else 22
    experiment_A()
    experiment_B(log2N)
    experiment_C()