#!/usr/bin/env python3
"""MJ Node core: nodes tree, users (PBKDF2), hash-chained ledger, rules, scores, sealing."""
import json, os, sys, shutil, hashlib, hmac, secrets, base64, getpass
from datetime import datetime
HERE = os.path.dirname(os.path.abspath(__file__)); NET = os.path.join(HERE, "net.json")
LV = [("CEN","Central","কেন্দ্র"),("DIV","Division","বিভাগ"),("DST","District","জেলা"),("UPZ","Upazila","উপজেলা"),
      ("UNI","Union","ইউনিয়ন"),("VIL","Village","গ্রাম"),("PAR","Para/Mohalla","পাড়া/মহল্লা"),("TIM","Team","টিম")]
ITER = 200000
RULES = {"w": {"task": 35, "dist": 25, "report": 20, "eval": 20}, "min_reports": 4}
def now(): return datetime.now().astimezone().isoformat(timespec="seconds")
def die(m): print("ERROR:", m, file=sys.stderr); sys.exit(1)
def load():
    if not os.path.exists(NET): die("net.json missing — run: ./run.sh init \"Name\"")
    with open(NET, encoding="utf-8") as f: return json.load(f)
def save(n):
    if os.path.exists(NET): shutil.copy(NET, NET + ".bak")
    with open(NET + ".tmp", "w", encoding="utf-8") as f: json.dump(n, f, ensure_ascii=False, indent=1)
    os.replace(NET + ".tmp", NET)
def sha(s): return hashlib.sha256(s.encode()).hexdigest()
def canon(o): return json.dumps(o, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
def ehash(e): return sha(canon({k: v for k, v in e.items() if k != "hash"}))
def node(n, i): return next((x for x in n["nodes"] if x["id"] == i), None)
def subtree(n, i):
    out = [i]
    for x in n["nodes"]:
        if x["parent"] == i: out += subtree(n, x["id"])
    return out
def ancestors(n, i):
    out = []; p = node(n, i)["parent"]
    while p: out.append(p); p = node(n, p)["parent"]
    return out
def kdf(pw, salt): return hashlib.pbkdf2_hmac("sha256", pw.encode(), bytes.fromhex(salt), ITER, 64).hex()
def new_user(n, nid, name):
    """One leader account per node; password shown once, only the derived key is stored."""
    pw = secrets.token_urlsafe(9); salt = secrets.token_hex(16)
    n["users"] = [u for u in n["users"] if u["id"] != nid] + [{"id": nid, "node": nid, "name": name, "salt": salt, "key": kdf(pw, salt)}]
    return pw
def auth(n, uid):
    u = next((x for x in n["users"] if x["id"] == uid.strip().upper()), None)
    pw = os.environ.get("MJ_PASS") or getpass.getpass(f"Password for {uid}: ")
    if not u or not hmac.compare_digest(kdf(pw, u["salt"]), u["key"]): die("authentication failed")
    return u
def entry(n, nid, kind, actor, data, ref=""):
    ch = [e for e in n["ledger"] if e["node"] == nid]
    e = {"id": f"LED-{len(n['ledger'])+1:06d}", "at": now(), "node": nid, "kind": kind, "actor": actor, "ref": ref, "data": data,
         "prev": ch[-1]["hash"] if ch else "0" * 64}
    e["hash"] = ehash(e); return e
def allowed(n, e):
    k, nd, a, d = e["kind"], e["node"], e["actor"], e["data"]
    if k == "genesis": return ""
    u = next((x for x in n["users"] if x["id"] == a), None)
    L = lambda i: next((x for x in n["ledger"] if x["id"] == i), None)
    if not u or u["node"] != nd: return "actor must act for own node"
    if k == "anchor" and node(n, nd)["level"] != 0: return "only central can anchor"
    if k == "task" and d["to"] not in subtree(n, nd)[1:]: return "task target must be a descendant"
    if k == "taskdone":
        t = L(e["ref"])
        if not t or t["kind"] != "task" or t["data"]["to"] != nd: return "not your task"
    if k == "witness":
        t = L(e["ref"])
        if not t or t["kind"] != "dist": return "unknown distribution entry"
        if nd == t["node"] or not (nd in ancestors(n, t["node"]) or node(n, nd)["parent"] == node(n, t["node"])["parent"]): return "witness must be an ancestor or sibling node"
    if k == "eval" and (d["of"] not in subtree(n, nd)[1:] or not 0 <= d["score"] <= 100 or not d["basis"] or any(not L(b) or L(b)["node"] not in subtree(n, d["of"]) for b in d["basis"])):
        return "eval needs a descendant, score 0-100 and basis entries that belong to the evaluated node"
    if k in ("node", "reset") and d["id"] not in subtree(n, nd)[1:]: return "only an ancestor may do this"
    return ""
def scores(n):
    W = n["rules"]["w"]; out = {}
    for nd in n["nodes"]:
        i = nd["id"]; L = [e for e in n["ledger"] if e["node"] == i]; parts = {}
        T = [e for e in n["ledger"] if e["kind"] == "task" and e["data"]["to"] == i]; D = {e["ref"]: e for e in L if e["kind"] == "taskdone"}
        if T: parts["task"] = sum(1 for t in T if t["id"] in D and D[t["id"]]["at"][:10] <= t["data"]["due"]) / len(T)
        S = [e for e in L if e["kind"] == "dist"]; wit = {e["ref"] for e in n["ledger"] if e["kind"] == "witness"}
        if S: parts["dist"] = sum(1 for e in S if e["id"] in wit) / len(S)
        parts["report"] = min(1, sum(1 for e in L if e["kind"] == "report") / n["rules"]["min_reports"])
        V = [e["data"]["score"] for e in n["ledger"] if e["kind"] == "eval" and e["data"]["of"] == i]
        if V: parts["eval"] = sum(V) / len(V) / 100
        tw = sum(W[k] for k in parts); out[i] = round(sum(W[k] * v for k, v in parts.items()) / tw * 100) if tw else None
    return out
def seal(key_hex, plain):
    key = bytes.fromhex(key_hex); nonce = secrets.token_bytes(16)
    ks = b"".join(hmac.new(key[:32], nonce + i.to_bytes(4, "big"), "sha256").digest() for i in range((len(plain) + 31) // 32))[:len(plain)]
    ct = (int.from_bytes(plain, "big") ^ int.from_bytes(ks, "big")).to_bytes(len(plain), "big")
    b = lambda x: base64.b64encode(x).decode()
    return {"n": b(nonce), "c": b(ct), "m": b(hmac.new(key[32:], nonce + ct, "sha256").digest())}
