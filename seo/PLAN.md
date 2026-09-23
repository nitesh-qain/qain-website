# QAInfinity SEO Plan & Daily Backlog

**Positioning target:** trusted QA/testing outsourcing partner for buyers *outside* India, US, and the Middle East — primarily UK/EU, Australia/NZ, Canada, and APAC companies who outsource QA work.

**How this file works:** the 1 AM daily automation reads this file top to bottom and works the first unchecked `[ ]` task(s) it finds, in order, unless marked `[NEEDS-YOU]` (those are skipped — they require an account/login only the site owner has, and are just flagged in the daily report as reminders). When a task ships it's checked off with the date and commit/PR link. New tasks discovered during research days get appended to the bottom of the relevant phase. Re-prioritize anytime by editing this file directly — the automation always re-reads it fresh each run.

**Canonical domain:** production is `https://www.qainfinity.com` (the apex `qainfinity.com` 308-redirects to `www`). Always use the `www` host in canonical, `og:url`, `og:image`, sitemap.xml, and JSON-LD URLs.

**Task tags:**
- `[AUTO]` — automation makes the change, verifies the site still works (preview server + browser checks), and if verification passes, pushes straight to `main` (auto-deploys via Vercel). If verification fails, it fixes and retries; if still failing, it reverts and leaves the task unchecked with a note in the day's report — nothing broken ships.
- `[PR]` — automation drafts content on a branch and opens a GitHub PR. Never merges it. Goes live only after you review and merge.
- `[NEEDS-YOU]` — requires an action only you can take (creating an account, verifying domain ownership, posting to LinkedIn). Automation will not attempt these; they stay listed as reminders.

---

## Phase 1 — Technical SEO foundation

- [x] `[AUTO]` Fix document structure on all 5 pages: add `<!DOCTYPE html>`, `<html lang="en">`, `<head>`, `<body>` wrapper (currently missing sitewide), `<meta charset="utf-8">`, `<meta name="viewport">`. Verify no visual regression on desktop + mobile. — done 2026-09-17, commit `30037ac`
- [x] `[AUTO]` Add unique `<meta name="description">` and canonical `<link>` tag per page (5 pages). — done 2026-09-18, commit `5cc07d2`
- [x] `[AUTO]` Add Open Graph + Twitter Card tags per page (title, description, image, url) so links preview correctly on LinkedIn/Slack/X. — done 2026-09-19, commit `b9bdd4e`
- [x] `[AUTO]` Add JSON-LD structured data: `Organization` sitewide, `FAQPage` on the homepage FAQ section, `Article` on each case study. — done 2026-09-20, commit `44e2471`
- [x] `[AUTO]` Add JSON-LD `Review`/testimonial markup for the homepage testimonials section. — done 2026-09-21, commit `8b5ffb2`
- [x] `[AUTO]` Create `robots.txt` and `sitemap.xml`, verify all 5 URLs resolve with no broken internal links or 404s sitewide. — done 2026-09-22, commit `2d77295` (site has grown to 7 pages since this task was scoped — `/contract-to-hire/` and `/release-readiness/` shipped manually on 2026-09-22 — so the sitemap covers all 7 live URLs)
- [x] `[NEEDS-YOU]` Verify site ownership in Google Search Console and submit `sitemap.xml` — done 2026-09-22 by the site owner; property is the domain property `sc-domain:qainfinity.com`, `nitesh0732@gmail.com` is Owner. Sitemap submission still needs confirming inside the GSC dashboard now that `sitemap.xml` exists (shipped 2026-09-22, commit `2d77295`).
- [ ] `[AUTO]` Basic Core Web Vitals pass — check the animated gradient/glow CSS isn't hurting LCP/CLS on mobile.

## Phase 2 — Information architecture

**Convention for every new page in this phase:** end the page's closing CTA with two options side by side — the primary "Book a Consult" link, plus a secondary `btn-outline` link to `/release-readiness/` (wording like "Not ready to talk? Check your risk first"). See the pattern already live on `/contract-to-hire/` and all 3 case-study pages. This is a deliberately low-commitment, self-serve option for CTO/CEO visitors who aren't ready to book a call yet — don't skip it when building new pages.

**Keyword-driven build order (from Keyword Planner data, Sept 2026 — ranges only, no live Ads campaign since 2020, but good enough to rank keywords against each other; owner will provide a fresh CSV monthly):**

*Tier 1 — build first, real volume (100–1K/month) in both US and Europe:* `qa outsourcing`, `software testing services`, `test automation services`, `qa testing services`, `quality assurance services`.

*Tier 2 — US only (100–1K/month), build after Tier 1:* `qa outsourcing company`, `qa outsourcing services`, `manual testing services`, `mobile app testing services` (line item, not a standalone page), `hire qa engineers`, `api testing services` (line item, not standalone).

*Keep as page content only, not page targets (10–100 or no data):* `qa staffing`, `contract to hire qa`, `qa team augmentation`, `software testing company dubai`.

*Middle East decision (owner-approved 2026-09-23):* every UAE/KSA keyword in the CSV is 10–100/month or no data — demoted from "parallel region page" to a lighter, later-stage page. Do not build a full UAE/KSA region page in the same pass as US/Europe; revisit in Month 3 or later, sized to the actual (low) demand.

*Region-page duplicate-content strategy (owner-approved 2026-09-23 — "do as per your judgement"):* no hreflang (content is English-only across all target markets, so there's no language variant to disambiguate). Each region page must be genuinely differentiated — different case-study emphasis, different time-zone-overlap specifics, GDPR language for EU, data-residency language for UAE/KSA when that page eventually gets built — and self-canonical (never pointing at a "master" page). Do not template three near-identical pages with the region name swapped; that risks Google treating them as duplicate content, the same risk flagged with `go.qainfinity.com`.

*Legacy `/services` URL decision (owner-approved 2026-09-23):* "let it die" — no 301 redirect from the old WordPress-era `/services`-style slugs. The new `/services/` build gets a fresh URL; the old indexed URLs are left to fall out of Google's index naturally (they already 404, and don't match any current page's naming).

- [ ] `[AUTO]` Build `/services/` hub + dedicated service pages, in the keyword-driven order above — not the original "4 pages named after the 4 homepage cards" plan. Hub targets `qa outsourcing` / `software testing services`; first two dedicated pages target `test automation services` (the Loopsy/AI automation angle) and `manual testing services`. (Note: the staffing service is now named "Dedicated QA Engineers" on the homepage, not "QA Staffing & Contract-to-Hire" — match that naming here; `hire qa engineers` is its target keyword, likely folding into `/contract-to-hire/` rather than a brand-new page — confirm with owner before building.)
- [ ] `[AUTO]` Build a real `/about` page — team credentials, certifications, and explicit time-zone-overlap messaging for UK/AU/APAC buyers.
- [ ] `[AUTO]` Add US and Europe region pages (Month 2) — see region-page strategy above. UAE/KSA demoted, not part of this pass.

## Phase 3 — Research (no site changes, findings feed Phase 4)

- [x] `[AUTO]` Competitor content scan: what are other QA-outsourcing vendors (targeting UK/AU/APAC buyers, not India/US directories) publishing? Identify content gaps. — done 2026-09-17, see Content Backlog below.
- [x] `[AUTO]` Tech/QA news scan: recent developments in AI-driven testing, QA outsourcing trends — identify timely blog angles. — done 2026-09-17, see Content Backlog below.
- [ ] `[AUTO]` Keyword shortlist for target geos (UK/EU/AU/APAC QA outsourcing intent), append to Content Backlog below. *(next research day — go deeper on search-volume/intent per keyword rather than topic gaps)*

## Phase 4 — Content / blog (each post = its own day, always `[PR]`)

**Convention:** every blog post should end with the same primary + secondary CTA pattern described under Phase 2 (Book a Consult + a link to `/release-readiness/`) — this is where CTO/CEO readers who've just read decision-stage content (cost comparisons, model comparisons) are most likely to want a low-commitment next step before booking a call.

- [ ] `[PR]` Blog: "In-House vs. Outsourced QA: A Cost and Risk Comparison for Startups"
- [ ] `[PR]` Blog: "What Is Contract-to-Hire QA Staffing (and Why It Reduces Hiring Risk)"
- [ ] `[PR]` Blog: "How AI QA Agents Cut Regression Testing Time by 90%" — do NOT name Angara or any real client in this post; the Angara engagement predated Loopsy/AI tooling, so tying their name to an AI-regression story would misrepresent that actual engagement. Write it as a general industry piece (framed around what agentic QA does to regression cycles, citing the Gartner/agentic-QA research already in the Content Backlog below), not a client case study.
- [ ] `[PR]` Blog: "A Buyer's Guide to QA Outsourcing Time Zones: Working Across UK/AU/APAC Hours"
- [ ] `[PR]` Blog: "Performance Testing Checklist Before Your Next Product Launch"
- [ ] `[PR]` Blog: "Agentic QA in 2026: What Autonomous Test Agents Actually Change for Your Release Cycle" (ties directly to Loopsy; timely trend per 2026-09-17 research)
- [ ] `[PR]` Blog: "QA Outsourcing Isn't One Thing: Managed Team vs. Staff Augmentation vs. Contract-to-Hire — Which Fits Your Stage" (fills a content gap identified 2026-09-17 — competitors don't write this comparison)

## Phase 5 — Off-page authority (mostly `[NEEDS-YOU]`)

- [ ] `[NEEDS-YOU]` Create and verify company profile on Clutch, GoodFirms, G2 (needs your account/company verification).
- [ ] `[NEEDS-YOU]` Solicit client reviews on the above platforms for existing case-study clients.
- [ ] `[AUTO]` (draft only) LinkedIn post drafts accompanying each shipped blog post — included in that day's report for you to post manually.

---

## Content Backlog (research findings land here)

**Research pass — 2026-09-17:**

*Competitor landscape:* Most QA-outsourcing content ranking today (TestDevLab, Testriq, DeviQA, GrooveTechnology, remote.qa, Botgauge, Testlio, QASource, TestingXperts) is either (a) "Top N QA outsourcing companies" comparison listicles — directory-bait, not trust-building — or (b) generic "why outsource QA" explainers not written for a specific buyer geography. Testlio/QASource/TestingXperts blogs skew toward broad methodology content aimed at a US/global audience; none found were writing specifically for UK/AU/APAC buyers on time-zone overlap, data-residency concerns outside the US, or "which QA model fits your company stage" (managed team vs. staff augmentation vs. contract-to-hire vs. self-serve AI tool) — that comparison-of-models angle is a real content gap we can own, especially paired with our actual contract-to-hire case study.

*Tech/QA news:* Agentic QA is the dominant 2026 trend across the space (Tricentis, Katalon, CloudQA, Autify, TestQuality, LuxeQuality all publishing on it). Key citable stat: Gartner projects 40% of enterprise applications will feature task-specific AI agents by end of 2026, up from under 5% in 2025; teams embedding GenAI into QA report ~40% higher test coverage and up to 10x productivity gains. This is a strong, timely hook to connect directly to Loopsy (our in-house AI QA platform) rather than talking about agentic QA in the abstract like most competitor posts do.

*AEO angle:* Competitor content is written as long SEO listicles, not as concise, directly-quotable answers. Structuring our posts with clear Q&A headers and tight definitive answers (matching the JSON-LD `FAQPage`/`Article` schema going in during Phase 1) gives us a real shot at being the source AI answer engines (ChatGPT, Perplexity, Google AI Overviews) cite for "what is contract-to-hire QA staffing" / "what is agentic QA" style queries, where competitors currently aren't optimized for extraction.

*New topics added to Phase 4 backlog as a result (see above):* the agentic QA + Loopsy piece, and the "which QA outsourcing model fits your stage" comparison piece.

Sources: [TestDevLab — Best QA Outsourcing Companies for Startups 2026](https://www.testdevlab.com/blog/best-qa-outsourcing-companies-startups) · [Botgauge — QA Outsourcing: A 2026 Guide](https://www.botgauge.com/blog/qa-outsourcing) · [remote.qa — Best QA Outsourcing Companies for Startups 2026](https://remote.qa/blog/best-qa-outsourcing-companies-startups-2026/) · [Tricentis — QA trends for 2026: AI, agents, and the future of testing](https://www.tricentis.com/blog/qa-trends-ai-agentic-testing) · [Katalon — What Is Agentic QA? The Complete Guide for 2026](https://katalon.com/resources-center/blog/what-is-agentic-qa-the-complete-guide-for-2026) · [TestQuality — The Shift to Agentic QA](https://testquality.com/the-shift-to-agentic-qa-beyond-automated-testing-to-autonomous-ai-generation-in-2026/) · [Testlio — QA Outsourcing: Why Startups Should Be Outsourcing](https://testlio.com/blog/startup-outsourcing-qa/) · [QASource Blog — QA Outsourcing](https://www.qasource.com/blog/topic/qa-outsourcing)

## Change Log

- 2026-09-17 — Initial PLAN.md, RUNBOOK.md, and report scaffolding created — commit `c58f6fb`
- 2026-09-17 — RUNBOOK verification steps adapted for headless cloud sandbox — commit `e862944`
- 2026-09-17 — Phase 3 research pass #1 (competitor scan + tech news) completed manually ahead of automation go-live; findings above, 2 new Phase 4 topics added
- 2026-09-17 — Phase 1: fixed document structure (DOCTYPE/html/head/body/meta charset/viewport) on all 5 pages — commit `30037ac`
- 2026-09-18 — Phase 1: added unique `<meta name="description">` and `<link rel="canonical">` to all 5 pages — commit `5cc07d2`
- 2026-09-19 — Phase 1: added Open Graph + Twitter Card meta tags to all 5 pages, plus a new shared branded OG image at `assets/og/default.png` (1200x630, rendered from the site's existing brand colors/logo/wordmark, no fabricated content) — commit `b9bdd4e`
- 2026-09-20 — Phase 1: added JSON-LD structured data — `Organization` on all 5 pages, `FAQPage` on the homepage FAQ section (5 Q&A pairs, text matched verbatim to visible content), `Article` on each of the 3 case study pages (headline/description from existing meta tags, dates from the homepage blog-date labels, author/publisher set to the QAInfinity organization since no individual byline exists on these pages) — commit `44e2471`
- 2026-09-21 — Phase 1: added JSON-LD `Review` markup for the 4 homepage testimonials (`reviewBody` matched verbatim to visible quotes, `author`/`worksFor` from the visible name/role/company; no `reviewRating` included since no star rating is displayed on the page) — commit `8b5ffb2`
- 2026-09-22 — Phase 1: added `robots.txt` (allow-all + sitemap reference) and `sitemap.xml` covering all 7 live pages (homepage, `/contract-to-hire/`, `/release-readiness/`, case-studies hub, and the 3 case-study pages — 2 more than the "5 pages" this task was originally scoped for, since the site owner shipped `/contract-to-hire/` and `/release-readiness/` manually earlier the same day); verified zero broken internal links/assets sitewide and all 7 pages + both new files return HTTP 200 in a headless-Chromium pass — commit `2d77295`

*(each shipped/opened item gets one line here: date — task — commit SHA or PR link)*
