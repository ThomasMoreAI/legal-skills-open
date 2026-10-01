# Consent records, versioning and re-prompting

Authoritative basis: Article 7(1) GDPR — "the controller shall be able to demonstrate that the data subject has consented"; Article 5(2) GDPR (accountability); CNIL recommandation n° 2020-092 paras 35–39 and 48; Garante per la protezione dei dati personali, Linee guida cookie, provvedimento 10 giugno 2021 n. 231, paras 6.1, 6.2, 7.1. Status as at 2026-08-05.

## What has to be demonstrable

Article 7(1) requires proof that *this* user consented to *these* purposes on *that* wording. A boolean in `localStorage` proves nothing: it does not show what was displayed, what the options were, or that a reject control existed.

The CNIL's recommandation n° 2020-092 para 48 lists proof modalities it considers adequate, non-exhaustively:

- escrow of the successive versions of the consent-collection code with a third party, or publication of a timestamped hash ("un condensat (ou « hash ») de ce code peut être publié de façon horodatée sur une plate-forme publique, pour pouvoir prouver son authenticité a posteriori");
- timestamped screenshots of the visual rendering on mobile and desktop, per site version;
- periodic third-party audits of the collection mechanism;
- timestamped retention of the tool configuration by the CMP vendor.

The practical translation: **version the banner, and store the version with every record.** The record points at an artefact; the artefact is what proves the wording.

## Record shape

Two halves. The client-side state decides what loads. The server-side record proves what happened. Do not conflate them.

Client state, in first-party `localStorage` or a first-party cookie:

```json
{
  "schema": 1,
  "consentId": "[[UUIDv4]]",
  "bannerVersion": "2026.03-b",
  "textVersion": "de-AT-2026-02",
  "timestamp": "2026-08-05T09:14:22.317Z",
  "categories": { "necessary": true, "functional": false, "analytics": true, "marketing": false },
  "providers": { "youtube": true },
  "signalSource": "banner",
  "scope": "example.com"
}
```

Server-side record, appended once per decision:

| Field | Content | Why it is needed |
|---|---|---|
| `consentId` | random UUID, also stored client-side | links the proof to the browser state without an account |
| `timestamp` | ISO 8601 with timezone, server clock | Art 7(1); the client clock is not evidence |
| `bannerVersion` | build identifier of the banner component | ties the record to a specific UI |
| `textVersion` | identifier of the notice/category wording | ties the record to specific words |
| `codeHash` | hash of the deployed banner bundle | CNIL para 48 first modality |
| `categories` | granted/denied per category, explicit both ways | proves granularity |
| `providers` | per-embed grants from click-to-load | those are separate consents |
| `signalSource` | `banner`, `settings`, `withdrawal`, `gpc`, `api` | distinguishes a choice from an inferred state |
| `scope` | domain or domain set the consent covers | consent does not travel across sites by default |
| `locale` | language actually rendered | "Language discontinuity" is a listed deceptive pattern |
| `userAgentFamily` | coarse UA, not the full string | shows which layout was rendered |
| `previousConsentId` | prior record, if this is a change | reconstructs the history including withdrawals |

Deliberately **not** in the record: full IP address, full user agent, page URL history. The proof obligation does not license building a profile out of the proof. If a supervisory authority needs an IP for a specific dispute, a truncated or hashed value with a short retention is the defensible middle.

Withdrawals are records too, with `signalSource: "withdrawal"` and every category `false`. A withdrawal that only deletes the prior record destroys the evidence that the user exercised Article 7(3).

## Retention

There is no statutory number. Anchor it to the limitation period for the claims the record defends against, and write the reasoning down.

- Keep the record while the consent is live, plus the period in which its validity could be challenged.
- Keep the **artefacts** — banner bundle, screenshots, text versions — at least as long as the newest record that references them. A record naming `bannerVersion: 2024.11-a` is worthless once that build is unreconstructable.
- Delete on the same schedule as other accountability evidence, and document the schedule.
- Do not keep records forever "for safety". That is its own Article 5(1)(e) problem.

`[[MISSING: retention period, chosen with the DPO or lawyer and recorded in the processing register]]`

## Versioning the banner so old proofs stay interpretable

```
banner/
  2026.03-b/
    bundle.js            # exact deployed artefact
    bundle.sha256
    text/de-AT.json      # category names, descriptions, button labels
    text/en.json
    screenshots/desktop.png
    screenshots/mobile.png
    manifest.json        # categories, vendors, defaults, hash, released_at
```

Rules that keep this honest:

- **Bump the version on any change to categories, vendor list, default states, button labels or layout.** A copy tweak that changes what a user understood is a version bump.
- **Never mutate a released version directory.** Publish a new one.
- **Adding a vendor to an existing category invalidates prior consent for that category** unless the user was told the vendor list could change and where to check it. Treat vendor additions as a re-consent event, not a config change.
- **Bump the storage key** (`consent.v3` → `consent.v4`) only when the shape changes; migrate rather than discard, so records remain linkable.

## Re-prompting

| Authority | Position | Nature |
|---|---|---|
| Garante (IT), provv. 10.06.2021 n. 231, §6.2 | The banner may be presented again "quando siano trascorsi almeno 6 mesi dalla precedente presentazione del banner" — at least six months after the previous presentation | Binding guidelines for Italy |
| CNIL (FR), recommandation n° 2020-092 §39 | Retaining the choices — **both consent and refusal** — for six months "constitue une bonne pratique" | Recommendation, not binding; §38 says the interval must reflect context and the scope of the original consent |
| EDPB Guidelines 03/2022 v2.0 §4.1.1 | "Continuous prompting": repeatedly asking users to consent, so that they give in from fatigue, is a deceptive design pattern | Guidance |

Implementation consequences:

- **Store refusals with the same durability as consents.** A refusal that is not stored produces a banner on every page load — which is both the Garante violation and the "Continuous prompting" pattern.
- **Do not re-prompt earlier than the applicable interval** for the jurisdictions in `intake.md`. Six months is the safe floor where Italian or French traffic is in scope.
- **A banner version bump is a legitimate reason to re-ask**, because the wording changed. Fatigue-driven bumps are not; if you are bumping versions monthly, the interval rule is being evaded.
- **Reopening the settings dialog from the footer link is not a re-prompt.** The user initiated it. Only unsolicited display counts.
- **Never treat a `null` state as a reason to fire.** Unknown means denied.

## Checkpoints

- [ ] Server-side record written on every decision, including refusals and withdrawals
- [ ] Record contains banner version, text version and code hash
- [ ] Deployed banner artefacts archived per version and immutable
- [ ] Categories stored explicitly as granted **and** denied, never by omission
- [ ] Per-provider embed grants recorded separately
- [ ] `signalSource` distinguishes banner, settings, withdrawal and GPC
- [ ] Withdrawal appends a record rather than deleting the prior one
- [ ] Retention period chosen, documented and enforced by a job
- [ ] No full IP or full user agent stored in the record
- [ ] Refusals persist for at least six months where IT or FR traffic is in scope
- [ ] Re-prompt only on version bump or after the interval; no per-page-load prompting
- [ ] `[[MISSING: …]]` raised for retention period and record storage location if undecided
