Tuesday talk outline
(authored by agents unless marked 🧑)

how much of the qualifying visible web appears dominated by machine-generated text, and what kinds of sites are these?
- why ask
  - three news screenshots
- what we can measure
  - qualifying sites with enough extractable text
  - not the whole web
  - page noise, filtering, and 15 usable pages per site
- how we check the classifier
  - held-out generated sites and historical sites labeled negative
  - training-size and transfer results
  - separate test-size study using different trained models
  - score distributions and Pangram comparison
  - newer checks do not calibrate older site calls
- what we found
  - Common Crawl: 6.0% positive calls among 94,908 qualifying sites
  - Bing how-to: 15.4% positive calls among 18,169 qualifying sites
  - examples of changing scores over time
- what kinds of sites
  - draft categories in selected, equal-sized comparison groups
- takeaway
  - classifier calls are not whole-web prevalence or verified truth
