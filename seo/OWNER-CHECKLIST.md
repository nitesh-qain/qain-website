# Owner checklist (the only things the nightly agent cannot do)

Keep this short. Anything here is also summarised in the agent's daily message.

## Every week (~20 min)
- [ ] Review and merge (or comment on) the **one** weekly PR. Check the preview link, and especially any number or claim in it (~10 min).
- [ ] Do the week's **one** off-page action from the latest file in `seo/outreach/`, and post the founder LinkedIn draft (~10 min).
- [ ] Skim the latest daily report in `seo/reports/`. Only the "Needs you" line matters.

## Every month (~10 min)
- [ ] Until the Search Console API is connected: export Search Console → Performance (28 days, Queries, Pages and Countries) as CSV into `seo/data/gsc-YYYY-MM.csv`.
- [ ] Note how many enquiries came in from organic search that month (count only) in the latest report or chat.
- [ ] First Monday: review the competitor agent's new proposals in `COMPETITOR-IDEAS.md` (mark Approved / Skip).

## One-time, highest value first
- [ ] **Google Search Console:** confirm `sitemap.xml` shows "Success", then use *URL Inspection → Request indexing* on the homepage, `/services/`, `/regions/us/`, `/regions/europe/` and each new page as it merges.
- [ ] **Search Console API:** a read-only service account so the agent reads queries itself.
- [ ] Bing Webmaster Tools: submit `sitemap.xml` (the verification file is already in the repo).
- [ ] **Answer the open decisions** D3, D4b, D5–D10 in [90-DAY-PLAN.md](90-DAY-PLAN.md). D3 is needed by W1 (Nov 2), D4b by W3, D8 by W4, D5 by W8.
- [ ] Decide a backup merger (a trusted person with GitHub write access) for when you are away.
- [ ] Add the `ANTHROPIC_API_KEY` repo secret so the second-check reviewer runs.
- [ ] 2026-11-30: decide on Clutch/GoodFirms review requests and video testimonials (parked until then).
- [ ] Open: do you hold any real certifications to list on `/about`? (Phase 2.)
- [ ] When the W9 AI-testing post PR arrives, confirm the wording matches what you really do.
