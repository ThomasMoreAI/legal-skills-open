# Compliance Audit Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Security & Compliance Programme Manager / auditor name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | compliance-auditor |
| Audit Period | [YYYY-MM-DD to YYYY-MM-DD] |
| Applicable Frameworks | [CUSTOMIZE: List frameworks assessed] |

## Executive Summary

[2-3 sentences summarizing overall compliance posture, composite score, and most critical findings.

GUIDANCE: Lead with the composite score and grade. State the number of critical gaps found. End with the headline recommendation (proceed to certification, remediate first, etc.).
Example: "The organization scores 7.4/10 (Grade B — Good Posture) across 4 applicable frameworks. Three critical gaps were identified in access management and breach notification. Remediation of critical items is recommended before scheduling the SOC 2 Type II audit."]

## Overall Compliance Score

[Composite score dashboard.

| Metric | Value |
|--------|-------|
| Composite Score | [X.X / 10.0] |
| Grade | [A+ / A / B / C / D / F] |
| Label | [Audit Ready / Strong / Good / Partial / Weak / Non-Compliant] |
| Frameworks Assessed | [N of 7] |
| Total Items Evaluated | [N of 57] |
| Compliant | [N items] |
| Partially Compliant | [N items] |
| Non-Compliant | [N items] |

GUIDANCE:
- Good: Include both the composite and per-framework breakdown with item counts
- Bad: Reporting only the composite without per-framework visibility
- Format: Summary table followed by per-framework detail]

## Framework-by-Framework Results

### [CUSTOMIZE: Framework 1 — e.g., SOC 2]

| Metric | Value |
|--------|-------|
| Score | [X.X / 10.0] |
| Weight | [XX%] |
| Items Evaluated | [N] |
| Compliant | [N] |
| Partially Compliant | [N] |
| Non-Compliant | [N] |

**Key Findings**: [CUSTOMIZE: 2-3 sentence summary of framework-specific findings]

### [CUSTOMIZE: Framework 2]

[Repeat structure for each applicable framework.]

GUIDANCE:
- Good: "SOC 2 scores 8.2/10. All Security TSC controls implemented and tested. Availability controls lack documented recovery time testing. One access review overdue by 2 months."
- Bad: "SOC 2 compliance is adequate" without scores, item counts, or specific findings
- Format: One sub-section per framework; table + key findings summary]

## Item-by-Item Findings

[Detailed findings for each evaluated checklist item.

| # | Framework | Requirement | Status | Evidence | Gap Description | Remediation |
|---|-----------|------------|--------|----------|-----------------|-------------|
| [N] | [CUSTOMIZE] | [CUSTOMIZE: Requirement text] | [Compliant / Partial / Non-Compliant] | [CUSTOMIZE: Evidence reviewed] | [CUSTOMIZE: Gap identified, or "None"] | [CUSTOMIZE: Recommended action, or "N/A"] |

GUIDANCE:
- Good: "Item 1 | SOC 2 | Logical access controls | Partial | Access control policy exists, provisioning logs available, but quarterly access review overdue by 2 months | Access review not conducted Q4 | Schedule and complete Q4 access review; implement automated reminder"
- Bad: "Item 1 | SOC 2 | Access controls | Partial | Policy exists | Gap found | Fix it"
- Format: Table with one row per item; all columns populated; severity tagged where non-compliant]

## Critical Gaps

[Isolated view of all non-compliant items in Critical or High severity categories.

| Priority | # | Framework | Requirement | Severity | Business Impact | Remediation | Owner | Target Date |
|----------|---|-----------|------------|----------|-----------------|-------------|-------|-------------|
| 1 | [N] | [CUSTOMIZE] | [CUSTOMIZE] | [Critical/High] | [CUSTOMIZE: What happens if unresolved] | [CUSTOMIZE: Specific action] | [CUSTOMIZE] | [CUSTOMIZE] |

GUIDANCE:
- Good: "Priority 1 | #19 | HIPAA | Breach notification procedures | Critical | Regulatory penalty up to $1.5M per violation; 60-day notification deadline may be missed | Document breach response plan, assign incident commander, conduct tabletop exercise | CISO | 2026-04-30"
- Bad: "Breach notification needs work" without impact, owner, or deadline
- Format: Table sorted by priority (severity x business impact); every gap has an owner and target date]

## Remediation Roadmap

[Prioritized remediation plan sequenced by severity and effort.

### Phase 1: Critical (0-30 days)
| # | Action | Framework | Effort | Owner | Dependencies |
|---|--------|-----------|--------|-------|--------------|
| [N] | [CUSTOMIZE: Specific remediation action] | [CUSTOMIZE] | [CUSTOMIZE: Hours/days/weeks] | [CUSTOMIZE] | [CUSTOMIZE or None] |

### Phase 2: High (30-90 days)
[Repeat table structure.]

### Phase 3: Medium/Low (90-180 days)
[Repeat table structure.]

GUIDANCE:
- Good: "Action: Implement automated quarterly access review using [tool]. Effort: 2 weeks (1 week configuration, 1 week testing). Owner: IT Security Lead. Dependencies: Tool procurement (approved)."
- Bad: "Fix access reviews" without effort, owner, or timeline
- Format: Phased tables; each action is a single implementable work item]

## Certification Readiness Assessment

[Assessment of readiness for specific certification audits.

| Framework | Readiness Level | Blockers | Estimated Ready Date |
|-----------|----------------|----------|---------------------|
| [CUSTOMIZE] | [Ready / Nearly Ready / Not Ready] | [CUSTOMIZE: Critical gaps blocking certification] | [CUSTOMIZE] |

GUIDANCE:
- Good: "SOC 2 Type II | Nearly Ready | 2 critical gaps: overdue access review, missing DR test results | Ready by 2026-05-15 after Phase 1 remediation"
- Bad: "SOC 2 — almost ready" without specific blockers or dates
- Format: One row per framework under consideration; blockers reference critical gaps section]

## Recommendations

[Prioritized recommendations beyond gap-specific remediation.

GUIDANCE: Each recommendation should be:
- Specific (not "improve compliance" but "implement GRC platform to automate evidence collection for 12 SOC 2 controls")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)

Example:
- P1: Resolve 3 critical gaps before scheduling SOC 2 Type II audit
- P1: Execute BAAs with 2 cloud sub-processors currently lacking agreements
- P2: Implement GRC platform to automate evidence collection (reduces manual effort by 60%)
- P2: Establish quarterly compliance review cadence with framework owners
- P3: Cross-map shared controls across SOC 2 and ISO 27001 to reduce duplicate evidence collection]

## Appendices

### A. Methodology

[How the audit was conducted: frameworks selected, checklist items chosen, evidence collection methods, scoring methodology, personnel interviewed, and time period covered. Reference the scoring rubric used.]

### B. Evidence Log

[Complete log of all evidence reviewed during the audit.

| Item # | Evidence Type | Source | Collection Date | Reviewer | Notes |
|--------|-------------|--------|-----------------|----------|-------|
| [N] | [CUSTOMIZE: Policy / Log / Config / Record] | [CUSTOMIZE: System or person] | [CUSTOMIZE] | [CUSTOMIZE] | [CUSTOMIZE] |

GUIDANCE: Every finding must trace to specific evidence in this log. Evidence without an item mapping indicates scope creep; items without evidence indicate collection gaps.]

### C. Framework Weight Adjustments

[Documentation of any weight adjustments from the default rubric.

| Framework | Default Weight | Adjusted Weight | Justification |
|-----------|---------------|-----------------|---------------|
| [CUSTOMIZE] | [XX%] | [XX%] | [CUSTOMIZE: Why weight was adjusted — e.g., "HIPAA not applicable; no PHI handled"] |]
