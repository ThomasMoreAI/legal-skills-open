# Inventory and reading design

This is the build contract for the shared ingestion layer. It implements the
PRD's central promise: every canonical-metadata claim needed to define units
or serve an approved consumer gets an isolated document read before it is
used, except a fully receipted regex result that is banked and covered by the
frozen sample audit. When review units are already defined without canonical
metadata and no approved consumer needs it, the lawyer may instead approve
`deferred-to-review` at Gate 1. Diligence family assembly always makes metadata
unit-defining, so diligence never defers these reads.

## The loop

The backbone is an orchestrator with one fresh-context worker per document.
The quality layer is deterministic schema and quote validation on every
worker result, plus a separate fresh-context checker for every high-band
finding.

Python is the preferred mechanics layer, not the legal method. At run start,
the orchestrator follows `execution-modes.md`: try the bundled stdlib scripts
first; if Python or local script execution is unavailable, preserve the same
isolated worker contracts and gates through host-native tools or sequential
execution. The fallback must disclose every deterministic check it could not
perform and may not claim coverage certification without stable file identity
and reconciled counts.

1. A script inventories and hashes every file. No model is needed to count,
   hash, detect duplicates, or measure text yield.
2. `extract_metadata_prep.py` extracts regex evidence into
   `regex-metadata/` and writes `read-plan.json`. Regex is an accelerator, not
   the reader. A record is bankable only when each populated identity claim
   and reference has an exact source-text receipt. Ten percent of banked IDs
   are deterministically reassigned to `regex-audit`. Under an explicitly
   selected `defer-non-unit-metadata` policy, readable rows instead become
   `deferred-to-review`: their free regex evidence remains non-canonical, and
   no reader input, bank, or audit is created.
3. The host orchestrator dispatches each `reader-required` and `regex-audit`
   ID to a fresh worker with `metadata-reader-prompt.md` and
   `metadata-reader.schema.json`. The worker sees one document and its ID.
   Text workers receive the path-free excerpt named in `reader_input`; image
   workers receive rendered pages without the source filename. A worker does
   not see folder-derived answers, other documents, prior workers, or an
   answer key.
   `deferred-to-review` rows are not dispatched at ingestion. The lawyer must
   approve the displayed deferred lane at Gate 1 before any semantic review
   uses that plan; a bare continue is not approval.
4. The orchestrator validates on receipt, checkpoints only a valid result,
   retries at most twice, and parks a poison document without stopping the
   run. Resume skips only schema-valid, quote-valid checkpoints. Progress is
   reported as done/total/ETA with parked counts.
5. `merge_metadata_reads.py` revalidates every result against the shared
   visible-text surface and writes the only canonical `metadata/` directory.
   Required or audit reads never fall back to regex after failure.
   Image checkpoints go to an explicit human review artifact and enter
   canonical metadata only with a lawyer confirmation receipt.
   Any audit disagreement invalidates the remaining bank and requires a new
   `--expand-bank` read plan before relationship mapping.
6. Deterministic blocking and relationship resolution operate on canonical
   metadata. `build_families.py --edge-plan-out` names only unresolved
   candidate pairs. Each fresh resolver sees two metadata records;
   `merge_edge_results.py` validates its stable ID, endpoints, relation, and
   receipt quote before compiling `model-edges.json`. The union-find assembler
   stays deterministic.
7. Gate 1 marks every edge based on reader evidence or a model edge resolver
   as proposed. The lawyer confirms or regroups the map. Downstream work reads
   only the confirmed artifact.

If the host supports worker fan-out, the orchestrator uses bounded parallel
dispatch. If it does not, it runs the exact same per-document contract
sequentially. Parallelism changes wall time, not the artifact contract or
safety controls. No production script selects a model.

This scheduling fallback is independent of the mechanics mode. Python scripts
may run with parallel or sequential workers. A no-script run may likewise use
parallel or sequential workers, but model reasoning never inherits the words
`script-verified`, `deterministic-visible-text`, or `coverage-certified` merely
because it followed the same schema.

## Read routing and receipts

- Native text: first pages plus the tail/signature region, strict verbatim
  quote verification against cleaned visible text.
- Scanned document: page images when the host can render them. A transcription
  is labeled not script-verifiable and the record stays in the human lane
  until confirmed. The system never calls an image-read claim quote-verified.
- Encrypted, corrupt, or suspect: parked before dispatch and counted in the
  coverage receipt.
- Deferred to review: no standalone metadata read or canonical identity
  claims. The frame-aware finding pass still reads the full document under its
  ordinary receipt and privilege rules. Rerun prep without the deferral flag
  to order canonical metadata later. For a partial un-deferral, merge the
  scoped plan into a fresh metadata run directory; stale-file detection
  intentionally refuses mixed old outputs outside that plan.

HTML/SEC SGML is converted to one shared visible-text surface. Entities are
decoded, block boundaries are retained, and script/style text is excluded.
The reader merger, quote verifier, and model-edge verifier use that same
surface.

## Relationship provenance

Relationship edges carry two independent facts:

- `provenance: rule | model` identifies the resolver.
- `evidence_source: regex | model-read | image-read-human-confirmed |
  model-edge` identifies where the relationship evidence came from.

A deterministic match over reader metadata is still a rule edge, but it is
proposed at Gate 1 because its evidence depends on a probabilistic read.

## Finding checker

Makers review one confirmed unit per frozen framework lens under
`finding-worker-prompt.md` and `finding-worker.schema.json`. A valid checkpoint
contains exactly one result for every issue in that lens. Before dispatch,
`build_review_plan.py` freezes the approved tier, exact unit/lens jobs, stable
checkpoint IDs, and every parked unit. `merge_finding_results.py` is the
deterministic consumer; it validates identity, issue coverage, member IDs,
schema, quotes, privilege candidates, and the returned `review_plan_id`. Then
`build_checker_plan.py` binds
the exact high-band ledger to separate fresh-context checker jobs under
`finding-checker-prompt.md`. The checker receives only the claim, its quote,
the governing framework item, and the unit documents, and is instructed to
refute. `merge_checker_results.py` rejects plan or ledger drift. Missing or
non-confirming output, including a wrong `checker_plan_id`, makes the finding
unresolved. The checker cannot make a lawyer-only ruling.

## Done checks

- Functional per document: planned ID has a validated checkpoint, a receipted
  regex bank, an explicitly approved deferred-policy lane, or a visible parked
  reason.
- Functional per run: unique planned IDs equal accepted plus banked plus
  deferred plus parked; no required ID disappears.
- Judgment for material claims: high-band finding has a fresh checker verdict.
- Human gates: family/cluster confirmation, framework calibration, privilege
  rulings, and final unresolved rulings.
