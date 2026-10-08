---
name: draft-warning-letter-sboghossian
title: Warning Letter (Employment Discipline)
description: 'Use when drafting a disciplinary warning letter — the formal written record of misconduct, rule violation, or performance failure that forms part of the progressive discipline ladder. Covers verbal-documented coaching through final written warning, with jurisdiction-specific rules for Lebanon (Article 75), KSA (Article 80), UAE federal (Decree-Law 33/2021), and DIFC. Flags the critical drafting rules: stick to facts, avoid characterizations without evidence, ensure equal treatment, and keep the letter confidential to the personnel file.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-warning-letter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Warning Letter (Employment Discipline)

A warning letter is the formal, written step in the progressive discipline process. It creates the documented record that protects an employer who subsequently terminates for cause — and equally, it creates the opportunity for the employee to understand the problem and correct it. In most MENA jurisdictions, courts and labor authorities look unfavorably on dismissals that have not been preceded by documented progressive discipline (except for the most serious misconduct).

## When to use this

- An employee has committed misconduct, violated a company policy, or failed to meet documented performance standards
- The employer has completed an investigation and determined that a formal warning (rather than informal coaching) is warranted
- Prior verbal discussions have not resulted in behavioral change and a written record is required
- As the penultimate step before termination for cause in a progressive discipline sequence

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Employee full name + title + employee ID | Precise identification | Must provide |
| Employer name and signatory | Issuing party | Must provide |
| Specific incident(s) with dates | Factual basis for the warning; vague warnings are unenforceable | Must provide |
| Policy or rule violated | Specific reference (by name, clause number, or company policy document) | Must provide |
| Level of warning | Verbal documented / Written / Final written | Must specify |
| Required corrective action | What the employee must do differently | Must provide; be specific and measurable |
| Consequence of recurrence | What happens if the behavior continues | Must state; typically: escalation to next level or termination |

## Optional inputs

- Prior verbal warnings or coaching sessions (reference with dates)
- Witness statements (attach separately; do not embed in warning letter)
- Applicable performance improvement plan (attach as Schedule 1 if this warning is accompanied by a PIP)
- Reference to HR investigation findings

## Progressive Discipline Ladder

| Stage | Instrument | When to use | Record |
|---|---|---|---|
| 1. Verbal documented coaching | Verbal conversation + email follow-up or signed note | Minor first offenses; performance dip | HR file note; manager email summary |
| 2. Written warning | Formal letter — this skill | Repeat minor offense; single moderate offense | Signed letter in personnel file |
| 3. Final written warning | Formal letter — this skill (elevated language) | Repeat offense after written warning; serious single offense | Signed letter in personnel file |
| 4. Suspension | Suspension notice | Pending investigation; or as a disciplinary measure where permitted | Separate suspension document |
| 5. Termination | Termination letter + severance | See [[draft-termination-letter]] | Separate instrument |

Most civil-law courts (LB, UAE onshore, KSA) and common-law employment tribunals (DIFC, UK) require evidence of progressive discipline before upholding a termination for conduct or performance — unless the conduct is so serious as to justify summary dismissal.

## Document Structure

### Warning Letter Template

```
[Company Letterhead]

CONFIDENTIAL — PERSONNEL FILE

Date: [Date]

[Employee Full Name]
[Title / Department]
[Employee ID]

Subject: [WRITTEN WARNING / FINAL WRITTEN WARNING] — [Subject Matter]

Dear [Employee Name],

1. PURPOSE OF THIS LETTER

This letter constitutes a [Written Warning / Final Written Warning] in
relation to the matter described below. It will be placed in your personnel
file and may be considered in any future disciplinary proceedings.

2. INCIDENT / CONDUCT

On [Date(s)], [specific factual description of what happened: what the
employee did or failed to do, in what context, and what the consequence was].

[For repeat offenses:]
This follows a verbal / written warning issued on [Date] in relation to
[prior incident], at which time you were informed that [required corrective
action].

3. POLICY VIOLATED

Your conduct described above constitutes a breach of [specific policy:
by name; section/clause number if applicable]. The relevant provision states:
"[Brief quote from policy if available]."

[Or, if no written policy:]
Your conduct is inconsistent with the Company's standards of [workplace
behavior / professional conduct / performance expectations] as communicated
to you on [dates of training, policy acknowledgment, performance review].

4. REQUIRED CORRECTIVE ACTION

Effective immediately, you are required to:

(a) [Specific, measurable corrective action 1]
(b) [Specific, measurable corrective action 2]
(c) [Specific, measurable corrective action 3]

These requirements will be monitored by [manager / HR] over the next
[30 / 60 / 90 days].

5. CONSEQUENCE OF RECURRENCE

Should a similar incident occur, or should you fail to meet the corrective
actions set out above, the Company will escalate to [a Final Written Warning
/ suspension / termination of employment], in accordance with the Company's
disciplinary policy and applicable law.

6. ACKNOWLEDGMENT

Please sign and return a copy of this letter to confirm receipt.
Your signature does not necessarily indicate agreement with the contents.
If you wish to record a response to this warning, you may do so in writing
within [5] business days; any response will be attached to this letter in
your file.

Yours sincerely,

[Manager / HR Director Name]
[Title]
[Company]

Receipt acknowledged: _________________________ Date: ____________
[Employee Signature]
```

## Jurisdictional Notes

### Lebanon (Labor Code Article 75)
- Article 75 requires that, before terminating an employee for certain types of misconduct (particularly misconduct that is not among the most serious categories listed in Article 73), the employer must have previously issued at least one written warning
- If the employer terminates for cause without a prior written warning (where one is required), the dismissal may be treated as arbitrary dismissal under Article 74, triggering additional indemnity
- Form: no specific statutory form for the warning; a signed letter is sufficient; a copy must be kept in the personnel file

### KSA (Labor Law Article 80)
- Article 80 sets out specific grounds for summary dismissal without notice or EOSA (end-of-service award)
- For dismissals outside Article 80 (e.g., general misconduct or performance issues), the employer should maintain documented warnings before terminating
- The Ministry of Human Resources and Social Development (MHRSD) may examine the employer's disciplinary file if an employee files a complaint; documented warnings significantly strengthen the employer's position
- Employee's right of response: the employer should allow the employee an opportunity to respond to the warning in writing before or at the time of issuance

### UAE Federal (Decree-Law 33/2021)
- Progressive discipline is expected but not strictly prescribed in statute; UAE labor courts examine the reasonableness of the employer's conduct
- For terminations for cause: if the cause does not fall within the specific grounds in Article 44 (which allow summary dismissal), the employer must show a reasonable disciplinary process
- Form: no statutory requirement; a signed letter filed with the HR record is standard
- Ministry of Human Resources: MoHRE can mediate disputes; documented warnings strengthen the employer's case in mediation and litigation

### DIFC (DIFC Employment Law + ACAS-equivalent guidance)
- The DIFC Courts apply principles similar to English employment law; ACAS-style procedural fairness is expected
- Minimum: employee should know the problem, have an opportunity to improve, receive a formal warning, and have a right of appeal
- A dismissal following no warning (unless for serious misconduct) is likely to be held procedurally unfair by the DIFC Courts
- Right of appeal: the warning letter should state the employee's right to appeal within [5–10] business days to [HR Director / CEO]; this right of appeal is expected under DIFC procedural practice

### UK (ACAS Code of Practice)
- The ACAS Code of Practice on Disciplinary and Grievance Procedures is not legally binding but is taken into account by employment tribunals when assessing unfair dismissal claims
- Three-stage discipline: oral warning → first written warning → final written warning → dismissal
- Right of appeal at each stage
- Right to be accompanied at formal disciplinary hearings

## Critical Drafting Rules

### Stick to facts — avoid characterizations without evidence
- BAD: "Your dishonest behavior has undermined trust in the department"
- GOOD: "On [date], you submitted a timesheet recording 8 hours for [date] when you were absent from the office from 10am to 4pm as confirmed by [access log / witness / CCTV record]"
- The fact-based approach: (a) avoids defamation risk; (b) creates a paper trail that can be relied on in subsequent proceedings; (c) gives the employee a clear and specific allegation to respond to

### Protected characteristics
The incident described in the warning must be assessed on its own merits, without any connection (even implied) to the employee's protected characteristics (religion, nationality, gender, age, etc.). If similar conduct by other employees has not been disciplined, the warning may be challenged as discriminatory.

### Equal treatment
The employer's disciplinary track record matters. If Employee A receives a warning for conduct X, and Employee B performs the same conduct X and receives no warning (or is immediately dismissed), both employees have grievances. Maintain consistency across similarly situated employees.

### Confidentiality
A warning letter is a confidential personnel document. It should not be circulated to colleagues, clients, or anyone outside the HR and management chain. Circulation beyond authorized persons:
- Undermines the employee's dignity
- Creates a hostile workplace claim
- In many jurisdictions, disclosure of personnel information is restricted by data protection law (GDPR, UAE Federal Law on Data Protection, DIFC Data Protection Law)

### The acknowledgment signature
The employee signing "receipt acknowledged" is confirmation of delivery — not agreement with the contents. This distinction must be clear. If the employee refuses to sign, note the refusal: "Employee declined to sign; letter delivered to [Employee] on [Date] in the presence of [Witness Name]."

### Investigation before warning
A warning should be preceded by at least a basic investigation: what happened, when, who was involved, what the policy says, and whether the employee had a chance to explain their conduct. For serious matters, a formal investigation (HR and/or line manager, with written findings) should precede the warning.

## Common Mistakes

- **Vague incidents** — "your performance has been unsatisfactory" without specific dates, targets, and misses is unenforceable and provides the employee with nothing to respond to
- **Threatening language** — warning letters that use threatening or aggressive language ("this is your last chance," "you are on notice that any further incident will result in instant dismissal") may give rise to a constructive dismissal claim if they are disproportionate
- **No corrective action** — a warning that only describes the problem without specifying what the employee must do differently fails its primary remedial purpose
- **No follow-up** — issuing a warning and never following up on the corrective actions renders the warning effectively meaningless and the employer's position weaker in any subsequent dismissal
- **Warning issued too late** — if months pass between the incident and the warning, the employee may argue they believed the matter was resolved; act promptly (within days to two weeks of conclusion of the investigation)

## Related skills

- [[draft-termination-letter]]
- [[draft-severance-agreement]]
- [[draft-employment-contract]]
- [[kb-employment-law-mena]]
