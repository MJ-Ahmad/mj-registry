#!/usr/bin/env python3
"""Shared helpers: load/save data.json safely, unique IDs, history log."""
import json, os, shutil, sys
from datetime import datetime
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data.json")
KIND = {"task": ("TSK", "tasks"), "note": ("NOT", "notes"), "audit": ("AUD", "audits")}

def now(): return datetime.now().astimezone().isoformat(timespec="seconds")

def load():
    with open(DATA, encoding="utf-8") as f: return json.load(f)

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
