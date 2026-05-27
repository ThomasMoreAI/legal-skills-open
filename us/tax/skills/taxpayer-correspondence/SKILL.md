---
name: taxpayer-correspondence
title: Taxpayer Correspondence
description: Drafts structured taxpayer correspondence summarizing tax records, income, deductions, credits, and tax positions. Covers IRS/state inquiry responses, audit preparation, advisor-client communications, and filing support. Use when drafting tax summary letters, responding to tax authority notices, preparing audit defense correspondence, or organizing client tax records into structured summaries.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/taxpayer-correspondence
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: tax
language: en
tags: [analysis, drafting, letter, regulatory, summarization, summary]
---

# Taxpayer Correspondence

Drafts structured correspondence summarizing tax records and financial information for authority responses, audit preparation, or advisor-client communication.

## Prerequisites

Gather before drafting:

- **Tax returns** — federal and state for relevant years
- **Income documents** — W-2s, 1099s (INT, DIV, MISC, NEC, B, R, SSA), K-1s
- **Deduction/credit support** — receipts, 1098s, 1098-Ts, charitable records
- **Financial statements** — bank/brokerage statements, business P&L if applicable
- **Authority correspondence** — IRS/state notices, inquiry letters, audit notifications
- **Filing context** — filing status, dependents, estimated payment history

## Quick Start

1. Collect all source documents for the relevant tax year(s)
2. Build the identification block with taxpayer info and purpose
3. Populate income, deductions, and credits — tie every figure to a source document
4. Summarize tax position (liability, withholding, balance due/refund)
5. If responding to a notice/audit, add the authority response section
6. Run the compliance checklist
7. List next steps with deadlines bolded

## Output Structure

### 1. Identification Block

| Field | Content |
|-------|---------|
| Taxpayer Name | Full legal name |
| TIN | Last four only (XXX-XX-####) |
| Tax Year(s) | All years covered |
| Filing Status | MFJ / MFS / Single / HOH / QSS |
| Purpose | Response to [notice] / Audit prep / Filing support / Advisory summary |
| Reference No. | IRS notice or case number if applicable |

### 2. Income Summary

Organize by IRC category. Reconcile each line to source documents. Flag discrepancies between 1099 reporting and return amounts.

| Category | Amount | Source Document |
|----------|--------|-----------------|
| Wages & Salaries (Line 1) | $ | W-2 from [employer] |
| Self-Employment (Sch C) | $ | 1099-NEC, P&L |
| Interest (Sch B) | $ | 1099-INT |
| Dividends (Sch B) | $ | 1099-DIV |
| Capital Gains/Losses (Sch D) | $ | 1099-B |
| Rental Income (Sch E) | $ | Lease agreements |
| Retirement Distributions | $ | 1099-R |
| Other Income | $ | [specify] |
| **Adjusted Gross Income** | **$** | |

### 3. Deductions & Credits

**Deductions:**

| Deduction | Amount | Authority | Documentation |
|-----------|--------|-----------|---------------|
| Standard / Itemized | $ | IRC §63 | |
| Mortgage Interest | $ | IRC §163(h) | Form 1098 |
| SALT (capped $10K) | $ | IRC §164 / TCJA §11042 | State returns, property tax bills |
| Charitable Contributions | $ | IRC §170 | Receipts, acknowledgment letters |
| Business Expenses | $ | IRC §162 | Receipts, mileage logs |
| Retirement Contributions | $ | IRC §219 / §401(k) | Plan statements |
| HSA Contributions | $ | IRC §223 | Form 5498-SA |

**Credits:**

| Credit | Amount | Authority | Eligibility Basis |
|--------|--------|-----------|-------------------|
| Child Tax Credit | $ | IRC §24 | Qualifying children, AGI phase-out |
| EITC | $ | IRC §32 | Income limits, qualifying children |
| Education Credits | $ | IRC §25A | 1098-T, enrollment verification |
| Energy Credits | $ | IRC §25C/§25D | Manufacturer certification |

### 4. Tax Position Summary

| Item | Amount |
|------|--------|
| Total Tax Liability | $ |
| Withholding (W-2, 1099) | $ |
| Estimated Payments (1040-ES) | $ |
| Credits Applied | $ |
| **Balance Due / (Refund)** | **$** |

Include: prior-year carryforwards (NOLs, capital losses, credits), amended return history, and open statute-of-limitation periods (3 years per IRC §6501; 6 years if >25% gross income omission).

### 5. Authority Response Section

_Include only when responding to IRS/state notice or audit._

- **Notice/Issue Identification** — restate each item questioned
- **Position & Support** — for each item: taxpayer's position, legal authority (IRC, Treas. Reg., Rev. Rul., case law), and supporting documentation
- **Penalty Abatement** — reasonable cause (IRC §6664(c)), first-time abatement, reliance on professional advice

### 6. Compliance Checklist

- [ ] Filing status appropriate and documented
- [ ] All income reconciled to information returns
- [ ] Estimated payments meet safe harbor (IRC §6654 — 100% prior year or 90% current; 110% if AGI >$150K)
- [ ] Penalties calculated: failure to file (§6651(a)(1)), failure to pay (§6651(a)(2)), accuracy-related (§6662)
- [ ] Record retention met (3-7 years)

### 7. Recommendations & Next Steps

Prioritize time-sensitive items with **bold deadlines**. Include actions required, documents to gather, estimated payments due, and planning opportunities. Flag statute-of-limitation or response deadlines prominently.

## Pitfalls & Checks

- **Privacy** — never include full SSN/TIN; last four digits only
- **Reconciliation** — tie every figure to a source document; note unresolved discrepancies explicitly
- **No fabrication** — identify document gaps; never estimate or fabricate figures
- **Uncertainty** — disclose reasoning and uncertainty level for ambiguous positions
- **Audience tone** — plain language for clients; precise IRC terminology for authority responses
- **Circular 230** — include disclaimer on written tax advice when applicable; do not provide covered opinions without appropriate disclaimers
- **State considerations** — address state-specific conformity or decoupling from federal provisions
