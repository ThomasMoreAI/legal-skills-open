# Auditing an existing site

Authoritative basis: Playwright API (`page.on('request')`, `browserContext.cookies()`, `page.addInitScript`, `storageState`) — verified against the Playwright documentation on 2026-08-05. The legal test being applied is Article 5(3) ePD as construed in EDPB Guidelines 2/2023 v2.0.

The pass condition is a **network-level assertion**, not a screenshot. A banner that looks right proves nothing about what already loaded behind it.

## Manual method — five minutes, catches most failures

1. New browser profile or a private window with **all extensions disabled**. Ad blockers and privacy extensions make a broken site look clean.
2. DevTools open, Network tab, "Preserve log" on, cache disabled, throttling off.
3. Load the page. **Touch nothing.** No scroll, no click, no keypress.
4. Sort by Domain. Every domain other than your own and your CDN is a finding. Note the initiator column — it tells you whether the request came from markup, a script or a CSS file.
5. Application tab → Storage. Record every cookie, `localStorage` key, `sessionStorage` key and IndexedDB database. Anything beyond your own session and consent keys is a finding.
6. Now click reject. Reload. Repeat 4 and 5 — a surprising number of banners gate only the first page view.
7. Now click accept. Repeat. This time the list should match the vendor list in the cookie policy exactly. Discrepancies in either direction are findings.

## Automated audit

Runnable as-is. Node 18+, `npm i -D playwright`, then `node consent-audit.mjs https://example.com`.

```js
// consent-audit.mjs
import { chromium } from 'playwright';

const TARGET = process.argv[2];
if (!TARGET) { console.error('usage: node consent-audit.mjs <url>'); process.exit(2); }

// Hosts allowed before a consent decision. Own origin and own CDN only.
const ALLOWED = [
  new URL(TARGET).host,
  // '[[cdn.example.com]]',
];

const ACCEPT_SELECTORS = [
  '[data-testid="consent-accept"]',
  'button:has-text("Accept all")',
  'button:has-text("Alle akzeptieren")',
];

const isAllowed = host => ALLOWED.some(a => host === a || host.endsWith('.' + a));

// data:, blob: and about: are not network requests to anyone.
const externalHost = url => {
  try { const u = new URL(url); return /^https?:$/.test(u.protocol) ? u.host : null; }
  catch { return null; }
};

// Instrumentation injected before any page script runs.
const PROBE = () => {
  window.__writes = [];
  const rec = (kind, key) => window.__writes.push({ kind, key, stack: new Error().stack });
  const origSet = Storage.prototype.setItem;
  Storage.prototype.setItem = function (k, v) { rec('storage.setItem', k); return origSet.call(this, k, v); };
  const openDb = indexedDB.open.bind(indexedDB);
  indexedDB.open = (name, ...rest) => { rec('indexedDB.open', name); return openDb(name, ...rest); };
  const cookieDesc = Object.getOwnPropertyDescriptor(Document.prototype, 'cookie');
  Object.defineProperty(document, 'cookie', {
    get: () => cookieDesc.get.call(document),
    set: v => { rec('document.cookie', String(v).split('=')[0]); return cookieDesc.set.call(document, v); },
  });
};

async function snapshot(context, page, label) {
  const cookies = await context.cookies();
  const storage = await page.evaluate(() => ({
    local: Object.keys(localStorage),
    session: Object.keys(sessionStorage),
    writes: window.__writes ?? [],
  }));
  let idb = [];
  try { idb = (await page.evaluate(() => indexedDB.databases?.() ?? [])).map(d => d.name); } catch {}
  return { label, cookies, ...storage, idb };
}

const run = async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext({ locale: 'de-AT', timezoneId: 'Europe/Vienna' });
  await context.addInitScript(PROBE);

  const requests = [];
  context.on('request', r => {
    const host = externalHost(r.url());
    if (host) requests.push({ url: r.url(), host, type: r.resourceType() });
  });

  const page = await context.newPage();
  await page.goto(TARGET, { waitUntil: 'networkidle', timeout: 60_000 });
  await page.waitForTimeout(5_000);          // catch delayed and idle-callback loaders

  const before = await snapshot(context, page, 'before decision');
  const violations = requests.filter(r => !isAllowed(r.host));

  // Optional second phase: accept, then compare against the declared vendor list.
  let after = null, afterHosts = [];
  const n = requests.length;
  for (const sel of ACCEPT_SELECTORS) {
    const el = page.locator(sel).first();
    if (await el.count() && await el.isVisible().catch(() => false)) {
      await el.click();
      await page.waitForTimeout(5_000);
      after = await snapshot(context, page, 'after accept');
      afterHosts = [...new Set(requests.slice(n).map(r => r.host))].filter(h => !isAllowed(h));
      break;
    }
  }

  const report = {
    target: TARGET,
    checkedAt: new Date().toISOString(),
    beforeDecision: {
      thirdPartyHosts: [...new Set(violations.map(v => v.host))].sort(),
      thirdPartyRequests: violations.length,
      cookies: before.cookies.map(c => ({ name: c.name, domain: c.domain, expires: c.expires })),
      localStorage: before.local,
      sessionStorage: before.session,
      indexedDB: before.idb,
      storageWrites: before.writes.map(w => ({ kind: w.kind, key: w.key })),
    },
    afterAccept: after && {
      newThirdPartyHosts: afterHosts.sort(),
      cookies: after.cookies.map(c => ({ name: c.name, domain: c.domain, expires: c.expires })),
      localStorage: after.local,
      indexedDB: after.idb,
    },
  };

  console.log(JSON.stringify(report, null, 2));
  await browser.close();

  const failed = report.beforeDecision.thirdPartyHosts.length > 0
    || report.beforeDecision.storageWrites.some(w => !/consent|csrf|session/i.test(w.key));
  if (failed) { console.error('\nFAIL: activity before a consent decision'); process.exit(1); }
  console.error('\nPASS: no third-party request and no non-essential storage write before a decision');
};

run().catch(e => { console.error(e); process.exit(2); });
```

Notes on why it is built this way:

- **`context.on('request')`, not `page.on('request')`** — it catches requests from iframes and workers as well.
- **`addInitScript` runs before page scripts**, so the storage probe sees the first write rather than the end state. An end-state snapshot cannot distinguish "written before consent" from "written after".
- **`networkidle` plus a fixed wait** — many tags load on `requestIdleCallback` or a timer, deliberately after the load event.
- **Locale and timezone are set** because some CMPs skip the banner for non-EEA-looking clients, and because banners render different layouts per language.
- **The exit code is the contract.** Wire it into CI so a new tag cannot ship without also passing the gate.

## Variations worth running

| Variation | Why |
|---|---|
| `--device="iPhone 15"` equivalent context | Mobile banners frequently differ; see the "Inconsistent interface" pattern |
| Second page of the site, direct entry | Gates are often applied only to the home page |
| After clicking reject, then reloading | Catches banners that gate only the first view |
| With `storageState` from a consenting session | Confirms that accepted state actually loads the declared vendors |
| Against a preview/CDN URL | Catches cached HTML containing unblocked tags |
| With `Sec-GPC: 1` set via `extraHTTPHeaders` | Confirms the GPC path in `gpc-us.md` |

## Reading the output

| Finding | Severity | Meaning |
|---|---|---|
| Any third-party host before a decision | critical | Article 5(3) ePD breach at load time |
| Storage write before a decision, not consent/session/CSRF | critical | Storage on terminal equipment without consent |
| Third-party host appears only after accept, but is not in the cookie policy | high | Notice and reality diverge |
| Host in the cookie policy never appears | medium | Stale policy, or a tag that silently broke |
| Cookie lifetime far beyond what the policy states | medium | Configuration drift |
| Banner absent on a subpage | high | Gate applied per page rather than per site |

Report findings in this shape, worst first:

| Severity | Host / key | Trigger | What the rule says | Fix |
|---|---|---|---|---|
| critical / high / medium | `www.googletagmanager.com` | initiator, file:line | Art 5(3) ePD; EDPB GL 2/2023 v2.0 §50 | concrete change |

## Checkpoints

- [ ] Audit run from a clean automated profile with no extensions
- [ ] Zero third-party hosts contacted before a decision
- [ ] Zero non-essential storage writes before a decision
- [ ] Reject path re-tested after reload
- [ ] Accept path compared against the declared vendor list, both directions
- [ ] Home page and at least one deep entry point tested
- [ ] Mobile viewport tested
- [ ] GPC header variant tested where US traffic is in scope
- [ ] Audit wired into CI with a failing exit code
- [ ] Findings reported with severity, initiator and rule, not as general advice
