---
name: mi-oakland-codearranger
title: Oakland County Circuit Court (Sixth Judicial Circuit — Pontiac)
description: This skill should be used when drafting or filing documents in the Oakland County Circuit Court — the Sixth Judicial Circuit, seated in Pontiac. Triggers include "Oakland County Circuit Court", "Sixth Circuit Pontiac", "6th Circuit Michigan", "file in Oakland County", "sued in Oakland County", "Oakland County Courthouse", "Oakland Business Court", "Oakland County scheduling order", "6th Circuit scheduling order", and "Oakland County case number". Covers the Civil/Criminal Division general civil jurisdiction (over $25,000), the case-type and case-number conventions, the Michigan Business Court docket under MCL 600.8031 et seq., the Sixth Circuit's local administrative orders and case-management / scheduling-order practice, and MiFILE / MiCOURT TrueFiling e-filing. Layer on top of `mi-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-oakland
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Oakland County Circuit Court (Sixth Judicial Circuit — Pontiac)

> **NOT LEGAL ADVICE.** These notes describe the venue's
> procedural mechanics as a drafting aid, not legal advice.
> Local administrative orders and judge-specific practices
> change; verify with the clerk and the current local rules
> before relying on anything here.

Use this skill in addition to `mi-statewide-format` when the case
is in the **Oakland County Circuit Court**, Michigan's **Sixth
Judicial Circuit**. Oakland is one of Michigan's most populous
counties; its Circuit Court is a high-volume general civil and
criminal trial court.

## Location and divisions

- **Oakland County Courthouse**, Pontiac (the Circuit Court
  complex on the County Service Center campus). Confirm the
  current street address, department/courtroom, and any annex
  locations with the Clerk / Register of Deeds office before
  filing or appearing.
- The Circuit Court is organized into a **Civil/Criminal
  Division** (general civil litigation and felony criminal) and a
  separate **Family Division** (domestic relations, juvenile,
  guardianship — see `mi-family-court`).
- This skill addresses the **Civil/Criminal Division** civil
  side. The Family Division is governed by MCR subchapter 3.200
  and is out of scope here.

## Jurisdiction

- The Circuit Court is Michigan's court of **general
  jurisdiction**. Civil actions seeking **more than $25,000** are
  filed in Circuit Court; matters at or below $25,000 are District
  Court matters (see `mi-district-courts`, `mi-36th-district`).
- Equity, superintending-control, and most appeals from District
  Court and administrative agencies also lie in Circuit Court.
- Confirm the amount-in-controversy and any small-claims /
  district overlap before choosing the forum.

## Case-type and case-number conventions

- Michigan circuit-court case numbers follow the statewide SCAO
  pattern of a **two-digit year, a sequential number, and a
  case-type code** (for example, a general civil case carries the
  **"NZ" / "CZ"**-family code, a business/commercial case the
  **"CB"** code, and an auto-negligence case the **"NI"** code).
  Confirm the exact suffix the Oakland clerk assigns for your
  cause of action — the case-type code drives docket routing.
- The case number, once assigned, anchors the caption per
  `mi-statewide-format`. **Do not guess the case-type code**;
  confirm it against the current SCAO case-type code list and the
  Oakland clerk's intake practice.

## Michigan Business Court (MCL 600.8031 et seq.)

- Every circuit with **not fewer than 3 circuit judges** must
  operate a **Business Court** as a special docket (MCL 600.8033).
  The Sixth Circuit (Oakland) meets that threshold and maintains a
  Business Court docket.
- A **"business or commercial dispute"** under **MCL 600.8031**
  includes actions where all parties are business enterprises, or
  where at least one party is a business enterprise and the claim
  arises out of the parties' business or commercial relationship —
  e.g., disputes over the sale/merger of a business, shareholder
  and member rights, commercial contracts, commercial real
  property, and trade-secret / non-compete matters.
- The statute **expressly excludes** personal injury, product
  liability, family-law matters, employment discrimination and
  civil-rights actions, wrongful discharge (except claims by
  corporate officers/directors), and workers'-compensation
  claims — those do **not** belong on the Business Court docket.
- A complaint that pleads a qualifying business/commercial dispute
  should be flagged for the Business Court docket at filing
  (typically via the case-type code and a civil cover sheet).
  Confirm the current Business Court assignment mechanics and any
  required statement with the Oakland clerk. See
  `mi-commercial-disputes` for the substantive framework.

## Local administrative orders and scheduling practice

- Beyond the statewide MCR, the Sixth Circuit operates under its
  own **local administrative orders (LAOs)** approved by the State
  Court Administrative Office, which govern case assignment,
  e-filing specifics, and docket management.
- The Circuit Court manages civil cases through **case-management
  and scheduling orders**: after the case is at issue, the court
  enters a **scheduling order** setting discovery cutoffs,
  motion-cutoff and dispositive-motion dates, case-evaluation /
  ADR (MCR 2.403 / 2.410) dates, settlement-conference dates, and
  the trial date. Calendar your obligations from the **scheduling
  order in your specific case**, not from a generic template.
- Status conferences and a **settlement / pretrial conference**
  are typically required before trial. Confirm the assigned
  judge's individual practice guidelines, motion-call day, and
  praecipe / notice-of-hearing requirements before noticing a
  motion. See `mi-schedule-hearing` and `mi-hearings`.

**Agent behavior:** before drafting a notice of hearing, setting
a page-limited brief, or calendaring a deadline, fetch the current
Sixth Circuit local administrative orders and the assigned judge's
practice guidelines, and read the scheduling order entered in the
case. Confirm motion-call procedure and chambers-copy
requirements.

## E-filing — MiFILE / MiCOURT TrueFiling

- Oakland County Circuit Court participates in Michigan's
  statewide **MiFILE** electronic-filing system (the **MiCOURT
  TrueFiling** platform). Confirm whether e-filing is **mandatory**
  for your case type and party, the current document-type
  selections, and the filing-fee / fee-waiver workflow.
- See `mi-file-packet` for the packet-assembly and preflight
  workflow and `mi-statewide-format` for the MCR 1.109 electronic
  document requirements.

## Composition

- For statewide format and the caption: `mi-statewide-format`
- For other Oakland venues / other counties: `mi-circuit-courts`,
  `mi-circuit-courts`; District Court matters under $25,000:
  `mi-district-courts`, `mi-36th-district`
- For Family Division matters: `mi-family-court`, `mi-family-law`
- For the substantive Business Court framework:
  `mi-commercial-disputes`
- For the first responsive pleading: `mi-first-30-days`
- For drafting motions / declarations / orders: `mi-draft-motion`,
  `mi-draft-declaration`, `mi-draft-note`, `mi-draft-order`
- For discovery and case evaluation / ADR: `mi-discovery`
- For scheduling and hearings: `mi-schedule-hearing`,
  `mi-hearings`
- For filing mechanics: `mi-file-packet`
- For pro se conventions: `mi-pro-se`

## References

- `mi-law-references` — MCR, MRE, Michigan statutes (incl. MCL
  600.8031 et seq.), and local-rules corpus
- Sixth Circuit (Oakland County) local administrative orders and
  the assigned judge's practice guidelines (confirm current
  versions with the clerk)
