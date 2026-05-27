---
name: corrective-action-plan-deficiencies
title: Corrective Action Plan for Healthcare Deficiencies
description: Drafts a regulator-ready Corrective Action Plan (CAP) for U.S. healthcare facilities responding to inspection, survey, or audit deficiencies. Covers root-cause analysis, remediation steps, accountability, milestones, monitoring, and validation. Trigger when the user mentions CAP, plan of correction, deficiency citation, scope/severity remediation, correction timeline, or sustainability monitoring for CMS, state, or Joint Commission findings.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/corrective-action-plan-deficiencies
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
tags: [drafting, memo, regulatory]
---

# Corrective Action Plan for Healthcare Deficiencies

Produces a regulator-ready CAP aligning documented findings with implementable remediation, measurable milestones, and post-correction validation.

## Gather Before Drafting

- Inspection documents: survey report, statement of deficiencies, exit notes, prior CAPs, correspondence
- Regulatory identifiers: CMS/state program notices, accreditation standards, certifications, response deadlines
- Root-source data: incident logs, QA metrics, training records, staffing schedules, policy versions
- Org structure: authority matrix, job descriptions, committee charters, budget constraints
- Legal posture: sanction exposure, privilege considerations, counsel alignment if liability implicated
- Submission target: regulator format requirements, filing deadlines

## Workflow

### 1. Intake and Factual Baseline

| Element | Content | Source |
|---|---|---|
| Header | Facility, program, finding IDs, dates, facility type | Survey/notice letters, CMS portal |
| Deficiency statement | Exact noncompliance language; dates, location, patient population, severity | Deficiency narrative, field notes |
| Citation mapping | Statute/regulation/standard references as written by regulator | Official citation text |
| Event timeline | Discovery → preliminary → formal findings → response date | Inspection log, correspondence |
| Prior-work continuity | Prior CAP references and outcomes; why prior actions failed if recurring | Historical CAPs, QA trend reports |

### 2. Root-Cause Analysis

1. Classify each deficiency as isolated vs. systemic.
2. Apply structured method (5-Whys / fishbone); name primary causal chain.
3. Link each driver to evidence: policy gaps, training gaps, staffing constraints, supervision blind spots, communication failures.
4. State recurrence risk and why prior controls failed.

### 3. Corrective Action Matrix

| # | Deficiency / Root Cause | Action Step | Owner | Due Date | Evidence Required | Verification Method |
|---|---|---|---|---|---|---|

Per row:
- Separate immediate correction from longer-term prevention.
- Reference the specific deficiency and root cause.
- Training entries: content, format, assessment method, proficiency threshold.
- Policy changes: section numbers, deleted/added language, distribution, acknowledgment.
- Capital/resource changes: procurement lead times, implementation dependencies.

### 4. Accountability and Escalation

- Designate CAP coordinator (single point of contact), departmental leads, executive sponsor.
- Escalation triggers: milestone missed >1 week, budget overrun above threshold, resource blockade.
- Review cadence: weekly operational, monthly executive.

### 5. Monitoring and Sustainability

| Element | Frequency | Source | Owner | Threshold |
|---|---|---|---|---|
| Process compliance | Daily/weekly initially, taper by risk | Audit tools, checklists, observation logs | QA staff | Defined target |
| Outcome data | Weekly/monthly | Quality indicators, incident reports | Clinical director/QA | Reduction to baseline |
| Competency retention | Go-live + periodic refresher | Test scores, direct observation | Education lead | Minimum met |

- Distinguish one-time completion from sustained compliance.
- Require minimum stable period before de-escalation.
- Use unannounced cross-shift audits to test durability.

### 6. Validation and Closure

- Pre-post comparison using identical metrics and sampling.
- Independent verification (internal or external) for high-risk findings.
- Closure criteria: compliance thresholds sustained across shifts and time.
- Tie to evidence logs, reports, and leadership sign-off.

### 7. Execution Template

Populate the following fields in the final output:

- Facility / Program / Agency
- Deficiency IDs / Citations / Severity
- Summary of findings (verbatim excerpts)
- Root cause(s)
- Immediate actions / Systemic actions
- Milestone schedule
- Monitoring matrix
- Validation criteria
- Escalation triggers
- Regulatory reporting cadence
- Executive approval / Signature block(s)

### 8. Pre-Output Checks

- No contradictions with prior regulator statements.
- All commitments feasible within budget, staffing, and operating constraints.
- Every obligation mapped to an evidence artifact.
- Dates are calendar-based with contingency notes.
- Legal review flagged where admissions increase enforcement risk.

## Pitfalls and Guardrails

- Use regulator-facing language; no defensive framing or noncommittal phrasing.
- Do not overpromise resources; if infeasible, request extension with substantiation and interim controls.
- Separate facts from analysis; no speculative causal assertions.
- For recurring deficiencies, state explicitly why prior remediation failed and what changed.
- IJ/condition-level findings: prioritize immediate patient-safety remediation and expedited reporting.
- Treat state-specific requirements and accreditor addenda as hard constraints.
- Verify all timelines against CMS/state/enforcement deadlines before submission.
- Include counsel review when findings imply sanction exposure, civil penalties, or contract termination risk.
- Mark uncertain legal standards with `[VERIFY]`.
- Do not include broad legal conclusions on liability; focus on compliance remediation.
