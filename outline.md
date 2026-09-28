# Tuesday talk: separate outline

(authored by agents unless marked 🧑)

Public GitHub Pages build: `https://sichanghe.github.io/DeGenTWeb_pre20260929/`. Main story: slides 1–10; curated archive and draft-paper figure gallery follows. White background, large body and source text, author/page footer. PNG resources are in `public/prior/` and `public/paper/`; gallery items with old numbers are historical illustrations only.

Core: estimate the positive-call share of *qualifying observed sites* whose extractable prose appears MGT-dominant (MGT = machine-generated text); characterize those sites. This is not a census of the whole web or verified ground truth.

1. Scope: two selected frames, article-heavy qualifying subdomains, extractable prose, site-level decisions.
2. Challenge: templates and boilerplate create false signals; detection errors matter when positives are rare.
3. Method: sample → crawl → extract/filter → score pages → classify sites at fixed thresholds.
4. Result: retained 2020–25 Common Crawl records versus top-20 Bing results for 10,000 WikiHow-title queries; distinguish sampled, eligible, and positive-call denominators.
5. Characterize detected sites: draft manuscript category comparison figure (service/SaaS, personal/organizational, financial-incentive proxy) on selected, equal-sized groups; label provisional pending audit.
6. Validation: human proxy negatives, generated sites, coverage and false positives; matched Pangram comparison. Older positive-call shares cannot be calibrated directly with the expanded evaluation because the classifier lineage is unproven.
7. Takeaway: an estimate conditional on the observed, qualifying cohort; excluded sites remain unknown.

Sources: the three previous Google Slides in `manager_mail/85c5dff58359-2184.txt:9-11` (PDF exports consulted); extracted screenshots and curated PDF slide images are in `public/prior/`. Paper-draft figure PNGs are in `public/paper/` and render from the PDFs in `dw-learning-curve-paper/figures/dw1/` and `dw-learning-curve-paper/degentweb_pipeline.pdf`. The author/page footer is adapted from `CSci656/presentation/components/Footer.vue`. Numeric claims remain provisional; central validation is still a marked placeholder.

ChatGPT review/revise pass (September 28): the browser reviewer recommended “Make the estimand explicit before showing the 6.0% / 15.4% numbers,” “Separate ‘measurement result’ from ‘validation status’ more visually,” and “Soften the category interpretation” (`/tmp/tuesday-slidev-final-review-medium.txt`). Slides 6–9 now make the denominators, uncalibrated classifier outputs, and selected characterization groups explicit.
