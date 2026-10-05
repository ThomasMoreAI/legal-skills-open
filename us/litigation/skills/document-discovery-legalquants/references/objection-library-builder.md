# Build and curate an objection library

Use this workflow when the lawyer asks to turn completed responses into reusable objection wording or requests an objection-selection HTML using examples without an approved library. Prepare curation as the necessary first handoff in that selection workflow, then wait for actual lawyer decisions before building request-specific choices. Supplying an example for a shell or one-off draft does not itself request a library. Deliver a useful, source-linked subset. Do not require a whole firm's precedents, new matter intake, or an exhaustive objection bank. Initial scope is readable DOCX and text-based PDF responses to federal RFPs. Capture supplied wording without treating prior use as current legal endorsement; apply the skill's authority method if asked to assess its legal validity.

The library is a selected work product, not an ambient profile or playbook. Approval makes an entry available as a starting point; it does not declare it legally sufficient, preferred in every matter, or immutable. Its source request numbers are locators, not restrictions on which future requests may use it. The lawyer may revise its wording, qualifications and usage guidance. Use ordinary host document tools first; use firm-selected specialist extraction or comparison tools when needed. The host model extracts and groups passages. The optional standard-library helper validates the review handoff and saves approved versions; it does not extract legal propositions or decide what is reusable.

## From documents to candidates

1. Read the supplied responses and practice guidance. Record the source documents, actual request occurrences, numbering/section boundaries, and extraction gaps in one working dataset. Distinguish repeated printed numbers by occurrence and locator. Verify text against the documents where extraction is uncertain. If a source cannot be read reliably, identify the affected coverage and continue with the useful readable subset.
2. Split each combined response into its **individual objection grounds**. The selection unit is one ground, usually a sentence or a few connected sentences needed to express that ground and its qualifications. A response containing privilege, scope and burden objections yields separate candidates, not one combined-response tile. Preserve exact ground excerpts and the relevant full response context; the original request number is a locator, never an entry type. Preserve general objections separately from request-specific objections. Distinguish matter identifiers, substantive answers, production commitments and service language from reusable objection text. Do not split off a qualification that defines the ground's scope. Keep that qualification in the proposed wording, even when a related factual condition also appears in guidance. If a passage cannot be separated confidently, retain the uncertainty for review instead of presenting the entire response as an atomic entry.
3. **Consolidate semantically equivalent grounds across the corpus, including differently worded examples.** Start from their meaning and scope, not exact-string deduplication or request numbers. One candidate may have several exact source excerpts. Use one family per objection type and separate variants only when a qualification materially changes its scope or application. Do not create variants merely because wording or source matter differs; do not merge distinct grounds merely because they occur together. Conflicting or uncertain meanings remain visible for lawyer judgment. Choose or synthesize proposed wording and show substitutions and generalizations against the exact excerpts; never describe a rewrite as a quotation. Use the visible `reason` to explain consequential scope changes, retained qualifications, and why paraphrases were consolidated or variants kept apart. These are proposed editing judgments, not restrictions on the lawyer's final wording. Practice guidance may support a proposed change, but its reusable wording and scope still need the lawyer's decision unless already explicitly approved.
4. Prepare candidate entries in the existing [proposal/library format](../schemas/objection-records.schema.json). Give each entry a stable ID, semantic `family`, short recognizable objection-type `label`, meaningful `variant`, exact proposed wording, named fields, usage guidance, conditions/exclusions, and sources. Prefer a label such as “Attorney-client privilege” over “Response to Request 6.” The family and label describe the ground, not a prior request or a bundle. There is no fixed sentence limit or built-in approved taxonomy; the lawyer controls wording and grouping. Avoid restating legal conclusions in guidance that the inputs do not establish. Retain unresolved or matter-only passages as non-reusable proposal items where they need a decision; an optional proposal `label` makes those tiles recognizable without creating an `after` entry.
5. Prepare a [curation catalog](../schemas/objection-library-curation.schema.json). Its `sources` identify the actual files and byte hashes. Its `passages` carry exact source request text, exact objection text under `original`, surrounding response under `context`, and the proposal IDs they support. A practice note may have an empty `request`; identify that source accurately. An entry's `sources[].source_id` refers to these catalog source IDs. Include a short coverage receipt with counts, excluded material, and unresolved extraction or grouping issues. Keep a census separate from the source excerpts needed for continued curation.

Start a new library with an empty curation base (it contains no approved entries and cannot be used to render request review):

```json
{"kind":"objection-library","format_version":1,"id":"chosen-library-id","version":1,"entries":[]}
```

Bind the proposal batch's `base_sha256` to that snapshot using `objection_review.digest`. New entries have `classification: new_entry`, `target_id: null`, `before: null`, and the candidate under `after`. Start every catalog proposal as `decision: pending` with `decision_record: null`. Do not assign an approved status or invent a decision record because wording appeared in a completed response or because a renderer requires approval. For an existing library, use its actual current snapshot and preserve original entries under `before`. Approved entries remain selectable; candidates remain outside the library.

Before delivery, inspect the actual rendered catalog as well as the source data: do type labels identify separately selectable grounds, do paraphrases consolidate, do material qualifiers survive in operative wording, and can the lawyer reach decisions beside the wording? Structural validation and source hashes cannot answer those semantic and usability questions. Record any unresolved grouping in the coverage receipt.

## Attorney curation

Render the catalog with the packaged helper when local execution is available:

```sh
python scripts/objection_library.py check-sources --catalog catalog.json --source-root sources
python scripts/objection_library.py render --catalog catalog.json --out curate-library.html
```

Source checking verifies file identities, not the truth of quotations or the completeness of extraction. Confirm those through the host's document tools and the source census. Catalog source paths are relative to the chosen source root; store confidential sources and catalog excerpts in the authorized workspace.

Use a small useful initial subset: enough approved wording to begin the requested drafting, with the remaining candidates available later. No exhaustive firm library is required. The page uses the same visual style as request review. Candidate tiles open proposed wording, sources, and guidance. The attorney can edit wording, qualifications, fields and guidance, approve an entry for reuse, exclude it, defer it, or leave it undecided. Suggested conditions and exclusions describe the proposal; they are not coded legal prohibitions. Approval checks complete draft fields and exact reviewed content, not whether the lawyer adopted the model's suggested position. Inspection is not approval. Changes clear the affected decision. Missing field descriptions prevent approval; incomplete drafts can still be saved as progress. There is no default selection or automatic approval of recurring wording.

Return both the HTML and a concise coverage/limitations receipt. Tell the lawyer to export library decisions and return the downloaded JSON. Closing the page alone does not save changes. If interactive HTML or local execution is unavailable, present the same source-linked candidates as a readable catalog and capture explicit decisions in chat against exact resulting entries; do not invent a browser action record. The existing proposal application helper also accepts directly recorded, explicitly authorized decisions.

## Save the approved subset and continue

With a returned browser decision file:

```sh
python scripts/objection_library.py apply --catalog catalog.json \
  --decisions decisions.json --out library-v2.json
```

The combined application revalidates the exact catalog, returned decisions and embedded base library at the final handoff; it regenerates approved proposals rather than trusting an edited intermediate file. It preserves source/target identity, applies only explicitly reviewed entry edits, creates a new snapshot and preserves the old file. `reconcile` remains available to inspect the decided proposals, but the combined `apply` path is preferred for browser returns. No accepted entries means no new version. Progress files cannot be applied. The action record records a button decision; it does not authenticate a person's identity or prove legal correctness.

Current decision exports use format version 2: the action binds both the chosen disposition and the exact resulting entry. Changing a deferral to an approval, or changing the wording, requires a new decision. Version 1 files remain historical evidence. Resume imports their available wording and notes as pending drafts, retaining prior dispositions and actions as history; it never upgrades an old action into a current approval. The lawyer can edit and decide those candidates again. With local tools, the equivalent migration is `python scripts/objection_library.py resume --catalog catalog.json --decisions old-decisions.json --out resumed-progress.json`. Preserve the original file.

Return the usable subset and a short count of approved/remaining entries. If the served set was already supplied for objection selection, use the subset to prepare the [request-review workflow](objection-review.md) without asking the lawyer to supply it again. Otherwise, offer the direct next action: supply the served set or continue curation. Use the actual library snapshot, including its approval records and version, without retyping or paraphrasing entries. Do not label excluded, deferred, or pending entries as approved library choices. A separately requested one-off proposal may use source material with its actual provenance and review status; approval is not a requirement to discuss or draft language.

To continue curation after applying a subset:

```sh
python scripts/objection_library.py continue --catalog catalog.json \
  --decisions decisions.json --library library-v2.json --out remaining-catalog.json
```

This retains pending/deferred candidates and their edits, drops applied/excluded items, and binds a fresh batch to the resulting version. It requires the exact version produced by those decisions. Incomplete draft entries need repair before a fresh catalog can render; their original progress remains intact. If another session changed the library, reconcile against that actual snapshot instead. Do not change the base hash alone or overwrite a concurrent version. Return only decisions affected by changed wording or scope for further review.

Automatic Word-to-library updates and returned-Word feedback curation are outside this first supported workflow. Keep later Word changes in the lawyer's document unless a separate task requests reusable changes. The earlier [feedback reference](objection-libraries.md) remains development material; do not launch that extra cycle after ordinary Word delivery.
