# QAInfinity SEO Plan & Daily Backlog

**Positioning target:** trusted QA/testing outsourcing partner for buyers *outside* India, US, and the Middle East — primarily UK/EU, Australia/NZ, Canada, and APAC companies who outsource QA work.

**How this file works:** the 1 AM daily automation reads this file top to bottom and works the first unchecked `[ ]` task(s) it finds, in order, unless marked `[NEEDS-YOU]` (those are skipped — they require an account/login only the site owner has, and are just flagged in the daily report as reminders). When a task ships it's checked off with the date and commit/PR link. New tasks discovered during research days get appended to the bottom of the relevant phase. Re-prioritize anytime by editing this file directly — the automation always re-reads it fresh each run.

**Task tags:**
- `[AUTO]` — automation makes the change, verifies the site still works (preview server + browser checks), and if verification passes, pushes straight to `main` (auto-deploys via Vercel). If verification fails, it fixes and retries; if still failing, it reverts and leaves the task unchecked with a note in the day's report — nothing broken ships.
- `[PR]` — automation drafts content on a branch and opens a GitHub PR. Never merges it. Goes live only after you review and merge.
- `[NEEDS-YOU]` — requires an action only you can take (creating an account, verifying domain ownership, posting to LinkedIn). Automation will not attempt these; they stay listed as reminders.

---

## Phase 1 — Technical SEO foundation

- [ ] `[AUTO]` Fix document structure on all 5 pages: add `<!DOCTYPE html>`, `<html lang="en">`, `<head>`, `<body>` wrapper (currently missing sitewide), `<meta charset="utf-8">`, `<meta name="viewport">`. Verify no visual regression on desktop + mobile.
- [ ] `[AUTO]` Add unique `<meta name="description">` and canonical `<link>` tag per page (5 pages).
- [ ] `[AUTO]` Add Open Graph + Twitter Card tags per page (title, description, image, url) so links preview correctly on LinkedIn/Slack/X.
- [ ] `[AUTO]` Add JSON-LD structured data: `Organization` sitewide, `FAQPage` on the homepage FAQ section, `Article` on each case study.
- [ ] `[AUTO]` Add JSON-LD `Review`/testimonial markup for the homepage testimonials section.
- [ ] `[AUTO]` Create `robots.txt` and `sitemap.xml`, verify all 5 URLs resolve with no broken internal links or 404s sitewide.
- [ ] `[NEEDS-YOU]` Verify site ownership in Google Search Console and submit `sitemap.xml` (needs your Google login).
- [ ] `[AUTO]` Basic Core Web Vitals pass — check the animated gradient/glow CSS isn't hurting LCP/CLS on mobile.

## Phase 2 — Information architecture

- [ ] `[AUTO]` Build `/services/` hub + 4 dedicated service pages (Manual & Automation Testing, AI-Powered Test Automation, QA Staffing & Contract-to-Hire, Performance & Security Testing) — each currently just a 2-line card on the homepage, not indexable on its own.
- [ ] `[AUTO]` Build a real `/about` page — team credentials, certifications, and explicit time-zone-overlap messaging for UK/AU/APAC buyers.
- [ ] `[AUTO]` Add an `/industries` or use-case page set (fintech, iGaming — reuse the existing real-money-gaming case study, SaaS).

## Phase 3 — Research (no site changes, findings feed Phase 4)

- [ ] `[AUTO]` Competitor content scan: what are other QA-outsourcing vendors (targeting UK/AU/APAC buyers, not India/US directories) publishing? Identify content gaps. Findings appended below.
- [ ] `[AUTO]` Tech/QA news scan: recent developments in AI-driven testing, QA outsourcing trends — identify timely blog angles. Findings appended below.
- [ ] `[AUTO]` Keyword shortlist for target geos (UK/EU/AU/APAC QA outsourcing intent), append to Content Backlog below.

## Phase 4 — Content / blog (each post = its own day, always `[PR]`)

- [ ] `[PR]` Blog: "In-House vs. Outsourced QA: A Cost and Risk Comparison for Startups"
- [ ] `[PR]` Blog: "What Is Contract-to-Hire QA Staffing (and Why It Reduces Hiring Risk)"
- [ ] `[PR]` Blog: "How AI QA Agents Cut Regression Testing Time by 90% — Lessons from the Angara Case Study"
- [ ] `[PR]` Blog: "A Buyer's Guide to QA Outsourcing Time Zones: Working Across UK/AU/APAC Hours"
- [ ] `[PR]` Blog: "Performance Testing Checklist Before Your Next Product Launch"
- [ ] *(more topics to be appended after the Phase 3 research day)*

## Phase 5 — Off-page authority (mostly `[NEEDS-YOU]`)

- [ ] `[NEEDS-YOU]` Create and verify company profile on Clutch, GoodFirms, G2 (needs your account/company verification).
- [ ] `[NEEDS-YOU]` Solicit client reviews on the above platforms for existing case-study clients.
- [ ] `[AUTO]` (draft only) LinkedIn post drafts accompanying each shipped blog post — included in that day's report for you to post manually.

---

## Content Backlog (research findings land here)

*(populated by Phase 3 research days)*

## Change Log

*(each shipped/opened item gets one line here: date — task — commit SHA or PR link)*
