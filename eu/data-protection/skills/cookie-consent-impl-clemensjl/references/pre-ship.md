# Pre-ship checklist

Run before every release that touches tags, embeds, the banner, the tag manager container or the CSP. Findings are reported with the rule and the initiator, not as general advice. The checklist ends in a machine assertion; a visual pass is not a pass.

## 0. Gate the checklist itself

- [ ] The build under test is the build that will ship — same bundle, same CDN, same tag manager container version
- [ ] Tested from a clean automated profile, extensions disabled
- [ ] Tag manager container published, not in preview mode

## 1. Blocking layer

- [ ] Every non-essential `<script>` in markup carries `type="text/plain"` and a category attribute
- [ ] Every gated tag reachable from JS is injected after the signal, not shipped in markup
- [ ] No `preconnect`, `dns-prefetch` or `preload` pointing at a gated third party
- [ ] No remote `@font-face`, CSS `url()`, `<img>` pixel or remote `poster` before consent
- [ ] Analytics SDKs are dynamic imports, not static ones
- [ ] No `document.write` path in any gated tag
- [ ] Service worker registration deferred or scoped to same-origin
- [ ] CSP enforcing, with `connect-src 'self'` unless deliberately widened; report endpoint receiving

## 2. Embeds

- [ ] No third-party iframe in the DOM before consent
- [ ] Placeholders use locally hosted thumbnails; no provider thumbnail requests
- [ ] One click activates; the remember option writes a recorded consent
- [ ] Fonts self-hosted; provider `<link>` removed
- [ ] Captcha and payment SDKs scoped to the pages that need them

## 3. Banner UI

- [ ] Reject control on the first layer, same element type as accept
- [ ] Accept and reject equal in size, weight and emphasis; reject text contrast ≥ 4.5:1
- [ ] No category pre-ticked except strictly necessary, which is disabled and explained
- [ ] Escape, backdrop click and scroll do not write consent
- [ ] Settings reachable from a persistent link on every route; reopened dialog shows current state
- [ ] Revoking all takes no more interactions than accepting all
- [ ] Banner locale matches page locale on every locale the site serves
- [ ] Keyboard operable and focus-trapped
- [ ] No promotional content inside the dialog

## 4. Signals

- [ ] Consent Mode `default` is the first executed script; all seven signals set; `wait_for_update` present
- [ ] Exactly one `update` per decision, with all seven signals
- [ ] Basic mode in use for EEA/UK traffic; advanced mode, if used, escalated in writing
- [ ] GTM tags carry explicit consent settings, not "not set"
- [ ] `Sec-GPC` read server-side; `navigator.globalPrivacyControl` read client-side; never treated as consent
- [ ] `/.well-known/gpc.json` published and current, where US traffic is in scope
- [ ] TCF, if present, justified by a named contractual requirement; `__tcfapi` stub loads first

## 5. Records

- [ ] Server-side record written on grant, refusal and withdrawal
- [ ] Record contains banner version, text version, code hash, categories both ways, scope, locale, signal source
- [ ] Banner artefacts archived immutably for the version being shipped
- [ ] Retention period implemented by a job, not by intention
- [ ] Refusals persist; no re-prompt before the applicable interval
- [ ] Version bump performed if categories, vendors, defaults or labels changed

## 6. Consistency with the published texts

The texts themselves belong to the `legal-*` skills. What is checked here is only whether the code matches them.

- [ ] Every host in the audit trace appears in the cookie policy
- [ ] Every vendor in the cookie policy appears in the trace after accept
- [ ] Cookie names and lifetimes in the policy match the observed cookies
- [ ] Category names in the banner match the category names in the notice
- [ ] Any divergence reported to whoever owns the text, with the trace attached

## 7. The verifiable assertion

This is the pass condition. Everything above is preparation.

```bash
node consent-audit.mjs https://[[HOST]]                 # exit 0 required
node consent-audit.mjs https://[[HOST]]/[[DEEP_PATH]]   # exit 0 required
```

Both runs must report:

- `beforeDecision.thirdPartyHosts` — empty
- `beforeDecision.storageWrites` — nothing outside consent, session and CSRF keys
- `beforeDecision.cookies` — nothing outside your own session, CSRF and consent cookies

Then, with the accept phase:

- `afterAccept.newThirdPartyHosts` — set-equal to the vendor host list in the cookie policy

Run the same two commands with a mobile context and with `Sec-GPC: 1` where US traffic is in scope. Four green runs, recorded in the release notes with the timestamp and the commit.

- [ ] Audit wired into CI so the build fails on regression
- [ ] Output of the four runs attached to the release record
- [ ] `<!-- CONSENT GATING – NOT VERIFIED AT NETWORK LEVEL -->` removed **only** after all runs pass, and only by the person who ran them

## Findings format

| Severity | Host / element | Initiator | Rule | Fix |
|---|---|---|---|---|
| critical / high / medium | what | file:line or network initiator | Art 5(3) ePD, GDPR Art, or EDPB document and paragraph | concrete change |

**Critical** means the site loads or stores something before a decision, the reject control is missing or unusable, or a consent cannot be evidenced. Critical findings block the release.
