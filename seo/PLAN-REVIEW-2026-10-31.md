# Plan review and rationale, 2026-10-31

> **Record, not a queue.** The owner approved this on 2026-10-31 and it now lives in Phase 6 of [PLAN.md](PLAN.md) (the queue) and [90-DAY-PLAN.md](90-DAY-PLAN.md) (the strategy and the current answers to owner decisions). The nightly agent executes those files, not this one.

Built from three independent reviews of the first 90-day plan (Claude, GPT, Gemini), plus checks against the live repo. Line numbers are as of 2026-10-31.

---

## 1. What we're doing wrong

All three reviewers agree on these:

| # | Problem | Claude | GPT | Gemini |
|---|---|:-:|:-:|:-:|
| 1 | The plan optimises for **output** (26 content PRs, 39 auto tasks). The real limits are **trust and authority**. | ✓ | ✓ | ✓ |
| 2 | **Pricing/models cluster:** 6 URLs competing for "QA outsourcing cost / pricing / models". | ✓ | ✓ | ✓ |
| 3 | **Region pages** (AU/NZ, Canada, Singapore) are near-template doorway pages. | ✓ | ✓ | ✓ |
| 4 | **Forced pairings** in W10–W12 (contract post↔AU, regression↔Canada, Playwright↔Singapore). | ✓ | ✓ | ✓ |
| 5 | **The engagement-models page comes last** (W13), though it's the most commercial page in the plan. | ✓ | ✓ | ✓ |
| 6 | **Fintech page** ("PCI DSS/PSD2 in mind") is a compliance hook with nothing behind it. | ✓ | ✓ | ✓ |
| 7 | **Off-page is almost absent.** All three said to unpark Clutch reviews now; the owner is keeping them parked until 2026-11-30. | ✓ | ✓ | ✓ |
| 8 | **Practitioner topics** (Playwright vs Cypress vs Selenium) attract engineers, not buyers. | ✓ | ✓ | ✓ |
| 9 | **"All new pages indexed"** is too absolute for a young domain. | ✓ | ✓ | ✓ |

The root cause, in GPT's words: the agent's objective is to *keep the backlog full*. It should be to *find the next real chance to win an overseas QA customer*. The "never-idle" rules fixed the 3-week stall, but they turned the agent into a content assembly line.

## 2. Problems on the live site (checked in the repo)

These matter more than any new page. An overseas CTO landing today gets mixed signals.

| Issue | Where | Status |
|---|---|---|
| **Wrong time-zone claim.** "…engineers work standard daytime hours that already line up with your team's working day end to end… No shifted schedules needed." Standard Indian hours overlap London by only ~4–5 h. The owner confirms the team can work any client's hours, so the fix is the wording: "we work your hours", not "our hours already line up". | `/regions/europe/` | Confirmed. **Fix in W1.** |
| **Two scheduling options the site never states together:** engineers work the client's own hours (full overlap), or the 24-hour cycle (overnight testing, 1–2 h overlap). | `/regions/us/`, `/regions/europe/`, `/services/` | Owner confirmed both (D1). |
| **Homepage leads with Contract-to-Hire** in 6 places: the stats bar ("100% Contract-to-hire conversion rate"), the services blurb ("trial-to-hire available on request"), the gaming case-study card, two insights rows, and the homepage FAQ (plus its JSON-LD). Overseas buyers can't buy it. | `/` | Owner: remove from the homepage, keep in the FAQ (D2). |
| **"98% Client satisfaction"** has no documented basis (only two documented engagements). | `/` line 473, `/regions/us/` 243, `/regions/europe/` 243, `/about/` 239 | Waiting on owner (D3). |
| **"Up to 80% faster to build & maintain"** (Loopsy) has no documented basis. | `/` line 493; the two AI blog posts (agentic-qa line 326, ai-qa-agents line 320) | Waiting on owner (D3). |
| **The gaming case study is a staffing story**: "How Contract-to-Hire Built a High-Performance QA Team — 11 Placed, 11 Converted". It proves we supply good engineers, not gaming *testing* delivery. A "proof-backed" gaming industry page would have to strip out the proof. | `/case-studies/real-money-gaming.html` | Confirmed. GPT was right; Claude and Gemini missed it. |
| **Existing models post** is CTH-titled with 26 CTH mentions, and the related-reading task would link overseas posts to it. | `/blog/qa-outsourcing-models-which-fits-your-stage.html` | Confirmed. |
| **Fixed-price/project-based work** appears in the old plan's W13 page and post, but it isn't a real offer. | plan | Owner: not offered (D4). Dropped. |
| **Brand spelling**: "QAINfinity" in every title tag; the homepage mixes three spellings. | site-wide | Confirmed. |
| **Measurement not started**: visibility log empty, Search Console/Bing checklist items unticked, outreach folder has no drafts. | `seo/` | Confirmed. |

## 3. Where the reviewers disagreed, and the call

| Topic | Claude | GPT | Gemini | **Call** |
|---|---|---|---|---|
| Gaming industry page | Proof-backed, ship | Reconsider: staffing proof only | Ship | **Don't ship now.** The case study is a CTH placement story. Use the MPL testimonial as staffing proof on the dedicated-engineers page instead. |
| AI/LLM testing | Move under services | Potential differentiator if methodology is real | Kill the page | **One methodology post, no service page** until the owner confirms paid delivery (D7). Keep it clearly separate from "AI-powered QA" (Loopsy). |
| On-demand page | Ask about Snabbit/Ninjacart | Conditional | Kill | **Park**, unless Snabbit/Ninjacart were QA engagements we can cite (D6). |
| Region pages | Canada → US page; one APAC page | Keep AU with real detail; delay Canada/SG | Scrap all; one global time-zone page | **One page for all regions** (`/offshore-qa/`), which also targets "offshore QA testing services". A dedicated country page only when Search Console shows demand from that country. |
| W4 cost post | Keep | Excellent | Cancel | **Keep**, with a clear split: post = market rates and cost drivers (cited); `/pricing/` = our own rates and models. |
| FAQ schema + llms.txt | Cargo cult | Low priority | "Strongest technical part" | **Keep `/faq/` (real objections), drop FAQ-schema nights elsewhere, llms.txt to the bottom.** Google limits FAQ rich results to authoritative government and health sites and says no special AI files are needed. Gemini is wrong here. |
| Performance & security page | Rename to performance testing | Only after capability is validated | — | **Conditional on D5.** If shipped: performance testing, with security limited to functional checks (auth, access control, input validation). |
| Content volume | Cut ~30% | 6–8 assets | Cut heavily | **~8 new URLs in 13 weeks**, plus fixes to existing pages. The last 4 weeks are demand-led. |
| PR cadence | Fewer, reviewed properly | Bundle into one theme PR a week | — | **One PR per week.** |
| Clutch profile value | Buyer trust + AI citations | Trust, not automatic SEO authority | "Immediate authority" | GPT's view: the value is **buyer trust and AI-answer citations**, not link equity. Still high value; the owner revisits on 2026-11-30. |

Errors to discard: GPT put "zero backfills" on the US page (it's in the gaming case study). Gemini overrated FAQ schema/llms.txt and missed that the gaming proof is CTH. Claude treated gaming as proof-backed and didn't flag the false Europe overlap claim.

None of the three reviewers had search-volume data. The keyword choices below are informed guesses until Search Console data or a Keyword Planner export exists.

---

## 4. The new plan as approved (the task-level version is Phase 6 in PLAN.md)

### Principles
1. **Fix trust before adding pages.** A false claim on a live page outweighs any new post.
2. **Publish only what is backed by proof or a real offer.** No approach-led industry pages, no compliance-adjacent wording.
3. **One PR a week**, bundled by theme, small enough for the owner to fact-check properly.
4. **One off-page action a week** from the owner. Fewer LinkedIn drafts (one, not three).
5. **Expansion is demand-led.** Weeks 10–13 are chosen from Search Console data, not from a topic bank.
6. **The agent's job is the next most valuable action**, not a full backlog. A night spent fixing a page or drafting an outreach asset counts.

### Owner decisions
| # | Decision | Answer / why it matters |
|---|---|---|
| D1 | What hours does the team work for US/UK/AU clients? | **Answered 2026-10-31:** any time zone the client needs. Two options: the client's own hours, or the 24-hour cycle. |
| D2 | Contract-to-Hire on the homepage? | **Answered 2026-10-31:** remove it from the homepage, keep it in the FAQ (details in W1/W6). The footer link, the CTH page and the CTH case studies stay unchanged. Never state "India-only". |
| D3 | What is the basis for "98% client satisfaction" and "up to 80% faster"? | Open. If there's no documented basis, remove or replace in W1. |
| D4 | Engagement models for overseas buyers? | **Answered 2026-10-31:** a remote QA team (embedded with the client's team or running testing end to end), billed hourly at $18–45/hr, with either scheduling option. No fixed-price projects. |
| D4b | Does working the client's hours (e.g. a US night shift) change the rate? | Open. Needed for `/pricing/`. |
| D5 | Do we deliver performance testing for clients (tools, a past engagement)? What security work, if any? | Open. Decides whether W8 ships. |
| D6 | Were Snabbit/Ninjacart QA engagements we can name and describe? | Open. Decides whether on-demand gets a proof-backed page later. |
| D7 | Have we tested an AI/LLM product for a paying client? | Open. AI page vs post. |
| D8 | Are the calculator rate bands OK: $18–30 junior/mid, $30–45 senior/SDET? | Open. Calculator. |
| D9 | Is the US a primary target? (The 2026-09-20 positioning note says outside India, US and the Middle East; the review pack says US is in.) | Open. Region emphasis. |
| D10 | A short founder bio for the byline (2–3 lines plus LinkedIn URL). | Open. Founder byline / Person schema. |

### Week 0 — owner one-off, ~30 min (this weekend if possible)
- Search Console: confirm the sitemap status is "Success"; request indexing for `/`, `/services/`, `/regions/us/`, `/regions/europe/`.
- Bing Webmaster Tools: submit the sitemap.
- Search Console API: add a read-only service account so the agent can read queries itself (free; replaces guessing from web searches).
- Answer the open decisions (D3, D4b, D5–D10), even partially.
- Clutch/GoodFirms review requests and video testimonials stay **parked until 2026-11-30** (owner decision).
- Optional (10 min): Keyword Planner volumes for the ~20 candidate terms in Appendix A.

### Phase 1 — Fix trust and the commercial core (W1–W4)
| Week | The one PR | Notes |
|---|---|---|
| W1 | **Trust-fix bundle** (existing pages only) | **Time zones (D1):** rewrite the Europe and US overlap copy and the `/services/` "time-zone overlap" line around the two real options (your hours, or the 24-hour cycle). **Homepage Contract-to-Hire (D2):** replace the "100% CTH conversion" stat with the Angara result (8 hrs → ~30 min); swap "trial-to-hire available on request" for the scheduling options; retitle the gaming card as a dedicated-team story (link unchanged); replace the two CTH insights rows with overseas-relevant posts; remove the CTH homepage FAQ question and its JSON-LD (it moves to `/faq/` in W6); keep the footer link. **Stats (D3):** remove or replace 98% and 80% on every page listed in section 2. Unify the brand spelling in titles. Founder byline + `Person` schema if D10 is in. |
| W2 | **`/services/dedicated-qa-engineers/`** | The service card already exists. Staff-aug positioning, onboarding/first-30-days section folded in (no separate post), MPL testimonial as staffing proof without CTH framing, honest overlap model. Update the `/services/` JSON-LD. |
| W3 | **`/pricing/`**: how a remote QA team works + rate range | Replaces both `/engagement-models/` and the W13 pricing-models post. One model (a remote QA team, embedded or running testing end to end), two scheduling options (your hours / 24-hour cycle), $18–45/hr as a range, not a quote, and what moves the rate (seniority, skills, D4b). No fixed-price. |
| W4 | **Calculator added to `/pricing/`** + post **"How Much Does QA Outsourcing Cost in 2026?"** | Post = market benchmarks with sources, linking to `/pricing/` for our own rates (keep the two clearly apart). Calculator uses the D8 bands, is labelled illustrative and captures nothing. |

### Phase 2 — The pitch and the buyer's due diligence (W5–W7)
| Week | The one PR | Notes |
|---|---|---|
| W5 | **`/offshore-qa/`**: "Offshore QA testing in your time zone: we work your hours, or run a 24-hour cycle" | One page for all regions, built on the two options. City table (New York, San Francisco, Toronto, Vancouver, London, Berlin, Sydney, Melbourne, Auckland, Singapore): what "your hours" means in IST, where the overnight handoff gives the most (US, Canada), where same-day overlap is natural (Singapore), and daylight-saving shifts. Replaces the 3 planned region pages. US/Europe pages and the time-zone/follow-the-sun posts link to it. |
| W6 | **`/faq/`** + post **"How to Evaluate an Offshore QA Partner"** | FAQ = real buyer objections (pricing, NDA/IP, onboarding, replacement if an engineer leaves, reporting, overlap, the two scheduling options), not copies of the homepage Q&As. **Includes the Contract-to-Hire Q&A moved from the homepage** (owner decision 2026-10-31; overrides the old "no CTH on /faq/" note). The post is a checklist for evaluating *any* vendor and links to the FAQ. |
| W7 | **`/industries/ecommerce/`** + a deeper Angara case study | Only proof-backed industry. No industries hub until there's a second one. The peak-season checklist moves to Aug–Sep 2027 (Black Friday 2026 is Nov 27, so a December post is too late for this year). |

### Phase 3 — Expertise, only where real (W8–W9)
| Week | The one PR | Notes |
|---|---|---|
| W8 | **`/services/performance-testing/`** *(if D5 = yes)* | Rescoped; security limited to functional checks. If D5 = no, use the slot for Loopsy page improvements or a deeper case study. |
| W9 | Post **"How to Test LLM Apps and AI Agents"** *(methodology, no client claims)* | Owner confirms the wording. Clearly separate from the two existing "AI-powered QA" posts. Becomes a service page only if D7 = yes. |

### Phase 4 — Demand-led (W10–W13)
- **W10:** the agent reads Search Console (API or the owner's CSV) and proposes the next 3 PRs, each with its evidence: a query with impressions, a country showing interest, or a page ranking 8–20. Candidates in Appendix A.
- **W11–W12:** ship the two strongest proposals the owner approves.
- **W13:** 90-day review against the KPIs below, then draft Phase 7 from the evidence. **No count-based backlog refill.**

### Auto lane (agent, no owner time)
**Keep:** breadcrumbs; image audit; heading audit; key-takeaways blocks; tables of contents; sitemap audit; JSON-LD validation; broken-link sweeps; Core Web Vitals; mobile pass; internal links to each new page after it merges; `Organization.sameAs` once the directory profiles are live.
**Change:**
- "Related reading" must **exclude the two CTH posts** from overseas-facing posts.
- **One** content refresh, triggered by a reason (dead link, outdated figure, Search Console data), instead of three date-bump passes on posts only 10–14 weeks old.
- Title/meta rewrites only for pages with Search Console impressions and low CTR.

**Cut:** FAQ schema on `/services/`, the service pages and the case studies (keep it only on `/faq/`). llms.txt moves to the bottom of the backlog.

### Off-page (owner ~10 min/week; agent drafts everything)
| Cadence | Action |
|---|---|
| Nov 30 | Owner decides on Clutch/GoodFirms review requests and video testimonials (parked until then). The agent drafts the two request emails beforehand so they're ready. |
| Once (spread over Nov) | Profiles: LinkedIn company page, Crunchbase, Sortlist (EU buyers), TechBehemoths. The agent prepares copy; the owner pastes. |
| Weekly | One founder LinkedIn post from the founder's own profile (not three drafts). |
| Monthly | One founder article for a QA community or publication (e.g. Ministry of Testing). The agent drafts; the founder edits and adds real experience. |
| Monthly | Ask one client or partner for a link to the published case study or a written testimonial. |
| Fill | Expert-quote requests (Qwoted, Featured.com, SourceBottle for AU/NZ). |
| When ready | Loopsy launch (Product Hunt + AI-tool directories). |
| Dropped | Video testimonials (written ones are enough); cold backlink pitches. |

### Runbook rule changes
- **Never-idle → never-wasted.** With no eligible PR work, the agent does auto-lane quality work, drafts next week's off-page asset, or writes next week's PR as a draft. It does **not** refill the content backlog to a count.
- **Backlog refill source:** Search Console evidence or owner-approved ideas only.
- Keep: open-PR cap (lower to **2**), stall alert, never merging its own PRs, all guardrails.

### KPIs by Jan 29, 2027
| KPI | Target |
|---|---|
| Priority pages indexed (home, services + 4 service pages, `/pricing/`, `/offshore-qa/`, `/faq/`, e-commerce) | All; index rate of everything else tracked as a quality signal |
| Non-brand impressions (Search Console) | Rising month on month |
| Clicks from target countries (Search Console country filter) | First clicks from UK, US, AU |
| Clutch/GoodFirms reviews | Decision on 2026-11-30; 2 by Jan 29 if requests go out in early December |
| Referring domains | +5–10 (profiles, reviews, 1–2 editorial) |
| Qualified enquiries from organic | Tracked monthly (GA4 form-submit event; add one if missing) |
| Brand queries | #1 (aspiration, not a business KPI) |

### Removed from the old Phase 6
Region pages for AU/NZ, Canada and Singapore (→ `/offshore-qa/`) · industries hub, gaming, fintech, AI/LLM and on-demand pages · `/tools/qa-cost-calculator/` as a separate URL (→ `/pricing/`) · `/engagement-models/` (→ `/pricing/`) · posts: onboarding (folded into W2), API testing, gaming, peak season (→ 2027), fintech, mobile checklist, contract checklist, regression strategy, Playwright vs Cypress vs Selenium, pricing models · 3 date-bump refresh passes · FAQ schema on 5 pages · blind CTR rewrite.

---

## Appendix A — candidate targets for the demand-led weeks
Unvalidated until Search Console or Keyword Planner data exists.
- Commercial: offshore QA testing services · QA outsourcing company (homepage/services, not a post) · dedicated QA engineers · QA staff augmentation · managed QA testing services · test automation services · API testing services (page, if delivered) · mobile app testing services (page, if delivered).
- Buyer posts: offshore vs in-house QA for a Series A startup · managed QA vs staff augmentation (rewrite of the existing models post without the CTH framing, if D2 allows) · moving from in-house QA to offshore without slowing CI/CD · what to put in a QA outsourcing contract.
- Country page (only with evidence): Australia/NZ first, if Search Console shows AU impressions.
