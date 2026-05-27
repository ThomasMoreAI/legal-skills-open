---
name: stock-ledger-certificates
title: Stock Ledger and Certificates
description: Drafts stock ledger and certificate packages for U.S. corporations, including master equity ledger, certificate templates, transfer procedures, and officer certification. Extracts capitalization data from formation documents. Use when forming a corporation, issuing initial shares, or establishing equity ownership records.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/stock-ledger-certificates
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [drafting]
---

# Stock Ledger and Certificates

Drafts the official equity ownership package: master stock ledger, individual certificate templates, transfer procedure block, and officer certification.

## Prerequisites

1. **Articles of Incorporation** — legal name, state, authorized shares, par value, share classes
2. **Bylaws or Organizational Minutes** — authorized officers, transfer restrictions
3. **Shareholders' Agreement** (if any) — ROFR provisions, transfer restrictions
4. **Existing stock records** (if any) — prior issuances, certificate numbers

## Quick Start

Extract from uploaded formation documents: (1) authorized capital by class, (2) par value per class, (3) initial issuances and consideration, (4) officer names for signature blocks. Draft all six sections below in sequence.

## Output Structure

### 1. Document Header

| Field | Content |
|---|---|
| Corporation Name | Full legal name |
| State of Incorporation | From articles |
| Date of Incorporation | From articles |
| Document Title | Stock Ledger and Stock Certificates |
| Prepared As Of | Current date |

### 2. Authorized Capital Structure

| Class | Shares Authorized | Par Value | Authorizing Document |
|---|---|---|---|
| Common | [#] | $[X] / No par | Articles of Incorporation, §[X] |
| Preferred | [#] | $[X] / No par | Articles of Incorporation, §[X] |

### 3. Stock Ledger Table

| Cert. No. | Date Issued | Shareholder | Shares | Class | Consideration | Transfer / Notes |
|---|---|---|---|---|---|---|
| 001 | [Date] | [Full legal name] | [#] | Common | $[X] cash / [desc] | — |

- Number certificates sequentially from **001**
- Flag gaps or inconsistencies in uploaded records
- Cancelled certificates: "CANCELLED — [date], replaced by Cert. No. [X]"

### 4. Stock Certificate Template

Each certificate must include:

- [ ] Certificate number matching ledger
- [ ] Corporation legal name and state of incorporation
- [ ] Shareholder legal name and address
- [ ] Share count in **numerals and words** ("100 — One Hundred shares")
- [ ] Class of stock and date of issuance
- [ ] Statement: *"Subject to the Corporation's Bylaws and any applicable Shareholder Agreement"*
- [ ] Corporate seal space or "Corporate Seal" notation
- [ ] Signature lines: **President/CEO** + **Secretary** with printed name and title

### 5. Transfer Procedure Block

> **To transfer shares:** (1) Surrendering shareholder endorses original certificate or executes a stock power/assignment, (2) delivers endorsed certificate and documentation to corporation, (3) corporation cancels old certificate, issues new, and updates ledger. Transfer restrictions in any shareholders' agreement or bylaws must be satisfied before recording.

### 6. Officer Certification

> *"The undersigned officers of [Corporation Name] hereby certify that the foregoing Stock Ledger accurately reflects all issuances and transfers of the corporation's capital stock as of [date]."*

Signature lines: President/CEO and Secretary, with printed name, title, and date.

## Checks and Pitfalls

- **State variance**: Certificate and ledger requirements vary by state — confirm state of incorporation and compliance with applicable Business Corporation Act
- **Securities legend**: Add restricted securities legend if applicable (e.g., §4(a)(2) exemption): *"These securities have not been registered under the Securities Act of 1933..."* — mark `[VERIFY]` for counsel review
- **S-corp**: Flag S-corp status; only eligible shareholders may hold shares, with restrictions on number and type
- **Multiple classes**: Distinguish classes in both ledger and certificates; reflect rights and preferences from articles
- **Inspection rights**: Shareholders have statutory inspection rights in most states — exclude confidential side letters from main ledger
- **Records location**: Ledger must be maintained at principal office or registered agent per state business corporation act
