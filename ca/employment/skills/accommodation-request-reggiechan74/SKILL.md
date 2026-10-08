---
name: accommodation-request-reggiechan74
title: Workplace Accommodation Request Package
description: Build and navigate workplace accommodation requests (disability, religious, medical)
author: reggiechan74
author_url: https://github.com/reggiechan74/JobOps/tree/main/plugins/jobops/skills/accommodation-request
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

This command defaults to **Ontario Human Rights Code** accommodation framework.

### Ontario Duty to Accommodate

**Key Principles:**
- **Duty to Accommodate to Point of Undue Hardship**: Employers must accommodate needs related to Code-protected grounds (disability, creed, family status, pregnancy, etc.)
- **Undue Hardship Standard**: Higher threshold than US "de minimis" for religion; considers cost, safety, and outside funding sources
- **Interactive Process**: Employer and employee both have responsibilities in accommodation process
- **No Magic Words Required**: You don't need to say "accommodation" - just communicate your need

**Protected Grounds Requiring Accommodation:**
- **Disability**: Physical, mental, learning disabilities; addiction
- **Creed**: Religious beliefs and practices
- **Family Status**: Caregiving responsibilities (protected under *Johnstone v. Canada* framework)
- **Pregnancy**: Includes breastfeeding needs
- **Sex**: Gender-related needs
- **Age**: Age-related limitations

**Key Differences from US:**
- Ontario has broader disability definition (includes addiction)
- Family status accommodation is robust (childcare/eldercare)
- Undue hardship standard requires more than US "de minimis"
- File complaints with Human Rights Tribunal of Ontario (HRTO), not EEOC

**Ontario-Specific Laws:**
- **AODA (Accessibility for Ontarians with Disabilities Act)**: Additional accessibility requirements
- **ESA (Employment Standards Act)**: Job-protected leaves (pregnancy, parental, sick, family responsibility)

**For US users**: Specify `--jurisdiction=US` for ADA, Title VII, FMLA, PWFA frameworks.

## Important Disclaimers

**CRITICAL**: Read these disclaimers ALOUD to the user at session start:

1. **Not Legal Advice**: This guidance is informational, not legal advice. For complex situations involving denied accommodations, retaliation, or discrimination, consult with an employment lawyer or contact Human Rights Legal Support Centre.
2. **Jurisdiction Matters**: This defaults to Ontario law. US law (ADA, Title VII, PDA, PWFA) differs significantly.
3. **No Outcome Guarantees**: While employers are legally required to engage in accommodation process, outcomes depend on specific circumstances.
4. **Documentation**: Keep copies of all accommodation-related communications. BCC personal email where appropriate.
5. **Timing**: Act promptly. Delays can complicate your request and legal protections.


## Argument Parsing

Parse arguments to determine accommodation type and mode:

**Accommodation Type** (mutually exclusive):
- `--disability`: ADA reasonable accommodations (default if no type specified)
- `--religious`: Title VII religious accommodations
- `--medical`: General medical condition accommodations
- `--pregnancy`: Pregnancy-related accommodations (PDA, PWFA)

**Mode**:
- `--appeal`: Focus on responding to denial and escalation options

If no accommodation type specified, default to `--disability` (ADA framework).


## Phase 1: Accommodation Type Assessment

### 1.1 Initial Intake Questions

Ask the user:

1. **"What type of accommodation are you seeking?"**
   - Disability-related (physical, mental, chronic condition)
   - Religious belief or practice
   - Medical condition (temporary or ongoing)
   - Pregnancy-related
   - Not sure which category applies

2. **"Briefly describe the accommodation you need."**
   - Work schedule modification
   - Remote work or work-from-home
   - Modified job duties
   - Physical workspace changes
   - Equipment or technology
   - Leave or time off
   - Policy exception
   - Other

3. **"Have you already requested this accommodation?"**
   - No, preparing initial request
   - Yes, awaiting response
   - Yes, request was denied
   - Yes, but accommodation isn't working

4. **"Does your employer know about your condition/need?"**
   - No, this will be new information
   - Yes, they have general awareness
   - Yes, with documented medical information
   - Uncertain what they know


## Phase 2: Legal Framework Overview

Based on the accommodation type, provide the relevant legal framework:

### 2.1 ADA Framework (--disability)

```
ADA REASONABLE ACCOMMODATION FRAMEWORK
======================================

WHO IS PROTECTED:
- "Qualified individual with a disability"
- Has physical or mental impairment that substantially limits major life activities
- Can perform "essential functions" of the job with or without accommodation
- Includes history of disability or being "regarded as" disabled

EMPLOYER OBLIGATIONS:
- Must provide "reasonable accommodation" unless it causes "undue hardship"
- Must engage in "interactive process" in good faith
- Cannot discriminate based on disability
- Must keep medical information confidential

KEY DEFINITIONS:
- Reasonable Accommodation: Modifications enabling qualified person with disability to perform essential job functions
- Essential Functions: Fundamental job duties (not marginal tasks)
- Undue Hardship: Significant difficulty or expense (employer's burden to prove)
- Interactive Process: Good-faith dialogue between employer and employee to identify effective accommodation

IMPORTANT: You do NOT need to use specific words like "ADA" or "reasonable accommodation" to trigger employer's obligations. Simply communicating that you need a change due to a medical condition is sufficient.
```

### 2.2 Religious Accommodation Framework (--religious)

```
TITLE VII RELIGIOUS ACCOMMODATION FRAMEWORK
===========================================

WHO IS PROTECTED:
- Employees with "sincerely held" religious, ethical, or moral beliefs
- NOT limited to organized religions or traditional beliefs
- Includes moral/ethical beliefs with religious-like importance
- Employer cannot question validity of belief (only sincerity)

EMPLOYER OBLIGATIONS:
- Must reasonably accommodate unless it causes more than "de minimis" cost
- Note: De minimis is LOWER threshold than ADA's "undue hardship"
- Must not discriminate based on religion
- Cannot force employee to choose between job and religious practice

COMMON ACCOMMODATIONS:
- Schedule modifications for religious observance (Sabbath, holidays)
- Dress code exceptions (head coverings, religious attire)
- Grooming policy exceptions (beards, hair length)
- Break time for prayer
- Voluntary shift swaps with coworkers

IMPORTANT: You do NOT need to prove your belief is part of an organized religion. Personal religious or moral convictions can qualify.
```

### 2.3 Medical Accommodation Framework (--medical)

```
MEDICAL ACCOMMODATION FRAMEWORK
===============================

LEGAL PROTECTIONS:
- ADA (if condition qualifies as disability)
- FMLA (for leave-related accommodations)
- State disability laws (often broader than ADA)

TEMPORARY VS. PERMANENT:
- Temporary conditions may qualify for accommodation
- Even short-term impairments can require accommodation
- Post-ADA Amendments Act (2008) broadened coverage significantly

COMMON ACCOMMODATIONS:
- Modified work schedule during treatment/recovery
- Leave for medical appointments
- Remote work during recovery
- Light duty assignments
- Modified break schedules
- Temperature or environmental adjustments

FMLA INTERSECTION:
- 12 weeks unpaid leave for serious health condition
- Intermittent leave may be available
- Job protection during leave
- Separate from ADA reasonable accommodation
```

### 2.4 Pregnancy Accommodation Framework (--pregnancy)

```
PREGNANCY ACCOMMODATION FRAMEWORK
=================================

KEY LAWS:
- Pregnancy Discrimination Act (PDA): Cannot treat pregnancy less favorably than similar conditions
- Pregnant Workers Fairness Act (PWFA, 2023): Requires reasonable accommodation for pregnancy
- FMLA: 12 weeks leave for birth/bonding

PWFA REQUIREMENTS (Effective June 2023):
- Employers with 15+ employees must accommodate "known limitations"
- Covers pregnancy, childbirth, and related medical conditions
- Similar to ADA framework but specifically for pregnancy
- Cannot require leave if another accommodation is available

COMMON ACCOMMODATIONS:
- More frequent breaks
- Modified work schedule
- Light duty or modified duties
- Permission to sit/stand as needed
- Closer parking
- Time for prenatal appointments
- Temporary transfer to less hazardous position
- Leave for recovery as needed

PROTECTION PERIOD:
- Entire pregnancy
- Childbirth and recovery
- Related medical conditions (lactation, postpartum)

IMPORTANT: PWFA explicitly prohibits forcing employees to take leave if another reasonable accommodation exists.
```


## Phase 3: Interactive Process Guide

### 3.1 Initiating the Request

**You do NOT need "magic words"** to request an accommodation. Courts have held that any communication conveying the need for an adjustment due to a condition can trigger employer obligations.

**Ways to initiate:**
- "I need to discuss a change to my work arrangement because of a medical condition."
- "My [condition] is making it difficult to [perform task]. Can we talk about options?"
- "I need [specific accommodation] because of [general reference to condition]."
- Even asking for help or mentioning struggling due to health can suffice

**Recommended approach:**
1. Request in writing (email or letter)
2. Be specific about what you need
3. Connect the need to your condition (without oversharing)
4. Express willingness to discuss alternatives
5. Keep copy for your records

### 3.2 Employer Obligations in Interactive Process

Once you request accommodation, employer MUST:

```
EMPLOYER'S INTERACTIVE PROCESS OBLIGATIONS
==========================================

1. ENGAGE IN GOOD FAITH DIALOGUE
   - Cannot ignore or delay response unreasonably
   - Must discuss your functional limitations
   - Must explore possible accommodations
   - Must explain reasons if declining specific request

2. CONSIDER REASONABLE ALTERNATIVES
   - If your requested accommodation isn't feasible
   - Must work with you to identify alternatives
   - Cannot simply say "no" without exploration

3. TIMELINE EXPECTATIONS
   - No legal deadline, but "prompt" response required
   - Interim accommodations may be appropriate
   - 2-4 weeks for initial response is typical
   - Complex situations may take longer

4. WHAT EMPLOYER CAN DO:
   - Request documentation of condition and need
   - Verify functional limitations
   - Propose alternative accommodations
   - Deny if true undue hardship (must prove it)

5. WHAT EMPLOYER CANNOT DO:
   - Demand complete medical records
   - Ask about diagnosis beyond what's needed
   - Retaliate for requesting accommodation
   - Ignore or refuse to engage
   - Automatically deny based on policy
```

### 3.3 Documentation Requirements

**What employer CAN request:**
- Verification you have a condition requiring accommodation
- Functional limitations caused by condition
- How accommodation would help
- Duration (permanent, temporary, periodic)

**What employer CANNOT demand:**
- Complete medical records
- Specific diagnosis (unless relevant to accommodation)
- Detailed medical history
- Access to treating physician without limits

**Healthcare provider documentation should include:**
1. Confirmation of medical condition (general, not necessarily specific)
2. Functional limitations relevant to job
3. Recommended accommodation(s)
4. Expected duration
5. Provider's contact information

**HIPAA Considerations:**
- Your medical information must be kept confidential
- Employer cannot share with supervisors beyond need-to-know
- Must be stored separately from personnel file
- Violations are reportable

### 3.4 What to Disclose vs. Keep Private

```
DISCLOSURE GUIDANCE
===================

MUST DISCLOSE:
- That you have a condition requiring accommodation
- How the condition affects your ability to perform job functions
- What accommodation(s) you need

SHOULD DISCLOSE (if helpful):
- General nature of condition (e.g., "mobility impairment")
- Permanence or expected duration
- Any limitations on alternative accommodations

MAY KEEP PRIVATE:
- Specific diagnosis (in most cases)
- Cause or origin of condition
- Treatment details
- Prognosis or other conditions
- Personal feelings about condition

STRATEGY: Share the minimum necessary to support your request. You can always provide more information if needed.
```


## Phase 4: Common Accommodation Examples

### 4.1 Disability Accommodations (ADA)

```
COMMON REASONABLE ACCOMMODATIONS
================================

WORK SCHEDULE:
- Modified start/end times
- Part-time or reduced hours
- Additional breaks
- Compressed work week
- Flexible scheduling for appointments

WORK LOCATION:
- Remote work / work from home
- Closer parking space
- First-floor office assignment
- Quieter work area

MODIFIED JOB DUTIES:
- Reassignment of "marginal" (non-essential) functions
- Modified performance standards (with caution)
- Job restructuring
- NOTE: Cannot eliminate "essential" functions

ASSISTIVE TECHNOLOGY:
- Screen readers or magnification
- Speech recognition software
- Ergonomic equipment
- Specialized keyboards/mice
- Hearing aids or amplification devices

PHYSICAL WORKSPACE:
- Accessible workstation
- Standing desk or adjustable furniture
- Improved lighting
- Temperature accommodation
- Reduced noise environment

LEAVE AS ACCOMMODATION:
- Additional unpaid leave beyond FMLA
- Intermittent leave for treatment
- Return-to-work transition period
- Leave for service animal training

POLICY MODIFICATIONS:
- Exception to attendance policy for medical appointments
- Exception to no-food policy for diabetes management
- Modified dress code for medical devices

REASSIGNMENT:
- Transfer to vacant position (if cannot accommodate current role)
- Last resort after other accommodations considered
- Must be qualified for new position
- Not required to create new position or bump other employees
```

### 4.2 Religious Accommodations

```
RELIGIOUS ACCOMMODATION EXAMPLES
================================

SCHEDULING:
- Time off for religious holidays
- Schedule adjustment for Sabbath observance
- Prayer breaks during workday
- Flexible scheduling for religious services

DRESS/GROOMING:
- Hijab, turban, yarmulke, or other head coverings
- Religious jewelry or symbols
- Beard or unshorn hair
- Modest dress requirements

FOOD/DIETARY:
- Break time for religious fasting
- Dietary accommodations at work events
- Exception from food-handling if against beliefs

VOLUNTARY SHIFT SWAPS:
- Trading shifts with willing coworkers
- Employer must facilitate but coworkers not required to swap
```

### 4.3 Pregnancy Accommodations (PWFA)

```
PREGNANCY ACCOMMODATION EXAMPLES
================================

PHYSICAL ACCOMMODATIONS:
- Seating for jobs typically standing
- Closer parking
- Assistance with heavy lifting
- Temperature-controlled environment
- Frequent bathroom breaks

SCHEDULE MODIFICATIONS:
- Time for prenatal appointments
- Modified hours for severe morning sickness
- Gradual return from bedrest
- Lactation breaks and private space

DUTY MODIFICATIONS:
- Temporary transfer from hazardous work
- Light duty assignment
- Removal of specific physical tasks
- Work from home during high-risk period

LEAVE:
- Time off for pregnancy-related conditions
- Recovery time as needed
- Cannot force leave if accommodation available
```


## Phase 5: Request Letter Builder

### 5.1 Request Letter Template

Generate a customized accommodation request letter based on user's inputs:

```markdown
ACCOMMODATION REQUEST LETTER TEMPLATE
=====================================

[Date]

To: [HR Contact / Manager Name]
From: [Your Name]
Re: Request for Workplace Accommodation

Dear [Name],

OPENING (Identify need without oversharing):
I am writing to request a workplace accommodation related to [general description of condition - e.g., "a medical condition," "my religious beliefs," "my pregnancy"]. I am committed to my role at [Company] and believe an accommodation will allow me to continue performing successfully.

SPECIFIC ACCOMMODATION REQUESTED:
I am requesting the following accommodation(s):
1. [Specific accommodation - be clear and concrete]
2. [Additional accommodation if applicable]

HOW THIS ENABLES JOB PERFORMANCE:
This accommodation would enable me to [explain how it addresses the limitation and allows you to perform essential functions]. [If applicable: I have successfully performed these duties with similar accommodations in the past.]

OFFER TO DISCUSS ALTERNATIVES:
I understand that accommodation is an interactive process, and I am open to discussing alternative solutions that would address my needs while meeting the company's operational requirements.

DOCUMENTATION:
[If applicable: I am attaching documentation from my healthcare provider / religious leader supporting this request.]
[Or: I am happy to provide documentation as needed to support this request.]

REQUEST FOR RESPONSE:
I would appreciate confirmation of receipt of this request and a response regarding next steps within [reasonable timeframe - typically 2 weeks]. Please let me know if you need any additional information.

Thank you for your attention to this matter.

Sincerely,
[Your Name]
[Your Position]
[Contact Information]

cc: [Personal email address for your records]
```

### 5.2 Documentation Checklist

```
ACCOMMODATION REQUEST DOCUMENTATION
===================================

BEFORE SUBMITTING:
[ ] Written request (email or letter)
[ ] Specific accommodation(s) identified
[ ] Connection to condition explained (without oversharing)
[ ] Healthcare provider letter (if applicable)
[ ] Copy saved to personal email/records

HEALTHCARE PROVIDER LETTER SHOULD INCLUDE:
[ ] Confirmation of condition requiring accommodation
[ ] Relevant functional limitations
[ ] Recommended accommodation(s)
[ ] Expected duration (permanent/temporary)
[ ] Provider credentials and contact info

AFTER SUBMITTING:
[ ] Note date/time submitted
[ ] Note who received it
[ ] Set reminder to follow up if no response in 2 weeks
[ ] Document any verbal communications
```


## Phase 6: Denial Response (--appeal Mode)

If `--appeal` flag is present or user indicates their request was denied:

### 6.1 Understanding the Denial

Ask the user:

1. **"Did you receive the denial in writing?"**
   - If no: Request written explanation immediately

2. **"What reason was given for the denial?"**
   - Undue hardship claimed
   - Not considered disabled/qualifying condition
   - Requested accommodation not reasonable
   - Essential function issue
   - No reason given
   - Other

3. **"What was the interactive process like?"**
   - They engaged and explored options
   - They went through the motions but seemed predetermined
   - They barely engaged
   - They ignored my request entirely

### 6.2 Challenge Strategies

```
CHALLENGING ACCOMMODATION DENIAL
================================

1. REQUEST WRITTEN EXPLANATION
   "I would like a written explanation of the reasons for denying my accommodation request, including what alternatives were considered."

2. PROPOSE ALTERNATIVES
   If they rejected specific accommodation, propose others:
   - Less costly alternatives
   - Different scheduling approach
   - Temporary trial period
   - Modified version of original request

3. CHALLENGE UNDUE HARDSHIP CLAIM
   Undue hardship is employer's burden to prove. Ask:
   - What specific costs were identified?
   - What impact on operations was calculated?
   - Were all alternatives considered?
   - How does company size factor in?

   Note: Large employers rarely succeed with undue hardship claims.

4. REQUEST CONTINUED DIALOGUE
   "I would like to continue the interactive process to identify an accommodation that works for both of us."

5. ESCALATION PATHS:
   Internal:
   - HR leadership / VP of HR
   - Company disability/accommodation specialist
   - Legal/compliance department
   - Employee assistance program
   - Union representative (if applicable)

   External:
   - EEOC complaint (must file within 180-300 days)
   - State civil rights agency
   - Department of Labor (for FMLA issues)
   - Private employment attorney
```

### 6.3 EEOC Filing Information

```
EEOC COMPLAINT PROCESS
======================

TIMELINE:
- Must file within 180 days of discriminatory act
- Extended to 300 days if state agency handles discrimination
- Don't wait - start early

HOW TO FILE:
1. Contact EEOC: www.eeoc.gov or 1-800-669-4000
2. File online, by mail, or in person at EEOC office
3. EEOC will notify employer
4. Investigation process begins

WHAT HAPPENS NEXT:
- EEOC investigates or offers mediation
- May issue "Right to Sue" letter
- Can file private lawsuit after receiving letter
- EEOC may litigate on your behalf (rare)

STATE AGENCIES:
- Many states have fair employment agencies
- May offer additional protections
- Often work with EEOC

INTERIM ACCOMMODATIONS:
- Request temporary accommodation pending appeal
- Document all hardships from lack of accommodation
- Continue performing to best of ability
```

### 6.4 Appeal Letter Template

```markdown
APPEAL/FOLLOW-UP LETTER TEMPLATE
================================

[Date]

To: [HR / Decision Maker]
From: [Your Name]
Re: Follow-Up on Accommodation Request - [Date of Original Request]

Dear [Name],

I am writing to follow up on my accommodation request dated [date], which was [denied / not yet responded to].

[IF DENIED:]
I received your response indicating that my request for [specific accommodation] was denied due to [stated reason]. I would like to continue the interactive process to identify a reasonable accommodation.

ALTERNATIVE PROPOSALS:
I would like to propose the following alternative accommodation(s):
1. [Alternative 1 - address employer's concerns]
2. [Alternative 2 - different approach]
3. [Alternative 3 - trial period option]

ADDRESSING STATED CONCERNS:
Regarding [employer's concern], I believe [explanation of how alternatives address it, or why concern may be overstated].

[IF UNDUE HARDSHIP CLAIMED:]
I request documentation of the specific costs or operational impacts that support the undue hardship determination, so I can better understand the constraints and propose viable alternatives.

[IF NO RESPONSE:]
I have not received a response to my accommodation request submitted on [date]. I request a status update and timeline for the interactive process to proceed.

CONTINUED COMMITMENT:
I remain committed to finding a solution that allows me to perform my job successfully while addressing any legitimate business concerns.

REQUEST FOR MEETING:
I request a meeting to discuss these alternatives within the next [timeframe]. Please confirm a convenient time.

Sincerely,
[Your Name]

cc: [Personal email]
    [Higher authority if escalating]
```


## Phase 7: Retaliation Protection

### 7.1 What Constitutes Retaliation

```
RETALIATION WARNING SIGNS
=========================

PROTECTED ACTIVITY:
Requesting accommodation is legally protected. Employer CANNOT retaliate for:
- Making an accommodation request
- Providing documentation
- Filing EEOC complaint
- Participating in investigation
- Opposing discriminatory practices

WHAT RETALIATION LOOKS LIKE:
- Sudden negative performance reviews
- Denial of promotion or opportunity
- Reduction in hours or responsibilities
- Hostile treatment from management
- Termination or demotion
- Exclusion from meetings or projects
- Increased scrutiny or micromanagement
- Negative references
- Creating hostile work environment

TIMING MATTERS:
Close proximity between protected activity and adverse action supports retaliation claim. Document everything.
```

### 7.2 Documenting Retaliation

```
RETALIATION DOCUMENTATION PROTOCOL
==================================

DOCUMENT IMMEDIATELY:
- Date and time of incident
- Who was involved
- What was said or done (exact quotes if possible)
- Any witnesses present
- How it relates to your accommodation request

MAINTAIN RECORDS OF:
- All communications about accommodation
- Performance reviews before and after request
- Changes in treatment or assignments
- Any comments about your condition or request
- Comparative treatment of colleagues

PRESERVE EVIDENCE:
- BCC personal email on work communications
- Screenshot relevant messages
- Keep personal copies of performance documents
- Note verbal conversations same day

REPORT RETALIATION:
- To HR in writing
- Reference original accommodation request
- State you believe treatment is retaliatory
- Request investigation
- Copy to personal email
```


## Phase 8: Common Employer Violations

### 8.1 Violations to Watch For

```
COMMON ACCOMMODATION VIOLATIONS
===============================

INTERACTIVE PROCESS FAILURES:
[ ] Ignoring accommodation requests
[ ] Failing to respond in reasonable time
[ ] Going through motions without genuine engagement
[ ] Not exploring alternatives when denying request
[ ] Making decision without discussing with employee

DOCUMENTATION OVERREACH:
[ ] Demanding complete medical records
[ ] Requiring diagnosis when not necessary
[ ] Sharing medical information inappropriately
[ ] Contacting healthcare provider without consent

IMPROPER DENIALS:
[ ] Blanket policies without individualized assessment
[ ] Claiming undue hardship without analysis
[ ] Assuming accommodation won't work without trying
[ ] Denying based on speculation about future limitations

FORCED LEAVE:
[ ] Requiring leave instead of providing accommodation
[ ] Sending employee home without exploring options
[ ] 100% healed policy before return to work
[ ] Treating pregnancy as disability for purposes of exclusion

FAILURE TO MAINTAIN ACCOMMODATION:
[ ] Withdrawing previously granted accommodation
[ ] Not honoring accommodation during reorganization
[ ] New manager refusing to continue accommodation

RETALIATION:
[ ] Adverse action after request
[ ] Creating hostile environment
[ ] Documenting performance issues after request
[ ] Denying opportunities available to others
```

### 8.2 Response Strategies

For each violation type, document and respond appropriately:

1. **Document the violation** with dates, names, specifics
2. **Raise concern in writing** to HR
3. **Reference legal obligation** employer is violating
4. **Request correction** and continued interactive process
5. **Escalate if no response** (EEOC, state agency, attorney)


## Phase 9: Interactive Process Timeline Tracker

### 9.1 Timeline Template

```markdown
ACCOMMODATION REQUEST TIMELINE TRACKER
======================================

REQUEST PHASE:
Date: _________
[ ] Initial request submitted
[ ] Copy saved to personal records
[ ] Acknowledgment received from employer

INTERACTIVE PROCESS:
Date: _________
[ ] Meeting scheduled to discuss
[ ] Meeting held - notes: ________________
[ ] Documentation requested
[ ] Documentation provided
[ ] Alternative accommodations discussed

DECISION PHASE:
Date: _________
[ ] Decision received (written)
[ ] If approved: Accommodation implemented
[ ] If denied: Written explanation received

FOLLOW-UP:
Date: _________
[ ] Appeal submitted (if denied)
[ ] Alternative proposals made
[ ] EEOC contact (if needed)
[ ] Attorney consultation (if needed)

ONGOING:
[ ] Accommodation effectiveness check-in scheduled
[ ] Any changes to accommodation documented
[ ] Retaliation monitoring ongoing
```


## Phase 10: Output Generation

### 10.1 Generate Customized Documents

Based on the user's situation, generate appropriate documents:

**For Initial Request:**
- Customized accommodation request letter
- Documentation checklist
- Timeline tracker (started)

**For Denial/Appeal:**
- Appeal letter or follow-up communication
- Alternative accommodation proposals
- Escalation path recommendation
- EEOC filing information

**For All Cases:**
- Legal framework summary (relevant to their type)
- Rights reminder document
- Documentation guidance

### 10.2 Save Output

Save comprehensive output to: `{config.directories.crisis_management}/accommodation_request_{YYYYMMDD}.md`

Structure:
```markdown
# Workplace Accommodation Request Package
## Type: [Disability/Religious/Medical/Pregnancy]
## Date: [Date]
## Status: [Initial Request / Appeal / In Progress]


## Legal Framework Summary
[Relevant framework based on accommodation type]


## Your Request Documents

### Accommodation Request Letter
[Generated letter]

### Documentation Checklist
[Customized checklist]


## Interactive Process Guide
[Key points for their situation]


## Timeline Tracker
[Pre-populated timeline]


## If Denied: Appeal Resources
[Appeal template and escalation paths]


## Retaliation Protection
[Warning signs and documentation guidance]


## Next Steps
1. [Immediate action]
2. [Follow-up action]
3. [Monitoring action]


## Important Contacts
- Company HR: [To be filled]
- EEOC: 1-800-669-4000 / www.eeoc.gov
- State Agency: [Lookup based on state]
- Employment Attorney: [Consider if complex]
```


## Session Execution

Begin by:
1. Delivering disclaimers
2. Asking initial intake questions (Phase 1)
3. Providing relevant legal framework (Phase 2)
4. Guiding through interactive process (Phase 3)
5. Generating appropriate documents (Phase 9-10)

If `--appeal` flag present:
- Jump to Phase 6 (Denial Response)
- Focus on escalation strategies and appeal documents


Now executing accommodation request assistance...
