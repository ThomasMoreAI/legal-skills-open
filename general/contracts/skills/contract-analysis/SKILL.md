---
name: contract-analysis
title: Contract Analysis
description: Analyzes contracts to identify key terms, obligations, risks, and negotiation opportunities. Produces structured risk assessments with executive summary, provision review, risk matrix, and prioritized recommendations. Use when reviewing agreements before execution, during negotiation, at closing, or for compliance monitoring.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/contract-analysis
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Contract Analysis

Extracts and evaluates material provisions, risk allocations, and obligations across one or more contracts to support negotiation, execution, or remediation decisions.

## Prerequisites

Before starting, collect:

1. **Contract document(s)** — executed or draft; note which
2. **Client role** — which party the analysis favors (or neutral)
3. **Jurisdiction** — governing law if known; flag if absent
4. **Scope** — full review, specific provisions, or multi-contract comparison

## Workflow

### 1. Executive Summary

- Parties, effective date, term, governing law (1–2 sentences each)
- Top 3–5 critical risks requiring immediate attention
- Overall favorability: favorable / balanced / unfavorable

### 2. Key Provisions Matrix

For each provision, record section number, summary, risk level (High/Med/Low), and notes.

Provisions to evaluate:
- **Term & Termination** — cure periods, notice, convenience rights
- **Payment Terms** — timing, late fees, set-off rights
- **Scope / Deliverables** — ambiguity, change-order mechanics
- **Indemnification** — mutual vs. one-sided, carve-outs
- **Limitation of Liability** — cap amount, excluded damages
- **Warranty / Disclaimer** — express vs. implied, remedy limits
- **Insurance** — required types, minimums
- **IP Ownership** — work-for-hire, license-back, background IP
- **Confidentiality** — term, carve-outs, residuals clause
- **Dispute Resolution** — arb vs. litigation, venue, fee-shifting
- **Auto-Renewal** — notice window, opt-out mechanics
- **Assignment / Change of Control** — consent requirements
- **Force Majeure** — scope, notice, extended FM termination right
- **Governing Law / Venue**

### 3. Risk Matrix

For each issue found, record section, severity, likelihood, and recommended action.

Risk categories:
- **Ambiguity** — language supporting multiple interpretations
- **Asymmetry** — one-sided obligations or liability allocation
- **Gaps** — material matters left unaddressed
- **Conflicts** — internal inconsistencies between sections
- **Unenforceability** — provisions likely void under applicable law

### 4. Comparative Analysis *(multi-contract only)*

Table comparing key terms across agreements; flag deviations from market standard.

### 5. Prioritized Recommendations

Rank issues by priority (Critical → High → Moderate) with provision reference, issue description, and proposed fix for each.

## Checks

- Cite exact section numbers and quote key language verbatim
- Flag auto-renewal clauses with short opt-out windows as high-priority regardless of other factors
- Note all cross-references to external documents, exhibits, or incorporated standards — treat as additional obligations
- For ambiguous provisions, state the full range of plausible interpretations and implications
- Mark `[VERIFY]` on any statutory or case citations — do not assess enforceability under specific state law without verifying current precedent
- UCC Article 2 applies to goods; common law governs services — note if contract mixes both without specifying
- Flag non-compete, non-solicit, and liquidated damages clauses for separate enforceability review under applicable state law
