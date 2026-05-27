---
name: royalty-report
title: Royalty Report Form
description: Drafts auditable royalty report forms for IP licensing agreements, calculating tiered royalties, minimum guarantees, and advance recoupments from governing license terms. Use when preparing licensee royalty reports, royalty payment calculations, license compliance filings, or periodic royalty submissions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/royalty-report
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Royalty Report Form

Drafts a certification-ready royalty report satisfying licensee reporting obligations under an IP license agreement. Functions as both an accounting instrument and a legally binding compliance document.

## Quick Start

1. Obtain the governing license agreement (including amendments)
2. Extract key terms into the extraction checklist below
3. Collect sales data for the reporting period (or confirm template-only output)
4. Draft report following the output structure
5. If prior reports exist, carry forward advance recoupment balances and cumulative tier thresholds

If multiple license agreements exist in uploaded documents, ask which governs before proceeding.

## Key Extraction Checklist

Extract from the license before drafting:

| Field | Source |
|---|---|
| Licensor / Licensee legal names | Signature blocks (exact match required) |
| Agreement date + amendments | Preamble / amendment headers |
| Reporting period / frequency | Reporting provisions |
| Royalty rate(s) and tiered thresholds | Royalty calculation section |
| Minimum royalty guarantee | Payment terms |
| Allowable deductions | Definitions / calculation provisions |
| Advance recoupment terms | Payment terms |
| Required accounting standard | Reporting provisions (GAAP or other) |
| Submission format / method | Reporting provisions |
| Confidentiality marking | Confidentiality section |
| Concurrent payment required? | Payment terms |
| Audit period | Audit rights section |

## Output Structure

### 1. Document Header

```
                        ROYALTY REPORT

[Licensee Legal Name]

For the [Quarter/Period] Ending [Date] / From [Start Date] through [End Date]

Pursuant to License Agreement dated [Date] between [Licensor Legal Name]
and [Licensee Legal Name] [, as amended by Amendment No. [X] dated [Date]]

Report No.: [If required]
```

### 2. Sales Data Table

| Product SKU | Product Description | Qty Sold | Unit Price | Gross Sales |
|---|---|---:|---:|---:|
| [SKU] | [Match licensed product definitions] | [X] | $[X.XX] | $[X.XX] |

- Organize by product line, territory, or license type if different rates apply
- Include subtotals per category before grand total
- If no sales data provided, use placeholder: **"[INSERT ACTUAL SALES DATA FROM ACCOUNTING RECORDS]"**

### 3. Royalty Calculation

```
Total Gross Sales                                    $[________]

Less Allowable Deductions:
  Returns & allowances                              ($[________])
  Freight & shipping (third-party)                  ($[________])
  Sales taxes & governmental charges                ($[________])
  Trade discounts                                   ($[________])
  [Other per agreement]                             ($[________])
Total Deductions                                    ($[________])

Net Sales Subject to Royalty                         $[________]

Royalty Calculation:
  [Rate]% on first $[threshold]                      $[________]
  [Rate]% on excess over $[threshold]                $[________]
Calculated Royalty                                   $[________]

Minimum Royalty Guarantee (if applicable)             $[________]
Royalty Due (greater of calculated or minimum)        $[________]

Less: Advance Recoupment                            ($[________])
Plus: Marketing Fund Contribution ([X]%)              $[________]
Plus: [Other fees per agreement]                      $[________]

TOTAL AMOUNT DUE                                     $[________]
```

- Show each deduction category separately — never aggregate
- Show each tier calculation independently
- Show advance recoupment as a separate line item from royalty earned

### 4. Certification & Signature Block

Certification must attest:
- Signer is authorized officer with authority to bind licensee
- Report prepared in accordance with the license agreement
- All information true, complete, and accurate after reasonable inquiry
- Data derived from books/records per the required accounting standard
- Payment represents full amount owed

> If the agreement prescribes specific certification language, incorporate it **verbatim**.

```
CERTIFICATION

The undersigned, a duly authorized officer of [Licensee], hereby certifies
that this Royalty Report has been prepared in accordance with the License
Agreement dated [Date], that all information is true, complete, and accurate
to the best of the undersigned's knowledge and belief after reasonable inquiry,
and that the sales data and calculations are derived from books and records
maintained in the ordinary course of business in accordance with
[GAAP/specified standard].

Signature: ___________________________
Name:      ___________________________
Title:     ___________________________
Date:      ___________________________
```

### 5. Payment Instructions

Include if concurrent payment required: amount due, payment method, payee name (exact per agreement), wire/mailing details, due date.

## Critical Checks

- **Entity names** — must exactly match signature block names; any variance may invalidate submission
- **Deductions** — include only those explicitly authorized; when uncertain, flag: `[VERIFY DEDUCTION ELIGIBILITY UNDER SECTION [X]]`
- **Audit exposure** — every figure must reconcile to source documents; reports typically auditable 2-3 years
- **Missing info** — use bracketed placeholders referencing the specific section: `[INSERT ROYALTY RATE FROM SECTION 4.2]`
- **Tiered calculations** — if cumulative annual thresholds apply, account for sales in prior periods of the same contract year
- **Supporting documents** — check whether agreement requires attachments (invoices, territory breakdowns, accountant certifications)
- **Misrepresentation risk** — report creates binding contractual representations; emphasize accuracy over speed

---

**Key changes made:**

- **Frontmatter**: Removed `tags` (not in spec), tightened description to be third-person with clear trigger guidance
- **Structure**: Replaced "Prerequisites" with a "Quick Start" workflow, renamed "Key Extraction from License Agreement" to shorter "Key Extraction Checklist", consolidated "Formatting Requirements" and "Guidelines" into a single "Critical Checks" section
- **Extraction table**: Merged licensor/licensee name rows; merged royalty rate/tier rows — fewer rows, same info
- **Templates preserved**: Header, sales table, royalty calculation, and certification blocks kept intact as essential domain content
- **Trimmed**: Removed Email/Phone from signature block (non-essential), removed Reference No. from header, removed "Currency per agreement; right-align all numerical columns" (obvious formatting), removed checkbox-style certification list (replaced with bullet attestation list), cut "Formatting Requirements" section entirely (standard knowledge)
- **Line count**: ~159 → ~127 lines of content (well under the 500-line limit)
