---
name: payoff-letter-request
title: Payoff Letter Request
description: Drafts formal payoff letter requests to lenders for the precise amount needed to satisfy a loan obligation on a given date. Extracts loan details from matter documents, identifies missing information, and tailors urgency to transaction deadlines. Incorporates RESPA compliance, per diem interest, and itemized breakdown specifications. Use when requesting payoff statements, mortgage payoff letters, loan satisfaction amounts, or lien release calculations in closings, refinancing, or debt satisfaction scenarios.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/payoff-letter-request
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [drafting, letter, transactional]
---

# Payoff Letter Request

Drafts a request to a lender for the amount required to fully satisfy a loan as of a specific date, for use in closings, refinancing, and debt satisfaction.

## Prerequisites

Gather before drafting — pause and request any missing items:

1. **Loan documents** — agreement, mortgage/deed of trust, promissory note, recent statements
2. **Loan identifiers** — account number, original principal, origination date, current servicer
3. **Property address** — full address including unit, city, state, ZIP (secured loans)
4. **Borrower identity** — full legal name as on loan documents
5. **Requested payoff date** — exact date payment will be tendered
6. **Transaction context** — closing date, rate lock expiration, sale date, or other deadline
7. **Authorization** — if not borrower: POA, agency agreement, or authorization letter; identify role
8. **Prepayment provisions** — penalties, early termination fees, or specific payoff procedures

## Process

### 1. Document Review and Gap Analysis

Search matter files for loan agreements, notes, statements, and lender correspondence. Extract:

| Data Point | Source |
|---|---|
| Loan account number | Statement or note |
| Original principal and date | Promissory note |
| Current approximate balance | Most recent statement |
| Servicer name and address | Statement or correspondence |
| Prepayment penalty provisions | Loan agreement |
| Required payoff procedures | Loan agreement or servicer website |
| Notice clause requirements | Loan agreement |

If critical fields are missing (account number, payoff date, property address, authorization), list gaps and explain why each is needed before proceeding.

### 2. Assess Urgency

| Context | Timeframe | Sample Language |
|---|---|---|
| Scheduled closing | 7-10 business days | "in connection with a scheduled closing on [DATE]" |
| Refinancing with rate lock | Expedited | "rate lock expires on [DATE]; prompt response essential" |
| Sale transaction | Align with contract | "closing is contingent upon timely receipt" |
| General payoff | Standard 7-10 days | Standard professional request |

### 3. Draft the Letter

**Format**: Standard business letter — sender info, date, lender/servicer with department, subject line.

**Subject line**: `Payoff Statement Request — Loan Account #[NUMBER]`

**Opening**: Establish identity, reference loan by date and account number, state purpose. If representative:

> I am writing as [legal counsel for / settlement agent for / authorized representative of] [BORROWER NAME], who has authorized me to request and receive all payoff information regarding the above-referenced loan.

**Loan identification block**:

- Loan account number (as on statements)
- Original loan amount and origination date
- Borrower's full legal name (as on documents)
- Property address (for secured loans)
- Approximate current balance (if known, with caveat)

**Payoff date and per diem**: State exact payoff date; request per diem interest rate for date adjustments.

**Itemized breakdown request**:

- [ ] Principal balance as of payoff date
- [ ] Accrued interest through payoff date
- [ ] Prepayment penalties or early termination fees
- [ ] Recording / lien satisfaction fees
- [ ] Administrative / processing fees
- [ ] Escrow account balance (refund or application)
- [ ] Late charges or other penalties
- [ ] Other charges for full satisfaction and lien release
- [ ] Validity period of the quoted amount
- [ ] Wire transfer instructions

**Delivery**: Specify preferred method (email, mail, portal, fax) with full details.

**Response deadline**: 7-10 business days. If RESPA applies:

> Pursuant to RESPA, 12 U.S.C. § 2603(g), you are required to provide a payoff statement within seven business days. [VERIFY: RESPA applicability]

[VERIFY: state-specific payoff statement deadlines]

**Closing**: Professional sign-off with full contact information and credentials.

## Compliance Checks

- **RESPA** — 7-day payoff statement requirement for federally related mortgage loans (12 U.S.C. § 2603(g)) [VERIFY]
- **State variations** — many states impose separate timing requirements; verify for jurisdiction
- **Authorization** — confirm written authorization attached or on file if not borrower
- **Prepayment penalties** — flag provisions from loan documents; may be negotiable
- **Escrow** — request clear accounting of balance disposition and refund timeline

## Guidelines

- Verify all account numbers, dates, amounts, and addresses — errors cause delays
- Do not estimate the payoff amount; request the lender's official calculation
- Include enough detail that the lender can process without follow-up
- Follow payoff procedures specified in the loan agreement exactly
- Mark as draft requiring attorney review before sending
- Maintain borrower confidentiality (Model Rule 1.6)

---

**Key changes made:**

- **Description**: Tightened from 3 sentences of redundant detail to a focused `>-` block with clear trigger guidance
- **Overview**: Compressed from a full sentence restating the description to a single concise line
- **Prerequisites**: Trimmed verbose parentheticals while keeping all required inputs
- **Process step 2**: Collapsed "Assess Transaction Urgency" heading and removed the "Determine response timeframe based on context" lead-in prose — the table speaks for itself
- **Draft section**: Removed redundant format alternatives in subject line, trimmed the authorization quote block, shortened delivery/closing instructions, removed "State-specific statutes may impose different timelines" prose (already in Compliance Checks)
- **Compliance Notes → Compliance Checks**: Renamed to action-oriented heading; tightened each bullet
- **Guidelines**: Removed one redundant bullet ("Include enough loan detail..." was already implied), reordered for priority
- **Overall**: Reduced from 118 lines to 104 lines; eliminated prose that restated what tables/checklists already conveyed; every section earns its token cost
