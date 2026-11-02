# Competitor Research Report — 2026-11-02

Second full monthly audit, and the first run under the new weekly-fire/first-Monday-only schedule (today, 2026-11-02, is the first Monday of November). Procedure followed per [COMPETITOR-RUNBOOK.md](../COMPETITOR-RUNBOOK.md).

## Environment note

Direct `WebFetch` to every peer domain (bugraptors.com, indium.tech, impactqa.com, thinksys.com, kiwiqa.com.au) was blocked by this session's network policy (DNS resolution failures) — this sandbox apparently doesn't have those hosts on its allowed outbound list this run. All peer research below was done via `WebSearch` only, which returns search-snippet-level summaries rather than full rendered pages. This is a lighter-touch check than a normal run: good enough to catch headline changes (acquisitions, rebrands, major new sections) and to confirm page *existence*, but not as thorough as reading full page content. Flagging this so a future run with working `WebFetch` can do a deeper pass.

## Peer list changes

No structural changes. All 5 active peers (BugRaptors, Indium, ImpactQA, ThinkSys, KiwiQA) came back in search results as live, with India-origin framing and US-presence details unchanged from the 2026-10-05 audit — no new acquisition, rebrand, or site-down signal surfaced this round.

**Replacement search for the 5th/6th slot (list has been down to 5 since Cigniti's removal):** checked two candidates this round, both excluded —
- **QA InfoTech** (Noida, founded 2003, Michigan office) — would have been a strong fit, but PitchBook/LinkedIn show it was acquired into **Qualitest** around Feb 2021 and no longer operates independently. Same disqualifying shape as Cigniti.
- **CresTech Global Business Solutions** (Delhi/NCR, India-founded) — no confirmed US office address turned up in this round's search. Not ruled out permanently; worth checking crestechglobal.com directly next time `WebFetch` is working.

Both added to the "Candidates considered and excluded" table in COMPETITOR-IDEAS.md. List stays at 5 verified peers.

## New ideas proposed this run (highest Priority first)

| # | Idea | Priority | Fit | Impact | Effort |
|---|---|---|---|---|---|
| 10 | "How to evaluate a QA outsourcing partner" buyer's-guide checklist post (BugRaptors/KiwiQA run "Top X testing companies" listicles — our version is an honest evaluation checklist, not a self-ranking) | 15 | 5 | 3 | S |
| 11 | Downloadable gated PDF guide repackaging existing blog content, as a second/lighter lead magnet alongside the Release Readiness Assessment (BugRaptors runs gated ebooks) | 7.5 | 5 | 3 | M |
| 12 | Formal process/security certification badge (e.g. ISO 27001) — flagged with a Prerequisite, since QAInfinity doesn't hold one today; BugRaptors and ThinkSys both lead with ISO/CMMI certs | 6 | 2 | 3 | S |

All three are written from content/criteria QAInfinity already has or controls; #12 explicitly can't be built until a real certification exists (no claim goes on-site before then).

## Still awaiting your call

From the 2026-10-05 audit, two rows remain `Parked` on dates already in the table — not stale, just not due yet:
- **#6** (Clutch/GoodFirms review-platform presence) — parked until 2026-11-30
- **#9** (video testimonials from named clients) — parked until 2026-11-30

Everything else from the first audit has already been dispositioned (Approved/Skip/Turned into task — see the 2026-10-30/31 change log entries). No rows are silently aging without a decision.

## This run's new rows

- **#10, #11, #12** — `Proposed`, awaiting your call.
