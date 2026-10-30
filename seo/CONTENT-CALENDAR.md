# Content calendar (Nov 2, 2026 – Jan 29, 2027)

Generated from the Phase 6 queue in [PLAN.md](PLAN.md); PLAN.md is the source of truth. Order matters more than dates. Every blog and page is a PR you merge; the automatic (AUTO) tasks go live on their own.

## New blog posts and pages

| Week | Mon — blog post (PR) | Wed — page (PR) |
|---|---|---|
| W1 (11-02) | How Much Does QA Outsourcing Cost in 2026? Pricing Models and What Drives the Rate | `/faq/` |
| W2 (11-09) | How to Choose a QA Outsourcing Vendor: 12 Questions to Ask Before You Sign | `/services/dedicated-qa-engineers/` (competitor idea #5, part 1) |
| W3 (11-16) | Test Automation ROI: When to Automate, and When Not To | `/services/performance-security-testing/` (competitor idea #5, part 2) |
| W4 (11-23) | How to Test LLM Apps and AI Agents: Evals, LLM-as-a-Judge and Regression Sets | `/tools/qa-cost-calculator/` |
| W5 (11-30) | Onboarding an Offshore QA Team: The First 30 Days | `/industries/` hub + `/industries/gaming/` (competitor idea #4) |
| W6 (12-07) | A Regression Testing Strategy for Teams That Ship Weekly | `/industries/ecommerce/` (competitor ideas #4 + #8) |
| W7 (12-14) | QA Metrics CTOs Should Actually Track (and the Vanity Ones to Ignore) | `/industries/fintech/` (approach-led, competitor idea #4) |
| W8 (12-21) | Mobile App Testing Checklist: Device Matrix, OS Fragmentation and Release Gates | `/industries/ai-llm-testing/` (approach-led, competitor idea #4) |
| W9 (12-28) | API Testing Beyond Status Codes: What to Cover Before Release | `/industries/on-demand-apps/` (approach-led, competitor idea #4) |
| W10 (01-04) | What to Put in a QA Outsourcing Contract: NDA, IP, SLAs and Exit Terms | `/regions/australia-nz/` |
| W11 (01-11) | E-commerce Peak-Season Testing Checklist: Checkout, Payments and Load | `/regions/canada/` |
| W12 (01-18) | Playwright vs. Cypress vs. Selenium in 2026: How to Choose | `/regions/singapore-apac/` |
| W13 (01-25) | Shift-Left Testing: Where an External QA Team Fits in Your CI/CD Pipeline | `/engagement-models/` |

## Automatic tasks (Tue / Thu / Fri)

**W1**
- Tue `AUTO` Add a "Related reading" block to every blog post (1 service page + 2 sibling posts each, relevant by topic, descriptive anchor text). Append only; no other text change.
- Thu `AUTO` Add `BreadcrumbList` JSON-LD to every sub-page (head-only change, no visible layout change).
- Fri `AUTO` Image and asset audit sitewide: alt text, explicit width/height, `loading="lazy"` below the fold, no oversized files. No visual change.

**W2**
- Tue `AUTO` Add a short "Key takeaways" block at the top of blog posts 1–5, built only from each post's own existing content (no new claims or stats).
- Thu `AUTO` Add the same "Key takeaways" block to the remaining existing blog posts.
- Fri `AUTO` Heading-hierarchy audit across all pages: exactly one H1, logical H2/H3, no skipped levels; fix without changing visible design.

**W3**
- Tue `AUTO` Add 3–5 real Q&As plus matching `FAQPage` JSON-LD to `/services/` (questions buyers actually ask; answers from existing site content only).
- Thu `AUTO` Add 3–5 Q&As plus `FAQPage` JSON-LD to `/services/manual-testing/`.
- Fri `AUTO` Add 3–5 Q&As plus `FAQPage` JSON-LD to `/services/test-automation/`.

**W4**
- Tue `AUTO` Add anchor-link tables of contents to long blog posts (over ~1,500 words).
- Thu `AUTO` Add a visible "Last updated" date to every blog post and `dateModified` to its Article JSON-LD. Author byline + `Person` schema for founder Nitesh Saxena only if a bio al…
- Fri `AUTO` Sitemap audit: every live page present, `lastmod` accurate, no non-existent URLs, canonical matches sitemap.

**W5**
- Tue `AUTO` Contextual internal-link pass for the new FAQ, dedicated-QA-engineers and performance/security pages: link from the services hub, region pages and the most relevant blog …
- Thu `AUTO` Core Web Vitals re-audit on the 5 heaviest pages after the new content; fix regressions.
- Fri `AUTO` Accessibility and SEO-adjacent pass: form labels, link text, contrast, focus states, `lang`.

**W6**
- Tue `AUTO` Cannibalization and duplicate-content audit across region pages and blog posts; report overlaps, fix thin duplicates by differentiating copy.
- Thu `AUTO` External-link audit: verify every cited source in blog posts still resolves; replace or remove dead ones.
- Fri `AUTO` Add a results table and 3 Q&As with `FAQPage` JSON-LD to the case-study pages, using only figures already published in them.

**W7**
- Tue `AUTO` Refresh the 3 oldest blog posts: update sources and figures, add a short "What's changed" note, bump `dateModified`.
- Thu `AUTO` Mobile layout pass at 375/768/1024px on all pages (nav, tables, tiles, calculators); fix overflow.
- Fri `AUTO` Contextual internal links to the new industry pages from relevant services, case-study and blog pages (body text only).

**W8**
- Tue `AUTO` Refresh the next 3 oldest blog posts.
- Thu `AUTO` JSON-LD validation sweep on every page: parses, correct `@type`, URLs use `https://www.qainfinity.com`; fix issues.
- Fri `AUTO` Anchor-text review of internal links: varied, descriptive, no generic "click here".

**W9**
- Tue `AUTO` Orphan- and thin-page check: every page reachable in ≤3 clicks from the homepage; list pages under ~300 words.
- Thu `AUTO` Cross-link the new region pages with the time-zone, nearshore-vs-offshore and follow-the-sun posts (body text only).
- Fri `AUTO` Metadata CTR audit (proposal only): for each page, list the current title/meta, the target keyword, and a proposed rewrite within length limits. Write proposals into the …

**W10**
- Tue `PR` Apply the metadata CTR audit proposals: rewrite titles and meta descriptions on the pages where the proposal is clearly better (within length limits, keeping each page's …
- Thu `AUTO` Broken-link and 404 sweep across every page, plus a check that the new pages are in the sitemap.
- Fri `AUTO` Add contextual links from case studies to the matching industry pages.

**W11**
- Tue `PR` Create `/llms.txt` (plain-text site summary for AI crawlers: who we are, services, key pages, contact) and reference it from nothing else. Facts only from existing site c…
- Thu `AUTO` Refresh the next 3 oldest blog posts (third batch).
- Fri `AUTO` Schema coverage matrix: for each page, list which JSON-LD types exist and which are missing; add missing low-risk types (head-only).

**W12**
- Tue `AUTO` Verify the site renders correctly with JavaScript disabled for key content (headings, body, links) and fix anything search engines would miss.
- Thu `AUTO` Refresh internal links and "Related reading" blocks across all posts so every new post is linked from at least 2 others.
- Fri `AUTO` Re-run the full technical audit (links, JSON-LD, titles/meta lengths, canonicals, sitemap, mobile) and fix everything fixable.

**W13**
- Tue `AUTO` Read the last 12 weeks of `seo/data/visibility-log.md` and the monthly GSC export (if the owner has added it to `seo/data/`); write `seo/reports/90-day-review.md`: what s…
- Thu `AUTO` Draft Phase 7 (next 90 days) into `PLAN.md`: ~60 tasks in the same weekly pattern, based on the 90-day review and the Content Backlog. This prevents an empty backlog afte…
- Fri `AUTO` Final Phase 6 check: confirm every shipped task is checked off with a link, and Phase 7 has at least 20 unchecked tasks.

## Weekends
Sat: outreach drafts (3 LinkedIn posts, 1 backlink pitch, 1 answer to post) in `seo/outreach/`. Sun: search-visibility log in `seo/data/` and backlog refill.
