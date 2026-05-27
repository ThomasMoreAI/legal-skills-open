---
name: form-10k
title: Form 10-K Annual Report
description: Drafts SEC Form 10-K Annual Reports under the Securities Exchange Act of 1934. Structures all four Parts with Regulation S-K compliance and GAAP financial integration. Use when drafting 10-K filings, annual reports, or public company annual SEC disclosures.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/form-10k
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: securities
language: en
tags: [corporate, drafting, memo, regulatory]
---

# Form 10-K Annual Report

Draft a complete Form 10-K pursuant to Section 13 or 15(d) of the Securities Exchange Act of 1934, compliant with Regulation S-K and GAAP.

## Gather Before Drafting

- **Prior SEC filings** — most recent 10-K, 10-Qs, 8-Ks, SEC comment letters
- **Audited financials** — balance sheets (2 yr), income/cash flow/equity statements (3 yr), auditor's report
- **Company records** — charter, bylaws, material contracts, board minutes
- **Compensation data** — equity awards, employment agreements, benefit plans
- **Risk/compliance** — ERM assessments, audit committee reports, litigation files
- **Stock/ownership** — transfer records, Schedule 13D/13G, Section 16 reports

## Cover Page

Include: registrant legal name, fiscal year end, Commission File Number, state of incorporation, EIN, principal office address, filer status (LAF/AF/NAF/SRC/EGC from public float + revenue), shell company status, aggregate market value of non-affiliate equity (closing price, last business day of most recent Q2).

## Part I — Business & Risk

**Item 1 — Business.** Draft in order: corporate history → products/services by segment (revenue %) → market size and share → competitive landscape (name competitors) → strategy → supply chain (sole-source dependencies) → IP portfolio → seasonality → customer concentration (≥10% of revenue) → regulatory environment → human capital (headcount, unions, CBAs).

**Item 1A — Risk Factors.** Organize by category (business/industry, technology/cyber, financial, legal/regulatory, key personnel, IP, capital/securities), most significant first within each. Each risk: specific heading → circumstances → exposure → triggers → quantified consequences. Flag new, escalated, diminished, or removed risks vs. prior year.

**Item 1B — Unresolved Staff Comments.** Disclose SEC comments issued ≥180 days before FYE still unresolved (substance, position, resolution steps). If none, state affirmatively.

**Item 2 — Properties.** Each material property: location, use, size, owned vs. leased, lease terms, encumbrances, capacity utilization, expansion plans.

**Item 3 — Legal Proceedings.** Each material proceeding (not routine): court, parties, claims, relief sought, company position, estimated loss/range, insurance, status. Environmental: disclose if sanctions could exceed lesser of $1M or 1% of current assets.

**Item 4 — Mine Safety.** Per Dodd-Frank §1503(a) if applicable; otherwise "Not applicable."

## Part II — Financial Performance

**Item 5 — Market/Equity/Dividends.** Exchange, ticker, quarterly price table (2 yr), holders of record, dividend history, Q4 repurchase table (monthly: shares, avg price, remaining authorization).

**Item 6 — Selected Financial Data.** Five-year table: revenue, income from continuing operations (total + per share), total assets, long-term obligations, dividends per share. Footnote comparability adjustments.

**Item 7 — MD&A.** Seven sections:
1. Executive overview — YoY performance, key metrics, major events
2. Results of operations — line-by-line YoY comparisons, quantify drivers (volume, price, FX, acquisitions)
3. Liquidity — operating/investing/financing cash flows, adequacy assessment
4. Capital resources — credit facilities (size, rate, maturity, covenants), capex plans
5. Contractual obligations — table (<1yr, 1-3yr, 3-5yr, >5yr)
6. Off-balance sheet arrangements — or affirmative negative statement
7. Critical accounting estimates — methodology, assumptions, sensitivity

**Item 7A — Market Risk.** Qualitative exposures (interest rate, FX, commodity) + hedging. Quantitative: tabular, sensitivity, or VaR per Item 305 Reg S-K.

**Item 8 — Financial Statements.** Balance sheets (2 yr), income/comprehensive income/cash flows/equity (3 yr), notes, auditor's report (GAAP + ICFR per SOX §404), supplementary quarterly data.

**Item 9 — Accountant Changes.** If change: date, firms, committee approval, disagreements, reportable events. If none, state affirmatively.

**Item 9A — Controls and Procedures.** CEO/CFO disclosure controls evaluation; management ICFR report (COSO framework); material weaknesses with remediation; Q4 ICFR changes.

**Item 9B — Other Information.** Q4 unreported 8-K events; Rule 10b5-1 arrangements adopted/modified/terminated. If none: "None."

## Part III — Governance & Compensation

May incorporate by reference from definitive proxy (filed ≤120 days after FYE); cite specific proxy sections.

**Item 10 — Directors/Officers/Governance.** Directors and officers (name, age, position, 5-yr experience, boards), committee membership + meeting counts, audit committee financial expert, code of ethics, nomination process.

**Item 11 — Executive Compensation.** CD&A (objectives, elements, say-on-pay response, metrics, clawback). Required tables: Summary Compensation (3 yr), Plan-Based Awards, Outstanding Equity, Options Exercised/Vested, Pension, Deferred Compensation (if applicable). Employment/severance/CIC terms. Director compensation table.

**Item 12 — Security Ownership/Equity Plans.** Beneficial ownership table (>5% holders, directors/NEOs, group total). Equity compensation plan table (approved vs. non-approved).

**Item 13 — Related Transactions/Independence.** Transactions exceeding lesser of $120K or 1% avg total assets: parties, terms, amounts, arm's-length comparison. Review policies. Director independence determinations.

**Item 14 — Accounting Fees.** Two-year table (audit, audit-related, tax, other). Pre-approval policies.

## Part IV — Exhibits & Signatures

**Item 15 — Exhibits.** Index per Item 601 Reg S-K. Required: charter/bylaws (3.x), security instruments (4.x), material contracts (10.x), code of ethics (14.1), subsidiaries (21.1), auditor consent (23.1), SOX §302 certs (31.x), SOX §906 certs (32.x), XBRL (101.x). Incorporated exhibits: cite filing type, date, exhibit number.

**Signatures.** Two blocks: (1) Section 13/15(d) — registrant, authorized officer, title, date; (2) Exchange Act — PEO, PFO, PAO/controller, majority of directors with conformed signatures.

## Drafting Rules

- Plain English per SEC guidance; no boilerplate or vague qualitative language
- Every assertion backed by specific facts, figures, or data
- Quantify trends with percentages and dollar amounts
- Internal consistency across all sections (financials, cross-references, exhibit citations)
- Financial statements: GAAP; narrative disclosure: Regulation S-K
- Flag incomplete data with `[DATA NEEDED]`, uncertain citations with `[VERIFY]`

## Filing Deadlines

| Filer Status | Deadline |
|---|---|
| Large Accelerated | 60 days after FYE |
| Accelerated | 75 days after FYE |
| Non-Accelerated | 90 days after FYE |

Form 12b-25 extends 15 days (good-cause showing required).

## Compliance Checklist

- [ ] All Items 1–15 addressed or cross-referenced
- [ ] Exhibits filed or incorporated with complete citations
- [ ] Financial data consistent across cover page, selected data, MD&A, and statements
- [ ] All signatures obtained and dated on/before filing
- [ ] XBRL tagging complete
- [ ] SOX §302 and §906 certifications executed
- [ ] EDGAR formatting verified
