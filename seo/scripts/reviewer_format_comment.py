#!/usr/bin/env python3
"""Formats the seo-reviewer PR comment from /tmp/verdict.json and exits
non-zero on failure, so the workflow step (and therefore the required
status check) fails when the reviewer found issues."""
import json
import sys

with open("/tmp/verdict.json") as f:
    d = json.load(f)

if d.get("pass"):
    print("**seo-reviewer: pass** ✅\n\nNo technical issues found in the diff.")
    sys.exit(0)

reasons = "\n".join(f"- {r}" for r in d.get("reasons", [])) or "- none"
print(f"""**seo-reviewer: issues found** ⚠️

{reasons}

This does not block @nitesh-qain's own review/merge decision on REVIEW-lane PRs -- flagging for awareness. For AUTO-lane PRs, this is a required check and blocks auto-merge until resolved.""")
sys.exit(1)
