---
name: academy-litigation-game-coach-sboghossian
title: Litigation Game Coach — Simulation-Based Litigation Training
description: Use when a junior litigator or litigation trainee wants to build courtroom and advocacy skills through simulation-based training without client-matter risk. Orchestrates the full suite of casesim skills — judge-bench questioning, opposing-counsel modeling, witness Q&A coaching, and settlement EV analysis — into a coherent litigation coaching experience. Distinct from individual casesim skills in that it provides an end-to-end training curriculum for litigators, not just a single simulation tool.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/academy/academy-litigation-game-coach
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Litigation Game Coach — Simulation-Based Litigation Training

## When to use this

Invoke when:
- A junior litigator asks "how do I get better at cross-examination without real cases?"
- A litigation team asks for a training curriculum for new associates
- A law school or bar-prep program wants structured litigation simulation exercises
- A lawyer is preparing for a specific hearing, trial, or arbitration and wants simulation-based rehearsal
- A firm's professional development manager asks for structured advocacy training

## What the Litigation Game Coach does

This skill is an **orchestration layer** — it brings together multiple casesim simulation skills into a coherent, progression-based litigation training program. The individual components are:

| Component | Skill | What it trains |
|---|---|---|
| Judge bench perspective | [[casesim-judge-bench-perspective]] | Anticipating judicial questions; fixing weak arguments |
| Opposing counsel simulator | [[casesim-opposing-counsel-simulator]] | Reading the other side's strategy; pre-empting attacks |
| Witness Q&A prep | [[casesim-client-q-and-a-prep]] | Coaching clients through depositions and testimony |
| Cross-examination rehearsal | [[casesim-cross-examination-rehearsal]] | Building cross outlines; practicing impeachment |
| Settlement EV analysis | [[casesim-settlement-vs-trial-ev-calculator]] | Making principled settlement vs. trial recommendations |

## Training levels

### Level 1 — Foundation (0–2 PQE / law students)

Goal: understand the basic mechanics of litigation without the pressure of a live matter.

Exercises:
1. **Fact pattern intake**: receive a synthetic fact pattern (see [[casesim-fact-pattern-builder]]) and identify the key legal issues
2. **Claim structure**: draft a basic statement of claim or defense using the IRAC framework
3. **Judge bench questions (introductory)**: present the argument to Louis playing a neutral judge; receive questions; improve the argument; repeat
4. **Client Q&A fundamentals**: practice opening and closing narrative coaching with a simulated cooperative client

Rubric criteria:
- Issue identification: are all material legal issues spotted?
- Legal reasoning: is the rule correctly stated and applied?
- Argument coherence: does the advocacy flow logically?
- Response to bench: does the lawyer adapt to judicial pushback?

### Level 2 — Intermediate (2–5 PQE)

Goal: develop tactical litigation skills and begin strategic thinking.

Exercises:
1. **Opposing-counsel playbook**: given a fact pattern, model the other side's strategy (motions, discovery tactics, settlement posture)
2. **Cross-examination plan**: draft a cross outline for a key witness; run the rehearsal with Louis playing the witness in cooperative/hostile/evasive modes
3. **Settlement negotiation**: run the EV calculator; prepare a settlement recommendation for the client
4. **Judge challenge mode**: Louis plays a skeptical or hostile bench; the lawyer must maintain composure and adapt in real time

Rubric additions at this level:
- Tactical awareness: does the lawyer anticipate the other side?
- Cross technique: are questions leading and properly sequenced? Are impeachment moments maximized?
- Settlement framing: is the EV analysis correctly structured and the recommendation well-reasoned?

### Level 3 — Advanced (5+ PQE / complex matter preparation)

Goal: simulate the full arc of a dispute from intake to trial or arbitration.

Exercises:
1. **Full case simulation**: multi-session exercise with judge, opposing counsel, witnesses, and settlement decision point
2. **Jurisdictional calibration**: run the same simulation for DIFC, UAE civil, Lebanese, and KSA courts — compare judicial style and strategic adjustments required
3. **Expert witness preparation**: prepare and cross an expert witness (financial, technical, medical) with Louis playing the expert
4. **Closing argument critique**: deliver a closing argument; Louis scores on structure, use of evidence, appeal to applicable law, and rhetoric

## Jurisdiction-specific calibration

Different courts demand different advocacy styles. The Litigation Game Coach adjusts simulation behavior based on the chosen court:

| Court / Forum | Style notes for simulation |
|---|---|
| DIFC Courts | English commercial court style; judges probe legal authority; persuasive precedent admissible |
| ADGM Courts | Similar to DIFC; lean on ADGM Court Procedure Rules |
| UAE Civil Courts (Onshore) | Code-centric; Arabic-language submissions; judges less inquisitorial; written pleadings carry more weight |
| KSA Commercial Courts | Formal; Arabized; sharia-influenced underlying principles; limited oral argument |
| Lebanese Courts | Civil law tradition; French-influenced procedure; oral advocacy at hearings but written submissions dominate |
| ICC / DIAC / LCIA Arbitration | Arbitral procedure; panel of three; written memorials primary; oral hearing compressed |

## Scoring and progression

Each session produces:
- A **session score** (0–100) broken down by rubric criteria
- A **weakness profile**: the two or three areas most needing work
- A **next-session recommendation**: which exercise to run next for maximum growth
- A **cumulative log**: over time, the coach builds a picture of the practitioner's improvement trajectory

## What the coach does not do

- It does not simulate the full emotional and physical pressure of a real courtroom. Experienced practitioners know that simulation has limits.
- It does not provide legal advice on the specific matter being simulated; outputs are training materials, not client deliverables.
- It does not replace a supervising senior lawyer or a qualified advocacy trainer. It supplements them.

## Related skills

- [[casesim-judge-bench-perspective]]
- [[casesim-opposing-counsel-simulator]]
- [[casesim-client-q-and-a-prep]]
- [[casesim-cross-examination-rehearsal]]
- [[casesim-settlement-vs-trial-ev-calculator]]
- [[academy-justinian-tutor]]
