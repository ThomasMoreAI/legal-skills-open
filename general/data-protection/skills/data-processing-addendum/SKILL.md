---
name: data-processing-addendum
title: GDPR Data Processing Addendum (DPA)
description: Drafts a GDPR Article 28-compliant Data Processing Addendum (DPA) between data controllers and processors. Extracts party details, processing scope, and service terms from uploaded documents. Produces an execution-ready DPA with all mandatory Art. 28(3) elements and four schedules. Use when supplementing a service agreement with data protection terms, negotiating processor contracts, or establishing GDPR-compliant EU data processing relationships.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/data-processing-addendum
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
tags: [agreement, drafting, regulatory]
---

# GDPR Data Processing Addendum (DPA)

Drafts an Art. 28-compliant DPA as a standalone addendum to an underlying service agreement, covering all mandatory processor obligations and four execution-ready schedules.

## Prerequisites

Extract from uploaded documents before drafting:

1. **Service agreement** — governing law, notice clauses, effective date, termination provisions
2. **Party details** — legal names, addresses, registration numbers, DPO contacts (both parties)
3. **Processing description** — subject matter, duration, nature/purpose, data types, data subject categories; flag Art. 9 special category data explicitly
4. **Sub-processor list** — names, locations, processing activities
5. **Security posture** — certifications (ISO 27001, SOC 2), policies, audit reports
6. **Transfer mechanisms** — SCCs, BCRs, adequacy decisions, or TIAs for EEA transfers

## Quick Start

Produce a numbered, cross-referenced document: recitals, operative provisions (Sections 1–11), signature block, and four schedules (A–D). Draft schedules in parallel with their corresponding sections.

## DPA Sections

### 1 — Parties & Main Agreement

| Element | Requirement |
|---|---|
| Party identification | Full legal name, address, registration number, DPO details |
| Hierarchy | DPA prevails over main agreement on data protection matters |
| Effective date | Specify; note retroactive application if processing already underway |
| Integration | DPA forms integral part of main agreement |

### 2 — Processing Details (→ Schedule B)

- **Subject matter & duration**: Tied to service agreement term; include renewal/termination triggers
- **Nature & purpose**: Enumerate operations (collection, storage, analysis, transmission, deletion); confirm necessity and proportionality
- **Data types**: Distinguish ordinary vs. special category (Art. 9)
- **Data subjects**: Employees, customers, end-users, children (flag Art. 8 if applicable)

### 3 — Processor Instructions (Art. 28(3)(a))

- [ ] Process only on documented controller instructions; initial scope defined by DPA and main agreement
- [ ] Procedure for additional/modified instructions (form, acknowledgment timeframe)
- [ ] Processor notifies controller immediately if any instruction violates GDPR or Member State law
- [ ] Processing beyond instructions for legal obligation: notify controller before processing unless prohibited on public-interest grounds

### 4 — Security (Art. 32) (→ Schedule C)

Schedule C minimum domains:

| Domain | Scope |
|---|---|
| Pseudonymization & encryption | At-rest, in-transit, key management |
| Confidentiality & integrity | Access controls, least-privilege, logging |
| Availability & resilience | Redundancy, DR, RTO/RPO |
| Testing & evaluation | Pen-test cadence, vulnerability management |
| Personnel | Confidentiality obligations for all authorized personnel |

Reference existing certifications (ISO 27001, SOC 2 Type II, TISAX) as baseline evidence.

### 5 — Sub-processors (Art. 28(2), 28(4)) (→ Schedule A)

- [ ] General written authorization (preferred) OR specific per-sub-processor authorization
- [ ] 30-day advance notice for additions/replacements; controller may object on reasonable grounds
- [ ] Objection consequences: processor proposes alternative OR controller may terminate without penalty
- [ ] Sub-processors bound by equivalent obligations (Art. 28(4))
- [ ] Processor fully liable for sub-processor performance

### 6 — Data Subject Rights (Art. 12–23)

- [ ] Processor supports controller responses: access (15), rectification (16), erasure (17), restriction (18), portability (20), objection (21)
- [ ] Direct requests from data subjects: notify controller within **48 hours**; do not respond without documented instruction
- [ ] Cost allocation for resource-intensive requests consistent with main agreement

### 7 — Breach Notification (Art. 33–34)

- [ ] Notify controller **without undue delay, max 24 hours** after awareness (adjust for data sensitivity)
- [ ] Notification must include: nature of breach, approximate affected subjects/records, contact point, likely consequences, mitigation measures
- [ ] Cooperate on investigation, supervisory authority notification (Art. 33/34), data subject communications
- [ ] Preserve all evidence; maintain incident log

### 8 — Compliance Assistance (Art. 32–36)

- [ ] Assist with Art. 32 security obligations and DPIAs (Art. 35)
- [ ] Support prior supervisory authority consultation (Art. 36) where required
- [ ] Provide all information to demonstrate Art. 28 compliance
- [ ] Allow for and contribute to audits (Section 9)

### 9 — Audits & Inspections

| Parameter | Position |
|---|---|
| Notice | 30 days (routine); shorter for cause |
| Frequency | Annual unless cause exists |
| Auditor | Controller team or independent third party (under NDA) |
| Remote audits | Permitted |
| Alternative evidence | Art. 42/40 certification, SOC 2 Type II, ISO 27001 (current and comprehensive) |
| Costs | Controller bears routine; processor bears remediation costs for non-compliance |
| Remediation | Specified timeline; escalation; controller may suspend or terminate for material breach |

### 10 — Data Return & Deletion

- [ ] Controller elects upon termination: return in structured format OR secure deletion (cryptographic erasure/physical destruction)
- [ ] Certification of completion within **30 days** (standard) / **60 days** (complex environments)
- [ ] Legal retention exception: retained data must be isolated, confidential, unused for service delivery
- [ ] Backups: isolate, exclude from restoration, delete per documented rotation schedule

### 11 — General Provisions

- [ ] **Definitions**: Incorporate GDPR Art. 4; add processing-specific terms
- [ ] **Governing law**: Compatible with GDPR Art. 3 territorial scope; must not undermine Chapter III rights
- [ ] **International transfers**: SCCs (Art. 46(2)(c)), BCRs (Art. 47), or adequacy (Art. 45); reference TIA post-*Schrems II*
- [ ] **Amendments**: Written mutual agreement; process for regulatory-driven updates
- [ ] **Dispute resolution**: Escalation → mediation → litigation/arbitration

## Schedules

| Schedule | Contents |
|---|---|
| **A** | Approved sub-processors: name, address, processing location, activity |
| **B** | Processing description: subject matter, duration, nature/purpose, data types, data subject categories |
| **C** | Technical and organizational security measures (by domain per Section 4) |
| **D** | Certifications, audit reports, compliance documentation |

Flag any schedule where source documents lack sufficient detail; note required information for completion.

## Pitfalls

- **Art. 28(3) completeness is mandatory** — all eight elements must appear; omission risks fines up to 4% global annual turnover / €20M
- **Special category data** (Art. 9): heighten security in Schedules B and C
- **Children's data**: flag Art. 8 and national implementing provisions
- **Jurisdiction**: GDPR applies by Art. 3 regardless of processor location; governing law must not conflict
- **SCCs**: verify against current EC SCC templates (June 2021) and EDPB Recommendations 01/2020
- **Never** allow processor to use personal data for own purposes — converts processor to controller
- **Never** grant open-ended sub-processor authorization without change-notification and objection rights
- **Reconcile** all cost, notice, and termination provisions with the underlying service agreement before execution
