---
name: commercial-promissory-note
title: Commercial Promissory Note
description: Drafts UCC-compliant U.S. Commercial Promissory Notes for commercial real estate finance transactions. Produces negotiable instruments with principal, interest, payment, default, and enforcement provisions protecting lender interests. Use when drafting promissory notes secured by real property, deed of trust, or mortgage in commercial lending.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/commercial-promissory-note
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
tags: [agreement, drafting, transactional]
---

# Commercial Promissory Note

Drafts a UCC Article 3–compliant Commercial Promissory Note for U.S. commercial real estate finance, structured to protect Payee/lender at negotiation and closing.

## Prerequisites

Collect before drafting:

1. **Parties** — Full legal names, entity types, principal places of business for Maker (borrower) and Payee (lender)
2. **Loan economics** — Principal amount, interest rate (fixed or variable index + margin), day-count convention, maturity date
3. **Payment structure** — Installment amounts/frequency, interest-only period, balloon payment date
4. **Security** — Recording county/state, property address, legal description or reference to deed of trust/mortgage of even date
5. **Governing law** — Jurisdiction (required for usury and prepayment penalty compliance)
6. **Prepayment terms** — Permitted/prohibited, penalty schedule, exceptions (casualty, condemnation)

## Quick Start

1. Gather all prerequisites above
2. Draft header with title `PROMISSORY NOTE`, principal in numerals and written form, execution date, city, state
3. Build sections per the template below
4. Run the verification checklist before finalizing

## Sections

| Section | Required Elements | Drafting Rules |
|---|---|---|
| **Promise to Pay** | Maker, Payee, "for value received," "to the order of" | Unconditional language only — conditions destroy UCC negotiability |
| **Interest Rate** | Rate (% p.a.), simple/compound, day-count (360 or actual/365), accrual start | Variable: SOFR index + margin, caps/floors, adjustment frequency; include usury savings clause |
| **Payment Schedule** | Payment count, amount/method, due date, commencement, maturity | Specify payment address/account; grace period before late charge |
| **Application of Payments** | Priority: (1) fees → (2) accrued interest → (3) principal | Address partial payments; flag negative-amortization risk if interest-only |
| **Late Charges** | Grace period (10–15 days typical), charge (4–5% of overdue or flat fee) | Must not exceed state maximum; acceptance ≠ waiver of default |
| **Prepayment** | Permitted/prohibited; partial/whole; penalty schedule; exceptions | Step-down if used (e.g., 3%/2%/1%); address casualty/condemnation proceeds |
| **Events of Default** | Monetary (payment failure + cure); non-monetary (covenant breach, bankruptcy, misrepresentation); cross-default | Monetary cure: 10 days written notice; non-monetary: 30 days; use objective triggers |
| **Remedies / Acceleration** | Optional acceleration of full balance + accrued interest; cumulative remedies | Non-exercise ≠ waiver; default interest rate if permitted; attorneys' fees as secured obligation |
| **Security Reference** | Deed of trust/mortgage of even date; property address + county/state; recourse or non-recourse | Non-recourse carve-outs: fraud, environmental, waste, misapplication of rents |
| **Maker Waivers** | Presentment, demand, notice of dishonor, protest, notice of default/acceleration | Bold or ALL CAPS per state conspicuousness rules; waive right to require Payee to proceed against collateral first |
| **Attorneys' Fees** | Prevailing party: reasonable fees + costs (trial, appeal, bankruptcy, collection) | Fees = secured obligation; check state mandatory-mutuality rules |
| **General** | Governing law, severability, successors/assigns, written amendment only, notice provisions, time-is-of-the-essence, integration | No Maker setoff/counterclaim unless negotiated |
| **Signature Block** | Entity: legal name + "By:" + signatory name/title + date; Individual: signature + name + date | Confirm signatory authority; joint Makers = joint and several; counterparts clause |

## Verification Checklist

Run before finalizing:

- [ ] Promise is unconditional and payable "to the order of" (UCC Art. 3 negotiability)
- [ ] Interest rate ≤ governing state usury ceiling — [VERIFY state-specific limit]
- [ ] Usury savings clause included (excess interest → applied to principal or refunded)
- [ ] Day-count convention stated explicitly (360 or actual/365)
- [ ] Variable rate uses SOFR (not LIBOR) with publication source and fallback language
- [ ] Prepayment penalty complies with governing state rules — [VERIFY state restrictions]
- [ ] Non-recourse carve-outs (if applicable) are enumerated explicitly, not vague
- [ ] Terms align with related deed of trust/mortgage, loan agreement, and guaranty
- [ ] Cross-default provisions mirrored across all security documents
- [ ] If any Maker is an individual, confirmed TILA/Reg Z/state consumer statutes do not apply (skill targets commercial transactions only)
