"""Plot audited Bing top-k exposure over all 10,000 sampled queries.

Counts are from DeGenTWeb_writeup/docs/notes/measurement_audit_2026_09_14.md,
Search reconciliation, produced from SHA-256-verified ranks.csv and sites.csv.
The denominator includes queries with no classified MGT-dominant result.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

QUERY_COUNT = 10_000
TOP_K = (10, 20)
MGT_QUERY_COUNTS = (4_532, 6_477)


def main() -> None:
    output = Path(__file__).resolve().parent.parent / "public/paper/search_queries_positive_calls.png"
    shares = [count / QUERY_COUNT for count in MGT_QUERY_COUNTS]
    if any(not 0 <= count <= QUERY_COUNT for count in MGT_QUERY_COUNTS):
        raise ValueError("Audited counts must be within the all-query denominator")

    figure, axis = plt.subplots(figsize=(15, 6.5), dpi=180)
    positions = list(range(len(TOP_K)))
    axis.barh(positions, shares, height=0.58, color=("#0072B2", "#009E73"))
    axis.set_yticks(positions, labels=[f"Top {rank}" for rank in TOP_K], fontsize=31)
    axis.invert_yaxis()
    axis.set_xlim(0, 1)
    axis.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1])
    axis.xaxis.set_major_formatter(PercentFormatter(1.0, decimals=0))
    axis.tick_params(axis="x", labelsize=27, length=8, width=1.6)
    axis.tick_params(axis="y", length=0, pad=18)
    axis.set_xlabel("Queries with an MGT-dominant site (%)", fontsize=30, labelpad=16)
    axis.grid(axis="x", color="#D8DEE2", linewidth=1.1)
    axis.set_axisbelow(True)
    axis.spines[["top", "left", "right"]].set_visible(False)
    axis.spines["bottom"].set_linewidth(1.6)
    for position, share, count in zip(positions, shares, MGT_QUERY_COUNTS, strict=True):
        axis.text(share + 0.013, position, f"{share:.1%} ({count:,})", fontsize=27, fontweight="bold", va="center")
    figure.subplots_adjust(left=0.19, right=0.93, top=0.96, bottom=0.23)
    figure.savefig(output, dpi=180, facecolor="white")
    plt.close(figure)


if __name__ == "__main__":
    main()
