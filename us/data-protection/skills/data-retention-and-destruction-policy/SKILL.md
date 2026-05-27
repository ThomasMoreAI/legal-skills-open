---
name: data-retention-and-destruction-policy
title: Data Retention and Destruction Policy
description: Drafts a law firm Data Retention and Destruction Policy covering practice-area retention schedules, secure destruction procedures, legal hold protocols, and compliance infrastructure. Trigger when establishing or updating records management frameworks, drafting retention schedules by matter type, or implementing secure destruction procedures for paper and electronic records.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/data-retention-and-destruction-policy
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: data-protection
language: en
tags: [drafting, memo, regulatory]
---

# Data Retention and Destruction Policy

Generates a firm-wide records management policy governing client file lifecycles, retention periods by practice area, secure destruction methods, legal holds, and audit requirements.

## Prerequisites

- Firm profile — practice areas, office locations, jurisdictions
- Current systems — DMS, cloud storage, email, backup infrastructure
- State bar rules — jurisdiction-specific ethics rules on client files
- Existing policies — information security, conflicts, client intake
- Vendors — certified document destruction services in use

## Quick Start

1. Gather firm profile and current systems inventory
2. Map applicable regulatory authorities to practice areas
3. Draft retention schedule by record category
4. Define destruction procedures (paper + electronic)
5. Establish legal hold protocol
6. Assign roles and build audit/training infrastructure

## Workflow

### 1. Regulatory Framework

Cite applicable authorities in the policy introduction:

| Authority | Applicability |
|---|---|
| ABA Model Rules 1.6, 1.15 | Confidentiality; safekeeping client property |
| State ethics rules | Jurisdiction-specific mandates (controls where more stringent) |
| Sarbanes-Oxley | Securities-related matters |
| HIPAA | Health law practices |
| IRS / IRC § 6001 | Tax work; 7-year documentation standard |

### 2. Scope

**Covered:** Client matter files, financial records (trust ledgers, billing), intake records (conflict databases, engagement letters), electronic records (email, cloud, mobile, backups), third-party collaboration platforms.

**Excluded:** Original client-owned documents (wills, deeds, certificates) — return on matter close; destruction requires written client authorization. Transitory communications (scheduling, duplicates) — delete promptly.

**Bound parties:** All firm personnel and third-party providers under confidentiality agreements.

### 3. Retention Schedule

| Record Category | Minimum Retention | Basis |
|---|---|---|
| General litigation / transactional | 6 yrs post-close | Malpractice SOL + margin |
| Estate planning | Permanent or client death + admin + SOL | Latent claim risk |
| Real estate | 7–10 yrs post-close | Title / environmental latency |
| Corporate formation / governance | Entity life + 7 yrs post-dissolution | Ongoing relevance |
| Tax preparation | 7 yrs post-filing | IRS extended audit period |
| Trust account records | 6 yrs or state bar rule (whichever longer) | Ethics rules |
| Firm accounting | 7 yrs | Tax audit exposure |
| Conflict / intake records | Duration of firm operation | Ongoing screening |
| Destruction logs | 3 yrs | Compliance evidence |

> **Legal Hold Override:** Schedules suspend immediately upon reasonable anticipation of litigation, investigation, or bar proceedings. Require written hold notice (scope, reason, responsible personnel). Retention restarts from hold release, not original close.

### 4. Destruction Procedures

**Paper:** Cross-cut shredding ≥ DIN 66399 P-4. On-site or certified vendor with chain-of-custody and destruction certificates. No regular trash or unsecured recycling.

**Electronic:**

| Sensitivity | Method |
|---|---|
| Standard | Cryptographic erasure / multi-pass overwrite (NIST SP 800-88) |
| Highly sensitive | Degaussing (magnetic) or physical destruction |
| SSDs / flash | Cryptographic erasure or physical destruction (overwrite unreliable) |

OS deletion / recycle-bin emptying is **not** sufficient.

**Scope:** Local workstations, servers, cloud, email, mobile, all backup generations, removable media.

**Device retirement:** Full sanitization or physical destruction before any device leaves firm control. Factory reset is insufficient.

**Client notification:** Written notice when matter eligible for destruction → reasonable retrieval period → document authorization or non-response.

**Destruction log fields:** Date, record description/matter ID, method used, personnel who performed/supervised.

### 5. Roles

| Role | Duties |
|---|---|
| Records Management Officer | Policy admin, exception auth, hold coordination, audit oversight |
| Supervising Attorneys | Annual file review, retention auth, hold initiation |
| IT | Automated retention flags, secure deletion, backup compliance |
| Admin Staff | Physical destruction, log maintenance, client notifications |

### 6. Training

- **New hire:** Policy overview, confidentiality, records handling, non-compliance consequences
- **Annual refresher:** Updates, audit findings, best practices
- **Records staff:** Technical destruction methods, hold procedures
- All training documented with signed acknowledgments

### 7. Auditing

**Annual audit:** Sample closed files for timely destruction, verify log completeness, attempt recovery on destroyed electronic records, review hold documentation.

**Quarterly hold review:** Confirm trigger still active, narrow scope where possible, release promptly on resolution with written notice.

**Vendor oversight (annual):** Review certifications, insurance, security protocols; inspect destruction facilities; require contractual confidentiality, security, and indemnification.

**Incident reporting:** Immediate report to Compliance Officer for violations/breaches. No retaliation. Triggers: root cause investigation, client notification assessment, regulatory reporting, corrective measures.

### 8. Policy Maintenance

- Annual review by Records Management Officer + firm leadership
- Interim review on: statutory/ethics changes, new technology, significant breach
- Amendments communicated within 30 days, incorporated into training
- Maintain version history with effective dates and approval records

## Pitfalls

- **[VERIFY]** State bar trust account minimums (commonly 5–7 yrs; varies by jurisdiction) — state rules control where more stringent
- **[VERIFY]** Malpractice SOL and discovery rule before setting retention floors; adjust if jurisdiction exceeds 6-year baseline
- **No indefinite retention** — holding beyond policy without justification increases breach exposure
- **Metadata** — electronic destruction must cover embedded metadata, not just visible content
- **Cloud/SaaS** — confirm contractual deletion rights; obtain vendor deletion certifications
- **Backups** — must include all generations; omitting backups leaves data recoverable
- **Malpractice carve-out** — allow attorneys to flag closed matters for extended retention with written justification and RMO approval
