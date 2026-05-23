#!/usr/bin/env python3
"""Plot a normalized semilogarithm value map against log(x).

The semilogarithm s is defined formally by

    s(s(x)) = log(x)

and normalized here by

    s(1/2) = 0.

This condition forces the value chain

    e -> sqrt(e) -> 1 -> 1/2 -> 0 -> -log(2) -> -infinity

and the positive half-step tower

    H0 = sqrt(e), H1 = exp(H0), H2 = exp(H1), ...

The equation and normalization determine these anchor values, but not a unique
continuous function between them. This script therefore builds a visual model by
monotone linear interpolation through the forced anchors and plots it together
with log(x), log(log(x)), and log(s(x)).
"""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
IMAGE_DIR = ROOT / "library" / "images"
OUTPUT = IMAGE_DIR / "semilogarithm-normalized.png"


def forced_positive_anchors() -> list[tuple[float, float, str]]:
    """Return known x -> s(x) anchors implied by s(1/2)=0."""
    h0 = math.sqrt(math.e)
    h1 = math.exp(h0)

    return [
        (0.0, -math.log(2.0), r"$s(0)=-\log 2$"),
        (0.5, 0.0, r"$s(1/2)=0$"),
        (1.0, 0.5, r"$s(1)=1/2$"),
        (h0, 1.0, r"$s(\sqrt{e})=1$"),
        (math.e, h0, r"$s(e)=\sqrt{e}$"),
        (h1, math.e, r"$s(e^{\sqrt{e}})=e$"),
    ]


def interpolated_semilogarithm(xs: np.ndarray, anchors: list[tuple[float, float, str]]) -> np.ndarray:
    """Approximate s(x) by linear interpolation through known anchors."""
    ax = np.array([x for x, _, _ in anchors], dtype=float)
    ay = np.array([y for _, y, _ in anchors], dtype=float)
    return np.interp(xs, ax, ay)


def main() -> None:
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    anchors = forced_positive_anchors()
    singular_x = -math.log(2.0)
    x_min = singular_x - 0.25
    x_max = anchors[-1][0]
    xs = np.linspace(x_min, x_max, 1100)

    semi = np.full_like(xs, np.nan)
    semi_mask = xs >= 0.0
    semi[semi_mask] = interpolated_semilogarithm(xs[semi_mask], anchors)

    log_values = np.full_like(xs, np.nan)
    log_mask = xs > 0.0
    log_values[log_mask] = np.log(xs[log_mask])

    loglog_values = np.full_like(xs, np.nan)
    loglog_mask = xs > 1.0
    loglog_values[loglog_mask] = np.log(log_values[loglog_mask])

    log_semi_values = np.full_like(xs, np.nan)
    log_semi_mask = semi > 0.0
    log_semi_values[log_semi_mask] = np.log(semi[log_semi_mask])

    print("Normalized semilogarithm anchors from s(1/2)=0")
    print("x\ts(x)\tlabel")
    for x, y, label in anchors:
        print(f"{x:.12g}\t{y:.12g}\t{label}")

    print("\nSampled comparison")
    print("x\ts_approx(x)\tlog(x)\tlog(s_approx(x))\tlog(log(x))")
    for x in [singular_x, 0.0, 0.05, 0.1, 0.25, 0.5, 1.0, math.sqrt(math.e), math.e, anchors[-1][0]]:
        sx = interpolated_semilogarithm(np.array([x]), anchors)[0] if x >= 0 else float("nan")
        lx = math.log(x) if x > 0 else float("nan")
        lsx = math.log(sx) if sx > 0 else float("nan")
        llx = math.log(lx) if lx > 0 else float("nan")
        print(f"{x:.12g}\t{sx:.12g}\t{lx:.12g}\t{lsx:.12g}\t{llx:.12g}")

    fig, ax = plt.subplots(figsize=(11, 7))
    ax.plot(xs, semi, linewidth=2.4, color="#1f77b4", label=r"normalized $s(x)$ approximation")
    ax.plot(xs, log_values, linewidth=2.0, color="#d62728", linestyle="--", label=r"$\log(x)$")
    ax.plot(xs, log_semi_values, linewidth=2.0, color="#2ca02c", linestyle="-.", label=r"$\log(s(x))$")
    ax.plot(xs, loglog_values, linewidth=2.0, color="#9467bd", linestyle=":", label=r"$\log(\log(x))$")

    anchor_x = [x for x, _, _ in anchors if x > 0]
    anchor_y = [y for x, y, _ in anchors if x > 0]
    ax.scatter(anchor_x, anchor_y, color="#1f77b4", edgecolor="white", linewidth=1.2, s=70, zorder=3)

    for x, y, label in anchors:
        if x <= 0:
            continue
        ax.annotate(
            label,
            xy=(x, y),
            xytext=(8, 8),
            textcoords="offset points",
            fontsize=9,
            color="#0f3d68",
        )

    ax.axhline(0, color="#333333", linewidth=0.8, alpha=0.5)
    ax.axhline(singular_x, color="#7f7f7f", linewidth=0.9, linestyle="--", alpha=0.7)
    ax.axvline(1, color="#333333", linewidth=0.8, alpha=0.35)
    ax.axvline(singular_x, color="#111111", linewidth=1.1, linestyle=":", alpha=0.85)
    ax.annotate(
        r"$x=-\log 2$, $s(x)\to-\infty$",
        xy=(singular_x, 0.0),
        xytext=(10, 34),
        textcoords="offset points",
        arrowprops={"arrowstyle": "->", "color": "#111111", "linewidth": 0.9},
        fontsize=9,
        color="#111111",
    )
    ax.annotate(
        r"$s(0)=-\log 2$",
        xy=(0.0, singular_x),
        xytext=(12, -22),
        textcoords="offset points",
        arrowprops={"arrowstyle": "->", "color": "#555555", "linewidth": 0.9},
        fontsize=9,
        color="#555555",
    )
    ax.set_title("Normalized semilogarithm value map and logarithmic comparisons")
    ax.set_xlabel("x")
    ax.set_ylabel("value")
    ax.set_xlim(x_min, x_max)
    finite_curves = np.concatenate([
        semi[np.isfinite(semi)],
        log_values[np.isfinite(log_values)],
        log_semi_values[np.isfinite(log_semi_values)],
        loglog_values[np.isfinite(loglog_values)],
    ])
    ax.set_ylim(finite_curves.min() - 0.25, finite_curves.max() + 0.4)
    ax.grid(True, color="#d9d9d9", linewidth=0.8, alpha=0.8)
    ax.legend(loc="upper left")

    fig.text(
        0.02,
        0.02,
        "Note: the curve for s(x) is an interpolation through forced values, not a unique analytic solution.",
        fontsize=9,
        color="#555555",
    )

    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(OUTPUT, dpi=180)
    print(f"\nSaved graph to {OUTPUT}")


if __name__ == "__main__":
    main()
