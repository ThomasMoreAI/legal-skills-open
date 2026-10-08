# Universal Pre-flight Steps

Run these BEFORE any section. Outputs are cached and shared across sections.

## 1. Geocode the address

Use Nominatim (works worldwide):

```bash
# Geocode the address — Nominatim, one result, addressdetails on
curl -sL "https://nominatim.openstreetmap.org/search.php?q=<URL-encoded-address>&format=json&addressdetails=1&extratags=1" \
  -H "User-Agent: Claude/1.0"
```

Extract:
- `lat`, `lon`
- `address.country_code` (canonical country signal)
- `address.postcode`
- Country-specific admin units:
  - **FR**: `address.village` / `municipality`, `address.county` (= département)
  - **DE**: `address.city` / `village`, `address.state` (Bundesland)
  - **UK**: `address.city`, `address.state` (England/Scotland/Wales/NI)
  - **IT**: `address.city`, `address.state` (regione), `address.county` (provincia)
  - **ES**: `address.city`, `address.state` (CCAA), `address.county` (provincia)
  - **NL**: `address.city`, `address.state` (province)
  - etc.
- The OSM `osm_id` if returned for a `way` (the road)

If the result is `osm_type=way` and the address has a street, capture `osm_id` for road queries.

## 2. Identify the road (if street address)

Query OSM Overpass for road tags:

```bash
# Query Overpass for amenities within the radius
curl -s -X POST "https://overpass-api.de/api/interpreter" \
  --data-urlencode "data=[out:json][timeout:25];way(<osm_id>);out tags;" \
  -H "User-Agent: Claude/1.0"
```

Capture:
- `tags.ref` — official road designation (e.g., `D 112` in FR, `B 96` in DE, `A1` in UK)
- `tags.highway` — OSM class (motorway / trunk / primary / secondary / tertiary / unclassified / residential)
- `tags.maxspeed` — speed limit in km/h or "mph"
- `tags.name` — street name

The `highway` class is a coarse traffic proxy when official counts are unavailable:
- motorway / trunk = very high
- primary = high
- secondary = moderate
- tertiary = low
- residential / unclassified = very low

## 3. Fetch the listing (if URL given)

Universal extraction prompt for any platform (SAFTI, SeLoger, Rightmove, ImmoScout24, Idealista, Funda, Sreality, Otodom, Zillow, Realtor.com, etc.):

> Extract from this property listing:
> - Asking price (and breakdown if shown: net seller / agency fee / VAT / transfer tax)
> - Surface area (living m² / sq ft, plus any breakdown like Carrez / Wohnfläche / build vs lot)
> - Land/lot size
> - Year built (or year of last renovation if shown)
> - Number of rooms / bedrooms / bathrooms
> - Energy rating / EPC / DPE (letter + kWh/m²/yr if shown)
> - Estimated annual energy cost
> - Heating type (fuel + system)
> - Condition (move-in / needs cosmetic / needs full renovation)
> - Sewer/drainage type if mentioned (mains / septic / "tout-à-l'égout" / Klärgrube / cesspit)
> - Pool, garage, basement, attic, outbuildings
> - Full description text
> - Agent contact details
> - Listing reference number and date listed if shown

Cache all extracted fields — multiple sections reference them.

## 4. Cache local admin facts

For the resolved locality, look up:
- Population (latest census)
- Population trend (% change since 2000, 2010, 2020)
- 3 nearest larger localities + distance
- Sub-prefecture / county seat / district capital
- Communauté de communes / Landkreis / district / county / province name
- Mayor / district authority contact (for verification path)

Source per country:
- **FR**: INSEE statistics, commune-mairie.fr, mairie phone in DICRIM
- **DE**: Destatis, Bürgeramt site
- **UK**: ONS, council site
- **IT**: ISTAT, comune site
- **ES**: INE, ayuntamiento site
- **NL**: CBS, gemeente site

## 5. Detect special zones

Run quick checks for special-status zones (each country playbook may extend):

| Zone type | Typical sources |
|---|---|
| Heritage / conservation area | UNESCO, country-specific monuments inventory |
| Coastal protection / floodplain | Country-level flood maps |
| Agricultural protection (ZAP / Ag-zone) | Country/regional cadastre |
| Mining/quarry concession | Country-level minerals/mining authority |
| Nuclear / Seveso PPI/zonage | Country-specific operator + government |
| National park / Natura 2000 | EU EEA Natura 2000 viewer + country park sites |
| Tourist tense zone (rental surcharge) | Country-specific (FR: zone tendue list) |

Cache any hits — they're inputs to risks, tax, rental sections.

## Output of pre-flight

Pre-flight produces a `context` object (mental model for the agent):

```yaml
# Resolved preflight output, ready for the section skills
country_iso2: fr
admin:
  commune: Adriers
  postcode: "86430"
  insee_or_equivalent: "86001"
  county_or_dept: Vienne
  region: Nouvelle-Aquitaine
geo:
  lat: 46.2582
  lon: 0.8040
  road:
    name: Rue Principale
    ref: D 112
    highway: secondary
    maxspeed: null
listing:
  url: https://...
  price_fai: 145000
  surface_m2: 234
  land_m2: 7642
  year_built: 1975
  dpe: E
  ...
local_facts:
  population: 701
  population_trend_since_2006: -6%
  nearest_subprefecture: Montmorillon
  ...
special_zones:
  nuclear_ppi: outside (25 km from Civaux)
  ...
```

This context is invisible to the user (don't print it unless asked); section playbooks consume it.

## Country detection cascade

If the user didn't pass `--country=<iso2>`:

1. Look for country name word in the address: `France`, `Frankreich`, `Francia` → `fr`; `Germany`, `Deutschland`, `DE` → `de`; etc.
2. Postcode pattern:
   - `^\d{5}$` and contains French commune/dept name → `fr`
   - `^\d{5}$` and contains German city → `de`
   - `^\d{5}$` and contains Italian city → `it`
   - `^\d{5}$` and contains Spanish city → `es`
   - `^[A-Z]{1,2}\d[A-Z\d]?\s?\d[A-Z]{2}$` → `uk`/`gb`
   - `^\d{4}\s?[A-Z]{2}$` → `nl`
   - `^\d{4}$` could be → `be` / `ch` / `at` / `dk` (need country name or other signal)
   - `^\d{4}-\d{3}$` → `pt`
   - `^\d{2}-\d{3}$` → `pl`
   - `^\d{3}\s?\d{2}$` → `cz`
3. Reverse-geocode lat/lon via Nominatim, take `address.country_code` (most reliable when an address resolves)
4. If still ambiguous, ask the user explicitly: "Which country is this address in? (`--country=<iso2>`)"

## Failure modes

- **Nominatim returns no result**: try with simplified address (drop street number), or accept lat/lon only
- **Nominatim rate-limit / 429**: max 1 req/sec under public-instance fair-use; **must** include `User-Agent: <descriptive>` header (anonymous requests are blocked); on 429 → back off ≥5 s OR fall back to country-official geocoder (FR: [data.geopf.fr geocodage](https://data.geopf.fr/geocodage/search/), DE: [BKG Geokodierungsdienst](https://gdz.bkg.bund.de/), UK: [postcodes.io](https://postcodes.io/), AT: [OEReB](https://www.basemap.at/), etc. — country playbooks list theirs)
- **Overpass timeout / 504**: skip the road query, mark traffic section as "low-confidence" (highway class fallback). Increase `timeout:N` in query body for large radius searches; use `[out:json][timeout:60]`
- **Overpass 406 Not Acceptable**: triggered when query is sent as GET with `?data=...` URL parameter or with wrong content-type. **MUST be POST + `--data-urlencode "data=<query>"` form body** (per the recipes in this file and `shared/amenities-osm.md`); also include `-H "User-Agent: <descriptive>"`. If still 406: try alternate mirror like `https://overpass.private.coffee/api/interpreter` (community-hosted, often more lenient)
- **Overpass response is HTML not JSON**: response is an error page; pre-check with `head -c 100 response.json | grep -c "^{"` before piping to `jq`/`json.load`. Common error pages: `429 Too Many Requests`, `504 Gateway Timeout`, `500 Internal Server Error`. Manual fallback: open `https://www.openstreetmap.org/#map=18/<LAT>/<LON>` in a browser and read the road/POIs visually
- **Listing URL behind login wall**: ask user to paste the listing text directly
- **Country playbook not loaded**: see master SKILL.md "Unsupported country" path

## Defensive curl pattern (recommended)

For any tool-call that consumes Overpass / Nominatim / similar JSON APIs:

```bash
# Send the request, capture status + body separately
HTTP_CODE=$(curl -sL -w "%{http_code}" -o /tmp/resp.json \
  -X POST "https://overpass-api.de/api/interpreter" \
  --data-urlencode "data=[out:json][timeout:30];..." \
  -H "User-Agent: <your-script-name>/1.0")

if [ "$HTTP_CODE" != "200" ]; then
  echo "API returned $HTTP_CODE; dumping first 200 bytes:"
  head -c 200 /tmp/resp.json
  exit 1
fi

# Validate JSON before parsing
head -c 1 /tmp/resp.json | grep -qE '^[\[{]' || {
  echo "Response is not JSON; first 200 bytes:"
  head -c 200 /tmp/resp.json
  exit 1
}

# Now safe to parse
python3 -c "import json; print(json.load(open('/tmp/resp.json')))"
```

This pattern surfaces failures cleanly and avoids opaque `JSONDecodeError` traces.
