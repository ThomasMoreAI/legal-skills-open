---
name: pa-workflow-transactional-clause-library-check-sboghossian
title: Clause Library Check
description: Use when a transactional team needs to verify that a contract uses the firm's or client's preferred standard clauses and flag deviations. Parses contract clauses, maps them against a firm clause library, highlights non-standard language, suggests replacement with the library version, and tracks which clauses deviate most frequently as a knowledge-base feedback loop. Applicable across MENA and multi-jurisdiction commercial contracts.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-transactional-clause-library-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Clause Library Check

## Purpose

Firms and in-house legal teams invest significantly in building playbooks and standard clause positions. This workflow ensures that every reviewed contract is checked against the approved library — surfacing deviations automatically, suggesting the approved replacement language, and tracking deviation patterns to improve the library over time. The output is a clause-by-clause compliance report with redline suggestions.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Contract document | Yes | PDF, Word, or plain text |
| Firm / client clause library | Yes | JSON, spreadsheet, or document format — defines standard clause positions |
| Contract type | Yes | MSA, NDA, SPA, employment contract, lease, etc. — determines which library sections apply |
| Deviation tolerance | Optional | "Must use" clauses (no deviation allowed) vs. "preferred" clauses (deviation requires justification) |
| Counterparty profile | Optional | Known aggressive counterparty? Adjust deviation flagging sensitivity |

## Processing Steps

### Step 1 — Contract parsing

Parse the contract into discrete clause units:
- Number each clause by section reference (e.g., Clause 14.3, Article 6(b))
- Identify clause type: limitation of liability, indemnification, termination, IP ownership, governing law, dispute resolution, confidentiality, payment terms, force majeure, etc.
- Flag clauses without a library counterpart as "novel / non-standard" for manual review

### Step 2 — Library mapping

For each parsed clause:
- Match to the relevant clause type in the library
- Pull the library's standard language for that clause type + contract type combination
- Run a comparison: word-level diff between the contract clause and the library standard

Matching considerations:
- Clause purpose matters more than literal text — a limitation of liability cap expressed as "aggregate fees paid in the three-month period" matches the library's "fees paid in the preceding quarter" (same position, different expression)
- Flag material meaning differences, not stylistic differences
- Recognize when clauses are absent entirely (library requires a clause that the contract omits)

### Step 3 — Deviation classification

For each deviation found, classify:

| Class | Definition | Example |
|---|---|---|
| MATERIAL-ADVERSE | Deviation materially disadvantages our client vs. library position | Liability cap: library = 12 months' fees; contract = 3 months' fees |
| MATERIAL-FAVORABLE | Deviation improves on the library position | Indemnity: contract grants broader IP indemnity than library standard |
| NON-MATERIAL | Stylistic or structural difference; same substance | Different definition of "Confidential Information" that captures same scope |
| MISSING | Required clause absent from contract | No governing law clause; no dispute resolution clause |
| NOVEL | Clause present in contract with no library equivalent | New AI-governance clause; new data processing terms |

Only MATERIAL-ADVERSE and MISSING deviations require automatic escalation. MATERIAL-FAVORABLE deviations should be flagged but not automatically replaced. NON-MATERIAL deviations should be noted but do not require redlining.

### Step 4 — Replacement suggestions

For each MATERIAL-ADVERSE or MISSING deviation:
- Quote the current contract language
- Quote the library standard
- Provide a redlined version showing the proposed change
- Add a brief rationale (why the library position is preferred)

### Step 5 — Knowledge-base feedback loop

Track deviation patterns across all contracts checked:
- Which clauses deviate most frequently?
- Which counterparties consistently push back on specific clauses?
- Which library positions are outdated (consistently negotiated away)?

Output a quarterly deviation report that feeds back into library maintenance — see [[pa-workflow-transactional-msa-against-firm-playbook]] for the playbook equivalent.

## Output Format

### Clause-by-clause report

```markdown
## Clause Library Check Report — [Contract Name] — [Date]

### Summary
- Clauses reviewed: 34
- Library matches (compliant): 21
- Material-Adverse deviations: 4 [MUST FIX]
- Material-Favorable deviations: 2 [NOTE]
- Non-Material deviations: 5 [COSMETIC]
- Missing required clauses: 2 [MUST ADD]
- Novel clauses (no library equivalent): 1 [REVIEW]

---

### MATERIAL-ADVERSE DEVIATIONS (4)

#### Clause 15.1 — Limitation of Liability
**Contract language**: "Neither party shall be liable for aggregate damages exceeding the fees paid in the month preceding the claim."
**Library standard**: "Neither party shall be liable for aggregate damages exceeding the total fees paid in the twelve (12) months preceding the claim."
**Deviation**: Cap is 1 month vs. library's 12 months — a 12x reduction
**Proposed redline**: [full redlined clause]
**Rationale**: Our standard 12-month cap reflects market practice; a 1-month cap is extremely favorable to the counterparty and inadequate protection for a long-term MSA.

---

### MISSING REQUIRED CLAUSES (2)

#### Missing: Governing Law and Dispute Resolution
**Library requirement**: All contracts must specify governing law and a designated dispute resolution forum.
**Proposed addition**: [standard DIFC governing law + DIAC arbitration clause from library]
**Rationale**: Without this clause, courts will apply default rules (potentially unfavorable jurisdiction for our client).
```

## Jurisdictional Notes

### Governing Law and Dispute Resolution Clauses

This is the highest-stakes missing clause in MENA contracts:
- **UAE mainland entities**: Without an explicit choice of law, UAE courts apply Federal law and mandatory rules. For commercial disputes, DIFC or ADGM governing law + DIAC/ADCCAC arbitration is preferred for international contracts.
- **KSA entities**: Saudi law is the default; courts apply Sharia-based commercial law. Saudi entities often resist foreign governing law in contracts involving Saudi performance.
- **Lebanon**: Lebanese law applies by default; French-influenced civil law. LCIA or ICC arbitration is standard for international contracts.
- **Egypt**: Egyptian Civil Code applies by default; party choice of law is respected in commercial contracts. CRCICA arbitration or ICSID for investment disputes.

### Language of Contract

- UAE and KSA courts require Arabic as the official language. English contracts are accepted but in court proceedings, the Arabic version prevails if there is a conflict. Library should include an "Arabic version prevails" vs. "English version prevails" clause position per contract type.
- DIFC / ADGM: English language contracts fully enforceable; no Arabic requirement.

### Notarization / Authentication

Some clause types (powers of attorney, certain commercial agreements) require notarization under UAE or KSA law. The clause library should flag any contract type where notarization of key provisions (signature pages, authority clauses) is required.

## Common Mistakes

- Treating all deviations as equally important — triage by MATERIAL-ADVERSE vs. cosmetic
- Not updating the library to reflect consistently negotiated-away positions
- Missing the "novel clause" category — contracts increasingly include AI, data, and cybersecurity clauses with no library equivalent
- Failing to check for absent clauses — a complete contract with all deviations compliant is worse than an incomplete contract with a missing governing-law clause

## Related Skills

- [[pa-workflow-transactional-msa-against-firm-playbook]]
- [[pa-workflow-transactional-contract-redline-20min]]
- [[pa-workflow-transactional-nda-triage-red-yellow-green]]
- [[pa-workflow-transactional-deal-point-analysis]]
