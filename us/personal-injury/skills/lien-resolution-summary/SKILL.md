---
name: lien-resolution-summary
title: Lien Resolution Summary
description: Generates a structured internal lien resolution summary for personal injury settlement cases. Triggers when resolving liens post-settlement, preparing settlement distribution statements, or auditing lien payoffs across health insurance subrogation, Medicare/Medicaid, hospital liens, workers' comp, and ERISA plans.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/lien-resolution-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
tags: [litigation, summarization, summary]
---

# Lien Resolution Summary

Internal tracking memorandum documenting identification, negotiation, resolution, and satisfaction of all liens against personal injury settlement proceeds. Mark output as **privileged/confidential attorney work product** — do not distribute to lienholders.

## Prerequisites

Gather before starting:

1. **Settlement agreement** — gross amount, distribution terms, holdback provisions
2. **Lien demand letters/notices** — from all asserting parties
3. **Medical billing records** — itemized statements, EOBs per lienholder
4. **Negotiation correspondence** — reduction requests, responses, final agreements
5. **Satisfaction documents** — releases, discharges, confirmation letters (if available)

## Workflow

### Step 1: Executive Overview

Produce a header table:

| Field | Content |
|-------|---------|
| Case caption | Parties, court, case number |
| Settlement date | Date funded |
| Total settlement | Gross amount |
| Aggregate liens asserted | Sum of initial claims |
| Aggregate liens resolved | Sum of final payments |
| Total savings | Dollar amount + percentage |
| Net to client | After liens, fees, costs |
| Resolution status | All resolved / X pending |

### Step 2: Classify Lienholders

Categorize each lien:

| Category | Legal Basis |
|----------|-------------|
| Private health insurance | Contractual subrogation, policy terms |
| Medicare/Medicaid | 42 U.S.C. § 1395y(b) (MSP) |
| Hospital/provider statutory | State hospital lien statutes |
| Workers' compensation | State WC subrogation statutes |
| ERISA plans | 29 U.S.C. § 1132(a)(3); *US Airways v. McCutchen* |
| Other (VA, Tricare, disability) | Varies by program |

For each lienholder record: legal name, claim/reference number, contact, legal basis (statutory cite or policy provision), and priority position.

### Step 3: Lien Detail Table

For **each** lien, produce a row covering:

- **Lienholder** — name + category
- **Initial amount claimed** and date of notice
- **Calculation method** — full benefits paid / % of settlement / other
- **Disputed items** — unrelated treatment, duplicates, excessive charges
- **Reduction arguments** — made-whole, common fund, comparative fault, fee sharing, statutory caps
- **Legal authority cited** — statute, case law, policy language
- **Final agreed amount** and reduction achieved ($ + %)
- **Payment terms** — due date, method, payee
- **Conditions** — release required, dismissal of enforcement action
- **Satisfaction status** — obtained/pending with date; identify supporting docs

### Step 4: Outstanding Issues

For unresolved liens or contingent claims, document:

- **Unresolved liens** — delay reason, negotiation status, anticipated timeline
- **Potential future claims** — Medicare conditional payments not yet identified, non-responsive carriers
- **Holdback funds** — amount reserved, release conditions
- **Financial exposure** — worst-case liability per outstanding item

### Step 5: Financial Summary

Reconciliation table (must tie to settlement distribution statement):

| Line Item | Amount |
|-----------|--------|
| Gross settlement | $ |
| Less: Attorney fees | ($ ) |
| Less: Costs | ($ ) |
| Less: Lien payments (itemize each) | ($ ) |
| **Net to client** | **$** |
| Total liens initially claimed | $ |
| Total liens paid | $ |
| **Total negotiated savings** | **$ (XX.XX%)** |

### Step 6: Compliance Checklist

- [ ] Medicare Section 111 reporting completed (42 U.S.C. § 1395y(b)(8))
- [ ] CMS final conditional payment letter obtained
- [ ] ERISA plan notification/appeal deadlines met
- [ ] State hospital lien satisfaction filed with court/recorder (if applicable)
- [ ] All lien releases executed and originals filed
- [ ] Client provided final distribution breakdown
- [ ] Records retention schedule documented

## Pitfalls and Checks

- **Medicare liens**: non-negotiable on validity — only dispute specific line items (unrelated treatment, amount errors). Use BCRC process; document final conditional payment from CMS.
- **Made-whole doctrine**: available in most states for equitable subrogation; generally unavailable against ERISA plans (*FMC Corp. v. Holliday*; *US Airways v. McCutchen*). Verify state law.
- **Common fund doctrine**: argue proportionate fee/cost reduction. Many states require insurers to share procurement costs. Not applicable to Medicare.
- **State lien caps**: several states cap hospital lien amounts or provide statutory reduction formulas. Cite the specific statute.
- **Precision**: all dollar amounts stated exactly; percentages to two decimal places. Every figure must reference source documentation.
- **Metadata**: include preparer name, date, and version number on every draft.
