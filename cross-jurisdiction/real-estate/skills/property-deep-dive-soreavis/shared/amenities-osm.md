# Amenities via OSM Overpass — Universal Section `--amenities`

The `--amenities` section uses **OpenStreetMap Overpass API** for parcel-level distance to essential services. **Works universally across all countries** — no per-country adaptation needed for the technical query.

## What this section provides

For the property's `(lat, lon)` from pre-flight, return distance + walking-time to the nearest of each:

1. **Grocery store** (supermarket / convenience)
2. **DIY / hardware store** (brico, hardware, doityourself)
3. **Pharmacy**
4. **General Practitioner** (doctor)
5. **Hospital**
6. **Schools** (primary + secondary if applicable)
7. **Public transport** (bus stop, train station, metro)

## Universal OSM Overpass query

```bash
# Single query for all amenity types within 5 km radius (Haversine)
curl -s -X POST "https://overpass-api.de/api/interpreter" \
  --data-urlencode "data=
[out:json][timeout:30];
(
  // Grocery
  node[\"shop\"~\"supermarket|convenience|grocery\"](around:5000,<LAT>,<LON>);
  way[\"shop\"~\"supermarket|convenience|grocery\"](around:5000,<LAT>,<LON>);
  // DIY / hardware
  node[\"shop\"~\"hardware|doityourself|trade|garden_centre\"](around:5000,<LAT>,<LON>);
  way[\"shop\"~\"hardware|doityourself|trade|garden_centre\"](around:5000,<LAT>,<LON>);
  // Pharmacy
  node[\"amenity\"=\"pharmacy\"](around:5000,<LAT>,<LON>);
  way[\"amenity\"=\"pharmacy\"](around:5000,<LAT>,<LON>);
  // GP / Doctor
  node[\"amenity\"=\"doctors\"](around:5000,<LAT>,<LON>);
  node[\"healthcare\"~\"doctor|general_practitioner\"](around:5000,<LAT>,<LON>);
  way[\"amenity\"=\"doctors\"](around:5000,<LAT>,<LON>);
  // Hospital
  node[\"amenity\"=\"hospital\"](around:10000,<LAT>,<LON>);
  way[\"amenity\"=\"hospital\"](around:10000,<LAT>,<LON>);
  // Schools
  node[\"amenity\"~\"school|kindergarten\"](around:5000,<LAT>,<LON>);
  way[\"amenity\"~\"school|kindergarten\"](around:5000,<LAT>,<LON>);
  // Public transport
  node[\"highway\"=\"bus_stop\"](around:1000,<LAT>,<LON>);
  node[\"railway\"~\"station|halt|tram_stop\"](around:3000,<LAT>,<LON>);
  node[\"public_transport\"=\"station\"](around:3000,<LAT>,<LON>);
);
out tags geom center 50;
" -H "User-Agent: Claude-property-deep-dive/1.0"
```

Replace `<LAT>` and `<LON>` with the property coordinates from pre-flight.

**Common failures + fallbacks**:

- **406 Not Acceptable**: query was sent as GET with `?data=...` URL parameter or wrong content-type. **MUST be POST + `--data-urlencode "data=<query>"` form body**. Always include `-H "User-Agent: <descriptive>"`.
- **504 Gateway Timeout / 429 Too Many Requests**: public Overpass instance is rate-limited. Mitigation:
  1. Increase `[out:json][timeout:60]` for large-radius queries
  2. Try alternate mirror: `https://overpass.private.coffee/api/interpreter` (community-hosted, often more lenient)
  3. On persistent failure: degrade to manual visual inspection at `https://www.openstreetmap.org/#map=14/<LAT>/<LON>` — OSM map tiles are always available even when Overpass is down
- **Response is HTML, not JSON**: error page from upstream. Pre-check `head -c 1 response.json` is `{` or `[` before parsing. See `shared/preflight.md` § Defensive curl pattern.
- **Empty results in rural areas**: OSM coverage is uneven for rural lieu-dit; cross-check with [Google Maps](https://www.google.com/maps) before reporting "no amenities within X km" — this is a frequent OSM gap, not necessarily reality.

## Tag matrix

| Service | OSM tags to query |
|---|---|
| **Supermarket** | `shop=supermarket`, `shop=convenience`, `shop=grocery`, `shop=greengrocer` (large list) |
| **DIY / brico** | `shop=hardware`, `shop=doityourself`, `shop=trade`, `shop=garden_centre`, `shop=paint`, `shop=tool_hire` |
| **Pharmacy** | `amenity=pharmacy` (universal); `healthcare=pharmacy` newer alternative |
| **GP / Doctor** | `amenity=doctors`, `healthcare=doctor`, `healthcare=general_practitioner`, `healthcare=clinic` |
| **Hospital** | `amenity=hospital`, `healthcare=hospital`, `healthcare=hospital;clinic` |
| **Dentist** (often asked) | `amenity=dentist`, `healthcare=dentist` |
| **Schools** | `amenity=school`, `amenity=kindergarten`, `amenity=college`, `amenity=university` |
| **Public transport** | `highway=bus_stop`, `railway=station`, `railway=halt`, `railway=tram_stop`, `public_transport=station` |
| **Veterinary** | `amenity=veterinary` |
| **Bank / ATM** | `amenity=bank`, `amenity=atm` |
| **Post office** | `amenity=post_office` |

## Distance computation

Haversine distance from property `(lat₀, lon₀)` to each POI `(lat, lon)`:

```python
# Haversine distance from the property to each amenity
import math

def haversine_km(lat1, lon1, lat2, lon2):
    R = 6371  # km
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return 2 * R * math.asin(math.sqrt(a))
```

For each amenity, return the **closest** POI (sort ascending, keep first).

## Walking time estimation

- 5 km/hr walking speed default
- 12 km/hr cycling
- Adjust for terrain: alpine → ÷ 1.3; flat → × 1.0; coastal → × 1.0
- For driving: 25 km/hr urban / 50 km/hr rural / 80 km/hr motorway

```
walk_min = (distance_km / 5) × 60
bike_min = (distance_km / 12) × 60
drive_min = (distance_km / 25) × 60     # urban; adjust
```

## Output template

```markdown
## Local Amenities

**Property coordinates**: <lat>, <lon>

| Service | Closest | Distance | Walk | Drive |
|---|---|---:|---:|---:|
| Supermarket | <name> | <X.X km> | <Y min> | <Z min> |
| Grocery / convenience | <name> | <X.X km> | <Y min> | <Z min> |
| DIY / hardware (brico) | <name> | <X.X km> | <Y min> | <Z min> |
| Pharmacy | <name> | <X.X km> | <Y min> | <Z min> |
| General Practitioner | <name> | <X.X km> | <Y min> | <Z min> |
| Hospital | <name> | <X.X km> | <Y min> | <Z min> |
| Primary school | <name> | <X.X km> | <Y min> | <Z min> |
| Bus stop | <name> | <X.X km> | <Y min> | — |
| Train station | <name> | <X.X km> | <Y min> | <Z min> |

### Verdict
- 🟢 < 1 km / < 12 min walk: convenient
- 🟡 1–3 km / 12–36 min walk: requires transport for bulk shopping
- 🟠 3–10 km: transport-dependent for daily needs
- 🔴 > 10 km: very rural; bulk-shopping trips needed; medical access concerns

**Walkability score**: <X/10>
**Medical access**: 🟢/🟡/🟠/🔴 — <one-line note>
**Convenience verdict**: <urban / suburban / rural / very rural / isolated>

⚠️ **OSM data caveat**: OpenStreetMap is community-maintained; rural areas may be incomplete. **Cross-check the closest result via Google Maps / Apple Maps** before signing.
```

## Confidence calibration

| Confidence | When |
|---|---|
| **HIGH** | Urban location (population > 50k); OSM well-mapped; > 5 amenities found in each category |
| **MEDIUM** | Smaller town; some categories with single-result; possible partial mapping |
| **LOW** | Rural or isolated; OSM mapping likely incomplete; verification recommended |

Rural French/Italian/Spanish villages: OSM may lack newer pharmacies / supermarkets — always note this.

## Special considerations per country

Most countries: standard OSM tags work universally. A few country-specific quirks to know:

| Country | Quirk |
|---|---|
| **FR** | "Pharmacie" widespread; tabacs (`shop=tobacco`) often double as small convenience |
| **IT** | "Tabacchi" sometimes function as mini-marts; check `shop=convenience` + `shop=tobacco` |
| **DE** | "Drogerie" (`shop=chemist` like dm/Rossmann) is NOT a pharmacy — it's a drugstore (no Rx); separate `amenity=pharmacy` for actual pharmacies |
| **CH** | Alpine villages: hospital can be 30+ km; "Spital" (DE) / "Hôpital" (FR) / "Ospedale" (IT) |
| **NO** | "Apotek" = pharmacy; rural areas have "legevakt" (out-of-hours) at variable distances |
| **SE** | "Apotek" = pharmacy; ICA / Coop / Hemköp are major supermarket chains |
| **FI** | "Apteekki" = pharmacy; Prisma / S-Market / K-Citymarket dominate grocery |
| **CZ/SK** | "Lékárna" / "Lekáreň" = pharmacy; Albert / Tesco / Lidl / Kaufland in cities |
| **PL/HU** | OSM well-mapped in cities; rural mapping varies |
| **UK/IE** | "Tesco / Sainsbury / Aldi" supermarkets; "Boots / Lloyds" pharmacy chains; "B&Q / Wickes" DIY |
| **PT** | "Continente / Pingo Doce / Lidl" supermarkets; "Farmácia" widespread |
| **ES** | "Mercadona / Carrefour / Lidl" major; rural pharmacy access regulated by Colegios |

## Failure modes

- **Overpass timeout** (large urban area, broad query): split into multiple smaller queries by amenity type
- **Empty results** (very rural): widen radius to 10 km or 20 km; note "no <type> found within X km" explicitly
- **OSM mapping incomplete**: warn user; suggest manual Google Maps verification
- **Borderline near-coordinate POIs** (right on radius edge): re-query at 1.5× radius to confirm
- **Multiple POIs same name** (chain locations): note which branch (`brand=...`)

## Universal applicability

This section's **technical query is country-agnostic**. The only country-specific layer is:
- Cultural distance expectations (rural Norway vs rural France differ in baseline access)
- Brand-naming conventions (lookup table above)
- Whether "out-of-hours doctor" / "legevakt" / "guardia medica" is included

The Overpass API works in every country with consistent OSM tagging.
