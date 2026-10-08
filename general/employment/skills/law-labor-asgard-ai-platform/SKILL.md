---
name: law-labor-asgard-ai-platform
title: Taiwan Labor Law (Labor Standards Act)
description: Analyze Taiwan labor law fundamentals under the Labor Standards Act including working hours, overtime, leave, and termination rules. Use this skill when the user needs to understand employment obligations, calculate overtime pay, evaluate whether a termination is lawful, or design compliant HR policies — even if they say 'how much overtime pay do I owe', 'can I fire this employee', 'what leave are employees entitled to', or 'are we complying with labor law'.
author: asgard-ai-platform
author_url: https://github.com/asgard-ai-platform/skills/tree/main/law-labor
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
sources:
- title: Labor Pension
  path: references/labor-pension.md
- title: Lsa Full Text
  path: references/lsa-full-text.md
---

# Taiwan Labor Law (Labor Standards Act)

## Overview

The Labor Standards Act (勞基法, LSA) sets minimum labor standards in Taiwan. It covers working hours, overtime, leave, wages, and termination. These are MINIMUMS — employers can offer better but not worse terms. This skill focuses on Taiwan-specific requirements.

## Framework

```
IRON LAW: LSA Is a Floor, Not a Ceiling

Everything in the LSA represents the MINIMUM employer obligation.
Employment contracts can exceed these standards but NEVER go below them.
A contract clause that provides less than LSA minimums is void even if
the employee signed it. "The employee agreed to it" is not a defense.
```

### Working Hours & Overtime

| Rule | Standard |
|------|---------|
| Regular hours | 8 hours/day, 40 hours/week |
| Overtime cap | 46 hours/month (can extend to 54 with labor-management agreement) |
| Rest day | 1 regular day off (例假) + 1 rest day (休息日) per week |

**Overtime Pay Calculation:**
| Period | Rate |
|--------|------|
| Weekday overtime, first 2 hours | 1.34x regular hourly rate |
| Weekday overtime, hours 3-4 | 1.67x regular hourly rate |
| Rest day (休息日) overtime, first 2 hours | 1.34x (minimum 4 hours counted) |
| Rest day overtime, hours 3-8 | 1.67x |
| Rest day overtime, hours 9-12 | 2.67x |
| Regular day off (例假) overtime | 2x + compensatory day off |
| National holiday overtime | 2x |

### Leave Entitlements

| Type | Entitlement |
|------|------------|
| Annual leave (特休) | 6 months: 3 days → 1 year: 7 days → 2 years: 10 days → 3-5 years: 14 days → 5-10 years: 15 days → 10+ years: +1 day per year (max 30) |
| Sick leave (病假) | 30 days/year at half pay (hospitalization: additional 1 year) |
| Personal leave (事假) | 14 days/year, unpaid |
| Maternity leave (產假) | 8 weeks at full pay (after 6 months employment) |
| Paternity leave (陪產假) | 7 days at full pay |
| Menstrual leave (生理假) | 1 day/month (first 3 counted as sick leave at half pay; additional at no pay) |

### Termination Rules

**Employer can terminate WITH notice (Art. 11):**
- Business closure or transfer
- Operating losses or business contraction
- Force majeure suspension > 1 month
- Business nature change requiring workforce reduction
- Employee clearly unable to perform duties

**Notice periods:**
| Tenure | Notice Required |
|--------|----------------|
| 3 months - 1 year | 10 days |
| 1 - 3 years | 20 days |
| 3+ years | 30 days |

**Employer can terminate WITHOUT notice (Art. 12):**
- Misrepresentation at hiring
- Violence or serious insult toward employer/coworkers
- Criminal sentence (not probation)
- Serious breach of contract or work rules
- Deliberate damage to equipment/products
- Absence without leave for 3+ consecutive days or 6+ days in a month

**Severance pay**: 0.5 months' average wage per year of service (new system under Labor Pension Act)

## Output Format

```markdown
# Labor Law Analysis: {Situation}

## Applicable Rules
| Rule | LSA Article | Requirement |
|------|-----------|-------------|
| {topic} | Art. {N} | {requirement} |

## Compliance Assessment
| Area | Status | Gap |
|------|--------|-----|
| Working hours | ✓/✗ | {detail} |
| Overtime pay | ✓/✗ | {detail} |
| Leave | ✓/✗ | {detail} |
| Termination | ✓/✗ | {detail} |

## Recommendation
{Specific actions to achieve compliance}
```

## Examples

### Correct Application
**Scenario:** Employee works 10 hours on a Tuesday (regular workday). Base monthly salary: NT$50,000.

Calculation:
- Hourly rate: NT$50,000 / 30 / 8 = NT$208.3
- First 2 overtime hours: NT$208.3 × 1.34 × 2 = NT$558.2
- **Total overtime pay: NT$558** ✓

### Incorrect Application
- "The employee signed a contract agreeing to no overtime pay" → Void. LSA overtime rates are minimum standards that cannot be waived by contract. Violates Iron Law: LSA is a floor.

## Gotchas

- **Exempt vs non-exempt**: Taiwan's LSA covers most workers. Certain categories (managers, supervisors, specific industries designated by the Ministry of Labor) may have modified rules, but the exemptions are NARROW. Don't assume management = exempt.
- **Attendance records are mandatory**: Employers must maintain daily attendance records for at least 5 years. Failure to do so creates a presumption in favor of the employee's claims.
- **Unused annual leave = cash out**: Unused special leave at year-end or termination must be paid out in cash. "Use it or lose it" policies are illegal.
- **Labor inspection**: The Ministry of Labor conducts inspections. Penalties for LSA violations range from NT$20,000 to NT$1,000,000 and repeat offenders are publicly named.
- **This is educational guidance, not legal advice**: Taiwan labor law is complex and frequently amended. Consult a labor attorney or the Ministry of Labor for specific situations.

## References

- For LSA full text (Chinese), see `references/lsa-full-text.md`
- For labor pension system (新制/舊制), see `references/labor-pension.md`
