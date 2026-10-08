---
name: pa-workflow-regulatory-compliance-gap-matrix-sboghossian
title: Regulatory — Compliance Gap Matrix
description: Use when counsel or a compliance team needs to map a client's current compliance posture against applicable regulatory requirements and produce a prioritized remediation plan. Generates a structured gap matrix showing each regulation, current compliance state (compliant / partial / non-compliant), risk severity, remediation effort, and target date. MENA-focused (CBUAE, SAMA, SDAIA, VARA, DFSA, FSRA) with multi-jurisdiction support.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-regulatory-compliance-gap-matrix
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Regulatory — Compliance Gap Matrix

## Purpose

A compliance gap matrix is the foundational tool for any regulatory assessment engagement. This workflow takes a defined regulatory framework (or set of frameworks) and a client's current policies, procedures, and operational state, then produces a structured gap matrix with risk scoring and a prioritized remediation plan suitable for presentation to the board, management, or the regulator.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Applicable regulations / frameworks | Yes | By name and jurisdiction — e.g., CBUAE AML/CFT framework, SAMA Cybersecurity Framework, GDPR, PDPL |
| Client policies and procedures | Recommended | Upload current policy documents; the gap analysis compares these against requirements |
| Client's industry sector | Yes | Determines which regulations apply and their materiality |
| Client's jurisdiction(s) of operation | Yes | Drives the regulatory universe |
| Prior regulatory inspection findings | If available | Escalate gaps flagged by a regulator |
| Risk appetite statement | Optional | Informs remediation prioritization |
| Remediation budget / timeline constraints | Optional | Enables realistic target-date setting |

## Gap Matrix Structure

### Regulation mapping

First, build the regulatory universe applicable to the client:

| Regulation | Issuing body | Jurisdiction | Applicability to client |
|---|---|---|---|
| AML/CFT Federal Decree-Law | CBUAE | UAE | Yes — licensed financial institution |
| Personal Data Protection Law (PDPL) | SDAIA | KSA | Yes — processes Saudi residents' data |
| DIFC Data Protection Law 2020 | DIFC Commissioner of Data Protection | DIFC | Yes — DIFC entity |
| SAMA Cybersecurity Framework | SAMA | KSA | Yes — licensed with SAMA |
| EU GDPR | European Data Protection Board | EU | Potentially — if EU customers |

### Gap scoring per requirement

For each material requirement within each regulation:

| Req. # | Requirement | Evidence reviewed | Current status | Gap description | Risk level | Remediation effort | Target date |
|---|---|---|---|---|---|---|---|
| AML-03 | Customer Due Diligence policy covering PEPs | Existing AML policy | PARTIAL | Policy covers standard CDD; PEP enhanced due diligence section is incomplete; no documented PEP screening process | HIGH | Medium (4–6 weeks) | 2025-07-01 |
| PDPL-08 | Data Subject Rights response process | No documented process | NON-COMPLIANT | No process for responding to access / deletion requests within 30-day PDPL window | HIGH | High (8–12 weeks) | 2025-09-01 |
| SAMA-CYB-02 | Incident response plan tested annually | Last test dated 2021 | PARTIAL | Plan exists but not tested in 3 years; results not documented | MEDIUM | Low (2 weeks) | 2025-06-01 |

**Status codes:**
- **COMPLIANT**: requirement is fully met with documented evidence
- **PARTIAL**: requirement is partially met; identifiable gaps
- **NON-COMPLIANT**: requirement is not met; no evidence of implementation
- **NOT APPLICABLE**: requirement does not apply to this client's profile (document reason)

**Risk levels:**

| Level | Definition |
|---|---|
| CRITICAL | Non-compliance is likely to result in regulatory sanction, license suspension, or criminal referral |
| HIGH | Non-compliance would likely result in a regulatory warning, fine, or public enforcement action |
| MEDIUM | Non-compliance would likely result in a management letter or remediation notice |
| LOW | Non-compliance is a procedural gap; unlikely to attract regulatory attention in isolation |

**Remediation effort** estimates time from start to complete for a competent team:

| Level | Weeks |
|---|---|
| Low | 1–3 |
| Medium | 4–8 |
| High | 9–20 |
| Very High | 20+ (structural change, regulatory approval required) |

## Executive Summary

Produce a one-page summary for management / board:

```markdown
## Compliance Gap Summary — [Client Name] — [Date]

**Regulations assessed**: 6
**Requirements reviewed**: 94
**Compliant**: 61 (65%)
**Partial**: 19 (20%)
**Non-compliant**: 14 (15%)

**Critical gaps (immediate action required)**: 3
**High gaps**: 8
**Medium gaps**: 15
**Low gaps**: 7

**Estimated remediation timeline**: 12–18 months for full compliance
**Estimated effort**: Medium-High (requires dedicated compliance resource)

**Top 3 priorities**:
1. AML/CFT PEP screening process (CRITICAL — CBUAE inspection scheduled Q3)
2. PDPL data subject rights process (HIGH — SDAIA has begun enforcement)
3. SAMA cybersecurity incident response testing (MEDIUM — remediation is straightforward)
```

## Remediation Roadmap

Output a sequenced remediation plan:

| Phase | Timeframe | Gaps addressed | Owner | Status |
|---|---|---|---|---|
| Phase 1 — Critical | Weeks 1–8 | 3 CRITICAL gaps | Legal + Compliance | In progress |
| Phase 2 — High | Weeks 5–20 | 8 HIGH gaps | Compliance + Operations | Not started |
| Phase 3 — Medium | Months 4–12 | 15 MEDIUM gaps | Operations + IT | Not started |

Sequence rationale:
- CRITICAL gaps with imminent regulatory inspection dates first
- Gaps requiring third-party vendors or regulatory approval early (long lead times)
- Process gaps before technology gaps (processes validate what technology is needed)
- Quick wins (LOW effort / HIGH risk) promoted even if lower risk — visible progress

## MENA Regulatory Context

- **CBUAE (UAE)**: AML/CFT inspections are annual for financial institutions; non-compliance results in fines under UAE Federal AML Law. Governance and board-level AML accountability are increasingly scrutinized.
- **SAMA (KSA)**: Cybersecurity framework compliance is formally assessed. Open Banking regulations are in active implementation. SAMA has issued formal enforcement actions against financial institutions publicly since 2022.
- **SDAIA / NDMO (KSA)**: Personal Data Protection Law (PDPL) entered force 2024. Data subject rights and cross-border transfer requirements are the most common gaps for multinationals operating in Saudi Arabia.
- **DIFC**: DFSA conducts annual risk-based supervision. A gap matrix is useful both for preparing for a DFSA inspection and for demonstrating remediation progress post-inspection.
- **ADGM**: FSRA supervision model is similar to DFSA. ADGM entities subject to GDPR-equivalent data protection through the ADGM DP Regulations 2021.
- **Lebanon**: BDL circulars impose compliance obligations; enforcement capacity is weakened by the banking sector crisis but regulatory obligations remain in force.
- **Egypt**: CBE and FRA regulate their sectors actively. AML compliance is under FATF assessment scrutiny.

## Output Formats

- **Full matrix**: spreadsheet/table with all requirements, gap scores, and evidence
- **Executive summary**: one-page board-ready overview
- **Remediation roadmap**: Gantt-style or phased action plan
- **Regulator-ready format**: structured for submission to a regulator as evidence of remediation commitment

## Related Skills

- [[pa-workflow-regulatory-client-alert-drafter-firm-voice]]
- [[pa-workflow-regulatory-cross-jurisdiction-tracker]]
- [[pa-workflow-regulatory-enforcement-likelihood-scorer]]
- [[pa-workflow-regulatory-daily-digest-publisher]]
