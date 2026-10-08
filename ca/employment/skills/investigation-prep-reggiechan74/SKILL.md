---
name: investigation-prep-reggiechan74
title: Workplace Investigation Preparation Report
description: Prepare for workplace HR or third-party investigations
author: reggiechan74
author_url: https://github.com/reggiechan74/JobOps/tree/main/plugins/jobops/skills/investigation-prep
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

This command defaults to **Ontario, Canada** workplace investigation framework.

**Key Ontario Investigation Context:**

- **Bill 168 (Workplace Violence/Harassment)**: Ontario employers must investigate harassment complaints and inform parties of results
- **OHSA Requirements**: Occupational Health and Safety Act mandates investigation of workplace harassment complaints
- **Human Rights Tribunal of Ontario (HRTO)**: External discrimination complaints are handled by HRTO, not internal HR
- **Ministry of Labour**: May investigate OHSA violations, health and safety complaints
- **No Weingarten Rights for Non-Union**: Unlike US union employees, non-unionized Ontario employees have no statutory right to representation during investigative interviews (union employees may have collective agreement protections)

**Ontario Employer Obligations:**
- Must investigate harassment complaints and inform complainant of results
- Must keep investigation confidential to extent possible
- Must not penalize employees for participating in investigations
- Must take appropriate corrective action based on findings

**For US users**: Specify `--jurisdiction=US`. US employees may have Weingarten rights (union), EEOC investigations, and state-specific protections.

## Important Disclaimers

**CRITICAL**: Read these disclaimers ALOUD to the user at session start:

1. **Not Legal Advice**: This guidance is strategic, not legal. For legally complex investigations (potential termination, discrimination claims, serious allegations), recommend consultation with an employment attorney.
2. **Cooperation Balance**: The goal is to protect your rights while cooperating appropriately with legitimate investigations.
3. **Confidentiality Reminder**: Investigation discussions are typically confidential. Be cautious about what you share outside this process.
4. **Documentation**: Keep personal notes of all investigation-related interactions.
5. **No Interference**: Never obstruct an investigation through evidence destruction, witness tampering, or dishonesty.


## Modes of Operation

Parse the role from arguments:
- `--accused`: You are the subject of allegations (default if not specified)
- `--complainant`: You filed the complaint being investigated
- `--witness`: You are being interviewed as a witness

If no mode specified, ask the user their role in the investigation.


## Input Documents

**Argument Handling**:
- If `$ARGUMENTS` contains document paths: Load specified files
- If no documents provided: Ask user what documentation they have

**Accepted Document Types**:
- Investigation notice or summons
- Complaint documents (if provided to you)
- Relevant emails or communications
- Company policies (harassment, code of conduct, etc.)
- Employment contract or handbook
- Prior performance reviews or documentation
- Timeline notes of relevant events


## Phase 1: Investigation Context Assessment

### 1.1 Understanding the Investigation Type

Determine the type of investigation:

```
INVESTIGATION TYPE ASSESSMENT
==============================

TYPE (Ontario):
- [ ] Internal HR Investigation (company HR leads)
- [ ] Third-Party Investigation (external investigator/law firm)
- [ ] Ministry of Labour Investigation (OHSA violations)
- [ ] Human Rights Tribunal of Ontario (HRTO) Application
- [ ] Union Grievance Investigation
- [ ] Ethics Hotline / Compliance Investigation
- [ ] Unknown (help determine based on communications)

TYPE (US - if applicable):
- [ ] EEOC Investigation
- [ ] DOL Investigation
- [ ] State agency investigation

SUBJECT MATTER:
- [ ] Harassment (sexual, discriminatory, bullying)
- [ ] Discrimination claim
- [ ] Policy violation
- [ ] Misconduct allegation
- [ ] Safety or ethics concern
- [ ] Theft or fraud allegation
- [ ] Conflict of interest
- [ ] Retaliation claim
- [ ] Other: [specify]

INVESTIGATION STAGE:
- [ ] Just notified / pre-interview
- [ ] Interview scheduled
- [ ] Interview completed, awaiting outcome
- [ ] Findings delivered, considering response
```

### 1.2 Timeline Assessment

Gather investigation timeline information:

```
INVESTIGATION TIMELINE
======================

Key Dates:
- Date of alleged incident(s): [Date(s)]
- Date complaint filed (if known): [Date]
- Date investigation notice received: [Date]
- Scheduled interview date: [Date]
- Response/appeal deadline (if any): [Date]

Time Constraints:
- Days until interview: [X days]
- Available preparation time: [assessment]
```

### 1.3 Key Players Identification

```
INVESTIGATION PARTICIPANTS
==========================

| Role | Name | Title | Relationship | Notes |
|------|------|-------|--------------|-------|
| Investigator | [Name] | [HR/External/Legal] | [Context] | [Observations] |
| HR Representative | [Name] | [Title] | [Your HR contact] | |
| Other Party | [Name] | [Title] | [Relationship] | |
| Potential Witnesses | [Names] | [Titles] | [What they know] | |
| Your Support Person | [Name] | [Title] | [If applicable] | |
```


## Phase 2: Understanding Your Rights

### 2.1 General Rights During Workplace Investigations

**Rights You Generally Have**:

1. **Right to Know Allegations**: You generally have the right to understand what you're accused of before being expected to respond (specifics vary by jurisdiction and situation)

2. **Right to Respond**: You have the right to tell your side of the story and provide relevant information

3. **Right to Due Process**: Legitimate investigations follow procedures, provide opportunity to respond, and base conclusions on evidence

4. **Right to Be Free from Retaliation**: Participating in an investigation (as complainant, accused, or witness) is protected activity

5. **Right to Privacy (Limited)**: Investigations should be conducted confidentially, though absolute privacy cannot be guaranteed

6. **Right to Review Evidence (Sometimes)**: In some cases, you may request to see evidence against you; this varies significantly

**Rights That Vary by Situation**:

1. **Weingarten Rights (Union Environments)**:
   - Right to union representation during investigatory interviews
   - Must request representation; not automatically provided
   - Applies when you reasonably believe discipline may result
   - Representative can advise but typically cannot answer for you

2. **Right to Representation (Non-Union)**:
   - Generally NO right to attorney during employer investigation
   - Some jurisdictions/situations allow support person
   - Check company policy on support persons
   - Can consult attorney before/after, just not during interview

3. **Right to Silence**:
   - Generally must cooperate with reasonable employer requests
   - Refusing to participate may itself be policy violation
   - Can decline to answer specific questions with explanation
   - Criminal investigation triggers different rights (5th Amendment)

### 2.2 Retaliation Protections

**Protected Activities Include**:
- Filing a good-faith complaint
- Participating in an investigation
- Serving as a witness
- Opposing unlawful practices

**Signs of Potential Retaliation**:
- Adverse action shortly after protected activity
- Change in treatment compared to before
- Negative performance feedback without prior issues
- Exclusion from meetings or opportunities
- Increased scrutiny of work

**If Retaliation Occurs**:
- Document specific incidents with dates and witnesses
- Report through separate HR complaint
- Consult employment attorney if pattern emerges

### 2.3 Confidentiality Expectations

**Typical Employer Expectations**:
- Don't discuss investigation details with coworkers
- Don't contact other witnesses about the case
- Don't share investigation documents

**Your Protections**:
- Can discuss with attorney (privileged)
- Can discuss with spouse (spousal privilege in some contexts)
- Can discuss with union representative
- Cannot be prohibited from discussing wages/working conditions (NLRA)
- Blanket confidentiality mandates may be unlawful

**What to Say If Asked About Investigation**:
> "I've been asked to keep investigation matters confidential. I'm not able to discuss it."


## Phase 3: Pre-Interview Preparation

### 3.1 Document Review and Organization

**Review Relevant Documents**:
- [ ] Investigation notice/summons
- [ ] Applicable company policies
- [ ] Relevant communications (emails, messages)
- [ ] Calendar entries for relevant dates
- [ ] Prior performance documentation
- [ ] Any evidence supporting your position

**Create Personal Timeline**:

```
PERSONAL EVENT TIMELINE
=======================
[Date/Time] - [Event/Action] - [Witnesses] - [Documentation]
[Date/Time] - [Event/Action] - [Witnesses] - [Documentation]
...

Note: Create this timeline as soon as possible while memory is fresh.
Document to personal device/email, not company systems.
```

### 3.2 Identify Supporting Evidence

**Evidence Categories**:

1. **Documentary Evidence**:
   - Emails supporting your account
   - Text messages or chat logs
   - Calendar entries showing whereabouts
   - Work product demonstrating performance
   - Prior communications with relevant parties

2. **Witness Evidence**:
   - Who observed relevant events?
   - Who can speak to your character/work?
   - Who has relevant context?
   - Note: Don't coach witnesses or discuss testimony

3. **Circumstantial Evidence**:
   - Patterns of behavior
   - Prior similar situations and outcomes
   - Inconsistencies in allegations
   - Motive or lack thereof

### 3.3 Prepare Key Talking Points

**Limit to 3-5 Core Points**:

```
KEY TALKING POINTS
==================

1. [Core point #1 - most important fact or context]
   Supporting evidence: [what backs this up]

2. [Core point #2]
   Supporting evidence: [what backs this up]

3. [Core point #3]
   Supporting evidence: [what backs this up]

4. [Optional point #4]

5. [Optional point #5]

PHRASES TO USE:
- "To the best of my recollection..."
- "I can provide documentation showing..."
- "I'd like to clarify..."
- "From my perspective..."

PHRASES TO AVOID:
- "I would never..."
- "They're lying..."
- "Everyone knows..."
- "I don't remember anything" (if you do remember)
```

### 3.4 Anticipate Questions

**Common Investigation Questions**:

*General/Opening Questions*:
- "Tell me about your role and responsibilities."
- "Describe your working relationship with [person]."
- "Walk me through what happened on [date]."

*Specific Incident Questions*:
- "What did you observe/hear/say?"
- "Where were you at [time]?"
- "Who else was present?"
- "What happened before/after the incident?"

*Follow-up and Clarification*:
- "Can you be more specific about...?"
- "How do you explain [contradictory evidence]?"
- "Is there anything you'd like to add?"
- "Is there anyone else I should speak with?"

*Potentially Difficult Questions*:
- Prepare responses that are honest without being harmful
- Identify questions that require careful answers
- Know when to say "I need to think about that" or "I'm not comfortable answering without more context"

### 3.5 Logistics Preparation

**Pre-Interview Checklist**:
- [ ] Confirm interview date, time, location
- [ ] Ask who will be present
- [ ] Request agenda or topics if not provided
- [ ] Understand estimated duration
- [ ] Clarify if recording is permitted (and by whom)
- [ ] Confirm whether support person is allowed
- [ ] Plan arrival time (early but not excessively)
- [ ] Prepare professional attire
- [ ] Arrange coverage for your work

**What to Bring**:
- [ ] Government ID (if required)
- [ ] Notepad and pen for notes (ask if permitted)
- [ ] Timeline you've prepared (for your reference)
- [ ] Copies of relevant documents (if sharing)
- [ ] Contact information for support resources


## Phase 4: Interview Strategies

### 4.1 General Interview Conduct

**DO**:
- Listen carefully to each question completely before answering
- Answer only the specific question asked
- Ask for clarification if a question is unclear
- Take your time before responding
- Stay calm and professional throughout
- Maintain appropriate eye contact
- Speak clearly and at measured pace
- Tell the truth consistently

**DON'T**:
- Interrupt the investigator
- Volunteer information beyond what's asked
- Speculate or guess about things you don't know
- Get defensive or emotional
- Make accusations about others' motives
- Use absolute language ("never," "always")
- Provide hearsay as fact
- Feel pressured to fill silence

### 4.2 Responding to Difficult Questions

**When You Don't Remember**:
> "I don't recall the specific details of that conversation. I can tell you what I generally remember, but I want to be accurate rather than guess."

**When You Need Time**:
> "That's a detailed question. Can I take a moment to think about it to give you an accurate answer?"

**When a Question is Unclear**:
> "I want to make sure I understand. Are you asking about [specific interpretation]?"

**When Asked to Speculate**:
> "I can only speak to what I personally observed or know directly. I wouldn't want to speculate about [other person's motives/actions]."

**When Asked About Others' Statements**:
> "I can't speak to what [person] said or meant. I can only tell you what I observed or experienced."

**When Confronted with Contradictory Evidence**:
> "I understand there may be different accounts. What I can tell you is what I personally experienced/observed..."

### 4.3 Note-Taking During Interview

**If Note-Taking is Permitted**:
- Note key questions asked
- Note any commitments or follow-ups mentioned
- Note names of people referenced
- Note documents or evidence mentioned
- Note anything that surprises you

**Immediately After Interview**:
- Complete detailed notes while fresh
- Document questions asked and your answers
- Note investigator's demeanor and reactions
- Record any concerns about the process
- Save to personal device/email

### 4.4 Knowing When to Pause

**Acceptable Requests**:
- "May I take a short break?"
- "I'd like to consult with my attorney before answering that."
- "I need a moment to collect my thoughts."
- "Can we revisit that question later in the interview?"
- "I'd like to provide that information in writing after I review my records."

**When to Consider Stopping**:
- If you feel you're being treated unfairly
- If questions seem designed to entrap rather than fact-find
- If you need legal advice before proceeding
- If you're too upset to continue professionally


## Phase 5: What NOT to Do

### 5.1 Critical Prohibitions

**Never Lie**:
- Dishonesty during investigation can be separate terminable offense
- Lies can turn a defensible situation into indefensible one
- Inconsistencies will be discovered
- Credibility is your most important asset

**Never Destroy Evidence**:
- Document destruction can be crime (obstruction)
- Creates inference of guilt even if underlying matter is defensible
- Electronic evidence is often recoverable
- Very serious legal and employment consequences

**Never Contact the Other Party Directly**:
- Can be perceived as intimidation or witness tampering
- May violate company policy or protective orders
- Creates additional incidents for investigation
- Document if they contact you (don't engage)

**Never Discuss with Other Witnesses**:
- Can appear as coordination/coaching
- May contaminate their recollection
- Can lead to obstruction allegations
- Investigators compare accounts for consistency

**Never Retaliate**:
- Retaliation is independently unlawful
- Creates additional claims against you
- Demonstrates consciousness of guilt
- Damages your position significantly

### 5.2 Common Mistakes to Avoid

**Don't Resign in Panic**:
- Resignation is often permanent
- May forfeit severance or unemployment benefits
- Appears as admission of guilt
- Removes leverage for negotiation
- Consult attorney before making this decision

**Don't Admit to Things You Didn't Do**:
- Pressure during investigation can lead to false admissions
- Take time to think before responding
- Distinguish between apologizing for impact vs. admitting fault
- "I'm sorry you felt that way" is different from "I did that"

**Don't Assume Worst Outcome**:
- Many investigations don't result in termination
- Due process exists for a reason
- Your perspective matters
- Wait for actual outcome before reacting

**Don't Ignore the Investigation**:
- Failure to cooperate can be policy violation
- Creates negative inference
- Forfeits opportunity to provide your side
- May accelerate adverse outcome


## Phase 6: Mode-Specific Guidance

### 6.1 If You Are the Accused (--accused)

**Your Priority**: Provide truthful account while protecting your rights and reputation.

**Specific Preparation**:

1. **Understand the Specific Allegations**:
   - Request clarification if notice is vague
   - Ask: "What specifically am I accused of doing?"
   - Understand dates, locations, and nature of claims
   - Identify what policy allegedly violated

2. **Prepare Your Defense**:
   ```
   DEFENSE PREPARATION
   ===================

   Allegation: [What you're accused of]
   Your Account: [What actually happened]
   Supporting Evidence: [What proves your account]
   Witnesses: [Who can corroborate]
   Alternative Explanation: [If applicable]
   Context Missing: [What investigator needs to know]
   ```

3. **Consider Representation**:
   - Consult employment attorney before interview if serious allegations
   - In union environment, exercise Weingarten rights
   - Ask about support person if non-union
   - Attorney can help prepare even if not present at interview

4. **Prepare for Possible Outcomes**:
   - Exoneration
   - Inconclusive finding
   - Partial responsibility
   - Disciplinary action
   - Termination
   - Have response plan for each scenario

5. **Document Your Version Contemporaneously**:
   - Write detailed account while memory is fresh
   - Include dates, times, witnesses, exact words
   - Save to personal device/email
   - Don't share with coworkers

### 6.2 If You Are the Complainant (--complainant)

**Your Priority**: Ensure thorough investigation while maintaining professionalism and documenting retaliation.

**Specific Preparation**:

1. **Organize Evidence Chronologically**:
   ```
   COMPLAINT EVIDENCE ORGANIZATION
   ===============================

   Incident 1:
   - Date/Time: [specific]
   - Location: [where it occurred]
   - What happened: [factual account]
   - Witnesses: [who was present]
   - Documentation: [emails, messages, notes]
   - Impact: [how it affected your work]

   Incident 2:
   [Repeat structure]
   ```

2. **Prepare Witness List**:
   - Who observed the behavior?
   - Who did you report to or confide in?
   - Who else may have experienced similar treatment?
   - Who can speak to impact on your work?

3. **Document Work Impact**:
   - How has this affected your job performance?
   - Have you missed work or opportunities?
   - Impact on your health or wellbeing?
   - Changes in how you're treated since complaining?

4. **Track Retaliation**:
   - Document any changes in treatment after filing
   - Note exclusions from meetings, projects, information
   - Record negative feedback or increased scrutiny
   - Save evidence of differential treatment
   - Report retaliation separately if it occurs

5. **Appropriate Follow-Up**:
   - Request timeline for investigation completion
   - Ask how you'll be informed of outcome
   - Inquire about interim protective measures
   - Document all follow-up in writing

### 6.3 If You Are a Witness (--witness)

**Your Priority**: Tell the truth about what you personally observed while maintaining neutrality.

**Specific Guidance**:

1. **Tell the Truth**:
   - Your only obligation is honesty
   - Don't embellish or minimize
   - Distinguish observation from inference
   - Acknowledge uncertainty where it exists

2. **Share Only What You Personally Observed**:
   - "I saw..." or "I heard..." (direct observation)
   - "I was told..." (hearsay - identify source)
   - "My impression was..." (clearly labeled as opinion)
   - Avoid: "Everyone knows..." or "It's common knowledge..."

3. **Don't Take Sides Publicly**:
   - Avoid discussing with either party
   - Don't share opinions about guilt or innocence
   - Maintain professional relationships with all parties
   - Don't become advocate for either side

4. **Maintain Confidentiality**:
   - Don't discuss interview with coworkers
   - Don't share what questions were asked
   - Don't speculate about investigation status
   - If pressured by either party, report to HR

5. **Document Your Participation**:
   - Note what you were asked and what you said
   - Save for your records
   - Document any pressure from either party
   - Report attempts to influence your testimony


## Phase 7: Post-Interview Actions

### 7.1 Immediate Post-Interview Tasks

**Same Day**:
- [ ] Complete detailed notes of interview
- [ ] Document all questions asked
- [ ] Record your answers as you remember them
- [ ] Note any concerning moments or red flags
- [ ] Save to personal device/email (not company systems)
- [ ] Send follow-up email if appropriate (see template below)

**Post-Interview Follow-Up Email Template**:
```
Subject: Follow-Up to Investigation Interview - [Date]

Dear [Investigator Name],

Thank you for meeting with me today regarding the [investigation/matter]. I appreciate the opportunity to provide my perspective.

As discussed, I will [any commitments you made, e.g., provide additional documentation].

I want to ensure my account was clear. To summarize the key points I made:
- [Key point 1]
- [Key point 2]
- [Key point 3]

If I can provide any additional information or clarification, please let me know.

[If applicable: I also want to note my concern about [specific process issue], which I mentioned during our meeting.]

Please confirm the expected timeline for next steps.

Regards,
[Your Name]
```

### 7.2 Monitoring for Process Concerns

**Document Any Issues**:
- Questions that seemed leading or unfair
- Evidence presented that was taken out of context
- Relevant witnesses who were not interviewed
- Evidence you provided that was dismissed
- Apparent bias in investigator's approach
- Confidentiality breaches

**Raise Concerns Appropriately**:
- If internal HR investigation: raise with HR leadership
- If external investigator: raise with contracting company representative
- Document concerns in writing
- Consider consulting employment attorney

### 7.3 Documenting Potential Retaliation

**Retaliation Documentation Template**:
```
RETALIATION INCIDENT LOG
========================

Date: [Date]
Time: [Time]
Location: [Location]

What Happened:
[Detailed description of adverse action or change in treatment]

Who Was Involved:
[Names and titles]

Witnesses:
[Names of anyone who observed]

Documentation:
[Emails, messages, or other evidence]

Connection to Investigation:
[Why you believe this is related to investigation participation]

Prior Baseline:
[How things were before to demonstrate change]

Impact:
[How this affects your work or employment]
```


## Phase 8: Responding to Investigation Findings

### 8.1 Understanding the Outcome

**Possible Findings**:
- Sustained (allegations proven)
- Not Sustained (insufficient evidence either way)
- Unfounded (allegations disproven)
- Policy Violation Found (technical violation, perhaps not as alleged)
- No Policy Violation

**What You Should Receive**:
- Written notice of findings
- Explanation of basis for conclusion (level of detail varies)
- Information about consequences (if any)
- Information about appeal rights (if any)
- Timeline for any required actions

### 8.2 Appeal Rights and Process

**Check Policy for**:
- Right to appeal adverse findings
- Deadline for filing appeal
- Appeal process and decision-maker
- What new evidence or arguments can be raised
- Whether you can have representation in appeal

**Appeal Preparation**:
```
APPEAL CONSIDERATIONS
=====================

Grounds for Appeal:
- [ ] New evidence not previously available
- [ ] Procedural errors in investigation
- [ ] Witnesses not interviewed
- [ ] Evidence mischaracterized or ignored
- [ ] Findings not supported by evidence
- [ ] Punishment disproportionate
- [ ] Inconsistent treatment vs. similar cases

Supporting Evidence:
[List specific evidence for each ground]

Requested Remedy:
[What outcome you're seeking]
```

### 8.3 Written Rebuttal Preparation

**If You Disagree with Findings**:
- Request to submit written rebuttal for personnel file
- Some jurisdictions provide this right by law
- Professional, factual, non-emotional tone
- Focus on facts, not attacking investigator

**Rebuttal Structure**:
```
REBUTTAL TO INVESTIGATION FINDINGS

Date: [Date]
Re: [Investigation reference number/description]

I respectfully submit this rebuttal to the findings dated [date] regarding [matter].

FACTUAL CORRECTIONS:
1. [Specific finding that is incorrect]
   Correction: [What actually occurred, with evidence]

2. [Repeat for each error]

PROCEDURAL CONCERNS:
[If applicable - witnesses not interviewed, evidence ignored, etc.]

CONCLUSION:
I maintain that [your position]. The evidence demonstrates [key point]. I request that this rebuttal be included in my personnel file alongside the investigation findings.

[Signature]
```

### 8.4 When to Escalate to Legal Counsel

**Consider Legal Consultation When**:
- Termination is likely or occurred
- You believe findings are fundamentally wrong
- Process was clearly biased or unfair
- Protected class discrimination is factor
- Retaliation for protected activity
- Significant financial or career consequences
- You're asked to sign agreements or releases

**What Employment Attorneys Evaluate**:
- Procedural fairness of investigation
- Whether findings are supported by evidence
- Discrimination or retaliation indicators
- Wrongful termination potential
- Severance negotiation leverage
- Defamation or reputation issues


## Phase 9: Output Deliverables

### 9.1 Investigation Preparation Report

Save comprehensive preparation guide to: `{config.directories.crisis_management}/investigation_prep_{YYYYMMDD}.md`

**Report Structure**:
```markdown
# Workplace Investigation Preparation Report
## Date: [Date]
## Role: [Accused/Complainant/Witness]
## Investigation Type: [Description]


## Executive Summary
[2-3 sentence summary of situation and preparation status]


## Investigation Context
- Type: [Internal HR/External/Legal/Other]
- Subject: [Description of matter]
- Status: [Pre-interview/Post-interview/Awaiting findings]
- Key Dates: [Timeline]
- Key Players: [Summary]


## Your Rights Summary
- [Key rights applicable to this situation]
- [Representation options]
- [Confidentiality obligations]


## Pre-Interview Preparation

### Personal Timeline
[Your chronological account of events]

### Key Talking Points
1. [Point 1]
2. [Point 2]
3. [Point 3]

### Supporting Evidence
[Evidence you have or can obtain]

### Anticipated Questions
[Questions to prepare for with guidance]


## Interview Strategy
- [Key dos and don'ts for your situation]
- [Specific responses to prepare]
- [When to pause or seek clarification]


## Post-Interview Checklist
- [ ] Complete interview notes
- [ ] Send follow-up email
- [ ] Monitor for retaliation
- [ ] Document any concerns


## Potential Outcomes & Response Plans
[For each likely outcome, what to consider]


## Escalation Triggers
[When to consult employment attorney]


## Appendix
### Retaliation Documentation Template
### Appeal/Rebuttal Templates
### Follow-up Email Templates
```

### 9.2 Role-Specific Checklists

**Accused Pre-Interview Checklist**:
```markdown
## Accused Party Preparation Checklist

UNDERSTANDING ALLEGATIONS:
- [ ] Received written notice of investigation
- [ ] Understand specific allegations against you
- [ ] Know which policies allegedly violated
- [ ] Identified relevant dates and incidents

EVIDENCE GATHERING:
- [ ] Created personal timeline of events
- [ ] Gathered supporting emails/documents
- [ ] Identified potential witnesses
- [ ] Saved relevant communications to personal device

PREPARATION:
- [ ] Prepared 3-5 key talking points
- [ ] Anticipated difficult questions
- [ ] Consulted with attorney (if appropriate)
- [ ] Requested support person (if available)

LOGISTICS:
- [ ] Confirmed interview date/time/location
- [ ] Know who will be present
- [ ] Prepared professional attire
- [ ] Arranged work coverage

MINDSET:
- [ ] Reviewed dos and don'ts
- [ ] Prepared to stay calm
- [ ] Ready to tell the truth
- [ ] Understand it's OK to say "I don't recall"
```

**Complainant Pre-Interview Checklist**:
```markdown
## Complainant Preparation Checklist

EVIDENCE ORGANIZATION:
- [ ] Documented all incidents chronologically
- [ ] Gathered supporting communications
- [ ] Identified witnesses for each incident
- [ ] Documented impact on work

PREPARATION:
- [ ] Prepared to describe each incident specifically
- [ ] Ready to explain why you found behavior problematic
- [ ] Documented any interim measures requested
- [ ] Set up retaliation monitoring system

INTERVIEW READINESS:
- [ ] Can speak calmly about difficult events
- [ ] Prepared for questions about your own conduct
- [ ] Ready to suggest additional witnesses
- [ ] Know to document any retaliation
```

**Witness Pre-Interview Checklist**:
```markdown
## Witness Preparation Checklist

RECALL:
- [ ] Reviewed what you personally observed
- [ ] Separated observation from inference
- [ ] Identified gaps in your knowledge
- [ ] Prepared to say "I don't know" when true

NEUTRALITY:
- [ ] Not discussed testimony with either party
- [ ] Avoided expressing opinions on outcome
- [ ] Prepared to report any pressure
- [ ] Maintaining professional relationships

DOCUMENTATION:
- [ ] Personal notes of what you observed
- [ ] Understanding of confidentiality expectations
- [ ] Plan to document interview afterward
```


## Quality Checks

Ensure the preparation guide:
- [ ] Addresses specific role (accused/complainant/witness)
- [ ] Provides actionable checklists
- [ ] Includes realistic preparation strategies
- [ ] Covers rights and limitations appropriately
- [ ] Prepares for likely interview scenarios
- [ ] Includes post-interview documentation templates
- [ ] Identifies when legal counsel is advisable
- [ ] Maintains balance between protection and cooperation
- [ ] Uses professional, non-inflammatory language
- [ ] Does not encourage obstruction or dishonesty


## Tone Guidelines

Throughout this process, maintain:

- **Protective but not paranoid**: Help user protect rights without creating adversarial mindset
- **Honest about limitations**: Clear that this is not legal advice
- **Empowering**: Focus on what user CAN control in difficult situation
- **Process-oriented**: Investigations follow procedures; understanding them helps
- **Professional**: Model the demeanor expected in investigation
- **Balanced**: Cooperation is generally expected; protection is also important


## Session Start

Begin by:
1. Delivering the disclaimers
2. Determining user's role (--accused, --complainant, --witness)
3. Loading any provided documents
4. Gathering investigation context (type, stage, timeline)
5. Walking through relevant preparation phases
6. Generating appropriate output documents

If the user has an interview scheduled soon, prioritize immediate preparation needs over comprehensive background.


Now proceeding with investigation preparation...
