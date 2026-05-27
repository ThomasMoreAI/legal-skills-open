---
name: employee-dispute-summary
title: Employee Dispute Summary
description: Produces a structured, source-cited summary of U.S. employment disputes for HR and litigation review. Trigger when asked to summarize an employee dispute, employment litigation, HR investigation, EEOC/agency matter, discrimination, harassment, retaliation, wrongful termination, wage-hour dispute, or grievance/arbitration file.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/employee-dispute-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags: [litigation, summarization, summary]
---

# Employee Dispute Summary

Produce an objective, source-cited summary of an employee dispute for HR and legal decision-making.

## Quick Start

Collect before drafting:
- **Source corpus** — complaints, witness statements, investigation reports, correspondence, disciplinary records, employment agreements, policies/handbooks, performance reviews, agency filings, pleadings, settlement docs
- **Parties** — all individuals/entities with roles and relationships
- **Timeline anchors** — key dates, deadlines, hearings, milestones
- **Forum** — internal process, arbitration, EEOC/state agency, court, union grievance
- **Resolution docs** — settlement, award, or decision documents (if any)

## Output Sections

### 1. Executive Overview
2–3 sentences: nature of dispute, core claims, current status, immediate next step.

### 2. Parties and Roles
| Party | Role | Relationship | Counsel/Rep | Source |
|---|---|---|---|---|

### 3. Allegations Matrix
| Allegation | Claim Type | Alleged Conduct | Dates/Locations | Witnesses | Policy/Statute | Status | Source |
|---|---|---|---|---|---|---|---|

### 4. Responses and Defenses
| Party | Position | Admissions | Denials | Affirmative Defenses | Disputed Facts | Source |
|---|---|---|---|---|---|---|

### 5. Procedural History
| Date | Event | Forum/Process | Outcome/Status | Next Deadline | Source |
|---|---|---|---|---|---|

### 6. Resolution / Outcome
| Type | Date | Monetary Terms | Non-Monetary Terms | Confidentiality | Appeal Status | Source |
|---|---|---|---|---|---|---|

Skip if no resolution exists.

### 7. Findings / Determinations
| Decision-Maker | Finding | Standard Applied | Scope | Effective Date | Source |
|---|---|---|---|---|---|

### 8. Outstanding Issues and Next Steps
- [ ] Open factual disputes
- [ ] Pending procedural steps
- [ ] Required notices/approvals
- [ ] Evidence gaps to close
- [ ] Decision points for HR/Legal

### 9. Risk and Policy Impact
| Risk Area | Exposure Level | Rationale | Potential Remedies | Policy Impact | Source |
|---|---|---|---|---|---|

### 10. Source Map
| Fact/Assertion | Source Doc ID | Page/Section | Confidence |
|---|---|---|---|

### 11. Gaps / Additional Information Needed
List missing documents, unclear facts, or unverified assertions.

## Source Handling

- Tag every factual assertion with a marker: `[Doc-12]`.
- Use quotation marks for direct quotes; cite document and page/section.
- If a fact is disputed, state both positions and label **Disputed**.

## Pitfalls and Checks

- **Neutrality** — never assess credibility or intent; state legal conclusions only if formally determined by a court, arbitrator, or agency.
- **Policy versions** — identify the governing policy version and effective date when cited.
- **Privilege** — note confidentiality restrictions; do not reproduce sensitive material beyond necessity.
- **Jurisdiction** — if unclear or non-U.S., flag explicitly and adjust labels; mark uncertain citations `[VERIFY]`.
- **Retaliation / preservation** — highlight anti-retaliation and document-preservation obligations when implicated.
- **Length** — target 2–5 pages for complex matters; keep scannable.
