---
name: investors-rights-agreement
title: Investors' Rights Agreement
description: 'Drafts a U.S. Investors'' Rights Agreement for VC/private equity financings, covering registration rights, information/management rights, pro rata rights, expenses, and termination. Use when drafting an IRA, Amended and Restated IRA, or VC financing governance package. Trigger keywords: "investors'' rights agreement", "IRA", "registration rights", "piggyback", "Form S-3", "information rights", "management rights", "pro rata", "ROFO".'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/investors-rights-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: securities
language: en
tags: [agreement, corporate, drafting, transactional]
---

# Investors' Rights Agreement

Draft a market-standard, internally consistent IRA tied to the financing closing. All defined terms must align with the SPA and Charter.

## Prerequisites

Gather before drafting:

- **Transaction docs** — SPA, Charter, Voting Agreement, ROFR/Co-Sale, cap table, closing schedule
- **Party data** — legal names, jurisdictions, notice addresses, signature authority
- **Deal economics** — share classes, price, amounts, investor thresholds
- **Negotiated terms** — thresholds, timing, delays, cutback priority, termination triggers
- **Governing law + forum** — selected state and venue
- **Investor-specific items** — ERISA management rights, observer rights, side letters

## Core Workflow

### 1. Schedules and Parties

- Company legal name + jurisdiction (from Charter)
- Schedule A (Investors): name, address, series/shares, original purchase price
- Schedule B (Founders): name, address, shares/class
- Effective date = closing date (match SPA)

### 2. Definitions

Align all to SPA/Charter. Required minimums:

`Registrable Securities` (with exclusions), `Holder`, `Initiating Holders`, `Major Investor` threshold, `New Securities`, `Excluded Securities`, `Deemed Liquidation Event` (from Charter), `Form S-3` / `Register` / `Registration Statement` (if used).

### 3. Registration Rights

Key levers — fill from deal terms:

| Topic | Default Range | Variable |
|---|---|---|
| Demand threshold | 25–40% of Registrable Securities | `{{DemandPct}}` |
| Demand count | 1–2 | `{{DemandCount}}` |
| Demand minimum | $5–10M offering size | `{{DemandMin}}` |
| Delay right | up to 90 days / 12 months | `{{DelayLimit}}` |
| Piggyback notice | 10–20 business days | `{{PiggybackNotice}}` |
| Cutback priority | 1) non-Company/non-Holder → 2) Company → 3) Holders pro rata | `{{CutbackOrder}}` |
| Form S-3 threshold | 10–30% | `{{S3Pct}}` |
| S-3 minimum | $1–5M | `{{S3Min}}` |
| S-3 frequency | 1–2 per 12 months | `{{S3Count}}` |

Piggyback exclusions: Form S-4 (M&A), Form S-8 (employee plans), reorganizations/splits, plus SPA-agreed exclusions.

### 4. Registration Procedures

**Company obligations:** prepare/file registration statement + amendments, provide filings/prospectus to Holders, blue sky qualification, legal opinions + comfort letters, exchange listing, underwriting agreement if applicable, maintain effectiveness through distribution.

**Holder obligations:** provide filing info, comply with prospectus delivery, execute custody/lock-up (≤ 180 days typical), execute POA for filings.

**Indemnification:** Company indemnifies Holders for misstatements/omissions except Holder-furnished info. Holders indemnify Company for Holder-furnished info. Contribution applies if indemnity unavailable.

### 5. Expenses

- **Company pays (Registration Expenses):** SEC/blue sky fees, printing, Company counsel, auditors, listing, transfer agent; one selling-holder counsel if agreed
- **Holders pay pro rata (Selling Expenses):** underwriting discounts, commissions, brokerage, holder-specific counsel, transfer taxes

### 6. Information Rights

Major Investor deliverables (if negotiated):

- Annual audited FS — 90–120 days after FY end
- Quarterly unaudited FS — 45 days after quarter end
- Annual budget — 30 days after FY start
- Monthly statements — 30 days after month end

Confidentiality: investment monitoring only; standard exceptions (public, third-party, independent, legal compulsion); competitive-sensitivity withholding with notice.

### 7. Management Rights

Include if needed for ERISA VC operating company qualification.

- Reasonable facility/records access with notice
- Board observer rights if no seat; periodic management meetings
- Advisory only — no fiduciary duty or control; privilege/conflict carve-outs

### 8. Pro Rata (ROFO) Rights

Process: Company notice 20–30 days pre-issuance → investor election 15–20 days → oversubscription pro rata → Company sells unsubscribed on no-better terms within 90–120 days.

**New Securities:** any equity or equity-linked (convertibles, warrants, options).

**Excluded Securities (align to SPA):** equity plan issuances, board-approved M&A/strategic (incl. preferred director), public offerings, existing conversions/exercises, debt/lease financings, sponsored research/strategic collaborations, other negotiated exclusions.

### 9. Termination Matrix

| Right | Terminates Upon |
|---|---|
| Registration | IPO + 5–7 years; Rule 144 free sale; deemed liquidation |
| Information | IPO; loss of Major Investor status; deemed liquidation |
| Management | IPO; loss of Major Investor status |
| Pro rata | IPO (or post-IPO sunset); loss of Major Investor status; deemed liquidation |

If citing SEC Rule 144 or Rule 415, confirm current accuracy. [VERIFY]

### 10. Miscellaneous

- Governing law + exclusive forum
- Jury trial waiver (if selected; make conspicuous)
- Amendments: Company + required % of Registrable Securities; class consent for adverse changes
- Waivers: written only; no implied waivers
- Assignment: Company restricted; Holders may assign to affiliates/qualified transferees with joinder
- Notices: methods, deemed receipt timing, update requirement
- Severability and reformation
- Counterparts + electronic signatures (E-SIGN compliant)
- Entire agreement clause tied to transaction documents

## Pitfalls and Checks

- Match all defined terms to SPA/Charter — never invent new definitions
- Keep thresholds, timing windows, and sunset periods consistent across all transaction docs
- Reconcile schedules to cap table and closing schedule totals
- Use U.S. securities law terminology consistently (Securities Act, registration statement, prospectus)
- Do not add arbitration unless expressly required by deal terms
- Flag any legal citation uncertainty with `[VERIFY]`
- Confirm board-approval or preferred-director consent requirements for exclusions
