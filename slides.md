---
theme: default
title: DeGenTWeb — what can we measure?
fonts:
  sans: Inter
transition: slide-left
layout: cover
class: text-center
---

# How much of the visible web is mostly machine-written?

### DeGenTWeb · Tuesday discussion draft

Steven Hé (Sīchàng)

---

# The question is about sites, not isolated sentences

<div class="grid grid-cols-3 gap-5 mt-16 text-center text-2xl">
<div class="rounded-xl border p-8">🌐<br/>Visible samples</div>
<div class="rounded-xl border p-8">📄<br/>Extractable prose</div>
<div class="rounded-xl border p-8">🏷️<br/>Mostly generated sites</div>
</div>

<div class="mt-12">Not all websites, all pages, or every AI-edited phrase.</div>

---

# One page can mislead

<div class="grid grid-cols-2 gap-8 mt-12 text-xl">
<div class="rounded-xl border-2 border-amber-400 p-8">Looks generated but is human?<br/><br/>Templates · repeated boilerplate</div>
<div class="rounded-xl border-2 border-rose-400 p-8">Generated but missed?<br/><br/>Editing · newer models · too few pages</div>
</div>

<div class="mt-12">When positives are rare, false positives matter.</div>

---

# A site-level measurement pipeline

<div class="flex items-center gap-3 mt-24 text-center text-lg">
<div class="rounded-xl border p-4 flex-1">sample<br/>sites</div>→
<div class="rounded-xl border p-4 flex-1">crawl<br/>pages</div>→
<div class="rounded-xl border p-4 flex-1">extract<br/>prose</div>→
<div class="rounded-xl border p-4 flex-1">score<br/>pages</div>→
<div class="rounded-xl border p-4 flex-1">classify<br/>sites</div>
</div>

<div class="mt-14">Fixed thresholds; insufficient usable pages remain unclassified.</div>

---

# Two views; neither is “the whole web”

<div class="grid grid-cols-2 gap-8 mt-10">
<div class="rounded-xl border p-8"><div class="text-2xl">Common Crawl</div><div class="mt-5 text-6xl text-teal-600">6.0%*</div><div class="mt-4">of 94,908 qualifying subdomains</div></div>
<div class="rounded-xl border p-8"><div class="text-2xl">Bing results</div><div class="mt-5 text-6xl text-purple-600">15.4%*</div><div class="mt-4">of 18,169 qualifying subdomains</div></div>
</div>

<div class="mt-10 text-sm">*Provisional manuscript positive-call shares; different sampling frames and no web-wide denominator.</div>

---

# What are the detected sites like?

<div class="grid grid-cols-3 gap-6 mt-14 text-center">
<div class="border-2 border-dashed rounded-xl p-6">Topics & genres<br/><br/>[verified distribution]</div>
<div class="border-2 border-dashed rounded-xl p-6">Search visibility<br/><br/>[audited rank graphic]</div>
<div class="border-2 border-dashed rounded-xl p-6">Incentives<br/><br/>[documented examples]</div>
</div>

<div class="mt-14">Observation is not proof of the site's motive.</div>

---

# The denominator is part of the result

<div class="mx-auto mt-12 w-4/5 text-xl text-center">
<div class="rounded-xl bg-gray-200 p-5 dark:bg-gray-700">409,805 archived Common Crawl subdomains*</div>
↓ enough usable pages
<div class="rounded-xl bg-blue-200 p-5 dark:bg-blue-800">94,908 classified*</div>
↓ fixed site rule
<div class="rounded-xl bg-teal-200 p-5 dark:bg-teal-800">6.0% positive calls among classified*</div>
</div>

<div class="mt-8 text-sm">*Draft manuscript counts; unknown inclusion probabilities prevent extrapolation to the entire open web.</div>

---

# How much confidence do the calls deserve?

<div class="grid grid-cols-2 gap-8 mt-12">
<div class="rounded-xl border p-8">Check: human proxy negatives, generated sites, filter coverage, false positives</div>
<div class="rounded-xl border p-8">Do not conflate: Pangram accuracy comparison with the site-level prevalence claim</div>
</div>

<div class="mt-12">[placeholder: final CC2014 site-disjoint evaluation and matched Pangram comparison]</div>

---

# Takeaway

<div class="text-3xl mt-16 leading-relaxed">We can estimate positive calls among <span class="text-teal-600">qualifying sites we observed</span> and describe their visible patterns.</div>

<div class="mt-14 text-xl">Unclassified sites are unknown, not human; wider prevalence needs better coverage and sampling.</div>
