---
name: lis-pendens
title: Lis Pendens (Notice of Pending Action)
description: 'Drafts a U.S. Lis Pendens (Notice of Pending Action) for recording against real property. Covers intake, statutory authority mapping, legal description, verification, and proof of service. Use when preparing a lis pendens, notice of pending action, or recording notice tied to title or possession claims. Trigger: lis pendens, notice of pending action, quiet title, specific performance, foreclosure, partition, lien enforcement, expungement.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/lis-pendens
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
---

# Lis Pendens (Notice of Pending Action)

Drafts a recordable notice providing constructive notice of pending litigation affecting title or right to possession of real property.

## Prerequisites

1. **Jurisdiction + county recorder** — state, county, local recorder formatting rules.
2. **Filed pleading** — operative complaint asserting a qualifying real property claim.
3. **Case metadata** — court name, division, case number, filing date, party names.
4. **Property records** — deed/title report with full legal description and APN/tax ID.

## Quick Start

Complete the intake table before drafting. Every field is required.

| Field | Value | Source |
|---|---|---|
| State + County | | |
| Court (full name) | | |
| Division/Dept | | |
| Case Number | | |
| Filing Date | | |
| Plaintiff(s) (exact) | | |
| Defendant(s) (exact) | | |
| Property Address | | |
| Legal Description | | |
| APN / Tax ID | | |
| Recorder Formatting Rules | | |
| Service Requirements | | |

## Core Workflow

### 1. Map Statutes and Rules

Fill each row, then cite in the document. Mark unverified entries `[VERIFY]`.

| Topic | Requirement | Citation |
|---|---|---|
| Statutory authority | | [VERIFY] |
| Real property claim definition | | [VERIFY] |
| Mandatory warning language | | [VERIFY] |
| Verification format | | [VERIFY] |
| Attorney certification | | [VERIFY] |
| Service timing/method | | [VERIFY] |
| Recorder formatting | | [VERIFY] |

### 2. Draft the Document

Adapt the template below to local format.

```text
[Recording Requested By:]
[When Recorded Mail To:]
[Space for Recorder's Stamp per county rules]

Attorney Name (Bar No.)
Law Firm
Address
Phone | Email | Fax (if required)
Attorney for [Plaintiff/Party]

[COURT CAPTION EXACTLY AS FILED]

NOTICE OF PENDING ACTION (LIS PENDENS)

1. Parties. [Plaintiff(s)] filed this action against [Defendant(s)].
2. Court and Case. This action is pending in [Court], Case No. [###], filed [Date].
3. Property.
   a. Street Address: [Address]
   b. Legal Description: [Full legal description]
   c. APN/Tax ID: [APN]
4. Real Property Claim. The action includes claims for [quiet title / specific performance / foreclosure / partition / lien enforcement / other], affecting title to or right to possession of the Property.
5. Relief Affecting Property. Plaintiff seeks [specific relief].
6. Statutory Authority. This Notice is recorded pursuant to [citation] [VERIFY].
7. Mandatory Notice. [Statutory warning language verbatim] [VERIFY].

Dated: [Date]                    __________________________
                                 [Attorney Name]
                                 Attorney for [Party]

VERIFICATION / DECLARATION
I, [Name], declare under penalty of perjury under the laws of [State] that the facts stated in the foregoing Notice of Pending Action are true and correct of my own knowledge, except as to matters stated on information and belief, and as to those matters I believe them to be true.

Executed on [Date] at [City, State].
__________________________
[Signature / Printed Name / Title]

[ATTORNEY CERTIFICATION (if required)]
I certify that the real property claim has probable validity under [statute] [VERIFY].
__________________________
[Attorney Signature]

[PROOF OF SERVICE (if required)]
Served on parties as follows: [method, date, address/service list].
__________________________
[Server Signature]
```

### 3. Verify Before Finalizing

```
- [ ] Caption matches court's required format
- [ ] Party names match operative complaint exactly
- [ ] Case number and filing date accurate
- [ ] Legal description + APN from deed/title report (not street address alone)
- [ ] Multiple parcels each have own legal description + APN
- [ ] Claim summary ties relief directly to title/possession
- [ ] Statutory authority cited
- [ ] Mandatory warning language included verbatim
- [ ] Verification/declaration properly completed
- [ ] Attorney certification included if required
- [ ] Proof of service prepared if required
- [ ] Recorder margins, font size, stamp-space rules met
```

### 4. Attorney Attention Notes

Append to every draft:

- Missing source data: [list]
- Unverified statutes/rules: [list with `[VERIFY]`]
- Potential issues: [e.g., non-qualifying claim, inadequate property description, service deadline risk]
- Recorder formatting risks: [list]

## Common Pitfalls

- **Non-qualifying claim** — only record for claims affecting title or possession; purely monetary claims do not support lis pendens.
- **Street address only** — always use verbatim legal description from deed/title report.
- **Party name mismatch** — names must match the operative complaint exactly.
- **Missing statutory warnings** — some states require verbatim warning language; omission risks expungement.
- **Service deadlines** — late or missing service can void the notice; confirm statutory timeframes.
- **Recorder formatting** — county-specific margin, font, and stamp-space rules vary; confirm before recording.
- **Expungement exposure** — flag jurisdiction-specific probable validity requirements early.
