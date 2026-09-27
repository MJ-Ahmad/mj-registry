#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
add.py — "mj" প্ল্যাটফর্মে টাস্ক, নোট, অডিট বা কোডক্রাফ্ট এন্ট্রি যোগ করার স্ক্রিপ্ট

ব্যবহার (index.html ও data.json এর ফোল্ডারে চালান):
    python add.py            নতুন কোডক্রাফ্ট এন্ট্রি যোগ করুন (ডিফল্ট)
    python add.py task       নতুন টাস্ক যোগ করুন
    python add.py note       নতুন নোট যোগ করুন
    python add.py audit      নতুন অডিট এন্ট্রি যোগ করুন
    python add.py code       নতুন কোডক্রাফ্ট এন্ট্রি যোগ করুন (মেনু গাছসহ)
    python add.py list       সব কিছুর তালিকা ও সংখ্যা দেখুন
    python add.py delete     যেকোনো ধরনের একটি এন্ট্রি মুছুন
    python add.py setup      প্রাথমিক মেনু, লোগো ও সাইট তথ্য (আবার) বসান
    python add.py serve      লোকাল সার্ভার চালু করুন (পোর্ট 8000)
    python add.py serve 9000 অন্য পোর্টে চালু করুন

সব এন্ট্রিই স্বয়ংক্রিয়ভাবে একটি অনন্য আইডি পায় (TSK-, NOT-, AUD-, CC-) এবং
স্বয়ংক্রিয়ভাবে Registry ও কার্যক্রম-লগে (log) যোগ হয় — আলাদা করে কিছু করতে হয় না।
"""

import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
import urllib.request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")

SITE_TITLE = "mj"
LOGO_URL = "https://MJ-Ahmad.github.io/mj-registry/assets/logo.png"
SEP = " › "

PREFIX = {"task": "TSK", "note": "NOT", "audit": "AUD", "code": "CC"}
COLLECTION = {"task": "tasks", "note": "notes", "audit": "audits", "code": "items"}

DEFAULT_SITE = {
    "title": SITE_TITLE,
    "tagline_en": "Task · Note · Audit · Registry",
    "tagline_bn": "টাস্ক · নোট · অডিট · রেজিস্ট্রি",
    "logo": LOGO_URL,
    "version": "1.0.0",
    "quote_en": "Where every script is a verdict, every invocation a vote, and every log a legacy.",
    "quote_bn": "যেখানে প্রতিটি স্ক্রিপ্ট একটি রায়, প্রতিটি চালনা একটি ভোট, আর প্রতিটি লগ একটি উত্তরাধিকার।",
    "quick_links": [
        {"label_en": "Website", "label_bn": "ওয়েবসাইট", "icon": "◎", "url": "https://mj-ahmad.github.io/qf"},
        {"label_en": "Github", "label_bn": "গিটহাব", "icon": "•", "url": "https://github.com/MJ-Ahmad"}
    ],
    "quick_commands": [
        {"en": "python add.py task — add a task", "bn": "python add.py task — নতুন টাস্ক যোগ করুন"},
        {"en": "python add.py note — add a note", "bn": "python add.py note — নতুন নোট যোগ করুন"},
        {"en": "python add.py audit — add an audit entry", "bn": "python add.py audit — নতুন অডিট এন্ট্রি যোগ করুন"},
        {"en": "python add.py code — add a CodeCraft entry", "bn": "python add.py code — নতুন কোডক্রাফ্ট এন্ট্রি যোগ করুন"},
        {"en": "python import_dir.py <folder> — import a whole folder into mj", "bn": "python import_dir.py <ফোল্ডার> — পুরো ফোল্ডার mj তে যোগ করুন"},
        {"en": "python add.py serve — open this dashboard", "bn": "python add.py serve — এই ড্যাশবোর্ড খুলুন"}
    ],
    "emergency_en": "Data won't load? Run: python add.py serve — then open http://localhost:8000",
    "emergency_bn": "ডাটা লোড হচ্ছে না? চালান: python add.py serve — তারপর http://localhost:8000 খুলুন",
}
DEFAULT_MENUS = [
    "Systems",
    {"name": "Projects", "children": ["Quraner Fariwala", "MJSovereign"]},
    "README", "Git", "Python", "Node", "JSON", ".NET", "CLI", "Command", "Scripts",
]

# ফাইলের এক্সটেনশন থেকে ভাষা/লেবেল চেনার তালিকা
EXT_LANG = {
    ".html": "HTML", ".htm": "HTML", ".css": "CSS",
    ".json": "JSON", ".py": "Python",
    ".js": "Node", ".mjs": "Node", ".cjs": "Node",
    ".ts": "TypeScript", ".sh": "Bash", ".bash": "Bash", ".zsh": "Bash",
    ".php": "PHP", ".java": "Java", ".c": "C", ".cpp": "C++", ".cs": "C#",
    ".go": "Go", ".rs": "Rust", ".sql": "SQL",
    ".yml": "YAML", ".yaml": "YAML", ".xml": "XML",
    ".md": "Markdown", ".txt": "Text", ".env": "Text", ".ini": "Text",
}


# ------------------------------------------------------------ menu tree ----
def norm_nodes(lst):
    out = []
    for m in lst or []:
        if isinstance(m, str):
            out.append({"name": m, "children": []})
        elif isinstance(m, dict) and m.get("name"):
            out.append({"name": m["name"], "children": norm_nodes(m.get("children"))})
    return out


def find_node(nodes, name):
    return next((n for n in nodes if n["name"] == name), None)


def children_of(tree, path):
    lst = tree
    for name in path:
        node = find_node(lst, name)
        if node is None:
            node = {"name": name, "children": []}
            lst.append(node)
        lst = node["children"]
    return lst


def merge_nodes(dst, src):
    for n in src:
        cur = find_node(dst, n["name"])
        if cur is None:
            dst.append({"name": n["name"], "children": []})
            cur = dst[-1]
        merge_nodes(cur["children"], n["children"])


def count_code_items(items, path):
    return sum(1 for it in items if it.get("path", [])[:len(path)] == path)


# ------------------------------------------------------------ data file ----
def normalize(data):
    site = data.setdefault("site", {})
    for k, v in DEFAULT_SITE.items():
        site.setdefault(k, v)

    data["menus"] = norm_nodes(data.get("menus") or DEFAULT_MENUS)
    data.setdefault("items", [])
    for it in data["items"]:
        if not isinstance(it.get("path"), list) or not it["path"]:
            it["path"] = [it["menu"]] if it.get("menu") else []
        it.pop("menu", None)
        children_of(data["menus"], it["path"])

    data.setdefault("tasks", [])
    data.setdefault("notes", [])
    data.setdefault("audits", [])
    data.setdefault("log", [])
    meta = data.setdefault("meta", {})
    meta.setdefault("counters", {})
    for k in PREFIX:
        meta["counters"].setdefault(k, 0)
    meta.setdefault("updated", time.strftime("%Y-%m-%d"))
    return data


def load_data():
    if not os.path.exists(DATA_FILE):
        return normalize({"site": {}, "menus": [], "items": [], "tasks": [], "notes": [], "audits": [], "log": []})
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return normalize(json.load(f))


def save_data(data):
    data["meta"]["updated"] = time.strftime("%Y-%m-%d")
    tmp = DATA_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.replace(tmp, DATA_FILE)


def next_id(data, kind):
    data["meta"]["counters"][kind] += 1
    return f"{PREFIX[kind]}-{data['meta']['counters'][kind]:06d}"


def log_event(data, action, kind, entry_id, title):
    data["log"].append({
        "id": f"LOG-{len(data['log']) + 1:06d}",
        "type": kind,
        "action": action,          # "created" | "deleted"
        "ref": entry_id,
        "title": title,
        "at": time.strftime("%Y-%m-%d %H:%M"),
    })


# ---------------------------------------------------------------- input ----
def ask(prompt, required=True, default=None):
    while True:
        suffix = f" [{default}]" if default else ""
        try:
            value = input(f"{prompt}{suffix}: ").strip()
        except EOFError:
            print("\nইনপুট শেষ হয়ে গেছে, বন্ধ করা হলো।")
            sys.exit(1)
        if not value and default:
            return default
        if value or not required:
            return value
        print("  ⚠ এটি খালি রাখা যাবে না।")


def ask_multiline(prompt):
    print(f"{prompt} (একাধিক লাইন লিখতে পারেন; শেষ করতে একটি খালি লাইনে Enter চাপুন)")
    lines = []
    while True:
        try:
            line = input("  > ")
        except EOFError:
            break
        if line == "":
            if lines:
                break
            print("  ⚠ এটি খালি রাখা যাবে না।")
            continue
        lines.append(line)
    return "\n".join(lines)


def choose_path(data):
    """mj এর মেনু গাছে ধাপে ধাপে নেমে গিয়ে (অসীম গভীরতা) একটি পথ বেছে নেয়।"""
    path = []
    print("\nmj এর কোন মেনুর আওতায় যোগ করবেন?")
    print("(মেনু বেছে ভেতরে ঢুকুন; দরকার হলে নতুন সাব মেনু বানান; শেষে 0 দিয়ে সংরক্ষণ করুন)")
    while True:
        kids = children_of(data["menus"], path)
        print("\n  📂 mj/" + SEP.join(path))
        for i, n in enumerate(kids, 1):
            total = count_code_items(data["items"], path + [n["name"]])
            sub = f", {len(n['children'])}টি সাব মেনু" if n["children"] else ""
            print(f"   {i}. {n['name']}  ({total}টি এন্ট্রি{sub})")
        new_no = len(kids) + 1
        print(f"   {new_no}. ➕ নতুন সাব মেনু তৈরি করুন")
        if path:
            print(f"   0. ✔ এখানেই সংরক্ষণ করুন  (mj/{SEP.join(path)})")

        raw = ask("নম্বর লিখুন (অথবা সরাসরি নাম লিখুন)")
        if raw == "0" and path:
            return path
        if raw.isdigit():
            n = int(raw)
            if 1 <= n <= len(kids):
                path = path + [kids[n - 1]["name"]]
            elif n == new_no:
                path = path + [ask("নতুন নাম")]
            else:
                print("  ⚠ ভুল নম্বর।")
                continue
        else:
            path = path + [raw]
        children_of(data["menus"], path)


# -------------------------------------------------------- file / source ----
def to_raw_github(url):
    m = re.match(r"^https?://github\.com/([^/]+)/([^/]+)/blob/(.+)$", url)
    if m:
        return f"https://raw.githubusercontent.com/{m.group(1)}/{m.group(2)}/{m.group(3)}"
    return url


def read_source(src):
    if re.match(r"^https?://", src, re.I):
        url = to_raw_github(src)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "mj-CodeCraft/1.0"})
            with urllib.request.urlopen(req, timeout=20) as resp:
                raw = resp.read()
        except Exception as e:
            print(f"  ⚠ লিংক থেকে আনা যায়নি: {e}")
            return None
        name = os.path.basename(urllib.parse.urlparse(url).path) or "file.txt"
    else:
        path = os.path.expanduser(src.strip('"').strip("'"))
        candidates = [path] if os.path.isabs(path) else [
            os.path.join(BASE_DIR, path),
            os.path.join(os.getcwd(), path),
        ]
        found = next((p for p in candidates if os.path.isfile(p)), None)
        if not found:
            print("  ⚠ ফাইল পাওয়া যায়নি। নাম/পথ আবার দেখুন।")
            return None
        try:
            with open(found, "rb") as f:
                raw = f.read()
        except OSError as e:
            print(f"  ⚠ ফাইল পড়া যায়নি: {e}")
            return None
        name = os.path.basename(found)

    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        print("  ⚠ এটি টেক্সট ফাইল নয় (বা UTF-8 নয়)। ছবি/বাইনারি ফাইল যোগ করা যাবে না।")
        return None
    return text.replace("\r\n", "\n").rstrip("\n"), name


def read_pasted_code():
    print("কোড/টেক্সট পেস্ট করুন। শেষ করতে একটি আলাদা লাইনে শুধু END লিখুন।")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines).rstrip("\n")


def guess_language(filename):
    return EXT_LANG.get(os.path.splitext(filename)[1].lower(), "Text")


# ------------------------------------------------------------- commands ----
def cmd_add_simple(kind, title_label):
    """task / note / audit — একই ছাঁচের সাধারণ এন্ট্রি।"""
    data = load_data()
    print("=" * 50)
    print(f"  mj — নতুন {title_label}")
    print("=" * 50)
    title = ask("\nহেডলাইন (শিরোনাম)")
    description = ask_multiline("\nবিবরণ")
    status = ask("অবস্থা (যেমন: চলমান/বাকি/সম্পন্ন)", required=False, default="")

    eid = next_id(data, kind)
    entry = {"id": eid, "title": title, "description": description, "created": time.strftime("%Y-%m-%d")}
    if status:
        entry["status"] = status
    data[COLLECTION[kind]].append(entry)
    log_event(data, "created", kind, eid, title)
    save_data(data)

    print(f"\n✔ যোগ হয়েছে!  আইডি: {eid}")
    print(f"  {title_label}: {title}")
    print("\nদেখতে চালান:  python add.py serve")


def cmd_add_code():
    data = load_data()
    print("=" * 50)
    print("  mj — নতুন CodeCraft এন্ট্রি")
    print("=" * 50)

    path = choose_path(data)
    title = ask("\nহেডলাইন (শিরোনাম)")
    description = ask_multiline("\nবিবরণ")

    print("\nফাইলের লিংক (https://…) লিখুন, অথবা ফাইল একই ফোল্ডারে থাকলে শুধু ফাইলের নাম লিখুন।")
    print("ফাইল ছাড়া শুধু কোড পেস্ট করতে চাইলে খালি রেখে Enter চাপুন।")
    code = filename = None
    while code is None:
        src = ask("ফাইল লিংক / ফাইলের নাম", required=False)
        if not src:
            code = read_pasted_code()
            if not code:
                print("  ⚠ কিছুই পেস্ট করা হয়নি।")
                code = None
                continue
            filename = ask("ফাইলের নাম (যেমন app.py, না থাকলে খালি রাখুন)", required=False)
            break
        result = read_source(src)
        if result:
            code, filename = result

    language = ask("ভাষা/লেবেল (HTML, JSON, Python, Node…)", default=guess_language(filename or ""))

    eid = next_id(data, "code")
    data["items"].append({
        "id": eid, "path": path, "title": title, "description": description,
        "language": language, "filename": filename or "", "code": code,
        "created": time.strftime("%Y-%m-%d"),
    })
    log_event(data, "created", "code", eid, title)
    save_data(data)

    print(f"\n✔ যোগ হয়েছে!  আইডি: {eid}")
    print(f"  মেনু    : mj/{SEP.join(path)}")
    print(f"  হেডলাইন : {title}")
    print(f"  ভাষা    : {language}   ফাইল: {filename or '—'}   ({len(code.splitlines())} লাইন)")
    print("\nদেখতে চালান:  python add.py serve")


def print_tree(nodes, items, path, depth):
    for n in nodes:
        p = path + [n["name"]]
        print("   " + "    " * depth + f"├─ {n['name']}  ({count_code_items(items, p)})")
        print_tree(n["children"], items, p, depth + 1)


def cmd_list():
    data = load_data()
    print(f"টাস্ক: {len(data['tasks'])}   নোট: {len(data['notes'])}   অডিট: {len(data['audits'])}   "
          f"CodeCraft: {len(data['items'])}")
    print(f"সব মিলিয়ে Registry: {len(data['tasks']) + len(data['notes']) + len(data['audits']) + len(data['items'])}\n")
    print("mj/  — মেনু গাছ:")
    print_tree(data["menus"], data["items"], [], 0)


def cmd_delete():
    data = load_data()
    rows = []
    for kind in ("task", "note", "audit", "code"):
        for it in data[COLLECTION[kind]]:
            rows.append((kind, it))
    if not rows:
        print("মোছার মতো কোনো এন্ট্রি নেই।")
        return
    for i, (kind, it) in enumerate(rows, 1):
        extra = (" mj/" + SEP.join(it["path"])) if kind == "code" else ""
        print(f"{i:>3}. [{it['id']}] {it['title']}{extra}")
    raw = ask("\nকোন নম্বরটি মুছবেন? (বাতিল করতে খালি রাখুন)", required=False)
    if not raw.isdigit() or not (1 <= int(raw) <= len(rows)):
        print("বাতিল করা হলো।")
        return
    kind, it = rows[int(raw) - 1]
    if ask(f"“{it['title']}” মুছে ফেলবেন? (y/n)", default="n").lower() != "y":
        print("বাতিল করা হলো।")
        return
    data[COLLECTION[kind]].remove(it)
    log_event(data, "deleted", kind, it["id"], it["title"])
    save_data(data)
    print("✔ মুছে ফেলা হয়েছে।")


def cmd_setup():
    """প্রাথমিক মেনু, লোগো ও সাইট তথ্য বিদ্যমান data.json এ যোগ করে (কিছু মোছে না)।"""
    data = load_data()
    merge_nodes(data["menus"], norm_nodes(DEFAULT_MENUS))
    # ব্র্যান্ড পরিচয় (নাম/লোগো/ট্যাগলাইন) সবসময় নতুন mj পরিচয়ে বসবে
    data["site"]["title"] = DEFAULT_SITE["title"]
    data["site"]["logo"] = DEFAULT_SITE["logo"]
    data["site"]["tagline_en"] = DEFAULT_SITE["tagline_en"]
    data["site"]["tagline_bn"] = DEFAULT_SITE["tagline_bn"]
    data["site"].pop("tagline", None)
    data["site"].pop("root_label", None)
    # বাকি সাইট তথ্য (কোট, কুইক লিংক ইত্যাদি) শুধু না থাকলেই বসবে
    for k, v in DEFAULT_SITE.items():
        data["site"].setdefault(k, v)
    save_data(data)
    print("✔ প্রাথমিক মেনু, লোগো ও সাইট তথ্য সেট হয়েছে। আগের এন্ট্রি অক্ষত আছে।\n")
    cmd_list()


def open_in_browser(url):
    try:
        if shutil.which("termux-open-url"):
            subprocess.Popen(["termux-open-url", url])
        else:
            import webbrowser
            webbrowser.open(url)
    except Exception:
        pass


def cmd_serve(port):
    import functools
    import http.server
    import socketserver

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=BASE_DIR)
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("127.0.0.1", port), handler) as httpd:
            url = f"http://localhost:{port}/index.html"
            print(f"mj চালু হলো: {url}   (বন্ধ করতে Ctrl+C)")
            open_in_browser(url)
            httpd.serve_forever()
    except OSError as e:
        print(f"সার্ভার চালু করা যায়নি: {e}\nঅন্য পোর্ট দিন, যেমন: python add.py serve 9000")
    except KeyboardInterrupt:
        print("\nসার্ভার বন্ধ করা হলো।")


def main():
    args = sys.argv[1:]
    cmd = args[0].lower() if args else "code"
    try:
        if cmd == "task":
            cmd_add_simple("task", "টাস্ক")
        elif cmd == "note":
            cmd_add_simple("note", "নোট")
        elif cmd == "audit":
            cmd_add_simple("audit", "অডিট এন্ট্রি")
        elif cmd == "code":
            cmd_add_code()
        elif cmd == "list":
            cmd_list()
        elif cmd == "delete":
            cmd_delete()
        elif cmd == "setup":
            cmd_setup()
        elif cmd == "serve":
            cmd_serve(int(args[1]) if len(args) > 1 and args[1].isdigit() else 8000)
        else:
            print(__doc__)
    except KeyboardInterrupt:
        print("\nবাতিল করা হলো।")


if __name__ == "__main__":
    main()
