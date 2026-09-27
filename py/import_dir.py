#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
import_dir.py — একটি গোটা ফোল্ডার একবারে mj এর CodeCraft এ যোগ করে

ব্যবহার (index.html/data.json/add.py এর ফোল্ডারে চালান):
    python import_dir.py /path/to/folder
    python import_dir.py /path/to/folder "কাস্টম মেনুর নাম"
    python import_dir.py ~/mj/projects/qf "Quraner Fariwala"

যা ঘটে:
    ১. ফোল্ডারের নাম (বা আপনার দেওয়া কাস্টম নাম) দিয়ে mj এর মেনু গাছের
       সবার উপরে একটি নতুন মেনু বসে।
    ২. ফোল্ডারের ভেতরের সাব-ফোল্ডার অনুযায়ী সাব মেনু তৈরি হয় (যত গভীরেই হোক)।
    ৩. প্রতিটি টেক্সট/কোড ফাইল তার সঠিক সাব মেনুর নিচে একটি CodeCraft এন্ট্রি
       হিসেবে যোগ হয় — প্রতিটির নিজস্ব অনন্য আইডি (CC-000123 ধরনের), এবং তা
       স্বয়ংক্রিয়ভাবে Registry ও কার্যক্রম-লগে যোগ হয়ে যায়।
    ৪. আগে একবার আনা ফাইল আবার চালালে বাদ যায় (ডুপ্লিকেট হয় না)।
    ৫. ছবি/ভিডিও/আর্কাইভ/বাইনারি ফাইল ও .git, node_modules ইত্যাদি ফোল্ডার
       এড়িয়ে যাওয়া হয়।
"""

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import add  # noqa: E402  (একই ফোল্ডারের add.py পুনর্ব্যবহার করা হচ্ছে)

SKIP_DIRS = {
    ".git", ".hg", ".svn", "node_modules", "__pycache__", ".venv", "venv",
    "env", "dist", "build", ".idea", ".vscode", ".next", ".cache",
    "target", "vendor", ".gradle", ".mypy_cache", ".pytest_cache",
}
SKIP_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".webp", ".bmp", ".svgz",
    ".pdf", ".zip", ".tar", ".gz", ".rar", ".7z", ".mp3", ".mp4", ".mov",
    ".avi", ".exe", ".dll", ".so", ".bin", ".class", ".jar", ".pyc",
    ".woff", ".woff2", ".ttf", ".eot", ".otf", ".db", ".sqlite", ".lock",
}
MAX_BYTES = 512_000  # এর চেয়ে বড় ফাইল বাদ যাবে (JSON ফুলে যাওয়া ঠেকাতে)


def build_fs_tree(root_path, root_name):
    """ডিরেক্টরি থেকে {name, children} মেনু-নোড ও ফাইলের তালিকা তৈরি করে।"""
    node = {"name": root_name, "children": []}
    files = []   # each: (path_list_including_root, absolute_file_path, filename)

    def walk(fs_dir, menu_node, path_list):
        try:
            names = sorted(os.listdir(fs_dir))
        except OSError as e:
            print(f"  ⚠ পড়া যায়নি: {fs_dir} ({e})")
            return
        for name in names:
            if name.startswith(".") or name in SKIP_DIRS:
                continue
            full = os.path.join(fs_dir, name)
            if os.path.isdir(full):
                child = {"name": name, "children": []}
                menu_node["children"].append(child)
                walk(full, child, path_list + [name])
            elif os.path.isfile(full):
                files.append((path_list, full, name))

    walk(root_path, node, [root_name])
    return node, files


def promote_to_top(menus, node):
    """একই নামের পুরোনো মেনু থাকলে সরিয়ে নতুন নোডটি সবার উপরে বসায়।"""
    existing = add.find_node(menus, node["name"])
    if existing is not None:
        menus.remove(existing)
    menus.insert(0, node)


def already_imported(items, path, filename):
    return any(it.get("path") == path and it.get("filename") == filename for it in items)


def read_text_file(full_path):
    try:
        size = os.path.getsize(full_path)
    except OSError:
        return None, "স্ট্যাট ব্যর্থ"
    if size > MAX_BYTES:
        return None, f"{size // 1024} KB — সীমার চেয়ে বড়"
    try:
        with open(full_path, "rb") as f:
            raw = f.read()
    except OSError as e:
        return None, str(e)
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        return None, "টেক্সট/UTF-8 নয়"
    return text.replace("\r\n", "\n").rstrip("\n"), None


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)

    src = os.path.expanduser(args[0])
    if not os.path.isdir(src):
        print(f"⚠ এটি কোনো ফোল্ডার নয় বা পাওয়া যায়নি: {src}")
        sys.exit(1)
    src = os.path.abspath(src)
    root_name = args[1] if len(args) > 1 and args[1].strip() else os.path.basename(src.rstrip("/")) or src

    print("=" * 54)
    print(f"  mj — ফোল্ডার ইম্পোর্ট: {src}")
    print(f"  মেনুর নাম: {root_name}")
    print("=" * 54)

    data = add.load_data()
    tree_node, files = build_fs_tree(src, root_name)
    promote_to_top(data["menus"], tree_node)

    added = skipped_binary = skipped_dup = skipped_ext = 0
    for path_list, full, name in files:
        ext = os.path.splitext(name)[1].lower()
        if ext in SKIP_EXTS:
            skipped_ext += 1
            continue
        if already_imported(data["items"], path_list, name):
            skipped_dup += 1
            continue
        text, err = read_text_file(full)
        if text is None:
            print(f"  ⚠ বাদ: {'/'.join(path_list[1:] + [name]) or name}  ({err})")
            skipped_binary += 1
            continue

        eid = add.next_id(data, "code")
        data["items"].append({
            "id": eid,
            "path": path_list,
            "title": name,
            "description": f"{root_name} থেকে স্বয়ংক্রিয়ভাবে আনা হয়েছে ({'/'.join(path_list[1:] + [name]) or name})।",
            "language": add.guess_language(name),
            "filename": name,
            "code": text,
            "created": time.strftime("%Y-%m-%d"),
        })
        add.log_event(data, "created", "code", eid, name)
        added += 1

    add.save_data(data)

    print(f"\n✔ {added}টি ফাইল CodeCraft এ যোগ হয়েছে (mj/{root_name} এর নিচে)।")
    if skipped_dup:
        print(f"  – {skipped_dup}টি আগেই আনা ছিল, বাদ দেওয়া হয়েছে।")
    if skipped_binary:
        print(f"  – {skipped_binary}টি ফাইল টেক্সট/UTF-8 নয় বা অনেক বড়, বাদ দেওয়া হয়েছে।")
    if skipped_ext:
        print(f"  – {skipped_ext}টি ছবি/বাইনারি ধরনের ফাইল এড়িয়ে যাওয়া হয়েছে।")
    print("\nদেখতে চালান:  python add.py serve")


if __name__ == "__main__":
    main()
