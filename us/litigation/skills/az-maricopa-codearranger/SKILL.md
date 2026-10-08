---
name: az-maricopa-codearranger
title: Superior Court of Arizona in Maricopa County (Phoenix)
description: This skill should be used when drafting or filing civil documents in the Superior Court of Arizona in Maricopa County — the largest trial court in Arizona, sitting in Phoenix. Triggers include "Maricopa County Superior Court", "file in Maricopa County", "Phoenix superior court", "Maricopa Commercial Court", "Maricopa compulsory arbitration", "Maricopa local rules", "Central Court Building Phoenix", "AZTurboCourt Maricopa", "sued in Maricopa County", and "Maricopa County civil case number". Covers the downtown and regional court facilities, general civil jurisdiction, the Local Rules of Practice for the Superior Court in Maricopa County, the compulsory-arbitration jurisdictional limit set by local rule, the Commercial Court specialty calendar, complex-case assignment, AZTurboCourt e-filing, and Maricopa case-type / case-number conventions. Layer on top of `az-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-maricopa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Superior Court of Arizona in Maricopa County (Phoenix)

> **NOT LEGAL ADVICE.** These notes describe the venue's
> procedural mechanics as a drafting aid, not legal advice. Local
> rules, administrative orders, and judge-specific practices
> change; verify with the clerk and the current Maricopa County
> local rules before relying on anything here.

Use this skill in addition to `az-statewide-format` when the
matter is a **civil** case in the **Superior Court of Arizona in
Maricopa County**, the state's largest court by caseload, serving
Phoenix and the balance of Maricopa County.

## Facilities

Maricopa County Superior Court is multi-campus. The downtown
Phoenix complex and several regional centers host civil
operations:

- **Central Court Building (CCB)** and the **East Court Building
  (ECB)** — the downtown Phoenix civil complex; the Clerk of the
  Superior Court's central filing counter and the bulk of civil
  judicial officers sit here.
- **Old Courthouse** — the historic downtown building used for
  certain calendars and ceremonial proceedings.
- **Northeast Regional Court Center** (northeast Phoenix area) and
  **Southeast Regional Court Center** (Mesa / east-valley area) —
  regional facilities that hear civil and family matters.
- **Northwest Regional Court Center** — Surprise (west-valley
  area).

Confirm the current building, civil-filing counter, and the
calendar assigned to your case with the Clerk of the Superior
Court before any in-person filing or appearance; facility
assignments and hours change.

## General civil jurisdiction

The Superior Court is Arizona's court of **general jurisdiction**
and hears civil actions without a statutory amount-in-controversy
ceiling, plus equitable claims and other matters within superior
court jurisdiction. Lower-value money claims and many
landlord-tenant and small-claims matters belong in the **Justice
Courts** — see `az-justice-courts`. Confirm the jurisdictional and
venue fit before filing; a misfiled case can be transferred or
dismissed.

## Local rules

Practice in this court is governed by the statewide **Arizona
Rules of Civil Procedure** as supplemented by the **Local Rules of
Practice for the Superior Court in Maricopa County** and the
court's standing **administrative orders**. The local rules
address civil case management, the compulsory-arbitration program,
complex-case designation, and motion and calendar practice.

Do not hard-code rule numbers or dollar thresholds from memory —
the local-rule provisions cited below are pointers; **verify the
controlling rule number, current threshold, and any amendment
against the corpus** (`az-law-references`) and the court's
published local rules before relying on them.

## Compulsory arbitration

Maricopa County operates a **compulsory (court-annexed)
arbitration** program under its local rules and the statewide
arbitration provisions of the Arizona Rules of Civil Procedure. A
civil money case at or below the **local jurisdictional limit**
(in which no party seeks affirmative relief other than a money
judgment) is routed to a court-appointed arbitrator rather than
tried to the assigned judge in the first instance.

- The complaint is generally accompanied by the **Certificate on
  Compulsory Arbitration** required by Ariz. R. Civ. P. 72(e),
  stating whether the controversy is at or below the arbitration
  limit. A case seeking an award above the limit is certified
  **not** subject to arbitration.
- A party dissatisfied with the arbitrator's award may **appeal
  for a trial de novo** before the assigned judge within the
  time set by rule.
- The **arbitration jurisdictional dollar limit, the certificate
  requirement, and the appeal deadline are set by the local rule
  and the Rules of Civil Procedure — confirm the current figures
  against `az-law-references`** rather than treating any number
  here as fixed. (Maricopa's limit has historically been at the
  higher end among Arizona counties; verify the controlling
  amount.)

## Commercial Court

Maricopa County operates a **Commercial Court** — a specialty
civil calendar created as an Arizona Supreme Court pilot in 2015
and made a **permanent feature of the Civil Department effective
January 1, 2019** — to manage commercial and business disputes
expeditiously before a small group of designated judges.

- Eligibility turns on the **nature of the dispute** (commercial
  and business controversies — among business entities and their
  owners, governance, transactions, and related categories), as
  defined by the controlling administrative order; confirm the
  current eligibility definition and any opt-in / assignment
  mechanics in that order.
- Commercial Court cases filed in the **Northeast and Southeast**
  regional facilities are assigned to one of the designated
  Commercial Court judges (who sit downtown). Confirm the current
  assignment procedure with the clerk.
- For substantive commercial-dispute drafting, see
  `az-commercial-disputes`.

Distinct from Commercial Court, the local rules also allow a case
to be designated **complex** (continuous judicial management) on a
party's request granted by the judge or on the judge's own motion,
with reassignment to a Complex Case judge. Confirm the current
complex-designation rule and procedure in the local rules.

## E-filing — AZTurboCourt / eFileAZ

Electronic filing in Maricopa County civil cases runs through the
statewide **AZTurboCourt / eFileAZ** system. E-filing is the
default channel for represented parties and most civil document
types; confirm whether your document type and party status require
e-filing or permit paper or counter filing, and confirm the
correct document-type / case-category selection at upload. See
`az-file-packet`.

## Case-type and case-number conventions

A Maricopa County civil case number embeds a **case-type
designator** that signals the case category. Civil actions
generally carry the **"CV"** prefix (e.g., `CV2026-#######`).
Family, probate, and other departments use different prefixes.
Confirm the controlling designator and any local sub-coding for
your specific claim with the Clerk of the Superior Court, and
select the matching case category at e-filing intake.

## Composition

- For statewide format and the Arizona caption:
  `az-statewide-format`
- For the first responsive pleading: `az-first-30-days`
- For drafting motions / notices / orders / declarations:
  `az-draft-motion`, `az-draft-note`, `az-draft-order`,
  `az-draft-declaration`
- For computing deadlines: `az-deadlines`
- For scheduling a hearing: `az-schedule-hearing`, `az-hearings`
- For assembling and e-filing a packet: `az-file-packet`
- For discovery: `az-discovery`
- For commercial / business substance: `az-commercial-disputes`
- For lower-value money, eviction, and small-claims matters:
  `az-justice-courts`
- For other counties: `az-pima`, `az-superior-courts`
- For pro se conventions: `az-pro-se`

## References

- `az-law-references` — Arizona Rules of Civil Procedure,
  evidence, citation, fees, and local-rules corpus (the canonical
  home for the compulsory-arbitration limit and the Maricopa
  local-rule text)
- Local Rules of Practice for the Superior Court in Maricopa
  County and the court's administrative orders
  (superiorcourt.maricopa.gov)
- Arizona Judicial Branch (azcourts.gov) for the statewide
  AZTurboCourt / eFileAZ system and the statewide arbitration
  rule
