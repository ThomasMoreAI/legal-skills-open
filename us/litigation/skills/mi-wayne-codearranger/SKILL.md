---
name: mi-wayne-codearranger
title: Wayne County Circuit Court (Third Judicial Circuit — Detroit)
description: This skill should be used when drafting or filing civil documents in the Wayne County Circuit Court — the Third Judicial Circuit, in Detroit, Michigan's largest circuit. Triggers include "Wayne County Circuit Court", "Third Circuit Detroit", "3rd Circuit Court", "file in Wayne County", "Detroit circuit court", "sued in Wayne County", "Wayne County Business Court", "3rd Circuit motion praecipe", "Wayne County praecipe", "Coleman A. Young Municipal Center", and "Wayne County civil division". Covers the Civil Division's general-jurisdiction practice (amount in controversy over $25,000), Wayne County case-type codes, the Michigan Business Court designation, the local praecipe motion-scheduling practice, and MiFILE/TrueFiling e-filing. Layer on top of `mi-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-wayne
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Wayne County Circuit Court (Third Judicial Circuit — Detroit)

> **NOT LEGAL ADVICE.** These notes describe the venue's
> procedural mechanics as a drafting aid, not legal advice. Local
> administrative orders and judge-specific practices change;
> verify with the clerk and the current Third Circuit local rules
> before relying on anything here.

Use this skill in addition to `mi-statewide-format` when the
matter is a **civil** case in the **Wayne County Circuit Court**,
which sits as the **Third Judicial Circuit**. It is the largest
circuit court in Michigan and serves the City of Detroit and the
balance of Wayne County.

## Location and divisions

- The **Civil Division** sits in downtown Detroit at the **Coleman
  A. Young Municipal Center** (2 Woodward Avenue); some civil
  operations and the clerk's office have historically used the
  **Penobscot Building**. Confirm the current civil-filing address
  with the clerk before a paper filing.
- The Third Circuit is organized into separate **Civil**,
  **Family**, and **Criminal** divisions. This skill covers the
  **Civil Division** only. Family-law matters route to the Family
  Division — use `mi-family-court` / `mi-family-law`. Criminal
  matters are out of scope.

## General civil jurisdiction

As a circuit court, the Third Circuit Civil Division hears civil
actions where the **amount in controversy exceeds $25,000**, plus
equitable claims and other matters within circuit jurisdiction.
Civil claims at or below $25,000 generally belong in district
court — in Detroit, the **36th District Court** (see
`mi-36th-district`). Confirm the jurisdictional fit before filing;
a misfiled case can be dismissed or transferred.

## Wayne County case-type codes

A Wayne County civil case number embeds a **case-type code** —
the two- or three-letter suffix on the case number that signals
the SCAO case category and routes the case for assignment. Common
civil families (confirm the controlling code with the clerk for
your specific claim):

| Code | General category |
|------|------------------|
| **CB** | Business claims — Michigan Business Court (MCL 600.8035) |
| **CZ** | General civil — catch-all for civil actions not otherwise coded |
| **NO** | Other personal injury / negligence |
| **NF** | Automobile no-fault / negligence (confirm current usage) |
| **NZ** | Other negligence civil family (confirm current usage) |

> The **CB** ("business claims") and core **C**/**N** civil codes
> are the statewide SCAO categories applied in Wayne County. The
> exact code for a given claim type — and any local sub-coding —
> should be **confirmed against the current SCAO case-type-code
> list and the Wayne County clerk's intake practice**; treat the
> `NF` / `NZ` rows above as families to verify, not as fixed.

## Michigan Business Court (CB cases)

Michigan circuit courts with sufficient caseload operate a
**Business Court** under **MCL 600.8031 et seq.**; the Third
Circuit's business docket began **July 1, 2013**.

- A matter qualifies as a **business or commercial dispute** under
  MCL 600.8031 when the amount in controversy is **$25,000 or
  more** *or* equitable/declaratory relief is sought, and the
  dispute fits the statutory definition (disputes among business
  enterprises and their owners/managers/shareholders; sale,
  merger, governance, dissolution, or finances of a business
  enterprise; and related categories under MCL 600.8031(3)).
- **Personal-injury, wrongful-death, malpractice, and
  individual-claimant product-liability** actions are expressly
  **excluded** from the business court.
- Under MCL 600.8035, an action that includes a qualifying
  business or commercial dispute **must** be assigned to the
  business court and maintained there even if it also pleads
  non-business claims.
- In the Third Circuit, business-court cases carry the **CB**
  code, **must be e-filed**, and are assigned to the sitting
  business-court judges (historically by blind draw). Confirm the
  current designation/assignment procedure in the Third Circuit's
  business-court administrative order. For substantive
  commercial-dispute drafting, see `mi-commercial-disputes`.

## Motion practice — the praecipe

Motions in the Third Circuit Civil Division are placed on a
judge's **motion docket** by filing a **praecipe** (the
"Request for Hearing on a Motion" — the local scheduling form),
in addition to the motion and notice of hearing:

- The praecipe is filed to obtain a **motion day / hearing date**
  before the assigned judge; the **general civil** praecipe is the
  white form (domestic-relations matters use a separate form).
- The praecipe must generally be filed a **set number of days
  before the hearing** (commonly reported as at least **7 days**
  ahead) — **confirm the current advance-filing interval and the
  assigned judge's motion-day schedule** in the local rules and
  the judge's practice guidelines, because motion-day mechanics
  and notice periods vary by judge and change over time.
- Service and notice of the motion run under the Michigan Court
  Rules (MCR 2.119 motion practice; MCR 2.107 service) — see
  `mi-statewide-format` and `mi-draft-motion` / `mi-draft-note`.

## E-filing — MiFILE / TrueFiling

The Third Circuit participates in Michigan's statewide
**MiFILE / MiCOURT TrueFiling** e-filing system. E-filing is
**mandatory for business-court (CB) cases** and is the default
channel for most civil filings; confirm whether your document
type and party status require e-filing or permit paper, and
confirm the correct document-type selection at upload. See
`mi-file-packet`.

## Composition

- For statewide format and the Michigan caption:
  `mi-statewide-format`
- For the first responsive pleading: `mi-first-30-days`
- For drafting motions / notices / orders / declarations:
  `mi-draft-motion`, `mi-draft-note`, `mi-draft-order`,
  `mi-draft-declaration`
- For computing deadlines: `mi-deadlines`
- For scheduling a hearing (praecipe / motion day):
  `mi-schedule-hearing`, `mi-hearings`
- For assembling and e-filing a packet: `mi-file-packet`
- For business / commercial substance: `mi-commercial-disputes`
- For Detroit district-court (≤ $25,000) matters:
  `mi-36th-district`
- For other circuits: `mi-oakland`, `mi-circuit-courts`
- For pro se conventions: `mi-pro-se`

## References

- `mi-law-references` — MCR, MRE, and Michigan citation corpus
- Third Judicial Circuit local administrative orders and the
  Business Court plan (3rdcc.org)
- SCAO case-type-code list (courts.michigan.gov) for confirming
  the controlling civil case code
