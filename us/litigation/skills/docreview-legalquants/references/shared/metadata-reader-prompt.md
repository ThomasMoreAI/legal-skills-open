# Metadata reader contract

Read exactly one document in a fresh context. Use only the supplied document
and return the JSON schema in `metadata-reader.schema.json`. Do not use the
path or filename as evidence.

- Classify a base contract of any kind as `agreement`. Use the narrower type
  only for an amendment, statement of work, schedule, exhibit, or guaranty.
- Report the document's own title and execution, made-as-of, or effective date.
  Do not substitute a filing date or the date of a referenced agreement.
- Parties are the contracting parties, not counsel, signatories, or entities
  mentioned only in recitals.
- References are distinct contract instruments needed to assemble the family.
  Do not report section cross-references, table-of-contents entries, SEC exhibit
  numbers, or schedules/exhibits contained inside the same file.
- Set `gap_eligible` true only when the quoted text establishes that the
  distinct referenced instrument should exist separately and may be missing
  from the room. A bare exhibit designator is never enough.
- Copy exact document text for every evidence quote. Use null, an empty list,
  or `other` when the document does not establish the claim.
- For supplied native text, set `receipt_mode` to `text` and every receipt's
  `page` to null. For supplied page images, set `receipt_mode` to
  `image-transcription`, transcribe the visible words faithfully, and put the
  1-based source page on every receipt. Image transcriptions are proposals for
  the lawyer's human-verification lane; never claim a script verified them.

The orchestrator supplies the document ID and document content. The worker
must return that exact ID. It must not select a model, inspect other documents,
or decide whether its output passed validation.
