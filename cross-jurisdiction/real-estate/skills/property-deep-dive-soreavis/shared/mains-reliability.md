# Universal `--mains` Section — Utilities Reliability Extension

Grid reliability + outage profile + load-shedding regime + 2024-2026 reform calendar + water-supply reliability for the property's country. Loaded when `--mains` is invoked alongside the per-country sewer/drain connection logic in each country playbook.

**Snapshot**: May 2026.

**Scope**: this doc supplies the *reliability* layer — how often the grid goes down, for how long, under what regime, and what reforms are imminent. The *connection* layer (which utilities exist, how to verify a parcel is connected, septic-vs-sewer thresholds) lives in each country's playbook `--mains` section.

## Universal contract

For the property's country, return:

1. **Grid type** (synchronous bloc + island/peninsula status + interconnections)
2. **SAIDI / SAIFI** (latest year-stamped figures from the national regulator) — or `data not publicly available — verify at <regulator URL>` if not published
3. **Outage band**: 🟢 <30 min/yr · 🟡 30-200 min/yr · 🟠 200-500 min/yr · 🔴 >500 min/yr (stage protocol if formalised)
4. **Load-shedding regime**: none / rare / scheduled / frequent / failed-grid (with hours/day if applicable)
5. **Notable 2024-2026 events** (blackouts, capacity warnings, court cases naming the grid operator)
6. **Reliability reforms 2024-2026** (capacity-market reform, unbundling, grid-code changes, transposition deadlines)
7. **Tariff reform recent** (rate hikes / cuts, banded structures introduced, subsidy phase-outs)
8. **Water reliability** (drought rationing, desalination dependency, groundwater stress — only if it materially differs from electricity)
9. **Confidence**: HIGH / MEDIUM / LOW per the skill's contract

## Reliability tier bands

| Band | SAIDI | Markets |
|---|---|---|
| 🟢 World top-tier | <30 min/yr | SG (0.26 min) · HK (CLP 6 / HK Electric <0.5) · MO (~2) · KR (<10) · DE (11.7, 2024) · DK (27, 2024) · QA · NL · UAE (DEWA CML 0.94 min) · TW (15.225, 2023) · CH |
| 🟡 Strong / EU-mainstream | 30-200 min/yr | UK (39.71 min, 2024/25) · AT (40.75) · FR (71.6, 2024 — climate-event regression) · IT mainland · BE Flanders/Brussels · IE · ES (pre-blackout) · PT (pre-blackout) · MX urban · BR mainland · UY · MU · SC · NO · SE · FI · IS (calm year) · JP (~36 min FY22 ex-Noto) · LU · MT · LV · LT · EE (calm year) · PL · CZ · SK · HU · SI · GE · AM · AZ |
| 🟠 Strain / managed | 200-500 min/yr | RO · HR · BG · RS · ME (8.87h CEDIS 2024) · MK · TR rural · IL post-Oct-2023 · CY · MA · EG (2024 summer) · CN western provinces · IN rural states · LK 2024-25 post-crisis · KZ · UZ · TN · KE rural · ZA pre-2026 · DR (EDESUR/EDENORTE) · CL urban + rural · PA |
| 🔴 Failed / crisis | >500 min/yr or daily scheduled | LB (~4 hr/day from EDL — failed grid) · NG (12+ grid collapses 2024-2025) · GH (dumsor return 2024) · EC (up to 14 hr/day Sep 2024-Apr 2025) · CO (Apr 2024 hydro near-blackout) · ES/PT for 2025 (28 Apr 2025 Iberian blackout, ~10 hr) · IS storm year (510 min Hokuriku) · KH (chronic dry-season) · MV outer islands · BS Family Islands (Abaco 17h Dec 2025) · JM (2,403 min 2023 + Hurricane Melissa Oct 2025) · BZ during CFE curtailments · PY (Feb 2026 1.4 M dark) · CR May 2024 (drought-driven, ended) · VN north summer 2023 · IN + ID rural states |

## ⚠️ 7 cross-cutting traps

1. **SAIDI excludes rare extreme events in some methodologies** — Spain/Portugal use TIEPI/NIEPI not SAIDI; FR Enedis distinguishes "criteria B" (incl. exceptional) from "criteria A"; Italian ARERA varies by zone. Comparing raw numbers across countries can mislead — check methodology.
2. **Island grids = single-point-of-failure tail risk** — IS (2 Oct 2024 storm), TW (Apr 2024 near-blackout, 3% reserve), CY, MT, MV outer islands, BS Family Islands, BZ (CFE-import dependency). Top-tier reliability in most years masks catastrophic-event risk.
3. **Synchronous decoupling reshapes everything** — Baltic states (EE/LV/LT) desynchronised from BRELL 8 Feb 2025 + synchronised with Continental EU 9 Feb 2025; SAIDI improved sharply (EE 142 min 2024 vs 453 min 2023). Equally, Iberian peninsula's weak FR-ES tie (~5% peak) caused 28 Apr 2025 ~10 hr blackout. Grid topology > generation mix when crisis hits.
4. **Hydro-dependency = drought-correlated outage risk** — EC (78% hydro), CO (87% normal → 47% Apr 2024), CR (99% normal → 86% Q2 2024 drought), BR (worst-recorded 2024 drought), AL (98% hydro), CN-Sichuan (2022 anchor), VN-north summer. A "🟢 in normal year" rating can flip 🔴 in a drought year.
5. **Tariff capping = silent outage subsidy** — HU rezsicsökkentés, AR Decree 55/2023 emergency subsidies, EG freeze through Jun 2026, KZ multi-year cap 2026-2032: when residential tariffs are political, utilities defer capex, outages worsen 2-3 years later. Look for tariff-vs-CPI gap.
6. **Water-shedding shadows load-shedding** — ZA Gauteng water-shedding parallel to Eskom load-shedding since 2022; LB Litani 2024-25 inflows -80% vs avg + EDL collapse; MA 7th drought year + electricity reliability OK; ES Catalonia + Andalusia drought emergencies through 2024; RO ANAR rationed 449 localities 2024; BG 5.8% population on rationing 2024 (Pleven 51%, Lovech 56%). Foreign buyers should NOT assume "electricity reliability OK = water OK".
7. **Tariff bands ≠ service-hour bands ≠ outage bands** — NG Apr 2024 introduced Bands A (20+ hr/day promised) / B (16) / C (12) / D (8) / E (4). 9 DisCos ordered to compensate Band A customers Apr 2025 for failing the 20-hr commitment. The marketed band is the price tier; the delivered hours are a separate question. Same applies to Caribbean utilities (BPL Family Islands, JPS Jamaica).

## Regional patterns

### Western Europe + microstates

Synchronous Continental Europe + Nordic + GB-island + IS-island + IE All-Island. Tier-1 reliability: DE (11.7 min 2024), DK (27, 2024), CH, NL, AT, NO transmission. Tier-2: FR (71.6 min 2024 — climate regression), UK (39.71), IE, IT mainland.

**Defining 2024-2026 events**:

- **28 Apr 2025 Iberian peninsula blackout** — voltage-control failure + Granada substation transformer overvoltage trip; 56M+ people, ~10 hr typical recovery (up to 20 hr in some islands and zones); >€1.6 bn estimated economic loss. ENTSO-E expert panel final report 20 Mar 2026 attributed root cause to systemic voltage control + reactive power gaps; renewables share NOT root cause.
- **NL grid congestion crisis** — TenneT 38 GW waitlist Q1 2025; new kWmaxweighted tariff Jan 2025; redispatch obligation ≥60 MW.
- **DE Redispatch reform** — €2.2 bn grid-management costs Q1-3 2025; AgNes process mid-2026; new fee regime from 1 Jan 2029.
- **UK NESO launch 1 Oct 2024** — £630m public acquisition of National Grid ESO division.
- **CH Stromgesetz / Mantelerlass referendum 9 Jun 2024** (68.72% Yes); Energy Act amendments effective 1 Jan 2025; Electricity Supply Act amendments effective 1 Jan 2026.
- **IS Jan-Apr 2024 H6 hydro curtailment** — Landsvirkjun curtailed industrial loads 19 Jan – 30 Apr 2024 (water-level-driven); plus 2 Oct 2024 storm outage worst since 2019.
- **IE winter 2024-25 LOLE 3.6h vs 3h standard** — peak demand record 6,024 MW (8 Jan 2025).

### CEE + Western Balkans + Baltics

Three sub-tiers:

- **Baltics (EE/LV/LT) post-9 Feb 2025**: synchronisation-with-CE complete; permanent ENTSO-E RG-CE membership 25 Nov 2025. SAIDI improved sharply (EE 142 min 2024 vs 453 min 2023; LT 121 min 2024 vs 399 min 2023).
- **CE-EU members (PL/CZ/SK/HU/RO/BG/SI/HR)**: synchronous-CE-EU, generally robust. Two flagship 2024-2025 incidents:
  - **Balkan cascade 21 Jun 2024** — HOPS overhead lines tripped on overgrown vegetation under 42°C heat, ~3h outage across HR-Adriatic + BA + ME + AL. ENTSO-E final report Q1 2025 confirmed cause as vegetation, NOT heatwave alone.
  - **CZ blackout 4 Jul 2025** — ČEPS V411 line phase-conductor rupture, 2,700 MW lost (~⅓ of national load), ~10h restoration, ~CZK 0.75bn damage.
- **Western Balkans non-EU (RS/ME/BA/MK/AL)**: SMM/Continental Europe synchronous; weaker grids; capacity-shortage exposure (especially AL hydro-dominant — 80% import dependency in 2024 drought).
- **MD**: post-2022 emergency synchronisation with Romania; **Jan-Feb 2025 acute crisis** when Russian gas transit via UA ended 31 Dec 2024, Cuciurgan/Kuchurgan plant in Transnistria stopped supplying MD on 1 Jan 2025 (had been 70-90% historically); RO emergency imports activated.

**Water reliability is the binding constraint in the south**: BG had **5.8% of population under rationing in 2024** (Pleven 51%, Lovech 56%, Pernik 83% network losses); RO ANAR rationed 449 localities (15%) across 12+ counties; HU's Tisza basin and Great Plain under recurring drought; AL hydropower-dependent (98% generation) means dry years trigger 80% import dependency.

### Anglo non-EU

- **US 2024**: ~660 min (~11 hours) avg per EIA — nearly 2× the prior-decade average; SC peaked at ~53 hours. 80% of 2024 outage hours hurricane-driven (Beryl Jul / Helene Sep / Milton Oct). Without major events, median ~2 hours.
- **CA**: Hydro-Québec 436 min 2024 (-50% YoY); AB 2024 wildfires worst by ignition count (1,210+ fires, 705,000 ha); Jan 2024 cold-snap nearly triggered AESO rolling outages.
- **AU**: ~1.5 outages/customer/yr SAIFI (NEM avg, AEMC FY2024); AEMO 2025 ESOO flags QLD 80 MW gap 2025-26 + SA 390 MW gap 2026-27 (Torrens B retirement); Capacity Investment Scheme underwriting 50+ GW new build.
- **NZ**: winter 2024 wholesale price shocks triggered MBIE-commissioned independent review; Cabinet response Sep 2025; from 1 Apr 2026: Vector +7.8% wtd, Aurora +21%; LNG import facility procurement reported to Cabinet Dec 2025.

### Latin America

Drought-correlated grid stress dominates 2024-2026:

- **EC**: Sep 2024 – Apr 2025 national rolling blackouts up to 14h/day; ~$2bn 2024 GDP loss (Banco Central del Ecuador); Coca Codo Sinclair plant operational failures; Framework Law to Promote Energy Generation enacted 27 Oct 2024.
- **CO**: Apr 2024 hydro crisis (super El Niño) — XM/CREG declared near-blackout (reservoirs 27%, 1 week from rationing); hydro share collapsed from 87% to 47%; Bogotá water rationing from 11 Apr 2024 (Chingaza <17%); 2026 super-El-Niño forecast threatens repeat.
- **CR**: May 2024 ICE imposed scheduled rationing during 'worst drought in 50 years'; renewable share fell to 86% (vs 99%+ normal); rationing ended later 2024 as rains returned. **Closed 2025 at 98.6% renewable per MINAE — not ongoing risk.**
- **MX**: May 2024 — CENACE declared state-of-emergency twice as reserves dropped below 3% (vs 6% min); blackouts in 21 states. Sheinbaum constitutional reform Oct 2024 + Secondary Legislation 18-19 Mar 2025 (LESE/LCFE/LPTE/LCNE) re-establishes CFE as State public entity, mandates ≥54% CFE dispatch share.
- **AR**: Milei DNU 55/2023 (18 Dec 2023) declared energy emergency; tariff hikes +268% in 2024 (CPI 117.8%); Mar 2025 BA blackout 1.2M users; Jan 2026 Edenor Morón blackout ~1M users.
- **BR**: 2024 worst-recorded drought (CEMADEN) — hydro fell to 27 TWh, lowest since Aug 2021; renewables cushioned no formal rationing; ANEEL hiked red flag tariff +52%.
- **CL**: 25 Feb 2025 near-total national blackout (~90% of population) caused by HV transmission line failure (ISA Interchile, Atacama→Santiago backbone); state of emergency declared.
- **PY**: Feb 2026 nationwide blackout when both 500 kV + 220 kV Itaipú feeder lines tripped simultaneously, ~1.4M users dark; ANDE confirmed no equivalent backup line; Yguazú-Valenzuela redundancy line still incomplete.
- **PE**: 19 of 214 distribution areas exceeded annual SAIDI/SAIFI limits in 2024 (vs 4 a year prior — nearly 5× increase); Aug 2025 6-region southern blackout.

### Caribbean

Worst region by reliability metrics:

- **DO**: EDEEEST customers see ~30h/month outages (latinvestor.com); Nov 11 2025 nationwide blackout from SPMI substation; EDEs accumulated 43.3% energy losses (Ministry of Energy Jul 2025).
- **JM**: SAIDI 2,403.3 min/customer (2023, OUR — ~40 hours, +21% YoY); SAIFI 11.8 (+57% YoY); Hurricane Melissa Cat 5 (Oct 2025) blacked out 72% of network (490,380 customers).
- **BS**: Dec 2025 Abaco 17-hour load-shedding events from Wilson City plant compressor failure; periodic since Hurricane Dorian 2019.
- **BB**: 2024 frequent outages (PM Mottley publicly criticized); Nov 2024 BLPC rate increase approved (first full rate review in 13 years).
- **TT** (Trinidad & Tobago): **T&TEC** state utility (gas-fired generation), voltage 115V/230V 60Hz; electricity is **heavily subsidised / among the cheapest in the Western Hemisphere** (secondary), but a **dated SAIDI/outage metric is NOT published — verify at T&TEC / the Regulated Industries Commission (RIC)**; the "outage-prone on aging infrastructure" characterisation is secondary, and backup (inverter/generator) is common on higher-end homes. **Water (WASA) is the binding constraint, not electricity**: only **~19–27% of WASA customers receive 24/7 supply** (19% in 2024; ~27% Jan–Apr 2025, per WASA verified records; ~34% in 2022) — the large majority are on **intermittent/scheduled supply**, so **on-site storage tanks/cisterns are effectively essential**. (Older "42–53% on 24/7" figures from a modelling/adaptation doc materially overstate continuous supply — reality is worse.) Many properties outside urban cores / in Tobago rely on **septic/soakaways** — never assume mains sewer. **Unlike the northern Caribbean, TT lies ~10–11°N *south of* the main Atlantic hurricane belt → comparatively LOW direct-strike risk** (🟡, not 🔴; Tobago more exposed than Trinidad), but **wet-season flooding is material** for parcel drainage. Band: **🟢 on tariff, 🟠 on water-supply continuity**. Confidence: HIGH on WASA 24/7 ~19–27% (2024–25 verified) + cheap-subsidised power, LOW on a dated T&TEC SAIDI. (Source: WASA verified records via Newsday/Guardian/Express 2024–25; RIC "Review of the State of WASA 2016–2019" Jun 2022 — playbook 2026-06-13.)
- **BZ**: ~46% of supply imported from CFE Mexico via Yucatán; May 2024 BEL issued formal load-shedding schedule due to CFE curtailment; Sep 2025 nationwide blackout when CFE supply collapsed.
- **KY** (Cayman, BOT): CUC sole grid on Grand Cayman, diesel/fuel-oil — base CI$0.1356/kWh + fuel-cost charge ≈ doubles it → all-in **~CI$0.32/kWh (~US$0.385/kWh)** (Jun 2025, secondary); among the more expensive markets. Regionally **strong** reliability (Cayman Enterprise City / CUC framing) — 2024 Linford Pierson undergrounding phase 1 hardened the network; but Sep 2025 CUC warned of a shrinking reserve margin → possible summer rolling outages (Cayman News Service). Hurricane-season single-island tail risk; standby generator standard for continuous-occupancy. Water = desalinated RO (Water Authority – Cayman + Cayman Water/CWCo on the Seven Mile Beach zone) → costly but generally reliable. Band: **🟡 (normal year) → 🟠/🔴 in a direct hurricane hit**. Confidence: HIGH tariff, LOW SAIDI metric.
- **BM** (Bermuda, BOT): BELCO monopoly grid (12 engines, ~145 MW, fuel-oil/diesel) — block tariff (eff. 1 Jan 2026): $0.137 (≤250) / $0.244 (251–700) / **$0.380/kWh (>700)** + quarterly **Fuel Adjustment Rate 13.799¢/kWh Q1 2026** → among the world's most expensive. 100% of HV transmission underground (decades); $50M cable-replacement programme since 2020. 2025 events: island-wide outage 8 Jul 2025; Hurricane Imelda (1–2 Oct 2025) ~18,000 customers out; Melissa (31 Oct 2025) ~18,839 out (Bernews/BELCO). **Water quirk**: no island-wide piped mains for most homes — each building harvests rainwater off the white Bermuda roof into an underground tank; trucked top-ups + parish-by-parish desalination/Watlington supply are the fallback (tank condition/capacity is a real ownership cost). Band: **🟡 (best-in-region most years) → 🔴 on direct hurricane**. Confidence: HIGH tariff, LOW SAIDI metric.
- **TC** (Turks & Caicos, BOT): **Pelican Energy TCI** (rebranded from FortisTCI, Sep 2025; Vision Ridge Partners) monopoly diesel island grid across Provo + Caicos cays, regulated by EUD; **~$0.45/kWh all-in** = ~$0.291 base + ~$0.156 fuel factor (Jan 2026, fortistci.com) — among the region's highest, strong solar case. ~18,500 customers; reputationally one of the more reliable Caribbean utilities, with good storm restoration (Hurricane Oscar 19 Oct 2024 brushed Grand Turk/S. Caicos; Melissa 29 Oct 2025 passed W with little damage). **Water = 100% RO desalination — no natural freshwater**: TCWC produces / Provo Water Co distributes (~90% of Provo from the Grace Bay RO plant); villas outside the PWC footprint run private cisterns. Band: **🟡 → 🔴 on direct hit**. Confidence: HIGH tariff, LOW SAIDI metric.
- **VG** (British Virgin Islands, BOT): **BVIEC** statutory monopoly, 11 diesel gensets, ~58.5 MW installed / ~32 MW peak, ~16,254 customers (corporate-secondary) → diesel = high per-kWh cost + fuel/outage exposure (current tariff **not publicly itemised — verify at bvielectricity.com; do not fabricate**). Grid was rebuilt after Hurricane Irma (2017) and remains storm-fragile; a Cabinet-approved merger of BVIEC + Water & Sewerage Dept into a new "Virgin Islands Energy and Water Company" is reported (confirm operating entity at bvi.gov.vg). **Water**: reticulated supply has had reliability issues; many villas rely on cistern rainwater catchment and/or RO. Band: **🟡 → 🔴 on direct hit** (Irma the anchor event). Confidence: HIGH on operator + fuel-mix, LOW on tariff + SAIDI.
- **KN** (St Kitts & Nevis): two separate utilities — **SKELEC** on St Kitts (~95% coverage; Needsmust ~15 diesel sets, ~43 MW firm / ~28 MW peak; commissioned a 6 MW temporary plant Oct 2024 to cover demand; solar+storage targeting 30–35% baseload) and **NEVLEC** on Nevis (separate; Nevis Peak geothermal ambitions). Diesel base → Caribbean-typical HIGH per-kWh (**pull exact tariff at skelec.kn — not captured; do not fabricate**). Storm-season outage risk → standby generator advised. **Water**: Water Services Dept (St Kitts) / Nevis Water Dept where mains exist; cisterns common. Band: **🟡 → 🟠/🔴 on direct hit**. Confidence: HIGH operator/capacity, LOW tariff + SAIDI.
- **AG** (Antigua & Barbuda): **APUA** = single statutory authority for electricity + water + telecoms (unusual). Power is largely diesel/fuel-oil thermal (some solar) with a fuel-variation charge → **grid reliability is VARIABLE, outages documented** (e.g. Friars Hill substation fault triggered automatic load-shedding; Sep 2025 emergency Cabinet meeting on outages). Backup generators common (**current tariff not captured — verify at apua.ag**). **Water is the binding constraint**: low-rainfall, RO-dependent island; the aging 27-yr-old Crabbs RO plant (~4.5 MGD) goes offline for maintenance, and RO output is itself power-dependent — supply is intermittent, with APUA's own 2025 target only "90% of customers, water 90% of the time." Cisterns/storage tanks near-essential. Band: **🟠 (variable grid + chronic water-shedding) → 🔴 on direct hit**. Confidence: HIGH on the qualitative variability + water stress, LOW on tariff + SAIDI.
- **LC** (Saint Lucia): **LUCELEC** sole vertically-integrated utility (diesel-dominant), regulated by NURC; domestic ~**EC$0.75/kWh ≤180 kWh, ~EC$0.80/kWh above** + a **volatile fuel surcharge** reported spiking to **EC$0.255/kWh in Apr 2026** (from EC$0.007 in Mar) — expensive + surcharge-exposed, budget high. Grid generally functional but storm-exposed; documented Sep 2024 outages (Cul de Sac plant generator failure + mandatory-maintenance overlap + third-party excavation damage), and island-wide system-shutdown events have occurred. **Water (WASCO)** intermittent in dry season / post-storm → cisterns common. Band: **🟡 → 🟠/🔴 on direct hit**. Confidence: HIGH tariff band, LOW SAIDI metric.
- **GD** (Grenada): **GRENLEC** sole licensed utility (predominantly diesel), regulated by PURC; **avg residential ≈ EC$0.63/kWh (~US$0.23/kWh)** — HIGH, fuel-pass-through; fixed-rate tiers cited at EC$0.36 / EC$0.45. 2024 saw higher generation-maintenance + emergency-unit rental costs; PURC ran a cost-of-service / tariff-study RfP Feb 2026 (**rates may change — re-verify at grenlec.com/customers/ratesandfees**). Grid storm-exposed (Carriacou/Petite Martinique on the system). **Water (NAWASA)**: dry-season rationing can occur → cisterns common. Band: **🟡 → 🟠/🔴 on direct hit**. Confidence: HIGH tariff, LOW SAIDI metric.

### Türkiye + MENA

- **🟢 World-class**: AE (DEWA CML 0.94 min 2024), QA (Kahramaa SAIDI -15.6% YoY, SML -93% transmission)
- **🟢 High**: SA, BH, OM
- **🟡 Stress**: KW (first load-shedding since 2006 in Aug 2024 — peak 17,640 MW @ +50°C from KNPC gas-processing shutdown disrupting 2 power plants + desal)
- **🟡 War-strained**: IL — post-Oct-2023 grid strain, 2024 deployment slowdown, Gaza supply line cut
- **🟠 Crisis-managed**: TR (Apr 2024 Black-Sea regional outage; tariff +25% Apr 2025; subsidy cap dropped to 5,000 kWh/yr Jan 2025), JO (water rationed-supply ~36 hr/week households + ToU tariff 2025-2026)
- **🔴 Failed-grid**: **LB — EDL ~4 hr/day national average in 2024**; nationwide blackout 17 Aug 2024 (fuel depletion); private generator-mafia parallel grid de-facto national supply; rooftop solar 1.2-1.3 GW boom 2021-2024 (10× growth); Litani 2024-25 inflows ~65 MCM vs 320 MCM long-term avg (-80%).

**Iraq-GCC interconnection energised end-2024** (Al-Wafrah KW ↔ Al-Faw IQ, 295 km / 500-600 MW).

### Asia-Pacific + South Asia

**Tier-1 reliability (<10 min/yr SAIDI)**: SG (0.26 min, EMA FY23/24), HK (CLP ~6 / HK Electric <0.5), MO (~2 min), KR (<10 min).

**Tier-2 (10-50 min)**: TW (15.225, 2023), JP (~36 min FY22 ex-Noto — but Hokuriku jumped 26→510 min after 1 Jan 2024 Noto Earthquake).

**Anchor crises**:

- **Sichuan 2022 drought** (CN) — anchor for hydro-climate-power coupling
- **Sri Lanka 2022** — 13-hr blackouts → political collapse; 2024-2025 stabilised; CEB unbundling approved 2024; new Electricity Act 2025; tariff cut -21.9% Jan 2025
- **Vietnam northern-summer 2023 industrial outages** — Foxconn 30% cut request; 2024 less severe; 500 kV Circuit-3 commissioned Aug 2024 doubles N-S capacity 2.5→5 GW
- **Mumbai 2020 cascade** (IN) — transformer fire + cascade still cited as Tier-1 risk
- **Noto Earthquake 1 Jan 2024** (JP) — Hokuriku SAIDI 26→510 min; Typhoon Shanshan Aug 2024
- **Luzon Apr-Jun 2024 alerts** (PH) — 13 plants forced out, ~3,482 MW
- **Typhoon Yagi 7 Sep 2024** (VN) — 3M+ without power, water disrupted; Quang Ninh + Haiphong worst hit
- **Bali island-wide blackout** (ID) — Java-Bali submarine cable, 1.8M customers, Ngurah Rai Airport on generators
- **Sri Lanka Feb 2025 island-wide** — 7-hr nationwide blackout
- **Port Vila M7.3 earthquake 17 Dec 2024** (VU) — **damaged two major Port Vila water reservoirs** (+ buildings; 14 dead, ~US$231.7M); co-located cyclone + seismic exposure on an archipelago routinely ranked #1 World Risk Index — reset perceived seismic-build + utility-resilience risk for any Efate purchase

**India state-by-state variance is massive**: best DISCOMs (Tata Mumbai, BSES Delhi) ~30-100 min/yr; rural/poor states 1,000-3,000+ min/yr; only 8/36 DISCOMs publish ≥5 yrs of standardised data. Bengaluru "Day Zero" Feb-May 2024 (500 ML/day deficit).

**MV outer-island fragility**: Greater Malé OK; only 24 of 200 inhabited islands have continuous power; ~50 islands rely on community generators; remaining have only 5-12 hrs/day.

**PK chronic load-shedding is structural**: scheduled + unannounced load-shedding is a baseline feature, worse in summer peak; **K-Electric** (privatised) serves Karachi, the rest of the country runs on **DISCOs** under the national grid. High tariffs + outages cited (Karachi Chamber of Commerce) as deterring investment (Dawn, 2024 — secondary). Backup (UPS/inverter/solar/generator) is a normal household expectation. **Water is also unreliable + infrastructure aging**: Karachi's KWSC reported a ~54 MGD shortfall after a power fault at the **Dhabeji pumping station** (primary intake), with 1956–1971 main lines prone to rupture (Dawn/Tribune 2024 — secondary); tanker-water + private bore/storage common; Lahore/Punjab on WASA bodies with groundwater depletion. **Gated "approved schemes" (DHA, Bahria Town) self-provide utilities at higher reliability than legacy city areas — verify per-scheme, do NOT generalise.** SAIDI/SAIFI + connection costs not primary-itemised (`verify at NEPRA / K-Electric / local DISCO + KWSC/WASA`). Band: **🟠/🔴 by city + scheme**. Confidence: HIGH on the structural load-shedding + Dhabeji/KWSC framing, LOW on a dated SAIDI metric. (Source: playbook 2026-06-13.)

**VU urban-grid + island fragility**: **UNELCO (ENGIE group)** is the main electricity concessionaire for **Port Vila/Efate** (VUI also operates); the grid is limited to urban centres and **outer islands rely on diesel + solar**; tariffs reported among the higher in the Pacific (secondary; *no tariff number published — verify at the Utilities Regulatory Authority, ura.gov.vu*). Port Vila reticulated water also runs via the UNELCO concession. The **#1-World-Risk-Index hazard profile** (cyclone + seismic + volcanic + SLR, co-located) means single-island single-point-of-failure tail risk; standby generator + inverter/solar advisable. SAIDI/SAIFI not published. Band: **🟡 → 🔴 on a direct cyclone/quake**. Confidence: HIGH on operator + fuel-mix + the Dec-2024 reservoir damage, LOW on tariff + SAIDI. (Source: playbook 2026-06-13.)

### Africa + Caucasus + Central Asia

- **🟢 ZA improving**: **Eskom 300 consecutive days no load-shedding by 12 Mar 2026**; EAF 65.85% FY2025/26; diesel spend down R8.58bn (-57%) YoY; NTCSA carved out as separate transmission entity Mar 2025. NERSA approved +12.74% retail-tariff hike effective 1 Apr 2025 with more anticipated 2026-2027.
- **🟠 BW**: **BPC** (Morupule-coal-centric, net importer from Eskom/SAPP) runs a **LIVE, oscillating load-shedding regime** — cascaded 2025 unit failures (**Morupule B Unit 2 14 Feb 2025**, **Unit 4 22 Mar 2025**, Unit 3 in long-term planned outage) forced load management; **Unit 2 returned 5 Nov 2025** and SAPP imports let shedding cease, **then load-shedding RETURNED Dec 2025** (BPC schedule for 24 Dec 2025). National demand ~640 MW peak / ~440 MW off-peak. *Cite the dated BPC notice at purchase — status oscillates.* SAIDI/SAIFI not published; **WUC** water-supply outage metrics also an open gap (`verify at wuc.bw`). Water scarcity HIGH (semi-arid Kalahari, recurrent drought) is the dominant habitability hazard; **landlocked → no cyclone/coastal exposure.** Standby generator/inverter advisable. Band: **🟠 (managed)**. Confidence: HIGH on the BPC load-shed status, LOW on SAIDI + WUC metrics. (Source: gov.bw Daily News; BPC load-shed notices 2025 — playbook 2026-06-13.)
- **🔴 NG**: 12+ grid collapses 2024-2025 + first 2026 collapse 23 Jan 2026; NERC ordered 9 DisCos to compensate Band A customers Apr 2025 for failing 20-hr/day commitment; Apr 2024 Band A tariff hiked >300% to ₦225/kWh.
- **🔴 GH dumsor return Q1 2024**; PURC vs ECG public dispute over load-management timetable; ECG cash-collection reforms 2024-2025.
- **🟠 EG**: daily 2-3 hr rotational load-shedding summer 2024 due to gas-import collapse; Aug 2024 tariff hike (residential up to +50%, commercial +23-46%, industry +21-31%); freeze extended through Jun 2026; LNG cargoes ~$3bn through 2026 to avoid summer 2025 repeat.
- **🟢 MU**: among Africa's most reliable; cyclone-related outages only (Cyclone Belal Jan 2024, Cyclone Chido Dec 2024); RE target revised 35%→60% by 2030 → 35% by 2028 (Jun 2025 budget reset).
- **NA**: **NamPower** national utility + grid, **SAPP** member, and Namibia is a **net electricity importer** (historically a large share from South Africa/Eskom + region) → supply security is partly tied to regional generation adequacy. SAIDI/SAIFI **not publicly itemised** (`verify at nampower.com.na / Electricity Control Board ecb.org.na`); among world's highest solar irradiation → rooftop PV+battery widely viable. **Water is the binding constraint**: chronic drought (ThinkHazard HIGH) — Windhoek runs **direct potable water reclamation (Goreangab plant)**; supply-reliability + tariff specifics not primary-itemised (`verify at namwater.com.na` + local authority). Standby generator/inverter sensible for continuous-occupancy. Band: **inheritance/regional-stress — no published metric**. Confidence: LOW on SAIDI/outage frequency, HIGH on the net-importer structure + water-scarcity framing. (Source: playbook 2026-06-13.)
- **CV ELECTRA unbundled 2023-2024** to EPEC (gen) + ONSEC (TSO) + EDEC (DSO); ARME 2024 tariff cut.
- **🟡 RW**: nationwide blackouts dropped 35 → 6 (FY2021/22 → FY2023/24); cumulative connectivity 84.6% Jul 2025 (59.6% on-grid + 25.0% off-grid solar).
- **🟠 KE**: SAIDI 10.14 hr/month FY2023/24 (~122 hr/yr ~7,300 min/yr); 44.9 unplanned outages/customer FY2022/23; system losses 24.2% (acceptable 17.5%); 25-26 Aug 2023 nationwide blackout still anchor.
- **GE Gardabani-3 (400 MW) auction 4× extended**; commissioning by 2027; GNERC 2024-2025 tariff review reduced rates ~3 tetri/kWh.
- **AM ENA nationalization process Jun 2025** — major institutional shift after PSRC declined ENA tariff cut.
- **AZ Jan 2025 new tiered residential tariffs** (8.4 / 10 / 15 qapik blocks); fixed monthly tariffs from Jan 2026.
- **🟠 KZ**: aging infrastructure 70-90% wear on >1/3 of 220 plants; Apr 2025 wholesale cap tariff +50% (KZT 13.1 → 24.68/kWh); Oct 2025 multi-year tariff cap announced 2026-2032.
- **UZ May 2024 household block tariffs** introduced — +53% lowest, >+400% highest; cost-recovery target 89% end-2025 (IMF support).

**Water red flags**: MA 7th drought year + <650 m³/yr per capita; CV trucked-water dependency; UZ Aral legacy + Amu/Syr Darya disputes; KZ Syr Darya + Ili tensions; TN 5+ drought years; KE Horn of Africa drought + Nairobi rationing; EG Nile/GERD diplomatic + Delta groundwater depletion.

## 2024-2026 reform calendar (40+ dated entries)

Calendar-actionable triggers for re-stamping affected playbook sections.

**EU + EEA**:

- **9 Feb 2025**: Baltic synchronisation with Continental EU complete (EE/LV/LT)
- **25 Nov 2025**: Permanent ENTSO-E RG-CE membership for AST/Elering/Litgrid
- **28 Apr 2025**: Iberian peninsula blackout
- **20 Mar 2026**: ENTSO-E final report on 28 Apr 2025 Iberian blackout
- **24 Jun 2025**: Spain RDL 7/2025 (voltage control oversight + 22.5 GW storage by 2030); RD 997/2025 successor 22 Jul 2025
- **1 Jan 2025**: NL kWmaxweighted tariff replaces kWmax
- **1 Oct 2024**: UK NESO launch
- **9 Jun 2024**: CH Stromgesetz / Mantelerlass referendum (68.72% Yes); Energy Act amendments 1 Jan 2025; Electricity Supply Act amendments 1 Jan 2026
- **21 Jun 2024**: Balkan cascade blackout (HR/BA/ME/AL ~3h)
- **4 Jul 2025**: CZ blackout (ČEPS V411 line, 2,700 MW)
- **1 Aug 2025**: FR TURPE 7 HTA/BT effective
- **End-2024**: BG export-tariff removed 1 Jul 2024; full electricity market liberalisation 1 Jul 2025
- **1 Jan 2026**: Apr 2025 RO offshore wind law operative
- **17 Aug 2023**: BA Law on Electricity entered force (FERK Quality of Supply rulebook 2024)

**Anglo + LatAm + Caribbean**:

- **18 Mar 2025**: MX Secondary Legislation (LESE/LCFE/LPTE/LCNE)
- **Apr 2024**: NG Bands A/B/C/D/E tariff regime
- **27 Oct 2024**: EC Framework Law to Promote Energy Generation
- **18 Dec 2023**: AR Milei DNU 55/2023 energy emergency
- **5 Mar 2025**: AR BA blackout 1.2M users
- **25 Feb 2025**: CL near-total national blackout
- **Feb 2026**: PY nationwide blackout (Itaipú feeder dual-trip)
- **1 Apr 2026**: NZ Vector +7.8%, Aurora +21% lines tariff
- **Mar 2026**: ZA Eskom 300-day load-shedding clear; NERSA +12.74% Apr 2025 hike

**MENA**:

- **Aug 2024**: KW first load-shedding since 2006 (peak 17,640 MW @ +50°C)
- **17 Aug 2024**: LB nationwide blackout (EDL fuel depletion)
- **End-2024**: Iraq-GCC interconnection energised (Al-Wafrah ↔ Al-Faw)
- **16 Apr 2024**: UAE historic floods (254.8 mm Al Ain, 142 mm Dubai/24h)
- **Aug 2024**: EG tariff hike up to +50% residential; freeze through Jun 2026 (Feb 2026 announcement)
- **Apr 2025**: TR retail electricity +25%; subsidy cap 5,000 kWh/yr Jan 2025
- **1 Jan 2025**: JO ToU tariff covering 30% of consumption; full coverage by Sep 2026

**Asia**:

- **1 Jan 2024**: JP Noto Peninsula Earthquake
- **24 Oct 2024**: KR KEPCO industrial tariff +9.7% (households exempt)
- **Apr 2024**: TW industrial tariff +14% avg, heavy users +25%
- **Apr 2025**: TW industrial +14%, residential +3%
- **Aug 2024**: VN 500 kV Circuit-3 commissioned (Quang Trach-Pho Noi)
- **Late 2024**: VN Electricity Law 2024 (cross-subsidy + DPPA + competitive market roadmap)
- **Mar 2024**: PH Mindanao-Visayas 450 MW HVDC operational (first cross-island synchronisation)
- **Jan 2025**: LK CEB+LECO tariff -21.9% (first reduction post-2022 crisis)
- **2025**: LK new Electricity Act passed (replacing 2009 Act)
- **Jan 2025**: TNB new tariff structure 2025-2027; Sabah ICPT framework reform

**Africa + Caucasus + Central Asia**:

- **Feb 2025**: KZ wholesale cap tariff +50% (KZT 13.1 → 24.68)
- **Oct 2025**: KZ multi-year tariff cap 2026-2032 announced
- **May 2024**: UZ household block tariffs (+53% / >+400%)
- **Apr 2024**: UZ Cabinet Resolution No. 252 (Energy Market Development and Regulation Agency formalized)
- **Jun 2025**: AM ENA nationalization process begins
- **Jan 2025**: AZ new tiered residential tariffs (8.4 / 10 / 15 qapik); Jan 2026 fixed monthly tariffs
- **17 May 2025**: ZA load-shedding suspended; **300-day clear by 12 Mar 2026**
- **1 Apr 2025**: ZA NTCSA operationalized
- **Apr 2024**: GH dumsor return Q1 2024
- **Q1 2024**: EG summer 2024 daily blackouts begin

## Universal mitigations

For foreign buyers, applicable across all 126 countries:

1. **Verify the EAF / SAIDI delta vs national-policy claim** — utilities often publish flattering averages while specific feeders / districts run far worse. Always check the specific suburb / commune / district feeder via local regulator.
2. **Budget for backup**: Tier-3+4 markets (LB, NG, GH, EC, CO during drought, KH, IN rural, Caribbean Family Islands, MV outer islands) require diesel/petrol generator OR Starlink-grade UPS + battery + solar buffer. Pricing: $5k-$30k upfront depending on size.
3. **Cross-reference water reliability** — the 7th cross-cutting trap. Don't assume electricity-OK = water-OK. Same drought hits both. Check municipal water-rationing schedule + reservoir levels before signing.
4. **Verify generation-mix exposure** — hydro-dominant markets (EC, CO, CR, BR, AL, CN-Sichuan, VN-north, NO) flip 🟢→🔴 in dry years. Get the most-recent reservoir levels before reliance.
5. **Insurance + business-interruption riders** — extended outage events not always covered under standard property policy; verify rider availability for grid-failure-induced losses (food spoilage, business interruption, sump-pump failure → flood damage).
6. **Tariff trajectory > current rate** — cheap tariff today can reflect under-investment that will surface as future outages OR steep hikes (KZ 2026-2032 caps, NG band-A vs band-E, EG freeze ending Jun 2026, ZA NERSA 2026-2027). Look at multi-year regulator decisions, not last-bill snapshot.
7. **Strata / HOA backup-power infrastructure** — apartment buildings in Tier-3+4 markets often have shared diesel generators with maintenance-fund implications. Verify generator condition + fuel-storage compliance + monthly service-fund accrual before bidding.

## Confidence labels

- **HIGH**: SAIDI/SAIFI from official regulator within 12 months; reform calendar cited via legal instrument; events documented in primary or major secondary source. Applies to: most Western Europe, US, JP, KR, TW, HK, MO, SG, ZA-electricity, NG, KE, CL, BR, EC, CO, MX, AR, IN-electricity-events.
- **MEDIUM**: Qualitative reliability characterisation strong; numeric SAIDI not publicly headlined OR data is in local-language regulator reports not extracted; events well-documented. Applies to: many CEE/Balkans, AU, NZ-quantitative, MY, ID, VN, PH, IN-DISCOM-numeric, RW, GE, AM, AZ, MU, SC, CV, GH-quantitative, TR-numeric, JO-numeric, OM, BH.
- **LOW**: Numeric SAIDI not publicly available; inheritance assumption from host grid; event-level data thin. Applies to: SM (no separate publication; IT-grid-embedded), AD/MC/LI (microstate limited publication), MV outer-islands (sparse data), TN-numeric, BA-numeric, AL-numeric, KH-numeric.

**Coverage gaps** (3 countries pending follow-up research): **LU** (Creos transmission, ILR regulates — likely 🟢 inheritance from CE-EU bloc); **CY** (EAC vertically integrated state monopoly, EuroAsia Interconnector under construction; CERA regulates); **MT** (Enemalta + 200 MW HVDC interconnector to Sicily since 2015; MRA regulates). These three are placeholders pending dedicated research; treat as MEDIUM-LOW confidence until next refresh.

## Status

**Last refreshed**: 2026-05-09. **Next refresh**: monthly for high-volatility markets (LB · NG · GH · EC · CO · KZ · UZ · KE · IN · EG · TR · CL · MD · ME), quarterly for stable Tier-2 (most EU, AU, NZ, JP, KR, TW), per-event (any nationwide blackout / regulator decision / capacity-market reform).

**Confidence**: MEDIUM-HIGH for the regional patterns + reform calendar (well-sourced); MEDIUM for per-country one-liners (mix of regulator-published + extrapolated); LOW for the 3 coverage-gap microstates pending follow-up.
