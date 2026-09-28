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

# What can we measure?

<div class="mgt-definition">MGT = machine-generated text</div>

<div class="source-note">Qualifying sites ≠ the whole web</div>

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

# Site-level decision

<div class="hero">15 usable pages → one call</div>

<Footer />

---

# Evaluation

<div class="two-stats"><div><span class="stat">82%</span><br/>Wix held out · 41/50</div><div><span class="stat">87%</span><br/>B12 median · 34/39</div></div>

<div class="source-note">DRAFT · old wild calls remain uncalibrated</div>

<Footer />

---

<img class="paper-plot" src="/paper/body_swap_transfer_and_size_errors_split_1to1.png" alt="Paper figure: site-classifier transfer and training-size sensitivity across Wix, B12, body-swap, and CC2014 sites"/>

<Footer />

---

<img class="paper-plot" src="/paper/cdf_baseline_svm_scores.png" alt="Paper figure: baseline site score distributions and overlap"/>

<Footer />

---

<img class="paper-plot" src="/paper/pangram_vs_binoculars.png" alt="Paper figure: Pangram AI percentage versus Binoculars score for 605 generated replacement texts"/>

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

<img class="paper-plot" src="/paper/transition_3site.png" alt="Paper figure: examples of temporal changes in detector scores on sampled sites"/>

<Footer />

---

# Selected categories

<img class="category-figure" src="/paper/llm_site_kinds_incentive_coarse_combined_1col.png" alt="Draft category comparison in selected, equal-sized groups"/>

<div class="source-note">Draft calls ≠ truth; labels ≠ motives</div>

<Footer />

---

# Takeaway

<div class="hero">Observed qualifying sites only</div>

<Footer />
