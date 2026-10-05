# Execution modes

`/diligence` and `/docreview` keep one legal method and one set of worker
contracts across hosts.  Python is the preferred deterministic mechanics
layer, not a condition for loading either skill.

## Choose the mode once

At the start of a run, try the bundled Python path before choosing a fallback:

1. Look for `python3`, then `python`, then `py -3`.
2. Confirm that the candidate can run a bundled script's `--help` command.
3. Do not install or upgrade Python, use `pip`, request `sudo`, or add a
   package.  The bundled path is Python-standard-library only.  Poppler is an
   optional extraction improvement, never a prerequisite.
4. If the host requires approval merely to execute a bundled local script,
   explain that the script processes local matter files without network access
   or package installation and ask once.  A denial selects the portable
   fallback; it is not an invitation to ask the lawyer to install anything.

Record the selected mode in the run log and display it at Gate 1 and Gate 3.
Do not switch modes silently in the middle of a run.

## Python mode — preferred

Use the bundled scripts for inventory, hashing, text normalization, blocking,
schema and receipt validation, merging, reconciliation, and rendering.  Use
host-native workers for the judgment steps.  Parallel workers are preferred
when available; otherwise process the same jobs sequentially.  Worker
selection never changes the plans, prompts, schemas, checkpoint IDs, retry
caps, gates, or coverage equation.

Python mode may claim the deterministic assurances only after the named
script checks pass.  Availability of an interpreter by itself proves nothing.

For finding jobs, `prepare_review_jobs.py` materializes one compact assignment
per approved unit/lens pair. The execution layer subdivides each assignment
into request batches of no more than 12 issues per model context while
preserving the approved full-lens order in the admitted checkpoint. A lower
bound is appropriate for long, image-heavy, or fact-dense units; no execution
path may enlarge the bound above 12. `run_review_jobs.py` provides bounded
scripted fan-out when the user or firm has authorized a callable headless
runtime. It defaults to five concurrent workers, accepts 1–12, and discloses
the selected concurrency and resource tradeoff before dispatch. Native-worker
and sequential paths apply the same request-batch and concurrency bounds.

Every path preserves the same lifecycle: dispatched, immutable raw response,
deterministic admission or rejection, bounded retry, and visible park. The
compact worker never constructs stable document or finding IDs. The admitter
binds ordinals, constructs IDs, verifies native quotes, and writes the
unchanged canonical checkpoint consumed by the merger.

## Substantive mapping quality gate

Substantive issue mapping is a high-recall legal judgment task. Use a
higher-capability reasoning model at medium effort or above; use high effort
for scanned, long, dense, or high-consequence material. The user may choose a
different route after seeing the recall, cost, and speed tradeoff. Model names
remain host-specific and are never fixed by the shared skill.

Calibrate recall before scale. The sample must contain at least one
source-verified responsive document and one plausible negative, and the model
must recover every known positive under the same request-batch size planned
for the full run. Schema validity, quote validity, and fast completion do not
establish recall. An all-negative result on image-only material receives a
fresh bounded second look during calibration. A missed known positive stops
scale; revise the model, effort, request-batch size, or worker framing and
obtain approval of the revised plan.

## Portable fallback — no Python or no script execution

Continue inside the same skill.  Do not replace the workflow with an informal
whole-room review.

1. Use host-native file and document tools for the mechanical operation named
   by each workflow step.  Produce the artifact shape in `schemas.md` or
   `comms-schemas.md` whenever the host can support it.
2. Give each document, pair, unit/lens job, and checker job the same isolated
   prompt and result schema used in Python mode.  Use native workers when the
   host provides them; otherwise run the jobs sequentially.
3. Keep authoritative intermediate state in the run dataset when a filesystem
   exists.  If it does not, keep a compact master ledger and checkpoint after
   each bounded batch; do not rely on unstructured chat history.
4. The parent validates IDs, source membership, required issue coverage,
   duplicate or missing jobs, receipt alignment, and reviewed + parked +
   unreadable counts before advancing.  A separate fresh context still checks
   every high-band finding.  The lawyer gates and privilege holds do not
   change.
5. Park any document or claim whose bytes, text, quote, membership, or count
   the available host tools cannot verify.  Never turn an unavailable
   deterministic check into model confidence.

The fallback is method-compatible, not assurance-equivalent.  State exactly
which checks were unavailable.  In particular:

- Do not claim SHA-256 identity, byte stability, deterministic regex banking,
  automated schema validation, automated quote verification, or automated
  count reconciliation unless a host-native tool actually performed it.
- If stable file identity and complete count reconciliation cannot be
  established, the run may deliver a clearly labeled review and unresolved
  queue, but it may not call the result coverage-certified.
- No artifact produced or checked only by model reasoning may be labeled
  `script-verified` or `deterministic-visible-text`.

Tell the lawyer about the assurance delta once, before costly fan-out.  Offer
Python mode as the better experience if it later becomes available, but do not
make installation the default user journey.

## Failure and resume

- Retry a rejected judgment at most twice in either mode, then park it.
  Transport failures have a separate bounded budget and do not consume a
  judgment attempt. Repeated permanent configuration errors stop the run.
- In Python mode, `journal.jsonl` is the append-only transition authority;
  immutable raw responses live under `attempts/`, canonical checkpoints under
  `maker-results/`, and deterministic expansion receipts under `receipts/`.
  `progress.json` and `parked.json` are derived views.
- `--detach` uses a process lease and heartbeat so a long batch survives the
  launching conversation. A second runner refuses a live lease. Resume only
  from raw attempts and checkpoints that the active mode can revalidate.
- Parked jobs never resume silently. Unpark requires an explicit actor and
  reason recorded as a journal event.
- If Python becomes unavailable after it created a plan, valid worker
  checkpoints may be retained, but every aggregate produced after the switch
  must disclose portable-fallback validation.  Rebuild any aggregate whose
  inputs or identity cannot be revalidated.
- A fallback run never weakens a lawyer-only ruling, privilege hold, quote
  requirement, or fail-closed stop condition.
