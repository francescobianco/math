#!/usr/bin/env python3
"""From S to staircase: the infinite application of a sigmoid self-map.

We study a smooth S-shaped (sigmoid) self-map of its own box,

    f : [a, b] -> [a, b],   f(a)=a,  f(c)=c,  f(b)=b,   c the centre of the S,

and the infinite iteration f^N as N -> infinity. The canonical example is the
"smoothstep" on [0,1],

    f(x) = 3x^2 - 2x^3,

which fixes 0, 1/2, 1, has its single inflection exactly at the centre c=1/2,
and is steep in the middle (f'(1/2)=3/2 > 1) and flat at the ends
(f'(0)=f'(1)=0).

The tools, following the displacement g(x) = f(x) - x of the infinite-
application program:

  * fixed points  = zeros of g (here a, c, b);
  * stability     = |f'| at the fixed point (<1 attract, >1 repel);
  * the KNEES g1,g2 = extrema of g, i.e. where g'(x)=f'(x)-1=0, i.e. f'(x)=1;
    they are the steepest risers of the eventual staircase and the threshold
    between local contraction (f'<1) and expansion (f'>1);
  * the inflection of the S = zero of f'' (here the centre c).

Result (a theorem for continuous increasing self-maps): no hysteresis, no
escape, no cycles of period > 1 -- every orbit is monotone and converges to a
fixed point -- so the infinite application is a STEP FUNCTION (staircase):

    f^inf(x) = a on [a, c),   c at c,   b on (c, b].

Iterating a sigmoid to infinity sharpens it into a hard threshold at c.

Usage:
    python3 library/scripts/s_map_staircase.py
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


# ---- the canonical S-map on [0,1] -----------------------------------------
A, B, C = 0.0, 1.0, 0.5


def f(x):
    return 3 * x ** 2 - 2 * x ** 3


def fp(x):     # f'
    return 6 * x - 6 * x ** 2


def fpp(x):    # f''
    return 6 - 12 * x


def g(x):      # displacement
    return f(x) - x


def iterate(x0, n):
    x = x0
    for _ in range(n):
        x = f(x)
    return x


# ---- the user's richer "double-bend" S on [0,1] ---------------------------
# Five crossings of the diagonal: attracting 0, c=1/2, 1 and repelling
# r1=1/4, r2=3/4. Its infinite iteration is the TWO-step staircase a->c->b.
ALPHA = 6.0
R1, R2 = 0.25, 0.75


def f2(x):
    return x - ALPHA * x * (x - R1) * (x - C) * (x - R2) * (x - B)


def f2p(x):
    h = 1e-6
    return (f2(x + h) - f2(x - h)) / (2 * h)


def iterate2(x0, n):
    x = x0
    for _ in range(n):
        x = f2(x)
    return x


def report():
    print("=" * 60)
    print("S-map  f(x) = 3x^2 - 2x^3  on [0,1]")
    print("=" * 60)

    print("\nfixed points (zeros of g = f - x) and their stability:")
    for p in (A, C, B):
        kind = "attract" if abs(fp(p)) < 1 else "repel "
        print(f"  x={p:<4}  g={g(p):+.3f}  f'={fp(p):+.3f}  [{kind}]")

    g1 = (3 - math.sqrt(3)) / 6
    g2 = (3 + math.sqrt(3)) / 6
    print("\nknees (g'=0  <=>  f'=1), the steepest risers:")
    print(f"  g1 = (3-sqrt3)/6 = {g1:.4f}   f'(g1)={fp(g1):.4f}   g(g1)={g(g1):+.4f} (min)")
    print(f"  g2 = (3+sqrt3)/6 = {g2:.4f}   f'(g2)={fp(g2):.4f}   g(g2)={g(g2):+.4f} (max)")
    print(f"\ninflection of the S (f''=0) at x={ (6/12):.3f}  (= centre c); f''(c)={fpp(C):.1f}")

    print("\nno cycles / no hysteresis: every orbit is monotone and converges:")
    for x0 in (0.05, 0.2, 0.49, 0.51, 0.8, 0.95):
        seq = [x0]
        x = x0
        for _ in range(300):
            x = f(x)
            seq.append(x)
        up = all(seq[i + 1] >= seq[i] - 1e-15 for i in range(len(seq) - 1))
        dn = all(seq[i + 1] <= seq[i] + 1e-15 for i in range(len(seq) - 1))
        print(f"  x0={x0:<4} -> limit={x:.6f}   monotone={'yes' if (up or dn) else 'NO'}")

    print("\nf^inf is the step function:  0 on [0,1/2),  1/2 at 1/2,  1 on (1/2,1].")
    print("Iterating the simple sigmoid to infinity yields ONE threshold at c=1/2.")

    print("\n" + "=" * 60)
    print(f"DOUBLE-BEND S  f(x) = x - {ALPHA}*x(x-1/4)(x-1/2)(x-3/4)(x-1)")
    print("=" * 60)
    print("\nfive fixed points (g=f-x crosses zero five times):")
    for p in (A, R1, C, R2, B):
        kind = "attract" if abs(f2p(p)) < 1 else "repel "
        print(f"  x={p:<5} f'={f2p(p):+.3f}  [{kind}]")
    print("\ninfinite iteration -> TWO-step staircase a -> c -> b:")
    for x0 in (0.1, 0.24, 0.26, 0.5, 0.74, 0.76, 0.9):
        x = x0
        for _ in range(400):
            x = f2(x)
        print(f"  x0={x0:<5} -> {x:.5f}")
    print("\nf^inf:  0 on [0,1/4),  1/2 on (1/4,3/4),  1 on (3/4,1].")
    print("Thresholds are the REPELLING fixed points r1=1/4, r2=3/4 -- the")
    print("centre c is now an attracting tread. Steps = attracting fixed points.")


def plot(out=None):
    import matplotlib.pyplot as plt

    g1 = (3 - math.sqrt(3)) / 6
    g2 = (3 + math.sqrt(3)) / 6
    xs = np.linspace(0, 1, 600)

    fig, ax = plt.subplots(2, 2, figsize=(11, 9))

    # (1) the S-map, the diagonal, fixed points, knees, and two cobwebs
    a0 = ax[0, 0]
    a0.plot(xs, f(xs), color="#b8336a", lw=2, label="$f(x)=3x^2-2x^3$")
    a0.plot(xs, xs, color="gray", ls="--", lw=1, label="$y=x$")
    for p, mk in ((A, "o"), (C, "s"), (B, "o")):
        a0.plot(p, p, mk, color="black", ms=7,
                label="fixed pt" if p == A else None)
    for k in (g1, g2):
        a0.plot(k, f(k), "^", color="#2a6f97", ms=8)
    a0.annotate("$g_1$", (g1, f(g1)), textcoords="offset points", xytext=(-14, 2))
    a0.annotate("$g_2$", (g2, f(g2)), textcoords="offset points", xytext=(6, -2))

    def cobweb(a, x0, color):
        x = x0
        for _ in range(40):
            y = f(x)
            a.plot([x, x], [x, y], color=color, lw=0.6)
            a.plot([x, y], [y, y], color=color, lw=0.6)
            x = y

    cobweb(a0, 0.42, "#e08a1e")
    cobweb(a0, 0.58, "#1ea05a")
    a0.set_title("the S-map: cobwebs fall to $a$ or $b$; $c$ is the watershed")
    a0.set_xlabel("$x$"); a0.set_ylabel("$f(x)$"); a0.legend(loc="upper left", fontsize=8)

    # (2) displacement g(x)=f(x)-x: zeros = fixed pts, extrema = knees
    a1 = ax[0, 1]
    a1.axhline(0, color="gray", lw=0.8)
    a1.plot(xs, g(xs), color="#6a4c93", lw=2, label="$g(x)=f(x)-x$")
    a1.plot(xs, fp(xs) - 1, color="#2a6f97", lw=1.3, ls=":",
            label="$g'(x)=f'(x)-1$")
    for p in (A, C, B):
        a1.plot(p, 0, "o", color="black", ms=6)
    for k in (g1, g2):
        a1.plot(k, g(k), "^", color="#2a6f97", ms=8)
    a1.annotate("$g_1$", (g1, g(g1)), textcoords="offset points", xytext=(-16, -2))
    a1.annotate("$g_2$", (g2, g(g2)), textcoords="offset points", xytext=(4, 2))
    a1.set_title("displacement $g=f-x$: zeros are fixed points, extrema are knees")
    a1.set_xlabel("$x$"); a1.legend(loc="upper left", fontsize=8)

    # (3) f^N steepening toward the staircase
    a2 = ax[1, 0]
    a2.plot(xs, xs, color="gray", ls="--", lw=1)
    for n, col in zip((1, 2, 3, 5, 10, 30),
                      plt.cm.viridis(np.linspace(0, 0.9, 6))):
        a2.plot(xs, iterate(xs, n), color=col, lw=1.6, label=f"$f^{{{n}}}$")
    a2.set_title("$f^N$ sharpens into a step function at $c=1/2$")
    a2.set_xlabel("$x$"); a2.set_ylabel("$f^N(x)$"); a2.legend(fontsize=8, ncol=2)

    # (4) first derivative f' crossing 1 at the knees
    a3 = ax[1, 1]
    a3.axhline(1, color="gray", lw=0.8, ls="--")
    a3.plot(xs, fp(xs), color="#b8336a", lw=2, label="$f'(x)$")
    for k in (g1, g2):
        a3.plot(k, 1, "^", color="#2a6f97", ms=8)
    a3.plot(C, fp(C), "s", color="black", ms=7)
    a3.annotate("$f'(c)=3/2$", (C, fp(C)), textcoords="offset points", xytext=(6, -2))
    a3.fill_between(xs, 1, fp(xs), where=(fp(xs) > 1), color="#b8336a", alpha=0.12)
    a3.set_title("$f'$: expansion ($f'>1$) only between the knees")
    a3.set_xlabel("$x$"); a3.set_ylabel("$f'(x)$"); a3.legend(loc="upper right", fontsize=8)

    fig.tight_layout()
    if out is None:
        out = Path(__file__).resolve().parent.parent / "images" / "s-map-staircase.png"
    fig.savefig(out, dpi=150)
    print(f"\nwrote {out}")


def plot_two_step(out=None):
    """The double-bend S and its two-step staircase a->c->b."""
    import matplotlib.pyplot as plt

    xs = np.linspace(0, 1, 600)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.8))

    a0 = ax[0]
    a0.plot(xs, f2(xs), color="#b8336a", lw=2, label="double-bend $f$")
    a0.plot(xs, xs, color="gray", ls="--", lw=1, label="$y=x$")
    for p in (A, C, B):           # attracting: filled
        a0.plot(p, p, "o", color="black", ms=7)
    for p in (R1, R2):            # repelling: open
        a0.plot(p, p, "o", mfc="white", mec="black", ms=7)

    def cobweb(a, x0, color):
        x = x0
        for _ in range(60):
            y = f2(x)
            a.plot([x, x], [x, y], color=color, lw=0.6)
            a.plot([x, y], [y, y], color=color, lw=0.6)
            x = y

    cobweb(a0, 0.18, "#e08a1e")   # -> 0
    cobweb(a0, 0.45, "#1ea05a")   # -> 1/2
    cobweb(a0, 0.82, "#2a6f97")   # -> 1
    a0.set_title("double-bend S: three attracting treads (filled),\n"
                 "two repelling thresholds $r_1,r_2$ (open)")
    a0.set_xlabel("$x$"); a0.set_ylabel("$f(x)$"); a0.legend(loc="upper left", fontsize=8)

    a1 = ax[1]
    a1.plot(xs, xs, color="gray", ls="--", lw=1)
    for n, col in zip((1, 2, 4, 8, 20, 60),
                      plt.cm.viridis(np.linspace(0, 0.9, 6))):
        a1.plot(xs, iterate2(xs, n), color=col, lw=1.6, label=f"$f^{{{n}}}$")
    a1.set_title(r"$f^N$ -> two-step staircase  $a\to c\to b$" "\n"
                 r"(treads at $0,\frac{1}{2},1$; risers at $r_1=\frac{1}{4}, r_2=\frac{3}{4}$)")
    a1.set_xlabel("$x$"); a1.set_ylabel("$f^N(x)$"); a1.legend(fontsize=8, ncol=2)

    fig.tight_layout()
    if out is None:
        out = Path(__file__).resolve().parent.parent / "images" / "s-map-two-step.png"
    fig.savefig(out, dpi=150)
    print(f"wrote {out}")


if __name__ == "__main__":
    report()
    plot()
    plot_two_step()
