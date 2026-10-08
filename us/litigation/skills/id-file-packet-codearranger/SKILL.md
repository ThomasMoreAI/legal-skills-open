---
name: id-file-packet-codearranger
title: Assemble an Idaho Court Filing Packet
description: Use when assembling and filing a complete Idaho court motion or pleading packet. Triggers include "file an Idaho court packet", "assemble Idaho filing", "iCourt e-file", "Odyssey File & Serve Idaho", "I.R.E.F.S. e-filing", "how do I e-file in Idaho", "what documents do I file with my Idaho motion", "Idaho filing checklist", "redact sensitive data Idaho", "Idaho filing fee", "fee waiver Idaho", "do I file on paper or electronically in Idaho". Walks through assembling the multi-document packet (motion + Memorandum + Notice of Hearing + proposed order + affidavit/declaration + certificate of service + exhibits), the iCourt / Odyssey File & Serve (I.R.E.F.S.) e-filing channel and whether it is mandatory, the Idaho sensitive-data handling rule, the filing-fee and fee-waiver question, and paper filing where applicable.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-file-packet
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Efiling Irefs
  path: references/efiling-irefs.md
- title: Packet Components
  path: references/packet-components.md
---

# Assemble an Idaho Court Filing Packet

> **NOT LEGAL ADVICE.** This skill walks through filing mechanics.
> Verify the e-filing platform, document types, fees, redaction
> rule, and pro-se acceptance with the filing court's clerk before
> submitting.

Use this skill when ready to **submit** an Idaho trial-court filing.
First determine the **filing channel**, then assemble and preflight
the multi-document packet.

## Idaho e-filing — iCourt / Odyssey File & Serve (I.R.E.F.S.)

Idaho's statewide e-filing system is **iCourt E-File**, built on
**Tyler Technologies' Odyssey File & Serve**, governed by the **Idaho
Rules for Electronic Filing and Service (I.R.E.F.S.)**:

- **Mandatory for attorneys.** Under **I.R.E.F.S. 4(a)**, attorneys
  must e-file.
- **Optional for self-represented individuals.** Under **I.R.E.F.S.
  4(b)**, a self-represented party **may** e-file but is not
  required to, and may still file on paper at the clerk's window.
- **E-filing = consent to e-service.** Under **I.R.E.F.S. 17**, a
  party who e-files consents to electronic service of subsequent
  documents.
- **E-format.** Documents are submitted per **I.R.E.F.S. 6** —
  **text-searchable PDF**, within the system's size caps.
- Odyssey's **"Guide & File"** assisted interview is an optional
  front end that helps self-represented filers assemble certain case
  types.

Confirm the court is live on iCourt for the case type and whether
the **Magistrate Division** vs. **District Court** routing affects
the filing path before assuming the channel.

## E-filing workflow (iCourt / Odyssey File & Serve)

The portal shape is consistent across courts:

1. Register / log in to an iCourt File & Serve account
2. Search for the case by case number or party name (or start a new
   case for an initial filing)
3. Select the court, case category, and the **filing / document
   type** for each component
4. Upload each component as a **separate text-searchable PDF** per
   I.R.E.F.S. 6 (mind the size caps)
5. Pay any filing fee, or attach the **fee-waiver** application
6. Submit; the system returns a filing confirmation / file-stamp and
   effects electronic service on registered parties (I.R.E.F.S. 17)

## Paper filing (self-represented; courts/case types not on iCourt)

A self-represented filer may file on **paper** under I.R.E.F.S. 4(b).
Bring clean copies to the clerk's window during business hours; the
clerk file-stamps the original and returns a stamped copy. Confirm
whether the court accepts mail or drop-box filings and how many
copies (judge's copy / conformed copy) the court wants.

## Multi-document packet — typical components

A standard Idaho motion packet consists of these documents:

| # | Document | Authority / note |
|---|----------|------|
| 1 | Motion | I.R.C.P. 7(b) — grounds with particularity |
| 2 | Memorandum in support | The supporting brief presented with the motion |
| 3 | Notice of Hearing | I.R.C.P. 7(b)(3) — served/filed ≥14 days before hearing (28 for Rule 56) |
| 4 | Affidavit or declaration | Notarized affidavit or Idaho Code § 9-1406 declaration; I.R.E. 803(6) records foundation |
| 5 | Exhibits | Attach written instruments referenced in the motion (part of the pleading, I.R.C.P. 10) |
| 6 | Proposed order | Submitted for the judge's signature; see `id-submit-order` |
| 7 | Certificate of Service | I.R.C.P. 5 — date, manner, recipients |

Choose the closest matching document-type label in the iCourt menu;
the menus vary by court and case category.

## Sensitive / personal information — redaction

Idaho **restricts sensitive and personal information** in court
filings. Before filing, review every component (including exhibits)
and handle protected data as the governing rule requires —
generally by **omitting or partially redacting** identifiers such as
Social Security and financial-account numbers, and using any
required sensitive-data mechanism where the data must reach the
court but be kept out of the public file.

> Verify the exact rule and procedure against `id-law-references` —
> confirm the precise list of protected identifiers, the
> partial-redaction format, and whether a separate sealed/restricted
> filing is required. The filing court may have additional local
> requirements.

The filing party is responsible for the redaction; the clerk does
not redact for you.

## Preflight — run the helper scripts

Before assembling the packet:

```
# Format / caption + form check (I.R.C.P. 2 baseline)
python3 plugins/id-court-docs/scripts/format-check.py path/to/filing.docx

# Deadline arithmetic — I.R.C.P. 2.2 computation, +3-day mail
# add-on, with Idaho court-holiday handling (I.C. § 73-108)
python3 plugins/id-court-docs/scripts/case-calendar.py ...
```

Use `case-calendar.py` to confirm the Notice-of-Hearing lead time
(14 days, or 28 for a Rule 56 motion) and to compute response
deadlines with the applicable mail add-on.

## Filing fees

Filing fees are set by statute and the clerk's fee schedule and vary
by court and case type. **Confirm the current amount with the filing
court's clerk** before submitting; do not hard-code a figure. Pay by
the portal's accepted method (card / e-check) or at the clerk's
cashier window for paper filings.

### Fee waiver

A filer who cannot afford the fees may apply for a **waiver of fees
and costs** on the ground of indigency. File the application with the
first filing rather than paying and seeking a refund. The court
reviews the application and enters an order. Verify the current
standard and the operative application form with the clerk. See
`id-pro-se`.

## Filing vs. service — two distinct steps

Filing with the court is **not** the same as serving the opposing
party:

1. **Filing** — through iCourt / Odyssey File & Serve, or at the
   clerk's window (self-represented).
2. **Service of process** (initial summons + complaint) — under
   **I.R.C.P. 4** (verify the current summons life / return period).
3. **Service of subsequent papers** (motions, Notice of Hearing,
   orders) — under **I.R.C.P. 5**, on every party by an allowed
   method, documented in the **Certificate of Service**. Add **+3
   days** for service by mail when computing any deadline that runs
   from service. E-filing constitutes consent to e-service under
   **I.R.E.F.S. 17**.

If the system performs electronic service on registered parties, a
party without an e-filing account must still be served by another
allowed I.R.C.P. 5 method — confirm the portal's e-service coverage
for each party.

## Pre-filing checklist

| Check | Done |
|-------|------|
| Filing channel identified (iCourt vs. paper) and mandatory-vs-optional confirmed (attorney = mandatory, self-represented = optional) | ☐ |
| `scripts/format-check.py` run; no FAIL | ☐ |
| `scripts/case-calendar.py` confirms the Notice-of-Hearing lead time + mail add-on | ☐ |
| `id-quality-check` pre-filing review complete | ☐ |
| `id-fact-check` deep audit complete (high-stakes filing) | ☐ |
| Caption (court / county / case number) matches across all documents | ☐ |
| Exhibits attached and referenced (part of the pleading, I.R.C.P. 10) | ☐ |
| Notice of Hearing prepared with 14-day (or Rule 56 28-day) timing | ☐ |
| Proposed order drafted as a separate document | ☐ |
| Each component saved as a separate text-searchable PDF (I.R.E.F.S. 6) | ☐ |
| Signature block compliant — Idaho State Bar number (attorney) or self-represented designation | ☐ |
| Certificate of Service shows method, date, recipients (I.R.C.P. 5) | ☐ |
| Sensitive / personal information handled per the Idaho redaction rule | ☐ |
| Filing fee available, or fee-waiver application ready | ☐ |
| Service-of-process plan (I.R.C.P. 4) / service-of-papers plan (I.R.C.P. 5) ready | ☐ |

## Composition

- For statewide format baseline: `id-statewide-format`
- For drafting each component: `id-draft-motion`,
  `id-draft-declaration`, `id-draft-note`, `id-draft-order`
- For pre-filing review: `id-quality-check` (lighter) and
  `id-fact-check` (deep evidentiary)
- For clearing the hearing date and the Notice of Hearing:
  `id-schedule-hearing`, `id-draft-note`
- For court-specific filing channels and local rules: `id-ada`,
  `id-bonneville`, `id-county-courts`, `id-family-court`
- For pro-se filers (fee waiver, self-represented conventions,
  paper-filing option): `id-pro-se`
- For deadline arithmetic: `id-deadlines`
- For post-hearing order submission: `id-submit-order`

## References to author

- `references/efiling-irefs.md` — iCourt / Odyssey File & Serve
  walkthrough and the I.R.E.F.S. 4 / 6 / 17 pointers
- `references/packet-components.md` — the component checklist and
  certificate-of-service form
