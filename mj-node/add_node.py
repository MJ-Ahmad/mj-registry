#!/usr/bin/env python3
"""./run.sh init "Central Head Name"
./run.sh node --parent DIV-0001 --en "Savar" --bn "সাভার" --leader "Name" [--postcode 1340]   (level = parent level + 1)
./run.sh node --reset UPZ-0002        (new password for a node leader; only an ancestor may do it)
Actors authenticate with their user ID (= their node ID); password via prompt or MJ_PASS env."""
import argparse
from nodelib import *
a = argparse.ArgumentParser(); a.add_argument("--init", default=""); a.add_argument("--parent", default=""); a.add_argument("--en", default="")
a.add_argument("--bn", default=""); a.add_argument("--leader", default=""); a.add_argument("--postcode", default=""); a.add_argument("--reset", default="")
a.add_argument("--as", dest="uid", default=os.environ.get("MJ_USER", "")); x = a.parse_args()
if x.init:
    if os.path.exists(NET): die("net.json already exists")
    n = {"rules": RULES, "levels": LV, "counters": {"CEN": 1}, "nodes": [{"id": "CEN-0001", "level": 0, "parent": "", "en": "Bangladesh Central", "bn": "বাংলাদেশ কেন্দ্রীয়", "leader": x.init, "postcode": "", "created_at": now()}], "users": [], "ledger": []}
    pw = new_user(n, "CEN-0001", x.init); n["ledger"].append(entry(n, "CEN-0001", "genesis", "CEN-0001", {"rules": RULES})); save(n)
    print(f"✔ Central created.\n  User ID : CEN-0001\n  Password: {pw}   (shown once — keep it safe)"); sys.exit()
n = load(); u = auth(n, x.uid or input("Your user ID: "))
if x.reset:
    t = node(n, x.reset.upper()) or die("node not found"); e = entry(n, u["node"], "reset", u["id"], {"id": t["id"]}); r = allowed(n, e)
    if r: die(r)
    pw = new_user(n, t["id"], t["leader"]); n["ledger"].append(e); save(n); print(f"✔ New password for {t['id']}: {pw}"); sys.exit()
p = node(n, x.parent.upper()) or die("--parent node not found")
if p["level"] >= 7: die("teams are the lowest level")
lv = p["level"] + 1; pf = LV[lv][0]; n["counters"][pf] = n["counters"].get(pf, 0) + 1; nid = f"{pf}-{n['counters'][pf]:04d}"
if not (x.en and x.leader): die("--en and --leader are required")
n["nodes"].append({"id": nid, "level": lv, "parent": p["id"], "en": x.en, "bn": x.bn or x.en, "leader": x.leader, "postcode": x.postcode, "created_at": now()})
e = entry(n, u["node"], "node", u["id"], {"id": nid, "en": x.en, "leader": x.leader}); r = allowed(n, e)
if r: die(r + f" (you are {u['node']})")
pw = new_user(n, nid, x.leader); n["ledger"].append(e); save(n)
print(f"✔ {LV[lv][1]} node {nid} under {p['id']}\n  User ID : {nid}\n  Password: {pw}   (shown once)")
