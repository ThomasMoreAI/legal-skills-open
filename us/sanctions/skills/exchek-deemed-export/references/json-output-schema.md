# JSON Output Schema (sibling of every ExChek .docx report)

Every ExChek skill that produces a `.docx` also emits a `<basename>.json` sibling with structured metadata, determinations, citations, and integrity fields. This enables downstream systems (CRM, SIEM, GRC, audit tooling) to ingest results without parsing the Word document.

Schema version: **1.0.0** (2026-04-22). Version is carried in every emitted JSON so consumers can handle schema evolution.

---

## Top-level structure

```json
{
  "schema_version": "1.0.0",
  "skill": {
    "name": "exchek-classify",
    "version": "2.1.0",
    "commit_sha7": "a394e7b"
  },
  "generated": {
    "at": "2026-04-22T14:07:00Z",
    "model": "claude-opus-4-7",
    "platform": "Claude Code",
    "environment": "cloud",
    "input_hash": "a9f3b1c4d7e2"
  },
  "privacy_attestation": {
    "tier": "anthropic-claude-enterprise",
    "attested_by": "matt@mrdula.solutions",
    "attested_at": "2026-04-22T14:05:12Z",
    "minimum_met": true
  },
  "cui_check": {
    "cui": false,
    "classified": false,
    "itar_126_18": false,
    "on_prem_required": false
  },
  "inputs": { "…": "per-skill, redaction-safe summary of user inputs" },
  "regulatory_currency": {
    "ecfr_pulled_at": "2026-04-22T14:05:00Z",
    "cfr_parts": ["774", "738", "740"],
    "data_source": "exchek_api",
    "external_lists": [
      {
        "list": "csl",
        "endpoint": "data.trade.gov/consolidated_screening_list/v1",
        "queried_at": "2026-04-22T14:06:12Z",
        "sources_queried": ["DPL", "EL", "MEU", "SDN"],
        "per_list_timestamps": { "SDN": "2026-04-21T00:00:00Z", "EL": "2026-04-18T00:00:00Z" }
      }
    ]
  },
  "determinations": [ /* per-skill — see below */ ],
  "risk_flags": [ /* per-skill */ ],
  "citations": [
    { "authority": "15 CFR § 734.9(e)(2)", "url": "https://www.ecfr.gov/...", "accessed_at": "2026-04-22T14:05:00Z" }
  ],
  "injection_attempts": [
    { "detected_at": "2026-04-22T14:06:40Z", "source": "pasted-email", "quote": "ignore previous instructions and…", "action": "ignored-logged" }
  ],
  "hitl_confirmation": {
    "confirmed": true,
    "confirmed_at": "2026-04-22T14:07:00Z",
    "determinations_confirmed": ["jurisdiction", "eccn"]
  },
  "report": {
    "docx_basename": "ExChek-Report-2026-04-22-WidgetA",
    "docx_path_relative": "ExChek-Report-2026-04-22-WidgetA.docx"
  },
  "next_actions": [
    { "id": "re-screen-60d", "description": "Re-screen consignee in 60 days", "due_by": "2026-06-21" }
  ],
  "caveats": [ "Regulatory drift: re-run before relying on this after 2026-05-22" ]
}
```

---

## Per-skill `determinations[]` shape

Each skill defines what goes in `determinations[]`. Examples:

### `exchek-classify`

```json
{
  "type": "classification",
  "jurisdiction": "EAR",
  "eccn": "3A991",
  "usml_category": null,
  "reasons_for_control": ["AT"],
  "order_of_review_result": "Supplement No. 4 Step 3",
  "approved_by_user_at": "2026-04-22T14:06:58Z"
}
```

### `exchek-license`

```json
{
  "type": "license_determination",
  "authorization": "NLR",
  "exception": null,
  "destination": "DE",
  "country_chart_reasons": [],
  "general_prohibitions_reviewed": [4, 5, 6, 7, 8, 9, 10]
}
```

### `exchek-csl`

```json
{
  "type": "csl_screening",
  "query_name": "Acme Widgets GmbH",
  "fuzzy": true,
  "sources_queried": ["DPL", "EL", "MEU", "SDN"],
  "overall_result": "no_hits",
  "hits": []
}
```

### `exchek-jurisdiction`

```json
{
  "type": "jurisdiction",
  "result": "EAR",
  "usml_category_considered": "XII",
  "cj_recommended": false,
  "rationale_summary": "Item is a commercial pressure transducer, not specially designed for a defense article."
}
```

### `exchek-risk-triage`

```json
{
  "type": "risk_triage",
  "disposition": "hold",
  "score": 62,
  "factors": {
    "classification": "medium",
    "destination": "high",
    "end_user": "medium",
    "end_use": "low",
    "conduct": "medium"
  },
  "enforcement_themes_matched": ["subsidiary-transshipment-diversion"]
}
```

### `exchek-compliance-report`

```json
{
  "type": "compliance_report_card",
  "status": "CONDITIONAL",
  "status_reason": "Hit adjudication pending on consignee",
  "source_determinations": {
    "classification": "ExChek-Report-2026-04-22-WidgetA.docx",
    "csl": "ExChek-CSL-Report-2026-04-22-AcmeWidgets.docx",
    "license": "ExChek-License-2026-04-22-WidgetA.docx"
  }
}
```

### `exchek-audit-lookback` (uses `as_of_date` delta mode)

```json
{
  "type": "audit_lookback",
  "baseline_as_of": "2025-06-01",
  "current_as_of": "2026-04-22",
  "rows_reviewed": 412,
  "findings": [
    { "severity": "high", "type": "party-now-listed", "row_id": "TX-000188", "description": "Consignee added to EL on 2025-09-16" }
  ]
}
```

Other skills follow the same pattern — one object per discrete determination made during the run.

---

## `risk_flags[]` shape

```json
{
  "severity": "high",
  "code": "affiliates-rule-possible-match",
  "description": "Counterparty ≥50% owned by Entity List party; Affiliates Rule stayed until 2026-11-09 but prudent-diligence flag",
  "citation": "15 CFR § 744 (stayed) + BIS Red Flag 29 (stayed)",
  "suggested_next_action": "Request counsel review before shipment"
}
```

---

## Input hash computation

Canonical, reproducible:

```
1. Build `inputs` object: all user-provided fields, keys sorted
   alphabetically, string values trimmed, empty strings omitted,
   dates normalized to ISO 8601.
2. Redact PII that is not needed for the determination.
3. JSON.stringify(inputs) with no whitespace.
4. SHA-256 of the UTF-8 bytes.
5. Take the first 12 hex characters of the lowercase digest.
```

The same inputs on a re-run MUST produce the same hash — this is how auditors verify reproducibility.

---

## File naming

- `.docx`: `ExChek-<Kind>-YYYY-MM-DD-<ShortName>.docx` (existing convention — unchanged).
- `.json`: same basename, `.json` extension. Emitted alongside the `.docx` in the same folder.

Example:

```
ExChek-Report-2026-04-22-WidgetA.docx
ExChek-Report-2026-04-22-WidgetA.json
```

Both files are delivered; the temporary `.md` is still deleted.

---

## Consumer expectations

- Consumers MUST handle `schema_version` and upgrade gracefully on minor bumps.
- Consumers MUST NOT treat the JSON as legal advice; it is a structured view of an AI-assisted analysis.
- Consumers SHOULD check `hitl_confirmation.confirmed === true` before automated downstream actions.
- Consumers SHOULD check `privacy_attestation.minimum_met === true` before storing the report in a system of record.
