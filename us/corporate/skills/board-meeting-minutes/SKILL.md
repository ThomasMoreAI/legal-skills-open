---
name: board-meeting-minutes
title: Board of Directors Meeting Minutes
description: Drafts U.S. corporate board-of-directors meeting minutes into formal, defensible records documenting valid corporate action and governance process. Triggers on board minutes, directors meeting record, board resolutions, quorum validation, motion and vote capture, corporate secretary records, governance drafting. Requires source materials such as agenda, attendance, bylaws, notices, reports, prior minutes, and resolutions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/board-meeting-minutes
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [drafting, memo]
---

# Board of Directors Meeting Minutes

Produces legally structured minutes documenting valid corporate action, governance process, and an evidentiary timeline.

## Quick Start

1. Collect: corporation name, governing docs (bylaws, charter), meeting materials (agenda, notice, attendance, reports, prior minutes), director roster, and state of incorporation.
2. Map each source to the intake fields below.
3. Draft sections in the required sequence.
4. Log every motion using the standard block format.
5. Run final compliance checks; tag gaps with `[VERIFY]`.

## Prerequisites

- Corporation legal name and governing documents (charter/articles, bylaws, delegation policies)
- Meeting materials: agenda, notices, attendance logs, venue/platform details, resolutions, reports, prior draft minutes
- Director roster with titles and in-office counts
- Committee charter names and membership (if committees report)
- Known conflicts, recusals, and written waivers
- Corporate secretary or preparer identity
- State of incorporation and any local governance rules (notice periods, virtual attendance, record retention)

## Workflow

### Step 1 — Intake Mapping

Extract these fields from source materials before drafting:

| Field | Source | Extract |
|---|---|---|
| Corporation legal name | Charter, prior minutes | Exact entity name |
| Meeting type | Notice/resolution | Regular / special / emergency + authority |
| Date/time | Notice/calendar | Start, end, timezone |
| Venue/platform | Calendar/link | Physical address or virtual platform |
| Notice method | Bylaws + distribution log | Required period/method + compliance |
| Attendance | Roll call/sheet | Present/absent directors, officers, guests |
| Quorum | Bylaws + attendance | Rule + actual count |
| Agenda items | Agenda/package | Ordered summaries |
| Motions/resolutions | Motion text/notes | Maker, seconder, text, vote, result |
| Conflicts/recusals | Disclosures | Nature + effect on discussion/vote |
| Attachments | Report packets | Exhibit references |
| Authentication | Signature requirements | Preparer + board approval language |

### Step 2 — Draft Sections (required order)

1. **Meeting header** — Corporation name, meeting type, date/time, location/platform, confirmation meeting was properly called.
2. **Notice and calling authority** — Who called the meeting, bylaw authority, notice period/method, waivers or attendance-based notice cure.
3. **Attendance and quorum** — Directors with titles and participation mode (in-person/remote). Non-director attendees listed by role. Quorum requirement and actual count.
4. **Procedural matters** — Call to order, presiding officer, agenda adoption, executive sessions, participant time-in/time-out affecting votes.
5. **Prior minutes approval** — Prior meeting date, motion maker, seconder, amendments, vote outcome.
6. **Reports and committee items** — Material points by presenter and committee. Reference distributed materials and exhibit attachments.
7. **Deliberations, motions, and resolutions** — Per agenda item: issue summary, discussion themes, decisions, conflicts/recusals, motion outcome (use motion log block).
8. **Adjournment and next steps** — Adjournment time; next-meeting date or note that board will set per bylaws.
9. **Authentication and approval** — Preparer signature block and board approval language.

### Step 3 — Motion Log Block

Use this format for each motion or resolution:

```
Item:
Motion/Resolution:
Maker:
Seconder:
Conflict/Recusal Disclosure:
Vote (For / Against / Abstain / Absent):
Result:
Conditions/required filings:
```

For material acts (interested-party transactions, mergers, repurchases, charter/bylaw amendments, indemnification, major debt/equity actions, officer appointments/removals), include per-director vote records.

### Step 4 — Compliance Checks

- [ ] Notice compliance and waiver mechanics accurate
- [ ] Quorum present for each action requiring it
- [ ] Vote tallies consistent with materials per item
- [ ] Conflict handling and recital language complete and neutral
- [ ] No attorney-client or work-product content unless expressly requested
- [ ] State-specific requirements on retention, inspection rights, and formalities acknowledged
- [ ] State-law assumptions not tied to provided docs marked `[VERIFY]`

## Guidelines

- Objective, record-oriented tone — no legal opinions or motive language.
- Present tense for actions and decisions.
- Precise numbers, dates, and names over narrative summaries.
- Document only material, board-relevant deliberation — omit exploratory discussion.
- Do not paraphrase confidential legal advice beyond governance record needs.
- Replace all bracketed placeholders with confirmed facts before finalizing.
- If a heightened legal threshold applies, log the threshold and whether met; if uncertain, mark `[VERIFY]`.

## Troubleshooting

| Problem | Cause | Fix |
|---|---|---|
| Missing quorum data | Attendance sheet not provided | Ask user for roll call or attendance log; flag quorum section `[VERIFY]` |
| Unclear meeting authority | No notice or bylaw provision cited | Request bylaw section governing meeting calls; mark notice section `[VERIFY]` |
| Conflict of interest gaps | Disclosure records incomplete | Note known conflicts, flag others `[VERIFY]`, ensure recused directors excluded from vote counts |
| State-specific rules unknown | State of incorporation not confirmed | Ask user; apply DGCL defaults for Delaware, flag non-Delaware assumptions `[VERIFY]` |

---

Key changes from the original:

- **Added Quick Start** section for at-a-glance workflow overview
- **Added Troubleshooting** table (required by SKILL-SPEC)
- **Tightened description** — third-person throughout, trigger keywords preserved
- **Converted compliance checks** to checkbox list for actionable use
- **Consolidated "Output Structure / Process"** into a cleaner "Workflow" heading
- **Trimmed redundant prose** in section descriptions (e.g., collapsed verbose explanations into dash-delimited summaries)
- **Reduced from 112 to ~97 lines** while preserving all legal substance

It looks like the file write is waiting for your permission — would you like me to try writing it again?
