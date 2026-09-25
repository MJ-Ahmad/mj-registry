#!/usr/bin/env python3
"""Builds sites/<NODE-ID>/index.html for every node. Each page contains ONLY that node's subtree, encrypted with its leader's key."""
import subprocess
from nodelib import *
if subprocess.call([sys.executable, os.path.join(HERE, "verify.py")], stdout=subprocess.DEVNULL): die("verify failed — run ./run.sh verify")
n = load(); S = scores(n); T = open(os.path.join(HERE, "site.tpl"), encoding="utf-8").read()
for u in n["users"]:
    sub = subtree(n, u["node"]); ids = set(sub)
    P = {"root": u["node"], "lv": LV, "rules": n["rules"], "built": now(), "anc": [{k: node(n, i)[k] for k in ("id", "en", "bn", "level")} for i in ancestors(n, u["node"])],
         "nodes": [x for x in n["nodes"] if x["id"] in ids], "scores": {i: S[i] for i in sub},
         "ledger": [e for e in n["ledger"] if e["node"] in ids or e["kind"] == "anchor"]}
    pk = {"u": u["id"], "s": base64.b64encode(bytes.fromhex(u["salt"])).decode(), **seal(u["key"], json.dumps(P, ensure_ascii=False).encode())}
    os.makedirs(os.path.join(HERE, "sites", u["id"]), exist_ok=True)
    open(os.path.join(HERE, "sites", u["id"], "index.html"), "w", encoding="utf-8").write(T.replace("__PACKS__", json.dumps([pk])).replace("__NODE__", u["id"]))
print(f"✔ built {len(n['users'])} node sites in sites/  (net.json stays private — never publish it)")
