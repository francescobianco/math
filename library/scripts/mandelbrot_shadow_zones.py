#!/usr/bin/env python3
"""What if fractals don't exist? — measuring the Mandelbrot boundary as a
machine-dependent object.

The Mandelbrot set is M = { c in C : the orbit of 0 under z -> z^2 + c stays
bounded }. The *set* is a perfectly well-defined object. What a computer draws
is not the set: it is the level set of a finite machine, controlled by three
quantizations —

  * GRID    : one pixel stands in for a whole square of c-values;
  * DEPTH   : we iterate only up to a cap N and paint "black" (= in the set)
              everything that has not yet escaped |z| > 2;
  * PRECISION: float32 vs float64 vs ... arithmetic.

This script measures how much the rendered set depends on those choices,
near the boundary where the finite escape-time test gives no verdict
(it only ever certifies escapes, never "never escapes"):

  1. black_breath()   : |black pixels| shrinks as the depth cap N grows --
                        the rendered set is never the true set, it only
                        approaches it from above, and keeps moving.
  2. precision_flip() : how many pixels change verdict (in <-> out) between
                        float32 and float64 at the same depth -- the boundary
                        you see depends on the mantissa.
  3. shadow_zone()    : the SHADOW = pixels whose verdict flips when you change
                        a machine parameter (depth or precision). A cheap SAMPLED
                        proxy for the "undecided" zone (a rigorous version needs
                        interval/ball arithmetic). Its share of the boundary band
                        is reported versus grid resolution: over the three
                        resolutions run it rises rather than falls -- a measured
                        trend, not a proven limit; consistent with, but not a
                        proof of, Shishikura's dim_H(dM) = 2.
  4. escape_faithfulness(): the OTHER side -- is an ESCAPE faithful? float64 vs
                        80-bit longdouble: spurious escapes (f64 says outside,
                        higher precision stays bounded), missed escapes, and
                        escape-time discrepancies. The divergence inequality is a
                        theorem about the TRUE orbit; the computed crossing is a
                        pseudo-orbit event, so plain float certifies escape no
                        better than it certifies boundedness near the boundary.

It also renders images/mandelbrot-shadow-zones.png: the set with the shadow
skin painted red -- an honest three-state picture (out / in / undecided).

Usage:
    python3 library/scripts/mandelbrot_shadow_zones.py
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

WINDOW = (-2.5, 1.0, -1.5, 1.5)  # (re_min, re_max, im_min, im_max)


_CDTYPE = {np.float32: np.complex64, np.float64: np.complex128,
           np.longdouble: np.clongdouble}


def escape_iter(window, res, maxiter, dtype=np.float64):
    """Return per-pixel escape iteration; -1 means 'still bounded at cap N'
    (i.e. painted black = classified IN the set)."""
    cdtype = _CDTYPE.get(np.dtype(dtype).type, np.complex128)
    re = np.linspace(window[0], window[1], res, dtype=dtype)
    im = np.linspace(window[2], window[3], res, dtype=dtype)
    C = (re[np.newaxis, :] + 1j * im[:, np.newaxis]).astype(cdtype)
    Z = np.zeros_like(C)
    out = np.full(C.shape, -1, dtype=np.int64)
    alive = np.ones(C.shape, dtype=bool)
    for n in range(maxiter):
        Z[alive] = Z[alive] * Z[alive] + C[alive]
        escaped_now = alive & (np.abs(Z) > 2)
        out[escaped_now] = n
        alive &= ~escaped_now
    return out


def inside_mask(window, res, maxiter, dtype=np.float64):
    """Boolean: pixel classified IN the set at this (depth, precision)."""
    return escape_iter(window, res, maxiter, dtype) < 0


def black_breath(res=600):
    print("1. The boundary breathes with the depth cap N")
    print("   (black = 'not yet escaped' = classified IN; shrinks as N grows)")
    caps = [50, 100, 200, 500, 1000, 2000]
    prev = None
    for N in caps:
        m = inside_mask(WINDOW, res, N)
        black = int(m.sum())
        delta = "" if prev is None else f"   (lost {prev - black} pixels vs previous N)"
        print(f"   N={N:>5}:  black pixels = {black:>7}{delta}")
        prev = black
    print()


def precision_flip(res=600, maxiter=1000):
    print("2. The boundary depends on the mantissa")
    m64 = inside_mask(WINDOW, res, maxiter, np.float64)
    m32 = inside_mask(WINDOW, res, maxiter, np.float32)
    flips = int(np.count_nonzero(m64 != m32))
    total = res * res
    print(f"   float32 vs float64 at N={maxiter}, {res}x{res} grid:")
    print(f"   {flips} pixels change verdict ({100*flips/total:.3f}% of the grid)")
    print(f"   -> the rendered set is not precision-independent near dM")
    print()


def escape_faithfulness(res=700, maxiter=2000):
    """The OTHER side: is an ESCAPE faithful? The divergence inequality is a
    theorem about the TRUE orbit; the machine checks it on a pseudo-orbit. Near
    the boundary a spurious crossing can paint a bounded point 'outside'.
    We compare float64 against 80-bit extended precision (longdouble)."""
    print("4. Is an escape even faithful? (the white side)")
    it64 = escape_iter(WINDOW, res, maxiter, np.float64)
    it80 = escape_iter(WINDOW, res, maxiter, np.longdouble)
    esc64, esc80 = it64 >= 0, it80 >= 0
    spurious = int(np.count_nonzero(esc64 & ~esc80))   # f64 escapes, f80 bounded
    missed = int(np.count_nonzero(~esc64 & esc80))
    both = esc64 & esc80
    dt = np.abs(it64 - it80)[both]
    print(f"   {res}x{res}, N={maxiter}, float64 vs 80-bit longdouble:")
    print(f"   escape-verdict flips: {spurious + missed}  "
          f"(SPURIOUS escapes f64 paints outside but stay bounded: {spurious}; "
          f"missed: {missed})")
    print(f"   among commonly-escaped pixels: max |escape-time difference| = "
          f"{int(dt.max())}, #(>=5) = {int((dt >= 5).sum())}")
    print(f"   -> the escape inequality is a theorem about the TRUE orbit; the")
    print(f"      computed crossing is a pseudo-orbit event, unfaithful near dM.")
    print(f"      Only interval arithmetic certifies escape; plain float does not.")
    print()


def shadow_zone():
    print("3. The shadow zone: pixels the machine cannot decide")
    print("   (verdict flips under a change of depth OR precision)")
    print("   shadow fraction is taken relative to the rendered boundary band,")
    print("   not the whole frame, so it is not diluted by trivial interior/exterior")
    for res in (300, 600, 1200):
        # reference (deep, double) vs cheaper machines
        deep64 = inside_mask(WINDOW, res, 4000, np.float64)
        shallow64 = inside_mask(WINDOW, res, 200, np.float64)
        deep32 = inside_mask(WINDOW, res, 4000, np.float32)
        depth_flip = deep64 != shallow64
        prec_flip = deep64 != deep32
        shadow = depth_flip | prec_flip
        n_shadow = int(shadow.sum())
        n_in = int(deep64.sum())
        # boundary band proxy: pixels adjacent to a verdict change in deep64
        b = deep64
        boundary = (
            (b[1:-1, 1:-1] != b[:-2, 1:-1])
            | (b[1:-1, 1:-1] != b[2:, 1:-1])
            | (b[1:-1, 1:-1] != b[1:-1, :-2])
            | (b[1:-1, 1:-1] != b[1:-1, 2:])
        )
        n_boundary = int(boundary.sum())
        print(f"   {res:>4}x{res:<4}:  shadow={n_shadow:>6}  "
              f"in={n_in:>7}  boundary-band={n_boundary:>6}  "
              f"shadow/boundary={n_shadow / max(n_boundary,1):.2f}")
    print("   -> over these three resolutions the undecided share RISES, not")
    print("      falls (measured trend, not a proven limit); consistent with")
    print("      dim_H dM = 2. Either way, a finite render must choose what to")
    print("      do with the band its escape-time test leaves unanswered.")
    print()


def render_three_state(res=900, out=None):
    """out / in / shadow image: the honest three-color picture."""
    import matplotlib.pyplot as plt

    deep64 = inside_mask(WINDOW, res, 4000, np.float64)
    shallow64 = inside_mask(WINDOW, res, 200, np.float64)
    deep32 = inside_mask(WINDOW, res, 4000, np.float32)
    shadow = (deep64 != shallow64) | (deep64 != deep32)

    img = np.zeros((res, res, 3))
    img[~deep64] = (0.05, 0.05, 0.12)     # outside: deep blue-black
    img[deep64] = (0.92, 0.92, 0.96)      # inside: near-white
    img[shadow] = (0.85, 0.12, 0.18)      # shadow skin: red

    fig, ax = plt.subplots(figsize=(7.2, 6.2))
    ax.imshow(img, extent=WINDOW, origin="lower")
    ax.set_title("The Mandelbrot set as a three-state object\n"
                 "white = certified-ish IN, dark = OUT, "
                 "red = SHADOW (verdict flips with N or precision)")
    ax.set_xlabel("Re $c$")
    ax.set_ylabel("Im $c$")
    fig.tight_layout()
    if out is None:
        out = Path(__file__).resolve().parent.parent / "images" / "mandelbrot-shadow-zones.png"
    fig.savefig(out, dpi=150)
    print(f"wrote {out}")


if __name__ == "__main__":
    print("=" * 64)
    print("What if fractals don't exist? Mandelbrot as a machine artifact")
    print("=" * 64)
    black_breath()
    precision_flip()
    shadow_zone()
    escape_faithfulness()
    render_three_state()
