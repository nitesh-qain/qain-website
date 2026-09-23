#!/usr/bin/env python3
"""
Rule-based classifier for the SEO agent's merge gate. Deliberately NOT an
LLM -- per seo/PLAN.md, the merge decision has to be deterministic.

Reads the diff between origin/main and the PR head, classifies it as
AUTO-eligible or REVIEW-required, and prints a JSON verdict for the
seo-gate workflow to act on.

Usage: gate_classify.py <base_ref> <head_ref>
"""
import json
import re
import subprocess
import sys

MAX_FILES = 20
SOFT_FILE_LIMIT = 5  # spec says "5 changes / 20 files" -- files is the
                      # stricter, unambiguous number, so it's what's
                      # actually enforced. See seo/RUNBOOK.md.

# Filenames that are allowed to be newly added under [AUTO] -- everything
# else being ADDED (a new file) is always REVIEW-lane per PLAN.md
# ("new/landing/region pages" are always review).
ALLOWED_NEW_FILES = {"llms.txt"}

# Always-review paths, defense in depth on top of CODEOWNERS (CODEOWNERS
# blocks the merge; this just makes sure the bot never auto-approves them
# even if CODEOWNERS is ever misconfigured).
ALWAYS_REVIEW_PATHS = {"robots.txt", "vercel.json"}
ALWAYS_REVIEW_PREFIXES = (".github/",)

# Content-level triggers: if an ADDED line in a MODIFIED file matches any
# of these, the change needs a human even though the file itself isn't in
# CODEOWNERS. This is the part that can't be done by path-matching alone.
CONTENT_TRIGGERS = [
    (re.compile(r"<title[ >]", re.I), "title tag changed"),
    (re.compile(r"<h1[ >]", re.I), "H1 changed"),
    (re.compile(r'rel="canonical"', re.I), "canonical tag changed"),
    (re.compile(r"<nav[ >]", re.I), "nav markup changed"),
    (re.compile(r"\bDisallow\b"), "robots directive changed"),
    (re.compile(r"hreflang", re.I), "hreflang changed"),
    (re.compile(r"\b30[1278]\b|Location:|redirect", re.I), "possible redirect"),
    (re.compile(r"\$\s?\d|/hr\b|₹|\bINR\b", re.I), "possible pricing content"),
]

# Known client names -- a NEW mention of any of these needs sign-off
# (client consent for names/logos/results claims, per PLAN.md).
CLIENT_NAMES = [
    "MPL", "Angara", "Adani", "Snabbit", "Ninjacart",
    "QualityLabs", "Creatiosoft", "Maestroedge",
]
CLIENT_RE = re.compile(r"\b(" + "|".join(re.escape(n) for n in CLIENT_NAMES) + r")\b", re.I)


def run(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True).stdout


def main():
    base, head = sys.argv[1], sys.argv[2]
    run(f"git fetch origin {base} {head} --quiet")

    name_status = run(f"git diff --name-status origin/{base}...{head}").strip().splitlines()
    if not name_status:
        print(json.dumps({"verdict": "auto", "reasons": ["no changes"], "files": []}))
        return

    reasons = []
    files = []
    for line in name_status:
        parts = line.split("\t")
        status, path = parts[0], parts[-1]
        files.append(path)

        if status.startswith("D"):
            reasons.append(f"{path}: file deleted (always review)")
            continue

        if status.startswith("A"):
            base_name = path.rsplit("/", 1)[-1]
            if base_name not in ALLOWED_NEW_FILES:
                reasons.append(f"{path}: new file (new pages/blogs are always review)")
            continue

        # Modified file -- check path-based always-review list first.
        base_name = path.rsplit("/", 1)[-1]
        if base_name in ALWAYS_REVIEW_PATHS or path.startswith(ALWAYS_REVIEW_PREFIXES):
            reasons.append(f"{path}: always-review path")
            continue

        # Content-level check: scan only ADDED lines in the diff for this file.
        # Track JSON-LD <script> blocks as we go -- structured data that
        # mirrors already-public visible content (e.g. an Article schema's
        # headline restating a case-study title) isn't a *new* claim, so
        # the title/H1/client-name triggers don't apply inside those
        # blocks. Schema markup is explicitly AUTO-lane per PLAN.md; this
        # keeps the gate from systematically blocking exactly that.
        diff = run(f"git diff origin/{base}...{head} -- {path!r}")
        removed_lines = {l[1:] for l in diff.splitlines() if l.startswith("-") and not l.startswith("---")}

        in_json_ld = False
        for line in diff.splitlines():
            if not (line.startswith("+") and not line.startswith("+++")):
                continue
            line_text = line[1:]

            if re.search(r'<script[^>]+application/ld\+json', line_text, re.I):
                in_json_ld = True
                continue
            if "</script>" in line_text:
                in_json_ld = False
                continue
            if in_json_ld:
                continue  # inside a JSON-LD block -- skip content triggers

            for pattern, label in CONTENT_TRIGGERS:
                if pattern.search(line_text):
                    reasons.append(f"{path}: {label}")
                    break
            m = CLIENT_RE.search(line_text)
            if m and line_text not in removed_lines:
                reasons.append(f"{path}: new mention of client name '{m.group(1)}'")

    if len(files) > MAX_FILES:
        reasons.append(f"{len(files)} files changed, exceeds hard limit of {MAX_FILES}")
    elif len(files) > SOFT_FILE_LIMIT:
        reasons.append(f"{len(files)} files changed, exceeds soft limit of {SOFT_FILE_LIMIT}")

    verdict = "review" if reasons else "auto"
    print(json.dumps({"verdict": verdict, "reasons": reasons, "files": files}, indent=2))


if __name__ == "__main__":
    main()
