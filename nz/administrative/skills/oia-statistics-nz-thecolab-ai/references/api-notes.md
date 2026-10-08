# OIA statistics data notes

## Primary source

- All-data CSV (preferred): `https://www.publicservice.govt.nz/assets/DirectoryFile/v_OIAStatisticsAllDataResults-1.csv`
- Landing page with period/table links: `https://www.publicservice.govt.nz/data/oia-statistics`
- Official alternative path used in issue text: `https://www.publicservice.govt.nz/guidance/official-information/oia-statistics` (redirects to the landing page above).

## CSV fields used

The CSV contains columns including:

- `OrgID`
- `Agency`
- `Agency_Preffered_Name`
- `Agency_Type`
- `SurveyPeriodEndDate`
- `OIA_RequestsHandled`
- `OIAs_CompletedWithinTimeframe`
- `Percent_OIAs_CompletedWithinTimeframe`
- `OIAs_Published`
- `OIA_extension`
- `Percent_OIA_extension`
- `OIA_transfer`
- `Percent_OIA_transfer`
- `OIA_refused`
- `Percent_OIAs_refused`
- `Ombudsman_Complaints`
- `OIA_average`
- `OIA_median`
- `FinalOpinionsbyOmbudsman`

## Link discovery and derived resources

- The landing page links each release's:
  - period summary PDFs
  - per-period XLSX tables
  - all-data CSV (`/assets/DirectoryFile/v_OIAStatisticsAllDataResults-1.csv`, the same file linked from the page)
- CLI commands use stdlib CSV and, when dates are damaged, ZIP/XML parsing of the dated release workbooks.

## Caveats / limitations

- Hosted pages can intermittently be protected; commands use a browser-like User-Agent and include retry-light failure handling.
- On 8 October 2026, every all-data CSV date was `00:00.0`. The fallback discovers the published half-year XLSX releases; annual 2015/16 and 2016/17 tables cannot establish the CSV’s six-month cut dates and are not guessed.
- `tables` exposes the official download URLs. At most 40 dated releases are recovered using four bounded concurrent requests and a 24-hour local cache.
- Published workbooks and the CSV also contain shifted/reused agency IDs. Warnings remain visible, affected records carry `identity_warning`, and exact agency names should be used for them. Counts and reporting periods come from the dated releases. Release records that match no CSV row are kept with `org_id: null`, so period totals equal the workbook sums (checked for all 18 half-year releases on 8 October 2026, e.g. 2018-12-31 = 40,059 and 2021-06-30 = 69,849). Undated CSV rows remain available in agency history. Agency lookups merge null-OrgID release records into a uniquely name-matching OrgID history (`inferred_org_id`). Blank on-time counts stay null and are excluded from on-time aggregates, which report `on_time_coverage`.
- Percent columns in source can appear as either fractions (`0.978`) or percentages (`97.8`); the CLI normalises to percentage values for command output and sorting.
