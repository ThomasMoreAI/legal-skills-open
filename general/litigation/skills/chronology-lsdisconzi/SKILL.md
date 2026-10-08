---
name: chronology-lsdisconzi
title: Chronology Builder
description: Build the canonical incident timeline from all transcript timestamps, evidence metadata, and violation records. Produces a court-ready chronology with every entry anchored to specific evidence.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/chronology
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Chronology Builder

Constructs the complete, evidence-anchored chronology of the matter's incident(s). Every timeline entry must be sourced to a specific transcript segment, document, or verified metadata. This is a deterministic engine — given the same sourced events it produces the same ordered timeline. It names no party or case.

## Running this skill

1. **Load configuration.** Read the configured matter profile and firm profile from the plugin config directory (see CLAUDE.md `## Configuration Location`). If a file is missing, or a critical field still shows `[PLACEHOLDER]`, STOP — tell the attorney: "This plugin needs setup. Run the `cold-start-interview` skill."
2. **Apply the frame.** The Plugin Operating Rules, Shared Guardrails, Decision posture, Jurisdiction recognition, Retrieved-content trust, and Ontology Governance sections of CLAUDE.md govern this skill. The workflow below is a FLOOR, not a ceiling.
3. **Resolve vault paths.** Every `{vault root}` reference resolves against `## Vault location` in CLAUDE.md. Never hard-code an absolute path.
4. **Apply the work-product header** from CLAUDE.md `## Outputs` to every internal deliverable; suppress it on externally-facing output per Quiet mode.
5. **Run the workflow below.**
6. **Close** with the `⚠️ Reviewer note` block and the next-steps decision tree from CLAUDE.md `## Outputs`. Run the `ontology-validate` skill on the output before it reaches a court or counterparty.

---

## Workflow

### 1. Source aggregation
Pull timestamped events from:
- All transcript files in the matter (segment timestamps from rendered HTML)
- Evidence registry metadata (`created_at_utc` fields)
- Violation records (`incident_timestamp` fields)
- Client contemporaneous notes
- Counterparty records (booking, scheduling, or operational logs)

### 2. Timeline construction — three precision layers
- **Layer 1 — Hard timestamps** (transcript segment start times, scheduled times).
  Format: `YYYY-MM-DD HH:MM:SS TZ — <event> (<evidence anchor>)`
- **Layer 2 — Approximate timestamps** (inferred from context, ~5–15 min precision). Prefix with `~`.
- **Layer 3 — Date-level events** (known date, unknown time).

### 3. Evidence anchoring
Every entry cites at least one evidence source:
- `(<transcript-key> seg-N at MM:SSs "verbatim text")` — transcript-anchored
- `(<evidence-id>)` — evidence registry item
- `(<violation-id>)` — violation record
- `[client notes, date]` — contemporaneous record

### 4. Gap identification
Flag unknown-duration events, missing timestamps, incomplete transcript coverage, and unrecorded interactions.

### 5. Multi-incident output
When the matter spans more than one incident, present incidents on parallel tracks — one column per incident — so cross-incident timing is visible.

### 6. Output formats
- **Narrative chronology** — prose timeline for briefs and demand letters
- **Tabular chronology** — sortable table: Date/Time, Event, Violation, Evidence, Actor
- **Visual timeline** — HTML dashboard with incidents on parallel tracks
- **Gap report** — all unverified timestamps, missing evidence, open temporal questions

## Integration

- After building the chronology, run `transcript-segment-analysis` to verify all timestamped claims.
- Run a `violation-analysis` sweep to sync violation records with the timeline.
- Run `claim-chart` to align claim elements with chronological events.

## Guardrails

- `~` marks approximate times — never present them as exact.
- Every entry must have an evidence anchor — no unsourced timeline claims.
- Present each event in its source timezone and label the UTC offset.
- Canonical dates from violation records take precedence over other sources.
- **Ontology compliance:** outputs must satisfy the litigation-relevant error codes in `core/ontology/error-catalog.md`. If an invariant violation is detected, flag with `[ONT-ERROR: <code>]` and do not produce confident output. I-1 is absolute: no conclusory language.
