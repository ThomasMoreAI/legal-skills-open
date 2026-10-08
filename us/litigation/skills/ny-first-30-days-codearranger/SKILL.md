---
name: ny-first-30-days-codearranger
title: First 30 Days — After Service in a New York Civil Case
description: Use when a New York defendant has just been served with a civil complaint. Triggers include 'just got served in New York', 'NY summons and complaint', 'CPLR 3012 answer deadline', '20 days to answer', '30 days to answer New York', 'CPLR 3211 motion to dismiss', 'pre-answer motion in NY', 'CPLR 3018 affirmative defenses', 'compulsory counterclaims NY', 'failure to state a cause of action', 'lack of personal jurisdiction in New York', 'how do I answer a NY complaint pro se', 'extension to answer stipulation NY'. Covers the CPLR 3012 answer deadlines (20 days for personal service in-state; 30 days for substituted service / out-of-state service / "leave and mail" complete 10 days after filing), the CPLR 3211 motion-to-dismiss grounds, CPLR 3018 affirmative defenses, CPLR 3019 counterclaims, and the New York consumer-credit pleading threshold under CPLR 3015(e) (CCFA 2022).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-first-30-days
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# First 30 Days — After Service in a New York Civil Case

> **NOT LEGAL ADVICE.** Missing the answer deadline can
> cause a default judgment under CPLR 3215. Compute the
> deadline carefully (see `ny-deadlines`).

## Answer deadlines — CPLR 3012

| Mode of service | Deadline |
|-----------------|---------|
| Personal delivery in-state (CPLR 308(1)) | **20 days** from service |
| Substituted "leave and mail" (CPLR 308(2)) | **30 days** from service being complete (service complete 10 days after filing affidavit of service) |
| "Nail and mail" (CPLR 308(4)) | **30 days** from service being complete |
| Personal service out-of-state | **30 days** from delivery |
| Service by publication (CPLR 308(5)) | **30 days** from publication complete |
| Service on Secretary of State (corporation, CPLR 311) | **30 days** from Secretary's mailing |

**Important**: under CPLR 308(2)/(4), service is **complete
10 days after** the affidavit of service is filed. The
answer clock runs from completion, not from the date
delivery was attempted. So substituted service has a built-in
40-day buffer (10 + 30) before the answer is due.

## Pre-answer motion to dismiss — CPLR 3211

Instead of answering, a defendant can file a pre-answer
motion to dismiss. Grounds under **CPLR 3211(a)**:

| Sub | Ground |
|-----|--------|
| (1) | A defense founded upon documentary evidence |
| (2) | Court has no subject-matter jurisdiction |
| (3) | Party lacks legal capacity to sue |
| (4) | There is another action pending between the same parties |
| (5) | Cause of action may not be maintained because of arbitration / collateral estoppel / discharge / infancy / payment / release / res judicata / statute of limitations / statute of frauds |
| (6) | Court lacks jurisdiction over a counterclaim |
| (7) | Pleading fails to state a cause of action |
| (8) | Court has no personal jurisdiction over the defendant |
| (9) | Court has no jurisdiction in cases involving the State |
| (10) | Court should not proceed in the absence of a person who should be a party |
| (11) | Subject of the action is property which has been distributed by a receiver / fiduciary |

**CPLR 3211(e)** is the consolidation rule: most CPLR 3211
defenses **must be raised in the first responsive paper** or
they are waived (especially (a)(1), (4), (5), (8) personal
jurisdiction). (a)(2) and (a)(7) can be raised at any time.

Filing a CPLR 3211 motion **extends the answer deadline**
until 10 days after service of the order deciding the motion
(CPLR 3211(f)).

## Common defenses by case type

### Consumer-debt complaint (most common pro se case)

- **CPLR 3211(a)(5) — Statute of Limitations**: Post-CCFA
  (2022), credit-card and other consumer-credit debts have a
  **3-year SOL** under CPLR 213(a). For older debt-buyer
  complaints, this is often the strongest defense.
- **CPLR 3211(a)(7) — Failure to state a cause of action**:
  Post-CCFA, the complaint must comply with CPLR 3015(e) —
  identifying the original creditor, chain of title, account
  number, default date, and amount as of charge-off.
  Non-compliance is fatal.
- **CPLR 3211(a)(8) — Lack of personal jurisdiction**: If
  service was defective (e.g., never received the summons),
  raise here.
- **CPLR 3211(a)(3) — Capacity**: Some debt buyers lack
  capacity if not registered/licensed where required (NY
  Gen. Bus. Law § 600).

### Tort complaint (PI, defamation)

- **CPLR 3211(a)(5) — Statute of Limitations**: PI 3 years
  (CPLR 214(5)); defamation 1 year (CPLR 215(3))
- **CPLR 3211(a)(7)**: failure to state a cause of action

### Foreclosure complaint

- **CPLR 3211(a)(3)**: standing (plaintiff must hold note
  and mortgage at commencement — see *Aurora Loan Services
  v. Taylor*, 25 NY3d 355 (2015))
- **CPLR 3408**: triggers mandatory foreclosure-settlement
  conference

## Answer mechanics — CPLR 3018

If answering rather than moving to dismiss, the answer must:

1. **Admit or deny each allegation** (CPLR 3018(a))
2. **Set forth affirmative defenses** (CPLR 3018(b)) — must
   be specifically pleaded; common: SOL, payment, release,
   accord-and-satisfaction, license, illegality, fraud,
   contributory negligence
3. **Plead counterclaims** as the answer (CPLR 3019(a))
4. **Verify** if the complaint was verified (CPLR 3020(a))

## Counterclaims — CPLR 3019

NY does not have a strict compulsory-counterclaim rule. CPLR
3019 says counterclaims **may** be asserted; the consequence
of not asserting is res judicata only as to claims actually
litigated. But waiting can be procedurally costly.

In consumer-debt defense: assert **FDCPA, GBL § 349, GBL §
600 violations** as counterclaims (see `ny-consumer-debt`).

## Extension stipulation

CPLR 2104 allows the parties to stipulate to an extension.
Typical practice: a 20-day or 30-day extension by emailed
stipulation (signed by both sides). File via NYSCEF as
"Stipulation Extending Time to Answer." No court approval
required if filed before the original deadline.

## Triage checklist

For a newly served defendant:

1. **Calendar the answer deadline** (`ny-deadlines`)
2. **Verify service was proper** (CPLR 308 — is the
   affidavit of service correct?)
3. **Run an SOL check** — was the debt charged off more
   than 3 years ago (CPLR 213(a)) for consumer credit?
4. **CCFA compliance check** — does the complaint identify
   the original creditor, chain of title, account number,
   default date (CPLR 3015(e))?
5. **Choose path**: CPLR 3211 motion / verified answer with
   affirmative defenses + counterclaims / extension
   stipulation if more time needed
6. **Draft via** `ny-draft-motion` or write an answer using
   the pro-se drafting framework

## Composition with other ny- skills

- `ny-statewide-format` — format for the answer / motion
- `ny-deadlines` — answer-deadline computation
- `ny-draft-motion` + `ny-draft-declaration` — scaffolders
- `ny-consumer-debt` — substantive defenses + counterclaims
- `ny-landlord-tenant` — RPAPL 7-day answer in summary
  proceedings (a different deadline structure)
- `ny-fact-check` — pre-filing QC
