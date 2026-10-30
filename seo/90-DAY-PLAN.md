# 90-Day SEO Plan, v2 (Nov 2, 2026 – Jan 29, 2027)

**Goal:** get overseas buyers (UK/EU, US, Australia/NZ, Canada, APAC) to find QAInfinity, trust it and start a conversation. Rankings and page counts are means, not the goal.

**Why v2 (2026-10-31):** the first version solved the 3-week idle stall by making the agent produce constantly (26 content PRs and 39 auto tasks in 13 weeks). Three independent reviews (Claude, GPT, Gemini) agreed that this was the wrong trade for a young, low-authority domain: overlapping pricing pages, doorway-style region pages, approach-led industry pages, compliance-adjacent wording, and almost no work on trust or authority. Repo checks also found problems on live pages that matter more than any new page. Full reasoning: [PLAN-REVIEW-2026-10-31.md](PLAN-REVIEW-2026-10-31.md). The queue itself is Phase 6 in [PLAN.md](PLAN.md); this file is the strategy.

**North star (owner, 2026-10-31): every change must make a visitor trust QAInfinity more.** When a task would add volume without adding trust, or puts a claim we can't back in front of a buyer, don't do it.

## Principles
1. **Fix trust before adding pages.** A false or unbacked claim on a live page outweighs any new post.
2. **Publish only what's backed by proof or a real offer.** No approach-led industry pages, no compliance or certification-adjacent wording.
3. **One PR a week**, bundled by theme, small enough to fact-check properly.
4. **One off-page action a week** from the owner, with the agent drafting everything.
5. **Expansion is demand-led.** Weeks 10–13 come from Search Console evidence, not a topic bank.
6. **The agent's job is the next most valuable action**, not a full backlog (RUNBOOK section 0).

## What we sell overseas (owner, 2026-10-31)
A **remote QA team** at **$18–45/hr** by experience and skill: engineers embedded in the client's team, or running testing end to end. Two scheduling options, any time zone:
1. **The client's own hours**: full overlap.
2. **The 24-hour cycle**: the client's devs hand off at end of day, QA tests overnight, bugs are ready next morning, 1–2 hour overlap.

No fixed-price or project-based engagements. Contract-to-Hire isn't offered overseas: it's off the homepage from W1, kept only as one `/faq/` Q&A, the footer link and its own page and case studies. Never say "India-only" publicly.

## The 13 weeks at a glance
| Weeks | Theme | The one PR each week |
|---|---|---|
| W1 | Fix trust | Time-zone copy, homepage Contract-to-Hire removal, unbacked stats, brand spelling |
| W2–W4 | Commercial core | `/services/dedicated-qa-engineers/` · `/pricing/` · estimator on `/pricing/` + "How much does QA outsourcing cost" post |
| W5–W7 | The pitch and due diligence | `/offshore-qa/` (all regions, both scheduling options) · `/faq/` + "How to evaluate an offshore QA partner" · `/industries/ecommerce/` + deeper Angara case study |
| W8–W9 | Expertise, only where real | `/services/performance-testing/` *(if D5)* · "How to test LLM apps and AI agents" *(owner confirms wording)* |
| W10–W13 | Demand-led | Search Console analysis → up to 2 owner-approved PRs → 90-day review → Phase 7 draft from evidence |

Auto tasks (no owner time) run on the other nights: related reading (never linking to the Contract-to-Hire posts), breadcrumbs, audits, internal links to each new page after it merges. Readable list: [CONTENT-CALENDAR.md](CONTENT-CALENDAR.md).

## Owner decisions
| # | Decision | Answer |
|---|---|---|
| D1 | Hours the team works for US/UK/AU clients | **Answered 2026-10-31:** any time zone; the two scheduling options above. |
| D2 | Contract-to-Hire on the homepage | **Answered 2026-10-31:** remove from the homepage, keep in `/faq/`; footer link, CTH page and case studies stay. |
| D3 | Basis for "98% client satisfaction" and "up to 80% faster" (Loopsy) | **Answered 2026-10-31:** placeholders, no basis. Both come off in W1. |
| D4 | Engagement models overseas | **Answered 2026-10-31:** remote QA team, hourly $18–45, either schedule; no fixed-price. |
| D4b | Does working the client's hours (e.g. a US night shift) change the rate? | Open. Needed for `/pricing/` (W3). |
| D5 | Do we deliver performance testing (tools, a past engagement)? Any security work? | Open. Decides W8. |
| D6 | Were Snabbit/Ninjacart QA engagements we can name and describe? | Open. Decides a future on-demand page. |
| D7 | Have we tested an AI/LLM product for a paying client? | Open. AI service page vs post only. |
| D8 | Estimator bands: $18–30 junior/mid, $30–45 senior/SDET? | Open. Needed by W4. |
| D9 | Is the US a primary target? (PLAN.md's header says outside India, US and the Middle East; the review pack included the US.) | Open. Affects region emphasis. |
| D10 | Founder bio (2–3 lines + LinkedIn URL) for bylines | Open. Byline + `Person` schema. |

## Off-page (owner ~10 min/week; the agent drafts everything)
| Cadence | Action |
|---|---|
| Once (Nov) | Directory profiles: LinkedIn company page, Crunchbase, Sortlist (EU buyers), TechBehemoths. The agent prepares the copy; the owner pastes. |
| Weekly | One founder LinkedIn post from the founder's personal profile. |
| Monthly | One founder article for a QA community or publication (e.g. Ministry of Testing). The agent drafts; the founder edits and adds real experience. |
| Monthly | Ask one client or partner for a link to the published case study, or a written testimonial. |
| As available | Expert-quote requests (Qwoted, Featured.com, SourceBottle for AU/NZ). |
| 2026-11-30 | Owner decides on Clutch/GoodFirms review requests and video testimonials (parked until then). |
| When ready | Loopsy launch (Product Hunt, AI-tool directories). |

No cold backlink pitches, no paid links, no guest-post networks.

## Measurement
- **Primary: Search Console** (API via a read-only service account once set up, otherwise the owner's monthly CSV in `seo/data/gsc-YYYY-MM.csv`) and **GA4**.
- **Directional only:** the agent's Sunday web-search visibility log in `seo/data/visibility-log.md`.

**KPIs by Jan 29, 2027**
| KPI | Target |
|---|---|
| Priority pages indexed (home, `/services/` + service pages, `/pricing/`, `/offshore-qa/`, `/faq/`, `/industries/ecommerce/`) | All; index rate of everything else tracked as a quality signal |
| Non-brand impressions | Rising month on month |
| Clicks from target countries (Search Console country filter) | First clicks from the UK, US and Australia |
| Referring domains | +5–10 (profiles, 1–2 editorial) |
| Clutch/GoodFirms reviews | Decision on 2026-11-30; 2 by Jan 29 if requests go out in early December |
| Qualified enquiries from organic | Owner's monthly count (GA4 form-submit event; add one if missing) |
| Brand queries (`qainfinity`, `qa infinity`) | #1 (aspiration, not a business KPI) |

Page-1 rankings for generic terms like `qa outsourcing` are unlikely this quarter and aren't a target.

## Away protocol
- Auto tasks keep going live on their own (low-risk, verified).
- PRs queue up to the cap of 2; after that the agent writes drafts ahead in `seo/blog-drafts/`. New pages and posts go live only when the owner merges.
- On return: merge in PR-number order, post the latest LinkedIn draft, read the latest report.
- Optional: name a backup person with merge rights. The agent never merges its own PRs.

## Guardrails
Never fabricate clients, stats, certifications or testimonials. No figure unless it's documented in a published case study or confirmed by the owner. No compliance or certification claims. No Contract-to-Hire in overseas-facing content (exceptions above), never "India-only" publicly. Never claim standard Indian hours already overlap a Western working day. Never merge own PRs. Parked until 2026-11-30: Clutch/GoodFirms reviews and video testimonials.
