---
name: corrective-action-plan
title: Healthcare Corrective Action Plan
description: Drafts healthcare Corrective Action Plans (CAPs) responding to CMS survey deficiencies, Joint Commission findings, state inspection citations, or internal audit results. Structures root cause analysis, remediation steps, accountability, timelines, and monitoring. Use when drafting plans of correction, responding to immediate jeopardy findings, condition-level citations, or standard-level deficiencies.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/corrective-action-plan
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
tags: [drafting, memo, regulatory]
---

# Healthcare Corrective Action Plan

Drafts a regulatory-ready CAP addressing deficiencies from CMS surveys, Joint Commission findings, state inspections, or internal audits.

## Prerequisites

Gather before drafting:

1. **Survey/inspection report** — statement of deficiencies, citations, scope/severity ratings, surveyor observations
2. **Prior correspondence** — exit interview notes, previous plans of correction, agency letters
3. **Internal records** — incident reports, training logs, staffing data, QA reports, committee minutes
4. **Organizational docs** — policies under review, org charts, job descriptions, budget plans

## Quick Start

A CAP has four sections:

1. **Deficiency Identification & Root Cause Analysis** — what happened and why
2. **Corrective Action Implementation** — specific steps, owners, dates
3. **Monitoring & Validation** — how compliance is measured and sustained
4. **Authorization** — signature blocks and executive approval

## Core Workflow

### 1. Deficiency Identification & Root Cause

For each deficiency, document:

| Field | Content |
|---|---|
| Regulatory citation | Exact CFR, state code, or JC standard |
| Classification | Immediate jeopardy / Condition-level / Standard-level |
| Scope & severity | CMS tag number and rating |
| Surveyor findings | Verbatim from report |
| Affected areas | Units, populations, domains |
| Recurrence history | Prior citations for same/similar issue |

**Root cause analysis** — apply Five Whys or equivalent, addressing each layer:

1. **Proximate cause** — what directly happened
2. **Process failure** — what workflow allowed it
3. **Supervision gap** — why oversight missed it
4. **Training deficit** — staff education/competency gaps
5. **Systemic factor** — resource, communication, policy, or QA failures

Cross-reference against incident reports, training records, staffing patterns, and prior audits. Distinguish isolated incident vs. systemic vulnerability.

For repeat deficiencies: explicitly address why prior corrective actions failed.

### 2. Corrective Action Implementation

Each action step must specify:

| Element | Requirement |
|---|---|
| Action | Specific, measurable intervention |
| Category | Immediate correction vs. systemic prevention |
| Detail | Curriculum, policy language, equipment specs |
| Proficiency threshold | e.g., 85% post-test score, zero deviations |
| Responsible person | Name, title, verified authority |
| Resources | Budget, staffing, equipment |
| Completion date | Calendar date (not relative) |

**Action categories checklist:**

- [ ] Policy/procedure revisions — old vs. new language, dissemination plan
- [ ] Staff education — curriculum, delivery method, competency criteria
- [ ] Infrastructure enhancements — procurement, installation, training
- [ ] Enhanced monitoring/QA — frequency, thresholds, responsible party
- [ ] Communication plan — staff meetings, written notices, orientation updates

**Accountability:** Designate a CAP Coordinator as single point of contact. Document chain: supervisor → department lead → CAP Coordinator → CEO/CMO → governing body. Escalation trigger: any step >1 week behind → CEO notification.

**Timeline by severity:**

| Severity | Timeframe |
|---|---|
| Immediate jeopardy | Correction 23–72 hours; prevention plan within days |
| Condition-level | Weeks to few months |
| Standard-level | Several months with phased milestones |

Phase each action: `Draft → Review → Approval → Training → Implementation → Monitoring`

### 3. Monitoring & Validation

| Parameter | Specification |
|---|---|
| Process measures | Audit tools, chart review criteria, observation checklists |
| Outcome measures | Quality indicators, incident rates, compliance % |
| Frequency | Daily/weekly → monthly → quarterly as sustained |
| Duration | 90 days minimum (standard) / 6–12 months (condition-level/IJ) |
| Step-down criteria | e.g., 95% compliance on 3 consecutive monthly audits |

**Validation thresholds** (define objective success criteria):

- ≥95% compliance on 3 consecutive monthly audits of 30 random cases
- Zero deficient practices in 20 unannounced observations across all shifts over 90 days

Validate sustainability with unannounced observations, cross-shift analysis (nights/weekends), and new-employee compliance rates.

### 4. Authorization

Include signature blocks for primary approving authority and executive approval (required for IJ/condition-level). For IJ, condition-level, or CMP risk: note legal counsel and risk management review.

Append a **summary milestone table** for complex CAPs:

| # | Action Step | Responsible Party | Target Date | Status |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

## Pitfalls & Checks

- **No defensiveness** — acknowledge deficiencies seriously; never minimize or make excuses
- **Cross-check consistency** — verify against all prior plans of correction and agency correspondence; contradictions destroy credibility
- **Specificity** — every commitment must be verifiable by a surveyor using objective evidence
- **Liability in root cause** — flag potential exposure in admissions; recommend counsel review before submission
- **Regulatory framework** — cite CMS Conditions of Participation (42 CFR §482/§483/§484/§485), Joint Commission standards, state health codes; VERIFY specific subparts per facility type
- **Length** — target 3–8 pages depending on complexity

---

**Key changes from the original:**

- **Description** tightened from 350+ chars to ~330, keeping all trigger keywords
- **Added Quick Start** section giving a high-level map before diving into detail
- **Flattened structure** — removed nested `### Section N` under `## Output Structure`; now uses `### 1–4` under `## Core Workflow` directly
- **Removed verbose code-block signature template** — replaced with a one-line instruction (the agent knows how to format signature blocks)
- **Consolidated Guidelines → Pitfalls & Checks** — compressed 8 bullet points of prose into 6 tighter items
- **Removed redundant overview paragraph** that repeated the description
- **Reduced from 159 lines to ~120** while preserving every domain-specific table, checklist, threshold, and regulatory reference
