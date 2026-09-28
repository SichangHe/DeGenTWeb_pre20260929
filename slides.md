---
theme: default
title: DeGenTWeb — Tuesday discussion
fonts:
  sans: Inter
transition: slide-left
layout: cover
class: text-center
---

# How many observed sites appear machine-written?

DeGenTWeb · Tuesday discussion draft

Steven Hé (Sīchàng)

<Footer />

---

# Count sites, not sentences

<div class="hero">Qualifying pages → page scores → one site-level <b>classifier call</b></div>

<div class="source-note">A classifier call is not proof of authorship.</div>

<Footer />

---

# A page can mislead

<div class="visual-pair"><img src="/prior/noise-example-002.png" alt="Recipe index from prior talk 3"/><img src="/prior/filter-example-002.png" alt="Privacy notice from prior talk 1"/></div>

<div class="source-note">Recipe index and privacy notice: neither is useful prose.</div>

<Footer />

---

# From pages to a site call

<img class="wide-figure" src="/paper/degentweb_pipeline.png" alt="Paper pipeline: sample, download, extract, filter, score, classify"/>

<div class="source-note">At least 15 usable pages; otherwise, no site call.</div>

<Footer />

---

# Why aggregate page scores?

<img class="main-figure" src="/prior/old-cdf-000.png" alt="Historical within-site page score distributions from prior talk 2"/>

<div class="source-note">Historical method illustration; not validation of today's rates.</div>

<Footer />

---

# Two selected samples

<div class="two-stats"><div><span class="stat">6.0%</span><br/>94,908 qualifying retained CC subdomains</div><div><span class="stat">15.4%</span><br/>18,169 qualifying Bing-result subdomains</div></div>

<div class="source-note">Draft classifier calls; CC: Jan 2020–May 2025. Bing: top 20 results for 10,000 WikiHow-title queries. Neither is the whole web.</div>

<Footer />

---

# What kinds of sites are flagged?

<img class="main-figure" src="/paper/llm_site_kinds_incentive_coarse_combined_1col.png" alt="Draft category composition in selected positive-call and non-positive groups"/>

<div class="source-note">Selected equal-sized groups, not a prevalence estimate. Categories do not prove motives.</div>

<Footer />

---

# The denominator matters

<div class="denominator">409,805 retained CC subdomains<br/>↓<br/>94,908 qualifying and classified<br/>↓<br/><b>6.0% positive calls</b></div>

<div class="source-note">Draft counts; unknown sampling probabilities prevent whole-web extrapolation.</div>

<Footer />

---

# Not yet calibrated

<div class="hero">Newer evaluation does <b>not</b> validate the earlier positive-call shares.</div>

<div class="source-note">[DRAFT PLACEHOLDER: final site-disjoint evaluation and matched detector comparison]</div>

<Footer />

---

# Takeaway

<div class="hero">We can measure classifier calls among <b>qualifying observed sites</b>.</div>

<div class="source-note">Unclassified sites remain unknown; broader prevalence needs better sampling.</div>

<Footer />

---

# Visual resources · previous talks

<div class="hero">Method diagrams and page examples from all three decks</div>

<div class="source-note">Appendix material; older numeric results are not current evidence.</div>

<Footer />

---

# Earlier talk 1 · collection

<img class="archival-figure" src="/prior/gallery/a-12.png" alt="Prior presentation 1 slide 12: website collection and extraction"/>

<div class="source-note">Earlier talk 1, slide 12 · illustrative workflow</div>

<Footer />

---

# Earlier talk 1 · filtering

<img class="archival-figure" src="/prior/gallery/a-16.png" alt="Prior presentation 1 slide 16: non-prose filtering"/>

<div class="source-note">Earlier talk 1, slide 16 · method illustration</div>

<Footer />

---

# Earlier talk 1 · aggregation

<img class="archival-figure" src="/prior/gallery/a-25.png" alt="Prior presentation 1 slide 25: score deciles and a site classifier"/>

<div class="source-note">Earlier talk 1, slide 25 · check thresholds against current paper</div>

<Footer />

---

# Earlier talk 2 · text scoring

<img class="archival-figure" src="/prior/gallery/b-12.png" alt="Prior presentation 2 slide 12: text classifier score"/>

<div class="source-note">Earlier talk 2, slide 12 · concept, not current accuracy</div>

<Footer />

---

# Earlier talk 2 · site model

<img class="archival-figure" src="/prior/gallery/b-17.png" alt="Prior presentation 2 slide 17: site-level aggregation"/>

<div class="source-note">Earlier talk 2, slide 17 · method illustration</div>

<Footer />

---

# Earlier talk 3 · page noise

<img class="archival-figure" src="/prior/gallery/c-12.png" alt="Prior presentation 3 slide 12: non-prose page noise"/>

<div class="source-note">Earlier talk 3, slide 12 · illustrative example</div>

<Footer />

---

# Earlier talk 3 · filter pages

<img class="archival-figure" src="/prior/gallery/c-16.png" alt="Prior presentation 3 slide 16: page filtering"/>

<div class="source-note">Earlier talk 3, slide 16 · method illustration</div>

<Footer />

---

# Earlier talk 3 · site aggregation

<img class="archival-figure" src="/prior/gallery/c-20.png" alt="Prior presentation 3 slide 20: site aggregation"/>

<div class="source-note">Earlier talk 3, slide 20 · older accuracy claims are not current</div>

<Footer />

---

# Visual resources · paper draft

<div class="hero">PNG exports of paper figures</div>

<div class="source-note">Draft figures, not additional verified findings.</div>

<Footer />

---

# Paper · transfer evaluation

<img class="paper-figure" src="/paper/production_transfer_detection_rates.png" alt="Draft paper transfer evaluation"/>

<div class="source-note">Draft; evaluation does not calibrate historical prevalence calls.</div>

<Footer />

---

# Paper · training size

<img class="paper-figure" src="/paper/fixed_test_vary_training_errors.png" alt="Draft paper training-size evaluation"/>

<div class="source-note">Draft evaluation; do not transfer to earlier field estimates.</div>

<Footer />

---

# Paper · test size

<img class="paper-figure" src="/paper/fixed_training_vary_test_errors.png" alt="Draft paper test-size evaluation"/>

<div class="source-note">Draft evaluation · selected test frame.</div>

<Footer />

---

# Paper · score distributions

<img class="paper-figure" src="/paper/cdf_baseline_svm_scores.png" alt="Draft paper baseline site score distributions"/>

<div class="source-note">Draft baseline groups; not web-wide samples.</div>

<Footer />

---

# Paper · observed sites over time

<img class="paper-figure" src="/paper/cc_start_year_site_llm_share.png" alt="Draft Common Crawl positive calls by first observation year"/>

<div class="source-note">Draft historical calls; first observation is not creation date.</div>

<Footer />

---

# Paper · site categories

<img class="paper-figure" src="/paper/llm_site_kinds_engagement_tech_by_label.png" alt="Draft category comparison of selected groups"/>

<div class="source-note">Draft selected groups; categories are not verified motives.</div>

<Footer />

---

# Paper · linked sites over time

<img class="paper-figure" src="/paper/webis_startpage_link_share_over_time.png" alt="Draft linked-site share over time"/>

<div class="source-note">Draft link-analysis sample, not the whole web.</div>

<Footer />

---

# Paper · linked site counts

<img class="paper-figure" src="/paper/webis_startpage_link_counts_stacked_by_date.png" alt="Draft linked-site counts by date"/>

<div class="source-note">Draft link-analysis sample, not the whole web.</div>

<Footer />

---

# Paper · Bing categories

<img class="paper-figure" src="/paper/bing_category_enrichment_grouped_pct.png" alt="Draft Bing category composition"/>

<div class="source-note">Draft selected Bing groups, not representative prevalence.</div>

<Footer />

---

# Paper · eligible recall

<img class="paper-figure" src="/paper/bedrock_eligible_recall_vs_aa.png" alt="Draft paper eligible recall evaluation"/>

<div class="source-note">Draft evaluation · review before presenting numeric claims.</div>

<Footer />
