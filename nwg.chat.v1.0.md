আমি আপনার জন্য পুরো প্রজেক্ট scaffold-টি এখনই প্রস্তুত করে দিচ্ছি, যাতে আপনি এটি কপি/পেস্ট করে আপনার GitHub repo-তে ব্যবহার করতে পারেন।  
নিচে আমি একটি সম্পূর্ণ, production-ready initial project structure এবং কোডের পূর্ণ সেট দেব।

প্রথমে এই repo-র জন্য ফাইল-স্ট্রাকচার:

national-workforce-grid/
├── index.html
├── data.json
├── add.py
├── validate.py
├── _lib.py
├── run.sh
├── README.md
├── CONTRIBUTING.md
├── DEPLOYMENT.md
├── ARCHITECTURE.md
├── package.json
├── .gitignore
├── .github/
│   ├── workflows/
│   │   └── validate.yml
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md
│       └── feature_request.md
├── assets/
│   ├── css/
│   │   ├── style.css
│   │   └── theme.css
│   ├── js/
│   │   ├── lang.js
│   │   ├── ui.js
│   │   └── main.js
│   ├── images/
│   │   ├── logo.svg
│   │   └── splash.svg
│   └── .gitkeep
├── includes/
│   ├── header.html
│   ├── menu.html
│   └── footer.html
├── modules/
│   ├── identity/
│   │   └── README.md
│   ├── governance/
│   │   └── README.md
│   ├── geogrid/
│   │   └── README.md
│   ├── reporting/
│   │   └── README.md
│   ├── analytics/
│   │   └── README.md
│   ├── command/
│   │   └── README.md
│   ├── ledger/
│   │   └── README.md
│   ├── zone/
│   │   └── README.md
│   └── core/
│       └── README.md

তারপর নিচের ফাইলগুলো একে একে:

1) README.md

```md
# National Workforce Grid

A production-ready bilingual (EN|BN) platform starter for workforce and governance coordination.

## Overview

This repository contains a complete initial project structure with:
- bilingual homepage
- JSON-driven data layer
- validation scripts
- module folders
- local serving script
- documentation and deployment guidance

## Repository Structure

```text
national-workforce-grid/
├── index.html
├── data.json
├── add.py
├── validate.py
├── _lib.py
├── run.sh
├── README.md
├── CONTRIBUTING.md
├── DEPLOYMENT.md
├── ARCHITECTURE.md
├── package.json
├── .gitignore
├── .github/
│   ├── workflows/
│   │   └── validate.yml
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md
│       └── feature_request.md
├── assets/
│   ├── css/
│   │   ├── style.css
│   │   └── theme.css
│   ├── js/
│   │   ├── lang.js
│   │   ├── ui.js
│   │   └── main.js
│   ├── images/
│   │   ├── logo.svg
│   │   └── splash.svg
│   └── .gitkeep
├── includes/
│   ├── header.html
│   ├── menu.html
│   └── footer.html
├── modules/
│   ├── identity/
│   │   └── README.md
│   ├── governance/
│   │   └── README.md
│   ├── geogrid/
│   │   └── README.md
│   ├── reporting/
│   │   └── README.md
│   ├── analytics/
│   │   └── README.md
│   ├── command/
│   │   └── README.md
│   ├── ledger/
│   │   └── README.md
│   ├── zone/
│   │   └── README.md
│   └── core/
│       └── README.md
```

## Quick Start

```bash
chmod +x run.sh
./run.sh
```

Then open:

```text
http://localhost:8000
```

## Validate Data

```bash
python3 validate.py
```

## Add Module Data

```bash
python3 add.py
```

## Features

- Bilingual EN|BN interface
- Central JSON data source
- Dynamic module rendering
- Modular architecture
- Validation layer
- Local dev server
- Deployment-ready structure

## License

MIT
```

2) .gitignore

```gitignore
__pycache__/
*.pyc
*.pyo
*.pyd
.venv/
venv/
.env
.env.*
.DS_Store
*.log
node_modules/
coverage/
.pytest_cache/
*.sqlite3
.idea/
.vscode/

# Build artifacts
build/
dist/
*.egg-info/
```

3) package.json

```json
{
  "name": "national-workforce-grid",
  "version": "1.0.0",
  "description": "Central bilingual (EN|BN) project management system for national workforce coordination",
  "main": "index.html",
  "scripts": {
    "start": "chmod +x run.sh && ./run.sh",
    "validate": "python3 validate.py",
    "add-module": "python3 add.py",
    "dev": "PORT=8000 ./run.sh"
  },
  "keywords": [
    "workforce",
    "governance",
    "bilingual",
    "platform",
    "modular",
    "dashboard",
    "national"
  ],
  "author": "MJ-Ahmad",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/MJ-Ahmad/national-workforce-grid.git"
  },
  "bugs": {
    "url": "https://github.com/MJ-Ahmad/national-workforce-grid/issues"
  },
  "homepage": "https://github.com/MJ-Ahmad/national-workforce-grid#readme"
}
```

4) data.json

```json
{
  "app": {
    "name": {
      "en": "National Workforce Grid",
      "bn": "ন্যাশনাল ওয়ার্কফোর্স গ্রিড"
    },
    "tagline": {
      "en": "Central coordination platform for a resilient national workforce system.",
      "bn": "একটি শক্তিশালী জাতীয় কর্মীবাহিনী ব্যবস্থার জন্য কেন্দ্রীয় সমন্বয় প্ল্যাটফর্ম।"
    }
  },
  "navigation": [
    { "key": "home", "label": { "en": "Home", "bn": "হোম" } },
    { "key": "identity", "label": { "en": "Identity", "bn": "পরিচয়" } },
    { "key": "governance", "label": { "en": "Governance", "bn": "শাসন" } },
    { "key": "geogrid", "label": { "en": "Geo Grid", "bn": "জিও গ্রিড" } },
    { "key": "reporting", "label": { "en": "Reporting", "bn": "রিপোর্টিং" } }
  ],
  "metrics": [
    { "key": "coverage", "label": { "en": "Coverage", "bn": "কভারেজ" }, "value": "98.4%", "context": { "en": "Operational coverage", "bn": "কার্যকর কভারেজ" } },
    { "key": "verified", "label": { "en": "Verified", "bn": "যাচাইকৃত" }, "value": "2.6M", "context": { "en": "Credentialed profiles", "bn": "যোগ্যতা সম্পন্ন প্রোফাইল" } },
    { "key": "alerts", "label": { "en": "Alerts", "bn": "এলার্ট" }, "value": "318", "context": { "en": "Priority incidents", "bn": "প্রাধান্য সংকট" } },
    { "key": "uptime", "label": { "en": "Uptime", "bn": "আপটাইম" }, "value": "99.97%", "context": { "en": "System reliability", "bn": "সিস্টেম নির্ভরযোগ্যতা" } }
  ],
  "modules": {
    "identity": {
      "title": { "en": "Identity & Verification", "bn": "পরিচয় ও যাচাই" },
      "description": {
        "en": "Secure, verifiable identity management for workforce and service access.",
        "bn": "কর্মী ও সেবা অ্যাক্সেসের জন্য নিরাপদ ও যাচাইকৃত পরিচয় ব্যবস্থাপনা।"
      },
      "status": { "en": "Operational", "bn": "কার্যকর" },
      "badge": "identity"
    },
    "governance": {
      "title": { "en": "Governance & Contracts", "bn": "শাসন ও কন্ট্রাক্ট" },
      "description": {
        "en": "Policies, accountability, and automation of governance workflows.",
        "bn": "নীতি, দায়বদ্ধতা এবং শাসন প্রক্রিয়ার স্বয়ংক্রিয়তা।"
      },
      "status": { "en": "Active", "bn": "সক্রিয়" },
      "badge": "governance"
    },
    "geogrid": {
      "title": { "en": "Geo Grid & Zones", "bn": "জিও গ্রিড ও অঞ্চল" },
      "description": {
        "en": "Map-based regional coordination for distributed operations and zones.",
        "bn": "বিতরণকৃত কার্যক্রম ও অঞ্চলগুলির জন্য মানচিত্রভিত্তিক আঞ্চলিক সমন্বয়।"
      },
      "status": { "en": "Mapped", "bn": "মানচিত্রিত" },
      "badge": "geogrid"
    },
    "reporting": {
      "title": { "en": "Reporting & Compliance", "bn": "রিপোর্টিং ও কমপ্লায়েন্স" },
      "description": {
        "en": "Operational reporting, auditability, and evidence-based compliance tracking.",
        "bn": "কার্যক্রম রিপোর্ট, অডিটযোগ্যতা এবং প্রমাণভিত্তিক কমপ্লায়েন্স ট্র্যাকিং।"
      },
      "status": { "en": "Live", "bn": "লাইভ" },
      "badge": "reporting"
    }
  },
  "translations": {
    "brand": {
      "eyebrow": { "en": "National Digital Infrastructure", "bn": "জাতীয় ডিজিটাল অবকাঠামো" },
      "title": { "en": "National Workforce Grid", "bn": "ন্যাশনাল ওয়ার্কফোর্স গ্রিড" }
    },
    "hero": {
      "kicker": { "en": "Central Coordination Platform", "bn": "কেন্দ্রীয় সমন্বয় প্ল্যাটফর্ম" },
      "title": {
        "en": "A resilient, bilingual public system for workforce governance.",
        "bn": "কর্মীবাহিনী শাসনের জন্য একটি স্থিতিশীল, দ্বিভাষিক জনসাধারণের সিস্টেম।"
      },
      "subtitle": {
        "en": "Connect identity, policy, reporting, analytics, and operational execution through a unified national framework.",
        "bn": "একটি একীভূত জাতীয় কাঠামোর মাধ্যমে পরিচয়, নীতি, রিপোর্টিং, বিশ্লেষণ ও কার্যক্রম সম্পাদনের সাথে সংযুক্ত হোন।"
      },
      "primaryAction": { "en": "Open dashboard", "bn": "ড্যাশবোর্ড খুলুন" },
      "secondaryAction": { "en": "Review modules", "bn": "মডিউল দেখুন" }
    },
    "modules": {
      "label": { "en": "Core Modules", "bn": "কোর মডিউল" },
      "title": { "en": "Operational capability map", "bn": "কার্যক্ষমতা মানচিত্র" }
    },
    "footer": {
      "text": {
        "en": "© 2026 National Workforce Grid. Built for secure and scalable national coordination.",
        "bn": "© ২০২৬ ন্যাশনাল ওয়ার্কফোর্স গ্রিড। নিরাপদ ও স্কেলেবল জাতীয় সমন্বয়ের জন্য নির্মিত।"
      }
    }
  }
}
```

5) index.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>National Workforce Grid</title>
    <meta
      name="description"
      content="A bilingual national workforce and governance dashboard."
    />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+Bengali:wght@400;500;600;700;800&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="assets/css/style.css" />
    <link rel="stylesheet" href="assets/css/theme.css" />
  </head>
  <body>
    <div class="app-shell">
      <header class="topbar">
        <div class="brand-wrap">
          <img src="assets/images/logo.svg" alt="Logo" class="brand-logo" />
          <div>
            <p class="eyebrow" data-i18n="brand.eyebrow">National Digital Infrastructure</p>
            <h1 class="brand-name" data-i18n="brand.title">National Workforce Grid</h1>
          </div>
        </div>

        <nav class="main-nav" id="main-nav" aria-label="Main navigation"></nav>

        <div class="header-actions">
          <button id="lang-toggle" class="lang-toggle" type="button" aria-label="Change language">
            <span>EN</span>
            <span class="divider">|</span>
            <span>BN</span>
          </button>
        </div>
      </header>

      <main class="page-content">
        <section class="hero-panel">
          <div class="hero-copy">
            <p class="hero-kicker" data-i18n="hero.kicker">Central Coordination Platform</p>
            <h2 data-i18n="hero.title">A resilient, bilingual public system for workforce governance.</h2>
            <p class="hero-text" data-i18n="hero.subtitle">
              Connect identity, policy, reporting, analytics, and operational execution through a unified national framework.
            </p>
            <div class="cta-row">
              <button class="primary-btn" data-i18n="hero.primaryAction">Open dashboard</button>
              <button class="secondary-btn" data-i18n="hero.secondaryAction">Review modules</button>
            </div>
          </div>

          <div class="hero-visual">
            <img src="assets/images/splash.svg" alt="System illustration" />
          </div>
        </section>

        <section class="metrics-grid" id="metrics-grid"></section>

        <section class="modules-section">
          <div class="section-header">
            <div>
              <p class="eyebrow" data-i18n="modules.label">Core Modules</p>
              <h3 data-i18n="modules.title">Operational capability map</h3>
            </div>
          </div>
          <div id="module-grid" class="module-grid"></div>
        </section>
      </main>

      <footer class="footer">
        <p data-i18n="footer.text">© 2026 National Workforce Grid. Built for secure and scalable national coordination.</p>
      </footer>
    </div>

    <script src="assets/js/lang.js"></script>
    <script src="assets/js/ui.js"></script>
    <script src="assets/js/main.js"></script>
  </body>
</html>
```

6) _lib.py

```python
import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "data.json"

def load_json(path: str | Path = DATA_FILE):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(data, path: str | Path = DATA_FILE):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

def get_lang_value(value, lang="en"):
    if isinstance(value, dict):
        return value.get(lang, value.get("en", next(iter(value.values()), "")))
    return value

def validate_structure(data):
    issues = []

    if "modules" not in data or not isinstance(data["modules"], dict):
        issues.append("Missing 'modules' object.")
        return issues

    for module_key, module_data in data["modules"].items():
        if not isinstance(module_data, dict):
            issues.append(f"Module '{module_key}' must be an object.")
            continue

        required_fields = ["title", "description", "status", "badge"]
        for field in required_fields:
            if field not in module_data:
                issues.append(f"Module '{module_key}' is missing '{field}'.")

        for field in ["title", "description", "status"]:
            if field in module_data and isinstance(module_data[field], dict):
                if "en" not in module_data[field] or "bn" not in module_data[field]:
                    issues.append(f"Module '{module_key}' field '{field}' requires both 'en' and 'bn' values.")

    return issues

def ensure_module_entry(module_key, title_en, title_bn, description_en, description_bn, status_en="Ready", status_bn="প্রস্তুত"):
    data = load_json()
    modules = data.setdefault("modules", {})

    modules[module_key] = {
        "title": {"en": title_en, "bn": title_bn},
        "description": {"en": description_en, "bn": description_bn},
        "status": {"en": status_en, "bn": status_bn},
        "badge": module_key,
    }

    save_json(data)
    return modules[module_key]
```

7) add.py

```python
#!/usr/bin/env python3
import json
from _lib import ensure_module_entry

def prompt(label, default=""):
    value = input(f"{label} [{default}]: ").strip()
    return value if value else default

def main():
    print("\nNational Workforce Grid - Module Data Adder\n")

    key = prompt("Module key", "new-module")
    title_en = prompt("English title", "New Module")
    title_bn = prompt("Bangla title", "নতুন মডিউল")
    description_en = prompt("English description", "A new module for the platform.")
    description_bn = prompt("Bangla description", "প্ল্যাটফর্মের জন্য একটি নতুন মডিউল।")
    status_en = prompt("English status", "Ready")
    status_bn = prompt("Bangla status", "প্রস্তুত")

    result = ensure_module_entry(
        key,
        title_en,
        title_bn,
        description_en,
        description_bn,
        status_en,
        status_bn,
    )

    print("\nModule added successfully:")
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
```

8) validate.py

```python
#!/usr/bin/env python3
from _lib import load_json, validate_structure

def main():
    print("Checking data.json structure...\n")
    data = load_json()
    issues = validate_structure(data)

    if not issues:
        print("Validation passed: data.json is structurally valid.")
        return 0

    print("Validation issues found:\n")
    for issue in issues:
        print(f"- {issue}")
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
```

9) run.sh

```bash
#!/usr/bin/env bash
set -euo pipefail

PORT="${PORT:-8000}"
HOST="${HOST:-0.0.0.0}"

printf '\nStarting local server at http://%s:%s\n\n' "$HOST" "$PORT"
python3 -m http.server "$PORT" --bind "$HOST"
```

10) assets/css/style.css

```css
:root {
  --bg: #07131f;
  --panel: rgba(11, 25, 38, 0.8);
  --panel-strong: rgba(18, 36, 51, 0.95);
  --panel-alt: rgba(14, 30, 45, 0.92);
  --card: rgba(17, 32, 46, 0.88);
  --card-hover: rgba(21, 39, 52, 0.98);
  --line: rgba(118, 156, 183, 0.2);
  --text: #edf6ff;
  --muted: #9bb8cc;
  --primary: #47d7b3;
  --secondary: #79b7ff;
  --accent: #e7b75a;
  --shadow: 0 24px 60px rgba(3, 10, 18, 0.25);
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  min-height: 100vh;
  background:
    radial-gradient(circle at top left, rgba(71, 215, 179, 0.18), transparent 20%),
    radial-gradient(circle at bottom right, rgba(121, 183, 255, 0.18), transparent 25%),
    var(--bg);
  color: var(--text);
  font-family: "Inter", "Noto Sans Bengali", sans-serif;
}
img { max-width: 100%; display: block; }
button { font: inherit; }

.app-shell {
  width: min(1200px, calc(100% - 32px));
  margin: 0 auto;
  padding: 24px 0 48px;
}

.topbar {
  position: sticky;
  top: 0;
  z-index: 20;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 18px 24px;
  margin-bottom: 24px;
  border: 1px solid var(--line);
  border-radius: 20px;
  background: rgba(8, 18, 28, 0.72);
  backdrop-filter: blur(16px);
  box-shadow: var(--shadow);
}

.brand-wrap { display: flex; align-items: center; gap: 14px; }
.brand-logo { width: 52px; height: 52px; border-radius: 14px; }
.eyebrow { margin: 0 0 4px; font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--primary); font-weight: 700; }
.brand-name { margin: 0; font-size: clamp(1.2rem, 2vw, 1.7rem); }
.main-nav { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; justify-content: center; }
.nav-link { color: var(--muted); text-decoration: none; padding: 10px 12px; border-radius: 10px; transition: 0.2s ease; font-weight: 500; }
.nav-link:hover, .nav-link:focus-visible { color: var(--text); background: rgba(255, 255, 255, 0.04); }
.header-actions { display: flex; align-items: center; gap: 10px; }
.lang-toggle {
  border: 1px solid var(--line);
  background: rgba(255, 255, 255, 0.04);
  color: var(--text);
  padding: 9px 12px;
  border-radius: 999px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: 0.2s ease;
}
.lang-toggle:hover { border-color: rgba(71, 215, 179, 0.5); }
.divider { color: var(--muted); }

.page-content { display: flex; flex-direction: column; gap: 24px; }

.hero-panel {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 24px;
  align-items: center;
  padding: 36px;
  border: 1px solid var(--line);
  border-radius: 28px;
  background: linear-gradient(135deg, rgba(17, 34, 49, 0.95), rgba(10, 24, 35, 0.88));
  box-shadow: var(--shadow);
}
.hero-kicker { margin: 0 0 16px; color: var(--primary); font-size: 0.78rem; letter-spacing: 0.14em; text-transform: uppercase; font-weight: 700; }
.hero-copy h2 { margin: 0; font-size: clamp(2.1rem, 4vw, 4rem); line-height: 1.02; letter-spacing: -0.05em; }
.hero-text { margin: 18px 0 0; color: var(--muted); font-size: 1.08rem; max-width: 640px; line-height: 1.7; }
.cta-row { display: flex; align-items: center; flex-wrap: wrap; gap: 12px; margin-top: 24px; }
.primary-btn, .secondary-btn {
  border: 1px solid transparent;
  border-radius: 12px;
  padding: 13px 18px;
  cursor: pointer;
  font-weight: 600;
  transition: 0.2s ease;
}
.primary-btn { background: linear-gradient(135deg, var(--primary), var(--secondary)); color: #022539; }
.secondary-btn { background: rgba(255, 255, 255, 0.03); border-color: var(--line); color: var(--text); }
.hero-visual { display: flex; justify-content: center; }
.hero-visual img { width: min(100%, 440px); filter: drop-shadow(0 30px 40px rgba(71, 215, 179, 0.18)); }

.metrics-grid { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 18px; }
.metric-card { padding: 24px 20px; border-radius: 18px; background: rgba(15, 29, 41, 0.8); border: 1px solid var(--line); box-shadow: var(--shadow); }
.metric-label { color: var(--muted); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 10px; }
.metric-value { font-size: clamp(1.7rem, 2vw, 2.3rem); font-weight: 800; margin: 0; }
.metric-context { margin-top: 8px; color: var(--muted); font-size: 0.92rem; }

.modules-section { padding: 8px 0 0; }
.section-header { margin-bottom: 18px; }
.section-header h3 { margin: 0; font-size: clamp(1.5rem, 2vw, 2.1rem); }
.module-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px; }
.module-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 18px;
  padding: 22px 20px;
  border-radius: 22px;
  border: 1px solid var(--line);
  background: linear-gradient(180deg, rgba(18, 33, 46, 0.95), rgba(11, 21, 31, 0.88));
  box-shadow: var(--shadow);
  transition: transform 0.2s ease, border-color 0.2s ease;
}
.module-card:hover { transform: translateY(-4px); border-color: rgba(71, 215, 179, 0.4); }
.module-top { display: flex; align-items: flex-start; justify-content: space-between; gap: 12px; }
.module-icon {
  width: 42px; height: 42px; display: inline-flex; align-items: center; justify-content: center;
  border-radius: 12px; background: rgba(71, 215, 179, 0.12); color: var(--primary); font-size: 1.3rem;
}
.module-status { padding: 7px 10px; border-radius: 999px; background: rgba(121, 183, 255, 0.12); color: var(--secondary); font-size: 0.72rem; font-weight: 700; white-space: nowrap; }
.module-card h4 { margin: 0 0 10px; font-size: 1.2rem; }
.module-card p { margin: 0; color: var(--muted); line-height: 1.7; }
.footer { padding: 30px 0 0; text-align: center; color: var(--muted); font-size: 0.92rem; }

@media (max-width: 980px) {
  .hero-panel { grid-template-columns: 1fr; }
  .metrics-grid, .module-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 640px) {
  .app-shell { width: min(100% - 18px, 1200px); }
  .topbar { flex-wrap: wrap; justify-content: center; }
  .main-nav { order: 3; width: 100%; }
  .metrics-grid, .module-grid { grid-template-columns: 1fr; }
  .hero-panel { padding: 22px 18px; }
}
```

11) assets/css/theme.css

```css
:root {
  --font-body: "Inter", "Noto Sans Bengali", sans-serif;
  --font-bn: "Noto Sans Bengali", "Inter", sans-serif;
}

html[lang="bn"] body,
html[lang="bn"] .brand-name,
html[lang="bn"] .hero-copy h2,
html[lang="bn"] h3,
html[lang="bn"] h4,
html[lang="bn"] p,
html[lang="bn"] button,
html[lang="bn"] .nav-link,
html[lang="bn"] .lang-toggle {
  font-family: var(--font-bn);
}

html[lang="bn"] .hero-copy h2 { letter-spacing: -0.03em; }
html[lang="bn"] .metric-label,
html[lang="bn"] .eyebrow,
html[lang="bn"] .hero-kicker {
  letter-spacing: 0.04em;
}
```

12) assets/js/lang.js

```javascript
(function () {
  const STORAGE_KEY = 'nwg-language';
  const defaultLang = 'en';

  function getSavedLanguage() {
    return localStorage.getItem(STORAGE_KEY) || defaultLang;
  }

  function setLanguage(lang) {
    document.documentElement.lang = lang;
    document.documentElement.setAttribute('data-lang', lang);
    localStorage.setItem(STORAGE_KEY, lang);
    document.dispatchEvent(new CustomEvent('languagechange', { detail: { lang } }));
  }

  function toggleLanguage() {
    const nextLang = document.documentElement.lang === 'bn' ? 'en' : 'bn';
    setLanguage(nextLang);
  }

  function initializeLanguage() {
    const preferred = getSavedLanguage();
    setLanguage(preferred === 'bn' ? 'bn' : 'en');
  }

  window.NWG = window.NWG || {};
  window.NWG.lang = {
    getSavedLanguage,
    setLanguage,
    toggleLanguage,
    initializeLanguage
  };

  document.addEventListener('DOMContentLoaded', initializeLanguage);
})();
```

13) assets/js/ui.js

```javascript
(function () {
  function renderNavigation(items, lang) {
    const nav = document.getElementById('main-nav');
    if (!nav) return;

    nav.innerHTML = items
      .map((item) => {
        const label = item.label?.[lang] || item.label?.en || item.key;
        return `<a class="nav-link" href="#${item.key}">${label}</a>`;
      })
      .join('');
  }

  function renderMetrics(items, lang) {
    const container = document.getElementById('metrics-grid');
    if (!container) return;

    container.innerHTML = items
      .map((item) => {
        const label = item.label?.[lang] || item.label?.en || item.key;
        const context = item.context?.[lang] || item.context?.en || '';
        return `
          <div class="metric-card">
            <div class="metric-label">${label}</div>
            <p class="metric-value">${item.value}</p>
            <div class="metric-context">${context}</div>
          </div>
        `;
      })
      .join('');
  }

  function renderModules(modules, lang) {
    const container = document.getElementById('module-grid');
    if (!container) return;

    const entries = Object.entries(modules).map(([key, value]) => {
      const title = value.title?.[lang] || value.title?.en || key;
      const description = value.description?.[lang] || value.description?.en || '';
      const status = value.status?.[lang] || value.status?.en || 'Ready';
      const iconMap = {
        identity: '◈',
        governance: '◎',
        geogrid: '⌖',
        reporting: '▣',
        analytics: '◌',
        command: '✦',
        ledger: '▤',
        zone: '◍',
        core: '⬢'
      };

      return `
        <article class="module-card" id="${key}">
          <div class="module-top">
            <div class="module-icon" aria-hidden="true">${iconMap[key] || '•'}</div>
            <span class="module-status">${status}</span>
          </div>
          <div>
            <h4>${title}</h4>
            <p>${description}</p>
          </div>
        </article>
      `;
    });

    container.innerHTML = entries.join('');
  }

  function applyTranslations(data, lang) {
    const i18nNodes = document.querySelectorAll('[data-i18n]');
    i18nNodes.forEach((node) => {
      const key = node.getAttribute('data-i18n');
      const path = key.split('.');
      let value = data;
      for (const part of path) {
        if (value && typeof value === 'object' && part in value) {
          value = value[part];
        } else {
          value = null;
          break;
        }
      }
      const text = value?.[lang] || value?.en || node.textContent;
      node.textContent = text;
    });

    renderNavigation(data.navigation, lang);
    renderMetrics(data.metrics, lang);
    renderModules(data.modules, lang);
  }

  window.NWG = window.NWG || {};
  window.NWG.ui = { applyTranslations, renderNavigation, renderMetrics, renderModules };
})();
```

14) assets/js/main.js

```javascript
(function () {
  async function fetchData() {
    const response = await fetch('./data.json', { cache: 'no-store' });
    if (!response.ok) {
      throw new Error('Unable to load data.json');
    }
    return response.json();
  }

  function bindLanguageToggle() {
    const toggleButton = document.getElementById('lang-toggle');
    if (!toggleButton) return;

    toggleButton.addEventListener('click', () => {
      window.NWG.lang.toggleLanguage();
    });
  }

  function handleLanguageChange() {
    document.addEventListener('languagechange', async (event) => {
      const lang = event.detail.lang;
      try {
        const data = await fetchData();
        window.NWG.ui.applyTranslations(data, lang);
        document.documentElement.lang = lang;
      } catch (error) {
        console.error('Translation update failed:', error);
      }
    });
  }

  async function init() {
    bindLanguageToggle();
    handleLanguageChange();

    try {
      const data = await fetchData();
      const initialLang = window.NWG.lang.getSavedLanguage();
      window.NWG.ui.applyTranslations(data, initialLang);
      document.documentElement.lang = initialLang;
    } catch (error) {
      console.error('Could not initialize application:', error);
    }
  }

  document.addEventListener('DOMContentLoaded', init);
})();
```

15) assets/images/logo.svg

```svg
<svg width="200" height="200" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" rx="30" fill="#0B1F2D"/>
  <circle cx="100" cy="100" r="70" stroke="#47D7B3" stroke-width="10"/>
  <circle cx="100" cy="100" r="42" fill="#79B7FF" fill-opacity="0.15" stroke="#79B7FF" stroke-width="6"/>
  <path d="M100 45L116 85H84L100 45ZM100 155L84 115H116L100 155ZM45 100L85 84V116L45 100ZM155 100L115 116V84L155 100Z" fill="#47D7B3"/>
</svg>
```

16) assets/images/splash.svg

```svg
<svg width="640" height="520" viewBox="0 0 640 520" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="640" height="520" rx="40" fill="#0C1E2D"/>
  <circle cx="176" cy="160" r="120" fill="#47D7B3" fill-opacity="0.12"/>
  <circle cx="470" cy="320" r="150" fill="#79B7FF" fill-opacity="0.10"/>
  <path d="M150 188H490C520 188 545 213 545 243V321C545 351 520 376 490 376H150C120 376 95 351 95 321V243C95 213 120 188 150 188Z" fill="#122B3C" stroke="#47D7B3" stroke-opacity="0.4"/>
  <path d="M150 128H490V173H150V128Z" fill="#1A3A52"/>
  <path d="M170 250H300V300H170V250ZM340 250H470V300H340V250ZM170 330H270V365H170V330ZM300 330H470V365H300V330Z" fill="#47D7B3" fill-opacity="0.9"/>
  <path d="M126 242L204 180L281 242L204 303L126 242Z" fill="#79B7FF" fill-opacity="0.14" stroke="#79B7FF" stroke-width="4"/>
  <path d="M359 177L417 142L475 177L417 214L359 177Z" fill="#47D7B3" fill-opacity="0.20" stroke="#47D7B3" stroke-width="4"/>
  <circle cx="209" cy="241" r="10" fill="#E7B75A"/>
  <circle cx="417" cy="177" r="10" fill="#E7B75A"/>
</svg>
```

17) includes/header.html

```html
<header class="topbar">
  <div class="brand-wrap">
    <img src="assets/images/logo.svg" alt="Logo" class="brand-logo" />
    <div>
      <p class="eyebrow">National Digital Infrastructure</p>
      <h1 class="brand-name">National Workforce Grid</h1>
    </div>
  </div>

  <nav class="main-nav" aria-label="Main navigation">
    <a href="#home" class="nav-link">Home</a>
    <a href="#identity" class="nav-link">Identity</a>
    <a href="#governance" class="nav-link">Governance</a>
    <a href="#geogrid" class="nav-link">Geo Grid</a>
    <a href="#reporting" class="nav-link">Reporting</a>
  </nav>

  <div class="header-actions">
    <button id="lang-toggle" class="lang-toggle" type="button">EN | BN</button>
  </div>
</header>
```

18) includes/menu.html

```html
<nav class="main-nav" aria-label="Main navigation">
  <a href="#home" class="nav-link">Home</a>
  <a href="#identity" class="nav-link">Identity</a>
  <a href="#governance" class="nav-link">Governance</a>
  <a href="#geogrid" class="nav-link">Geo Grid</a>
  <a href="#reporting" class="nav-link">Reporting</a>
</nav>
```

19) includes/footer.html

```html
<footer class="footer">
  <p>© 2026 National Workforce Grid. Built for secure and scalable national coordination.</p>
</footer>
```

20) modules/identity/README.md

```md
# Identity Module

This module handles secure identity verification and onboarding workflows.

## Purpose

- person verification
- credential validation
- decentralized identity support
- access control
```

21) modules/governance/README.md

```md
# Governance Module

This module manages policy enforcement and decision workflows.

## Purpose

- governance policies
- smart contract review
- accountability tracking
- reward and review rules
```

22) modules/geogrid/README.md

```md
# GeoGrid Module

This module manages geographic coverage, region mapping, and territorial coordination.

## Purpose

- zone visibility
- mapping integration
- regional planning
- operational placement
```

23) modules/reporting/README.md

```md
# Reporting Module

This module supports reports, compliance checks, and audit evidence.

## Purpose

- KPI reporting
- compliance monitoring
- audit logs
- operational summaries
```

24) modules/analytics/README.md

```md
# Analytics Module

This module supports dashboards and intelligence summarization.

## Purpose

- predictions
- trend analysis
- performance metrics
- insight generation
```

25) modules/command/README.md

```md
# Command Module

This module provides command and operational control surfaces.

## Purpose

- response planning
- live coordination
- escalation events
- operator orchestration
```

26) modules/ledger/README.md

```md
# Ledger Module

This module manages permanent transaction and activity records.

## Purpose

- registry tracking
- immutable records
- evidence retention
- accountability logs
```

27) modules/zone/README.md

```md
# Zone Module

This module manages service zone boundaries and local coordination.

## Purpose

- zone definitions
- assignment logic
- resource distribution
- traffic balancing
```

28) modules/core/README.md

```md
# Core Module

This module is responsible for foundational infrastructure and shared platform operations.

## Purpose

- system orchestration
- shared services
- security controls
- platform lifecycle
```

29) CONTRIBUTING.md

```md
# Contributing to National Workforce Grid

Thank you for your interest in contributing. This project welcomes contributions in several areas.

## How to Contribute

### 1. Adding Module Data

```bash
python3 add.py
```

### 2. Validating Changes

```bash
python3 validate.py
```

### 3. Creating Module Implementations

Create a new directory under `modules/` with:
- `README.md`
- `index.html`
- `data.json` if needed

### 4. Style Guidelines

- Always provide English and Bangla values.
- Keep Python scripts clean and documented.
- Use clear commit messages.

## Pull Request Process

1. Fork the repo
2. Create a branch
3. Make changes
4. Run validation
5. Open a pull request

## Reporting Issues

Open a GitHub issue and include:
- steps to reproduce
- expected behavior
- actual behavior
- environment details
```

30) DEPLOYMENT.md

```md
# Deployment Guide

## Local Development

```bash
git clone https://github.com/MJ-Ahmad/national-workforce-grid.git
cd national-workforce-grid
chmod +x run.sh
./run.sh
```

Open:

```text
http://localhost:8000
```

## Production Deployment

### Python HTTP server

```bash
PORT=8080 HOST=0.0.0.0 ./run.sh
```

### Gunicorn

```bash
pip install gunicorn
gunicorn --bind 0.0.0.0:8000 --workers 4
```

### Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
EXPOSE 8000
CMD ["python3", "-m", "http.server", "8000", "--bind", "0.0.0.0"]
```

Build:

```bash
docker build -t national-workforce-grid .
docker run -p 8000:8000 national-workforce-grid
```

## Health Checking

```bash
curl http://localhost:8000/
curl http://localhost:8000/data.json
python3 validate.py
```
```

31) ARCHITECTURE.md

```md
# National Workforce Grid - Architecture

## Overview

This project is a modular bilingual platform for workforce governance, identity management, and national operational coordination.

## Layers

- Frontend: HTML/CSS/JS
- Data layer: data.json
- Utilities: _lib.py
- Runtime: run.sh
- Modules: modules/*

## Key Features

- bilingual EN|BN support
- JSON-driven structure
- dynamic content rendering
- module-based extensibility
- validation automation

## Future Extension

This scaffold is ready to expand into:
- dashboards
- API-backed system
- user authentication
- persistent database
- microservice architecture
```

32) .github/workflows/validate.yml

```yaml
name: Validate Data Structure

on:
  push:
    paths:
      - 'data.json'
      - '**.py'
      - '.github/workflows/validate.yml'
  pull_request:
    paths:
      - 'data.json'
      - '**.py'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Validate data.json
        run: python3 validate.py
```

33) .github/ISSUE_TEMPLATE/bug_report.md

```md
---
name: Bug Report
about: Report a bug or issue
title: '[BUG] '
labels: bug
assignees: ''
---

## Description

A clear and concise description of the bug.

## Steps to Reproduce

1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

## Expected Behavior

What you expected to happen.

## Actual Behavior

What actually happened.

## Environment

- Browser:
- OS:
- Python version:
```

34) .github/ISSUE_TEMPLATE/feature_request.md

```md
---
name: Feature Request
about: Suggest an idea for this project
title: '[FEATURE] '
labels: enhancement
assignees: ''
---

## Description

Is your feature request related to a problem? Please describe.

## Proposed Solution

Describe the solution you'd like.

## Use Case

Explain the use case and benefit.
```

---

এই ব্লকগুলো একসাথে ব্যবহার করলে আপনার repo-তে **একটি সম্পূর্ণ প্রজেক্ট scaffold** তৈরি হবে।

### এখন আপনি কী করতে পারেন:
- এগুলো কপি করে একটি নতুন repo-তে রেখে দিতে পারবেন
- বা আমি পরের ধাপে এগিয়ে গিয়ে **একই জিনিসগুলো folders/files ধরে ধরে আরও polished version** বানিয়ে দিব

### অত্যন্ত গুরুত্বপূর্ণ:
GitHub write access সমস্যার কারণে আপনার repo-তে সরাসরি push করা সম্ভব হচ্ছে না।  
তাই বর্তমান অবস্থায়:

- আমি কোড/ফাইলগুলো ঠিকভাবে সাজিয়ে দিচ্ছি
- আপনি নিজের repo-তে save / create করে নিন
- তারপর আমি পরের ধাপে **রান/বাগ-ফিক্স / UI polish / production enhancement** করতে পারব

যদি চান, আমি এখনই **পরবর্তী ধাপ** শুরু করে দিচ্ছি:
- `index.html` এবং JS কে আরো production-grade করে
- dynamic module pages
- admin panel
- login page
- form system
- Bangla UX refinement
- API-ready backend structure

আমি চাইলে **একটি সম্পূর্ণ professional dashboard** সংস্করণও বানিয়ে দিতে পারি।
