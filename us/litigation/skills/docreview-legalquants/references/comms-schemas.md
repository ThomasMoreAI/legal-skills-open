# /docreview data contracts

`/docreview` uses the locally bundled Stage 1 manifest, read-plan, canonical
metadata, and gap-report contracts originally shared with `/diligence`. This
file defines the disputes relationship layer and privilege hold. Artifacts use
sorted keys and stable IDs and contain no timestamps added by the run, absolute
paths, or host names.

For non-message singletons under an enumerated request or issue frame, the
prospective read-plan policy defaults to metadata deferral when no
canonical-metadata consumer is active. The workflow still presents both plans,
and only after the lawyer approves the deferred lane at Gate 1 do those
singletons use `deferred-to-review` while remaining fully in scope for the
finding pass. The shared read-plan, placeholder, reversal, and partition rules
are defined in `references/shared/schemas.md`.

## messages.json

`parse_messages.py` writes one canonical record per unique message hash:

```json
{
  "messages": {
    "sha256:ab12cd34ef56": {
      "path": "farmer-d/inbox/42.eml",
      "custodian": "farmer-d",
      "folder": "inbox",
      "from": "jane@example.com",
      "to": ["mark@example.com"],
      "cc": [],
      "date": "2001-03-14T16:02:00+00:00",
      "date_local": "2001-03-14T08:02:00-08:00",
      "subject": "meter 6315",
      "message_id": "<1234.JavaMail@host>",
      "in_reply_to": ["<1230.JavaMail@host>"],
      "references": ["<1230.JavaMail@host>"],
      "has_attachments": false,
      "body_fp": "874c79cd261f",
      "duplicate_paths": []
    }
  },
  "non_messages": ["sha256:0c77d1e2f3a4"]
}
```

- `date` is UTC-normalized. `date_local` preserves the sender offset and drives
  collection-month gaps.
- `in_reply_to`, `references`, `to`, `cc`, and `duplicate_paths` are always
  arrays. The clusterer normalizes legacy scalar-or-null relationship fields
  before use.
- `body_fp` is a deterministic normalized-body fingerprint used only for copy
  quorum checks. It is not a document identity or a substantive finding.
- Custodian is the first relative path segment. Non-messages use the shared
  isolated document-reader path before any issue review.

## clusters.json

```json
{
  "threads": [
    {
      "cluster_id": "t2d68bd3ce281",
      "members": ["sha256:ab12cd34ef56", "sha256:cd34ef56ab12"],
      "basis": {
        "kind": "thread",
        "normalized_subjects": ["meter 6315"],
        "reference_links": 1
      }
    }
  ],
  "channels": [
    {
      "cluster_id": "c676a6451678e",
      "members": [
        "sha256:ab12cd34ef56",
        "sha256:cd34ef56ab12",
        "sha256:ef56ab12cd34"
      ],
      "basis": {
        "kind": "participant-set",
        "participants": ["jane@example.com", "mark@example.com"],
        "occurrences": 3
      }
    }
  ],
  "custodian_months": {
    "farmer-d": {"2001-02": 210, "2001-03": 190}
  }
}
```

Threads use normalized subject plus message-ID reference chains and
deterministic union-find. Channels are normalized participant sets occurring
at least three times. Both use `cluster_id`; relationship facts live under
`basis`. A thread is the issue-review unit. A message outside a multi-message
thread remains a singleton unit.

## Shared gap report

`comms_gaps.py` merges, deduplicates, and sorts its entries in the existing
`gap-report.json`; it never replaces manifest or index entries. It adds:

- `custodian-gap`: a zero-message custodian month between populated neighbor
  months, or an indexed custodian with no produced messages.
- `thread-gap`: an absent cited message-ID or a missing archive copy under the
  documented quorum rule. It also records the message-parser scope limitation
  when a production contains non-message artifacts but zero parseable native
  messages. Flattened PDFs and images remain singleton review units; their
  filenames are not evidence of participants, dates, or thread relationships.

## Privilege queue and hold

Workers never decide privilege. Any of these signals emits a candidate:
`attorney-domain`, `legend`, `legal-advice-content`, or `counsel-name`.

```json
{
  "candidates": [
    {
      "doc_id": "sha256:ab12cd34ef56",
      "reason": "The message requests legal advice from identified counsel.",
      "quote": "Please advise us on the legal exposure.",
      "receipt_mode": "text",
      "page": null,
      "signals": ["counsel-name", "legal-advice-content"]
    }
  ],
  "ruled": [
    {
      "doc_id": "sha256:cd34ef56ab12",
      "reason": "Business-only distribution list.",
      "quote": "Weekly sales totals attached.",
      "receipt_mode": "text",
      "page": null,
      "signals": ["attorney-domain"],
      "ruling": "not-privileged",
      "by": "lawyer"
    }
  ]
}
```

Only an explicit lawyer ruling moves a record to `ruled`. Pending candidates,
`privileged` rulings, and `needs-review` rulings remain held. Only
`not-privileged` releases the document. A held document holds its entire
thread or family unit. Reconciliation, report rendering, and register export
fail closed if a finding touches a held unit.

`render_privilege_queue.py` is the lawyer-facing decision surface. Pass the
queue, normalized messages, manifest, and original document root so every
candidate has a source-document link. The visible page uses plain-language
candidate explanations and keeps stable IDs, raw signal names, and model
candidate reasons under collapsed technical receipts. It exports
`privilege-rulings.json`, whose exact shape is
`privilege-rulings.schema.json`. The receipt covers every pending candidate
exactly once and binds the exact queue and manifest digests.

`ingest_privilege_rulings.py` validates those bindings before writing a new
queue copy. It never overwrites the source queue. Each moved record preserves
the candidate quote, reason, receipt, and signals and adds only `ruling`,
`by: lawyer`, and `lawyer_note`. Queue or manifest drift exits nonzero before
output. The rendered page itself records nothing and never releases a hold.

## Review setup and approval receipt

`render_dmap.py` consumes the canonical shapes above and produces one
self-contained pre-review surface. The primary flow asks whether the legal
review questions are right, whether the collection coverage looks expected,
and whether the proposed test sample is useful. Custodian/date detail and gaps
support those decisions. Execution mode, channels, hashes, plan IDs, worker
mechanics, and reproducibility assurances remain available under collapsed
technical receipts.

The offline page never starts review. It exports `review-setup-approval.json`,
whose exact schema is `review-setup-approval.schema.json`. The receipt binds the
corpus, manifest, framework, relationship map, metadata policy, review plan,
unit IDs, and issue IDs, and authorizes only the sample. It contains no
timestamp so repeated exports are byte-stable. `approval_source` is
`offline-export`, or `conversation` when the lawyer explicitly approves all
four decisions in the task rather than through the page.

`ingest_review_setup_approval.py` validates every binding before writing
`review-plan.approved.json` and `clusters.confirmed.json`. Drift or an incomplete
decision exits nonzero before either output is written. Source artifacts are
never overwritten: the plan copy changes only `approved` and `approval`; the
cluster copy adds only `confirmed: true`.

## instruments.json and typed request frames

`parse_instruments.py` writes a deterministic census before any interpretive
review. The exact top-level shape is:

```json
{
  "counts": {
    "by_kind": {"rfa": 4, "rfp": 12, "srog": 3},
    "elements": 19,
    "instruments": 3
  },
  "instruments": [
    {
      "elements": [
        {"no": 1, "text": "Admit the stated fact."},
        {"no": 1, "series": "D", "text": "Admit the synthetic record."}
      ],
      "instrument_id": "rfa-set-one",
      "kind": "rfa",
      "label": "RFA Set One.md",
      "party": null,
      "set": null,
      "staged": false
    }
  ]
}
```

Kinds are `rfp`, `rfa`, `srog`, and explicitly declared `issues-list`.
Instrument IDs are stable filename-stem slugs. Plain served designators use
positive ASCII integers. A compound designator such as `D-1` stores `no: 1`
plus optional `series: "D"`; the grammar is uppercase letters, one hyphen, and
a positive ASCII integer. The `series` key is omitted for plain elements.
Served designators and element text are preserved exactly; numbering gaps
remain gaps, and duplicates or unclassifiable designators are refused. Counts
cover both plain and series elements across the entire census, including sets
staged rather than compiled in the current framework.

The shared `framework-schema.md` defines the optional `frame` block and each
item's singular `target_ref`. A requests frame uses one item per non-staged
element. `validate_framework.py --instruments` proves that every such element
is represented exactly once, target IDs exist, and each lens aligns with its
instrument. The frame's optional `corpus_id` is compared with the manifest
when both are supplied.

## Production review and review-feedback.json

`render_crosswalk.py` joins `findings[].issue_id` through the framework item to
its `target_ref` and renders one deterministic, self-contained HTML review:

- **Requests** is the default orientation: one row per served request, full
  request text, responsive documents first, and reviewed-negative documents
  collapsed. Requests with no responsive document are visible without being
  overstated beyond the approved tier.
- **Documents** shows each produced file and only the requests it matched.
  Outside-tier and reviewed-negative files are opt-in under the default
  responsive-only filter.
- A file with one or more unresolved calls appears once in **Needs attention**,
  not once per request. `unresolved` does not by itself mean the file was
  unreadable; the machine explanation and available safe inline review copy
  remain visible there for the lawyer's call.
  Image transcriptions remain labeled **Needs your eyes**.
- Privilege candidates and recorded queue rulings remain a separate document
  property. The review UI does not release a hold or mutate the privilege
  queue.
- Wire statuses remain `present`, `absent`, and `unresolved`. Main-view labels
  are `Responsive`, `Nothing found`, and `Needs a decision`; stable IDs remain in
  expandable receipts rather than the main reading flow.

Every render receives `--document-root` and the sibling `--review-copies`
sidecar. The renderer revalidates exact manifest coverage, source bytes,
derivative bytes, and bundle contents before embedding anything. EML previews
include decoded headers, body text, and separately receipted attachments
without executing embedded or remote content. Request-side finding cards open
and expand the corresponding verified copy in the Documents tab. The original
file remains a secondary provenance link.

### Review render contract

Every in-scope reviewed document and attachment needs an inline reviewable
representation. A raw-file link is provenance only. The universal review-copy
builder covers EML, ordinary text-family files, common images, browser-native
PDF, and safe visible text from readable DOCX, XLSX, and PPTX packages.
Optional Poppler and LibreOffice support may add page images or rendered PDFs.
Each derivative binds to the immutable source document ID, records the renderer
and version, preserves page order, and hashes every output. The original
remains evidence; the derivative is labeled as a review copy and never receives
a new responsiveness proposal.

If a review representation cannot be produced, park the document and any
dependent findings in a visible `Needs rendering` lane. Do not substitute an
original-file link or extracted text when visual layout may matter. The tool
cascade is built-in preview → available open-source renderer → firm-selected
native/legal-grade renderer. Verified ready copies remain visible even when a
different document is parked in Needs rendering, but dependent approval and
feedback export stay locked.

The page works from `file://`, makes no external request, and exports the
lawyer's explicit per-finding rulings plus document-level image-review
confirmations as `review-feedback.json`. Rulings are sorted by `finding_id`;
image confirmations are sorted by `doc_id`; neither browser export nor
deterministic ingest adds a timestamp. The exact JSON Schema is
`review-feedback.schema.json`:

```json
{
  "artifact": "review-feedback",
  "version": 1,
  "review_plan_id": "3efae5fc4f6e1720",
  "framework_version": 1,
  "framework_digest": "sha256:...",
  "frame_id": "matter-rfp-audit",
  "corpus_id": "0123456789abcdef",
  "ledger_digest": "sha256:...",
  "source": "findings.sample.checked.json",
  "image_confirmations": [
    {
      "confirmation": "confirmed",
      "confirmed_by": "lawyer",
      "doc_id": "sha256:ab12cd34ef56",
      "finding_ids": ["rfp-set-001/sha256:ab12cd34ef56"],
      "note": "Reviewed the complete image-based request bundle.",
      "proposal_digest": "sha256:..."
    }
  ],
  "rulings": [
    {
      "finding_id": "rfp-set-001/sha256:ab12cd34ef56",
      "issue_id": "rfp-set-001",
      "doc_id": "sha256:ab12cd34ef56",
      "machine_status": "present",
      "ruling": "responsive",
      "note": "",
      "ruled_by": "lawyer"
    }
  ]
}
```

Ruling values are `responsive`, `not-responsive`, `needs-review`, and
`privileged`. An image confirmation is `confirmed` or `needs-review`. It covers
one document's complete set of image-lane finding calls, including responsive,
no-match, and unresolved proposals. `finding_ids` and `proposal_digest` bind
that exact bundle; a changed call, status, quote, reason, or receipt makes the
confirmation stale. `ledger_digest` hashes the canonical proposal ledger with
both `lawyer_ruling` and `image_confirmations` overlays removed, so proposal
identity stays stable across repeated review rounds. `framework_digest` hashes
the whole framework, not only its version number.

`ingest_review_feedback.py --feedback review-feedback.json --findings
findings.json --framework framework.json --manifest manifest.json --out
findings.ruled.json` validates every binding and subject before writing. It
refuses stale ledger, framework, review-plan, frame, corpus, version, machine
status, duplicate, unknown-finding, and stale image-bundle inputs. The output
is a deterministic copy; source proposal fields and evidence receipts are
unchanged. A ruling adds only the following per-finding overlay:

```json
{
  "lawyer_ruling": {
    "note": "",
    "ruled_by": "lawyer",
    "ruling": "responsive"
  }
}
```

Confirmed image bundles are stored only in the additive top-level
`image_confirmations` array. The output path must differ from the source
findings path. Re-render the ruled copy to show the overlays; a `privileged`
overlay redacts the excerpt in the main view while the proposal and its receipt
remain in the bound ledger.

## Document Review Gate 3 image reconciliation

Run `reconcile_docreview_gate3.py` with the same manifest, findings,
framework, relationship maps, privilege queue, and approved review plan used
by shared reconciliation. It composes `reconcile_counts.py` without modifying
that shared script. A lawyer-confirmed, exact image bundle may satisfy only the
shared error that an image-derived present finding is not script-verifiable;
it cannot waive missing coverage, a bad stable ID, an empty quote, a checker
failure, a privilege hold, or any other error.

The deterministic output follows
`docreview-gate3-reconciliation.schema.json`. Exit 0 requires ordinary
coverage reconciliation plus `confirmed` overlays for every image-review
document. Missing, `needs-review`, duplicated, non-lawyer, extra-document,
stale-finding-list, or stale-proposal-digest confirmations exit 1. The report
names every exact shared error satisfied by a lawyer image confirmation and
retains the immutable machine receipt as `human-required`; it never rewrites
that receipt to `confirmed`.
