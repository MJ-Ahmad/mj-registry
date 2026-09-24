#!/usr/bin/env python3
"""python3 add_audit.py "Title" --result pass|warning|fail [--target ..] [--findings ..] [--auditor ..] [--related TSK-2026-0001,NOT-..] [--bn ..] [--category ..] [--tags ..]"""
import argparse
from _lib import *
a = argparse.ArgumentParser()
a.add_argument("title", nargs="?", default=""); a.add_argument("--bn", default=""); a.add_argument("--result", default="", choices=["pass", "warning", "fail"])
a.add_argument("--target", default=""); a.add_argument("--findings", default=""); a.add_argument("--auditor", default="")
a.add_argument("--related", default=""); a.add_argument("--category", default="general"); a.add_argument("--tags", default="")
x = a.parse_args()
if not x.title:
    print("— New audit (Enter to skip optional fields) —")
    x.title = ask("Title (EN) *", req=True); x.bn = ask("শিরোনাম (BN)")
    x.result = ask("Result pass/warning/fail *", req=True, choices=["pass", "warning", "fail"])
    x.target = ask("Target"); x.findings = ask("Findings"); x.auditor = ask("Auditor", "MJ Ahmad")
    x.related = ask("Related IDs a,b"); x.category = ask("Category", "general"); x.tags = ask("Tags a,b")
if not x.result: die("--result is required (pass|warning|fail)")
d = load()
for r in tags(x.related):
    if find(d, r)[0] is None: die(f"related ID not found: {r}")
i = next_id(d, "audit")
d["audits"].append({"id": i, "title": x.title, "title_bn": x.bn, "result": x.result, "target": x.target,
  "findings": x.findings, "auditor": x.auditor, "related": tags(x.related), "category": x.category,
  "tags": tags(x.tags), "created_at": now(), "history": [{"at": now(), "event": "created"}]})
save(d); print("✔ Audit added:", i)
