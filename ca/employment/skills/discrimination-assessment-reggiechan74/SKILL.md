---
name: discrimination-assessment-reggiechan74
title: Discrimination Assessment Report
description: Assess potential discrimination patterns and document protected class treatment disparities
author: reggiechan74
author_url: https://github.com/reggiechan74/JobOps/tree/main/plugins/jobops/skills/discrimination-assessment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ca
practice: employment
language: en
---

## Configuration

Read `.jobops/config.json`. If missing, stop with:

> JOBOPS NOT CONFIGURED
> Run /jobops:setup to initialize your workspace.

Use `config.directories.<key>` for all file paths in this skill.
Use `config.preferences.cultural_profile` if this skill generates resume-style content.
Use `config.preferences.default_jurisdiction` if this skill has jurisdiction-sensitive logic (crisis/legal skills accept `--jurisdiction=<ISO-3166-2>` to override).

## Default Jurisdiction: Ontario, Canada

This command defaults to **Ontario Human Rights Code** protections.

### Ontario Human Rights Code - Protected Grounds

**All Ontario employees are protected from discrimination based on:**
- **Race**: Including colour, ethnic origin, ancestry, place of origin
- **Creed**: Religion or faith (broadly interpreted)
- **Sex**: Including pregnancy, breastfeeding, gender identity, gender expression
- **Sexual Orientation**: Including LGBTQ2S+ identity
- **Age**: All ages 18+ protected (unlike US ADEA which only protects 40+)
- **Disability**: Physical, mental, learning, developmental disabilities; addiction
- **Family Status**: Parent-child relationship; caregiving responsibilities
- **Marital Status**: Single, married, divorced, common-law, etc.
- **Record of Offences**: Only provincial offences or pardoned federal offences
- **Citizenship**: Canadian citizen, permanent resident, or legally entitled to work

**Filing a Complaint:**
- **Human Rights Tribunal of Ontario (HRTO)**: File Application within 1 year of discrimination
- No requirement to file with employer first (unlike US EEOC)
- Can file directly with HRTO online at HRTO website
- Free to file; no lawyer required (but recommended for complex cases)
- Can seek compensation, policy changes, and other remedies

**Key Differences from US:**
- No "40+" age requirement - all ages protected
- Broader disability definition (includes addiction)
- Family status explicitly protected
- Direct access to tribunal (no EEOC-like agency gate)

**For US users**: Specify `--jurisdiction=US` or your state. US law uses Title VII, ADEA (40+), ADA, EEOC filing requirements.


## CRITICAL DISCLAIMERS - READ ALOUD TO USER

**YOU MUST READ THESE DISCLAIMERS TO THE USER BEFORE PROCEEDING:**

### 1. THIS IS NOT LEGAL ADVICE

**CRITICAL**: This tool is for DOCUMENTATION and ORGANIZATION purposes ONLY. It does NOT provide:
- Legal conclusions about whether discrimination occurred
- Advice on whether to file a complaint or lawsuit
- Predictions about the viability or outcome of any legal claim
- Guidance that replaces consultation with a qualified employment attorney

**The information provided here is educational and organizational in nature. It is NOT a substitute for legal counsel.**

### 2. DISCRIMINATION CLAIMS ARE LEGALLY COMPLEX

Employment discrimination law involves:
- Complex legal standards that vary by jurisdiction
- Burden-shifting frameworks that require expert analysis
- Nuanced factual determinations that only courts can make
- Statute of limitations that are strictly enforced
- Procedural requirements that must be followed precisely

**Only a licensed employment attorney can properly evaluate whether your situation constitutes unlawful discrimination.**

### 3. ATTORNEY CONSULTATION IS ESSENTIAL

**YOU MUST CONSULT AN EMPLOYMENT ATTORNEY** before taking any action based on this assessment. This is not optional guidance - it is a critical recommendation. Reasons include:

- Legal strategy requires professional judgment
- Filing deadlines are strict and missing them can forfeit your rights
- Evidence preservation has legal requirements
- Improper documentation can harm your case
- Retaliation protections have specific triggers
- Settlement negotiations require legal expertise

### 4. RISKS OF FALSE OR UNSUBSTANTIATED CLAIMS

Be aware that:
- False claims of discrimination can have serious legal consequences
- Unsubstantiated allegations can damage your professional reputation
- Employers may countersue for defamation in extreme cases
- Documentation should be factual and contemporaneous
- This tool helps organize information but cannot verify claims

### 5. CONFIDENTIALITY AND PRIVILEGE CONSIDERATIONS

- This conversation may NOT be protected by attorney-client privilege
- Documentation you create may be discoverable in legal proceedings
- Be thoughtful about what you document and how
- Consider consulting an attorney BEFORE creating detailed written records
- Do not share this analysis with others without legal guidance


**User Acknowledgment Required**: Before proceeding, confirm you understand these disclaimers and that you will seek legal counsel for any decisions about filing complaints or taking legal action.


## Argument Handling

**Parse Arguments:**
- `$1` (optional): Incident log file or folder containing documentation
- `--protected-class=X` (optional): Specific protected class to focus analysis on

**If `$1` is provided**: Load and analyze the specified file(s)
**If `$1` is not provided**: Proceed with structured interview to gather information

**Protected Class Options** (for `--protected-class` flag):
- `race` - Race, color, national origin
- `sex` - Sex, gender, pregnancy, sexual harassment
- `age` - Age (40+)
- `disability` - Disability, failure to accommodate
- `religion` - Religion, religious accommodation
- `retaliation` - Retaliation for protected activity
- `multiple` - Intersectional or multiple bases


## Phase 1: Protected Class Identification

### 1.1 Ontario Human Rights Code Protected Grounds (Default)

Systematically identify which protected characteristics may be relevant to the analysis under Ontario law.

#### Race, Ancestry, Place of Origin, Colour, Ethnic Origin
**Protected Grounds:**
- Race (all races protected)
- Colour (skin tone)
- Ancestry and ethnic origin
- Place of origin (country or region of origin)
- Citizenship status

**Questions to Explore:**
1. Have you experienced different treatment related to your race, colour, ancestry, or ethnic origin?
2. Have comments been made about your ethnicity, accent, or cultural background?
3. Are there patterns in how employees of different backgrounds are treated?

#### Sex, Gender Identity, Gender Expression, Pregnancy
**Protected Grounds:**
- Sex (male/female/non-binary)
- Gender identity and gender expression
- Sexual orientation (LGBTQ2S+)
- Pregnancy, breastfeeding, and related needs
- Family status (caregiving responsibilities)

**Questions to Explore:**
1. Have you experienced different treatment related to your sex, gender identity, or expression?
2. Did treatment change after pregnancy announcement or parental leave?
3. Are there comments or patterns related to gender stereotypes?
4. Have caregiving responsibilities been held against you?

#### Age (All Ages 18+ Protected in Ontario)
**Protected Ground:**
- Age (Ontario protects ALL ages 18+, not just 40+ like US ADEA)

**Questions to Explore:**
1. Have comments been made about your age, regardless of whether you're older or younger?
2. Have employees of certain ages been treated differently in layoffs, promotions, or assignments?
3. Has there been pressure related to age-based assumptions?

#### Disability
**Protected Ground:**
- Physical disabilities
- Mental health conditions
- Learning disabilities
- Addiction and substance use disorders (explicitly protected in Ontario)
- Past and present disabilities

**Questions to Explore:**
1. Do you have a physical or mental condition that affects you at work?
2. Have you requested accommodations? What was the response?
3. Did treatment change after disclosure of a medical condition?
4. Have you been subjected to improper medical inquiries?

#### Creed (Religion)
**Protected Ground:**
- Religious beliefs, practices, and observances
- Sincerely held spiritual beliefs
- Indigenous spirituality
- Need for religious accommodation

**Questions to Explore:**
1. Have you requested religious accommodation? What was the response?
2. Have comments been made about your religious beliefs or practices?
3. Have you been scheduled to work during religious observances despite accommodation requests?

#### Marital Status, Family Status, Record of Offences
**Protected Grounds:**
- Marital status (single, married, divorced, common-law, widowed)
- Family status (parent-child caregiving relationships)
- Record of offences (provincial offences or pardoned federal offences only)

**Questions to Explore:**
1. Have you been treated differently due to your marital or family status?
2. Has your caregiving role affected how you're treated at work?

### 1.2 US Federal Protected Classes (For US Users)

**For users in US jurisdictions**, the following federal laws apply:

**Title VII of Civil Rights Act**: Race, color, national origin, sex (including sexual orientation per Bostock), religion

**Age Discrimination in Employment Act (ADEA)**: Age 40+ only

**Americans with Disabilities Act (ADA)**: Physical/mental impairment substantially limiting major life activities

**Genetic Information Nondiscrimination Act (GINA)**: Genetic test results, family medical history

**Note**: US users must file with EEOC before pursuing court action (180-300 days deadline).

### 1.3 Document Applicable Jurisdiction

**Ontario (Default)**:
- File directly with Human Rights Tribunal of Ontario (HRTO)
- 1-year deadline from last incident of discrimination
- No EEOC-equivalent requirement

**US Users**:
- State: _______________
- EEOC filing deadline: [180 or 300 days depending on state]
- State human rights agency: _______________

### 1.3 Intersectional Considerations

Discrimination may occur based on MULTIPLE characteristics simultaneously (e.g., Black women, older women, disabled veterans).

**Document intersections:**
- Primary protected class: _______________
- Secondary protected class (if any): _______________
- How do these intersect in the treatment patterns?


## Phase 2: Adverse Action Documentation

### 2.1 Types of Adverse Employment Actions

Document which adverse actions have occurred. An adverse action is a materially significant disadvantage to an employee.

#### Termination/Discharge
```
TERMINATION DOCUMENTATION
=========================
Date of termination: _______________
Stated reason: _______________
Who made the decision: _______________
Was reason given in writing? Yes/No
Severance offered? Yes/No
Release of claims requested? Yes/No
Witnesses to termination: _______________
Documents received (separation agreement, final pay, COBRA, etc.): _______________
```

#### Demotion
```
DEMOTION DOCUMENTATION
======================
Date of demotion: _______________
Previous title/level: _______________
New title/level: _______________
Compensation change: _______________
Stated reason: _______________
Was reason given in writing? Yes/No
Who made the decision: _______________
Did comparators receive similar treatment? Yes/No
```

#### Failure to Promote
```
FAILURE TO PROMOTE DOCUMENTATION
================================
Position applied for: _______________
Date(s) of application: _______________
Who was selected: _______________
Qualifications of person selected: _______________
Your qualifications: _______________
Stated reason for non-selection: _______________
Interview process: _______________
Decision-makers: _______________
Pattern of promotion decisions: _______________
```

#### Unequal Compensation
```
COMPENSATION DISPARITY DOCUMENTATION
====================================
Your compensation: _______________
Comparator(s) compensation (if known): _______________
Same/similar job duties? Yes/No
Tenure comparison: _______________
Qualifications comparison: _______________
How did you learn of disparity? _______________
Source of information: _______________
```

#### Harassment
```
HARASSMENT DOCUMENTATION
========================
Type of harassment: Verbal / Physical / Visual / Written / Electronic
Frequency: One-time / Occasional / Frequent / Continuous
Severity: _______________
Perpetrator(s): _______________
Reported to: _______________
Date(s) reported: _______________
Response to report: _______________
Witnesses: _______________
Ongoing? Yes/No
```

#### Hostile Work Environment
```
HOSTILE WORK ENVIRONMENT DOCUMENTATION
=====================================
Nature of hostility: _______________
Frequency and duration: _______________
Severe and/or pervasive? _______________
Effect on work performance: _______________
Effect on work environment: _______________
Perpetrator(s) and their roles: _______________
Employer knowledge: _______________
Employer response: _______________
```

#### Retaliation
```
RETALIATION DOCUMENTATION
=========================
Protected activity engaged in: _______________
Date of protected activity: _______________
Adverse action(s) following: _______________
Date(s) of adverse action(s): _______________
Temporal proximity (days between activity and action): _______________
Decision-maker knowledge of protected activity: _______________
Change in treatment pattern: _______________
```

#### Denial of Accommodation
```
ACCOMMODATION DENIAL DOCUMENTATION
==================================
Accommodation requested: _______________
Date of request: _______________
Basis for request (disability, religion, pregnancy): _______________
To whom was request made: _______________
Interactive process engaged? Yes/No
Reason given for denial: _______________
Would accommodation cause undue hardship? (Employer's claim)
Alternative accommodations offered: _______________
```

### 2.2 Additional Adverse Actions to Consider

Other potential adverse actions (document if applicable):
- [ ] Negative performance evaluation
- [ ] Exclusion from meetings or projects
- [ ] Reduced hours or schedule changes
- [ ] Denial of training opportunities
- [ ] Increased scrutiny or micromanagement
- [ ] Assignment to less desirable work
- [ ] Denial of reasonable accommodation
- [ ] Constructive discharge (forced resignation)
- [ ] Negative references
- [ ] Blacklisting or interference with future employment
- [ ] Discipline inconsistent with policy
- [ ] Isolation or ostracism
- [ ] Denial of benefits
- [ ] Transfer to less favorable position or location


## Phase 3: Comparator Analysis Framework

### 3.1 Identifying Similarly Situated Employees

**CRITICAL CONCEPT**: A strong discrimination claim often requires showing that similarly situated employees OUTSIDE your protected class were treated more favorably.

**"Similarly Situated" Means:**
- Same or similar job duties and responsibilities
- Same supervisor or decision-maker
- Same department or work unit
- Similar tenure and experience level
- Same time period
- Similar performance level
- Same conduct or situation (for discipline comparisons)

### 3.2 Comparator Documentation Matrix

Create a comparison matrix for each relevant comparator:

```
COMPARATOR ANALYSIS MATRIX
==========================

Comparator #1:
Name/Identifier: _______________
Protected class status: _______________
Job title/duties: _______________
Supervisor: _______________
Tenure: _______________
Performance level: _______________

COMPARISON POINTS:
| Factor | You | Comparator | Different Treatment? |
|--------|-----|------------|---------------------|
| Same supervisor | Yes/No | Yes/No | |
| Same job duties | Yes/No | Yes/No | |
| Same time period | Yes/No | Yes/No | |
| Similar performance | Yes/No | Yes/No | |
| Similar conduct | Yes/No | Yes/No | |
| Treatment received | [describe] | [describe] | Yes/No |

Evidence of different treatment:
_______________________________________________________________

Comparator #2:
[Repeat structure above]

Comparator #3:
[Repeat structure above]
```

### 3.3 Statistical Patterns (If Available)

If you have information about broader patterns:

```
STATISTICAL PATTERN ANALYSIS
============================
(Note: This requires data that may not be available to you)

Workforce composition:
- Total employees in unit: _______________
- Breakdown by protected class: _______________

Adverse action distribution:
- Who has been terminated? Protected class breakdown: _______________
- Who has been promoted? Protected class breakdown: _______________
- Who has been disciplined? Protected class breakdown: _______________

Pattern observations:
_______________________________________________________________
```


## Phase 4: Pattern Recognition

### 4.1 Incident Frequency and Escalation

**Incident Timeline:**
Create chronological record of all relevant incidents:

```
INCIDENT CHRONOLOGY
===================
| Date | Incident Description | Witnesses | Documentation | Reported? |
|------|---------------------|-----------|---------------|-----------|
| | | | | |
| | | | | |
| | | | | |
```

**Frequency Analysis:**
- Total incidents documented: _______________
- Time span covered: _______________
- Frequency pattern: Increasing / Decreasing / Stable
- Correlation with any events (new supervisor, complaint, leave, etc.): _______________

### 4.2 Escalation Pattern

```
ESCALATION ANALYSIS
===================
Has severity increased over time? Yes/No

Escalation timeline:
1. [Date]: [First incident - severity level]
2. [Date]: [Next incident - severity level]
3. [Date]: [Next incident - severity level]
...

Triggering events for escalation:
- Did escalation follow any complaint or protected activity?
- Did escalation follow any change (new supervisor, disclosure of status)?
- Is there a pattern to timing of escalation?
```

### 4.3 Comments or Statements (Direct Evidence)

**CRITICAL**: Direct evidence of discriminatory intent is rare but powerful. Document ANY statements that:
- Reference protected characteristics
- Reflect stereotypes or bias
- Indicate discriminatory motive

```
STATEMENT DOCUMENTATION
=======================
Statement #1:
Date: _______________
Speaker (name, title): _______________
Context/Setting: _______________
Exact words (as close as possible): _______________
Witnesses present: _______________
Your response: _______________
Documentation created at the time? Yes/No

Statement #2:
[Repeat structure]
```

**Types of statements to document:**
- Direct references to protected class ("You're too old for this role")
- Stereotyping comments ("Women don't work well on this team")
- Coded language ("Not a good cultural fit", "lacks executive presence")
- Jokes or "humor" related to protected characteristics
- Comments about accommodation requests
- Comments about protected activity

### 4.4 Policy Application Disparities

```
POLICY APPLICATION ANALYSIS
===========================
Policy in question: _______________

Application to you:
- Alleged violation: _______________
- Consequence: _______________
- Date: _______________

Application to comparators (same or similar conduct):
- Comparator 1: Conduct: _______________ Consequence: _______________
- Comparator 2: Conduct: _______________ Consequence: _______________
- Comparator 3: Conduct: _______________ Consequence: _______________

Disparity observed:
_______________________________________________________________
```

### 4.5 Opportunity Allocation Differences

```
OPPORTUNITY ALLOCATION ANALYSIS
===============================
| Opportunity Type | Given to You? | Given to Others? | Pattern by Protected Class |
|-----------------|---------------|------------------|---------------------------|
| Training | Yes/No | | |
| High-profile projects | Yes/No | | |
| Mentorship | Yes/No | | |
| Client exposure | Yes/No | | |
| Advancement opportunities | Yes/No | | |
| Stretch assignments | Yes/No | | |
```


## Phase 5: Causation Timeline

### 5.1 Timeline Construction

**CRITICAL**: Establish temporal relationships between protected status/activity and adverse actions.

```
CAUSATION TIMELINE
==================

PROTECTED STATUS/ACTIVITY:
Date: _______________
Event: _______________
(e.g., filed complaint, disclosed disability, announced pregnancy, turned 40)

Who knew about this status/activity?
- Direct supervisor: Yes/No - Date they learned: _______________
- HR: Yes/No - Date they learned: _______________
- Decision-maker: Yes/No - Date they learned: _______________

SUBSEQUENT ADVERSE ACTIONS:
| Date | Adverse Action | Days After Protected Event | Decision-Maker |
|------|----------------|---------------------------|----------------|
| | | | |
| | | | |

CHANGE IN TREATMENT PATTERN:

Before protected event:
- Performance ratings: _______________
- Relationship with supervisor: _______________
- Opportunities provided: _______________
- General treatment: _______________

After protected event:
- Performance ratings: _______________
- Relationship with supervisor: _______________
- Opportunities provided: _______________
- General treatment: _______________

Notable change? Describe:
_______________________________________________________________
```

### 5.2 Temporal Proximity Analysis

**Legal Context** (Educational Only - Consult Attorney):
Courts often consider temporal proximity between protected activity and adverse action. Very close timing (days to weeks) may support inference of causation, though this varies by jurisdiction and is just one factor among many.

```
TEMPORAL PROXIMITY ASSESSMENT
=============================
Protected activity date: _______________
Adverse action date: _______________
Days between: _______________

Proximity category:
[ ] Very close (0-7 days)
[ ] Close (8-30 days)
[ ] Moderate (31-90 days)
[ ] Attenuated (91+ days)

If substantial time gap, intervening events that may explain gap:
_______________________________________________________________
```

### 5.3 Decision-Maker Knowledge

```
DECISION-MAKER KNOWLEDGE ANALYSIS
=================================
Decision-maker for adverse action: _______________

Did they know about your protected status/activity?
[ ] Yes - direct knowledge
[ ] Yes - should have known
[ ] Unknown
[ ] No

Evidence of knowledge:
_______________________________________________________________
```

### 5.4 Pretext Indicators

**IMPORTANT**: "Pretext" means the employer's stated reason for the adverse action is not the true reason.

**Potential Pretext Indicators** (document if applicable):

```
PRETEXT ANALYSIS
================
Employer's stated reason for adverse action:
_______________________________________________________________

Pretext indicators (check all that apply):

[ ] Shifting explanations - Reason has changed over time
    Initial reason: _______________
    Later reason: _______________

[ ] Timing inconsistency - Reason existed before but action only taken after protected activity

[ ] Comparative treatment - Others with same issue not treated the same

[ ] Procedural irregularities - Normal procedures not followed

[ ] Severity mismatch - Punishment disproportionate to alleged offense

[ ] Prior positive treatment - Praised or rewarded for same conduct previously

[ ] Documentation gaps - Claimed performance issues not previously documented

[ ] Factual inaccuracies - Stated facts are demonstrably wrong

[ ] Decision-maker statements - Comments suggesting discriminatory motive

Evidence supporting pretext finding:
_______________________________________________________________
```


## Phase 6: Evidence Assessment

### 6.1 Evidence Categories

Organize all evidence by type and assess strength.

#### Direct Evidence
Evidence that directly proves discriminatory intent without inference.

```
DIRECT EVIDENCE INVENTORY
=========================
| Evidence Description | Source | Date | Strength | Notes |
|---------------------|--------|------|----------|-------|
| | | | Strong/Medium/Weak | |
```

**Examples of Direct Evidence:**
- Discriminatory statements by decision-makers
- Written communications showing bias
- Admission of discriminatory motive
- Policy explicitly based on protected class

#### Circumstantial Evidence
Evidence requiring inference to prove discrimination.

```
CIRCUMSTANTIAL EVIDENCE INVENTORY
=================================
| Evidence Description | Source | Date | Strength | Notes |
|---------------------|--------|------|----------|-------|
| | | | Strong/Medium/Weak | |
```

**Examples of Circumstantial Evidence:**
- Comparator treatment patterns
- Temporal proximity
- Pretext indicators
- Statistical patterns
- History of treatment

#### Documentary Evidence
Written or recorded evidence.

```
DOCUMENTARY EVIDENCE INVENTORY
==============================
| Document Type | Date | Source | Location | Key Content |
|--------------|------|--------|----------|-------------|
| Emails | | | | |
| Performance reviews | | | | |
| Policies/Handbooks | | | | |
| Written warnings | | | | |
| Meeting notes | | | | |
| Text messages | | | | |
| HR complaint records | | | | |
| Medical documentation | | | | |
| Accommodation requests | | | | |
```

#### Witness Evidence
People who may have relevant information.

```
WITNESS INVENTORY
=================
| Witness Name | Relationship | What They Know | Willingness | Contact Info |
|-------------|--------------|----------------|-------------|--------------|
| | | | Known/Unknown | |
```

**Categories of Witnesses:**
- Eyewitnesses to incidents
- Comparators who can describe their treatment
- Former employees with similar experiences
- HR personnel who processed complaints
- Supervisors/managers with relevant knowledge
- Medical providers (for ADA claims)

#### Statistical Evidence
Data showing patterns across groups.

```
STATISTICAL EVIDENCE INVENTORY
==============================
| Data Type | What It Shows | Source | Accessibility |
|-----------|---------------|--------|---------------|
| | | | |
```

### 6.2 Evidence Strength Assessment

Rate overall evidence strength in each category:

```
EVIDENCE STRENGTH SUMMARY
=========================
| Evidence Type | Strength Rating | Key Pieces | Gaps |
|--------------|-----------------|------------|------|
| Direct Evidence | Strong/Medium/Weak/None | | |
| Circumstantial Evidence | Strong/Medium/Weak/None | | |
| Documentary Evidence | Strong/Medium/Weak/None | | |
| Witness Evidence | Strong/Medium/Weak/None | | |
| Statistical Evidence | Strong/Medium/Weak/None | | |

Overall Evidence Assessment: Strong / Medium / Weak

Key Strengths:
1. _______________
2. _______________
3. _______________

Key Gaps:
1. _______________
2. _______________
3. _______________
```


## Phase 7: Retaliation Analysis

### 7.1 Protected Activity Identification

Retaliation claims require: (1) protected activity, (2) adverse action, (3) causal connection.

**Types of Protected Activity:**
- Filing a discrimination charge or complaint
- Participating in investigation or proceeding
- Opposing discriminatory practices (internal or external complaint)
- Requesting accommodation
- Providing testimony or evidence in discrimination case
- Refusing to participate in discriminatory conduct

```
PROTECTED ACTIVITY DOCUMENTATION
================================
Activity #1:
Type of activity: _______________
Date: _______________
To whom reported/filed: _______________
Documentation of activity: _______________
Who knew about this activity?
- Supervisor: Yes/No
- HR: Yes/No
- Decision-maker for later adverse action: Yes/No

Activity #2:
[Repeat structure]
```

### 7.2 Retaliation Timeline

```
RETALIATION TIMELINE
====================
| Date | Protected Activity or Adverse Action | Days Since Last Protected Activity |
|------|-------------------------------------|-----------------------------------|
| | [Protected activity] | N/A |
| | [Adverse action] | |
| | [Protected activity] | N/A |
| | [Adverse action] | |
```

### 7.3 Change in Treatment Pattern

```
TREATMENT PATTERN ANALYSIS
==========================
BEFORE complaint/protected activity:
- Performance ratings: _______________
- Relationship with management: _______________
- Assignments and opportunities: _______________
- Disciplinary history: _______________

AFTER complaint/protected activity:
- Performance ratings: _______________
- Relationship with management: _______________
- Assignments and opportunities: _______________
- Disciplinary history: _______________

Specific changes:
1. _______________
2. _______________
3. _______________
```


## Phase 8: Legal Framework Overview (Educational Only)

### 8.1 Disparate Treatment vs. Disparate Impact

**EDUCATIONAL INFORMATION - NOT LEGAL ADVICE**

**Disparate Treatment:**
- Intentional discrimination based on protected class
- Requires evidence of discriminatory intent
- Most common type of discrimination claim

**Disparate Impact:**
- Neutral policy or practice disproportionately affects protected group
- No intent required, but employer can defend with business necessity
- Typically requires statistical evidence

**Your situation likely involves:** [ ] Disparate Treatment [ ] Disparate Impact [ ] Both [ ] Unclear

### 8.2 McDonnell Douglas Burden-Shifting Framework

**EDUCATIONAL INFORMATION - NOT LEGAL ADVICE**

This is a common framework for analyzing discrimination claims:

**Step 1 - Prima Facie Case** (Employee's initial burden):
- Member of protected class
- Qualified for position
- Suffered adverse employment action
- Circumstances suggest discrimination (e.g., replaced by someone outside protected class)

**Step 2 - Legitimate Reason** (Employer's burden):
- Employer articulates legitimate, non-discriminatory reason for action

**Step 3 - Pretext** (Employee's burden):
- Employee shows employer's reason is pretextual (not the real reason)

**NOTE**: This is a simplified overview. Actual application is complex and varies by claim type and jurisdiction.

### 8.3 Hostile Work Environment Elements

**EDUCATIONAL INFORMATION - NOT LEGAL ADVICE**

General elements (vary by jurisdiction and claim type):
1. Unwelcome conduct
2. Based on protected class
3. Severe OR pervasive (affects work environment)
4. Objectively hostile (reasonable person standard)
5. Subjectively offensive (you found it hostile)
6. Employer liability (knew or should have known, failed to act)

### 8.4 Statute of Limitations Overview

**CRITICAL - FILING DEADLINES**

**EEOC Filing Deadlines:**
- **180 days** from adverse action in states WITHOUT state/local agency
- **300 days** from adverse action in states WITH state/local agency

**State agency deadlines may differ** - research your specific jurisdiction.

**Continuing violations:** Some claims (like hostile work environment) may allow inclusion of earlier conduct if part of continuing pattern.

**ACTION ITEM**: Determine your filing deadline IMMEDIATELY with an attorney.


## Phase 9: EEOC and State Agency Considerations

### 9.1 Administrative Filing Requirements

**CRITICAL INFORMATION:**

Before filing a lawsuit under Title VII, ADEA, or ADA, you MUST:
1. File a charge with the EEOC (or state equivalent)
2. Receive a "Right to Sue" letter
3. File lawsuit within 90 days of receiving Right to Sue letter

### 9.2 Filing Deadlines Summary

```
FILING DEADLINE TRACKER
=======================
Adverse action date: _______________
Today's date: _______________
Days elapsed: _______________

Federal filing deadline:
- 180-day deadline date: _______________
- 300-day deadline date (if applicable): _______________

State agency deadline (research required):
- State: _______________
- Deadline: _______________

Days remaining to file: _______________

**URGENT?** [ ] Yes - immediate action needed [ ] No - time available

ATTORNEY CONSULTATION DEADLINE: _______________
(Recommend consulting attorney WELL before filing deadline)
```

### 9.3 Dual Filing with State Agencies

Many states have their own anti-discrimination agencies (e.g., state civil rights commissions). Benefits of state filing:
- May extend federal deadline to 300 days
- State law may provide additional protections
- Some states allow direct lawsuit without administrative filing

**State agency for your jurisdiction:**
Agency name: _______________
Filing deadline: _______________

### 9.4 The EEOC Process (Overview)

**EDUCATIONAL INFORMATION:**

1. **File Charge**: Submit formal complaint to EEOC
2. **Charge Sent to Employer**: Employer notified and asked to respond
3. **Investigation**: EEOC may investigate, request documents, interview witnesses
4. **Mediation** (Optional): EEOC offers voluntary mediation
5. **Determination**: EEOC issues finding (cause/no cause)
6. **Right to Sue Letter**: Issued either upon request or after EEOC process complete
7. **File Lawsuit**: Must file within 90 days of receiving Right to Sue letter


## Phase 10: Documentation Gaps and Next Steps

### 10.1 Evidence Gaps

Based on the analysis, identify what additional information would strengthen the documentation:

```
EVIDENCE GAP ANALYSIS
=====================

MISSING DOCUMENTARY EVIDENCE:
[ ] Performance reviews - Request from HR
[ ] Written policies - Obtain employee handbook
[ ] Emails/communications - Preserve immediately
[ ] Complaint records - Request copies from HR
[ ] Personnel file - Request copy (check state law for right)
[ ] Comparator information - Limited access

MISSING WITNESS INFORMATION:
[ ] Witness contact information
[ ] Witness willingness to participate
[ ] Witness recollections (memories fade)

MISSING COMPARATOR INFORMATION:
[ ] Identities of similarly situated employees
[ ] Their protected class status
[ ] Their treatment outcomes
[ ] Their performance levels

DOCUMENTATION TO CREATE:
[ ] Detailed chronology with dates
[ ] Contemporaneous notes going forward
[ ] List of all witnesses
[ ] Document preservation list
```

### 10.2 Evidence Preservation

**IMMEDIATE ACTION ITEMS:**

```
EVIDENCE PRESERVATION CHECKLIST
===============================
[ ] Forward relevant emails to personal email (check policy first)
[ ] Screenshot text messages and communications
[ ] Save copies of performance reviews
[ ] Note names and contact information of witnesses
[ ] Create contemporaneous notes of undocumented incidents
[ ] Request copy of personnel file
[ ] Request copy of relevant policies
[ ] Preserve any recordings (if legally made)
[ ] Document organizational charts and reporting structures
[ ] Save copies of job postings and position descriptions
```

**CAUTION:**
- Do NOT take confidential company documents without authorization
- Do NOT secretly record in states requiring two-party consent
- Check company policy on forwarding emails
- Consult attorney about what preservation steps are legally appropriate

### 10.3 Witnesses to Interview

```
WITNESS OUTREACH PLAN
=====================
| Witness | What They Know | Contact Status | Willingness | Notes |
|---------|----------------|----------------|-------------|-------|
| | | | | |
```


## Phase 11: Risk Assessment

### 11.1 Preliminary Claim Viability

**DISCLAIMER**: This is NOT a legal assessment. Only an attorney can evaluate claim viability.

**Organizational Assessment (for information purposes only):**

```
PRELIMINARY ASSESSMENT FACTORS
==============================
| Factor | Strength | Notes |
|--------|----------|-------|
| Protected class membership | Clear / Unclear | |
| Adverse action occurred | Clear / Unclear | |
| Circumstantial evidence of causation | Strong / Medium / Weak | |
| Direct evidence of discrimination | Yes / No | |
| Comparator evidence | Strong / Medium / Weak / None | |
| Pretext indicators | Strong / Medium / Weak / None | |
| Documentary evidence | Strong / Medium / Weak | |
| Witness support | Strong / Medium / Weak | |
| Employer defenses (anticipated) | Strong / Medium / Weak | |

Overall organizational strength: Strong / Medium / Weak

**REMINDER**: This is NOT a legal assessment. Consult an attorney.
```

### 11.2 Potential Employer Defenses

Anticipate defenses the employer may raise:

```
ANTICIPATED EMPLOYER DEFENSES
=============================
[ ] Legitimate non-discriminatory reason for action
    Likely claim: _______________
    Evidence to counter: _______________

[ ] Employee performance issues
    Likely claim: _______________
    Evidence to counter: _______________

[ ] Same decision-maker defense (supervisor is also protected class)
    Applicable? Yes/No
    Counter: _______________

[ ] Statute of limitations
    Applicable? Yes/No
    Counter: _______________

[ ] No knowledge of protected status
    Applicable? Yes/No
    Counter: _______________

[ ] Undue hardship (accommodation cases)
    Applicable? Yes/No
    Counter: _______________
```

### 11.3 Costs and Considerations of Pursuing

**Important factors to consider (discuss with attorney):**

```
COST-BENEFIT CONSIDERATIONS
===========================
(Informational - discuss with attorney)

POTENTIAL COSTS:
- Emotional toll of litigation (typically 1-3+ years)
- Career impact (current and future employment)
- Financial costs (if not contingency)
- Time commitment (discovery, depositions, trial)
- Privacy (personal information may become public record)
- Relationship damage (colleagues may be involved)

POTENTIAL BENEFITS:
- Vindication
- Financial recovery (back pay, front pay, damages)
- Stopping ongoing discrimination
- Helping others in similar situations
- Holding employer accountable

QUESTIONS TO DISCUSS WITH ATTORNEY:
1. What is realistic recovery estimate?
2. How long will process take?
3. What is likelihood of success?
4. What are alternatives to litigation (settlement, mediation)?
5. What is fee arrangement (contingency, hourly)?
```


## Phase 12: Output and Deliverables

### 12.1 Save Assessment Report

Save comprehensive analysis to: `{config.directories.crisis_management}/discrimination_assessment_{YYYYMMDD}.md`

**Report Structure:**

```markdown
# Discrimination Assessment Report
## FOR ATTORNEY CONSULTATION PURPOSES ONLY

**DISCLAIMER**: This document is for organizational and informational purposes only.
It does NOT constitute legal advice. All conclusions and strategies must be reviewed
with a licensed employment attorney before any action is taken.


## Summary
Date prepared: _______________
Prepared for: _______________
Primary protected class(es): _______________
Primary adverse action(s): _______________
Filing deadline: _______________


## Protected Class Analysis
[Summary of Phase 1 findings]

## Adverse Actions Documented
[Summary of Phase 2 findings]

## Comparator Analysis
[Summary of Phase 3 findings]

## Pattern Recognition
[Summary of Phase 4 findings]

## Causation Timeline
[Summary of Phase 5 findings]

## Evidence Inventory
[Summary of Phase 6 findings with strength ratings]

## Retaliation Analysis
[Summary of Phase 7 findings, if applicable]

## Administrative Filing Considerations
[Summary of Phase 9 findings, including deadlines]

## Documentation Gaps
[Summary of Phase 10 findings]

## Risk Assessment
[Summary of Phase 11 findings]


## IMMEDIATE ACTION ITEMS

1. **CONSULT EMPLOYMENT ATTORNEY** (Highest Priority)
   - Research attorneys: NELA, state bar referral, etc.
   - Schedule consultations with 2-3 attorneys
   - Deadline for attorney consultation: _______________

2. **PRESERVE EVIDENCE**
   - [Specific preservation steps]

3. **DOCUMENT ONGOING INCIDENTS**
   - Create contemporaneous notes
   - Note witnesses
   - Preserve communications

4. **KNOW YOUR DEADLINES**
   - Filing deadline: _______________
   - Days remaining: _______________


## ATTORNEY CONSULTATION PREPARATION

Bring to attorney consultation:
- This assessment report
- All documentary evidence gathered
- Chronology of events
- Witness list
- Questions for attorney


## DISCLAIMERS (REPEATED)

1. This assessment is NOT legal advice.
2. Only a licensed attorney can evaluate your legal claims.
3. Filing deadlines are strict - act promptly.
4. False claims can have serious consequences.
5. This document may be discoverable in legal proceedings.
```

### 12.2 Recommended Next Steps

**PRIORITY 1 - IMMEDIATE (This Week):**
1. Consult employment attorney
2. Preserve all evidence
3. Calculate filing deadline

**PRIORITY 2 - SHORT TERM (Next 2 Weeks):**
1. Complete attorney consultations
2. Gather missing documentation
3. Create detailed chronology

**PRIORITY 3 - ONGOING:**
1. Document any new incidents contemporaneously
2. Maintain evidence preservation
3. Follow attorney guidance


## Error Handling

**If insufficient information provided:**
- Conduct structured interview to gather missing information
- Note gaps in documentation
- Recommend specific information to gather

**If filing deadline is imminent:**
- Immediately flag urgency
- Recommend contacting attorney TODAY
- Do not delay documentation process

**If situation suggests immediate danger:**
- Physical safety concerns take priority over documentation
- Recommend appropriate resources (law enforcement if applicable)
- Employment issues are secondary to personal safety


## Session Completion

**Before concluding, confirm:**
1. Assessment report saved to {config.directories.crisis_management}/
2. User understands this is NOT legal advice
3. User has clear next steps for attorney consultation
4. Filing deadlines are clearly communicated
5. Evidence preservation steps are understood

**Final reminder to user:**
> "This assessment is designed to help you organize information for legal consultation. It is NOT legal advice and does NOT constitute a legal evaluation of your claims. Employment discrimination law is complex and varies by jurisdiction. You MUST consult with a licensed employment attorney before taking any action. Filing deadlines are strict and cannot be extended. Please prioritize scheduling an attorney consultation immediately."


Now proceeding with discrimination assessment...
