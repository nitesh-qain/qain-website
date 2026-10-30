# Owner checklist (the only things the nightly agent cannot do)

Keep this short. Anything here is also summarised in the agent's daily message.

## Every week (~20 min)
- [ ] Merge (or comment on) the 2 PRs: the Monday blog post and the Wednesday page. Check the preview link in the PR.
- [ ] Post the LinkedIn drafts from the latest file in `seo/outreach/` (3 posts) and send the backlink pitch if you like it.
- [ ] Skim the latest daily report in `seo/reports/` — only the "Needs you" line matters.

## Every month (~10 min)
- [ ] Export Google Search Console → Performance (28 days, Queries and Pages) as CSV into `seo/data/gsc-YYYY-MM.csv`; add the Keyword Planner CSV too when you have it.
- [ ] First Monday: review the competitor agent's new proposals in `COMPETITOR-IDEAS.md` (mark Approved / Skip).

## One-time, highest value first
- [ ] **Google Search Console:** confirm `sitemap.xml` shows "Success", then use *URL Inspection → Request indexing* on the homepage, `/services/`, `/regions/us/`, `/regions/europe/` and each new page as it merges. This is the fastest way to get pages into search.
- [ ] Bing Webmaster Tools: submit `sitemap.xml` (the verification file is already in the repo).
- [ ] Decide a backup merger (a trusted person with GitHub write access) for when you are away.
- [ ] Add the `ANTHROPIC_API_KEY` repo secret so the second-check reviewer runs.
- [ ] Parked until 2026-11-30: Clutch/GoodFirms reviews (idea #6) and video testimonials (idea #9).
- [ ] Open: do you hold any real certifications to list on `/about`? (Phase 2.)
- [ ] When the AI/LLM industry page PR arrives, confirm the wording matches what you really do.
