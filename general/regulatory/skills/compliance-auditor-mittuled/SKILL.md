---
name: compliance-auditor-mittuled
title: compliance-auditor
description: This skill conducts comprehensive compliance audits across 7 regulatory frameworks using a 57-item checklist with quantitative scoring and remediation guidance. Use when preparing for certification audits (SOC 2, ISO 27001) or regulatory reviews. Also consider when onboarding enterprise customers with compliance requirements. Suggest when annual compliance review cycle begins.
author: mittuled
author_url: https://github.com/mittuled/skill-os/tree/main/agents/legal/security-compliance-programme-manager/compliance-auditor
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# compliance-auditor

## Agent: Security & Compliance Programme Manager

L2 security and compliance programme manager (1x) responsible for SOC 2, security awareness training, disaster recovery, GDPR/CCPA compliance, and penetration test programme management.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Conducts comprehensive compliance audits across 7 regulatory frameworks using a 57-item checklist with quantitative scoring, gap identification, and prioritized remediation roadmaps.

## When to Use

- When preparing for a certification audit (SOC 2 Type I/II, ISO 27001) or regulatory review and the company needs to understand its current compliance posture.
- When onboarding enterprise customers who require evidence of compliance with specific frameworks (HIPAA, PCI DSS, GDPR) as a procurement condition.
- When the annual compliance review cycle begins and cross-framework compliance status must be assessed and reported to leadership.

## Workflow

1. **Determine Applicable Frameworks**: Assess which of the 7 supported frameworks apply based on business type, geography, customer requirements, and data handled. Adjust framework weights in the scoring rubric (see [scoring-rubric.md](references/scoring-rubric.md)) based on applicability — frameworks that do not apply receive zero weight and their weight is redistributed proportionally. Deliverable: framework applicability assessment with weight adjustments.

2. **Select Checklist Items**: From the 57-item master checklist (see [checklist.md](references/checklist.md)), select items relevant to the applicable frameworks. For each selected item, confirm the requirement text, evidence needed, and severity rating. Deliverable: tailored checklist with applicable items and evidence requirements.

3. **Gather Evidence**: For each checklist item, collect evidence: policies, procedures, technical control configurations, access logs, training records, audit trails, and vendor assessments. Record evidence source, collection date, and completeness. Deliverable: evidence inventory mapped to checklist items.

4. **Score Each Item**: Score each checklist item as Compliant (control documented, implemented, and tested), Partially Compliant (control exists but has gaps in documentation, implementation, or testing), or Non-Compliant (control absent or fundamentally deficient). Rate evidence quality for each item. Deliverable: scored checklist with status, evidence rating, and findings per item.

5. **Calculate Framework Scores**: Calculate the compliance score for each applicable framework using the scoring rubric criteria and weights. Compute the overall composite score across all frameworks. Deliverable: framework-level and composite compliance scores with grade.

6. **[GATE] Identify Critical Gaps**: Isolate all non-compliant items in Critical or High severity categories. These represent regulatory exposure, certification blockers, or customer deal risks. Flag any gap that could result in enforcement action, failed certification, or lost customer. Deliverable: critical gaps register approved by compliance programme manager.

7. **Generate Remediation Roadmap**: For each gap, produce a remediation recommendation with: specific action required, responsible team, estimated effort (hours/days/weeks), dependencies, and priority based on severity multiplied by effort efficiency. Sequence remediation by priority and dependencies. Deliverable: prioritized remediation roadmap with timeline.

8. **Produce Compliance Audit Report**: Assemble the final report using the template (see [compliance-audit-report-template.md](assets/compliance-audit-report-template.md)). Include executive summary with composite score, framework-by-framework results, item-by-item findings, critical gaps section, remediation roadmap, and certification readiness assessment. Deliverable: complete compliance audit report delivered to security leadership and executive team.

## Anti-Patterns

- **Point-in-time snapshot mentality**: Treating the audit as a one-time assessment rather than a baseline for continuous monitoring. *Why*: compliance degrades between audits as systems change, employees turn over, and new regulations take effect; without continuous monitoring, the next audit will reveal regression.

- **Framework siloing**: Auditing each framework independently without mapping shared controls across frameworks. *Why*: SOC 2, ISO 27001, and GDPR share significant control overlap (access management, encryption, incident response); siloed audits duplicate effort and produce inconsistent findings for the same underlying control.

- **Severity-blind remediation**: Prioritizing remediation by ease of implementation rather than by regulatory severity and business impact. *Why*: fixing low-severity items first while critical gaps persist maximizes the window of regulatory exposure and delays certification readiness.

- **Evidence-free scoring**: Assigning compliance scores based on verbal assurances or policy existence without verifying implementation and operational effectiveness. *Why*: a policy that exists but is not followed provides zero compliance value; auditors and regulators evaluate operating effectiveness, not documentation completeness.

## Output

**On success**: Produces a complete compliance audit report containing composite and per-framework compliance scores with letter grades, item-by-item findings with evidence ratings, critical gaps register, prioritized remediation roadmap with effort estimates, and certification readiness assessment. Delivered to security leadership, executive team, and relevant framework owners.

**On failure**: Report which frameworks could not be fully assessed (e.g., evidence unavailable, control owners unresponsive), what partial scores were calculated with confidence qualifiers, and what must be resolved to complete the audit. Include the partial report with explicit gap markers and a plan to obtain missing evidence.

## Related Skills

- [`contract-review-orchestrator`](../../../legal/corporate-counsel/contract-review-orchestrator/SKILL.md) -- Compliance audit findings inform contract review by identifying which compliance commitments the company can credibly make to counterparties.
- [`soc2-programme-manager`](../soc2-programme-manager/SKILL.md) -- SOC 2-specific findings from the compliance audit feed directly into the SOC 2 programme remediation and evidence collection workflows.
- [`gdpr-ccpa-compliance-manager`](../gdpr-ccpa-compliance-manager/SKILL.md) -- GDPR and CCPA findings from the audit inform ongoing privacy compliance programme priorities.
