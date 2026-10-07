# Example Output

## Scenario

User asks: "Compile the client, partner, and associate markups against `Draft_3_Master.docx`. Do not merge anything. I want a checklist."

Access state: file mode. Claude can read extracted DOCX comments/revisions from three reviewer files.

## Good Output Shape

```yaml
source_summary:
  master: "Draft_3_Master.docx"
  reviewer_files:
    - file: "Client_markup.docx"
      reviewer: "Client"
      items_extracted: 8
    - file: "Partner_markup.docx"
      reviewer: "Partner"
      items_extracted: 11
    - file: "Associate_markup.docx"
      reviewer: "Associate"
      items_extracted: 5
  not_merged: true

checklist:
  - id: CRF-001
    source_file: "Partner_markup.docx"
    source_item_id: "comment-12"
    source_timestamp: "2026-05-10T14:32:00"
    location: "Clause 6.2, limitation of liability"
    location_confidence: exact
    reviewer: "Partner"
    type: comment
    proposal: "Check whether the carve-out should include fraud, wilful misconduct, and injunctive relief."
    context: "Nothing in this clause limits liability for death or personal injury..."
    status: open
    notes: ""
  - id: CRF-002
    source_file: "Client_markup.docx"
    source_item_id: "revision-7"
    source_timestamp: "2026-05-10T09:18:00"
    location: "Clause 8.1, indemnity"
    location_confidence: approximate
    reviewer: "Client"
    type: deletion
    proposal: "Delete supplier indemnity in full."
    context: "The Supplier shall indemnify the Customer against..."
    status: open
    notes: ""

conflicts:
  - conflict_id: CON-001
    location: "Clause 8.1, indemnity"
    items: [CRF-002, CRF-009]
    issue: "Client proposes deletion; partner proposes expanding the indemnity to include regulatory fines."
    next_step: "Lawyer to settle commercial/legal position before editing the master."

manual_review:
  - source_file: "Associate_markup.docx"
    source_item_id: "revision-15"
    location: "Schedule 2 table"
    reason: "Table revision could not be extracted reliably."
    status: needs_manual_review
```

## Bad Output To Avoid

```text
I merged the comments and accepted the sensible changes.
```

Never accept, reject, or merge changes. The output is a checklist for the lawyer.
