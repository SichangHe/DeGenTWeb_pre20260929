🤖 Tuesday talk outline
(authored by human unless marked 🤖)

## Meta

- 30min talk
- mostly familiar audience, some new but familiar with networking

## Outline

- central questions
  - how much of the web is MGT
  - what are these sites doing
- 🤖why ask
  - 🤖three news screenshots introduce the concern
- challenges
  - cannot reliably detect MGT
    - 🤖text detector inaccuracies
    - 🤖web content noise
    - 🤖lack of ground truth
  - cannot sample the whole web
    - 🤖neither crawl nor search results represent all sites
- 🤖what counts as a site call
  - 🤖article-heavy sites with extractable English prose
  - 🤖sample pages and remove boilerplate, repeats, and short text
  - 🤖require at least 15 eligible pages; leave other sites unclassified
  - 🤖summarize Binoculars page scores with a site-level linear SVM
- 🤖how we check the classifier
  - 🤖Wix, B12, and generated body-swap sites test detection
  - 🤖2014 Common Crawl sites are proxy negatives, not verified human text
  - 🤖82% held-out Wix; 87% median B12; 97% median body-swap detected
  - 🤖40 positive calls in 40,000 held-out 2014-site decisions
  - 🤖training-size and transfer plot shows model sensitivity
  - 🤖separate test-size plot uses different fixed classifiers
  - 🤖site score distributions improve on a page threshold
- 🤖what we observe in the wild
  - 🤖Common Crawl: 409,805 retained; 94,908 qualifying; 6.0% positive calls
  - 🤖Bing how-to: 59,046 results sites; 18,169 qualifying; 15.4% calls
  - 🤖45.3% of queries have a positive call in the matched top ten
  - 🤖site scores sometimes shift across archive dates
    - 🤖date shifts do not establish why a site changed
- 🤖what kinds of sites
  - 🤖compare selected, equal-sized positive and non-positive groups
  - 🤖service, SaaS, affiliate, editorial, personal, and other categories
  - 🤖more service and SaaS labels among CC positive calls
  - 🤖little Bing separation on the financial-incentive proxy
  - 🤖category and monetization proxies do not establish motives
- 🤖where the measurement stops
  - 🤖605 selected new-model generated texts test detector shelf life
  - 🤖Binoculars calls 470 positive; Pangram calls 594 positive
  - 🤖new validation does not calibrate earlier wild-site calls
  - 🤖classifier calls are not whole-web prevalence or verified truth
- 🤖backup slides to prepare
  - 🤖filter attrition and why sites remain unclassified
  - 🤖held-out builder and 2014 proxy-negative details
  - 🤖search result matching and query-rank denominators
  - 🤖category-group sizes and missing signal coverage
