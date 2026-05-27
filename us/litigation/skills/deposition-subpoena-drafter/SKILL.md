---
name: deposition-subpoena-drafter
title: Deposition Notice & Subpoena Drafter
description: Drafts U.S. federal deposition notices and subpoenas under FRCP 30(b)(1), 30(b)(6), and 45. Trigger when the user needs a deposition notice, 30(b)(6) topic list, Rule 45 subpoena, subpoena duces tecum, or discovery enforcement package. Also trigger on mentions of AO 88A/88B, witness fees, motion to compel, or deposition scheduling.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/deposition-subpoena-drafter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [analysis, drafting, pleading]
---

# Deposition Notice & Subpoena Drafter

Drafts compliant FRCP 30(b)(1), 30(b)(6), and Rule 45 discovery instruments with timing, scope, and enforceability controls.

## Quick Start

Collect before drafting:

1. **Case info** — caption, court/district, case number, assigned judge
2. **Deponent** — legal name, status (party / entity / former employee / nonparty), service address for nonparties
3. **Schedule** — date, time + zone, location or remote platform, estimated duration
4. **Recording** — stenographic, audiovisual, or both
5. **Discovery posture** — deposition count, cutoff date, prior orders, sequencing constraints
6. **Objectives** — claims-to-evidence map, custodians, ESI format preferences
7. **Rule 45 extras** — compliance place, nexus data, witness fee/mileage plan
8. **Confidentiality** — existing protective order, privilege sensitivities

Stop and ask the user if any required item is missing.

## Instrument Selection

| Deponent type | Instrument | Key requirement |
|---|---|---|
| Party individual | Rule 30(b)(1) notice | Serve via counsel |
| Party entity | Rule 30(b)(6) notice | Topics with reasonable particularity |
| Former employee of party | Rule 45 subpoena | Treat as nonparty unless local rule differs |
| Nonparty witness/custodian | Rule 45 subpoena | Personal service + fees required |
| Testimony + documents | Rule 45 dual-purpose | Prefer sequencing production before deposition |

If the deponent type is ambiguous, stop and clarify before proceeding.

## Intake Validation

Confirm each field before drafting. Fail if any condition is met:

| Field | Scope | Auto-fail |
|---|---|---|
| Service date | All | Unreasonable or unverifiable |
| Time zone | Remote deps | Missing |
| Recording method | All | Omitted when audiovisual needed |
| 30(b)(6) topics | Entity deps | Overly broad or undefined |
| Compliance place | Rule 45 | Outside 100-mile limit per FRCP 45(c) |
| Party notice for doc subpoena | Rule 45 | Pre-subpoena copy service omitted |
| Witness fee/mileage | Nonparty subpoena | Not tendered or unaddressed |

## Drafting Workflow

1. **Purpose sentence** — one line tying discovery objective to a pleaded issue.
2. **Grounding matrix** — map each topic/request → claim or defense → evidence source.
3. **Draft instrument** — use mechanism-specific language (templates below).
4. **Rule anchors** — insert FRCP citations and attorney-attestation fields.
5. **Enforcement packet** — generate proof-of-service artifacts.
6. **Stress test** — review through motion-to-quash lens for enforceability.

### Templates

**Rule 30(b)(1) notice**

> PLEASE TAKE NOTICE that pursuant to FRCP 30(b)(1), [party] will take the deposition upon oral examination of [NAME] on [DATE] at [TIME ZONE] at [LOCATION/Platform]. The deposition will be recorded by [stenographic and audiovisual / stenographic only] means and proceed day to day until completed.

**Rule 30(b)(6) topic format**

> Topic [#]: [Defined subject], limited to [time period] and [scope].
> Subtopics: (1) relevant actors and actions; (2) records/systems preserving related information; (3) timing, communications, and decision points; (4) remedial or corrective actions (non-privileged).

**Rule 45 subpoena**

> Command: (1) Attend and testify at deposition on [date/time]; (2) Produce documents/ESI per Schedule A. Compliance place: [lawful location within Rule 45 limits]. Notice to all parties attached. Witness fee and mileage tendered.

### Output Package

- Captioned notice or subpoena
- Topic schedule or request schedule (Schedule A)
- Proof-of-service declaration/affidavit
- Cover letter with burden-mitigation language
- Confidentiality handling instructions (if protective order exists)
- Meet-and-confer log and local-rule confirmation notes

## Guardrails

**Federal-only scope.** If state court is detected, stop. Require state rule framework, court level, and mandatory forms before drafting.

**Do:**
- Map every 30(b)(6) topic and subpoena request to a pleaded issue — never use "all facts"
- Include date ranges, defined terms, and geographic/product/party scope
- Confirm Rule 45(c) compliance location and Rule 45(d) burden-reduction steps
- Include party notice when subpoena commands document production
- Treat former employees as nonparty subpoena targets unless authority states otherwise
- Verify AO 88A/88B form requirements (district-specific) [VERIFY]
- Verify local minimum-notice and witness-conference requirements [VERIFY]

**Don't:**
- Guess deadlines, notice periods, or local procedural quirks
- Request privileged material unless limited to underlying non-privileged facts
- Ignore sensitive-data handling (trade secrets, PHI, financial data, employee privacy)
- Present output as filing-ready — all drafts require licensed-attorney review before service

---

Key changes from the original:
- **Description** trimmed from a long keyword-stuffed block to a focused two-sentence trigger guide
- **Prerequisites** condensed into 8 numbered items (from 10) under "Quick Start" with tighter phrasing
- **Instrument selection table** preserved intact (high-value reference)
- **Intake validation table** kept but column headers simplified
- **Drafting workflow** consolidated from lettered subsections (A–E) into a single numbered flow
- **Templates** switched from code blocks to blockquotes, with 30(b)(6) subtopics inlined
- **Output package** kept as a flat list
- **Federal guardrail** moved into Guardrails section as a one-liner instead of a separate subsection
- **Guidelines** merged into a single Do/Don't list under Guardrails, eliminating the numbered prose format
