# Climate Projections — Universal Section `--climate`

Universal logic for the 10th section: climate change projections specific to the property's coordinates. Works in every country via Copernicus + IPCC AR6 Atlas + national downscaled models (where available).

## Universal contract for `--climate`

For the property's exact location (lat/lon from preflight), return:

1. **Temperature trajectory** (now → 2050 → 2100) per RCP/SSP scenario
2. **Heatwave days/year** (current vs projected) — TX35 / TX40 thresholds
3. **Sea-level rise** at coastal coordinates (where applicable)
4. **Flood risk multiplier** (current → projected)
5. **Drought / water stress index**
6. **Wildfire potential** (vegetation × heat × wind)
7. **Cooling/heating degree-day shift** (impacts insulation choice + HVAC sizing)
8. **Precipitation pattern shift** (winter wetter / summer drier — typical for EU)
9. **Verdict + confidence**

## Output template

```markdown
## Climate & Long-term Resilience

**Coordinates**: <lat>, <lon>
**Climate zone**: <Köppen-Geiger code, e.g., Cfb>
**Coastal**: <yes/no — distance to sea: X km>
**Elevation**: <X m a.s.l.>
**Reference period**: 1981–2010 baseline → 2050 (mid-century) and 2100 (end-century)
**Scenarios**: SSP2-4.5 (moderate) + SSP5-8.5 (worst-case high-emissions)

### Temperature trajectory

| Metric | 1981–2010 | 2050 SSP2-4.5 | 2050 SSP5-8.5 | 2100 SSP5-8.5 |
|---|---:|---:|---:|---:|
| Mean annual temp (°C) | <X> | <+1.5> | <+2.5> | <+4.5> |
| Hot days TX≥30°C / yr | <X> | <X+10> | <X+20> | <X+45> |
| Tropical nights TN≥20°C / yr | <X> | <X+5> | <X+12> | <X+25> |

### Sea-level rise (coastal only)

| Year | RCP4.5 (cm) | RCP8.5 (cm) | High-end (cm) |
|---|---:|---:|---:|
| 2050 | +20 | +25 | +35 |
| 2100 | +50 | +80 | +120 |

**Property elevation buffer**: <elevation - high-end SLR>m

### Drought + water stress

- **SPEI projection** (12-month standardized precipitation-evapotranspiration index): <↑ ↓ →>
- **Aridity index trend**: <wetter / stable / drier>
- **Summer precipitation change**: <%>
- **Groundwater stress**: <category>

### Wildfire potential

- **FWI (Fire Weather Index)** projection: <% increase by 2050>
- **Vegetation type proximity**: <forest / scrub / urban>
- **Historical fires within 10 km**: <count last 20 yrs>

### Heating ↔ cooling shift

- **HDD (heating degree days)** 1981-2010: <X> → 2050: <X-Y>
- **CDD (cooling degree days)** 1981-2010: <X> → 2050: <X+Y>
- **Implication**: HVAC system + insulation strategy

### Verdict

- 🟢 **Resilient** — minimal impact projected, low exposure to acute climate events
- 🟡 **Watch** — moderate warming, some adaptation needed (cooling, insulation)
- 🟠 **Adapt** — meaningful long-term cost or risk (sea-level, fire, drought)
- 🔴 **Avoid or fortify** — high exposure to multiple acute events; insurance + resale risk

### Confidence

<HIGH | MEDIUM | LOW> — <one-sentence justification>

### Sources
- Copernicus Climate Atlas: <link to specific cell>
- IPCC AR6 Interactive Atlas: <link>
- National downscaled model: <country-specific>
- Climate Central Coastal Risk Screening Tool (if coastal): <link>
```

## Universal data sources

### Tier 1: Global, all countries

| Source | URL | What it gives |
|---|---|---|
| **Copernicus Climate Data Store (CDS)** | `https://cds.climate.copernicus.eu/` | ERA5 reanalysis, CMIP6 projections; global, 0.25° grid |
| **Copernicus Climate Atlas** | `https://atlas.climate.copernicus.eu/` | Interactive viewer for CMIP6 projections; per-cell extraction |
| **IPCC AR6 Interactive Atlas** | `https://interactive-atlas.ipcc.ch/` | Regional projections, climate hazard indices, Köppen-Geiger maps |
| **Climate Central Coastal Risk Screening Tool** | `https://coastal.climatecentral.org/` | Sea-level rise + flood projections globally |
| **WorldClim 2.1** | `https://www.worldclim.org/` | High-resolution (1 km) historical + future bioclimatic variables |
| **NASA POWER** | `https://power.larc.nasa.gov/` | Historical solar + meteorology per coordinate |
| **Köppen-Geiger climate classification** | `https://koeppen-geiger.vu-wien.ac.at/` | Climate zone per coord |

### Tier 2: European countries

| Source | URL | What it gives |
|---|---|---|
| **Copernicus C3S European Climate Indicators** | `https://climate.copernicus.eu/` | EU-specific extreme indices |
| **EEA Climate-ADAPT** | `https://climate-adapt.eea.europa.eu/` | Adaptation case studies per country |
| **DRIAS (FR)** | `https://www.drias-climat.fr/` | French downscaled CMIP6 |
| **DKRZ ESGF (DE)** | `https://esgf-data.dkrz.de/` | German climate data |
| **CMCC (IT)** | `https://www.cmcc.it/` | Italian climate projections |

### Tier 3: National downscaled (where available)

- 🇫🇷 DRIAS portal — already in `fr/playbook.md`
- 🇩🇪 KLIWAS, DWD Klimaatlas — already in `de/playbook.md`
- 🇨🇭 NCCS — already in `ch/playbook.md`
- 🇸🇪 SMHI Klimatscenarier — `https://www.smhi.se/klimat/framtidens-klimat/`
- 🇫🇮 Climateguide.fi — `https://www.climateguide.fi/`
- 🇳🇴 Klimaservicesenter — `https://klimaservicesenter.no/`
- 🇩🇰 DMI Klimaatlas — `https://www.dmi.dk/klima/`
- 🇳🇱 KNMI Klimaatscenario's — `https://www.knmi.nl/klimaatscenarios/`

## Forward + near-property-resolution projection layer

The sources above are either **forward but coarse** (Copernicus / IPCC AR6 ~25 km cell + sub-continental regions) or, for the national portals a buyer instinctively reaches for, **near-property but current-hazard-only**. The buyer's real question — *how will the risk at THIS address change over my ownership horizon?* — is answered at near-property resolution by only a handful of sources. Use this layer when the property's flood / coastal / heat exposure is decision-critical; otherwise the regional projections above suffice. **Do not imply parcel-level forward precision where it does not exist.**

### Government — forward + near-property resolution (the buildable core)

| Jurisdiction | Source | Resolution | Forward horizon | Notes |
|---|---|---|---|---|
| 🇬🇧 England | **Check long-term flood risk (NaFRA2)** — `https://check-long-term-flood-risk.service.gov.uk/` | **postcode / area** (NOT individual property) | present + "how climate change might increase the chance of flooding" (2050s, UKCP18 + SLR) | The service's own caveat: it *"does not tell you how likely it is that an individual property will flood"* — treat as area-level, then confirm the specific parcel with a surveyor / Environment Agency detailed-data request. Scotland (SEPA) + Wales (NRW) + NI run separate portals |
| 🇳🇱 Netherlands | **Klimaateffectatlas** — `https://www.klimaateffectatlas.nl/` | ~100 m grid (partial address-level) | 2050 / 2100, KNMI'23 scenarios (heat, pluvial + fluvial flood, drought, subsidence, SLR) | The most genuinely forward + near-address government portal in the corpus; built on the KNMI'23 climate scenarios |

As of May 2026 only **England (postcode)** and the **Netherlands (~100 m grid)** publish a forward, near-property *government* layer. There is no equivalent address-level government forward portal elsewhere in the 121-country corpus — say so rather than implying one.

### Tier-2 (NGO / commercial — label as model-tier, NOT government)

| Source | Coverage | Resolution | Notes |
|---|---|---|---|
| **First Street** (formerly RiskFactor) — `https://firststreet.org/` | US (parcel) | parcel · 30-yr | 30-yr property flood / fire / heat / wind scores. **Commercial model, not government** — MSCI completed its acquisition 3 Aug 2026; riskfactor.com now redirects to firststreet.org behind a terms-of-use gate with a paid tier above the free reports (verify free access before relying on it); Zillow de-emphasised the scores from late 2025 (see the US `--risks` portal-badge note + `regulatory-watch.md`); pull it direct and label model-tier |
| **Climate Central Coastal Risk Screening** — `https://coastal.climatecentral.org/` | global (coastal) | point · SLR only | Forward SLR + coastal-flood waterline by decade / warming scenario; coastal only (also listed in the Tier-1 table above) |
| **Coastal Risk Australia** — `https://coastalrisk.com.au/` | AU (coastal) | address-ish | Forward coastal-inundation to 2100; NGO / commercial, NOT an ABS / government product |

### The honest tail (everywhere else)

For the ~115 other jurisdictions there is **no forward, address-level government portal**. The honest fallback is the regional layer already in this section — **IPCC AR6 Interactive Atlas (sub-continental regions) + Copernicus (~25 km grid)** — which is forward but NOT address-level. State this explicitly.

### ⚠️ Trap — current-hazard portals are NOT forward projections

Several popular national portals look authoritative but show **today's mapped hazard**, not a forward projection. Do not present them as climate-future; they belong under `--risks` (current exposure):

- 🇫🇷 **Géorisques** (`georisques.gouv.fr`) — current PPRN / TRI / zonage (climate change is a policy driver, not a 2050/2100 map)
- 🇺🇸 **FEMA NFHL / FIRM** (`msc.fema.gov`) — current regulatory flood map (static; not forward)
- 🇮🇹 **IdroGEO / ISPRA** (`idrogeo.isprambiente.it`) — current PAI hazard mosaics
- 🇯🇵 **MLIT / GSI Hazard Map Portal** (`disaportal.gsi.go.jp`) — current hazard
- 🇦🇺 **ARR (Australian Rainfall & Runoff)** — an engineering **design guideline**, NOT a public address-level hazard portal

## Compute steps

1. **Geocode** the property (already done in preflight) → (lat, lon, elevation)
2. **Köppen-Geiger lookup**: classify climate zone from baseline (1981-2010)
3. **Distance to coast** via Overpass `natural=coastline` query
4. **Pull projections** for the cell (0.25° = ~28 km × ~22 km in EU latitudes):
   - From Copernicus Climate Atlas: temperature, precipitation, hot days
   - From IPCC AR6: Köppen shifts, regional indices
   - From Climate Central: SLR + flood (if coastal)
5. **National downscaled override**: if country has finer-resolution model (DRIAS, DKRZ, etc.), prefer that over CMIP6 raw
6. **Compute degree-days**: HDD = Σ max(0, 18°C - T_daily_mean); CDD = Σ max(0, T - 22°C)
7. **Wildfire FWI**: pull from EFFIS (EU) or country-specific model

## Verdict bands

| Band | Triggers |
|---|---|
| 🟢 **Resilient** | All risk indices stable or improving; no SLR exposure; low fire risk; insulation sufficient |
| 🟡 **Watch** | +2°C warming projected; cooling load doubles; minor SLR (<20 cm by 2100) |
| 🟠 **Adapt** | +3°C; SLR 20–50 cm by 2100; fire risk up 50%; cooling cost +€500/yr |
| 🔴 **Avoid or fortify** | SLR >50 cm by 2100 with low elevation buffer; fire risk doubles; multiple acute hazards converge |

## Acute-event flags

Surface these as **🔴 RED FLAG** if any apply to the property:

- **Coastal property** with elevation < 5m above current MSL + SLR > 80 cm by 2100
- **Wildland-urban interface** (within 100 m of forest/scrub) in Mediterranean / Alpine fire zone
- **River floodplain** within 100 m, with flood risk multiplier > 2x by 2050
- **Permafrost zone** (high latitude) with thaw projected during ownership horizon
- **Glacial outburst flood (jökulhlaup) zone** (IS, parts of NO)

## Insurance implications

For each climate hazard surface:
- **Currently insurable**: yes/no
- **Premium trend**: stable / rising / unaffordable by 2050
- **Coverage exclusions** likely (e.g., gradual SLR, repeated flooding)
- **National disaster scheme** coverage (e.g., FR Cat-Nat, IS NTÍ, ES Consorcio de Compensación)
- **Insurability-cliff cross-check**: once the hazard zone is established, cross-check insurability via the **[Insurability cliff (flood / peril) carve-out](insurance.md#insurability-cliff-flood--peril--mortgage--resale-knock-on-cross-link---climate)** in `--insurance` — an uninsurable address is unmortgageable, collapsing the buyer pool to cash and impairing resale.

## Caveats to surface in every output

- **Climate models have uncertainty bounds** — surface 5th–95th percentile ranges
- **CMIP6 cell resolution** ~25 km — coarse for microclimate (valley fog, coastal breezes)
- **Adaptation actions** can offset many risks (better insulation, flood barriers, fire-resistant landscaping) — note them
- **Insurance markets adapt** — premium increases may signal risk before hazards materialize
- **Long-horizon claims** (2100) are inherently uncertain — focus on 2050 for purchase-decision-relevant signals
- **National downscaled models override** when available; surface methodology difference
- **Date stamps**: every climate datum gets "as of YYYY based on ARX/CMIPY"

## Confidence labels

- **HIGH**: Multi-model ensemble + national downscaled model agreement + coastal property has Climate Central data + insurance market signal aligns
- **MEDIUM**: CMIP6 only (no national downscaling); 2050 timeframe; one acute hazard
- **LOW**: 2100 timeframe; large model spread; rapidly evolving science (e.g., AMOC collapse risk)

## Forbidden hallucinations

- Never invent specific year of a climate event
- Never claim "X will happen" — climate is probabilistic; use "projected", "X% likelihood", "ensemble mean"
- Never override national model with personal interpretation of CMIP6
- Surface model uncertainty — buyers underestimate it
- Don't extrapolate beyond IPCC scenarios (no "by 2200…")

## Pairs well with

- `--risks` (acute geological hazards complement chronic climate)
- `--insurance` (climate drives premium structure)
- `--energy` (degree-days drive HVAC + insulation choice)
- `--mains` (climate stress on water + sewer systems)
