---
name: intercreditor-lien-priority
title: Intercreditor Agreement (Lien Priority)
description: 'Drafts U.S. intercreditor agreements establishing first lien vs second lien priority over shared collateral, covering standstill, enforcement control, payment waterfall/turnover, and 11 U.S.C. 510(a) subordination. Use for first lien/second lien financings, refinancing, or intercreditor negotiations requiring lien priority and remedies governance. Trigger: intercreditor, lien priority, first lien, second lien, standstill, turnover, payment waterfall, subordination agreement.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/intercreditor-lien-priority
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
tags: [agreement, drafting, transactional]
---

# Intercreditor Agreement (Lien Priority)

Allocates collateral control, remedies, and payment rights between first lien and second lien creditors under a shared collateral structure.

## Quick Start

1. Collect first lien and second lien credit/security documents.
2. Populate the intake table below from deal term sheet.
3. Confirm key elections with parties.
4. Draft per article outline; run required-clauses checklist before delivery.

## Intake

| Field | Source | Notes |
|---|---|---|
| Parties/roles | Term sheet | Agents, lenders, borrower, guarantors |
| Collateral scope | Security agreements | Shared vs excluded collateral |
| Obligations scope | Credit agreements | Principal, interest, fees, hedging, LCs |
| Standstill period | Term sheet | Exact days and triggers |
| Permitted payments | Term sheet | Allowed payments to second lien, if any |
| Bankruptcy positions | Term sheet | DIP, cash collateral, 363 sale, plan voting |
| Governing law | Term sheet | Commonly NY or DE |

## Key Elections

| Election | Options | Insert |
|---|---|---|
| Standstill trigger | First lien EoD notice or occurrence | [INSERT] |
| Standstill length | Fixed days | [__] days |
| Permitted payments to 2L | None / limited | [INSERT] |
| 2L enforcement after standstill | Allowed / restricted | [INSERT] |
| Borrower party | Signatory / acknowledgment | [INSERT] |
| Discharge definition | Cash pay + cash collateralize | [INSERT] |

## Article Outline

1. Definitions and construction
2. Lien priority and subordination
3. Enforcement rights and standstill
4. Payment waterfall and turnover
5. Bankruptcy and insolvency
6. Amendments/restrictions on second lien documents
7. Representations and warranties
8. Covenants and cooperation
9. Miscellaneous (governing law, jurisdiction, notices, jury waiver, successors)

## Required Clauses Checklist

- [ ] Absolute first lien priority over shared collateral regardless of perfection timing
- [ ] Subordination continuing until Discharge of First Lien Obligations
- [ ] Exclusive enforcement control by first lien agent during standstill
- [ ] Turnover obligation for junior receipts
- [ ] Proceeds waterfall: first lien first, then second lien
- [ ] Prohibition on junior objections to first lien enforcement (with negotiated carve-outs)
- [ ] Bankruptcy subordination under 11 U.S.C. 510(a)
- [ ] Restrictions on second lien document amendments that worsen senior position
- [ ] Notice mechanics and amendment consent requirements

## Template Snippets

Standstill clause:

```text
"Standstill Period" means the period beginning on the date the First Lien Agent delivers written notice of a First Lien Event of Default and ending [__] days thereafter.

During the Standstill Period, the Second Lien Secured Parties shall not take any Enforcement Action with respect to the Collateral or contest any Enforcement Action taken by the First Lien Secured Parties.
```

Turnover clause:

```text
Any payment or distribution received by any Second Lien Secured Party in violation of this Agreement shall be held in trust and immediately turned over to the First Lien Agent for application in accordance with the Payment Waterfall.
```

## Pitfalls and Checks

- **Lien vs debt subordination**: Use lien subordination language unless debt subordination is also intended; align waterfall and turnover accordingly.
- **Discharge definition**: Must include cash collateralization or backstop of contingent LC/hedging exposure.
- **Permitted junior payments**: If allowed, limit to scheduled interest and fees when no first lien default exists.
- **Bankruptcy provisions**: Confirm 11 U.S.C. 510(a) enforceability; address cash collateral, DIP financing, relief from stay, and plan voting. Verify post-petition interest allocation under 11 U.S.C. 552(b)(1) [VERIFY].
- **UCC Article 9**: Confirm perfection status; verify after-acquired property and proceeds coverage.
- **Borrower covenants**: If borrower is a party, include covenant not to direct payments contrary to waterfall.
- **Post-standstill rights**: Define narrowly whether junior creditors may file proofs of claim or seek adequate protection after standstill expiry.
- **Consistency**: Keep defined terms aligned across agreement; cross-reference credit documents precisely. Match notices, consent, and assignment provisions to deal structure.
