"""Plot Bing and Common Crawl filtering from separate, frozen source cohorts.

Bing counts are queried from the SHA-256-verified frozen Search snapshot.
Common Crawl's pre-filter cache has one combined token-length/duplication count,
not separate counts; it is a different cohort from the paper's scored 94,908 sites.
Its base includes latest successful captures with a classification, and English
and Dolma counts are separate marginals rather than successive filtering stages.
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import duckdb
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

SOURCE_SHA256 = "4fbeb3e951829efcb37f3455a6230130899866a4391935fdeea5cd8d0bc5e90c"
SOURCE_PATH = Path("/ssd1/sichangheagent/source1840-filtering-artifacts/inputs/20260415_160556.duckdb")
CC_SOURCE_PATH = Path("/ssd1/sichangheagent/source1840-archive-artifacts/inputs/cc_dolma_fresh_20260330_233845.duckdb")
CC_SOURCE_SHA256 = "e16c5cb21c4896e255c6981c9d1ccb3de19bf004eae0d1514f19550c7b00afb2"
PAGE_LABELS = ("Total crawled", "Has English body", "≥200 tokens", "Pass Dolma", "≤50% dup")
SITE_LABELS = ("Search-result sites", "Has saved pages", "≥1 eligible page", "≥15 eligible pages")
CC_PAGE_LABELS = ("Successful captures\nwith classification", "English\n(separate marginal)", "Dolma pass\n(separate marginal)", "Dolma + ≥200 tokens\n& ≤50% duplication")
CC_SITE_LABELS = ("Total crawled", "Has English body", "Pass Dolma", "≥1 eligible page", "≥15 eligible pages")


def draw_bars(labels: tuple[str, ...], counts: tuple[int, ...], units: str, output: Path, note: str | None = None) -> None:
    figure, axis = plt.subplots(figsize=(16, 8), dpi=180)
    positions = list(range(len(labels)))
    colors = ["#0072B2"] * (len(labels) - 1) + ["#E69F00"]
    if note is not None:
        colors[1] = "#009E73"
    axis.barh(positions, counts, height=0.61, color=colors)
    axis.set_yticks(positions, labels=labels, fontsize=28 if note else 32)
    axis.invert_yaxis()
    axis.set_xlim(0, max(counts) * (1.43 if max(counts) > 10_000_000 else 1.28))
    axis.set_xlabel(units, fontsize=35, labelpad=13)
    axis.xaxis.set_major_formatter(
        FuncFormatter(
            lambda value, _: "0" if value == 0 else
            f"{value / 1_000_000:g}M" if units == "Pages" else f"{value / 1_000:g}k"
        )
    )
    axis.tick_params(axis="x", labelsize=28, length=8, width=1.6)
    axis.tick_params(axis="y", length=0, pad=17)
    for position, count in zip(positions, counts, strict=True):
        axis.text(count + max(counts) * 0.015, position, f"{count:,}", va="center", fontsize=31)
    axis.spines[["top", "right", "left"]].set_visible(False)
    axis.spines["bottom"].set_linewidth(1.6)
    figure.subplots_adjust(left=0.43 if note else 0.34, right=0.985, top=0.96, bottom=0.27 if note else 0.19)
    if note is not None:
        figure.text(0.5, 0.035, note, ha="center", va="bottom", fontsize=19)
    figure.savefig(output, dpi=180)
    plt.close(figure)


def require_counts(row: tuple[int, ...] | None) -> tuple[int, ...]:
    """Reject absent aggregate results before using their counts."""
    if row is None:
        raise SystemExit("Missing filtering counts", locals())
    return row


# 🧑 "Convert the filtering breakdown to bar plots. Y labels should be “Total crawled” “Has English text” “≥200 tokens” “Pass Dolma” “≤50% dup” Do page-level breakdown, right? Then have a final breakdown of how many sites we are left with"
def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=SOURCE_PATH)
    parser.add_argument("--cc-database", type=Path, default=CC_SOURCE_PATH)
    parser.add_argument("--output-dir", type=Path, default=Path("public/paper"))
    parser.add_argument("--cc-pages-only", action="store_true")
    args = parser.parse_args()
    with args.database.open("rb") as database:
        if hashlib.file_digest(database, "sha256").hexdigest() != SOURCE_SHA256:
            raise ValueError("Frozen Search source does not match the audited snapshot")
    with args.cc_database.open("rb") as database:
        if hashlib.file_digest(database, "sha256").hexdigest() != CC_SOURCE_SHA256:
            raise ValueError("Frozen Common Crawl source does not match the audited snapshot")
    with duckdb.connect(str(args.database), read_only=True) as connection:
        page_counts = require_counts(connection.execute("""
            SELECT count(*),
                count(*) FILTER (WHERE crawl_ok AND w_browser AND is_english),
                count(*) FILTER (WHERE crawl_ok AND w_browser AND is_english AND n_tokens >= 200),
                count(*) FILTER (WHERE crawl_ok AND w_browser AND is_english AND n_tokens >= 200 AND passes_filter),
                count(*) FILTER (WHERE crawl_ok AND w_browser AND is_english AND n_tokens >= 200 AND passes_filter AND pcent_relative_dupe <= 50)
            FROM df_all_source
        """).fetchone())
        site_counts = (
            require_counts(connection.execute("SELECT count(DISTINCT subdomain) FROM result_subdomains").fetchone())[0],
            require_counts(connection.execute("SELECT count(DISTINCT subdomain) FROM df_all_source").fetchone())[0],
            require_counts(connection.execute("""
                SELECT count(*) FROM (
                    SELECT subdomain FROM df_all_source
                    WHERE crawl_ok AND w_browser AND is_english AND n_tokens >= 200
                        AND passes_filter AND pcent_relative_dupe <= 50
                    GROUP BY subdomain
                )
            """).fetchone())[0],
            require_counts(connection.execute("""
                SELECT count(*) FROM (
                    SELECT subdomain FROM df_all_source
                    WHERE crawl_ok AND w_browser AND is_english AND n_tokens >= 200
                        AND passes_filter AND pcent_relative_dupe <= 50
                    GROUP BY subdomain HAVING count(*) >= 15
                )
            """).fetchone())[0],
        )
    with duckdb.connect(str(args.cc_database), read_only=True) as connection:
        cc_counts = require_counts(connection.execute("""
            SELECT sum(n_total), sum(n_english), sum(n_gopher_all), sum(n_kept),
                count(*), count(*) FILTER(WHERE n_english > 0),
                count(*) FILTER(WHERE n_gopher_all > 0),
                count(*) FILTER(WHERE n_kept > 0),
                count(*) FILTER(WHERE n_kept >= 15)
            FROM count_df_cache
        """).fetchone())
    cc_page_counts = cc_counts[:4]
    cc_site_counts = cc_counts[4:]
    if page_counts[0] != 4_723_161 or page_counts[-1] != 1_322_091 or site_counts != (59_046, 46_949, 38_309, 18_169):
        raise ValueError("Unexpected filtering totals")
    if cc_page_counts != (44_388_672, 40_786_889, 18_062_509, 9_105_147) or cc_site_counts != (805_268, 766_984, 543_686, 425_834, 100_309):
        raise ValueError("Unexpected Common Crawl cache totals")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    if not args.cc_pages_only:
        draw_bars(PAGE_LABELS, page_counts, "Pages", args.output_dir / "filter_pages_bing.png")
        draw_bars(SITE_LABELS, site_counts, "Sites", args.output_dir / "filter_sites_bing.png")
        draw_bars(CC_SITE_LABELS, cc_site_counts, "Sites", args.output_dir / "filter_sites_cc.png")
    # 🧑 "your slides' CC page-level stats is wrong and needs fixing"
    draw_bars(CC_PAGE_LABELS, cc_page_counts, "Pages", args.output_dir / "filter_pages_cc.png", note="English and Dolma are separate subsets of the classified-capture base.\nSeparate token/duplication stages and all-crawl denominator unavailable.")
    print("Bing pages:", *page_counts)
    print("Bing sites:", *site_counts)
    print("Common Crawl cache pages:", *cc_page_counts)
    print("Common Crawl cache sites:", *cc_site_counts)


if __name__ == "__main__":
    main()
