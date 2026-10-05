# Parent fan-out reference

This reference describes the portable parent procedure for the cite-check fan-out. It is progressive guidance for hosts that can delegate work; a host without workers follows the same assignment and result contract sequentially.

## Prepare once

Convert the supplied target to UTF-8 Markdown or plain text with one physical line per extractable text container. Make one unit for every paragraph, list item, table cell, heading, caption, footnote, endnote, header, footer, or text box the host can expose. Preserve source order, assign stable `P####` IDs to body units and `F####` IDs to footnotes, and record each unit's source file path and line range. For a footnote, record the body unit that anchors it when known.

Do not first ask which units contain citations. The unit inventory is mechanical. Do one once-over of the supplied authority files to confirm that roughly the expected kinds and number of files are present and readable; detailed source judgment happens inside assigned unit reviews. If authorities were not supplied, record that the run can search for cited cases but cannot verify what they say; do not use model memory as source evidence.

Create one dedicated run directory. Keep the prepared brief, authority inventory, prompt inputs, raw attempts, terminal receipts, normalized results, and report artifacts inside the run boundary as the host permits. The authoritative inventory for the run is the complete set of prepared unit IDs.

Run the packaged `scripts/cite_check.py`. It uses one fresh Codex session for each prepared unit. If the host cannot run it, use native workers with the same one-unit assignments or process those assignments one at a time. The environment probe is local and synthetic; it makes no model call and reads no matter content.

## Assign one unit at a time

Each fresh session receives the same assignment contract. If the packaged script cannot run, native workers or one-at-a-time processing use the same assignments. Do not combine several prepared units into one review. Each session receives:

- the full path to this prompt and the full path to `references/cite-check-rubric.md`, with an instruction to read the rubric before working;
- the assigned unit's stable ID, exact text, source path, and line range;
- about five units before and five units after the assigned unit;
- the nearest section path or heading;
- for a footnote, the anchored body unit and the same bounded nearby body context; and
- the full path to the prepared brief and the supplied authority files.

The assignment envelope owns location. The worker must not author a new location, add another unit, or report a citation that appears only in surrounding context. It returns one terminal JSON result for the assigned unit. A unit with no citation returns `no_citations_found` and an empty citation array; this is complete accounting, not a missing result.

## Reconcile and retry once

Keep each raw attempt and terminal receipt in the same run directory. Give one targeted retry for mechanically incomplete evidence: a missing excerpt, missing locator, invalid or out-of-authority source ID, or inconsistent source-match fields. Do not retry substantive legal disagreement. If the repair still fails, retain the citation as amber (claimed but unverified). Preserve completed receipts and raw attempts; do not rewrite worker-authored fields during validation.

## Render and sense-check once

Render the lawyer-facing HTML. The runner's `--output-dir <run>/results` contains worker receipts in `<run>/results/results/`; therefore, when the packaged scripts are present, run `scripts/aggregate_report.py --manifest <run>/manifest.json --results <run>/results/results --receipt-dir <run>/results --output-dir <run>/report` to validate the receipts and render the supplied template. If local scripts are unavailable, render the same validated report data with `../assets/report-template.html` using host-native capabilities. Do not hand-author replacement HTML unless the user requests a custom report. The main body contains units with citation rows. The appendix accounts for every prepared unit and records `no_citations_found`, complete, failed, or still-missing coverage. Run one bounded sense check: the appendix accounts for every prepared unit, no visibly citation-dense passage has zero citation rows, and no finding contradicts itself on its face. Put any apparent anomaly in `Caveats / Issues`; do not start a second retry cycle.
