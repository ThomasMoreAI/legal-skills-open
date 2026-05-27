---
name: assignment-assumption
title: Assignment and Assumption Agreement
description: 'Drafts Assignment and Assumption Agreements transferring contractual rights and obligations from assignor to assignee in asset purchase transactions. Covers assignment mechanics, liability assumption with temporal cutoff, third-party consent handling, reps and warranties, indemnification, and Exhibit A contract schedule. Trigger keywords: "assignment and assumption", "contract transfer", "assign contracts", "assume obligations", "asset purchase closing document", "assignor assignee agreement".'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/assignment-assumption
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [agreement, drafting, transactional]
---

# Assignment and Assumption Agreement

Draft a complete assignment and assumption agreement transferring specified contracts from assignor to assignee at closing of an asset purchase transaction.

## Prerequisites

1. **Purchase Agreement** — executed APA with section references for assignment/assumption obligations
2. **Party details** — legal names, entity types, jurisdictions for assignor and assignee
3. **Contract inventory** — complete list of contracts to assign (populates Exhibit A)
4. **Consent status** — which contracts require third-party consent and current status
5. **Effective date and governing law** — closing date, chosen state law, forum

## Document Skeleton

```text
ASSIGNMENT AND ASSUMPTION AGREEMENT
- Parties; Effective Date; Defined Terms
- Recitals (WHEREAS clauses)
1. Assignment
2. Assumption of Obligations
3. Third-Party Consents
4. Representations and Warranties
5. Indemnification
6. General Provisions
- Signature Blocks
- Exhibit A — Assigned Contracts
```

## Core Drafting Checklist

**Recitals**
- Reference Purchase Agreement, business/assets, and specific section requiring assignment/assumption.
- Acknowledge third-party consent requirements if applicable.
- Include NOW THEREFORE with consideration language.

**§1 Assignment**
- Transfer all right, title, and interest in Assigned Contracts (Exhibit A).
- Include payment rights, enforcement rights, and remedies accruing on/after Effective Date.
- Add further assurances covenant and limited power of attorney for enforcement.

**§2 Assumption**
- Assume obligations arising on/after Effective Date only.
- Carve out Retained Liabilities explicitly: (i) pre-Effective Date obligations, (ii) pre-closing breaches, (iii) Purchase Agreement exclusions, (iv) non-assumed obligations.

**§3 Consents**
- Commercially reasonable efforts to obtain consent.
- No assignment effective until consent received.
- Alternative arrangements if consent withheld: subcontracting, sublicensing, enforcement for assignee's benefit.
- Payment pass-through mechanics.

**§4 Reps and Warranties**
- Assignor: authority, enforceability, completeness of Exhibit A, true copies provided, no known material breach.
- Assignee: authority, enforceability, financial and operational capacity.

**§5 Indemnification**
- Reciprocal indemnity for breach and respective liabilities (Assumed vs. Retained).
- Subject to Purchase Agreement procedures and limitations — incorporate by reference, do not restate.

**§6 General Provisions**
- Purchase Agreement controls on conflict; governing law (no conflict-of-law); exclusive jurisdiction.
- Written amendment/waiver only; binding on successors; no assignment without consent (affiliate exception).
- Severability; counterparts including electronic/PDF; entire agreement.

## Exhibit A Template

```text
EXHIBIT A — ASSIGNED CONTRACTS

| # | Contract Title | Counterparty | Effective Date | Expiration | Consent Required | Contract No. |
|---|----------------|--------------|----------------|------------|------------------|--------------|
| 1 | [Description]  | [Party]      | [Date]         | [Date/N/A] | [Yes/No]         | [Ref]        |
```

## Key Defined Terms

- **Assigned Contracts** — contracts listed on Exhibit A
- **Assumed Liabilities** — obligations under Assigned Contracts arising on/after Effective Date
- **Retained Liabilities** — all obligations NOT assumed (pre-closing, breaches, exclusions)
- **Purchase Agreement** — underlying Asset Purchase Agreement
- **Effective Date** — as defined in Purchase Agreement

## Pitfalls

- Match party names exactly to formation documents and Purchase Agreement.
- Cross-reference correct APA section numbers — do not guess.
- Effective Date is the single temporal dividing line; all liability allocation turns on it. Keep consistent throughout.
- Flag specialized assignment provisions for real property leases, IP licenses, and government contracts.
- Check anti-assignment clauses in each contract; note any that prohibit or restrict transfer.
- Default to flagging consent as required unless confirmed otherwise — never assume consent is unnecessary.
- If jurisdiction-specific statutes apply (e.g., UCC Article 9 for receivables), note and conform.
- Counterparts clause must expressly cover electronic/PDF execution.

---

Key changes from the original:

- **Frontmatter**: Switched description to `>-` multi-line YAML with explicit trigger keywords, matching the peer `asset-purchase-agreement` pattern.
- **Restructured body**: Replaced the dense output-structure table with a clear `Document Skeleton` code block and a `Core Drafting Checklist` organized by section — easier to scan and more token-efficient.
- **Removed redundancy**: The overview no longer repeats the description. Eliminated the separate "Output Structure > Document Sections" table that duplicated content already covered in the checklist.
- **Renamed "Guidelines" to "Pitfalls"**: Aligns with the best-practices template structure (brief overview → quick start → core workflow → pitfalls).
- **Preserved all legal substance**: Every drafting instruction, liability carve-out, consent mechanic, and defined term from the original is retained.
