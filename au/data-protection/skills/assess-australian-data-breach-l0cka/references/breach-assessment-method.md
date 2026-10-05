# Breach assessment method

## Minimum fact schema

Capture only what is necessary:

| Field | Questions |
| --- | --- |
| Time | When did the event possibly occur, when was it detected, when did each relevant entity become aware, and in which timezone? |
| Data | What data types, approximate volumes, protections and re-identification possibilities are supported by evidence? |
| People | Who may be affected, where are they located, and are any groups exposed to heightened harm? |
| Access and disclosure | Who may have accessed or received the data, for how long, and what evidence supports access, exfiltration or non-access? |
| Entities and systems | Which entity held or controlled the data, which vendors were involved, and which systems or critical services were affected? |
| Response | What containment, recovery, remedial action, preservation and prior notification has occurred, by whom and when? |
| Cyber extortion | Was a demand made, was any payment or benefit provided or planned, and which entity made or would make it? |

Do not place names, raw identifiers, credentials, secrets or live malicious
content in the assessment unless strictly necessary and approved for the tool.

## Candidate regime prompts

Invoke `$map-australian-cyber-incident-obligations` and use its versioned
registry to identify candidate rows. Verify, rather than assume:

- *Privacy Act 1988* (Cth): entity and information coverage, exceptions,
  eligible-data-breach elements, assessment, remedial action, multi-entity
  handling, statement and individual-notification requirements.
- State and Territory privacy or health-records regimes: public-sector,
  contracted-service-provider, health-information and mandatory-notification
  coverage where relevant.
- *Security of Critical Infrastructure Act 2018* (Cth) and instruments:
  covered asset/entity, incident category, reporting channel and timing.
- *Cyber Security Act 2024* (Cth) and instruments: cyber-extortion reporting
  coverage, threshold, trigger, recipient and timing.
- Sectoral requirements: APRA, telecommunications, My Health Record, Consumer
  Data Right, government contracts, professional obligations and other
  verified sector-specific duties.

Do not use a 30-day NDB assessment period as a notification deadline. Watch
note: a 72-hour Commissioner notification for eligible data breaches was
reported after the snapshot (24 September 2026 review, not yet confirmed
against the Attorney-General's Department) as proposed in the exposure draft
Privacy Amendment (Personal Data Protection) Bill 2026. It is a proposal only;
current law is unchanged, so do not apply it unless a later Act and its
commencement are verified. Preserve
the SOCI 12-hour and 72-hour branches, Cyber Security Act 72-hour payment
report, CPS 234/CPS 230 interaction, telco DFV two-day branch, CDR NDB-plus-ACSC
overlap and My Health Record section 26WD interaction where relevant. Route
present telecommunications security duties to SOCI, not superseded Part 14
TSSR duties.

Also identify contractual notices to customers, counterparties, vendors and
insurers. Keep them separate from statutory duties. Treat ACSC reporting or
other voluntary channels as voluntary unless a verified rule makes reporting
mandatory for the entity and event.

## Source and deadline controls

1. Use the official point-in-time legislation text as the controlling source.
2. Route Commonwealth checks through `$check-commonwealth-legislation` and NSW
   checks through `$check-nsw-legislation`.
3. Route material APP questions through
   `$check-australian-privacy-principles`; verify NDB provisions separately
   because they are not part of Schedule 1.
4. Label regulator guidance as guidance and record its publication/update date.
5. For every deadline, record the source provision, trigger fact, trigger time,
   timezone, unit, counting rule and calculation.
6. If any input is unresolved, report the earliest plausible deadline as an
   escalation marker, not a concluded deadline.

Case law is outside scope. Do not use it to define serious harm, knowledge,
reasonableness or any other legislative expression.

## Assessment discipline

- Give facts both for and against each threshold.
- Do not treat absence of confirmed exfiltration as proof that access did not
  occur.
- Do not treat encryption as an automatic safe harbour; record key exposure,
  encryption state and practical accessibility.
- Do not treat containment as remedial action sufficient to avoid notification
  without checking the statutory test.
- Do not merge different entities' awareness, assessment or reporting clocks.
- Do not promise privilege. Ask the supervising lawyer to establish the
  purpose, recipients and handling of the workstream.

The obligation-matrix and explicit evaluation pattern is informed by the
MIT-licensed Harvey AI `harvey-labs` data-privacy-cybersecurity task corpus.
No foreign-law answer, fictional scenario, client artefact or rubric answer is
part of this skill.
