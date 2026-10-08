---
name: draft-pip-letter-sboghossian
title: Performance Improvement Plan (PIP)
description: Use when drafting a Performance Improvement Plan (PIP) letter — formal documentation of identified performance deficiencies with specific improvement objectives, success metrics, timeline, support commitments, and consequence disclosure. Covers best-practice standards (SMART objectives, specificity over generality, documentation of support), anti-patterns (pretextual PIPs, retaliation risk), and jurisdictional considerations for UAE, KSA, Lebanon, and DIFC. Triggers on "pip", "performance improvement plan", "performance warning letter", or "underperformance documentation" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-pip-letter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Performance Improvement Plan (PIP)

## When to use this

A Performance Improvement Plan (PIP) is a formal HR document issued to an employee who is failing to meet their role's performance standards. Its legal purposes are:
1. To give the employee clear notice of the specific deficiencies and a genuine opportunity to improve
2. To create a documented record that any subsequent termination for cause was procedurally fair
3. To protect the employer from wrongful-dismissal claims by demonstrating that termination followed a fair process

Use this skill when:
- An employee has received informal coaching and verbal feedback but performance has not improved
- HR or legal counsel has approved escalation to a formal PIP
- The manager has specific, documented examples of underperformance (not just a "feeling")

A PIP should NOT be used as a pretext to build a termination file for an employee who has already been mentally dismissed — this is a significant legal risk (see Anti-patterns below).

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Employee name, role, department | Full identification |
| Manager and HR contact | Accountability and monitoring |
| Specific performance issues (with examples and dates) | Vague issues are unenforceable and legally weak |
| Improvement objectives (SMART) | Gives the employee a real path to compliance |
| Success metrics | How improvement is measured objectively |
| Review timeline and checkpoint dates | Creates an auditable process |
| Support to be provided | Manager coaching, training, resources — protects employer against claim that improvement was impossible |
| Consequences if not improved | Clear statement of what happens if the PIP is not met |

## Document structure

### 1. Header
```
PERFORMANCE IMPROVEMENT PLAN

Employee Name:     [Full Name]
Role / Title:      [Job Title]
Department:        [Department]
Manager:           [Name, Title]
HR Contact:        [Name, Title]
PIP Start Date:    [Date]
PIP Review Date:   [Date — typically 30, 60, or 90 days]
```

### 2. Purpose and background
One paragraph: "The purpose of this Performance Improvement Plan is to outline specific areas of concern regarding [Employee Name]'s performance, provide clear expectations for improvement, and describe the support the Company will provide to assist [Employee] in meeting those expectations. This PIP covers the period from [start date] to [review date]."

### 3. Specific performance issues identified
This is the most legally critical section. For each issue:
- **State the standard** expected: "The role requires [specific behavior/output]..."
- **State the actual performance**: "Over the past [period], [Employee] has [specific behavior/failure]..."
- **Give concrete examples with dates**: "For example, on [date], [specific incident]. On [date], [another specific incident]."
- **Show the gap**: the delta between the standard and the actual

**Good (specific)**: "Response to client emails is required within 24 hours of receipt. Between [date] and [date], [Employee] responded to 8 out of 15 client emails after the 24-hour deadline, with delays averaging 3 business days. Specific incidents: [Date] — Client [X] email dated [date] was responded to on [date], a delay of 4 business days."

**Bad (unenforceable)**: "Employee's communication with clients has been poor."

### 4. Improvement objectives
State 3-5 SMART objectives:
- **Specific**: each objective is a defined behavior or output
- **Measurable**: success can be verified objectively
- **Achievable**: the objective is within the employee's capability
- **Relevant**: directly addresses the identified performance issue
- **Time-bound**: the objective applies during the PIP period (or a subset)

**Example objective:**
> "Objective 1 — Client Response Time: Respond to all client emails within 24 business hours of receipt. Compliance will be measured by a weekly review of [Employee]'s email log by the Manager. Success standard: 95% of client emails responded to within 24 hours over each 30-day period of the PIP."

### 5. Success metrics
Define how each objective will be measured:
- Quantitative metrics (response rate %, error rate, revenue target, attendance record)
- Process metrics (did the employee follow the procedure?)
- Manager assessment (where quantification is not possible, specify the assessment criteria)

Success threshold: define what level of achievement constitutes passing the PIP (e.g., "Employee must meet all 5 objectives at the stated level throughout the PIP period, with no more than 1 minor exception per 30-day period").

### 6. Timeline and checkpoints
**30-day checkpoint** (for a 90-day PIP):
- Manager reviews progress against each objective
- Written summary of progress provided to Employee
- If improvement is satisfactory: continue; note progress in file
- If improvement is not satisfactory: documented conversation; formal warning if applicable

**60-day checkpoint**:
- Same review process
- If Employee is on track: continue; note progress
- If Employee is not improving: escalation decision; HR involved

**90-day conclusion** (or at the end of the PIP period):
- Final review: pass (all objectives met) or fail (objectives not met)
- If pass: exit PIP; note achievement in file; continued employment on standard terms
- If fail: proceed per consequence stated in Section 7

### 7. Support provided by the Company
This section protects the employer from the argument that the PIP objectives were unachievable or that the employee was not given a genuine opportunity to improve.

Document specifically:
- Manager coaching sessions: frequency, content (e.g., "Weekly 30-minute coaching sessions with [Manager] on [day]")
- Training: specific courses, online modules, external training — with dates
- Mentoring: internal mentor assigned
- Resources: tools, systems access, templates provided
- Reduced workload or adjusted scope during the PIP period (if applicable)

### 8. Consequences if objectives are not met
State plainly and specifically:
"If [Employee Name] does not achieve the improvement objectives set out in this PIP by [date], or if performance deteriorates further during the PIP period, the Company may take further disciplinary action, including but not limited to a formal written warning, demotion, or termination of employment."

Do not soften this language to the point of ambiguity — the employee must clearly understand the consequence.

### 9. Employee acknowledgment and response
"Receipt and acknowledgment of this PIP does not constitute agreement with the contents. [Employee Name] has the right to provide written comments or a response to this PIP within [5] business days."

Signature block:
```
Employee Name: ___________________    Date: ___________
               (Signature acknowledges receipt; not necessarily agreement)

Manager:       ___________________    Date: ___________

HR Representative: _______________    Date: ___________
```

## Best practices

**Specificity is mandatory** — courts and employment tribunals review PIPs for specificity. "Improve attitude" is non-actionable. Describe exact behaviors: "Employee raised voice toward colleagues in two team meetings on [dates], using language that [specific description]. This behavior violates the Company's Code of Conduct, Section X."

**Reasonable objectives** — if the objectives are impossible to meet (insufficient time, unrealistic targets, contradictory demands), the PIP is pretextual. Courts and labor tribunals will look at whether the standard was achievable.

**Document the support** — a PIP without documented support from the employer weakens the fair-process defense. The employer must have made a genuine effort to help the employee improve.

**Consistent treatment** — the performance standard in the PIP must be the same one applied to comparable employees in comparable roles. Selective enforcement of standards is a discrimination risk.

**HR review mandatory** — no PIP should be issued by a manager alone without HR review and approval. HR must verify: legal compliance, consistency with prior practice, factual basis for stated deficiencies.

**Timing** — issuance of a PIP immediately after (or during) an employee complaint, whistleblowing report, protected leave (maternity, medical), or request for accommodation creates a presumption of retaliation in most jurisdictions. Before issuing a PIP in these circumstances, take specialist employment-law advice.

## Anti-patterns

- **Pretextual PIP**: if the termination decision has already been made, issuing a PIP to "build a file" is pretextual and may expose the employer to larger wrongful-dismissal damages. Once the business decision to terminate is made, proceed directly to termination in compliance with applicable law.
- **PIP issued during protected status**: employee on sick leave, maternity/paternity leave, or who has just filed a workplace complaint — issuing a PIP immediately creates a retaliation claim risk
- **Generic template without customization**: a PIP with generic language that could describe any employee in any role is evidentially weak and legally vulnerable
- **"Improve attitude" / "be more professional"**: non-actionable characterizations; describe the specific behaviors that are objectionable

## Jurisdictional considerations

| Jurisdiction | Key considerations |
|---|---|
| **UAE federal** | Labor Law (Decree-Law 33/2021) requires cause for termination of indefinite-term contracts; PIP documentation supports the cause. MOHRE and courts will review whether the termination process was fair. Gratuity obligations and notice period must still be paid even for cause termination unless the cause is one of the specific grounds in Art. 44 (which are narrow). |
| **KSA** | Labor Law Art. 80 allows termination for cause without end-of-service benefit only in specific serious-misconduct circumstances. For poor-performance terminations, notice and EOSB are generally required. Qiwa platform records must be updated. PIP supports the disciplinary record. |
| **Lebanon (LB)** | Labor Code Art. 74 requires specific grounds for termination; an unjustified termination triggers indemnity obligations. A PIP supports the employer's documentation chain. Note: if the employee is covered by a collective agreement, the CBA procedure may apply. |
| **DIFC** | DIFC Employment Law; fair process matters; the PIP is common practice in the financial services and professional services sectors. |

## Related skills

- [[draft-offer-letter]]
- [[draft-employment-contract]]
- [[draft-non-compete]]
- [[review-employment-risk]]
