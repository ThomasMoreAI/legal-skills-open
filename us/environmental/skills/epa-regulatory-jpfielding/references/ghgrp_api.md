# EPA Greenhouse Gas Reporting Program (GHGRP) — Envirofacts API Reference

## Base URL

```
https://data.epa.gov/efservice/
```

No API key required. No authentication. Public access.

---

## URL Pattern

The Envirofacts REST API uses a path-based query syntax:

```
https://data.epa.gov/efservice/{TABLE}/{COLUMN}/{OPERATOR}/{VALUE}/.../{OUTPUT}
```

**Components:**

| Component | Description | Example |
|-----------|-------------|---------|
| `TABLE` | View/table name | `V_GHG_EMITTER_SUBPART` |
| `COLUMN` | Column to filter on | `STATE`, `YEAR`, `SUBPART_NAME` |
| `OPERATOR` | Optional comparison | `CONTAINING`, `BEGINNING`, `!=`, `>`, `<` |
| `VALUE` | Filter value | `WV`, `2022`, `W` |
| `rows/M:N` | Row range (0-indexed, inclusive) | `rows/0:99` |
| `count` | Return record count only | `count/JSON` |
| `OUTPUT` | Response format | `JSON`, `CSV`, `XML` |

**Operator notes:**
- Omit operator for exact match: `.../STATE/WV/...`
- `CONTAINING` does substring match: `.../FACILITY_NAME/CONTAINING/EQT/...`
- `BEGINNING` matches prefix
- Numeric comparisons: `>`, `<`, `!=`

Multiple filters are chained in the path:
```
/V_GHG_EMITTER_SUBPART/STATE/WV/SUBPART_NAME/W/YEAR/2022/rows/0:99/JSON
```

---

## Available Tables

### V_GHG_EMITTER_SUBPART (Primary — Use This)

Facility-level emissions broken down by subpart, gas, and year. This is the
most detailed and useful table for GHGRP queries.

**Columns:**

| Column | Type | Description |
|--------|------|-------------|
| `facility_id` | int | Unique GHGRP facility identifier |
| `facility_name` | str | Facility name |
| `address1` | str | Street address line 1 |
| `address2` | str | Street address line 2 (often null) |
| `city` | str | City |
| `state` | str | 2-letter state code (WV, TX, PA...) |
| `state_name` | str | Full state name |
| `zip` | str | ZIP code |
| `county_fips` | str | 5-digit FIPS code |
| `county` | str | County name |
| `latitude` | float | Facility latitude |
| `longitude` | float | Facility longitude |
| `year` | int | Reporting year (2010-present) |
| `subpart_name` | str | Subpart letter code (W, C, UU, PP, Y, MM...) |
| `subpart_category` | str | Subpart description ("Petroleum and Natural Gas Systems") |
| `subpart_type` | str | "E" = emitter, "S" = supplier |
| `co2e_emission` | float | CO2-equivalent emissions (metric tons) |
| `ghg_quantity` | float | Raw GHG mass (metric tons of actual gas) |
| `gas_code` | str | Gas identifier (CO2, CH4, N2O, SF6, HFCs...) |
| `gas_name` | str | Full gas name ("Carbon Dioxide", "Methane"...) |

### V_GHG_EMITTER_GAS

Facility-level emissions aggregated by gas (no subpart breakdown).

**Columns:**

| Column | Type | Description |
|--------|------|-------------|
| `facility_id` | int | GHGRP facility identifier |
| `facility_name` | str | Facility name |
| `address1` | str | Street address |
| `address2` | str | Address line 2 |
| `city` | str | City |
| `state` | str | 2-letter state code |
| `state_name` | str | Full state name |
| `zip` | str | ZIP code |
| `county_fips` | str | FIPS code |
| `county` | str | County name |
| `latitude` | float | Latitude |
| `longitude` | float | Longitude |
| `year` | int | Reporting year |
| `gas_code` | str | Gas code |
| `gas_name` | str | Gas name |
| `co2e_emission` | float | CO2e emissions (metric tons) |

### V_GHG_EMITTER_FACILITIES

**Status: NOT AVAILABLE** at the Envirofacts REST endpoint as of 2025.
Returns "The table is not available" error. Use `V_GHG_EMITTER_SUBPART`
instead and aggregate by `facility_id` if needed.

### V_GHG_EMITTER_SECTOR

**Status: NOT AVAILABLE** at the Envirofacts REST endpoint as of 2025.
Returns "The table is not available" error.

---

## Key Subpart Codes for PNGE

| Subpart | Category | Description | Type |
|---------|----------|-------------|------|
| **W** | Petroleum and Natural Gas Systems | Production, processing, transmission, distribution, storage, LNG import/export, underground NG storage. **Primary subpart for O&G.** | E |
| **C** | Stationary Combustion | General fuel combustion at any facility (boilers, turbines, engines). Broad — appears at nearly every large facility. | E |
| **Y** | Petroleum Refining | Refinery process emissions (catalytic cracking, coking, sulfur recovery, etc.) | E |
| **UU** | Injection of CO2 | Facilities that inject CO2 underground (EOR, carbon storage). Reports quantities injected. | S |
| **PP** | Suppliers of CO2 | Facilities that produce/supply CO2 (capture, purification). | S |
| **MM** | Suppliers of Petroleum Products | Refiners, importers, exporters of petroleum products. Reports upstream supply-side CO2. | S |
| **RR** | Geologic Sequestration of CO2 | Facilities with EPA-approved monitoring plans for CO2 sequestration. | E |

**Subpart type codes:**
- `E` = Direct emitter (emissions from facility operations)
- `S` = Supplier (fuel/gas entering commerce — upstream accounting)

---

## Gas Codes

| Code | Name | GWP (AR5, 100-yr) | Notes |
|------|------|--------------------|-------|
| CO2 | Carbon Dioxide | 1 | Dominant by mass |
| CH4 | Methane | 25 | Key for O&G sector — venting, leaks, flaring |
| N2O | Nitrous Oxide | 298 | Combustion byproduct |
| SF6 | Sulfur Hexafluoride | 22,800 | Electrical equipment |
| HFCs | Hydrofluorocarbons | Varies | Refrigerants |
| PFCs | Perfluorocarbons | Varies | Aluminum, semiconductor |
| NF3 | Nitrogen Trifluoride | 17,200 | Semiconductor |

**Note:** `co2e_emission` is already converted using GWP factors.
`ghg_quantity` is the raw mass of the specific gas in metric tons.

---

## Example Queries

### Subpart W facilities in a state for a year
```bash
curl -s "https://data.epa.gov/efservice/V_GHG_EMITTER_SUBPART/SUBPART_NAME/W/STATE/WV/YEAR/2022/JSON"
```

### Count of Subpart W records nationally for a year
```bash
curl -s "https://data.epa.gov/efservice/V_GHG_EMITTER_SUBPART/SUBPART_NAME/W/YEAR/2022/count/JSON"
# Returns: [{"TOTALQUERYRESULTS": 5782}]
```

### First 20 rows with pagination
```bash
curl -s "https://data.epa.gov/efservice/V_GHG_EMITTER_SUBPART/SUBPART_NAME/W/YEAR/2022/rows/0:19/JSON"
```

### Search by facility name
```bash
curl -s "https://data.epa.gov/efservice/V_GHG_EMITTER_SUBPART/FACILITY_NAME/CONTAINING/EQT/YEAR/2022/JSON"
```

### Search by subpart category text
```bash
curl -s "https://data.epa.gov/efservice/V_GHG_EMITTER_SUBPART/SUBPART_CATEGORY/CONTAINING/Petroleum/STATE/TX/YEAR/2022/rows/0:19/JSON"
```

### Filter by gas type
```bash
curl -s "https://data.epa.gov/efservice/V_GHG_EMITTER_SUBPART/SUBPART_NAME/W/STATE/WV/YEAR/2022/GAS_CODE/CH4/JSON"
```

### Get data as CSV
```bash
curl -s "https://data.epa.gov/efservice/V_GHG_EMITTER_SUBPART/SUBPART_NAME/W/STATE/WV/YEAR/2022/CSV"
```

### Emissions by gas (no subpart breakdown)
```bash
curl -s "https://data.epa.gov/efservice/V_GHG_EMITTER_GAS/STATE/WV/YEAR/2022/rows/0:19/JSON"
```

### Petroleum refineries in Texas
```bash
curl -s "https://data.epa.gov/efservice/V_GHG_EMITTER_SUBPART/SUBPART_NAME/Y/STATE/TX/YEAR/2022/rows/0:19/JSON"
```

---

## Row Limits and Pagination

- Default (no `rows/` specifier): returns all matching records (can be large)
- Use `rows/0:99` for first 100, `rows/100:199` for next 100, etc.
- Row indices are 0-based and inclusive on both ends
- Use `count/JSON` first to determine total, then paginate as needed
- No hard per-request limit, but large result sets (>10,000 rows) are slow

**Pagination pattern:**
```
# Page 1 (rows 0-99)
/V_GHG_EMITTER_SUBPART/SUBPART_NAME/W/YEAR/2022/rows/0:99/JSON
# Page 2 (rows 100-199)
/V_GHG_EMITTER_SUBPART/SUBPART_NAME/W/YEAR/2022/rows/100:199/JSON
```

---

## FLIGHT Tool Reference

The EPA FLIGHT (Facility Level Information on GreenHouse gases Tool) provides
an interactive web map and data download at:

```
https://ghgdata.epa.gov/ghgp/
```

FLIGHT is browser-only (no API). Use it for:
- Interactive map exploration
- Bulk data download (Excel/CSV) with custom filters
- Cross-referencing facility_id values from the API

---

## Data Notes

1. **Reporting threshold:** Only facilities emitting 25,000+ MT CO2e/year are
   required to report. Smaller sources are not in this dataset.
2. **Coverage:** 2010-present (Subpart W data starts 2011 for some segments).
3. **Update cycle:** Annual — data for year N published ~October of year N+1.
4. **Units:** `co2e_emission` in metric tons CO2-equivalent.
   `ghg_quantity` in metric tons of the specific gas.
5. **Subpart W segments:** Within Subpart W, facilities report by industry
   segment (onshore production, offshore production, processing, transmission
   compression, underground NG storage, LNG, distribution). Segment-level
   detail is available in FLIGHT downloads but NOT in the Envirofacts API.
6. **Double counting:** A single facility may report under multiple subparts
   (e.g., Subpart C for combustion AND Subpart W for process emissions).
   Sum across subparts for total facility emissions, but be aware some
   emissions sources may overlap depending on reporting boundaries.
