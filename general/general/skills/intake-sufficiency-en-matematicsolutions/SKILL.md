---
name: intake-sufficiency-en-matematicsolutions
title: Intake Sufficiency EN - is the instruction enough to start on
description: 'Scores whether an instruction or brief is complete enough to start work on. Before any legal analysis begins, checks that the purpose, scope, parties, facts, constraints and success criteria are actually present; lists the gaps and ambiguities; turns each gap into a question ready to send to the client; and drafts the skeleton of a matter card. Separates the client''s legal assertions from facts and marks them for verification. The mirror of legal-request-router-en: the router decides what control the OUTPUT needs, this decides whether the INPUT is enough to begin. Jurisdiction-neutral. Use when: "do I have enough to start", "score this brief", "what is missing from this instruction", "what should I ask the client", "is this instruction complete", "gaps in the brief", "intake" - at the start of a matter, after first contact, after an intake call.'
author: matematicsolutions
author_url: https://github.com/matematicsolutions/awesome-matematic-skills-en/tree/main/verification-foundation/skills/intake-sufficiency-en
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Intake Sufficiency EN - is the instruction enough to start on

## Why this exists

**Half of all weak legal opinions are not analytical failures. They are thin inputs.** The
client writes "review this contract", and it turns out nobody knows against which risk, who
the counterparty is, or what the client wants out of it. This skill names what is missing
**before** the work starts, and turns the gaps into questions for the client instead of
assumptions buried in a deliverable.

The skill **does no legal work**. It scores completeness and drafts questions.

## The mirror of the router

- `legal-request-router-en` looks at the task and decides what control the **output** needs.
- `intake-sufficiency-en` looks at the instruction and decides whether the **input** is
  enough to begin at all.

The natural order is intake first, then the work, then the router.

## Sufficiency rubric (six dimensions, 0-100)

| Dimension | Control question | Weight |
|---|---|---|
| Purpose | Is it clear what the client came for: opinion, audit, filing, negotiation? | 20 |
| Scope | Is the scope defined, including what falls outside it? | 20 |
| Parties | Are the parties identified: legal name, company or VAT number, role? | 15 |
| Facts | Are there documents or a factual account to build the analysis on? | 20 |
| Constraints | Are the hard limits known: deadline, budget, confidentiality, jurisdiction? | 15 |
| Success criteria | Is it known what a good outcome means for the client? | 10 |

Verdict: **strong** at 80 or above, **adequate** at 50 or above, **insufficient** below 50.

## Workflow

1. **Check privilege** with `privilege-preflight-en` if the instruction carries client-identifying
   or privileged material and an external model is involved.
2. **Score** the instruction across the six dimensions. Each score cites the facts behind it
   rather than a general impression.
3. **List gaps and ambiguities** - what is concretely absent or unclear.
4. **Separate the client's legal premises.** Every *legal* assertion in the instruction ("the
   deadline has passed", "the contract is void for want of form", "section X forbids this", "we
   have 14 days to reply") is a **premise to verify, not a fact**. A client can be wrong about
   the law, and an analysis built on a false premise is wrong in full even when the reasoning
   is sound. For each premise:
   - list it separately under the plugin's confidence tags (`CLAUDE.md`): a premise starts as
     **check** and becomes **verified** only once the source has been read in this session;
     a premise contradicted at source is **do not use**,
   - if it is MATERIAL to the outcome, verify it before starting, using the primary source
     (the contract text, the statute, `eu-sparql-search`, `authority-triage-en`), or make it
     the first item in the preliminary instructions,
   - if verification DISPROVES it, say so plainly and do not continue on the false assumption,
     however firmly the client stated it.
5. **Generate follow-up questions** - one per gap, each tied to a dimension and marked required
   or optional. A question must be ready to send to the client, not a note to self.
6. **Draft the matter card** - purpose, scope, parties, risks, success criteria, preliminary
   instructions. Fields that cannot be filled from the input stay explicitly "(to be confirmed -
   see questions)".

## Output schema

```json
{
  "sufficiency": {
    "score": 45,
    "verdict": "insufficient",
    "gaps": ["no defined purpose", "counterparty not identified"],
    "ambiguities": ["'urgent' with no actual date"]
  },
  "legal_premises": [
    { "id": "p1", "assertion": "the reply period is 14 days", "material": true, "confidence": "check", "verify_against": "contract text / procedural rules" }
  ],
  "follow_up_questions": [
    { "id": "q_purpose", "text": "Are you looking for an opinion, a filing, or negotiation support?", "dimension": "purpose", "required": true }
  ],
  "matter_card": {
    "purpose": "(to be confirmed - see questions)",
    "scope": "...",
    "parties": "...",
    "risks": [],
    "success_criteria": [],
    "preliminary_instructions": "..."
  }
}
```

## Output for the user

```
## Instruction sufficiency: 45/100 (insufficient)

### Gaps
- no defined purpose for the matter
- counterparty not identified (no legal name or company number)

### Questions for the client (ask BEFORE starting)
- [required] (purpose) Do you want an opinion, a filing, or support in negotiation?
- [required] (parties) Which company is the counterparty - full legal name and company number?
- [optional] (constraints) Is there a hard deadline?

### Matter card (skeleton)
- Purpose: (to be confirmed - see questions)
- Scope: review of the supply agreement
- Parties: (to be confirmed)
- Preliminary instructions: obtain the full set of schedules to the agreement

Recommendation: do not start substantive analysis before the required questions are answered.
```

## Hard rules

- **Insufficient means stop, not guess.** On an insufficient verdict, do not fill the gaps with
  assumptions inside a deliverable. Questions to the client come first. A guess written down as
  a fact is the seed of a wrong opinion.
- **One question per gap, none on spec.** Do not ask about things the input already contains.
- **One input, one score.** This scores completeness, not the merits of the matter.
- **A client's legal premise is a hypothesis, not a fact.** Client assertions about the law -
  deadlines, prohibitions, invalidity, what a provision says - do not pass into the matter card
  as findings. They go to `legal_premises` tagged **check**. Substantive analysis does
  not start on a material premise nobody has checked at source.

## Data protection

The assessment runs on the text of the instruction. Where that text carries privileged or
client-identifying material and an external model is involved, run `privilege-preflight-en`
first. Note its limit: it returns a verdict and can prepare a redacted draft, but it does not
perform the final redaction and this hub ships no pseudonymisation engine. Redaction is a human
step or your own tool.

## AI Act

Naming gaps and ambiguities at the input keeps the decision with a person: they choose
knowingly whether to begin on an incomplete instruction, instead of receiving a deliverable
that merely looks complete.

Scope note: Article 14 of Regulation (EU) 2024/1689 requires human oversight of **high-risk**
AI systems. Whether your deployment is in that class is a separate question, which this skill
neither answers nor presumes - see `eu-ai-act-triage-en`.

## Attribution

Sufficiency pattern (score, gaps, follow-up questions, matter card) inspired by
[AnttiHero/lavern](https://github.com/AnttiHero/lavern) (Apache-2.0, briefing-schema); premise
verification adapted from [akunikkola/claude-for-legal-finland](https://github.com/akunikkola/claude-for-legal-finland)
(MIT). Rubric, schema and rules written from scratch. English counterpart of
`intake-sufficiency-pl`, rebuilt rather than translated: party identifiers, source-verification
routes and the privilege step follow what this repository ships, not the Polish originals.
