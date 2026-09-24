#!/usr/bin/env python3
"""python3 add_task.py "Title" [--bn "শিরোনাম"] [--desc ..] [--priority low|medium|high|urgent] [--due YYYY-MM-DD] [--category ..] [--tags a,b]"""
import argparse
from _lib import *
a = argparse.ArgumentParser()
a.add_argument("title", nargs="?", default=""); a.add_argument("--bn", default=""); a.add_argument("--desc", default="")
a.add_argument("--priority", default="medium", choices=["low", "medium", "high", "urgent"])
a.add_argument("--due", default=""); a.add_argument("--category", default="general"); a.add_argument("--tags", default="")
x = a.parse_args()
if not x.title:
    print("— New task (Enter to skip optional fields) —")
    x.title = ask("Title (EN) *", req=True); x.bn = ask("শিরোনাম (BN)"); x.desc = ask("Description")
    x.priority = ask("Priority low/medium/high/urgent", "medium", choices=["low", "medium", "high", "urgent"])
    x.due = ask("Due YYYY-MM-DD"); x.category = ask("Category", "general"); x.tags = ask("Tags a,b")
d = load(); i = next_id(d, "task")
d["tasks"].append({"id": i, "title": x.title, "title_bn": x.bn, "desc": x.desc, "status": "todo",
  "priority": x.priority, "due": x.due, "category": x.category, "tags": tags(x.tags),
  "created_at": now(), "completed_at": "", "history": [{"at": now(), "event": "created"}]})
save(d); print("✔ Task added:", i)
