# Example Output

## Scenario

User asks: "Build me a working chronology from the public judgment in DnaNudge and the pleaded conversion dispute. Keep source pinpoints."

Access state: live source mode. Claude retrieved DnaNudge Limited v Ventura Capital GP Limited [2023] EWCA Civ 1142 from Find Case Law.

## Good Output Shape

```yaml
access_mode: live_source
scope:
  date_range: "2023-03-08 to 2023-10-05"
  sources_reviewed:
    - "DnaNudge Limited v Ventura Capital GP Limited [2023] EWCA Civ 1142, Find Case Law"

chronology:
  - event_date: "2023-03-08"
    document_date: "2023-10-05"
    date_extracted_from: "judgment para 1"
    date_certainty: exact
    actor: "HHJ Hodge KC"
    event: "High Court decision determined that conversion of Series A shares was void for lack of required written consent."
    source_identifier: "DnaNudge [2023] EWCA Civ 1142 at [1]"
    source_date: "2023-10-05"
    quote: "The Judge determined that the conversion... was void and of no effect because the conversion had not received the consent in writing..."
    confidence: high
    tags: [appeal_background, share_conversion, articles]
    notes: ""

  - event_date: "2023-10-05"
    document_date: "2023-10-05"
    date_extracted_from: "judgment date"
    date_certainty: exact
    actor: "Court of Appeal"
    event: "Court of Appeal gave judgment in DnaNudge appeal."
    source_identifier: "DnaNudge [2023] EWCA Civ 1142"
    source_date: "2023-10-05"
    quote: "Lord Justice Snowden"
    confidence: high
    tags: [appeal, judgment]
    notes: "Judgment author shown in public source."

gaps:
  - period: "Before the claim"
    issue: "Underlying company notices, articles, and shareholder communications not included in this public-source-only chronology."
    request: "Add pleadings, articles, notices, and shareholder correspondence for a matter chronology."

disputed_or_low_confidence:
  - event_date: "conversion date"
    issue: "Public judgment extract used here does not provide enough source material to build full transaction chronology."
    status: source_missing
```

## No-Source Mode

```yaml
access_mode: no_source
output: chronology_schema_only
source_requests:
  - "Correspondence bundle"
  - "Pleadings"
  - "Orders/notices"
  - "Witness statements or attendance notes"
```
