---
name: case-management-judicialmind
title: Case Management
description: Legal case and matter management skill for law firm operations. Use when the user needs assistance with case organization, deadline tracking, calendaring, task management, or matter workflows. Triggers on keywords like "case management", "matter", "deadline", "calendar", "docket", "statute of limitations", "filing deadline", "task tracking", "case status".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/case-management
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: general
language: en
sources:
- title: Checklists
  path: references/checklists.md
- title: Deadline Rules
  path: references/deadline-rules.md
- title: Workflow Templates
  path: references/workflow-templates.md
---

# Case Management

This skill provides expert guidance for managing legal matters, deadlines, and law firm workflows.

## Core Capabilities

### 1. Matter Organization
- Matter intake
- File structure
- Team assignments
- Status tracking

### 2. Deadline Management
- Court deadlines
- Statute of limitations
- Filing requirements
- Calendar rules

### 3. Task Management
- Task assignment
- Progress tracking
- Delegation
- Quality control

### 4. Workflow Automation
- Standard processes
- Checklists
- Triggers
- Notifications

## Matter Lifecycle

### Matter Phases
```
┌──────────────────────────────────────────────────────────────┐
│                    MATTER LIFECYCLE                           │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  Intake → Active → Closing → Closed → Retention → Destruction│
│                                                               │
│    ↓        ↓         ↓         ↓          ↓           ↓     │
│                                                               │
│  Conflict  Work     Final     File      Archive    Destroy   │
│  check     product  billing   storage   per        per       │
│  Open      Deadlines Document Return    policy     schedule  │
│  matter    Tasks    assembly  property                       │
└──────────────────────────────────────────────────────────────┘
```

### Matter Opening Checklist
- [ ] Client/matter conflict check
- [ ] Engagement letter executed
- [ ] Matter number assigned
- [ ] File opened in system
- [ ] Team assigned
- [ ] Initial deadlines entered
- [ ] Budget established (if applicable)
- [ ] Billing setup confirmed
- [ ] Document folder structure created
- [ ] Welcome/intake information gathered

## Deadline Calculation

### Federal Rules (FRCP)

**Computing Time (Rule 6(a))**:
1. Exclude day of trigger event
2. Count every day including weekends/holidays
3. If last day is weekend/holiday, extend to next business day
4. Periods under 11 days: Exclude weekends and holidays from count

**Service Extensions (Rule 6(d))**:
| Service Method | Extension |
|----------------|-----------|
| Mail | +3 days |
| Electronic (CM/ECF) | +3 days |
| Leaving with clerk | +3 days |

### Common Federal Deadlines

| Event | Deadline | Rule |
|-------|----------|------|
| Answer to complaint | 21 days (60 if waiver) | FRCP 12(a) |
| Motion to dismiss | Before responsive pleading | FRCP 12(b) |
| Initial disclosures | 14 days after 26(f) | FRCP 26(a)(1) |
| Discovery responses | 30 days | FRCP 33, 34, 36 |
| Summary judgment | Per scheduling order | FRCP 56 |
| Appeal notice | 30/60 days | FRAP 4 |

### State Variations
- Always verify state-specific rules
- Many states use court days vs. calendar days
- Service methods and extensions vary
- Local rules may modify deadlines

### Statute of Limitations (Common)

| Claim Type | Federal | State (Varies) |
|------------|---------|----------------|
| Personal injury | N/A | 1-6 years |
| Contract (written) | N/A | 3-10 years |
| Contract (oral) | N/A | 2-6 years |
| Property damage | N/A | 2-6 years |
| Employment discrimination | 180/300 days (EEOC) | Varies |
| Securities fraud | 2 years (discovery) | N/A |
| Medical malpractice | N/A | 1-6 years |
| Legal malpractice | N/A | 1-6 years |

### Tolling Doctrines
- Discovery rule (when injury discovered)
- Minority (until age of majority)
- Incapacity
- Fraudulent concealment
- Continuing violation
- Equitable tolling

## Task Management

### Task Categories
| Category | Examples |
|----------|----------|
| Deadlines | Court filings, response dates |
| Assignments | Research, drafting, review |
| Calendar | Hearings, depositions, meetings |
| Administrative | Client calls, billing |
| Reminders | Ticklers, follow-ups |

### Task Assignment Template
```
TASK ASSIGNMENT

Matter: [Matter Number/Name]
Task: [Description]
Assigned to: [Name]
Assigned by: [Name]
Due date: [Date]
Priority: [High/Medium/Low]

Instructions:
[Detailed instructions and context]

Resources:
- [Document 1]
- [Document 2]

Questions: Contact [Name] at [contact info]
```

### Status Tracking

**Matter Status Categories**:
| Status | Description |
|--------|-------------|
| Active | Ongoing work |
| On Hold | Temporarily paused |
| Awaiting Response | Waiting on external party |
| Awaiting Decision | Court/other decision pending |
| Closing | Wrapping up |
| Closed | Completed |

**Status Report Template**:
```
MATTER STATUS REPORT

Matter: [Number/Name]
Client: [Name]
Responsible Attorney: [Name]
Report Date: [Date]

CURRENT STATUS: [Status]

RECENT ACTIVITY:
- [Date]: [Activity]
- [Date]: [Activity]

UPCOMING DEADLINES:
- [Date]: [Deadline]
- [Date]: [Deadline]

OPEN ISSUES:
1. [Issue]
2. [Issue]

NEXT STEPS:
1. [Action]
2. [Action]

BUDGET STATUS:
Budget: $[Amount]
Billed: $[Amount]
Remaining: $[Amount]
```

## Calendar Management

### Calendar Categories
| Category | Color (Suggested) | Examples |
|----------|-------------------|----------|
| Court dates | Red | Hearings, trials, deadlines |
| Depositions | Orange | Scheduled depositions |
| Meetings | Blue | Client meetings, conferences |
| Internal | Green | Team meetings, reviews |
| Reminders | Yellow | Follow-ups, ticklers |

### Court Date Checklist
- [ ] Date and time confirmed
- [ ] Location/courtroom verified
- [ ] Judge/courtroom procedures reviewed
- [ ] Documents filed/prepared
- [ ] Exhibits organized
- [ ] Witnesses notified
- [ ] Travel arrangements (if needed)
- [ ] Technology tested
- [ ] Backup copies prepared
- [ ] Post-appearance tasks scheduled

### Scheduling Conference Preparation
- [ ] Review case file
- [ ] Identify discovery needs
- [ ] Prepare proposed schedule
- [ ] Consider dispositive motion timing
- [ ] Identify expert witness needs
- [ ] Evaluate settlement posture
- [ ] Coordinate with co-counsel
- [ ] Prepare questions for court

## Workflow Templates

### New Litigation Matter
```
PHASE 1: INTAKE (Days 1-7)
□ Conflict check
□ Engagement letter
□ Open matter
□ Gather initial documents
□ Interview client
□ Identify key dates

PHASE 2: INVESTIGATION (Days 1-30)
□ Document review
□ Legal research
□ Identify witnesses
□ Preserve evidence
□ Timeline creation
□ Theory development

PHASE 3: PLEADINGS
□ Draft complaint/answer
□ Review and revise
□ Client approval
□ File and serve
□ Calendar response deadlines

PHASE 4: DISCOVERY
□ Prepare discovery plan
□ Draft written discovery
□ Respond to discovery
□ Schedule depositions
□ Expert retention/disclosure
□ Discovery motion practice

PHASE 5: DISPOSITIVE MOTIONS
□ Summary judgment analysis
□ Motion drafting
□ Opposition/reply briefing
□ Oral argument preparation

PHASE 6: TRIAL PREPARATION
□ Pretrial motions
□ Witness preparation
□ Exhibit preparation
□ Trial brief
□ Jury instructions

PHASE 7: TRIAL/RESOLUTION
□ Trial
□ Post-trial motions
□ Appeal consideration
□ Settlement/judgment
□ Close matter
```

### Transaction Matter
```
PHASE 1: INTAKE
□ Conflict check
□ Engagement letter
□ Open matter
□ Initial call/meeting
□ Document requests

PHASE 2: DUE DILIGENCE
□ Due diligence request list
□ Data room review
□ Issues identification
□ Report preparation

PHASE 3: NEGOTIATION
□ Draft/review documents
□ Negotiate terms
□ Track changes
□ Client updates

PHASE 4: CLOSING
□ Closing checklist
□ Document preparation
□ Signature coordination
□ Closing execution
□ Post-closing items

PHASE 5: WRAP-UP
□ Final billing
□ Document organization
□ Client debrief
□ Close matter
```

## Quality Control

### File Review Checklist
- [ ] Engagement documentation complete
- [ ] Deadlines calendared correctly
- [ ] All deadlines met
- [ ] Work product quality reviewed
- [ ] Client communications documented
- [ ] Billing current and accurate
- [ ] Documents properly organized
- [ ] Privileged materials marked
- [ ] Conflicts cleared

### Error Prevention
- Multiple calendar entries for critical deadlines
- Reminder before deadline
- Peer review of calculations
- Confirmation of court dates
- Service verification
- Document version control

## Integration with Other Skills

- **litigation**: Litigation case management
- **court-filings**: Filing procedures
- **billing-operations**: Matter billing
- **client-intake**: New matter intake
- **legal-analytics**: Case analysis

## Reference Files

For detailed guidance:
- `references/deadline-rules.md` - Deadline calculation reference
- `references/workflow-templates.md` - Matter workflow templates
- `references/checklists.md` - Case management checklists
