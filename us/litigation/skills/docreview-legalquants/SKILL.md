---
name: docreview-legalquants
title: Document Review
description: Review an incoming litigation production against the matter's requests or issues, with deterministic inventory and coverage receipts, a plain-language setup approval, human privilege decisions, source-linked Requests/Documents HTML, and drift-bound lawyer feedback. Use when asked to organize or review a production, map documents to RFPs or pleadings, identify production gaps, or prepare a privilege queue.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-plugin-oss/tree/main/plugins/legalquants-litigation/skills/docreview
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Comms Schemas
  path: references/comms-schemas.md
- title: Openai Codex Runtime
  path: references/openai-codex-runtime.md
- title: Edge Resolver Prompt
  path: references/shared/edge-resolver-prompt.md
- title: Execution Modes
  path: references/shared/execution-modes.md
- title: Finding Checker Prompt
  path: references/shared/finding-checker-prompt.md
- title: Finding Worker Prompt
  path: references/shared/finding-worker-prompt.md
- title: Framework Schema
  path: references/shared/framework-schema.md
- title: Inventory Design
  path: references/shared/inventory-design.md
- title: Metadata Reader Prompt
  path: references/shared/metadata-reader-prompt.md
- title: Review Ui
  path: references/shared/review-ui.md
- title: Schemas
  path: references/shared/schemas.md
---

# Document Review

## Outcome and boundaries

Turn a local production into a coverage-receipted review package: inventory,
communication map, gaps, approved review questions, immutable machine
proposals, lawyer-only privilege decisions, a Requests/Documents review page,
lawyer-feedback overlays, and final reconciliation.

The lawyer decides responsiveness, relevance, materiality, and privilege. This
skill proposes and verifies; it does not produce, serve, file, or transmit
documents. A privilege signal always creates a hold until the lawyer rules.

Keep the machine proposal ledger and its evidence receipts immutable. Setup
approvals, privilege rulings, image confirmations, and responsiveness rulings
are additive artifacts or overlays bound to the exact inputs they govern.

## Read the applicable contracts

- Before inventory or scheduling, read
  [execution-modes.md](references/shared/execution-modes.md),
  [inventory-design.md](references/shared/inventory-design.md), and the
  relevant artifact definitions in [schemas.md](references/shared/schemas.md).
- Before message clustering, privilege review, setup approval, feedback
  ingestion, or final reconciliation, read
  [comms-schemas.md](references/comms-schemas.md).
- Before compiling review questions, read
  [framework-schema.md](references/shared/framework-schema.md). For an
  enumerated request set, use the adjacent machine schema and preserve every
  served element.
- Before dispatching judgment work, read the matching metadata-reader,
  finding-worker, or finding-checker prompt and schema in
  `references/shared/`. When a permitted local headless runtime will execute
  the compact finding jobs, also read its provider reference before choosing
  the worker command.
- Before producing lawyer-facing HTML, read
  [review-ui.md](references/shared/review-ui.md) and
  [review-copies.schema.json](references/shared/review-copies.schema.json).
  Before ingesting a browser export, read its adjacent receipt schema.

Only confirmed `[docreview]` lines in `lqplaybook.md` may shape the work. Do
not read `lqprofile.md` during a review run.

## Runtime and assurances

Prefer the bundled Python path. Every bundled Python script uses the standard
library only. Try `python3`, then `python`, then `py -3`; confirm the selected
interpreter can run a bundled script's `--help`. Do not install Python packages
or change the host.

Poppler and LibreOffice are optional, open-source rendering rungs when already
available. They are executables, not Python dependencies. The core text,
email, OOXML, hashing, receipt, and HTML paths remain offline and standard
library only.

If local scripts cannot run, follow the portable fallback in
`execution-modes.md`, using isolated workers when available and the same jobs
sequentially otherwise. Preserve every privilege hold and lawyer gate. State
which deterministic checks were unavailable; without stable file identity and
complete count reconciliation, do not call the result coverage-certified.

Use one run directory for intermediate state and one source root for the
production. Durable artifacts contain relative paths, stable IDs, sorted JSON,
no run-added timestamps, no host names, and no external URLs.

For finding jobs, prefer `scripts/shared/prepare_review_jobs.py` followed by
`scripts/shared/run_review_jobs.py`. The runner defaults to five concurrent
jobs and accepts `--workers 1..12`. Before fan-out, surface its run-started
disclosure: selected concurrency, source of that setting, job count, estimated
invocations, and the resource/throttling tradeoff. Keep one model and effort
for the whole run and record them in the journal. Do not read or modify a
host's global configuration to choose concurrency.

The runner preserves immutable attempts, admits compact responses through
`admit_finding_result.py`, writes canonical checkpoints and deterministic
receipts, and journals every transition. Report progress from `progress.json`
and failures from `parked.json`. Use `--detach` when the execution must survive
the parent conversation. A parked job remains stopped until an explicit
`unpark --by ... --reason ...` receipt.

## Workflow

### 1. Inventory the production and build review copies

Run `scripts/shared/build_manifest.py` over the production root. When the
production includes an index or load file, run
`scripts/shared/reconcile_index.py`; retain every manifest, duplicate,
unreadable, and index gap.

After the manifest is final, build the mandatory review-copy layer:

```text
scripts/shared/review_copies.py build \
  --manifest <run>/manifest.json \
  --source-root <production> \
  --sidecar <run>/review-copies.json \
  --bundle-root review-copies \
  --mode auto
```

Keep `review-copies.json`, its `review-copies/` bundle, and every HTML file
that consumes it in the same directory. The sidecar binds the canonical
manifest digest, every source hash and byte count, separately reviewable email
attachments, every derivative hash, and the exact bundle contents. It carries
no legal conclusion.

The built-in path renders escaped text and EML, common images, browser-native
PDF, and safe visible text from readable DOCX, XLSX, and PPTX packages.
`--mode auto` adds Poppler pages and LibreOffice-to-Poppler Office pages when
those tools are already present. Legacy, corrupt, unsupported, or incomplete
formats remain **Needs rendering**.

Exit 0 means all documents and separately reviewable attachments are ready.
Exit 1 means the sidecar is valid but at least one item still needs rendering;
park every dependent review result and do not approve that tier. Exit 2 means
integrity or containment failed; stop and repair the source, manifest, or
bundle before continuing.

### 2. Map the production and plan reads

Run `scripts/parse_messages.py`, `scripts/cluster_comms.py`, and
`scripts/comms_gaps.py`. Thread membership comes from message headers and
reference chains; channels come from repeated participant sets. Flattened
PDFs and images remain singleton units. Never infer a custodian, date,
participant, or thread from a filename.

Run `scripts/shared/extract_metadata_prep.py`. For message-heavy request
review, pass `messages.json` through `--include-ids` so non-message files are
explicitly planned. Build both ordinary and
`--defer-non-unit-metadata` plans when canonical metadata is unnecessary, and
let the lawyer choose that policy during setup. Deferred files remain fully
in scope for the finding pass. Only `scripts/shared/merge_metadata_reads.py`
writes canonical metadata.

### 3. Compile and read back the review questions

The lawyer supplies the request sets, pleadings, chronology, or issue list.
For served or otherwise enumerated instruments, run
`scripts/shared/parse_instruments.py` first. Show the complete census and use
`--scaffold` for a one-item-per-element requests framework. Preserve served
numbers, series, and text; leave sets outside this run visibly staged.

For prose framing inputs, compile conservative issue questions without
inventing legal positions. Include the four privilege signals defined in
`comms-schemas.md`. Run `scripts/shared/validate_framework.py` with the
instrument census and manifest when applicable, then
`scripts/shared/render_readback.py`. The validated framework is the only
instruction channel to makers and checkers.

### 4. Obtain a plain-language setup approval

Choose up to five representative thread or singleton units and run
`scripts/shared/build_review_plan.py --tier sample`. Render
`scripts/render_dmap.py` with the manifest, messages, clusters, gaps, read
plan, review plan, `--framework`, its derived framework readback, execution
mode, assurance note,
`--document-root`, and the sibling `--review-copies` sidecar. The setup page
revalidates the complete sidecar and disables sample approval while any source
or separately reviewable attachment still needs rendering.

The visible page asks the lawyer to decide:

1. Are these the right review questions?
2. Does the collection coverage look right?
3. Is this a useful test sample?
4. If proposed, may standalone metadata reads be deferred to the issue pass?

The page must say that approval authorizes only the displayed test sample. It
does not authorize a full run, change a privilege hold, or start work merely
because the button was clicked. Plans, hashes, worker mechanics, and IDs stay
in collapsed technical receipts.

Ingest `review-setup-approval.json` with
`scripts/ingest_review_setup_approval.py`. It must refuse corpus, framework,
cluster, read-plan, review-plan, unit, issue, or metadata-policy drift before
writing `review-plan.approved.json` and `clusters.confirmed.json`. Start the
sample only after successful ingest or an explicit conversation approval
recorded in the same receipt shape. A bare “continue” is not approval.

### 5. Run and merge the test sample

Materialize the approved plan with `prepare_review_jobs.py`. Give each
unit/lens assignment isolated contexts containing only its documents, a
bounded request batch, exact plan and job IDs, and the compact finding-worker
contract. Follow the substantive mapping quality gate in
`references/shared/execution-modes.md`: select a higher-capability reasoning
route, use medium effort or above, cap each model context at 12 requests, and
prove recall on source-verified sample positives before scale. Use
`run_review_jobs.py run` for an authorized scripted fan-out; otherwise give
the same bounded assignments to native workers or process them sequentially.
The worker echoes only the plan and job IDs. The admitter binds
document ordinals, constructs every document and finding ID, expands compact
negative rows, verifies receipts, and writes the canonical checkpoint. Retry
a rejected judgment at most twice, then park it with a reason; transport
failures have a separate bounded budget.

Run `scripts/shared/merge_finding_results.py` with the approved plan,
framework, manifest, production root, confirmed clusters, and results
directory. It revalidates admitted checkpoints before writing the proposal
ledger or privilege queue. Missing jobs, invalid quotes, outside-tier units,
and privilege-held units remain parked.

### 6. Obtain lawyer privilege rulings

Before showing dependent findings, render every pending candidate with
`scripts/render_privilege_queue.py`. A candidate's source must be present and
its `review-copies.json` entry must be ready before asking the lawyer to rule;
the original-file link is provenance, not a substitute for the verified
review copy.

The lawyer chooses **Privileged**, **Not privileged**, or **Need more review**
for every candidate and exports `privilege-rulings.json`. Ingest it with
`scripts/ingest_privilege_rulings.py`. Queue or manifest drift must fail before
output. The source queue remains unchanged; the ruled copy preserves the
candidate evidence and adds only the lawyer ruling and note.

Rerun the finding merger with the ruled queue. Only `not-privileged` releases
a unit. Pending, `privileged`, and `needs-review` records remain held across
every lens.

### 7. Verify findings independently

Build a checker plan with `scripts/shared/build_checker_plan.py` after
privilege rulings. Every present high-band finding goes to a fresh checker
without the maker's reasoning. Merge checker outputs with
`scripts/shared/merge_checker_results.py`. Missing, stale, drifted, or
non-confirming results become unresolved; they never disappear.

Render the checked sample with `scripts/shared/render_sample.py` for the
internal calibration receipt. If lawyer feedback changes a framework field,
compile a new framework version and obtain a new plan approval before running
again. Approval freezes the calibrated version.

### 8. Review findings in Requests and Documents

Before every lawyer-facing findings render, verify the sidecar against the
current source bytes and manifest. Then run `scripts/render_crosswalk.py` with
`--document-root`, `--review-copies`, and the framework, checked findings,
manifest, and ruled privilege queue. The sidecar and HTML must be siblings.
Any sidecar integrity error stops rendering.

The default **Requests** tab answers which documents respond to each request.
The **Documents** tab reverses the same ledger and renders each source once.
Responsive items appear first; reviewed negatives are collapsed by default.
An unresolved legal call is **Needs a decision**, not “unreadable.” A file
with unresolved calls appears once in **Needs attention**, and a rendering
failure appears as **Needs rendering**. Outside-tier documents are never
called nonresponsive.

The page works from `file://`, loads no remote resource, and exports sorted,
timestamp-free `review-feedback.json`. The lawyer may rule a finding
**Responsive**, **Not responsive**, **Needs review**, or **Privileged** and
may separately confirm an image document's complete finding bundle.

Ingest feedback with `scripts/ingest_review_feedback.py`. It must refuse stale
ledger, framework, plan, frame, corpus, machine-status, finding, or image-bundle
bindings before writing. It never overwrites the proposal ledger or alters a
machine status, quote, evidence receipt, checker receipt, or privilege queue.
Per-finding `lawyer_ruling` and top-level `image_confirmations` are additive
overlays only.

Re-render the ruled copy using the existing artifacts. Export, ingest, and
rerender are deterministic file operations and require no new model call.

### 9. Scale only after calibration

Build a new targeted or full review plan from the frozen framework and
confirmed clusters. Show the exact scope, higher-capability model class,
reasoning effort, request-batch limit, projected model-call count, and cost
basis and obtain explicit approval of that plan before dispatch. Prepare the
same bounded assignments, surface the run-started disclosure, and run the same
admission, privilege, checker, review-copy, lawyer-feedback, and rerender
sequence. Resume only from attempts and checkpoints whose raw hashes, receipts,
and plan bindings still validate. Never resume a parked job without a receipted
unpark.

### 10. Reconcile and deliver

Run `scripts/reconcile_docreview_gate3.py` with the exact manifest, ruled
findings overlay, framework, confirmed clusters, privilege queue, and approved
review plan. It must prove the complete issue-by-unit count equation and exact
lawyer confirmation of every image-review bundle. Fix the run, never the
numbers.

Finally run:

```text
scripts/shared/review_copies.py verify \
  --manifest <run>/manifest.json \
  --source-root <production> \
  --sidecar <run>/review-copies.json
```

Delivery requires exit 0. Exit 1 leaves a visible rendering blocker; exit 2
means integrity failure. Neither state is lawyer-reviewed, client-ready, or
coverage-certified.

## Completion criteria

- Every source is accounted for as reviewed, parked with a reason, or outside
  the explicitly approved tier; the count reconciliation exits 0.
- The setup receipt was ingested before the sample, and the lawyer explicitly
  approved the exact full-plan ID and scope before full review started.
- The sample recovered every source-verified positive under the same model
  class, effort, and request-batch limit used for scale; schema validity and
  runtime speed alone are not calibration.
- Every privilege candidate has an explicit lawyer ruling, and no held unit
  contributes a deliverable finding.
- Every present high-band finding has an independent checker confirmation;
  every quote and source membership check passed or became unresolved.
- `review-copies.json` verifies at exit 0 against the final manifest, source
  bytes, derivatives, attachments, and bundle contents.
- Setup, privilege, sample, and Requests/Documents HTML were regenerated and
  exercised from `file://` in light and dark mode, including tabs, filters,
  keyboard/focus hooks, downloads, and blocked states.
- A second render from identical inputs is byte-identical. Rerendering used no
  model call.
- Temporary working state is removed at completion; deliverables remain in the
  matter folder and nothing was transmitted.
