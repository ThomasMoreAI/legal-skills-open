---
name: prompt-pack-performance-improvement-plan-sboghossian
title: Performance Improvement Plan
description: 'Use when drafting a performance improvement plan (PIP) for an underperforming employee. Covers specific performance issues, SMART goals, measurable targets, support resources, check-in schedule, timeline, and consequences for non-improvement. MENA-first: addresses UAE Labour Law, KSA Labour Regulations, Lebanese Labour Code, and Egyptian Labour Law requirements for disciplinary documentation before dismissal, as well as DIFC/ADGM employment frameworks.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-performance-improvement-plan
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Performance Improvement Plan

## When to use this

Use this skill when an employer needs to place an employee on a formal performance improvement plan as a structured intervention before considering disciplinary action or dismissal. A well-drafted PIP serves three purposes: (1) gives the employee a genuine opportunity to improve; (2) documents the employer's compliance with procedural fairness requirements; (3) establishes the evidentiary record required to support a lawful dismissal if performance does not improve.

**Jurisdictional importance**: In MENA jurisdictions, labour courts place significant weight on whether an employer provided adequate notice of performance deficiencies and a reasonable opportunity to improve before dismissal. A PIP that is a sham (designed to fail) will not protect the employer; a PIP that is genuine and properly documented is strong evidence of procedural compliance.

Triggers:
- "Draft a PIP for our Marketing Manager who has missed targets for two consecutive quarters."
- "We need to put an employee on a formal performance plan before we consider letting them go."
- "Create a performance improvement template for HR to use consistently."

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Employee name and role | Identifies the PIP subject | Ask user |
| Company name | Identifies the employer | Ask user |
| Specific performance issues | The documented, objective deficiencies that prompted the PIP | Ask user — must be specific, not vague |
| SMART goals | The measurable targets the employee must achieve | Ask user — must be achievable |
| PIP duration | The period over which performance will be assessed | 30 / 60 / 90 days — ask user |
| Support provided | What the company will do to help the employee succeed | Ask user |
| Check-in schedule | Frequency and format of progress reviews | Bi-weekly with line manager |
| Governing law / jurisdiction | Determines mandatory procedural steps | Ask user |

## Optional inputs

- Prior disciplinary record (if any prior informal warnings)
- HR Business Partner involvement
- Whether a union representative is involved (if applicable)
- Whether notice of potential dismissal must be included in the PIP

## PIP document structure

---

**PERFORMANCE IMPROVEMENT PLAN**
**CONFIDENTIAL — EMPLOYMENT RECORD**

**Employee:** [Name]
**Position:** [Job title]
**Department:** [Department name]
**Manager:** [Line manager name]
**HR Representative:** [Name]
**PIP Start Date:** [Date]
**PIP Review Date:** [Date — typically 30/60/90 days after start]

---

### Section 1: Purpose of This Plan

This Performance Improvement Plan is designed to:
- Clearly identify the specific areas where [Employee Name]'s performance has not met [Company Name]'s expectations
- Set clear, measurable targets for improvement
- Provide [Employee Name] with structured support to achieve the required improvement
- Document the steps taken and the outcomes of this process

This PIP is not a disciplinary action. It is a formal performance management process. Successful completion of this plan will remove the performance concerns and allow [Employee Name] to continue in their role.

**Important**: If the required improvements are not achieved by [Review Date], [Company Name] may take further action up to and including termination of employment in accordance with applicable law.

---

### Section 2: Performance Concerns

Document each performance issue with objective, specific, and factual language. Avoid generalizations.

**Performance area 1: [e.g., Sales Target Achievement]**
- **Required standard**: [e.g., Achieve monthly sales target of [AED/SAR X] as set out in the sales plan for Q[X]]
- **Observed performance**: [e.g., Achieved [X]% of target in [Month 1], [Y]% in [Month 2], [Z]% in [Month 3]]
- **Impact**: [e.g., Team's aggregate target shortfall of [AED X] in the past quarter; company revenue projections impacted]
- **Evidence**: [Performance reports dated [X]; meeting notes dated [X]; prior feedback conversation dated [X]]

**Performance area 2: [e.g., Reporting Deadlines]**
- **Required standard**: [e.g., Submit weekly activity reports by 5:00 pm each Friday]
- **Observed performance**: [e.g., Reports submitted late in [X] of the last [Y] weeks; two reports not submitted at all in [period]]
- **Impact**: [e.g., Management cannot track pipeline accurately; delays in forecasting]
- **Evidence**: [Report submission logs; email correspondence dated [X]]

---

### Section 3: Improvement Goals (SMART Format)

For each performance area, set goals that are Specific, Measurable, Achievable, Relevant, and Time-bound.

| Goal | Measure | Target | Deadline |
|---|---|---|---|
| Achieve monthly sales target | Sales system revenue data | [X]% of monthly target for [2 of 3 months] during PIP period | [Date] |
| Submit weekly reports on time | Submission timestamp log | 100% of reports submitted by 5:00 pm Friday; no missed submissions | Rolling throughout PIP period |

---

### Section 4: Support Provided by [Company Name]

To support [Employee Name] in achieving the improvement goals, [Company Name] will provide:

- **Coaching**: [Line Manager Name] will conduct bi-weekly 1:1 coaching sessions; first session on [Date]
- **Training**: Enrollment in [Training Program Name] — [Date/Duration]
- **Resources**: Access to [specific tools, data, or systems] previously unavailable
- **Mentoring**: Introduction to [Mentor Name] from [Department] for [specific skill area] by [Date]
- **Clear feedback**: Manager will provide written feedback after each check-in meeting summarizing progress against goals

---

### Section 5: Check-In Schedule

| Check-in | Date | Format | Participants | Purpose |
|---|---|---|---|---|
| Week 2 check-in | [Date] | 30-min meeting | Employee + Manager | Review initial progress; address early obstacles |
| Week 4 check-in | [Date] | 45-min meeting | Employee + Manager + HR | Formal mid-point review; document progress |
| Week 6 check-in | [Date] | 30-min meeting | Employee + Manager | Progress update |
| Final review | [PIP Review Date] | 1-hour meeting | Employee + Manager + HR | Final assessment of goal achievement |

**Documentation**: The manager will prepare a brief written record after each check-in (delivered to employee within [2 business days]) confirming the topics discussed, progress assessed, and any adjustments to the support plan.

---

### Section 6: Outcomes

At the conclusion of the PIP period ([Review Date]), one of the following outcomes will apply:

1. **Goals achieved**: Performance meets the required standards. PIP is completed successfully. A written confirmation of completion will be placed on the employee's record. Normal performance management resumes.

2. **Partial progress**: Significant improvement demonstrated but not all goals fully met. Company may extend the PIP for a further [30] days with revised targets, or, at Company's discretion, proceed to outcome 3.

3. **Insufficient improvement**: Required improvement standards not achieved. Company will initiate a formal disciplinary process, which may result in further warnings or termination of employment in accordance with applicable law and the Company's disciplinary procedure.

---

### Section 7: Employee Acknowledgment

The employee acknowledges receipt of this PIP and that it has been explained to them.

**Employee statement**: _____________________________________________
[Employee may add comments or disagreement here]

---

| Signature | Name | Title | Date |
|---|---|---|---|
| Employee | | | |
| Line Manager | | | |
| HR Representative | | | |

---

## Jurisdictional notes on PIPs and dismissal

| Jurisdiction | Key requirements before dismissal for performance |
|---|---|
| **UAE (onshore Labour Law)** | Warning(s) required before dismissal for performance reasons; if employer dismisses without warning and opportunity to improve, courts typically award 3 months' wages as compensation; written documentation of performance issues strongly recommended. End-of-service gratuity remains payable even on dismissal for performance (not misconduct). |
| **DIFC (Employment Law)** | Procedural fairness required; documented process (warning, opportunity to improve, decision) protects against unfair dismissal claims; DIFC Courts assess reasonableness of the employer's decision-making process. |
| **ADGM** | Similar to DIFC; ADGM Employment Regulations require fair process before dismissal. |
| **KSA (Labour Regulations)** | Two documented warnings required before dismissal for performance in most cases; HRSD (Ministry of Human Resources) can scrutinize dismissals; GOSI gratuity obligations unaffected by performance dismissal (unlike misconduct). |
| **Lebanon (Labour Code)** | Termination for performance requires notice and NLIF (National Labour Institution Fund) notification; courts assess good faith; redundancy payments apply. |
| **Egypt (Labour Law)** | Social insurance and notice obligations; termination for repeated underperformance documented through HR process; referral to arbitration committee required in some cases before dismissal. |

**MENA general principle**: Labour courts across MENA jurisdictions generally favor employees in dismissal disputes. A well-documented PIP is the employer's primary protection against an arbitrary dismissal finding. Ensure all check-in notes are retained; the employer bears the burden of demonstrating just cause.

**Garden leave / notice**: If employment is terminated at the end of a failed PIP, the employee is entitled to statutory or contractual notice. Payment in lieu of notice is common; do not terminate on the PIP review date without addressing notice obligations.

## Common mistakes

- **Vague performance concerns**: "attitude issues" or "not meeting expectations" without objective evidence are legally weak; courts dismiss such grounds; specify the behaviors and document the evidence.
- **Unrealistic targets**: a PIP designed to fail (targets no reasonable employee could meet in the timeframe) will not protect the employer and may be considered bad faith.
- **No support offered**: failure to provide any support undermines the PIP's procedural legitimacy in common-law and many civil-law jurisdictions.
- **No employee acknowledgment**: the employee should sign the PIP; if they refuse, document the refusal in writing with a witness.
- **Failing to follow through on check-ins**: skipping scheduled check-ins and then terminating without warning is grounds for an unfair dismissal finding.
- **Treating PIP as equivalent to a final warning without saying so**: if dismissal may follow, say so clearly; surprise terminations after a PIP not disclosed as disciplinary are challenged successfully.

## Related skills

- [[prompt-pack-non-compete-agreement]]
- [[heuristic-always-state-jurisdiction-first]]
