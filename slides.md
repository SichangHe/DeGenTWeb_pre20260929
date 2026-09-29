---
theme: default
title: DeGenTWeb — Tuesday discussion
fonts:
  sans: Inter
transition: slide-left
layout: cover
class: text-center
---

# DeGenTWeb: A First Look at MGT-dominant Websites

---

<div class="news-pair"><img src="/prior/news-wired.jpg" alt="WIRED headline: AI Slop Is Flooding Medium"/><img src="/prior/news-rolling-stone.jpg" alt="Rolling Stone headline: Facebook’s AI-Generated Spam Problem Is Worse Than You Realize"/></div>

<img class="news-feature" src="/prior/news-mit-tech-review.jpg" alt="MIT Technology Review headline: Junk websites filled with AI-generated text are pulling in money from programmatic ads"/>

---

<v-clicks>

- Hallucination?
- Plagiarism?
- Misinformation?

</v-clicks>

---

Which page is generated?

<div class="site-examples"><img src="/prior/example-a-original.jpg" alt="Original embedded website capture A from the prior talk: a health article"/><img src="/prior/example-b-original.jpg" alt="Original embedded website capture B from the prior talk: an article about snow blowers"/></div>

<div class="visual-caption">Original page images from prior talk 3 · authorship unknown</div>

---

- How much of the web is MGT
    - Machine-generated text
- What are these sites doing

---

- How much of the web is MGT
    - Machine-generated text
- Mission impossible

---

<v-clicks>

- Text detectors inaccurate
- Web content noisy
- No ground truth
- Cannot sample whole web

</v-clicks>

---

# Page noise

<div class="visual-pair"><img src="/prior/noise-example-002.png" alt="Recipe index from prior talk 3"/><img src="/prior/filter-example-002.png" alt="Privacy notice from prior talk 1"/></div>

---

- Cannot tell ground truth
- *SoTA forgeries are almost indistinguishable from “real” media* (Frank, SP2024)

---

Narrow down measured target

- English prose-heavy sites
    - ignore non-prose
- Text dominated by MGT
    - ignore LLM-polished

---

What we contribute

- Filter noisy pages and aggregate site scores
- Check generated builders against historical controls
- Measure two bounded samples of websites

---

# Six-stage pipeline

<img class="wide-figure" src="/paper/degentweb_pipeline.png" alt="Sample, download, extract, filter, score, classify"/>

---

Sample pages

<div class="pipeline-highlight" style="--focus-start:0%;--focus-end:15%"><img src="/paper/degentweb_pipeline.png" alt="Sampling is highlighted in the six-stage pipeline"/></div>

- Site sitemap
- Wayback Machine index
- Common Crawl's archive index

---

Extract main text

<div class="pipeline-highlight" style="--focus-start:32%;--focus-end:45%"><img src="/paper/degentweb_pipeline.png" alt="Content extraction is highlighted in the six-stage pipeline"/></div>

- Trafilatura: reader-mode prose
- Not images, code, video, or layout

---

Filter page noise

<div class="pipeline-highlight" style="--focus-start:49%;--focus-end:62%"><img src="/paper/degentweb_pipeline.png" alt="Page filtering is highlighted in the six-stage pipeline"/></div>

- Remove poor-quality and repeated text
- Abstain if fewer than 15 pages survive

---

Which pages count?

<v-clicks>

- Extracted English prose: ≥200 tokens
- Dolma text-quality filter
- Repeated text: ≤50% of extracted bytes
- ≥15 eligible pages per site

</v-clicks>

---

No label ≠ negative label

<img class="method-plot" src="/paper/cc2014_site_attrition.png" alt="Among 10,000 archived CC2014 sites with 15 source pages, 2,917 reached classification; other processing and page filters abstain"/>

<div class="visual-caption">2014 cohort · missing extractions do not prove ineligible source text</div>

---

We need a labeled baseline

- Generate Wix sites from company topics
- Generate B12 sites from personal-blog topics
- Hold out entire generated sites for evaluation

---

Build whole generated sites

<div class="site-examples"><img src="/prior/wix-post-creator-original.jpg" alt="Original Wix AI Post Creator embedded image from the prior talk"/><img src="/prior/wix-generated-example-original.jpg" alt="Original embedded image of the Joint Journey generated Wix site from the prior talk"/></div>

<div class="visual-caption">Original Wix UI and generated-site images · prior talk 3</div>

---

Body swaps test new layouts

- Keep original templates
- Replace article prose with generated text
- Test new layouts, not a new builder

---

Historical controls are proxies

- CC2014 pages predate modern public LLMs
- Their individual authorship is not verified
- A positive site call is a **proxy** false positive

---

One page is not enough

<img class="paper-plot cdf-plot" src="/paper/cdf_baseline_svm_scores.png" alt="Overlapping page-score distributions across selected baseline site types"/>

<div class="visual-caption">Overlapping page scores → aggregate at the site level</div>

---

Why aggregate page scores?

- Earlier 144-site baseline: 92.8% best page accuracy
- 100% mean site accuracy on that baseline
- Not a substitute for held-out builder tests

---

Site-level decision

- Binoculars scores each retained page
- Nine score deciles summarize the site
- A linear SVM assigns the site call

---

Detector-comparison chart: awaiting new-baseline scores

- Older 144-site comparison is **not** new-baseline validation
- No matched multi-detector scores for the new Wix/CC2014 cohort yet

---

Do more detector scores help?

- Current: Binoculars score deciles
- Next: combined detector scores
- Same held-out sites; result pending

---

Held-out generated sites

<div class="bar-study"><div><strong>Wix</strong><span class="bar-track"><i style="width:82%"></i></span><b>41/50 · 82%</b></div><div><strong>B12</strong><span class="bar-track"><i class="second" style="width:87.2%"></i></span><b>34/39 · 87% median</b></div></div>

- Wix: same builder
- B12: new builder and site type

---

Body swaps test new layouts

- 1,142 / 1,172 detected, median over fixed runs
- 97.4% for sampled layouts and generation models

---

Historical-site proxy FPR

- 40 positive calls / 40,000 held-out CC2014 decisions
- 0.1% **proxy** false-positive rate
- CC2014 labels do not verify human authorship

---

CC2014 calls across repeated classifier fits

- htmlbible.com: positive in 1 / 3 fits
- jeeps-for-sale.net: positive in 4 / 5 fits
- lawnmowersforsale.net: positive in 4 / 5 fits

<div class="visual-caption">Historical labels are proxies; authorship unverified</div>

---

Why might old pages look generated?

- Repeated templates and formulaic prose
- Falcon-7B may have learned similar web text
- **Memorization was not tested**

---

Polished text is a different task

- 327 / 328 polished sites not flagged
- This is not a test of fully generated sites

---

<img class="paper-plot" src="/paper/body_swap_transfer_and_size_errors_split_1to1.png" alt="Paper figure: site-classifier transfer and training-size sensitivity across Wix, B12, body-swap, and CC2014 sites"/>

<div class="visual-caption">Training-size and transfer study · held-out builder and CC2014 sites</div>

---

<img class="paper-plot" src="/paper/fixed_training_vary_test_errors.png" alt="Separate test-size study: observed body-swap misses and historically negative-labeled Common Crawl positive calls, sampled at varying held-out test sizes for five fixed classifiers"/>

<div class="visual-caption">Other cohort · 30 resamples · observed 5–95% range, not confidence intervals · 2014 authorship unverified</div>

---

Wild-site calls remain uncalibrated

- Later evaluation used a different fit
- Stored wild-run history does not match it
- Calls are not verified accuracy

---

Newer models expose detector limits

<img class="paper-plot" src="/paper/pangram_vs_binoculars.png" alt="Paper figure: Pangram AI percentage versus Binoculars score for 605 selected generated replacement texts"/>

---

The detector matters

- Binoculars max-F1: 470 / 605 selected generated texts flagged
- Pangram: 594 / 605 returned AI labels
- Selected positives cannot compare matched false-positive rates

---

Findings in the wild

- Common Crawl archive sample
- Bing how-to search sample
- Neither is a whole-web census

---

Common Crawl: count who could be classified

- 409,805 retained subdomains, 2020–May 2025
- 94,908 have ≥15 qualifying pages
- The rest receive no site call

---

Bing: count who could be classified

- 59,046 distinct search-result sites
- 18,169 have enough eligible pages
- 15.4% positive calls **among the qualifying sites**

---

<img class="wild-plot" src="/paper/qualified_site_positive_calls.png" alt="Paper-style comparison: positive classifier calls among 94,908 qualifying Common Crawl subdomains and 18,169 qualifying Bing result sites; separate sampling frames, not web-wide prevalence"/>

---

<img class="wild-plot" src="/paper/search_queries_positive_calls.png" alt="Paper-style comparison: of 10,000 Bing how-to queries, 45.3 percent have a matched positive call in the top ten; 64.8 percent in the top twenty; unclassified results remain unknown"/>

---

Some archived pages shift in score

- 1,486 / 26,414 sites meet the archive-date shift criterion
- 234 expected under within-site date shuffling
- Genre and selection limit the interpretation

---

<img class="temporal-plot" src="/paper/transition_3site.png" alt="Paper examples of page-score shifts over modification dates; this figure does not prove LLM adoption"/>

<div class="visual-caption">Illustrative modification-date curves · shifts do not prove LLM adoption</div>

---

What do selected site groups contain?

<img class="category-figure" src="/paper/llm_site_kinds_incentive_coarse_combined_1col.png" alt="Draft category comparison in selected, equal-sized groups"/>

<div class="visual-caption">Equal-sized comparison groups · not the web's category mix</div>

---

<img class="wild-plot" src="/paper/selected_cc_financial_incentive.png" alt="Paper-style comparison: clear-financial-incentive category proxy in selected equal-size positive and other-call Common Crawl site groups, not actual site motivations"/>

---

What this work contributes

- Filter noisy pages
- Aggregate scores across each site
- Test builders and historical proxies
- Study two bounded wild-site samples
- Not whole-web prevalence

---

Backup: builder design

- Wix: company topics, generated names and blog prompts
- B12: personal-blog topics, separate builder
- Body swaps: real layouts with generated article bodies

---

Backup: denominator details

- CC: 409,805 retained; 94,908 qualified
- Bing: 59,046 result sites; 18,169 qualified
- Top-ten calls: 4,532 / 10,000 matched queries
