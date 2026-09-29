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

Cannot sample whole web

- Limited budget

---

Text detectors inaccurate

- On RAID (ACL 2024), Binoculars catches 70% at 1% false positives

---

Web content noisy

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

<ul class="challenge-list-plain"><li>Cannot sample whole web</li><li>Text detectors inaccurate</li><li>Web content noisy</li><li class="active">No ground truth</li></ul>

---

# Common Crawl (CC)

- Largest public archive of open web
- Regularly since 2008

---

# Negative baseline

- 2014 Common Crawl (CC) archives
    - predate modern language models
    - 10k sites
- Common practice in LLM detection

---

# AI Website builders

<div class="site-examples"><img src="/prior/wix-post-creator-original.jpg" alt="Original Wix AI Post Creator image embedded in the previous presentation"/><img src="/prior/wix-generated-example-original.jpg" alt="Original generated Wix site image embedded in the previous presentation"/></div>

---

# AI Website builders

- nn Wix.com + nn B12.io
- From descriptions of real sites
- Home pages + blog posts
- Lots of clicking

---

# Swap existing site bodies

- Retain layout/boilerplate
- Summarize → expand → swap
- 1,172 sites

---

# Diverse body-swap sites

- 8 LLMs: GPT-3.5/4/OSS-120B, Haiku 4.5, Sonnet 4/4.6, Mixtral, Llama

---

<ul class="challenge-list-plain"><li>Cannot sample whole web</li><li class="active">Text detectors inaccurate</li><li class="active">Web content noisy</li><li>No ground truth</li></ul>

---

# Website detection pipeline

<img class="wide-figure" style="margin-top: -2em;margin-bottom: -2em;" src="/paper/degentweb_pipeline.png" alt="Sample, download, extract, filter, score, classify"/>

- Filter & aggregate signal
- Accurate site-level classification

---

<div class="pipeline-highlight" style="--focus-start:0%;--focus-end:15%"><img src="/paper/degentweb_pipeline.png" alt="Sampling is highlighted in the six-stage pipeline"/></div>

- Sitemap
- Wayback Machine Content Index
- Common Crawl's archive index

---

<ul class="challenge-list-plain"><li>Cannot sample whole web</li><li>Text detectors inaccurate</li><li class="active">Web content noisy</li><li>No ground truth</li></ul>

---

<div class="pipeline-highlight" style="--focus-start:33%;--focus-end:47%"><img src="/paper/degentweb_pipeline.png" alt="Content extraction is highlighted in the six-stage pipeline"/></div>

<div class="extract-lead"><img src="/paper/trafilatura-logo.png" alt="Trafilatura logo"/><span>(ACL 2021)</span></div>

- Reader-mode body text extraction
- No asset, markup, layout

---

<pre class="extraction-quote">Capital: Andorra la Vella
Population: 84000
Area (km2): 468.0

Population: 84000
Area (km2): 468.0
Capital: Abu Dhabi
Population: 4975593
Area (km2): 82880.0</pre>

<div class="cdf-caption">Trafilatura · <a href="https://www.scrapethissite.com/pages/simple/">Scrape This Site: country listing</a></div>

---

⇒ Narrow down target

- English prose-heavy pages
    - ~~Listings, functionality pages~~

---

<div class="pipeline-highlight" style="--focus-start:49%;--focus-end:62%"><img src="/paper/degentweb_pipeline.png" alt="Page filtering is highlighted in the six-stage pipeline"/></div>

- Long enough: ≥200 tokens
- Repeated text: ≤50% bytes
- Dolma Quality Filter

---

# Dolma Quality Filter (AI2 2024)

- 50–100,000 words; median word 3–10 characters
- Symbols ≤10%; alphabetic words ≥80%
- ≥2 common English words
- Punctuation cleaning first; not a rejection rule

---

# Dolma: reject repetitive text

- Frequent 2–4 grams: ≤20%, 18%, 16%
- Repeated 5–10 grams: ≤15% to 10%
- Bulleted lines ≤90%; ellipsis lines ≤30%
- Duplicate lines and their characters ≤30%

---

<ul class="challenge-list-plain"><li>Cannot sample whole web</li><li class="active">Text detectors inaccurate</li><li>Web content noisy</li><li>No ground truth</li></ul>

---

<div class="detector-heading"><img src="/prior/binoculars-logo.svg" alt="Binoculars project logo"/><h1>Binoculars (ICML 2024)</h1></div>

- Base ⨁ instruct LLM probabilities
- Low false positive rate
- ~~LLM-polished~~
- Can be replaced

---

- <br>
- <br>

<img class="paper-plot cdf-plot" src="/paper/cdf_new_baseline_binoculars.png" alt="Binoculars page-score distributions from five selected CC2014, five Wix, and five B12 sites; fifteen scored pages per site, not accuracy or a population estimate"/>

<div class="cdf-caption">Select baseline sites.</div>

---

- Page scores overlap
- Site-wide distributions consistent

<img class="paper-plot cdf-plot" src="/paper/cdf_new_baseline_binoculars.png" alt="Binoculars page-score distributions from five selected CC2014, five Wix, and five B12 sites; fifteen scored pages per site, not accuracy or a population estimate"/>

<div class="cdf-caption">Select baseline sites.</div>

---

- Page scores overlap
- Site-wide distributions consistent

⇒ Detect MGT-dominant sites

---

<img class="paper-plot method-pipeline" src="/paper/degentweb_pipeline.png" alt="Page scoring and site classification in the detection pipeline"/>

- Require ≥15 qualified pages per site
- 9 deciles of page Binoculars scores
- Linear support vector machine (SVM)

---

# Methods Eval

- 1,172 body-swap + 10k CC2014
- In-domain: 1:1 train-test split
- Out-of-domain: 39 B12 + 50 Wix

---

In-domain

<img class="method-plot todo-plot" src="/paper/todo_training_size_errors.png" alt="Training-size sensitivity: positive calls among historical negative-labeled sites and misses among generated body-swap sites"/>

- <0.2% FPR
- More training → not help

---

Out-of-domain

<img class="method-plot todo-plot" src="/paper/todo_out_of_domain_transfer.png" alt="Missed generated Wix and B12 sites over thirty classifier fits"/>

- Generalizes to different data

---

In-domain

<img class="method-plot todo-plot" src="/paper/todo_test_size_errors.png" alt="Varying test size with a fixed classifier, showing body-swap misses and positive calls among historical negative-labeled sites"/>

- More test data → not worse

---

Why old sites positive?

- Repeated templates and formulaic prose
- Binoculars memorization

---

# ~~LLM-polished sites~~

- Not "MGT-dominant"
- 327/328 negative

---

# Accuracy-cost tradeoff

- Binoculars worse on newer LLMs
- Could replace detector
- E.g. <img class="detector-inline-logo" src="/prior/pangram-logo.svg" alt="Pangram"/>

---

- 605 Claude texts, varying scores
- Binoculars max-F1: 470 positive
- Pangram: 594 positive
    - Also better FPR; both low
    - Costly: \$50 for above

---

# Findings in the wild

- Common Crawl archive
- Bing how-to search

---

<!-- TODO: Give a proper breakdown like we did before: no English text, too short, fail Dolma filter, fail duplication, etc. Could be page level -->
- Crawled 409,805 Common Crawl
- 94,908 have ≥15 qualified pages

---

Common Crawl: 6.0% MGT-dominant

<!-- Don't use " / ", use "/" -->
- 5,643/94,908 qualifying subdomains

---

<!-- TODO: Make the axis texts 2x large. Follow font sizes used in the paper plots in general. Make the gap in between small. x axis should say "% Sites classified as MGT-dominant". -->
<img class="wild-plot" src="/paper/qualified_site_positive_calls_clean.png" alt="Positive classifier calls: 6.0% of qualifying Common Crawl sites, 15.4% of qualifying Bing search-result sites"/>

---

<!-- TODO: Seems to be missing many slides regarding growth trend etc. -->

<!-- TODO: What's the shifting criterion? -->
<!-- I think we drop these entirely -->
<!-- Some archived sites shift in score

- 1,486/26,414 sites meet the shift criterion
- 234 expected after shuffling capture dates -->

---

<!-- <img class="temporal-plot" src="/paper/transition_3site.png" alt="Paper examples of page-score shifts over modification dates"/> -->

---

<!-- TODO: Also do a proper breakdown here, including how many were unreachable -->
Bing result sites: 15.4% positive

- 18,169 sites with ≥15 eligible pages

---

<img class="wild-plot" src="/paper/search_queries_positive_calls.png" alt="Among 10,000 Bing how-to queries, 45.3% have a matched positive call in the top ten and 64.8% in the top twenty"/>

---

Within the same searches

- 6,474 queries contain both site groups
- Positive sites rank two positions later on average

---

# Site classification

TODO: a slide on how we do it with GPT-OSS-120B

<img class="category-figure" src="/paper/llm_site_kinds_incentive_coarse_combined_1col.png" alt="Draft category comparison in selected, equal-sized groups"/>

---

In selected CC groups: financial incentive

- 78.8% of flagged sites
- 55.8% of the comparison group

---

Takeaways

- Detect across pages, not from a single page
- Quantify positives in two web samples
- Compare what the flagged sites do

---

Backup: builder design

- Wix: company topics, generated names and blog prompts
- B12: personal-blog topics, separate builder
- Body swaps: real layouts with generated article bodies

---

Training-size sensitivity

<img class="paper-plot" src="/paper/fixed_test_vary_training_errors.png" alt="Paper training-size study with a fixed balanced test set"/>

---

Test-size sensitivity

<img class="paper-plot" src="/paper/fixed_training_vary_test_errors.png" alt="Separate paper test-size study with five fixed classifiers"/>

---

Backup: denominator details

- CC: 409,805 retained; 94,908 qualified
- Bing: 59,046 result sites; 18,169 qualified
- Top-ten calls: 4,532/10,000 matched queries

---

<img class="method-plot" src="/paper/cc2014_site_attrition.png" alt="Among 10,000 archived 2014 sites, 2,917 reach classification after extraction and page filters"/>
