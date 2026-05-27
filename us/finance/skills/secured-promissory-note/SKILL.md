---
name: secured-promissory-note
title: Secured Promissory Note
description: Drafts U.S. secured promissory notes for commercial lending with lender-protective terms, UCC Article 9 collateral grants, and state usury compliance. Trigger when the user needs a secured promissory note, lender note, collateral-backed loan note, or UCC-1 financing instrument.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/secured-promissory-note
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
tags: [agreement, corporate, drafting, transactional]
---

# Secured Promissory Note

Draft an enforceable secured promissory note for a commercial loan with collateral-backed repayment.

## Quick Start

Gather before drafting:

1. **Parties** — borrower and lender legal names, entity types, states, addresses, authorized signatories.
2. **Deal terms** — principal, interest structure (fixed/variable, index, margin, floor/cap), day-count convention, payment schedule, maturity, prepayment, fees, default rate.
3. **Collateral** — description with sufficient detail for UCC Article 9; filing jurisdictions (debtor location, fixture/real property).
4. **Governing law** — state, venue, dispute resolution preference.
5. **Related documents** — security agreement, guaranty, subordination/intercreditor, board/manager approvals.

## Workflow

1. Collect intake fields; flag unresolved items before drafting.
2. Draft using the section outline and template below.
3. Insert optional clauses only when deal-specific.
4. Run the review checklist.

### Intake Fields

| Field | Req | Notes |
|---|---|---|
| Borrower name, entity, state, address | Yes | Exact registered name and suffix |
| Lender name, entity, state, address | Yes | Match org docs |
| Effective date / funding date | Yes | Note if different |
| Principal amount | Yes | Numeric and words |
| Interest rate type | Yes | Fixed/variable; index, margin, floor/cap |
| Day-count convention | Yes | actual/360, actual/365, or 30/360 |
| Payment schedule | Yes | Frequency, amortization or balloon |
| Late fee / grace period | Yes | — |
| Default interest rate | Yes | Confirm within legal limits |
| Prepayment terms | Yes | Penalty, exceptions |
| Collateral description | Yes | Category + itemized detail |
| UCC filing jurisdictions | Yes | Debtor location; fixture/real property filings |
| Covenants | Opt | Reporting, insurance, restrictions |
| Cross-default thresholds | Opt | Other debt, judgments |
| Notice addresses / methods | Yes | Delivery methods, deemed receipt |

### Section Outline

1. Title, date, parties
2. Promise to pay; principal; use of proceeds
3. Interest rate; day-count; default rate; usury savings clause
4. Payment schedule; application waterfall; late charges; non-business days
5. Prepayment terms and penalties
6. Collateral grant; proceeds; security agreement reference
7. Perfection authorization (UCC-1 filings)
8. Representations and warranties
9. Affirmative and negative covenants
10. Events of default; notice and cure periods
11. Remedies; acceleration; UCC Article 9 enforcement; costs/fees
12. Waivers (presentment, demand, notice)
13. Governing law; venue; jury trial waiver or ADR
14. Notices; assignments; successors; integration; severability
15. Signature blocks and execution

### Collateral Schedule (Exhibit A)

```
Category:
Specific Description:
Location:
Title/Registration Data (if applicable):
```

### Optional Clauses

Include only when applicable:

- Balloon payment provision
- Interest-only period
- Cross-default to other material debt
- Judgment default threshold
- MAC clause
- Subordination / intercreditor references
- Cash dominion or lockbox

## Review Checklist

- [ ] Defined terms used consistently throughout
- [ ] Interest and fees within applicable usury limits
- [ ] Collateral description sufficient for UCC filing
- [ ] Cure periods aligned with lender policy
- [ ] Notice addresses and delivery methods complete
- [ ] Signatory authority confirmed

## Pitfalls

- **Usury** — always include a usury savings clause; verify default interest and late fees against governing-state limits.
- **Real property collateral** — reference the mortgage or deed of trust; the note alone is insufficient.
- **Titled assets / IP** — add perfection steps matching title or federal registration practices.
- **Default categories** — distinguish monetary vs. non-monetary defaults with explicit cure periods.
- **Remedies** — must include acceleration and Article 9 disposition rights with commercially reasonable notice.
- **Consumer loans** — omit consumer-law disclosures unless the loan is consumer-purpose or to an individual borrower.
- **Assignments** — borrower assignment typically prohibited; lender assignment typically permitted with notice.
- **Jury trial waiver** — include only if enforceable in governing jurisdiction and parties are sophisticated.
