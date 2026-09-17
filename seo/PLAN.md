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

- [x] `[AUTO]` Competitor content scan: what are other QA-outsourcing vendors (targeting UK/AU/APAC buyers, not India/US directories) publishing? Identify content gaps. — done 2026-09-17, see Content Backlog below.
- [x] `[AUTO]` Tech/QA news scan: recent developments in AI-driven testing, QA outsourcing trends — identify timely blog angles. — done 2026-09-17, see Content Backlog below.
- [ ] `[AUTO]` Keyword shortlist for target geos (UK/EU/AU/APAC QA outsourcing intent), append to Content Backlog below. *(next research day — go deeper on search-volume/intent per keyword rather than topic gaps)*

## Phase 4 — Content / blog (each post = its own day, always `[PR]`)

- [ ] `[PR]` Blog: "In-House vs. Outsourced QA: A Cost and Risk Comparison for Startups"
- [ ] `[PR]` Blog: "What Is Contract-to-Hire QA Staffing (and Why It Reduces Hiring Risk)"
- [ ] `[PR]` Blog: "How AI QA Agents Cut Regression Testing Time by 90% — Lessons from the Angara Case Study"
- [ ] `[PR]` Blog: "A Buyer's Guide to QA Outsourcing Time Zones: Working Across UK/AU/APAC Hours"
- [ ] `[PR]` Blog: "Performance Testing Checklist Before Your Next Product Launch"
- [ ] `[PR]` Blog: "Agentic QA in 2026: What Autonomous Test Agents Actually Change for Your Release Cycle" (ties directly to Loopsy; timely trend per 2026-09-17 research)
- [ ] `[PR]` Blog: "QA Outsourcing Isn't One Thing: Managed Team vs. Staff Augmentation vs. Contract-to-Hire — Which Fits Your Stage" (fills a content gap identified 2026-09-17 — competitors don't write this comparison)

## Phase 5 — Off-page authority (mostly `[NEEDS-YOU]`)

- [ ] `[NEEDS-YOU]` Create and verify company profile on Clutch, GoodFirms, G2 (needs your account/company verification).
- [ ] `[NEEDS-YOU]` Solicit client reviews on the above platforms for existing case-study clients.
- [ ] `[AUTO]` (draft only) LinkedIn post drafts accompanying each shipped blog post — included in that day's report for you to post manually.

---

## Content Backlog (research findings land here)

**Research pass — 2026-09-17:**

*Competitor landscape:* Most QA-outsourcing content ranking today (TestDevLab, Testriq, DeviQA, GrooveTechnology, remote.qa, Botgauge, Testlio, QASource, TestingXperts) is either (a) "Top N QA outsourcing companies" comparison listicles — directory-bait, not trust-building — or (b) generic "why outsource QA" explainers not written for a specific buyer geography. Testlio/QASource/TestingXperts blogs skew toward broad methodology content aimed at a US/global audience; none found were writing specifically for UK/AU/APAC buyers on time-zone overlap, data-residency concerns outside the US, or "which QA model fits your company stage" (managed team vs. staff augmentation vs. contract-to-hire vs. self-serve AI tool) — that comparison-of-models angle is a real content gap we can own, especially paired with our actual contract-to-hire case study.

*Tech/QA news:* Agentic QA is the dominant 2026 trend across the space (Tricentis, Katalon, CloudQA, Autify, TestQuality, LuxeQuality all publishing on it). Key citable stat: Gartner projects 40% of enterprise applications will feature task-specific AI agents by end of 2026, up from under 5% in 2025; teams embedding GenAI into QA report ~40% higher test coverage and up to 10x productivity gains. This is a strong, timely hook to connect directly to Loopsy (our in-house AI QA platform) rather than talking about agentic QA in the abstract like most competitor posts do.

*AEO angle:* Competitor content is written as long SEO listicles, not as concise, directly-quotable answers. Structuring our posts with clear Q&A headers and tight definitive answers (matching the JSON-LD `FAQPage`/`Article` schema going in during Phase 1) gives us a real shot at being the source AI answer engines (ChatGPT, Perplexity, Google AI Overviews) cite for "what is contract-to-hire QA staffing" / "what is agentic QA" style queries, where competitors currently aren't optimized for extraction.

*New topics added to Phase 4 backlog as a result (see above):* the agentic QA + Loopsy piece, and the "which QA outsourcing model fits your stage" comparison piece.

Sources: [TestDevLab — Best QA Outsourcing Companies for Startups 2026](https://www.testdevlab.com/blog/best-qa-outsourcing-companies-startups) · [Botgauge — QA Outsourcing: A 2026 Guide](https://www.botgauge.com/blog/qa-outsourcing) · [remote.qa — Best QA Outsourcing Companies for Startups 2026](https://remote.qa/blog/best-qa-outsourcing-companies-startups-2026/) · [Tricentis — QA trends for 2026: AI, agents, and the future of testing](https://www.tricentis.com/blog/qa-trends-ai-agentic-testing) · [Katalon — What Is Agentic QA? The Complete Guide for 2026](https://katalon.com/resources-center/blog/what-is-agentic-qa-the-complete-guide-for-2026) · [TestQuality — The Shift to Agentic QA](https://testquality.com/the-shift-to-agentic-qa-beyond-automated-testing-to-autonomous-ai-generation-in-2026/) · [Testlio — QA Outsourcing: Why Startups Should Be Outsourcing](https://testlio.com/blog/startup-outsourcing-qa/) · [QASource Blog — QA Outsourcing](https://www.qasource.com/blog/topic/qa-outsourcing)

## Change Log

- 2026-09-17 — Initial PLAN.md, RUNBOOK.md, and report scaffolding created — commit `c58f6fb`
- 2026-09-17 — RUNBOOK verification steps adapted for headless cloud sandbox — commit `e862944`
- 2026-09-17 — Phase 3 research pass #1 (competitor scan + tech news) completed manually ahead of automation go-live; findings above, 2 new Phase 4 topics added

*(each shipped/opened item gets one line here: date — task — commit SHA or PR link)*
