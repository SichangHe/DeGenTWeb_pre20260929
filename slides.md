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

<Footer />

---

<div class="news-pair"><img src="/prior/news-wired.jpg" alt="WIRED headline: AI Slop Is Flooding Medium"/><img src="/prior/news-rolling-stone.jpg" alt="Rolling Stone headline: Facebook’s AI-Generated Spam Problem Is Worse Than You Realize"/></div>

<img class="news-feature" src="/prior/news-mit-tech-review.jpg" alt="MIT Technology Review headline: Junk websites filled with AI-generated text are pulling in money from programmatic ads"/>

<Footer />

---

# What is MGT?

<div class="mgt-definition">MGT = machine-generated text</div>

<div class="source-note">Includes templates, not just LLMs</div>

<Footer />

---

# Three obstacles

<div class="challenge-list">Text detectors err<br/>Web pages are noisy<br/>Ground truth is scarce</div>

<div class="source-note">Neither crawl nor search samples the whole web</div>

<Footer />

---

# Page noise

<div class="visual-pair"><img src="/prior/noise-example-002.png" alt="Recipe index from prior talk 3"/><img src="/prior/filter-example-002.png" alt="Privacy notice from prior talk 1"/></div>

<Footer />

---

# Six-stage pipeline

<img class="wide-figure" src="/paper/degentweb_pipeline.png" alt="Sample, download, extract, filter, score, classify"/>

<Footer />

---

# Which pages count?

<div class="challenge-list">English prose · ≥200 tokens<br/>No repeated boilerplate<br/>≥15 eligible pages per site</div>

<div class="source-note">Other sites remain unclassified</div>

<Footer />

---

# Site-level decision

<div class="hero">Binoculars page scores<br/>→ score distribution<br/>→ linear SVM site call</div>

<Footer />

---

# Evaluation

<div class="two-stats"><div><span class="stat">82%</span><br/>Wix held out · 41/50</div><div><span class="stat">87%</span><br/>B12 median · 34/39</div></div>

<div class="source-note">DRAFT · old wild calls remain uncalibrated</div>

<Footer />

---

<div class="two-stats"><div><span class="stat">97.4%</span><br/>body-swap median detected</div><div><span class="stat">40/40k</span><br/>CC2014 proxy positive calls</div></div>

<div class="source-note">2014 labels do not verify human authorship</div>

<Footer />

---

<img class="paper-plot" src="/paper/body_swap_transfer_and_size_errors_split_1to1.png" alt="Paper figure: site-classifier transfer and training-size sensitivity across Wix, B12, body-swap, and CC2014 sites"/>

<Footer />

---

<div class="plot-caption">Generated test sites</div>

<svg class="test-size-panel" viewBox="0 105 1030 800" role="img" aria-label="Test-size study: five fixed classifiers' missed generated body-swap sites versus 25 to 400 test sites, with observed fifth-to-ninety-fifth percentile ranges over 30 samples; separate training cohort from previous slide"><defs><clipPath id="body-plot-clip"><rect x="0" y="105" width="1030" height="800"/></clipPath></defs><image href="/paper/fixed_training_vary_test_errors.png" width="2196" height="1026" clip-path="url(#body-plot-clip)"/><rect x="940" y="105" width="90" height="660" fill="white"/></svg>

<div class="plot-caveat">Other cohort · fixed Wix/CC models</div>

<Footer />

---

<div class="plot-caption">Historical-CC test sites</div>

<svg class="test-size-panel" viewBox="1010 105 1186 800" role="img" aria-label="Test-size study: positive-call rate among historically negative-labeled Common Crawl sites versus 100 to 2000 test sites, with observed fifth-to-ninety-fifth percentile ranges over 30 samples; negative-labeled does not verify human authorship"><defs><clipPath id="cc-plot-clip"><rect x="1010" y="105" width="1186" height="800"/></clipPath></defs><image href="/paper/fixed_training_vary_test_errors.png" width="2196" height="1026" clip-path="url(#cc-plot-clip)"/></svg>

<div class="plot-caveat">2014 negative label ≠ verified human</div>

<Footer />

---

<img class="paper-plot" src="/paper/cdf_baseline_svm_scores.png" alt="Paper figure: baseline site score distributions and overlap"/>

<Footer />

---

# CC denominator

<div class="denominator">409,805 retained<br/>↓<br/>94,908 qualifying<br/>↓<br/>6.0% positive calls ≠ whole web</div>

<Footer />

---

# Two sampling frames

<div class="two-stats"><div><span class="stat">6.0%</span><br/>CC 2020–25 · 94,908 qualifying</div><div><span class="stat">15.4%</span><br/>Bing how-to · 18,169 qualifying</div></div>

<div class="source-note">Classifier calls ≠ web prevalence</div>

<Footer />

---

<div class="two-stats"><div><span class="stat">45.3%</span><br/>queries · top 10</div><div><span class="stat">64.8%</span><br/>queries · top 20</div></div>

<div class="source-note">≥1 matched positive call · unclassified results unknown</div>

<Footer />

---

<img class="temporal-plot" src="/paper/transition_3site.png" alt="Paper examples of changes in detector scores over page dates, without attributing cause"/>

<div class="source-note">Score shifts ≠ proof of LLM adoption</div>

<Footer />

---

# Selected categories

<img class="category-figure" src="/paper/llm_site_kinds_incentive_coarse_combined_1col.png" alt="Draft category comparison in selected, equal-sized groups"/>

<div class="source-note">Draft calls ≠ truth; labels ≠ motives</div>

<Footer />

---

# Selected group differences

<div class="challenge-list">CC: more services and SaaS among positive calls<br/>Bing: little separation on the incentive proxy</div>

<div class="source-note">Equal-sized groups · not a web-wide mix</div>

<Footer />

---

<img class="paper-plot" src="/paper/pangram_vs_binoculars.png" alt="Paper figure: Pangram AI percentage versus Binoculars score for 605 selected generated replacement texts"/>

<Footer />

---

<div class="two-stats"><div><span class="stat">470/605</span><br/>Binoculars · max-F1 calls</div><div><span class="stat">594/605</span><br/>Pangram · AI labels</div></div>

<div class="source-note">Selected generated texts · no matched false-positive rates</div>

<Footer />

---

# Takeaway

<div class="hero">Calls among qualifying sites<br/>≠ prevalence across the web</div>

<Footer />

---

# Backup slides to prepare

<div class="challenge-list">Filter attrition<br/>Held-out builder & CC2014 checks<br/>Search-rank and category denominators</div>

<Footer />
