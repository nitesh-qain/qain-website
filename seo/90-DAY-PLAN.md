# 90-Day SEO Plan (Nov 2, 2026 – Jan 29, 2027)

**Goal:** start appearing in search results for QA-outsourcing queries from UK/EU, Australia/NZ, Canada, APAC and US buyers — and keep shipping every night even when the owner is unavailable.

**Why this plan exists:** from about Oct 8 to Oct 29 the nightly agent found "no actionable backlog" for ~3 weeks. Causes: (1) the backlog was finite and nothing refilled it; (2) the only open tasks needed the owner (`[NEEDS-YOU]` or approvals); (3) `[PR]` work can't go live without a merge; (4) nothing flagged the stall. This plan fixes each one — see "Never-idle rules".

## Where we honestly are
- On-page foundation is done: structured data, sitemap, canonical/OG, services/region pages, 9 blog posts, case studies, a lead magnet.
- What now limits "appearing in search" is **indexing, content depth and authority**, not more technical tweaks. A young domain needs more pages that answer real queries, links from other sites, and proof that Google has crawled the pages.
- We have no search-performance data inside the agent. Mitigation: a weekly visibility log (below) plus a monthly Search Console export from the owner.

## Weekly rhythm (nightly run, 1 AM IST)
| Night | Work | Lane |
|---|---|---|
| Mon | One new blog post | PR |
| Tue | On-page / internal linking / content refresh | AUTO |
| Wed | One new page (service, industry, region, tool) | PR |
| Thu | Technical or content-quality task | AUTO |
| Fri | Technical or content-quality task | AUTO |
| Sat | Outreach drafts (LinkedIn posts, a backlink pitch, an answer to post) saved in `seo/outreach/` — drafts only | AUTO |
| Sun | Visibility log + backlog health check + replenish | AUTO |

Expected load on the owner: **2 PRs a week** (one post, one page) plus 3 LinkedIn drafts. ~20 minutes.

Full list of every post, page and task: [CONTENT-CALENDAR.md](CONTENT-CALENDAR.md).

## Month by month
**Month 1 (Nov) — close the gaps buyers hit first.** Pricing and vendor-selection posts, FAQ page, Dedicated QA Engineers and Performance & Security pages, the cost calculator, the industries hub with Gaming. AUTO work: related-reading links, breadcrumbs, key-takeaway blocks, FAQ schema on services.
**Month 2 (Dec) — industries and depth.** E-commerce, Fintech, AI/LLM, On-demand pages; LLM-testing, regression, metrics, mobile and API posts; refresh the oldest posts; accessibility, Core Web Vitals and cannibalization audits.
**Month 3 (Jan) — new markets and consolidation.** Australia/NZ, Canada, Singapore/APAC region pages; engagement-models/pricing page; title/meta CTR rewrite PR; `llms.txt`; 90-day review; **Phase 7 drafted so the backlog never empties**.

## Never-idle rules (also enforced in RUNBOOK.md)
1. **The agent may never end a night with "no actionable backlog".** If the queue has nothing eligible, it runs the evergreen rotation in the RUNBOOK.
2. **Backlog health on Sundays:** if fewer than 15 eligible tasks remain, replenish from the topic bank below before doing anything else. In week 12–13 it drafts Phase 7.
3. **Open-PR cap of 4.** When 4 agent PRs are waiting, further blog/page work is written as a draft in `seo/blog-drafts/` (not deployed) and the night's slot goes to AUTO work. Nothing is lost; PRs open when the pile clears.
4. **`[NEEDS-YOU]` never blocks the queue** — they sit in `OWNER-CHECKLIST.md`, not in the way.
5. **Stall alert:** the daily chat message leads with "Needs you:" — open PR count and age of the oldest. If 5+ PRs or any PR older than 10 days, say so in the first line.

## Away protocol (when the owner is unavailable)
- AUTO tasks keep going live on their own (low-risk, verified).
- PRs queue up to the cap of 4, then the agent writes drafts ahead. Visible new pages and posts go live only after the owner merges.
- On return: merge in the order of the PR numbers, post the LinkedIn drafts from `seo/outreach/`, read the latest report. About 30 minutes clears a 3-week absence.
- **Decision for the owner (optional):** name a backup person with merge rights who can review PRs while the owner is away. The agent never merges its own PRs.

## Visibility tracking (how we'll know it's working)
- **Sundays:** the agent runs web searches for the target keywords and the brand and records whether `qainfinity.com` appears and where, in `seo/data/visibility-log.md`. It is a best-effort proxy (not Search Console), but it shows the trend.
- **Monthly (owner, 5 min):** export Search Console → Performance (last 28 days, queries and pages) as CSV into `seo/data/gsc-YYYY-MM.csv`; the Keyword Planner CSV too when available. The agent reads these in reports.
- **Targets by Jan 29** (modest, honest): all new pages indexed; brand queries (`qainfinity`, `qa infinity`) ranking #1; at least a few non-brand queries with impressions in Search Console. First clicks from non-brand queries is a good outcome for a new domain in 90 days; page-1 ranking for `qa outsourcing` itself is unlikely this quarter.

## Topic bank (for replenishing)
Blog: QA outsourcing vs. in-house for startups at each stage; test-data management; flaky-test fixes; visual regression testing; accessibility testing basics (informational only, we don't sell compliance testing); performance testing tools compared; AI test generation limits; how to read a QA vendor's proposal; QA for SaaS onboarding flows; release checklist templates.
Pages: comparison pages (managed testing vs. staff augmentation); a glossary hub; a resources/downloads page (checklists); more industry pages only where we can write approach-led content honestly.
Off-page (drafts for the owner to send): guest-post pitches to QA and engineering-leadership blogs; answers on Quora/Stack Exchange/Reddit where genuinely helpful (disclose affiliation); expert-quote services; Loopsy launch posts.

## Guardrails that still apply
Never fabricate clients, stats, certifications or testimonials. No Contract-to-Hire for non-India audiences (internal rule, never stated publicly). No compliance/certification claims. Never merge own PRs. Parked: Clutch/GoodFirms and video testimonials until 2026-11-30.
