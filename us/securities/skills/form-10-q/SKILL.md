---
name: form-10-q
title: Form 10-Q Quarterly Report
description: 'Drafts SEC-compliant Form 10-Q quarterly reports covering Part I financials, MD&A, market risk, controls, Part II updates, exhibits, and SOX certifications. Use when preparing quarterly SEC filings, EDGAR-ready 10-Qs, or interim disclosure packages. Trigger keywords: Form 10-Q, quarterly report, MD&A, Regulation S-K, Regulation S-X, SOX 302, SOX 906, XBRL, EDGAR, interim financial statements.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/form-10-q
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: securities
language: en
tags: [corporate, drafting, regulatory, summary]
---

# Form 10-Q Quarterly Report

Produce an SEC-compliant quarterly report with required financial and non-financial disclosures.

## Prerequisites

1. Registrant identity: legal name, EIN, SEC file number, ticker/exchange, jurisdiction, principal office address, phone.
2. Quarter-end date and filer status classification (large accelerated, accelerated, non-accelerated, smaller reporting, emerging growth).
3. Prior Form 10-K and most recent 10-Q for roll-forward disclosures.
4. Unaudited interim financial statements with footnote support under GAAP.
5. MD&A variance drivers, segment data, liquidity data (cash flows, credit facilities, covenants, capital plans).
6. Market risk exposures, hedging activities, disclosure controls evaluation, ICFR changes.
7. Legal proceedings updates, risk factor changes, equity transactions, mine safety data if applicable.
8. Exhibit list, SOX certifications, XBRL tag set.

## Output Structure / Process

### Cover Page

Exact registrant name, quarter-end date, SEC file number, EIN, address/phone, jurisdiction, ticker/exchange, filer status checkboxes, shell company status. Must conform to Form 10-Q cover page format and match EDGAR header data [VERIFY].

### Part I — Financial Information

**Item 1 — Financial Statements** (Reg S-X Article 10 [VERIFY]):

- Condensed balance sheet: current quarter end and prior fiscal year end
- Condensed income statement: quarter and YTD with prior-year comparatives
- Condensed comprehensive income: quarter and YTD with comparatives
- Condensed cash flows: YTD with prior-year comparative
- Condensed stockholders' equity
- Footnotes: significant policies, estimate changes, contingencies, subsequent events, segments, EPS/dilution, related-party transactions

**Item 2 — MD&A** (Reg S-K Item 303 [VERIFY]):

```text
Executive Overview
Results of Operations
Liquidity and Capital Resources
Known Trends, Events, Demands, Commitments, and Uncertainties
Critical Accounting Policies and Estimates (if material changes)
```

Quantify material changes; explain volume, price, mix, and cost drivers.

**Item 3 — Market Risk**: If no material change since 10-K, state so. Otherwise quantify exposures using tabular, sensitivity, or VaR format.

**Item 4 — Controls and Procedures**: Disclosure controls evaluation per Exchange Act Rules 13a-15(e)/15d-15(e) [VERIFY]; ICFR changes; evaluation within 90 days of filing [VERIFY].

### Part II — Other Information

| Item | Content | Key Rules |
|------|---------|-----------|
| 1 — Legal Proceedings | Updates to pending matters | Reg S-K Item 103 [VERIFY]; 10% of current assets threshold [VERIFY] |
| 1A — Risk Factors | Material changes only | Tailored captions; quantify impacts |
| 2 — Equity Transactions | Unregistered sales; issuer repurchases | Securities Act exemption [VERIFY]; Rule 10b-18 if used [VERIFY] |
| 3 — Defaults | Senior securities defaults | Disclose if >5% of total assets; dividend arrearages |
| 4 — Mine Safety | Dodd-Frank §1503(a) [VERIFY] | If applicable |
| 5 — Other Information | Unreported 8-K items; 10b5-1 trading arrangement updates [VERIFY] | |
| 6 — Exhibits | Index per Reg S-K Item 601 [VERIFY] | Include Exhibits 31.1, 31.2, 32.1 [VERIFY] |

**Repurchase table format** (Item 2):

| Month | Total Shares Purchased | Avg Price Paid | Shares Under Public Program | Max Shares/$ Remaining |
|-------|------------------------|----------------|-----------------------------|------------------------|

**Exhibits index format**:

| Exhibit No. | Description | Filing Method | Source Filing and Date |
|-------------|-------------|---------------|------------------------|

### Signatures and EDGAR

- Authorized officer and principal financial/accounting officer signatures with dates.
- Filing deadlines: 40 days (large accelerated/accelerated) or 45 days (non-accelerated) after quarter end [VERIFY].
- EDGAR HTML/ASCII formatting, XBRL tags, Exhibit 101 if required [VERIFY].

## Quality Checks

- Cross-foot all financial statements; reconcile to MD&A and notes.
- Verify cross-references, exhibit numbers, and incorporation-by-reference cites.
- Confirm units and rounding consistency across the filing.
- Confirm legal proceedings align with contingencies footnote.
- Confirm risk factor updates reflect only material changes since last filing.
- Confirm certification text matches required SEC form language.
- Validate EDGAR formatting and XBRL tagging.

## Guidelines

- Use company-specific, quantified explanations; avoid boilerplate.
- Mark uncertain regulatory citations with `[VERIFY]`.
- If an item has no material update, state explicitly or omit per form instructions.
- Do not incorporate SOX 906 exhibits into Securities Act registration statements [VERIFY].
- Apply plain English standards per Rule 421(d) of Regulation C [VERIFY].
- Coordinate with finance and legal to align disclosures with GAAP and SEC rules.
