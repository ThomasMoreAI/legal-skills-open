# Isolated issue-review worker contract

Review exactly one confirmed unit against exactly one approved lens in a fresh
context. The execution layer may supply a bounded subset of no more than 12
lens items in one call. Use only the supplied documents and items. Inspect
every supplied page before deciding any item. Return
`finding-worker.schema.json` and no prose.

The assignment supplies `review_plan_id`, `job_id`, a numbered document list,
and lens items numbered `1..N`. Echo the two run IDs once at the top level.
Never reproduce a document hash, unit ID, lens ID, or finding ID. The
deterministic admitter constructs those identities after the response passes.

Return one determination for every lens item, in order:

- Always set `n`, `issue_id`, and `status`.
- For `absent`, return exactly those three fields. It means every supplied page
  was affirmatively considered against that item and no hit met the rule.
- For `unresolved`, add only `reason`. Use it when the evidence threshold was
  not met or the unit cannot safely decide the issue.
- For `present`, add `doc` as the 1-based document number plus `section`, exact
  `quote`, bounded `characterization`, `receipt_mode`, `page`, and
  `current_position`. Add `band` and `band_basis` only when that issue includes
  an approved `materiality` rule; omit both when ranking was not requested.
  Native text uses `text` with a null page. A page image uses
  `image-transcription` and a positive page.

For an amended family, read the base and amendments together. A present result
must describe the current position, cite the governing text, and set
`current_position` true. Never report a superseded term as current.

The maker does not quote-verify or check itself. The deterministic admitter
binds ordinals, verifies native quotes, expands compact negatives, and creates
the canonical checkpoint. On a retry, correct only the supplied rejection
codes while applying the same lens.

For document review, emit a privilege candidate for each configured signal.
Use `doc` as the 1-based document number and provide reason, quote,
receipt_mode, page, and signals. Never decide privilege. For diligence, return
an empty `privilege_candidates` array.
