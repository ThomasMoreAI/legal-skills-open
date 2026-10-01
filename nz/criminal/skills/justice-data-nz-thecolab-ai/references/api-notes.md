# Justice Data NZ API Notes

## Primary source

- Upstream publisher: New Zealand Ministry of Justice
- Data-tables page: `https://www.justice.govt.nz/justice-sector-policy/research-data/justice-statistics/data-tables/`
- Current live source shape: public `.xlsx` workbooks linked from the data-tables page
- Update cadence stated on the MoJ page: calendar-year tables in March and financial-year tables in September

The issue requested CSV/download endpoints. Live discovery during implementation found direct workbook downloads rather than CSV files. The CLI therefore parses `.xlsx` files directly with Python standard-library `zipfile` and `xml.etree.ElementTree`, reading cached cell values from workbook XML.

## Implemented workbook mappings

- `tables`: parses workbook links from the MoJ data-tables page
- `convictions`: uses:
  - `People with finalised charges (including convicted charges)` sheet `4.People convicted by offence`
  - `All finalised charges and convicted charges` sheets `1a.Charges by offence-division` and `3a.Conv charges-offence-div`
- `sentencing`: uses:
  - `People with finalised charges (including convicted charges)` sheet `5a.Convicted by sentence`
  - `All finalised charges and convicted charges` sheet `4.Conv charges by sentence`
- `family-violence`: uses the `Family violence offences` workbook, including all charges, outcome, people charged, people convicted, and sentence sheets
- `youth`: uses either:
  - `Children and young people with charges finalised in any court`
  - `Children and young people with charges finalised in the Youth Court`

## data.govt.nz / CKAN fallback

The data.govt.nz CKAN API is keyless:

```text
https://catalogue.data.govt.nz/api/3/action/package_search
```

MoJ data-table packages exist in CKAN, and the CLI uses `package_search` as a metadata fallback for `tables` if the MoJ page is unavailable. Current CKAN resources for these workbooks point back to the MoJ data-tables page rather than direct current workbook URLs. Several `datastore_search` resources also expose stale or malformed single-column rows from workbook note sheets. For that reason, CKAN is not used for current data values.

## Bot-protection and blocked states

The official MoJ page was reachable during implementation, but issue #137 warned that `justice.govt.nz` can return 403 from some networks. The CLI treats HTTP 403 and 429 as blocked/rate-limited states and reports a clear `upstream_blocked` style message rather than trying to bypass protection.

If the MoJ page is blocked:

- `tables` falls back to CKAN metadata when possible
- data commands fail clearly because current workbook values require direct MoJ workbook downloads
- users should retry from a permitted network or browser-grade/residential context; this skill does not attempt CAPTCHA bypass or authenticated access

## Interpretation notes

- The MoJ workbooks include notes and definitions sheets. Read those before making strong claims from a row.
- Some "people" tables count one person once per year for their most serious finalised or convicted charge, so offence-specific people counts can undercount people with multiple offences.
- Youth tables use rounded counts and special outcome categories under the Oranga Tamariki Act 1989.
- Use `tables --json` to include exact workbook URLs in citations.
