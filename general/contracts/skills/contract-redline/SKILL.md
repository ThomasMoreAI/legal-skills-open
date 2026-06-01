---
name: contract-redline
title: Contract Redline Against Your Playbook
description: Use this skill to produce a first-pass redline on an inbound contract (MSA, NDA, SOW, vendor agreement, partnership agreement, employment contract) against a configured negotiation playbook. Triggers when the user shares a contract draft, says "redline this contract", "review this MSA", "first pass on this NDA", or similar. Saves the user 30-70% of what a lawyer would charge for the first pass.
author: Kotrotsos
author_url: https://github.com/Kotrotsos/claude-skills-non-coding/tree/main/contract-redline
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Contract Redline Against Your Playbook

## When to use this skill

A counterparty sends a contract draft. The user knows their lawyer will charge $500-2,000 to do the first redline. Most of the changes are routine clauses they have negotiated many times before. This skill does the first pass against a configured playbook, leaving the lawyer to do the final review on the meaningful edge cases.

## Input the user provides

- The inbound contract draft
- The contract type (MSA, NDA, SOW, vendor agreement, partnership, employment, etc.)
- Optionally: the user's playbook (if not already configured, the skill will use sensible defaults and flag them)
- Optionally: deal context (size, strategic importance, relationship history with counterparty)

## What this skill does

1. Reads the contract in full
2. Identifies each clause against the user's playbook on the key terms
3. Redlines clauses that fall outside the acceptable range
4. Adds rationale notes for each proposed change
5. Prioritizes changes by deal impact (must-have, should-have, nice-to-have)
6. Flags clauses that need lawyer review rather than automated handling
7. Produces a redlined document plus a one-page summary

## Default playbook clauses (override per user)

These are the eight clauses most contracts hinge on. The user should override these defaults with their own playbook.

1. **Liability cap**: default to 1x annual fees, push to 2x, hard floor at 12 months fees
2. **IP ownership**: default to user retains pre-existing IP, joint ownership of co-developed, customer owns work product
3. **Payment terms**: default Net 30, push back on Net 60+, never accept Net 90+
4. **Termination rights**: mutual termination for convenience with 30-60 day notice, immediate for cause
5. **Indemnity**: mutual indemnity for IP and confidentiality, with carve-outs
6. **Audit rights**: limited to annual, with 30 day notice, at requestor's expense
7. **Data handling**: GDPR/CCPA compliance affirmed, data residency named, breach notification within 72 hours
8. **Exclusivity**: avoid; if required, narrow to specific use case and time-limited

## Output structure

```
# Redline Summary: [Contract type] with [Counterparty]
*Pages reviewed: [n]. Material edits: [n]. Lawyer review needed on: [count] sections.*

## Must-have changes (deal-breakers if not accepted)
1. **Section [n] - [Clause name]**:
   - Current: [quote or close paraphrase]
   - Proposed: [revised text]
   - Why: [one sentence on the risk being mitigated]

2. [...continue]

## Should-have changes (push hard for, but not deal-breakers)
[Same structure]

## Nice-to-have changes (worth raising, accept if pushed back on)
[Same structure]

## Flagged for lawyer review
- Section [n]: [reason this needs a real lawyer]
- Section [n]: [reason]

## Clauses we accept as-is
[List with brief note on why these are within acceptable range]

## Negotiation strategy
2-3 sentences on which battles to fight in which order. Which changes can be conceded if the counterparty pushes back. Which are non-negotiable.
```

## Calibration notes

- This skill produces a first pass. It does not replace a lawyer. The output is the document the user takes to their lawyer to review, not the document they send to the counterparty unedited.
- For each proposed change, include the underlying risk. "Push to 2x liability cap" is incomplete. "Push to 2x liability cap because the deal size means 1x could leave us under-protected on a single major incident" is useful.
- Distinguish between "outside our playbook but acceptable" and "outside our playbook and unacceptable." Not every deviation needs to be a fight.
- Flag clauses that have changed materially from prior versions of this contract type, if the user has shared past examples.
- For unusual or high-stakes provisions (IP assignment, non-compete, control rights in M&A), recommend lawyer review explicitly rather than redlining yourself.

## What this skill does NOT do

- Does not provide legal advice
- Does not interpret jurisdiction-specific case law
- Does not handle deals over a user-defined threshold without flagging lawyer review
- Does not replace counsel for any contract with material litigation, regulatory, or tax exposure

## When NOT to use this skill

- M&A documents (different complexity tier, always lawyer-first)
- Litigation settlement agreements
- Anything where the counterparty has explicitly stated they will not negotiate the standard form
- Contracts in jurisdictions the user has not configured (flag and stop)
