---
name: pa-workflow-transactional-msa-against-firm-playbook-sboghossian
title: MSA Against Firm Playbook
description: Use when a transactional lawyer needs to review an incoming Master Services Agreement (MSA) against the firm's or client's pre-defined negotiation playbook. Loads the playbook's positions on key clauses, compares the incoming MSA clause by clause, scores deviations, highlights required negotiation positions, and generates a tracked-changes redline with playbook-sourced replacement language. Integrates with the firm knowledge RAG for playbook retrieval.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-transactional-msa-against-firm-playbook
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# MSA Against Firm Playbook

## Purpose

A firm or in-house legal team's MSA playbook represents its accumulated negotiating knowledge — the positions it will accept, the positions it will fight, and the language it prefers. This workflow applies that playbook automatically to any incoming MSA, transforming a document-by-document review process into a systematic, consistent, and fully annotated redline. The result is counsel's time spent on exceptions and edge cases, not on re-establishing positions the firm has already decided.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Incoming MSA (counterparty's form) | Yes | PDF or Word |
| Firm playbook | Yes | Loaded via [[tool-rag-firm-knowledge]] or uploaded directly |
| Client's position (service provider or customer) | Yes | The playbook may have different positions depending on which side the client is on |
| Jurisdiction | Recommended | Governs interpretation of any legal standards referenced |
| Counterparty profile | Optional | Known aggressive counterparty? History with this company? |
| Deal context | Optional | Value, duration, sensitivity of services |

## Processing Steps

### Step 1 — Load firm playbook

Retrieve the playbook from the firm knowledge base via [[tool-rag-firm-knowledge]] using the contract type and client position as query parameters. The playbook contains:
- **Must-have** positions: terms the firm will not waive (e.g., mutual limitation of liability, fraud carve-out)
- **Standard** positions: preferred language; negotiable within defined parameters
- **Fallback** positions: acceptable compromise language if counterparty pushes back
- **Redlines**: specific language changes the firm always makes to counterparty forms
- **Absolute red lines**: terms the firm will not accept under any circumstances (e.g., unlimited liability)

### Step 2 — Parse the incoming MSA

Identify all material clauses:
- Definitions and scope of services
- Fees and payment terms
- Intellectual property (ownership of deliverables, background IP, license grants)
- Confidentiality
- Data protection and security
- Representations and warranties
- Indemnification
- Limitation of liability
- Term and termination
- Governing law and dispute resolution
- Change of control
- Assignment
- Force majeure

### Step 3 — Score against playbook

For each clause, score:

| Score | Label | Meaning |
|---|---|---|
| 5 | ACCEPT | Matches firm's standard or is better than standard |
| 4 | ACCEPT WITH MINOR EDIT | Minor language improvement from playbook; low priority |
| 3 | NEGOTIATE | Deviates from standard; use playbook fallback position in negotiation |
| 2 | MUST CHANGE | Deviates materially from standard; use playbook preferred language |
| 1 | RED LINE | Absolute red line; cannot accept; walk away if not changed |

### Step 4 — Generate redline

For each clause scoring 1–3, produce:
- **Current language** (from incoming MSA)
- **Playbook position** (what the firm normally requires)
- **Proposed redline** (tracked-changes version of the clause with firm's language)
- **Negotiation note** (why this matters; what the fallback is; how hard to push)

### Step 5 — Produce negotiation summary

A one-page summary for the client or senior partner:
- How many red lines triggered?
- Key negotiating priorities in order
- Which positions to lead with; which to trade
- Any novel clauses not covered by the playbook (escalate for position determination)

## Output Format

### Playbook Compliance Scorecard

```markdown
## MSA Playbook Review — [Counterparty] — [Date]

### Overall assessment: 67/100 (NEGOTIATE REQUIRED)

| Clause | Score | Label | Priority |
|---|---|---|---|
| Limitation of liability | 1 | RED LINE | CRITICAL |
| IP ownership of deliverables | 2 | MUST CHANGE | HIGH |
| Payment terms | 4 | ACCEPT WITH MINOR EDIT | LOW |
| Governing law | 5 | ACCEPT | — |
| Confidentiality | 3 | NEGOTIATE | MEDIUM |
| Data protection | 2 | MUST CHANGE | HIGH |
| Force majeure | 4 | ACCEPT WITH MINOR EDIT | LOW |
| Change of control | 1 | RED LINE | CRITICAL |

### CRITICAL RED LINES (2)

#### Limitation of Liability (Clause 17)
**Current**: "In no event shall [Service Provider] be liable to Customer for any amounts exceeding USD 10,000 in the aggregate."
**Playbook standard**: Mutual cap = 12 months' fees; minimum USD 500,000 floor
**Issue**: Cap is absolute at USD 10,000 regardless of contract value; playbook requires proportionate cap and mutuality
**Playbook redline**: [Full clause with tracked changes]
**Negotiation note**: This is a deal-breaker. If counterparty refuses to move, escalate to senior partner before proceeding. Fallback: 3 months' fees cap with mutual carve-out for gross negligence.

#### Change of Control (Clause 23)
**Current**: "Either party may terminate this Agreement upon 5 days' notice if the other party undergoes a change of control."
**Playbook standard**: Firm requires consent right (not automatic termination) on change of control; minimum 30 days' notice
**Issue**: 5 days is commercially unworkable; automatic termination without consent right is a structural problem
**Playbook redline**: [Full clause with tracked changes]
```

## MENA-Specific MSA Issues

### IP Ownership — MENA Context

In UAE and KSA, the default rule under employment law is that employer-owned work created within the scope of employment belongs to the employer. However, this rule does not automatically apply to contractor/vendor deliverables — the contract must assign IP ownership explicitly.

For technology MSAs in the UAE and KSA:
- Deliverables developed specifically for the client should be assigned to the client (work-for-hire equivalent)
- Background IP (pre-existing tools, frameworks, libraries) should be licensed to the client for use of the deliverables; ownership stays with the vendor
- Open-source components must be disclosed — GPL/LGPL copyleft provisions create contamination risk

### Data Protection Obligations

Any MSA involving data processing must include a data processing addendum (DPA) or data processing agreement (DPA) if the counterparty processes UAE resident personal data (under PDPL-UAE 2022), Saudi resident data (under PDPL KSA 2024), or EU/UK resident data (GDPR / UK GDPR). If no DPA is attached, flag as MISSING and provide template from the playbook.

### Dispute Resolution — MENA Default

For UAE-seated contracts: DIAC (Dubai International Arbitration Centre) or ADCCAC (Abu Dhabi) is the preferred institutional arbitration. ICC and LCIA are also well-accepted for international contracts. DIFC Courts or ADGM Courts are available for contracts with DIFC/ADGM-incorporated parties.

For KSA-seated contracts: SCCA (Saudi Center for Commercial Arbitration) is the default. International arbitration is enforceable in KSA under the New York Convention (KSA joined in 1994).

## Common Mistakes

- Treating the playbook as inflexible — it is a starting position; some deviations are commercially acceptable when documented with client consent
- Failing to update the playbook after consistently conceding a point — a playbook that doesn't reflect practice undermines the workflow's value
- Not flagging novel clauses (AI liability, cybersecurity audit rights, data residency) that the playbook doesn't cover yet
- Omitting the negotiation strategy note — counsel needs to know not just *what* to change but *how hard to push*

## Related Skills

- [[pa-workflow-transactional-clause-library-check]]
- [[pa-workflow-transactional-contract-redline-20min]]
- [[pa-workflow-transactional-deal-point-analysis]]
- [[pa-workflow-transactional-nda-triage-red-yellow-green]]
- [[tool-rag-firm-knowledge]]
