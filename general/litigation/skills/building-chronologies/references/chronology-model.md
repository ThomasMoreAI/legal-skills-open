# Chronology Model

Use this reference when building or reviewing a legal chronology.

## Purpose

A chronology is a working evidence map. It is not a statement of facts, submissions, or a merits conclusion. It lets the lawyer see sequence, sources, conflicts, and gaps.

## Core Fields

| Field | Meaning |
|---|---|
| `event_date` | date the event happened |
| `document_date` | date of the source document |
| `date_extracted_from` | where the date came from |
| `date_certainty` | `exact`, `approximate`, `date_uncertain`, `source_conflict` |
| `actor` | person/entity acting or speaking |
| `event` | short neutral event description |
| `source_identifier` | Bates, exhibit, file path, email id, bundle tab, URL, paragraph |
| `quote` | exact words supporting the event |
| `confidence` | `high`, `medium`, `low` |
| `significance` | `key`, `supporting`, `background`, `unknown` |
| `issue_tags` | legal or operational tags |
| `notes` | conflicts, assumptions, or follow-up |

## Event Date Discipline

Never collapse event date and document date.

Examples:

- Email sent on 12 March saying delivery failed on 10 March: `event_date = 2024-03-10`, `document_date = 2024-03-12`.
- Pleading dated 1 April alleging a 15 March promise: `event_date = 2024-03-15`, `document_date = 2024-04-01`, `confidence = low` unless source exists.
- File metadata date: not an event date unless metadata itself matters.

## Significance and Tags

Use significance sparingly:

- `key` - likely central to claim, defence, limitation, causation, quantum, or remedy.
- `supporting` - helps prove or contextualise a key point.
- `background` - sequence/context only.
- `unknown` - cannot assess without case theory.

Useful issue tags:

- `breach`
- `notice`
- `limitation`
- `causation`
- `quantum`
- `disclosure_target`
- `privilege_review`
- `pleading_source`
- `witness_follow_up`
- `expert_issue`
- `procedural_deadline`

## Source Conflicts

Do not decide which account is true. Group competing accounts under the same event where helpful and mark:

- `source_conflict` - sources materially differ.
- `later_recollection` - later witness account conflicts with contemporaneous record.
- `pleaded_only` - appears in pleading but no underlying document found.
- `document_gap` - event referred to but source document absent.

## Gaps

The gaps section is part of the deliverable. Include:

- missing custodians,
- missing date ranges,
- missing correspondence threads,
- documents referenced elsewhere but not supplied,
- likely disclosure targets,
- events that require primary-source confirmation.

## Narrative Conversion

Do not convert a working chronology into advocacy prose unless asked. If asked, preserve citations and filter/flag disputed or low-confidence entries.
