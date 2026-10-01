# Global Privacy Control and the US layer

Authoritative basis: W3C Global Privacy Control specification (w3c.github.io/gpc); California Attorney General CCPA page (oag.ca.gov/privacy/ccpa); Colorado Department of Law Universal Opt-Out Mechanism list (coag.gov/uoom). Status as at 2026-08-05.

The US model is opt-out, the EU model is opt-in. They are not alternatives — a site with traffic from both must satisfy both, and the same tag-gating machinery satisfies both if it is built to accept more than one input.

## The signal

| Surface | Exact form |
|---|---|
| HTTP request header | `Sec-GPC: 1` — the field value is defined as `Sec-GPC-field-value = "1"` |
| DOM | `navigator.globalPrivacyControl`, declared as `readonly attribute boolean globalPrivacyControl` |
| Site declaration | `/.well-known/gpc.json`, a JSON object with members `gpc` (boolean) and `lastUpdate` (RFC 3339 date) |

```json
{ "gpc": true, "lastUpdate": "2026-08-05" }
```

Serve that file with `Content-Type: application/json` from the origin the declaration applies to. It states that the site honours the signal.

GPC became an official work item of the W3C Privacy Working Group in November 2024 and is being standardised.

## Which US jurisdictions require honouring it

Verified:

- **California.** The Attorney General's CCPA page states that a user-enabled global privacy control such as GPC "must be honored by covered businesses as a valid consumer request to stop the sale or sharing of personal information", and that businesses collecting personal information online must offer two or more opt-out methods.
- **Colorado.** The Colorado Department of Law maintains the list of recognised Universal Opt-Out Mechanisms. GPC is currently the only mechanism on it, and controllers within the Colorado Privacy Act thresholds must recognise listed mechanisms from **1 July 2024**. The Department notes the list "shall be updated periodically" and does not exclude further mechanisms.

`[[UNVERIFIED: several other state comprehensive privacy laws (among them Connecticut, Montana, Oregon, Texas, Delaware, Nebraska, New Hampshire, New Jersey, Minnesota and Maryland) are widely reported to require recognition of universal opt-out mechanisms on staggered dates. None of these was verified against a primary source in this session. Confirm each applicable state's statute and rules before advising, and never state an effective date from memory.]]`

## Wiring GPC alongside an EU banner

Rules of combination:

1. **GPC is an opt-out, never an opt-in.** A present GPC signal must never be read as consent for EU purposes. Its only effect is to force categories off.
2. **Read it server-side where you can.** The header arrives with the document request, so the server can decide before a byte of HTML is written — which avoids the SSR trap in `frameworks.md`.
3. **The signal overrides a stale stored state in the opt-out direction only.** If the user has GPC on and a stored grant, treat the grant as withdrawn for sale/share purposes and record the change with `signalSource: "gpc"`.
4. **Do not show an EU-style banner to a GPC user and then ignore it.** That is the "Misleading action" pattern (EDPB Guidelines 03/2022 v2.0 §4.4.3) and, in the US, a failure to honour a valid request.
5. **Record it** like any other decision (`consent-record.md`).

```js
// server (any framework): derive the initial state before rendering
export function initialConsent(req, geo) {
  const gpc = req.headers['sec-gpc'] === '1';
  if (gpc) {
    return { source: 'gpc', categories: { necessary: true, functional: false, analytics: false, marketing: false }, suppressBanner: geo.region === 'US' };
  }
  return { source: 'none', categories: { necessary: true, functional: false, analytics: false, marketing: false }, suppressBanner: false };
}
```

```js
// client: confirm and persist, in case the header was stripped by a proxy
if (navigator.globalPrivacyControl === true) {
  const c = getConsent();
  if (!c || c.categories.analytics || c.categories.marketing) {
    setConsent({ ...(c ?? {}), signalSource: 'gpc', categories: { necessary: true, functional: false, analytics: false, marketing: false } });
  }
}
```

Note the asymmetry: in the EEA, suppressing the banner is wrong even with GPC present, because the user still needs the opportunity to consent to functional purposes and the site still needs a mechanism to obtain consent. In US-only contexts, honouring GPC silently is the expected behaviour.

## Why the same gating solves the pixel-litigation exposure

Private litigation in California under the Invasion of Privacy Act (Cal. Penal Code § 631 and § 632.7) has been used against websites that run third-party pixels, session-replay tools and chat widgets, on the theory that the third party is an unauthorised party to the communication. The claims turn on facts a developer controls:

- **whether the third-party script ran at all before the user agreed** — the identical question Article 5(3) ePD asks;
- **what it received** — form field contents, URLs, identifiers;
- **whether the user was told and agreed** — and whether that can be proven.

A deny-by-default loading layer with a durable consent record answers all three at once. That is the practical argument for building the gate even for a purely US-facing site: it is the cheapest available reduction of an active litigation exposure, and it costs nothing extra once built for the EU.

`[[UNVERIFIED: California legislative proposals to narrow CIPA's application to website technologies were pending in 2025. Confirm the current statutory position with US counsel; do not represent CIPA exposure as settled either way.]]`

This is exposure management, not legal advice. Anything beyond "gate the tags and keep the records" belongs to counsel.

## Checkpoints

- [ ] `Sec-GPC` header read server-side and applied before first render
- [ ] `navigator.globalPrivacyControl` checked client-side as a fallback
- [ ] `/.well-known/gpc.json` published and current
- [ ] GPC never interpreted as consent
- [ ] GPC-triggered state changes recorded with `signalSource: "gpc"`
- [ ] EEA visitors still receive a banner regardless of GPC
- [ ] Applicable US states confirmed against primary sources, not from memory
- [ ] Session-replay, chat and form-field-capturing tools inventoried separately — they carry the largest litigation exposure
- [ ] Consent records retained in a form usable as evidence
