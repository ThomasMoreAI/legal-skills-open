# The blocking layer

Authoritative basis: Article 5(3) Directive 2002/58/EC; EDPB Guidelines 2/2023 on the technical scope of Art. 5(3) ePrivacy Directive, Version 2.0, adopted 7 October 2024 (para 36: storage occurs when a party instructs software on the terminal equipment; para 50: distributing a tracking pixel or link is already storage through client-side caching; para 51: collecting the identifier back is "gaining of access"). Status as at 2026-08-05.

Consequence: the unit of control is **the request**, not the cookie. Everything below exists to stop requests.

## 1. Type swapping — for markup you control

Give a blocked script a non-executable `type` and carry the real one in a data attribute. Browsers do not execute unknown script types and do not fetch their `src`.

```html
<!-- blocked until consent -->
<script type="text/plain" data-consent-category="analytics"
        data-src="https://cdn.example-analytics.com/tracker.js"></script>

<!-- inline code is blocked the same way -->
<script type="text/plain" data-consent-category="marketing">
  window.fbq && fbq('track', 'PageView');
</script>
```

The unblocker rebuilds the element. Attributes must be copied; you cannot flip `type` in place on a script that has already been parsed.

```js
// consent-unblock.js — first-party, loaded normally, no dependencies
export function unblock(category) {
  const nodes = document.querySelectorAll(
    `script[type="text/plain"][data-consent-category="${category}"]`
  );
  for (const old of nodes) {
    const s = document.createElement('script');
    for (const { name, value } of old.attributes) {
      if (name === 'type' || name === 'data-src' || name === 'data-consent-category') continue;
      s.setAttribute(name, value);
    }
    if (old.dataset.src) s.src = old.dataset.src;
    else s.textContent = old.textContent;
    s.async = old.hasAttribute('async');
    old.parentNode.replaceChild(s, old);
  }
}
```

Order matters: replaced scripts execute in DOM order for `src` scripts only if you preserve `async`/`defer` semantics deliberately. If a vendor requires a strict sequence, chain on `load` instead of replacing in a loop.

## 2. Dynamic injection — the safer default

For anything you can call from JS, do not ship the tag in markup at all. Inject after the signal.

```js
const loaded = new Set();

export function loadScript(src, { attrs = {}, async = true } = {}) {
  if (loaded.has(src)) return Promise.resolve();
  loaded.add(src);
  return new Promise((resolve, reject) => {
    const s = document.createElement('script');
    s.src = src;
    s.async = async;
    for (const [k, v] of Object.entries(attrs)) s.setAttribute(k, v);
    s.onload = () => resolve();
    s.onerror = () => { loaded.delete(src); reject(new Error(`failed: ${src}`)); };
    document.head.appendChild(s);
  });
}
```

Wire it to a single consent store so every consumer reads one source of truth:

```js
const KEY = 'consent.v3';                 // bump with the banner version
const listeners = new Set();
let state = null;

export function getConsent() {
  if (state) return state;
  try { state = JSON.parse(localStorage.getItem(KEY)); } catch { state = null; }
  return state;
}

export function setConsent(next) {
  state = next;
  localStorage.setItem(KEY, JSON.stringify(next));
  for (const fn of listeners) fn(next);
}

export function onConsent(fn) { listeners.add(fn); const s = getConsent(); if (s) fn(s); }

// consumer
onConsent(c => {
  if (c.categories.analytics) loadScript('https://cdn.example-analytics.com/tracker.js');
});
```

The consent store itself is strictly necessary within the meaning of Article 5(3) ePD — it retains a preference expressed by the user (Cookie Banner Taskforce report, adopted 17 January 2023, para 30, citing WP29 Opinion 04/2012). Keep it first-party and do not gate it behind itself.

## 3. Content-Security-Policy — the backstop

CSP does not implement consent. It catches the tag someone adds in the tag manager on a Friday. Deploy a policy that omits every non-essential host, and widen it only when you also widen the gate.

```
Content-Security-Policy:
  default-src 'self';
  script-src 'self' 'nonce-[[NONCE]]';
  connect-src 'self';
  img-src 'self' data:;
  font-src 'self';
  frame-src 'none';
  base-uri 'self';
  object-src 'none';
  report-uri /csp-report
```

Two properties make this useful: violations are reported with the blocked URI, and `connect-src 'self'` also stops `fetch`, XHR, WebSocket and `navigator.sendBeacon` — the channels a bundled SDK uses without ever adding a script tag. Run it in `Content-Security-Policy-Report-Only` first, read the reports, then enforce.

CSP cannot be your only control: a consenting user needs the third-party hosts allowed, and a policy cannot vary per user without server-side rendering of the header. Where consent is server-visible, emit two policies; where it is not, keep CSP tight and rely on the JS gate, using CSP reports purely as a leak detector.

## 4. Where consent leaks

| Leak | Why it fires early | Fix |
|---|---|---|
| `<link rel="preconnect">`, `rel="dns-prefetch">` | Opens DNS/TCP/TLS to the third party during parse, before any script decision | Remove; inject the hint together with the script after consent |
| `<link rel="preload" as="script">` | Downloads the resource immediately | Remove |
| `<img src>` pixel, `<img srcset>` | A pixel is a request; Guidelines 2/2023 §3.1 puts it squarely in scope | Swap `src` to `data-src`, restore after consent |
| CSS `@font-face { src: url(https://…) }`, `background-image: url(https://…)` | Fetched by the CSSOM, no JS involved | Self-host the asset |
| `<iframe src>` | Loads a full third-party document | Click-to-load, see `embeds.md` |
| `document.write('<script src=…>')` in a legacy tag | Bypasses attribute-based blocking entirely and destroys the document if called after load | Replace the tag with its async loader; if the vendor has none, shim `document.write` before unblocking, or drop the vendor |
| Inline `onload=`/`onclick=` handlers on blocked elements | Attribute handlers run regardless of script `type` | Move to `addEventListener` inside the gated module |
| Bundled SDK imported statically (`import mixpanel from …`) | The bundler inlines it; there is no tag to block, and the SDK connects on import | Convert to `await import()` inside the consent callback |
| Service worker registered before consent | Persists and can re-fetch third-party resources | Register only after consent, or restrict its fetch handler to same-origin |
| `<video>`/`<audio>` with a remote `src` or `poster` | Same request rule as images | Self-host or gate |
| Web font loaders (`WebFontLoader`, `Typekit`) | Fetch from the vendor on init | Self-host, see `embeds.md` |

## 5. Guarding against re-introduction

Add a runtime guard in non-production builds that fails loudly when a blocked host is contacted. It catches regressions faster than CSP reports.

```js
if (import.meta.env.DEV) {
  const ALLOWED = [location.host];
  const check = url => {
    const h = new URL(url, location.href).host;
    if (!ALLOWED.includes(h) && !getConsent()) {
      throw new Error(`consent leak: request to ${h} before consent`);
    }
  };
  const of = window.fetch;
  window.fetch = (input, init) => { check(typeof input === 'string' ? input : input.url); return of(input, init); };
  new PerformanceObserver(list => list.getEntries().forEach(e => check(e.name)))
    .observe({ type: 'resource', buffered: true });
}
```

The authoritative check remains the automated one in `audit.md`. This guard is a development aid.

## Checkpoints

- [ ] Every non-essential `<script>` in markup carries `type="text/plain"` plus a category attribute
- [ ] Every non-essential tag reachable from JS is injected, not shipped in markup
- [ ] `preconnect`, `dns-prefetch` and `preload` hints for third parties removed
- [ ] Pixels, remote images, remote posters converted to `data-src`
- [ ] Remote `@font-face` and CSS `url()` references self-hosted
- [ ] Statically imported analytics SDKs converted to dynamic `import()`
- [ ] No `document.write` path remains in any blocked tag
- [ ] Inline event-handler attributes removed from blocked elements
- [ ] Service worker registration deferred or scoped to same-origin
- [ ] CSP deployed with `connect-src 'self'`, report endpoint live, reports reviewed
- [ ] Consent store is first-party and not itself gated
- [ ] `[[MISSING: …]]` raised for any vendor with no async loader
