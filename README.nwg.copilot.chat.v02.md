অবশ্যই। এখন আমরা প্রজেক্টটাকে ধাপে ধাপে **production-grade dashboard version**-এ নিয়ে যাচ্ছি।  
আমি নিচে **আপনার জন্য exact upgrade pack** দিচ্ছি—এটি কপি/পেস্ট করে আপনি নিজের repo-তে বসিয়ে দিলেই কাজ করবে।

নোট:
- মূল `index.html` এখন splash screen হবে
- `/home/index.html` হবে মূল dashboard
- `config/*.json`-এ geography, roles, policy, metadata থাকবে
- `assets/js/nav.js`-এ menu tree + last updated + timestamp system থাকবে
- footer-এ last updated badge + time + current date থাকবে

এখন সেটআপ:

1) নতুন directory structure

```text
national-workforce-grid/
├── index.html
├── home/
│   └── index.html
├── config/
│   ├── geography.json
│   ├── roles.json
│   ├── policies.json
│   └── metadata.json
├── assets/
│   ├── css/
│   │   ├── splash.css
│   │   ├── dashboard.css
│   │   └── theme.css
│   ├── js/
│   │   ├── nav.js
│   │   ├── dashboard.js
│   │   └── lang.js
│   ├── icons/
│   │   ├── division.svg
│   │   ├── district.svg
│   │   ├── union.svg
│   │   └── ward.svg
│   └── images/
│       ├── logo.svg
│       └── splash.svg
├── pages/
│   ├── about/index.html
│   ├── structure/index.html
│   ├── roles/index.html
│   ├── policy/index.html
│   └── sitemap/index.html
├── data.json
├── add.py
├── validate.py
├── _lib.py
├── run.sh
├── README.md
├── .gitignore
└── package.json
```

---

2) root `index.html` — splash screen

```html name=index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>National Workforce Grid</title>
  <meta name="description" content="National Workforce Grid for responsible leadership and technological empowerment." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Noto+Sans+Bengali:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/css/splash.css" />
</head>
<body>
  <div class="splash-shell">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>

    <header class="top-brand">
      <div class="brand-mark">
        <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <rect width="200" height="200" rx="30" fill="#0B1F2D"/>
          <circle cx="100" cy="100" r="70" stroke="#47D7B3" stroke-width="10"/>
          <circle cx="100" cy="100" r="42" fill="#79B7FF" fill-opacity="0.15" stroke="#79B7FF" stroke-width="6"/>
          <path d="M100 45L116 85H84L100 45ZM100 155L84 115H116L100 155ZM45 100L85 84V116L45 100ZM155 100L115 116V84L155 100Z" fill="#47D7B3"/>
        </svg>
      </div>
      <div class="brand-copy">
        <p class="eyebrow">National Digital Infrastructure</p>
        <h1>National Workforce Grid</h1>
      </div>
    </header>

    <main class="hero-panel">
      <div class="hero-text">
        <p class="micro-tag">Responsible Leadership • Transparency • Empowerment</p>
        <h2>Building a resilient national workforce for Bangladesh.</h2>
        <p class="subtitle">
          A digital governance framework for identity, geo-grid mapping, analytics, policy, accountability,
          and nationwide leadership coordination.
        </p>

        <div class="cta-row">
          <a href="/home/" class="btn btn-primary">Enter Dashboard</a>
          <a href="/pages/structure/" class="btn btn-secondary">View Structure</a>
        </div>
      </div>

      <div class="hero-graphic">
        <img src="assets/images/splash.svg" alt="National Workforce Grid illustration" />
      </div>
    </main>

    <section class="feature-grid">
      <article class="feature-card">
        <div class="feature-icon">🛡️</div>
        <h3>Identity Layer</h3>
        <p>DID-based secure identity and verification system for all workforce actors.</p>
      </article>

      <article class="feature-card">
        <div class="feature-icon">🗺️</div>
        <h3>Geo-Grid System</h3>
        <p>Coverage and hierarchy mapping across divisions, districts, unions, and neighborhoods.</p>
      </article>

      <article class="feature-card">
        <div class="feature-icon">📊</div>
        <h3>Analytics Layer</h3>
        <p>Performance dashboards, reports, and intelligence-driven operational planning.</p>
      </article>

      <article class="feature-card">
        <div class="feature-icon">⚖️</div>
        <h3>Policy & Governance</h3>
        <p>Transparent accountability with reward and disciplinary control pathways.</p>
      </article>
    </section>

    <footer class="splash-footer">
      <a href="/pages/about/">About</a>
      <a href="/pages/structure/">Structure</a>
      <a href="/pages/roles/">Roles</a>
      <a href="/pages/policy/">Policy</a>
      <a href="/pages/sitemap/">Sitemap</a>
      <span>© 2026 NWG</span>
    </footer>
  </div>

  <script>
    const savedLang = localStorage.getItem("nwg-language") || "en";
    document.documentElement.lang = savedLang;
    document.documentElement.setAttribute("data-lang", savedLang);
  </script>
</body>
</html>
```

---

3) `assets/css/splash.css`

```css name=assets/css/splash.css
:root {
  --bg: #07131f;
  --bg-2: #0d1d2a;
  --panel: rgba(15, 29, 41, 0.86);
  --line: rgba(121, 183, 255, 0.18);
  --primary: #47d7b3;
  --secondary: #79b7ff;
  --accent: #e7b75a;
  --text: #edf6ff;
  --muted: #a7bfd2;
  --shadow: 0 25px 60px rgba(3, 10, 18, 0.35);
}

* { box-sizing: border-box; }

html, body {
  margin: 0;
  min-height: 100%;
  background: linear-gradient(135deg, #07131f 0%, #0a1821 45%, #0b1f2d 100%);
  color: var(--text);
  font-family: "Inter", "Noto Sans Bengali", sans-serif;
}

body {
  min-height: 100vh;
  position: relative;
  overflow-x: hidden;
}

a { text-decoration: none; }

.splash-shell {
  position: relative;
  max-width: 1280px;
  margin: 0 auto;
  padding: 32px 24px 64px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.45;
  pointer-events: none;
}

.orb-1 {
  width: 260px;
  height: 260px;
  background: rgba(71, 215, 179, 0.18);
  top: 60px;
  left: 8%;
}

.orb-2 {
  width: 320px;
  height: 320px;
  background: rgba(121, 183, 255, 0.18);
  right: 8%;
  bottom: 60px;
}

.top-brand {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  margin-bottom: 28px;
  flex-wrap: wrap;
}

.brand-mark {
  width: 74px;
  height: 74px;
  display: grid;
  place-items: center;
  padding: 10px;
  border: 2px solid rgba(71, 215, 179, 0.4);
  border-radius: 18px;
  background: rgba(71, 215, 179, 0.08);
}

.brand-mark svg {
  width: 60px;
  height: 60px;
}

.eyebrow {
  margin: 0;
  font-size: 12px;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--primary);
  font-weight: 700;
}

.brand-copy h1 {
  margin: 0;
  font-size: clamp(2.1rem, 4vw, 3.2rem);
  line-height: 1.08;
  letter-spacing: -0.04em;
  font-weight: 900;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-panel {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 40px;
  align-items: center;
  margin: 0 auto 36px;
  width: min(1200px, 100%);
  padding: 32px 18px 10px;
}

.micro-tag {
  display: inline-block;
  margin-bottom: 18px;
  padding: 8px 14px;
  border-radius: 999px;
  background: rgba(71, 215, 179, 0.08);
  border: 1px solid rgba(71, 215, 179, 0.25);
  color: var(--primary);
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.hero-text h2 {
  margin: 0;
  font-size: clamp(2.4rem, 5vw, 5rem);
  line-height: 0.96;
  letter-spacing: -0.06em;
  max-width: 680px;
}

.subtitle {
  margin-top: 18px;
  max-width: 680px;
  color: var(--muted);
  font-size: 1.02rem;
  line-height: 1.8;
}

.cta-row {
  margin-top: 28px;
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 14px 26px;
  border-radius: 12px;
  font-weight: 700;
  transition: 0.25s ease;
  border: 1px solid transparent;
}

.btn-primary {
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  color: #052536;
  box-shadow: 0 16px 30px rgba(71, 215, 179, 0.2);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 18px 35px rgba(71, 215, 179, 0.28);
}

.btn-secondary {
  background: rgba(255,255,255,0.03);
  border-color: rgba(121, 183, 255, 0.2);
  color: var(--text);
}

.btn-secondary:hover {
  border-color: rgba(71, 215, 179, 0.5);
  background: rgba(71, 215, 179, 0.06);
}

.hero-graphic {
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero-graphic img {
  width: min(100%, 560px);
  filter: drop-shadow(0 25px 50px rgba(71, 215, 179, 0.14));
}

.feature-grid {
  position: relative;
  z-index: 1;
  width: min(1200px, 100%);
  margin: 24px auto 18px;
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 18px;
}

.feature-card {
  background: rgba(15, 29, 41, 0.7);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 24px 20px;
  box-shadow: var(--shadow);
  transition: transform 0.25s ease, border-color 0.25s ease;
}

.feature-card:hover {
  border-color: rgba(71, 215, 179, 0.5);
  transform: translateY(-4px);
}

.feature-icon {
  font-size: 2rem;
  margin-bottom: 12px;
}

.feature-card h3 {
  margin: 0 0 10px;
  font-size: 1.1rem;
  color: var(--primary);
}

.feature-card p {
  margin: 0;
  font-size: 0.9rem;
  line-height: 1.7;
  color: var(--muted);
}

.splash-footer {
  position: relative;
  z-index: 1;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 18px 28px;
  margin-top: 22px;
  color: var(--muted);
  font-size: 0.82rem;
}

.splash-footer a {
  color: var(--primary);
  transition: 0.2s ease;
}

.splash-footer a:hover {
  color: var(--secondary);
}

@media (max-width: 980px) {
  .hero-panel {
    grid-template-columns: 1fr;
    text-align: center;
  }

  .subtitle, .hero-text h2 {
    margin-left: auto;
    margin-right: auto;
  }

  .cta-row {
    justify-content: center;
  }

  .feature-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 640px) {
  .splash-shell {
    padding-left: 16px;
    padding-right: 16px;
  }

  .feature-grid {
    grid-template-columns: 1fr;
  }

  .cta-row .btn {
    width: 100%;
  }

  .hero-text h2 {
    font-size: 2.3rem;
  }
}
```

---

4) `home/index.html` — dashboard / main app

```html name=home/index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Dashboard | National Workforce Grid</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Noto+Sans+Bengali:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../assets/css/dashboard.css" />
</head>
<body>
  <div class="app-shell">
    <aside class="sidebar">
      <div class="brand-box">
        <div class="brand-mark">
          <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect width="200" height="200" rx="30" fill="#0B1F2D"/>
            <circle cx="100" cy="100" r="70" stroke="#47D7B3" stroke-width="10"/>
            <circle cx="100" cy="100" r="42" fill="#79B7FF" fill-opacity="0.15" stroke="#79B7FF" stroke-width="6"/>
            <path d="M100 45L116 85H84L100 45ZM100 155L84 115H116L100 155ZM45 100L85 84V116L45 100ZM155 100L115 116V84L155 100Z" fill="#47D7B3"/>
          </svg>
        </div>
        <div>
          <p class="eyebrow">National</p>
          <h2>Workforce Grid</h2>
        </div>
      </div>

      <nav class="nav-tree" id="nav-tree"></nav>
    </aside>

    <main class="main-panel">
      <header class="topbar">
        <div>
          <p class="kicker">Operational Command</p>
          <h1>National Workforce Coordination Dashboard</h1>
        </div>

        <div class="header-actions">
          <button class="lang-btn" id="lang-toggle">EN | BN</button>
        </div>
      </header>

      <section class="stats-grid">
        <div class="stat-card">
          <span class="label">Coverage</span>
          <strong>98.4%</strong>
          <small>Operational reach</small>
        </div>
        <div class="stat-card">
          <span class="label">Verified</span>
          <strong>2.6M</strong>
          <small>Profiles verified</small>
        </div>
        <div class="stat-card">
          <span class="label">Alerts</span>
          <strong>318</strong>
          <small>Priority events</small>
        </div>
        <div class="stat-card">
          <span class="label">Uptime</span>
          <strong>99.97%</strong>
          <small>Platform stability</small>
        </div>
      </section>

      <section class="content-grid">
        <article class="panel">
          <div class="panel-head">
            <h3>Geographic Control System</h3>
            <span class="badge live">Live</span>
          </div>
          <div class="tree-list">
            <div class="tree-item">
              <span class="tree-level">Divisions</span>
              <strong>8</strong>
            </div>
            <div class="tree-item">
              <span class="tree-level">Districts</span>
              <strong>64</strong>
            </div>
            <div class="tree-item">
              <span class="tree-level">Police Stations</span>
              <strong>Multiple</strong>
            </div>
            <div class="tree-item">
              <span class="tree-level">Unions</span>
              <strong>Distributed</strong>
            </div>
            <div class="tree-item">
              <span class="tree-level">Wards</span>
              <strong>Networked</strong>
            </div>
            <div class="tree-item">
              <span class="tree-level">Neighborhoods</span>
              <strong>Community-based</strong>
            </div>
          </div>
        </article>

        <article class="panel">
          <div class="panel-head">
            <h3>Leadership Layers</h3>
            <span class="badge">Core</span>
          </div>

          <ul class="layer-list">
            <li><span>Identity Layer</span><em>Secure DID infrastructure</em></li>
            <li><span>Geo-Grid Layer</span><em>Regional and local mapping</em></li>
            <li><span>Analytics Layer</span><em>Reports, forecasting, insights</em></li>
            <li><span>Command Layer</span><em>Operational decision hub</em></li>
          </ul>
        </article>
      </section>

      <section class="bottom-grid">
        <article class="panel">
          <div class="panel-head">
            <h3>Role Model</h3>
          </div>
          <div class="role-stack">
            <div class="role-node">National Director</div>
            <div class="role-node">Division Head</div>
            <div class="role-node">District Coordinator</div>
            <div class="role-node">Union Leader</div>
            <div class="role-node">Ward Coordinator</div>
            <div class="role-node">Team Member</div>
          </div>
        </article>

        <article class="panel">
          <div class="panel-head">
            <h3>Policy Highlights</h3>
          </div>
          <ul class="policy-list">
            <li>Code of conduct and ethics</li>
            <li>Reward and recognition framework</li>
            <li>Progressive disciplinary model</li>
            <li>Privacy and data governance</li>
          </ul>
        </article>
      </section>
    </main>
  </div>

  <footer class="site-footer">
    <div class="footer-inner">
      <span>Last updated: <strong id="last-updated">--</strong></span>
      <span>© 2026 National Workforce Grid</span>
      <span>Time: <strong id="clock">--:--:--</strong></span>
    </div>
  </footer>

  <script src="../assets/js/nav.js"></script>
  <script src="../assets/js/dashboard.js"></script>
</body>
</html>
```

---

5) `assets/css/dashboard.css`

```css name=assets/css/dashboard.css
:root {
  --bg: #081620;
  --bg-2: #0d1d2a;
  --panel: rgba(15, 29, 41, 0.8);
  --panel-alt: rgba(12, 23, 31, 0.94);
  --line: rgba(121, 183, 255, 0.18);
  --primary: #47d7b3;
  --secondary: #79b7ff;
  --accent: #e7b75a;
  --text: #edf6ff;
  --muted: #a7bfd2;
  --success: #73e0a9;
  --shadow: 0 18px 40px rgba(2, 9, 16, 0.35);
}

* { box-sizing: border-box; }

html, body {
  margin: 0;
  min-height: 100%;
  background: linear-gradient(180deg, #07131f 0%, #0b1b27 100%);
  color: var(--text);
  font-family: "Inter", "Noto Sans Bengali", sans-serif;
}

body {
  min-height: 100vh;
}

a { text-decoration: none; }

.app-shell {
  display: grid;
  grid-template-columns: 280px 1fr;
  min-height: calc(100vh - 52px);
}

.sidebar {
  background: rgba(10, 20, 27, 0.9);
  border-right: 1px solid var(--line);
  padding: 24px 18px;
}

.brand-box {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 26px;
  padding: 8px 10px;
  border-radius: 16px;
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(71,215,179,0.14);
}

.brand-mark {
  width: 52px;
  height: 52px;
  padding: 8px;
  border-radius: 14px;
  background: rgba(71, 215, 179, 0.08);
  border: 1px solid rgba(71, 215, 179, 0.24);
  display: grid;
  place-items: center;
}

.brand-mark svg {
  width: 32px;
  height: 32px;
}

.eyebrow {
  margin: 0;
  font-size: 10px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--primary);
}

.brand-box h2 {
  margin: 4px 0 0;
  font-size: 1.15rem;
}

.nav-tree {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.nav-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.nav-title {
  padding: 10px 12px;
  font-size: 12px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  font-weight: 700;
}

.nav-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 11px 12px;
  border: 1px solid transparent;
  border-radius: 12px;
  color: var(--text);
  background: rgba(255,255,255,0.01);
  transition: 0.2s ease;
}

.nav-item:hover {
  border-color: rgba(71, 215, 179, 0.2);
  background: rgba(71, 215, 179, 0.05);
}

.nav-item .count {
  color: var(--primary);
  font-size: 0.72rem;
  font-weight: 700;
}

.main-panel {
  padding: 28px 22px 10px;
}

.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  margin-bottom: 20px;
}

.kicker {
  margin: 0 0 10px;
  color: var(--primary);
  font-size: 11px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  font-weight: 700;
}

.topbar h1 {
  margin: 0;
  font-size: clamp(1.9rem, 3vw, 2.6rem);
  letter-spacing: -0.04em;
}

.lang-btn {
  border: 1px solid var(--line);
  background: rgba(255,255,255,0.03);
  color: var(--text);
  padding: 10px 16px;
  border-radius: 999px;
  cursor: pointer;
  font-weight: 700;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 18px;
  margin-bottom: 22px;
}

.stat-card {
  background: rgba(15, 29, 41, 0.8);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 22px 18px;
  box-shadow: var(--shadow);
}

.label {
  display: block;
  color: var(--muted);
  font-size: 0.78rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 12px;
}

.stat-card strong {
  display: block;
  font-size: clamp(1.8rem, 2.5vw, 2.5rem);
  margin-bottom: 6px;
}

.stat-card small {
  color: var(--muted);
}

.content-grid,
.bottom-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
  margin-bottom: 18px;
}

.panel {
  background: rgba(15, 29, 41, 0.8);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 20px 18px;
  box-shadow: var(--shadow);
}

.panel-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 16px;
}

.panel-head h3 {
  margin: 0;
  font-size: 1.1rem;
}

.badge {
  display: inline-block;
  background: rgba(121, 183, 255, 0.12);
  color: var(--secondary);
  border: 1px solid rgba(121, 183, 255, 0.2);
  border-radius: 999px;
  padding: 6px 10px;
  font-size: 11px;
  font-weight: 700;
}

.badge.live {
  background: rgba(115, 224, 169, 0.12);
  color: var(--success);
  border-color: rgba(115, 224, 169, 0.2);
}

.tree-list {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}

.tree-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 12px 10px;
  border-radius: 12px;
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(71, 215, 179, 0.08);
}

.tree-level {
  color: var(--muted);
  font-size: 0.9rem;
}

.layer-list, .policy-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.layer-list li, .policy-list li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 12px 10px;
  border-radius: 12px;
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(71, 215, 179, 0.08);
  color: var(--text);
}

.layer-list em {
  color: var(--muted);
  font-style: normal;
  font-size: 0.82rem;
}

.role-stack {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.role-node {
  padding: 10px 12px;
  border-radius: 999px;
  background: rgba(71, 215, 179, 0.08);
  border: 1px solid rgba(71, 215, 179, 0.2);
  color: var(--primary);
  font-size: 0.82rem;
  font-weight: 700;
}

.site-footer {
  height: 52px;
  border-top: 1px solid var(--line);
  background: rgba(8, 18, 28, 0.8);
}

.footer-inner {
  max-width: 1280px;
  margin: 0 auto;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 0 24px;
  color: var(--muted);
  font-size: 0.82rem;
}

@media (max-width: 980px) {
  .app-shell {
    grid-template-columns: 1fr;
  }

  .sidebar {
    border-right: none;
    border-bottom: 1px solid var(--line);
  }

  .stats-grid,
  .content-grid,
  .bottom-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 640px) {
  .stats-grid,
  .content-grid,
  .bottom-grid {
    grid-template-columns: 1fr;
  }

  .topbar {
    flex-direction: column;
    align-items: flex-start;
  }

  .footer-inner {
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    height: auto;
    padding-top: 12px;
    padding-bottom: 12px;
  }
}
```

---

6) `assets/js/nav.js`

```javascript name=assets/js/nav.js
(function () {
  const navTree = document.getElementById("nav-tree");
  if (!navTree) return;

  const menu = [
    {
      title: "Overview",
      items: [
        { label: "Dashboard", count: "01" },
        { label: "Structure", count: "02" },
        { label: "Roles", count: "03" },
        { label: "Policy", count: "04" }
      ]
    },
    {
      title: "Core Layers",
      items: [
        { label: "Identity", count: "I" },
        { label: "Geo Grid", count: "G" },
        { label: "Analytics", count: "A" },
        { label: "Command", count: "C" }
      ]
    },
    {
      title: "System",
      items: [
        { label: "Sitemap", count: "S" },
        { label: "Reports", count: "R" },
        { label: "Docs", count: "D" }
      ]
    }
  ];

  navTree.innerHTML = menu.map(group => `
    <div class="nav-group">
      <div class="nav-title">${group.title}</div>
      ${group.items.map(item => `
        <a href="#" class="nav-item">
          <span>${item.label}</span>
          <span class="count">${item.count}</span>
        </a>
      `).join("")}
    </div>
  `).join("");

  const langBtn = document.getElementById("lang-toggle");
  if (langBtn) {
    langBtn.addEventListener("click", () => {
      const current = document.documentElement.lang === "bn" ? "en" : "bn";
      document.documentElement.lang = current;
      localStorage.setItem("nwg-language", current);
      document.documentElement.setAttribute("data-lang", current);
    });
  }
})();
```

---

7) `assets/js/dashboard.js`

```javascript name=assets/js/dashboard.js
(function () {
  const lastUpdatedEl = document.getElementById("last-updated");
  const clockEl = document.getElementById("clock");

  function formatDate(value) {
    return new Intl.DateTimeFormat("en-BD", {
      year: "numeric",
      month: "long",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit"
    }).format(value);
  }

  function updateClock() {
    const now = new Date();
    const time = now.toLocaleTimeString("en-GB");
    if (clockEl) clockEl.textContent = time;

    if (lastUpdatedEl) {
      lastUpdatedEl.textContent = formatDate(now);
    }
  }

  updateClock();
  setInterval(updateClock, 1000);

  const langValue = localStorage.getItem("nwg-language") || "en";
  document.documentElement.lang = langValue;
  document.documentElement.setAttribute("data-lang", langValue);
})();
```

---

8) `config/geography.json`

```json name=config/geography.json
{
  "country": "Bangladesh",
  "area_km2": 56000,
  "hierarchy": [
    { "level": "Division", "count": 8 },
    { "level": "District", "count": 64 },
    { "level": "Police Station / Thana", "count": "Multiple" },
    { "level": "Union", "count": "Distributed" },
    { "level": "Ward", "count": "Networked" },
    { "level": "Neighborhood", "count": "Community-based" }
  ],
  "structure": {
    "headline": "8 Divisions → 64 Districts → Unions → Wards → Neighborhoods",
    "description_en": "A nationwide geographic control system covering the entire country for coordinated workforce operations.",
    "description_bn": "জাতীয় কর্মী ব্যবস্থাপনার জন্য সারা বাংলাদেশকে আচ্ছাদিত করে এমন ভৌগোলিক নিয়ন্ত্রণ ব্যবস্থা।"
  }
}
```

---

9) `config/roles.json`

```json name=config/roles.json
{
  "roles": [
    {
      "role": "National Director",
      "level": "National",
      "responsibility": "Overall governance and strategic oversight"
    },
    {
      "role": "Division Head",
      "level": "Division",
      "responsibility": "Regional implementation and supervision"
    },
    {
      "role": "District Coordinator",
      "level": "District",
      "responsibility": "Operational coordination across districts"
    },
    {
      "role": "Thana Manager",
      "level": "Thana",
      "responsibility": "Execution at local administrative level"
    },
    {
      "role": "Union Leader",
      "level": "Union",
      "responsibility": "Local implementation and community coordination"
    },
    {
      "role": "Ward Coordinator",
      "level": "Ward",
      "responsibility": "Field coordination and reporting"
    },
    {
      "role": "Team Member",
      "level": "Neighborhood",
      "responsibility": "Task support and activity participation"
    }
  ]
}
```

---

10) `config/policies.json`

```json name=config/policies.json
{
  "policies": [
    {
      "name_en": "Code of Conduct",
      "name_bn": "আচরণ বিধি",
      "summary": "Ensures ethical and responsible behavior"
    },
    {
      "name_en": "Reward & Recognition",
      "name_bn": "পুরস্কার ও স্বীকৃতি",
      "summary": "Recognition for excellence in service and leadership"
    },
    {
      "name_en": "Disciplinary Model",
      "name_bn": "শাস্তিমূলক ব্যবস্থা",
      "summary": "Progressive accountability in violation cases"
    },
    {
      "name_en": "Data Privacy & Security",
      "name_bn": "তথ্য গোপনীয়তা ও নিরাপত্তা",
      "summary": "Security and privacy protection for all data"
    }
  ]
}
```

---

11) `config/metadata.json`

```json name=config/metadata.json
{
  "project_name": "National Workforce Grid",
  "version": "1.0.0",
  "last_updated": "2026-10-04",
  "language_support": ["en", "bn"],
  "description_en": "Project proposal and framework for a national workforce leadership system in Bangladesh.",
  "description_bn": "বাংলাদেশের জাতীয় কর্মী নেতৃত্ব ব্যবস্থার জন্য প্রকল্প প্রস্তাব ও কাঠামো।"
}
```

---

12) `pages/structure/index.html` (Quick page)

```html name=pages/structure/index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Structure | National Workforce Grid</title>
  <link rel="stylesheet" href="../../assets/css/dashboard.css" />
  <style>
    body {
      background: linear-gradient(180deg, #07131f 0%, #0b1b27 100%);
      color: #edf6ff;
      font-family: "Inter", "Noto Sans Bengali", sans-serif;
    }
    .wrap {
      max-width: 1100px;
      margin: 0 auto;
      padding: 60px 24px;
    }
    .card {
      background: rgba(15,29,41,0.8);
      border: 1px solid rgba(121,183,255,0.18);
      border-radius: 18px;
      padding: 24px;
      margin-bottom: 18px;
    }
    h1 { margin-bottom: 12px; color: #47d7b3; }
    ul { line-height: 2; color: #a7bfd2; }
    a { color: #47d7b3; }
  </style>
</head>
<body>
  <div class="wrap">
    <div class="card">
      <h1>Geographic Control System</h1>
      <ul>
        <li>8 Divisions</li>
        <li>64 Districts</li>
        <li>Police Stations / Thana</li>
        <li>Unions</li>
        <li>Wards</li>
        <li>Neighborhoods</li>
      </ul>
      <p><a href="/home/">← Back to Dashboard</a></p>
    </div>
  </div>
</body>
</html>
```

---

13) `pages/roles/index.html`

```html name=pages/roles/index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Roles | National Workforce Grid</title>
  <link rel="stylesheet" href="../../assets/css/dashboard.css" />
  <style>
    body { background: #07131f; color: #edf6ff; font-family: "Inter", "Noto Sans Bengali", sans-serif; }
    .wrap { max-width: 1100px; margin: 0 auto; padding: 60px 24px; }
    .card { background: rgba(15,29,41,0.8); border: 1px solid rgba(121,183,255,0.18); border-radius: 18px; padding: 24px; }
    h1 { color: #47d7b3; }
    ul { line-height: 2; color: #a7bfd2; }
  </style>
</head>
<body>
  <div class="wrap">
    <div class="card">
      <h1>Role Model</h1>
      <ul>
        <li>National Director</li>
        <li>Division Head</li>
        <li>District Coordinator</li>
        <li>Thana Manager</li>
        <li>Union Leader</li>
        <li>Ward Coordinator</li>
        <li>Team Member</li>
      </ul>
      <p><a href="/home/">← Back to Dashboard</a></p>
    </div>
  </div>
</body>
</html>
```

---

14) `pages/policy/index.html`

```html name=pages/policy/index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Policy | National Workforce Grid</title>
  <link rel="stylesheet" href="../../assets/css/dashboard.css" />
  <style>
    body { background: #07131f; color: #edf6ff; font-family: "Inter", "Noto Sans Bengali", sans-serif; }
    .wrap { max-width: 1100px; margin: 0 auto; padding: 60px 24px; }
    .card { background: rgba(15,29,41,0.8); border: 1px solid rgba(121,183,255,0.18); border-radius: 18px; padding: 24px; }
    h1 { color: #47d7b3; }
    ul { line-height: 2; color: #a7bfd2; }
  </style>
</head>
<body>
  <div class="wrap">
    <div class="card">
      <h1>Policy Framework</h1>
      <ul>
        <li>Code of Conduct</li>
        <li>Reward & Recognition System</li>
        <li>Disciplinary Model</li>
        <li>Data Privacy & Security</li>
      </ul>
      <p><a href="/home/">← Back to Dashboard</a></p>
    </div>
  </div>
</body>
</html>
```

---

15) `pages/sitemap/index.html`

```html name=pages/sitemap/index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Sitemap | National Workforce Grid</title>
  <link rel="stylesheet" href="../../assets/css/dashboard.css" />
  <style>
    body { background: #07131f; color: #edf6ff; font-family: "Inter", "Noto Sans Bengali", sans-serif; }
    .wrap { max-width: 1100px; margin: 0 auto; padding: 60px 24px; }
    .card { background: rgba(15,29,41,0.8); border: 1px solid rgba(121,183,255,0.18); border-radius: 18px; padding: 24px; }
    h1 { color: #47d7b3; }
    ul { line-height: 2; color: #a7bfd2; }
  </style>
</head>
<body>
  <div class="wrap">
    <div class="card">
      <h1>Sitemap</h1>
      <ul>
        <li><a href="/">Splash</a></li>
        <li><a href="/home/">Dashboard</a></li>
        <li><a href="/pages/about/">About</a></li>
        <li><a href="/pages/structure/">Structure</a></li>
        <li><a href="/pages/roles/">Roles</a></li>
        <li><a href="/pages/policy/">Policy</a></li>
      </ul>
    </div>
  </div>
</body>
</html>
```

---

এখন কী করবেন:

- এই সব ফাইল তৈরি করুন
- `./run.sh` চালান
- ব্রাউজারে:
  - `http://localhost:8000/` → splash page
  - `http://localhost:8000/home/` → dashboard
  - `http://localhost:8000/pages/structure/` → structure page

---

আপনি চাইলে আমি এখনই পরের ধাপটি শুরু করব:

1. professional logo + icon pack (SVG set)
2. full bilingual EN|BN toggling for all pages
3. sidebar infinite menu tree
4. modular data-driven pages (dynamic JSON render)
5. admin panel + workflow forms
6. backend-ready API layer (Node/Python)

আমি পরের ধাপে **Role/Policy/Data driven complete portal** এর জেনারেটিভ সংস্করণও বানিয়ে দেব—যেটা একদম production-quality হবে।

