---
name: deficiency-corrective-action-plan
title: Corrective Action Plan (Healthcare)
description: Drafts U.S. healthcare corrective action plans (CAPs / plans of correction) responding to survey deficiencies, audits, or inspections. Produces deficiency statements, root cause analysis, corrective actions, accountability assignments, timelines, monitoring, and validation aligned to CMS, Joint Commission, and state health department standards. Triggers on CAP, plan of correction, statement of deficiencies, survey findings, accreditation response, regulatory remediation, QAPI corrective action.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/deficiency-corrective-action-plan
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
tags: [drafting, policy, checklist, regulatory]
---

# Corrective Action Plan (Healthcare)

Produces a regulator-ready CAP that is specific, measurable, and mapped to cited healthcare compliance deficiencies.

## Quick Start

1. Collect the survey report with citations, scope/severity, and dates.
2. Run root cause analysis (Five Whys or fishbone) for each deficiency.
3. Draft corrective actions (immediate + systemic) with absolute dates, owners, and monitoring metrics.
4. Complete the submission checklist and obtain executive signatures.

## Prerequisites

1. Statement of deficiencies / survey report — citations, scope/severity, dates, cited evidence.
2. Prior regulator correspondence, exit interview notes, prior plans of correction.
3. Relevant policies, procedures, training curricula, competency records.
4. RCA inputs — incident reports, audit data, QA/QAPI logs, staffing metrics, workflow artifacts.
5. Org chart with role owners for each corrective action.
6. Submission deadline and format requirements from regulator/accreditor.

## Output Structure

### 1. Document Header

Facility name, survey/audit date(s), regulator/accreditor, CAP version/date, primary contact, submission deadline.

### 2. Deficiency Summary

One row per cited deficiency. Use verbatim finding text from the survey report.

| Deficiency ID | Citation/Standard | Survey Finding (Verbatim) | Scope/Severity | Affected Unit | Date(s) | Repeat? | Immediate Jeopardy? |
|---|---|---|---|---|---|---|---|
| D-1 | 42 CFR §___ / State Code ___ / JC Std ___ | | | | | Y/N | Y/N |

### 3. Root Cause Analysis

- Use Five Whys or fishbone for each deficiency.
- Distinguish systemic vs. isolated causes.
- Tie each cause to evidence from records.

### 4. Corrective Action Plan Table

One row per corrective action. Separate immediate correction from systemic prevention.

| Deficiency ID | Root Cause(s) | Immediate Correction | Systemic Prevention | Owner (Name/Title) | Resources | Start Date | Due Date | Milestones | Monitoring Metric | Frequency | Validation Criteria | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D-1 | | | | | | | | | | | | |

Action categories: policy updates, training, staffing, workflow redesign, technology, resource commitments.

### 5. Accountability

- Name CAP coordinator and action owners by title.
- Confirm each owner has authority to allocate resources and enforce compliance.

### 6. Timeline

- Absolute dates for every action and milestone.
- Align with regulator deadlines; escalate conflicts to leadership.

### 7. Monitoring and Validation

| Element | Define |
|---|---|
| Process metrics | Measure implementation progress |
| Outcome metrics | Measure deficiency resolution |
| Sampling method | How data is collected |
| Frequency | How often metrics are reviewed |
| Reporting line | Who receives reports |
| Success threshold | Objective criteria for sustained compliance |
| Duration | Period of sustained compliance required |
| Evidence | Artifacts proving compliance |

### 8. Sustainability

Integrate corrective actions into routine QAPI, orientation, and periodic re-audits.

### 9. Consistency Check

Reconcile with prior statements to regulators. Flag and resolve any conflicts.

### 10. Attachments

List all supporting artifacts: policies, training materials, audit tools, evidence documents.

## Submission Checklist

- [ ] Citations and standards verified against survey report
- [ ] Actions specific, measurable, and mapped to root causes
- [ ] Absolute dates for every action and milestone
- [ ] Monitoring and validation thresholds defined and objective
- [ ] Responsibilities aligned with actual authority and reporting lines
- [ ] PHI removed or de-identified; HIPAA-compliant references only
- [ ] Consistency checked against prior regulator communications
- [ ] Executive approvals and signatures obtained

## Guidelines

- Use the regulator's language for findings — do not minimize or dispute in the CAP.
- Avoid legal admissions beyond cited findings; stay factual and precise.
- If prior corrective actions failed, state why and how this plan differs.
- Use absolute dates, never relative timeframes.
- Tie every corrective action to a root cause and a monitoring metric.
- If multiple deficiencies share a root cause, document linkage and draft one integrated fix.
- Redact PHI; refer to cases by internal ID only.
- Keep tone professional, accountable, and non-defensive.

## Troubleshooting

**Regulator rejects CAP as too vague**: Ensure each action specifies who, what, when, and how — not just policy revision intent. Add measurable milestones.

**Repeat deficiency from prior survey**: Explicitly address why the prior CAP failed and what differs this time. Regulators expect escalation, not repetition.

**Timeline conflicts with regulator deadline**: Escalate to leadership immediately. Request extension in writing before deadline, with interim safeguards documented.

**Multiple deficiencies share one root cause**: Draft a single integrated corrective action and cross-reference from each deficiency row. Do not duplicate.
