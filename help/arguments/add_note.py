#!/usr/bin/env python3
"""python3 add_note.py "Title" [--bn ..] [--body ..] [--category ..] [--tags a,b] [--pinned]"""
import argparse
from _lib import *
a = argparse.ArgumentParser()
a.add_argument("title", nargs="?", default=""); a.add_argument("--bn", default=""); a.add_argument("--body", default="")
a.add_argument("--category", default="general"); a.add_argument("--tags", default=""); a.add_argument("--pinned", action="store_true")
x = a.parse_args()
if not x.title:
    print("— New note (Enter to skip optional fields) —")
    x.title = ask("Title (EN) *", req=True); x.bn = ask("শিরোনাম (BN)"); x.body = ask("Body")
    x.category = ask("Category", "general"); x.tags = ask("Tags a,b"); x.pinned = ask("Pin? y/n", "n", choices=["y", "n"]) == "y"
d = load(); i = next_id(d, "note")
d["notes"].append({"id": i, "title": x.title, "title_bn": x.bn, "body": x.body, "category": x.category,
  "tags": tags(x.tags), "pinned": x.pinned, "created_at": now(), "history": [{"at": now(), "event": "created"}]})
save(d); print("✔ Note added:", i)
