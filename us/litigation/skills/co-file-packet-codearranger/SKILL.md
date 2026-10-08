---
name: co-file-packet-codearranger
title: Assemble a Colorado Court Filing Packet
description: This skill should be used when assembling and filing a complete Colorado court motion or pleading packet. Triggers include "file a Colorado packet", "assemble my filing for Colorado courts", "Colorado Courts E-Filing", "CCEFS filing", "what documents do I need to file with my Colorado motion", "Colorado filing checklist", "filing fee Colorado". Walks through the assembly of the multi- document packet (motion + declaration + proposed order + certificate of service), the CCEFS upload workflow with the correct document codes for each component, the filing-fee schedule under C.R.S. art. 32 of title 13, the fee-waiver process under C.R.S. § 13-16-103 using JDF 205/206, and the paper-filing alternative for pro se filers in counties where CCEFS Pro Se is not yet active.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-file-packet
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Assemble a Colorado Court Filing Packet

> **NOT LEGAL ADVICE.** This skill walks through filing mechanics.
> Verify document codes, fees, and pro se acceptance with the filing
> court's clerk before submitting.

Use this skill when ready to **submit** a Colorado court filing
through Colorado Courts E-Filing (CCEFS) or by paper.

## CCEFS — the principal filing channel

**CCEFS (Colorado Courts E-Filing System)** is the statewide
e-filing portal:

**https://www.jbits.courts.state.co.us/efiling/**

CCEFS has two tracks:

- **Attorney track** — mandatory for represented parties in most
  counties (district and county courts both)
- **Pro Se track** — free account; available in most district courts
  and many county courts; not yet universal

To file via CCEFS:

1. Log in with your registered account
2. Search for the case by case number or name
3. Click "File" / "New filing" on the case
4. Select the **document code** for each component (see below)
5. Upload each component as a **separate PDF**
6. Pay any associated filing fee by credit card, or attach JDF
   205/206 for a fee-waiver request
7. Submit; CCEFS will generate a "stamp" PDF showing the date /
   time of acceptance

## Multi-document packet — typical components

A standard Colorado motion packet consists of these separately
filed documents:

| # | Document | CCEFS doc code (common) |
|---|----------|------|
| 1 | Motion | MOT - Motion |
| 2 | Supporting Declaration / Affidavit | DEC - Declaration (or AFF - Affidavit) |
| 3 | Exhibits (attached to the declaration or filed as one packet PDF) | EXH - Exhibit(s) |
| 4 | Proposed Order | PROP - Proposed Order |
| 5 | Certificate of Service | COS - Certificate of Service (often included as last page of the motion rather than separately) |
| (6) | Notice of Hearing — if self-scheduled | NTC - Notice |
| (7) | Certificate of Conferral — included in motion or as separate doc | CRT - Certificate |

CCEFS's document-code menus vary slightly by court division —
choose the closest matching code from the dropdown.

## Filing fees — C.R.S. art. 32 of title 13

Current Colorado filing fees (verify with the clerk for current
amounts):

### District Court — civil

| Filing | Fee | Authority |
|---|---|---|
| New complaint / petition | $235 (Class A — most consumer matters) | C.R.S. § 13-32-101(1)(a) |
| New complaint where amount in controversy > $100,000 | Higher tier per the schedule | C.R.S. § 13-32-101 |
| Answer / response | $192 | C.R.S. § 13-32-101(2) |
| Counterclaim / cross-claim | Sliding scale per damages tier | C.R.S. § 13-32-101 |
| Most motions | No separate filing fee | — |
| Certified copy of order / judgment | $20 per document | C.R.S. § 13-32-104 |
| Jury demand | $190 | C.R.S. § 13-32-102 |

### County Court — civil

| Filing | Fee | Authority |
|---|---|---|
| New complaint, ≤ $1,000 | $35 | C.R.S. § 13-32-101(1)(b)(I) |
| New complaint, $1,001 - $10,000 | $85 | C.R.S. § 13-32-101(1)(b)(II) |
| New complaint, $10,001 - $25,000 | $135 | C.R.S. § 13-32-101(1)(b)(III) |
| Answer | $65 | C.R.S. § 13-32-101(2)(b) |
| FED complaint (eviction) | $85 / $97 | C.R.S. § 13-32-101 |
| Small claims (≤ $7,500) | $31 | C.R.S. § 13-32-103 |

### Domestic Relations (district court)

| Filing | Fee | Authority |
|---|---|---|
| Petition for Dissolution / Legal Separation | $230 | C.R.S. § 13-32-101 |
| Petition for Declaration of Invalidity (annulment) | $230 | |
| Petition for Allocation of Parental Responsibilities | $225 | |
| Response | $116 | |

## Fee waiver — JDF 205 + JDF 206

Pro se filers with limited income should file:

- **JDF 205** — Motion to File without Payment of Filing Fee
- **JDF 206** — Sworn Financial Affidavit Supporting Motion

The court reviews and grants or denies under C.R.S. § 13-16-103.
If granted, the waiver covers filing fees, sheriff's service-of-
process fees, jury fees, and certified-copy fees. Re-apply for
subsequent stages if circumstances change.

Submit JDF 205/206 **with** the first filing — do not pay fees and
later try to get them refunded.

## Service of process — separate from filing

Filing with the court is **not** the same as serving the opposing
party. Two distinct steps:

1. **Filing** — through CCEFS or paper to the clerk
2. **Service of process** (for the initial summons + complaint) — by
   sheriff, private process server, or otherwise per C.R.C.P. 4
3. **Service of pleadings** (for subsequent papers) — through CCEFS
   e-service if both parties are on CCEFS, otherwise by mail, hand
   delivery, or email under C.R.C.P. 5(b)(2)(E)

The **C.R.C.P. 4** initial-service deadline is **63 days** after
the complaint is filed. Missing this triggers Rule 4(m) dismissal.

## Paper-filing alternative

For pro se filers in counties without CCEFS Pro Se, or when paper
filing is necessary (some sealed documents, certified original
records):

1. Print the filing as a clean PDF or paper copy
2. Bring to the **clerk's window** of the district or county court
   during business hours (typically 8 AM - 5 PM weekdays)
3. The clerk file-stamps the original and returns a stamped copy to
   you
4. Pay filing fee at the cashier window
5. Serve opposing parties separately via mail / hand delivery

Some clerk's offices accept **drop-box filings** (drop after hours;
the filing is dated the next business day). Verify with the
specific clerk.

## E-Service through CCEFS

When both parties are registered CCEFS users, e-filing automatically
e-serves the other party via CCEFS notification. The system
generates an electronic service receipt; no separate Certificate of
Service is required for e-served papers, though many practitioners
still include one for redundancy.

When the opposing party is **pro se without a CCEFS account**, the
filer must serve separately by mail, hand delivery, or (with
agreement / court order) email under C.R.C.P. 5(b)(2)(E).

## Pre-filing checklist

| Check | Done |
|-------|------|
| All packet documents drafted and reviewed | ☐ |
| `scripts/format-check.py` passes on each `.docx` | ☐ |
| `co-fact-check` deep audit complete (high-stakes) | ☐ |
| `co-quality-check` pre-filing review complete | ☐ |
| Caption matches across all documents | ☐ |
| Certificate of Conferral included (non-dispositive) | ☐ |
| Proposed Order is separate document | ☐ |
| Each component saved as PDF | ☐ |
| CCEFS account ready / filing fee available / JDF 205/206 ready | ☐ |
| Service plan: e-service automatic or alternate method ready | ☐ |

## Composition

- For statewide format: `co-statewide-format`
- For drafting each component: `co-draft-motion`,
  `co-draft-declaration`, `co-draft-order`, `co-draft-note`
- For pre-filing format/content review: `co-quality-check`,
  `co-fact-check`
- For court-specific filing channels: `co-denver`, `co-arapahoe`,
  `co-county-courts`
- For pro se filers without CCEFS: `co-pro-se`
- For fee waivers: `co-pro-se` (JDF 205/206 mechanics)
- For post-filing scheduling: `co-schedule-hearing`

## References

- `references/ccefs-workflow.md` — full CCEFS upload walkthrough
- `references/document-codes.md` — common CCEFS document codes
- `references/filing-fees.md` — full Colorado fee schedule
- `references/jdf-205-206.md` — fee-waiver instructions and form
  index
- `references/service-vs-filing.md` — the distinction in detail
