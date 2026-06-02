---
name: tone-modes
title: tone-modes
description: Switch between lawyer mode and casual mode, apply the read-aloud test, and use scripts as scaffolds rather than oracles — triggers whenever Claude is about to draft user-facing language or is about to treat a script's output as final.
author: EvanOchsner
author_url: https://github.com/EvanOchsner/personal-advocacy-toolkit/tree/main/.claude/skills/tone-modes
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# tone-modes

Two registers, one test, one rule about scripts. This skill is a
portable codification of a pattern: keep the internal reasoning
candid, keep the outbound language defensible, and never let a script
pretend to be a lawyer.

## When this skill fires

- About to draft any user-facing artifact: letter, complaint,
  position paper, email, exhibit cover.
- About to paraphrase something the user said into paperwork.
- About to present the output of an intake / triage / packet script
  as the answer rather than as a scaffold.

## The two modes

**Lawyer mode.** The register for anything that leaves the private
workspace. Properties:

- Claims are stated as positions, not as feelings. Every factual
  assertion is traceable to an exhibit or a cited rule.
- Adversarial language ("they're trying to re-underwrite the policy
  after the loss") is rephrased ("the insurer's conduct is
  inconsistent with the agreed-value endorsement at policy
  inception").
- Hedges where warranted — "the record shows," "the file reflects,"
  not "obviously" or "clearly."
- Tight. The read-aloud test (below) is the pressure check.

**Casual mode.** The register for internal reasoning, comments in
drafts, strategy discussions, and the user's own notes. Properties:

- Honest about weak legs of the argument. If the specialist-labor-rate
  premium is the weakest line item, casual mode says so.
- Uses the user's own idiom, not courthouse idiom.
- Free to name what the counterparty is doing in plain language.
- Must not leak into the final artifact. Anything written in casual
  mode needs a translation pass before it goes outside.

## The read-aloud test

Before any lawyer-mode paragraph ships, read it out loud (literally —
subvocalize the words). Two filters:

1. **Would a hostile reader quote this sentence back at you?** If the
   sentence contains a word that reads as snide, speculative, or
   emotionally loaded, it's a gift to opposing counsel. Rephrase.
2. **Does every noun and verb carry its own weight?** Adverbs
   ("grossly," "blatantly") and intensifiers ("clearly," "obviously")
   almost always weaken the sentence they inhabit. Cut them.

If a sentence passes both filters out loud, it's ready.

## Scripts as scaffolds, not oracles

The toolkit's scripts — `situation_classify.py`,
`authorities_lookup.py`, `pii_scrub.py`, `build.py` — are
deterministic rules engines against YAML tables. They are good at
what they do. They do not:

- Know whether the user's framing is correct.
- Know whether an authority's jurisdiction actually covers this
  matter.
- Know whether a PII substitution preserves meaning.
- Know whether a packet is persuasive.

**The rule:** every script output is a starting point the assistant
reviews with the user, not a final answer the user signs. When a
script emits a classification, name it aloud and let the user
confirm. When PII scrub proposes a substitution, show the diff and
let the user confirm. When the packet builder emits a PDF, open it
and read it.

## Synthetic example

Casual-mode note in the Maryland-Mustang file:

> They're pretending the specialist-shop rate is a customary-rate
> problem. It's not. It's them trying to re-underwrite an
> agreed-value policy after the loss.

Lawyer-mode rendering in the MIA complaint:

> The insurer's 2025-05-09 position letter deducts $5,280.50 from
> the agreed value for "non-customary charges." This deduction is
> inconsistent with the agreed-value endorsement (CIM-AV-ENDT-2023)
> in effect at policy inception, which sets the schedule of value
> absent fraud or material misrepresentation — neither of which is
> alleged.

Same fact, two registers. The casual version stays in the internal
notes and is never copy-pasted into paperwork.

## Do not

- Do not try to write in both registers at once. Pick the mode,
  write the thing, then translate if it needs to move to the other
  register.
- Do not let a script's output pass straight into a filing. Every
  output is a draft for the user, not a conclusion.
