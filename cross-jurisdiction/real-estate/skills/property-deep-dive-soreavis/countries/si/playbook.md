# Slovenia 🇸🇮 — Property Due-Diligence Playbook

ISO2: `si`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4 digits (`1000` Ljubljana, `2000` Maribor, `3000` Celje, `4000` Kranj, `6000` Koper, `9000` Murska Sobota)
- **Admin levels**: 12 statistical regions + 212 občine (municipalities)
- **Currency**: **EUR (€)** — adopted 1 Jan 2007 (first new EU member to join eurozone)
- **Languages**: Slovenian (official); Italian + Hungarian (constitutional minorities along borders)
- **Cadastre**: **GURS (Geodetska uprava RS)** — Surveying and Mapping Authority
- **Identifier**: **parcelna številka** + **katastrska občina (KO)** (e.g., `123/4 k.o. Ljubljana`)
- **Ownership types**:
  - **Lastnina** (full ownership)
  - **Etažna lastnina** (condominium ownership for apartments)
  - **Solastnina** (co-ownership)
  - **Skupna lastnina** (joint ownership)
  - **Stavbna pravica** (right to build on someone else's land)
- **Zemljiška knjiga** (land register, e-Sodstvo) governs all real estate

## Section: `--price`

### Primary sources

- **GURS Javni vpogled v podatke o nepremičninah** (FREE official cadastre): `https://ipi.eprostor.gov.si/jv/`
- **GURS Vrednotenje** (mass valuation, free public viewer): `https://vrednotenje.gov.si/EV_JV/`
  - **MAJOR REFORM 13 May 2025**: new posplošena vrednost regulation effective; new model values issued June 2025
- **OPSI** open data: `https://podatki.gov.si/dataset/kataster-nepremicnin`
- **ETN (Evidenca trga nepremičnin)** — transactions register, GURS-managed
  - Aggregated stats free; per-transaction limited
- **e-Sodstvo Zemljiška knjiga**: `https://evlozisce.sodisce.si/esodstvo/index.html` — land register lookup
- **SURS (Statistični urad RS)**: `https://www.stat.si/` — national stats

### Listing platforms

- **Nepremicnine.net** — DOMINANT: `https://www.nepremicnine.net/`
- **Bolha.com**: `https://www.bolha.com/nepremicnine`
- **Salomon.si**, **Slonep.net** — secondary
- Agency networks: **Stoja Trade**, **Re/Max Slovenia**, **TopRealitet**, **DODOMA**

### 2025 price benchmarks (GURS ETN transacted + nepremicnine.net asking prices per listing — verify against GURS ETN transacted values)

| Region | Avg €/m² (apt) | Avg total (hiša, single-family) |
|---|---:|---:|
| **Ljubljana centro** | 4,000–6,500 | 500,000–1,200,000+ |
| **Ljubljana okolica** | 3,000–4,500 | 380,000–650,000 |
| **Maribor** | 1,800–2,800 | 180,000–320,000 |
| **Koper / Izola / Piran** (coastal) | 3,500–5,500+ | 380,000–800,000+ |
| **Celje** | 1,600–2,400 | 160,000–280,000 |
| **Kranj / Bled / Bohinj** | 2,200–4,500 | 250,000–600,000 |
| **Smaller cities** | 1,200–1,800 | 130,000–230,000 |
| **Rural Štajerska / Prekmurje** | 700–1,400 | 80,000–180,000 |

### 2025 reform — posplošena vrednost (MAJOR)

- **13 May 2025**: new regulation on property valuation models in force
- **June 2025**: property owners receive new generalized values by mail
- Total Slovenian property value: **€298 billion** (2025 GURS aggregate)
- Average **+8% increase** vs 2020 values
  - Apartments: +64% (2019-2024)
  - Houses: +54% (2019-2024)
  - Building land: +74% (2019-2024)
- Sets the base for any future davek na nepremičnine

### Compute

1. €/m² = price / **uporabna površina** (usable area)
2. **Posplošena vrednost** ≠ market value (typically lower, conservative)
3. **Etažna lastnina**: read **Pogodba o medsebojnih razmerjih** + **Zapisniki zborov etažnih lastnikov** + **Rezervni sklad** before buying flat

### Key terms

- Stanovanje = apartment
- Hiša = house
- Posplošena vrednost = generalized (mass-appraised) value — used for property tax base
- ETN = real estate market evidence
- Etažna lastnina = condominium ownership
- Zemljiška knjiga = land register

---

## Section: `--traffic`

### Sources

- **DRSI (Direkcija RS za infrastrukturo)**: `https://www.gov.si/drzavni-organi/organi-v-sestavi/direkcija-za-infrastrukturo/`
- **DARS** (motorway operator): `https://www.dars.si/`
- **Promet.si**: `https://www.promet.si/`

### Key term

**PLDP (Povprečni letni dnevni promet)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (občinska cesta, residential)
- 🟡 1,500–10,000 v/d (državna cesta, regional route)
- 🟠 10,000–30,000 v/d (urban arterial, državna I.)
- 🔴 > 30,000 v/d (avtocesta, hitra cesta, Ljubljana ring)

---

## Section: `--tax`

### Annual property tax (status uncertain — REFORM PENDING)

- **NUSZ (Nadomestilo za uporabo stavbnega zemljišča)** — compensation for use of building land — currently the main municipal property charge
  - Set per občina via odlok (ordinance)
  - Typical residential: **€100–€600/yr**
- **Davek na nepremičnine** (proper property tax): repeatedly proposed since 2013

### Davek na nepremičnine reform 2025-2026 (PENDING)

- 2025 posplošena vrednost reform sets the base
- **Government izhodišča (23 Dec 2024)**: **1.45%** of the GURS posplošena vrednost on residential property, the first home the owner actually lives in fully exempt (MF gov.si, 2024-12-23) — **NOT ENACTED**, it never advanced past the izhodišča
- **Status**: no law; MF collected responses to 25 Jan 2025 and no successor bill was found in the sources read on 2026-09-24 (FURS page refreshed 29 Dec 2025; a secondary 8 Sep 2026 report says the proposal never became law); the 16th Government (appointed 4 Jun 2026) has not been shown to revive it — re-verify at MF gov.si before quoting a rate
- **No implementation date**: no enacted law
- Strateški svet bo pregledal pripombe — review of comments + draft law expected

### Transaction taxes

- **Davek na promet nepremičnin (DPN)**: **2%** of price (paid by seller, but often passed to buyer in practice)
- **DDV (VAT)**:
  - 9.5% reduced (residential new builds)
  - 22% standard (commercial)
- **Notar fees**: ~1.0–1.5%
- **Realtor commission**: market-rate 3–4% still typical. The 4% cap under ZNPosr Article 5 was **annulled by the Constitutional Court in 2025** (following CJEU ruling on EU Services Directive 2006/123/EC) — paragraphs 1, 2, 6, 7 of Art. 5 and parts of 4, 5 struck; only the para-3 rule remains (no charging the non-engaging party). Verify in mandate contract. (2026-05-27 verified, source pfp.law / iusinfo.si)

### Total transaction cost (buyer side)

- **From seller side**: 2% DPN + 4% realtor (often shifted)
- **Buyer side direct**: ~1.5–2.5% (notar + zemljiška knjiga + sodne takse)

### Capital gains

- Reduced over time (held by individual; 2025 data, source PwC + FURS, 2026-05-27 verified):
  - **0–5 yrs ownership**: 25%
  - **5–10 yrs**: 20%
  - **10–15 yrs**: 15%
  - **>15 yrs**: 0% (exempt — no further brackets)
- **Primary residence**: exempt if continuous declared **permanent residence** for >3 years (verify with FURS)
- **Pre-2002 acquisition**: total exemption
- **Inheritance + gifting**: separate tax tariff

### Future risk

- **Davek na nepremičnine**: NOT ENACTED — the Dec 2024 1.45% izhodišča never advanced (see above); any revival by the 16th Government is unverified
- **NUSZ stays**: MF stated the proposed tax would NOT have replaced NUSZ (it would have abolished only the ZDO davek od premoženja)
- **Posplošena vrednost** revaluation cycles

---

## Section: `--rental`

### Long-term residential

- Standard income tax on rental: 25% flat with 10% cost allowance (akontacija dohodnine)
- **Tenant protection moderate** (less strict than DE/AT)
- Standard contract: 1-3 yrs typical

### Short-let (kratkoročno oddajanje)

- **ZGos-1** (Zakon o gostinstvu) **adopted Oct 2025, in force 1 Jan 2026**. Day-count caps (60-day apartments in multi-unit buildings / 150-day single- or two-unit dwellings) were scheduled to apply **from 1 Jan 2027** plus 75% co-owner consent + adjacent-neighbour consent every 3 years.
- **2026-05-11**: National Assembly passed a **moratorium (intervencijski zakon) suspending ZGos-1 implementation in 2026** — 2027 day-caps effectively waived pending revised legislation. Legal vacuum on the day-cap regime as of 2026-05-27. (Source: zgsd.si + pfp.law)
- **Ljubljana** strict (similar to Praha/Wien direction)
- **Sobodajalec** (short-let provider) licensing per občina
- **EU 2024/1028 transposition**: full application 20 May 2026 (national Single Digital Entry Point)
- **AVRSK + STO** (tourist board) registration

### Tax on rental

- 25% flat with 10% cost allowance, OR
- Cedolare-style 25% final tax (no further deduction)
- **Sobodajalec status**: VAT applies above €50,000 turnover

---

## Section: `--work=<profession>`

### Sources

- **Zavod RS za zaposlovanje (ZRSZ)**: `https://www.ess.gov.si/`
- **MojeDelo.com**, **Optius.com**
- **LinkedIn SI**

### Self-employment

- **S.P. (samostojni podjetnik)** = sole trader
  - **Pavšalna obdavčitev** (normirani s.p. / flat-tax option): from 1 Jan 2026, full-time threshold raised to **€120,000 revenue** (part-time €50,000); progressive tax 20% on tax base ≤ €72,000 (= revenue ≤ €120,000) + **35% above**. Exit if 2025 revenue >€60,000 full-time / >€30,000 part-time. (2026-05-27 verified, source Pravni SOS + FURS)
  - Mandatory ZZZS (health) + ZPIZ (pension) contributions
- **D.O.O.** (limited): min **€7,500 capital**

### Salary benchmarks (2025)

- Median monthly gross:
  - Ljubljana: ~€2,400–€3,200
  - Maribor / Celje: ~€1,900–€2,500
  - Smaller cities: ~€1,700–€2,200
- **Minimalna plača** (minimum wage): **€1,277.72 gross (2025)** → **€1,481.88 gross (2026)** (≈ €1,000 neto, effective 1 Jan 2026). (Source: Uradni list RS odločbe, 2026-05-27 verified)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **ARSO (Agencija RS za okolje)** | `https://www.arso.gov.si/` | Flood, climate, weather |
| **Atlas okolja** | `https://gis.arso.gov.si/atlasokolja/` | Environmental hazard maps |
| **GeoZS (Geološki zavod Slovenije)** | `https://www.geo-zs.si/` | Geology, **seismic, radon** |
| **URSZR (Uprava RS za zaščito in reševanje)** | `https://www.gov.si/drzavni-organi/organi-v-sestavi/uprava-za-zascito-in-resevanje/` | Civil protection |
| **Direkcija RS za vode (DRSV)** | `https://www.gov.si/drzavni-organi/organi-v-sestavi/direkcija-za-vode/` | Water management |

### Specific risks

- **Poplava (floods)**: Sava, Drava, Mura, Soča valleys; **August 2023 catastrophic floods** — major reform driver; **June 2014 ice storm + flood**; coastal Koper
- **Potresna ogroženost (seismic)**: among the higher seismic-hazard countries in Central Europe (verify against GeoZS national hazard map)
  - Posočje (Soča valley) M 5+ historical (**1998 M 5.6 + 2004 M 5.2 Bovec**)
  - **Ljubljana 1895 M 6.1** catastrophic
  - **Cona 1** (highest, PGA 0.250g): covers western SI (Posočje, Bovec, Tolmin)
  - **Cona 2** (PGA 0.175g): central SI incl. Ljubljana
  - **Cona 3** (PGA 0.125g): eastern SI
- **Plaz / zemeljski plaz** (landslides): widespread in Karavanke + Kamniško-Savinjske Alpe + flysch areas
  - **Stože plaz 2000** (7 dead near Log pod Mangartom)
- **Suša + požar** (drought + fire) increasing climate risk
- **Karst hazards**: **Mali Krasovi** (small karst formations) widespread; cave/sinkhole risk
- **Radon**: elevated in some karst + Pohorje + parts of Slovenia; not as severe as CZ/SK
  - **GeoZS radon map**: zoned per Eurocode/national survey
- **Klimatske spremembe**: est. +2.0–3.5 °C by 2050 (verify scenario + year against ARSO climate projections)

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1963 (pre-Skopje quake)** | Non-seismic standards — DANGEROUS in cona 1 |
| **1963–1981** | Improved seismic (post-Skopje reforms) |
| **1981–2008** | PBAB81 standards |
| **Post-2008 EC8** | Modern seismic |
| **Asbestos**: pre-1990 buildings likely |
| **PCB**: 1970s-1980s buildings |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **Energetska izkaznica (EI)** | Energy certificate, mandatory at sale + lease | 10 years |
| **Penalty for missing EI** | up to **€1,000** (FO) | n/a |
| **Zemljiškoknjižni izpisek** | Land register extract | At sale |
| **Posplošena vrednost notification** | Since May 2025 | Annual |
| **Pogodba** + **notarska overitev** | Contract + notary verification | At sale |

### Climate change projections

- est. +2.0–3.5 °C by 2050 (verify scenario + year against ARSO climate projections)
- Reduced summer precipitation, increased winter
- More extreme rainfall (August 2023 type)
- Adriatic coast sea-level rise
- Karst water-supply stress

---

## Section: `--mains`

### Sources

- **Komunalne službe** per občina (municipal services)
- **JP VOKA SNAGA** (Ljubljana water + wastewater operator, Javni holding Ljubljana; formerly Vodovod-Kanalizacija Ljubljana): `https://www.vokasnaga.si/` — drinking-water supply and wastewater, incl. public reporting under Uredba o pitni vodi (Ur. l. RS, št. 61/23) (2026-09-18 verified)
- **Mariborski vodovod** + regional public utilities
- Most občine have own komunala
- Universal in cities; rural Karst + Pohorje villages on greznica (cesspit)

### Verification

- Cities + most občine: javni vodovod + javna kanalizacija
- **Karst** villages (e.g., parts of Notranjska, Kras, Bela krajina): often on cesspit (greznica)
- **Mali sistemi za čiščenje odpadnih vod (MČN)**: small wastewater treatment plants for rural

### Costs

| Scenario | Cost (€) |
|---|---:|
| Priklop na javno kanalizacijo | 4,000–10,000 |
| MČN namestitev | 5,000–12,000 |
| Greznica reorganizacija | 3,000–8,000 |
| Vodovodni priključek | 1,500–4,500 |

---

## Cost benchmarks (SI 2026)

| Work | Cost (€) |
|---|---:|
| Energetska izkaznica | 150–400 |
| Notar | 1.0–1.5% of price |
| DPN (transfer tax) | 2% (often shifted from seller) |
| Realtor (capped) | up to 4% typical |
| Zemljiška knjiga + sodne takse | €100–€500 |
| **Total transaction cost (buyer)** | **~3–6%** (lower than EU avg) |
| Septik to mains | 4,000–10,000 |
| Roof (terracotta tile, 200 m²) | 15,000–25,000 |
| Energy retrofit (Class C → A) | 30,000–80,000 |
| Antiseismic retrofit (small house) | 25,000–60,000 |
| Asbestos removal | 1,500–8,000 |

## Active fiscal incentives (2025-2026)

- **Eko sklad** energy retrofit grants (heat pumps, insulation)
- **EKO sklad subvencije** for renovation, electric heating
- **Stanovanjski sklad RS** loans for first-time buyers
- **Subvencije za mlade** (young families) per občina
- **Subvencija za izgradnjo MČN** (small wastewater treatment)

## Common listing platforms

- **Nepremicnine.net** — biggest
- **Bolha.com** — secondary
- **Salomon.si**, **Slonep.net**
- Agency networks: Stoja Trade, Re/Max SI, TopRealitet, DODOMA

## Caveats unique to SI

- **Among the higher seismic-hazard countries in Central Europe** — cona 1 covers Posočje + Ljubljana cona 2; pre-1963 builds dangerous
- **Posplošena vrednost reform 2025** — new mass-appraised values effective 13 May 2025
- **Davek na nepremičnine NOT ENACTED** — the Dec 2024 1.45% izhodišča never advanced; NUSZ + ZDO davek od premoženja remain payable
- **EU 2007 currency** — no FX risk (vs CZ/PL/HU)
- **Adriatic coast (Koper-Piran)**: tourist premium + sea-level rise concern
- **Karst** specific construction issues — caves, sinkholes
- **Triglav National Park** strict construction limits
- **Mali Krasovi** (small karst formations) widespread; cave/sinkhole risk
- **Yugoslav-era apartment buildings** (1960s-1980s): variable seismic compliance
- **DPN paid by seller** (unusual in EU) — often shifted to buyer in negotiation
- **Realtor cap 4%** by ZNPosr law (one of strictest in EU)
- **Italian + Hungarian linguistic minorities** along borders — bilingual signage + listings
- **Bovec earthquakes 1998 + 2004** as recent reference events
- **August 2023 catastrophic flood** as recent reform driver
- **Brez davka na nepremičnine**: the 1.45% proposal was NOT enacted and would not have replaced NUSZ — NUSZ (municipal) + the ZDO davek od premoženja remain the charges
- **Etažna lastnina**: rezervni sklad (reserve fund) requirements

## Reddit / forum sources

- **r/Slovenia** (active, English-friendly)
- **Slo-Tech.com** forums
- **MojCG.com**, **Bolha.com** discussions
- **Slovenia Times** (English news)
- **Total Slovenia News** (English)

## Verification authorities

| Authority | When to call |
|---|---|
| **GURS** | Cadastre, posplošena vrednost |
| **Občina** | NUSZ, permits, planning |
| **e-Sodstvo Zemljiška knjiga** | Title verification |
| **FURS** | Tax calculations, capital gains |
| **ARSO** | Hazard zones, environmental |
| **GeoZS** | Seismic, radon, geology |
| **Notar** | Sale process |

## Source URL templates

| Source | URL pattern |
|---|---|
| GURS Javni vpogled | `https://ipi.eprostor.gov.si/jv/` |
| GURS Vrednotenje | `https://vrednotenje.gov.si/EV_JV/` |
| Zemljiška knjiga (e-Sodstvo) | `https://evlozisce.sodisce.si/esodstvo/index.html` |
| OPSI open data | `https://podatki.gov.si/` |
| ARSO Atlas okolja | `https://gis.arso.gov.si/atlasokolja/` |
| Nepremicnine.net | `https://www.nepremicnine.net/` |
| FURS (tax) | `https://www.fu.gov.si/` |
| GeoZS | `https://www.geo-zs.si/` |
| DRSI traffic | `https://www.gov.si/drzavni-organi/organi-v-sestavi/direkcija-za-infrastrukturo/` |
| URSZR (civil protection) | `https://www.gov.si/drzavni-organi/organi-v-sestavi/uprava-za-zascito-in-resevanje/` |

## Status

✅ **Fully populated** as of 2026-04-25 (Ljubljana water / wastewater operator re-identified as JP VOKA SNAGA 2026-09-18; the si:286 connection-cost figures were not re-verified). Tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).
**Coverage check**: pricing, traffic, tax (with the not-enacted 1.45% proposal note), rental, work, risks (incl. seismic cona zoning + August 2023 flood reference), mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for posplošena vrednost reform (Bloomberg Adria, Kalko, N24, MojMojster, alfaelmas all confirm 13 May 2025 effective + €298B aggregate + +8% average); HIGH for cadastre + GeoZS sources; MEDIUM for the NOT-ENACTED status of the davek na nepremičnine 1.45% proposal (izhodišča of 23 Dec 2024 never advanced; re-verify any successor plan at MF gov.si before output).

## Extension TODOs

- [ ] Per-občina NUSZ rates from odlok
- [ ] Posplošena vrednost extraction patterns (post-May 2025)
- [ ] Seismic cona overlay per parcela
- [ ] Karst hazard detection
- [ ] Triglav NP construction limits
- [ ] Coastal sea-level rise (Koper-Piran-Portorož)
- [ ] Italian-language listings (border zones)
- [ ] August 2023 flood-affected zones
- [ ] Davek na nepremičnine final rate tracking
- [ ] Etažna lastnina rezervni sklad health
