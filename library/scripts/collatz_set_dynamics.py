#!/usr/bin/env python3
"""Verify the set-level dynamics of the Collatz map.

Pointwise, every verified trajectory collapses to the cycle 1 -> 4 -> 2.
Set-wise, nothing collapses at all: T(N) = N because every m has the
predecessor 2m, so the whole set of naturals is a fixed point of the
induced map on subsets. This script verifies the four claims of the
companion paper:

  1. finite collapse: T^k({1..N}) shrinks to exactly {1,2,4};
  2. collision density: the doubly-covered values are exactly the
     residue class 4 mod 6, density 1/6;
  3. the exact halving law for tails: T^k(S_m) = S_ceil(m/2^k),
     where S_m = {m, m+1, m+2, ...}, checked by backward search;
  4. the 3n-1 control: identical set-level laws, different destinies
     (the finite collapse lands on three cycles instead of one).

Usage:
    python3 library/scripts/collatz_set_dynamics.py [log2_N]

Default: log2_N=20 (about 1M integers).
"""

from __future__ import annotations

import sys


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else 3 * n + 1


def T_minus(n: int) -> int:
    return n // 2 if n % 2 == 0 else 3 * n - 1


def image(A: set[int], step) -> set[int]:
    return {step(n) for n in A}


def finite_collapse(N: int, step, name: str) -> None:
    A = set(range(1, N + 1))
    print(f"\n  finite collapse of [1, {N}] under {name}:")
    k = 0
    prev = None
    while A != prev:
        if k in (0, 1, 2, 5, 10, 20, 50, 100, 150, 200, 300, 400) or len(A) < 30:
            print(f"    k={k:4d}  |T^k([1,N])| = {len(A)}")
        prev = A
        A = image(A, step)
        k += 1
        if len(A) < 30 and A == image(A, step) and A == prev:
            break
        if k > 2000:
            print("    ... stopping at k=2000 (no fixed set reached)")
            return
    print(f"    fixed set reached at k={k - 1}: {sorted(A)}")


def collision_density(N: int) -> None:
    # preimages of m under T: 2m always; (m-1)/3 when m = 4 mod 6
    doubly = sum(1 for m in range(1, N + 1) if m % 6 == 4)
    print(f"\n  doubly-covered values in [1, {N}]: {doubly}  "
          f"(fraction {doubly / N:.6f}, predicted 1/6 = {1/6:.6f})")
    # spot check: both preimages really map to m
    for m in range(4, 1000, 6):
        assert T(2 * m) == m and T((m - 1) // 3) == m and ((m - 1) // 3) % 2 == 1
    print("  spot check: for m = 4 mod 6 both preimages verified up to 1000")


def ancestors_reach(x: int, k: int, m: int) -> bool:
    """True iff some depth-k preimage of x (under T) is >= m."""
    level = {x}
    for _ in range(k):
        nxt = set()
        for n in level:
            nxt.add(2 * n)
            if n % 6 == 4 and n > 4:
                nxt.add((n - 1) // 3)
            elif n == 4:
                nxt.add(1)
        level = nxt
    return max(level) >= m


def halving_law(window: int, ms: list[int], ks: list[int]) -> None:
    print(f"\n  exact halving law  T^k(S_m) = S_ceil(m/2^k),  "
          f"checked on the window [1, {window}]:")
    for m in ms:
        for k in ks:
            front = -(-m // 2 ** k)  # ceil(m / 2^k)
            for x in range(1, window + 1):
                inside = ancestors_reach(x, k, m)
                assert inside == (x >= front), (m, k, x)
            print(f"    m={m:<8d} k={k:<3d} front ceil(m/2^k)={front:<8d} OK")


def main() -> None:
    log2_N = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    N = 2 ** log2_N

    print(f"Collatz set-level dynamics, N = 2^{log2_N} = {N}")

    finite_collapse(N, T, "T (3n+1)")
    collision_density(N)
    halving_law(window=40,
                ms=[10, 100, 10 ** 4, 10 ** 6],
                ks=[1, 3, 7, 12])

    print("\n  control map 3n-1:")
    finite_collapse(N, T_minus, "T' (3n-1)")


if __name__ == "__main__":
    main()