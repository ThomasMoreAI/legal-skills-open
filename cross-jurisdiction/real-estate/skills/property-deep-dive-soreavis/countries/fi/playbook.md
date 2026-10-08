# Finland 🇫🇮 — Property Due-Diligence Playbook

ISO2: `fi`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 5 digits (`00100` Helsinki, `33100` Tampere, `20100` Turku)
- **Admin levels**: 19 maakuntaa (regions) + 309 kuntaa (municipalities)
- **Currency**: EUR (€) — adopted 1999/2002
- **Languages**: **Finnish + Swedish (both official)**; Sámi minority (Lapland)
- **Cadastre**: **Maanmittauslaitos (NLS Finland)** + **KTJ (Kiinteistötietojärjestelmä)** national property register
- **Identifier**: kiinteistötunnus 4-section format (e.g., `091-018-0118-0006` = `<kunta>-<kylä/kaupunginosa>-<rekisterinumero>-<rekisteriyksikkö>`)
- Distinct ownership types: **kiinteistö** (real-estate freehold — land + building together), **asunto-osakeyhtiö (As Oy)** (housing company — share-based, MAJOR form), **käyttöoikeus** (right of use)

## Section: `--price`

### Primary sources

- **Maanmittauslaitos KTJ portal**: `https://www.maanmittauslaitos.fi/en/e-services`
- **KTJ Kiinteistörekisteri** (cadastre records): paid extracts
- **OmaKiinteistö** (own-property service)
- **Hintaseuranta** (price tracking by Etuovi)

### Listing platforms

- **Etuovi.com** — largest: `https://www.etuovi.com/`
  - Search by kunta + alueet + asunto-tyyppi
- **Oikotie**: `https://asunnot.oikotie.fi/`
- **Vuokraovi.com** (rentals)
- **Bjäkari, Habita, Sp-Koti, OPKK** — agency networks
- **Kiinteistömaailma**, **Huoneistokeskus** — premium agencies

### 2025 price benchmarks (Tilastokeskus + Hintaseuranta)

| Region | Asunto-Oy €/m² | Omakotitalo avg total |
|---|---:|---:|
| **Helsinki** | 5,500–8,500 (centro 7,500–11,000) | €600,000–€1,500,000 |
| **Espoo, Vantaa** | 4,500–6,500 | €550,000–€900,000 |
| **Tampere** | 3,200–5,000 | €350,000–€600,000 |
| **Turku** | 3,000–4,500 | €320,000–€500,000 |
| **Oulu** | 2,200–3,500 | €280,000–€450,000 |
| **Jyväskylä** | 2,500–3,800 | €280,000–€450,000 |
| **Lahti, Kuopio, Pori** | 2,000–3,200 | €230,000–€380,000 |
| Smaller cities | 1,500–2,500 | €180,000–€280,000 |
| Rural / Mökki | 700–1,500 | €80,000–€200,000 (mökki up to €500k+ Lapland resort) |

### Compute

1. Listing €/m² = price / **asuinpinta-ala** (residential area, includes interior walls)
2. **Trap**: asuinpinta-ala vs huoneistoala (apartment area, slightly different) vs kerrosala (gross floor)
3. **As Oy math**: you buy **shares** (osake) in housing company; each share = € amount; **yhtiövastike** (monthly fee) covers building maintenance + sometimes shared mortgage
4. **Yhtiölaina** (housing company loan) tied to apartment — apartment carries portion of building debt

---

## Section: `--traffic`

### Primary sources

- **Väylävirasto** (Finnish Transport Infrastructure Agency): `https://vayla.fi/`
  - Open data via Liikennevirasto
- **Liikennevirasto Open data portal**: `https://www.liikennetilanne.fi/` (real-time)
- **Traficom** (traffic safety agency): `https://www.traficom.fi/`

### Key term

**KVL (keskimääräinen vuorokausiliikenne)** = AADT-equivalent

### Verdict bands

- 🟢 < 1,000 v/d (paikallistie, residential katu)
- 🟡 1,000–8,000 v/d (kantatie, urban arterial)
- 🟠 8,000–30,000 v/d (valtatie, major urban)
- 🔴 > 30,000 v/d (moottoritie, central Helsinki/Tampere ring)

---

## Section: `--tax`

### Annual property tax — Kiinteistövero

**Set by each kunta within state-mandated bands**:

| Property type | 2025 rate range |
|---|---:|
| **Yleinen** (general, default) | 0.93–2.00 % of taxable value |
| **Vakituinen asunto** (primary residence) | **0.41–1.00 %** |
| **Muu asuinrakennus / vapaa-ajan asunto** (secondary/holiday) | **0.93–2.00 %** — significantly higher |
| **Voimalaitos / yleishyödyllinen** | 0.93–3.10 % / variable |

**Calculation base**: Verovirasto-determined valuation (~50–70 % of market value). Reform pending — bills could rise.

**Bills**: annually, paid March + September.

**Exemptions**: agricultural land + maa- ja metsätalous = 0.93–2.00 % (cheaper than vapaa-ajan asunto).

### Transaction taxes — Varainsiirtovero (REFORM 2024)

**MAJOR REDUCTION 1 January 2024** (retroactive from 12 Oct 2023):

| Asset | Old rate | **2024+ rate** |
|---|---:|---:|
| **Kiinteistö (real estate)** | 4.0 % | **3.0 %** |
| **Asunto-osakeyhtiö (As Oy) shares** | 2.0 % | **1.5 %** |
| **Other securities (incl. real-estate-company shares)** | 1.6 % / 2.0 % | **1.5 %** (unified from 1 Jan 2024) (2026-05-27 verified, source: vero.fi / Krogerus / Roschier) |

**First-time buyer exemption ABOLISHED** in 2024 (was 4 %/2 % for 18-39 year-old first-time buyers since 1989).

### Notary / title

- **No notary** in Finland real estate; transactions handled by **kaupanvahvistaja** (purchase witness)
- Kaupanvahvistajan palkkio: ~€120-200 fixed
- Maanmittauslaitos kirjaaminen (registration): **€132** (2025 rate)
- Real estate agent (välittäjä) fee: **est. 2.5–4.0 %** of price (market practice; negotiable), paid by seller

### Capital gains — Luovutusvoittovero

- **30 %** for gain ≤ €30,000/yr
- **34 %** above threshold
- Rates/threshold per pääomatulo (capital-income) schedule — same as verified `--rental` entry below (source: vero.fi luovutusvoitto / rental-income guidance, 2026-05-27 verified)
- **Primary residence exemption**: 2 yrs ownership + occupation → fully exempt
- **Vapaa-ajan asunto** (secondary): full tax applies

### VAT (ALV)

- 25.5 % standard (raised from 24 % in Sept 2024)
- **13.5 %** reduced (food, restaurant services, books, pharmaceuticals, passenger transport — lowered from 14 % effective 1 Jan 2026, vero.fi) (2026-05-27 verified)
- 10 % reduced (books, accommodation services, transport)
- New residential property: **25.5 % ALV** (standard rate from 1 Sep 2024) in price typically; existing: VAT-exempt (2026-05-27 verified, source: vero.fi VAT rates)
- Commercial: 25.5 %

### Total transaction cost (buyer side)

- Real estate freehold: ~3.5–5 % of price
- As Oy shares: ~2–4 % of price
- Among the **lower** in EU (after 2024 reform)

### Future risk

- Kiinteistövero reform: proposals to base the tax on market value could raise bills materially (~est. 30-50 % in higher-value areas) — verify at vero.fi / VM (valtiovarainministeriö) reform tracker
- ALV may continue rising
- Vapaa-ajan asunto kiinteistövero pressure increasing

---

## Section: `--rental`

### Long-term residential

- **Asuinhuoneiston vuokrasta annettu laki** (Tenancy Act)
- Tenant protection moderate (less strict than DE/SE/AT)
- **Toistaiseksi voimassa oleva** (indefinite term) common
- **Määräaikainen** (fixed-term) up to 6 yrs typical

### Short-let (Airbnb / Booking)

- **As Oy approval** typically required (most As Oy ban or restrict short-let in their yhtiöjärjestys)
- **Helsinki + Tampere + Turku** + spa towns: tightening regulation 2024-2026
- **EU Regulation 2024/1028**: FI transposition pending May 2026

### Tax on rental

- **Pääomatulo (capital income)**: 30 % up to €30k, 34 % above
- **Vähennykset** (deductions): kunnossapito, korjaukset, yhtiövastike, korot
- **Tulonhankkimisvähennys**: lump-sum option
- **Sähkölämmitys** (electric heating) typically not deductible separately
- **No de-minimis exemption for rental income** — all rent is capital income (30 %/34 %), reportable even when net is zero after deductions (2026-05-27 verified, source: vero.fi rental-income guidance)

---

## Section: `--work=<profession>`

### Job platforms

- **Työ- ja elinkeinotoimisto (TE-toimisto)**: `https://www.te-palvelut.fi/`
- **LinkedIn FI**, **Duunitori**, **Oikotie työpaikat**, **Indeed.fi**
- **Monster.fi**, **MOL.fi**

### Self-employment

- **Toiminimi (sole trader)**: simplest
- **Osakeyhtiö (Oy / Ltd)**: **no minimum share capital since 1 Jul 2019** (previously €2,500); Oyj (public Ltd) still €80,000 (2026-05-27 verified, source: Waselius)
- **YEL** (yrittäjän eläkevakuutus) pension insurance mandatory above ~€9,500/yr earnings
- **Sairausvakuutus** + **TyEL/YEL** social
- **Verohallinto Y-tunnus** business ID needed

### Salary benchmarks (2025)

- Median monthly gross:
  - Helsinki: ~€3,800
  - Tampere, Turku: ~€3,300
  - Smaller cities: ~€2,800
- **No statutory minimum wage** (set per industry by union agreement)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **SYKE (Suomen ympäristökeskus)** | `https://www.syke.fi/` | Environment institute |
| **Tulvakartta** (flood maps) | `https://www.vesi.fi/vesitieto/tulvakarttapalvelu/` | Q10/Q100/Q1000 flood hazard |
| **GTK (Geologinen tutkimuskeskus)** | `https://gtk.fi/` | Geology, radon |
| **STUK (Säteilyturvakeskus)** | `https://www.stuk.fi/` | Radon program |
| **STUK Radonkartta** | `https://stuk.fi/en/radon-in-finland` | Indoor radon levels — Finland highest in EU |
| **Ilmatieteen laitos (FMI)** | `https://www.ilmatieteenlaitos.fi/` | Climate, weather |
| **Ympäristöministeriö** | `https://www.ymparisto.fi/` | Aggregated environment portal |

### Specific risks

- **Tulva (flooding)** — coastal Helsinki + Espoo, lake/river plains; Vuoksi basin (East FI)
- **Radon — HIGHEST INDOOR LEVELS IN EU** on average:
  - **Pirkanmaa, Päijät-Häme, Itä-Uusimaa, Etelä-Karjala, Kanta-Häme** worst-affected
  - ~est. 7-9 % of single-family houses exceed the WHO 100 Bq/m³ reference level (per STUK radon program — see source table above; verify specific figure/year at stuk.fi)
  - Mandatory testing in some kunnat
- **Earthquake** — very low (stable Fennoscandian Shield)
- **Roudan aiheuttama vaurio** (frost heave) — ground freezing affects shallow foundations
- **Lumikuorma** (snow load) — heavy winters can cause roof collapse (esp. flat roofs)
- **Maaston eroosio** (coastal erosion) — Baltic Sea coastline
- **Luonnonpalo (wildfires)** — increasing climate risk
- **Sea-level rise** + **post-glacial rebound**: net effect varies (positive uplift in Lapland, negative on south coast)

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1960s** | Lead paint, asbestos, weak insulation |
| **1960s–1980s "betonilähiö"** (concrete suburbs) | Asbestos very common (joints, isolation), low energy efficiency |
| **1980s–2000s** | Improved insulation, modern wiring, formaldehyde from particleboard |
| **Post-2010 (E-luokka)** | Energy efficiency standards |
| **Post-2017 nZEB** | Strict |

**Asbestos**: pre-1994 buildings highly likely (banned 1994); removal ~est. €30–€80/m² (see FI 2026 cost benchmarks below).

**Putkiremontti (pipe renovation)**: ~50-year cycle for stamb (vertical pipe runs); buildings 1960s-1970s coming due now or already done; **cost per apartment €30,000-80,000+** for full renovation.

### Mandatory diagnostics at sale

| Document | Required because | Validity |
|---|---|---|
| **Energiatodistus** (energy certificate) | All sales since 2009 | 10 years |
| **Kuntotutkimus** (condition study) | Strongly recommended; sometimes required | Per case |
| **Asbestikartoitus** (asbestos survey) | Pre-1994 buildings during renovation | Per case |
| **Yhtiöjärjestys** + **isännöitsijän todistus** | If As Oy | At sale |
| **Yhtiön tilinpäätös** + **toimintakertomus** + **kunnossapitosuunnitelma** | If As Oy | At sale |
| **Kaupanvahvistajan todistus** | All sales | At signing |

### As Oy diligence (CRITICAL)

Before buying any As Oy apartment, demand:
1. **Yhtiöjärjestys** — articles of association
2. **Isännöitsijän todistus** (manager's certificate, valid 3 months)
3. **3-vuoden tilinpäätös** + **toimintakertomus**
4. **PTS (Pitkän tähtäimen kunnossapitosuunnitelma)** — long-term maintenance plan
5. **Yhtiölaina** (building debt allocated to your share) — often €30k–€100k+
6. **Tulevat hankkeet** — upcoming putkiremontti, julkisivu, katto

**Red flags**: yhtiölaina > €100k/apt without recent renovation, deferred putkiremontti for 1970s building, monthly yhtiövastike >€8/m².

### Climate change projections (FMI)

- +2.0–4.0 °C by 2050 (RCP scenarios)
- More precipitation: winter rain increasing (less snow)
- Sea-level rise (south coast): partial offset by isostatic rebound (north)
- Drought: rare but increasing summer events
- Forest fires: rising
- Permafrost retreat in Lapland

---

## Section: `--mains`

### Sources

- **Vesilaitosyhdistys (VVY)**: `https://www.vvy.fi/` — national water utility association
- Each kunta manages own vesilaitos + viemärilaitos
- Major: **HSY** (Helsinki region — Helsinki + Espoo + Vantaa + Kauniainen), **Tampereen Vesi**, **Turun Seudun Vesi**, **Oulun Vesi**

### Verification

- Most populated areas: kunnan mains universal
- Rural + mökki: own **porakaivo** (drilled well) + **saostuskaivot** (septic)
- **Hajajätevesiasetus** (Government Decree 157/2017): strict requirements for cottages — must comply by 31 Oct 2019 (extensions possible)

### Costs

| Scenario | Cost (€) |
|---|---:|
| Liittymismaksu (mains connection) | 5,000–15,000 |
| Saostuskaivo upgrade compliant | 5,000–15,000 |
| Pienpuhdistamo (small treatment plant) | 8,000–18,000 |
| Porakaivo (drilled well) | 6,000–12,000 |

---

## Cost benchmarks (FI 2026)

| Work | Cost (€) |
|---|---:|
| Energiatodistus | 300–700 |
| Kuntotarkastus (condition survey) | 400–800 |
| Kuntotutkimus (deeper) | 1,000–3,000 |
| Asbestikartoitus | 200–500 |
| Kaupanvahvistaja | 120–200 |
| Maanmittauslaitos kirjaaminen | 132 |
| **Varainsiirtovero (kiinteistö)** | **3 % of price** |
| **Varainsiirtovero (As Oy shares)** | **1.5 % of price** |
| **Total transaction cost (kiinteistö)** | **~3.5–5 %** of price |
| **Total transaction cost (As Oy)** | **~2–4 %** of price |
| Saostuskaivo upgrade compliant | 5,000–15,000 |
| Roof (steel sheet, 150 m²) | 15,000–30,000 |
| Asbestos removal (200 m²) | 4,000–10,000 |
| Putkiremontti per apartment (As Oy) | 30,000–80,000 |
| Energy retrofit (Class C → A) | 40,000–90,000 |

## Active fiscal incentives (2025-2026)

- **Kotitalousvähennys** (household tax deduction): **35 %** of VAT-inclusive labour from a company (or 13 % of gross wages if hiring directly); **max €1,600/yr/person, €3,200 for a couple**; €150 self-pay threshold. Oil-heating replacement gets the elevated **60 %/€3,500** rate only (2026-05-27 verified, source: vero.fi)
- **Asuntoremontin verovähennys**: included in kotitalousvähennys
- **Energia-avustus** (energy grants via ARA): up to €4,000/apt for energy retrofit
- **Lämpöpumppu-avustus** heat pump grants
- **Aurinkosähkö-avustus** PV solar (5 % deduction)

## Common listing platforms

- **Etuovi.com** — biggest, full extraction
- **Oikotie** — major, listings + price tracking (Hintaseuranta)
- **Vuokraovi** — rentals
- **OPKK, Sp-Koti, Habita, Bjäkari, Aktia** — agency networks
- **Tori.fi**, **Huutokaupat.com** — privates + foreclosures

## Caveats unique to FI

- **As Oy ownership is share-based** — you own shares in a housing company, NOT the apartment directly. Yhtiövastike covers maintenance + utilities + sometimes mortgage of building.
- **Yhtiöjärjestys** (articles of association) defines share rights — must read before buying
- **Yhtiölaina** (allocated building debt) often hidden cost: total apartment "real cost" = listing price + share of yhtiölaina
- **Kuntotutkimus + isännöitsijän todistus** = key due-diligence documents for As Oy purchase
- **Putkiremontti** cycle ~50 years — 1970s buildings approaching this can have €30-80k assessment per apartment
- **Highest indoor radon in EU** — radon test mandatory for Pirkanmaa + Etelä-Karjala
- **Mökkikulttuuri** (cottage culture) — secondary-home market huge; **vapaa-ajan asunto kiinteistövero up to 2 %** (significant)
- **Rauhoitusalueet** (protected areas) — strict construction limits
- **Sähkölämmitys** (electric heating) common in older houses — high running costs vs heat pump retrofit
- **Varainsiirtovero reduced 2024** — buyer-side costs now lower
- **No notary** in real estate transactions — handled by kaupanvahvistaja
- **Two official languages**: documents may need Swedish translation in bilingual kunnat (Helsinki/Espoo + Pohjanmaa coast)
- **Kotipaikkavaatimus** (residence requirement): some As Oy require permanent residence — affects investment buyers
- **AHL (asunto-osakeyhtiölaki) 2010** governs As Oy

## Reddit / forum sources

- **r/Finland**, **r/AskFinland**, **r/Helsinki**
- **r/Suomi** (Finnish-language)
- **Vauva.fi forum** (Finnish discussion incl. property)
- **Asuntoblogi**, **Talousliikkuja** financial blogs
- Expat: **r/Finland** + **The Local Finland**

## Verification authorities

| Authority | When to call |
|---|---|
| **Maanmittauslaitos** | Title verification, kiinteistö data |
| **Kunta rakennusvalvonta** | Permits, asemakaava |
| **Verohallinto** | Kiinteistövero, varainsiirtovero |
| **Kaupanvahvistaja** | Final transfer (purchase witness) |
| **Vesilaitos kunta** | Mains drains verification |
| **As Oy isännöitsijä** | If apartment: financials, planned projects |
| **STUK** | Radon information |
| **GTK** | Geology |
| **SYKE / ELY-keskus** | Floods, environment |

## Quirks to know

- **Kiinteistö vs As Oy** distinction is fundamental (freehold vs share-based)
- **Lainhuutotodistus** (title certificate) for kiinteistö
- **Osakekirja** (share certificate) for As Oy — increasingly digital via ASREK
- **Hallinnanjakosopimus** (subdivided occupancy agreement) for split apartments
- **Tonttioikeusvuokrasopimus** (ground lease) — common in Helsinki city land
- **Asunnon hallintaoikeus** transfers to buyer once kauppa finalised
- **Pakettilaki** (consumer protection) for new As Oy (RS-järjestelmä)
- **Vakuutus pakollinen** (insurance mandatory) for mortgage holders typically

## Source URL templates

| Source | URL pattern |
|---|---|
| Maanmittauslaitos | `https://www.maanmittauslaitos.fi/` |
| Etuovi | `https://www.etuovi.com/<kaupunki>` |
| Oikotie | `https://asunnot.oikotie.fi/<kaupunki>` |
| Tilastokeskus | `https://stat.fi/` |
| Tulvakartta | `https://www.vesi.fi/vesitieto/tulvakarttapalvelu/` |
| GTK | `https://gtk.fi/` |
| STUK Radon | `https://stuk.fi/en/radon-in-finland` |
| Verohallinto Kiinteistövero | `https://www.vero.fi/henkiloasiakkaat/asuminen/kiinteistovero/` |
| Liikennetilanne | `https://www.liikennetilanne.fi/` |

## Status

✅ **Fully populated** as of 2026-04-25.
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for tax + cadastre sources (Maanmittauslaitos + Verohallinto definitive); HIGH for varainsiirtovero 2024 reform (3 % / 1.5 % confirmed). MEDIUM for short-let regulation (EU 2024/1028 transposition pending May 2026 deadline).

## Extension TODOs

- [ ] Per-kunta kiinteistövero rate tables
- [ ] As Oy yhtiöjärjestys red-flag detection (kotipaikkavaatimus, short-let bans)
- [ ] Putkiremontti cycle estimate per building age + region
- [ ] Tulvakartta address-level lookup
- [ ] Radon zone overlay per kunta
- [ ] Yhtiölaina / debt-tied-to-shares calculation tooling
- [ ] Mökki-specific tax + utility decision tree
- [ ] Bilingual kunnat (Swedish-required documents)
