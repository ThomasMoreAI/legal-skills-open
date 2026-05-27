---
name: corporate-resolution-bank-account
title: Corporate Resolution — Bank Account Authorization
description: Drafts a board resolution authorizing the opening and management of corporate bank accounts, including signatory designation, account types, borrowing authority, and secretary certification. Triggers when a financial institution requires formal board authorization to establish or manage accounts, when updating authorized signatories, or when documenting banking authority during entity formation or reorganization.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/corporate-resolution-bank-account
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [drafting]
---

# Corporate Resolution — Bank Account Authorization

Produces a board-level governance document that satisfies both internal corporate formality and bank due diligence for account opening, maintenance, and transaction authority.

## Required Inputs

1. **Corporation legal name** — must match articles of incorporation exactly
2. **State of incorporation**
3. **Adoption method** — board meeting or written consent of directors
4. **Financial institution(s)** — named institution or class (e.g., "any FDIC-insured institution")
5. **Authorized signatories** — names, titles, tiered authority thresholds
6. **Scope** — account types, transaction types, borrowing authority (yes/no), dollar limits
7. **Prior resolutions** — to supersede, if any
8. **Bylaws** — provisions on banking authority and consent requirements

## Quick Start

1. Collect all required inputs above.
2. Confirm bylaw authorization for board delegation of banking authority.
3. Confirm adoption-method validity under applicable state law.
4. Draft resolution sections in order: Header → Operative Resolutions → Certification.
5. Verify legal name, signatory tiers, and dollar thresholds before finalizing.

## Output Structure

### 1. Header & Recitals

| Field | Content |
|---|---|
| Title | RESOLUTIONS OF THE BOARD OF DIRECTORS OF [CORP NAME] |
| Date | Adoption date |
| Method | Board meeting (quorum + notice) OR written consent (check state unanimity requirement) |
| Bylaw reference | Cite specific provision authorizing banking resolutions |
| Purpose | Brief operational need (payments, payroll, receivables, etc.) |

### 2. Operative Resolutions

Draft each as a separate RESOLVED clause:

- **Account Authority** — Authorize named officers to open, maintain, modify, and close specified account types (checking, savings, money market, CD, other) at designated institution(s).
- **Signatory Designation** — Tiered structure:
  - Single signature: transactions up to $[threshold]
  - Dual signature: transactions exceeding $[threshold]
  - Covers: checks, wires, ACH, online banking, bank-required forms
- **Transaction Scope** — Deposits, withdrawals, standard transactions. If borrowing: specify dollar cap, permitted obligation types, whether collateral pledges need separate approval.
- **Document Execution** — Officers may execute all bank-required documents, signature cards, and agreements without further board action for routine forms.
- **Ratification** — Ratify prior banking acts if accounts/transactions predate formal authorization.
- **Supersession** — Supersedes all prior banking-authority resolutions, effective [date].
- **Continuing Authority** — Remains in effect until amended/revoked by board action. Corporation must notify institution of changes. Optionally: auto-terminate on signatory separation.

### 3. Secretary Certification

Must certify:
1. Resolutions were duly adopted on [date] per bylaws and state law
2. Resolutions have not been amended, modified, or revoked
3. Resolutions remain in full force and effect

Include: printed name, title (Secretary/Assistant Secretary), date, corporate seal if required.

## Pitfalls & Checks

- **Name mismatch** — Corporation name must match articles exactly; most common cause of bank rejection
- **Bylaw gap** — If bylaws don't authorize banking delegation, amend bylaws first
- **Consent threshold** — Most states require unanimous written consent unless bylaws provide otherwise; verify state statute
- **Quorum** — For meeting adoption, confirm quorum present throughout; document in minutes
- **Borrowing caps** — Always specify dollar limits; unlimited borrowing authority creates fiduciary exposure
- **Signatory changes** — Banks typically require re-certification of the resolution (not just new signature cards) when officers change
- **Stale certification** — Banks often require certification dated within 30–90 days; flag for recurring use
- **State law** — Procedural validity governed by state corporate code (e.g., Delaware § 141, California Corp. Code § 307) — verify applicable statute for client's jurisdiction
