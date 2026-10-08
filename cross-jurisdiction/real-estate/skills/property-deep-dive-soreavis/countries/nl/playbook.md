# Netherlands 🇳🇱 — Property Due-Diligence Playbook

ISO2: `nl`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4 digits + 2 letters (`1011 AA` Amsterdam centrum, `3011 AA` Rotterdam, `2511 AA` Den Haag)
- **Admin levels**: 12 provincies + 342 gemeenten (post-2024 mergers)
- **Currency**: EUR (€)
- **Languages**: Dutch (official); Frisian (Fryslân, co-official)
- **Cadastre**: **Kadaster** — `https://www.kadaster.nl`
- **Identifier**: kadastrale aanduiding `<gemeente> <sectie> <perceel>` (e.g., `AMSTERDAM A 1234`)
- **Ownership types**:
  - **Eigendom** (freehold)
  - **Erfpacht** (leasehold ground) — Amsterdam ~80% of housing; Den Haag, Utrecht common
  - **VvE-aandeel** (share in homeowners' association for apartments)
  - **Mandeligheid** (shared ownership of common parts)
  - **Recht van opstal** (right to build on someone else's land)

## Section: `--price`

### Primary sources

- **Kadaster** (cadastre + transfer register): `https://www.kadaster.nl`
  - **Online inzage** for €2.95: title + price paid
  - **Kadastraal recht (cadastral right)**: 4-page extract for verified transfers
- **WOZ-waardeloket** (FREE WOZ value lookup): `https://www.wozwaardeloket.nl/`
  - Annual gemeente assessment; basis for OZB + Box 1 + Box 3
- **CBS (Centraal Bureau voor de Statistiek)**: `https://www.cbs.nl/` — house price index
- **NVM (Nederlandse Vereniging van Makelaars)**: `https://www.nvm.nl/` — quarterly market reports
- **De Nederlandsche Bank (DNB)** financial stability: `https://www.dnb.nl/`

### Listing platforms

- **Funda** — DOMINANT (~95% market share): `https://www.funda.nl`
  - Member of NVM/VBO/VastgoedPRO; near-universal coverage
  - URL: `https://www.funda.nl/koop/<location>/`
- **Pararius** — rentals focus: `https://www.pararius.com`
- **Jaap.nl**, **Huislijn.nl** — alternative aggregators
- **Direct-Wonen** — rentals
- Agency networks: **Era**, **Makelaarsland**, **DNGB**, **Remax NL**

### 2025 price benchmarks (NVM + CBS)

**2026 update**: CBS/Kadaster index shows prices still rising into 2026 at +4–5% YoY (Q1 2026 +5.2%, April +4.3%, May +4.4%), well off the ~10% pace of early 2025; ranges below remain plausible (2026-07-03 verified; source CBS nieuws 2026/21 + 2026/26)

| Region | Avg €/m² (apt) | Avg total (semi-detached) |
|---|---:|---:|
| **Amsterdam centrum** | 8,000–12,500+ | 800,000–1,800,000+ |
| **Amsterdam ring** | 6,000–9,500 | 700,000–1,200,000 |
| **Utrecht** | 5,500–8,000 | 600,000–950,000 |
| **Den Haag / Rotterdam** | 4,500–7,500 | 500,000–850,000 |
| **Eindhoven** | 4,000–6,000 | 400,000–700,000 |
| **Groningen / Maastricht** | 3,500–5,500 | 380,000–650,000 |
| **Smaller cities** | 3,000–4,500 | 320,000–500,000 |
| **Rural NL** | 2,500–4,000 | 280,000–450,000 |

### Compute

1. €/m² = price / **gebruiksoppervlakte (GO; usable area)** — NEN 2580 standard
2. **Erfpacht trap**: Amsterdam canon (lease ground rent) can be €0 (afgekocht) to €25,000+/yr — affects yield massively
3. **VvE check**: read **MJOP (Meerjarenonderhoudsplan)** + **vergaderingsverslagen** + **balans/winst-verlies** before buying flat
4. **WOZ vs market**: typically WOZ = 70–95% of market value (gemeente conservative)

### Key terms

- Eigendom = freehold
- Erfpacht = ground lease
- Canon = annual ground rent
- Afgekocht = ground rent paid off (capital sum)
- VvE = Vereniging van Eigenaren (homeowners' assoc)
- WOZ = Waardering Onroerende Zaken (property valuation)
- GO = gebruiksoppervlakte
- NHG = Nationale Hypotheek Garantie

---

## Section: `--traffic`

### Sources

- **Rijkswaterstaat** (national highways): `https://www.rijkswaterstaat.nl/`
- **NDW (Nationaal Dataportaal Wegverkeer)**: `https://www.ndw.nu`
- **Provincie wegen** for N-roads
- **Gemeente verkeer** for local roads

### Key term

**Etmaalintensiteit** = AADT-equivalent (vehicles/day, both directions).

### Verdict bands

- 🟢 < 1,000 v/d (woonstraat, residential)
- 🟡 1,000–10,000 v/d (gemeentelijke ontsluitingsweg)
- 🟠 10,000–35,000 v/d (provinciale weg, urban arterial)
- 🔴 > 35,000 v/d (snelweg, A-road, ringweg)

---

## Section: `--tax`

### Annual property tax — OZB (Onroerendezaakbelasting)

- Set per gemeente; rate × WOZ
- Typical rates: **est. 0.05–0.15%** of WOZ (varies per gemeente; verify at gemeente OZB)
- 2025-2026 typical: €300–€2,000/yr depending on WOZ + gemeente
- Owners + users (commercial) tax separately
- Plus **rioolheffing** (sewerage) + **afvalstoffenheffing** (waste) + **waterschapsbelasting** (water board)

### Box 1 — Eigenwoningforfait (imputed income)

For primary residence:
- **0.35% of WOZ** (2025-2026, sliding bracket)
- Added to taxable income
- Mortgage interest deductible (max **37.56%** aftrektarief, 2026; capped) (2026-07-03 verified)
- **Hillen aftrek** phase-out (full phase-out by 2048)

### Box 3 — Vermogensrendementsheffing (savings + investment tax)

**MAJOR REFORM in progress**:
- **2026 forfaitair rendement (deemed yield)**:
  - Bank deposits: **1.28%**
  - Other assets (incl. property, stocks): **6.00%** (down from 7.78% 2025)
  - Debts: 2.70%
- Tax rate: **36%** of deemed return
- Tax-free allowance: **€59,357 per fiscal partner** (2026)
- Real return option: can use **werkelijk rendement** if lower
- **Wet werkelijk rendement Box 3** (wetsvoorstel 36.748): permanent actual-return capital tax replacing the notional-yield system — **vermogensaanwas** as the main rule, **vermogenswinst taxed on realisation for real estate** (and start-up shares), with rent + dividend taxed in the year received. Passed Tweede Kamer (lower house) 12 Feb 2026; statutory reference date for entry into force is still **1 Jan 2028**, but commencement is by **koninklijk besluit**. ⚠️ **STALLED IN THE EERSTE KAMER (Senate) as of 7 Aug 2026** — plenary debate held 30 Jun 2026, after which a Senate majority (ordevoorstel-Crone, GroenLinks-PvdA) resolved to **SUSPEND the final vote** until the cabinet's announced **novelle** is treated; no Senate vote on the bill has been held. The motie-Schalk c.s. (no overriding objection if the government itself withdrew the bill) was **REJECTED 7 Jul 2026** (verworpen bij zitten en opstaan), so withdrawal was not endorsed either. The 1 Jan 2028 start is **NOT secured** — do not treat actual-return taxation as live before the Senate has voted on both the novelle and this bill. **Prinsjesdag 15 Sep 2026: the Belastingplan 2027 bill and its memorie van toelichting contain no Box 3 measure, and no novelle to 36.748 has been introduced**; the Finance ministers' letter of 14 Sep 2026 (EK 36.748, Q) says no adjustment proposal with broad parliamentary support can yet be reached, asks the Senate to keep holding the bill and lists four scenarios, one of which is withdrawing it (forfaitaire system with tegenbewijsregeling kept longer, full vermogenswinstbelasting in 2030); the Senate Finance committee discussed the letter 22 Sep 2026 and decided to invite the ministers for a mondeling overleg after the Tweede Kamer's Algemene Financiële Beschouwingen ([Eerste Kamer — brief 14 Sep 2026, EK 36.748 Q](https://www.eerstekamer.nl/behandeling/20260914/brief_van_de_minister_en/meta)); the rijksoverheid.nl Box 3 theme page (undated) says the bill "blijft de basis voor box 3 vanaf 2028" while a vermogenswinstbelasting is studied (2026-09-17 verified — motie-Schalk outcome per [Eerste Kamer moties bij 36.748](https://www.eerstekamer.nl/moties_bij?key=vmnm2y9y4oyv); sources [Belastingdienst — what is my actual return](https://www.belastingdienst.nl/wps/wcm/connect/en/income-in-box-3/content/what-is-my-actual-return) + [Eerste Kamer 30 Jun 2026 — Senaat houdt stemming Box 3-wet](https://www.eerstekamer.nl/nieuws/20260630/senaat_houdt_stemming_box_3_wet) + Deloitte NL for the 12 Feb 2026 Tweede Kamer adoption)

### Transaction taxes — Overdrachtsbelasting

- **Primary residence (owner-occupier)**: **2%**
- **First-time buyer < €555,000 (2026)**: **0%** (jonge starter, 18-35 yrs; was €525k 2025, €510k 2024) (2026-05-27 verified; source [business.gov.nl Property transfer tax](https://business.gov.nl/regulation/property-transfer-tax/))
- **Second home / BTL / investor**: **8%** from 1 Jan 2026 (Belastingplan 2026; was 10.4% in 2023-2025) (2026-05-27 verified; source [government.nl real-estate-transfer-tax-rates](https://business.gov.nl/regulations/property-transfer-tax/))
- **Commercial**: 10.4%
- Calculated on contract price

### Notaris fees + Kadaster

- **Notaris**: ~€1,500–€3,000 (transfer + mortgage deeds)
- **Kadaster registration**: ~€140 (per deed)
- **Makelaar** (buyer-side, optional): ~1–2% (or fixed fee)

### Total transaction cost (buyer side)

- **First-time buyer < €555,000 (2026)**: **~1–2%** (no transfer tax + notaris + makelaar)
- **Mover, primary**: **~3–4%** (2% transfer + ~1–2% other)
- **Second home / BTL**: **~10–11%** (8% transfer from 1 Jan 2026 + others)

### Capital gains

- **Primary residence**: NO capital gains tax (still applies; no separate CGT; only Box 1 forfait while owned)
- **Investment property**: taxed in Box 3 (deemed return)

### VAT (BTW)

- Standard 21%
- New build: **21% BTW** included in price (developer pays)
- Existing: BTW-exempt (only overdrachtsbelasting)

### Future risk

- **Wet werkelijk rendement Box 3** (targeted 1 Jan 2028 — **NOT secured**; final Eerste Kamer vote suspended pending the cabinet's novelle; no novelle introduced as of 17 Sep 2026, the Belastingplan 2027 bill carries no Box 3 measure, and the cabinet's 14 Sep 2026 letter (EK 36.748, Q) asks the Senate to keep holding the bill while listing withdrawal plus a full vermogenswinstbelasting in 2030 as one of four scenarios; 2026-09-17 verified): real return basis, with vermogenswinst on real estate taxed on realisation — major change for landlords + investors
- **OZB** rising annually
- **Eigenwoningforfait** continues to phase ratchet
- **Box 3** for second homes likely tighter post-2028

---

## Section: `--rental`

### Long-term residential

- **Liberalisatiegrens** (free-market / mid-segment ceiling): **€1,228.07/mo (2026)** = max rent at 186 WWS points; 187+ points or start-rent above it = vrije sector (indexed annually, +3.65% for 2026; was €1,184.82 in 2025 — the grens at contract start governs, not today's) (2026-07-03 verified; source [Volkshuisvesting Nederland maximale huurprijsgrenzen](https://www.volkshuisvestingnederland.nl/onderwerpen/huren-en-wonen/inkomensgrenzen-huurprijsgrenzen-en-huurtoeslagparameters/maximale-huurprijsgrenzen))
- **WWS (Woningwaarderingsstelsel)**: points system for sociale huur (regulated)
- **Wet betaalbare huur** (Affordable Rent Act, 1 Jul 2024): regulated mid-market segment now up to **€1,228.07/mo (2026)** = 186 WWS points; social ≤ **€932.93** (≤143 pts); free sector 187+ pts (2026-07-03 verified)
- **Tenant rights strict**:
  - Indefinite contracts default
  - Limited notice for landlord
  - Rent increases capped: vrije sector **max 4.4% (2026)** = lower of inflation/CAO-wage +1%; middenhuur **6.1% (2026)** = CAO-wage +1%; sociale huur **4.1%** (from 1 Jul 2026) (2026-07-03 verified)
- **Tijdelijke huur** (temporary): Wet Doorstroming Huurmarkt — 2-year fixed; **abolished 1 Jul 2024** for new contracts (Wet vaste huurcontracten)

### Short-let (Airbnb / vakantieverhuur)

**Per-gemeente regimes**:
- **Amsterdam**: 30 nights/year citywide primary-residence cap, but **15 nights/year since 1 Apr 2026** in 8 designated wijken (7 in Centrum — Burgwallen-Nieuwe Zijde, De Weteringschans, Grachtengordel-West/Zuid, Haarlemmerbuurt, Jordaan, Nieuwmarkt/Lastage — plus Oude Pijp in Zuid) under the **Eerste aanwijzingsbesluit 15-nachtencriterium**; **registratie + meldplicht + vergunning** required; max 4 guests; full ban possible in a wijk if the halving is insufficient (2026-07-02 verified; source [Gemeenteblad 2026 nr.151001](https://zoek.officielebekendmakingen.nl/gmb-2026-151001.html))
- **Rotterdam**: 60 nights; registratie required
- **Den Haag**: 60 nights; registratie required
- **Utrecht**: 60 nights; registratie required (since 2023)
- **Other gemeenten**: variable; many require **logiesvergunning**
- **Bestemmingsplan** (zoning) often requires "wonen" use — short-let may breach

### Tax on rental

- **Long-term rental of own apartment**: Box 1 if leased (uncommon) or Box 3 (capital tax)
- **Short-let primary**: typically Box 3 + income from Airbnb
- **B&B regime**: separate (commercial use)

---

## Section: `--work=<profession>`

### Sources

- **Werk.nl** (UWV): `https://www.werk.nl/`
- **Indeed.nl**, **LinkedIn NL**, **Nationale Vacaturebank**, **Monsterboard**
- **NVB (Nederlandse Vacaturebank)**

### Self-employment

- **ZZP (zelfstandige zonder personeel)**: most common self-employment form
- **KvK (Kamer van Koophandel)** registration mandatory
- **BTW** (VAT): from €20,000 turnover (kleineondernemersregeling)
- **Inkomstenbelasting**: progressive 36.97% / 49.5% (2025)
- **Zelfstandigenaftrek**: phasing down to €900 (2027)
- **MKB-winstvrijstelling**: 12.7% deduction
- **30%-ruling** for expat workers: duration remains **60 months (5 years)** throughout. Tapering 30/20/10 introduced for 2024 is being **repealed and replaced by a flat 27% for the full 60 months from 1 Jan 2027** (raised salary norms **€50,436 / €38,338** for <30 with master's — both at 2024 price level, indexed annually before 2027) (2026-07-03 verified; source Belastingplan 2025 tweede nota van wijziging, Kamerstuk 36602 — NB the previously cited business.gov.nl/ondernemersplein portal pages show €38,388 for the under-30 norm; the legislative text says €38,338 (superseded))

### Salary benchmarks (2025)

- Median annual gross:
  - Amsterdam: ~€55,000–€75,000
  - Randstad: ~€48,000–€65,000
  - Smaller cities: ~€42,000–€55,000

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Risicokaart** | `https://www.risicokaart.nl` | Provincial hazard layer aggregator |
| **Klimaateffectatlas** | `https://www.klimaateffectatlas.nl/` | Climate change projections per gemeente |
| **Atlas Leefomgeving** | `https://www.atlasleefomgeving.nl/` | Environmental quality |
| **Waterschap (water board)** | per region | Flood maps, dike inspection |
| **TNO** | `https://www.tno.nl/` | Subsidence, geology |
| **KNMI** | `https://www.knmi.nl/` | Climate, weather |
| **RIVM** | `https://www.rivm.nl/` | Air quality, radon |
| **NCG (Nationaal Coördinator Groningen)** | `https://www.nationaalcoordinatorgroningen.nl/` | Groningen earthquake monitoring |

### Specific risks

- **Wateroverlast + dijkdoorbraak (flooding + dyke breach)** — major existential risk:
  - 60% of NL below sea level or vulnerable to river flooding
  - **Hoogwaterbeschermingsprogramma** (HWBP) — €30B dyke upgrade programme
  - Major flood reference: 1953 Watersnoodramp (1,836 deaths)
- **Bodemdaling (subsidence)** — peat areas:
  - Holland, Frisia, Brabant peat lowlands
  - Oxidation of peat = 0.5–1.5 cm/yr subsidence
  - **Funderingsproblematiek** (foundation rot) — wooden pile foundations affected
- **Groningen aardbevingen (induced earthquakes)**:
  - Gas-extraction induced; production wound down 2023-2024
  - Affected areas: 200,000+ properties damaged
  - **NCG damage compensation programme** ongoing
- **Zeespiegelstijging (sea-level rise)**:
  - +20–80 cm by 2100 (KNMI 2023 scenarios)
  - High RCP 8.5: +1.2m by 2100
- **Klimaatadaptatie** mandatory per gemeente
- **Asbestos** — banned 1994; older buildings extensively contaminated
- **Loodleidingen** (lead pipes) — pre-1960 buildings

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | Wooden pile foundations (peat areas), no DPC, lead, asbestos cement starts |
| **1920s–1940s** | Lead pipes, asbestos, weak foundations |
| **1945–1970s** | Funderingsproblematiek (peat areas), asbestos very common |
| **1970s–1990s** | Asbestos in roofing/walls, energy-inefficient |
| **1990s+** | Energy improvements; asbestos-free post-1994 |
| **Post-2010 BENG** | Bijna Energieneutrale Gebouwen — strict energy standard |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **Energielabel** (energy label) | All sales since 2015 | 10 years |
| **Bouwkundig keuring** (construction survey) | Recommended; not mandatory | Per case |
| **VvE-stukken** (HOA documents) | If apartment | At sale |
| **Splitsingsakte** (condominium deed) | If apartment | At sale |

### Climate change projections (KNMI 2023)

- +1.2–4.2 °C by 2100
- Sea-level rise: +20–120 cm by 2100
- Precipitation +30% winter, -30% summer
- More extreme heat events
- Increased flood + drought risk

---

## Section: `--mains`

### Sources

- **Waterschap** + gemeente — sewer plans
- Universal in urban areas
- **IBA (individuele behandeling afvalwater)** systems in rural Frisia, Drenthe, Zeeland

### Verification

- Most populated areas: gemeentelijk riool universal
- Rural NL (esp. Friesland, Drenthe): often **IBA klasse 1-3**
- Buitengebied: ask gemeente riolering department for **gebiedsgerichte aanpak**

### Costs

| Scenario | Cost (€) |
|---|---:|
| Aansluiting op riool | 5,000–15,000 |
| IBA klasse 1 installatie | 5,000–8,000 |
| IBA klasse 3 installatie | 12,000–20,000 |
| Funderingsherstel (foundation repair, peat areas) | 40,000–100,000+ |

---

## Cost benchmarks (NL 2026)

| Work | Cost (€) |
|---|---:|
| Energielabel | 200–400 |
| Bouwkundig keuring | 400–800 |
| Notaris (transport + hypotheek) | 1,500–3,000 |
| Kadaster fees | 140–500 |
| Makelaar (buyer, optional) | 1–2% |
| **Overdrachtsbelasting (FTB <€555k, 2026)** | **0%** |
| **Overdrachtsbelasting (eigen woning)** | **2%** |
| **Overdrachtsbelasting (2nd home/BTL, 2026)** | **8%** |
| **Total transaction cost (FTB)** | **~1–2%** |
| **Total transaction cost (mover)** | **~3–4%** |
| **Total transaction cost (BTL/2nd home)** | **~10–11%** |
| Asbestos removal | 1,000–10,000 |
| Funderingsherstel | 40,000–100,000+ |
| IBA installatie | 5,000–20,000 |
| Energy upgrade C → A | 30,000–70,000 |
| Dakvervanging | 15,000–35,000 |
| Riothering | 5,000–15,000 |

## Active fiscal incentives (2025-2026)

- **NHG (Nationale Hypotheek Garantie)**: cap **€470,000** (2026; €498,200 with energy-saving uplift; was €450k 2025); fee 0.4% of mortgage (2026-05-27 verified; source [Rijksoverheid NHG 2026](https://www.volkshuisvestingnederland.nl/actueel/nieuws/2025/10/08/nhg-grens-stijgt-naar-470.000-euro-afsluitpremie-blijft-04))
- **Starterslening** (gemeente top-up loans for FTB)
- **Energiesubsidie ISDE**: heat pumps, insulation
- **30% ruling** for expat workers (60 months / 5 years; tapering repealed, flat 27% for full 60 months from 1 Jan 2027 — see `--work`)
- **Box 3 vrijstelling**: green investments, social housing

## Common listing platforms

- **Funda** — DOMINANT, ~95% coverage
- **Pararius** — rentals
- **Jaap.nl**, **Huislijn.nl** — alternatives
- Agency networks: NVM/VBO members

## Caveats unique to NL

- **Overdrachtsbelasting 8% second home/BTL** (from 1 Jan 2026; was 10.4% in 2023-2025 — see `--tax`) — punitive on investor purchases
- **Erfpacht** (ground lease) — Amsterdam ~80% of housing; Den Haag, Utrecht common
  - Canon (annual ground rent) can be €0 (afgekocht) to €25,000+/yr
  - **AB2016 reform** (Amsterdam) lets owners switch from voortdurend to eeuwigdurend (perpetual buyout)
- **VvE health checks** mandatory pre-purchase (apartment): MJOP, vergaderingsverslagen, balans/winst-verlies, **achterstallige bijdragen**
- **Funderingsproblematiek** in peat / clay areas — wooden pile foundation rot
  - KCAF (Kennis Centrum Aanpak Funderingsproblematiek): public knowledge
  - Cost: €40k–€100k+ per house
- **Energielabel C** required for office space; tightening for residential rental
- **Wet werkelijk rendement Box 3 (targeted 2028 — NOT secured)** — major Box 3 reform; passed Tweede Kamer 12 Feb 2026 but stalled in the Eerste Kamer, final vote suspended pending the cabinet's novelle, not introduced as of 17 Sep 2026 — the 15 Sep 2026 Belastingplan 2027 bill carries no Box 3 measure, and the cabinet's 14 Sep 2026 letter (EK 36.748, Q) lists withdrawing the bill (full vermogenswinstbelasting in 2030) as one of four scenarios (2026-09-17 verified — see `--tax`)
- **Wet betaalbare huur (1 Jul 2024)** — regulated mid-market up to 186 WWS points (**€1,228.07/mo**, 2026)
- **Tijdelijke huur abolished** (1 Jul 2024) — flexible tenancy ending
- **NHG cap €470,000 (2026)** — entry-level affordability (see `--tax` incentives)
- **30% ruling** — duration remains 5 years (60 months); tapering repealed, flat 27% for full 60 months from 1 Jan 2027 (see `--work`)
- **Groningen** earthquake compensation programme — affects northern provinces specifically
- **Climate adaptation** mandatory per gemeente — affects new build constraints
- **Watersnoodramp** memory (1953) shapes flood policy

## Reddit / forum sources

- **r/Netherlands**, **r/thenetherlands** (English)
- **r/Amsterdam**, **r/AskNetherlands**
- **r/PersonalFinanceNL** — Box 3 + tax discussion
- **Tweakers Forum** — VvE + technical
- Expat: **IamExpat NL**, **DutchNews.nl**

## Verification authorities

| Authority | When to call |
|---|---|
| **Kadaster** | Title verification, transfer history |
| **Gemeente Bouw- en Woningtoezicht** | Permits, planning history |
| **Gemeente OZB** | Tax band, exemptions |
| **Belastingdienst** | Box 1/3, transfer tax, capital gains |
| **Waterschap** | Drainage, dyke inspection |
| **VvE-bestuur** | If apartment: financials, MJOP |
| **NCG** | Groningen earthquake damage |

## Source URL templates

| Source | URL pattern |
|---|---|
| Kadaster online inzage | `https://www.kadaster.nl/` |
| WOZ-waardeloket | `https://www.wozwaardeloket.nl/` |
| Funda | `https://www.funda.nl/koop/<gemeente>/` |
| Risicokaart | `https://www.risicokaart.nl` |
| Klimaateffectatlas | `https://www.klimaateffectatlas.nl/` |
| Belastingdienst Box 3 | `https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/` |
| Energielabel register | `https://www.ep-online.nl/` |
| NDW traffic | `https://www.ndw.nu/` |
| RIVM | `https://www.rivm.nl/` |
| KNMI | `https://www.knmi.nl/` |

## Status

✅ **Fully populated** (initially populated 2026-04-25); **Last verified**: 2026-09-17 (Box 3 re-verified after Prinsjesdag — the Belastingplan 2027 bill carries no Box 3 measure and no novelle has been introduced, 1 Jan 2028 still not secured; previous stamp 2026-08-07; balance of the 2026-07-03 Tier-A quarterly refresh unchanged). Rental / tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early — Box 3 file 36.748: cabinet letter 14 Sep 2026 (EK Q) asks the Senate to keep holding the bill and lists withdrawal as one of four scenarios; Senate Finance committee set a mondeling overleg on 22 Sep 2026; see shared/regulatory-watch.md).
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for Box 3 2026 rates (Belastingdienst + Van Lanschot + Deloitte confirm), HIGH for transfer tax (Belastingdienst), HIGH for Wet werkelijk rendement status (passed Tweede Kamer 12 Feb 2026; STALLED in the Eerste Kamer — final vote suspended 30 Jun 2026 pending the cabinet's novelle) but LOW for its 1 Jan 2028 start date (not secured; commencement by koninklijk besluit), HIGH for Wet betaalbare huur (1 Jul 2024 effective). MEDIUM for per-gemeente short-let licensing (rules change frequently).

## Extension TODOs

- [ ] Per-gemeente OZB rates table
- [ ] Per-gemeente B&B / short-let rules (Amsterdam 30 (15 in 8 designated wijken since 1 Apr 2026), Rotterdam/DH/Utrecht 60)
- [ ] Erfpacht canon calculation (Amsterdam AB2016)
- [ ] VvE health check rubric (MJOP, achterstallige bijdragen, reservefonds)
- [ ] Funderingsproblematiek triggers per peat area
- [ ] Box 3 werkelijk rendement transition (2028)
- [ ] Groningen earthquake compensation eligibility
- [ ] Klimaatadaptatie zoning impact per gemeente
- [ ] NHG eligibility decision tree
- [ ] 30% ruling expat eligibility decision tree
