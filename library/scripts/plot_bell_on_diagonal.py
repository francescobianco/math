#!/usr/bin/env python3
"""Plot the bell on the diagonal and its oscillating destiny.

The map is a Gaussian bell laid on the diagonal,

    f(x) = x - delta + A * exp(-(x - c)^2 / (2 sigma^2)),

with A > delta > 0 and c > 0. Both tails of the graph run a distance delta
below the diagonal y = x; only the dome pierces it, on the interval
(x-, x+) where

    x± = c ± sigma * sqrt(2 log(A / delta)).

With the parameters used in the book (A=3, delta=1, c=1, sigma=3/5) both
fixed points repel — x- by amplification (f' ≈ +3.47), x+ by reflection
(f' ≈ -1.47) — and the orbit settles onto an attracting 2-cycle astride
the right rim of the dome.

Left panel: the map, the diagonal, the dome, and a cobweb sliding in from
the right tail onto the oscillation. Right panel: the even-iterate limit
E(x) = lim f^{2n}(x), a step function alternating between the two cycle
points on stripes accumulating at the wall x-.
"""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

A, DELTA, C, SIGMA = 3.0, 1.0, 1.0, 0.6


def f(x):
    return x - DELTA + A * np.exp(-((x - C) ** 2) / (2 * SIGMA**2))


def main() -> None:
    d = SIGMA * math.sqrt(2 * math.log(A / DELTA))
    x_minus, x_plus = C - d, C + d

    # Attracting 2-cycle by Newton on f(f(x)) - x.
    def fp(x):
        return 1 - A * (x - C) / SIGMA**2 * math.exp(-((x - C) ** 2) / (2 * SIGMA**2))

    a = 1.6
    for _ in range(80):
        a -= (f(f(a)) - a) / (fp(f(a)) * fp(a) - 1)
    b = float(f(a))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.2))

    # --- Left panel: the map and a cobweb ---------------------------------
    xs = np.linspace(-1.5, 4.5, 1000)
    ax1.plot(xs, xs, color="gray", lw=1, label="$y = x$")
    ax1.plot(xs, f(xs), color="#b8336a", lw=2, label="$f(x)$")
    dome = np.linspace(x_minus, x_plus, 300)
    ax1.fill_between(dome, dome, f(dome), color="#b8336a", alpha=0.15)

    x = 4.2
    for _ in range(40):
        y = float(f(x))
        ax1.plot([x, x], [x, y], color="#2a6f97", lw=0.8)
        ax1.plot([x, y], [y, y], color="#2a6f97", lw=0.8)
        x = y

    for pt, name in ((x_minus, "$x_-$"), (x_plus, "$x_+$")):
        ax1.plot(pt, pt, "o", color="black", ms=5)
        ax1.annotate(name, (pt, pt), textcoords="offset points", xytext=(6, -12))
    ax1.plot([a, b], [b, a], "o", color="#2a6f97", ms=6)
    ax1.set_title("The bell on the diagonal, cobweb from the right tail")
    ax1.set_xlabel("$x$")
    ax1.set_ylabel("$y$")
    ax1.legend(loc="upper left")

    # --- Right panel: the even-iterate limit ------------------------------
    grid = np.linspace(x_minus + 1e-4, 4.5, 4000)
    limits = []
    for x0 in grid:
        x = float(x0)
        for _ in range(2000):
            x = float(f(x))
        limits.append(a if abs(x - a) < abs(x - b) else b)
    ax2.plot(grid, limits, ".", color="#2a6f97", ms=1.5)
    ax2.axhline(a, color="gray", lw=0.6, ls=":")
    ax2.axhline(b, color="gray", lw=0.6, ls=":")
    ax2.axvline(x_minus, color="black", lw=1, ls="--")
    ax2.set_yticks([a, b])
    ax2.set_yticklabels(["$a$", "$b$"])
    ax2.set_title("Even-iterate limit $E(x) = \\lim f^{2n}(x)$: phase stripes")
    ax2.set_xlabel("$x$")
    ax2.annotate("wall $x_-$", (x_minus, (a + b) / 2), textcoords="offset points",
                 xytext=(8, 0))

    fig.tight_layout()
    out = Path(__file__).resolve().parent.parent / "images" / "bell-on-diagonal.png"
    fig.savefig(out, dpi=160)
    print(f"wrote {out}")
    print(f"x- = {x_minus:.6f}, x+ = {x_plus:.6f}")
    print(f"2-cycle: a = {a:.6f}, b = {b:.6f}, multiplier = {fp(a) * fp(b):.6f}")


if __name__ == "__main__":
    main()