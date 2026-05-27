---
name: motion-to-dismiss-indictment
title: Motion to Dismiss Indictment
description: Drafts motions to dismiss criminal indictments in federal and state courts. Covers defective indictments, statute of limitations, speedy trial, double jeopardy, prosecutorial misconduct, and jurisdictional defects. Use when the agent needs to challenge the legal sufficiency of criminal charges or draft a pre-trial dismissal motion.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/motion-to-dismiss-indictment
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: criminal
language: en
tags: [drafting, litigation, motion]
---

# Motion to Dismiss Indictment

Draft a defense motion to dismiss a criminal indictment on legal grounds, challenging the prosecution's ability to proceed.

## Required Inputs

- **Charging document** — indictment or information to challenge
- **Statutes charged** — elements of each offense
- **Procedural timeline** — arrest, indictment, arraignment, continuances
- **Grand jury materials** — transcripts if available (jurisdiction-dependent)
- **Dismissal grounds** — specific legal basis (see below)
- **Controlling authority** — key case law in the jurisdiction

## Quick Start

1. Identify the strongest ground(s) for dismissal from the charging document and procedural record.
2. Classify each ground as facial (indictment alone) or factual (requires evidentiary hearing).
3. Draft using the output structure below.
4. If factual disputes exist, include an evidentiary hearing request.
5. Verify all citations or mark `[VERIFY]`.

## Grounds for Dismissal

### Defective Indictment (FRCP 7/12(b) or state equivalent)

- Fails to state an offense (missing essential element)
- Unconstitutionally vague (inadequate notice)
- Multiplicitous (same offense in multiple counts)
- Duplicitous (multiple offenses in single count)
- Constructive amendment (proof would differ materially from indictment)

### Statute of Limitations

- Compare offense date, limitations period, and indictment date
- Address tolling: absence from jurisdiction, concealment, continuing offense
- Cite the specific limitations statute

### Speedy Trial

**Sixth Amendment** — apply *Barker v. Wingo* factors: length of delay, reason, defendant's assertion, prejudice. For pre-indictment delay, use due process analysis.

**Speedy Trial Act (18 U.S.C. §§ 3161–3174)** (federal only):
- 30 days arrest → indictment; 70 days indictment/arraignment → trial
- Calculate excludable vs. non-excludable time
- Remedy: dismissal with or without prejudice

### Double Jeopardy (Fifth Amendment)

- Prior prosecution for same offense; apply *Blockburger* same-elements test
- Collateral estoppel
- Note dual sovereignty exception (state/federal)

### Prosecutorial Misconduct

- Grand jury abuse (misleading instructions, withholding exculpatory evidence)
- Vindictive prosecution (retaliation for exercising legal rights)
- Selective prosecution (discriminatory enforcement — equal protection)
- Outrageous government conduct (entrapment-related)

### Jurisdictional Defects

- Lack of federal jurisdiction; insufficient interstate commerce nexus
- Improper venue (offense not committed in the district)

## Output Structure

1. **Caption** — criminal case caption; title: "Defendant's Motion to Dismiss Indictment"
2. **Introduction** — charges at issue, ground(s) for dismissal, relief requested
3. **Factual Background** — procedural and factual history from the record (not disputed facts requiring a hearing)
4. **Legal Argument** — for each ground: (a) legal standard with authority, (b) application to facts, (c) prejudice to defendant, (d) remedy requested
5. **Evidentiary Hearing Request** (if factual disputes exist) — identify issues, witnesses, and exhibits
6. **Conclusion** — request dismissal with prejudice (preferred) or without; for speedy trial, argue factors favoring with-prejudice dismissal

## Pitfalls and Checks

- **File early** — some grounds are waived if not raised pre-trial
- **Facial vs. factual** — facial challenges rely on the indictment alone; factual challenges require a hearing
- **Speedy trial timeline** — build a detailed period-by-period excludable/non-excludable chart
- **Grand jury challenges are narrow** — courts rarely look behind the indictment
- **Selective/vindictive prosecution** — extremely high bar; assess viability candidly
- **Strategic fit** — consider whether a motion to suppress or going to trial is a stronger path
- **Citation hygiene** — verify every case cite or flag `[VERIFY]`

---

It looks like I don't have write permission to the file. Could you grant write access so I can save this, or would you like to copy the content above directly?
