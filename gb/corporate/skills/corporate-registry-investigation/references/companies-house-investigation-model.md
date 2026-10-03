# Companies House Investigation Model

Use this reference for UK company registry investigation.

## Investigation Flow

1. **Search** - resolve name to company number; prefer exact company number.
2. **Profile** - status, incorporation, registered office, SIC, accounts, confirmation statement.
3. **Officers** - current/former officers, appointment/resignation dates, officer ids where available.
4. **PSCs** - persons/entities with significant control and natures of control.
5. **Charges** - outstanding/satisfied charges, secured parties, classification, particulars.
6. **Filing history** - accounts, confirmation statements, name changes, charges, insolvency/strike-off/restoration filings.
7. **Filing extraction** - read filing text where possible.
8. **Risk and follow-up** - registry facts, leads, and verification queue.

## Access Modes

Use:

- `live_registry` - profile/pages/API retrieved in-session.
- `user_supplied_registry` - user supplies profile PDF, filing PDFs, screenshots, HTML, CSV, API export, or copied text.
- `no_source` - prepare search plan only.

Do not state registry facts without live or user-supplied registry material.

## Snapshot Fields

```yaml
company_snapshot:
  company_name: string
  company_number: string
  status: string
  incorporation_date: string
  registered_office: string
  sic_codes: []
  accounts_status: string
  confirmation_statement_status: string
  source_mode: live_registry | user_supplied_registry
  date_checked: string
```

## Officer and PSC Cautions

Do not conflate individuals by name alone. Use:

- officer id,
- month/year of birth where public,
- service address,
- appointment/resignation dates,
- source filing,
- corporate officer identifiers.

If uncertain, mark `possible_match_needs_verification`.

Do not infer wrongdoing, nominee status, control, or beneficial ownership from nationality, residence, service address, or name pattern alone.

## Charges

For each charge:

- creation date,
- registration date,
- status,
- persons entitled,
- classification,
- particulars,
- assets charged,
- floating charge indicators,
- negative pledge or crystallisation language where visible,
- satisfaction/release filings.

Outstanding charges are diligence leads, not distress findings.

## Filing Extraction Methods

Classify extraction method:

- `json`
- `xhtml`
- `xml`
- `ixbrl`
- `pdf_native`
- `pdf_scanned_no_ocr`
- `unsupported`
- `source_missing`

If a filing is scanned or text extraction fails, ask for OCR or another source. Do not invent filing contents from filing title.

## Risk Signal Rubric

Registry risk leads:

- overdue accounts,
- overdue confirmation statement,
- non-active company status,
- liquidation/administration/insolvency marker,
- strike-off/restoration history,
- rapid officer churn,
- unresolved charges,
- repeated address/corporate-officer patterns,
- missing/odd PSC statement,
- consolidated/group filings.

Label these as `risk_lead`, not findings or allegations.

## Group Role Heuristics

Potential group indicators:

- corporate PSC,
- parent/subsidiary language in filings,
- consolidated accounts,
- group accounts exemption,
- charges involving group security,
- intercompany names or addresses.

Mark as `group_role_indicator` unless verified from filings.

## Output Contract

Use:

```yaml
company_snapshot: {}
registry_evidence: []
officers: []
pscs: []
charges: []
filings_reviewed: []
risk_leads: []
group_role_indicators: []
identity_cautions: []
follow_up: []
```
