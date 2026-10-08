---
name: mi-36th-district-codearranger
title: 36th District Court (Detroit)
description: This skill should be used when a Michigan civil case is in the 36th District Court in Detroit — the state's highest-volume district court and the primary consumer-debt and eviction forum. Triggers include "36th District Court", "Detroit district court", "Detroit eviction court", "Detroit small claims", "debt collection lawsuit Detroit", "landlord tenant 36th district", "sued in Detroit district court", "36th District Court summary proceedings", and "421 Madison Detroit court". Covers the district court's limited civil money jurisdiction, the landlord-tenant / summary-proceedings docket under MCL 600.5701 et seq. and MCR 4.201, small claims under MCR 4.301 et seq., general civil practice under the MCR 2.xxx rules as modified for district court, how cases are commenced and noticed, MiFILE/MiCOURT e-filing, and the high default-judgment volume in consumer-debt cases. Layer on top of `mi-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-36th-district
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# 36th District Court (Detroit)

> **NOT LEGAL ADVICE.** Drafting and filing guidance only. District
> court deadlines — especially in summary proceedings — are short and
> unforgiving. Verify every date and every local-rule requirement
> against the current Michigan Court Rules and the court's own
> administrative orders before acting.

Use this skill in addition to `mi-statewide-format` whenever a civil
case is in the **36th District Court**, located at **421 Madison
Street, Detroit, MI 48226**. It is the **largest district court in
Michigan and one of the busiest courts in the United States** — and
the **dominant consumer-debt and eviction forum** in the state: high
volume, short summary-proceedings timelines, and a very large
default-judgment docket.

## What kind of court this is

Michigan **district courts** are limited-jurisdiction trial courts.
General civil practice runs under the **MCR 2.xxx** rules as modified
for district court, while three specialized civil tracks are governed
by their own rules:

- **General civil** — money claims up to the district-court civil
  jurisdiction cap. Above the cap, the matter belongs in Circuit
  Court (in Detroit, the Wayne County / Third Circuit — see
  `mi-wayne`). **Confirm the current cap in the corpus** before
  relying on it.
- **Landlord-tenant / summary proceedings** — recovery of possession
  under **MCL 600.5701 et seq.** and **MCR 4.201** (see below).
- **Small claims** — informal, no-lawyer, no-appeal track under
  **MCR 4.301 et seq.** and **MCL 600.8401 et seq.** (see below).

## Divisions

The 36th District Court is organized into functional divisions:

- **Civil Division** — general civil and landlord-tenant matters.
- **Small Claims Division** — small-value disputes (in-person
  proceedings; confirm the current courtroom/calendar with the
  clerk).
- **Traffic Division** and **Criminal Division** — out of scope for
  this civil-drafting skill.
- **Collections / Enforcement** — post-judgment collection and
  garnishment processing.

## Commencing and noticing a case

- A general civil action is commenced by filing a **complaint** with
  the clerk, who issues a **summons**; the plaintiff serves the
  summons and complaint under the MCR 2.105 service rules. Use
  `mi-statewide-format` for the caption, numbered paragraphs, the
  P-number signature block, and the proof of service.
- A **summary proceeding** is commenced by a **complaint to recover
  possession** preceded by the statutorily required **demand /
  notice** (e.g., notice to quit / demand for possession) — see the
  landlord-tenant section below.
- A **small-claims** matter is commenced on an **SCAO affidavit and
  claim** form, not a formal Rule 2.113 pleading.

## Landlord-tenant / summary proceedings — the eviction docket

Summary proceedings to recover possession are the 36th District
Court's highest-volume civil docket. Key mechanics:

- **Governing law: MCL 600.5701 et seq.** (summary proceedings) and
  **MCR 4.201** (procedure). The matter is filed in the Civil
  Division.
- **Pre-suit notice is a prerequisite.** The landlord must serve the
  correct **demand for possession / notice to quit** (the type and
  notice period depend on the ground — nonpayment, termination,
  health/safety, etc.) before filing the complaint. A notice defect
  is a common and dispositive defense.
- **Compressed timeline.** Summary proceedings move on a **much
  shorter clock** than ordinary civil cases — short summons-return
  windows and prompt hearing dates. Treat every date as
  jurisdictional and verify it against MCR 4.201 and the court's
  scheduling practice.
- **SCAO mandatory forms** govern the summons, complaint, and
  judgment in summary proceedings; use the current SCAO form set.

For the substantive defense framework — habitability, retaliation,
the Truth in Renting Act, security-deposit issues, notice defects,
and any federal notice overlay where applicable — see
`mi-landlord-tenant`.

## Small claims

- **Governing law: MCR 4.301 et seq.** and **MCL 600.8401 et seq.**
- **Informal, no-attorney, no-jury** track. Parties generally may not
  be represented by counsel, there is **no formal discovery**, and a
  small-claims **judgment is not appealable** (a party who wants the
  right to appeal or to be represented must instead remove the case
  to the general civil docket before trial — confirm the current
  removal mechanics).
- **Monetary cap is statutory and periodically adjusted for
  inflation.** **Do not assume a fixed dollar figure — confirm the
  current small-claims cap in the corpus** (`mi-law-references`)
  before advising on forum choice.

## Consumer-debt and the default-judgment docket

The 36th District Court processes an enormous volume of
**consumer-debt collection** suits, and a large share resolve by
**default judgment** when the defendant does not appear. That makes
the consumer-protection posture important:

- A defendant who is served must **respond by the deadline** to avoid
  a default; once a default judgment enters, relief runs through the
  post-judgment / set-aside rules (see `mi-post-judgment`).
- Debt-buyer plaintiffs must be able to prove **standing / chain of
  title** and the **business-records foundation** (MRE 803(6) /
  902(11)) for the account documents — frequently weak points in a
  high-volume docket.
- Federal and Michigan collection-practice law (FDCPA, Regulation F,
  and the Michigan collection statutes) supply both defenses and
  affirmative claims.

See `mi-consumer-debt` for the full debt-defense framework (FDCPA,
Reg F, the Michigan consumer-protection and collection-agency
regimes, statutes of limitation, and chain-of-title challenges) and
`mi-first-30-days` for answering and avoiding default.

## E-filing (MiFILE / MiCOURT)

Michigan's statewide electronic-filing system is **MiFILE** (the
MiCOURT TrueFiling platform). The 36th District Court accepts
electronic filing through the state system; certain post-judgment
collection items (e.g., garnishments) route through dedicated
electronic workflows. Confirm the current filing channel, document
types, and any fee with the clerk and the court's website before
filing — see `mi-file-packet` for packet assembly and preflight.

## Caption / court identifier

For documents filed in this court, use the district-court identifier
line in the caption:

```
   STATE OF MICHIGAN
   IN THE 36TH DISTRICT COURT
```

Follow the caption fields, numbered-paragraph form, P-number
signature block, and proof-of-service conventions in
`mi-statewide-format`. Use the current **SCAO mandatory forms** for
summary proceedings and small claims rather than free-form pleadings.

## Composition

- For statewide format and the caption: `mi-statewide-format`
- For consumer-debt defense: `mi-consumer-debt`
- For eviction / summary-proceedings defense: `mi-landlord-tenant`
- For answering and avoiding default in the first 30 days:
  `mi-first-30-days`
- For default set-aside and post-judgment relief: `mi-post-judgment`
- For deadline computation: `mi-deadlines`
- For pro se conventions: `mi-pro-se`
- For e-filing packet assembly: `mi-file-packet`
- For other Michigan district courts: `mi-district-courts`
- For the companion Wayne County Circuit Court (over-cap matters):
  `mi-wayne`

## References

- `mi-law-references` — Michigan Court Rules (incl. MCR 2.xxx,
  MCR 4.201 summary proceedings, MCR 4.301 et seq. small claims),
  MCL 600.5701 et seq. (summary proceedings), MCL 600.8401 et seq.
  (small claims, including the current monetary cap), the MRE
  business-records / self-authentication rules, and the
  federal-debt-laws corpus
