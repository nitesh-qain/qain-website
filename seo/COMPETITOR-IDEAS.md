# Competitor Content & Structure Ideas

Maintained by the Competitor Research agent (procedure: [COMPETITOR-RUNBOOK.md](COMPETITOR-RUNBOOK.md)). This agent **never edits, commits, or pushes anything on the live site** — Bash/Read/Write access is restricted in its routine config, but the real guardrail is this: it only ever writes to this file and its own `seo/reports/competitor-*.md` reports. It proposes; you decide.

**How to use this file:** each row under Ideas is one proposal. Set its `Status` cell to `Approved` or `Skip`. On its next run, the daily SEO agent ([RUNBOOK.md](RUNBOOK.md)) scans for `Approved` rows and turns each into a task in `PLAN.md` (tagged `[AUTO]`/`[PR]`/`[NEEDS-YOU]` per the normal rules), then flips this row's Status to `Turned into task` with a link. `Skip` rows are never re-proposed as-is; a genuinely new variant of a skipped idea can still show up later as a new row.

---

## Verified Peer List

6–8 India-run QA/testing firms with a real, verifiable US presence. "India-run" means founded and/or substantively operated from India — not a US (or other) company that merely outsources delivery work to an India office. "Real US presence" means a specific, checkable US address/entity, not just a marketing claim of "global coverage." Re-spot-checked at the top of each monthly audit (sites get acquired, pivot, or relaunch); this table is that audit's starting point, not re-derived from scratch every time.

| Peer | India origin | Real US presence | Notes |
|---|---|---|---|
| [BugRaptors](https://www.bugraptors.com) | Founded 2016 by R P Singh & Yashu Kapila, Mohali, Punjab — HQ and leadership based in India | Corporate office: 5858 Horton Street, Suite 101, Emeryville, CA 94608 | Clearest fit of the set — dual-HQ company that is genuinely run out of India with a real US corporate entity. |
| [Indium Software](https://www.indium.tech) | HQ Chennai (Eldams Road, Teynampet) | Offices in Cupertino CA, Princeton NJ, Johns Creek GA | Larger, more established India-run testing/engineering firm; broader service line than pure QA. |
| [ImpactQA](https://www.impactqa.com) | Founded 2011 by Jyoti Prasad Bhatt, incorporated in India; India delivery centers in Chennai and Bengaluru | Office in Houston, TX (13201 Northwest Fwy Suite 800); also markets a NYC address | India-founded, has since built out real US offices rather than just claiming them — opened its first US office (Dallas) in 2016. |
| [Cigniti Technologies](https://www.cigniti.com) | Founded 1998, HQ Hyderabad; publicly listed in India (BSE/NSE) | Office in Irving, TX (433 E Las Colinas Blvd, Suite #1240) | Largest/most established name on this list — a useful "what does a mature India-run QA firm's site look like at scale" reference, even though their target buyer skews larger-enterprise than QAInfinity's. |
| [ThinkSys](https://thinksys.com) | Founded 2012 by Rajiv Jain; ThinkSys Software Private Limited incorporated in India; Noida office | HQ address given as Sunnyvale, CA (440 N Wolfe Road, Suite #22) | **Caveat:** publicly positions itself primarily as a US company ("based in Sunnyvale") with India framed as an "R&D wing" rather than the operational core — included because the entity is Indian-incorporated and the founder appears India-based, but verify this one yourself if it matters for a specific idea you're borrowing from them. |
| [KiwiQA](https://www.kiwiqa.com.au) | Founded 2009 in Ahmedabad, India by Niranjan Limbachiya | US office: 505 Ellicott St, Buffalo, NY 14203 | **Caveat:** founded and originally based in India, but current primary marketing HQ is positioned as Sydney, Australia (separate .com.au / .co.uk / .com properties per region) — India-origin but no longer clearly "India-run" day to day. Included for the founder history and the real US office; weight its ideas a bit lower than the four above. |

### Candidates considered and excluded

| Candidate | Why excluded |
|---|---|
| QASource | Founded 2002 in Silicon Valley by Rajeev Rai (ex-Apple/IBM/Adobe) specifically to run US-side; a small India team in Chandigarh was *hired* to do delivery work. This is a US company with an India delivery arm, not an India-run company — the inverse of what we're looking for. |
| QA Mentor | Founded 2010 in New York by Ruslan Desyatnikov. India is one of 11 global "testing operation centers" alongside Ukraine, Canada, UK, etc. — not the operational core. |
| TestingXperts | Traces back to Damco (1996, US/India software testing arm), rebranded 2013–2014 under Manish Gupta. Now a genuine multinational (13 offices: US, UK, Canada, Netherlands, South Africa, UAE, Singapore, India) — India is one of several large delivery hubs rather than a distinctly "India-run" identity. Ambiguous enough that I left it out rather than force a fit; revisit if you disagree. |
| QualiZeal | Founded 2021, explicitly positions as "US-based" (Irving, TX HQ) with India as its first Global Delivery Centre — same shape as QASource, just newer. |

*(Original candidate list from the brief: ImpactQA, BugRaptors, ThinkSys, TestingXperts, QA Mentor, QASource, Indium Software, KiwiQA. Cigniti Technologies was added to replace the three excluded above and keep the verified list at 6.)*

---

## Scoring

Every idea gets three scores, set by the agent:

- **Fit (1–5)** — how well the idea matches what QAInfinity can honestly claim *today*, with zero new certifications, clients, or capabilities invented to make it work. 5 = buildable now with existing facts; 1 = would require something we don't have (see Prerequisites).
- **Impact (1–5)** — expected SEO/AEO/trust-signal value if built. 5 = fills a real, visible gap versus multiple peers on a high-intent page type (service/comparison/FAQ pages buyers actually read before contacting); 1 = marginal or cosmetic.
- **Effort** — `S` / `M` / `L`, rough build size (S ≈ a few hours, M ≈ a day, L ≈ multi-day/new page type).

**Priority** = Fit × Impact ÷ EffortWeight (S=1, M=2, L=3), sorted highest first in the table. It's a sort aid to help you scan, not a committee decision — your judgment on Status overrides it.

---

## Ideas

*(Populated by the first full audit — see [COMPETITOR-RUNBOOK.md](COMPETITOR-RUNBOOK.md). Empty until then.)*

| # | Idea | Seen on | What they do | Why it works | Our version | Prerequisites | Fit | Impact | Effort | Priority | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Status legend

- **Proposed** — agent-suggested, awaiting your call.
- **Approved** — you've greenlit it; the daily SEO agent adds a `PLAN.md` task on its next run.
- **Skip** — you passed; not re-proposed in this exact form.
- **Turned into task** — the daily SEO agent added a `PLAN.md` task for this row; see the linked task line.

---

## Change Log

- 2026-10-01 — File created. Verified peer list built and checked (6 peers confirmed India-run with real US presence; QASource, QA Mentor, TestingXperts, and QualiZeal considered and excluded — see table above; Cigniti Technologies added as a replacement). Ideas table awaits the first full audit.
