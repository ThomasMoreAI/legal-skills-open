---
name: legal-analytics-judicialmind
title: Legal Analytics
description: Legal analytics and outcome prediction skill for case assessment and strategy. Use when the user needs assistance with case outcome prediction, judge analysis, litigation risk assessment, legal fee estimation, or data-driven legal strategy. Triggers on keywords like "legal analytics", "outcome prediction", "judge analysis", "litigation risk", "case assessment", "win rate", "settlement value", "fee estimate", "legal metrics".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/legal-analytics
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Analytics Sources
  path: references/analytics-sources.md
- title: Report Templates
  path: references/report-templates.md
- title: Valuation Methods
  path: references/valuation-methods.md
---

# Legal Analytics

This skill provides expert guidance for data-driven legal analysis, outcome prediction, and strategic decision-making.

## Core Capabilities

### 1. Outcome Prediction
- Case outcome analysis
- Settlement probability
- Damages estimation
- Motion success rates

### 2. Judge & Court Analysis
- Judge ruling patterns
- Court statistics
- Venue selection
- Case duration data

### 3. Opposing Counsel Analysis
- Attorney track records
- Firm patterns
- Settlement behavior
- Litigation style

### 4. Cost & Resource Planning
- Fee estimation
- Budget modeling
- Resource allocation
- ROI analysis

## Case Assessment Framework

### Litigation Risk Matrix
```
┌─────────────────────────────────────────────────────────────────┐
│                    LITIGATION RISK MATRIX                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│         High           │          High                           │
│         Damages        │          Damages                        │
│         Low            │          High                           │
│         Probability    │          Probability                    │
│                        │                                         │
│    ──────────────────────────────────────────                   │
│                        │                                         │
│         Low            │          Low                            │
│         Damages        │          Damages                        │
│         Low            │          High                           │
│         Probability    │          Probability                    │
│                                                                  │
│  X-axis: Probability of Adverse Outcome                         │
│  Y-axis: Potential Damages/Exposure                             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Expected Value Calculation
```
Expected Value = Σ (Probability × Outcome Value)

Example:
- Win probability: 60%
- Win value: $500,000
- Lose probability: 40%
- Lose value: -$200,000 (costs + adverse judgment)

Expected Value = (0.60 × $500,000) + (0.40 × -$200,000)
               = $300,000 - $80,000
               = $220,000
```

### Decision Tree Analysis
```
                    ┌── Win (60%) ──── $500,000
         ┌── Trial ─┤
         │          └── Lose (40%) ──── -$200,000
Case ────┤
         │          ┌── Accept (100%) ── $150,000
         └── Settle ─┤
                    └── Reject ──── [Return to Trial]

Trial EV: $220,000
Settlement: $150,000 (certain)
Decision: Go to trial (higher EV) OR Settle (risk-averse)
```

## Judge Analysis

### Judge Profile Elements
| Category | Data Points |
|----------|-------------|
| Background | Prior practice, education, appointment |
| Caseload | Types of cases, volume |
| Rulings | Motion grant rates, tendencies |
| Trials | Jury vs. bench preferences |
| Appeals | Reversal rates, affirmed decisions |
| Timing | Average case duration, scheduling |
| Demeanor | Courtroom style, preferences |

### Motion Success Rates (Sample Metrics)
| Motion Type | Judge Average | National Average |
|-------------|---------------|------------------|
| 12(b)(6) Dismissal | 35% | 30% |
| Summary Judgment | 45% | 40% |
| Motion to Compel | 70% | 65% |
| Motion in Limine | 55% | 50% |

### Judge-Specific Factors
```
JUDGE ANALYSIS TEMPLATE

Judge: [Name]
Court: [Jurisdiction]
Appointed: [Year] by [President/Governor]

BACKGROUND
- Prior practice: [Plaintiff/Defense/Government]
- Specialty areas: [Areas]
- Judicial philosophy: [Description]

RULING PATTERNS
- Dispositive motions: [Grant rate]
- Discovery disputes: [Tendency]
- Evidentiary rulings: [Tendency]

TRIAL PREFERENCES
- Jury selection: [Approach]
- Trial length: [Typical duration]
- Technology: [Preferences]

NOTABLE DECISIONS
- [Case 1]: [Holding and significance]
- [Case 2]: [Holding and significance]
```

## Venue Analysis

### Venue Selection Factors
| Factor | Analysis |
|--------|----------|
| Legal standards | Applicable law, favorable precedent |
| Judge pool | Judicial tendencies, experience |
| Jury pool | Demographics, verdict patterns |
| Case timing | Docket congestion, time to trial |
| Convenience | Location, travel costs |
| Appeal route | Circuit court tendencies |

### Jurisdiction Comparison
```
| Factor | Jurisdiction A | Jurisdiction B |
|--------|----------------|----------------|
| Time to trial | 18 months | 24 months |
| Plaintiff win rate | 55% | 45% |
| Median damages | $250,000 | $175,000 |
| Summary judgment rate | 35% | 45% |
| Appeal reversal rate | 15% | 12% |
```

## Damages Analysis

### Damages Estimation Approach
1. **Identify comparable verdicts/settlements**
2. **Adjust for case-specific factors**
3. **Calculate ranges (low, middle, high)**
4. **Apply probability weights**
5. **Determine expected value**

### Comparables Analysis
```
VERDICT/SETTLEMENT COMPARABLES

Matter: [Description]
Jurisdiction: [Location]

COMPARABLE 1
Case: [Citation]
Facts: [Brief description]
Outcome: [Verdict/Settlement amount]
Relevance: [Why comparable]

COMPARABLE 2
[Continue...]

ANALYSIS
Low range: $[X] (conservative)
Mid range: $[X] (most likely)
High range: $[X] (optimistic)

Recommended settlement range: $[X] - $[X]
```

### Damages Categories
| Type | Calculation Method |
|------|-------------------|
| Lost profits | Historical + projected |
| Lost wages | Income history + work life expectancy |
| Medical expenses | Bills + future care |
| Pain and suffering | Per diem, multiplier, comparable |
| Punitive | Ratio to compensatory |
| Prejudgment interest | Statutory rate |

## Cost Analysis

### Litigation Budget Framework
```
LITIGATION BUDGET ESTIMATE

Matter: [Description]
Phase: [Scope]

PHASE ESTIMATES
                        Low         Mid         High
──────────────────────────────────────────────────────
Pre-litigation         $[X]        $[X]        $[X]
Pleadings              $[X]        $[X]        $[X]
Discovery              $[X]        $[X]        $[X]
Motions                $[X]        $[X]        $[X]
Trial prep             $[X]        $[X]        $[X]
Trial                  $[X]        $[X]        $[X]
──────────────────────────────────────────────────────
TOTAL                  $[X]        $[X]        $[X]

ASSUMPTIONS
- [Key assumption 1]
- [Key assumption 2]
- [Key assumption 3]
```

### Cost Drivers
| Factor | Impact on Cost |
|--------|---------------|
| Complexity | Number of issues, legal difficulty |
| Document volume | E-discovery, review costs |
| Witnesses | Depositions, expert fees |
| Motions | Briefing, arguments |
| Trial length | Daily trial costs |
| Jurisdiction | Local rates, travel |

### ROI Analysis
```
Litigation ROI = (Expected Recovery - Litigation Costs) / Litigation Costs

Example:
Expected Recovery: $500,000
Litigation Costs: $200,000
ROI: ($500,000 - $200,000) / $200,000 = 150%

Settlement Comparison:
Settlement Offer: $250,000
Settlement Costs: $50,000
Settlement Net: $200,000

Trial Expected Value:
Expected Recovery: $300,000 (probability-adjusted)
Expected Costs: $200,000
Trial Net: $100,000

Recommendation: Accept settlement ($200,000 > $100,000)
```

## Opposing Counsel Analysis

### Counsel Profile
```
OPPOSING COUNSEL PROFILE

Attorney: [Name]
Firm: [Name]
Practice areas: [Areas]
Bar admissions: [States]

TRACK RECORD
- Win/loss record: [X]%
- Settlement rate: [X]%
- Average case duration: [X] months
- Appeals: [Win/loss]

LITIGATION STYLE
- Aggressiveness: [1-5 scale]
- Discovery approach: [Cooperative/Combative]
- Settlement posture: [Early/Late/Never]
- Trial readiness: [High/Medium/Low]

RELEVANT EXPERIENCE
- Similar cases: [List]
- Outcomes: [Results]
- Client relationship: [History with client]
```

## Data Sources

### Legal Analytics Platforms
| Platform | Focus | Data |
|----------|-------|------|
| Lex Machina | Litigation analytics | Case outcomes, timing, damages |
| Westlaw Edge | Litigation Analytics | Judge analytics, case prediction |
| Bloomberg Law | Docket analytics | Trends, comparables |
| Premonition | Attorney analytics | Win rates, timing |
| Ravel Law | Legal research | Citation network, judge language |
| Gavelytics | Judge analytics | Ruling patterns, tendencies |

### Data Points to Track
- Case duration by case type
- Motion success rates
- Settlement rates and timing
- Verdict amounts
- Appeal rates and outcomes
- Attorney performance
- Expert witness effectiveness

## Reporting

### Case Assessment Report
```
CASE ASSESSMENT REPORT

Matter: [Description]
Date: [Date]
Prepared by: [Name]

EXECUTIVE SUMMARY
[2-3 paragraph overview]

OUTCOME ANALYSIS
Probability of favorable outcome: [X]%
Expected damages range: $[X] - $[X]
Settlement recommendation: $[X] - $[X]

RISK FACTORS
1. [Risk 1]: [Impact]
2. [Risk 2]: [Impact]
3. [Risk 3]: [Impact]

COST ESTIMATE
Estimated fees: $[X] - $[X]
Estimated expenses: $[X] - $[X]
Time to resolution: [X] months

RECOMMENDATION
[Strategic recommendation]
```

## Integration with Other Skills

- **litigation**: Case strategy development
- **legal-research**: Precedent analysis
- **case-management**: Resource planning
- **billing-operations**: Budget management
- **due-diligence**: Transaction risk assessment

## Reference Files

For detailed guidance:
- `references/valuation-methods.md` - Damages calculation approaches
- `references/analytics-sources.md` - Data platform guide
- `references/report-templates.md` - Analysis report formats
