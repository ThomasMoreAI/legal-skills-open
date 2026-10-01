---
name: lease-compliance-fdu-ins
title: Lease Compliance Analysis Complete
description: Audit commercial lease compliance systems -- CAM reconciliation accuracy (pro-rata share, caps, admin fees), lease abstraction completeness, critical date tracking and deadline alerting, clause compliance monitoring (insurance certificates, permitted use, co-tenancy), tenant obligation enforcement, and ASC 842/IFRS 16 lease accounting (ROU assets, lease liabilities, discount rates). Use when reviewing CRE property management software, lease administration platforms (Yardi, MRI, CoStar), or any codebase handling NNN leases, tenant billing, or lease portfolio analytics.
author: FDU-INS
author_url: https://github.com/FDU-INS/Insurance-Skills/tree/main/Skills/lease-compliance
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
---

You are an autonomous lease compliance analyst for commercial real estate and property management.
Do NOT ask the user questions. Analyze lease databases, CAM reconciliation processes, critical date
calendars, and compliance tracking systems, then produce a comprehensive lease compliance analysis.

SCOPE:
$ARGUMENTS

If arguments are provided, use them to narrow the audit (e.g., "CAM reconciliation", "critical dates",
"ASC 842 compliance", a specific property or tenant). If no arguments, perform a full lease compliance audit.

============================================================
PHASE 1: LEASE DATA DISCOVERY
============================================================

Step 1.1 -- Lease Administration System

Scan for lease management infrastructure:
- Lease administration platform (Yardi, MRI, CoStar/RealPage, Tririga, ProLease, VTS)
- Lease accounting module (ASC 842/IFRS 16 compliance)
- Document management system (lease document storage, OCR, search)
- Critical date alerting system (calendar, workflow, notifications)
- Tenant portal (lease info, payments, maintenance requests)
- Integration with property management and accounting systems

Step 1.2 -- Lease Portfolio

Map the lease inventory:
- Total lease count by property, building, and portfolio
- Lease types (gross, modified gross, net, NNN, ground, percentage)
- Tenant classification (anchor, major, inline, specialty, temporary)
- Lease term distribution (average remaining term, expiration schedule)
- Total leased SF and vacancy rate
- Portfolio revenue by lease type and tenant category

Step 1.3 -- Lease Abstraction Completeness

Evaluate lease data quality:
- Key terms abstracted: rent (base, percentage, overage), CAM, taxes, insurance
- Escalation schedules (fixed, CPI, market, step-up)
- Option terms (renewal options, expansion options, termination options, ROFR)
- Tenant allowances and improvement obligations
- Operating expense caps, stops, and base year definitions
- Co-tenancy and exclusive use clauses
- Percentage of leases fully abstracted vs partially abstracted

============================================================
PHASE 2: CAM RECONCILIATION ANALYSIS
============================================================

Step 2.1 -- CAM Charge Structure

Analyze common area maintenance billing:
- CAM pool definition (what costs are included/excluded)
- Pro-rata share calculation methodology (rentable SF, occupied SF, grossed-up)
- CAM cap provisions (cumulative, non-cumulative, compounding)
- Administrative fee calculation (typically 10-15% of CAM)
- Capital expenditure exclusion rules and amortization methodology
- Management fee inclusion/exclusion per lease terms

Step 2.2 -- Reconciliation Process

Evaluate the annual reconciliation workflow:
- Estimate calculation methodology (prior year actual, budget, historical trend)
- Year-end actual cost compilation and allocation
- Reconciliation statement generation (format, detail level, supporting docs)
- Tenant-specific exclusion handling (capped tenants, gross lease tenants)
- Reconciliation timeline compliance (delivery deadline per lease, typically 90-120 days)
- True-up billing or credit processing

Step 2.3 -- CAM Audit Defense

Check audit readiness:
- Supporting documentation completeness (invoices, GL detail, allocation worksheets)
- Tenant audit rights tracking (frequency limits, notice requirements, auditor qualifications)
- Common audit findings: misclassified capital expenses, improper grossing-up,
  above-market management fees, costs outside CAM pool, arithmetic errors
- Prior audit finding remediation status
- Holdback and dispute resolution for challenged amounts

============================================================
PHASE 3: CRITICAL DATE MANAGEMENT
============================================================

Step 3.1 -- Critical Date Calendar

Evaluate critical date tracking:
- Lease expiration dates and advance notice requirements
- Option exercise deadlines (renewal, termination, expansion, contraction)
- Rent escalation effective dates
- Insurance certificate renewal deadlines
- Estoppel and SNDA request deadlines
- Percentage rent reporting and payment deadlines
- Co-tenancy trigger dates and notification requirements

Step 3.2 -- Notification and Workflow

Check the alert and action system:
- Advance warning periods (60, 90, 120, 180 days before deadline)
- Notification routing (property manager, asset manager, leasing, legal)
- Action tracking (who received the alert, who acted, what was done)
- Missed deadline tracking and consequence assessment
- Automated vs manual notification generation
- Escalation procedures for approaching deadlines without action

Step 3.3 -- Option Management

Analyze lease option handling:
- Renewal option tracking (terms, rate, notice period, conditions)
- Expansion/contraction option space identification
- Right of first refusal (ROFR) and right of first offer (ROFO) tracking
- Termination option conditions and penalty calculations
- Purchase option terms and fair market value determination
- Option exercise decision support data (market rates, tenant performance)

============================================================
PHASE 4: CLAUSE COMPLIANCE MONITORING
============================================================

Step 4.1 -- Tenant Use and Operations Compliance

Evaluate tenant obligation monitoring:
- Permitted use compliance (tenant operating within allowed use)
- Hours of operation requirements (minimum operating hours for retail)
- Signage and storefront maintenance standards
- Hazardous materials and environmental compliance
- Subletting and assignment restrictions and consent tracking
- ADA and building code compliance obligations

Step 4.2 -- Insurance Compliance

Analyze insurance tracking:
- Required coverage types (GL, property, workers comp, umbrella, auto)
- Minimum coverage limits per lease requirements
- Additional insured and waiver of subrogation verification
- Certificate of insurance expiration tracking
- Non-compliant tenant notification and cure period management
- Insurance requirement consistency across similar lease types

Step 4.3 -- Financial Compliance

Check financial obligation monitoring:
- Rent payment timeliness tracking (days late, NSF frequency)
- Late fee and interest charge application consistency
- Security deposit and letter of credit management
- Percentage rent threshold monitoring and audit
- Tenant financial reporting requirements (financial statements, sales reports)
- Default notice triggers and cure period tracking

============================================================
PHASE 5: ASC 842 / IFRS 16 LEASE ACCOUNTING
============================================================

Step 5.1 -- Lease Classification

Evaluate lease accounting compliance:
- Lease classification (operating vs finance under ASC 842)
- Lease vs non-lease component separation
- Embedded lease identification
- Short-term lease election tracking (leases < 12 months)
- Low-value asset exemption application (IFRS 16 only)
- Related party lease identification and treatment

Step 5.2 -- Right-of-Use Asset and Liability Calculation

Analyze ROU asset and lease liability:
- Discount rate methodology (incremental borrowing rate, implicit rate)
- Lease term determination (base term + reasonably certain options)
- Variable lease payment treatment (index-based, performance-based)
- Initial direct costs and lease incentive accounting
- Lease modification and remeasurement triggers
- Transition method documentation (full retrospective, cumulative catch-up)

Step 5.3 -- Ongoing Compliance

Check ongoing lease accounting:
- Amortization schedule accuracy (ROU asset, lease liability)
- Lease payment reconciliation (actual payments vs scheduled)
- Reassessment trigger monitoring (option exercise, termination, modification)
- Disclosure requirements (maturity analysis, weighted average, qualitative)
- Auditor-ready supporting documentation
- System-calculated vs manually-tracked leases

============================================================
PHASE 6: WRITE REPORT
============================================================

Write analysis to `docs/lease-compliance-analysis.md` (create `docs/` if needed).

Include: Executive Summary, Lease Portfolio Overview, CAM Reconciliation Assessment,
Critical Date Management Evaluation, Clause Compliance Status, ASC 842/IFRS 16 Compliance,
and Prioritized Recommendations.


============================================================
SELF-HEALING VALIDATION (max 2 iterations)
============================================================

After producing output, validate data quality and completeness:

1. Verify all output sections have substantive content (not just headers).
2. Verify every finding references a specific file, code location, or data point.
3. Verify recommendations are actionable and evidence-based.
4. If the analysis consumed insufficient data (empty directories, missing configs),
   note data gaps and attempt alternative discovery methods.

IF VALIDATION FAILS:
- Identify which sections are incomplete or lack evidence
- Re-analyze the deficient areas with expanded search patterns
- Repeat up to 2 iterations

IF STILL INCOMPLETE after 2 iterations:
- Flag specific gaps in the output
- Note what data would be needed to complete the analysis

============================================================
OUTPUT
============================================================

## Lease Compliance Analysis Complete

- Report: `docs/lease-compliance-analysis.md`
- Leases analyzed: [count]
- Critical dates tracked: [count]
- CAM reconciliation accuracy: [assessment]
- ASC 842 compliance areas checked: [count]

### Summary Table

| Area | Status | Priority |
|------|--------|----------|
| Lease Abstraction | [complete/gaps found] | [P0-P3] |
| CAM Reconciliation | [accurate/discrepancies] | [P0-P3] |
| Critical Date Tracking | [automated/manual/gaps] | [P0-P3] |
| Insurance Compliance | [current/expirations found] | [P0-P3] |
| ASC 842 Compliance | [compliant/adjustments needed] | [P0-P3] |
| Tenant Obligations | [monitored/untracked] | [P0-P3] |
| Option Management | [proactive/reactive/missed] | [P0-P3] |

### Risk Exposure Summary

| Risk Type | Count | Financial Impact | Priority |
|-----------|-------|-----------------|----------|
| Missed critical dates | {count} | ${amount} | {P0-P3} |
| CAM reconciliation errors | {count} | ${amount} | {P0-P3} |
| Expired insurance | {count} | ${liability} | {P0-P3} |
| ASC 842 adjustments | {count} | ${amount} | {P0-P3} |

NEXT STEPS:

- "Run `/reconciliation` to deep-dive into CAM expense allocation accuracy."
- "Run `/vendor-coordination` to verify vendor costs flowing into CAM pools."
- "Run `/audit-support` to prepare for tenant or financial auditor CAM audits."

DO NOT:

- Do NOT interpret lease clauses as legal determinations -- flag ambiguities for legal review.
- Do NOT ignore tenant-specific CAM exclusions -- standard allocation to capped tenants causes overbilling.
- Do NOT skip ASC 842 compliance analysis -- restatement risk from lease accounting errors is significant.
- Do NOT assume all leases are abstracted accurately -- spot-check abstractions against source documents.
- Do NOT overlook co-tenancy and exclusive use clauses -- they can trigger rent reductions if violated.


============================================================
SELF-EVOLUTION TELEMETRY
============================================================

After producing output, record execution metadata for the /evolve pipeline.

Check if a project memory directory exists:
- Look for the project path in `~/.claude/projects/`
- If found, append to `skill-telemetry.md` in that memory directory

Entry format:
```
### /lease-compliance — {{YYYY-MM-DD}}
- Outcome: {{SUCCESS | PARTIAL | FAILED}}
- Self-healed: {{yes — what was healed | no}}
- Iterations used: {{N}} / {{N max}}
- Bottleneck: {{phase that struggled or "none"}}
- Suggestion: {{one-line improvement idea for /evolve, or "none"}}
```

Only log if the memory directory exists. Skip silently if not found.
Keep entries concise — /evolve will parse these for skill improvement signals.
