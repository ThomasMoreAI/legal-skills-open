# Review objections and deliver Word responses

Use this workflow when the lawyer wants to inspect proposed objections to readable federal RFPs before receiving an editable Word draft. It preserves the portable handoff: open the local HTML, return the downloaded decisions, receive Word, and finish substantive responses there. A response shell or one-off draft does not require HTML or library curation; use [response-shells.md](response-shells.md) and the main skill's relevant drafting method directly.

## Start from the requested work

The automated initial Word check covers ordinary body paragraphs: each request heading, request text and selected component occupies one or more whole paragraphs. Split runs and layout-only whitespace are supported. Tables, text boxes, fields and other structures inside that region need separate host inspection; preserve the supplied format and disclose that boundary. This check does not constrain later Word drafting.

Read the served set, supplied format, and any selected library or precedent before asking questions. Infer supported case and administrative details; use descriptive blanks for ordinary missing information. Ask only when an ambiguity materially prevents useful preparation. Do not require a case-map interview for faithful reuse or assembly.

**A usable approved library is a prerequisite for this objection-selection page.** Use the actual approved snapshot supplied or selected for this run, preserving its approval records. Its approval means permission to reuse starting language, not a legal determination or a restriction on the lawyer's edits. Completed responses and examples are not an approved library. If only examples are supplied, prepare [library curation](objection-library-builder.md) first and return that page for the lawyer's decisions. A useful approved subset is sufficient; the rest can wait. Do not invent approval records or use an empty-library custom-entry page as an equivalent substitute. If neither a library nor examples are available, identify the missing input and the available shell/direct-drafting route. Shells and direct Word drafting remain available without a library.

## Capture the requests once

Preserve complete served text, printed labels, subparts, definitions/context, and order in one reusable source record. Distinguish repeated labels by occurrence and locator. Reconcile that record against the visible sources, including PDF pages where needed. Unreadable text or uncertain boundaries remain identified gaps; a count or file hash does not prove complete extraction. Continue useful work on readable material without declaring a partial set complete.

A version 2 review embeds the frozen source census. Use the packaged source helper with ordinary DOCX/text inputs; for a PDF, provide host-extracted text using `--text` at both capture and freeze, retain that text file, and compare it with the source pages. The helper records its extraction limits. It does not determine request boundaries or legal meaning.

```sh
python scripts/objection_source.py capture --source served.docx --out source-extraction.json
python scripts/objection_source.py freeze --extraction source-extraction.json \
  --mapping source-mapping.json --comparison source-comparison.json \
  --source served.docx --out source-census.json
```

Map source block spans (`block`, zero-based `start`, exclusive `end`) into ordered `requests` with stable `id`, `label_spans`, `text_spans`, and `context_ids`. Map relevant definitions/instructions under `context` with `id`, `title` and `spans`; account for remaining non-request material under `other` with `spans` and an explanation. Do not call omitted request text non-request material. The comparison record states who checked (`by`), actual `method`, `notes`, `status: checked` or `partial`, and an explicit `unresolved` list. This records source comparison already performed; it does not require another attorney approval. Unmapped or unresolved material requires partial coverage and a visible gap.

Construct `review.json` using [the record schema](../schemas/objection-records.schema.json), copying source, requests and context from the frozen census and adding the selected library and suggestions. An existing compatible review can be attached without changing its wording:

```sh
python scripts/objection_source.py attach --review draft-review.json \
  --census source-census.json --out review.json
```

The census controls the request sequence; do not modify requests independently in review JSON. Render and materialization check that the complete ordered requests and context still equal the frozen source spans. These checks detect changes after capture; the recorded source comparison addresses extraction accuracy. Reuse the capture rather than repeatedly extracting the documents.

## Surface candidates, then prepare selectable wording

Keep three states distinct:

| State | Meaning |
| --- | --- |
| Surfaced | An approved objection type has a reasonably apparent connection and appears among the request's primary choices for consideration. It need not be selected or recommended for inclusion. |
| Selected | The checkbox includes the request-specific wording in the complete Word preview. |
| Accepted | The lawyer's deliberate Export for Word authorizes the exact selected wording in that export. Opening, inspecting, or saving the page does not authorize assembly. |

For **each request**, examine its actual words and supplied context against the approved library's grounds, variants, conditions and exclusions. Surface the reasonably apparent possibilities, including multiple distinct grounds when appropriate. Use the lower threshold of a plausible connection for consideration, not the higher threshold of a fully supported recommendation to include the objection. Do not substitute a tile count for this assessment, restrict candidates to the same-numbered prior response, or repeat the entire library under every request. Source request numbers locate precedent; neither matching nor different numbers establish applicability. Consolidated entries can draw on any of their source examples.

For each surfaced candidate, give a concise reason connecting the current request to the ground, the supporting supplied context, and any material missing facts or authority limits. An unconfirmed predicate can justify a visible conditional option with an unchecked box; it does not automatically justify hiding the option. Preserve consequential qualifications in the proposed wording. Distinguish facts supplied, facts still needed, and legal questions still open. Do not invent an established burden, privilege, confidentiality fact, search result or withholding position to make an option appear complete.

Leave less apparent alternatives in **Other library objections**. Use the optional request `candidate_note` for a short assessment explanation, especially when no approved entry has a supported connection or the readable inputs leave an assessment gap. “No wording selected” describes the lawyer's current selections; it does not mean no plausible objection was identified. An empty candidate list alone is not evidence of a substantive no-objection conclusion. Do not add a new objection type merely to avoid an empty list; the lawyer may still inspect other entries or add their own wording.

The existing record field `suggestions` is the list of **surfaced** primary candidates. Each has an approved `entry_id`, named `params`, `rationale` explaining the connection, `basis` identifying the supplied support or relevant authority, and `missing` for unresolved inputs. Set `preselected: false` by default. That flag controls initial checkbox selection and Word-preview inclusion, not tile visibility. Automatic checking is separate behavior for an explicit user preference, never a remedy for failing to surface options. A model-origin checked choice is still not accepted until deliberate export.

Apply the main skill's authority method to new legal recommendations. Faithful adaptation of supplied approved starting wording does not itself establish legal validity or require a new validity determination before the option can be considered. If a relevant check is incomplete, explain the specific limitation beside that candidate; do not impose a blanket suppression rule. Put shared authority limitations once in the set details or handoff. Keep `candidate_note` focused on that request's assessment and `missing` focused on that candidate's unresolved predicates or applicable legal issue; do not repeat a generic disclaimer in every request and candidate or attach unrelated legal cautions. Stay within the skill's jurisdictional scope and avoid definitive procedural or legal claims that the available sources do not establish. Request-specific custom wording can supplement an approved library; it does not replace preparing that library when examples alone were supplied.

Library templates use `{{field_name}}` substitutions with descriptive field labels. Show the complete resulting request-specific text, including scope qualifications and any connective language that will enter Word. Review notes are separate and never silently appended. Distinguish variants by their actual differences. Do not impose categorical objection policies through a checkbox rule, immutable qualification, or hidden default.

With local Python, render the packaged offline interface:

```sh
python scripts/objection_review.py render --review review.json --out review.html
```

Resolve these skill-relative commands and working-file paths to their actual locations. Helpers write new files rather than replacing user work. No account, network resource, installation, or specialist document tool is required. Use ordinary capable host tools, with firm-selected specialist tooling as an optional rung.

The page shows each exact request followed by **Wording for Word**: the complete selected text, one component per paragraph, in its intended order. This read-only preview updates when wording is selected, deselected, edited, or reordered. Selected wording is included when the lawyer chooses Export for Word, unless the request is explicitly marked Needs input. **Review notes — not included in Word** remain visibly separate.

Horizontal tiles identify objection types, stay in library order and wrap to fit. The main choices are surfaced candidates, selected entries and custom drafts; less apparent approved types are available in one library disclosure. Their checkbox selects wording; their label opens inspection without selecting or approving it. Show the connection and material conditions in the inspector and accessible reason control, separately from wording for Word. Review actions and the opened inspector precede long lists of choices. Inspection puts request-specific wording first and makes canonical wording and source context available nearby. Existing editors and ordering controls change the same components used by preview and assembly. Keep continuous scrolling, readable labels, distinct inspection/selection/focus states, and the packaged light/dark style. Changing layout or theme does not change the legal text or review state.

## Save and return decisions

Each request is open, needs input, or reviewed. Selected wording does not require a separate Mark reviewed click: **Export for Word** records acceptance of its exact current content. Model suggestions alone are not acceptance; opening a page, inspecting wording, and saving progress never create approval. Any change to operative wording, substitutions, selection or order invalidates the earlier content binding; a subsequent export records the changed selected wording. The lawyer may revise a qualification or select a conditional option without an additional approval gate.

Keep **Mark all reviewed** visible in the toolbar. It marks current choices ready, including requests with no selected wording, while leaving explicit Needs input requests open. This review state can be saved; assembly is authorized only by deliberate export. Per-request Mark reviewed remains useful for a no-objection decision or for resolving Needs input. An untouched empty request remains open on ordinary export; a reviewed empty request records an affirmative no-objection choice. Incomplete selected wording must be completed, deselected, or left as Needs input before it can enter Word. Explain the affected request and preserve all edits.

**Save progress** preserves all work, including deselected custom text, deselected library-derived edits, unfinished blank drafts, order, and notes. It does not authorize assembly. The durable artifact is the downloaded progress file; requesting a download is not proof it reached disk. Closing the page alone does not save work. Explain Save progress and Resume plainly, with the set/library identity in the handoff. Wrong, corrupt or stale imports must preserve current work.

**Export for Word** is the assembly handoff. It binds complete selected wording in non-Needs-input requests to the exact content being exported, including any request-specific edits and component order. The lawyer returns that file here; apply it without asking for another approval of unchanged wording. Partial review can still produce a useful draft: include every request, use the accepted wording, and list unresolved request numbers outside the pleading. Empty unfinished custom wording can be saved but cannot become an operative component.

Current decisions preserve all drafts separately from their selected order and bind each accepted row to its exact content using the existing version 2 review action. Export-generated actions record `kind: batch` and `trigger: export-selected`; individual and Mark all reviewed actions remain supported. This is a content receipt, not authenticated attorney identity. Export must not record stale content if editing occurs during validation. Legacy progress may be migrated through `resume` as a draft; a new export accepts its selected wording under the same rules. Preserve the original file. Never silently reinterpret an older unreviewed record as an approval; use an explicit lawyer direction, record its source separately, and retain the original return. Wording omitted by an older export cannot be recovered from that file.

```sh
python scripts/objection_review.py resume --review review.json \
  --selections older-progress.json --out resumed-progress.json
python scripts/objection_review.py materialize --review review.json \
  --selections decisions.json --out assembly.json
```

Import validates the review/source/library identities, complete ordered request coverage, component origins and exact reviewed content. The draft stays bound to its selected library version even if a newer snapshot exists. A mismatch calls for the correct file or review of changed content, not a guessed hash edit. These checks bind content; they do not authenticate a person or determine legal sufficiency.

If interactive HTML or local scripting is unavailable, use the available host tools to present the same exact request/wording decisions and record explicit review. Disclose that changed interaction and any mechanical checks not performed; never fabricate browser actions or promise untested browser support.

## Assemble and deliver Word

Use [response-shells.md](response-shells.md) for the complete formatting and cleanup method. Adapt a copy of the supplied format with capable host document tools; use the bundled neutral RFP shell when no example is supplied. The served source controls requests, the reviewed decisions control objection text/order, and the example controls appearance. Preserve useful pleading structure, caption, drafting areas, signature and service forms. Populate supported administrative details; leave unknowns editable. Do not treat old responses or signed forms as evidence of current acts.

Insert each exact request and its reviewed components, followed by an expandable substantive-response area. For open requests, keep an ordinary drafting area and a concise unresolved item in the delivery note. This workflow leaves substantive answers for Word; do not invent search results, production commitments, withholding facts, signatures or completed service. If accepted wording itself raises a concern, identify it outside the draft rather than silently changing what the lawyer reviewed.

The initial-delivery check re-materializes expected assembly from the original review and returned decisions, then compares the whole supported Word request/response region. It checks the absence of extra unselected wording, not only whether selected passages occur. The supported helper path is ordinary main-body paragraphs with split runs; it is not a universal verifier of every Word structure. Preserve the supplied format when it needs another structure and use explicit host inspection/mapping, stating the unperformed mechanical check rather than flattening the document to satisfy the helper.

Record the actual template framing in `word-layout.json`: `kind: objection-word-layout`, `format_version: 1`, the review and selections digests, one ordered `requests` row per occurrence with `request_id`, `request_heading`, `response_heading` and `drafting_prompt`, and `after_responses` identifying the unique first post-response paragraph, such as the actual signature/date line. Keep the exact served label in `request_heading`; the response heading or drafting prompt may be empty when the format has none. Framing describes template headings and drafting prompts, not a place to put extra objections or substantive answers. The helper normalizes layout whitespace only; substantive text and punctuation remain exact.

```sh
python scripts/objection_word.py bind --assembly assembly.json \
  --review review.json --selections decisions.json --layout word-layout.json \
  --docx responses.docx --out assembly-with-baseline.json
```

Independently inspect all relevant document stories, retained drawings/fields and stored content for prior-matter carryover. Render and inspect every page, comparing corresponding regions with the supplied format. When an editable application is available, use a separate check copy to expand a response, edit a form slot, save and reopen. A successful XML match or render alone does not establish native Word editability.

Deliver the **DOCX first**, with covered set/count, a short list of unresolved request numbers or administrative blanks, and the next action: finish substantive responses in Word. Keep the actual initial delivery, decisions and source records as a coherent baseline in the authorized workspace; save later corrections separately. The initial assembly check does not restrict subsequent Word edits. Do not automatically initiate Word-to-library feedback, propose changes to an approved library from redlines, or add another return loop to this first supported workflow.
