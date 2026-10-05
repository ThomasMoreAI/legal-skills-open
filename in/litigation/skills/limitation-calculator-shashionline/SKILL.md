---
name: limitation-calculator-shashionline
title: Limitation Calculator
description: Calculate precise limitation periods under Limitation Act 1963 including COVID-19 extension (531 days), exclusions, and extensions. This skill should be used when determining filing deadlines for legal proceedings, appeals, applications, or when analyzing whether a claim is time-barred.
author: shashionline
author_url: https://github.com/shashionline/indian-law-plugin/tree/master/skills/limitation-calculator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: in
practice: litigation
language: en
---

# Limitation Calculator

This skill provides precise limitation period calculation following Limitation Act 1963, including the Supreme Court COVID-19 extension order (March 15, 2020 - October 2, 2021 = 531 days).

## Purpose

Calculate accurate limitation periods by:
1. Identifying correct Article from Limitation Act Schedule
2. Computing basic limitation period
3. Applying exclusions (Section 14, prior litigation)
4. Applying extensions (COVID-19 531 days, acknowledgment, part payment)
5. Determining final filing deadline with precision

## When to Use This Skill

Use this skill when:
- Determining if suit/appeal/application is within limitation
- Calculating exact filing deadline for legal proceeding
- Analyzing whether cause of action is time-barred
- Advising on urgency of legal action
- Drafting pleadings requiring limitation analysis

## Critical Warning

⚠️ **LIMITATION IS MANDATORY** ⚠️

Section 3, Limitation Act 1963:
> "Subject to the provisions contained in sections 4 to 24 (inclusive), every suit instituted, appeal preferred, and application made after the prescribed period shall be dismissed although limitation has not been set up as a defence."

**LIMITATION BARS THE REMEDY, NOT THE RIGHT**

Once period expires:
- Court MUST dismiss (mandatory language)
- No discretion to condone delay (except Section 5 for appeals/applications, NOT suits)
- Cause of action extinguished

## Key Articles - Limitation Periods

Refer to @references/limitation-articles-table.md for complete list.

### Common Articles

**Contracts & Specific Relief**:
- **Article 54**: Specific performance of contract - **3 years** (from date fixed for performance OR if no date fixed, from refusal to perform)
- **Article 55**: Breach of contract - **3 years** (from breach)
- **Article 113**: Suit on contract - **3 years** (from accrual of right to sue)

**Property & Possession**:
- **Article 65**: Suit for possession of immovable property - **12 years** (from dispossession)
- **Article 64**: Suit to recover possession based on title - **12 years** (from accrual of right)

**Torts**:
- **Article 113**: Compensation for wrongful act - **3 years** (from act)

**Appeals**:
- **Article 116**: Appeal from decree/order of civil court (CPC Order 43) - **30/90 days** (from decree/order)
- **Article 117**: Appeal under CPC where no period fixed - **90 days**

**Applications**:
- **Article 137**: Residuary article (applications) - **3 years** (from right to apply accrues)

**Money Suits**:
- **Article 62**: Money lent - **3 years** (from refusal or expiry of notice period)
- **Article 113**: Money payable under contract - **3 years** (from breach)

## Limitation Calculation Workflow

### Step 1: Identify Applicable Article

**Process**:
1. Determine nature of proceeding (suit, appeal, application)
2. Identify cause of action / subject matter
3. Match to Article in Limitation Act Schedule
4. Note limitation period and starting point

**Example**:
```
Proceeding: Suit for specific performance of sale agreement
Nature: Civil suit
Subject: Specific Relief Act, Section 10 (specific performance)
Article: Article 54, Limitation Act
Period: 3 years
Starting Point: Date fixed for performance OR refusal to perform
```

Refer to: @references/article-finder-guide.md

### Step 2: Determine Starting Point (Accrual Date)

**Critical**: Each Article specifies "time from which period begins to run"

**Common Starting Points**:
- Contracts: Date of breach OR date fixed for performance
- Torts: Date of wrongful act
- Possession: Date of dispossession
- Decrees: Date of decree
- Knowledge-based: Date of knowledge (fraud, mistake)

**Example - Article 54**:
```
Sale agreement dated: January 1, 2020
Performance date: June 1, 2020
Seller refused: June 15, 2020
Starting Point: June 15, 2020 (refusal to perform)
```

### Step 3: Calculate Basic Limitation Period

Formula:
```
Basic Expiry Date = Starting Point + Limitation Period
```

**Example (Article 54 - 3 years)**:
```
Starting Point: June 15, 2020
+ 3 years
= June 15, 2023 (basic expiry)
```

### Step 4: Apply Exclusions (Section 14)

**Section 14 - Exclusion of time in certain cases**:

If prior litigation pending in good faith in wrong court:
```
Excluded Time = [Date prior suit filed] to [Date prior suit finally disposed]
Extended Deadline = Basic Expiry + Excluded Time
```

**Conditions**:
1. Prior suit in court lacking jurisdiction
2. Filed in good faith (bonafide belief court had jurisdiction)
3. Diligence shown (no unnecessary delay)

**Example**:
```
Basic Expiry: June 15, 2023
Prior suit filed: March 1, 2021 (wrong court)
Prior suit dismissed: December 1, 2021 (lack of jurisdiction)
Excluded Period: March 1 - December 1, 2021 = 9 months
Extended Deadline: June 15, 2023 + 9 months = March 15, 2024
```

Refer to: @references/section-14-guide.md

### Step 5: Apply COVID-19 Extension

**Supreme Court Order (March 23, 2020 + subsequent extensions)**:

**TOTAL EXTENSION: 531 DAYS**
- Period: March 15, 2020 - October 2, 2021
- Applicability: ALL proceedings (suits, appeals, applications, execution)

**How to Apply**:
```
If limitation period expired OR was running during March 15, 2020 - Oct 2, 2021:
  Extended Deadline = Basic Expiry + 531 days

If limitation started AFTER October 2, 2021:
  No COVID extension applicable
```

**Example 1 - Period Expired During COVID**:
```
Basic Expiry: June 15, 2020 (during COVID extension)
+ 531 days
= November 28, 2021 (extended deadline)
```

**Example 2 - Period Running During COVID**:
```
Starting Point: January 1, 2020
Basic Expiry: January 1, 2023 (3-year period)
COVID Extension: + 531 days (period was running during March 15, 2020 - Oct 2, 2021)
Final Deadline: June 15, 2024
```

**Example 3 - Period Started After COVID**:
```
Starting Point: December 1, 2021 (after Oct 2, 2021)
Basic Expiry: December 1, 2024
COVID Extension: NOT APPLICABLE
Final Deadline: December 1, 2024
```

Refer to: @scripts/covid_calculator.py for automated calculation

### Step 6: Apply Other Extensions/Exclusions

**Section 18 - Acknowledgment**:
Fresh limitation starts from date of written acknowledgment signed by party

**Section 19 - Part Payment**:
Fresh limitation starts from date of part payment

**Section 5 - Condonation of Delay**:
- Applies ONLY to appeals and applications
- Does NOT apply to suits
- Requires "sufficient cause" for delay
- Court has discretion (unlike Section 3)

### Step 7: Final Deadline Determination

**Output Format**:
```
LIMITATION CALCULATION SUMMARY

Proceeding: [Description]
Article: [Number] - [Description]
Base Period: [X] years/days
Starting Point: [Date + event triggering limitation]

CALCULATION:
1. Basic Expiry: [Date]
2. Section 14 Exclusion: + [X] days
3. COVID-19 Extension: + 531 days
4. Other Extensions: + [X] days (if any)

FINAL DEADLINE: [Date]
Days Remaining: [X] days (if not expired)
Status: ✓ WITHIN LIMITATION / ✗ TIME-BARRED

URGENCY: [HIGH/MEDIUM/LOW]
```

**Example Output**:
```
LIMITATION CALCULATION SUMMARY

Proceeding: Suit for specific performance of sale agreement
Article: 54 - Specific performance of contract
Base Period: 3 years
Starting Point: June 15, 2020 (refusal to perform)

CALCULATION:
1. Basic Expiry: June 15, 2023
2. Section 14 Exclusion: + 0 days (no prior litigation)
3. COVID-19 Extension: + 531 days (period expired during extension)
4. Other Extensions: + 0 days

FINAL DEADLINE: November 28, 2024
Days Remaining: 328 days
Status: ✓ WITHIN LIMITATION

URGENCY: MEDIUM (>100 days remaining)
```

## Calculation Script

**File**: @scripts/limitation_calculator.py

**Usage**:
```python
from limitation_calculator import calculate_limitation

result = calculate_limitation(
    article=54,
    starting_point="2020-06-15",
    prior_litigation_days=0,
    apply_covid=True
)

print(result.final_deadline)  # Output: 2024-11-28
print(result.days_remaining)  # Output: 328
print(result.status)           # Output: "WITHIN LIMITATION"
```

**Features**:
- Handles all 137 Articles automatically
- COVID-19 531-day calculation
- Section 14 exclusion logic
- Leap year adjustments
- Business days vs calendar days
- Time-bar warnings

## Integration

### With Protocols
- IL-LIMITATION-001 references this skill for all calculations
- All protocols cite with limitation warnings

### With Agents
- Limitation-specialist agent uses this for all period calculations
- Other agents invoke when analyzing time-sensitive matters

### With Commands
- `/calculate-limitation <article> <start-date>` triggers this skill

### With Hooks
- **limitation-warning** hook uses this to display countdown warnings

## Special Cases

### 1. Continuous Wrongs / Torts
Fresh cause of action each day wrong continues

### 2. Fraudulent Concealment (Section 17)
Limitation starts from date of discovery

### 3. Minor/Person of Unsound Mind (Sections 6-7)
Limitation starts from attaining majority / regaining sanity

### 4. Legal Representative (Section 16)
Limitation extended for estate legal representative

## Urgency Classification

Based on days remaining:
- **CRITICAL** (< 30 days): Immediate filing required
- **HIGH** (30-100 days): File soon, prepare now
- **MEDIUM** (100-365 days): Plan filing, gather evidence
- **LOW** (> 365 days): Ample time, systematic preparation

## Common Errors to Avoid

1. ❌ Forgetting COVID-19 extension (531 days)
2. ❌ Using wrong starting point for Article
3. ❌ Confusing calendar days vs court working days
4. ❌ Assuming Section 5 condonation applies to suits (it doesn't)
5. ❌ Not checking if period expired during COVID extension period

## Tools Required

This skill uses:
- **Read**: Access reference files, Articles table
- **Bash**: Execute Python calculation scripts

## Disclaimer

This skill provides limitation period calculation assistance. It does not constitute legal advice. Always:
- Verify Article applicability with advocate
- File well before deadline (never on last day)
- Consider Section 5 condonation unavailable for suits
- Consult qualified advocates for time-critical matters
- Note that limitation is MANDATORY bar under Section 3

**LAW IS A PRECISE ENDEAVOR. LIMITATION CALCULATIONS REQUIRE ABSOLUTE ACCURACY.**

---

**Skill Version**: 1.0.0
**Last Updated**: 2025-12-05
**Part of**: Indian Law Knowledge Ecosystem
**Dependencies**: None
**Critical Skill**: Time-sensitive legal deadlines
