---
name: broker-dealer-customer-agreement
title: Broker-Dealer Customer Agreement
description: Drafts SEC/FINRA-compliant Broker-Dealer Customer Agreements covering account opening, trading, margin, fees, risk disclosures, privacy, arbitration, and execution. Use when drafting or updating customer account agreements, brokerage agreements, or customer documentation for registered broker-dealers.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/broker-dealer-customer-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: securities
language: en
---

# Broker-Dealer Customer Agreement

Drafts the master contractual agreement between a registered broker-dealer and its customers, covering all regulatory requirements under SEC, FINRA, Reg BI, and AML frameworks.

## Prerequisites

Gather before drafting:

- **Firm registration** — Form BD, FINRA CRD, state registrations, dual-registrant status
- **Business model** — execution-only vs. full-service, order routing, PFOF, principal trading
- **Product catalog** — all offered security types (equities, options, mutual funds, ETFs, penny stocks, alternatives)
- **Fee schedule** — commissions, account fees, margin rates, revenue sharing
- **Existing docs** — current applications, margin/options agreements, privacy policy, Form CRS
- **Regulatory history** — exam findings, deficiency letters, enforcement actions

## Quick Start

1. Confirm firm's business model and capacity (execution-only, recommendation-making, or dual registrant)
2. Identify all offered products and applicable special rules
3. Draft agreement sections per the structure below
4. Tailor provisions to firm's actual services — omit inapplicable sections
5. Verify all statutory/rule citations against current law
6. Ensure margin and arbitration warnings use prominent formatting (bold/caps, separate signature)
7. Cross-check consistency with Form CRS, Reg BI disclosure, fee schedule, and privacy policy

## Agreement Sections

### 1. Party Identification & Account Establishment

- BD identification: legal name, principal office, SEC reg number, FINRA CRD
- Customer identification per CIP Rule (USA PATRIOT Act §326): name, address, DOB, SSN/TIN, citizenship
- Entity customers: beneficial owners ≥25% or control persons
- Account types: cash (Rule 15c3-3), margin (Reg T), retirement, joint (JTWROS/TIC)
- KYC/suitability data per FINRA Rules 2090/2111
- Firm reserved rights: reject applications, restrict activities, close accounts

### 2. Service Relationship & Obligations

- Capacity disclosure: execution-only, recommendation-making (Reg BI), or dual registrant (BD vs. IA)
- If recommendations made: Reg BI four obligations — Disclosure, Care, Conflict of Interest, Compliance
- Product-specific rules: penny stock (Rules 15g-2–15g-9), options (Rule 2360 + ODD), mutual funds (share class/12b-1), leveraged ETFs (compounding risk), day trading ($25K minimum)

### 3. Trading Authorization & Order Handling

- Order channels with authentication requirements (MFA, recording disclosure)
- Best execution obligations: price, speed, execution likelihood, order size, total cost
- Order routing disclosure per SEC Rule 606; PFOF conflict disclosure
- Order type risks: market (no price protection), limit (no fill guarantee), stop (becomes market), GTC (monitor intent)
- Discretionary authority per FINRA Rule 3260 if applicable

### 4. Fee & Compensation Disclosure

- Commissions, markups/markdowns, account fees (exact amounts or fee schedule reference)
- Margin interest: base rate, spread, calculation method, tiered rates
- PFOF, revenue sharing, 12b-1 fees, underwriting concessions, proprietary product conflicts
- Cross-reference Reg BI disclosure and Form CRS

### 5. Margin Lending

- Regulatory framework: Reg T (50% initial), FINRA 4210 (25% maintenance), house requirements
- Include concrete margin call example showing equity erosion and call trigger
- Firm rights: charge interest, hypothecate securities per Rule 15c3-3, no lending of fully paid without consent
- **Liquidation rights (PROMINENT):** firm may sell without notice/consent; sole discretion on securities/timing; not required to minimize loss
- **Bold risk warnings** (require separate signature): losses can exceed investment; may owe more than deposited; firm can force sale; customer cannot choose securities sold

### 6. Risk Disclosures & Acknowledgments

- Product-specific risks: market, liquidity, equity, options (unlimited on uncovered writes), fixed income, penny stock, leveraged ETFs, international
- Required acknowledgments (signature/initial): understood agreement, received ODD/penny stock disclosure, total loss possible, sole responsibility in non-discretionary accounts

### 7. Corporate Actions & Account Maintenance

- Dividends, mandatory/voluntary actions, proxy voting, securities lending
- Confirmations (T+1) and statements (monthly/quarterly); must review for errors
- Error reporting deadlines: confirmations 5 business days, statements 30 days

### 8. Privacy & Data Security

- Draft per SEC Regulation S-P
- Cover: information collected, uses, sharing categories (providers, regulators, affiliates, non-affiliates)
- Opt-out procedures, security measures, breach notification per state laws

### 9. Amendment, Assignment & Termination

- Amendments: 30 days' notice; continued use = acceptance; regulatory changes may take immediate effect
- Assignment: customer needs consent; firm may assign in mergers/acquisitions
- Termination: customer-initiated (settle trades, ACATS 5-7 days) and firm-initiated (violations, suspicious activity, death)
- Records retained per SEC Rule 17a-4 (6 years post-close)

### 10. Mandatory Arbitration

- Include FINRA-required all-caps disclosure (waiver of jury trial, limited discovery, binding awards)
- Scope: all controversies, all legal theories
- Forum: FINRA Dispute Resolution; >$100K three arbitrators (majority public); ≤$100K single arbitrator
- Limited judicial review: vacatur only for fraud, partiality, or excess of powers
- Preserved rights: customer may still file with SEC/FINRA/state regulators
- Governing law and severability provision

### 11. Execution & Acknowledgments

- Customer representations: legal capacity, accurate information, understands risk
- Entity-specific: signatory authorization, governing document compliance, supporting docs
- Signature requirements by account type (individual, joint, entity)
- E-signature compliance per E-SIGN Act/UETA; click-to-agree accepted; right to withdraw e-delivery consent
- Integration clause: agreement + incorporated documents = entire agreement
- Non-waiver provision

## Key Regulatory Citations

| Citation | Subject |
|----------|---------|
| USA PATRIOT Act §326 / CIP Rule | Customer identification |
| FINRA Rules 2090/2111 | KYC and suitability |
| Regulation Best Interest | Recommendation standard (four obligations) |
| SEC Rule 15c3-3 | Customer protection / segregation |
| Reg T / FINRA Rule 4210 | Margin requirements |
| SEC Rules 15g-2–15g-9 | Penny stock requirements |
| FINRA Rule 2360 | Options |
| SEC Rule 606 | Order routing disclosure |
| FINRA Rule 3260 | Discretionary authority |
| SEC Regulation S-P | Privacy |
| SEC Rule 17a-4 | Records retention |
| E-SIGN Act / UETA | Electronic signatures |
| Federal Arbitration Act | Arbitration enforceability |

## Pitfalls

- **Omitting penny stock provisions** — required if firm offers penny stocks (Rules 15g-2–15g-9); must not be skipped
- **Weak margin warnings** — liquidation rights and risk warnings must be prominent (bold/caps) with separate signature/initial
- **Inconsistent documents** — agreement must align with Form CRS, Reg BI disclosure, fee schedule, and privacy policy
- **Unverified citations** — always verify statutory and rule citations against current law before finalizing
- **State law variations** — enforceability varies by jurisdiction, especially arbitration; flag issues
- **Retail comprehensibility** — agreement must be understandable by investors with limited financial sophistication
- **Including unused provisions** — omit provisions for services the firm does not offer

For detailed per-section drafting specifications including field-level requirements, example language, and product-specific tables, see `references/SECTION-SPECS.md`.
