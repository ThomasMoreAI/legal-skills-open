---
name: contract-analysis-builderced
title: Contract Analysis
description: Analyze contracts to identify key clauses, risks, obligations, deadlines, and parties. Multi-language support with focus on French and EU commercial law.
author: BuilderCed
author_url: https://github.com/BuilderCed/agent-skills/tree/main/skills/documents/contract-analysis
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: commercial
language: en
---

# Contract Analysis

> **DISCLAIMER**: This skill provides guidance for contract review. It does not constitute legal advice. Always consult a lawyer for contract decisions.

## When to Use

- Reviewing a contract before signing
- Identifying key obligations and deadlines
- Spotting risky or unusual clauses
- Comparing contract terms to market standards
- Extracting structured data from contracts

## Analysis Framework

For each contract, extract and assess:

### 1. Parties
- Full legal names and registration numbers (SIRET for France)
- Roles (client, provider, licensor, licensee)
- Authorized signatories

### 2. Scope & Deliverables
- What is being provided/purchased
- Acceptance criteria
- Exclusions (what is NOT included)

### 3. Financial Terms
- Total amount and payment schedule
- Payment terms (30 days net, 45 days end of month)
- Late payment penalties (FR: BCE rate + 10 points minimum)
- Price revision clauses

### 4. Duration & Termination
- Start date and duration (fixed or indefinite)
- Renewal (automatic? tacit reconduction?)
- Termination conditions (for cause, for convenience)
- Notice period (FR: usually 3 months for B2B services)
- Exit penalties

### 5. Risk Clauses (Flag These)

| Clause | Risk Level | What to Check |
|--------|-----------|---------------|
| Liability limitation | HIGH | Is it mutual? Is the cap reasonable? |
| Indemnification | HIGH | One-sided? Unlimited? |
| Non-compete | HIGH | Duration? Geographic scope? Too broad? |
| Exclusivity | HIGH | Does it prevent working with competitors? |
| IP assignment | HIGH | Are you transferring all IP or just licensing? |
| Auto-renewal | MEDIUM | Notice period to opt out? |
| Force majeure | MEDIUM | Does it include pandemics? Cyber attacks? |
| Governing law | MEDIUM | Which country's law? Which court? |
| Confidentiality | LOW | Duration after termination? Scope? |
| Data processing | MEDIUM | GDPR compliant? DPA included? |

### 6. Deadlines & Obligations Matrix

Extract into structured format:
```
| Who | Must Do What | By When | Consequence if Late |
|-----|-------------|---------|-------------------|
| Provider | Deliver v1.0 | 2026-06-01 | 5% penalty/week |
| Client | Provide specs | 2026-05-01 | Delivery date extends |
```

## French-Specific Contract Rules

| Rule | Requirement |
|------|------------|
| Language | Contract must be in French if performed in France (Loi Toubon) |
| Late payment | Minimum penalty = BCE rate + 10 points (Code de commerce L441-10) |
| Recovery fee | 40 EUR fixed indemnity for late payment |
| Auto-renewal | Must inform before renewal deadline (Loi Chatel for B2C) |
| Non-compete | Must be limited in time, geography, and activity |
| Imbalance | Significant imbalance in B2B contracts voidable (Art. L442-1) |

## Output Format

```
CONTRACT ANALYSIS
Document: {name}
Parties: {A} ↔ {B}
Type: {service agreement / license / NDA / employment}
Duration: {X months/years, renewable}
Total value: {amount}

KEY RISKS:
[HIGH] Unlimited indemnification for Provider (clause 8.2)
[HIGH] IP assignment includes background IP (clause 12.1)
[MED]  Auto-renewal with 30-day opt-out window (clause 3.4)

DEADLINES:
- 2026-05-01: Client provides specs
- 2026-06-01: Provider delivers v1.0
- 2026-06-15: Acceptance period ends

RECOMMENDATION: Review clauses 8.2 and 12.1 with legal counsel before signing.
```

## What This Skill Does NOT Do

- Does not provide legal advice
- Does not sign or execute contracts
- Does not replace lawyer review (especially for high-value contracts)
- Does not handle employment contracts (different legal framework)
- Does not translate contracts (use professional translators)
