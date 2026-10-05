# EPA Envirofacts & ECHO — Table Reference

This document catalogs the tables, columns, and query patterns verified against
the live APIs as of March 2026.

---

## Envirofacts REST API

**Base URL:** `https://data.epa.gov/efservice/`

> The legacy `enviro.epa.gov/enviro/efservice/` domain now 301-redirects to
> `data.epa.gov/efservice/`. Always use the new domain.

### URL Pattern

```
GET https://data.epa.gov/efservice/{TABLE}/{COLUMN}/{VALUE}/rows/{START}:{END}/{FORMAT}
```

- **TABLE**: Table name (case-insensitive in URL but uppercase by convention)
- **COLUMN/VALUE**: Zero or more filter pairs chained in URL path
- **rows/START:END**: Row range (0-based, inclusive)
- **FORMAT**: `JSON`, `XML`, or `CSV`

Multiple filters are concatenated:

```
/TRI_FACILITY/STATE_ABBR/WV/COUNTY_NAME/MONONGALIA/rows/0:10/JSON
```

Comparison operators are placed after the column name:

```
/TRI_FACILITY/STATE_ABBR/WV/rows/0:10/JSON          # equals (default)
/TRI_FACILITY/FAC_LATITUDE/>/390000/rows/0:10/JSON   # greater-than
/TRI_FACILITY/CITY_NAME/BEGINNING/MORGAN/rows/0:10/JSON  # starts-with
/TRI_FACILITY/FACILITY_NAME/CONTAINING/COAL/rows/0:10/JSON  # contains
```

Operator keywords: `=`, `!=`, `>`, `<`, `BEGINNING`, `CONTAINING`

### No API Key Required

The Envirofacts API does **not** require authentication. All tables are publicly
accessible without an API key.

---

### Available Tables (verified working)

#### TRI_FACILITY — Toxic Release Inventory Facilities

Facilities that report under TRI (Section 313 of EPCRA). Filter by `STATE_ABBR`.

| Column | Type | Description |
|--------|------|-------------|
| `tri_facility_id` | string | Unique TRI facility ID (TRIFID) |
| `facility_name` | string | Facility name |
| `street_address` | string | Street address |
| `city_name` | string | City |
| `county_name` | string | County |
| `state_abbr` | string | 2-letter state code |
| `state_county_fips_code` | string | 5-digit FIPS code |
| `zip_code` | string | ZIP code |
| `region` | string | EPA region number (1-10) |
| `fac_closed_ind` | string | 1 = closed, 0 = active |
| `parent_co_name` | string | Parent company name |
| `fac_latitude` | int | Latitude (DDMMSS format, divide for decimal) |
| `fac_longitude` | int | Longitude (DDDMMSS format) |
| `pref_latitude` | float | Preferred latitude (decimal degrees, may be null) |
| `pref_longitude` | float | Preferred longitude (decimal degrees, may be null) |
| `epa_registry_id` | string | FRS registry ID (links to FRS tables) |
| `standardized_parent_company` | string | Standardized parent company name |
| `asgn_public_contact` | string | Public contact person |
| `asgn_public_phone` | string | Public contact phone |
| `asgn_public_contact_email` | string | Public contact email |

**Example:**
```bash
curl -sL "https://data.epa.gov/efservice/TRI_FACILITY/STATE_ABBR/WV/COUNTY_NAME/MONONGALIA/rows/0:10/JSON"
```

#### TRI_REPORTING_FORM — TRI Chemical Reporting Details

Per-chemical annual reporting data for TRI facilities. Links to TRI_FACILITY
via `doc_ctrl_num` structure. Filter by `STATE_ABBR`.

| Column | Type | Description |
|--------|------|-------------|
| `doc_ctrl_num` | string | Document control number (unique per report) |
| `reporting_year` | int | Reporting year |
| `cas_chem_name` | string | CAS chemical name |
| `facility_id` | string | TRI facility ID |
| `form_type_ind` | string | Form type (A = short, R = long) |
| `entire_fac` | int | 1 = entire facility, 0 = partial |
| `max_amount_of_chem` | string | Max amount code (01-10) |
| `production_ratio` | float | Production ratio vs prior year |
| `one_time_release_qty` | float | One-time release quantity (lbs) |
| `certif_name` | string | Certifying official |
| `certif_official_title` | string | Official title |
| `certif_date_signed` | string | Date signed |
| `active_status` | int | 1 = active |
| `public_contact_person` | string | Public contact |
| `public_contact_phone` | string | Contact phone |

**Example:**
```bash
curl -sL "https://data.epa.gov/efservice/TRI_REPORTING_FORM/STATE_ABBR/WV/REPORTING_YEAR/2022/rows/0:5/JSON"
```

#### TRI_RELEASE_QTY — TRI Release Quantities

Release quantities by medium for each TRI report. Links via `doc_ctrl_num`.

| Column | Type | Description |
|--------|------|-------------|
| `doc_ctrl_num` | string | Document control number |
| `environmental_medium` | string | Release medium (AIR FUG, AIR STACK, WATER, LAND TREA, OTH DISP, etc.) |
| `water_sequence_num` | int | Water body sequence (null for non-water) |
| `total_release` | float | Total release quantity (lbs) |
| `release_na` | string | 1 = not applicable |
| `release_basis_est_code` | string | Estimation method (E=estimated, M=measured, C=calculated) |
| `release_range_code` | string | Range code if exact amount not reported |

**Example:**
```bash
curl -sL "https://data.epa.gov/efservice/TRI_RELEASE_QTY/rows/0:5/JSON"
```

#### FRS_FACILITY_SITE — Facility Registry Service

Master facility registry linking all EPA program data. Filter by `STATE_CODE`.

| Column | Type | Description |
|--------|------|-------------|
| `registry_id` | string | Unique FRS registry ID |
| `primary_name` | string | Facility name |
| `location_address` | string | Street address |
| `city_name` | string | City |
| `county_name` | string | County |
| `state_code` | string | 2-letter state code |
| `postal_code` | string | ZIP code |
| `epa_region_code` | string | EPA region (01-10) |
| `site_type_name` | string | Site type (STATIONARY, etc.) |
| `federal_facility_code` | string | Federal facility indicator |
| `tribal_land_code` | string | On tribal land (Y/N) |
| `std_county_fips` | string | 5-digit FIPS code |
| `public_ind` | string | Public record indicator |
| `data_quality_code` | string | Data quality indicator |

**Example:**
```bash
curl -sL "https://data.epa.gov/efservice/FRS_FACILITY_SITE/STATE_CODE/WV/rows/0:10/JSON"
```

#### FRS_PROGRAM_FACILITY — FRS Program Linkages

Links FRS registry IDs to specific EPA program system IDs (ICIS, RCRA, etc.).
Filter by `STATE_CODE`.

| Column | Type | Description |
|--------|------|-------------|
| `registry_id` | string | FRS registry ID |
| `primary_name` | string | Facility name |
| `pgm_sys_acrnm` | string | Program acronym (ICIS, RCRAINFO, SEMS, etc.) |
| `pgm_sys_id` | string | Program-specific ID |
| `state_code` | string | 2-letter state code |
| `county_name` | string | County |
| `city_name` | string | City |
| `location_address` | string | Address |
| `postal_code` | string | ZIP code |
| `source_of_data` | string | Source system |
| `huc_code_8` | string | 8-digit Hydrologic Unit Code |

**Example:**
```bash
curl -sL "https://data.epa.gov/efservice/FRS_PROGRAM_FACILITY/STATE_CODE/WV/PGM_SYS_ACRNM/ICIS/rows/0:10/JSON"
```

#### PCS_PERMIT_FACILITY — NPDES Permit Facilities (Legacy PCS)

NPDES permit holders (Clean Water Act discharge permits). Note: this is the
legacy Permit Compliance System; current data is in ICIS-NPDES via ECHO.

| Column | Type | Description |
|--------|------|-------------|
| `npdes` | string | NPDES permit number |
| `name_1` | string | Facility name line 1 |
| `name_2` | string | Facility name line 2 |
| `major_discharge_indicator` | string | M = major discharger |
| `region` | string | EPA region |
| `county_name` | string | County |
| `sic_code` | string | SIC industry code |
| `location_state` | string | State (filter column) |
| `location_city` | string | City |
| `location_zip_code` | string | ZIP |
| `latitude` | string | Latitude (DDMMSS format) |
| `longitude` | string | Longitude (DDDMMSS format) |
| `permit_issued_date` | string | Permit issue date |
| `permit_expired_date` | string | Permit expiration date |
| `inactive_code` | string | A = active |
| `type_of_ownership` | string | PRI, FED, GOV, MUN, etc. |
| `receiving_waters` | string | Receiving water body name |
| `river_basin` | string | River basin code |
| `industry_class` | string | Industry classification |

**Note:** Filter by `LOCATION_STATE`, not `STATE_CODE`:
```bash
curl -sL "https://data.epa.gov/efservice/PCS_PERMIT_FACILITY/LOCATION_STATE/WV/rows/0:10/JSON"
```

#### PCS_INSPECTION — NPDES Inspections (Legacy PCS)

Inspection records for NPDES permit holders.

```bash
curl -sL "https://data.epa.gov/efservice/PCS_INSPECTION/LOCATION_STATE/WV/rows/0:5/JSON"
```

---

### Unavailable Tables (404 as of March 2026)

These tables were documented in the Envirofacts API but currently return
`404 — The table is not available`:

| Table | Description | Alternative |
|-------|-------------|-------------|
| `UIC_WELL` | Underground Injection Control wells | Use ECHO CWA or state UIC databases |
| `UIC_VIOLATION` | UIC violations | Use ECHO enforcement data |
| `SDWIS_WATER_SYSTEM` | Safe Drinking Water systems | Use ECHO SDW endpoint |
| `SDWA_VIOLATION` | SDWA violations | Use ECHO SDW endpoint |
| `SDWA_PUB_WATER_SYSTEM` | Public water systems | Use ECHO SDW endpoint |
| `RCRA_FACILITY` | RCRA hazardous waste | Use ECHO RCRA endpoint |
| `RCRAINFO_FACILITY_SITE` | RCRA facility details | Use ECHO RCRA endpoint |
| `ICIS_FACILITY` | ICIS permits | Use ECHO CWA endpoint |
| `CERCLIS_SITE` | Superfund sites | Use ECHO or SEMS |

---

## ECHO REST API

**Base URL:** `https://echodata.epa.gov/echo/`

ECHO (Enforcement and Compliance History Online) provides compliance,
inspection, enforcement, and violation data across all EPA programs.

### No API Key Required

ECHO endpoints do not require authentication.

### Two-Step Query Pattern

Most ECHO searches use a two-step process:

1. **Search** — returns a `QueryID` and summary statistics
2. **Retrieve** — use the `QueryID` to fetch actual records page by page

### ECHO Service Families

#### CWA — Clean Water Act (NPDES)

```bash
# Step 1: Search for CWA facilities
curl -sL "https://echodata.epa.gov/echo/cwa_rest_services.get_facilities?output=JSON&p_st=WV&p_co=MONONGALIA"
# Returns: QueryID, QueryRows count, violation/inspection summary

# Step 2: Retrieve facility records
curl -sL "https://echodata.epa.gov/echo/cwa_rest_services.get_qid?output=JSON&qid=QUERY_ID&pageno=1&pagesize=20"
```

**Common CWA search parameters:**

| Parameter | Description | Example |
|-----------|-------------|---------|
| `p_st` | State code | WV |
| `p_co` | County name | MONONGALIA |
| `p_zip` | ZIP code | 26505 |
| `p_sic` | SIC code | 1311 (crude petroleum) |
| `p_fac_ind` | Facility indicator (NPDES, POTW, etc.) | NPDES |
| `p_maj` | Major discharger flag | Y |
| `p_act` | Active status | Y |
| `p_qiv` | Quarters in violation | GT1 |

**CWA facility response fields:**

| Field | Description |
|-------|-------------|
| `CWPName` | Facility name |
| `SourceID` | NPDES permit ID |
| `CWPStreet` | Street address |
| `CWPCity` | City |
| `CWPState` | State |
| `CWPCounty` | County |
| `FacLat` | Latitude (decimal degrees) |
| `CWPPermitStatusDesc` | Permit status (Effective, Expired, Terminated) |
| `PercentPeopleOfColor` | EJ: percent people of color in area |
| `FacPopDen` | Population density around facility |

#### RCRA — Resource Conservation and Recovery Act

```bash
# Search RCRA facilities
curl -sL "https://echodata.epa.gov/echo/rcra_rest_services.get_facilities?output=JSON&p_st=WV&p_co=MONONGALIA"

# Retrieve results
curl -sL "https://echodata.epa.gov/echo/rcra_rest_services.get_qid?output=JSON&qid=QUERY_ID&pageno=1&pagesize=20"
```

**RCRA-specific parameters:**

| Parameter | Description | Example |
|-----------|-------------|---------|
| `p_hwp` | Hazardous waste activity | GEN (generator) |
| `p_lrg` | Large quantity generator | Y |
| `p_rcra_lqg` | LQG status | Y |

#### SDW — Safe Drinking Water Act

```bash
# Search drinking water systems
curl -sL "https://echodata.epa.gov/echo/sdw_rest_services.get_systems?output=JSON&p_st=WV&p_co=MONONGALIA"

# Retrieve system details
curl -sL "https://echodata.epa.gov/echo/sdw_rest_services.get_qid?output=JSON&qid=QUERY_ID&pageno=1&pagesize=20"
```

**SDW-specific parameters:**

| Parameter | Description | Example |
|-----------|-------------|---------|
| `p_pswsid_code_type` | System type | community |
| `p_pswsid_src_code` | Source water type | GW (groundwater) |
| `p_act` | Active status | A |

**SDW system response fields:**

| Field | Description |
|-------|-------------|
| `PWSName` | Water system name |
| `PWSId` | Public Water System ID |
| `PWSTypeDesc` | Type (Community, Transient, etc.) |
| `PrimarySourceDesc` | Water source (Ground water, Surface water, etc.) |
| `PopulationServedCount` | Population served |
| `PWSActivityDesc` | Active/Inactive |
| `SeriousViolator` | Serious violator flag |
| `SDWAContaminantsInViol3yr` | Contaminant rules violated (3 yr) |
| `ViolationCategories` | Violation category descriptions |
| `DfrUrl` | Link to Detailed Facility Report |

#### Air — Clean Air Act

```bash
curl -sL "https://echodata.epa.gov/echo/air_rest_services.get_facilities?output=JSON&p_st=WV&p_co=MONONGALIA"
curl -sL "https://echodata.epa.gov/echo/air_rest_services.get_qid?output=JSON&qid=QUERY_ID&pageno=1&pagesize=20"
```

---

## Cross-Reference Strategy

EPA maintains facility IDs across multiple systems. The **FRS Registry ID** is
the master cross-reference key:

```
FRS Registry ID
  ├── TRI: tri_facility_id  (via epa_registry_id in TRI_FACILITY)
  ├── NPDES: npdes permit ID (via FRS_PROGRAM_FACILITY where pgm_sys_acrnm=ICIS)
  ├── RCRA: EPA handler ID  (via FRS_PROGRAM_FACILITY where pgm_sys_acrnm=RCRAINFO)
  ├── SDWA: PWS ID          (via FRS_PROGRAM_FACILITY where pgm_sys_acrnm=SDWIS)
  └── ECHO: DfrUrl          (uses registry_id as fid parameter)
```

To link data across programs for a single facility:
1. Find the facility in any table (TRI, CWA, RCRA, etc.)
2. Get its FRS Registry ID
3. Query `FRS_PROGRAM_FACILITY` with that registry ID to find all linked program IDs
4. Use those IDs to query specific program tables or ECHO endpoints

---

## EPA Region Reference

| Region | States |
|--------|--------|
| 01 | CT, MA, ME, NH, RI, VT |
| 02 | NJ, NY, PR, VI |
| 03 | DC, DE, MD, PA, VA, **WV** |
| 04 | AL, FL, GA, KY, MS, NC, SC, TN |
| 05 | IL, IN, MI, MN, OH, WI |
| 06 | AR, LA, NM, OK, TX |
| 07 | IA, KS, MO, NE |
| 08 | CO, MT, ND, SD, UT, WY |
| 09 | AZ, CA, GU, HI, NV |
| 10 | AK, ID, OR, WA |

West Virginia is in **EPA Region 03**.

---

## SIC Codes Relevant to PNGE Research

| SIC Code | Description |
|----------|-------------|
| 1311 | Crude Petroleum and Natural Gas |
| 1321 | Natural Gas Liquids |
| 1381 | Drilling Oil and Gas Wells |
| 1382 | Oil and Gas Field Services, NEC |
| 1389 | Services Allied to Oil and Gas Extraction |
| 2819 | Industrial Inorganic Chemicals, NEC (includes Li compounds) |
| 2869 | Industrial Organic Chemicals, NEC |
| 4911 | Electric Services |
| 4923 | Natural Gas Transmission and Distribution |
| 4925 | Mixed, Manufactured, or LP Gas Production/Distribution |
