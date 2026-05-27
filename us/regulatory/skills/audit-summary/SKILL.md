---
name: audit-summary
title: Legal Audit Summary
description: 'Produces structured U.S. legal audit summaries that distill compliance findings into executive-ready risk prioritization and remediation plans, covering likelihood/impact scoring, consequence analysis, and corrective actions with timelines and owners. Use for legal audits, compliance audits, regulatory audits, compliance gap analyses, risk assessments, audit report summaries, or remediation roadmaps. Trigger keywords: audit summary, compliance findings, audit report, risk prioritization, remediation plan, regulatory exposure, corrective action plan.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/audit-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
tags: [analysis, summarization, summary]
---

# Legal Audit Summary

Distill audit findings into a prioritized compliance roadmap with risk-scored findings, remediation actions, and governance follow-up.

## Prerequisites

1. Complete audit materials: reports, checklists, evidence, interviews, exhibits.
2. Jurisdictional scope and governing authorities per audit domain.
3. Applicable statutes, regulations, standards, or guidance.
4. Organizational context: business units, systems, and processes in scope.
5. Point of contact for ownership and timeline validation.

## Output Structure / Process

1. Intake and scope confirmation.
2. Executive Overview.
3. Findings Summary (aggregated).
4. Detailed Findings (per issue).
5. Remediation Roadmap.
6. Governance and Follow-Up.
7. Appendix (sources, assumptions, limitations).

**Executive Overview Template**

```text
Overall Compliance Posture: {concise assessment}
Total Findings: Critical {#} | High {#} | Medium {#} | Low {#}
Top Risk Areas: {domain 1}, {domain 2}, {domain 3}
Immediate Actions (0–60 days): {1–3 items}
Near-Term Actions (61–180 days): {1–3 items}
Long-Term Actions (181+ days): {1–3 items}
```

**Findings Summary Table**

| ID | Domain | Requirement | Deficiency | Risk | Likelihood | Impact | Consequence | Owner |
|---|---|---|---|---|---|---|---|---|
| F-01 | {Domain} | {Citation} | {Gap} | {C/H/M/L} | {H/M/L} | {H/M/L} | {Penalty/License/Reputation} | {Dept} |

**Risk Rating Criteria**

| Rating | Criteria |
|---|---|
| Critical | Criminal exposure, license loss, business continuity threat, severe penalties |
| High | Material civil penalties, regulatory sanctions, major reputational harm |
| Medium | Noticeable compliance gap with moderate enforcement or cost exposure |
| Low | Minor gap, low enforcement likelihood, limited impact |

**Detailed Finding Template**

```text
Finding ID: F-##
Domain: {e.g., Data Privacy}
Requirement: {Statute/Regulation/Guidance + citation}
Issue: {What is missing or deficient}
Facts/Evidence: {Key facts supporting gap}
Risk Assessment:
  Likelihood: {H/M/L} | Impact: {H/M/L}
  Rationale: {brief, evidence-based}
Consequences: {Regulatory, civil, operational, reputational}
Recommendation:
  Action: {specific corrective action}
  Timeline: {date or days}
  Owner: {department/role}
  Resources: {budget, tools, external counsel, vendors}
```

**Financial Exposure**

- Provide ranges when exact penalties are unknown.
- Cite penalty provisions; use `[VERIFY]` where uncertain.
- Separate direct costs (fines, sanctions) from indirect costs (monitoring, remediation, litigation).

**Remediation Roadmap**

| Workstream | Actions | Priority | Dependencies | Timeline | Owner | Status Metric |
|---|---|---|---|---|---|---|
| {Domain} | {Action list} | {C/H/M/L} | {Upstream items} | {dates} | {Dept} | {KPI} |

**Governance and Follow-Up**

- Recommend compliance task force with reporting cadence.
- Include audit re-check schedule and validation approach.

**Privilege Legend (if applicable)**

```text
Attorney–Client Privileged / Attorney Work Product
Confidential — Prepared at the Direction of Counsel
```

## Guidelines

- Use objective, non-admissions language; describe gaps as risks or deficiencies.
- Prioritize by risk; list Critical and High first.
- Keep citations accurate; add `[VERIFY]` for any uncertain authority.
- Provide concrete actions with owners and timelines, not generic recommendations.
- State interpretive uncertainty and propose mitigation steps.
- Avoid legal jargon; keep executive readability high.
- Ensure scope and limitations are explicit in the Appendix.
