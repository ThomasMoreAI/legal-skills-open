# The wiki — layout, history, receipts

The wiki is an OKF v0.2 bundle: markdown notes with YAML frontmatter, readable without any tooling, diffable in git, openable in Obsidian. `note_types.md` says what a note *means*; this file is the mechanical contract — what exists on disk, what each file may contain, what every mutation records, and what the receipt prints.

## Bundle layout

```
<wiki>/
  index.md                  # Wiki Home: browse topics, notes, sources and review work
  log.md                    # human narration of what landed when, generated from the history
  sources/
    index.md                # human-browsable source catalogue
  review/
    index.md                # conflicts, gaps and proposed changes awaiting judgment
  privacy/                  # one directory per practice area
    index.md
    insights/               # Legal Insight notes
    checklists/             # Checklist notes
    traps/                  # Trap notes
    positions/              # Position notes — excluded from every export; never leave the machine
  .wiki/                    # machine sidecar — no .md file, ever
    manifest.json            # stable wiki id, schema and safe operational configuration
    history.jsonl           # append-only hash chain, one record per mutation
    versions/               # prior state of every note, per note (.mdv)
    pending/                # proposed amendments awaiting review (.mdp)
    review/queue.jsonl      # closed-enum review dispositions; no rejected prose
    automation.json         # legacy import idempotency; never an opt-in
    vocab.json              # canonical values for tags, practice areas, jurisdictions, document kinds
    severity.json           # review-triage severity table (editable; the confidentiality gate is not)
    lock                    # single-writer lock, held for the duration of a mutation
```

- **`index.md`** is the Wiki Home: it declares `okf_version: "0.2"`, routes the lawyer to topics, note types, sources, recent changes and review work, and is capped at 200 lines (a hard budget: an index nobody can read is not an index). Regeneration **always preserves the root frontmatter** and never lists `index.md` or `log.md` as concepts. Pending notes are excluded from its counts.
- **`log.md`** is narration for the lawyer: date-grouped, `## YYYY-MM-DD` headings newest first, no frontmatter and no `type`. It is *generated from the history and never parsed* — editing it changes nothing; regenerating it restores the record.
- **No `.md` file may ever exist anywhere under `.wiki/`.** Versions are `.mdv`, pending amendments `.mdp`, everything else JSON. That is what keeps the sidecar outside the bundle's note rules, and the conformance checker enforces it as a hard failure.
- **Path grammar**: each path segment matches `[A-Za-z0-9_][A-Za-z0-9_.\-]*`, and the characters `: * ? " < > |` are additionally forbidden so every wiki is writable on every platform. Body links are document-relative (`../traps/silent-subprocessor-lists.md`); paths in frontmatter resolve from the bundle root.
- A note edited outside the wiki's own commands is never dropped: unrecognized frontmatter keys are preserved verbatim in source order. It may be **renormalized** (canonical keys, canonical order) on its next mutation.

## The history — `.wiki/history.jsonl`

One JSON object per line, appended, never rewritten. Each record chains to the one before it, so a later edit to an earlier line is detectable.

```json
{"seq": 41, "ts": "2026-08-19T14:02:11Z", "op": "update_note",
 "note": "privacy/insights/art28-flow-down.md", "actor": "human:t.varga",
 "origin": "auto-built", "mode": "markup", "content_sha256": "…",
 "prior_content_sha256": "…", "prev_checksum": "…", "checksum": "…", "schema_version": 1}
```

| Field | Meaning |
|---|---|
| `seq` | monotonic record number, assigned under the lock; gaps are a defect |
| `ts` | UTC timestamp of the mutation, `YYYY-MM-DDThh:mm:ssZ` |
| `op` | the operation (enum below) |
| `note` | bundle-root-relative path the operation acted on (absent for `intake_skip`) |
| `actor` | `human:<id>` for a lawyer-issued command; old records may identify a legacy import adapter |
| `origin` | provenance of the note as it now stands: `seeded`, `auto-built` or `accepted` |
| `mode` | landing mode in force: `auto` or `markup` |
| `content_sha256` | digest of the note file after the operation |
| `prior_content_sha256` | digest before it (absent on `create_note`) |
| `prev_checksum` | the preceding record's `checksum` — the chain link |
| `checksum` | this record's own digest |
| `schema_version` | record format version, `1` |

**Operations.** `create_note` · `update_note` · `rename_note` · `merge_notes` · `delete_note` · `purge_note` · `accept_suggestion` · `decline_suggestion` · `rollback` · `intake_skip`.

**Historical skip records.** The legacy import operation `intake_skip` carries exactly one value from a closed set: `routine` · `no-new-rule` · `matter-specific` · `no-boundary-found` · `unreadable` · `over-cap`. These identifiers preserve existing history; they do not enable automatic saving.

Four rules hold the chain up:

1. **No free text ever enters the chain.** Skip and purge reasons are closed enum values mapped by the script, never sentences copied from a distillation. Diagnostic prose belongs in the session receipt and is not persisted.
2. **Digests are sha256 over canonical JSON** — sorted keys, no whitespace — never over concatenated fields.
3. **Renames never falsify the chain.** History records are immutable — a rename or merge appends a new record rather than rewriting old ones — so each record's digest covers the whole record (including the note path: tampering with attribution is detectable), and the chain still verifies after any rename or merge.
4. **Verification is non-cascading.** `verify` checks each record's own checksum, its link to the previous record, and sequence contiguity; one corrupt line is reported as one corrupt line, naming the note and the reason, not as a condemnation of everything after it.

**Deletion has two forms, and they are not the same act.** `delete` writes a tombstone: the note leaves the wiki and stays recoverable from its versions. `purge` is leak remediation: content *and* all versions are destroyed, irreversibly, and the chain keeps only the record that it happened.

## Versions — `.wiki/versions/`

Before every mutation the note's prior state is copied to:

```
.wiki/versions/<first 16 hex of sha256(note path)>/<UTC compact timestamp>.mdv
        e.g.  .wiki/versions/9f2c41ab77e0d315/20260819T140211Z.mdv
```

The directory name is a digest, not a path, so nested notes and long titles cannot produce unwritable filenames; the **human-readable note path is recorded in the file's first header line**. Two writes in the same second get a numeric suffix. No colons and no path separators appear in any version filename.

## Receipts, dry runs, and rollback

Every mutation prints one short receipt. A status view prints the full one:

> notes 47 · sources 31 · review 3 open · disputed 1 · stale 1 · unreviewed disk changes 2

"Unreviewed disk changes" is deliberate: a note edited by an editor or a sync tool is reported as drift, never silently promoted to lawyer-verified. `verified` is set only by an explicit act — accepting a suggestion, or verifying a note by name.

**`land`, `rename` and `delete` take `--dry-run`** and print exactly what they would do without touching a file; every mutating command prints a one-line receipt. **`rollback` additionally requires `--yes`**: it restores by replaying versions and records a single `rollback` entry rather than a wave of edits.

## Where the wiki lives, and what it may contain

Three places, three different rules, and they do not overlap. The **matter folder** may hold client facts; that is what it is for. The **wiki** holds gate-certified method and legal knowledge only. The **profile and playbook** hold neither — they hold preferences.

The wiki therefore lives **outside any matter folder**. It is cross-matter by nature, its path is chosen once and recorded in the registries (see "Finding the wiki" below), and it is found only through those registries — nothing scans a disk guessing for one. Manual work never needs a transcript cache. Optional host automation is off unless explicitly enabled, and when off it does not read transcripts or log prompt text.

**What this wiki may contain.** The wiki is a knowledge file, not a matter file. It contains no party names, no signatory names, no matter numbers, no client facts, and nothing from which a matter could be reconstructed — not in a note, not in a filename, not in the history, not in a skip reason. Every candidate passes the confidentiality gate before it lands, and the gate refuses rather than guesses. What survives is law and method: what a provision requires, what to check, what goes wrong, what argument held — statements that would be equally true if the lawyer had never had that client. Anything that fails is parked with a reason and is not written. If matter material does reach the wiki, `purge` destroys it and its versions; that is the remedy, and it is the only operation in the system that is not reversible.

## Finding the wiki (the registry)

Each wiki owns its authoritative `.wiki/manifest.json`: stable id, schema
version, and safe operational configuration. A user-level address book at
`~/.wiki/wikis.json` records only stable id, display name, canonical path,
default selection, and last-opened time — never note or source contents.

Resolution order is: explicit wiki, current-folder manifest, named registry
entry, registered default, sole registered wiki. If several valid wikis
remain ambiguous, ask. A registered wiki whose directory is gone is reported
by name and path; nothing is created at a stale path and nothing scans the disk
guessing for a wiki. A moved wiki is reconnected by matching its stable manifest
id, not by creating another wiki.

## One writer at a time

Two sessions can point at one wiki, so single-writer is enforced rather than assumed.

- **The lock.** `.wiki/lock` is created exclusively and held for the whole mutation window, carrying the process id, host, and timestamp. A second session is refused honestly: another session is writing this wiki. A lock older than ten minutes whose owner process is gone is broken automatically, with a notice on the receipt.
- **The history is appended line-wise** — one open, one line, one close — and `seq` is assigned under the lock, so a crash mid-run can never produce a half-written record.
- **Every other file is written to a temporary file and atomically replaced**, so no reader ever sees a half-written note or index. A wiki is meant to be open in an editor, and on Windows a replace onto a file that is held open is refused outright: the writer retries with backoff and, if it still cannot proceed, names the file that is locked instead of failing silently.

## Optional automation scope

See [automation settings](automation.md). Project locations are operational
metadata beside the user registry, never wiki knowledge or matter-source links.
A confirmed scope entry selects the exact root-list digest; the hooks verify it
before matching the task's working directory.
