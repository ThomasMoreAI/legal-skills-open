---
name: settlement-summary
title: Settlement Summary
description: Generates structured summaries of settlement negotiations and agreements in commercial litigation. Use when summarizing settlement history, documenting negotiation timelines, analyzing settlement terms, preparing implementation checklists, or reviewing release and confidentiality provisions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/settlement-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Settlement Summary

Summarizes settlement negotiations and final agreement terms from litigation matter files into a structured format covering chronology, key terms, strategic context, and implementation steps.

## Required Inputs

- **Settlement documents** — demands, offers, counteroffers, term sheets, executed agreements
- **Mediation materials** — statements, mediator proposals (if any)
- **Correspondence** — emails/letters reflecting negotiation positions
- **Case context** — claims, parties, litigation posture at settlement time

## Output Structure

### 1. Executive Overview

| Field | Content |
|---|---|
| Parties | All settling parties and roles |
| Settlement date | Date of executed agreement |
| Total consideration | Amount and structure |
| Key non-monetary terms | Injunctive relief, practice changes, etc. |
| Case disposition | Dismissal type (with/without prejudice) |

### 2. Negotiation Chronology

Capture each significant event in date order:

| Date | Party | Action | Terms Proposed | Conditions |
|---|---|---|---|---|
| _date_ | _party_ | Demand / Offer / Counter / Mediation | Amounts and terms | Attached conditions |

Include mediator name/date for mediation sessions. Note case developments (rulings, discovery) that influenced shifts.

### 3. Settlement Terms Analysis

**Monetary consideration** — total amount, payment structure (lump sum vs. structured), allocation among claimants, tax provisions, payment deadlines, default provisions.

**Release provisions** — scope (mutual/unilateral), claims covered and carve-outs, covered parties (affiliates, successors). Quote key release language with section cites.

**Confidentiality** — what is confidential (terms, amount, existence), permitted disclosures, breach consequences.

**Liability language** — quote admission/denial clause verbatim with section cite.

**Ongoing obligations** — compliance monitoring, cooperation requirements, performance obligations with deadlines.

### 4. Special Provisions

Flag if present:

- [ ] Court approval required (class action, minor, bankruptcy)
- [ ] Board or third-party consent conditions precedent
- [ ] Insurance allocation between covered/non-covered claims
- [ ] Reservation of rights language
- [ ] Enforcement dispute resolution mechanism
- [ ] Non-standard or unusual terms for the practice area

### 5. Strategic Assessment

| Factor | Analysis |
|---|---|
| Settlement vs. trial exposure | Compare to realistic verdict range |
| Litigation costs avoided | Estimated remaining costs |
| Risk factors driving settlement | Key vulnerabilities per side |
| Insurance implications | Coverage issues, policy limits, contribution |

### 6. Implementation Checklist

- [ ] File dismissal (with/without prejudice) — deadline: ___
- [ ] Execute mutual releases
- [ ] Initial payment due — date: ___
- [ ] Provide notice to third parties
- [ ] Return/destroy confidential materials
- [ ] Calendar ongoing obligation deadlines

## Pitfalls

- **Never infer missing terms** — flag gaps explicitly when documents are incomplete
- **Quote exactly** for release, confidentiality, and liability provisions — always cite section/paragraph numbers
- **Chronology is date-ordered** — do not group by party
- **Insurance allocation** — address covered vs. non-covered claims separately when insurance is involved
- **Conditions precedent** — note all conditions that must be satisfied before the settlement is effective
- **Plain language** for client-facing sections; preserve legal precision for technical provisions
