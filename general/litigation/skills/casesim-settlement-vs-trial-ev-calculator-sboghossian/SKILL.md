---
name: casesim-settlement-vs-trial-ev-calculator-sboghossian
title: Settlement vs. Trial EV Calculator — Should You Take the Offer?
description: Use when an attorney or client needs to compare the expected value of accepting a settlement offer against the expected value of proceeding to trial — incorporating P(win), damages range, costs to trial, loser-pays rules, discount rate, and strategic or reputational factors. Produces an EV comparison (trial vs. settlement), a recommendation (take/counter/decline), and a sensitivity analysis showing which assumptions matter most. Always disclaimed as a probabilistic estimate. Always paired with the outcome probability estimator.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/casesim/casesim-settlement-vs-trial-ev-calculator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Settlement vs. Trial EV Calculator — Should You Take the Offer?

## When to use this

Invoke when:
- Opposing counsel has made a settlement offer and the client asks "should we take it?"
- A litigation team is preparing for a settlement conference and needs an internal floor / ceiling analysis
- A client's board asks for a "go / no-go" recommendation on litigation versus early resolution
- An attorney needs to explain the settlement vs. trial decision in quantitative terms to a client who wants numbers
- A funding decision for continued litigation needs to be made

This skill works alongside [[casesim-outcome-probability-estimator]], which generates the P(win) and damages range inputs. Use both together for a complete client counseling package.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Settlement offer amount | Yes | The net figure the client would receive (or pay) |
| P(win at trial) | Yes | From [[casesim-outcome-probability-estimator]] or attorney's own assessment |
| Damages range at trial (low / mid / high) | Yes | If liability established, what would the court award? |
| Costs to trial (own side) | Yes | Estimate to judgment; separate from costs already spent |
| Loser-pays rule | Yes | Does the forum apply loser-pays (English rule) or each side bears its own costs (American rule)? |
| Discount rate | Optional | Default: 5–8% depending on jurisdiction and client risk profile |
| Time to judgment | Optional | Months from today to expected judgment date |
| Strategic / reputational factors | Optional | Confidentiality value, business relationship, precedent-setting risk, management distraction |
| Appeal probability | Optional | Will opposing counsel appeal a first-instance win? |

## Calculation methodology

### EV(Trial) — Expected Value of Going to Trial

```
EV(Trial) = [P(win) × E(award | win) - Costs(own)]
            + [P(lose) × -Costs(own)]
            ± [Loser-pays adjustment]
            × [Time discount factor]
```

**Where:**
- E(award | win) = probability-weighted average across the low / mid / high damages scenarios
- Costs(own) = estimate of legal fees and disbursements to trial
- Loser-pays adjustment:
  - If win: add recovery of opponent's costs (partial — typically 60–70% recovery in English-rule forums)
  - If lose: subtract payment of opponent's costs
- Time discount: apply the discount rate over the expected time to judgment

**Example:**

| Variable | Value |
|---|---|
| P(win on liability) | 65% |
| Expected award (mid scenario) | USD 800,000 |
| Costs to trial (own) | USD 120,000 |
| Loser-pays rule | English rule (DIFC) |
| Opposing costs if lose | USD 100,000 |
| Discount rate | 6% |
| Time to judgment | 18 months |

EV(Trial) = [0.65 × (800,000 + 0.65 × 100,000) - 120,000]
           + [0.35 × -(120,000 + 100,000)]
           discounted at 6% over 18 months
           ≈ [0.65 × 865,000 - 120,000] + [0.35 × -220,000] × 0.915
           = [562,250 - 120,000 - 77,000] × 0.915
           = 365,250 × 0.915
           ≈ USD 334,200

### EV(Settlement) — Expected Value of Accepting Settlement

```
EV(Settlement) = Settlement amount - Costs already spent (sunk) + [Optional: value of strategic benefits]
```

Note: **sunk costs do not affect the forward-looking decision.** The only relevant comparison is future EV(Trial) against the net benefit of settlement from today. Costs already spent are the same whether the client settles or litigates; they do not change the calculus.

However, where the client is framing the question as "what do I net from this whole matter?" — include sunk costs in the total cost presentation (not in the EV comparison but in the client narrative).

### Net Comparison

```
Settlement advantage / disadvantage = EV(Settlement) - EV(Trial)
```

- **Positive:** settlement is worth more (in expected value terms) than going to trial
- **Negative:** trial has higher expected value; settlement offer is below fair value
- **Near zero:** the decision turns on strategic / non-quantitative factors

## Sensitivity analysis

The most important output after the EV comparison is the sensitivity analysis: **which assumption matters most?**

Louis generates a table showing how the recommendation changes as key variables shift:

| Variable | Base case | Sensitivity test | Effect on recommendation |
|---|---|---|---|
| P(win) | 65% | 55% / 75% | At 55%, settlement more attractive; at 75%, trial clearly preferred |
| Costs to trial | USD 120k | USD 80k / USD 180k | Higher costs make settlement more attractive |
| Time to judgment | 18 months | 12 months / 30 months | Longer time = greater discounting = settlement more attractive |
| Award (mid scenario) | USD 800k | USD 600k / USD 1M | Affects the upside case significantly |

This tells the attorney: "The decision is **most sensitive to P(win)**. If we have reason to believe our win probability is above 70%, we should push back on this offer. If it's below 60%, the settlement looks fair."

## Recommendation framework

Based on the EV calculation and sensitivity analysis, Louis outputs one of:

**TAKE — settlement offer exceeds or approximates EV(trial)**
- Recommended when: settlement is within 10–15% of EV(trial) and strategic factors favor resolution
- Key message to client: "The offer is fair value. The certainty of settlement is worth the small discount versus the expected trial outcome."

**COUNTER — settlement offer is below EV(trial) but trial is not clearly superior**
- Recommended when: settlement offer is 20–40% below EV(trial) but costs, time, or strategic risks make trial unattractive
- Key message to client: "Push back. Make a counter at [X], which reflects a reasonable settlement range. Trial is an option but not our preference given [costs / timing / relationship]."

**DECLINE — EV(trial) materially exceeds the settlement offer**
- Recommended when: settlement offer is more than 40% below EV(trial) and the case is strong
- Key message to client: "This offer does not reflect the value of your claim. Proceed to trial unless opposing counsel substantially improves their position."

## Strategic and non-quantitative factors

The EV calculation captures the financial dimension. These factors may change the recommendation:

| Factor | Effect |
|---|---|
| Confidentiality | If reputational or commercial harm from a public trial is material, settlement has a premium beyond its financial value |
| Business relationship | Settlement may preserve a commercial relationship that has ongoing value |
| Precedent / principle | A public judgment may be worth litigating for even if the EV is comparable — signals to other potential claimants or deters future breach |
| Management distraction | Litigation absorbs executive time; cost is real but hard to quantify |
| Counterparty financial risk | Is the counterparty likely to be able to pay a judgment? An insolvent win has limited value |

## Mandatory disclaimer

Every output of this skill must include: **"This expected value analysis is a probabilistic planning tool, not a prediction of actual outcomes. Legal proceedings involve inherent uncertainty. All assumptions should be reviewed with qualified legal counsel before making any decision."**

## Related skills

- [[casesim-outcome-probability-estimator]]
- [[casesim-opposing-counsel-simulator]]
- [[casesim-judge-bench-perspective]]
- [[casesim-client-q-and-a-prep]]
