---
name: legal-hold-lsdisconzi
title: Legal Hold
description: Issue, refresh, release, or report on evidence-preservation / litigation-hold demands. Drafts preservation notices and judicial preservation requests, tracks custodians, and calendars refresh. Use when the user says "issue a hold", "preserve the evidence", "preservation notice", "refresh hold", "release hold", or asks for hold status.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/legal-hold
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Legal Hold

A plaintiff-side, offensive preservation workflow. The matter rarely controls the critical evidence — counterparties and third parties do. This workflow demands that they preserve it and escalates to judicial preservation orders when a notice is not enough. It owns four phases: **issue → refresh → (release) → track**. It names no party itself; targets and custodians come from the matter.

**Time-limited evidence is the priority.** Recordings, CCTV, and operational logs are often on routine deletion cycles (commonly 30–90 days). Until a preservation demand is on record — and ideally a judicial order issued — every run treats any time-limited item the matter's evidence gap analysis flags as the priority 🔴 Blocking item.

## Running this skill

1. **Load configuration.** Read the configured matter profile and firm profile from the plugin config directory (see CLAUDE.md `## Configuration Location`). If a file is missing, or a critical field still shows `[PLACEHOLDER]`, STOP — tell the attorney: "This plugin needs setup. Run the `cold-start-interview` skill."
2. **Apply the frame.** The Plugin Operating Rules, Shared Guardrails, Decision posture, Jurisdiction recognition, Retrieved-content trust, and Ontology Governance sections of CLAUDE.md govern this skill. The workflow below is a FLOOR, not a ceiling.
3. **Resolve vault paths.** Every `{vault root}` and `matters/…` reference resolves against `## Vault location` / `## Matter workspaces` in CLAUDE.md. Never hard-code an absolute path.
4. **Determine active packs.** Read which jurisdiction packs the matter declares (matter profile `## Packs`).
5. **Apply the work-product header** to internal deliverables; strip it from any external notice.
6. **Run the workflow below.**
7. **Close** with the `⚠️ Reviewer note` block and the next-steps decision tree from CLAUDE.md `## Outputs`.

---

## Load context

- The matter ledger (`matters/_log.yaml`) and `matters/<matter-slug>/history.md` — the append target for hold events.
- `{vault root}/03-evidence/` — the evidence registry; identifies what the matter holds vs. what a counterparty holds.
- The output of the `evidence-integrity-monitor` agent and the `evidence-chain-verification` skill — both produce the gap matrix this workflow turns into preservation demands. Consume theirs; do not re-derive it.

## Jurisdiction note — preservation is a different mechanism per forum

Preservation duties and the instruments that compel them differ by forum. Never collapse them. For each jurisdiction the matter declares, read the preservation mechanisms from its jurisdiction pack `procedural-rules.yaml` — typically an out-of-court preservation notice and a pre-suit judicial measure to secure evidence at risk. Every step in a foreign jurisdiction is tagged `[direito estrangeiro — verificar com co-counsel]` and routed to local counsel before issuance.

## Modes

The command takes a flag: `--issue | --refresh | --release | --status`. Default (no flag) → prompt.

### `--issue` — first preservation demand

**Priority order.** Issue in descending risk order: time-limited recordings/CCTV first (pair with a judicial preservation request the same week), then official records, then counterparty database entries, then internal SOPs and contested documents, then personnel records, then audio originals and call logs. Take the risk ranking from the evidence gap analysis.

**Inputs to capture per target:** custodian (entity and, where known, the department or named actor); scope (specific enough that the custodian cannot claim ambiguity, broad enough to catch derivative copies — backups, exports, mirrors); date range; spoliation framing stated per the forum; deadline to confirm preservation (typically 5 business days).

**Draft the preservation notice** in the custodian's jurisdiction language (per the jurisdiction pack `language-defaults.yaml`). It is an external deliverable — strip the work-product header, apply the destination check, keep the reviewer note on the internal copy only. The notice: identifies the firm and client; states that litigation is in prospect; demands integral preservation, without alteration, deletion, overwriting, or discard, of an enumerated scope; states that the preservation covers originals, copies, backups, exports, and derivative versions in any medium; states the spoliation consequence per the forum; and requests written confirmation within the deadline, naming the custodian.

**Judicial preservation request — when a notice is not enough.** For any item the integrity monitor flags as actively at risk, draft the judicial measure alongside the notice, per the jurisdiction pack: state the urgency (deletion cycle), the merits basis (the evidence is central), and the prejudice from delay (it will not exist by the time the main suit is served). Route any foreign-jurisdiction measure to local counsel.

**Writes:**
- `demand-letters/preservacao-<target>-<jurisdiction>-<yyyy-mm>/draft-v1.docx` via the `docx` skill (one folder per target).
- For judicial measures: a petition skeleton in the same folder, tagged `[direito estrangeiro — verificar com co-counsel]` for any foreign jurisdiction.
- Appends a dated event to `matters/<matter-slug>/history.md`.
- Updates `matters/_log.yaml` — adds or refreshes a `legal_hold:` block on the matter row (issued flag, date, targets, scope, custodians, judicial-measure status, last/next refresh, released).

### `--refresh` — periodic reaffirmation

Default refresh cadence: 90 days (tighter where time-limited evidence is at risk). When `next_refresh < today`, or on manual invocation, draft a refresh notice that restates the demand, lists new items surfaced since issuance, and requests re-confirmation of custody. Flag any target that has not confirmed preservation in writing, any stale custodian contact, and any at-risk item still unconfirmed — an unconfirmed hold on time-limited evidence escalates to a judicial measure, it does not simply roll over. Writes the next-version notice, a `history.md` entry, and updated refresh dates in `_log.yaml`.

### `--release` — close the hold

Release only when the matter is genuinely over (see the `matter-close` skill) and no appeal or related proceeding remains live. Premature release is a spoliation exposure — confirm with the attorney. Capture release authority, date, and retention instruction; draft a one-paragraph release notice; update `_log.yaml` → `released`; append `history.md`.

### `--status` — preservation status report

Read `_log.yaml` and the latest `evidence-integrity-monitor` output. Produce a status report: a table of active holds (target, issued, confirmed?, last/next refresh, judicial measure, state); an immediate-attention section (at-risk time-limited evidence, targets with no written confirmation, overdue refreshes); and a reconciliation of covered items against the evidence registry (items a counterparty holds with no hold issued).

## Integration

- **`evidence-integrity-monitor` (agent)** — produces the gap matrix and flags at-risk evidence each run. This workflow consumes that output. A 🔴 from the monitor carries as a 🔴 floor here.
- **`evidence-chain-verification` (engine)** — its gap analysis is the input to `--issue`. Run it first if no recent gap matrix exists.
- **`demand-draft`** — preservation notices share the `demand-letters/` workflow; a preservation demand often precedes the substantive demand letter to the same defendant.
- **`deadline-tracker` (agent)** — the `next_refresh` date and the matter's prescription clocks are tracked there.

## What this skill does not do

- **Preserve the evidence itself.** It demands preservation; the custodian preserves. It cannot reach into a counterparty's systems.
- **File the judicial measure.** It drafts the petition skeleton and routes foreign measures to local counsel. An attorney files.
- **Decide foreign procedure.** Every foreign-jurisdiction step is flagged `[direito estrangeiro — verificar com co-counsel]`.
- **Conclude spoliation occurred.** Per Invariant I-1, missing or destroyed evidence is an allegation and a flag, never an adjudicated finding.
- **Serve anything.** It drafts `.docx`; the attorney serves per forum.
