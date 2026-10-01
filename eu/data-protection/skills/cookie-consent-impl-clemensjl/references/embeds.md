# Third-party embeds and click-to-load

Authoritative basis: Article 5(3) ePD; EDPB Guidelines 2/2023 v2.0 (adopted 7 October 2024) paras 36–38 and 50–51. An `<iframe src>` to a third party is a full document load on the user's device: DNS, TLS, HTML, JS, cache entries. It is in scope whether or not a cookie is written. Status as at 2026-08-05.

## The rule about "privacy-enhanced" modes

Vendors offer modes that reduce *personalisation*. None of them removes the *request*. That distinction is the whole point: Article 5(3) attaches to storage and access, not to profiling.

| Embed | Vendor's privacy mode | What it actually changes | Consent still required |
|---|---|---|---|
| YouTube | `youtube-nocookie.com` | Google: the view "will not be used to personalize the YouTube browsing experience"; non-personalised ads are served instead | Yes — the iframe, player JS and cached assets still load |
| Vimeo | `?dnt=1` | Vendor-documented reduction of session tracking `[[UNVERIFIED: exact scope of Vimeo's dnt parameter — check developer.vimeo.com before asserting]]` | Yes — the player still loads from `player.vimeo.com` |
| Google Maps | none documented | — | Yes |
| X / Twitter | none | — | Yes |
| Instagram | none | — | Yes |
| Spotify | none | — | Yes |
| Calendly | none | — | Yes |

State this to stakeholders once and move on: swapping to `youtube-nocookie.com` is a good default *after* consent, and irrelevant *before* it.

## Click-to-load pattern

One implementation covers every embed. The placeholder is first-party: local thumbnail, local text, no remote asset.

```html
<div class="embed-gate"
     data-embed-provider="youtube"
     data-embed-category="marketing"
     data-embed-src="https://www.youtube-nocookie.com/embed/[[VIDEO_ID]]?rel=0"
     data-embed-title="[[Video title]]">
  <img src="/thumbs/[[VIDEO_ID]].jpg" alt="" width="1280" height="720" loading="lazy">
  <div class="embed-gate__notice">
    <p>[[Notice text — wording belongs to the legal-* skills]]</p>
    <button type="button" data-embed-load>Load video</button>
    <label><input type="checkbox" data-embed-remember> Always load YouTube embeds</label>
  </div>
</div>
```

```js
import { getConsent, setConsent, onConsent } from './consent-store.js';

function activate(gate) {
  const iframe = document.createElement('iframe');
  iframe.src = gate.dataset.embedSrc;
  iframe.title = gate.dataset.embedTitle || '';
  iframe.loading = 'lazy';
  iframe.allowFullscreen = true;
  iframe.referrerPolicy = 'strict-origin-when-cross-origin';
  iframe.setAttribute('allow', 'accelerometer; encrypted-media; picture-in-picture');
  gate.replaceWith(iframe);
  iframe.focus();                     // keep keyboard position after replacement
}

document.addEventListener('click', e => {
  const btn = e.target.closest('[data-embed-load]');
  if (!btn) return;
  const gate = btn.closest('.embed-gate');
  const remember = gate.querySelector('[data-embed-remember]')?.checked;
  if (remember) {
    const c = getConsent() ?? { categories: {}, providers: {} };
    c.providers[gate.dataset.embedProvider] = true;
    setConsent(c);                    // records a per-provider consent, see consent-record.md
  }
  activate(gate);
});

// blanket consent already given for the category or the provider
onConsent(c => {
  document.querySelectorAll('.embed-gate').forEach(gate => {
    if (c.providers?.[gate.dataset.embedProvider] || c.categories?.[gate.dataset.embedCategory]) {
      activate(gate);
    }
  });
});
```

Requirements that are easy to miss:

- **The placeholder must not fetch the thumbnail from the provider.** `img.youtube.com/vi/…/hqdefault.jpg` is a request to Google. Download the thumbnail at build time and serve it yourself.
- **A single click must be enough.** Requiring click-to-consent then click-to-play adds a step that the EDPB classifies as "Longer than necessary" (Guidelines 03/2022 v2.0 §4.4.2) when the equivalent invasive path is shorter.
- **The remember checkbox is consent** and must be recorded like any other consent (`consent-record.md`), and revocable from the settings dialog.
- **Keyboard and screen-reader parity.** The button is a real `<button>`; focus moves into the iframe after replacement.
- **Do not preconnect to the provider** while the placeholder is showing.

## Fonts

Self-hosting is the correct answer, not a workaround. A request to `fonts.googleapis.com` or `fonts.gstatic.com` transmits the IP address to a third party and populates the HTTP cache on the device — access and storage under Article 5(3) ePD, plus a transfer question under Chapter V GDPR.

```
/* download the woff2 files once, ship them from your own origin */
@font-face {
  font-family: '[[Family]]';
  src: url('/fonts/[[family]]-400.woff2') format('woff2');
  font-weight: 400;
  font-display: swap;
  font-style: normal;
}
```

Checklist for the swap:

1. Fetch the CSS the provider serves for your exact `font-family`/`weight`/`subset` combination and read the `src` URLs out of it.
2. Download the `woff2` files and commit them.
3. Rewrite `@font-face` to local paths; delete the `<link>` to the provider **and** any `preconnect` to it.
4. Add `<link rel="preload" as="font" type="font/woff2" crossorigin>` for the one or two faces used above the fold — now safe, because the origin is yours.
5. Confirm the licence permits self-hosting. Google Fonts are open-licensed; Adobe Fonts (Typekit) generally are not — for Adobe Fonts, gate the loader behind consent or replace the family.

Bunny Fonts, Fontshare and similar "GDPR-friendly" proxies are still third-party requests. They may reduce the transfer problem; they do not remove the Article 5(3) problem.

## Other common embeds

- **Google Maps.** Prefer a static, self-hosted image plus a link that opens Maps in a new tab. That removes the embed entirely for most "where we are" use cases. Where interaction is genuinely needed, gate the iframe; consider a self-hostable alternative (OpenStreetMap tiles from your own tile cache) if map interaction is core.
- **reCAPTCHA / hCaptcha / Turnstile.** Anti-fraud on a form the user requested is arguable as strictly necessary, but that assessment belongs to the `legal-*` skills. Implementation-wise: load the widget on form focus, not on page load. Never load it on pages without a form.
- **Chat widgets.** Almost always marketing or functional, never strictly necessary. Load on click of a first-party launcher button.
- **Calendly / scheduling.** Gate; the fallback is a link to the scheduling page.
- **Payment SDKs.** Load on entry to checkout, not on every page. On the checkout step, contract performance may cover them — again a legal call, but a global `<script src="https://js.stripe.com/…">` in the root layout is indefensible on the home page.
- **Social share buttons.** Replace with plain links to the share URL. No SDK, no request, no consent question.

## Checkpoints

- [ ] No third-party iframe is present in the DOM before a consent signal
- [ ] Placeholders use locally hosted thumbnails and text
- [ ] One click loads the embed; the remember option writes a recorded consent
- [ ] `youtube-nocookie.com` used for YouTube after consent
- [ ] All fonts served from own origin; provider `<link>` and `preconnect` removed
- [ ] Font licence checked before self-hosting
- [ ] Captcha and payment SDKs scoped to the pages and moments that need them
- [ ] Social buttons replaced with plain links
- [ ] Keyboard focus moves into the embed after activation
- [ ] `[[MISSING: …]]` raised for any embed with no first-party fallback
