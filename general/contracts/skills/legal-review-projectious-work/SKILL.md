---
name: legal-review-projectious-work
title: Legal Review
description: Structures a systematic legal and compliance review of contracts, policies, or technical decisions — identifying key clauses, risks, and questions for counsel. Use when asked to review a contract, check compliance implications, flag legal risks in a technical design, or prepare for a legal consultation. Always surfaces work for qualified counsel; never replaces legal advice.
author: projectious-work
author_url: https://github.com/projectious-work/processkit/tree/main/src/context/skills/product/legal-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Legal Review

## Intro

Legal review in a processkit context is a **pre-consultation
structure** skill: it organizes what has been read, flags what
needs expert attention, and prepares the questions to bring to
counsel. It does not provide legal advice or interpret law. The
output of this skill is a structured review document that makes
a lawyer's time more efficient, not a substitute for their judgment.

## Overview

### Scope and limits

**This skill does:**
- Identify clauses and provisions that commonly create risk
- Summarize key terms for non-lawyers
- Flag questions that require legal advice
- Organize a review document for a legal consultation
- Identify missing standard provisions

**This skill does NOT do:**
- Provide legal advice
- Interpret law or jurisdiction-specific regulations
- Make compliance determinations
- Replace review by qualified counsel for contracts above a materiality threshold

For any contract being signed, for compliance questions affecting
users' data, or for any matter with significant financial or legal
exposure — qualified legal counsel must review. This skill reduces
the time that review takes; it does not replace it.

### Contract review checklist

When reviewing a contract, work through these sections:

**Parties and authority**
- [ ] Are both parties correctly named (legal entity, not trade name)?
- [ ] Is the signatory authorized to bind the entity?

**Scope and services**
- [ ] Is the scope of work clearly defined?
- [ ] Is it possible to interpret the scope more broadly or narrowly than intended?
- [ ] Are deliverables and acceptance criteria specific?

**Term and termination**
- [ ] What is the initial term?
- [ ] What are the auto-renewal provisions?
- [ ] What termination rights exist (for cause, for convenience)?
- [ ] What is the notice period for termination?
- [ ] What survives termination (licenses, obligations, confidentiality)?

**Payment**
- [ ] Are fees, payment schedule, and late payment terms clear?
- [ ] Are fee increases governed or uncapped?
- [ ] What happens to paid fees if terminated early?

**Intellectual property**
- [ ] Who owns work product created under the contract?
- [ ] Are pre-existing IP and background IP excluded from assignment?
- [ ] Does the other party get a license to our IP? Is it revocable?
- [ ] Are there restrictions on how we can use deliverables?

**Confidentiality**
- [ ] What is the definition of confidential information?
- [ ] What obligations apply to each party?
- [ ] What exceptions exist (public domain, prior knowledge, required disclosure)?
- [ ] What is the confidentiality term?

**Data and privacy**
- [ ] Who is controller vs. processor of personal data?
- [ ] What data processing terms are included (DPA, SCCs, BAA if healthcare)?
- [ ] Where can data be stored / transferred?
- [ ] What security obligations apply?
- [ ] What breach notification obligations exist?

**Liability**
- [ ] Is liability limited? To what cap (e.g., fees paid in prior 12 months)?
- [ ] What is excluded from the cap (IP indemnity, fraud, death/injury)?
- [ ] Are consequential, indirect, and incidental damages excluded?

**Representations and warranties**
- [ ] What does each party represent?
- [ ] What disclaimers apply?
- [ ] What happens if a representation is false?

**Indemnification**
- [ ] Who indemnifies whom for what?
- [ ] Is the scope of indemnification reasonable and bounded?

**Dispute resolution**
- [ ] Governing law and jurisdiction?
- [ ] Mandatory arbitration? Class action waiver?
- [ ] Is the jurisdiction reasonable for your business?

**Other**
- [ ] Assignment restrictions — can the contract be assigned without consent?
- [ ] Entire agreement / merger clause — are prior agreements superseded?
- [ ] Amendment procedure — how can the contract be changed?
- [ ] Force majeure — what events excuse performance?

### Review document format

```markdown
# Contract Review — [Counterparty] [Contract Type] — [Date]

**Reviewer:** [Name]  
**Qualified counsel review needed:** Yes / No / For these sections only: [list]

## Summary

**What this contract does:** [2-3 sentences]

**My overall read:** [Balanced for us / Leans vendor-favorable / Needs significant negotiation]

## Red flags (counsel review required)

- **[Section or clause]:** [Specific risk] — [Why it matters]
- **[Section or clause]:** [Specific risk] — [Why it matters]

## Key terms

| Term | What the contract says | Industry standard | Our position |
|---|---|---|---|
| Term | [X months] | [12 months] | [Acceptable / Negotiate to Y] |
| Liability cap | [1× fees] | [Varies] | [Acceptable] |
| IP ownership | [Vendor retains all] | [Client owns work product] | **Flag for negotiation** |

## Missing provisions

- [Standard clause that is absent and should be requested]

## Questions for counsel

1. [Specific question about an unclear clause]
2. [Jurisdiction-specific question]
3. [Is our interpretation of [clause] correct?]

## Recommended negotiation points

| Priority | Clause | Current text | Requested change |
|---|---|---|---|
| High | [Section] | [What it says] | [What we want] |
| Medium | [Section] | [What it says] | [What we want] |

## Non-negotiable items (our baseline)

- [Clause we will not agree to without]
- [Clause we will not accept at all]
```

### Technical compliance review

For technical decisions with compliance implications (GDPR, HIPAA,
SOC 2, PCI DSS, etc.):

1. **Identify the applicable frameworks** — what regulations apply to
   this data or system?
2. **Map the technical design to controls** — which controls does the
   design satisfy, which does it not?
3. **Flag gaps** — what controls are missing or not yet implemented?
4. **Prioritize** — which gaps are blockers vs. accepted risk?
5. **Recommend** — what changes to the design or compensating controls
   close the gaps?

This surfaces the questions and gaps; a compliance expert or
counsel reviews the analysis.

## Gotchas

Agent-specific failure modes — provider-neutral pause-and-self-check items:

- **Treating a legal review summary as legal advice.** This skill organizes and flags; it does not interpret law or provide compliance determinations. Always state clearly that flagged items require qualified counsel and that the review document is a preparation tool, not a legal opinion.
- **Reviewing only the standard sections without reading the definitions.** Defined terms in a contract control everything. A "confidential information" definition that excludes "information disclosed orally" completely changes the confidentiality provisions. Read the definitions section before anything else.
- **Missing survival clauses.** Provisions that survive termination (confidentiality, IP ownership, payment obligations, indemnification) are among the most important in a contract. A termination clause that looks clean may hide obligations that last years. Always identify what survives.
- **Treating favorable terms as non-issues.** A term that appears favorable may create unexpected obligations or exclude something important. A very broad IP assignment from the vendor that assigns "all improvements and derivatives" may capture pre-existing IP if the definition is broad enough. Don't skip positive-looking clauses.
- **Not flagging missing standard provisions.** Contracts sometimes simply omit things — a limitation of liability, a data processing addendum, a notice clause. An absence is as important as a problematic presence. The checklist exists to surface both.
- **Reviewing a contract without understanding the business context.** A 1-year auto-renewing contract is fine for a commodity service and problematic for a strategic dependency. The same limitation of liability is appropriate for a small vendor and unacceptable for a mission-critical one. Context determines risk.
- **Summarizing without flagging questions for counsel.** The most useful output of a pre-consultation review is a specific list of questions. "Does our interpretation of the IP assignment in Section 8.2 mean we cannot use this code in our own products?" is far more useful than "Section 8.2 may be an issue."

## Full reference

### Common non-standard clauses to flag

- **Broad IP assignments** that include pre-existing IP or derivatives
- **Unlimited liability** carve-outs for IP infringement that dwarf the contract value
- **Unilateral modification rights** (vendor can change terms with 30 days notice)
- **Audit rights** that require access to your entire technical infrastructure
- **Non-solicitation** clauses that go beyond their typical 12-month / role-specific scope
- **Exclusivity** provisions that are not explicitly limited to scope and duration
- **MFN (most favored nation)** clauses with broad scope

### Data processing quick-check

For contracts involving personal data of EU residents:
- [ ] GDPR compliant? Is there a signed DPA?
- [ ] Standard Contractual Clauses (SCCs) if transferring outside EEA?
- [ ] Data retention and deletion obligations specified?
- [ ] Breach notification obligations (72-hour GDPR requirement)?
- [ ] Sub-processor list and approval rights?

For US healthcare data (HIPAA):
- [ ] Signed Business Associate Agreement (BAA)?
- [ ] BAA covers all PHI processing under the contract?
- [ ] Breach notification: 60-day requirement covered?

### When to stop and escalate to counsel

Stop the review and escalate immediately if:
- The contract involves personal data of many users and the data terms are unclear
- The liability exposure exceeds a material threshold for the business
- You see a clause you genuinely cannot interpret
- The contract is for a regulated service (financial, healthcare, legal)
- The other party is pressing for signature before review is complete
