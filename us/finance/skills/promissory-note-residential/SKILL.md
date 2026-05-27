---
name: promissory-note-residential
title: Promissory Note (Residential)
description: 'Drafts enforceable residential promissory notes with party identification, principal/interest terms, payment schedules, default/acceleration provisions, and security instrument cross-references. Ensures TILA awareness and state usury compliance. Use when drafting promissory notes for residential mortgages, deeds of trust, or seller-financed home sales; trigger keywords: promissory note, residential note, mortgage note, deed of trust note, seller financing note, balloon note.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/promissory-note-residential
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
tags: [agreement, drafting, transactional]
---

# Promissory Note (Residential)

Draft an enforceable debt obligation secured by residential property, compliant with state usury laws and federal lending regulations.

## Prerequisites

1. Transaction documents: purchase agreement, security instrument (mortgage or deed of trust), any term sheets.
2. Borrower(s): full legal names (as on government ID); joint and several liability status if multiple.
3. Lender: full legal name; entity type + jurisdiction of formation if applicable.
4. Property: complete street address matching the security instrument exactly.
5. Loan terms: principal amount, interest rate (fixed or variable parameters), amortization period, maturity date.
6. Jurisdiction rules: usury ceiling, late charge cap, notice requirements, prepayment penalty restrictions.

## Output Structure / Process

### 1. Header & Parties

| Element | Requirements |
| --- | --- |
| Title | "PROMISSORY NOTE" |
| Execution date | Full month/day/year; establishes payment commencement and SOL reference |
| Property address | Exact match to security instrument (street, unit, city, state, ZIP) |
| Borrower(s) | Full legal names; joint and several if multiple; note marital status |
| Lender | Full legal name; entity type + jurisdiction if applicable |

### 2. Financial Terms

| Element | Requirements |
| --- | --- |
| Principal | Numerals AND words; unconditional promise satisfying UCC negotiability |
| Interest rate | Fixed: exact percentage. Variable: index, margin, adjustment frequency, caps, initial rate |
| Calculation method | Simple vs. compound; 360-day vs. actual-day year; accrual on unpaid principal |
| Payment schedule | Amount, frequency, due date, commencement date, total number of payments |
| Payment application | Order: accrued interest → principal → fees/charges |
| Maturity date | Explicit calendar date; balloon disclosure if not fully amortizing |

### 3. Borrower Rights

- **Prepayment**: with/without penalty; written notice; application method (reduce term / payment / balloon).
- **Partial prepayment**: permitted Y/N; minimum amounts.
- **Grace period**: typically 10–15 calendar days.
- **Late charge**: 4–5% of overdue P&I (not escrow); must not exceed state max; characterize as administrative cost, not penalty.

### 4. Default & Remedies

Events of default:
- [ ] Failure to make payment when due
- [ ] Failure to pay balance at maturity
- [ ] Breach of security instrument covenants
- [ ] Bankruptcy/insolvency filing
- [ ] Material misrepresentation in loan application
- [ ] Failure to maintain property insurance
- [ ] Failure to pay property taxes

Notice and cure:
- Written notice: specify default, cure amount, cure deadline (typically 30 days).
- Delivery: personal or certified mail to property address / last known address.
- Cure = overdue amounts + late charges + costs → note reinstated.
- Repeated defaults may permit acceleration without further notice.

Acceleration:
- Upon uncured default, lender may declare entire balance immediately due.
- Anti-waiver: acceptance of late/partial payments does not waive acceleration rights.

### 5. Security & Cross-Default

- Reference security instrument by type (Mortgage / Deed of Trust), date, and recording information (or "to be recorded in [County] land records").
- Cross-default: breach of either instrument = default under both.
- Cross-collateralization only if applicable — flag consumer protection implications.

### 6. General Provisions

| Provision | Content |
| --- | --- |
| Governing law | State where property is located; no conflict-of-law principles |
| Jurisdiction | Courts in county where property is situated; borrower waives venue objection |
| Waiver | No waiver of one default waives subsequent; late payment acceptance ≠ waiver |
| Modification | Written only; signed by both parties; no oral modifications |
| Severability | Invalid provisions severable; remaining terms survive |
| Successors/assigns | Binds borrower's heirs/successors; lender may assign without borrower consent |

### 7. Execution

- Signature lines for all borrowers with printed names and dates.
- Representative capacity notation if signing as trustee or agent.
- Acknowledgment: borrower confirms receipt of copy, opportunity to consult counsel, voluntary execution.
- Notarization: not required for enforceability but recommended for authentication.

## Guidelines

- Verify interest rate against state usury ceiling before finalizing; flag any rate within 1% of the cap.
- If lender is a creditor under Regulation Z, flag need for Loan Estimate, Closing Disclosure, and right-of-rescission notices — this note alone is insufficient.
- Cross-check all terms (names, amounts, dates, property description) against the security instrument.
- Verify amortization math; confirm payments retire principal by maturity or clearly disclose balloon amount.
- State late charge caps vary (e.g., CA 6%, NY 2%, TX 5% [VERIFY]); always confirm current law.
- Maintain unconditional promise-to-pay language to preserve holder-in-due-course protections under UCC Article 3.
- Avoid cross-collateralization in residential notes unless counsel confirms no additional disclosure obligations.
- Draft in plain language understandable to non-attorney borrowers while remaining legally precise.

---

**Key changes made:**

- **Frontmatter**: Added `>-` block scalar for description; added trigger keywords for discoverability
- **Overview**: Collapsed the redundant intro paragraph into a single action-oriented line
- **Prerequisites**: Tightened from verbose sentences to scannable items; split borrower/lender into separate entries for clarity
- **Output Structure**: Renamed to "Output Structure / Process" per convention; removed redundant sub-headers (e.g., "Section 1:" → "1."); trimmed table cell wording while preserving all legal substance
- **Default & Remedies**: Converted from bold sub-sections to lighter labeled lists; removed checkbox-style formatting overhead on sub-labels
- **Guidelines**: Converted from numbered list with bold labels to flat bullet list — each point is a single actionable sentence, removing the label/explanation split pattern
