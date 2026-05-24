#!/usr/bin/env python3
"""Plot the logarithmic butterfly for the derivative mystery paper."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
IMAGE_DIR = ROOT / "library" / "images"
OUTPUT = IMAGE_DIR / "logarithmic-butterfly.png"


def clipped(values: np.ndarray, y_min: float, y_max: float) -> np.ndarray:
    out = values.astype(float).copy()
    out[(out < y_min) | (out > y_max) | ~np.isfinite(out)] = np.nan
    return out


def main() -> None:
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    x_min, x_max = -3.0, 8.0
    y_min, y_max = -3.0, 8.0
    xs = np.linspace(x_min, x_max, 2400)

    with np.errstate(over="ignore", invalid="ignore"):
        exp_x = clipped(np.exp(xs), y_min, y_max)
        exp_exp_x = clipped(np.exp(np.exp(xs)), y_min, y_max)

    log_x = np.full_like(xs, np.nan)
    mask_log = xs > 0
    log_x[mask_log] = np.log(xs[mask_log])
    log_x = clipped(log_x, y_min, y_max)

    log_log_x = np.full_like(xs, np.nan)
    mask_loglog = xs > 1
    log_log_x[mask_loglog] = np.log(np.log(xs[mask_loglog]))
    log_log_x = clipped(log_log_x, y_min, y_max)

    fig, ax = plt.subplots(figsize=(9, 9))
    ax.plot(xs, xs, color="#222222", linewidth=1.2, linestyle="--", label=r"major diagonal $y=x$")
    ax.plot(xs, exp_x, color="#d62728", linewidth=2.2, label=r"$e^x$")
    ax.plot(xs, log_x, color="#1f77b4", linewidth=2.2, label=r"$\log x$")
    ax.plot(xs, exp_exp_x, color="#ff7f0e", linewidth=2.2, label=r"$e^{e^x}$")
    ax.plot(xs, log_log_x, color="#9467bd", linewidth=2.2, label=r"$\log(\log x)$")

    ax.fill_between(xs, exp_x, exp_exp_x, where=np.isfinite(exp_x) & np.isfinite(exp_exp_x), color="#ff7f0e", alpha=0.08)
    ax.fill_between(xs, log_log_x, log_x, where=np.isfinite(log_x) & np.isfinite(log_log_x), color="#1f77b4", alpha=0.08)

    ax.annotate(
        "exponential wing",
        xy=(0.45, float(np.exp(np.exp(0.45)))),
        xytext=(-2.25, 6.8),
        arrowprops={"arrowstyle": "->", "linewidth": 0.9, "color": "#a84d00"},
        fontsize=10,
        color="#a84d00",
    )
    ax.annotate(
        "logarithmic wing",
        xy=(6.2, float(np.log(np.log(6.2)))),
        xytext=(3.4, -2.2),
        arrowprops={"arrowstyle": "->", "linewidth": 0.9, "color": "#4a2c83"},
        fontsize=10,
        color="#4a2c83",
    )
    ax.annotate(
        "reflection axis",
        xy=(3.8, 3.8),
        xytext=(5.0, 4.6),
        arrowprops={"arrowstyle": "->", "linewidth": 0.9, "color": "#222222"},
        fontsize=10,
        color="#222222",
    )

    ax.set_title("The logarithmic butterfly")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, color="#dddddd", linewidth=0.8)
    ax.legend(loc="upper left", framealpha=0.95)

    fig.text(
        0.5,
        0.025,
        r"$e^x$ and $\log x$ are mirror curves; $e^{e^x}$ and $\log(\log x)$ form the outer mirrored wings.",
        ha="center",
        fontsize=10,
        color="#555555",
    )

    fig.tight_layout(rect=(0, 0.045, 1, 1))
    fig.savefig(OUTPUT, dpi=180)
    print(f"Saved graph to {OUTPUT}")


if __name__ == "__main__":
    main()
