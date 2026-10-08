# Frame Hardening & Checkpoint 1

Checkpoint 1 is the load-bearing human moment: approve a bad frame and everything downstream is well-executed error. Two failure modes need different fixes — **wrong frame (commission)** and **missing subgoal (omission)**. Omission is the more dangerous: absence doesn't look like anything. These passes attack the frame before the user sees it and make omissions visible rather than silent.

On **contested pieces** (the proportionality test in SKILL.md) the two passes are dispatched as Opus Task subagents **in one turn, in parallel with the orchestrator's own framing work**; on trivial pieces they may be skipped (`frame: unhardened (trivial)` in the ledger).

## Matter context (read before framing)

If `matter-context.md` exists in the working directory, the Lead Strategist reads it **before** Step 1. The user's brief then supplies only the *delta* (the specific piece and its terms); the frame inherits the rest. Schema:

```markdown
# Matter context — <matter name / proceedings number>
_Privileged work product — same confidentiality rule as the ledger. Updated: <ISO>_
## Parties & relationships
## Procedural history (dated, one line each)
## Adverse findings / known weaknesses on the record
## Live issues & positions taken (don't contradict a position already taken)
## Authorities relied on to date (link prior authorities packs)
## Standing constraints (must/can't concede; register rules; who signs)
## FRAME-MISS log (imported from prior audits — what earlier frames missed)
```

After each run, the orchestrator offers to write new findings (adverse findings surfaced, positions taken, FRAME-MISSes) back into this file — the compounding loop.

## Frame Challenger — role prompt (paste verbatim)

> You are the **Frame Challenger**. You attack the FRAME of a persuasive piece before any drafting exists — not the prose, the frame. **FIRST** read `references/porter-method.md` (Rules 1, 2, 5). You are given the draft frame (reader, desired conclusion, controlling proposition, resistances, constraints, subgoal table) and the brief. Answer adversarially:
> 1. **Wrong reader?** Is this the real decision-maker? Who actually acts on this piece, and do their priors differ from those stated?
> 2. **Over-reached conclusion?** Would any reader in this position grant this conclusion on any facts? What conclusion is a piece to this reader actually *capable* of earning? If lower than the stated one, say so and state the highest earnable conclusion.
> 3. **Wrong controlling proposition?** Does the stated proposition, if established, actually compel the conclusion for this reader — or is there a hidden premise the frame assumes?
> 4. **Opposing counsel's read.** State, in one paragraph, what the reader's adviser will say this piece is really doing.
> Your objections are presented to the user UNRESOLVED at checkpoint 1 — do not soften them, do not pre-answer them. Write to `agent-reports/<piece_slug>/cycle<N>-frame-challenge.md`. Then stop.

## Issue Spotter — role prompt (paste verbatim)

> You are the **Issue Spotter**. Read the supplied materials in full — not just the brief — and return candidate issues the brief did not raise. **FIRST** read `references/porter-method.md` (Rule 2). Work this checklist against the materials, then add anything material outside it:
> - limitation periods and time bars; offer/acceptance formalities and validity (incl. Calderbank/Offer-of-Compromise requirements)
> - costs consequences and costs orders already made; security for costs
> - privilege and without-prejudice status of anything quoted or relied on; the implied (Harman) undertaking
> - adverse findings, admissions, or positions already taken on the record that the piece could contradict
> - regulatory overlay (professional-conduct, TGA/AHPRA, disclosure obligations)
> - the counterparty's likely parallel moves (their own offer, strike-out, security application)
> - factual assertions in the brief that the materials do not support, or contradict
> For each: one line, why it matters to THIS piece, proposed subgoal (`F#`/`O#`), proposed weight, `legal` tag if applicable. Do not research the law (Stage 0's job) and do not draft. Write to `agent-reports/<piece_slug>/cycle<N>-issue-spotting.md`. Then stop.

The orchestrator **diffs** the Issue Spotter's list against the tagged subgoals; the delta goes to checkpoint 1 as proposals ("materials disclose X; brief didn't raise it; proposed as O2 [LB] — confirm or strike"), never silently adopted or silently dropped.

## Checkpoint-1 template (presented to the user before any Stage-0/Stage-2 dispatch)

```markdown
# Checkpoint 1 — confirm the frame — <piece_slug>
## Framed goal
Reader: <…> · Desired conclusion: <one sentence> · Controlling proposition: <…> · Register/constraints: <…>
## Subgoal table
| ID | Subgoal | Weight | legal? | Source (brief / matter-context / Issue Spotter) |
## Frame Challenger — unresolved objections
- <verbatim; incl. "highest earnable conclusion" if lower than stated>
## Issue Spotter delta — confirm or strike
- <materials disclose X; brief didn't raise it; proposed as <ID> [<weight>]>
## Assumptions (each with consequence-if-wrong)
- <assumption> — if wrong: <which subgoals/beats change>
## Negative space — this run will NOT
- Research: <legal questions not tagged and so not going to Stage 0>
- Address: <issues considered and excluded, with one-line reason>
_If any of these matter, say so now. Stage 0 will run on: <list of legal LB IDs>._
```

The confirmed frame is recorded in the ledger with a **version number**; any later correction increments it, re-triggers **only the affected subgoal chain** (new/changed IDs → targeted dispatches → affected beats redrafted), and is logged.

## FRAME-MISS logging

Anything surfaced downstream that the confirmed frame missed — an Issue-Spotter-class issue found by the Devil's Advocate, an unresearched legal point caught at check 7 — is logged in the ledger and audit as `FRAME-MISS: <what> — surfaced by <agent/check> at cycle <N>`, and offered back into `matter-context.md` and (where generalisable) this checklist. The log hardens the next run; hiding a miss breaks Rule 2.

## Optional: duet cross-check (highest-stakes frames)

Where the user asks (or the stakes warrant offering it), the confirmed-candidate frame may be sent through the duet-bridge for a cross-vendor second opinion **before** checkpoint 1 is presented, with the disagreement (if any) shown alongside the Frame Challenger's objections. One bridge call; never default; never a substitute for the user's confirmation.
