# Curate objection wording and review Word feedback

**Development reference — outside the first supported workflow.** The supported path is initial source-linked [library curation](objection-library-builder.md), [request review and Word delivery](objection-review.md). Preserve this earlier feedback design and its artifacts; do not start it automatically when Word is returned or present it as a required step. Later Word editing remains unrestricted.

The library is a user-selected work product, not ambient memory or shipped firm policy. This workflow uses the same approved snapshot as [objection review](objection-review.md). Keep pending proposals separate from selectable entries. Use ordinary host document tools first, then firm-authorized specialist comparison/research tools if selected. No model SDK, installation, shared account or remote service is required.

## Build a useful subset

Read [objection-library-builder.md](objection-library-builder.md) for source extraction, variant grouping, the offline candidate-curation page, and saving an approved subset. It uses the same library/proposal format as Word feedback. Prior use, repeated edits, and completed parsing do not approve reusable wording.

## Read returned Word edits

Keep the actual delivered baseline and its assembly record. Compare the returned DOCX to that baseline even when revisions were already accepted. Read tracked insertions/deletions, moved passages and relevant comments with available document tools. Do not treat absence of tracked changes as absence of edits.

An optional narrow extraction helper provides a starting observation record:

```sh
python scripts/objection_word.py compare --assembly assembly-with-baseline.json \
  --baseline responses.docx --docx returned.docx --out word-observations.json
```

It compares accepted main-body paragraph text, binds the baseline hash, and reports changed passages with component overlaps. It reads text in tables and preserves whitespace. It does not compare formatting, headers/footers, notes, graphics or all Word revision semantics. Comments are returned as unanchored context; use host tools to recover their actual anchors before associating them with a passage. Its `component_overlap` is evidence to confirm, not a finding of legal intent. Mixed edits, insertions at a component boundary, moved text, or altered request text may require explicit contextual reconciliation.

Use request text, served occurrence, component wording and surrounding response context to confirm origins. Do not guess an entry from a repeated phrase or paragraph index. Keep uncertain passages unresolved with the competing interpretations visible. A changed request does not itself authorize changing the served instrument in a later draft.

Classify with judgment:

| Classification | Treatment |
| --- | --- |
| `replacement` | Propose exact reusable wording against its original variant. |
| `new_variant` | Keep the original; propose a new stable ID and explicit recurring context. |
| `guidance` | Propose usage guidance without changing the wording. |
| `new_entry` | Propose a new one-off objection as a candidate, if reusable scope is supported. |
| `matter_only` | Retain the edit in the matter; do not promote it. |
| `substantive_response` | Exclude from objection policy. |
| `formatting_only` | Normally omit from the substantive proposal list. |
| `unresolved` | Show the passage and what cannot be established; do not promote. |

An unexplained deletion is not proof the objection is generally inappropriate. Repeated edits do not imply approval; deduplicate matching proposals while retaining all source contexts. If a component used substitutions or request-specific wording, recover its original library template and separately show the proposed generalization. Do not write current matter values into reusable fields.

## Persist proposals and approved versions

Save the structured proposals and a readable before/after list in the authorized working location. Each item carries its source edit/context, classification and rationale, exact original entry under `before`, proposed resulting entry under `after`, and decision state. Pending/rejected/deferred items do not influence future drafts. Keep confidential source context in the matter workspace; shared library provenance can use a nonconfidential source ID pointing to a separately authorized record.

For interactive curation, wrap those pending proposals in the [builder's catalog](objection-library-builder.md) with exact Word passages and source hashes. The page shows the current approved entry alongside the proposed result. Use its returned decision file through `objection_library.py reconcile`, then apply the resulting proposals as below. A non-reusable classification has no approval button; turning it into reusable wording requires an explicit, supported new proposal.

Returning redlines authorizes analysis and saving proposals. It authorizes library promotion only when the instruction identifies the exact reusable change and scope. Apply explicit decisions without asking for another ceremonial confirmation:

```sh
python scripts/objection_review.py apply-library --library library-v1.json \
  --proposals library-proposals.json --out library-v2.json
```

The operation checks the original snapshot and before-entry, applies only accepted reusable classifications, creates a new version and preserves the prior file. Conflicting accepted changes to one entry, a stale base or a repeated batch are rejected. Use a new output filename; never overwrite a concurrent update. Reconcile conflicts against the actual current library and return only the affected decisions for review. Rejected proposals remain in their saved proposal record.

Use the explicit new snapshot for the next set. Keep earlier Word drafts bound to the version they used. No observation automatically becomes firm practice, a global preference or retraining data. Retain these purposeful work products; remove only disposable extraction intermediates when done.
