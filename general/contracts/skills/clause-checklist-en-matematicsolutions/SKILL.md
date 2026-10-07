---
name: clause-checklist-en-matematicsolutions
title: Clause checklist - what a contract is missing, and what bites
description: 'A clause checklist for a single contract - walks the contract against 41 clause categories (the CUAD taxonomy), assesses which of them this deal needs, and marks each applicable one present / absent / risky, so the clause that should be there but is missing does not slip through. Extractive (quotes the contract, does not paraphrase). Common-law native, jurisdiction-neutral framing. Different from a bulk audit - this goes deep on one contract and asks "what is missing and what bites here". Pairs with adversarial-legal-review-en and reviewer-en. Use when: "check the clauses in this contract", "what is missing from this agreement", "clause spotting", "contract checklist", "review a single contract", "which clauses are risky" - before signing, in negotiation, or in DD of one contract.'
author: matematicsolutions
author_url: https://github.com/matematicsolutions/awesome-matematic-skills-en/tree/main/verification-foundation/skills/clause-checklist-en
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Clause checklist - what a contract is missing, and what bites

## Philosophy

**The most expensive clauses are the ones that are not in the contract.** Reviewing a contract is not
only reading what is written - it is checking that no safeguard this deal needs is absent. This skill
walks the contract against a fixed list of 41 clause categories and, for each, says: present / absent
/ present-but-risky, quoting the clause when present.

It is **extractive** - what it shows comes from the contract, not from paraphrase. It flags presence
and risk; the assessment and the call stay with the lawyer.

One caution built into the method: **CUAD is an extraction taxonomy, not a list of safeguards every
agreement must contain.** Several categories are deal-specific, and some are mutually exclusive pairs
(uncapped vs cap on liability; unlimited vs limited licence grants). Treating every absence as a red
flag buries the real gaps in false positives.

## The 41 categories (CUAD taxonomy)

Groups follow CUAD (1-6) plus ungrouped categories. Two steps per category: first **applicability** -
does this deal need the clause, given the contract type, the parties and the subject matter; then, for
applicable categories only: present / absent / risky + a quote when present. Mutually exclusive pairs
count as one decision - record which side the contract takes, not the "absence" of the other side.

### Contract metadata
- **Document name**, **Parties** (verify authority to sign), **Governing law**.

### Group 1 - term and dates
- Agreement date · Effective date · Expiration date · Renewal term (auto-renew?) · Notice period to terminate renewal.

### Group 2 - competition restrictions
- Non-compete · Exclusivity · No-solicit of customers · Competitive restriction exception (carve-outs).

### Group 3 - control and assignment
- Change of control (consent/termination on M&A?) · Anti-assignment.

### Group 4 - licences
- License grant · Non-transferable license · Affiliate license (licensor) · Affiliate license (licensee) · Unlimited/all-you-can-eat license · Irrevocable or perpetual license.

### Group 5 - post-term and audit
- Post-termination services · Audit rights.

### Group 6 - liability
- Uncapped liability · Cap on liability.

### Ungrouped
- Most favored nation · No-solicit of employees · Non-disparagement · Termination for convenience · ROFR/ROFO/ROFN · Revenue/profit sharing · Price restrictions · Minimum commitment · Volume restriction · IP ownership assignment · Joint IP ownership · Source code escrow · Covenant not to sue · Liquidated damages · Warranty duration · Insurance · Third-party beneficiary.

## Output format

```
RED FLAGS (top):
- ABSENT: <category, applicable to this deal> - <why this deal needs it>
- RISKY: <category> - <how it is one-sided>
(a category marked not applicable never becomes a red flag)

41-CATEGORY TABLE:
| Category | Applicable | Status | Note | Quote (if present) |
| Governing law | yes | present | New York; courts of NY | "..." |
| Cap on liability | yes | absent | no liability ceiling | - |
| Source code escrow | no - no software licensed | n/a | - | - |
...
```

## Limits

- A presence-and-risk checklist, not an interpretation of clause wording. Whether a clause is
  effective, and the recommendation, are the lawyer's.
- The taxonomy is common-law-oriented at source (CUAD); for a specific jurisdiction add local-law
  anchors (for Poland, see klauzule-kontraktowe-pl).
- Descriptive references without a clause ("the parties intend to cooperate") have nothing to match -
  mark as "no clause, manual check".

## Attribution

The 41-category clause taxonomy is based on **CUAD (Contract Understanding Atticus Dataset)**, The
Atticus Project, **CC BY 4.0** (https://www.atticusprojectai.org/cuad). Category descriptions and the
risk framing are MateMatic's own. MateMatic interpretation, not the position of any bar or regulator.

<!-- shared-rules:begin (generated from ../../SHARED-RULES.md by scripts/shared-rules-sync.py - do not edit here) -->
## Shared rules of the verification-foundation plugin

These rules apply to every skill in this plugin, including where the skill itself is silent. They are copied into each skill, so they hold whether you install the whole plugin or a single skill.

### Five layers of protection (before any disclaimer)

1. **Source verification** - provisions and case law from databases, not the model's memory.
2. **Confidence class** - every legal claim marked: verified / check / do not use.
3. **Premise check** - facts from the user are tested before analysis.
4. **Explicit negative scope** - each skill states what it does NOT do.
5. **Human gate** - a qualified person reviews and approves the output.

If an error would pass without being stopped by layers 1-5, the fault is in the skill. Fix the tool, do not add a note. "This is not legal advice" stops no error and transfers no responsibility.

### Confidence tags

- **Verified** - source checked in this session, with a full identifier: `(GDPR Art. 6)`, `(Case C-311/18, CJEU)`.
- **Check** - plausible, unverified: `[check on EUR-Lex]`.
- **Do not use** - an invented case number or provision. Omit it, never fabricate.

The tag sits next to the line it concerns. A case number that exists is not enough - check the content.

### Human gate

Nothing is sent, filed, signed or published before a qualified person checks and approves it. A skill output is a draft, not a finished document.

### Scope

The verification foundation is jurisdiction-neutral - the method, not the substance of any one legal system. It connects to no external source (no MCP connectors) and makes no outbound calls of its own; what you type still goes to your configured model (see https://github.com/matematicsolutions/awesome-matematic-skills-en/blob/main/TRUST.md). Substance comes from separate plugins (eu-law-sources). Deep national law (e.g. Polish case law) lives in the Polish marketplace, by design.
<!-- shared-rules:end -->
