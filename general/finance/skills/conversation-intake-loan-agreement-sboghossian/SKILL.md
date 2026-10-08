---
name: conversation-intake-loan-agreement-sboghossian
title: Intake — Loan Agreement
description: Use when a user wants to draft a loan agreement, facility agreement, or credit agreement and Claude must gather the financing, security, and structural inputs before generating the document. Triggers on requests to prepare a lending arrangement between any combination of individuals and corporate entities. Covers multi-jurisdictional MENA (UAE, KSA, LB, EG, DIFC) with Islamic finance carve-out for Sharia-compliant structures, and secondary coverage of UK, EU, and US.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/conversation/conversation-intake-loan-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Intake — Loan Agreement

## When this applies

Activate when a user requests drafting of a loan agreement, facility letter, credit agreement, intercompany loan, or any instrument documenting a debt financing arrangement. This skill collects the twelve structural inputs before routing to [[draft-loan-agreement]]. The Islamic finance flag (item 5) is particularly important: if the borrower or lender requires a Sharia-compliant structure, the entire instrument changes (no interest, profit-sharing or commodity-based structures instead).

## Behavior

Multi-turn intake (up to three turns for complex syndicated or multi-tranche facilities). Extract any information already given in the user's opening message. Raise the Islamic finance question early — it determines the template entirely.

## Required fields

### 1. Lender and Borrower

- Full legal name, entity type (bank, fund, SPV, individual, government entity), jurisdiction of incorporation, and commercial registration (CR) or equivalent.
- For individuals: name, passport number, jurisdiction of residence.
- Identify the type of lending relationship:
  - **Bank to corporate/individual**: regulated lending; confirm lender is licensed (Central Bank of UAE, Saudi Central Bank / SAMA, Banque du Liban, etc.).
  - **Corporate-to-corporate intercompany**: common in groups; confirm arm's-length pricing required for transfer-pricing compliance.
  - **Individual-to-company**: confirm usury / anti-unconscionable lending rules apply in the relevant jurisdiction.
  - **Shareholder loan**: subordinated? convertible? Affects insolvency ranking.

### 2. Principal amount and currency

- Loan amount and denomination.
- Multi-currency facility: if payments may be made in more than one currency, note the exchange rate mechanism (mid-market fix, bank's offered rate, etc.).
- Flag: if the currency is LBP (Lebanese Pound) for a Lebanon loan, address the USD/LBP dual-track risk explicitly — specify whether the loan is in "fresh dollars" (offshore) or LBP.

### 3. Disbursement

- Lump-sum single drawdown, or committed facility with multiple tranches/drawdowns?
- Drawdown conditions precedent (CPs): standard CPs include corporate authorization (board resolution, power of attorney), satisfactory security registration, audited financials, no material adverse change (MAC).
- Availability period: the window during which the borrower may draw.
- For construction or development loans: confirm phased disbursement tied to milestones.

### 4. Repayment

- Tenor / term (months / years).
- Amortization schedule: bullet (all principal at maturity), equal installment (straight-line amortization), or balloon (partial amortization + bullet at end).
- Prepayment: voluntary prepayment permitted? Any prepayment fee (yield maintenance, flat fee, break cost for fixed-rate)?
- Mandatory prepayment triggers: asset sale, insurance proceeds, change of control, excess cash-flow sweep.

### 5. Interest rate — or Islamic structure flag

**Critical**: ask this before drafting any pricing clause.

- **Conventional**: fixed rate, floating rate (SOFR + margin; LIBOR is retired — confirm replacement benchmark), or hybrid.
  - Day-count convention: 30/360, Actual/360, Actual/365 — material for interest calculation.
  - Payment frequency: monthly, quarterly, semi-annual.
  - Default rate: rate applicable after an Event of Default (typically prevailing rate + 2–3%).
- **Islamic finance (Sharia-compliant)**: if the borrower is a GCC Islamic bank, a Sharia-observant institution, or any party for whom charging or paying interest (riba) is prohibited:
  - **Murabaha** (cost-plus sale): lender purchases an asset and on-sells to borrower at a disclosed markup; used for commodity and trade finance.
  - **Ijarah** (lease-to-own): lender purchases and leases the asset to the borrower; title passes at end of term.
  - **Diminishing Musharaka** (declining co-ownership): lender and borrower co-own an asset; borrower buys out lender's share over time; used for real estate and equipment financing.
  - **Sukuk**: asset-backed certificates representing ownership in an underlying asset; used for capital markets / bond-equivalent financing.
  - Confirm the applicable Sharia board approval and whether the structure must be certified by a named scholar or institution (AAOIFI standards; IFSB guidance).

### 6. Security

What collateral / credit support is being provided?

| Security type | Typical use | Registration required |
|---|---|---|
| Mortgage over real estate | Property loans | UAE: Dubai Land Department / Abu Dhabi DLD; KSA: MOJ Notary; LB: Real Estate Notary |
| Pledge over shares | Corporate loans, LBO | UAE: SCA registry; DIFC: DIFC share transfer register; KSA: MOC Commercial Register annotation |
| Pledge over bank account / fixed deposit | Cash-collateralized loans | Bank lien notice; some jurisdictions require notarization |
| Assignment of receivables / contract rights | Working capital facilities | Requires notice to the account debtor to perfect |
| Personal guarantee | SME, owner-managed business | Confirm unlimited vs capped; enforceability in domestic jurisdiction of guarantor |
| Corporate guarantee from parent | Group financing | Board authorization of guarantor entity; financial assistance rules (LB, UK) |
| Floating charge over assets (all-asset security) | UK / DIFC / ADGM law-governed facilities | Register with Companies House (UK); DIFC Registrar |

### 7. Covenants

- **Financial covenants**: leverage ratio (Net Debt / EBITDA), interest coverage ratio (EBITDA / Interest), minimum liquidity (cash or current ratio), minimum net worth. Specify tested period (quarterly, semi-annual) and remedy cure period.
- **Operational covenants** (affirmative): maintain insurance, maintain licenses, provide annual audited accounts within 90/120 days.
- **Negative / restrictive covenants**: no additional indebtedness above threshold, no security over assets (negative pledge), no disposal of material assets, no change of business, no M&A without consent.
- **Information undertakings**: financial statements, compliance certificates, KYC updates.

### 8. Events of Default and acceleration

Standard events: payment default (grace period typically 3–5 business days), covenant breach (cure period typically 30 days for remediable), misrepresentation, cross-default, insolvency, change of control, MAC. Confirm whether acceleration is automatic or requires lender notice.

### 9. Cross-default and cross-acceleration

- Confirm cross-default threshold (e.g., any payment default on indebtedness exceeding USD 1 million triggers default under this facility).
- Cross-acceleration: only triggers if other indebtedness is actually accelerated (narrower than cross-default).

### 10. Governing law, dispute resolution, and jurisdiction

| Option | Typical use |
|---|---|
| DIFC Courts + DIFC law | International finance transactions in UAE; English-language; familiar to international banks |
| ADGM Courts + ADGM law | Fintech, Islamic finance structured in ADGM |
| UAE onshore courts + UAE law | Onshore mortgages; government-related borrowers |
| English courts + English law | International syndicated loans (LMA standard); MENA sovereign and quasi-sovereign issuers |
| KSA courts + KSA law | Domestic KSA lending; Saudi Central Bank-regulated institutions |
| LB courts + LB law | Lebanon domestic lending; Banque du Liban-regulated |
| LCIA / ICC / DIAC arbitration | Private commercial loans where court litigation is undesirable |

### 11. Bank secrecy and data protection

- **LB**: Lebanese Banking Secrecy Law (Law 3/1956) — strict; information sharing requires customer consent or court order. Standard confidentiality clause must not conflict.
- **UAE / DIFC**: UAE Federal Decree-Law No. 45/2021 on Personal Data Protection; DIFC Data Protection Law 2020. DPA addendum required if personal data is processed cross-border.
- **KSA**: Personal Data Protection Law (PDPL), effective 2022. Data localization requirements for sensitive data.
- **EU**: GDPR applies to EU data subjects; standard contractual clauses required for transfers to non-adequate third countries.

### 12. Tax (withholding and gross-up)

- Is the lender subject to withholding tax on interest in the borrower's jurisdiction?
  - **UAE**: currently no WHT on interest (as at 2025 — verify current position under UAE Corporate Tax Law).
  - **KSA**: 5% WHT on interest paid to non-resident lenders.
  - **LB**: 10% WHT on interest to non-residents; 7% on resident banks.
  - **EG**: 20% WHT on interest to non-residents (reduced by applicable DTA).
  - **UK / France**: standard WHT applies unless DTA reduces; gross-up clause customary.
- Gross-up clause: borrower agrees to increase payments so lender receives the contractual amount net of any WHT.

## Output

At the end of intake, produce:

1. A structured intake summary confirming all twelve fields and any outstanding items.
2. An Islamic vs conventional structure recommendation with one-paragraph rationale where the user is undecided or where Islamic finance appears applicable.
3. A routing instruction to [[draft-loan-agreement]] with the completed intake data.

## Do not

- Draft a conventional interest-bearing loan agreement without first asking whether any party requires Sharia compliance.
- Ignore registration requirements for security — an unregistered pledge or mortgage may be ineffective against third parties or in insolvency.
- Apply LMA English-law standard terms without adaptation to MENA civil-law governing law requirements.

## Related skills

- [[draft-loan-agreement]]
- [[draft-security-agreement]]
- [[kb-banking-finance-mena]]
- [[kb-islamic-finance]]
- [[conversation-intake-msa]]
- [[conversation-uncertainty-language]]
