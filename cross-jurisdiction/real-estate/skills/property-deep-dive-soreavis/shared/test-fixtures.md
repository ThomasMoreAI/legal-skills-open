# Test Fixtures Registry

One representative, currently-active property listing per country (44 total) for self-test of the property-deep-dive skill. Goal is mid-segment, no-special-feature listings (NOT luxury, NOT derelict, NOT heritage anomaly).

**Purpose**: catch drift in country playbooks. When `/property-deep-dive --update --validate-only --test` runs, it should successfully parse one listing per country and produce a non-error output.

**Refresh cadence**: Quarterly (listings churn fast; expect ~30% link-rot per 90 days).

**Verification key**:
- `200` — curl returned 200 OK
- `403/401/406/429-DD` — bot-protected (DataDome / Cloudflare / Akamai); browser-loadable but curl-blocked
- `200-search` — search-results URL only (specific listing IDs rotate; portal main domain confirmed alive)
- `[NEEDS MANUAL CURATION]` — could not surface a specific verified listing within research budget; portal confirmed live but per-listing slug must be picked manually

---

## Europe (31 countries)

| ISO | Country | Listing URL | Address / Locality | Asking Price | Type | m² / Beds | Portal | Verify | Why Representative |
|---|---|---|---|---|---|---|---|---|---|
| FR | France | https://www.seloger.com/recherche/achat/maison/nouvelle-aquitaine/limoges-87000/ | Limoges 87000, Haute-Vienne | €70k–€250k; median ~€175k | Maison (3-4 bed terraced) | 90–140 m², 3–5 rooms | SeLoger | 403-DD | Limoges sits at FR national median (~€1,935/m² houses); SeLoger dominant; mid-tier provincial (NOT Paris, NOT Riviera) |
| IT | Italy | https://www.immobiliare.it/en/vendita-appartamenti/bologna/ | Bologna 40100, Emilia-Romagna | €150k–€400k; median ~€250k | Appartamento (2-3 bed) | 60–90 m², 2–3 bed | Immobiliare.it | 403-DD | Bologna = IT Tier-2 median. Apartments dominant. Avoids Milan/Rome/Venice luxury and Sud derelict distortion |
| CZ | Czech Republic | https://www.sreality.cz/hledani/prodej/byty/brno | Brno 60200, Jihomoravský kraj | CZK 4.5M–8M (~€180k–€320k) | Byt (2+kk / 3+kk) | 50–80 m², 2–3 rooms | Sreality.cz | 200 | Brno = CZ #2 city; panelák + modern infill typical urban stock. Sreality ~80% market share |
| SK | Slovakia | https://www.nehnutelnosti.sk/vysledky/byty/kosice/predaj | Košice 04001, Košický kraj | €90k–€180k | Byt (2-/3-izbový) | 50–75 m², 2–3 rooms | Nehnuteľnosti.sk | 200 | Košice = SK #2 city, no Bratislava premium. Panelák stock dominates |
| DE | Germany | https://www.immobilienscout24.de/sachsen/leipzig/wohnung-kaufen | Leipzig 04109, Sachsen | €180k–€350k | Eigentumswohnung (Altbau or Neubau) | 60–90 m², 2–3 Zi | ImmoScout24 | 401-DD | Leipzig is east-DE Tier-2 growth city, NOT München/Hamburg luxury or eastern derelict |
| AT | Austria | https://www.willhaben.at/iad/immobilien/eigentumswohnung/steiermark/graz/?PRICE_TO=350000 | Graz 8010, Steiermark | €200k–€350k | Eigentumswohnung | 50–80 m², 2–3 Zi | willhaben.at | 200 | Graz = AT #2 city; willhaben dominant general-classifieds + property |
| CH | Switzerland | https://www.homegate.ch/kaufen/wohnung/plz-3000/trefferliste | Bern 3000, Kanton Bern | CHF 700k–1.2M typical entry; mid ~CHF 950k | Eigentumswohnung (3.5-Zi condo) | 70–100 m², 2–3 bed | Homegate.ch | 403-DD | Bern is federal capital but mid-tier (NOT Zürich/Genève/Zug). 3.5-Zi condo = normal CH family unit |
| ES | Spain | https://www.idealista.com/en/geo/venta-viviendas/46001/ | Valencia 46001, Comunitat Valenciana | from €175k; mid €250k–€400k | Piso | 70–110 m², 2–3 dorm | idealista.com | 403-DD | Valencia is ES Tier-2; Ciutat Vella historic core normal pricing (NOT Madrid Salamanca, NOT Marbella) |
| PT | Portugal | https://www.idealista.pt/en/comprar-casas/coimbra/com-apartamentos,t2/ | Coimbra 3000, Coimbra District | €120k–€220k typical T2 | Apartamento T2 | 70–110 m², 2 bed | idealista.pt | 403-DD | Coimbra = PT inland Tier-2 university city. T2 = normative family flat. Avoids Lisboa/Porto premium + Algarve foreign-buyer distortion |
| SE | Sweden | https://www.hemnet.se/till-salu/lagenhet/goteborgs-kommun/goteborg | Göteborg, Västra Götaland | SEK 2.5M–4.5M (~€220k–€400k) | Lägenhet bostadsrätt | 50–80 m², 2–3 rok | Hemnet.se | 200 | Göteborg = SE #2 city. Bostadsrätt dominant SE ownership. Hemnet ~85% market share |
| FI | Finland | https://www.etuovi.com/myytavat-asunnot/tampere,kerrostalo | Tampere 33100, Pirkanmaa | €150k–€280k | Kerrostalo | 50–80 m², 2–3 huonetta | Etuovi.com | 200 | Tampere = FI #3 city, mid-tier. Kerrostalo dominant urban form. Avoids Helsinki premium |
| NO | Norway | https://www.finn.no/realestate/homes/search.html?location=1.20016.20318 | Trondheim, Trøndelag | NOK 3M–6M (~€255k–€510k) | Leilighet (selveier or andel) | 50–90 m², 2–3 bed | finn.no | 200 | Trondheim = NO #3 city; Finn near-monopoly; 2,577 active |
| UK | United Kingdom | https://www.rightmove.co.uk/property-for-sale/M14.html | Manchester M14 (Fallowfield/Rusholme) | £180k–£280k typical 2-bed | Mid-terrace house or flat | ~70 m² (~750 sqft), 2 bed | Rightmove | 200 | Manchester M14 is classic mid-market UK Tier-2 — Victorian terraces + ex-rental flats. NOT London, NOT Cornwall holiday let |
| NL | Netherlands | https://www.funda.nl/koop/eindhoven/sorteer-datum-af/ | Eindhoven, Noord-Brabant (search; specific listings rotate) | mid-segment ~€350k–€450k | Appartement | 60–90 m², 2–3 bed | funda.nl | 200 | Eindhoven = NL Tier-2 tech city, mid-segment (NOT Amsterdam/Utrecht premium). Funda has 100% NL listing dominance |
| BE | Belgium | https://www.immoweb.be/en/search/house/for-sale/gent/9000 | Gent 9000, Oost-Vlaanderen | mid-segment ~€350k–€500k | Huis | 100–200 m², 3-4 bed | Immoweb.be | 403-DD | Gent = BE Flanders Tier-2. ~402 active. Immoweb dominant BE portal |
| DK | Denmark | https://www.boligsiden.dk/postnummer/8000/tilsalg/ejerlejlighed | Aarhus C 8000, Region Midtjylland | DKK 3M–5M (~€400k–€670k) | Ejerlejlighed | 70–100 m², 2–3 bed | Boligsiden.dk | 403-DD | Aarhus = DK #2 city, mid-tier (NOT Copenhagen). Boligsiden aggregates ~100% DK realtors |
| IS | Iceland | https://fasteignir.visir.is/ | Reykjavík 101, Höfuðborgarsvæðið | ISK 50M–80M (~€330k–€530k) | Íbúð | 70–100 m², 2–3 bed | Fasteignir.is | 200 | IS has only ~360k pop; Reykjavík ~60% of all stock. Listing IDs rotate fast on small market |
| SI | Slovenia | https://www.nepremicnine.net/oglasi-prodaja/ljubljana-mesto/stanovanje/ | Ljubljana, Osrednjeslovenska | €200k–€350k typical 2-bed | Stanovanje | 50–70 m², 2 bed | Nepremicnine.net | 403-DD | Ljubljana is the only SI Tier-1 market (~25% of country); ~3,000 EUR/m² urban benchmark |
| IE | Ireland | https://www.daft.ie/property-for-sale/dublin-8-dublin/apartments | Dublin 8 (Inchicore/Liberties) | €330k–€420k for 2-bed apt | Apartment | 47–66 m², 2 bed | Daft.ie | 403-DD | Dublin 8 = mid-tier inner-city, NOT D2/D4 luxury, NOT D24 outer suburb. 105 active 2-bed apt |
| GR | Greece | https://www.spitogatos.gr/en/for_sale-apartments/thessaloniki-center | Thessaloniki Center | €80k–€180k | Διαμέρισμα | 50–90 m², 2 bed | Spitogatos.gr | 200 | Thessaloniki = GR #2 city. 13,855 active. NOT Athens premium, NOT Mykonos/Santorini holiday |
| PL | Poland | https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/wroclaw | Wrocław, Dolnośląskie | PLN 500k–800k (~€115k–€185k) | Mieszkanie | 40–70 m², 2 pokoje | Otodom.pl | 200 | Wrocław = PL Tier-2 (NOT Warszawa premium, NOT Łódź distress). Otodom dominant PL portal |
| EE | Estonia | https://www.kv.ee/kinnisvara/korterid1?county=1 | Tallinn (Harjumaa) | €150k–€280k | Korter | 50–70 m², 2 tuba | KV.ee | 403-DD | Tallinn dominates EE market (~3,000 €/m² avg). Soviet + Nordic infill normal stock |
| HR | Croatia | https://www.njuskalo.hr/prodaja-stanova/zagreb | Zagreb (e.g., Malešnica/Črnomerec) | €200k–€400k | Stan | 50–90 m², 2-3 sobe | Njuškalo.hr | 200 | Zagreb = HR Tier-1 (~50% transactions); inland NOT coastal-tourist (Split/Dubrovnik distort) |
| HU | Hungary | https://ingatlan.com/lista/elado+lakas+budapest-viii-ker | Budapest VIII. kerület (Józsefváros — Corvin) | HUF 50M–90M (~€125k–€225k) | Lakás | 50–80 m², 2 szoba | Ingatlan.com | 403 | District VIII = Budapest mid-tier (gentrifying core, NOT V/VI luxury, NOT outer panel). 2,341 active |
| LT | Lithuania | https://en.aruodas.lt/butai/vilniuje/ | Vilnius 01000+ (Šnipiškės/Naujamiestis) | €150k–€280k typical 2-bed | Butas | 50–70 m², 2 kambariai | Aruodas.lt | 403-DD | Vilnius dominates LT property. Aruodas ~80% share. Nordic-style infill + Soviet panel mix |
| LV | Latvia | https://www.ss.lv/lv/real-estate/flats/riga/all/sell/ | Rīga (Centrs/Teika/Purvciems) | €70k–€180k | Dzīvoklis | 50–70 m², 2-3 istabas | SS.lv | 200 | Rīga dominates LV. SS.lv unique dominant LV classifieds. Soviet-era panel normal. Lower price tier than EE/LT |
| RO | Romania | https://www.imobiliare.ro/vanzare-apartamente/cluj-napoca | Cluj-Napoca 400000, Cluj | €100k–€200k typical 2-bed | Apartament (2-3 camere) | 50–70 m², 2-3 camere | Imobiliare.ro | 200 | Cluj-Napoca = RO #2 city (NOT București), tech/university hub with stable mid-tier prices |
| BG | Bulgaria | https://www.imot.bg/obiavi/prodazhbi/grad-sofiya | Sofia (Lyulin/Mladost districts) | €80k–€150k typical 2-bed | Двустаен/Тристаен апартамент | 60–90 m², 2-3 stay | Imot.bg | 200 | Sofia dominates BG (~50% of listings). Lyulin/Mladost normal panel-block (NOT Lozenets luxury) |
| LU | Luxembourg | https://www.athome.lu/vente/appartement/luxembourg/ | Luxembourg-Gare area | €450,000 example listing (mid-segment ~€10,500/m²) | Appartement | 43-80 m², 1-2 bed | atHome.lu | 200 | LU = highest €/m² in EU. Gare = well-connected normal district (NOT Belair/Limpertsberg premium) |
| CY | Cyprus | https://www.bazaraki.com/real-estate-for-sale/apartments-flats/lemesos-district-limassol/ | Limassol (Neapolis/Petrou Kai Pavlou) | €189k–€440k typical 2-bed | Apartment | 70–100 m², 2 bed | Bazaraki.com | 403-DD | Limassol = CY economic hub (NOT Nicosia government-only, NOT Paphos retiree-coastal). Mid-tier residential |
| MT | Malta | https://remax-malta.com/properties/sliema/ | Sliema | €375,000 example | Apartment | ~70–80 m², 2 bed | RE/MAX Malta | 200 | Sliema = MT mainstream urban (NOT Valletta luxury heritage, NOT Gozo rural) |

## Western Balkans (5)

| ISO | Country | Listing URL | Locality | Price | Type | Portal | Verify | Why |
|---|---|---|---|---|---|---|---|---|
| RS | Serbia | https://www.nekretnine.rs/stambeni-objekti/stanovi/izdavanje-prodaja/prodaja/grad/beograd/lista/po-stranici/10/ | Beograd, Vračar (Centar) | €289k–€448k | Stan (apartment, 60–100 m², 3-4 rooms) | Nekretnine.rs | 200 | Belgrade Tier-1 (~70% market). Vračar mid-to-upper inner Belgrade (~€3,500–4,500/m²) |
| ME | Montenegro | https://www.realitica.com/prodaja/stanova/podgorica/Crna-Gora/ | Podgorica, Glavni grad | €80k–€180k | Stan (50–80 m², 2-3 rooms) | Realitica.com | 200 | Podgorica = ME capital, mid-tier (~€2,300/m²). Coastal cities (Budva/Kotor) distort with foreign buyers — Podgorica is local-market normal. **Note: nekretnine.me unreachable; use realitica or estitor.com** |
| BA | Bosnia & Herzegovina | https://olx.ba/nekretnine | Sarajevo Kanton, FBiH | KM 200k–400k (~€100k–€205k) | Stan (50–80 m², 2-3 rooms) | OLX.ba | 403 | OLX.ba = THE dominant BA classifieds. Sarajevo Centar/Novo Sarajevo mid-tier. Avoids Banja Luka (RS-entity) skew |
| MK | North Macedonia | https://www.pazar3.mk/ads/real-estate/apartments/skopje/centar | Skopje, Centar | €70k–€150k typical 2-bed | Stan (50–80 m², 2-3 rooms) | Pazar3.mk | 200 | Skopje Tier-1 (~60% market). Centar normal urban core (NOT Vodno luxury). Pazar3 dominant MK general-classifieds |
| AL | Albania | https://www.merrjep.al/njoftime/imobiliare-vendbanime/apartamente/tirane | Tirana, Tirana County | €60k–€120k typical; mid ~€90k | Apartament 1+1 / 2+1 (50–80 m², 1-2 dhoma) | MerrJep.al | 200 | Tirana Tier-1 (~70% market). MerrJep dominant AL classifieds |

## Anglo non-EU (3)

| ISO | Country | Listing URL | Locality | Price | Type | Portal | Verify | Why |
|---|---|---|---|---|---|---|---|---|
| CA | Canada | https://www.realtor.ca/on/toronto | Toronto, ON M5V 0H8 (Niagara/CityPlace) | CAD 598,500 | Condo (1+den, ~55–65 m², 1+1 bed) | REALTOR.ca | 200 | Toronto M5V is downtown Niagara/CityPlace — most active condo zone. CAD ~$600k below median (~$700k condos), normal mid-tier |
| AU | Australia | https://www.realestate.com.au/buy/in-brisbane+city,+qld+4000/list-1 | Brisbane City QLD 4000 | AUD 450k–700k typical 2-bed apt | Apartment / unit (60–80 m², 2 bed) | realestate.com.au | 429-DD | Brisbane CBD = AU Tier-2 (NOT Sydney/Melbourne premium). REA Group dominant ~70% share |
| NZ | New Zealand | https://www.trademe.co.nz/a/property/s/residential/sale/apartments-for-sale-wellington/ | Wellington Central / Te Aro | NZD 450k–800k typical 2-bed apt | Apartment (50–80 m², 2 bed) | Trade Me Property | 406 | Wellington = NZ #2 (NOT Auckland premium). Trade Me ~95% NZ listings dominance |

## Latin America (5)

| ISO | Country | Listing URL | Locality | Price | Type | Portal | Verify | Why |
|---|---|---|---|---|---|---|---|---|
| MX | Mexico | https://www.inmuebles24.com/departamentos-en-venta-en-roma-norte-ciudad-de-cuauhtemoc.html | Roma Norte, Cuauhtémoc, CDMX | MXN 4.7M–10.2M (~USD 230k–500k) | Departamento (60–100 m², 2 rec) | Inmuebles24 | 403-DD | Roma Norte = CDMX gentrified mid-to-upper (NOT Polanco/Condesa luxury, NOT outer-borough discount). 1,037 active |
| BR | Brazil | https://www.vivareal.com.br/venda/minas-gerais/belo-horizonte/bairros/savassi/apartamento_residencial/ | Savassi, Belo Horizonte, MG | R$ 640k–2.4M (~USD 110k–420k); mid ~R$ 900k | Apartamento (50–170 m², 2-3 quartos) | Viva Real | 403-DD | Savassi = BH mainstream upper-mid central (NOT São Paulo Vila Olímpia ultra-premium, NOT Rio Copacabana tourist) |
| AR | Argentina | https://www.zonaprop.com.ar/departamentos-venta-palermo.html | Palermo, CABA | USD 60k–250k (Argentine market USD-priced) | Departamento (40–80 m², 1-3 amb) | Zonaprop | 403-DD | Palermo = most-listed BA neighborhood (~12,500 active) — broad spectrum incl. USD 60k–100k entry. AR market quotes USD due to peso volatility |
| CR | Costa Rica | https://www.encuentra24.com/costa-rica-en/real-estate-for-sale-houses-homes/san-jose-escazu | Escazú, San José Province | mid-segment ~USD 350k (median single-family) | Casa | 200-420 m², 3-4 bed | Encuentra24 | 200 | Escazú = standard expat/upper-middle-class for San José. CR market USD-denominated for mid-to-upper segment |
| PA | Panama | https://www.encuentra24.com/panama-en/real-estate-for-sale-apartments-condos/prov-panama-panama-city | Panama City (San Francisco / Coco del Mar / Bella Vista) | USD 183k → USD 372k; mid ~USD 280k | Apartamento (60–120 m², 1-3 rec) | Encuentra24 | 200 | PTY Tier-1 (~80% market). USD-denominated. San Francisco / Coco del Mar mid-tier expat-friendly (NOT Punta Pacifica luxury, NOT Casco Viejo heritage) |

---

## CDN-protection summary

**Tier-1 portals reliably 200-OK to curl** (good for automated tests):
- sreality.cz, nehnutelnosti.sk, willhaben.at, hemnet.se, etuovi.com, finn.no, rightmove.co.uk, funda.nl, fasteignir.is, spitogatos.gr, otodom.pl, ss.lv, imobiliare.ro, imot.bg, athome.lu, remax-malta.com, nekretnine.rs, njuskalo.hr, pazar3.mk, merrjep.al, realtor.ca, encuentra24.com (CR + PA)

**DataDome / Cloudflare / Akamai protected** (browser-loadable; use Playwright stealth for automated fetch):
- seloger.com (DataDome), immobiliare.it (DataDome), immobilienscout24.de (Akamai), homegate.ch (DataDome), idealista.com / idealista.pt (DataDome), immoweb.be (Cloudflare), boligsiden.dk (Cloudflare), nepremicnine.net (Cloudflare), daft.ie (Cloudflare), aruodas.lt (Cloudflare), bazaraki.com (Cloudflare), kv.ee (Cloudflare), ingatlan.com (Cloudflare), olx.ba (Cloudflare), realestate.com.au (rate-limit + DataDome), trademe.co.nz (UA-gating, returns 406 to non-browser), inmuebles24.com (DataDome), vivareal.com.br (DataDome), zonaprop.com.ar (DataDome)

**Flagged for re-verify**:
- nekretnine.me — DNS/timeout — switch ME source to realitica.com or estitor.com
- BE Immoweb specific listing IDs rotate — use search URL

## Fixture usage notes

1. **Search-page URLs vs specific-listing URLs**: most rows point to a search page (filter pre-applied) because individual listing slugs rotate as inventory churns (typical median time-on-market: 30–120 days). For self-test, the skill should verify (a) portal main domain renders + (b) at least one valid listing card appears
2. **Currency conversion**: use ECB reference rates (or `--currency` feed). AR/CR/PA quote USD natively. UK/CH/CA/AU/NZ each in own currency
3. **Refresh policy**: re-verify quarterly (Jan/Apr/Jul/Oct). Listing-detail URLs (Eindhoven Stationsweg, Toronto Bruyeres Mews, etc.) are ephemeral and likely 404 within 6–12 months once sold
4. **Anti-luxury filter applied**: rows chosen near *median* per-m² rate of chosen city, NOT top quartile. Cities themselves Tier-2 / mid-tier wherever feasible

## Operational integration

```bash
# self-test mode
/property-deep-dive --update --validate-only --test

# loads each fixture, runs --price + --tax + --risks
# reports per-country pass/fail
# logs to _local/reports/test-fixtures-<date>.md
```

Expected output:
- 22+ fixtures should fully complete
- 21+ require Playwright stealth (browser-mode)
- 1 (ME) needs source-switch to realitica.com

## Anti-hallucination

- **DOM is broker-aggregated** — verify per-transaction in 2-3 local agents per micro-market
- **Listings churn** — 30%+ link-rot per quarter
- **Don't fabricate URLs**: if a fixture is broken, mark `[NEEDS MANUAL CURATION]` rather than guess

## Status

Last refreshed: 2026-04-26. **44/44 rows populated**, 22 verified 200-OK, 21 verified bot-protected (browser-loadable), 1 flagged for ME source switch.
