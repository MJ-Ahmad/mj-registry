#!/usr/bin/env python3
"""Checks every hash chain, sequence, time order, every rule, anchors; prints the score tree. --anchor = Central records all chain heads."""
import argparse
from nodelib import *
a = argparse.ArgumentParser(); a.add_argument("--anchor", action="store_true"); a.add_argument("--as", dest="uid", default=os.environ.get("MJ_USER", "")); x = a.parse_args()
n = load(); errs = []; prev = {}; last = ""
for k, e in enumerate(n["ledger"], 1):
    if e["id"] != f"LED-{k:06d}": errs.append(f"{e['id']}: sequence gap")
    if e["at"] < last: errs.append(f"{e['id']}: time goes backwards")
    last = e["at"]
    if e["prev"] != prev.get(e["node"], "0" * 64) or ehash(e) != e["hash"]: errs.append(f"{e['id']}: CHAIN BROKEN (edited or removed entry)")
    prev[e["node"]] = e["hash"]; r = allowed(n, e)
    if r: errs.append(f"{e['id']}: {r}")
    if e["kind"] == "anchor":
        errs += [f"{e['id']}: anchored head of {nd} no longer in chain" for nd, h in e["data"]["heads"].items() if not any(y["hash"] == h for y in n["ledger"] if y["node"] == nd)]
if errs: print("✘ PROBLEMS:"); [print("  -", m) for m in errs]; sys.exit(1)
if x.anchor:
    u = auth(n, x.uid or input("Central user ID: ")); e = entry(n, u["node"], "anchor", u["id"], {"heads": dict(prev)}); r = allowed(n, e)
    if r: die(r)
    n["ledger"].append(e); save(n); print("✔ anchored", e["id"])
S = scores(n)
def show(i, d=0):
    nd = node(n, i); print("  " * d + f"{LV[nd['level']][0]} {i} {nd['en']} / {nd['bn']} — {nd['leader']}  score: {S[i] if S[i] is not None else '—'}")
    [show(c["id"], d + 1) for c in n["nodes"] if c["parent"] == i]
show("CEN-0001"); print(f"✔ OK — {len(n['nodes'])} nodes, {len(n['ledger'])} entries, all chains and rules verified")
