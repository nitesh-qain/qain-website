# Daily SEO Runbook (run by the 1 AM scheduled agent)

This is the exact procedure to follow on each daily run. Read [PLAN.md](PLAN.md) first.

## 1. Pick today's task(s)
Read `seo/PLAN.md` top to bottom. Take the first unchecked `[AUTO]` or `[PR]` task. Skip `[NEEDS-YOU]` tasks but note any you pass over in today's report as a reminder. Do one task per run unless it's small enough to safely pair with the next (e.g. robots.txt + sitemap.xml).

## 2. If it's an `[AUTO]` site/technical task
1. Make the change directly in the working tree on `main`.
2. This routine runs in a headless cloud sandbox (Bash/Read/Write/Edit/Glob/Grep only — no GUI browser tool). Verify with a real headless browser via Bash, not just HTTP status codes:
   - `npx --yes playwright install --with-deps chromium` once per run (or reuse if cached), then run a small throwaway Node/Playwright script (write it to a temp file, don't commit it) that: starts `python3 -m http.server 4173` in the repo root in the background, then for every page (`index.html`, everything under `case-studies/`, and any new pages added) opens it in headless Chromium and checks (a) the page loads with HTTP 200 and no uncaught console errors/exceptions, (b) every internal `<a href>` on the page resolves to an existing local file (no dead links), (c) key interactive elements for the change (nav links, contact form fields, FAQ toggles, CTA buttons, calendar link) are present and clickable without throwing, (d) the page renders at a mobile viewport (375x812) without obvious overflow/console errors.
   - If the change touches head/meta/schema, also validate the JSON-LD blocks parse as JSON (`python3 -m json.tool`) and that title/meta description tags are present and non-empty.
   - If Playwright cannot be installed in the sandbox (no network access to npm, etc.), fall back to: `python3 -m http.server` + `curl -o /dev/null -s -w "%{http_code}"` against every page and every internal link found via `grep -oE 'href="[^"]+"'`, plus the JSON validity checks above. Note in the day's report that only HTTP/static checks ran, not a real browser pass, so the user should double-check visually that morning.
3. **If verification fails:** fix the issue and re-run step 2. Allow up to 2 fix-retry cycles. If still failing, revert the change (`git checkout -- <files>` or equivalent), leave the PLAN.md task unchecked, and write the failure reason in today's report. Do not push.
4. **If verification passes:** `git add` the specific files, commit (message describing the change, ending with the required `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>` line), and push directly to `main`. Vercel auto-deploys.
5. Check off the task in `PLAN.md` with the date and short commit SHA, and add a line to the Change Log section.

## 3. If it's a `[PR]` content/blog task
1. Research first: use web search for (a) what competing QA-outsourcing vendors targeting UK/AU/APAC buyers are publishing, and (b) any recent, relevant QA/AI-testing news worth referencing for timeliness. Keep it grounded — don't fabricate stats, sources, or client names.
2. Write the post as a real page matching the site's existing design system (reuse the head/meta/schema pattern established in Phase 1 once it has landed). Save it under `blog/<slug>.html` (create the `blog/` directory and a `blog/index.html` listing on the first post).
3. Create a branch named `seo/blog-<slug>`, commit the draft there, push the branch.
4. Open a PR (`gh pr create`) with: the rendered post content, target keyword(s)/positioning note, and a one-line summary of the research angle. **Do not merge.**
5. In `PLAN.md`, update the task line to `PR opened: <link> — awaiting review` (don't check it off — that only happens once you merge it yourself).

## 4. If it's a `[AUTO]` research-only task (Phase 3)
No site changes. Run the web research, then append findings directly into the `Content Backlog` section of `PLAN.md` (new candidate blog topics, keyword notes) so Phase 4 has fresh material. If findings suggest a new `[AUTO]` or `[PR]` task worth prioritizing, add it to the relevant phase list.

## 5. Always: write the daily report
Create `seo/reports/YYYY-MM-DD.md` with:
- **Shipped today** — task, files changed, commit link (if pushed to main)
- **Opened for review** — PR links awaiting merge (blog posts)
- **Blocked / not shipped** — task + why verification failed, what was tried
- **Research findings** — competitor content gaps, relevant tech/QA news, new keyword ideas (if a Phase 3 day)
- **LinkedIn draft** — if today's work produced a blog post or notable milestone, include a ready-to-post LinkedIn draft in the report (never post it — the user posts manually)
- **Reminders** — any `[NEEDS-YOU]` items skipped

End the run by sending a short chat message to the user summarizing the day in 2-3 sentences with a link to the report and any PR(s).

## Target flow: PRs + merge gate (built 2026-09-23, NOT YET ACTIVE)

This is the intended end-state from the nightly-agent rebuild, per the owner's spec. The infrastructure below is fully built and tested against real historical commits, but **steps 2 and 3 above still push straight to `main`** — that hasn't been switched over yet. Do not change that push behavior based on this section alone; it needs one more explicit go-ahead from the owner, since flipping it changes how every future run behaves starting that same night. If/when that's given, this section's steps replace step 2.4 and step 3.3-3.4 above, and this note gets deleted.

**What's already built and live in the repo:**
- `.github/CODEOWNERS` — forces @nitesh-qain review on `index.html`, `robots.txt`, `vercel.json`, and `.github/` itself, regardless of what the gate below decides.
- `seo/scripts/gate_classify.py` — rule-based (not LLM) classifier. Diffs the PR against `main`, applies PLAN.md's AUTO vs REVIEW rules (new/deleted files, title/H1/canonical/nav/robots/hreflang/redirect/pricing changes, new client-name mentions outside JSON-LD blocks, >5 or >20 files changed), outputs `{"verdict": "auto"|"review", "reasons": [...]}`. Tested against 3 real historical commits (`44e2471`, `8b5ffb2` correctly classify AUTO; `76a0ab9`, `f03f987..d5744b5` correctly classify REVIEW).
- `.github/workflows/seo-gate.yml` — runs the classifier on every PR into `main`, comments the verdict, and for AUTO-eligible PRs, approves + queues auto-merge. For REVIEW PRs, does nothing further — branch protection (once enabled) blocks merge until @nitesh-qain approves.
- `.github/workflows/seo-reviewer.yml` — the independent second check. Sends the raw diff (never the worker's own reasoning) to Claude, checks for broken-looking links, invalid JSON-LD, and visible-text changes that look bigger than an additive SEO edit. Blocks AUTO-lane auto-merge on failure; never blocks the owner's own manual merge of REVIEW-lane PRs. **Currently skips itself** — needs the `ANTHROPIC_API_KEY` repo secret before it does anything (reminder scheduled for 2026-09-24 2:30pm IST to gather this + 3 other LLM keys).
- Repo settings changed to make the above possible: `allow_auto_merge` and Actions' `can_approve_pull_request_reviews` were both off by default and are now on.

**What's still needed to actually activate this:**
1. Branch protection on `main` — require a PR, require 1 approval, require the `seo-gate` and (once the API key exists) `seo-reviewer` status checks. Not yet enabled.
2. This RUNBOOK's steps 2.4 and 3.3-3.4 need rewriting so the worker pushes to a branch (e.g. `seo/auto/<date>` or `seo/review/<slug>`) and opens a PR instead of pushing straight to `main`.
3. Explicit owner confirmation to flip both of the above on the same night, since before that point every `[AUTO]` push still goes straight to `main` with no gate at all.

## Guardrails (do not deviate)
- Never push to `main` without a passing verification pass per step 2.3.
- Never merge a blog PR — that is always the user's action.
- Never create third-party accounts (Clutch/GoodFirms/G2/LinkedIn) — those are `[NEEDS-YOU]`.
- Never fabricate client names, testimonials, statistics, or press mentions in blog content.
- One task focus per run — don't silently expand scope beyond what PLAN.md lists.
