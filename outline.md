(authored by human unless marked 🤖)
<!-- Try to preserve human-authored text as possible and suitable -->

## Meta

- 30min talk
- mostly familiar audience, some new but familiar with networking
- rough pacing
    - 5 min motivation
    - 15 min methodology
    - 10 min findings and takeaways

## Outline

- motivation
    - background
        - three news screenshots introduce the concern
        - concrete quality concerns
    - central questions
        - how much of the web is MGT
        - what are these sites doing
    - challenges
        - cannot reliably detect MGT
            - text detector inaccuracies
            - web content noise
            - lack of ground truth
        - cannot sample the whole web
- methods
    - narrow down measured target
        - English prose-heavy sites
            - ignore non-prose
        - text dominated by MGT
            - ignore LLM-polished
    - DeGenTWeb pipeline: address web content noise (show whole pipeline)
        - screenshot: site page with navigation and boilerplate
        - sample pages (pipeline figure, corresponding part highlighted)
            - (use semi-transparent overlay to phase out other parts)
            - Sitemap
            - Wayback Machine Content Index
        - extract main text (pipeline figure…)
            - Tranfilatura (logo)
        - filtering (pipeline figure…)
            - English text, ≥200 tokens
            - Dolma Quality Filter (details)
                - common preexisting NLP practice
            - duplication ≤50%
            - ≥15 qualified pages per site
    - address lack of ground truth
        - generate Wix and B12 baseline sites from real site topics
            - (somewhat detailed explanation)
        - generate body-swap sites from real sites/pages
            - (somewhat detailed explanation)
        - 2014 Common Crawl (CC) sites as proxy negatives
            - common practice in MGT detection to use historical text
        - 🤖show paired site examples or a traceable issue screenshot
    - compensate for text detector inaccuracies
        - score each qualified page with Binoculars
        - text detectors inaccurate
            <!-- TODO: Let a dw agent recompute those using this new baseline and plot using plotting config used in paper -->
            - bar chart accuracies among detectors
            - overlapping page-score distributions
                - insight: classify distributions, not individual pages
        - use 9 score deciles as feature vector
        - train a linear SVM classifier on feature vectors
    - does it work (bar chart/ box plot for each)
        - in-domain
        - out-of-domain
        - on more data
        - compare with page level
        - on LLM-polished sites
        <!-- - TODO: call it FPR, not positive call rate -->
    - understanding limitations
        <!-- TODO: get a dw agent to do this -->
        - breakdown of disqualified CC 2014 sites
        - worse FNR on newer LLMs
        - accuracy-cost tradeoff
            - Pangram vs Binoculars on Sonnet 4/4.6
- findings in the wild
    <!-- TODO: Make this part more meaty. Try to cover the good stuff in the paper -->
    <!-- TODO: Plot bar charts of some of these even if there are only 1 or 2 bars, following plotting conventions in the paper. -->
    - 🤖Common Crawl archive sample
        - estimate prevalence on open web
        - 🤖409,805 retained subdomains
            - 🤖94,908 qualifying
        - 🤖6.0% positive calls among qualifying sites
    - 🤖Bing how-to search sample
        - estimate prevalence in search results
        - 🤖59,046 result sites
            - 🤖18,169 qualifying
        - 🤖15.4% positive calls among qualifying sites
        - 🤖45.3% of queries have a matched positive call in the top ten
    - 🤖characterize selected site groups
        <!-- TODO: This is where you put in the screenshots -->
        - 🤖compare equal-sized positive and non-positive groups
        - 🤖show category differences without inferring motives
        - 🤖show archive-date score shifts without asserting their cause
- contributions
- backup slides
    - baseline construction prompts
    - CC 2014 negatives and training/test-size study details
