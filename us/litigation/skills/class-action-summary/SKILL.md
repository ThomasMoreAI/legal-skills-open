---
name: class-action-summary
title: Class Action Lawsuit Summary
description: Produces structured U.S. class action lawsuit summaries covering claims, class definition, Rule 23 analysis, procedural history, and outcomes. Use when summarizing class actions, class certification rulings, MDL proceedings, or settlement approvals for litigation evaluation, due diligence, or compliance monitoring.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/class-action-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Class Action Lawsuit Summary

Produce a neutral, citation-ready summary of a U.S. class action from filing through resolution or current posture.

## Required Inputs

1. Operative complaint (and amendments).
2. Docket report with key dates and ECF numbers.
3. Orders on motions to dismiss, class certification, summary judgment, trial.
4. Settlement/approval materials or verdict documents.
5. MDL transfer/coordination orders if applicable.

## Workflow

1. Extract metadata into the caption block.
2. Write a 3–4 sentence executive summary.
3. Complete each section per the table below with record citations.
4. Run certification and resolution checklists.
5. Add significance note if there is a published opinion or industry impact.

## Caption Block

```
Case Caption:
Court:
Docket No.:
Filed:
Judge(s):
Jurisdiction/Venue:
MDL/JPML (if any):
Parties (Plaintiffs/Defendants):
Status (pending/settled/tried/appeal):
```

## Sections

| Section | Content |
|---|---|
| Claims and Allegations | Causes of action; statutes cited; alleged misconduct and timeframe; class period; damages theory; key defenses resolved |
| Class Definition and Certification | Proposed/certified class definitions; membership criteria; geographic/temporal limits; subclasses; estimated size; Rule 23(a) findings; Rule 23(b) basis ((b)(1)/(b)(2)/(b)(3)); certification granted/denied/decertified with reasons |
| Procedural History | Filing; removal/transfer; major motion rulings; discovery milestones; certification briefing and order date; Rule 23(f) appeals; MDL coordination; trial or settlement milestones |
| Resolution / Outcomes | Settlement amount and fund structure; claims process/deadlines; allocation; fees/costs/service awards; non-monetary relief; approval dates/objections; verdict/damages; post-trial motions/appeals; current posture if pending |
| Significance | Published opinions; precedential holdings; industry impact (include only if applicable) |

## Certification Checklist

- [ ] Operative class definition text and class period
- [ ] Rule 23(a): numerosity, commonality, typicality, adequacy
- [ ] Rule 23(b) basis and relief type (injunctive vs damages)
- [ ] Subclasses and rationale
- [ ] If denied/decertified: court's reasoning (predominance, ascertainability, typicality)

## Resolution Checklist

- [ ] Settlement amount; reversionary or cy pres terms
- [ ] Allocation formula and claims rate
- [ ] Attorneys' fees, costs, service awards
- [ ] Injunctive/programmatic relief and compliance monitoring
- [ ] Preliminary and final approval dates; opt-out and objection counts

## Citation Format

Use record-specific citations: document title, ECF number, date, pin cite.

```
("Order Granting Class Certification", ECF No. 123, at 7-10 (2024-05-12))
```

## Pitfalls

- Distinguish allegations from adjudicated facts — use "alleged" or "purported" unless admitted or adjudicated.
- Prefer operative complaint and final orders; flag inconsistencies across versions.
- State "Not stated in record" for missing facts — never infer.
- Note whether the case is federal Rule 23 or a state analog; mark `[VERIFY]` if unclear.
- Omit sealed or protected information; note confidentiality limits.
- Highlight interlocutory appeals and their disposition.
