---
name: commission-plan-agreement
title: Commission Plan Agreement
description: Drafts U.S. commission plan agreements establishing compensation terms for agents, salespeople, or affiliates. Covers flat/tiered/hybrid structures, payment mechanics, clawbacks, territory definitions, termination effects, independent contractor classification, and restrictive covenants. Use when drafting or negotiating commission-based compensation in employment, consulting, or affiliate contexts.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/commission-plan-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
---

# Commission Plan Agreement

Drafts a U.S.-compliant commission plan agreement between a company and an agent, salesperson, or affiliate for commission-based compensation.

## Prerequisites

1. **Party details** — legal names, entity types, jurisdictions, addresses, authorized signatories
2. **Commission structure** — rate(s), basis (gross vs. net), tier thresholds, triggering event (signing, payment receipt, etc.)
3. **Territory** — geographic boundaries or named market segments
4. **Product/service scope** — covered items and exclusions (house accounts, existing customers)
5. **Payment schedule** — frequency, method (ACH/wire/check), statement format
6. **Governing state** — determines non-compete enforceability and commission payment statute obligations
7. **Existing documents** — prior commission agreements, sales policies, expense policies

## Output Structure

### 1. Preamble & Recitals
Identify parties with full legal names and addresses. Recitals establish commission-based sales relationship.

### 2. Definitions

| Term | Drafting Notes |
|---|---|
| **Net Sales** | Gross revenue less returns, refunds, discounts, taxes, shipping — list each deduction |
| **Qualified Sale** | Triggering criteria: executed contract, payment received, shipped, etc. |
| **Territory** | Geographic region or named accounts; map to Exhibit A if complex |
| **Commission Period** | Calendar month/quarter tied to payment cycle |
| **House Accounts** | Excluded accounts not eligible for commission |
| **Clawback Event** | Return, refund, chargeback, or cancellation within defined lookback window |

### 3. Commission Structure

**Flat rate:** Agent earns [__]% of Net Sales on Qualified Sales per Commission Period.

**Tiered rate** (Exhibit A or inline table):

| Cumulative Net Sales (per period) | Rate |
|---|---|
| $0–$[X] | [_]% |
| $[X+1]–$[Y] | [_]% |
| Above $[Y] | [_]% |

**Key provisions:**
- [ ] When commission is "earned" (signing vs. payment)
- [ ] Split-commission formula for multiple agents
- [ ] Residual/recurring commissions on subscriptions (duration + conditions)
- [ ] Clawback adjustments within [90/180] days of payment
- [ ] Minimum performance thresholds and consequences
- [ ] Exclusions (house accounts, excluded territories, minimum order)

### 4. Payment Terms
- Payment within [15/30] days after Commission Period end
- Detailed statement: sales included, deductions, net amount
- Agent responsible for income taxes; company issues **Form 1099-NEC**
- Dispute window: [30] days to object or statement deemed accepted

### 5. Expenses
Choose one approach:
- **Agent bears all** (typical for independent contractors)
- **Company reimburses approved** — pre-approval threshold, receipts, cap, timeline

### 6. Term & Termination

| Scenario | Commission Treatment |
|---|---|
| For Cause | Forfeit pending/unclosed; pay earned but unpaid |
| Without Cause ([30/60] days notice) | Pay earned but unpaid; address pipeline per schedule |
| Expiration | Same as without-cause |

Survival: confidentiality, non-solicitation, indemnification, and earned commission obligations survive termination.

### 7. Restrictive Covenants

**Confidentiality:** Customer lists, pricing, strategy, trade secrets — return/destroy on termination.

**Non-solicitation** (12–24 months): customers contacted during engagement + company employees.

**Non-compete:** Narrowly tailor by scope, geography, duration. [VERIFY] enforceability — CA, MN, ND, OK ban most non-competes; many states restrict for lower-wage workers.

### 8. Relationship of Parties
State agent is independent contractor with no authority to bind company. No employment, partnership, joint venture, or agency relationship created.

### 9. Representations & Warranties
- **Mutual:** Authority to enter; no conflicting obligations
- **Agent:** Compliance with applicable law (consumer protection, anti-bribery, FCPA if international)

### 10. Governing Law & Dispute Resolution
- Governing law: [State] (typically company HQ)
- Exclusive venue: [County, State]
- Optional: mediation then AAA arbitration (seat, cost allocation, injunctive relief carve-out)

### 11. Signature Block
Authorized representatives with name, title, date. Counterparts clause; e-signatures valid under ESIGN/UETA.

## Guidelines

- **Commission statutes:** CA, IL, NY, TX require written agreements and timely payment — [VERIFY] governing state requirements
- **Misclassification risk:** Review ABC test or applicable state standard before classifying as independent contractor
- **Non-compete:** Confirm current enforceability before including; overreach can void the clause
- **Clawback window:** Keep reasonable (90–180 days); longer periods harder to enforce
- **Tax:** 1099-NEC threshold $600/year for U.S. persons; non-U.S. agents require W-8 series
- **Merger clause:** Confirm no oral side agreements on commission promises before including

**Key changes made:**
- Removed `tags` from frontmatter (not in Anthropic spec; only `name` and `description` required)
- Tightened description — removed "comprehensive" and "generating sales" filler
- Compressed prerequisites — removed parenthetical elaborations that Claude already understands
- Removed blockquote template language in sections 3 and 8 — replaced with direct instructions
- Removed time-sensitive FTC rule reference ("FTC rule status uncertain as of 2026")
- Removed emoji from non-compete heading
- Shortened table cell text throughout (e.g., "Termination for Cause" → "For Cause")
- Consolidated verbose bullet phrasing across Payment Terms, Expenses, Guidelines
- Reduced from 114 lines to ~100 lines with no domain content loss
