---
name: deliverable-fidelity-en-matematicsolutions
title: Deliverable Fidelity EN - does the document still say what the analysis found
description: 'Checks whether the final document still carries what the analysis actually found. Takes the list of findings with their severities and the finished deliverable, runs a mechanical coverage check with a bundled zero-dependency script, then an LLM spot-check on the RED findings for tone-downgrading, and returns a deterministic verdict PASS / CONDITIONAL_PASS / FAIL from published weights and thresholds. An omitted RED finding blocks. The third axis of verification, next to citation checking (are the sources real) and adversarial review (does the thesis hold): this one asks whether the summary is faithful to the analysis. Jurisdiction-neutral. Use when: "does the summary cover everything", "did anything drop out of the executive summary", "fidelity check", "is the deliverable faithful", "check the memo against the findings" - before sending any document that summarises a longer analysis.'
author: matematicsolutions
author_url: https://github.com/matematicsolutions/awesome-matematic-skills-en/tree/main/verification-foundation/skills/deliverable-fidelity-en
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Deliverable Fidelity EN - does the document still say what the analysis found

## Why this exists

**The dangerous failure is not a bad citation. It is a real finding that fell out of the
summary.** The analysis flagged a RED clause, the opinion runs to twelve pages, and the
board summary does not mention that clause at all, because the model dropped it while
"summarising". Every citation checks out, the thesis survives attack, and the deliverable
still lies by omission.

Three separate axes of verification:

- `citation-extraction-en` - do the cited sources exist and say what is claimed (truth).
- `adversarial-legal-review-en` - does the thesis survive attack (robustness).
- `deliverable-fidelity-en` - does the deliverable carry the analysis (fidelity).

## When to run it

When a final document **summarises a longer analysis**: an opinion with an executive summary,
a due-diligence memo with a risk table, a report with a conclusions section. Anywhere that
shortening can lose a finding. Not needed for a short letter with no analysis-to-summary layer.

## Input

```json
{
  "findings": [
    { "id": "F1", "severity": "RED", "text": "liability cap conflicts with the mandatory statutory minimum", "resolution": "recommend deleting the cap" },
    { "id": "F2", "severity": "YELLOW", "text": "payment term of 60 days creates a cash-flow risk", "resolution": "" }
  ],
  "deliverable": "<full text of the final document>"
}
```

Severities: `RED`, `YELLOW`, `GREEN` or `INFO`. `resolution` is optional and is checked separately:
a finding can be mentioned while the recommendation attached to it quietly disappears.

## Workflow

1. **Mechanical check (the script, free of judgement)**:

   ```bash
   node scripts/fidelity-check.mjs <task.json>
   ```

   The script extracts the key terms of each finding, normalises them (case, whitespace, quotes,
   dashes) and expands each term into its likely English surface forms (plural, `-ies`/`-y`,
   `-ed`, `-ing`), then checks how many appear in the deliverable. Per finding: represented or
   omitted. **An omitted RED exits 1.** Resolutions are checked too.

   The engine deliberately expands rather than truncates. Cutting characters off a word is how
   the Polish counterpart absorbs inflection, but in English it manufactures false matches -
   "clause" truncated to "clau" would match "claustrophobia". A false match is the dangerous
   direction, because it silently passes an omitted RED finding.

2. **LLM spot-check (judgement)** - for the RED findings the script lists under
   `heaviest_for_llm_spotcheck` (three at most), check not just that the words are present but
   that the **meaning** survived. A RED finding can be mentioned and simultaneously defused -
   "a point to consider" where the analysis said "void provision". No mechanical match catches
   a downgrade of tone. Where there are no RED findings this step does not run; the script does
   not escalate YELLOW.

3. **Verdict** - computed deterministically by the function below, never by general impression.

## Verdict function (deterministic, published weights and thresholds)

Three steps, always in this order:

**Step A - critical conditions. Any one of these means FAIL, with no further arithmetic:**

- an omitted RED finding (script: `omitted_red` non-empty, exit 1),
- a RED finding present but downgraded (LLM spot-check),
- a RED finding's resolution not reflected (script: `red_resolutions_missing` non-empty).

**Step B - weighted coverage score.** Each finding carries a weight by severity:

| Severity | Weight |
|---|---|
| RED | 5 |
| YELLOW | 2 |
| GREEN / INFO | 1 |

`score = sum of weights of represented findings / sum of weights of all findings`.
**A score below 0.85 means FAIL**, even when no RED dropped out. Losing YELLOW findings
wholesale is still omission.

**Step C - conditional threshold.** Three or more omitted YELLOW findings cap the result at
**CONDITIONAL_PASS**: the deliverable may go out only after a human decides, with the list of
omitted findings attached. Otherwise **PASS**.

The weights and thresholds are published on purpose. An auditor can reconstruct the verdict
from the numbers in the report alone, without asking the model to justify itself. That is the
AI Act record-keeping requirement reduced to arithmetic.

## Output for the user

```
## Deliverable fidelity: FAILED

Mechanical: 4/5 findings represented
- OMITTED (RED): F3 "contractual penalty with no upper limit" - BLOCKING, absent from deliverable

LLM spot-check (RED, max 3):
- F1 (RED) - faithfully carried
- F2 (RED) - PRESENT BUT DOWNGRADED: analysis said "void provision", deliverable says "a point to consider"
- F4 (YELLOW) - carried

Verdict function:
- Step A (critical): omitted RED F3 plus downgraded RED F2, so FAIL.
- Step B (for information): represented F1(5)+F2(5)+F4(2)+F5(1) over all F1..F5 (5+5+5+2+1)
  = 13/18 = 0.72, below 0.85.

Verdict: FAIL - do not send. Add F3 to the summary and restore F2 to its actual weight.
```

## What this skill does not do

It does **no legal work and no legal judgement**. It does not decide whether a finding was
correct, only whether it survived into the deliverable: a wrong finding faithfully carried
passes this check, and that is by design - correctness is the job of
`adversarial-legal-review-en` and `citation-extraction-en`. It does not rewrite the document,
does not rank findings, and does not invent severities; it consumes the severities you supply.
A PASS verdict means the analysis reached the page, never that the analysis was right.

## Hard rules

- **An omitted RED is an absolute block.** A red finding missing from the deliverable is silence
  about a material risk. Never pass it.
- **Downgrading counts as omission.** A RED described as "a minor point" is worse than an absence,
  because it puts the reader at ease. The spot-check exists to catch exactly this.
- **The script says what is present, the model says whether it is faithful.** Do not trust word
  matching alone, and do not ask the model to count presence - that is the script's job.

## Data protection

The check runs locally on text you already hold. The script makes no network calls and writes
nothing outside the task file you point it at. Where the deliverable carries privileged or
client-identifying material and an external model is involved in the spot-check, run
`privilege-preflight-en` first.

## AI Act

A published verdict function with explicit weights makes the control reproducible by a third
party from the report alone. Fidelity is the axis that catches a deliverable which is accurate
in every sentence and still misleading in what it leaves out.

## Attribution

English counterpart of MateMatic's `deliverable-fidelity-pl` (Apache-2.0). Rebuilt rather than
translated, because the matching engine is language-dependent: the Polish version truncates
endings to absorb inflection, this one expands terms into surface forms. Rubric, verdict
function and thresholds are shared by design, so the two versions produce comparable verdicts.

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
