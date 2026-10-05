# Case Valuation Methodologies

## Overview

Case valuation combines legal analysis with quantitative methods to assess potential outcomes and guide settlement decisions. This guide covers methodologies for damages calculation, probability assessment, and settlement analysis.

## Fundamental Valuation Framework

### Expected Value Calculation

**Basic Formula:**
```
Expected Value = Probability of Success × Potential Recovery - Litigation Costs

EV = (P × R) - C

Where:
P = Probability of winning (0 to 1)
R = Potential recovery amount
C = Expected litigation costs (both sides' costs if fee-shifting)
```

**Example:**
```
Probability of Success: 60%
Potential Recovery: $1,000,000
Litigation Costs: $200,000

EV = (0.60 × $1,000,000) - $200,000
EV = $600,000 - $200,000
EV = $400,000

Rational settlement range: $400,000 (adjusting for risk preferences)
```

### Decision Tree Analysis

```
DECISION TREE STRUCTURE

                            [WIN AT TRIAL]
                           /    60%
                          /     $1,000,000
        [SURVIVE MSJ]    /
       /    70%         <
      /                  \
[CASE]                    \
      \                    [LOSE AT TRIAL]
       \                       40%
        \                      $0
         [LOSE MSJ]
             30%
             $0

Calculation:
Node 1 (Trial): 0.60 × $1M + 0.40 × $0 = $600,000
Node 2 (MSJ): 0.70 × $600,000 + 0.30 × $0 = $420,000
Expected Value (before costs): $420,000
```

### Multi-Outcome Scenarios

```
SCENARIO ANALYSIS

                    Probability    Damages      Weighted Value
────────────────────────────────────────────────────────────────
Best Case           10%           $5,000,000    $500,000
Good Case           25%           $2,000,000    $500,000
Base Case           35%           $1,000,000    $350,000
Poor Case           20%           $250,000      $50,000
Worst Case          10%           $0            $0
────────────────────────────────────────────────────────────────
Total               100%                        $1,400,000

Risk-Adjusted Value: $1,400,000
Less Costs: ($300,000)
Net Expected Value: $1,100,000
```

## Damages Models by Claim Type

### Contract Damages

**Expectation Damages:**
```
Damages = Benefit of Bargain - Actual Position

= [Contract Price × Expected Volume] - [Cost to Perform] - [Mitigation]

Example:
Contract price: $100/unit × 10,000 units = $1,000,000
Cost to perform: $700,000
Lost profit: $300,000
Partial mitigation (cover contract): ($150,000)
Net expectation damages: $150,000
```

**Consequential Damages:**
```
Elements Required:
1. Foreseeable at contract formation
2. Proximately caused by breach
3. Proved with reasonable certainty

Common Categories:
- Lost profits on downstream contracts
- Cost of cover
- Incidental costs (storage, shipping)
- Interest/financing costs
```

### Tort Damages

**Personal Injury:**
```
ECONOMIC DAMAGES:
+ Past medical expenses (documented)
+ Future medical expenses (present value)
+ Past lost wages (documented)
+ Future lost earnings (present value)
+ Loss of earning capacity
+ Other out-of-pocket costs
= Total Economic Damages

NON-ECONOMIC DAMAGES:
+ Pain and suffering
+ Emotional distress
+ Loss of enjoyment
+ Loss of consortium
= Total Non-Economic Damages

TOTAL DAMAGES = Economic + Non-Economic (subject to caps)
```

**Wrongful Death:**
```
SURVIVAL CLAIM:
+ Decedent's pain and suffering (pre-death)
+ Medical expenses (pre-death)
+ Funeral expenses

WRONGFUL DEATH CLAIM:
+ Lost financial support (present value)
+ Lost services
+ Loss of companionship
+ Beneficiary's emotional distress
```

### Employment Damages

**Discrimination/Wrongful Termination:**
```
BACK PAY:
+ Lost wages (termination to judgment)
+ Lost benefits value
+ Lost bonus/commission
- Mitigation earnings
- Unemployment received
= Net Back Pay

FRONT PAY (Alternative to Reinstatement):
+ Future lost wages (until retirement or mitigation)
+ Future lost benefits
Present valued to judgment date

COMPENSATORY DAMAGES:
+ Emotional distress
+ Reputational harm
+ Medical expenses (mental health)

PUNITIVE DAMAGES:
+ Subject to ratio limitations
+ Typically capped at 2-3× compensatory
```

**Wage and Hour:**
```
Unpaid wages: $X
+ Liquidated damages (100% FLSA): $X
+ Pre-judgment interest
+ Attorney's fees
= Total Recovery
```

### Intellectual Property Damages

**Patent Infringement:**
```
LOST PROFITS (preferred):
Requires: Demand, absence of substitutes, manufacturing
capability, calculable profits

Lost profits = (Sales lost) × (Profit margin)

REASONABLE ROYALTY (floor):
Royalty = [Royalty base] × [Royalty rate]

Georgia-Pacific factors determine reasonable rate
Historical royalty rates as benchmark

ENHANCED DAMAGES:
Up to 3× actual damages for willful infringement
```

**Trademark Infringement:**
```
PLAINTIFF'S DAMAGES:
+ Lost profits
+ Corrective advertising costs
+ Reputation damage

DEFENDANT'S PROFITS:
+ Gross revenues from infringing sales
- Costs (defendant's burden)

STATUTORY DAMAGES (if available):
$1,000 to $2,000,000 per counterfeit mark
```

### Securities Fraud Damages

**Section 10(b) / Rule 10b-5:**
```
OUT-OF-POCKET MEASURE:
Damages = Purchase Price - True Value at Purchase
(adjusted for market factors)

"True value" determined by:
- Price decline after disclosure
- Event study removing market effects
```

**Section 11 (Registration Statement):**
```
Damages = Purchase Price - Value at Suit (or Sale)
Capped at offering price
Reduced by value unrelated to misstatement
```

## Probability Assessment

### Liability Probability Factors

```
PROBABILITY ASSESSMENT CHECKLIST

Legal Strength (0-100%):
[ ] Clear legal duty/violation
[ ] Favorable controlling authority
[ ] No significant defenses
[ ] Statute of limitations satisfied
Base Legal Probability: ____%

Factual Strength (0-100%):
[ ] Documentary evidence supports claim
[ ] Credible witnesses available
[ ] No significant factual disputes
[ ] Favorable expert support
Base Factual Probability: ____%

Procedural Factors (adjustment):
[ ] Favorable forum/judge (+/- %)
[ ] Discovery advantages (+/- %)
[ ] Resource asymmetry (+/- %)
Procedural Adjustment: ____%

COMBINED LIABILITY PROBABILITY: ____%
```

### Damages Probability Assessment

```
DAMAGE PROBABILITY BY COMPONENT

Component          Low Est.    Mid Est.    High Est.   Probability
────────────────────────────────────────────────────────────────────
Direct damages     $200K       $400K       $600K       90%
Consequentials     $100K       $300K       $500K       60%
Punitive           $0          $500K       $1M         30%
Attorneys' fees    $150K       $200K       $250K       70%

WEIGHTED CALCULATIONS:
Direct: 0.90 × $400K = $360K
Consequentials: 0.60 × $300K = $180K
Punitive: 0.30 × $500K = $150K
Fees: 0.70 × $200K = $140K

Expected Damages Award: $830K
```

## Settlement Analysis

### Settlement Range Calculation

```
SETTLEMENT ZONE ANALYSIS

PLAINTIFF'S MINIMUM:
Expected Value - Risk Premium
$1,000,000 × 60% - $200,000 = $400,000
Less risk aversion adjustment (20%): $320,000

DEFENDANT'S MAXIMUM:
Expected Loss + Risk Premium
$1,000,000 × 60% + $200,000 = $800,000
Plus risk aversion (cost of trial): $900,000

ZONE OF POSSIBLE AGREEMENT (ZOPA):
$320,000 to $900,000

Midpoint: $610,000
```

### Negotiation Value Framework

```
BATNA ANALYSIS (Best Alternative to Negotiated Agreement)

PLAINTIFF'S BATNA:
- Trial with expected value: $400,000
- Adjusted for time value: $350,000
- Adjusted for risk: $320,000
Plaintiff walks away below: $320,000

DEFENDANT'S BATNA:
- Trial with expected loss: $600,000
- Plus litigation costs: $200,000
- Plus business disruption: $100,000
Defendant walks away above: $900,000
```

### Monte Carlo Simulation

```
SIMULATION APPROACH

Variables:
- Liability probability (50-70%, normal distribution)
- Damages range ($500K-$2M, log-normal)
- Litigation cost ($150K-$300K, uniform)
- Duration (18-36 months, triangular)

Run 10,000 simulations
Plot distribution of outcomes

Results:
5th percentile: $150,000
25th percentile: $400,000
50th percentile (median): $700,000
75th percentile: $1,100,000
95th percentile: $2,000,000

Insight: Wide range suggests high uncertainty;
consider structured settlement
```

## Valuation Report Template

```
CASE VALUATION MEMORANDUM

CONFIDENTIAL - ATTORNEY WORK PRODUCT

Matter: [Name]
Date: [Date]
Prepared by: [Name]

═══════════════════════════════════════════════════════════════

EXECUTIVE SUMMARY

Estimated Case Value Range: $[Low] to $[High]
Most Likely Value: $[Amount]
Recommended Settlement Range: $[Low] to $[High]

═══════════════════════════════════════════════════════════════

1. LIABILITY ASSESSMENT

Claim 1: [Description]
- Legal probability: ___%
- Factual probability: ___%
- Combined: ___%

Claim 2: [Description]
- Legal probability: ___%
- Factual probability: ___%
- Combined: ___%

Key Risks:
- [Risk 1]
- [Risk 2]

═══════════════════════════════════════════════════════════════

2. DAMAGES ANALYSIS

[Table of damage components with probability weighting]

Component         Amount Range      Probability    Weighted
─────────────────────────────────────────────────────────────
[Category 1]      $X - $Y          ___%           $Z
[Category 2]      $X - $Y          ___%           $Z

Total Expected Damages: $[Amount]

═══════════════════════════════════════════════════════════════

3. COST ANALYSIS

Estimated Litigation Costs Through:
- Summary judgment: $[Amount]
- Trial: $[Amount]
- Appeal: $[Amount]

Timing: [Expected duration]

═══════════════════════════════════════════════════════════════

4. EXPECTED VALUE CALCULATION

[Decision tree or formula showing calculation]

Expected Value: $[Amount]
Risk-Adjusted Value: $[Amount]

═══════════════════════════════════════════════════════════════

5. SETTLEMENT RECOMMENDATION

Minimum acceptable: $[Amount]
Target: $[Amount]
Walk-away: $[Amount]

Rationale: [Explanation]

═══════════════════════════════════════════════════════════════

6. SENSITIVITY ANALYSIS

If liability probability changes by +/-10%: $[Range]
If damages change by +/-20%: $[Range]
If costs increase by 50%: $[Impact]

═══════════════════════════════════════════════════════════════

APPENDICES

A. Comparable verdicts/settlements
B. Detailed damages calculations
C. Legal research summary
D. Expert opinions (if any)

═══════════════════════════════════════════════════════════════
```

## Best Practices

### Valuation Process

1. **Start with legal analysis** - Understand the claims and defenses
2. **Quantify each damages component** - Don't lump
3. **Assess probabilities independently** - Liability vs. damages
4. **Consider multiple scenarios** - Best, base, worst case
5. **Account for costs and timing** - Present value matters
6. **Update regularly** - As case develops
7. **Document assumptions** - For defensibility

### Common Pitfalls

1. **Anchoring** - Don't let demand/offer set your valuation
2. **Overconfidence** - Probability estimates tend high
3. **Ignoring uncertainty** - Ranges are more useful than points
4. **Sunk cost fallacy** - Past costs don't affect future decisions
5. **Emotional factors** - Client anger doesn't increase case value
