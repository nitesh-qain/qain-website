# Daily SEO Runbook (run by the 1 AM scheduled agent)

This is the exact procedure to follow on each daily run. Read [PLAN.md](PLAN.md) first.

## 1. Pick today's task(s)
Read `seo/PLAN.md` top to bottom. Take the first unchecked `[AUTO]` or `[PR]` task. Skip `[NEEDS-YOU]` tasks but note any you pass over in today's report as a reminder. Do one task per run unless it's small enough to safely pair with the next (e.g. robots.txt + sitemap.xml).

## 2. If it's an `[AUTO]` site/technical task
1. Make the change directly in the working tree on `main`.
2. Start the local preview: `preview_start {name: "qain-website"}` (serves the repo at `http://localhost:4173`).
3. Verify, using the browser tools — not assumptions:
   - Load `index.html` and every page under `case-studies/` (and any new pages added). Check `read_console_messages` for JS errors.
   - Click through primary nav links, footer links, and all internal `<a href>` targets — confirm none 404 (`read_network_requests` / status check).
   - Exercise key interactive elements relevant to the change (buttons, the contact form fields, FAQ section, calendar link) via `read_page` + `computer`.
   - Check mobile viewport with `resize_window {preset: "mobile"}` and re-check for layout breakage or console errors.
   - If the change touches head/meta/schema, sanity-check the JSON-LD is valid (no malformed JSON) and title/description tags render.
4. **If verification fails:** fix the issue and re-run step 3. Allow up to 2 fix-retry cycles. If still failing, revert the change (`git checkout -- <files>` or equivalent), leave the PLAN.md task unchecked, and write the failure reason in today's report. Do not push.
5. **If verification passes:** `git add` the specific files, commit (message describing the change, ending with the required `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>` line), and push directly to `main`. Vercel auto-deploys.
6. Check off the task in `PLAN.md` with the date and short commit SHA, and add a line to the Change Log section.

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
