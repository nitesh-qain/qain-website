#!/usr/bin/env python3
"""Sends the PR diff to Claude for the independent seo-reviewer check.
Reads /tmp/pr_trimmed.diff, writes /tmp/verdict.json. Requires
ANTHROPIC_API_KEY in the environment. Kept as a real script rather than
inline in the workflow YAML -- see gate_format_comment.py for why."""
import json
import os
import urllib.request

with open("/tmp/pr_trimmed.diff") as f:
    diff = f.read()

prompt = f"""You are reviewing a git diff from an automated SEO agent working on a static HTML marketing site (QAInfinity). You only see this diff -- you have no access to the agent's reasoning or task description.

Check for:
1. Any internal link (href="...") pointing at a path that looks newly broken or malformed within this diff.
2. Any <script type="application/ld+json"> block whose content isn't valid JSON.
3. Any visible body-text change that looks like more than an additive/technical SEO edit -- e.g. deleted paragraphs, rewritten claims, new numbers/stats, new client names, anything that reads like a content rewrite rather than a schema/meta/link/alt-text change.
4. Anything that looks like a redirect, canonical, robots, or nav change hidden inside what looks like an unrelated file.

Respond with ONLY valid JSON, no prose: {{"pass": true or false, "reasons": ["short reason", ...]}}. Empty reasons list if pass is true.

DIFF:
{diff}
"""

body = json.dumps({
    "model": "claude-sonnet-5",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": prompt}],
})

req = urllib.request.Request(
    "https://api.anthropic.com/v1/messages",
    data=body.encode(),
    headers={
        "x-api-key": os.environ["ANTHROPIC_API_KEY"],
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    },
)
with urllib.request.urlopen(req) as resp:
    result = json.load(resp)

text = result["content"][0]["text"].strip()
if text.startswith("```"):
    text = text.split("```")[1]
    if text.startswith("json"):
        text = text[4:]

verdict = json.loads(text.strip())
with open("/tmp/verdict.json", "w") as f:
    json.dump(verdict, f)
print(json.dumps(verdict, indent=2))
