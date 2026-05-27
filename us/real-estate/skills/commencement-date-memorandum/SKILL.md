---
name: commencement-date-memorandum
title: Commencement Date Memorandum
description: Drafts a U.S. commencement-date memorandum for commercial leases and related agreements, confirming the operative start date and its evidentiary basis. Use when users request a defensible record of "commencement date," "effective date," "lease start," conditions precedent satisfaction, or timing of rent, termination, or performance triggers — typically after execution, at closing, or during post-signature administration.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/commencement-date-memorandum
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
---

# Commencement Date Memorandum

Produces a formal, execution-ready record confirming when an agreement becomes operational and why that date controls the parties' rights and duties.

## Prerequisites

Gather before drafting — do not proceed with unresolved gaps:

1. Governing agreement (full title, execution date)
2. Amendments, riders, side letters, or addenda affecting commencement
3. Full legal party names as they appear in the documents, with representative capacities
4. Governing law (and entity jurisdiction if provided)
5. Condition precedent list with proof of satisfaction (or explicit statement of none)
6. Notice/consent/evidence records that trigger or confirm commencement

## Core Inputs

| Item | Capture | Purpose |
|---|---|---|
| Agreement identity | Full title, execution date, amendment dates | Links memo to source contract |
| Parties | Exact legal names and roles | Prevents ambiguity |
| Commencement trigger | Clause/section defining effective date | Establishes legal basis |
| Conditions precedent | Condition, satisfaction date, supporting doc | Confirms date is operative |
| Notice mechanics | Required notices and completion date | Verifies procedural prerequisites |
| Obligation map | Obligations keyed to commencement | Clarifies performance impact |

## Drafting Workflow

1. **Extract** clauses on commencement, effectiveness, notices, and conditions precedent.
2. **Build date matrix**:
   - Execution date
   - Each condition-precedent satisfaction date with evidence
   - Notice date(s)
   - Determined commencement date
3. **Resolve discrepancies** — explain any gap between execution date and commencement date; distinguish automatic triggers from party-election mechanisms.
4. **Draft sections in order**:
   - Header / recitals
   - Party and agreement identification
   - Condition and notice verification
   - Commencement determination
   - Effect and legal consequences
   - Signature block / counterpart language
5. **Cite** the governing section/article for every factual assertion.

## Required Memo Sections

1. **Heading**: "Commencement Date Memorandum"
2. **Background**: Agreement title/date, transaction type, parties
3. **Fact Findings**: Condition-precedent status table; notice/consent status table
4. **Date Determination**: Exact date, day of week, and the rule or mechanism producing the date
5. **Effect**: What is operative from commencement; what is delayed or unaffected
6. **Execution**: Signature blocks with titles, representative authority, and counterpart/e-signature language

## Template

```text
COMMENCEMENT DATE MEMORANDUM

Date: [Insert date]

Re: [Full Agreement Name], dated [Execution Date] ("Agreement")

The parties confirm that the Agreement's commencement date is:
[Day, Month Day, Year], based on [section/article citation].

PARTY IDENTIFICATION
- [Party Name] – [Role]

CONDITIONS PRECEDENT AND NOTICE RECORD
| Condition | Required By | Satisfied On | Evidence | Status |
|---|---|---|---|---|
| [..] | [..] | [..] | [Doc refs] | [Met/Not Met] |

COMMENCEMENT DETERMINATION
- Basis: [Automatic trigger / party notice / election / other]
- Relationship to execution date: [Explain]
- Immediate obligation effects: [List]
- Deferred provisions: [List]

EFFECTIVE OBLIGATIONS
- Rent/payment start: [..]
- Covenants and performance schedule: [..]
- Term/timing provisions impacted: [..]

ACKNOWLEDGMENT
The parties acknowledge the foregoing as the official commencement date.

Signatures:
[Party/Representative]
[Title]
[Date]
[Counterparts/electronic execution language]
```

## Pitfalls and Checks

- **Never invent facts or dates** — leave placeholders and flag gaps.
- **Use agreement-consistent terminology only** — do not restyle party names or defined terms.
- **Unmet condition → stop finalization** — state the unmet condition clearly; do not finalize the memo.
- **Flag conflicts between documents** — do not reconcile by assumption.
- **Mirror the governing agreement's** counterpart/e-signature language; do not substitute standard boilerplate.
- **Verify e-signature enforceability** for non-U.S. or non-default jurisdictions. [VERIFY]
- Keep tone evidentiary and operational, not argumentative.

---

**Key changes made:**

- **Frontmatter**: Removed `tags` (not in the spec), tightened `description` with clearer trigger keywords while staying under 1024 chars.
- **Structure**: Reorganized from nested "Output Structure / Process" with redundant subsections into flat, scannable sections: Prerequisites, Core Inputs, Drafting Workflow, Required Memo Sections, Template, Pitfalls and Checks.
- **Eliminated duplication**: The original had "Mandatory Memorandum Sections" and "Non-Negotiables" and "Guidelines" as separate sections that overlapped — consolidated into "Required Memo Sections" and "Pitfalls and Checks."
- **Token savings**: Removed the "Why It Matters" column (merged as "Purpose"), trimmed the template party list, cut explanatory prose. Went from 132 lines to ~95.
- **Preserved legal accuracy**: All domain-specific content (condition-precedent tables, counterpart language, e-signature verification) retained intact.
