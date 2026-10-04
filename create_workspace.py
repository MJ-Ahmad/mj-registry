#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from datetime import datetime


# ============================================================
# CONFIGURATION
# ============================================================

ROOT = Path("mj/root/mj")

# ============================================================
# HELPERS
# ============================================================

def create_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def create_file(path: Path, content: str):
    if not path.exists():
        path.write_text(content, encoding="utf-8")


# ============================================================
# DATE STRUCTURE
# ============================================================

today = datetime.now()

YEAR = today.strftime("%Y")
MONTH = today.strftime("%Y-%m")
DAY = today.strftime("%Y-%m-%d")

WORKSPACE = (
    ROOT
    / "workspace"
    / YEAR
    / MONTH
    / DAY
)

# ============================================================
# GENERAL DAILY WORKSPACE
# ============================================================

general_folders = [
    "notes",
    "tasks",
    "commands",
    "scripts",
    "files",
    "logs",
    "research",
    "meetings",
    "ideas",
    "drafts",
    "scratchpad",
    "output",
    "archive",
]

for folder in general_folders:
    create_dir(WORKSPACE / folder)

# ============================================================
# ALI BABA WORKSPACE
# ============================================================

ali_baba_folders = [
    "tasks",
    "printing",
    "photocopy",
    "scanning",
    "typing",
    "graphics",
    "customers",
    "finance",
    "reports",
    "notes",
]

for folder in ali_baba_folders:
    create_dir(
        WORKSPACE
        / "ali-baba"
        / folder
    )

# ============================================================
# QURANER FARIWALA WORKSPACE
# ============================================================

qf_folders = [
    "tasks",
    "planning",
    "fundraising",
    "donors",
    "zakat",
    "waqf",
    "printing",
    "distribution",
    "marketing",
    "finance",
    "volunteers",
    "schools",
    "masjids",
    "publication",
    "media",
    "campaigns",
    "inventory",
    "reports",
    "ideas",
    "notes",
]

for folder in qf_folders:
    create_dir(
        WORKSPACE
        / "quraner-fariwala"
        / folder
    )

# ============================================================
# README
# ============================================================

create_file(
    WORKSPACE / "README.md",
    f"""# Daily Workspace

Date: {DAY}

## Primary Objectives

-

## Important Tasks

-

## Notes

-

## Challenges

-

## Review

-

## Next Actions

-

"""
)

# ============================================================
# DAILY LOG
# ============================================================

create_file(
    WORKSPACE / "logs" / "daily-log.md",
    f"""# Daily Log

Date: {DAY}

## Morning

-

## Afternoon

-

## Evening

-

## Completed

-

## Pending

-

"""
)

# ============================================================
# ALI BABA LOG
# ============================================================

create_file(
    WORKSPACE
    / "ali-baba"
    / "notes"
    / "daily-work-log.md",
    f"""# Ali Baba Daily Log

Date: {DAY}

## Customers

-

## Printing

-

## Photocopy

-

## Scanning

-

## Typing

-

## Graphics

-

## Income

-

## Notes

-

"""
)

# ============================================================
# QURANER FARIWALA LOG
# ============================================================

create_file(
    WORKSPACE
    / "quraner-fariwala"
    / "notes"
    / "daily-progress.md",
    f"""# Quraner Fariwala Daily Progress

Date: {DAY}

## Tasks

-

## Fundraising

-

## Donors

-

## Distribution

-

## Marketing

-

## Finance

-

## Volunteers

-

## Progress

-

## Next Steps

-

"""
)

# ============================================================
# OUTPUT
# ============================================================

print()
print("=" * 60)
print("DAILY WORKSPACE READY")
print("=" * 60)
print(f"Date      : {DAY}")
print(f"Workspace : {WORKSPACE}")
print("=" * 60)
print()
