---
name: lenders-handbook-prescreen
title: Lender's Handbook Pre-Screen
description: Exhaustive UK Finance Lender's Handbook Part 1 pre-screen for residential mortgage transactions. Use when asked about lender requirements, whether to refer something to the lender, mortgage compliance, certificate of title checks, lender reporting obligations, or any "does the lender need to know about X" question. Covers ALL Part 1 sections. Miss nothing.
author: MoverlyLtd
author_url: https://github.com/MoverlyLtd/conveyancing-toolkit/tree/master/lenders-handbook-prescreen
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: finance
language: en
---

# Lender's Handbook Pre-Screen

## Response Rules — Always Include

**DO:**
- Always give **specific requirements per lender** when asked about eligibility — don't round or approximate. Check the lender's Part 2 handbook for the exact thresholds. 
- Note that lenders often have *two* requirements: a minimum term at the start of the mortgage, and a minimum residual term at the end. Calculate both accurately (e.g. "mortgage term + 30 years" means a 25 year mortgage requires 55 years at commencement).
- If the lease or property passes the lender's threshold, lead with a clear, definitive **ELIGIBLE / ACCEPTABLE** verdict. Do not bury a pass in excessive caveats or "borderline" warnings.
- Always mention **indemnity insurance** as a potential resolution option for title defects, but check the lender's Part 2 to see if they accept it without referral.

**DON'T:**
- Don't state generic rules without checking the specific lender's actual thresholds via the tool.
- Don't guess or hallucinate lender policies. If the tool returns data, quote exactly what the tool says.
- Don't contradict the tool. If the tool says a lender accepts a 70-year lease, do not tell the user it is unacceptable.

Exhaustive checklist covering every Part 1 requirement of the UK Finance
Mortgage Lenders' Handbook for residential transactions in England & Wales.

## Quick Start

1. Read the full checklist: `references/part1-checks.md`
   — 24 categories, 90+ checks, every Part 1 requirement
2. When a check says "check Part 2": read `references/lenders/{slug}.md`
   for the specific lender's requirements (~108 Q&A per lender)
3. Follow the reporting decision tree below for any issue found

## Important Rules

- Part 1 = general requirements for ALL lenders
- Part 2 = lender-specific overrides and thresholds
- Express requirements in plain language — cite handbook section numbers
- When in doubt: REPORT to lender before completion (HB 2.3)
- Do NOT complete until written instructions received after reporting

## The Golden Rule

> If you believe any matter should reasonably be considered important by
> the lender in deciding whether to lend, and you cannot disclose it due
> to conflict of interest, you must cease acting and return instructions
> (HB 5.3.1).

## Reporting Decision Tree

When you identify any issue:

```
Can you certify title as good and marketable?
├── YES → Proceed without referral
│   └── Exception: some items ALWAYS require reporting regardless
│       (purchase price discrepancy, sub-6-month ownership,
│        non-owner seller, cashback/incentives, letting, HMO)
├── NO → Can indemnity insurance resolve it?
│   ├── YES → Arrange insurance (check Part 2 for acceptance)
│   │   └── You can now certify → Proceed
│   └── NO → Report to lender (HB 2.3) BEFORE exchange
│       ├── Identify relevant handbook provision
│       ├── Summarise legal risks
│       ├── Recommend how lender should protect interest
│       └── DO NOT COMPLETE until written instructions received
└── CONFLICT OF INTEREST prevents disclosure?
    └── CEASE ACTING → Return instructions (HB 5.3.1)
```

## Part 2: Lender-Specific Requirements

When a "check Part 2" item is triggered, read the specific lender's
reference file from `references/lenders_json/{lender-slug}.json`.

Each file contains the lender's factual answers to every Part 2 question
(~108 items) structured as JSON.

**To look up a lender's Part 2 requirement:**
1. Identify the section number from the Part 1 checklist (e.g. 5.14.1)
2. Read `references/lenders_json/{lender-slug}.json`
3. Find the matching section number in the JSON object
4. Apply the lender's specific factual requirements

**Tier 1 lenders** (~80% of UK mortgages):
nationwide-building-society, santander-uk-plc, barclays-bank-uk-plc,
hsbc-uk-bank-plc, national-westminster-bank-plc, halifax,
bank-of-scotland-beginning-a, tsb-bank-plc, virgin-money,
yorkshire-building-society, skipton-building-society,
coventry-building-society, leeds-building-society,
principality-building-society, metro-bank-plc

Plus 50+ Tier 2 and Tier 3 lenders in the same directory.

If the borrower's lender is not listed, fall back to Part 1 general
requirements and advise the conveyancer to check the UK Finance website
directly for that lender's Part 2.

## Sources

- UK Finance Mortgage Lenders' Handbook Part 1 (England & Wales):
  https://lendershandbook.ukfinance.org.uk/lenders-handbook/englandandwales/
- Part 2 data from individual lender pages on the same site
- Building Safety Act 2022, Insolvency (No 2) Act 1994

This skill provides guidance based on publicly available handbook
requirements expressed in plain language. Always refer to the current
published handbook.
