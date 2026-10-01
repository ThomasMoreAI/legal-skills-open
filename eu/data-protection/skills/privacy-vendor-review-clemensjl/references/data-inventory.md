# Question 1 — what does this integration actually transmit

Vendor documentation describes the intended data flow. The review needs the real one. Every finding in this file is obtained by observation; the vendor's page is only used to explain what was observed.

Status as at 2026-08-05.

## Why observation comes first

Art 30(1)(c) GDPR requires the categories of personal data in the record; Art 13(1)(e) requires the recipients in the notice; Art 5(3) ePrivacy attaches to what is actually written to the device. All three are statements about behaviour. A default snippet routinely does more than the quick-start page says: it loads a second script from a different host, it enables automatic event capture, it captures full URLs including query strings, or it attaches an existing first-party cookie.

An identifier that singles out a user is personal data even without a name (Recital 26 GDPR, and Austrian DSB 2021-0.586.257, published 12.01.2022, on the Google Analytics `cid`). "We only send a random ID" is not a defence.

## Browser-side capture

Run in a **fresh profile with no stored consent**. Do not click the banner: the pre-consent picture is the one that decides the Art 5(3) question.

```js
// third-party-audit.mjs
// npm i playwright && npx playwright install chromium
// node third-party-audit.mjs https://[[YOUR-SITE]]
import { chromium } from 'playwright';

const TARGET = process.argv[2] ?? 'https://[[YOUR-SITE]]';
const FIRST_PARTY = new URL(TARGET).hostname.replace(/^www\./, '');

const browser = await chromium.launch();
const context = await browser.newContext();   // fresh profile, no prior consent
const page = await context.newPage();

const hits = new Map();
page.on('request', (req) => {
  let host;
  try { host = new URL(req.url()).hostname; } catch { return; }  // data:, blob:
  if (!host || host.endsWith(FIRST_PARTY)) return;
  const key = host;
  if (!hits.has(key)) hits.set(key, []);
  hits.get(key).push({
    method: req.method(),
    type: req.resourceType(),
    url: req.url().slice(0, 400),
    body: req.postData()?.slice(0, 800) ?? null,
  });
});

await page.goto(TARGET, { waitUntil: 'networkidle' });

const storage = await page.evaluate(() => ({
  localStorage: Object.keys(localStorage),
  sessionStorage: Object.keys(sessionStorage),
  indexedDB: typeof indexedDB !== 'undefined' ? 'present' : 'absent',
}));
const cookies = await context.cookies();

console.log(JSON.stringify({
  preConsentThirdPartyHosts: [...hits.keys()].sort(),
  requests: Object.fromEntries(hits),
  cookies: cookies.map(c => ({ name: c.name, domain: c.domain, expires: c.expires })),
  storage,
}, null, 2));

await browser.close();
```

Repeat the run **after** accepting, and after refusing. Three captures, three lists. The delta between "refused" and "no interaction" exposes banners that load tags on dismissal.

Manual equivalent: DevTools → Network, filter by domain, "Preserve log"; DevTools → Application → Cookies / Local Storage / IndexedDB / Service Workers. Export a HAR for the file.

## Reading the payloads

| Vendor pattern | What to look for |
|---|---|
| `…/g/collect?v=2&tid=G-…&cid=…&dl=…&dr=…` | GA4 measurement protocol. `cid` = client identifier, `dl` = full page URL including query string, `dr` = referrer. `dl` leaks whatever your URLs contain. |
| `facebook.com/tr/?id=…&ev=PageView&…` plus `cd[…]` params | Meta pixel. `cd[]` carries custom data; automatic advanced matching hashes form-field values including e-mail. |
| POST to an ingest host with a JSON envelope | Error/telemetry SDKs. Inspect for request headers, cookies, breadcrumbs and user context. |
| `…/e/?ip=1&…` or a base64 `data=` query param | Product analytics. Decode it; autocapture SDKs send DOM text content. |
| Any request whose path contains the current URL | Full-URL leakage — the highest-yield finding on account, checkout and health-adjacent routes |

Always check whether the full URL, the referrer, the page title and form values travel with the event. A page path is metadata until the path is `/patients/appointments/oncology`, at which point it is Art 9 data.

## Server-side and SDK-side capture

Browser capture misses backend integrations. For those:

1. Read the SDK's serialisation options rather than its README. Look specifically for a flag that attaches request headers, cookies, IP address or user identity to every event — the flags are usually named around "PII", "user context", "request data" or "attach stacktrace locals". Record the value **as configured in your repo**, not the library default.
2. Grep the repository for what is passed into the vendor call: `grep -rn "setUser\|identify(\|captureException\|track(" src/`.
3. Check log scrubbing/denylist configuration and whether it runs before or after transmission. Client-side scrubbing that runs in the vendor's cloud is not scrubbing for transfer purposes — the data has already left.
4. For webhooks in the other direction, record what the vendor sends *you*: webhook payloads frequently contain more than the API response does.

## Recording the result

Produce this table per integration. It feeds `artefacts.md` directly.

| Field | Value |
|---|---|
| Data categories transmitted | `[[list]]` |
| Identifiers | `[[cookie ID / user ID / device ID / IP / hashed e-mail]]` |
| Free-text exposure | `[[yes/no + which fields]]` |
| Art 9 risk | `[[none / possible via URL paths / possible via free text]]` |
| Full URL and referrer transmitted | `[[yes/no]]` |
| Fires before consent | `[[yes/no]]` (from the fresh-profile run) |
| Device storage written | `[[cookie names / localStorage keys / IndexedDB stores / none]]` |
| Third-party hosts contacted | `[[hosts]]` |
| Direction | `[[browser→vendor / server→vendor / vendor→server webhook]]` |
| Capture date and method | `[[date]]`, `[[Playwright / DevTools HAR / code review]]` |

## Checkpoints

- [ ] Capture run in a fresh profile with no stored consent
- [ ] Three captures taken: no interaction, refused, accepted
- [ ] Every third-party host listed, including ones loaded by other third parties (tag managers chain)
- [ ] Cookies, localStorage, sessionStorage, IndexedDB and service workers all inspected, not only cookies
- [ ] Payloads decoded, not just hosts counted
- [ ] Full-URL and referrer transmission explicitly checked against account/checkout/health-adjacent routes
- [ ] Server-side SDK options read from the repository configuration, not from library defaults
- [ ] Webhook payloads inspected for the reverse direction
- [ ] Result table completed with a capture date
- [ ] Any gap recorded as `[[MISSING: …]]`, never filled from vendor documentation
