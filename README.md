# DeGenTWeb Tuesday slides

(authored by agents unless marked 🧑)

Slidev presentation and a separate [`outline.md`](outline.md). Twenty-four slides explain the paper's questions, detection method, evaluation, sampled findings, characterization, and limits; the final slide proposes backup material. All six active paper figures appear in manuscript order. The separately requested historical test-size plot uses a different cohort from the paper's training-size plot. The 6.0% and 15.4% values are historical classifier calls among qualifying subdomains, not whole-web prevalence or validated ground truth.

Run `npm ci && npm run dev` locally. GitHub Pages builds with `npm run build -- --base /DeGenTWeb_pre20260929/ --router-mode hash`. Source figures stay as PNGs in `public/prior/` and `public/paper/` so slides can reuse them.

The earlier presentations are:

- [Talk 1](https://docs.google.com/presentation/d/10gFWtQwDLl5eOjvtH-C0057kkfRU1g5aUrQVGQrmoms/edit)
- [Talk 2](https://docs.google.com/presentation/d/1PHiPwkIvFBgtEKWSVPwUkWSygKkjqfO-lWImE-s5Nyc/edit)
- [Talk 3](https://docs.google.com/presentation/d/1ZGh9lTAzUyrYv2m6tjD6l5HLP-c7y94uY0D9Ug8N1Qw/edit)

The three `public/prior/news-*.jpg` article images were extracted directly from embedded images on prior talk 1, slide 5, not captured from its rendered slides. Active paper PNGs render the identically named PDF in `dw-learning-curve-paper/figures/dw1/`, except `degentweb_pipeline.png` from the paper root. The separate test-size PNG is a copy of the reviewed historical `fixed_training_vary_test_errors.png` artifact. Unused image resources do not appear in the talk.
