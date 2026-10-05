---
name: epa-regulatory-jpfielding
title: EPA Regulatory Skill (Envirofacts + ECHO + GHGRP + Subpart W)
description: 'Query U.S. EPA regulatory data across four subsystems in one skill: Envirofacts (TRI, FRS, legacy NPDES), ECHO (CWA/RCRA/SDW/CAA compliance and enforcement), GHGRP facility greenhouse gas emissions, and Subpart W oilfield methane deep-dive. Use whenever the user asks about EPA, Envirofacts, ECHO, UIC, UIC Class II, GHGRP, Subpart W, methane emissions, facility emissions, oilfield methane, compliance history, enforcement, NPDES permits, TRI releases, drinking water systems, hazardous waste, or facility-level environmental data. Triggers on EPA facilities in a state, TRI releases near a town, NPDES permits, drinking water violations, injection well compliance, operator compliance history, GHG emissions from gas plants, methane emissions Appalachian basin, top methane emitters Permian, refinery carbon footprint, EPA FLIGHT, GHGRP facility lookup, venting and flaring, carbon intensity of produced water operations. Produces facility tables, ranked emission tables, gas breakdowns,
  and narrative summaries.'
author: jpfielding
author_url: https://github.com/jpfielding/claude.pnge/tree/main/plugins/pnge-federal-data/skills/epa-regulatory
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: environmental
language: en
sources:
- title: Envirofacts Tables
  path: references/envirofacts_tables.md
- title: Ghgrp Api
  path: references/ghgrp_api.md
---

# EPA Regulatory Skill (Envirofacts + ECHO + GHGRP + Subpart W)

One skill, four subsystems. Route by intent to the correct data source.

| Mode | Use when user wants | Data source |
|------|---------------------|-------------|
| **Envirofacts** | TRI releases, FRS cross-reference, legacy NPDES/PCS | `data.epa.gov/efservice/` |
| **ECHO** | Current compliance, enforcement, SDWA/RCRA/CAA/CWA violations, UIC compliance | `echodata.epa.gov/echo/` |
| **GHGRP** | Facility-level GHG emissions across all subparts (C, W, Y, UU, PP, MM, RR) | `data.epa.gov/efservice/V_GHG_EMITTER_SUBPART` |
| **Subpart W** | Oilfield methane deep-dive (petroleum & natural gas systems) | `data.epa.gov/efservice/V_GHG_EMITTER_SUBPART` filtered to W |

---

## Credential Handling

**No API key is required today.** All four subsystems return data without
authentication. The old build plan referenced an api.data.gov key for
Envirofacts; testing in 2026 confirmed it is not enforced.

**Contingency credential resolution** (if EPA adds key requirements):

1. `~/.config/epa/credentials` — parse `api_key=<value>`
2. `EPA_API_KEY` env var — fallback
3. Prompt user — "EPA may now require an API key. Get one free at
   https://api.data.gov/signup/ — store in `~/.config/epa/credentials` as
   `api_key=YOUR_KEY` (chmod 600)."

Never hardcode or log keys. If activated, pass as `?api_key=<KEY>` query
parameter.

**Reading the credentials file (bash):**
```bash
KEY=$(grep '^api_key=' ~/.config/epa/credentials 2>/dev/null | cut -d= -f2)
[ -z "$KEY" ] && KEY="${EPA_API_KEY}"
```

**Reading the credentials file (Go):**
```go
func resolveAPIKey() (string, error) {
    if home, err := os.UserHomeDir(); err == nil {
        creds := filepath.Join(home, ".config", "epa", "credentials")
        if data, err := os.ReadFile(creds); err == nil {
            for _, line := range strings.Split(string(data), "\n") {
                if strings.HasPrefix(line, "api_key=") {
                    return strings.TrimPrefix(line, "api_key="), nil
                }
            }
        }
    }
    if k := os.Getenv("EPA_API_KEY"); k != "" {
        return k, nil
    }
    return "", fmt.Errorf("no EPA API key found")
}
```

---

## Mode Selection (Intent Routing)

Use this lookup table first. Match the user's question to a mode, then
follow that mode's workflow section.

| User asks about | Mode | Entry point |
|-----------------|------|-------------|
| TRI chemical releases, TRI facilities | Envirofacts | `TRI_FACILITY`, `TRI_REPORTING_FORM` |
| FRS cross-reference across EPA programs | Envirofacts | `FRS_FACILITY_SITE`, `FRS_PROGRAM_FACILITY` |
| Legacy NPDES permits (pre-ICIS) | Envirofacts | `PCS_PERMIT_FACILITY`, `PCS_INSPECTION` |
| **Current NPDES / discharge permits** | **ECHO** | `cwa_rest_services` |
| Drinking water systems, SDWA violations | ECHO | `sdw_rest_services` |
| Hazardous waste (RCRA) handlers | ECHO | `rcra_rest_services` |
| Air (CAA) facility compliance | ECHO | `air_rest_services` |
| **UIC Class II injection wells** | **ECHO or state** | See UIC caveat below |
| Facility compliance / enforcement history | ECHO | program-specific endpoint |
| Environmental justice context | ECHO | EJ fields included in results |
| Facility GHG emissions (any subpart) | GHGRP | `V_GHG_EMITTER_SUBPART` |
| Total facility emissions (no subpart breakdown) | GHGRP | `V_GHG_EMITTER_GAS` |
| Oilfield methane, Subpart W deep-dive | Subpart W | `V_GHG_EMITTER_SUBPART` + `SUBPART_NAME/W` |
| CO2 injection / carbon storage | GHGRP | subparts UU, RR |
| Refinery emissions | GHGRP | subpart Y |

### CRITICAL: UIC Class II wells are NOT on Envirofacts

The `UIC_WELL`, `UIC_VIOLATION`, and `SDWIS_WATER_SYSTEM` tables return
`{"error": "...The table is not available."}` on the current Envirofacts
endpoint. **Do not query them.** Instead:

| Goal | Correct path |
|------|-------------|
| UIC injection well records | State regulator (see below) |
| UIC compliance / enforcement | ECHO SDW (`sdw_rest_services.get_systems`) with UIC program flags, or state UIC data |
| SDWA public water systems | ECHO SDW (`sdw_rest_services`) |

**State UIC programs** for oilfield-relevant Class II:

| State | Program | Skill |
|-------|---------|-------|
| Texas | RRC W-10 / H-10 / H-5 | `pnge-state-regulatory:tx-rrc` |
| New Mexico | OCD injection well DB | `pnge-state-regulatory:nm-ocd` |
| Oklahoma | OCC Form 1015 | `pnge-state-regulatory:ok-occ` |
| North Dakota | NDIC DMR | `pnge-state-regulatory:nd-dmr` |
| Colorado | ECMC injection | `pnge-state-regulatory:co-ecmc` |
| California | CalGEM UIC | `pnge-state-regulatory:calgem` |
| West Virginia | WVDEP OOG | (WVGES wells + DEP) |

Direct users there for UIC well-level data. Use ECHO for compliance flags.

---

## Mode 1: Envirofacts

### API structure

**Base URL:** `https://data.epa.gov/efservice/`

The legacy `enviro.epa.gov/enviro/efservice/` domain now 301-redirects here.
Always use `data.epa.gov`.

**URL pattern:**
```
GET https://data.epa.gov/efservice/{TABLE}/{COL}/{VAL}/.../rows/{S}:{E}/{FMT}
```

| Component | Description | Example |
|-----------|-------------|---------|
| `TABLE` | Table name (case-insensitive, uppercase by convention) | `TRI_FACILITY` |
| `COL/VAL` | Zero or more filter pairs | `STATE_ABBR/WV` |
| `rows/S:E` | Row range (0-based, inclusive) | `rows/0:99` |
| `count/JSON` | Return record count instead | appended instead of rows |
| `FMT` | Response format | `JSON`, `XML`, `CSV` |

**Comparison operators** (between column and value):

| Operator | Keyword | Example |
|----------|---------|---------|
| Equals | *(default)* | `STATE_ABBR/WV` |
| Not equal | `!=` | `FAC_CLOSED_IND/!=/1` |
| Greater than | `>` | `FAC_LATITUDE/>/390000` |
| Less than | `<` | `FAC_LATITUDE/</400000` |
| Starts with | `BEGINNING` | `FACILITY_NAME/BEGINNING/PATRIOT` |
| Contains | `CONTAINING` | `FACILITY_NAME/CONTAINING/COAL` |

### Verified working tables

| Table | Filter Column | Description |
|-------|--------------|-------------|
| `TRI_FACILITY` | `STATE_ABBR` | TRI facility locations and contacts |
| `TRI_REPORTING_FORM` | `STATE_ABBR` | Per-chemical annual TRI reports |
| `TRI_RELEASE_QTY` | *(via doc_ctrl_num)* | Release quantities by medium |
| `FRS_FACILITY_SITE` | `STATE_CODE` | Master facility registry |
| `FRS_PROGRAM_FACILITY` | `STATE_CODE` | Cross-references to all EPA programs |
| `PCS_PERMIT_FACILITY` | `LOCATION_STATE` | Legacy NPDES permits |
| `PCS_INSPECTION` | `LOCATION_STATE` | Legacy NPDES inspections |

### Tables that return 404 on this endpoint

| Table | Use instead |
|-------|-------------|
| `UIC_WELL` | State regulator (see UIC caveat above); ECHO for compliance |
| `UIC_VIOLATION` | ECHO (`sdw_rest_services`) |
| `SDWIS_WATER_SYSTEM` | ECHO (`sdw_rest_services`) |
| `RCRA_FACILITY` | ECHO (`rcra_rest_services`) |
| `CERCLIS_SITE` | ECHO or EPA SEMS |

See `references/envirofacts_tables.md` for complete column listings.

### Workflow

1. Match user intent → choose table
2. Build URL: chain `COL/VAL` pairs, add `rows/0:99`, add `/JSON`
3. `curl -sL <URL>` — response is a flat JSON array
4. Aggregate / format / present

**Example — TRI facilities in Monongalia County, WV:**
```bash
curl -sL "https://data.epa.gov/efservice/TRI_FACILITY/STATE_ABBR/WV/COUNTY_NAME/MONONGALIA/rows/0:50/JSON"
```

**Example — FRS cross-reference for a registry ID:**
```bash
curl -sL "https://data.epa.gov/efservice/FRS_PROGRAM_FACILITY/REGISTRY_ID/110000344896/rows/0:20/JSON"
```

**Example — TRI barium releases in WV:**
```bash
curl -sL "https://data.epa.gov/efservice/TRI_REPORTING_FORM/STATE_ABBR/WV/CAS_CHEM_NAME/CONTAINING/BARIUM/rows/0:20/JSON"
```

### Response shape

Flat JSON array at root — no wrapper, no pagination metadata. Detect more
pages by comparing returned row count against your requested range.

```json
[
  {"tri_facility_id": "26504PTRTM1090C", "facility_name": "PATRIOT MINING...", ...},
  {"tri_facility_id": "26504PTRTM12MIA", "facility_name": "PATRIOT MINING...", ...}
]
```

---

## Mode 2: ECHO

### API structure

**Base URL:** `https://echodata.epa.gov/echo/`

ECHO uses a **two-step query pattern**: search returns a `QueryID`, then
retrieve pages through `get_qid`.

| Program | Search endpoint | Retrieve endpoint |
|---------|-----------------|-------------------|
| CWA (Clean Water Act, NPDES) | `cwa_rest_services.get_facilities` | `cwa_rest_services.get_qid` |
| RCRA (Hazardous Waste) | `rcra_rest_services.get_facilities` | `rcra_rest_services.get_qid` |
| SDW (Drinking Water + UIC) | `sdw_rest_services.get_systems` | `sdw_rest_services.get_qid` |
| CAA (Clean Air Act) | `air_rest_services.get_facilities` | `air_rest_services.get_qid` |

### Common search parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `output` | Format (always `JSON`) | `JSON` |
| `p_st` | State code | `WV` |
| `p_co` | County name (uppercase) | `MONONGALIA` |
| `p_zip` | ZIP code | `26505` |
| `p_sic` | SIC code | `1311` |
| `p_ncs` | NAICS code | `211120` |
| `p_act` | Active status | `Y` |
| `p_maj` | Major facility only | `Y` |
| `p_qiv` | Quarters in violation | `GT1` |
| `p_fn` | Facility name substring | `EQT` |

### Workflow

```bash
# Step 1 — search
RESULT=$(curl -sL "https://echodata.epa.gov/echo/cwa_rest_services.get_facilities?output=JSON&p_st=WV&p_co=MONONGALIA")
QID=$(echo "$RESULT" | jq -r '.Results.QueryID')
TOTAL=$(echo "$RESULT" | jq -r '.Results.QueryRows')
echo "QueryID: $QID, Total: $TOTAL"

# Step 2 — retrieve page 1 (20 records)
curl -sL "https://echodata.epa.gov/echo/cwa_rest_services.get_qid?output=JSON&qid=$QID&pageno=1&pagesize=20"
```

Always:
- Check `.Results.Message` (`Success` or `Working` both indicate valid)
- Check `.Results.Error.ErrorMessage` if present
- Read `.Results.QueryRows` for total count
- Page with `pageno` / `pagesize` on `get_qid`

### Response shape

```json
{
  "Results": {
    "Message": "Working",
    "QueryRows": "2153",
    "QueryID": "357",
    "PageNo": "1",
    "Facilities": [
      {"CWPName": "FACILITY NAME", "SourceID": "WV0045233",
       "PercentPeopleOfColor": "12.4", "FacPopDen": "45.2", ...}
    ]
  }
}
```

### Useful ECHO patterns

**Oil & gas facilities by SIC:**
```bash
# SIC 1311 = Crude Petroleum and Natural Gas
curl -sL "https://echodata.epa.gov/echo/cwa_rest_services.get_facilities?output=JSON&p_st=WV&p_sic=1311"
```

**Drinking water systems in a county:**
```bash
curl -sL "https://echodata.epa.gov/echo/sdw_rest_services.get_systems?output=JSON&p_st=WV&p_co=MONONGALIA&p_pswsid_code_type=community"
```

**Facilities in violation for 4+ quarters:**
```bash
curl -sL "https://echodata.epa.gov/echo/cwa_rest_services.get_facilities?output=JSON&p_st=WV&p_qiv=GT4"
```

### Environmental justice fields (in all ECHO program results)

- `PercentPeopleOfColor` — percent people of color in nearby area
- `FacPopDen` — population density around facility
- `AcsPopulationDensity` — ACS population density
- `PercentLowIncome` — percent low-income households

Use to flag EJ concerns near disposal sites, gas plants, processing
facilities.

---

## Mode 3: GHGRP

### API structure

**Base URL:** `https://data.epa.gov/efservice/`

Same Envirofacts URL pattern as Mode 1. GHGRP uses dedicated views.

**Primary table:** `V_GHG_EMITTER_SUBPART` — facility emissions broken
down by subpart, gas, and year. **This is the correct table** — the old
`PUB_FACTS_SUBPRT_GHG_W` table referenced in pre-consolidation skills
returns 404 and must not be used.

**Secondary table:** `V_GHG_EMITTER_GAS` — facility emissions by gas only
(no subpart breakdown). Good for total facility emissions.

**Tables that are NOT served:**
- `V_GHG_EMITTER_FACILITIES` — 404
- `V_GHG_EMITTER_SECTOR` — 404
- `PUB_FACTS_SUBPRT_GHG_W` — 404 (do not use)
- `PUB_FACTS_FACILITY_GHG_EMITTER` — 404

See `references/ghgrp_api.md` for full column reference and all subpart codes.

### Key columns (V_GHG_EMITTER_SUBPART)

| Column | Description |
|--------|-------------|
| `facility_id` | Unique GHGRP facility ID |
| `facility_name` | Facility name |
| `state`, `state_name` | State code and full name |
| `county`, `county_fips` | County name, 5-digit FIPS |
| `latitude`, `longitude` | Facility coordinates (decimal degrees) |
| `year` | Reporting year |
| `subpart_name` | Subpart letter (W, C, Y, UU, PP, MM, RR) |
| `subpart_category` | Subpart description |
| `subpart_type` | `E` = emitter, `S` = supplier |
| `co2e_emission` | CO2-equivalent metric tons (GWP-weighted) |
| `ghg_quantity` | Raw mass in metric tons of the specific gas |
| `gas_code`, `gas_name` | Gas identifier and full name |

**Use `co2e_emission`** for ranking and totals. **Use `ghg_quantity`** for
gas-composition analysis (e.g., tons of methane leaked).

Each facility appears as multiple rows (one per gas per subpart).
Aggregate by `facility_id` before ranking.

### Key subparts

| Subpart | Category | Use |
|---------|----------|-----|
| **W** | Petroleum and Natural Gas Systems | Primary for O&G — production, gathering/boosting, processing, transmission, distribution, storage, LNG |
| **C** | Stationary Combustion | Boilers, turbines, engines at any large facility |
| **Y** | Petroleum Refining | Refinery process emissions |
| **UU** | Injection of CO2 | EOR and carbon storage injection volumes (supplier) |
| **PP** | Suppliers of CO2 | CO2 capture/supply (supplier) |
| **MM** | Suppliers of Petroleum Products | Upstream supply accounting (supplier) |
| **RR** | Geologic Sequestration of CO2 | EPA-approved CO2 sequestration (emitter) |

### Workflow

1. Check count first for large queries: `.../count/JSON`
2. Default to most recent complete year (current year minus 2 is safe)
3. Fetch with appropriate subpart, state, year filters
4. Aggregate by `facility_id`
5. Rank by total `co2e_emission`
6. Present table + gas breakdown

**Get count first:**
```bash
curl -s "https://data.epa.gov/efservice/V_GHG_EMITTER_SUBPART/SUBPART_NAME/W/YEAR/2022/count/JSON"
# Returns: [{"TOTALQUERYRESULTS": 5782}]
```

**Subpart W in WV, 2022:**
```bash
curl -s "https://data.epa.gov/efservice/V_GHG_EMITTER_SUBPART/SUBPART_NAME/W/STATE/WV/YEAR/2022/JSON"
```

**Methane only, specific state:**
```bash
curl -s "https://data.epa.gov/efservice/V_GHG_EMITTER_SUBPART/SUBPART_NAME/W/STATE/PA/YEAR/2022/GAS_CODE/CH4/rows/0:99/JSON"
```

**Search by operator substring:**
```bash
curl -s "https://data.epa.gov/efservice/V_GHG_EMITTER_SUBPART/FACILITY_NAME/CONTAINING/EQT/SUBPART_NAME/W/YEAR/2022/JSON"
```

**Aggregation (bash + jq):**
```bash
curl -s "URL" | jq '[group_by(.facility_name)[] |
  {facility: .[0].facility_name, state: .[0].state,
   total_co2e: ([.[].co2e_emission] | add)}] |
  sort_by(-.total_co2e) | .[:10]'
```

---

## Mode 4: Subpart W Deep-Dive

Subpart W is a GHGRP subset — use `V_GHG_EMITTER_SUBPART` with
`SUBPART_NAME/W`. This mode adds industry context and segment-level
interpretation.

### Subpart W industry segments (40 CFR Part 98 Subpart W)

| Segment | Key equipment sources |
|---------|----------------------|
| Production | Pneumatic controllers, wellhead, completions, workovers, storage tanks |
| Gathering and Boosting | Compressors, separators, dehydrators, pneumatics, pipeline leaks |
| Processing | Compressors, dehydrators, acid gas removal, flaring |
| Transmission Pipelines | Compressors, metering stations, pipeline blowdowns |
| Distribution | City gate stations, distribution mains, service connections |
| Underground Storage | Compressors, well venting, flaring |
| LNG Storage | Liquefaction equipment, vaporizers |

**Largest Subpart W source nationally:** pneumatic devices (~35-40% of
reported CH4), followed by gathering compressors and storage tanks.

**NOTE on segment-level detail:** The Envirofacts API returns
subpart-level totals. Segment-level breakdowns (production vs
transmission compression within Subpart W) are **only available via the
EPA FLIGHT bulk download** at https://ghgdata.epa.gov/ghgp/ — not this
API. If the user needs segment-level detail, direct them to FLIGHT.

### CH4 GWP reference

Envirofacts reports in mtCO2e. To convert to physical mass:

```
CH4 mass (t) = CH4 (tCO2e) / GWP
```

| GWP basis | CH4 GWP | Context |
|-----------|---------|---------|
| AR4 100-yr | 25 | **EPA GHGRP regulatory basis** |
| AR5 100-yr | 28 | IPCC AR5 |
| AR6 100-yr | 27.9 | IPCC AR6 |
| AR4 20-yr | 72 | Short-term impact |
| AR6 20-yr | 81.2 | Short-term impact |

Example: 100,000 tCO2e CH4 at AR4 = 4,000 tonnes CH4.

### National Subpart W benchmarks

| Metric | Value | Notes |
|--------|-------|-------|
| Total U.S. GHGRP Subpart W | ~175 MtCO2e/yr | ~2022 reported |
| Subpart W share of U.S. GHG | ~2.5-3.5% | EPA GHG Inventory |
| Production segment share | ~35-40% of Subpart W | EPA analysis |
| Gathering & Boosting share | ~30-35% of Subpart W | EPA analysis |
| GHGRP reporting threshold | 25,000 tCO2e/yr | 1,000 t CH4/yr at GWP 25 |
| Appalachian states (WV+PA+OH) | ~12-20 MtCO2e/yr combined | Marcellus/Utica |

### Subpart W workflow

Standard GHGRP workflow (Mode 3) with `SUBPART_NAME/W` locked in. Add
these aggregation steps:

**Aggregate CH4 by facility:**
```bash
curl -s "https://data.epa.gov/efservice/V_GHG_EMITTER_SUBPART/SUBPART_NAME/W/STATE/WV/YEAR/2022/GAS_CODE/CH4/rows/0:499/JSON" | jq '
  group_by(.facility_id) |
  map({
    facility: .[0].facility_name,
    county: .[0].county,
    total_ch4_co2e: (map(.co2e_emission | tonumber) | add)
  }) |
  sort_by(-.total_ch4_co2e) | .[:15]
'
```

**Year-over-year trend (merge per-year requests):**
```bash
for YEAR in 2018 2019 2020 2021 2022; do
  curl -s "https://data.epa.gov/efservice/V_GHG_EMITTER_SUBPART/SUBPART_NAME/W/STATE/WV/YEAR/${YEAR}/JSON"
done
```

The API does not accept year ranges in one call — issue one request per
year and merge client-side.

---

## Output Format

Match the house style: markdown table + narrative summary. Cap tables at
~20 rows. Always include units, year, and data caveats.

### Envirofacts / ECHO example

```
## TRI Facilities — Monongalia County, WV

| Facility | TRI ID | City | Status | Parent |
|----------|--------|------|--------|--------|
| PATRIOT MINING CO INC OSAGE MINE | 26504PTRTM1090C | Star City | Active | ANKER GROUP |
| ... | ... | ... | ... | ... |

**Summary:** 4 TRI-reporting facilities in Monongalia County (EPA Region
03). Two coal mines (PATRIOT MINING) report zinc and other releases.
Cross-reference via FRS for CWA/RCRA status.

**Caveats:** TRI data is industry self-reported annually; release
quantities may be estimated (E), measured (M), or calculated (C).
Reporting thresholds apply — sub-threshold releases do not appear.
```

### GHGRP / Subpart W example

```
## Subpart W Emissions — West Virginia (2022)

### Top facilities by total CO2e

| Rank | Facility | County | Total CO2e (MT) |
|------|----------|--------|-----------------|
| 1 | DTM Appalachia Gathering, LLC | Doddridge | 183,921.6 |
| 2 | HG Energy II Appalachia, LLC | Ritchie | 172,815.1 |
| ... | ... | ... | ... |

### Gas breakdown (all WV Subpart W)

| Gas | CO2e (MT) | % of total |
|-----|-----------|------------|
| Carbon Dioxide | 601,604.8 | 53.7% |
| Methane | 518,635.5 | 46.3% |
| Nitrous Oxide | 593.0 | <0.1% |

**Summary:** WV Subpart W facilities reported 1,120,833 MT CO2e in 2022
across 43 facilities. Methane accounts for 46% of CO2e despite being a
small fraction by mass (AR4 GWP=25). Top 3 facilities account for 43%
of state total. Gathering/processing dominates, consistent with WV's
role in Marcellus/Utica production.

**Units:** metric tons CO2-equivalent (MT CO2e), AR4 GWP basis.
**Reporting threshold:** 25,000 MT CO2e/yr facility-wide.
**Data vintage:** 2022 final.
```

---

## Pagination

### Envirofacts / GHGRP

```python
all_rows = []
start = 0
page = 500
while True:
    rows = fetch(table, filters, start, start + page - 1)
    all_rows.extend(rows)
    if len(rows) < page:
        break
    start += page
```

Warn user if total > 5,000 rows; suggest narrowing by state, year, SIC,
or subpart.

### ECHO

`pageno` and `pagesize` on `get_qid`:

```python
page = 1
while page * pagesize <= total:
    records = echo_retrieve(program, qid, pageno=page, pagesize=20)
    page += 1
```

---

## Error Handling

| Condition | Meaning | Action |
|-----------|---------|--------|
| HTTP 404 + `"...table is not available"` | Envirofacts view retired (e.g., UIC_WELL, PUB_FACTS_SUBPRT_GHG_W) | Use the correct alternative; see tables above |
| Envirofacts returns `[]` | No matching rows | Broaden filters; check column/value spelling |
| HTTP 404 with no JSON body | Bad URL path | Check table name, column spelling, operator placement |
| HTTP 500 from ECHO | Invalid parameter combination | Re-check parameter names against docs |
| ECHO `Error.ErrorMessage` present | Query rejected | Read message, fix params, retry |
| ECHO `QueryRows: "0"` | No matching facilities | Broaden p_st, drop p_co, check p_sic |
| GHGRP `GHG_QUANTITY` comes as string | Envirofacts returns all values as strings | Cast `.ghg_quantity \| tonumber` in jq |
| Result set > 5,000 | Performance concern | Add geographic/temporal filter |
| Old data only (API lags 1-2 years) | Normal | Note latest available year; GHGRP for year N releases ~October N+1 |

---

## Cross-Reference Strategy

EPA maintains facility IDs across programs. **FRS Registry ID** is the
master cross-reference key:

```
FRS Registry ID (e.g., 110000344896)
  |-- TRI:   tri_facility_id  (via epa_registry_id in TRI_FACILITY)
  |-- NPDES: permit ID         (via FRS_PROGRAM_FACILITY, pgm_sys_acrnm=ICIS)
  |-- RCRA:  handler ID        (via FRS_PROGRAM_FACILITY, pgm_sys_acrnm=RCRAINFO)
  |-- SDWA:  PWS ID            (via FRS_PROGRAM_FACILITY, pgm_sys_acrnm=SDWIS)
  |-- ECHO:  DfrUrl            (uses registry_id as fid parameter)
  |-- GHGRP: facility_id       (match by name+location; no direct key)
```

**Link a facility across programs:**
1. Find facility in any table → get its FRS Registry ID
2. Query `FRS_PROGRAM_FACILITY` with that ID
3. Use returned program IDs to query specific tables or ECHO endpoints

---

## EPA Region Reference

| Region | States |
|--------|--------|
| 03 | WV, PA, VA, DC, DE, MD |
| 04 | KY, TN, NC, SC, GA, AL, MS, FL |
| 05 | OH, MI, IN, IL, WI, MN |
| 06 | TX, NM, OK, LA, AR |
| 08 | CO, UT, WY, MT, ND, SD |

---

## SIC / NAICS Codes for PNGE Research

| SIC | NAICS | Description |
|-----|-------|-------------|
| 1311 | 211120 / 211130 | Crude Petroleum / Natural Gas |
| 1321 | 211112 | Natural Gas Liquids |
| 1381 | 213111 | Drilling Oil and Gas Wells |
| 1382 | 213112 | Oil and Gas Field Services |
| 1389 | 213112 | Services Allied to O&G Extraction |
| 2819 | 325180 | Industrial Inorganic Chemicals (Li compounds) |
| 4923 | 486210 | Natural Gas Transmission and Distribution |
| 2911 | 324110 | Petroleum Refining |

---

## PNGE Research Context

### Carbon intensity of produced water operations

Subpart W covers produced-water-adjacent emissions: separators, tanks,
pneumatics, flares at well sites. For produced water Li/Mg recovery TEA:

1. Query Subpart W for target basin to set a baseline facility-level
   O&G emissions benchmark
2. Compare against proposed DLE energy inputs
3. Remember: co-producing Li/Mg from existing brine handling may add
   minimal incremental emissions vs standalone hard-rock mining

### Methane as the key concern

In Subpart W, methane typically accounts for 40-60% of CO2e despite
being a small mass fraction (AR4 GWP=25). Key sources:

- Pneumatic controllers and pumps
- Equipment leaks (fugitive)
- Associated gas venting and flaring
- Liquids unloading
- Gathering and boosting compressor stations
- Produced water tanks (flash emissions)

### Cross-skill patterns

- `pnge-core:usgs-produced-waters` — match GHGRP facility locations with
  produced water chemistry (Li/Mg vs emissions profile)
- `pnge-state-regulatory:wvges-wells`, `pnge-state-regulatory:tx-rrc`, `pnge-state-regulatory:co-ecmc`, `pnge-state-regulatory:ok-occ`,
  `pnge-state-regulatory:nm-ocd`, `pnge-state-regulatory:nd-dmr`, `pnge-state-regulatory:calgem` — link GHGRP facilities
  to state well records by operator + county
- `pnge-federal-data:fracfocus` — cross-reference GHGRP reporters with HF chemical
  disclosures
- `pnge-core:eia-data` — compare GHGRP emissions against EIA production
  volumes for emissions intensity (MT CO2e per barrel or per Mcf)
- `pnge-federal-data:ejscreen-cejst-svi` — overlay ECHO EJ fields with EJScreen

---

## Caveats and Data Limitations

### Across all modes

- **Self-reported:** Envirofacts TRI, GHGRP, and most ECHO program data
  are submitted by regulated entities. EPA verifies but errors and
  underreporting occur.
- **Publication lag:** TRI ~18 months, GHGRP ~9-15 months, ECHO ~1
  quarter. As of April 2026, most recent complete GHGRP year is 2024
  (released ~Oct 2025); 2025 data expected Oct 2026.
- **Data currency:** Envirofacts and ECHO refresh asynchronously; FRS
  is the most current cross-reference index.

### Envirofacts specific

- `fac_latitude` / `fac_longitude` are DDMMSS integer format (e.g.,
  393800 = 39d 38m 00s). Use `pref_latitude` / `pref_longitude` (decimal
  degrees) when available.
- PCS tables are legacy — replaced by ICIS-NPDES. Use ECHO CWA for
  current data.
- `UIC_WELL`, `UIC_VIOLATION`, `SDWIS_WATER_SYSTEM`, `RCRA_FACILITY`,
  `CERCLIS_SITE` return 404 — use ECHO or state sources.

### ECHO specific

- Compliance data updates quarterly; new violations may not appear for
  up to 90 days.
- Major/minor facility distinction (`p_maj`) is an EPA classification;
  small facilities may be under-represented in "major" queries.

### GHGRP / Subpart W specific

- **Reporting threshold 25,000 MT CO2e/yr facility-wide.** Thousands of
  small O&G facilities are not in the dataset.
- **Engineering calculations, not measurement.** Subpart W allows
  emission factors + throughput rather than direct measurement.
  Independent atmospheric studies suggest actual emissions are 1.5-3x
  higher for some equipment categories.
- **GWP basis:** EPA uses AR4 (CH4=25). State and corporate inventories
  may use AR5 or AR6. Be explicit about which GWP is used when
  comparing values.
- **Segment-level detail NOT in API.** Use FLIGHT bulk downloads.
- **Double counting risk:** Facilities may report under multiple
  subparts (e.g., C combustion + W process). Sum across subparts
  carefully.
- **Supplier vs. emitter:** subparts UU, PP, MM are type `S` — they
  report quantities entering commerce, not direct atmospheric emissions.
  Do not add supplier and emitter subpart totals for facility emissions.
- **2024 EPA methane rule (40 CFR Part 98 revisions, effective 2025):**
  Expands monitoring and revises emission factors. Reported 2025+
  values may show step-change increases reflecting methodology change
  rather than real emission increases.
- **Offshore:** Subpart W covers OCS platforms but they report
  differently. Use `pnge-federal-data:boem-offshore` for offshore production context.

---

## Implementation Notes

- Prefer `bash` with `curl -sL` + `jq` for all modes
- Go client examples in `references/go_example.go`
- Python stdlib client in `references/python_example.py` — covers
  Envirofacts, ECHO, and GHGRP
- Response types:
  - Envirofacts / GHGRP: flat JSON array at root
  - ECHO: nested JSON with `.Results` wrapper + `.Error` check
- `co2e_emission` and `ghg_quantity` in GHGRP responses come as numeric
  but may round-trip as strings; always `tonumber` in jq
- Cap output tables at 20 rows for readability; note total count
- Always state units (MT CO2e, lbs, count) and data year
- Note when a query returns facility-wide vs subpart-specific results
