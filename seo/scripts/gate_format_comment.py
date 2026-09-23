#!/usr/bin/env python3
"""Formats the seo-gate PR comment body from /tmp/verdict.json. Kept as a
real script rather than inline in the workflow YAML -- multi-line Python
embedded in a YAML block scalar is a real footgun (indentation rules
differ between YAML and Python), so logic like this belongs in a file."""
import json

with open("/tmp/verdict.json") as f:
    d = json.load(f)

if d["verdict"] == "auto":
    print(f"""**seo-gate: AUTO-eligible** ✅

No review-lane triggers matched ({len(d['files'])} file(s) changed). Approving and queuing auto-merge.""")
else:
    reasons = "\n".join(f"- {r}" for r in d["reasons"]) or "- none"
    print(f"""**seo-gate: REVIEW required** \U0001F50E

{reasons}

Not auto-approved. This needs @nitesh-qain's manual review and merge.""")
