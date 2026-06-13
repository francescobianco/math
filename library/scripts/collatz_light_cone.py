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


def displacement_at_vertex(b: int) -> Fraction:
    """g(V) = (vertex y) - (vertex x) = f(x)-x at the vertex.

    Positive => the throat sits ABOVE the bisector (the trapping/dome side);
    negative => BELOW it (the escaping side). Equals b/5, so its sign tracks
    the sign of b and FLIPS under the origin reflection b -> -b.
    """
    vx, vy = vertex(b)
    return vy - vx


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
        g = displacement_at_vertex(b)
        side = "ABOVE (dome / trapping side)" if g > 0 else "BELOW (escaping side)"
        print(f"  cone vertex V = ({vx}, {vy})")
        print(f"  diagonal slope 1 in (1/2, 3)? yes -> y=x lies inside the wedge")
        print(f"  displacement g(V) = {g} -> vertex is {side}; sign matches sign(b)")
        verify_edges(b)
        print(f"  every orbit point lies on a cone edge: OK")
        d = drift(b)
        print(f"  mean log-multiplier / macrostep = {d:+.4f} "
              f"(log(3/4) = {math.log(3/4):+.4f}); contracts toward the vertex")
        print(f"  positive cycles: {find_cycles(b)}")
        print("-" * 64)


# ---------------------------------------------------------------------------
# The continuum abstraction: a generic continuous f whose graph lives in the
# cone. Edges have slopes s_- = 1/2 < 1 < 3 = s_+ and meet at V; the only
# datum that matters is delta = g(V) = yV - xV (= b/5).
# ---------------------------------------------------------------------------

def edge_zone(b: int) -> None:
    """Lemma A/B: edge displacements and the throat sign-zone."""
    sm, sp = Fraction(1, 2), 3
    vx, vy = vertex(b)
    delta = vy - vx  # = b/5
    # g_pm(x) = (s_pm - 1)(x - vx) + delta; zeros:
    x_lo = vx - delta / (sm - 1)   # lower edge meets bisector
    x_hi = vx - delta / (sp - 1)   # upper edge meets bisector
    print(f"3x{b:+d}: V=({vx},{vy}), delta=g(V)={delta}")
    print(f"  lower edge (slope 1/2) meets y=x at x={x_lo}")
    print(f"  upper edge (slope 3)  meets y=x at x={x_hi}")
    if delta > 0:
        print(f"  throat zone [{vx},{x_lo}): whole cone ABOVE bisector "
              f"-> every confined f is pushed RIGHT (toward a trap)")
    else:
        print(f"  throat zone [{vx},{x_hi}): whole cone BELOW bisector "
              f"-> every confined f is pushed LEFT (out through the throat)")
    # Theorem A: forward-invariance of [xV, inf) for ALL confined f
    invariant = vy >= vx
    print(f"  forward-invariant for ALL confined f? {invariant}  "
          f"(holds iff delta>=0, i.e. yV>=xV)")


def confined(f, b: int, lo: float = 1.0, hi: float = 60.0, n: int = 600) -> bool:
    xs = np.linspace(lo, hi, n)
    fx = np.array([f(x) for x in xs])
    return bool(np.all((xs / 2 <= fx + 1e-12) & (fx <= 3 * xs + b + 1e-12)))


def contraction_demo() -> None:
    """Theorem B (delta>0): a confined Lipschitz contraction drains the whole
    cone to a single throat point. Illustrative continuous model for b=+1."""
    b = 1
    f = lambda x: x / 2 + 1            # slope 1/2 < 1, fixed point x* = 2
    print(f"\n  Theorem B demo (3x+1): f(x) = x/2 + 1, a confined contraction")
    print(f"    confined on [1,60]? {confined(f, b)}")
    for seed in (1, 3, 7, 27, 1000):
        x = float(seed)
        for _ in range(80):
            x = f(x)
        print(f"    orbit from {seed:>4} -> {x:.6f}   (unique throat x* = 2)")


def identity_counterexample() -> None:
    """Bare confinement is NOT enough: the identity lives in the cone yet every
    point is fixed -- no drainage."""
    b = 1
    f = lambda x: x
    print(f"\n  counterexample: f(x) = x is confined (b=+1, x>=0)? "
          f"{confined(f, b)} -- yet f^n(x)=x for all n (no collapse).")
    print(f"    => convergence needs a strict contraction hypothesis, not just"
          f" 'lives in the cone'.")


def leak_and_fragmentation_demo() -> None:
    """delta<0 (3x-1): the cone is not forward-invariant (it leaks below the
    vertex), and a confined map can fragment into several attractors.

    NOTE (see paper section 13): the multi-attractor part is an illustrative
    CARTOON, not a verification. Iterating a non-contracting confined map in
    floating point is quantization-sensitive -- rounding can change the limit
    -- so the reported limits are suggestive only. The leak itself (one step
    of f=x/2 falling below the vertex) is exact and robust.
    """
    b = -1
    vx, _ = vertex(b)
    print(f"\n  3x-1 leak: lower-edge map f(x)=x/2 sends throat points below "
          f"the vertex xV={vx}:")
    x = 0.5
    for i in range(4):
        x = x / 2
        print(f"    step {i+1}: x={x:.4f}  (below xV={float(vx):.2f}? {x < float(vx)})")
    f = lambda x: x - 0.4 * math.sin(2 * math.pi * math.log(x + 1))
    print(f"  3x-1 multi-attractor CARTOON (quantization-sensitive, not a "
          f"verification -- see section 13):")
    print(f"    f(x)=x-0.4 sin(2pi log(x+1)), confined on [1,60]? {confined(f, b)}")
    limits = []
    for seed in (2, 5, 9, 20, 60):
        x = float(seed)
        for _ in range(300):
            x = f(x)
        limits.append(round(x, 3))
        print(f"    orbit from {seed:>4} -> {x:.4f}")
    print(f"    distinct limits: {sorted(set(limits))} -> several drains, like "
          f"the three 3x-1 cycles.")


def report_continuum() -> None:
    print("=" * 64)
    print("CONTINUUM ABSTRACTION: generic continuous f living in the cone")
    print("=" * 64)
    for b in (1, -1):
        edge_zone(b)
        print("-" * 64)
    contraction_demo()
    identity_counterexample()
    leak_and_fragmentation_demo()
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

        # --- zoom inset on the vertex: above vs below the bisector ----------
        axin = ax.inset_axes([0.58, 0.10, 0.38, 0.38])
        zx = np.linspace(float(vx) - 0.6, float(vx) + 0.6, 200)
        axin.plot(zx, 3 * zx + b, color="#b8336a", lw=1.4)
        axin.plot(zx, zx / 2, color="#2a6f97", lw=1.4)
        axin.plot(zx, zx, color="gray", lw=1, ls="--")
        axin.fill_between(zx, zx / 2, 3 * zx + b, where=(3 * zx + b >= zx / 2),
                          color="#f2c14e", alpha=0.25)
        axin.plot(float(vx), float(vy), "o", color="black", ms=5)
        gsign = "above" if (vy - vx) > 0 else "below"
        axin.set_title(f"vertex {gsign} $y=x$", fontsize=8)
        axin.set_xticks([])
        axin.set_yticks([])

    draw_cone(ax1, 1, 7, "Collatz cone $3x+1$: one drain $\\{1,2,4\\}$")
    draw_cone(ax2, -1, 7, "The $3x-1$ cone: mirror image, three drains")

    fig.tight_layout()
    out = Path(__file__).resolve().parent.parent / "images" / "collatz-light-cone.png"
    fig.savefig(out, dpi=160)
    print(f"wrote {out}")


if __name__ == "__main__":
    report()
    report_continuum()
    plot()