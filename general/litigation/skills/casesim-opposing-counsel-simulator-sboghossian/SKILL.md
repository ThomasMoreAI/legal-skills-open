---
name: casesim-opposing-counsel-simulator-sboghossian
title: Opposing Counsel Simulator — Build the Other Side's Playbook
description: Use when an attorney wants to model opposing counsel's strategy, predict their likely motions and tactical moves, understand their settlement posture, and build a playbook to pre-empt attacks. Calibrated by firm reputation, counsel personality, and case type. Covers aggressive, collaborative, and dilatory strategies; likely motions (MTD, MSJ, discovery disputes); forum-shopping and parallel proceedings. Output is a structured opposing-counsel playbook for negotiation leverage, settlement strategy, and hearing preparation.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/casesim/casesim-opposing-counsel-simulator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Opposing Counsel Simulator — Build the Other Side's Playbook

## When to use this

Invoke when:
- An attorney needs to anticipate opposing counsel's strategy before a hearing, negotiation, or filing
- A litigation team wants to understand what motions the other side will likely bring
- A transactional lawyer needs to model the counterparty's negotiating approach
- A settlement team wants to understand the other side's likely settlement posture before entering discussions
- A client asks "what will they do next?" and the attorney needs a structured answer

## Inputs

| Input | Required | Notes |
|---|---|---|
| Case summary | Yes | Facts, claims, current status |
| Opposing party's interests | Yes | What outcome do they actually want? What would they take? |
| Opposing firm / counsel identity | Optional | Known firm reputation, counsel personality, past litigation behavior |
| Forum and jurisdiction | Yes | Shapes available tactics |
| Stage of proceedings | Yes | Pre-filing / discovery / pre-trial / settlement discussions / post-judgment |
| Known constraints on opposing side | Optional | Budget, reputational exposure, client instruction limits, insurance involvement |

## Strategic calibration by style

Louis builds the simulation around one of three primary strategic styles (or a blend):

### Aggressive / "Scorched Earth"
Characteristics: high volume of motions; discovery maximalism; forum-shopping; quick to escalate; uses litigation as a pressure tactic against client resources.

Predicts:
- Early procedural motions (jurisdiction challenges, service objections, preliminary objections) to create cost and delay
- Broad discovery requests targeting privileged material
- Motions to dismiss on technical grounds before engaging on merits
- Counterclaims calibrated to increase the defendant's exposure and the settlement price
- Parallel regulatory complaints or press activity to increase pressure

Counter-strategy: procedurally tight filings; early application to narrow discovery scope; clear privilege logs; anticipate and prepare for each early motion now.

### Collaborative / "Problem-Solver"
Characteristics: signals willingness to negotiate early; uses correspondence strategically to build a reasonable-person record; co-operates on procedural matters.

Predicts:
- Early without-prejudice settlement correspondence
- Motions only on matters where they have a strong legal basis
- Discovery cooperation as a trust-building signal, with selective fights on the issues that matter most
- Openness to mediation as a parallel track

Counter-strategy: take the co-operative signals at face value while maintaining full litigation readiness; do not mistake collaborative style for weak substantive position.

### Dilatory / "Attrition"
Characteristics: maximizes time; frequent extensions; complex discovery; appeals every intermediate order.

Predicts:
- Applications for extension of time at every step
- Discovery disputes calibrated to generate satellite litigation
- Appeals of interlocutory orders (procedural harassment)
- Leveraging of client's financial constraints

Counter-strategy: apply for directions / case management orders early to lock in a timetable; resist extensions unless clearly justified; consider a costs order application at an early stage if dilatory behavior is documented.

## Likely motions map

Based on the case facts and forum, Louis generates a map of likely motions by stage:

### Pre-Hearing / Pleadings Stage
- Jurisdictional challenge (especially in cross-border MENA matters: UAE court vs. DIFC vs. arbitral tribunal)
- Improper service challenge
- Preliminary objection to standing
- Application to strike / demurrer
- Motion to compel arbitration (if arbitral clause present but claimant filed in court)

### Discovery Stage
- Broad discovery requests targeting email communications and privilege boundaries
- Motion to compel (if your side is slow on production)
- Motion for protective order (if your side is too aggressive)
- Expert disclosure disputes

### Pre-Trial / Pre-Hearing Stage
- Motion for summary judgment / summary disposal
- Motion to exclude expert evidence (Daubert / FRE 702 equivalent in applicable forum)
- Motion in limine on specific evidence
- Procedural motions to delay hearing

### Settlement Stage
- Walk-away bluff (final demand framed as "last offer" when it is not)
- Conditional settlement offers that restructure rather than resolve
- Settlement structured to shift future liability (indemnities, warranties, non-disclosure obligations)

## Likely settlement posture

Based on the case analysis and opposing party profile:

| Factor | Effect on settlement posture |
|---|---|
| Strong merit position | Lower motivation to settle; higher opening demand |
| Reputational risk | Motivation to settle quietly; will pay a premium for confidentiality |
| Insurance coverage | Settlement authority may be with insurer, not client; adjuster has own incentives |
| Liquidity constraint | High motivation to settle quickly; may accept a low figure that closes the matter |
| Business relationship | Will prioritize relationship-preserving resolution over maximum recovery |
| Public company | Sensitive to litigation uncertainty on earnings; motivated to settle before a major disclosure event |
| KSA / government-adjacent counterparty | Political and relationship dimensions may outweigh pure legal merits |

## Parallel proceedings / jurisdictional tactics

In MENA disputes, jurisdiction shopping is a significant tactical tool:

- A party may file in UAE onshore courts, DIFC Courts, and an arbitral tribunal simultaneously, then use the most favorable forum for interim relief
- A party may use a Lebanese court injunction to freeze assets before a DIFC arbitration award is obtained
- Forum non conveniens arguments are available in DIFC/ADGM but not in civil law forums
- Anti-suit injunctions: available in DIFC/ADGM; not available in UAE onshore or KSA courts

Louis maps the likely jurisdictional moves and how to respond to each.

## Output

1. **Opposing counsel playbook** (structured by stage: pre-filing → discovery → hearing → settlement)
2. **Predicted motions list** (with likelihood rating and recommended preparation for each)
3. **Settlement posture analysis** (motivation to settle, likely range, tactical levers)
4. **Counter-strategy recommendations** (one-line action for each predicted move)

## Limits

- The simulation is based on the facts provided and general patterns; it cannot replicate access to actual legal strategy documents or internal client instructions of the opposing side.
- Calibration by firm / counsel personality relies on general reputation; individual counsel may deviate from firm norms.
- This is a preparation tool, not a prediction of what opposing counsel will do.

## Related skills

- [[casesim-judge-bench-perspective]]
- [[casesim-client-q-and-a-prep]]
- [[casesim-cross-examination-rehearsal]]
- [[casesim-outcome-probability-estimator]]
- [[casesim-settlement-vs-trial-ev-calculator]]
