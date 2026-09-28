# Tuesday talk: separate outline

Core: estimate the positive-call share of *qualifying observed sites* whose extractable prose appears MGT-dominant (MGT = machine-generated text); characterize those sites. This is not a census of the whole web or verified ground truth.

1. Scope: two selected frames, article-heavy qualifying subdomains, extractable prose, site-level decisions.
2. Challenge: templates and boilerplate create false signals; detection errors matter when positives are rare.
3. Method: sample → crawl → extract/filter → score pages → classify sites at fixed thresholds.
4. Result: retained 2020–25 Common Crawl records versus top-20 Bing results for 10,000 WikiHow-title queries; distinguish sampled, eligible, and positive-call denominators.
5. Characterize detected sites: draft manuscript category comparison figure (service/SaaS, personal/organizational, financial-incentive proxy) on selected, equal-sized groups; label provisional pending audit.
6. Validation: human proxy negatives, generated sites, coverage and false positives; matched Pangram comparison. Older positive-call shares cannot be calibrated directly with the expanded evaluation because the classifier lineage is unproven.
7. Takeaway: an estimate conditional on the observed, qualifying cohort; excluded sites remain unknown.

Sources: the three previous Google Slides in `manager_mail/85c5dff58359-2184.txt:9-11` (PDF exports consulted); extracted figures in `public/prior/` include presentation 1 slide 15's privacy-notice screenshot, presentation 2 slide 18's historical score-distribution chart, and presentation 3 slide 16's recipe-index screenshot. The six-stage pipeline and footer come from `/ssd1/sichangheagent/CSci656/presentation/`. The category chart is rendered from the current draft manuscript `/ssd1/sichangheagent/dw-learning-curve-paper/figures/dw1/llm_site_kinds_incentive_coarse_combined_1col.pdf`; draft text `/ssd1/sichangheagent/dw-learning-curve-paper/sections/{abstract,wild,method,incentives,limitations}.tex`. Numeric claims remain provisional. Placeholders are for this preview, not final presentation slides.

ChatGPT review/revise pass (September 28): the browser reviewer recommended “Make the estimand explicit before showing the 6.0% / 15.4% numbers,” “Separate ‘measurement result’ from ‘validation status’ more visually,” and “Soften the category interpretation” (`/tmp/tuesday-slidev-final-review-medium.txt`). Slides 6–9 now make the denominators, uncalibrated classifier outputs, and selected characterization groups explicit.
