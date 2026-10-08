---
name: mi-file-packet-codearranger
title: Assemble a Michigan Court Filing Packet
description: This skill should be used when assembling and filing a complete Michigan court motion or pleading packet. Triggers include "file a Michigan court packet", "assemble my Michigan filing", "how do I e-file in Michigan", "MiFILE e-filing", "MiCOURT TrueFiling", "TrueFiling Michigan", "what documents do I file with my Michigan motion", "Michigan filing checklist", "redact PII Michigan MCR 1.109", "protect personal identifying information Michigan", "Michigan filing fee", "MC 20 fee waiver", "do I file on paper or electronically in Michigan". Walks through assembly of the multi- document packet (motion + brief + notice of hearing + proof of service + proposed order + exhibits), the MiFILE / TrueFiling e-filing channel and whether it is mandatory in the venue, the MCR 1.109(D)(9) protected-personal-identifying-information redaction rule, the filing-fee question and the MC 20 fee waiver, and the difference between filing and service.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-file-packet
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Assemble a Michigan Court Filing Packet

> **NOT LEGAL ADVICE.** This skill walks through filing mechanics.
> Verify the e-filing platform, document types, fees, and pro-se
> acceptance with the filing court's clerk before submitting.

Use this skill when ready to **submit** a Michigan trial-court
filing. First determine the **filing channel** for the venue, then
assemble and preflight the multi-document packet.

## Michigan e-filing — MiFILE / MiCOURT (TrueFiling)

Michigan's statewide e-filing system is **MiFILE**, built on the
Tyler Technologies **TrueFiling** platform and reached through the
**MiCOURT** portal. E-filing is governed by **MCR 1.109(G)**
(electronic filing and electronic service).

E-filing has been rolling out **court by court**, and is
**mandatory in many courts** for many case types — but not every
court or case type is live. Before assuming the channel, confirm
for the specific court:

1. **Whether MiFILE / TrueFiling is live** in that court; and
2. **Whether e-filing is mandatory** for the case type, or paper is
   still accepted.

Where the court is not yet on MiFILE, file on **paper** at the
clerk's window (see below).

## E-filing workflow (MiFILE / TrueFiling)

The TrueFiling shape is consistent across courts:

1. Register / log in to a MiFILE account through the MiCOURT portal
2. Search for the case by case number or party name (or start a new
   case for an initial filing)
3. Select the court, case type, and the **filing / document type**
   for each component
4. Upload each component as a **separate PDF** (text-searchable;
   verify any bookmark / size requirements for long filings)
5. Pay any filing fee, or attach the **MC 20** fee-waiver request
6. Submit; the system returns a file-stamp / acceptance confirmation
   and effects electronic service on registered parties

## Paper filing (courts not on MiFILE)

Where e-filing is unavailable, bring clean copies to the clerk's
window during business hours; the clerk file-stamps the original and
returns a stamped copy. Confirm whether the court accepts mail or
drop-box filings, and how many copies (judge's copy / conformed
copy) the court wants.

## Multi-document packet — typical components

A standard Michigan motion packet consists of these documents:

| # | Document | Authority / note |
|---|----------|------|
| 1 | Motion | MCR 2.119 |
| 2 | Brief in support (if used) | MCR 2.119(A)(2); page limits are local |
| 3 | Notice of Hearing | MCR 2.119(C) notice period; see `mi-schedule-hearing` |
| 4 | Supporting affidavit (sworn) | MCR 2.119(B); MRE 803(6) records foundation |
| 5 | Exhibits | Attach written instruments referenced in the motion |
| 6 | Proposed Order | Submitted with the motion; see `mi-submit-order` |
| 7 | Proof of Service | MCR 2.107(D) — date, method, recipients |

Choose the closest matching document-type label in the TrueFiling
menu; the menus vary by court and case type.

## Personal identifying information — MCR 1.109(D)(9)

Michigan **protects personal identifying information** in court
filings under **MCR 1.109(D)(9)**. Before filing, review every
component (including exhibits) and handle protected PII as the rule
requires — generally by **excluding or partially redacting** items
such as Social Security / financial-account numbers and similar
identifiers, and using the **MC 97 / MC 97a** addendum mechanism
where the protected data must be supplied to the court but kept out
of the public filing.

> Verify the exact subrule text and the current MC 97-series
> procedure against `mi-law-references` — the precise list of
> protected identifiers and the partial-redaction format are set by
> rule, and the filing court may have additional requirements.

The redacting party is responsible for the redaction; the clerk does
not redact for you.

## Preflight — run the helper scripts

Before assembling the packet:

```
# Format / MCR 1.109 caption + form check
python3 plugins/mi-court-docs/scripts/format-check.py path/to/filing.docx

# Deadline arithmetic — MCR 1.108 computation, MCR 2.107(C) service
# add-ons, with Michigan court-holiday handling
python3 plugins/mi-court-docs/scripts/case-calendar.py ...
```

Use `case-calendar.py` to confirm the motion's hearing is noticed
with the required lead time under **MCR 2.119(C)** and to compute any
response deadline with the applicable service add-on.

## Filing fees

Filing fees are set by statute and the clerk's fee schedule and vary
by court and case type. **Confirm the current amount with the filing
court's clerk** before submitting; do not hard-code a figure. Pay by
the platform's accepted method (card / e-check) or at the clerk's
cashier window for paper filings.

### Fee waiver — MC 20

A filer who cannot afford the fees may request a waiver by filing the
**MC 20** (Fee Waiver Request / affidavit and order suspending fees)
with the first filing — do not pay and seek a refund later. The court
reviews the request and enters an order granting, denying, or
deferring fees. Verify the current MC 20 form and eligibility
standard with the clerk. See `mi-pro-se`.

## Filing vs. service — two distinct steps

Filing with the court is **not** the same as serving the opposing
party:

1. **Filing** — through MiFILE / TrueFiling or at the clerk's window.
2. **Service of process** (initial summons + complaint) — under
   **MCR 2.105**, with the summons issued under **MCR 2.102** and its
   life / return governed by that rule (verify the current summons
   validity period).
3. **Service of subsequent papers** (motions, notices, orders) —
   under **MCR 2.107**, on every party by an allowed method;
   document it in the **Proof of Service** under MCR 2.107(D). Add
   the applicable service period under **MCR 2.107(C)** when service
   is by mail or other non-personal method.

If MiFILE performs electronic service on registered parties under
MCR 1.109(G) / MCR 2.107(C)(4), a party without an e-filing account
must still be served by another allowed MCR 2.107 method — confirm
the platform's e-service coverage for each party.

## Pre-filing checklist

| Check | Done |
|-------|------|
| Filing channel identified (MiFILE / TrueFiling vs. paper) and mandatory-vs-optional confirmed for the court + case type | ☐ |
| `scripts/format-check.py` run; no FAIL | ☐ |
| `scripts/case-calendar.py` confirms MCR 2.119(C) notice lead time + any service add-on | ☐ |
| `mi-quality-check` pre-filing review complete | ☐ |
| `mi-fact-check` deep audit complete (high-stakes filing) | ☐ |
| Caption (court / county / case number) matches across all documents (MCR 1.109(D) + MCR 2.113(C)) | ☐ |
| Exhibits attached and referenced | ☐ |
| Proposed Order drafted as a separate document | ☐ |
| Each component saved as a separate text-searchable PDF | ☐ |
| Signature block compliant (MCR 1.109(E)) — bar # (attorney) or self-represented designation | ☐ |
| Proof of Service shows method, date, recipients (MCR 2.107(D)) | ☐ |
| Protected personal identifying information handled per MCR 1.109(D)(9) (MC 97-series where required) | ☐ |
| Filing fee available, or MC 20 fee-waiver request ready | ☐ |
| Service-of-process plan (MCR 2.105) / service-of-papers plan (MCR 2.107) ready | ☐ |

## Composition

- For statewide format baseline: `mi-statewide-format`
- For drafting each component: `mi-draft-motion`,
  `mi-draft-declaration`, `mi-draft-order`, `mi-draft-note`
- For pre-filing review: `mi-quality-check` (lighter) and
  `mi-fact-check` (deep evidentiary)
- For clearing the hearing date and the Notice of Hearing:
  `mi-schedule-hearing`
- For court-specific filing channels and local rules: `mi-wayne`,
  `mi-oakland`, `mi-circuit-courts`, `mi-district-courts`,
  `mi-36th-district`
- For pro-se filers (MC 20 fee waiver, self-represented
  conventions): `mi-pro-se`
- For deadline arithmetic: `mi-deadlines`
- For post-hearing order submission: `mi-submit-order`

## References

- `mi-law-references` for MCR 1.108, 1.109, 2.102, 2.105, 2.107,
  2.113, and 2.119 text and the MCR 1.109(D)(9) protected-PII subrule
- The MiCOURT / MiFILE portal and the filing court's clerk for the
  current e-filing status, document types, and fee schedule
- Confirm whether e-filing is mandatory in the venue before assuming
  a channel — Michigan e-filing is rolling out court by court.
