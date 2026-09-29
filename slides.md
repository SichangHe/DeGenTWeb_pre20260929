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

- 48 Wix.com + 39 B12.io
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

Problem

<pre class="extraction-quote">Capital: Andorra la Vella
Population: 84000
Area (km2): 468.0

Population: 84000
Area (km2): 468.0
Capital: Abu Dhabi
Population: 4975593
Area (km2): 82880.0</pre>

<div class="cdf-caption">https://www.scrapethissite.com/pages/simple/</div>

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
- Out-of-domain: 39 B12 + 48 Wix

---

In-domain: low false-positive rate

<img class="method-plot todo-plot" src="/paper/todo_training_size_errors.png" alt="False-positive and false-negative rates across training-set sizes"/>

---

Out-of-domain: generalizes

<img class="method-plot todo-plot" src="/paper/todo_out_of_domain_transfer.png" alt="False-negative rates on Wix and B12 sites across thirty fits"/>

---

In-domain: test-size sensitivity

<img class="method-plot todo-plot" src="/paper/todo_test_size_errors.png" alt="False-negative and false-positive rates across test-set sizes with a fixed classifier"/>

---

Why old sites positive?

- Repeated templates
- Formulaic prose
- Binoculars memorization

---

# ~~LLM-polished sites~~

- Not "MGT-dominant"
- 327/328 negative

---

# Accuracy-cost tradeoff

- Binoculars worse on newer LLMs
- Could replace detector
- E.g. <img class="detector-inline-logo" style="margin-left: -2em" src="/prior/pangram-logo.svg" alt="Pangram"/>

---

- 605 Claude texts, varying scores
    - Binoculars max-F1: 77.7% positive
    - Pangram: 98.2% positive
- Also better FPR; both low
- Costly: \$50 for above

---

# Findings in the wild

- Common Crawl archive
    - Jan 2020 ~ May 2025
- Bing how-to search
    - 10k WikiHow, 2025

---

Common Crawl: page filtering

<!-- TODO: This plot is wrong. Should match Bing's -->
<img class="filter-plot" src="/paper/filter_pages_cc.png" alt="Common Crawl saved filtered pages: 9,107,806 stored, 8,605,649 with valid scores, 7,440,696 on qualifying sites"/>

---

Common Crawl: qualifying sites

<!-- TODO: This plot is wrong. Should match Bing's except not have search result sites and instead do "Total crawled" in place of "Has saved pages" -->
<img class="filter-plot" src="/paper/filter_sites_cc.png" alt="Common Crawl sites: 425,941 in saved source, 409,805 with scored pages, 94,908 with at least 15 scored pages"/>

---

Bing: page filtering

<!-- TODO: Instead of "English text", use "English body". Same for other plots -->
<img class="filter-plot" src="/paper/filter_pages_bing.png" alt="Cumulative Bing page records: 4,723,161 saved crawl records, 2,829,286 with English text, 1,668,750 with at least 200 tokens, 1,479,112 passing Dolma, 1,322,091 passing the repetition filter"/>

---

Bing: qualifying sites

<img class="filter-plot" src="/paper/filter_sites_bing.png" alt="Bing search-result sites: 59,046 candidates, 46,949 with saved pages, 38,309 with an eligible page, 18,169 with at least 15 eligible pages"/>

---

<img class="wild-plot" src="/paper/qualified_site_positive_calls_clean.png" alt="Sites classified as MGT-dominant: 6.0% in Common Crawl, 15.4% in Bing search results"/>

---

TODO: Prevalence vs half-year curve for CC from paper

---

<!-- Let's not talk about these -->
<!-- Do archived page scores shift?

- ≥4 captured pages before and after ChatGPT
- Post-launch upper quartile below pre-launch lower quartile

---

1,486/26,414 sites shift

- 234 mean after 200 within-site date shuffles

--- -->

Prevalent in Bing search

<img class="wild-plot" style="margin-top: -1em" src="/paper/search_queries_positive_calls.png" alt="Among 10,000 Bing how-to queries, 45.3% have an MGT-dominant site in the top ten and 64.8% in the top twenty"/>

---

# Mean search ranks

- MGT-dominant: 11.7
- Non-: 11.2

---

# Site classification

- GPT-OSS-120B
- Up to 5 sampled pages per site
- Page text and metadata

---

Site signals

- Wappalyzer: technologies
- EasyList: ads
- Link patterns: affiliates

---

Compare equally sized site groups

- CC: 3,366 MGT-dominant; 3,366 comparison
- Bing: 2,393 MGT-dominant; 2,393 comparison

---

<!-- TODO: The only thing that should have changed was the "LLM-" revert all other changes of this plot -->
<img class="category-figure" src="/paper/llm_site_kinds_incentive_coarse_combined_1col.png" alt="Draft category comparison in selected, equal-sized groups"/>

---

In selected CC groups: financial incentive

- 78.8% of flagged sites
- 55.8% of the comparison group

---

Site types differ in Common Crawl

- More service and SaaS sites in the MGT-dominant group
- Fewer personal and organizational sites

---

In Bing, the financial-incentive split narrows

- 76.2% of MGT-dominant sites
- 71.0% of comparison sites

---

Bing sites: ad platforms

- AdSense: 26.6% versus 17.1%
- Ezoic: 8.5% versus 2.4%
- Raptive: 4.1% versus 13.2%

---

Audience-building tools

- 2.6% of MGT-dominant sites
- 6.0% of comparison sites

---

Shared revenue identifiers

- 215 sites share 75 IDs across domains
- Largest shared AdSense group: 18 MGT-dominant sites

---

Similar sites, shared technology

- 31 MGT-dominant editorial sites with similar designs
- Shared Gatsby query fingerprints

---

- Low-FPR MGT detection at *site-level*
- Large, diverse MGT site baseline
- Rising prevalence in Common Crawl
- High prevalence in Bing search
- High incentive, low effort

---

# Appendix

---

Builder prompt → ChatGPT 4o

> Give a one-paragraph summary description of what content "[website domain name]" website has, without mentioning its name.

---

Builder prompt → ChatGPT 4o

> Come up with a suiting name for a similar website. Suggest 30 diverse and suiting blog posts for this website.

---

Body swap: factual brief

> Summarize the source text as a compact factual brief for a separate writer. List its topic, claims, named entities, dates, numbers, and important relationships.

---

Body swap: new article

> Write a detailed standalone web-page main body from the factual brief below. The source text is unavailable: use only the brief, and do not imply that you saw or are rewriting another text.

---

Training-size sensitivity

<img class="paper-plot" src="/paper/fixed_test_vary_training_errors.png" alt="Paper training-size study with a fixed balanced test set"/>

---

Test-size sensitivity

<img class="paper-plot" src="/paper/fixed_training_vary_test_errors.png" alt="Separate paper test-size study with five fixed classifiers"/>

---

<img class="method-plot" src="/paper/cc2014_site_attrition.png" alt="Among 10,000 archived 2014 sites, 2,917 reach classification after extraction and page filters"/>
