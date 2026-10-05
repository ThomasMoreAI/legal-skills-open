---
name: matter-workspace-rbh227
title: /matter-workspace
description: Manage matter workspaces — create, list, switch, close, or detach (practice-level). Keeps one client or engagement's context separate from every other for multi-client practitioners. Use when the user wants to open a new matter, switch matters, list matters, close/archive a matter, or work at practice-level only.
author: rbh227
author_url: https://github.com/rbh227/privacy-counsel-plugin/tree/main/skills/matter-workspace
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

<!-- MODIFIED from anthropics/claude-for-legal (Apache-2.0), commit 4a6c651 — see VENDORED.md.
Changes: configuration redirected to this plugin's pre-filled practice playbook (../../profile/privacy-playbook.md),
setup/cold-start gates removed (playbook is always configured), /privacy-legal:* command handoffs replaced
with natural-language skill references, mutable state moved to ~/.claude/privacy-counsel/, practice overlay appended. -->

# /matter-workspace

Practitioners work across multiple clients and matters. A matter workspace keeps one client or engagement's context separate from every other. This skill manages those workspaces.

## Subcommands

- `the matter-workspace skill new <slug>` — create a new matter workspace, run a short intake, write `matter.md`
- `the matter-workspace skill list` — list matters with status and active flag
- `the matter-workspace skill switch <slug>` — set the active matter
- `the matter-workspace skill close <slug>` — archive a matter (move to `~/.claude/privacy-counsel/matters/_archived/`, never delete)
- `the matter-workspace skill none` — detach from any active matter, work at practice-level only

## Instructions

1. Read `../../profile/privacy-playbook.md` → `## Matter workspaces`. For the partner this is Enabled ✓ and SILENT: infer the active matter from context, create `~/.claude/privacy-counsel/matters/<matter-slug>/` on demand, and never ask the partner to manage workspaces.
2. Use the subcommand logic below.
3. Dispatch on the first token of `$ARGUMENTS`:
   - `new` → run the intake interview, write `~/.claude/privacy-counsel/matters/<slug>/matter.md`, seed `history.md` and `notes.md`, and append the matter (slug + client + status open) to the `## Matters` registry in `~/.claude/privacy-counsel/state.md`.
   - `list` → enumerate `~/.claude/privacy-counsel/matters/*/matter.md`, print a table, mark the active matter.
   - `switch` → treat the named matter as this SESSION's active matter (session-scoped only; never persisted).
   - `close` → move `~/.claude/privacy-counsel/matters/<slug>/` to `~/.claude/privacy-counsel/matters/_archived/<slug>/`, log the close date in `history.md`.
   - `none` → this session uses practice-level context only.
4. Show the user what changed and confirm before writing.

## Notes

- The skill never reads across matters — `Cross-matter context` is `off` (playbook `## Matter workspaces`); client confidentiality between matters is absolute.
- Archiving is not deletion — closed matters remain readable for retention/conflicts purposes.
- Slugs are lowercase with hyphens. If a slug is reused across archived and active, the archived one is preserved under `_archived/<slug>/`.

---

# Matter Workspace

Multi-client practitioners (private practice — solo, small firm, large firm) work across many matters. Context from one must not leak into another. This skill is the thin file-management layer that makes that true.

**Default state for the partner is ON and silent.** Matters isolate client contexts (cross-matter context OFF — client confidentiality between matters is absolute). The machinery stays invisible: no commands, no filing requests, no narration of workspace state.

## Storage layout

All matter data lives under:

```
~/.claude/privacy-counsel/
├── state.md                        # matter registry + practice-level notes (no active pointer)
└── matters/
    ├── <slug>/
    │   ├── matter.md               # client, counterparty, matter type, key facts, overrides
    │   ├── history.md              # dated log of events, decisions, drafts, reviews
    │   ├── notes.md                # free-form working notes
    │   └── outputs/                # skill outputs for this matter (optional subfolder)
    └── _archived/
        └── <slug>/                 # closed matters — readable but not active
```

Slugs are lowercase with hyphens. Examples: `acme-msa-2026`, `zenith-renewal`, `vendor-xyz-nda`.

## Active matter is SESSION-SCOPED

There is NO persisted active-matter pointer. Each session resolves its own
matter from its own conversation, by exact, unique client/matter match
against the registry in `~/.claude/privacy-counsel/state.md` (`## Matters` list;
create the file with an empty list if missing). Concurrent Cowork sessions
on different clients therefore can never contaminate each other through
shared state. When two matters could both fit the context (shared
counterparties, similar names), STOP and confirm which matter before
reading or writing any matter file. `state.md` holds only: the matter
registry (slug + client + status) and practice-level (non-client) notes —
never an active pointer, never client facts.

## Subcommand logic

### `new <slug>`

1. Confirm slug is not already present in `matters/<slug>/` or `matters/_archived/<slug>/`. If reused, ask the user to pick a different slug.
2. Run the intake interview:
   - **Client** (the party we represent, or the internal business unit if in-house)
   - **Counterparty** (the other side — may be multiple)
   - **Matter type** (read the plugin's practice profile for typical categories; for privacy-legal: PIA (processing activity) | DPA review | DSAR | regulator inquiry | transfer-mechanism review | incident | other)
   - **Confidentiality level** (standard | heightened | clean-team — heightened prompts extra care in cross-matter settings)
   - **Key facts** (2–5 sentences: what this matter is about, who the stakeholders are, what's at stake)
   - **Matter-specific overrides to the practice playbook** (e.g., "client requires 24-month LoL cap not 12", "counterparty is a strategic partner — relationship-preserving tone")
   - **Related matters** (slugs of any connected matters)
3. Write `matters/<slug>/matter.md` using the template below.
4. Seed `matters/<slug>/history.md` with a single "Opened" entry.
5. Create an empty `matters/<slug>/notes.md`.
6. Do **not** auto-switch to the new matter. Ask: "Want to switch to `<slug>` now? (`the matter-workspace skill switch <slug>`)"

### `list`

Enumerate `matters/*/matter.md`. Read each file's front-matter or first few lines to extract status. Print a table:

| Slug | Client | Matter type | Status | Opened | Active |
|---|---|---|---|---|---|

Mark the currently-active matter with `*`. Include `_archived/*` under a separate "Archived" heading if any exist.

### `switch <slug>`

1. Confirm `matters/<slug>/matter.md` exists. If not, offer `the matter-workspace skill new <slug>`.
2. Use `<slug>` as this session's active matter (session-scoped; nothing persisted).
3. Show the user the matter.md summary so they can confirm they're on the right matter.

### `close <slug>`

1. Confirm `matters/<slug>/` exists.
2. Append a "Closed" entry to `matters/<slug>/history.md` with today's date.
3. Move `matters/<slug>/` → `matters/_archived/<slug>/`.
4. Update the matter's status to `closed` in the `state.md` registry; this session drops it as active.

### `none`

Drop the session's active matter and use practice-level context only. Confirm with the user.

## `matter.md` template

```markdown
[WORK-PRODUCT HEADER — per `../../profile/privacy-playbook.md` `## Outputs`]

# Matter: [Client] — [short description]

**Slug:** [slug]
**Opened:** [YYYY-MM-DD]
**Status:** active
**Confidentiality:** [standard / heightened / clean-team]

---

## Parties

**Client:** [name]
**Counterparty:** [name(s)]

## Matter type

[vendor MSA | customer agreement | NDA | SaaS subscription | amendment | renewal | other — with one-line rationale]

## Key facts

[2–5 sentences. What this matter is about. Who the stakeholders are. What's at stake. What makes it different from the default playbook.]

## Matter-specific overrides

*Any deviation from the practice-level playbook that applies to this matter
and only this matter. This is rung 2 of the ladder in the playbook's
`## Overrides` — it beats the practice-level overrides file, so it is where
a client's own requirement lives.*

**One position per line, `key: value`, same keys the practice overrides use
(`../../commands/setup.md` lists them).** The precedence contract compares
sources by key: a position written as prose here is read as a note and is
NEVER applied as an override, which means the client's actual requirement
would silently lose to the partner's house default. Write the key.

```
dpa/liability-cap: 24 months' fees — client requires, not house standard 12
governing-law/forum: English law
```

### Notes

*Prose that explains or qualifies the positions above. Read for context,
never applied as an override.*

- [e.g., "Tone: relationship-preserving — counterparty is a strategic partner."]

## Related matters

- [slug — one line why related]

## Notes on confidentiality

[If heightened or clean-team, describe why. Who may see matter files. Whether cross-matter context is permissible even if globally on.]
```

## `history.md` seed

```markdown
# History: [Client] — [short description]

Append-only event log. Most recent at top.

---

## [YYYY-MM-DD] — Matter opened

Intake completed. Slug: `[slug]`. Status: active.
[Any initial context worth preserving beyond matter.md — e.g., "Opened in response to inbound MSA draft from [counterparty]."]
```

## Cross-matter context

The playbook's `## Matter workspaces` sets `Cross-matter context: off` (permanent for this practice): a skill working in matter A **never reads** files in `matters/B/` for any other `B`. Period. This is the confidentiality guarantee the setting exists to provide.

When it's `on`, a skill may read files across matter folders only when the user explicitly asks it to (e.g., "compare our position on liability caps across the last five vendor matters"). Even when `on`, the default is to load only the active matter unless the user asks for a cross-matter view.

## What this skill does not do

- **Run a conflicts check.** Conflicts are the practitioner's/firm's job; the intake captures what the user declares.
- **Enforce retention.** Closing archives a matter; it does not delete. Retention policy is out of scope.
- **Auto-route outputs.** The substantive skill decides where to write; this skill tells it *which folder* is active, not what to put in it.
- **Decide whether cross-matter is appropriate.** It reads the flag and obeys.

## practice overlay

- Output in partner mode: bottom line first, prioritized, short. The
  partner can ask to dive deeper ("explain" / "dive deeper" / "full
  analysis").
- Report only issues that matter. If the workflow surfaced 30 comments and
  4 are meaningful, they see 4 (say "N minor points available on request").
  Materiality invariant: anything legally material always survives the cut.
- Distinguish negotiable points from low-value comments; recommend, don't
  enumerate.
- The playbook at `../../profile/privacy-playbook.md` is pre-configured;
  never prompt for setup. If an entry is missing or unfitting, state the
  assumption and proceed; matter documents override playbook defaults.
- Never create administrative work for the partner. Workspace/state maintenance is
  silent (see the playbook's Matter workspaces section).
- All guardrails in this skill and the playbook's Shared guardrails remain
  in force.
