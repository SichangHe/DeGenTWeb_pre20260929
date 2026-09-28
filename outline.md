# Tuesday talk: separate outline

(authored by agents unless marked 🧑)

Public GitHub Pages build: `https://sichanghe.github.io/DeGenTWeb_pre20260929/`. The 11 slides follow the current paper; no appendix or extra plots. White background, large body and source text, small author/page footer. The three original-resolution article screenshots embedded in the first prior deck's slide 5 were extracted individually to `public/prior/news-*.jpg`; these are not captures of rendered Google Slides pages.

Core: estimate the positive-call share of *qualifying observed sites* whose extractable prose appears MGT-dominant (MGT = machine-generated text); characterize those sites. This is not a census of the whole web or verified ground truth.

1. Introduction: the full paper title; the three original article screenshots on one slide; distinguish news claims from measured evidence.
2. Scope: article-heavy qualifying subdomains, extractable prose, site-level decisions; two nonrepresentative sampling frames.
3. Detection: page noise, six-stage pipeline, at least 15 usable pages per site.
4. Evaluation and limits: the manuscript reports held-out generated-site tests and CC2014 proxy-negative results, but old positive-call shares cannot be calibrated directly using the newer evaluation because classifier lineage is not established.
5. Findings: 409,805 retained Common Crawl subdomains, 94,908 qualifying; 6.0% positive calls. WikiHow-style Bing frame: 18,169 qualifying and 15.4% positive calls. These are not whole-web prevalence estimates.
6. Characteristics: draft category comparison on selected equal-sized groups; this does not establish motives or general web-wide composition. Linked-site material and other omitted figures are not slides.
7. Takeaway: estimates conditional on the observed, qualifying cohorts; excluded sites remain unknown.

Sources: the current `dw-learning-curve-paper/degentweb_thewebconf2027.tex` and its `sections/` define title and sequence; prior Google Slides are in `manager_mail/85c5dff58359-2184.txt:9-11` (PDF exports consulted). The news article JPGs are original embedded images extracted from that first deck's PDF, not screenshots of its slides. The pipeline and category PNGs derive from the active draft paper. The footer adapts `CSci656/presentation/components/Footer.vue`. Numeric claims remain provisional; central calibration of the older wild shares is unavailable.

ChatGPT review/revise pass (September 28): the browser reviewer recommended “Make the estimand explicit before showing the 6.0% / 15.4% numbers,” “Separate ‘measurement result’ from ‘validation status’ more visually,” and “Soften the category interpretation” (`/tmp/tuesday-slidev-final-review-medium.txt`). Slides 7–10 now make the denominators, uncalibrated classifier outputs, and selected characterization groups explicit.
