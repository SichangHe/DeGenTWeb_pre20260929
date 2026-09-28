# Tuesday talk: separate outline

(authored by agents unless marked 🧑)

Public GitHub Pages build: `https://sichanghe.github.io/DeGenTWeb_pre20260929/`. The 15 slides follow the active `origin/master` paper revision (September 28, 2026): all six active figures appear in manuscript order, with no figures from deleted or hidden content. White background, large body and source text, small author/page footer. The three original-resolution article screenshots embedded in the first prior deck's slide 5 were extracted individually to `public/prior/news-*.jpg`; these are not captures of rendered Google Slides pages.

Core: estimate the positive-call share of *qualifying observed sites* whose extractable prose appears MGT-dominant (MGT = machine-generated text); characterize those sites. This is not a census of the whole web or verified ground truth.

1. Introduction: the full paper title; the three original article screenshots on one slide; distinguish news claims from measured evidence.
2. Scope: article-heavy qualifying subdomains, extractable prose, site-level decisions; two nonrepresentative sampling frames.
3. Detection: page noise, six-stage pipeline, at least 15 usable pages per site.
4. Evaluation and limits: the manuscript reports held-out generated-site tests and CC2014 proxy-negative results, then the training/transfer, baseline score-distribution, and Pangram-versus-Binoculars figures. Old positive-call shares cannot be calibrated directly using the newer evaluation because classifier lineage is not established.
5. Findings: 409,805 retained Common Crawl subdomains, 94,908 qualifying; 6.0% positive calls. WikiHow-style Bing frame: 18,169 qualifying and 15.4% positive calls. The paper's transition example follows these two frames. These are not whole-web prevalence estimates.
6. Characteristics: draft category comparison on selected equal-sized groups; this does not establish motives or general web-wide composition. Linked-site material and other omitted figures are not slides.
7. Takeaway: estimates conditional on the observed, qualifying cohorts; excluded sites remain unknown.

Sources: `dw-learning-curve-paper` branch `origin/master` at `0fa2603` defines the current title, sections, and exactly six visible figures; the local `main` checkout is 31 commits behind and was not used for figure selection. The three prior Google Slides appear in `manager_mail/85c5dff58359-2184.txt:9-11`; their news article JPGs are original embedded images extracted from the first deck's PDF, not screenshots of its slides. All six active figure PNGs were rendered directly from that paper revision's PDFs. The footer adapts `CSci656/presentation/components/Footer.vue`. Numeric claims remain provisional; central calibration of older wild shares is unavailable.

ChatGPT review/revise pass (September 28): the browser reviewer recommended “Make the estimand explicit before showing the 6.0% / 15.4% numbers,” “Separate ‘measurement result’ from ‘validation status’ more visually,” and “Soften the category interpretation” (`/tmp/tuesday-slidev-final-review-medium.txt`). Slides 7–10 now make the denominators, uncalibrated classifier outputs, and selected characterization groups explicit.
