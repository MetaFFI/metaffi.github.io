"""Generate dark-theme performance figures for the MetaFFI website.

Reads benchmark data from tests/results/ and produces PNG charts
in assets/images/ suitable for display on a dark-themed Jekyll site.
"""

import json
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


# Resolve paths relative to the repo root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
TESTS_ROOT = os.path.join(os.path.dirname(REPO_ROOT), "tests", "results")
OUTPUT_DIR = os.path.join(REPO_ROOT, "assets", "images")

# Dark-theme-friendly colors
COLOR_METAFFI = "#4da6ff"
COLOR_GRPC = "#ff6b6b"
COLOR_DEDICATED = "#66cc66"
TEXT_COLOR = "#e0e0e0"
GRID_COLOR = "#333333"
BG_COLOR = "none"  # transparent


def setup_dark_style():
    """Configure matplotlib for dark-theme output."""
    plt.rcParams.update({
        "figure.facecolor": BG_COLOR,
        "axes.facecolor": "#1a1a1a",
        "axes.edgecolor": GRID_COLOR,
        "axes.labelcolor": TEXT_COLOR,
        "text.color": TEXT_COLOR,
        "xtick.color": TEXT_COLOR,
        "ytick.color": TEXT_COLOR,
        "grid.color": GRID_COLOR,
        "grid.alpha": 0.5,
        "font.size": 14,
        "axes.titlesize": 16,
        "legend.facecolor": "#1a1a1a",
        "legend.edgecolor": GRID_COLOR,
        "legend.fontsize": 12,
        "savefig.facecolor": BG_COLOR,
        "savefig.transparent": True,
    })


def load_consolidated():
    """Load mechanism averages from consolidated.json."""
    path = os.path.join(TESTS_ROOT, "consolidated.json")
    with open(path) as f:
        data = json.load(f)
    return data["mechanism_averages_by_pair"]


def load_complexity():
    """Load complexity data from complexity.json."""
    path = os.path.join(TESTS_ROOT, "complexity.json")
    with open(path) as f:
        data = json.load(f)
    return data["aggregate_by_mechanism"]


def deduce_dedicated_name(host, guest, entries):
    """Find the dedicated/native mechanism name for a pair."""
    for e in entries:
        if e["host"] == host and e["guest"] == guest and e["mechanism"] not in ("grpc", "metaffi"):
            return e["mechanism"]
    return None


def generate_cross_pair_summary(averages):
    """Generate horizontal grouped bar chart comparing MetaFFI, Dedicated, gRPC."""
    # Build data per pair
    pairs = []
    seen = set()
    for e in averages:
        key = (e["host"], e["guest"])
        if key not in seen:
            seen.add(key)
            pairs.append(key)

    # Sort pairs for consistent ordering
    pairs.sort()

    labels = []
    metaffi_vals = []
    dedicated_vals = []
    dedicated_names = []
    grpc_vals = []

    for host, guest in pairs:
        label = f"{host} \u2192 {guest}"
        labels.append(label)

        metaffi_ns = None
        grpc_ns = None
        ded_ns = None
        ded_name = None

        for e in averages:
            if e["host"] == host and e["guest"] == guest:
                if e["mechanism"] == "metaffi":
                    metaffi_ns = e["average_mean_ns"]
                elif e["mechanism"] == "grpc":
                    grpc_ns = e["average_mean_ns"]
                else:
                    ded_ns = e["average_mean_ns"]
                    ded_name = e["mechanism"]

        metaffi_vals.append(metaffi_ns or 0)
        grpc_vals.append(grpc_ns or 0)
        dedicated_vals.append(ded_ns or 0)
        dedicated_names.append(ded_name or "native")

    y = np.arange(len(labels))
    bar_height = 0.25

    fig, ax = plt.subplots(figsize=(12, 7))

    ax.barh(y - bar_height, metaffi_vals, bar_height, label="MetaFFI", color=COLOR_METAFFI)
    ax.barh(y, dedicated_vals, bar_height, label="Dedicated (native)", color=COLOR_DEDICATED)
    ax.barh(y + bar_height, grpc_vals, bar_height, label="gRPC", color=COLOR_GRPC)

    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=13)
    ax.set_xscale("log")
    ax.set_xlabel("Average Latency (ns, log scale)", fontsize=14)
    ax.set_title("Cross-Language Call Latency by Mechanism", fontsize=16, pad=15)
    ax.legend(loc="lower right", fontsize=12)
    ax.grid(axis="x", alpha=0.3)
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "perf-cross-pair-summary.png")
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {out_path}")


def generate_complexity_summary(complexity):
    """Generate 3-panel complexity comparison chart."""
    mechanisms = ["metaffi", "grpc", "native"]
    display_names = ["MetaFFI", "gRPC", "Dedicated"]
    colors = [COLOR_METAFFI, COLOR_GRPC, COLOR_DEDICATED]

    # Metrics to compare
    metrics = [
        ("avg_benchmark_sloc", "Avg Benchmark SLOC"),
        ("avg_language_count", "Avg Languages Required"),
        ("avg_benchmark_max_cc", "Avg Max Cyclomatic Complexity"),
    ]

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    for idx, (key, title) in enumerate(metrics):
        ax = axes[idx]
        vals = [complexity[m][key] for m in mechanisms]
        bars = ax.bar(display_names, vals, color=colors, width=0.6, edgecolor="#555")

        # Add value labels on bars
        for bar, val in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max(vals) * 0.02,
                    f"{val:.1f}" if val != int(val) else f"{int(val)}",
                    ha="center", va="bottom", fontsize=12, color=TEXT_COLOR)

        ax.set_title(title, fontsize=14, pad=10)
        ax.grid(axis="y", alpha=0.3)
        ax.set_ylim(0, max(vals) * 1.2)

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "perf-complexity-summary.png")
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {out_path}")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    setup_dark_style()

    print("Loading benchmark data...")
    averages = load_consolidated()
    complexity = load_complexity()

    print("Generating figures...")
    generate_cross_pair_summary(averages)
    generate_complexity_summary(complexity)

    print("Done.")


if __name__ == "__main__":
    main()
