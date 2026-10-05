# Competitor Research Report — 2026-10-05

First Monday of the month, first full audit run of this routine. Full procedure per [COMPETITOR-RUNBOOK.md](../COMPETITOR-RUNBOOK.md): re-verify the peer list, review each peer's site, compare against the current qainfinity.com, propose new ideas.

**Methodology note:** this sandbox's network egress proxy blocked direct WebFetch to every one of the six peer domains (bugraptors.com, indium.tech, impactqa.com, cigniti.com, thinksys.com, kiwiqa.com.au and siblings) for every sub-agent, on every attempt. All findings below come from WebSearch (search snippets, cached page text, third-party directories like Clutch/GoodFirms/Crunchbase/Glassdoor, and independent press coverage) rather than direct page loads. Where a finding couldn't be independently corroborated, it's marked as such rather than asserted as fact. Recommend a follow-up pass with working WebFetch access to these domains to confirm schema/llms.txt specifics with certainty.

## Peer list changes

- **Cigniti Technologies — removed from the verified peer list.** Acquired and dissolved into Coforge Limited via an NCLT-sanctioned amalgamation effective May 5, 2026; delisted from BSE/NSE (1:1 share exchange, completed June 2026). cigniti.com reportedly now shows a "Cigniti is now a Coforge company" banner redirecting to Coforge's own site. It's no longer an independently operating India-run QA company. **The verified list is down to 5 peers** (BugRaptors, Indium Software, ImpactQA, ThinkSys, KiwiQA) until a replacement is sourced and vetted on a future audit.
- **Indium Software — ownership/positioning shift, kept on the list.** Rebranded from "Indium Software" to "Indium" (March 2025); BPEA EQT, a global private-equity firm, acquired a majority stake in December 2023, with a new external Chairman and EQT partners now on the board. Quality Engineering is now one of four pillars (alongside Agentic AI, Data & Analytics, Application Engineering) rather than the company's lead identity. HQ and day-to-day leadership remain India-based, so it still qualifies as India-run on substance — flagging for context since it's no longer purely founder/India-owned.
- **BugRaptors and ImpactQA — both show a "US-headquartered" marketing drift,** without any underlying structural change (same founders/ownership/India delivery centers). Noted for pattern-tracking; neither disqualifies them this run.
- **ThinkSys's existing caveat (positions primarily as a US company, India framed as delivery/R&D) re-checked and found unchanged-to-stronger** — no softening since it was first flagged.
- **KiwiQA's existing caveat (Sydney-forward positioning) re-checked and found stronger** — it now runs four-plus regional domains, with third-party profiles listing HQ as Sydney, Australia. The original India-founder story is still told on the .com.au "Our Philosophy" page, just demoted. Kept on the list, still weighted lower than the others.

Full detail and updated notes are in the Verified Peer List table in [COMPETITOR-IDEAS.md](../COMPETITOR-IDEAS.md).

## New ideas proposed this run (9), highest Priority first

| Priority | Idea | Fit | Impact | Effort |
|---|---|---|---|---|
| 15 | Fix `areaServed: "IN"` in the Contract-to-Hire page's Service schema | 5 | 3 | S |
| 15 | Standalone dedicated FAQ page (`/faq/`) | 5 | 3 | S |
| 12 | Dedicated Compliance & Accessibility Testing service page | 4 | 3 | S |
| 10 | Industry vertical landing page — Gaming / Real-Money Gaming | 5 | 4 | M |
| 10 | Dedicated pages for "Dedicated QA Engineers" and "Performance & Security Testing" | 5 | 4 | M |
| 10 | Establish a third-party review-platform presence (Clutch, GoodFirms) | 2 | 5 | S |
| 8 | Interactive "QA Outsourcing Cost Calculator" (second lead magnet) | 4 | 4 | M |
| 7.5 | Industry vertical landing page — E-commerce / Retail | 5 | 3 | M |
| 6 | Film video testimonials from existing named clients | 3 | 4 | M |

Full write-up of each (seen-on, why it works, our version, prerequisites) is in the Ideas table in [COMPETITOR-IDEAS.md](../COMPETITOR-IDEAS.md), rows 1-9.

Two patterns came up repeatedly across peers but were deliberately **not** proposed as rows:
- **Displayed ISO/SOC2-style certifications** — three of five peers lean on this, but QAInfinity doesn't hold a certification today and inventing or implying one isn't on the table. Worth a business-side look at whether pursuing a real certification is worthwhile, but that's a decision for the owner, not a content idea.
- **llms.txt** — no peer could be confirmed (or denied) to have one given the egress block, so this isn't a verified "peers have it, we don't" gap this run. Worth revisiting once a peer is confirmed to have one, or on its own merits independent of peer comparison.

## Still awaiting your call

This is the first-ever audit, so there are no `Proposed` rows from a *prior* run aging in the queue — all 9 rows above are new as of today. Nothing older to flag.

## Peer-by-peer notes (condensed)

- **BugRaptors** — still live, same founders/ownership. Has `/verticals/` industry pages (Banking & Finance, Healthcare), a gated eBook library, a standalone FAQ page, branded tooling ("RaptorVista," "MoboRaptors"), a large blog archive, a news/press page, claimed ISO 9001/27001 certs, and Clutch/GoodFirms/Glassdoor/Trustpilot profiles.
- **Indium** — ownership/rebrand as above. Has a dedicated Compliance Testing page, industry verticals (BFSI, Healthcare, Retail, Manufacturing), separate pages per QA sub-service, branded tooling ("iAccelerate" suite, "uphoriX"), and Everest Group analyst recognition (enterprise-scale, not replicable at QAInfinity's size).
- **ImpactQA** — unchanged structurally, US-HQ framing growing. Strongest logo wall of the set (Panasonic, Coinbase, Starbucks, Axis Bank, KPMG, Honda, and more), 8-10+ named case studies with hard metrics, active Clutch (4.6) and GoodFirms (4.6) profiles, named video testimonials plus a YouTube channel, an `/industries/` hub, and separate pages for narrow specialties (SAP/Oracle/ERP, blockchain, medical-device testing).
- **Cigniti** — removed, see above.
- **ThinkSys** — caveat unchanged/stronger. Has a standalone `/faqs/` page, a named "Zero Critical Bugs Guarantee" with its own page and press release, claimed ISO 27001/CMMI Level 3 certs, a live "QA ROI Calculator," an `/industries/` hub (Fintech, InsureTech, Healthcare, Retail, Travel, AdTech, eLearning, Gaming), and several named case studies with hard metrics (Boostlingo, WorkMarket by ADP, Rise Pay).
- **KiwiQA** — caveat stronger (multi-domain, Sydney-forward). Runs four-plus regional domains, branded tooling ("K-FAST," "K-SPARC"), industry verticals (Fintech, Healthcare, Gaming), separate Performance/Security Testing pages plus a distinct "Managed QA" offering, claimed ISO certs, Clutch/GoodFirms profiles, named enterprise case studies (DP World, Navidium), and a dedicated video-testimonials page.

Recurring, cross-peer patterns that drove the proposed ideas: **industry vertical landing pages** (all five remaining peers have them), **third-party review-platform presence** (all five have it, QAInfinity has none), and **splitting sub-services into their own pages** (three of five do this; QAInfinity already does it for two of its four services but not the other two).
