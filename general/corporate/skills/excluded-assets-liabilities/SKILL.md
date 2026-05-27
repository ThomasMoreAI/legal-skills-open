---
name: excluded-assets-liabilities
title: Excluded Assets and Liabilities Schedule
description: Drafts a categorized schedule of excluded assets and liabilities as an exhibit to an asset purchase agreement. Delineates retained assets and unassumed liabilities by class. Use when drafting APA schedules, negotiating asset carve-outs, preparing closing exhibits, or defining exclusion scope in M&A asset sales.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/excluded-assets-liabilities
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Excluded Assets and Liabilities Schedule

Drafts a schedule/exhibit to an APA enumerating assets retained by seller and liabilities not assumed by buyer.

## Prerequisites

1. **Near-final APA** — title, date, section referencing this schedule
2. **Party details** — full legal names, jurisdictions
3. **Asset inventory** — sold vs. retained
4. **Liability allocation** — which obligations stay with seller
5. **Defined terms** from the main agreement

## Quick Start

1. Gather APA details, party information, and asset/liability lists
2. Draft preamble referencing the principal agreement
3. Cross-reference or locally define key terms
4. Enumerate excluded assets by category with item-level specificity
5. Enumerate excluded liabilities by category with identifying detail
6. Add seller representations and standard miscellaneous provisions
7. Verify every material retained asset and unassumed liability is listed

## Core Sections

### 1. Preamble

- Full legal names and jurisdictions of both parties
- Reference principal agreement (title, date, governing section)
- State schedule is exhaustive and controlling for exclusion determinations

### 2. Definitions

Cross-reference main agreement definitions. Define locally only if APA lacks them:

- **Excluded Assets / Excluded Liabilities** — eliminate interpretive ambiguity
- **Affiliate / Subsidiary** — if intercompany items exist
- **Intellectual Property** — if IP carve-outs involved
- **Permitted Encumbrances** — if real property excluded

State explicitly whether incorporating by reference or defining independently.

### 3. Excluded Assets

Draft each category with item-level specificity. Match detail to materiality.

| Category | Required Detail |
|----------|----------------|
| Cash & Equivalents | Account numbers, institution, balances as of reference date |
| Accounts Receivable | Pre-closing vs. specific customers; cut-off methodology |
| Intellectual Property | Registration numbers, jurisdictions (patents, marks, copyrights, trade secrets, domains) |
| Real Property & Leaseholds | Legal descriptions or addresses; improvements and fixtures |
| Personal Property & Equipment | Serial/VIN numbers or detailed descriptions |
| Contracts & Agreements | Counterparty, date, subject matter |
| Corporate Records & Non-Transferable Permits | Org docs, minute books, stock ledgers, tax records; non-assignable licenses |
| Intercompany Assets | Affiliate receivables, equity interests |

Reference sub-exhibits for extensive listings.

### 4. Excluded Liabilities

Each item must be identifiable enough to resolve disputes. Use representative examples plus descriptive catch-all when universe is large.

| Category | Required Detail |
|----------|----------------|
| Indebtedness | Lender, principal amount, agreement date |
| Accounts Payable & Accrued Expenses | Pre-closing payables; cut-off methodology |
| Litigation & Claims | Case name, court/forum, case number; include threatened claims |
| Tax Liabilities | Pre-closing income, sales/use, property, payroll; deficiencies/assessments |
| Environmental | Contamination, remediation, compliance tied to excluded properties |
| Employee & Benefits | Pension, severance, workers' comp, benefit plan obligations |
| Contract Liabilities | Pre-closing warranty claims, indemnification under excluded contracts |
| Intercompany Liabilities | Affiliate payables, guarantees |
| Contingent & Unknown | Risk allocation; specify triggering circumstances |

### 5. Seller Representations

- Excluded Assets list is complete — all unlisted assets transfer
- Seller owns excluded assets free of transfer obligations
- Retention violates no agreement or law
- No excluded asset is necessary for buyer's operation of acquired business as currently conducted
- Excluded liabilities are valid seller obligations; seller has capacity to satisfy them

Specify survival period, indemnification subject to APA framework.

### 6. Miscellaneous

- Governing law: same as main agreement
- Amendments: written, signed by both parties (or per APA procedures)
- Integration: this schedule + main agreement + transaction docs = entire agreement on exclusions
- Conflict: this schedule controls for identification of excluded items
- Severability and counterparts

## Pitfalls

- **Bare catch-alls** — general exclusion language must be carefully circumscribed, never open-ended
- **Inconsistent terms** — use identical defined terms as the APA throughout
- **Vague cross-references** — cite specific APA sections, not general references
- **Missing parallel structure** — mirror asset and liability category organization where logical
- **Tax characterization** — consider effects on both parties when categorizing excluded items
- **Incomplete listing** — confirm every material retained asset and unassumed liability is explicitly listed before finalizing

---

Key changes from the original:

- **Removed `tags`** — not part of the spec (only `name` and `description` in frontmatter)
- **Trimmed description** — kept under 1024 chars, third-person, with clear triggers
- **Added Quick Start** — numbered workflow for immediate use
- **Collapsed definitions table to a bullet list** — same info, fewer tokens
- **Converted seller reps from checklist to plain list** — checkboxes are for tracking workflow progress, not output content
- **Renamed "Guidelines" to "Pitfalls"** — focuses on what goes wrong rather than generic advice
- **Cut redundant prose** — removed repeated instructions and explanatory text throughout
- **~90 lines vs ~108** — tighter while preserving all legal substance
