# Document-review data contracts

Exact shapes for every artifact the scripts exchange. Scripts validate on read and write. Deterministic artifacts carry no timestamps, no absolute paths, and no machine names; run metadata lives in the run log, never in these files. Keys sort alphabetically on serialization (`json.dumps(..., sort_keys=True, indent=2)`), documents sort by `id`.

## manifest.json (build_manifest.py)

```json
{
  "corpus_id": "d19d7b47f21b42c1",
  "root_label": "<basename of the data-room folder>",
  "documents": [
    {
      "id": "sha256:9f3a1c04b2d7",
      "path": "3.2 Supplier Agreements/acme-msa.pdf",
      "bytes": 184223,
      "ext": "pdf",
      "pages": 42,
      "readability": "native",
      "text_yield": 0.97
    }
  ],
  "counts": {
    "files": 15,
    "native": 12,
    "scanned": 2,
    "suspect": 0,
    "encrypted": 0,
    "corrupt": 1
  }
}
```

- `id`: `sha256:` plus the first 12 hex of the file's SHA-256. The stable doc ID everywhere.
- `corpus_id`: the first 16 lowercase hexadecimal characters of SHA-256 over
  the newline-joined, sorted unique document IDs. Byte-duplicate paths and
  path renames do not change it; a content change does. The field is additive:
  consumers accept older manifests without it.
- `path`: relative to root, forward slashes.
- `pages`: integer for paginated formats, null otherwise.
- `readability`: `native` (text_yield >= 0.5), `scanned` (extractable pages but yield < 0.5), `suspect` (an objective truncation or byte-size receipt failed), `encrypted`, `corrupt`.
- Invariant: `counts.files == len(documents)` and equals the walk count; the script exits nonzero otherwise.

One ingestion identified by `corpus_id` may support any number of analysis
frames and runs. Analysis-run artifacts reference ingestion artifacts by path;
the manifest, message map, cluster map, and gap report remain frame-free. No
registry or database is implied.

DOCX, XLSX, and EML use deterministic standard-library text surfaces. DOCX
extracts body text only; tracked changes, comments, and embedded objects are
not interpreted. XLSX emits one non-empty cell per line as
`Sheet name!A1: value` in declared sheet order and stored cell order; formulas
are not evaluated, page is null, and the cell reference in the line is the
location anchor. EML emits From/To/Cc/Date/Subject followed by decoded plain
text, or visible HTML when no plain part exists; attachments are not expanded.

## read-plan.json and reader checkpoints

`extract_metadata_prep.py` writes regex evidence to `regex-metadata/`, never to
the canonical `metadata/` directory. It writes one read-plan row per unique
content ID with aliases, canonical path, `read_mode` (`text | image`), a
path-free `reader_input` for text mode, and one of these dispositions:

- `reader-required`: a fresh document read is mandatory.
- `regex-audit`: a bankable regex record selected by the frozen 10 percent audit.
- `regex-banked`: all identity claims and populated references have receipts.
- `deferred-to-review`: readable and fully in review scope, but the standalone
  canonical-metadata read is deferred because units are already derivable and
  no approved consumer needs the identity inventory.
- `parked-unreadable`: no worker call; the coverage lane records the reason.

The fifth disposition is legal only when the plan has top-level
`"deferral_policy": "defer-non-unit-metadata"`, units are header-derived
threads or singletons, the invoking workflow does not assemble families from
this metadata, and the lawyer explicitly approves the displayed deferred lane
at Gate 1. The field is omitted entirely for ordinary plans. Diligence never
defers because canonical metadata defines its families. Deferral does not
replace privilege holds, finding receipts, or any human gate.

`scope.kind` is `manifest` for diligence. `/docreview` passes `messages.json` to
`--include-ids`, producing an `include-ids` scope containing only
`non_messages`. The summary reports extracted text characters and an explicit
four-characters-per-token input estimate; current worker pricing is supplied
separately by the orchestrator after the user or host selects a model.

The host orchestrator checkpoints one schema-valid raw result per ID using
`metadata-reader.schema.json`. It may fan out workers when the host supports
that capability and must use the same one-document contract sequentially when
it does not. `merge_metadata_reads.py` is the only writer of canonical
`metadata/`; it fails closed on a missing, malformed, wrong-ID, or unverified
required/audit result. `metadata-merge-report.json` is the receipt for reader
coverage and audit disagreement. `plan_id` binds the exact scope, routing,
dispositions, audit mode, and estimates; the merger recomputes it before
accepting any checkpoint.

The metadata merge report proves the partition: planned rows equal fresh
reader results accepted plus regex banked plus deferred plus parked. A reader
checkpoint present for a deferred ID is refused because it contradicts the
plan.

If any audited identity or reference field disagrees, the merge report sets
`requires_full_regex_read: true` and invalidates every un-audited banked
record. The orchestrator reruns prep with `--expand-bank`, dispatches those
isolated reads, and merges again before relationship mapping.

Text workers receive `reader-inputs/<hash>.txt`, never the source path or
filename. Those temporary excerpts contain the opening pages plus tail region
and are deleted with the run dataset. Image-mode rows have a null input path;
the host renders the opening pages and tail page without presenting the source
filename as evidence. A valid image checkpoint is written to
`image-metadata-review.json`, not silently discarded. Its transcription and
page cite enter canonical metadata only when `merge_metadata_reads.py` receives
an explicit lawyer receipt shaped as
`{"confirmed":[{"doc_id":"sha256:...","by":"lawyer"}]}`.

Deferred rows also have a null input path. The merger writes a blank canonical
record for every deferred ID with status `deferred-to-review`, null identity
fields, and empty arrays. The finding pass never backfills that record.
Upgrading it requires rerunning prep, optionally scoped with `--include-ids`,
without the deferral flag. A partial un-deferral merge must write to a fresh
metadata run directory; stale-file detection intentionally refuses an output
directory that still contains records outside the scoped plan. No consumer may
treat a deferred placeholder as metadata; `block_candidates.py` fails closed
if any is present.

## metadata/<id>.json (canonical output from merge_metadata_reads.py)

```json
{
  "id": "sha256:9f3a1c04b2d7",
  "doc_type": "amendment",
  "title": "Amendment No. 2 to Master Services Agreement",
  "parties": ["Acme Corp", "Bolt Industries LLC"],
  "dated": "2023-01-05",
  "references": [
    {
      "kind": "parent-agreement",
      "text": "Master Services Agreement dated January 5, 2023 between Acme Corp and Bolt Industries",
      "quote": "this Amendment No. 2 to the Master Services Agreement dated January 5, 2023",
      "page": null,
      "source": "model-read",
      "gap_eligible": true
    }
  ],
  "evidence": {
    "doc_type": {"quote": "AMENDMENT NO. 2", "page": null, "source": "model-read"},
    "title": {"quote": "AMENDMENT NO. 2 TO MASTER SERVICES AGREEMENT", "page": null, "source": "model-read"},
    "dated": {"quote": "January 5, 2023", "page": null, "source": "model-read"},
    "parties": [
      {"value": "Acme Corp", "quote": "Acme Corp", "page": null, "source": "model-read"},
      {"value": "Bolt Industries LLC", "quote": "Bolt Industries LLC", "page": null, "source": "model-read"}
    ]
  },
  "status": "complete"
}
```

- `source`: `regex`, `model-read`, or `image-read-human-confirmed` (`model`
  remains accepted for legacy artifacts). Text claims carry an exact quote and
  null page. Image claims carry a transcription and positive page, and their
  source records that a lawyer, not a script, confirmed them. The verifier
  blanks failed text claims before setting `quote-unverified`.
- `gap_eligible`: true only when the quote identifies a distinct instrument that should exist separately. Bare SEC exhibit labels and internal attachments are false.
- `status`: `complete`, `metadata-incomplete`, `quote-unverified`, or
  `deferred-to-review`. Parked files stay in the manifest counts.
- `dated`: ISO date or null.

## candidates.json (block_candidates.py)

```json
{
  "blocks": [
    {
      "block_id": "b001",
      "basis": ["party:acme corp", "title:master services agreement"],
      "members": ["sha256:9f3a1c04b2d7", "sha256:aa10b2c9d001"]
    }
  ],
  "pairs": [
    {"a": "sha256:9f3a1c04b2d7", "b": "sha256:aa10b2c9d001", "block": "b001"}
  ]
}
```

## families.json (build_families.py)

Before the final family build, `build_families.py --edge-plan-out` writes one
stable job for each candidate pair still disconnected after rule resolution.
The host gives an isolated resolver only the two named canonical metadata
records and checkpoints `edge-resolver.schema.json` as `<job_id>.json`.
`merge_edge_results.py` binds each result to the metadata digest and accepts a
linked edge only when its quote is an existing receipt in the declared source
record. Missing, malformed, not-linked, and unresolved decisions remain in
`edge-merge-report.json`; only accepted links enter `model-edges.json`.

```json
{
  "families": [
    {
      "family_id": "sha256:aa10b2c9d001",
      "members": [
        {"id": "sha256:aa10b2c9d001", "role": "base", "order": 0},
        {"id": "sha256:9f3a1c04b2d7", "role": "amendment", "order": 1}
      ],
      "edges": [
        {
          "src": "sha256:9f3a1c04b2d7",
          "dst": "sha256:aa10b2c9d001",
          "relation": "amends",
          "provenance": "rule",
          "evidence_source": "model-read",
          "quote": "this Amendment No. 2 to the Master Services Agreement dated January 5, 2023"
        }
      ]
    }
  ],
  "orphans": ["sha256:0c77d1e2f3a4"]
}
```

- `relation`: `amends | sow-under | schedule-of | guarantees | supersedes | duplicate-of`.
- `provenance`: `rule` (deterministic resolver) or `model` (edge resolver).
- `evidence_source`: `regex | model-read | image-read-human-confirmed |
  model-edge`. A rule resolved from reader evidence remains a rule, but Gate 1
  treats it as proposed until the lawyer confirms it.
- `family_id`: the base agreement's doc ID; families sort by `family_id`, members by `order` (base first, then by `dated`, then id).

## gap-report.json (reconcile_index.py + build_manifest.py + build_families.py contributions)

```json
{
  "entries": [
    {
      "type": "index-missing",
      "detail": "Index row 3.2.4 'Amendment No 3' has no matching file",
      "evidence": "index.csv row 17"
    },
    {"type": "referenced-absent", "detail": "...", "evidence": "<quote>"},
    {"type": "unreadable", "detail": "...", "evidence": "readability=corrupt"},
    {"type": "duplicate", "detail": "...", "evidence": "same sha256 as sha256:aa10b2c9d001"},
    {"type": "custodian-gap", "detail": "...", "evidence": "custodian-month rollup"},
    {"type": "thread-gap", "detail": "...", "evidence": "message-id reference chain"}
  ]
}
```

## review-plan.json and maker checkpoints

`build_review_plan.py` converts the unit map and framework into the actual
dispatch contract. `sample` and `targeted` tiers require an explicit unit
selection; `full` always means every unit. One job exists per selected
unit/lens with a stable `job_id`, exact issue and member IDs, and input-volume
estimates. Unselected, unreadable, and pre-dispatch failures are named in
`parked_units`, so every manifest unit is accounted for.

The plan ID hashes the version, tier, framework version and full framework
digest, jobs, parked units, and the cost summary shown at the gate. Lawyer
approval changes only `approved` to true and `approval` to
`{"by":"lawyer","plan_id":"<plan_id>"}`. `prepare_review_jobs.py` writes one
deterministic assignment per job under `inputs/`. The compact v2 response
echoes the plan and job IDs once, identifies documents by 1-based ordinal, and
uses only `{n, issue_id, status}` for an absent determination.

`run_review_jobs.py` preserves raw responses under
`attempts/<job_id>/attempt-N.json`, writes the append-only `journal.jsonl`, and
derives `progress.json` and `parked.json`. `admit_finding_result.py` constructs
document and finding IDs, expands compact rows into the unchanged v1
checkpoint shape under `maker-results/`, verifies receipts, and writes a
deterministic transformation receipt under `receipts/`.
`merge_finding_results.py` revalidates canonical checkpoints, recomputes plan
identity and the unit map, merges privilege candidates, and writes per-lens
parked jobs on any failure.

## Gate 1 surface (render_gate1.py)

Input: manifest.json, families.json, gap-report.json, optional
framework-readback.json, metadata read plan, and prospective review plan.
Output: one self-contained `gate1.html`, no external requests, readable in
light and dark. The renderer requires an explicit `execution_mode` and
plain-English `assurance_note`; the surface shows both beside the exact
review-plan ID and cost basis. The lawyer's confirmation is recorded by the
orchestrator in `families.confirmed.json` and the plan approval receipt;
downstream stages read only those confirmed artifacts.

The Gate 3 renderer requires the same two disclosure fields. It shows them on
both an issued report and a reconciliation-refusal page, so a degraded run can
never inherit Python-mode assurance by omission.
