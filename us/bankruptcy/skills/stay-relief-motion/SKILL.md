---
name: stay-relief-motion
title: Motion for Relief from Automatic Stay
description: Drafts a Motion for Relief from Automatic Stay under 11 U.S.C. § 362(d). Covers § 362(d)(1) cause/adequate protection, (d)(2) no equity/not necessary, and (d)(3) single asset real estate grounds. Use when a creditor needs to lift the automatic stay to foreclose, repossess collateral, or continue state court litigation against a debtor in bankruptcy.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/stay-relief-motion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: bankruptcy
language: en
tags: [drafting, litigation, motion]
---

# Motion for Relief from Automatic Stay

Drafts a procedurally compliant motion under 11 U.S.C. § 362(d) to lift the automatic stay. Ensures compliance with FRBP 4001, 9014, and local rules.

## Prerequisites

1. **Loan/lease documents** — note, security agreement, deed of trust, UCC filings
2. **Perfection evidence** — recording info, UCC-1 receipts, title reports
3. **Payment history** — account ledger, defaults, arrearage calculation
4. **Valuation evidence** — appraisal, BPO, tax assessment, or comparables
5. **Bankruptcy case info** — case number, chapter, filing date, court/district/division, debtor name
6. **Post-petition facts** — adequate protection payments, insurance status, property condition

## Quick Start

1. Gather all prerequisites; confirm statutory ground(s): § 362(d)(1), (d)(2), and/or (d)(3)
2. Draft caption with exact debtor name, case number, chapter, and movant capacity
3. Build chronological fact section from loan origination through post-petition default
4. Draft legal argument matching each ground to evidentiary support
5. Prepare supporting declaration with FRE 803(6) foundation and exhibit list
6. Verify service list and 21-day notice requirement under FRBP 4001

## Output Structure

### 1. Caption & Case Identification

| Element | Requirement |
|---------|-------------|
| Court | U.S. Bankruptcy Court, [District], [Division] |
| Debtor | Exact legal name from petition; entity type |
| Case No. | Jurisdiction-specific format |
| Chapter | 7, 11, 12, or 13 |
| Movant | Full legal name + capacity (e.g., "as holder of a first-priority deed of trust") |
| Title | "MOTION FOR RELIEF FROM AUTOMATIC STAY PURSUANT TO 11 U.S.C. § 362(d)" |

### 2. Introduction

- Movant identity, relationship to debtor, collateral description
- Specific relief sought: termination / modification / annulment
- Statutory basis and procedural context (filing date, stay duration, deadlines)

### 3. Factual Background

Present chronologically:

- **Pre-petition:** Transaction date, principal, rate, terms, maturity; guarantors/co-borrowers
- **Collateral:** Legal description (real property) or make/model/VIN (personal property); recording/UCC-1 data; perfection method and priority position
- **Default:** First missed payment, arrearage itemization (principal, interest, late charges, fees), pre-petition collection efforts, failed workout attempts
- **Post-petition impact:** How stay halted remedies; insurance lapses; waste/deterioration; missed adequate protection payments

### 4. Legal Argument

**§ 362(d)(1) — Cause / Lack of Adequate Protection**

- Define adequate protection under § 361 (cash payments, replacement liens, indubitable equivalent)
- Show declining collateral value with appraisal support (petition-date vs. current)
- Calculate equity cushion; cite circuit authority on minimum threshold (typically ≥ 20%)
- Show post-petition payments insufficient to cover accruing interest + depreciation
- Additional cause if applicable: bad faith/serial filing, no reorganization prospect, violation of prior orders
- Burden: under § 362(g)(2), debtor bears burden on adequate protection

**§ 362(d)(2) — No Equity + Not Necessary for Reorganization**

- *No equity (movant's burden, § 362(g)(1)):* Current FMV, all liens in priority order, total encumbrances > FMV
- *Not necessary for reorganization:*
  - Ch. 7: liquidation; reorganization element inapplicable
  - Ch. 11: no plan filed / not confirmable / business not viable
  - Ch. 13: cannot afford payments + cure / insufficient income
- Cite circuit authority: debtor must show "reasonable possibility of successful reorganization within a reasonable time"

**§ 362(d)(3) — Single Asset Real Estate (if applicable)**

- Debtor qualifies as SARE under § 101(51B)
- Failed to file plan or begin interest payments within 90 days

### 5. Prayer for Relief

- Relief from stay to exercise non-bankruptcy remedies (specify: foreclose, repossess, litigate)
- Address FRBP 4001(a)(3) 14-day stay: request waiver if emergency
- Without prejudice to seek further relief
- Attorney's fees and costs (cite contractual or statutory basis)

### 6. Supporting Declaration

Declarant must have personal knowledge (loan servicer, asset manager, corporate representative).

- Position, responsibilities, familiarity with account
- Business records foundation under FRE 803(6)
- Factual narrative supporting all motion allegations
- Post-petition communications and adequate protection history
- Current collateral condition and value

### 7. Exhibits

| Exhibit | Description |
|---------|-------------|
| A | Promissory note / lease agreement |
| B | Deed of trust / security agreement |
| C | Proof of perfection (recorded docs / UCC filings) |
| D | Payment history / account ledger |
| E | Default notices / demand letters |
| F | Appraisal / valuation evidence |
| G | Property condition photos (if applicable) |
| H | Post-petition correspondence re: adequate protection |

Each exhibit referenced in declaration with FRE 803(6) authentication.

### 8. Service & Certificate

**Service list:** Debtor, debtor's counsel, U.S. Trustee, Ch. 7/13 Trustee (if appointed), special notice parties (Rule 2002), corporate debtors per Rule 7004.

**Timing:** Serve ≥ 21 days before hearing. File motion to shorten time if emergency.

**Certificate:** Party name, address, method (CM/ECF or mail), date served.

## Checks

- Use persuasive point headings stating conclusions, not neutral labels
- Cite specific numbers, dates, and exhibits — avoid conclusory statements
- Prioritize binding circuit/district authority with parentheticals
- Preemptively distinguish likely adverse authority
- Verify all Bluebook citations and local standing orders (mediation, certification, proposed order format)
- Local formatting: 12pt Times New Roman/Arial, 1" margins, double-spaced, consecutive paragraph numbering
- Signature block: /s/ format, bar number, firm, address, phone, email
- Emergency relief requires separate motion to shorten time
- Tone: professional, forceful, respectful
