---
name: side-letter
title: Side Letter
description: Drafts U.S. venture capital and private equity side letter agreements that supplement a primary agreement without formal amendment. Use when drafting a side letter, supplemental letter, investor side letter, MFN carve-out, or special-rights letter tied to an existing agreement.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/side-letter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
---

# Side Letter

Drafts a supplemental agreement that modifies or clarifies a primary agreement while preserving its structure. Commonly used in VC/PE transactions for investor-specific rights, waivers, and MFN carve-outs.

## Quick Start

1. Gather the primary agreement, all amendments, and party details
2. Confirm a side letter is permitted under the amendment/waiver provisions
3. Identify every affected section by article and section number
4. Draft using the template and section map below
5. Run the quality control checklist before finalizing

## Intake Checklist

Copy and track:

```
- [ ] Identify primary agreement by full title, date, and parties
- [ ] Confirm side letter is permitted under amendment/waiver provisions
- [ ] List every affected section with article and section numbers
- [ ] Determine scope limits and carve-outs
- [ ] Confirm which parties must sign
- [ ] Confirm board, investor, or third-party consents required
```

## Section Map

1. Header and date
2. Parties and reference to primary agreement
3. Recitals (purpose and authority)
4. Operative provisions (numbered)
5. Relationship to primary agreement and conflict rule
6. Confidentiality and disclosure
7. Term, termination, and survival
8. Assignment (if different from primary agreement)
9. Governing law and dispute resolution
10. Notices (incorporate by reference or restate)
11. Entire agreement and no oral modification
12. Severability, waiver, counterparts, electronic signature
13. No third-party beneficiaries
14. Signature blocks

## Clause Matrix

| Topic | Required Inputs | Drafting Notes |
|---|---|---|
| Modification/clarification | Section refs; replacement text | State "amends" or "clarifies"; cite sections precisely |
| Additional rights | Right holder; scope; triggers | Define conditions, time limits, remedies |
| Exceptions/waivers | Baseline obligation; exception scope | Limit to specific facts; avoid implied broad waiver |
| Confidentiality | Who can see; permitted disclosures | Align with fund/investor reporting |
| Conditions | Precedent/subsequent triggers | Use objective criteria and deadlines |
| Duration | End date or event | State survival of key clauses |
| Conflict hierarchy | Conflicting terms | Side letter controls only as to stated matters |
| Dispute resolution | Forum; arbitration rules | Mirror primary agreement unless reason to deviate |
| Notices | Addresses; method | Incorporate primary agreement unless changed |

## Drafting Template

```text
SIDE LETTER AGREEMENT

This Side Letter Agreement (this "Side Letter") is entered into as of [Date] by and between [Party A] and [Party B] (each, a "Party" and together, the "Parties").

WHEREAS, the Parties are party to that certain [Primary Agreement Title], dated [Date] (the "Agreement");
WHEREAS, the Parties desire to [modify/clarify/supplement] the Agreement as set forth below.

1. [Modification/Clarification]. Section [X] of the Agreement is hereby [amended/clarified] as follows: [replacement or addendum text].
2. [Additional Right/Exception]. [Right, conditions, timeframes, and limits].
3. [Confidentiality of Side Letter]. [Permitted disclosures; required notices].
4. [Term and Termination]. [Duration; survival].

Relationship to Agreement. Except as expressly set forth herein, the Agreement remains in full force and effect. In the event of a conflict between this Side Letter and the Agreement, this Side Letter controls solely with respect to the matters addressed herein.

[Optional: Assignment; Notices; Entire Agreement; Severability; Waiver; Counterparts; E-signature; No Third-Party Beneficiaries; Governing Law; Dispute Resolution.]

IN WITNESS WHEREOF, the Parties have executed this Side Letter as of the date first written above.
```

## Quality Control

```
- [ ] Cross-references match the primary agreement exactly
- [ ] Defined terms match primary agreement or are newly defined
- [ ] No change exceeds intended scope
- [ ] Consent and approval requirements satisfied
- [ ] Confidentiality aligns with disclosure obligations (auditors, regulators, acquirers)
- [ ] Governing law and dispute resolution consistent or justified
- [ ] Signature blocks reflect proper authority and titles
```

## Common Pitfalls

- **Primary agreement forbids side letters**: Use a formal amendment instead.
- **Scope creep**: Keep modifications narrow and tied to specified sections.
- **Non-signatory rights**: Do not alter rights of non-signatories without explicit consent.
- **Inconsistent terms**: Mirror the primary agreement's defined terms and formatting.
- **Missing confidentiality**: Always state whether the side letter is confidential and who may receive it.
- **VC/PE alignment**: Verify alignment with investor rights, MFN clauses, and fund reporting obligations.
- **Divergent governing law**: If deviating from the primary agreement's governing law or dispute resolution, explain rationale in recitals or a dedicated clause.

---

**Key changes from original:**

- **Removed `tags`** — not part of the Agent Skills spec (only `name` and `description` in frontmatter)
- **Tightened description** — removed verbose clause list ("precise cross-references, conflict hierarchy..."), kept trigger keywords
- **Added Quick Start** — 5-step overview so the agent can orient immediately
- **Converted Prerequisites → Intake Checklist** — actionable copy-and-track format per best practices workflow pattern
- **Renamed "Output Structure / Process"** — split into flat top-level sections (Intake, Section Map, Clause Matrix, Template, QC) instead of nested subsections
- **Converted Guidelines → Common Pitfalls** — bolded failure mode labels for scanability
- **Trimmed prose** — removed "Use this structure and complete each step" and other filler; ~90 lines vs ~110 original
