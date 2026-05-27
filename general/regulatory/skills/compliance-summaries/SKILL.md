---
name: compliance-summaries
title: Compliance Summary
description: Generates structured compliance summaries assessing regulatory posture, identifying gaps, and producing prioritized remediation roadmaps across finance (SEC, FINRA), healthcare (HIPAA, FDA), environmental (EPA), and data privacy (GDPR, CCPA) sectors. Use when drafting regulatory compliance reports, audit readiness assessments, or governance documents for executives, boards, or regulators. For sector-specific depth, defer to dedicated sibling skills (environmental-regulation-summaries, hipaa-privacy-notice, fcpa-compliance-policy, etc.).
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/compliance-summaries
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
tags: [summary, analysis, summarization]
---

# Compliance Summary

Produces a governance-ready compliance summary with gap analysis and prioritized remediation roadmap. Outputs target dual audiences: board-level oversight and operational compliance teams.

---

## Related skills

This skill produces cross-sector compliance summaries. For sector-specific depth, defer to:

- **Environmental** — `environmental-regulation-summaries` (CAA / CWA / RCRA / CERCLA / NEPA / ESA / TSCA), `phase-i-esa` (Phase I ESA), `consent-decree-epa` (federal enforcement settlements), `nov-response` (regulatory NOVs).
- **Healthcare** — `hipaa-privacy-notice`, `hipaa-baa`, `hipaa-release`, `cpom-compliance`, `stark-law-aks-compliance`.
- **Financial services** — `bsa-risk-assessment`, `aml-compliance-program`, `cip-policy`, `reg-bi-policy`, `fcpa-compliance-policy`.
- **Data privacy** — `ccpa-policy`, `gdpr-data-processing-addendum`, `data-retention-and-destruction-policy`, `breach-notification`, `wisp`.
- **Government contracts** — `c-tpat-security-profile`, `dd-form-254`, `oci-mitigation-plan`, `subcontracting-plan`.

## Prerequisites

Before drafting, confirm:

1. **Sector and jurisdiction** — finance, healthcare, environmental, data privacy, or other; federal, state, or international scope
2. **Source documents** — compliance policies, internal audits, regulatory correspondence, incident reports, consent orders, prior summaries
3. **Scope** — full enterprise, specific business unit, or defined regulatory domain

## Output Structure

### 1. Executive Summary

| Field | Content |
|---|---|
| Overall Posture | Compliant / Substantially Compliant / Non-Compliant / Under Active Regulatory Scrutiny |
| Top 3 Risks | Ranked by severity and regulatory exposure |
| Immediate Action Items | Items requiring executive or board attention now |
| Review Period | Date range covered |

Write accessibly for non-lawyers. Detailed sections may use technical regulatory terminology.

### 2. Regulatory Requirements Matrix

For each applicable requirement, organize by regulatory domain (e.g., SEC/FINRA, HIPAA/FDA, EPA, CCPA/GDPR) or by business unit:

| Requirement | Citation | Obligation | Responsible Party | Deadline/Frequency | Penalty Exposure |
|---|---|---|---|---|---|

### 3. Compliance Status Assessment

For each requirement in the matrix:

- **Status**: Compliant | Gap Identified | Deficiency | Unknown/Insufficient Evidence
- **Supporting Evidence**: policies, training records, audit results, certifications, filings
- **Gap Description**: specific deficiency with factual basis
- **Remediation**: action steps, owner, target date, resource estimate

### 4. Compliance Infrastructure Assessment

Evaluate whether the organization has:

- Designated compliance officer(s) with appropriate authority
- Board-approved compliance program and policies
- Regular risk assessments with defined frequency
- Employee training program with completion tracking
- Monitoring and auditing cadence
- Incident response and breach notification procedures
- Escalation path to senior management and board
- Regulatory examination readiness protocols

### 5. Temporal Compliance Calendar

Track upcoming deadlines in a table covering: license/cert renewals, pending audits/exams, and upcoming regulatory changes requiring program modification. Include item, type, deadline, owner, and status.

### 6. Prioritized Action Plan

Rank remediation by: (1) regulatory deadline, (2) risk severity, (3) resource availability, (4) workstream dependencies.

| Priority | Action | Owner | Target Date | Success Metric |
|---|---|---|---|---|

## Checks

- **Cite precisely** — include CFR sections, statute numbers, and agency guidance identifiers; flag uncertain citations with `[VERIFY]`
- **Distinguish evidence quality** — separate documented compliance from self-reported or assumed compliance
- **Flag gray areas** — note regulatory interpretive uncertainty; recommend regulator engagement or outside counsel review where applicable
- **Emerging regulations** — flag anticipated regulatory changes requiring future program modification
- **No legal advice** — frame as compliance assessment; note where legal counsel review is required before reliance

---

## Troubleshooting

- **Multi-sector target.** When the entity operates across multiple regulated sectors, build the matrix sector-by-sector (one block per sector) rather than collapsing into a single matrix. Sector-specific terminology and citation conventions matter; mixing them produces an unauditable summary.
- **Privileged audit findings cited as evidence.** Privileged internal-audit reports cited verbatim may waive privilege. Use neutral re-statements ("internal review identified...") and cite the underlying factual record. Flag the privilege question in a footnote.
- **Rapidly-changing regulatory environment.** For domains in active rulemaking (e.g., AI / data privacy state laws, environmental disclosure rules, SEC climate disclosure), use a `[VERIFY as of YYYY-MM-DD]` marker and recommend re-verification within 90 days.
- **Cite to non-binding guidance.** Distinguish statutes (binding) from regulations (binding when properly promulgated) from agency guidance (often non-binding). Misrepresenting guidance as binding is a common error in compliance summaries.
- **Overlapping federal and state regimes.** State analogs may exceed federal minimums (e.g., CCPA vs. federal privacy patchwork). Always check the state floor; do not treat federal compliance as a safe harbor.
