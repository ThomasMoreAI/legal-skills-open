# Matter record template

Use this template for the approved record. Keep the human-readable sections and the provenance ledger together so a later reviewer can tell what was asserted, what came from a source, and what remains unknown.

```markdown
# Matter record: [matter title]

**Matter ID:** [stable ID — assigned once]
**Record version:** [integer]
**Record state:** preview | approved | superseded
**Created:** [date or unknown]
**Last updated:** [date or unknown]
**Approved by:** [person or unknown]
**As of:** [date or unknown]

## Identity and parties

- **Client / represented entity:** [name or unknown]
- **Internal business unit:** [name or not applicable]
- **Opposing / affected parties:** [exact names or unknown]
- **Known counsel / authority:** [names and roles or unknown]
- **Reference number:** [docket, claim, investigation, subpoena, or unknown]
- **How it arrived:** [source category]
- **Factual description:** [one or two sentences limited to supplied facts]

## Role, side, and forum

- **Representation role:** [enum]
- **Side:** [enum]
- **Forum:** [enum]
- **Court / tribunal / regulator / setting:** [exact value or unknown]
- **Jurisdiction / venue:** [value or unknown]
- **Governing law:** [value or unknown]
- **Stage:** [enum]

## Conflicts posture — human assertion

- **Status:** [cleared | pending | not-run | waived | unknown]
- **Assertion:** [what the human said]
- **Verified by / at:** [person and date or unknown]
- **Method:** [system, outside counsel, client list, informal, other, unknown]
- **Names / entities checked:** [list or unknown]
- **Scope and limitations:** [text]

## Engagement and authority

- **Engagement:** [not-engaged | proposed | signed | declined | unknown]
- **Scope / effective dates:** [text]
- **Lead counsel / team:** [text]
- **Who may instruct:** [text or unknown]
- **Who may sign communications:** [text or unknown]
- **Settlement / spend authority:** [text or unknown]
- **Escalation contact:** [text or unknown]

## Urgency and dates

| Date kind | Date / time / zone | Source | Basis | Urgency | Verified? |
|---|---|---|---|---|---|
| [received / served / response / objection / hearing / other] | [value] | [SRC-###] | [source-stated / user assertion / derived-pending-confirmation / unknown] | [overdue / imminent / near-term / future / unknown] | [yes / no / pending] |

**Urgent flag:** [none or `URGENT — HUMAN REVIEW NOW` with reason]
**No legal computation performed:** [yes]

## Preservation posture

- **Status:** [not-assessed | not-triggered-asserted | anticipated-asserted | hold-requested | hold-issued | released | unknown]
- **Trigger and date:** [text]
- **Owner / notice date:** [text or unknown]
- **Custodians / systems / range:** [text or unknown]
- **Known preservation gaps:** [text]
- **Next human decision:** [text]

## Current status

- **Status:** [inquiry | threatened | active | stayed | resolved | closed | unknown]
- **Status basis:** [user-asserted | source-stated | derived-pending-confirmation | unknown]
- **Verified by / at:** [person and date or unknown]
- **Current stage:** [enum]
- **Immediate need:** [text]
- **Related matters:** [IDs and relationship or none known]

## Open questions and blockers

- [question or blocker, owner if known, source IDs]

## Approved handoff to organize-case-docs

- **Matter ID / record version:** [values]
- **Approved sources:** [source IDs and locators]
- **Requested outputs:** [inventory / chronology / issue framework / claim chart / gaps / other]
- **Restrictions:** [privilege, confidentiality, disclosed-document, or use limits]
- **Unresolved items:** [list]
- **Handoff state:** [awaiting explicit user invocation | ready to offer]

## Provenance ledger

| Field | Value or section | Source IDs | Basis | Review state | Notes |
|---|---|---|---|---|---|
| [field name] | [value] | [SRC-###] | [user_asserted / source_stated / derived-pending-confirmation / unknown] | [confirmed by human / pending / unknown] | [limitations] |

## Action boundary

This record was prepared from the listed sources. No conflict search, engagement execution, deadline filing or calendaring, legal-hold issuance or release, contact, upload, service, or other external action was performed by this intake.
```

The template is not a substitute for a firm matter-management schema. If a host has a canonical schema, map these fields to it without dropping provenance, unknowns, blockers, or the action boundary.
