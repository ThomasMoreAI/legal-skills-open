---
name: casesim-outcome-probability-estimator-sboghossian
title: Outcome Probability Estimator — Probabilistic Litigation Assessment
description: Use when an attorney or client needs a structured probabilistic assessment of likely litigation outcomes — estimating P(win on liability) and a damage range to derive an expected award, adjusted for jurisdiction, judge or tribunal characteristics, appeal probability, and loser-pays cost rules. Produces probability-weighted scenarios at 50th, 75th, and 90th percentile confidence levels with reasoned ranges (not single-point estimates). Always paired with the settlement EV calculator for client counseling. Always disclaimed as an estimate, not a guarantee.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/casesim/casesim-outcome-probability-estimator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Outcome Probability Estimator — Probabilistic Litigation Assessment

## When to use this

Invoke when:
- A client asks "what are our chances?"
- An attorney needs to provide a structured case assessment for a litigation budget discussion
- A settlement negotiation requires a credible internal valuation before entering discussions
- A client is deciding whether to fund litigation to judgment or accept an early offer
- A board or in-house counsel needs a range of outcomes to record in the litigation reserve

Always pair this skill with [[casesim-settlement-vs-trial-ev-calculator]] to give the client a complete picture: the probability-weighted value of trial versus the certainty value of settlement.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Case facts and claims | Yes | What are the legal claims? What happened? |
| Forum and jurisdiction | Yes | Substantially affects the probability analysis |
| Evidence quality | Yes | Strong, mixed, or weak for each element of the claim |
| Applicable law assessment | Yes | How favorable is the legal framework to your position? |
| Quantum of damages (range) | Yes | Low / mid / high estimates for damages if liability is established |
| Cost structure | Yes | Expected costs to trial; whether loser-pays applies and at what rate |
| Time to judgment | Optional | Estimate; affects net present value of any award |
| Appeal probability | Optional | Is an adverse judgment likely to be appealed? What is the reversal rate? |
| Judge or tribunal profile | Optional | Known tendencies, if applicable |

## Analytical framework

### Step 1: Decompose the claim into elements

Every legal claim has elements that must be proved. The probability of success on the full claim is the product of the probability of success on each element (or sub-claim), accounting for dependencies.

Example — breach of contract (DIFC):
- P(valid contract) × P(breach proved) × P(causation) × P(damages quantified) = P(win)

Where one element is structurally strong (e.g., the contract is clearly valid), that factor approaches 1 and does not drive the overall probability. The weak elements dominate.

### Step 2: Assess evidence quality per element

For each element, score the evidence:
- **Compelling** (documentary, unambiguous, corroborated): 80–95% probability
- **Solid** (good documents, credible witnesses, some gaps): 65–80%
- **Contested** (documents support both sides; credibility will be tested): 45–65%
- **Weak** (circumstantial; opposing evidence stronger): 25–45%
- **Problematic** (evidence favors opposing party): 10–25%

### Step 3: Apply jurisdictional adjustments

The same facts and evidence receive different treatment across forums:

| Forum | Adjustment factors |
|---|---|
| DIFC Courts | Well-developed commercial law; high quality of judicial reasoning; outcomes are more predictable based on legal analysis; appeal rate moderate |
| UAE Civil Courts (Onshore) | Outcome more dependent on expert evidence appointed by the court; judicial discretion in damages is significant; delay risk substantial |
| KSA Commercial Courts | Judicial discretion is high; formal legal analysis matters but Sharia-influenced equity considerations can affect damages reduction; appeal common |
| Lebanese Civil Courts | Slow; outcome highly influenced by the specific judge assigned; evidence presentation quality is critical |
| ICC / DIAC Arbitration | Panel composition is the largest variable; outcomes depend heavily on the arbitrators' backgrounds |

### Step 4: Generate probability-weighted scenarios

Louis outputs three scenarios:

**Conservative scenario (50th percentile — "what's more likely than not")**
- The claim outcome a reasonably competent attorney would give as the baseline expectation
- Used for: litigation reserve calculation; board reporting; realistic client expectation-setting

**Favorable scenario (75th percentile — "if things go well")**
- The outcome if the evidence comes in well, witnesses perform as expected, and the legal arguments land
- Used for: settlement floor calculation; upside case for litigation funding

**Best case scenario (90th percentile — "realistic upside")**
- The outcome in a well-run case with no significant adverse surprises
- Used for: maximum demand in settlement; "should we litigate?" decision support

### Step 5: Factor in appeal risk

If the claim succeeds at first instance:
- What is the probability opposing counsel appeals?
- What is the historical reversal rate for this type of claim in this forum?
- How long does appeal add to the timeline (additional cost; discount rate effect)?

Net expected value = P(win trial) × Award × (1 - P(reversal on appeal)) - Costs

### Step 6: Adjust for time value

A judgment in 3 years is worth less than a judgment today. Apply a discount rate to the net expected award:
- User provides discount rate or Louis applies a default based on jurisdiction context
- Higher discount rates favor settlement (the settlement is certain and immediate)

## Output format

```
OUTCOME PROBABILITY ASSESSMENT
Case: [Reference]
Forum: [Court / Arbitral body]
Date of assessment: [Date]

LIABILITY ASSESSMENT
Primary claim: [Description]
Element breakdown:
  - [Element 1]: [Score] — [Brief rationale]
  - [Element 2]: [Score] — [Brief rationale]
  - [Element n]: [Score] — [Brief rationale]

P(win on liability): [XX%] — [Confidence range]

DAMAGES ASSESSMENT
Low scenario: [AED/USD/LBP X]
Mid scenario: [AED/USD/LBP Y]
High scenario: [AED/USD/LBP Z]

PROBABILITY-WEIGHTED SCENARIOS
Conservative (50th pct): [EV] — assuming [brief assumptions]
Favorable (75th pct): [EV] — assuming [brief assumptions]
Best case (90th pct): [EV] — assuming [brief assumptions]

APPEAL ADJUSTMENT
P(appeal if we win): [XX%]
P(reversal): [XX%]
Net expected value after appeal adjustment: [EV]

COST ADJUSTMENT
Costs to trial (our side): [Estimate]
Loser-pays recovery (if applicable): [Estimate]
Net EV after costs: [EV]

DISCLAIMER: This is a probabilistic estimate for planning and counseling purposes.
It is not a guarantee or prediction of any actual outcome. Legal proceedings involve
inherent uncertainty that no model can fully capture. This assessment should be
reviewed by qualified counsel and updated as the case develops.
```

## Mandatory disclaimer

Every output of this skill must include the disclaimer: **"Predictions are estimates for planning purposes, not guarantees. Actual outcomes depend on facts, law, and judicial discretion that no model can fully predict. Pair this assessment with qualified legal judgment."**

## Related skills

- [[casesim-settlement-vs-trial-ev-calculator]]
- [[casesim-opposing-counsel-simulator]]
- [[casesim-judge-bench-perspective]]
- [[casesim-fact-pattern-builder]]
