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
- CLI commands use only stdlib parsing of the CSV.

## Caveats / limitations

- Hosted pages can intermittently be protected; commands use a browser-like User-Agent and include retry-light failure handling.
- XLSX parsing is intentionally not implemented in this skill because the repo requires stdlib-only parsing and XLSX dependencies are excluded.
- The CLI still exposes discovered XLSX/CSV/PDF resources from the page in `tables`.
- Percent columns in source can appear as either fractions (`0.978`) or percentages (`97.8`); the CLI normalises to percentage values for command output and sorting.
