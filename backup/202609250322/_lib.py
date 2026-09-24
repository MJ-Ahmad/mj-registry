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
