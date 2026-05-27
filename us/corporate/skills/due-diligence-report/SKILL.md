---
name: due-diligence-report
title: Due Diligence Report
description: 'Produces U.S. corporate/M&A due diligence reports summarizing legal risks across corporate records, contracts, liabilities, regulatory compliance, and IP. Use when drafting a diligence report, red flags memo, or legal risk summary for acquisitions, asset purchases, minority investments, or financing. Trigger keywords: due diligence, diligence report, red flags, M&A, acquisition, target review, HSR, CFIUS, reps and warranties, indemnity.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/due-diligence-report
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
---

# Due Diligence Report

Deliver a structured legal risk report that supports deal decisions and negotiation strategy.

## Prerequisites

1. **Transaction overview** — structure, parties, valuation, timeline, governing law, closing conditions.
2. **Data room index** — document list with dates, versions, and confidentiality labels.
3. **Diligence scope** — materiality thresholds (revenue %, dollar threshold, key customers).
4. **Deal sensitivities** — regulatory approvals, IP dependencies, key contracts, employee retention.
5. **Prior work product** — existing diligence memos or red-flag lists, if any.

## Output Structure / Process

### 1) Report Sections

1. Executive summary — top 5–10 risks, required approvals, open items.
2. Risk rating framework.
3. Findings matrix (issue-level table).
4. Area analyses: Corporate/Cap Table, Material Contracts, Litigation/Claims, Regulatory/Compliance, IP/Technology, Employment/Benefits, Real Estate/Leases, Taxes, Data Privacy/Cybersecurity, Environmental, Insurance, Other as applicable.
5. Open items and follow-up requests.
6. Deal protections and drafting recommendations.

### 2) Risk Ratings

| Rating | Definition | Deal Impact |
|---|---|---|
| Critical | Likely deal-breaker or closing condition | Resolve pre-close or terminate |
| Significant | Material value/operations impact | Address with price, reps, indemnity, escrow |
| Moderate | Manageable risk | Address with covenants or post-close plan |
| Minor | Low impact | Note for awareness |

### 3) Findings Matrix Template

| Area | Issue | Source (Doc/§/Date) | Risk | Exposure/Impact | Recommendation | Proposed Deal Protection |
|---|---|---|---|---|---|---|

### 4) Area Checklist

| Area | Required Checks |
|---|---|
| Corporate/Cap Table | Formation docs; charter/bylaws; equity issuances; options/RSUs; board/stockholder approvals; subsidiaries; liens |
| Material Contracts | Change-of-control; assignment; exclusivity; MFN; termination; renewals; pricing; SLAs; non-compete; key customer/supplier concentration |
| Litigation/Claims | Pending/threatened claims; settlements; subpoenas; arbitration; investigations |
| Regulatory/Compliance | Licenses/permits; sanctions/export; antitrust/HSR; CFIUS; industry regulators; SEC/FINRA if applicable |
| IP/Technology | Chain of title; employee/contractor assignment; OSS compliance; licenses in/out; infringement claims; domains |
| Employment/Benefits | Key employee agreements; non-solicit; wage/hour claims; benefits plans; 401(k); union matters |
| Taxes | Returns; audits; NOLs; sales/use tax; transfer pricing; tax sharing agreements |
| Privacy/Cybersecurity | Privacy policies; DPAs; breach history; security audits; data localization; HIPAA/GLBA/FERPA if applicable |
| Real Estate | Leases; environmental reports; zoning; landlord consent |
| Environmental | Permits; contamination; remediation obligations; indemnities |
| Insurance | Coverage types; exclusions; claims history; tail coverage |

### 5) Executive Summary Template

```text
Executive Summary
- Critical risks: [Issue | Impact | Required action]
- Significant risks: [Issue | Impact | Proposed deal protection]
- Required approvals: [HSR/CFIUS/Industry/Other]
- Open items: [Missing docs or confirmations]
```

### 6) Deal Protections Mapping

| Risk Type | Drafting Lever |
|---|---|
| Known liability | Specific indemnity; escrow; special rep |
| Compliance gap | Pre-close covenant; condition to close |
| Contract consent | Closing condition; bring-down |
| IP ownership gap | Assignment; rep; escrow holdback |
| Litigation exposure | Litigation rep; cap; survival term |

### 7) Citation Format

- Quote only material clauses; cite as `DocName §X (Date)`.
- Flag missing or inconsistent documents in the open items section.

## Guidelines

- Maintain neutral, risk-focused tone; avoid advocacy.
- Tie each issue to evidence and transaction impact.
- Use `[VERIFY]` for any legal citation or regulatory threshold not confirmed.
- Assume U.S. transaction unless specified; call out non-U.S. jurisdictions explicitly.
- Separate factual findings from recommendations.
- Do not invent documents or confirm approvals without evidence.
