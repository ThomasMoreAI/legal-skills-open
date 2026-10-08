---
name: workplace-documentation-reggiechan74
title: Incident Report
description: Build organized documentation of workplace incidents and issues
author: reggiechan74
author_url: https://github.com/reggiechan74/JobOps/tree/main/plugins/jobops/skills/workplace-documentation
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

This command defaults to **Ontario, Canada** employment law framework. Key considerations:

- **Human Rights Code**: Ontario Human Rights Code provides broad protections against discrimination and harassment in employment
- **Occupational Health and Safety Act**: OHSA protects workers who report health and safety concerns from reprisal
- **ESA Job-Protected Leaves**: Employment Standards Act provides various job-protected leaves (pregnancy, parental, sick, family medical, etc.)
- **Recording Consent**: Ontario is a one-party consent jurisdiction for audio/video recording (you can record conversations you're part of)
- **Privacy**: Personal Information Protection laws govern workplace information handling

**For US users**: Specify `--jurisdiction=US` or mention your state. US laws differ (Title VII, FMLA, state-specific recording laws).

## Important Disclaimers

**CRITICAL**: Read these disclaimers ALOUD to the user at session start:

1. **Not Legal Advice**: This documentation guidance is strategic, not legal. For legally complex situations (discrimination, harassment, retaliation), recommend consultation with an employment attorney.
2. **Documentation Timing Matters**: Courts and HR departments give more weight to contemporaneous documentation (written at or near the time of the incident). Document incidents as soon as possible.
3. **Personal Security**: Store documentation on personal devices and accounts, not work systems. Employers may monitor work devices and accounts.
4. **Evidence Rules**: What you can legally retain varies by jurisdiction. Generally, personal notes about your experiences are yours. Be cautious about copying company proprietary information.
5. **No Outcome Guarantees**: Thorough documentation improves your position but cannot guarantee outcomes.


## Modes of Operation

Parse the mode from arguments:
- `--new-incident` (default): Document a new incident using guided interview
- `--review`: Assess quality and completeness of existing documentation
- `--timeline`: Generate visual timeline and pattern analysis from incident log

If no mode specified, default to `--new-incident`.


## Input Handling

**Argument Handling**:
- If `$1` contains a mode flag, parse mode
- If `$2` is provided: Load specified incident log file for review or timeline generation
- If no file provided for `--review` or `--timeline`: Ask user which log file to analyze

**Accepted Input Types**:
- Existing incident logs (markdown files)
- Previous documentation exports
- Notes or drafts to be formalized

**Default Output Location**:

All modes write to a single continuously-updated log file:
`{config.directories.crisis_management}/workplace_documentation_log.md`

## Output mode: APPEND (continuously-updated log)

This skill maintains ONE log file per workspace. Every invocation — new incident,
timeline update, evidence indexing, or review — APPENDS a new entry to the same
file. Existing content is preserved.

**Append contract:**
- Read existing `workplace_documentation_log.md` if present.
- Add a new section at the end of the file with a timestamp header, for example:
  `## [YYYY-MM-DD HH:MM] <mode>: <short label>` (e.g. `## [2026-04-23 09:14] new-incident: Retaliation after accommodation request`)
- Preserve all prior entries verbatim. Never rewrite or truncate earlier sections.
- If the file does not exist, create it with a top-level heading
  (`# Workplace Documentation Log`) followed by the first entry.
- Incident logs, timelines, and evidence indices are all appended as dated
  sections inside the same log — not written to separate files.


## Mode 1: New Incident Documentation (--new-incident)

### 1.1 Incident Intake Interview

**CRITICAL**: Conduct this interview systematically. Use conversational questions to gather complete information before documenting.

#### Basic Incident Information

Ask the user:

1. **"What date and time did this incident occur? Be as specific as possible."**
   - Date (required)
   - Time of day (specific if known, or morning/afternoon/evening)
   - Duration of incident if applicable

2. **"Where did this incident take place?"**
   - Physical location (office building, floor, room)
   - Virtual location (video call platform, chat channel)
   - Public vs. private setting
   - Was this a scheduled meeting or impromptu encounter?

3. **"Who was directly involved in this incident?"**
   - Names and titles of all participants
   - Role of each person (perpetrator, target, bystander)
   - Reporting relationships (manager, peer, subordinate, HR)

4. **"Were there any witnesses? Include anyone who might have seen or heard what happened."**
   - Names and titles
   - Contact information if known
   - Their relationship to involved parties
   - Whether they are likely to cooperate

#### Incident Details

5. **"Describe what happened in factual terms. Start from the beginning and walk me through the sequence of events."**

   Probe for:
   - Triggering event (what started it?)
   - Sequence of actions
   - Physical actions or gestures
   - Tone of voice, body language
   - How the incident ended

6. **"What was said? Please recall as many exact quotes as possible."**

   Prompt the user:
   - "Who said what first?"
   - "What exact words were used?"
   - "Was anything repeated or emphasized?"
   - "Were there any threatening, discriminatory, or demeaning statements?"
   - Use quotation marks for verbatim quotes
   - Use "approximately" or "words to the effect of" for paraphrasing

7. **"How did you respond during the incident?"**
   - What you said
   - What you did
   - What you didn't say or do (and why)

8. **"How did this incident make you feel?"**

   Note: Emotional impact is relevant for harassment and hostile work environment claims.
   - Immediate emotional response
   - Ongoing emotional effects
   - Impact on work performance or comfort
   - Physical symptoms (anxiety, sleep issues, etc.)

#### Evidence Collection

9. **"Do you have any physical evidence of this incident?"**

   Inventory by type:
   - Emails (before, during, or after incident)
   - Text messages or chat logs
   - Calendar invitations
   - Documents or memos
   - Screenshots
   - Audio or video recordings (note: legality varies by jurisdiction)
   - Physical objects
   - Photographs

10. **"What follow-up actions have been taken since the incident?"**
    - Did you report to HR or management?
    - Were there any conversations about the incident afterward?
    - Any written acknowledgment or response?
    - Any changes in behavior or treatment since?
    - Any retaliation concerns?

#### Context Questions

11. **"Is this part of a pattern, or a first-time occurrence?"**
    - Similar previous incidents with same person?
    - Similar incidents with different people?
    - First time this specific behavior occurred?

12. **"Have you observed similar treatment of others?"**
    - Colleagues experiencing similar issues?
    - Witnesses to patterns?
    - Comparators (people in similar situations treated differently)?

13. **"Did this incident occur after any protected activity?"**

    Protected activities include (Ontario):
    - Filing a complaint (internal, Human Rights Tribunal, Ministry of Labour)
    - Reporting safety violations (OHSA protected)
    - Requesting accommodation (Human Rights Code)
    - Taking job-protected leave (ESA: pregnancy, parental, sick, family medical, etc.)
    - Participating in workplace investigation
    - Refusing unsafe work (OHSA protected)

    **US protected activities**: FMLA leave, EEOC complaints, OSHA reports, whistleblower activities

### 1.2 Incident Documentation Template

After completing the interview, generate a formal incident record:

```markdown
# Incident Report

## Incident Metadata
| Field | Value |
|-------|-------|
| Incident ID | [Auto-generated: YYYY-MM-DD-001] |
| Date Documented | [Today's date] |
| Date of Incident | [Date] |
| Time of Incident | [Time or approximate time] |
| Location | [Physical/Virtual location] |
| Incident Type | [Harassment/Discrimination/Retaliation/Policy Violation/Other] |
| Document Status | Contemporaneous / Reconstructed (if >24 hours later) |


## Parties Involved

### Subject (Target of Incident)
- **Name**: [Your name]
- **Title/Position**: [Your role]
- **Department**: [Your department]

### Involved Parties
| Name | Title | Role in Incident | Relationship to Subject |
|------|-------|------------------|-------------------------|
| [Name] | [Title] | [Perpetrator/Participant] | [Manager/Peer/etc.] |

### Witnesses
| Name | Title | Contact Info | Cooperation Likelihood |
|------|-------|--------------|------------------------|
| [Name] | [Title] | [If known] | [Likely/Unknown/Unlikely] |


## Incident Description

### What Happened (Factual Account)
[Detailed, chronological description of events using factual language]

### Exact Quotes
> "[Verbatim quote 1]" - [Speaker Name]

> "[Verbatim quote 2]" - [Speaker Name]

*Note: Quotes marked with [approximate] are paraphrased to the best of recollection.*

### Your Response
[How you responded during the incident]

### Emotional Impact
[How the incident made you feel and any ongoing effects]


## Evidence Inventory

### Available Evidence
| Evidence Type | Description | Location | Date Obtained |
|---------------|-------------|----------|---------------|
| [Email/Screenshot/etc.] | [Brief description] | [File path or storage] | [Date] |

### Evidence Needed
| Evidence Type | Why Needed | How to Obtain | Status |
|---------------|-----------|---------------|--------|
| [Type] | [Relevance] | [Method] | [Pending/In Progress] |


## Context & Pattern

### Related Incidents
| Date | Brief Description | Linked Record |
|------|-------------------|---------------|
| [Date] | [Summary] | [Link if applicable] |

### Protected Activity Timeline
| Date | Activity | Relevance |
|------|----------|-----------|
| [Date] | [Complaint/Leave/etc.] | [Connection to incident] |


## Follow-Up Actions

### Actions Taken
| Date | Action | Outcome |
|------|--------|---------|
| [Date] | [Reported to HR/Spoke with manager/etc.] | [Response received] |

### Next Steps
- [ ] [Action item 1]
- [ ] [Action item 2]


## Documentation Certification
This document was prepared on [Date] at [Time] documenting events that occurred on [Incident Date]. [I certify this is a true and accurate account to the best of my recollection / This account was reconstructed from memory approximately X days after the incident.]


*Document ID: [Auto-generated]*
*Last Modified: [Timestamp]*
*Part of Incident Log: [Log filename]*
```

### 1.3 Documentation Best Practices Checklist

After generating the incident record, verify:

```
DOCUMENTATION QUALITY CHECKLIST
================================

TIMING:
- [ ] Documented within 24 hours of incident (contemporaneous)
- [ ] If reconstructed, noted as such with approximate delay

SPECIFICITY:
- [ ] Specific date and time (not "sometime last week")
- [ ] Specific location (not "at work")
- [ ] Specific names and titles (not "my manager")
- [ ] Exact quotes where possible (with quotation marks)
- [ ] Paraphrases clearly marked as approximate

OBJECTIVITY:
- [ ] Facts separated from opinions
- [ ] Observations separated from interpretations
- [ ] Avoided editorializing ("he rudely said" vs "he said in a raised voice")
- [ ] Documented what you SAW vs what you HEARD vs what you ASSUMED

COMPLETENESS:
- [ ] All parties identified with names and roles
- [ ] Witnesses documented even if uncooperative
- [ ] Evidence inventory created
- [ ] Follow-up actions recorded
- [ ] Emotional impact documented (relevant for some claims)

SECURITY:
- [ ] Saved to personal device/account
- [ ] Not stored on work systems
- [ ] Backup copy created
- [ ] Access limited to yourself (and attorney if applicable)
```


## Mode 2: Documentation Review (--review)

### 2.1 Load Existing Documentation

@$2

Read and analyze the provided incident log file.

### 2.2 Quality Assessment Framework

Evaluate documentation strength across these dimensions:

```
DOCUMENTATION STRENGTH ASSESSMENT
=================================

OVERALL RATING: [Strong / Medium / Weak]

DIMENSION ANALYSIS:

1. CONTEMPORANEITY (Weight: 25%)
   Rating: [Strong/Medium/Weak]
   - % of entries within 24 hours: [X%]
   - % reconstructed: [X%]
   - Longest gap between incident and documentation: [X days]
   - Recommendation: [Specific improvement]

2. SPECIFICITY (Weight: 25%)
   Rating: [Strong/Medium/Weak]
   - Specific dates/times: [Yes/Partial/No]
   - Named individuals: [Yes/Partial/No]
   - Exact quotes documented: [Yes/Partial/No]
   - Locations specified: [Yes/Partial/No]
   - Recommendation: [Specific improvement]

3. OBJECTIVITY (Weight: 20%)
   Rating: [Strong/Medium/Weak]
   - Facts vs opinions separated: [Yes/Partial/No]
   - Editorializing present: [None/Some/Significant]
   - Clear attribution (saw/heard/inferred): [Yes/Partial/No]
   - Recommendation: [Specific improvement]

4. EVIDENCE SUPPORT (Weight: 15%)
   Rating: [Strong/Medium/Weak]
   - Evidence inventory complete: [Yes/Partial/No]
   - Corroborating documents identified: [Yes/Partial/No]
   - Witness information documented: [Yes/Partial/No]
   - Evidence gaps identified: [Yes/Partial/No]
   - Recommendation: [Specific improvement]

5. PATTERN DOCUMENTATION (Weight: 15%)
   Rating: [Strong/Medium/Weak]
   - Incidents linked thematically: [Yes/Partial/No]
   - Comparators identified: [Yes/Partial/No]
   - Protected activity timeline: [Yes/Partial/No]
   - Escalation pattern visible: [Yes/Partial/No]
   - Recommendation: [Specific improvement]

CRITICAL GAPS IDENTIFIED:
- [ ] [Gap 1 with specific recommendation]
- [ ] [Gap 2 with specific recommendation]
- [ ] [Gap 3 with specific recommendation]

ADDITIONAL DOCUMENTATION NEEDED:
- [ ] [Specific documentation to add]
- [ ] [Evidence to gather]
- [ ] [Witnesses to contact]
```

### 2.3 Improvement Recommendations

For each identified weakness, provide:

1. **What's Missing**: Specific gap in documentation
2. **Why It Matters**: Legal or strategic significance
3. **How to Fix**: Concrete action to address
4. **Priority**: Critical/High/Medium/Low


## Mode 3: Timeline Generation (--timeline)

### 3.1 Load and Parse Incident Log

@$2

Read the incident log and extract all incidents.

### 3.2 Generate Visual Timeline

Create a text-based timeline visualization:

```markdown
# Incident Timeline
## [Company Name] - [Date Range]

===== TIMELINE =====

[YEAR 1]
|
|-- [DATE 1] ----------------------------------------
|   INCIDENT: [Brief title]
|   Type: [Harassment/Discrimination/Retaliation/etc.]
|   Parties: [Names]
|   Severity: [High/Medium/Low]
|   Evidence: [Strong/Medium/Weak]
|   → [Key detail or quote]
|
|-- [DATE 2] ----------------------------------------
|   PROTECTED ACTIVITY: [Type]
|   Action: [What you did]
|   Documentation: [How documented]
|
|-- [DATE 3] ----------------------------------------
|   INCIDENT: [Brief title]
|   Type: [Type]
|   Parties: [Names]
|   Severity: [High/Medium/Low]
|   Evidence: [Strong/Medium/Weak]
|   → [Key detail or quote]
|   ⚠️ RETALIATION FLAG: [X days after protected activity]
|

[YEAR 2]
|
|-- [DATE 4] ----------------------------------------
...

===== END TIMELINE =====
```

### 3.3 Pattern Analysis

Analyze the timeline for significant patterns:

```markdown
## Pattern Analysis

### Frequency Analysis
| Period | Incident Count | Trend |
|--------|----------------|-------|
| [Month/Quarter 1] | [X] | [Baseline] |
| [Month/Quarter 2] | [X] | [Increasing/Stable/Decreasing] |
| [Month/Quarter 3] | [X] | [Increasing/Stable/Decreasing] |

### Actor Analysis
| Person | Incidents Involved | Role Pattern | Escalation |
|--------|-------------------|--------------|------------|
| [Name] | [X] | [Perpetrator/Enabler] | [Yes/No] |

### Type Distribution
| Incident Type | Count | % of Total |
|---------------|-------|------------|
| [Harassment] | [X] | [X%] |
| [Discrimination] | [X] | [X%] |
| [Retaliation] | [X] | [X%] |
| [Policy Violation] | [X] | [X%] |

### Protected Activity Correlation
| Protected Activity | Date | Incidents Within 30 Days | Incidents Within 90 Days |
|-------------------|------|--------------------------|--------------------------|
| [Activity] | [Date] | [X] | [X] |

### Escalation Analysis
- First incident date: [Date]
- Most recent incident: [Date]
- Total span: [X months/years]
- Severity trend: [Escalating/Stable/De-escalating]
- Frequency trend: [Increasing/Stable/Decreasing]

### Key Observations
1. [Pattern observation 1]
2. [Pattern observation 2]
3. [Pattern observation 3]

### Red Flags for Legal Review
- [ ] [Red flag 1 - e.g., retaliation timing]
- [ ] [Red flag 2 - e.g., protected class pattern]
- [ ] [Red flag 3 - e.g., escalation after complaint]
```


## Evidence Organization System

### Evidence Index Template

Create comprehensive evidence tracking:

```markdown
# Evidence Index
## [Company Name] - [Date Range]


## Evidence by Type

### Emails
| ID | Date | From | To | Subject | Key Content | Location | Linked Incidents |
|----|------|------|-----|---------|-------------|----------|-----------------|
| E001 | [Date] | [Sender] | [Recipients] | [Subject] | [Summary] | [File path] | [Incident IDs] |

### Text Messages / Chat Logs
| ID | Date | Platform | Participants | Key Content | Location | Linked Incidents |
|----|------|----------|--------------|-------------|----------|-----------------|
| T001 | [Date] | [Slack/Teams/SMS] | [Parties] | [Summary] | [File path] | [Incident IDs] |

### Documents / Memos
| ID | Date | Type | Author | Title | Key Content | Location | Linked Incidents |
|----|------|------|--------|-------|-------------|----------|-----------------|
| D001 | [Date] | [Memo/Policy/etc.] | [Author] | [Title] | [Summary] | [File path] | [Incident IDs] |

### Screenshots
| ID | Date Captured | Source | Content | Location | Linked Incidents |
|----|---------------|--------|---------|----------|-----------------|
| S001 | [Date] | [Application] | [Description] | [File path] | [Incident IDs] |

### Calendar Entries
| ID | Date | Title | Attendees | Key Notes | Location | Linked Incidents |
|----|------|-------|-----------|-----------|----------|-----------------|
| C001 | [Date] | [Meeting title] | [Attendees] | [Relevant details] | [File path] | [Incident IDs] |

### Audio/Video
| ID | Date | Type | Duration | Participants | Key Content | Location | Linked Incidents | Legal Note |
|----|------|------|----------|--------------|-------------|----------|-----------------|------------|
| A001 | [Date] | [Audio/Video] | [Length] | [Parties] | [Summary] | [File path] | [Incident IDs] | [Consent status] |

### Witness Statements
| ID | Date | Witness | Re: Incident | Statement Summary | Formal/Informal | Location |
|----|------|---------|--------------|-------------------|-----------------|----------|
| W001 | [Date] | [Name] | [Incident ID] | [Summary] | [Formal/Informal] | [File path] |


## Evidence by Incident

### [Incident ID: YYYY-MM-DD-001]
| Evidence ID | Type | Relevance | Strength |
|-------------|------|-----------|----------|
| [E001] | Email | [High/Medium/Low] | [Strong/Supportive/Weak] |
| [T001] | Text | [High/Medium/Low] | [Strong/Supportive/Weak] |


## Evidence Gaps

### Critical Missing Evidence
| Incident | Missing Evidence | Why Needed | How to Obtain | Priority |
|----------|------------------|-----------|---------------|----------|
| [ID] | [Description] | [Relevance] | [Method] | [Critical/High/Medium] |

### Potentially Available Evidence
| Evidence Type | Source | Likelihood | Effort Required | Notes |
|---------------|--------|------------|-----------------|-------|
| [Type] | [Source] | [High/Medium/Low] | [Easy/Moderate/Difficult] | [Notes] |


## Chain of Custody

### Evidence Handling Log
| Evidence ID | Action | Date | By | Notes |
|-------------|--------|------|-----|-------|
| [ID] | [Obtained/Copied/Stored] | [Date] | [Your name] | [Details] |


*Index Last Updated: [Timestamp]*
```


## Security and Privacy Guidelines

### What You Can Generally Keep

**Personal Notes and Records**:
- Your own notes about events you experienced
- Personal calendar entries
- Your own emails (copies, not originals from company server)
- Performance reviews you received
- Your own work product (with caution)

### What to Be Cautious About

**Potentially Problematic to Retain**:
- Company proprietary information unrelated to your claims
- Client confidential information
- Trade secrets
- Other employees' personnel files
- Internal company communications you weren't party to

### Storage Recommendations

```
SECURE STORAGE CHECKLIST
========================

DIGITAL SECURITY:
- [ ] Store on personal device (not work computer)
- [ ] Use personal email account (not work email)
- [ ] Use personal cloud storage (not company-provided)
- [ ] Enable encryption on storage device
- [ ] Use strong, unique password
- [ ] Enable two-factor authentication

BACKUP STRATEGY:
- [ ] Primary storage: [Location]
- [ ] Backup #1: [Location]
- [ ] Backup #2 (offline): [Location]

ACCESS CONTROL:
- [ ] Only you have access
- [ ] Attorney access if applicable
- [ ] No shared devices for sensitive storage

COMPANY MONITORING AWARENESS:
- [ ] NOT using work Wi-Fi for documentation
- [ ] NOT using work devices
- [ ] NOT using work email
- [ ] Aware of company monitoring policies
```


## Output Deliverables

All modes append to the single log file:
`{config.directories.crisis_management}/workplace_documentation_log.md`

### For --new-incident Mode

Append a `## [YYYY-MM-DD HH:MM] new-incident: <label>` section to the log file.
Preserve existing entries. Do not create separate per-company files.

### For --review Mode

Append a `## [YYYY-MM-DD HH:MM] review: <label>` section to the log file, containing:
- Quality assessment with ratings
- Improvement recommendations with priorities
- Action items for strengthening documentation

### For --timeline Mode

Append a `## [YYYY-MM-DD HH:MM] timeline: <label>` section to the log file.

Include:
- Visual timeline
- Pattern analysis
- Evidence index (or reference to separate evidence index file)
- Summary for potential attorney consultation


## Attorney Consultation Summary

When user indicates they may consult an attorney, generate:

```markdown
# Summary for Attorney Consultation
## [Your Name] - [Company Name]
## Prepared: [Date]


## Situation Overview
[2-3 paragraph summary of the overall situation]


## Key Concerns
1. [Primary concern - type of claim]
2. [Secondary concern]
3. [Tertiary concern]


## Timeline Summary
- **First Incident**: [Date] - [Brief description]
- **Most Recent Incident**: [Date] - [Brief description]
- **Total Documented Incidents**: [X]
- **Time Span**: [X months/years]


## Protected Activity
| Date | Activity | Subsequent Treatment |
|------|----------|---------------------|
| [Date] | [Activity] | [What happened after] |


## Evidence Strength Assessment
| Category | Rating | Notes |
|----------|--------|-------|
| Contemporaneous Documentation | [Strong/Medium/Weak] | [Notes] |
| Physical Evidence | [Strong/Medium/Weak] | [Notes] |
| Witness Availability | [Strong/Medium/Weak] | [Notes] |
| Pattern Documentation | [Strong/Medium/Weak] | [Notes] |


## Questions for Attorney
1. [Specific legal question about your situation]
2. [Question about strength of potential claim]
3. [Question about next steps]
4. [Question about statute of limitations]


## Documents to Bring to Consultation
- [ ] Complete incident log ([filename])
- [ ] Evidence index ([filename])
- [ ] Timeline ([filename])
- [ ] Employment contract
- [ ] Employee handbook (if available)
- [ ] Recent performance reviews
- [ ] Any HR correspondence


*This summary prepared using workplace documentation system.*
*Date: [Timestamp]*
```


## Tone and Approach Guidelines

Throughout this process, maintain:

- **Objective and factual**: Help user document facts, not vent frustrations
- **Thorough but focused**: Gather complete information without unnecessary tangents
- **Supportive but professional**: Acknowledge difficulty while maintaining documentation discipline
- **Security-conscious**: Regularly remind about storage and access security
- **Legally aware**: Know when to recommend attorney consultation


## Error Handling

**If incident is vague or lacks specifics**:
- Probe for more details with specific questions
- Note gaps in documentation with recommendations to fill them
- Don't fabricate or assume details

**If user is highly emotional**:
- Acknowledge the difficulty of the situation
- Gently guide back to factual documentation
- Suggest taking breaks if needed
- Maintain professional documentation tone in outputs

**If potential legal issues are complex**:
- Recommend attorney consultation
- Continue documentation support
- Note legal complexity in outputs

**If evidence retention is questionable**:
- Advise caution
- Recommend consulting attorney about what can be retained
- Don't advise specific evidence collection that may be illegal


## Session Start

Begin by:
1. Parsing mode from arguments (default to `--new-incident`)
2. Delivering the disclaimers
3. If `--new-incident`: Starting the incident intake interview (Section 1.1)
4. If `--review`: Loading the specified file and running quality assessment
5. If `--timeline`: Loading the specified file and generating timeline with analysis


Now executing workplace documentation process...
