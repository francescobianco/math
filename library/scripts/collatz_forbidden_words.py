#!/usr/bin/env python3
"""Analyze the forbidden words of the Collatz phase language.

The phase word is the infinite sequence phi(1) phi(2) phi(3) ... with
phi(n) = sigma(n) mod 3 (sigma = total stopping time). Empirically, exactly
72 of the 729 possible length-6 blocks never occur — the same 72 at
n < 2^22 and at n < 2^24. This script reproduces and extends that analysis:

  * subword complexity p(L) versus 3^L for L = 1..max_len;
  * the missing length-L words, decoded;
  * structure tests on the missing set: zigzag membership (no equal
    adjacent letters), closure under letter rotation w -> w+1 mod 3,
    closure under reversal;
  * persistence: missing sets compared at half range and full range.

Usage:
    python3 library/scripts/collatz_forbidden_words.py [log2_N] [word_len]

Defaults: log2_N=22 (about 4.2M integers), word_len=6.
"""

from __future__ import annotations

import sys

import numpy as np


def stopping_times(limit: int) -> np.ndarray:
    sigma = np.zeros(limit, dtype=np.int64)
    for n in range(2, limit):
        m, steps = n, 0
        while m >= n:
            m = m >> 1 if m % 2 == 0 else 3 * m + 1
            steps += 1
        sigma[n] = steps + sigma[m]
    return sigma


def block_codes(seq: np.ndarray, length: int) -> np.ndarray:
    codes = np.zeros(len(seq) - length + 1, dtype=np.int64)
    for i in range(length):
        codes = codes * 3 + seq[i : len(seq) - length + 1 + i]
    return codes


def missing_words(seq: np.ndarray, length: int) -> set[int]:
    return set(range(3**length)) - set(np.unique(block_codes(seq, length)).tolist())


def decode(code: int, length: int) -> tuple[int, ...]:
    return tuple((code // 3 ** (length - 1 - i)) % 3 for i in range(length))


def encode(word: tuple[int, ...]) -> int:
    code = 0
    for letter in word:
        code = code * 3 + letter
    return code


def is_zigzag(word: tuple[int, ...]) -> bool:
    return all(word[i] != word[i + 1] for i in range(len(word) - 1))


def main() -> None:
    log2_n = int(sys.argv[1]) if len(sys.argv) > 1 else 22
    word_len = int(sys.argv[2]) if len(sys.argv) > 2 else 6

    limit = 1 << log2_n
    phases = (stopping_times(limit) % 3)[1:]

    print(f"phase word on n = 1..{limit - 1}, word length {word_len}\n")

    print(f"{'L':>3} {'p(L)':>10} {'3^L':>10}")
    for length in range(1, word_len + 1):
        p = len(np.unique(block_codes(phases, length)))
        print(f"{length:>3} {p:>10} {3**length:>10}")

    half = missing_words(phases[: limit // 4], word_len)
    full = missing_words(phases, word_len)
    print(f"\nmissing at quarter range : {len(half)}")
    print(f"missing at full range    : {len(full)}")
    print(f"persistent               : {len(half & full)} (appeared: {len(half - full)})")

    words = sorted(decode(c, word_len) for c in full)
    zig = [w for w in words if is_zigzag(w)]
    rotated = {encode(tuple((x + 1) % 3 for x in w)) for w in words}
    reversed_ = {encode(w[::-1]) for w in words}
    print(f"\nzigzag among missing     : {len(zig)} / {len(words)}")
    print(f"closed under rotation +1 : {rotated == full}")
    print(f"closed under reversal    : {reversed_ == full}")

    print("\nmissing words:")
    for w in words:
        print("  " + "".join(map(str, w)))


if __name__ == "__main__":
    main()