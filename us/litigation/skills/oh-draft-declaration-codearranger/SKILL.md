---
name: oh-draft-declaration-codearranger
title: Draft an Ohio Affidavit
description: Use to draft an Ohio affidavit. Triggers include 'Ohio affidavit', 'R.C. 2319.04 affidavit', 'Ohio Civ. R. 56 affidavit', 'verify Ohio affidavit', 'Ohio affidavit format'. Produces a properly-formatted Ohio affidavit conforming to R.C. 2319.04 and Civ. R. 56(C). **Skill name is 'declaration' for filename consistency across the marketplace; the output is an Ohio affidavit, not a federal-style declaration under 28 U.S.C. § 1746.**
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-draft-declaration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft an Ohio Affidavit

> **NOT LEGAL ADVICE.** Ohio civil practice uses
> affidavits, not declarations. The skill name
> "draft-declaration" reflects marketplace filename
> consistency — the output is an Ohio affidavit.

## Form of an Ohio affidavit

Required elements under R.C. 2319.04 and Civ. R. 56(C):

```
IN THE COURT OF COMMON PLEAS OF [COUNTY], OHIO

[Plaintiff Name],
                            Plaintiff,
        vs.                                Case No. [CV-NNNNN]
[Defendant Name],
                            Defendant.

                         AFFIDAVIT OF [AFFIANT NAME]

STATE OF OHIO    )
                  ) ss:
COUNTY OF [...]  )

I, [Affiant Name], being first duly sworn, depose and state:

1. I am over 18 years of age and competent to testify to
   the matters set forth herein, which are based on my
   personal knowledge.

2. [First substantive paragraph.]

3. [Second substantive paragraph.]

...

   FURTHER AFFIANT SAYETH NAUGHT.

                                __________________________
                                [Affiant Name]

Sworn to and subscribed before me this ___ day of
___________, 20__.

                                __________________________
                                Notary Public, State of Ohio
                                My commission expires: ______
```

## Required content

- **Competency clause** — affiant is over 18 and testifies
  from personal knowledge
- **Numbered factual paragraphs** — each containing facts
  within personal knowledge (no legal conclusions, no
  hearsay)
- **Closing**: `FURTHER AFFIANT SAYETH NAUGHT`
- **Notarization** — Ohio affidavits require notary
  acknowledgment under R.C. 2319.04 unless another officer
  authorized to administer oaths is used (R.C. 147.07)

## Civ. R. 56(C) affidavit standards

When supporting a motion for summary judgment:

- Affidavit must be made on personal knowledge
- Must set forth facts that would be admissible in evidence
- Must show that the affiant is competent to testify
- Sworn or certified copies of all papers referred to must
  be attached

A defective Civ. R. 56 affidavit (hearsay, opinion, no
personal knowledge) will be disregarded by the court and
may sink the motion.

## Common drafting errors

- **Hearsay** — affiant cannot testify to what someone else
  said unless an exception applies (Evid. R. 803-804)
- **Legal conclusions** — "The contract was breached" is a
  conclusion; "On March 1, 2025, Plaintiff failed to
  deliver the goods" is a fact
- **Missing notarization** — Ohio courts will strike
  unsworn affidavits from the record
- **Mismatched caption** — affidavit caption must match the
  motion it supports

## Exhibit handling

- Attach exhibits as `Exhibit A`, `Exhibit B`, etc.
- Each exhibit incorporated by reference: "A true and
  accurate copy of [document description] is attached
  hereto as Exhibit A and incorporated herein by reference."
- For business records (Evid. R. 803(6)): the affidavit
  must establish the foundation — custodian of records,
  ordinary course of business, contemporaneous record-
  keeping

## Composition with other oh- skills

- `oh-statewide-format` — caption + paper format
- `oh-draft-motion` — the supported motion
- `oh-pro-se` — pro-se affiant conventions
- `oh-fact-check` — citation verification within the
  affidavit
- `oh-consumer-debt` — debt-buyer affidavit-of-account
  attacks (foundation challenges under Evid. R. 803(6))
