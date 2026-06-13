#!/usr/bin/env python3
"""Forcing contexts and frontier analysis of the Collatz phase language.

Extends collatz_forbidden_words.py with the 2026-06-12 findings:

  * the paired-hole law: every length-5 context touched by the 72
    forbidden hexagrams loses exactly 2 of its 3 children, giving 36
    forward (and 36 backward) forcing rules — deterministic windows;
  * the frontier at lengths 7 and 8: missing words split into inherited
    (containing a shorter forbidden word) and genuinely new; the new ones
    are persistence-tested against the quarter-range sample and grouped
    by their forcing contexts;
  * the reversal break: reversal closure is exact at length 6 but fails
    at length 7 (24 of the 48 genuinely-new missing words have reversals
    that occur);
  * the complexity ratios p(L)/p(L-1), strictly below 3.

Usage:
    python3 library/scripts/collatz_phase_frontier.py [log2_N]

Default: log2_N=22 (about 4.2M integers).
"""

from __future__ import annotations

import os
import sys
from collections import Counter, defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from collatz_forbidden_words import block_codes, decode, encode, missing_words, stopping_times


def missing_decoded(seq: np.ndarray, length: int) -> set[tuple[int, ...]]:
    return {decode(c, length) for c in missing_words(seq, length)}


def forcing_rules(missing: set[tuple[int, ...]], length: int) -> dict:
    prefixes = defaultdict(set)
    for w in missing:
        prefixes[w[:-1]].add(w[-1])
    return {p: holes for p, holes in prefixes.items()}


def main() -> None:
    log2_n = int(sys.argv[1]) if len(sys.argv) > 1 else 22
    limit = 1 << log2_n
    phases = (stopping_times(limit) % 3)[1:]
    quarter = phases[: limit // 4]

    print(f"phase word on n = 1..{limit - 1}\n")

    # --- paired holes and forcing rules at length 6 -----------------------
    m6 = missing_decoded(phases, 6)
    rules = forcing_rules(m6, 6)
    counts = Counter(len(h) for h in rules.values())
    print(f"length-6 missing: {len(m6)}")
    print(f"forcing 5-contexts: {len(rules)}, hole counts: {dict(counts)}")
    print("forward forcing rules (context -> forced letter):")
    line = []
    for p in sorted(rules):
        if len(rules[p]) == 2:
            forced = ({0, 1, 2} - rules[p]).pop()
            line.append("".join(map(str, p)) + "->" + str(forced))
    for i in range(0, len(line), 6):
        print("  " + "  ".join(line[i : i + 6]))

    # --- frontier at lengths 7 and 8 --------------------------------------
    prev = m6
    for length in (7, 8):
        mL = missing_decoded(phases, length)
        new = sorted(w for w in mL if w[:-1] not in prev and w[1:] not in prev)
        qL = missing_decoded(quarter, length)
        persistent = sum(1 for w in new if w in qL)
        ctx = forcing_rules(set(new), length)
        ctx_counts = Counter(len(h) for h in ctx.values())
        occ = set(np.unique(block_codes(phases, length)).tolist())
        rev_occurs = sum(1 for w in new if encode(w[::-1]) in occ)
        print(f"\nlength-{length} missing: {len(mL)}, genuinely new: {len(new)}")
        print(f"  persistent from quarter range: {persistent}/{len(new)}")
        print(f"  forcing {length - 1}-contexts: {len(ctx)}, hole counts: {dict(ctx_counts)}")
        print(f"  genuinely-new whose reversal occurs: {rev_occurs}/{len(new)}")
        singles = sorted(
            "".join(map(str, p)) for p, h in ctx.items() if len(h) == 1
        )
        if singles:
            print(f"  single-hole contexts: {' '.join(singles)}")
        prev = mL

    # --- complexity ratios -------------------------------------------------
    print(f"\n{'L':>3} {'p(L)':>8} {'3^L':>8} {'ratio':>8}")
    prev_p = None
    for length in range(5, 9):
        p = 3**length - len(missing_decoded(phases, length))
        ratio = f"{p / prev_p:.4f}" if prev_p else ""
        print(f"{length:>3} {p:>8} {3**length:>8} {ratio:>8}")
        prev_p = p


if __name__ == "__main__":
    main()
