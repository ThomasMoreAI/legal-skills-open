---
name: dispute-resolution-general
title: Dispute Resolution Clause -- General
description: Outlines the agreed mechanism for resolving conflicts, whether through negotiation, mediation, arbitration, or litigation. Reduces uncertainty and cost by defining a clear path before disagreements escalate.
author: scholarly360
author_url: https://github.com/scholarly360/contract-intelligence/tree/main/skills/dispute-resolution-general
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Dispute Resolution Clause -- General

This skill provides expert-level analysis and drafting assistance for
**Dispute Resolution** clauses in **General** contracts.

---

## When to Activate

Activate this skill when the user:

- Uploads or pastes a contract containing a Dispute Resolution clause
- Asks to **draft**, **redline**, or **improve** a Dispute Resolution clause
- Asks for a **risk assessment** of an existing Dispute Resolution provision
- Mentions keywords: *dispute resolution, arbitration, mediation clause*

---

## Workflow

### Step 1 -- Intake

Ask the user (if not already provided):

1. **Which party** are you representing? *(e.g., vendor, client, buyer, seller)*
2. **Jurisdiction** governing the contract? *(e.g., New York, California, England & Wales)*
3. **Is this a draft for review or should I generate fresh language?**

### Step 2 -- Analysis

If reviewing existing language, output the following structure:

```
## Dispute Resolution Clause Analysis

### Plain-Language Summary
[2-3 sentence plain-English description of what the clause does]

### Key Provisions Identified
- [Provision 1]
- [Provision 2]

### Risk Assessment
| Item | Risk Level | Notes |
|------|-----------|-------|
| [item] | High / Medium / Low | [explanation] |

### Recommended Redlines
[Specific suggested changes with rationale]

### Market Standard Comparison
[How this clause compares to typical General market standard]
```

### Step 3 -- Drafting

If generating new language, produce:

1. **Balanced version** (neither party-favored)
2. **Favorable to client** version
3. **Negotiation notes** -- what the other side will likely push back on

---

## Dispute Resolution Playbook -- General

> See `scripts/playbook.md` for detailed clause-specific guidance,
> fallback positions, jurisdiction-specific notes, and precedent language.

---

## Important Notes

- Always caveat that output is not legal advice and should be reviewed by qualified counsel.
- Flag any provisions that may be unenforceable or jurisdiction-specific.
- When jurisdiction is unknown, apply general common-law principles and note assumptions.
