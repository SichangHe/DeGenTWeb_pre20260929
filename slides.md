---
theme: default
title: DeGenTWeb — what can we measure?
fonts:
  sans: Inter
transition: slide-left
layout: cover
class: text-center
---

# How many sampled sites appear MGT-dominant?

### DeGenTWeb · Tuesday discussion draft

Steven Hé (Sīchàng)

<div class="mt-8 text-2xl">MGT = machine-generated text. We classify extractable prose, not known authorship.</div>

<Footer />

---

# The question is about sites, not isolated sentences

<div class="grid grid-cols-3 gap-5 mt-16 text-center text-3xl">
<div class="rounded-xl border p-6">🌐<br/>Two samples</div>
<div class="rounded-xl border p-6">📄<br/>Extractable prose</div>
<div class="rounded-xl border p-6">🏷️<br/>Site-level calls</div>
</div>

<div class="mt-10 text-2xl">We cannot count the whole web from these samples.</div>

<Footer />

---

# One page can mislead

<div class="grid grid-cols-2 gap-6 mt-8 items-center">
<div class="text-2xl">A recipe index is mostly tiles, not prose.<br/><br/>Templates and privacy notices can also confuse a text detector.</div>
<div class="flex justify-center gap-3">
<div class="relative"><img src="/prior/noise-example-002.png" class="h-80 rounded" alt="Recipe-index screenshot extracted from third previous talk"/><div class="absolute inset-0 flex items-center justify-center text-8xl text-red-700 font-bold opacity-80">⊘</div></div>
<img src="/prior/filter-example-002.png" class="h-80 rounded" alt="Privacy-notice screenshot extracted from first previous talk"/>
</div>
</div>

<div class="mt-3 source-note">Prior presentations 3 (slide 16) and 1 (slide 15) · illustrative pages, not site labels</div>

<Footer />

---

# A site-level measurement pipeline

<img src="/prior/pipeline-template.png" class="mx-auto mt-12 w-full max-h-64 object-contain" alt="Six-stage DeGenTWeb pipeline from previous Slidev template"/>

<div class="mt-5 text-2xl">At least 15 usable pages → page scores → one site-level call.</div>

<div class="mt-3 source-note">Prior Slidev pipeline resource · fixed thresholds · insufficient pages remain unclassified</div>

<Footer />

---

# Why score distributions instead of one page?

<div class="grid grid-cols-2 gap-8 mt-10 items-center">
<div class="text-2xl">The old baseline plot showed within-site score distributions, not single decisive sentences.<br/><br/>This figure explains the method; it does <b>not</b> validate today's prevalence calls.</div>
<img src="/prior/old-cdf-000.png" class="w-full max-h-80 object-contain" alt="Historical baseline page-score distributions extracted from prior talk"/>
</div>

<div class="mt-3 source-note">Prior presentation 2, slide 18 · historical illustrative baseline, not current validation</div>

<Footer />

---

# Classifier calls among qualifying subdomains

<div class="grid grid-cols-2 gap-8 mt-8">
<div class="rounded-xl border p-6"><div class="text-2xl">Retained CC, Jan 2020–May 2025</div><div class="mt-3 text-6xl text-teal-600">6.0%*</div><div class="mt-3 text-2xl">positive among 94,908 qualifying retained subdomains</div></div>
<div class="rounded-xl border p-6"><div class="text-2xl">Bing how-to queries</div><div class="mt-3 text-6xl text-purple-600">15.4%*</div><div class="mt-3 text-2xl">positive among 18,169 qualifying result subdomains</div></div>
</div>

<div class="mt-5 source-note">*Draft manuscript. Bing: top 20 results for 10,000 WikiHow-title queries. Neither sample represents the whole web.</div>

<div class="mt-2 source-note">Historical classifier outputs · not calibrated by the expanded evaluation</div>

<Footer />

---

# What kinds of sites receive positive calls?

<img src="/prior/draft-category-comparison.png" class="mx-auto mt-2 max-h-72 w-auto object-contain" alt="Draft manuscript category composition of selected positive-call and non-positive groups in Common Crawl and Bing"/>

<div class="mt-2 text-2xl">Selected CC groups: more service/SaaS labels among positives.</div>

<div class="mt-2 source-note">Selected equal-sized groups. Bing has little separation on this proxy. Draft figure; categories do not prove motives.</div>

<div class="source-note">Draft figure awaiting audit · historical calls not calibrated by expanded evaluation</div>

<Footer />

---

# The denominator is part of the result

<div class="mx-auto mt-9 w-4/5 text-2xl text-center">
<div class="rounded-xl bg-gray-200 p-4 dark:bg-gray-700">409,805 subdomains in retained CC records*</div>
↓ enough usable pages
<div class="rounded-xl bg-blue-200 p-4 dark:bg-blue-800">94,908 qualifying subdomains classified*</div>
↓ fixed site rule
<div class="rounded-xl bg-teal-200 p-4 dark:bg-teal-800">6.0% positive calls among classified*</div>
</div>

<div class="mt-5 source-note">*Draft manuscript; unknown inclusion probabilities prevent extrapolation to the entire web.</div>

<div class="source-note">Historical classifier outputs · not calibrated by the expanded evaluation</div>

<Footer />

---

# What is still unvalidated?

<div class="mt-12 text-3xl">The expanded evaluation does <b>not</b> calibrate these older positive-call shares.</div>

<div class="mt-8 text-2xl">We cannot verify that the earlier classifier used the newer scoring and training procedure. Pangram compares detectors, not site prevalence.</div>

<div class="mt-5 source-note">[DRAFT PLACEHOLDER — omit before presentation: final CC2014 site-disjoint evaluation and matched Pangram comparison]</div>

<Footer />

---

# Takeaway

<div class="text-3xl mt-16 leading-relaxed">We can measure positive calls among <span class="text-teal-600">qualifying sites we observed</span> and describe their visible patterns.</div>

<div class="mt-14 text-2xl">Unclassified sites are unknown, not human; wider prevalence needs better coverage and sampling.</div>

<Footer />
