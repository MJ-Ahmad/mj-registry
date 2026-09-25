#!/usr/bin/env python3
"""Append-only ledger. Every entry is signed by the actor's account, chained by hash, and can never be edited or deleted.
./run.sh log --as TIM-0001 report "text"
   task "Title" --to NODE --due 2026-10-01       (to a descendant)      done TASKID "evidence"
   dist --item "Quran" --qty 50 --recipient "Mosque X" [--serial A1-A50] [--postcode 1340]
   witness DISTID     (an ancestor or sibling node confirms)      eval --of NODE --score 80 --basis LED-1,LED-2 "comment"
   appeal "text" [--against LED-x]   (any node; visible to every ancestor up to Central)"""
import argparse
from nodelib import *
p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter); p.add_argument("--as", dest="uid", default=os.environ.get("MJ_USER", ""))
s = p.add_subparsers(dest="k", required=True)
r = s.add_parser("report"); r.add_argument("text")
t = s.add_parser("task"); t.add_argument("title"); t.add_argument("--to", required=True); t.add_argument("--due", required=True)
d = s.add_parser("done"); d.add_argument("task"); d.add_argument("text")
b = s.add_parser("dist"); b.add_argument("--item", required=True); b.add_argument("--qty", type=int, required=True); b.add_argument("--recipient", required=True); b.add_argument("--serial", default=""); b.add_argument("--postcode", default="")
w = s.add_parser("witness"); w.add_argument("dist")
v = s.add_parser("eval"); v.add_argument("--of", required=True); v.add_argument("--score", type=int, required=True); v.add_argument("--basis", required=True); v.add_argument("text")
q = s.add_parser("appeal"); q.add_argument("text"); q.add_argument("--against", default="")
x = p.parse_args(); n = load(); u = auth(n, x.uid or input("Your user ID: "))
K = {"report": ("report", {"text": getattr(x, "text", "")}, ""), "task": ("task", {"title": getattr(x, "title", ""), "to": getattr(x, "to", "").upper(), "due": getattr(x, "due", "")}, ""),
 "done": ("taskdone", {"text": getattr(x, "text", "")}, getattr(x, "task", "")),
 "dist": ("dist", {"item": getattr(x, "item", ""), "qty": getattr(x, "qty", 0), "recipient": getattr(x, "recipient", ""), "serial": getattr(x, "serial", ""), "postcode": getattr(x, "postcode", "")}, ""),
 "witness": ("witness", {}, getattr(x, "dist", "")),
 "eval": ("eval", {"of": getattr(x, "of", "").upper(), "score": getattr(x, "score", 0), "basis": [i.strip() for i in getattr(x, "basis", "").split(",") if i.strip()], "text": getattr(x, "text", "")}, ""),
 "appeal": ("appeal", {"text": getattr(x, "text", "")}, getattr(x, "against", ""))}
kind, data, ref = K[x.k]; e = entry(n, u["node"], kind, u["id"], data, ref); err = allowed(n, e)
if err: die(err)
n["ledger"].append(e); save(n); print("✔", e["id"], kind, "→ chain of", u["node"], e["hash"][:12])
