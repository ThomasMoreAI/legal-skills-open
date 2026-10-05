# APP framework verification method

## Verification layers

Do not describe user-supplied JSON as verified law. Establish and report five
layers independently:

1. `APP text`: complete Schedule 1 text and structure from the applicable
   authorised Privacy Act compilation.
2. `Application perimeter`: relevant definitions, territorial application,
   entities, exemptions, permitted situations and enforcement provisions,
   including sections 5B, 6, 6A–6D, 7–7C and 13–16C.
3. `Codes and instruments`: Part IIIB, section 100, Privacy Regulations and the
   OAIC registered-code inventory applicable to the facts.
4. `Known future amendments`: enacted changes whose future compilation may not
   yet exist, including C2024A00128 Schedule 1 Part 15 items 87–88 (application provision item 89) commencing
   10 December 2026.
5. `Guidance`: separately versioned OAIC APP Guidelines and topic guidance.

Use the Federal Register and `$check-commonwealth-legislation` for current law.
Use `$trace-commonwealth-legislative-change` across any amendment,
commencement, deployment or retention horizon. Check the OAIC code register and
guidance pages separately. Case law is outside scope.

## Inventory schema

The script requires a provenance-bound comparison object:

```json
{
  "title_id": "C2004A03712",
  "compilation_id": "<Federal Register compilation ID>",
  "as_at": "YYYY-MM-DD",
  "source": {
    "canonical_url": "https://www.legislation.gov.au/C2004A03712/<compilation ID or effective-from date>",
    "final_url": "<same canonical path after retrieval>",
    "retrieved_at": "YYYY-MM-DDTHH:MM:SSZ",
    "raw_sha256": "<SHA-256 of the retrieved official document>",
    "effective_from": "YYYY-MM-DD",
    "effective_to": null
  },
  "coverage": {"schedule": "Schedule 1", "complete": true, "method": "Inspected complete official boundaries"},
  "principles": [
    {"identifier": "<displayed identifier>", "heading": "<heading>", "clause_range": "<range>", "text": "<complete text>"}
  ],
  "framework_layers": {
    "application_perimeter": {"sha256": "<digest>", "sources": ["<verified provisions>"]},
    "applicable_instruments": {"sha256": "<digest>", "sources": ["<regulations and code-register snapshot>"]},
    "guidance": {"sha256": "<digest>", "sources": ["<versioned OAIC pages>"]}
  }
}
```

The source URL must be bound to Privacy Act Title ID `C2004A03712` and identify
the compilation ID or effective-from date. The as-at date must fall in the
effective period. Preserve the resolved final URL, retrieval timestamp and raw
document digest. Reject homepage redirects or unrelated Register titles.

`coverage.complete`, the extraction method and supplied digests remain
self-attested. Therefore `validate` returns only `INVENTORY SCHEMA VALID`.

## Comparison and stop rules

Compare normalized full APP text, ordering, the application-perimeter digest,
the instruments digest and guidance digest. Reject reverse chronology and the
same compilation ID paired with inconsistent source or APP content.

- Any APP text, perimeter or instrument change returns `APP FRAMEWORK CHANGE
  DETECTED – LEGAL CONTENT REVIEW REQUIRED`.
- A horizon crossing a mapped future amendment returns `APP TEXT UNCHANGED –
  APPLICATION LAW REVIEW REQUIRED` unless a present statutory change controls.
- A guidance-only change returns `GUIDANCE REFRESH REQUIRED` in the guidance
  layer, not a statutory-framework-change result.
- No script result alone returns `APP FRAMEWORK VERIFIED`.

Only after the official source, effective period, Schedule boundaries and all
fact-triggered layers are independently established may the legal workflow
report `APP FRAMEWORK VERIFIED`, qualified to those sources, facts and dates.
If any layer is missing, use `APP FRAMEWORK NOT VERIFIED – DO NOT RELY`.

The known-future ledger includes the 10 December 2026 automated-decision
amendments and their application to post-commencement decisions even where the
arrangement, information use or acquisition occurred earlier. Invoke
`$assess-automated-decision-transparency` when that entry is relevant.
