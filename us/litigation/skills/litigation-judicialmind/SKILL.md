---
name: litigation-judicialmind
title: Litigation
description: Civil litigation and motion practice skill. Use when the user needs assistance with lawsuits, pleadings, motions, discovery, trial preparation, or court procedures. Triggers on keywords like "litigation", "lawsuit", "complaint", "motion", "discovery", "deposition", "trial", "pleading", "summary judgment", "injunction", "court filing".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/litigation
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Discovery Forms
  path: references/discovery-forms.md
- title: Motion Templates
  path: references/motion-templates.md
- title: Trial Checklist
  path: references/trial-checklist.md
---

# Litigation

This skill provides expert guidance for civil litigation from case inception through trial and appeal.

## Core Capabilities

### 1. Pleadings
- Complaint drafting
- Answer and affirmative defenses
- Counterclaims and cross-claims
- Amended pleadings

### 2. Motion Practice
- Motion to dismiss
- Motion for summary judgment
- Discovery motions
- Motions in limine

### 3. Discovery
- Written discovery (interrogatories, RFPs, RFAs)
- Depositions
- Expert discovery
- Privilege review

### 4. Trial Preparation
- Witness preparation
- Exhibit organization
- Trial briefs
- Jury instructions

## Litigation Lifecycle

```
┌─────────────────────────────────────────────────────────────────┐
│                    LITIGATION PHASES                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐     │
│  │  Pre-    │ → │ Pleading │ → │Discovery │ → │ Disposit.│     │
│  │  Filing  │   │  Phase   │   │  Phase   │   │  Motions │     │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘     │
│       │              │              │              │             │
│       ▼              ▼              ▼              ▼             │
│  - Demand       - Complaint    - Initial      - MSJ           │
│  - Investigation- Answer        disclosures  - MtD            │
│  - Preservation - Scheduling   - Written     - Daubert        │
│  - Tolling        conference     discovery                     │
│                                - Depositions                    │
│                                - Expert reports                 │
│                                                                  │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐     │
│  │  Pre-    │ → │  Trial   │ → │ Verdict  │ → │ Appeal   │     │
│  │  Trial   │   │          │   │ & Judgt  │   │          │     │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘     │
│       │              │              │              │             │
│       ▼              ▼              ▼              ▼             │
│  - Final pre-  - Jury        - Post-trial  - Notice          │
│    trial conf    selection     motions     - Briefing        │
│  - MILs        - Opening     - Judgment    - Oral argument   │
│  - Trial brief - Evidence      entry       - Mandate         │
│  - Exhibit/    - Closing                                      │
│    witness list- Jury charge                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Key Deadlines (Federal)

| Event | Rule | Deadline |
|-------|------|----------|
| Answer to Complaint | FRCP 12(a) | 21 days (60 if waiver) |
| Motion to Dismiss | FRCP 12(b) | Before responsive pleading |
| Initial Disclosures | FRCP 26(a)(1) | 14 days after 26(f) conf |
| Discovery Cutoff | Local Rule | Per scheduling order |
| Expert Disclosures | FRCP 26(a)(2) | Per scheduling order |
| Summary Judgment | FRCP 56 | Per scheduling order |
| Pretrial Motions | Local Rule | Per scheduling order |

## Motion Practice

### Motion to Dismiss (Rule 12(b))

**Grounds**:
1. Lack of subject matter jurisdiction (12(b)(1))
2. Lack of personal jurisdiction (12(b)(2))
3. Improper venue (12(b)(3))
4. Insufficient process (12(b)(4))
5. Insufficient service (12(b)(5))
6. **Failure to state a claim (12(b)(6))** - most common
7. Failure to join necessary party (12(b)(7))

**12(b)(6) Standard** (Twombly/Iqbal):
- Must state a claim that is "plausible on its face"
- Factual allegations must raise right to relief "above speculative level"
- Court accepts well-pleaded facts as true
- Legal conclusions are not entitled to presumption of truth

### Motion for Summary Judgment (Rule 56)

**Standard**: No genuine dispute of material fact; movant entitled to judgment as a matter of law

**Framework**:
```
1. Identify elements of claim/defense
2. For each element:
   - Cite undisputed facts (with record citations)
   - Explain why no genuine dispute exists
   - Apply law to facts
3. Address opponent's evidence
   - Show it's inadmissible, irrelevant, or insufficient
4. Conclude entitlement to judgment
```

**Response Strategy**:
- Cite specific facts showing genuine dispute
- Provide record citations for every disputed fact
- Argue reasonable inferences in non-movant's favor
- Consider Rule 56(d) continuance if discovery incomplete

## Discovery

### Written Discovery

| Type | Rule | Purpose | Limits (Federal) |
|------|------|---------|------------------|
| Interrogatories | 33 | Factual questions | 25 (including subparts) |
| RFPs | 34 | Documents/ESI | No numeric limit |
| RFAs | 36 | Admit facts | No numeric limit |

### Deposition Practice

**Preparation Checklist**:
- [ ] Review all documents produced by/about witness
- [ ] Outline topics by subject matter
- [ ] Prepare exhibits and marking strategy
- [ ] Know the rules (7-hour limit, objection grounds)
- [ ] Coordinate with co-counsel on areas

**Objection Grounds** (FRCP 30(c)(2)):
- Form of question (leading, compound, vague)
- Privilege
- Outside scope (for 30(b)(6))
- Harassment

### Privilege Review

**Attorney-Client Privilege Elements**:
1. Communication
2. Between attorney and client
3. Made in confidence
4. For purpose of legal advice

**Work Product Doctrine**:
- Prepared in anticipation of litigation
- Opinion work product (mental impressions) vs. ordinary work product
- Can be overcome by substantial need/undue hardship (ordinary only)

## Document Formatting

### Motion Format
```
UNITED STATES DISTRICT COURT
[DISTRICT]

[PLAINTIFF],            )
                        )
     Plaintiff,         )    Case No. [XX-cv-XXXX]
                        )
v.                      )    [DOCUMENT TITLE]
                        )
[DEFENDANT],            )
                        )
     Defendant.         )
________________________)

[TITLE OF MOTION]

[INTRODUCTION - 1 paragraph summary]

STATEMENT OF FACTS
[Relevant facts with record citations]

ARGUMENT
I. [LEGAL ARGUMENT 1]
   A. [Subargument]
   B. [Subargument]

II. [LEGAL ARGUMENT 2]

CONCLUSION

[Signature block]
```

## Key Standards of Review

| Motion Type | Standard |
|-------------|----------|
| 12(b)(1) | De novo (facial); preponderance (factual) |
| 12(b)(6) | De novo (accepting facts as true) |
| Summary Judgment | De novo (viewing facts in light most favorable to non-movant) |
| Discovery | Abuse of discretion |
| Preliminary Injunction | Abuse of discretion |

## Preliminary Injunction Factors

**Federal Standard** (Winter v. NRDC):
1. Likelihood of success on the merits
2. Likelihood of irreparable harm absent injunction
3. Balance of hardships favors movant
4. Injunction is in public interest

## Best Practices

### General
- Know your local rules (they vary significantly)
- Meet deadlines or seek extensions early
- Maintain organized case file/database
- Preserve all potentially relevant evidence

### Pleadings
- Plead all viable claims and defenses
- Include factual detail supporting plausibility
- Request all available forms of relief

### Discovery
- Propound discovery early
- Respond completely and timely
- Meet and confer before filing motions
- Document discovery disputes

### Motions
- Comply with page limits and formatting
- Cite controlling authority
- Include all required certifications
- Propose orders

## Integration with Other Skills

- **legal-research**: Case law and precedent analysis
- **e-discovery**: Electronic document review
- **deposition-prep**: Witness preparation
- **brief-writing**: Appellate briefs
- **court-filings**: ECF procedures

## Reference Files

For detailed templates and checklists:
- `references/motion-templates.md` - Standard motion formats
- `references/discovery-forms.md` - Written discovery templates
- `references/trial-checklist.md` - Trial preparation guide
