---
name: labor-violation-summary
title: Labor Violation Summary
description: Produces structured summaries of labor law violation investigations with categorized findings, evidence citations, affected worker counts, and remedial recommendations. Covers wage/hour (FLSA), OSHA safety, and worker rights (NLRA) violations. Use when summarizing labor investigations, compliance audits, OSHA inspections, wage theft findings, or workplace safety enforcement actions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/labor-violation-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
---

# Labor Violation Summary

Distills inspection reports, payroll records, witness statements, and regulatory findings into a categorized violation analysis with evidence citations and remedial actions.

## Prerequisites

Gather before starting:

- Inspection reports, regulatory findings, citations, agency correspondence
- Payroll and timekeeping records (for wage/hour quantification)
- Witness statements, filed complaints, interview transcripts
- OSHA logs, incident reports, safety audit results
- Settlement agreements, consent decrees, or pending litigation filings

## Quick Start

1. Identify all violation categories present (wage/hour, safety, worker rights)
2. Build the Executive Overview table
3. Document each violation using the category-specific fields below
4. Assess culpability indicators
5. Compile remedial actions with deadlines and status
6. Flag open items and unresolved disputes

## Output Structure

### 1. Executive Overview

| Field | Content |
|-------|---------|
| Employer/Entity | Name, location(s), industry |
| Investigation Period | Date range |
| Investigating Agency | DOL WHD, OSHA, NLRB, state agency |
| Violation Categories | Wage/hour, safety, worker rights |
| Workers Affected | Total count, by category |
| Status | Confirmed, preliminary, or ongoing |

### 2. Violation Findings

One section per category. For each violation found, capture these fields:

**A. Wage and Hour** — Violation type (unpaid overtime, minimum wage, misclassification, illegal deductions, missed breaks) · Applicable law (FLSA § ___, state law § ___ [VERIFY against jurisdiction]) · Workers affected (count) · Time period · Back wages owed (amount + calculation basis) · Evidence (document name, page, date) · Willfulness (negligent vs. willful — affects FLSA SOL: 2 yr vs. 3 yr)

**B. Workplace Safety** — Hazard/condition · OSHA standard violated (29 CFR § ___) · Classification (other-than-serious, serious, willful, repeat) · Injuries/illnesses · Prior employer notice · Missing controls (PPE, training, protocols) · Penalty assessed (amount + citation number)

**C. Worker Rights** — Violation type (retaliation, union interference, discrimination, FMLA denial, whistleblower reprisal) · Applicable law (NLRA § 7/8, Title VII, FMLA, state equivalents) · Targeted workers (who, how many) · Adverse actions (termination, demotion, schedule changes, threats) · Evidence (temporal proximity, documented statements, pattern evidence)

### 3. Culpability Assessment

Check all that apply:

- [ ] Negligence / lack of knowledge
- [ ] Willful disregard
- [ ] Concealment or record destruction
- [ ] Worker intimidation or investigation interference
- [ ] Prior violations or warnings on record
- [ ] Repeat violation status

### 4. Remedial Actions

| Action | Details | Deadline | Status |
|--------|---------|----------|--------|
| Back wage payments | Amount, recipients | | |
| Penalties/fines | Amount, agency | | |
| Policy changes | Specific policies | | |
| Safety corrections | Equipment, training, protocols | | |
| Worker reinstatement | Names, positions | | |
| Monitoring/reporting | Frequency, duration | | |
| Settlement terms | Key obligations | | |

### 5. Open Items

- Ongoing investigation areas and pending steps
- Parallel private litigation relationship to administrative findings
- Unresolved factual disputes (state each side's evidence)

## Pitfalls and Checks

- **Label violation status** — Mark every finding as alleged, preliminary, or confirmed
- **Cite every assertion** — Document name, page, date; no unsupported claims
- **Disputed facts** — Present both sides with supporting evidence
- **Multi-site investigations** — Organize findings by location or department
- **Pattern flagging** — Recurring violations across time/location affect penalty severity and willfulness determinations
- **Quantify always** — Dollar amounts, worker counts, date ranges
- **Statutory references** — Cite specific sections; mark [VERIFY] when jurisdiction-specific numbers are uncertain
