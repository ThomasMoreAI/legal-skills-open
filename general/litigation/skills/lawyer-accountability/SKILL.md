---
name: lawyer-accountability
title: Lawyer Accountability
description: Track and evaluate solicitor performance, costs, and accountability. Use when the user says "is my lawyer doing their job", "track my legal costs", "review my solicitor's advice", "hold my lawyer accountable", "was I properly represented", "review the settlement process", "check my legal bills", or has concerns about their solicitor's conduct or advice.
author: odin33g
author_url: https://github.com/odin33g/family-court-strategist/tree/main/plugin/skills/lawyer-accountability
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Lawyer Accountability

Help the user systematically track, evaluate, and hold their legal representation accountable. Whether they currently have a solicitor or are reviewing past representation, this skill builds an evidence-based assessment.

## What to Track

### 1. Communication Log
For every interaction with the solicitor, record:
- Date and method (email, phone, meeting)
- What was discussed
- What advice was given
- What the user was told to do
- What the solicitor said they would do
- What actually happened next

### 2. Cost Tracking
Build a detailed cost record:
- Cost agreement terms (hourly rate, estimate, fixed fee)
- Every invoice received (date, amount, description of work)
- Running total of costs vs original estimate
- Value assessment: what did each dollar achieve?

Ask: does the total cost make sense for the work done? Were there charges for work that didn't advance the case?

### 3. Advice Assessment
For every significant piece of advice, evaluate:

**Was the advice in the client's interest?**
- Did the advice consider all available evidence?
- Were alternatives presented?
- Was the client given time to consider?
- Did the advice align with the evidence or contradict it?

**Was the client pressured?**
- Was there a rushed timeline?
- Was the client told "this is your only option"?
- Were consequences overstated to force a decision?
- Was the client given proper opportunity to review documents?

**What was NOT said?**
- Were there arguments the lawyer didn't make?
- Evidence they didn't use?
- Witnesses they didn't call?
- Applications they didn't file?
- Subpoenas they didn't pursue?

### 4. Settlement Review (if applicable)
If the case was settled, assess:
- How much time was given to consider the offer?
- Was all evidence reviewed before settlement?
- Were there untested arguments that could have changed the outcome?
- Did the solicitor recommend settlement despite strong evidence?
- Was the client's consent truly informed?

## Red Flags

Flag any of these to the user:
- Solicitor recommending settlement without reviewing all subpoena material
- Rushed settlement timelines (less than a week to decide)
- Advice that contradicts what the evidence shows
- Failure to pursue relevant subpoenas or evidence
- Not cross-examining key witnesses
- Billing for work that wasn't done or didn't advance the case
- Not explaining the implications of consent orders
- Failing to follow up on expert recommendations
- Not raising alienation when evidence supports it

## For Self-Represented Parents

If the user doesn't have a lawyer:
- Help them understand what a solicitor SHOULD be doing at each stage
- Flag when they need professional advice (they can get limited-scope help)
- Help them prepare questions for any consultations
- Track interactions with the other party's solicitor
- Ensure they understand their rights in negotiations

## Output

Present findings as a structured assessment:
1. **Representation Timeline** — key interactions and decisions
2. **Cost Analysis** — total spend, value delivered, questionable charges
3. **Advice Assessment** — what was good, what was missed, what was wrong
4. **Accountability Issues** — specific failures with evidence
5. **Recommended Actions** — what the user can do about it (complaint, costs application, new representation)

## Important Notes

- This is not legal advice. This is evidence organisation and pattern identification.
- Recommend the user seek independent legal advice before taking formal action against a solicitor.
- A costs assessment can be requested through the court or the legal costs review body in their jurisdiction.
- Professional conduct complaints go to the relevant law society or legal services commissioner.
