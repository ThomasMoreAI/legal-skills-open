---
name: bylaw-amendment-resolution
title: Bylaw Amendment Resolution
description: Drafts a formal Bylaw Amendment Resolution for U.S. corporations, LLCs, or non-profits. Invoke when a board, shareholders, or members approve bylaw changes and need an auditable WHEREAS/RESOLVED record with amendment text, vote tallies, effective date, and secretary certification for minute books, bank submissions, or state filings.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/bylaw-amendment-resolution
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [agreement, drafting]
---

# Bylaw Amendment Resolution

Produces a governance-compliant resolution recording bylaw amendments with exact text, voting record, and certification suitable for minute books, financial institutions, state filings, and litigation.

## Prerequisites

Collect before drafting:

1. **Entity info** — legal name (per formation docs), jurisdiction, entity type (corp/LLC/non-profit)
2. **Current bylaws** — adoption or last-amendment date, article/section numbers being amended
3. **Amendment text** — verbatim existing language and proposed replacement
4. **Approval authority** — acting body (board/shareholders/members), quorum and vote thresholds per bylaws or statute
5. **Meeting or consent details** — date, location, or unanimous written consent with all signatories
6. **Effective date** — immediate, date-certain, contingent, or upon state filing

## Quick Start

1. Gather prerequisites above
2. Draft header with entity name, acting body, resolution number, adoption date
3. Build WHEREAS recitals establishing authority and rationale
4. Draft RESOLVED clauses with verbatim amended text
5. Record voting tally or consent confirmation
6. Set effective date and any transitional provisions
7. Add secretary certification block

## Document Structure

### Header

```
RESOLUTION OF THE [BOARD OF DIRECTORS / SHAREHOLDERS / MEMBERS]
TO AMEND THE BYLAWS OF [FULL LEGAL ENTITY NAME]
[Resolution No. ___]
Date of Adoption: [Date]
```

### WHEREAS Recitals

1. Bylaws originally adopted [date], last amended [date]
2. Provision requiring amendment (Art. ___, § ___) with current text
3. Business purpose/rationale
4. Statutory/documentary authority for amendment
5. Governing body properly convened; notice given; quorum present
6. *(if applicable)* Special voting requirements met (supermajority, class vote)

Close final recital with `"; and"` to transition to operative language.

### RESOLVED Clauses

```
NOW, THEREFORE, BE IT RESOLVED, that Article ___, Section ___ of the
Bylaws of [Entity Name] is hereby amended to read in its entirety as follows:

[ARTICLE/SECTION NUMBER AND TITLE]
[Full text of amended provision]

RESOLVED FURTHER, that all provisions not expressly amended hereby
remain in full force and effect.

RESOLVED FURTHER, that officers are authorized to make technical,
non-substantive corrections to formatting, cross-references, and
section numbering as necessary.
```

- Multiple amendments: use `RESOLVED FIRST / RESOLVED SECOND ...`
- Show changes: ~~deleted language~~ and **added language**, or `[DELETED]` / `[NEW]`
- Add conforming-change resolutions for affected cross-references

### Voting Record

| Field | Value |
|-------|-------|
| Action taken by | Board / Shareholders / Members |
| Meeting date & location | ___ |
| Votes in favor / against / abstentions | ___ / ___ / ___ |
| Total eligible votes | ___ |
| Required threshold met | Yes — [threshold] |

- **Written consent**: state explicitly; confirm all signatures on file
- **Multi-stage** (e.g., board + shareholder): document each stage with separate date, tally, and threshold

### Effective Date & Transition

- State operative date: immediate / specific date / triggering event / upon filing
- Address pending matters under prior language or grandfathered arrangements

### Secretary Certification

```
CERTIFICATE OF SECRETARY

The undersigned, [Name], [Title] of [Entity Name], a [State]
[corporation/LLC/non-profit], certifies that the foregoing resolution
was duly adopted by the [Board/Shareholders/Members] on [Date] in
accordance with applicable law and governing documents, and remains
in full force and effect as of this date.

_______________________________
[Printed Name], [Title]
Date: _______________
[CORPORATE SEAL, if required]
```

Add countersignature line for president/chair if bylaws require it.

## Pitfalls & Checks

- **Verbatim text** — quote current and amended language exactly; never paraphrase
- **State law variance** — voting thresholds and procedures vary by jurisdiction; flag where statute may override bylaws `[VERIFY applicable statute]`
- **Non-profits** — confirm whether members, board, or both must approve; some states require AG notice for charitable entities
- **Filing triggers** — amendments to registered agent, principal office, or name may require concurrent articles amendment and state filing
- **Bank/lender use** — financial institutions may require a separate incumbency certificate alongside this resolution
- **Standalone record** — final document must be self-contained for permanent minute-book filing
