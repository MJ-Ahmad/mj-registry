#!/usr/bin/env python3
"""Shared helpers: load/save data.json safely, unique IDs, history log."""
import json, os, shutil, sys
from datetime import datetime
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data.json")
KIND = {"task": ("TSK", "tasks"), "note": ("NOT", "notes"), "audit": ("AUD", "audits"), "code": ("CDE", "codes")}

def now(): return datetime.now().astimezone().isoformat(timespec="seconds")

def load():
    with open(DATA, encoding="utf-8") as f: d = json.load(f)
    d.setdefault("codes", []); return d

def save(d):
    d["meta"]["updated_at"] = now()
    if os.path.exists(DATA): shutil.copy(DATA, DATA + ".bak")
    tmp = DATA + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    os.replace(tmp, DATA)

def next_id(d, kind):
    """Never reuses an ID: PREFIX-YYYY-NNNN, counter kept per kind & year."""
    p, _ = KIND[kind]; y = datetime.now().year
    c = d["meta"].setdefault("counters", {}).setdefault(kind, {})
    c[str(y)] = c.get(str(y), 0) + 1
    return f"{p}-{y}-{c[str(y)]:04d}"

def find(d, id_):
    for k, (p, key) in KIND.items():
        for it in d[key]:
            if it["id"] == id_: return k, it
    return None, None

def tags(s): return [t.strip() for t in (s or "").split(",") if t.strip()]

def die(msg): print("ERROR:", msg, file=sys.stderr); sys.exit(1)

def ask(label, default="", req=False, choices=None):
    """Interactive prompt used when a script runs without arguments."""
    while True:
        v = input(f"{label}{' ['+default+']' if default else ''}: ").strip() or default
        if req and not v: print("  required"); continue
        if choices and v not in choices: print("  choose:", "/".join(choices)); continue
        return v

import hashlib
EXT = {"html":("html","HTML"),"htm":("html","HTML"),"json":("json","JSON"),"py":("python","Python"),
 "js":("node","Node.js"),"mjs":("node","Node.js"),"cjs":("node","Node.js"),"ts":("ts","TypeScript"),
 "jsx":("react","React"),"tsx":("react","React"),"sh":("shell","Shell"),"bash":("shell","Shell"),
 "css":("css","CSS"),"md":("markdown","Markdown"),"yml":("yaml","YAML"),"yaml":("yaml","YAML"),
 "sql":("sql","SQL"),"xml":("xml","XML"),"php":("php","PHP"),"java":("java","Java"),"c":("c","C"),
 "cpp":("cpp","C++"),"go":("go","Go"),"rs":("rust","Rust"),"txt":("text","Text")}
SHEBANG = {"python":("python","Python"),"node":("node","Node.js"),"bash":("shell","Shell"),"sh":("shell","Shell")}

def detect(name, text, force=""):
    if force:
        return next((v for v in EXT.values() if v[0] == force), (force, force.upper()))
    ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""
    if ext in EXT: return EXT[ext]
    if text.startswith("#!"):
        for k, v in SHEBANG.items():
            if k in text.split("\n", 1)[0]: return v
    return ("text", "Text")

import re
def walk(ns, path=()):
    for n in ns:
        yield n, path + (n["id"],)
        yield from walk(n.get("children", []), path + (n["id"],))

def find_node(d, ref):
    """ref = menu id, or a label path like 'CodeCraft/Web/Portal' (EN/BN/id, case-insensitive). -> (node, [id path]) or (None, None)"""
    ref = ref.strip()
    for n, p in walk(d["menu"]):
        if n["id"] == ref: return n, list(p)
    segs = [s.strip().lower() for s in ref.strip("/").split("/") if s.strip()]
    if not segs: return None, None
    def go(ns, sg, path):
        for n in ns:
            if sg[0] in (n["id"].lower(), (n.get("en") or "").lower(), (n.get("bn") or "").lower()):
                if len(sg) == 1: return n, path + [n["id"]]
                r = go(n.get("children", []), sg[1:], path + [n["id"]])
                if r[0]: return r
        return None, None
    r = go(d["menu"], segs, [])
    if r[0]: return r
    root = next((n for n in d["menu"] if n["id"] == "codecraft"), None)   # 'Web/Portal' means CodeCraft/Web/Portal
    return go(root.get("children", []), segs, ["codecraft"]) if root else (None, None)

def ensure_root(d):
    root = next((n for n in d["menu"] if n["id"] == "codecraft"), None)
    if not root:
        root = {"id": "codecraft", "bn": "কোডক্রাফ্ট", "en": "CodeCraft", "icon": "❮❯", "open": True, "view": {"type": "codes"}, "children": []}
        k = next((j for j, n in enumerate(d["menu"]) if n["id"] == "registry"), len(d["menu"])); d["menu"].insert(k, root)
    root.setdefault("children", []); return root

def ensure_chain(d, parent, ppath, names, bns=()):
    """Create (or reuse, matched by name) nested submenus under parent. -> (deepest node, id path)"""
    ids = {n["id"] for n, _ in walk(d["menu"])}
    for k, name in enumerate(names):
        sib = parent.setdefault("children", [])
        hit = next((c for c in sib if name.lower() in ((c.get("en") or "").lower(), (c.get("bn") or "").lower())), None)
        if not hit:
            bn = bns[k].strip() if k < len(bns) and bns[k].strip() else name
            base = "c-" + (re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "m"); nid = base; i = 2
            while nid in ids: nid = f"{base}-{i}"; i += 1
            ids.add(nid)
            hit = {"id": nid, "bn": bn, "en": name, "view": {"type": "codes", "filter": {"menu_path": nid}}}
            sib.append(hit)
        parent = hit; ppath = ppath + [hit["id"]]
    return parent, ppath

def normalize(d):
    """Upgrade older data: language nodes filter by menu_path; entries get a menu_path."""
    root = ensure_root(d)
    for c in root["children"]:
        f = c.get("view", {}).get("filter", {})
        if "lang" in f: c["view"]["filter"] = {"menu_path": c["id"]}
    for it in d["codes"]:
        it.setdefault("menu_path", ["codecraft", "c-" + it["lang"]])
    return d
