# Competitor Research Runbook (run by the monthly scheduled agent)

This agent's job is strictly read-and-propose. It must **never** edit, commit, or push any file on the live site. The only files it may ever touch are `seo/COMPETITOR-IDEAS.md` and its own `seo/reports/competitor-YYYY-MM-DD.md` report. If a run notices something on qainfinity.com it wants to fix directly, it does not fix it — it writes a row in COMPETITOR-IDEAS.md instead and leaves the site alone.

## Guardrails (do not deviate)

- **Never** edit, create, or delete any repo file except `seo/COMPETITOR-IDEAS.md` and `seo/reports/competitor-YYYY-MM-DD.md`. No exceptions, even for a "tiny" or "obviously correct" site fix — that's the daily SEO agent's job, and only after the owner approves the idea here.
- **Never** copy a peer's text verbatim or near-verbatim. Describe the pattern or mechanism in your own words; "our version" in each row must be written fresh for QAInfinity, not adapted/reworded from the peer's copy.
- **Never** propose a claim, certification, award, client name, testimonial, or statistic QAInfinity doesn't actually have. If a peer's page works *because* of something we lack (a named client logo, an ISO/SOC2 cert, a review-platform badge, a DPA template), the idea row should describe the general pattern, and the missing ingredient goes under Prerequisites phrased as "worth getting" — never fabricated to make the idea look ready.
- **Never** create third-party accounts, sign up for trials, or submit any form on a peer's site.
- Commit and push directly to `main` — this is a documentation-only change (same category as `seo/PLAN.md` updates in the main RUNBOOK), so no browser-verification pass is needed. Just confirm the markdown table you wrote is well-formed (consistent column counts) before pushing.

## 1. Is this run a real first-Monday fire?

Cron fires this routine weekly (every Monday) because standard cron can't express "first Monday of the month" directly. Check today's date in IST (`TZ=Asia/Kolkata date +%d`). If the day-of-month is **not** between 01 and 07, this is not actually the first Monday — exit immediately, write nothing, touch nothing. Do not write a report for a skipped fire.

## 2. Full audit procedure

Every real fire (the first-ever run, and every first Monday thereafter) runs the same procedure — there's no separate lighter "change-check" mode; at monthly cadence, a fresh look each time is cheap enough to just always do the full pass.

1. **Re-verify the Verified Peer List** in `seo/COMPETITOR-IDEAS.md`. For each peer, a quick check (WebFetch the homepage, or WebSearch if the site is down) that: the site is still live, still reads as India-run, and still has a real US presence. Note anything changed (rebrand, acquisition, site gone, no longer India-run) in the report — don't silently edit the table without flagging it.
2. **For each verified peer**, review (via WebFetch/WebSearch — this sandbox has no GUI browser tool):
   - Service pages — structure, naming, depth, what's bundled vs. split out
   - US-buyer-specific pages — regional pages, time-zone framing, compliance language
   - Trust signals — certifications, client logos, review-platform badges (Clutch/GoodFirms/G2), team/leadership depth
   - Case studies — format, specificity, metrics shown, how client consent/anonymity is handled
   - FAQ / comparison / industry-vertical pages
   - AI-search structure — JSON-LD schema types in use, FAQ schema, `llms.txt`, how cleanly content answers a direct question (AEO)
   - Lead-capture offers — anything beyond a plain contact form (free assessments, calculators, guides, estimators)
3. **Compare against the current state of qainfinity.com** — read the live repo files directly (this part needs no WebFetch, it's already checked out).
4. **For every genuinely new idea** — a pattern two or more peers use that QAInfinity doesn't have, or one peer uses particularly well and it's a good fit — add a row to the Ideas table in `seo/COMPETITOR-IDEAS.md` per its schema. Do not re-propose a row that's already `Proposed`/`Approved`/`Skip`/`Turned into task` from a prior audit unless the idea has materially changed (note what changed if you do).
5. **Score every new row** using the Fit / Impact / Effort rubric defined at the top of `seo/COMPETITOR-IDEAS.md`. Compute Priority = Fit × Impact ÷ EffortWeight (S=1, M=2, L=3).
6. Set every new row's `Status` to `Proposed`. Never set `Approved` or `Skip` yourself — that's the owner's call, made by editing the file between runs. Leave existing `Approved`/`Skip`/`Turned into task` rows untouched unless a factual update is needed (e.g., the peer example went offline) — note any such edit in the report.
7. Write `seo/reports/competitor-YYYY-MM-DD.md` (real current IST date) covering:
   - **Peer list changes** (if any — or "none")
   - **New ideas proposed this run** (table or list, with Priority scores, highest first)
   - **Still awaiting your call** — a short list of `Proposed` rows from *prior* audits that haven't been marked yet, so nothing silently ages out of view
   - It is a fully valid outcome to find nothing new — don't pad the table with weak ideas just to have something to show.
8. Commit `seo/COMPETITOR-IDEAS.md` and the day's report, push to `main`.
9. Finish with a short chat message (2-3 sentences): how many new ideas, the top 1-2 by Priority, and a link to the report.

## 3. Relationship to the daily SEO agent

This agent never writes to `PLAN.md` and never touches site files. Turning an `Approved` idea into an actual task is the daily SEO agent's job — see the "Competitor ideas" step in [RUNBOOK.md](RUNBOOK.md). Keep the two runbooks' guardrail sections in sync if either changes (e.g., if the no-fabrication rule is tightened, update both).
