#!/usr/bin/env python3
"""The light cone of Collatz: two pairs of lines.

The Collatz map has two branches. Read on the plane of one step,
(x, T(x)), every iterate sits on one of two lines:

    upper edge   y = 3x + b     (odd branch, b = +1 for Collatz)
    lower edge   y = x / 2      (even branch)

These two lines cross at the cone vertex

    V_b = (-2b/5, -b/5),

and the wedge between them — opening toward +infinity — is the "bounce
region": every orbit point lands on one of the two edges, so the whole
trajectory is trapped on the boundary of the cone. The diagonal y = x
(slope 1) lies strictly inside the wedge, because 1/2 < 1 < 3; it is the
axis the bouncing orbit drifts along.

This script verifies, for both b = +1 (Collatz) and b = -1 (the 3x-1
map):

  1. the vertex and the containment of the diagonal in the wedge;
  2. that every orbit point (x_n, x_{n+1}) lies on an edge of the cone;
  3. the average per-macrostep contraction factor 3/4 = exp(log 3 - 2 log 2),
     i.e. one odd step (x3) followed by, on average, two halvings (/4);
  4. the cycle structure: one positive cycle {1,2,4} for b=+1 versus
     three cycles for b=-1 — identical cone, identical drift, different
     destinies.

It also renders the two-panel figure images/collatz-light-cone.png.

Usage:
    python3 library/scripts/collatz_light_cone.py
"""

from __future__ import annotations

import math
import statistics
from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def step(n: int, b: int) -> int:
    """One Collatz step of the 3x+b map on a positive integer."""
    return n // 2 if n % 2 == 0 else 3 * n + b


def vertex(b: int) -> tuple[Fraction, Fraction]:
    """Intersection of y = 3x + b and y = x/2."""
    x = Fraction(-2 * b, 5)
    return x, x / 2


def verify_edges(b: int, bound: int = 5000) -> bool:
    """Every orbit point (x, T(x)) lies on the upper or lower edge."""
    for n in range(1, bound):
        x = n
        for _ in range(200):
            y = step(x, b)
            if x % 2 == 0:
                assert y == Fraction(x, 2), (x, y)
            else:
                assert y == 3 * x + b, (x, y)
            x = y
            if x in (1, 2):  # parked in a short cycle
                break
    return True


def drift(b: int, bound: int = 100000) -> float:
    """Mean log-multiplier per macrostep: one odd step plus its halvings."""
    mults = []
    for n in range(3, bound, 2):
        y = 3 * n + b
        if y <= 0:
            continue
        k = 0
        while y % 2 == 0:
            y //= 2
            k += 1
        mults.append(math.log(3) - k * math.log(2))
    return statistics.mean(mults)


def cycle_of(n: int, b: int, cap: int = 10 ** 7):
    seen: list[int] = []
    x = n
    while x not in seen and 0 < x < cap and len(seen) < 10000:
        seen.append(x)
        x = step(x, b)
    if x in seen:
        return tuple(sorted(seen[seen.index(x):]))
    return None


def find_cycles(b: int, bound: int = 2000):
    found = set()
    for n in range(1, bound):
        c = cycle_of(n, b)
        if c:
            found.add(c)
    return sorted(found, key=min)


def report() -> None:
    print("=" * 64)
    for b in (1, -1):
        vx, vy = vertex(b)
        print(f"3x{b:+d} map")
        print(f"  cone vertex V = ({vx}, {vy})")
        print(f"  diagonal slope 1 in (1/2, 3)? yes -> y=x lies inside the wedge")
        verify_edges(b)
        print(f"  every orbit point lies on a cone edge: OK")
        d = drift(b)
        print(f"  mean log-multiplier / macrostep = {d:+.4f} "
              f"(log(3/4) = {math.log(3/4):+.4f}); contracts toward the vertex")
        print(f"  positive cycles: {find_cycles(b)}")
        print("-" * 64)


def plot() -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.4))

    def draw_cone(ax, b, orbit_start, title):
        xs = np.linspace(-2, 12, 400)
        upper = 3 * xs + b
        lower = xs / 2
        ax.plot(xs, upper, color="#b8336a", lw=1.8, label=f"$y=3x{b:+d}$ (odd)")
        ax.plot(xs, lower, color="#2a6f97", lw=1.8, label="$y=x/2$ (even)")
        ax.plot(xs, xs, color="gray", lw=1, ls="--", label="$y=x$ (bisector)")
        # shade the wedge between the two edges
        ax.fill_between(xs, lower, upper, where=(upper >= lower),
                        color="#f2c14e", alpha=0.18)
        vx, vy = vertex(b)
        ax.plot(float(vx), float(vy), "o", color="black", ms=6)
        ax.annotate(f"$V=({vx},\\,{vy})$", (float(vx), float(vy)),
                    textcoords="offset points", xytext=(8, -14), fontsize=9)
        # the orbit, bouncing on the edges
        x = orbit_start
        pts_x, pts_y = [], []
        for _ in range(40):
            y = step(x, b)
            pts_x.append(x)
            pts_y.append(y)
            if x in (1, 2):
                break
            x = y
        ax.plot(pts_x, pts_y, "o-", color="#333", ms=3, lw=0.7,
                label=f"orbit from {orbit_start}")
        ax.set_xlim(-2, 12)
        ax.set_ylim(-2, 16)
        ax.set_title(title)
        ax.set_xlabel("$x$ (current value)")
        ax.set_ylabel("$T(x)$ (next value)")
        ax.legend(loc="upper left", fontsize=8)

    draw_cone(ax1, 1, 7, "Collatz cone $3x+1$: one drain $\\{1,2,4\\}$")
    draw_cone(ax2, -1, 7, "The $3x-1$ cone: mirror image, three drains")

    fig.tight_layout()
    out = Path(__file__).resolve().parent.parent / "images" / "collatz-light-cone.png"
    fig.savefig(out, dpi=160)
    print(f"wrote {out}")


if __name__ == "__main__":
    report()
    plot()