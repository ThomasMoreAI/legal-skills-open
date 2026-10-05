# The checklist compiler contract

The compiler turns the lawyer's checklist into `framework.json`, the single file every worker is judged against. This document is the contract; `framework.schema.json` beside it is the machine-checkable version (`validate_framework.py` enforces it).

Three rules govern everything here:

1. **The framework is the only instruction channel.** The orchestrator injects the approved `framework.json` verbatim into every worker. Nothing else about the checklist reaches a worker. If a calibration is not written in the framework, it does not exist.
2. **Versions are immutable.** Every recompile increments `framework_version` and writes a new file (`framework.v3.json`). Gate 2 approval freezes one version; the run records which version it used. Calibration history is the diff between versions.
3. **Knobs are fields.** Calibration at Gate 2 means editing named fields, never freehand instructions to a worker.

## framework.json shape

```json
{
  "framework_version": 2,
  "approved": false,
  "source_inputs": [
    {"kind": "checklist", "label": "client DD request list"},
    {"kind": "rfp", "label": "defense RFP set, served 2026-05-01"}
  ],
  "lenses": [
    {
      "lens_id": "change-of-control",
      "name": "Change of control and assignment",
      "items": [
        {
          "issue_id": "coc-01",
          "question": "Does the agreement restrict change of control or assignment?",
          "hit_rule": "Consent required for change of control or assignment, or a termination right triggered by either.",
          "exclusions": ["Notice-only assignment clauses", "Assignment permitted to affiliates without consent"],
          "materiality": {
            "default": "medium",
            "bands": [
              {"band": "high", "when": "Termination right triggered, or consent required and TCV above 250000"},
              {"band": "low", "when": "TCV below 250000 and non-exclusive"}
            ]
          },
          "evidence": {
            "required": "verbatim quote plus section reference",
            "unresolved_when": "The clause cross-references a schedule or definition not in the data room, or the quote cannot be located"
          },
          "answer_shape": {
            "statuses": ["present", "absent", "unresolved"],
            "characterization_max_words": 30,
            "template": "SECTION: consent required on change of control (QUOTE). Severity: BAND (basis)."
          },
          "disposition": "report",
          "overlap_owner": null
        }
      ]
    }
  ]
}
```

An enumerated requests framework adds this optional top-level block and a
singular target on each item:

```json
{
  "frame": {
    "kind": "requests",
    "frame_id": "served-rfp-audit",
    "corpus_id": "d19d7b47f21b42c1",
    "purpose": "receiving-audit",
    "instruments": [
      {
        "instrument_id": "rfp-set-one",
        "kind": "rfp",
        "label": "RFP Set One.md",
        "party": null,
        "set": null,
        "element_count": 12,
        "staged": false
      }
    ]
  },
  "target_ref": {"instrument_id": "rfp-set-one", "element": 1, "series": "D"}
}
```

Field meanings, and which are calibration knobs (K):

- `frame`: optional typed analysis-frame identity. `requests` is the
  structure-preserving enumerated mode; `issues` is the interpretive prose
  mode. Its optional `corpus_id` binds the frame to one additive manifest
  identity without making older manifests invalid. `purpose` records
  `receiving-audit` or `producing-review`; v1 ships the receiving-audit path.
- `frame.instruments`: the complete census. `staged: true` keeps an instrument
  visible without compiling its elements into this framework version.
- `target_ref`: the singular enumerated element an item represents. It is
  optional in the general schema, required exactly once per item in a
  `requests` frame, and forbidden in an `issues` frame. Its optional uppercase
  `series` reconstructs a served compound designator: `series: "D"` with
  `element: 1` is displayed as `D-1`; without `series`, it remains `1`.
- `question`: the checklist item, in the lawyer's own terms.
- `hit_rule` (K): what counts as a finding. The most load-bearing field in the skill.
- `exclusions` (K): what looks like a hit and is not. Where Gate 2 noise complaints land.
- `materiality.bands` (K): ranking rules once a hit is found. `default` applies when no band matches.
- `evidence.required`: fixed at quote plus section; not a knob.
- `evidence.unresolved_when` (K): when a worker must stop deciding and route to the Gate 3 queue.
- `answer_shape.template` and `characterization_max_words` (K): what the finding text looks like.
- `disposition`: `report` (findings report), `register` (also feeds the further-enquiries register), `queue` (straight to the unresolved queue for a human).
- `overlap_owner` (K): when two lenses can catch the same clause, the lens_id that owns it; the other lens suppresses the duplicate.

## The read-back

`render_readback.py` derives `framework-readback.json` from framework.json: one row per item with `{lens, issue_id, question, hit_rule, materiality, evidence_required}`. That file feeds the Gate 1 surface (render_gate1.py `--readback`). The read-back is a deliverable the lawyer approves, never an internal artifact; it must stay plain English, one line per field, no schema jargon.

## Compact maker response and canonical checkpoint

Each isolated unit/lens maker returns `finding-worker.schema.json` under the
instructions in `finding-worker-prompt.md`. Its `determinations` array contains
exactly one result for every issue in the supplied lens, in lens order. The
maker echoes the plan and job IDs once, uses document ordinals for evidence,
and never constructs a document or finding ID. An absent row contains only its
ordinal, issue ID, and status.

`admit_finding_result.py` binds the response to the approved assignment,
constructs stable identities, expands compact rows, and validates exact issue
coverage, member documents, evidence, and characterization caps. Only then
does it write the unchanged canonical maker checkpoint consumed by the merger.
The worker supplies neither quote-verification nor adversarial-verification
fields.
Native-text receipts use `receipt_mode: text` and a null page. Image receipts
use `receipt_mode: image-transcription` and a positive page, are labeled as not
script-verifiable, and route the result to the human lane.

## findings.json (the merged ledger)

```json
{
  "framework_version": 2,
  "review_plan_id": "5a7d2e101f403987",
  "findings": [
    {
      "finding_id": "coc-01/sha256:9f3a1c04b2d7",
      "issue_id": "coc-01",
      "lens_id": "change-of-control",
      "unit_id": "sha256:aa10b2c9d001",
      "doc_id": "sha256:9f3a1c04b2d7",
      "status": "present",
      "section": "9.2",
      "quote": "neither party may assign this Agreement without the prior written consent",
      "characterization": "9.2: consent required on assignment and change of control.",
      "band": "medium",
      "band_basis": "TCV 180000, non-exclusive",
      "quote_verification": {"status": "confirmed", "checker": "deterministic-visible-text", "reason": null},
      "verification": {"status": "confirmed", "checker": "adversarial"},
      "current_position": true
    }
  ],
  "parked": [
    {
      "job_id": "7f305811d76ba189",
      "lens_id": "change-of-control",
      "member_ids": ["sha256:0c77d1e2f3a4"],
      "reason": "maker checkpoint missing",
      "unit_id": "sha256:0c77d1e2f3a4"
    }
  ]
}
```

- `finding_id` is `issue_id/doc_id`: stable, so response handling can attach in v1.1.
- `unit_id` is the family when relationships exist, else the doc itself. `current_position: true` asserts the finding reflects the post-amendment position; a worker reading an amended family must set it and quote the governing text, never a superseded term.
- Quotes are verified by the same visible-text machinery as metadata. A present
  finding is reportable only with `quote_verification.status: confirmed`. A
  failed quote is deterministically downgraded to unresolved and routed for
  human review.
- Every high-band present finding receives a separate fresh-context checker
  pass under `finding-checker.schema.json`. The checker sees only the finding,
  its frozen framework item, and its confirmed unit documents. Missing,
  refuted, or unresolved checker output downgrades the finding to unresolved;
  the maker never grades its own work. `build_checker_plan.py` binds the exact
  pre-check ledger to the required high-finding jobs. Checker checkpoints use
  the first 16 hexadecimal characters of `SHA-256(finding_id)` plus `.json`
  and carry the exact `checker_plan_id`;
  `merge_checker_results.py --framework --manifest --room-root --checker-plan`
  refuses a drifted framework, ledger, unit membership, source document, or
  incomplete plan.
- `review_plan_id` binds the ledger to the lawyer-approved dispatch. Parked
  jobs are lens-specific; a failed pass in one lens cannot silently excuse a
  different lens.
- Coverage invariant: for each lens, findings (all statuses) plus that lens's
  parked units equals the manifest count of reviewable units.
  `reconcile_counts.py --review-plan` refuses the report otherwise.

## Compiler behavior

### Interpretive compilation

The compiler is a model step the SKILL.md orchestrates, with these constraints: it reads the lawyer's raw inputs (any format), proposes lenses and items, and must produce schema-valid output (validate_framework.py gates it, capped retries). It never invents materiality thresholds: where the lawyer's input is silent, `default` is `medium` and the band list is empty, and the read-back marks the item "materiality: default (tune at Gate 2)". Vague inputs compile to conservative hit rules plus an explicit exclusions list of zero: over-inclusion is tuned down at Gate 2, silence is never tuned up. The calibration eval (case-02) holds an example: one vague checklist item and the expected compiled JSON.

Interpretive consolidation is legal only for an `issues` frame, where items do
not carry `target_ref`. Pleadings, chronologies, and other prose inputs remain
under this contract.

### Structure-preserving compilation

Enumerated requests and numbered issue lists first pass through
`parse_instruments.py`. Its census preserves served numbers and verbatim
element text. `--scaffold` creates one non-staged lens per compiled instrument
and exactly one item per element, with one singular `target_ref`; elements may
not be grouped, dropped, duplicated, renumbered, or relabeled. Instruments not
compiled into the current framework remain visible as staged census rows.
Plain designators are positive ASCII integers. Compound designators use
uppercase letters plus a hyphen and a positive ASCII integer; the census stores
that prefix as optional `series`. Element identity and the census-to-item
bijection use `(instrument_id, series-or-null, element)`, preserving plain `1`
and `D-1` as distinct served requests. `validate_framework.py --instruments`
proves that bijection.
Interpretive notes may be added later without changing that structural map.
