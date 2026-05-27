---
name: first-right-of-refusal-agreement
title: First Right of Refusal Agreement (Franchise)
description: Drafts a U.S. franchise first right of refusal (ROFR) agreement as an addendum or schedule to an existing Franchise Agreement. Trigger when a franchisor needs transfer-control protection covering third-party sale, change-of-control, or ownership-interest transfers. Covers notice flow, bona-fide-offer matching, exercise windows, anti-circumvention rules, carve-outs, valuation fallback, closing mechanics, and enforcement remedies.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/first-right-of-refusal-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: commercial
language: en
tags: [agreement, drafting, transactional]
---

# First Right of Refusal Agreement (Franchise)

Drafts a ROFR addendum to a U.S. Franchise Agreement that secures franchisor approval rights while preserving a lawful transfer path for the franchisee.

## Prerequisites

1. Signed Franchise Agreement with transfer/consent and termination clauses.
2. Party details: legal names, entity type, jurisdiction, authorized signers.
3. Governing law, venue, and equitable-remedy preferences.
4. Transfer framework: single- vs. multi-unit ownership; definition of control transfer.
5. Negotiation parameters: notice/election days, completion windows, carve-out policy, valuation approach, remedy priorities.

## Quick Start

Collect inputs before drafting:

| Input | Capture |
|---|---|
| Parties | Franchisor / franchisee names and addresses |
| Governed contract | Franchise Agreement date and cross-reference |
| Transfer scope | Asset sale, stock/membership transfer, merger, reorg, pledge |
| Trigger windows | Notice period, exercise period, closing period |
| Default remedies | Cure standards, breach consequences |
| Jurisdiction | Governing law, forum, service addresses |

## Drafting Order

1. Heading and recitals
2. Definitions
3. ROFR grant and covered-transaction scope
4. Notice-package requirements
5. Franchisor election process
6. Non-exercise / approval-to-close rules
7. Value and economics matching
8. Closing conditions and costs
9. Reinstatement and relationship to Franchise Agreement
10. Warranties, breaches, and remedies
11. Miscellaneous (assignment, survival, amendment, integration, notices, signatures)

Use clause-level placeholders throughout:

    [FRANCHISOR NAME]
    [FRANCHISEE NAME]
    [FRANCHISE EFFECTIVE DATE]
    [GOVERNING LAW]
    [NOTICE ADDRESS]

## Trigger Logic

| Condition | Franchisee action | Consequence |
|---|---|---|
| Bona fide third-party offer received | Deliver complete notice package within agreed days | Franchisor gets matching right |
| Incomplete notice | Cure request + fixed cure period | Exercise window paused until cured |
| Franchisor elects to purchase | Written election within exercise period | Binding purchase on matching terms |
| Franchisor declines / no response | Close only on materially identical terms | Material changes restart process |
| Sham or structured avoidance | Immediate breach workflow | Equitable relief + damages |

## Notice Package Checklist

- Signed offer docs (LOI / term sheet / purchase agreement)
- Purchase price and all payment components
- Financing terms and contingencies
- Identity and affiliates of proposed purchaser
- Escrow/security assumptions, liabilities, excluded assets
- Proposed closing timeline and conditions
- Non-circumvention and no-bad-faith-structuring certifications

## Timeline Blocks

Use numeric deadlines, not narrative-only terms:

    Notice deadline:              ____ business days after offer
    Franchisor exercise window:   ____ days after complete notice
    Closing target:               ____ days after election
    Third-party completion window: ____ days
    Materiality trigger:          price change >____% OR >$____

## Transfer Scope Matrix

| Transaction type | ROFR applies? | Notes |
|---|---|---|
| Direct sale of franchised business | Yes/No | Scope-defined |
| Controlling ownership transfer | Yes | Include mergers/reorgs |
| Minority non-controlling transfer | Yes/No | Clarify threshold |
| Estate or family transfer | Carve-out/conditional | Preserve franchisor rights |
| Pledge or collateralization | Optional carve-out | Define restart on default |

## Anti-Circumvention

Include provisions prohibiting:
- Step transactions structured to evade ROFR
- Pre-closing assignment/flip structures without disclosure
- Related-party or changed-party deals without refreshed notice and election period

## Pitfalls and Checks

- Lock definitions first — every operative clause must reference defined terms.
- Harmonize with Franchise Agreement transfer provisions; state which document controls on conflict.
- Separate scope exceptions (family, estate, affiliate) from approval rights to reduce interpretation disputes.
- Preserve full remedy stack: injunctive relief, specific performance, attorneys' fees, and Franchise Agreement termination rights.
- Use fixed deadlines, not vague "reasonable" language, for all time-bound obligations.
- Never leave undefined attachment or exhibit references.
- If enforceability is jurisdiction-sensitive, flag for legal review: reasonableness of restraints on alienation, time-limit adequacy, remedy limits. [VERIFY]
