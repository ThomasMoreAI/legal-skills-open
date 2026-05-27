---
name: collateral-assignment-of-contracts
title: Collateral Assignment of Contracts
description: Drafts a Collateral Assignment of Contracts assigning a borrower's contractual rights as security for debt under UCC Article 9. Triggers when securing lender interests in contract rights, drafting pre-closing security documents, or structuring collateral packages for U.S. commercial credit facilities.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/collateral-assignment-of-contracts
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
tags: [agreement, drafting, transactional]
---

# Collateral Assignment of Contracts

UCC Article 9-compliant security instrument assigning a borrower's contractual rights to a lender as collateral for a debt obligation.

## Prerequisites

Gather before drafting:

1. **Loan/credit agreement** — principal, date, parties, default provisions
2. **Assigned contracts** — name, date, counterparties, subject matter, ID numbers, payment terms
3. **Party details** — legal names, jurisdiction of organization, principal place of business (Assignor and Assignee)
4. **Consent posture** — whether counterparty consent is required or obtained
5. **Governing law** — typically Assignee's jurisdiction or UCC Article 9 choice-of-law location
6. **Filing intent** — separate UCC-1 filing or authorization language in the instrument

## Document Sections

### 1. Parties

- **Assignor** (Borrower/debtor) — legal name, state of org, principal office
- **Assignee** (Lender/secured party) — same; note capacity as secured party
- **Obligors** (Contract counterparties) — include if notice/consent is relevant

### 2. Recitals

- Identify underlying debt with specificity (date, principal, parties)
- Identify each assigned contract (date, parties, subject matter, contract number)
- State assignment is **as security**, not absolute transfer

### 3. Assignment Clause

Grant Assignee a **security interest** in Assignor's right, title, and interest in:
- Each identified contract
- All payment rights, proceeds, and benefits thereunder
- All proceeds (insurance, condemnation awards, substitute collateral)

Address explicitly:
- **Present vs. future rights** — affects perfection under UCC § 9-204 [VERIFY state enactment]
- **Pre-default enforcement** — whether Assignee may collect before default or rights reserved to Assignor
- **Proceeds direction** — ordinary-course collection by Assignor vs. lockbox/direct remittance

### 4. Representations and Warranties

- **Authority** — full right and power to grant security interest
- **Ownership** — sole owner; free of liens except as disclosed
- **Contract validity** — assigned contracts valid, binding, enforceable
- **No defaults** — no existing defaults under assigned contracts
- **No prior assignments** — no prior security interests in same contracts
- **Consents** — all required counterparty consents obtained (or none required)

### 5. Covenants

**Affirmative:** perform contract obligations; maintain contracts in force; provide counterparty notice if required; deliver periodic status reports; notify Assignee of defaults, disputes, or material adverse changes.

**Negative:** no amendment/termination of assigned contracts without Assignee consent; no additional security interests in same collateral.

### 6. Default and Remedies

**Triggers:** payment failure; breach of rep/warranty/covenant; Assignor bankruptcy/insolvency; default under assigned contract.

**Assignee remedies (UCC Article 9):** notify counterparties; collect payments directly; enforce contracts in Assignee's or Assignor's name; apply proceeds to debt with surplus accounting.

Align notice-and-cure periods with underlying loan agreement.

### 7. Boilerplate

Governing law, entire agreement, severability, amendment (written consent), non-waiver, notices, successors/assigns (no Assignor assignment without consent), further assurances, UCC-1 filing authorization (if applicable), counterparts.

### 8. Signature Blocks

Authorized representative for each party (name, title, date). Add notarization if jurisdiction requires. Add corporate secretary attestation if entity governance requires.

## Pitfalls and Checks

- **Perfection**: Contract rights are general intangibles — perfect by UCC-1 filing. Confirm jurisdiction under UCC § 9-307 (Assignor's location) [VERIFY]
- **Anti-assignment clauses**: Review each assigned contract for transfer restrictions; obtain consent/waiver pre-closing
- **Future rights**: Assignment of unexecuted contracts requires UCC § 9-204 drafting and may have delayed attachment [VERIFY]
- **Obligor notice**: Under UCC § 9-406, notified counterparties must pay Assignee — coordinate timing with Assignor's operations
- **Proceeds scope**: Define broadly (insurance, condemnation, substitute collateral)
- **Loan agreement alignment**: Default definitions, cure periods, and remedy triggers must match the underlying credit agreement

---

**Key changes made:**
- Tightened the `description` frontmatter — shorter, third-person, with explicit trigger guidance
- Replaced verbose tables (Parties, Reps & Warranties) with compact bullet lists
- Collapsed Covenants into inline semicolon-delimited lists (affirmative/negative)
- Condensed Default/Remedies and Boilerplate into terse formats
- Renamed "Guidelines" → "Pitfalls and Checks" for clarity
- Renamed "Output Structure" → "Document Sections" 
- Removed redundant prose throughout while preserving all legal substance and [VERIFY] markers
