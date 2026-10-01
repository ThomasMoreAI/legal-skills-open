# IAB Europe TCF

Authoritative basis: IAB Europe Transparency and Consent Framework documentation (iabeurope.eu); IAB Tech Lab CMP API v2 specification (github.com/InteractiveAdvertisingBureau/GDPR-Transparency-and-Consent-Framework); Belgian Data Protection Authority decision of 2 February 2022. Status as at 2026-08-05.

## When a site actually needs TCF

TCF is a **contractual** requirement of the programmatic advertising supply chain, not a legal one. No statute mentions it. You need it when:

- you sell display inventory through an SSP, ad exchange or header-bidding setup whose partners require a TC String;
- you run Google's ad stack in a configuration that requires a Google-certified CMP for EEA/UK traffic;
- a demand partner's contract names TCF.

You do **not** need it when:

- the site has no programmatic advertising;
- the only third parties are analytics, embeds, fonts and a CRM;
- advertising is limited to your own campaigns measured by your own tags.

**Advice for a site without programmatic demand: do not adopt TCF.** It imports several hundred vendors, a purpose vocabulary written for ad tech, a legal-basis model that regulators have already found wanting, and a UI whose vendor list is a textbook "Too many options" pattern (EDPB Guidelines 03/2022 v2.0 §4.1.3). A four-category first-party banner with real blocking is both simpler and easier to defend.

## Mechanics, if you do need it

The CMP exposes a global function. Verbatim signature from the CMP API v2 specification:

```js
__tcfapi(command, version, callback, parameter)
```

Commands:

| Command | Status | Purpose |
|---|---|---|
| `ping` | required | returns loading status synchronously, without async logic |
| `addEventListener` | required | registers a callback invoked on TC String changes |
| `removeEventListener` | required | unregisters a listener by `listenerId` |
| `getInAppTCData` | optional | in-app storage variant |
| `getVendorList` | optional | fetches the Global Vendor List by version |
| `getTCData` | **deprecated in TCF v2.2** | the spec directs you to `addEventListener` and its callback instead |

Enumerations: `cmpStatus` is `'stub' | 'loading' | 'loaded' | 'error'`; `displayStatus` is `'visible' | 'hidden' | 'disabled'`; `eventStatus` is `'tcloaded' | 'cmpuishown' | 'useractioncomplete'`.

Reading consent correctly:

```js
function onTcf(cb) {
  if (typeof window.__tcfapi !== 'function') return;      // no CMP: treat as denied
  window.__tcfapi('addEventListener', 2, (tcData, success) => {
    if (!success) return;
    if (tcData.eventStatus !== 'tcloaded' && tcData.eventStatus !== 'useractioncomplete') return;
    if (tcData.gdprApplies === false) return cb({ applies: false, tcData });
    cb({ applies: true, tcData });
  });
}
```

Key fields on `tcData`: `tcString` (base64url encoded), `tcfPolicyVersion`, `cmpId`, `cmpVersion`, `gdprApplies`, `eventStatus`, `cmpStatus`, `listenerId`, `isServiceSpecific`, `publisherCC`, `purposeOneTreatment`, plus nested `purpose`, `vendor`, `specialFeatureOptins` and `publisher` objects.

Three implementation traps:

1. **`gdprApplies` is a tri-state.** `true`, `false`, or `undefined` when the CMP cannot determine it. Undefined must be handled as "assume it applies".
2. **The stub matters.** The `__tcfapi` stub must exist before any vendor script runs, otherwise vendors that call it early get no answer and fall back to their own default — which is not yours.
3. **A TC String is not a blocking mechanism.** It communicates a decision to vendors that agreed to honour it. The vendor script still has to be gated by `blocking-layer.md`; the TC String tells it what to do once loaded.

## Vendor list mechanics

The Global Vendor List is a versioned JSON document enumerating registered vendors, their declared purposes, legal bases, retention periods and policy URLs. A CMP fetches it, renders it, and encodes the user's per-vendor and per-purpose decisions into the TC String.

Consequences you own as a publisher:

- **The list changes without your involvement.** Vendors are added between GVL versions. A user who consented under GVL version N did not consent to vendors added in N+1. Decide, and document, whether a GVL bump triggers re-consent — see the vendor-change rule in `consent-record.md`.
- **You are responsible for the vendors you enable**, not the CMP. Enabling all vendors by default because the CMP offers it is the "Deceptive snugness" pattern (EDPB Guidelines 03/2022 v2.0 §4.2.1).
- **Purpose 1 (storing and accessing information on a device) is the Article 5(3) purpose.** Without it, nothing else in the framework is lawful for that vendor.

## Version status

Version history as published by IAB Europe on its Transparency and Consent Framework page:

| Version | Launched |
|---|---|
| v1.1 | 25 April 2018 |
| v2.0 | 21 August 2019 |
| v2.1 | 19 August 2020 |
| v2.2 | 16 May 2023 |
| v2.3 | April 2025, with an adoption deadline of 28 February 2026 |

`[[UNVERIFIED: IAB Europe's own /tcf/ page still described v2.2 as the latest version when checked on 2026-08-05, while the Transparency and Consent Framework page lists v2.3 with a 28 February 2026 adoption deadline. Confirm the version your CMP and your demand partners are actually running before quoting a version number.]]`

## The IAB Europe case

The Belgian Data Protection Authority decided on **2 February 2022** that:

- the TC String, which captures and links user preferences to identifiable individuals, constitutes personal data;
- IAB Europe acts as a data controller in respect of it;
- there was no valid legal basis, insufficient transparency, and missing accountability documentation (register of processing, DPO, DPIA).

Sanction: an administrative fine of **€250,000** plus corrective measures within two months, including a prohibition on relying on legitimate interest for TCF data processing. An action plan was validated by the authority on 11 January 2023, but its implementation was suspended pending the courts.

IAB Europe appealed to the Belgian Market Court, which referred preliminary questions to the Court of Justice of the European Union as **case C-604/22**.

`[[UNVERIFIED: the CJEU judgment in C-604/22 and the Belgian Market Court's final ruling could not be retrieved from a primary source in this session (curia.europa.eu and eur-lex.europa.eu did not render). Check curia.europa.eu for C-604/22 and the Belgian DPA's newsroom for the Market Court outcome before advising on TCF's current legal standing.]]`

What does not depend on the outcome: TCF governs signalling between publishers and vendors. Whatever the courts conclude about IAB Europe's role, a publisher that loads a vendor script before the user decides has breached Article 5(3) ePD on its own account.

## Checkpoints

- [ ] TCF adoption justified by a named contractual requirement, not by habit
- [ ] `__tcfapi` stub present before any vendor script can call it
- [ ] `gdprApplies === undefined` handled as "applies"
- [ ] Consent read via `addEventListener`, not the deprecated `getTCData`
- [ ] Vendor scripts still gated at the loading layer, independently of the TC String
- [ ] Vendor selection reviewed and reduced; not "all vendors" by default
- [ ] GVL version recorded with the consent record; re-consent policy on GVL bumps documented
- [ ] Purpose 1 handling verified for every vendor
- [ ] CMP version and TCF version confirmed against demand partners
- [ ] `[[MISSING: …]]` raised where the demand-partner requirement cannot be evidenced
