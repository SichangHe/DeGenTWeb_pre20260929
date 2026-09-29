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

- Hallucination?
- Plagiarism?
- Spam?
- Scam?

---

- How much of the web is MGT
    - Machine-generated text
- What are these sites doing

---

# Project DeGenTWeb

- **De**tect **Gen**erated **T**ext on the **Web**
- Or "Degenerate Web"

---

- How much of the web is MGT

<div class="mission-center">Mission impossible</div>

---

- Cannot sample whole web
- Text detectors inaccurate
- Web content noisy
- No ground truth

---

Web content noise

<div class="visual-pair"><img src="/prior/noise-example-002.png" alt="Recipe index from prior talk 3"/><img src="/prior/filter-example-002.png" alt="Privacy notice from prior talk 1"/></div>

---

Cannot tell ground truth:
- *SoTA forgeries are almost indistinguishable from “real” media* (SP 2024)
- …Unless we generated

---

# Addressing challenges

- Impossible
- → different scope but possible

---

We can still measure something useful

- Detect sites dominated by MGT
- Characterize them in bounded web samples

---

Narrow down measured target

- English prose-heavy sites
    - ~~Listings, functionality sites~~
- Text dominated by MGT
    - ~~LLM-polished~~

---

<ul class="challenge-list-plain"><li>Cannot sample whole web</li><li>Text detectors inaccurate</li><li class="active">Web content noisy</li><li>No ground truth</li></ul>

---

# Website detection pipeline

<img class="wide-figure" src="/paper/degentweb_pipeline.png" alt="Sample, download, extract, filter, score, classify"/>

---

<div class="pipeline-highlight" style="--focus-start:0%;--focus-end:15%"><img src="/paper/degentweb_pipeline.png" alt="Sampling is highlighted in the six-stage pipeline"/></div>

- Sitemap
- Wayback Machine Content Index
- Common Crawl's archive index

---

<div class="pipeline-highlight" style="--focus-start:33%;--focus-end:47%"><img src="/paper/degentweb_pipeline.png" alt="Content extraction is highlighted in the six-stage pipeline"/></div>

<div class="extract-lead"><img src="/paper/trafilatura-logo.png" alt="Trafilatura logo"/><span>(ACL 2021)</span></div>

- Reader-mode body text extraction
- Not assets, markup, or layout

---

<ul class="challenge-list-plain"><li>Cannot sample whole web</li><li>Text detectors inaccurate</li><li class="active">Web content noisy</li><li>No ground truth</li></ul>

---

<div class="pipeline-highlight" style="--focus-start:49%;--focus-end:62%"><img src="/paper/degentweb_pipeline.png" alt="Page filtering is highlighted in the six-stage pipeline"/></div>

- Long enough: ≥200 tokens
- Dolma Quality Filter
- Repeated text: ≤50% bytes

---

# Dolma Quality Filter (AI2 2024)

- Reject excessive repetition and list-like text
- Reject low linguistic quality
- Relax punctuation-line cutoff for web boilerplate

---

Aggregate pages into one site call

- ≥15 eligible pages per site
- Nine deciles of page-level Binoculars scores
- Linear SVM assigns a positive or other call

---

<ul class="challenge-list-plain"><li>Cannot sample whole web</li><li>Text detectors inaccurate</li><li>Web content noisy</li><li class="active">No ground truth</li></ul>

---

# Common Crawl (CC)

- Largest archive of the open web
- Collected regularly since 2008

---

# Negative baseline

- Common Crawl archives from 2014
    - predate modern language models
    - 10k sites
- Common practice in LLM detection

---

# AI Website builders

<div class="site-examples"><img src="/prior/wix-post-creator-original.jpg" alt="Original Wix AI Post Creator image embedded in the previous presentation"/><img src="/prior/wix-generated-example-original.jpg" alt="Original generated Wix site image embedded in the previous presentation"/></div>

---

# AI Website builders

- Generate sites with Wix.com/B12.io
- Based on descriptions of real sites
- Generate home pages and blog posts

---

Need lots of clicking

---

# Swap existing site bodies

- Retain layout/boilerplate
- OpenRouter → text → swap body
- 8 LLMs: GPT-3.5/4/OSS-120B, Haiku 4.5, Sonnet 4/4.6, Mixtral, Llama

---

<ul class="challenge-list-plain"><li>Cannot sample whole web</li><li class="active">Text detectors inaccurate</li><li>Web content noisy</li><li>No ground truth</li></ul>

---

<img class="paper-plot cdf-plot" src="/paper/cdf_new_baseline_binoculars.png" alt="Binoculars page-score distributions from five selected CC2014, five Wix, and five B12 sites; fifteen scored pages per site, not accuracy or a population estimate"/>

<div class="cdf-caption">Select baseline sites.</div>

Per-page scores vary

---

Detector comparison: new-baseline scores pending

- Compare detectors on the same Wix/CC2014 sites
- Result not ready for this talk

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

Findings in two samples

- Common Crawl archive sample
- Bing how-to search sample

---

<ul class="challenge-list-plain"><li class="active">Cannot sample whole web</li><li>Text detectors inaccurate</li><li>Web content noisy</li><li>No ground truth</li></ul>

---

Common Crawl is the largest publicly available web sample

- Still not a census of the open web
- Analyze only subdomains with ≥15 eligible pages

---

Common Crawl: who could be classified?

- 9.1m saved page rows → 8.6m scored
- 409,805 subdomains have scored pages
- 94,908 have ≥15 qualifying pages

---

Bing: who could be classified?

- 59,046 distinct search-result sites
- 18,169 have ≥15 eligible pages
- Positive rate: 15.4% of those sites

---

Bing: selected filtering stages

- 4.72m page records
- 1.34m lacked a successful browser fetch
- 995k rejected by the Dolma filter
- 1.32m retained after all filters

---

<img class="wild-plot" src="/paper/qualified_site_positive_calls.png" alt="Paper-style comparison: positive classifier calls among 94,908 qualifying Common Crawl subdomains and 18,169 qualifying Bing result sites; separate sampling frames, not web-wide prevalence"/>

---

<img class="wild-plot" src="/paper/search_queries_positive_calls.png" alt="Paper-style comparison: of 10,000 Bing how-to queries, 45.3 percent have a matched positive call in the top ten; 64.8 percent in the top twenty; unclassified results remain unknown"/>

---

Some archived pages shift in score

- 1,486 / 26,414 sites meet the archive-date shift criterion
- 234 expected under within-site date shuffling
- Suggestive of adoption; not a causal test

---

<img class="temporal-plot" src="/paper/transition_3site.png" alt="Paper examples of page-score shifts over modification dates; this figure does not prove LLM adoption"/>

<div class="visual-caption">Illustrative page-score shifts · timing alone does not prove adoption</div>

---

Bing ranks within matched queries

- 6,474 queries contain both classified groups
- Positive sites rank 2 positions later on average
- Topic differences prevent a ranking-policy claim

---

What do selected site groups contain?

<img class="category-figure" src="/paper/llm_site_kinds_incentive_coarse_combined_1col.png" alt="Draft category comparison in selected, equal-sized groups"/>

<div class="visual-caption">Equal-sized comparison groups · not the web's category mix</div>

---

<img class="wild-plot" src="/paper/selected_cc_financial_incentive.png" alt="Paper-style comparison: clear-financial-incentive category proxy in selected equal-size positive and other-call Common Crawl site groups, not actual site motivations"/>

---

Engagement tools are less common

- Positive group: 2.6% use audience-building tools
- Other group: 6.0%
- Selected sites; tools are proxies for strategy

---

What this work contributes

- Site-level detection after page filtering
- Generated-site baseline and held-out checks
- Positive rates and site types in two samples

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

---

<img class="method-plot" src="/paper/cc2014_site_attrition.png" alt="Among 10,000 archived 2014 sites, 2,917 reach classification after extraction and page filters"/>

---

Missing extractions ≠ negative labels

- 10,000 archived sites; 15 source pages each
- 2,776 sites lack 15 processed extractions
- Processing gap, not proven ineligibility
