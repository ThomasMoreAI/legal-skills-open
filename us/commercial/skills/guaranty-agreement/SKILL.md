---
name: guaranty-agreement
title: Guaranty Agreement
description: Drafts U.S. commercial guaranty agreements securing a debtor's obligations to a creditor. Covers payment/collection elections, scope, caps, waivers, defaults, remedies, and enforceability. Trigger when the user needs a guaranty, guarantee, surety, continuing guaranty, payment guaranty, credit enhancement, or lender-required guaranty for loans, credit facilities, or real estate financing.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/guaranty-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: commercial
language: en
---

# Guaranty Agreement

Draft a commercially enforceable guaranty clarifying scope, liability, waivers, and remedies.

## Gather Before Drafting

1. **Underlying obligation** — date, parties, principal amount, obligations covered, maturity, collateral
2. **Guarantor** — legal name, entity type, jurisdiction, authority, address, financial condition
3. **Creditor** — legal name, address, notice info
4. **Elections** — payment vs collection, cap, term, continuing scope, governing law, dispute forum
5. **Execution** — signatories, titles, notarization or spousal consent if needed

## Elections Checklist

Resolve each before drafting:

- Type: `Payment` · `Collection`
- Scope: `All obligations` · `Specified obligations`
- Cap: `None` · `$[amount]`
- Term: `Continuing` · `Fixed end date`
- Survival: `Survives bankruptcy/insolvency`
- Multiple guarantors: `Joint and several` · `Several`
- Waivers: `Presentment/notice/defenses` included
- Subrogation: `Deferred until paid in full`
- Remedies: `Setoff` · `Costs` · `Attorneys' fees`
- Dispute: `Forum` · `Jury waiver` · `Arbitration`
- Notices: `Method` · `Address` · `Email allowed?`
- Assignment: `Creditor assignable` · `Guarantor restricted`

## Section Map

| Section | Content |
|---|---|
| Parties | Legal names, entity types, jurisdictions, addresses |
| Recitals | Underlying obligation summary, relationship, consideration |
| Definitions | "Obligations," "Guaranteed Obligations," "Guarantor," "Creditor" |
| Guaranty | Payment vs collection, unconditional, continuing, cap, survival |
| Waivers | Presentment, demand, notice, defenses, marshaling |
| Subrogation | No subrogation until paid in full |
| Consideration | Credit/forbearance and indirect benefit |
| Reps & Warranties | Authority, enforceability, solvency, no litigation |
| Covenants | Maintain existence, provide financials, no asset stripping |
| Events of Default | Payment default, covenant breach, insolvency, misrep |
| Remedies | Acceleration, direct action, setoff, fees |
| Governing Law | State law, jurisdiction, venue, jury waiver |
| Miscellaneous | Amendments, assignments, notices, counterparts, e-sign |
| Execution | Signature blocks with titles and dates |

## Drafting Steps

1. Define parties and underlying obligation details.
2. Insert elections from checklist.
3. Draft guaranty grant with scope, cap, and continuation.
4. Add waivers, subrogation deferral, and costs.
5. Add reps, covenants, defaults, and remedies.
6. Finalize boilerplate and execution blocks.

## Core Clause Templates

Guaranty grant:

```
Guarantor hereby unconditionally and irrevocably guarantees to Creditor the full and punctual payment and performance of the Guaranteed Obligations. This is a guaranty of [PAYMENT/COLLECTION] and not of collection only. [If payment: Creditor may proceed directly against Guarantor without first exhausting remedies against Debtor or collateral.] [If continuing: This guaranty is continuing and covers all present and future Obligations, whether direct or indirect, absolute or contingent, now existing or hereafter arising.]
```

Cap (if applicable):

```
Guarantor's maximum aggregate liability under this Guaranty shall not exceed $[AMOUNT], plus interest, fees, and enforcement costs to the extent permitted by law.
```

Waivers:

```
Guarantor waives presentment, demand, notice of acceptance, notice of default, protest, diligence, and all suretyship defenses, including any requirement that Creditor first proceed against Debtor or any collateral, and any defense arising from any modification, extension, or release of Debtor or collateral.
```

Subrogation:

```
Guarantor shall have no right of subrogation, reimbursement, contribution, or indemnity against Debtor until Creditor has been paid in full in cash.
```

Costs:

```
Guarantor shall reimburse Creditor for all reasonable costs of enforcement, including attorneys' fees and court costs.
```

Remedies:

```
Upon an Event of Default, Creditor may declare the Guaranteed Obligations immediately due and payable and exercise any and all rights and remedies available at law or in equity, including setoff.
```

Signature block:

```
GUARANTOR:
[Legal Name]
By: __________________________
Name:
Title:
Date:
```

## Pitfalls & Checks

- Specify payment vs collection explicitly — ambiguity invites dispute.
- State cap only if negotiated; otherwise confirm no cap.
- Tie consideration to the credit extension or forbearance.
- Confirm authority and solvency reps for entity guarantors.
- Never omit waiver of defenses when creditor expects payment guaranty.
- Include jury waiver only if enforceable in the governing jurisdiction.
- Verify jurisdiction-specific spousal consent or notarization requirements.
- Check statute of frauds compliance; check anti-deficiency rules if not purely commercial.
- Use consistent defined terms — capitalize and quote on first use.

---

**Key changes from original:**

- **Frontmatter**: Removed `tags` (not in spec), tightened `description` to third-person with explicit trigger guidance
- **Structure**: Renamed "Prerequisites" → "Gather Before Drafting", "Output Structure / Process" → split into focused sections ("Elections Checklist", "Section Map", "Drafting Steps", "Core Clause Templates"), "Guidelines" → "Pitfalls & Checks"
- **Token savings**: Removed redundant "Key Elections Checklist" / "Section Map Table" / "Drafting Steps" sub-headers under a single parent; stripped `text` language identifiers from code blocks; consolidated guideline prose into terse bullet checks
- **All legal substance preserved** — same elections, same section map, same clause templates, same enforceability guidance
