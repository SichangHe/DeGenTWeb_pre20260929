# DeGenTWeb Tuesday slides

(authored by agents unless marked 🧑)

Slidev presentation and a separate [`outline.md`](outline.md). Seventeen slides follow the active paper revision and contain all six of its active figures. One extra, independently reviewed historical test-size plot was specifically requested; its two panels occupy separate slides for readability and use a different cohort from the paper's training-size plot. The 6.0% and 15.4% values are historical classifier calls among qualifying selected subdomains, not whole-web prevalence or validated ground truth.

Run `npm ci && npm run dev` locally. GitHub Pages builds with `npm run build -- --base /DeGenTWeb_pre20260929/ --router-mode hash`. Source figures stay as PNGs in `public/prior/` and `public/paper/` so slides can reuse them.

The earlier presentations are:

- [Talk 1](https://docs.google.com/presentation/d/10gFWtQwDLl5eOjvtH-C0057kkfRU1g5aUrQVGQrmoms/edit)
- [Talk 2](https://docs.google.com/presentation/d/1PHiPwkIvFBgtEKWSVPwUkWSygKkjqfO-lWImE-s5Nyc/edit)
- [Talk 3](https://docs.google.com/presentation/d/1ZGh9lTAzUyrYv2m6tjD6l5HLP-c7y94uY0D9Ug8N1Qw/edit)

The three `public/prior/news-*.jpg` article images were extracted directly from embedded images on prior talk 1, slide 5, not captured from its rendered slides. The source for active paper PNGs is the draft paper's identically named PDF in `dw-learning-curve-paper/figures/dw1/`, except `degentweb_pipeline.png`, which comes from the paper root. The additional test-size PNG comes from the reviewed historical artifact identified in `outline.md`. Unused image resources do not appear in the talk.
