#!/usr/bin/env python3
"""Plot the bell on the anti-diagonal and its two destinies.

The map is a Gaussian bell laid on the anti-diagonal,

    f(x) = -x - delta + A * exp(-(x - c)^2 / (2 sigma^2)),

with A > delta > 0. Without the bump the map x -> -x - delta is an
involution: every point swings forever on a neutral 2-cycle, a pendulum.
The dome poking above y = -x supplies the only friction, damping the
pendulum doubly-exponentially slowly, and the destiny is decided by where
the bell meets the *main* diagonal y = x.

Left panel (c = 1.2): the diagonal cuts only the left tail — a unique
attracting fixed point (f' ≈ -0.71); the cobweb swings inward and spirals
onto it. Right panel (c = 0.8): the diagonal cuts the dome's right flank
(f' ≈ -2.23) — the reflection is too violent and the orbit bounces
chaotically on the dome forever (Lyapunov ≈ 0.51).
"""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

A, DELTA, SIGMA = 3.0, 1.0, 0.6


def make(c):
    def f(x):
        return -x - DELTA + A * np.exp(-((x - c) ** 2) / (2 * SIGMA**2))

    return f


def panel(ax, c, x0, n_steps, title):
    f = make(c)
    d = SIGMA * math.sqrt(2 * math.log(A / DELTA))
    xs = np.linspace(-3.9, 3.9, 1200)
    ax.plot(xs, xs, color="gray", lw=1, label="$y = x$")
    ax.plot(xs, -xs, color="gray", lw=1, ls="--", label="$y = -x$")
    ax.plot(xs, f(xs), color="#b8336a", lw=2, label="$f(x)$")
    dome = np.linspace(c - d, c + d, 300)
    ax.fill_between(dome, -dome, f(dome), color="#b8336a", alpha=0.15)

    x = x0
    for _ in range(n_steps):
        y = float(f(x))
        ax.plot([x, x], [x, y], color="#2a6f97", lw=0.7, alpha=0.8)
        ax.plot([x, y], [y, y], color="#2a6f97", lw=0.7, alpha=0.8)
        x = y

    ax.set_xlim(-3.9, 3.9)
    ax.set_ylim(-3.9, 3.9)
    ax.set_aspect("equal")
    ax.set_title(title)
    ax.set_xlabel("$x$")
    ax.legend(loc="lower left", fontsize=8)


def main() -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    panel(ax1, 1.2, 2.6, 80,
          "$c = 1.2$: pendulum spirals onto the tail point $x_*$")
    panel(ax2, 0.8, 2.2, 250,
          "$c = 0.8$: chaotic bounce on the dome")

    # mark the attracting fixed point on the left panel
    f = make(1.2)
    x = -0.45
    for _ in range(200):
        x = 0.5 * (x + float(f(x)))  # damped iteration converges to x*
    ax1.plot(x, x, "o", color="black", ms=6)
    ax1.annotate("$x_*$", (x, x), textcoords="offset points", xytext=(8, -14))

    fig.tight_layout()
    out = Path(__file__).resolve().parent.parent / "images" / "bell-on-antidiagonal.png"
    fig.savefig(out, dpi=160, bbox_inches="tight")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()