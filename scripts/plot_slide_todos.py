"""Render slide-sized transfer and training plots from saved 1:1 split results."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.ticker import PercentFormatter

FALSE_POSITIVE_COLOR = "#E69F00"
FALSE_NEGATIVE_COLOR = "#0072B2"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as source:
        return list(csv.DictReader(source))


# 🧑 "Where are the box plots? Rid the area plots. ... follow what the paper plot does very very closely."
def draw_rate_boxes(axis: plt.Axes, groups: list[np.ndarray], color: str, marker: str) -> None:
    positions = np.arange(len(groups), dtype=float)
    axis.boxplot(
        groups,
        positions=positions,
        widths=0.58,
        whis=(0, 100),
        showmeans=True,
        showfliers=False,
        patch_artist=True,
        boxprops={"facecolor": color, "edgecolor": color, "alpha": 0.58, "linewidth": 1.6, "zorder": 3},
        medianprops={"color": "#111111", "linewidth": 2.2, "zorder": 4},
        meanprops={
            "marker": "D", "markeredgecolor": "#111111", "markerfacecolor": "#111111",
            "markeredgewidth": 1.0, "markersize": 9, "zorder": 5,
        },
        whiskerprops={"color": color, "linewidth": 1.6, "zorder": 3},
        capprops={"color": color, "linewidth": 1.6, "zorder": 3},
    )
    for position, group in zip(positions, groups, strict=True):
        axis.scatter(
            position + np.linspace(-0.11, 0.11, len(group)), group,
            color=color, marker=marker, s=60, linewidth=1.25, alpha=0.62, zorder=2,
        )


def style_rate_axis(axis: plt.Axes, groups: list[np.ndarray], ylabel: str, xlabel: str) -> None:
    axis.set_xlabel(xlabel)
    axis.set_ylabel(ylabel)
    axis.set_ylim(0, max(0.01, float(np.concatenate(groups).max()) * 1.15))
    axis.yaxis.set_major_formatter(PercentFormatter(1.0))
    axis.grid(axis="y", color="#BBBBBB", linewidth=0.7, alpha=0.45)
    axis.spines[["top", "right"]].set_visible(False)
    axis.spines["bottom"].set_position(("outward", 6))


def box_legend(sample_label: str, color: str, marker: str) -> list[Patch | Line2D]:
    return [
        Patch(facecolor="#888888", alpha=0.45, label="Middle 50% (IQR)"),
        Line2D([], [], color="#777777", linewidth=2, label="Observed range"),
        Line2D([], [], color="#111111", linewidth=2, label="Median"),
        Line2D([], [], marker="D", color="#111111", linestyle="none", markersize=9, label="Mean"),
        Line2D([], [], marker=marker, color=color, linestyle="none", markersize=9, label=sample_label),
    ]


def render_transfer(rows: list[dict[str, str]], output: Path) -> None:
    if len(rows) != 30 or {int(row["n_train_swap"]) for row in rows} != {586}:
        raise ValueError("Expected 30 transfer fits for the saved 1:1 split")
    figure, axis = plt.subplots(figsize=(13.33, 7.5))
    figure.subplots_adjust(left=0.20, right=0.96, bottom=0.20, top=0.78)
    groups = [np.asarray([float(row[key]) for row in rows]) for key in ("wix_fnr", "b12_fnr")]
    draw_rate_boxes(axis, groups, FALSE_NEGATIVE_COLOR, "*")
    style_rate_axis(axis, groups, "False-negative rate", "Held-out builder sites")
    axis.set_xlim(-0.45, 1.45)
    axis.set_xticks(
        np.arange(2),
        [f'{rows[0]["n_test_wix"]} Wix sites', f'{rows[0]["n_test_b12"]} B12 sites'],
    )
    figure.legend(handles=box_legend("30 fits", FALSE_NEGATIVE_COLOR, "*"),
                  loc="upper center", bbox_to_anchor=(0.5, 0.98), ncol=3,
                  fontsize=20, columnspacing=1.0, frameon=False)
    figure.savefig(output, dpi=170, facecolor="white")
    plt.close(figure)


def render_training(rows: list[dict[str, str]], output: Path) -> None:
    checkpoints = [10, 50, 100, 200, 400]
    groups = [
        [row for row in rows if int(row["n_train_swap"]) == count and int(row["repeat"]) < 30]
        for count in checkpoints
    ]
    if any(len(group) != 30 for group in groups):
        raise ValueError("Expected 30 training fits at each saved 1:1 checkpoint")
    full = [row for row in rows if int(row["n_train_swap"]) == 586]
    if len(full) != 1:
        raise ValueError("Expected one full-training result for the saved 1:1 split")
    labels = [f'{group[0]["n_train_swap"]}/{group[0]["n_train_cc"]}' for group in groups] + ["586/5k"]
    figure, axes = plt.subplots(1, 2, figsize=(17, 7.5))
    figure.subplots_adjust(left=0.12, right=0.98, bottom=0.27, top=0.77, wspace=0.43)
    metrics = (
        ("in_domain_cc_fpr", FALSE_POSITIVE_COLOR, "False-positive rate"),
        ("in_domain_swap_fnr", FALSE_NEGATIVE_COLOR, "False-negative rate"),
    )
    for axis, (metric, color, ylabel) in zip(axes, metrics, strict=True):
        values = [np.asarray([float(row[metric]) for row in group]) for group in groups]
        draw_rate_boxes(axis, values, color, "x")
        axis.scatter([len(groups)], [float(full[0][metric])], marker="P", s=190, color="#111111", zorder=6)
        axis.set_xticks(range(len(labels)), labels)
        style_rate_axis(axis, values, ylabel, "Training sites (swap/CC)")
        axis.set_xlim(-0.55, len(groups) + 0.55)
        axis.xaxis.label.set_fontsize(25)
        axis.yaxis.label.set_fontsize(27)
        axis.tick_params(axis="x", labelsize=18)
        plt.setp(axis.get_xticklabels(), rotation=25, ha="right", rotation_mode="anchor")
    figure.legend(
        handles=box_legend("30 fits", FALSE_NEGATIVE_COLOR, "x") + [
            Line2D([], [], color="#111111", marker="P", linestyle="none", markersize=12, label="Full training pool")],
        loc="upper center",
        bbox_to_anchor=(0.5, 0.98),
        ncol=3,
        fontsize=20,
        columnspacing=1.0,
        frameon=False,
    )
    figure.savefig(output, dpi=170, facecolor="white")
    plt.close(figure)


def render_test_size(features_path: Path, training_rows: list[dict[str, str]], output: Path) -> None:
    import pandas as pd
    from sklearn.svm import SVC

    features = pd.read_csv(features_path)
    production = features[features["score_mode"] == "production"]
    swap = production[production["site_kind"] == "body_swap"].set_index("site_identity")
    historical = production[production["site_kind"] == "cc"].set_index("site_identity")
    deciles = [f"decile_{quantile}" for quantile in range(10, 100, 10)]
    split_rng = np.random.RandomState(20260922)
    swap_ids = split_rng.permutation(swap.index)
    historical_ids = split_rng.permutation(historical.index)
    train_swap = swap.loc[swap_ids[:586], deciles].to_numpy(dtype=float)
    test_swap = swap.loc[swap_ids[586:], deciles].to_numpy(dtype=float)
    train_historical = historical.loc[historical_ids[:5000], deciles].to_numpy(dtype=float)
    test_historical = historical.loc[historical_ids[5000:], deciles].to_numpy(dtype=float)
    if len(test_swap) != 586 or len(test_historical) != 5000:
        raise ValueError("The saved 1:1 test pools have changed")
    classifier = SVC(kernel="linear", C=1e6, random_state=42)
    classifier.fit(
        np.vstack([train_historical, train_swap]),
        np.r_[np.zeros(len(train_historical), dtype=int), np.ones(len(train_swap), dtype=int)],
    )
    errors = [classifier.predict(test_swap) == 0, classifier.predict(test_historical) == 1]
    saved_full = next(row for row in training_rows if int(row["n_train_swap"]) == 586)
    expected = [float(saved_full["in_domain_swap_fnr"]), float(saved_full["in_domain_cc_fpr"])]
    if any(not np.isclose(result.mean(), rate) for result, rate in zip(errors, expected, strict=True)):
        raise ValueError("Recreated classifier does not match the saved full-training result")

    figure, axes = plt.subplots(1, 2, figsize=(17, 7.5))
    figure.subplots_adjust(left=0.12, right=0.98, bottom=0.23, top=0.77, wspace=0.43)
    panels = [
        (errors[0], [25, 50, 100, 200, 400], FALSE_NEGATIVE_COLOR, "False-negative rate", "Body-swap test sites"),
        (errors[1], [100, 250, 500, 1000, 2000], FALSE_POSITIVE_COLOR, "False-positive rate", "Historical-CC test sites"),
    ]
    for axis, (error_flags, sizes, color, ylabel, xlabel) in zip(axes, panels, strict=True):
        groups = []
        for size in sizes:
            sample_rng = np.random.RandomState(20260929 + size + len(error_flags))
            groups.append(np.asarray([
                error_flags[sample_rng.choice(len(error_flags), size=size, replace=False)].mean()
                for _ in range(30)
            ]))
        draw_rate_boxes(axis, groups, color, "x")
        axis.scatter([len(sizes)], [error_flags.mean()], color="#111111", marker="P", s=190, zorder=6)
        axis.set_xticks(range(len(sizes) + 1), [*[f"{size:,}" for size in sizes], f"{len(error_flags):,}"])
        style_rate_axis(axis, groups, ylabel, xlabel)
        axis.set_xlim(-0.55, len(sizes) + 0.55)
        axis.xaxis.label.set_fontsize(25)
        axis.yaxis.label.set_fontsize(27)
        axis.tick_params(axis="x", labelsize=19)
    figure.legend(
        handles=box_legend("30 samples", FALSE_NEGATIVE_COLOR, "x") + [
            Line2D([], [], color="#111111", marker="P", linestyle="none", markersize=12, label="Full test pool")],
        loc="upper center",
        bbox_to_anchor=(0.5, 0.98),
        ncol=3,
        fontsize=20,
        columnspacing=1.0,
        frameon=False,
    )
    figure.savefig(output, dpi=170, facecolor="white")
    plt.close(figure)


def render_qualifying_site_calls(output: Path) -> None:
    figure, axis = plt.subplots(figsize=(13.33, 7.5))
    figure.subplots_adjust(left=0.24, right=0.97, bottom=0.19, top=0.94)
    axis.barh([0.38, 0], [6.0, 15.4], height=0.30, color=["#4C78A8", "#188878"])
    axis.set_yticks([0.38, 0], ["Common Crawl", "Bing search"])
    axis.set_ylim(-0.16, 0.54)
    axis.set_xlim(0, 100)
    axis.set_xticks([0, 20, 40, 60, 80, 100])
    axis.set_xlabel("% Sites classified as MGT-dominant")
    axis.grid(axis="x", alpha=0.2)
    axis.set_axisbelow(True)
    axis.spines[["top", "right", "left"]].set_visible(False)
    axis.spines["bottom"].set_visible(True)
    axis.tick_params(axis="y", length=0)
    axis.tick_params(axis="x", length=7)
    axis.text(7.4, 0.38, "6.0%\n(5,643/94,908)", va="center", fontsize=31)
    axis.text(16.8, 0, "15.4%\n(2,803/18,169)", va="center", fontsize=31)
    figure.savefig(output, dpi=170, facecolor="white")
    plt.close(figure)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--transfer-csv", required=True, type=Path)
    parser.add_argument("--training-csv", required=True, type=Path)
    parser.add_argument("--features-csv", type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.size": 25, "axes.labelsize": 31, "xtick.labelsize": 24, "ytick.labelsize": 27, "legend.fontsize": 22})
    render_transfer(read_rows(args.transfer_csv), args.output_dir / "todo_out_of_domain_transfer.png")
    training_rows = read_rows(args.training_csv)
    render_training(training_rows, args.output_dir / "todo_training_size_errors.png")
    if args.features_csv:
        render_test_size(args.features_csv, training_rows, args.output_dir / "todo_test_size_errors.png")
    render_qualifying_site_calls(args.output_dir / "qualified_site_positive_calls_clean.png")


if __name__ == "__main__":
    main()
