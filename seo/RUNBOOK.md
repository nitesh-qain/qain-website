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

## Guardrails (do not deviate)
- Never push to `main` without a passing verification pass per step 2.3.
- Never merge a blog PR — that is always the user's action.
- Never create third-party accounts (Clutch/GoodFirms/G2/LinkedIn) — those are `[NEEDS-YOU]`.
- Never fabricate client names, testimonials, statistics, or press mentions in blog content.
- One task focus per run — don't silently expand scope beyond what PLAN.md lists.
