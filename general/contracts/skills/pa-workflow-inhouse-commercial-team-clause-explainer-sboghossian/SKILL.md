---
name: pa-workflow-inhouse-commercial-team-clause-explainer-sboghossian
title: In-House — Clause Explainer for Commercial Team
description: Use when an in-house lawyer needs to explain contract clauses to the commercial, sales, or business team in plain language — translating the legal meaning, commercial impact, and risk exposure of specific provisions. Triggers when a non-lawyer asks "what does this clause mean?", "can we accept this?", or "what should we push back on?" about a contract clause or contract section.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-inhouse-commercial-team-clause-explainer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# In-House — Clause Explainer for Commercial Team

The biggest bottleneck in most in-house legal teams is not complex legal work — it is the high-volume, repetitive task of explaining what a clause means to a sales or business colleague who needs an answer now. This skill provides the framework for generating plain-language clause explanations that are accurate, decision-useful, and appropriately qualified.

## Purpose

Translate specific contract clauses into four answers the commercial team actually needs:
1. **What does this clause mean?** — plain English summary of the legal effect
2. **What is the commercial impact?** — what the business gains or loses if this clause stands
3. **What should we push back on?** — the negotiating ask, if any
4. **When to escalate to legal?** — the trigger for referring back

## Inputs

| Input | Why it matters |
|---|---|
| The clause text | The specific provision to explain |
| Contract type | NDA / MSA / SaaS / employment / JV — changes the context |
| Our position | Are we the customer or supplier? Impacts which risks matter |
| Jurisdiction | Affects legal effect of the clause |
| Counterparty | Large corporation, startup, government — affects negotiating leverage |
| Deal context | What is the commercial relationship? What is at stake? |

## Output format for commercial team

### Plain-language explanation

Write for someone with no legal training. Max 3–5 sentences. No legal jargon.

**Example clause:** "The Supplier shall indemnify, defend, and hold harmless the Customer from and against any and all third-party claims, damages, losses, and expenses, including reasonable attorneys' fees, arising out of or related to the Supplier's breach of this Agreement or infringement of any intellectual property rights."

**Plain English:**
"If our product or our mistake causes a lawsuit against your company, we cover the cost of defending that lawsuit and pay any damages. This includes legal fees. The trigger is: (1) we broke the contract, or (2) we infringed someone's IP."

### Commercial impact

What does this clause do for the business?

**Risk to us:** If the clause is in a contract where we are the Supplier — this is a broad indemnity. "Any and all third-party claims" is very wide; a narrow indemnity would limit to direct IP infringement, not consequential claims.

**Benefit to us:** If we are the Customer — this gives us full cost coverage; no financial exposure from Supplier's IP issues.

**Key threshold:** Note any cap or carve-out. An uncapped indemnity with no liability limit is material risk.

### Negotiating ask

What should the commercial team request (or resist)?

| Scenario | Ask |
|---|---|
| We are the Supplier with broad indemnity | Narrow to "direct infringement of third-party IP" only; add a mutual cap on indemnity tied to contract value |
| Counterparty has narrower indemnity than ours | Reciprocate — ask for the same scope we are offering |
| No indemnity from the other side | Seek a reciprocal indemnity at minimum |

### Escalate to legal when

- The clause is uncapped and the potential exposure exceeds [company threshold]
- The clause involves regulatory liability (data protection, financial services, AML)
- The clause is in a language other than English without a verified translation
- The other party has sent a heavily redlined version that changes the entire risk allocation
- The deal is above the GC's pre-approved delegation of authority limit

## High-frequency clause explanations

These are the clauses commercial teams most often need explained:

### Limitation of liability

**What it means:** caps the total amount one party can recover from the other, no matter what goes wrong.
**Commercial impact:** protects the company from catastrophic exposure; also limits your recovery if the other side defaults on a large contract.
**Typical ask:** "Limitation of liability should be mutual and capped at 12 months of fees paid."
**Escalate if:** the limitation excludes personal injury, death, IP infringement, or wilful misconduct — those are industry standard carve-outs and their absence or presence matters.

### Auto-renewal / evergreen clauses

**What it means:** the contract renews automatically unless you give notice by a specific date.
**Commercial impact:** if no one manages the notice date, you are locked in for another term.
**Typical ask:** "Set a reminder in the contract management system. Notice period should be 60+ days for any contract over 6 months."
**Escalate if:** the notice period is less than 30 days or the renewal term is longer than the original term.

### IP ownership / work-for-hire

**What it means:** determines who owns the deliverable — if we are contracting an agency/developer, do we own what they build?
**Commercial impact:** without an assignment clause, the agency retains copyright in their work; you get a licence, not ownership.
**Typical ask:** ensure the clause includes "all work product created under this Agreement shall be the sole and exclusive property of [Company] upon full payment."
**Escalate if:** the developer is retaining IP rights or including a licence-back.

### Governing law and dispute resolution

**What it means:** which country's law applies, and where do you go if there's a dispute?
**Commercial impact:** if you're a UAE company and the clause says "Courts of England and Wales" — a dispute requires UK litigation, with UK costs and a UK law firm.
**Typical ask:** match governing law to the jurisdiction where the company operates; use DIAC or DIFC arbitration for MENA commercial contracts.
**Escalate if:** the governing law is an unfamiliar jurisdiction, or arbitration is in a location that is practically or legally difficult for the company.

## MENA-specific considerations

| Clause type | MENA notes |
|---|---|
| Penalty clauses | UAE Civil Code / KSA: liquidated damages are enforceable if proportionate; courts have power to reduce. Different from common-law "penalty clause" doctrine. |
| Agency / exclusivity | UAE: commercial agency law creates statutory protections for registered agents. A distribution clause can inadvertently trigger UAE Commercial Agencies Law. Escalate. |
| Language | In UAE courts, Arabic is the court language; English-only contract requires certified translation. Alert commercial team if the contract should be in Arabic or bilingual. |
| Notarisation | Some UAE transaction types require notarised contracts (Tawtheeq). If this might apply, escalate before signature. |

## Related skills

- [[pa-workflow-inhouse-cross-functional-translation]]
- [[pa-workflow-inhouse-contract-intake-routing]]
- [[output-irac-structure]]
- [[output-mobile-friendly-short]]
