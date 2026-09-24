#!/usr/bin/env python3
"""Manage the CodeCraft menu tree.
python3 menu.py                                        show the tree (ids, names, entry counts)
python3 menu.py --new "Web/Portal" [--bn "ওয়েব/পোর্টাল"] [--under "CodeCraft/Tools"]   create empty submenus
python3 menu.py --move CDE-2026-0001 --to "CodeCraft/Web/Portal"                       move an entry"""
import argparse
from _lib import *
a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
a.add_argument("--new", default=""); a.add_argument("--bn", default=""); a.add_argument("--under", default="")
a.add_argument("--move", default=""); a.add_argument("--to", default="")
x = a.parse_args(); d = normalize(load()); root = ensure_root(d); changed = False
if x.new:
    node, path = root, ["codecraft"]
    if x.under:
        node, path = find_node(d, x.under)
        if not node: die(f"menu not found: {x.under}")
    node, path = ensure_chain(d, node, path, [s.strip() for s in x.new.split("/") if s.strip()], x.bn.split("/")); changed = True
    print("✔ menu ready:", " › ".join(path))
if x.move:
    k, it = find(d, x.move)
    if k != "code": die(f"CodeCraft entry not found: {x.move}")
    node, path = find_node(d, x.to)
    if not node: die(f"menu not found: {x.to}")
    it["menu_path"] = path; it["history"].append({"at": now(), "event": "moved", "note": " › ".join(path)}); changed = True
    print(f"✔ {x.move} → {' › '.join(path)}")
if changed: save(d)
def show(ns, ind=0):
    for n in ns:
        c = f"  ({sum(1 for it in d['codes'] if n['id'] in it['menu_path'])})" if n.get("view", {}).get("type") == "codes" else ""
        print("  " * ind + f"{'└ ' if ind else ''}{n.get('en') or n.get('bn')} / {n.get('bn','')}  [{n['id']}]{c}")
        show(n.get("children", []), ind + 1)
if not (x.new or x.move): show(d["menu"])
