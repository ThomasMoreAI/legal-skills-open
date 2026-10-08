# India 🇮🇳 — Property Due-Diligence Playbook

ISO2: `in`. Status: ✅ Fully populated (researched 2026-05).

> **🇮🇳 LEAD WARNING — read before any other section.** India's property regime is **decentralised at every layer**. There is **no national cadastre** — land records sit at the State/UT level under State Stamp Acts + State Registration Acts + the colonial-era Registration Act 1908. Stamp duty rates, RERA rollout, sub-registrar procedure, electronic-record availability and **the very identifier of a parcel** (Survey Number / Khata / Khasra / Patta / Property Identification Number) all change at the state border. **Foreign-buyer access is governed by FEMA Notification No. 21(R)/2018-RB (RBI; supersedes 21/2000-RB) — NRI/OCI may freely buy residential or commercial property; foreign nationals (non-NRI/non-OCI) are effectively barred except via inheritance or 182-day prior-financial-year residency + RBI prior approval; nationals of Pakistan, Bangladesh, Sri Lanka, Afghanistan, China, Iran, Nepal and Bhutan need RBI prior approval EVEN for inheritance (FEMA 21 §6 longstanding RBI restriction). Separately, Press Note 3/2020 adds a corporate-FDI scrutiny gate for India's 7 land-border countries: PK/BD/BT/CN/NP/MM/AF — Sri Lanka + Iran are NOT in Press Note 3; Myanmar is NOT in the FEMA 21 §6 inheritance list (2026-05-27 verified, source: DPIIT + RBI Master Direction).** Six- to seven-figure decisions in India demand a state-licensed property advocate + a chartered-accountant + a RERA-certified due-diligence firm — non-negotiable. Title insurance is **not mandatory** and the market is thin; clouded titles are widespread.

## Country profile

- **PIN code (postcode)**: 6 digits (PIN — Postal Index Number, India Post since 1972). First digit = postal region (e.g., 1 N, 4 W, 5 S, 7 E, 6 SW). Examples: `110001` New Delhi · `400001` Mumbai Fort · `400050` Bandra W · `560001` Bengaluru GPO · `600001` Chennai GPO · `700001` Kolkata GPO · `500001` Hyderabad · `411001` Pune · `380001` Ahmedabad · `122001` Gurugram. Lookup: [`https://www.indiapost.gov.in/locate-postoffice`](https://www.indiapost.gov.in/locate-postoffice).
- **Admin levels**: 28 States + 8 Union Territories (UTs) → 783 districts → ~7,000 sub-districts (tehsils / taluks / mandals) → ~250,000 villages + ~4,000 towns + ~100 cities. Source: Ministry of Home Affairs `https://www.mha.gov.in/`.
- **Population**: ~1.428 B (UN World Population Prospects 2024 medium projection — verify at [`https://population.un.org/wpp/`](https://population.un.org/wpp/); India's last decennial Census was 2011 — Census 2021 was deferred and as of May 2026 not yet executed; new headcount expected 2026–2027 per MHA statements at `https://censusindia.gov.in/`).
  - Mumbai Metropolitan Region: ~21M · Delhi NCT + NCR: ~33M · Bengaluru Metro: ~13M · Hyderabad Metro: ~10M · Chennai Metro: ~11M · Kolkata Metro: ~15M · Pune Metro: ~7M · Ahmedabad Metro: ~8M (UN-DESA 2024 + state Census-projection figures — verify per metropolitan-development-authority).
- **Currency**: INR (Indian Rupee, ₹ / `Rs.`); managed-float; capital controls under FEMA + RBI's Liberalised Remittance Scheme (LRS) capping outbound at **USD 250,000 / individual / FY** (RBI A.P. (DIR Series) Circular updates). RBI reference rate daily: [`https://www.rbi.org.in/Scripts/ReferenceRateArchive.aspx`](https://www.rbi.org.in/Scripts/ReferenceRateArchive.aspx). Recent depreciation trend ~3–5 % p.a. against USD over 2018–2025 (IMF + RBI data).
- **Languages**: 22 scheduled languages (Constitution 8th Schedule). **Hindi + English are the two official Union languages** (Official Languages Act 1963). **English dominates legal + commercial + conveyancing across India** (court judgments, registered sale deeds in metros, RBI/SEBI/IRDAI regulations all in English). State sale deeds may be in the local script (Marathi in Maharashtra, Tamil in Tamil Nadu, Kannada in Karnataka, Telugu in Telangana/AP, Bengali in West Bengal) with English translation often appended.
- **Cadastre — DECENTRALISED PER STATE / UT (no national registry)**:
  - State Revenue Department + Department of Stamps & Registration runs the title-deed registry per the Registration Act 1908 + state amendments
  - Sub-Registrar Offices (SROs) at sub-district level register sale deeds + collect stamp duty + registration fee
  - **Digital India Land Records Modernization Programme (DILRMP)** — Department of Land Resources, MoRD, since 2008 (rebranded NLRMP → DILRMP 2016): [`https://dilrmp.gov.in/`](https://dilrmp.gov.in/) — driving cadastral re-survey + digitisation of Records of Rights (RoR) + integration of textual + spatial records; uneven progress per state
  - **Major state portals** (verify per parcel state):
    - Maharashtra: **MahaBhulekh** [`https://bhulekh.mahabhumi.gov.in/`](https://bhulekh.mahabhumi.gov.in/) + **e-Search 7/12** + **iSarita / Maharashtra Department of Registration & Stamps** [`https://igrmaharashtra.gov.in/`](https://igrmaharashtra.gov.in/)
    - Karnataka: **Bhoomi RTC** [`https://landrecords.karnataka.gov.in/`](https://landrecords.karnataka.gov.in/) + **Kaveri Online Services** [`https://kaveri.karnataka.gov.in/`](https://kaveri.karnataka.gov.in/)
    - Tamil Nadu: **Patta Chitta** [`https://eservices.tn.gov.in/`](https://eservices.tn.gov.in/) + **TNREGINET** [`https://tnreginet.gov.in/portal/`](https://tnreginet.gov.in/portal/)
    - Delhi: **DLRC / Delhi Online Registration Information System (DORIS)** [`https://doris.delhigovt.nic.in/`](https://doris.delhigovt.nic.in/)
    - Telangana: **Bhu Bharati (భూ భారతి)** [`https://bhubharati.telangana.gov.in/`](https://bhubharati.telangana.gov.in/) — successor to **Dharani**: the Telangana Bhu Bharati (Record of Rights in Land) Act, 2025 (Act No. 1 of 2025, assent 3 Jan 2025, first published in the Telangana Gazette Part IV-B Extraordinary on 4 Jan 2025) repealed the Telangana Rights in Land and Pattadar Pass Books Act, 2020 (Act No. 9 of 2020) at s.23(1); s.1(3) brings the Act into force area-by-area on dates the State Government notifies, so a parcel may still sit under the old record set — check which regime applies before relying on a printout (2025 statute, Telangana Gazette Part IV-B Extraordinary No. 1; 2026-09-18 verified)
    - Andhra Pradesh: **MeeBhoomi** [`https://meebhoomi.ap.gov.in/`](https://meebhoomi.ap.gov.in/)
    - Uttar Pradesh: **Bhulekh UP** [`https://upbhulekh.gov.in/`](https://upbhulekh.gov.in/) + **IGRSUP** [`https://igrsup.gov.in/`](https://igrsup.gov.in/)
    - Gujarat: **AnyROR** [`https://anyror.gujarat.gov.in/`](https://anyror.gujarat.gov.in/) + **Garvi** registration portal
    - West Bengal: **Banglarbhumi** [`https://banglarbhumi.gov.in/`](https://banglarbhumi.gov.in/)
    - Haryana: **Jamabandi** [`https://jamabandi.nic.in/`](https://jamabandi.nic.in/)
    - Rajasthan: **Apna Khata** [`https://apnakhata.rajasthan.gov.in/`](https://apnakhata.rajasthan.gov.in/)
    - Kerala: **e-Rekha + ReLIS** [`https://erekha.kerala.gov.in/`](https://erekha.kerala.gov.in/)
- **Identifiers** (state-specific — translation matters):
  - **Survey Number / Sy. No.** — primary land identifier in most southern + western states (KA, TN, MH, AP, TS); a numeric reference assigned during the British-era cadastral survey + revenue resurvey
  - **Khata Number** — owner-folio number in revenue records (Karnataka, AP, Telangana); required for property-tax assessment
  - **Khasra Number** — analogous to survey number in northern states (UP, MP, Rajasthan, Haryana, Punjab, Bihar)
  - **Patta** (Tamil Nadu, AP, Telangana) — Record-of-Rights document for agricultural land
  - **Plot Number / Property ID** — municipal plot reference (urban authorities like DDA, MMRDA, BDA assign these for planned layouts)
  - **CTS Number** (City Survey Number) — Mumbai/Maharashtra urban survey reference
  - **APMR / Property Identification Number (PID)** — Bengaluru BBMP property tax ID
- **Ownership types**:
  - **Freehold** — outright ownership of land + building (most resale + cooperative-society apartments + standalone houses)
  - **Leasehold** — typically 30 / 60 / 99-year lease from state development authority (DDA Delhi, NOIDA, GIDC Gujarat, MIDC Maharashtra industrial estates, MHADA Mumbai, BDA Bengaluru); lease conversion to freehold available in many cases on payment of conversion charge
  - **Cooperative Housing Society (CHS)** — common in Maharashtra (Mumbai/Pune), Gujarat — buyer holds shares + occupancy right via Share Certificate; society holds the land freehold; CHS regulated by Maharashtra Cooperative Societies Act 1960 + state amendments; sale requires society NOC
  - **Apartment / Condominium** — undivided share in land + exclusive possession of unit + common-area share; governed by state Apartment Ownership Acts (e.g., Maharashtra Apartment Ownership Act 1970, Karnataka Apartment Ownership Act 1972) plus RERA 2016
  - **Builder Floor / Independent Floor** — common in Delhi NCR; floor-wise undivided-share split in a small standalone building
  - **Power of Attorney (POA / GPA) "sale"** — historically prevalent for under-the-table transactions; **not a transfer of title** per Supreme Court ruling **Suraj Lamp & Industries v. State of Haryana (2011)** — only a registered Sale Deed transfers title; flag aggressively in due diligence

## 🇮🇳 Foreign buyer eligibility (READ FIRST — deal-killer zone)

### Statutory regime: FEMA Notification No. 21/2000-RB

The **Foreign Exchange Management Act 1999** + **FEMA (Acquisition and Transfer of Immovable Property in India) Regulations** (currently FEMA Notification No. 21(R)/2018-RB superseding the 2000 notification) govern foreign-person property acquisition. Source: RBI Master Direction on Acquisition and Transfer of Immovable Property under FEMA — [`https://www.rbi.org.in/Scripts/BS_FemaNotifications.aspx`](https://www.rbi.org.in/Scripts/BS_FemaNotifications.aspx) + Master Circular updates.

| Buyer type | Residential / commercial freehold | Agricultural land | Plantation / farmhouse |
|---|---|---|---|
| **Indian citizen resident in India** | ✅ Allowed | ✅ Allowed (subject to state ceiling laws) | ✅ Allowed |
| **NRI (Non-Resident Indian — Indian citizen residing abroad)** | ✅ Allowed (FEMA 21 §3) — no RBI permission | ❌ **Prohibited** | ❌ **Prohibited** |
| **OCI (Overseas Citizen of India — registered cardholder under §7A Citizenship Act)** | ✅ Allowed (FEMA 21 §3) — no RBI permission | ❌ **Prohibited** | ❌ **Prohibited** |
| **PIO (Person of Indian Origin)** | OCI subsumed PIO since Jan 2015; legacy PIO cards converted to OCI | — | — |
| **Foreign national resident in India ≥182 days in prior FY** | ⚠️ Allowed with RBI prior approval (FEMA 21 §7) | ❌ Prohibited | ❌ Prohibited |
| **Foreign national NOT resident in India** | ❌ **Prohibited** (purchase) — only inheritance + lease ≤5 yrs allowed | ❌ Prohibited | ❌ Prohibited |
| **Pakistani / Bangladeshi / Sri Lankan / Afghan / Chinese / Iranian / Nepalese / Bhutanese national** | ⚠️ RBI prior approval mandatory **even for inheritance** (FEMA 21 §6 + Press Note 3/2020 lineage) | ❌ Prohibited | ❌ Prohibited |
| **Foreign company (branch / project office in India)** | ⚠️ Allowed only for the office's own use, with RBI/AD-bank reporting | ❌ Prohibited | ❌ Prohibited |

### Definitions

- **NRI** (FEMA / Income Tax): an Indian citizen who is a resident outside India for FX purposes — practically, an Indian passport holder whose principal place of residence is abroad. FEMA residency test differs from Income Tax test — verify both per case.
- **OCI**: an "Overseas Citizen of India" registered under §7A of the Citizenship Act 1955; lifetime multi-entry visa to India, near-equivalent rights to NRI for FEMA property purposes since 2005. **OCI is NOT Indian citizenship**; India does not allow dual citizenship (Constitution Art. 9 + Citizenship Act §9). Apply: [`https://ociservices.gov.in/`](https://ociservices.gov.in/).
- **Press Note 3 (2020)** (DPIIT, MoCI, 17 April 2020): tightened FDI scrutiny for entities of "country which shares land border with India" — Pakistan, Bangladesh, Bhutan, China, Nepal, Myanmar, Afghanistan — including beneficial-owner pass-through. Source: [`https://dpiit.gov.in/`](https://dpiit.gov.in/).

### Path 1: NRI / OCI freehold purchase (✅ standard route for diaspora buyers)

- **No RBI permission needed** for residential or commercial freehold (FEMA 21 §3) — purchase via standard sale deed registration at the Sub-Registrar Office (SRO).
- **Funding**: must be from inward remittance in foreign currency through normal banking channels OR from balances in NRE / NRO / FCNR(B) account held with an Authorised Dealer bank (RBI guidelines). Cash payment NOT permitted — Income Tax Act §269SS / §269T thresholds.
- **No purchase quota** (unlike condominium foreign quotas in some markets).
- **Joint purchase with a foreign-national spouse who is NOT NRI/OCI** is possible only if the foreign-national spouse qualifies independently under §6 (resident in India ≥182 days in prior FY) — otherwise the foreign spouse must be excluded from title.
- **Repatriation of sale proceeds**: NRE-funded purchase → freely repatriable (subject to lock-in of 10-yr equivalent or actual holding period); NRO-funded → up to USD 1M / FY per RBI guidelines; capital-gain proof + Chartered Accountant Form 15CA/15CB + bank confirmation required.
- **Number-of-properties cap**: NRI/OCI may sell residential property only twice in a lifetime with full repatriation (per RBI guidance on remittance of sale proceeds — verify current Master Direction).

### Path 2: Foreign national resident in India ≥182 days

- Foreign national who is "resident in India" under FEMA §2(v) (i.e., resided in India ≥182 days in the **preceding financial year**) may acquire residential/commercial property with **RBI prior approval** under FEMA 21 §7.
- Approval is discretionary; turnaround typically 2–6 months; must demonstrate genuine residential intent + funding via banking channels.
- **Cannot** acquire agricultural / plantation / farmhouse property under any circumstances.
- Excludes: Pakistani / Bangladeshi / Sri Lankan / Afghan / Chinese / Iranian / Nepalese / Bhutanese nationals, who require RBI approval irrespective of residency status.

### Path 3: Inheritance

- Foreign national may inherit any immovable property (including agricultural) from a person who was resident in India + acquired the property legally (FEMA 21 §6).
- Pakistani / Bangladeshi / etc. nationals (the 8-country list above) require **RBI prior approval even for inheritance** (Press Note 3 lineage).
- Inherited agricultural land may be **retained** but not freely sold to non-Indian-resident persons; sale to a citizen-resident or NRI/OCI residential conversion is the practical path.

### Path 4: Lease ≤5 years (no RBI approval)

- A foreign national NOT resident in India may take a lease of immovable property up to 5 years without RBI permission (FEMA 21 §5). Useful for short-term rental + corporate housing; not a freehold path.

### What is NOT a path

- ❌ **Holding through an Indian company majority-owned by foreign nationals** to acquire agricultural land — the company is treated as foreign-owned for FEMA purposes; agricultural land is barred. Press Note 3 (2020) tightened this for neighbouring countries' beneficial owners.
- ❌ **Power of Attorney "transfer"** — Supreme Court **Suraj Lamp** (2011) confirmed only registered Sale Deed transfers title; GPA-based "sales" do not move title regardless of buyer nationality.
- ❌ **Tourist visa + property purchase** — purchase by a non-resident foreign national without RBI approval is void under FEMA + can attract penalty up to 3× the property value (FEMA §13).

### Visa pathways — NO golden visa via real estate

⚠️ **India has NO residency-by-investment / citizenship-by-investment programme tied to real-estate**. Property purchase by NRI/OCI does NOT confer any additional visa right (OCI cardholders already have lifetime multi-entry). Foreign nationals must independently qualify under:

- **Employment Visa (E)** — sponsored by Indian employer; min annual gross income ≥ USD 25,000 (with exceptions for ethnic-cuisine chefs, language teachers, artists)
- **Business Visa (B)** — for visiting on business; not a long-stay residence visa
- **Project Visa (P)** — power/steel sector projects
- **Research Visa (R)** — academic
- **Medical / Tourist / Conference / Student Visa** — short-stay
- **Citizenship by naturalisation** — Citizenship Act 1955 §6 + 3rd Schedule: 12 years total residence in India (11 yrs in past 14 yrs + 1 yr immediately before application); single citizenship (renunciation of prior nationality required at oath)
- **OCI** — for persons of Indian origin (via descent up to 4th generation, spouse of Indian citizen, etc.) — lifetime multi-entry; NOT citizenship

⚠️ **No "investor visa" by direct property purchase exists** — distinct from regional peers (Singapore, UAE Golden Visa, Thailand Elite). India's investor route is via FDI in operating businesses (DPIIT-approved sectors) — not passive real estate.

### Confidence

**HIGH** — FEMA Notification 21(R)/2018-RB + RBI Master Direction on Acquisition and Transfer of Immovable Property + Citizenship Act 1955 + Press Note 3/2020 are all primary statute or regulator sources. **MEDIUM** for RBI-approval timelines on §7 cases (case-by-case discretion). **HIGH** for the absence of golden visa (DPIIT + MEA confirmed; perennial discussion of investor pathways but none enacted as of May 2026).

---

## Section: `--price`

### Primary sources

- **NHB Residex** (National Housing Bank — Government of India) — quarterly residential price index covering 50+ cities in two segments (HPI@Assessment Prices, HPI@Market Prices): [`https://residex.nhbonline.org.in/`](https://residex.nhbonline.org.in/) — the canonical official series
- **RBI House Price Index (HPI)** — quarterly, 10-city index based on data from State Registration Departments via NHB: [`https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=14274`](https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=14274)
- **State Sub-Registrar registered sale prices** — declared values per registered Sale Deed; access varies per state portal (Kaveri, MahaBhulekh, IGRSUP, Patta Chitta, etc.)
- **Income Tax Department Circle Rates / Ready Reckoner Rates / Guideline Values** — state-published minimum-stamp-duty values per location (the "floor" for stamp duty assessment); typically 10–40 % below realised market price; verify per state portal

### Listing platforms (secondary, listing = seller-controlled)

- **MagicBricks** — [`https://www.magicbricks.com/`](https://www.magicbricks.com/) — biggest by listings + monthly PropIndex report
- **99acres** (InfoEdge) — [`https://www.99acres.com/`](https://www.99acres.com/) + quarterly Insite report
- **Housing.com** (REA Group) — [`https://housing.com/`](https://housing.com/)
- **NoBroker** — [`https://www.nobroker.in/`](https://www.nobroker.in/) (FSBO, no broker fees)
- **CommonFloor** (Quikr) + **OLX Real Estate** — secondary
- **Square Yards / PropertyWala / Sulekha Property** — long-tail

### Professional secondary aggregators

- **PropEquity** — [`https://www.propequity.in/`](https://www.propequity.in/) (paid; primary-market analytics)
- **Anarock Property Consultants** — quarterly Indian Real Estate Outlook: [`https://www.anarock.com/`](https://www.anarock.com/)
- **Knight Frank India** — quarterly India Real Estate Update + Prime Global Cities: [`https://www.knightfrank.co.in/`](https://www.knightfrank.co.in/)
- **JLL India** + **Cushman & Wakefield India** + **CBRE India** + **Colliers India** — quarterly market reports
- **Liases Foras** — primary-market data syndication

### Price benchmarks (Q4 2025 / Q1 2026 — listing-derived; rates may have changed since)

> Source warning: NHB Residex + RBI HPI are official mix-adjusted indices; listing-platform averages run 10–25 % above realised; State Circle Rate is the stamp-duty floor, not market value. Use NHB/RBI for index trajectory, listings for comp shopping, Circle Rate for tax estimate.

| Locality | Listing INR/sqft (built-up area) | INR/sqm est. | USD/sqm est. (1 USD ≈ INR 84, Q1 2026) | Source |
|---|---|---|---|---|
| **Mumbai South + Worli + Lower Parel** (prime apt) | 50,000–125,000+ | 5.4–13.5 lakh | ≈ $6,420–$16,070 | MagicBricks + Knight Frank Q1 2026 |
| **Mumbai Bandra W / Khar / Juhu** | 35,000–80,000 | 3.8–8.6 lakh | ≈ $4,500–$10,250 | 99acres Q1 2026 |
| **Mumbai Powai / Andheri / Goregaon** | 18,000–35,000 | 1.9–3.8 lakh | ≈ $2,310–$4,500 | Housing.com Q1 2026 |
| **Mumbai Thane / Navi Mumbai** | 9,000–20,000 | 0.97–2.15 lakh | ≈ $1,160–$2,560 | MagicBricks Q1 2026 |
| **Delhi Lutyens / Golf Links / Jor Bagh** | 70,000–250,000+ | 7.5–27 lakh | ≈ $8,930–$32,140 | Knight Frank Q1 2026 |
| **Delhi South — Vasant Vihar / Anand Niketan / GK** | 35,000–80,000 | 3.8–8.6 lakh | ≈ $4,500–$10,250 | 99acres Q1 2026 |
| **Gurugram (Golf Course Road / DLF Phase 1-5)** | 18,000–55,000 | 1.9–5.9 lakh | ≈ $2,310–$7,030 | MagicBricks Q1 2026 |
| **Noida (Sector 50 / Sector 150 / Expressway)** | 8,000–18,000 | 0.86–1.94 lakh | ≈ $1,030–$2,310 | Housing.com Q1 2026 |
| **Bengaluru — Indiranagar / Koramangala / HSR** | 12,000–25,000 | 1.3–2.7 lakh | ≈ $1,540–$3,210 | MagicBricks Q1 2026 |
| **Bengaluru — Whitefield / Sarjapur / Electronic City** | 7,500–14,000 | 0.81–1.51 lakh | ≈ $960–$1,800 | 99acres Q1 2026 |
| **Hyderabad — Banjara Hills / Jubilee Hills** | 12,000–28,000 | 1.3–3.0 lakh | ≈ $1,540–$3,570 | MagicBricks Q1 2026 |
| **Hyderabad — Gachibowli / Hitech City / Kondapur** | 7,500–14,000 | 0.81–1.51 lakh | ≈ $960–$1,800 | Housing.com Q1 2026 |
| **Chennai — Adyar / Besant Nagar / Boat Club** | 18,000–40,000 | 1.94–4.30 lakh | ≈ $2,310–$5,120 | 99acres Q1 2026 |
| **Chennai — OMR / ECR / Velachery** | 6,500–12,000 | 0.70–1.29 lakh | ≈ $830–$1,540 | MagicBricks Q1 2026 |
| **Pune — Koregaon Park / Kalyani Nagar** | 14,000–28,000 | 1.51–3.0 lakh | ≈ $1,800–$3,570 | MagicBricks Q1 2026 |
| **Pune — Hinjewadi / Wakad / Baner** | 8,000–14,000 | 0.86–1.51 lakh | ≈ $1,030–$1,800 | 99acres Q1 2026 |
| **Kolkata — Alipore / Ballygunge / Salt Lake** | 9,000–20,000 | 0.97–2.15 lakh | ≈ $1,160–$2,560 | Housing.com Q1 2026 |
| **Ahmedabad — SG Highway / Bodakdev** | 6,500–14,000 | 0.70–1.51 lakh | ≈ $830–$1,800 | MagicBricks Q1 2026 |
| **Goa — North (Anjuna / Assagao / Vagator)** | 12,000–35,000 | 1.3–3.8 lakh | ≈ $1,540–$4,500 | 99acres Q1 2026 |

> Ranges are listing-derived and reflect built-up area (saleable area inclusive of common-area share). Verify realised vs listing using NHB Residex per city ([`https://residex.nhbonline.org.in/`](https://residex.nhbonline.org.in/)) + state Sub-Registrar data.

### Compute

1. INR/sqft = listing INR ÷ saleable area. **Trap (Carpet vs Built-Up vs Super Built-Up)**: pre-RERA listings quote "super built-up area" (loading 25–35 % over carpet for common-area share); RERA 2016 mandates **Carpet Area** disclosure (Real Estate (Regulation and Development) Act §4(2)(h)). Always normalise to carpet area for comparison.
2. **Trap (Loading factor)**: post-RERA developers may quote carpet area in the agreement but use super built-up in marketing — verify the registered RERA filing on the state RERA portal; loading should not exceed ~25 % under most state RERA-approved layouts.
3. Compare to NHB Residex city quarterly trajectory.
4. Compare to 3–5 same-tower / same-society listings on MagicBricks + 99acres + Housing.com.
5. Pull the **State Circle Rate / Ready Reckoner / Guideline Value** for the parcel — this is the stamp-duty floor, not market value (typically 10–40 % below realised market). Sources: state IGRS portals (e.g., Karnataka Kaveri, Maharashtra IGR, TN TNREGINET).
6. **Trap (Builder Floor / Independent Floor)**: in Delhi NCR, "Builder Floor" listings (entire floor of a small building) frequently quote per-floor price not per-sqft — normalise carefully.
7. **Trap (Goa villa premium)**: Goa villa pricing has structural foreign-buyer + lifestyle premium 30–60 % above comparable Maharashtra coastal — verify trend on 99acres Goa quarterly.

### Confidence

**HIGH** for top-7 metro mid-tier ranges (NHB Residex + RBI HPI + multiple listing platforms within ±15 %). **MEDIUM** for tier-2 cities (less granular Residex coverage). **LOW** for Goa / Coorg / Munnar / hill-station leisure markets (thin transaction sample; foreign-NRI dominant pricing).

---

## Section: `--traffic`

### Primary sources

- **Ministry of Road Transport & Highways (MoRTH)** — Road Transport Year Book + traffic-flow surveys: [`https://morth.nic.in/`](https://morth.nic.in/)
- **NHAI (National Highways Authority of India)** — toll-plaza traffic + AADT for NH network: [`https://nhai.gov.in/`](https://nhai.gov.in/) + FASTag transaction data
- **State PWD / State Highway Authority** — state highway traffic counts (per state)
- **Urban: City Traffic Police** + **Smart Cities Mission ICCC dashboards** — city-level traffic where deployed
- **OSM `highway` tag** — fallback for non-NH/SH coverage

### Verdict bands (AADT, vehicles/day)

🟢 < 1,000 (rural / interior residential lanes, panchayat road) · 🟡 1,000–10,000 (district road, suburban arterial) · 🟠 10,000–50,000 (state highway, urban arterial, NH section) · 🔴 > 50,000 (NH expressway, urban core arterials Mumbai SV Road / Delhi Ring Road / Bengaluru ORR / Chennai GST Road).

### Coarse fallback (OSM `highway` tag)

`motorway` / `trunk` = National Expressway / NH (NE-1, NE-3, Yamuna Expressway, Mumbai-Pune Expressway, Bengaluru-Mysuru Expressway, Eastern Peripheral Expressway) · `primary` = NH / major state highway · `secondary` = state highway / major district road · `tertiary` = district road / urban collector · `residential` = city/town local.

### Metro-specific quirks

- **Mumbai**: chronic congestion on Western Express Highway, Eastern Express Highway, SV Road, LBS Marg, Sion-Panvel; rush-hour speeds on WEH commonly ~10–15 km/h (Mumbai Traffic Police data + IIT Bombay TraIM studies); proximity to **suburban rail station** within 1 km is structural value driver (Western, Central, Harbour lines).
- **Delhi NCR**: Delhi-Gurgaon Expressway peak congestion; Outer Ring Road; chronic peak-hour gridlock; **Delhi Metro proximity within 800 m** drives premium (12-line network operated by DMRC).
- **Bengaluru**: ORR (Outer Ring Road) tech-corridor congestion (Marathahalli, Bellandur, Sarjapur); Whitefield-Hosur Road; **Namma Metro Phase 2 + 2A + 2B** rolling out 2024–2027 — proximity to upcoming station drives speculative premium.
- **Hyderabad**: ORR + flyover network mitigates congestion vs other metros; Hyderabad Metro (3 lines) and Outer Ring Road network.
- **Chennai**: GST Road / OMR / ECR — IT/auto corridor; Chennai Metro Phase 1 + Phase 2 expansion ongoing; **proximity to Chennai Metro station within 800 m** premium.
- **Pune**: Pune Metro (PMRDA + MahaMetro) Phase 1 operational since 2022; Mumbai-Pune Expressway connectivity material to Pune values.

### Air pollution + traffic-related

- **PM2.5** seasonal: **🔴 Delhi NCR + Punjab + Haryana** — winter PM2.5 100–300+ μg/m³ (CPCB data; daily AQI 300–500 hazardous Nov-Feb); structural exposure flag — see `--risks`.
- **🟠 Mumbai + Kolkata + Lucknow + Patna**: PM2.5 60–120 μg/m³ winter.
- **🟡 Bengaluru + Hyderabad + Chennai + Pune**: PM2.5 30–70 μg/m³ winter (still 3–7× WHO guideline).

### Confidence

**MEDIUM** — MoRTH AADT publication patchy at parcel-level; state PWD highly variable; urban-arterial counts available via city Traffic Police but not consistently digitised. OSM-class fallback realistic baseline.

---

## Section: `--tax`

### Annual property tax — Municipal Corporation level

**Constitutional basis**: Article 243W (74th Amendment, 1992) devolves property tax to Urban Local Bodies (Municipal Corporations + Municipal Councils + Nagar Panchayats). **Each ULB sets its own rate, base + assessment method** — three common methods:

1. **Capital Value System (CVS)** — Mumbai BMC (since 2010), Hyderabad GHMC partial, Bengaluru BBMP zonal slabs
2. **Annual Rateable Value (ARV)** — Delhi MCD, Chennai Corporation, Kolkata KMC, many tier-2 cities
3. **Unit Area System (UAS)** — Patna Municipal, Hyderabad GHMC, several northern cities (per-sqm rate × built-up × usage factor × age factor)

**Effective annual property tax — typical residential (Q1 2026)**:

| ULB | Method | Effective rate | Source |
|---|---|---|---|
| **Mumbai BMC** | Capital Value (Capital Value × Tax Rate) | ~0.25–0.50 % of capital value (MCGM published rates) | [`https://portal.mcgm.gov.in/`](https://portal.mcgm.gov.in/) |
| **Delhi MCD** (post-trifurcation reunification 2022) | ARV × Rate | ~6–12 % of ARV (Category A–H zones) | [`https://mcdonline.nic.in/`](https://mcdonline.nic.in/) |
| **Bengaluru BBMP** | Unit Area / zonal slabs | ~25–50 % of UAS-derived rate × built-up (varies by zone A–F) | [`https://bbmp.gov.in/`](https://bbmp.gov.in/) |
| **Hyderabad GHMC** | ARV (Annual Rental Value) | ~17 % of ARV (slab-based) | [`https://www.ghmc.gov.in/`](https://www.ghmc.gov.in/) |
| **Chennai Corporation** | ARV-based half-yearly | ~6.62–12.40 % of half-year ARV | [`https://chennaicorporation.gov.in/gcc/department/revenue`](https://chennaicorporation.gov.in/gcc/department/revenue) |
| **Kolkata KMC** | Unit Area Assessment (since 2017 for new, ARV legacy) | varies per ward | [`https://www.kmcgov.in/`](https://www.kmcgov.in/) |
| **Pune PMC** | Capital value (since 2020-21) | ~0.30–0.80 % of capital value | [`https://propertytax.punecorporation.org/`](https://propertytax.punecorporation.org/) |
| **Ahmedabad AMC** | Carpet area-based | per-sqm slab × built-up × factors | [`https://ahmedabadcity.gov.in/`](https://ahmedabadcity.gov.in/) |

**Worked example** (Mumbai 2BHK Bandra W, capital value INR 4 Cr, BMC rate ~0.30 %): annual property tax ≈ INR 120,000/yr (~USD 1,430). Verify per current BMC rate slab + age + ward factor.

**Discounts**: many ULBs grant 5–10 % rebate for early annual payment + senior citizen + woman owner + green-building rebate (BMC, BBMP, GHMC selectively).

### Transaction taxes (one-time at purchase)

| Tax | Rate (state-dependent) | Base | Who pays | Source |
|---|---|---|---|---|
| **Stamp Duty** | 4–8 % of consideration or Circle/Ready Reckoner Rate (whichever higher) | State Stamp Acts under Indian Stamp Act 1899 + state amendments | Buyer | State Department of Stamps & Registration |
| **Registration Fee** | 1 % typically; some states cap (Maharashtra cap INR 30,000) | Registration Act 1908 + state schedule | Buyer | Sub-Registrar Office |
| **GST** (under-construction only) | **5 %** without ITC (affordable) / **12 %** without ITC (non-affordable) | GST Act 2017; ready-possession + resale = **0 %** | Buyer | Developer collects + remits |
| **TDS u/s 194-IA** | 1 % of consideration if ≥ INR 50 lakh | Income Tax Act §194-IA | Buyer (deducts from seller) | CBDT |
| **TDS u/s 195** (NRI seller) | 12.5 % LTCG / slab STCG + applicable surcharge + cess | Income Tax Act §195 | Buyer (deducts from NRI seller) | CBDT |
| **TCS** | n/a typically | — | — | — |

**State stamp duty rates (Q1 2026 reference — verify per state IGRS portal)**:

| State / UT | Standard rate | Women-buyer concession | Notes |
|---|---|---|---|
| **Maharashtra** | 6 % (Mumbai, Pune urban) / 5 % some areas | **5 % Mumbai (women)**; 1 % Mumbai metro cess slab | + 1 % registration |
| **Delhi NCT** | 6 % (men) / **4 % (women)** / 5 % (joint) | women 4 % | + 1 % registration |
| **Karnataka** | 5 % (above 45L), 3 % (21–45L), 2 % (≤20L) | no women slab; e-stamp via Kaveri | + 1 % registration |
| **Tamil Nadu** | 7 % | none | + 4 % registration |
| **Telangana** | 4 % (Telangana revised 2024) | none | + 1.5 % registration |
| **Andhra Pradesh** | 5 % | none | + 1.5 % registration |
| **Kerala** | 8 % | none | + 2 % registration |
| **West Bengal** | 5 % (≤1 Cr) / 6 % (>1 Cr) urban | 1 % rebate women | + 1 % registration |
| **Uttar Pradesh** | 7 % | 1 % rebate women (up to 10L) | + 1 % registration |
| **Haryana** | 5 % (women) / 7 % (men) urban | women 5 % | + 1 % registration |
| **Gujarat** | 4.9 % | none | + 1 % registration |
| **Rajasthan** | 6 % | 5 % women | + 1 % registration |
| **Punjab** | 7 % | 5 % women | + 1 % registration |
| **Madhya Pradesh** | 7.5 % | 6.5 % women | + 1 % registration |

> Sources: state IGRS / Stamps & Registration department portals. Rates change frequently (state budget amendments) — verify before transaction.

### GST on under-construction property (post-1 Apr 2019 reform)

- **Affordable housing**: 5 % GST without Input Tax Credit (defined: carpet area ≤ 60 sqm metro / ≤ 90 sqm non-metro AND consideration ≤ INR 45 lakh)
- **Non-affordable under-construction**: 12 % GST without ITC
- **Ready-possession (Occupancy Certificate / Completion Certificate already issued)**: **0 % GST** (treated as immovable property, not goods/services)
- **Resale (secondary market)**: **0 % GST** (immovable property out of GST net)
- **GST on landlord-paid maintenance** (society dues): if monthly maintenance > INR 7,500/unit AND aggregate society annual turnover > INR 20 lakh, 18 % GST applies on the maintenance (CBIC Circular)

### Capital Gains Tax — Finance Act 2024 reform (MAJOR — verify current law)

**Pre-Finance Act 2024 regime** (transitions complete; superseded for sales on/after 23 July 2024):
- LTCG (held > 24 months for immovable property): 20 % with **indexation benefit** (Cost Inflation Index) — Section 112
- STCG (held ≤ 24 months): taxed at slab (top 30 % + surcharge + 4 % cess)

**Post-Finance Act 2024 regime (sales on/after 23 July 2024)** — major reform:
- LTCG: **flat 12.5 % WITHOUT indexation** (Section 112(1)(b)(ii) as amended) for sales of immovable property held > 24 months
- **Grandfathering option** (Finance (No. 2) Act 2024 transition): for residential property acquired **before 23 July 2024**, the taxpayer may elect the OLD regime (20 % with indexation) — assess case-by-case
- STCG: held ≤ 24 months → slab rate (top 30 % + surcharge up to 37 % + 4 % cess)
- **NRI sellers**: same rates apply; **TDS u/s 195** at 12.5 % (LTCG) / slab (STCG) + applicable surcharge + cess **deducted by buyer** at consideration; lower-deduction certificate u/s 197 available with CA + AO process (typically 4–8 weeks)

**Reinvestment exemptions (still applicable post-2024)**:
- **Section 54** (residential to residential): LTCG exempt if reinvested in 1 residential house in India (cap **INR 10 Cr** since FY 2023-24) within 1 year before / 2 years after / 3 years construction; reinvested property must be held 3 yrs
- **Section 54F** (any LTCG to residential): LTCG on non-residential capital asset reinvested in 1 residential house — full or proportional exemption
- **Section 54EC** (LTCG to NHAI / REC bonds): up to **INR 50 lakh** in NHAI / REC / PFC / IRFC bonds; 5-year lock-in; rate ~5–6 % (verify current bond yield); **deadline: invest within 6 months of sale**
- **Section 54B** (agricultural-to-agricultural): for capital asset that was agricultural land

**Source**: Income Tax Act 1961 + Finance (No. 2) Act 2024 — [`https://incometaxindia.gov.in/`](https://incometaxindia.gov.in/).

### Tax on rental income

- **Annual Rental Value** computed under §22-§27 Income Tax Act
- **30 % standard deduction** for repair + maintenance (§24(a)) — fixed, no proof required
- **Home loan interest deduction**: §24(b) up to **INR 2 lakh / FY** (self-occupied) or actual interest paid (let-out)
- **Net rental income** added to total income → slab tax (top 30 % + surcharge up to 37 % + 4 % cess)
- **NRI rental from Indian property**: TDS u/s 195 at slab rate by tenant on monthly rent; NRI files ITR; refund/credit via DTAA (US, UK, UAE, Singapore, etc.)
- **Section 80EE / 80EEA**: first-time-buyer affordable-home-loan interest deduction (verify current applicability — sunset clauses)

### Inheritance + gift tax

- **No inheritance tax** in India (Estate Duty Act repealed 1985); BUT **inherited property cost basis = original cost** for future capital gains; FY of acquisition by deceased counts for indexation/holding period.
- **Gift Tax**: §56(2)(x) Income Tax Act — gift of immovable property to non-relative > INR 50,000 stamp value taxed at slab as "Income from Other Sources"; gifts between specified relatives (spouse, lineal ascendant/descendant, sibling, etc.) exempt.

### Future risk

- **Finance Act 2024 LTCG 12.5 % flat without indexation** — verify if any further amendments by Finance Act 2026 (FY 2026-27 Budget). Source: CBDT [`https://incometaxindia.gov.in/`](https://incometaxindia.gov.in/).
- **DTC (Direct Tax Code)** — long-pending overhaul of Income Tax Act; not enacted as of May 2026.
- **GST Council** periodically reviews under-construction rate — watch for shifts in affordable definition + ITC restoration.
- **State stamp duty cuts** as fiscal-stimulus tool — Maharashtra 2020-21 cut precedent; episodic.
- **RA 12001-equivalent state Circle Rate revision** — many states underdate Circle Rates; revisions cyclically tighten effective stamp duty.

### Confidence

**HIGH** for the statutory framework (Income Tax Act, GST Act, Indian Stamp Act, Finance Act 2024 are authoritative). **HIGH** for state stamp duty headline rates (state IGRS). **MEDIUM** for ULB property-tax effective rates (highly variable per ward + age + use factor — verify with current ULB calculator).

---

## Section: `--rental`

### Long-term residential rental

- **Statute**: state-level Rent Control Acts (most legacy; e.g., Maharashtra Rent Control Act 1999, Delhi Rent Act 1995, Karnataka Rent Act 1999, Tamil Nadu Rent Control Act); **Model Tenancy Act 2021** (Government of India, advisory) — recommends 2-yr tenancy with 1-yr extension, security deposit caps (2 mo residential / 6 mo commercial), digital rent agreement, dedicated tenancy authority + tribunal — **adoption is state-level + voluntary**; only a handful of states have notified (Andhra Pradesh, UP, Tamil Nadu partial, etc.).
- **Tenancy contract**: typically 11-month Leave & Licence Agreement (sub-12-month avoids registration in most states); 12-month+ Lease Deed mandatorily registered (Registration Act 1908 §17). 11-month L&L commonly notarised but unregistered → enforcement via civil suit (months-to-years).
- **Security deposit**: 2 months residential standard (rises to 10–12 months in Bengaluru tech-corridor, Delhi NCR; 6 months Mumbai; Model Tenancy Act caps at 2 mo recommended but states free to deviate).
- **Tax**: rental income in landlord's hands at slab; 30 % standard deduction §24(a); home-loan interest §24(b) deductible.

### Short-term rentals (Airbnb / Booking)

**Legal landscape — fragmented + state/ULB-specific**:

- **No central STR-specific statute** — STR not directly prohibited at the Union level.
- **Cooperative Housing Society (CHS) bylaws** + **Apartment Owners Association (AOA) rules** are the most binding constraint in practice — many Mumbai/Pune CHS forbid daily/weekly letting via the Society NOC + bylaw amendment.
- **Local police registration**: Goa requires Form C (foreigner stay registration) + tourist trade licence; many Mumbai SROs require police verification of tenants under Tenant Verification Form (city-level enforcement).
- **GST**: STR is a "hotel-equivalent service" under GST § Schedule II — 12 % GST if tariff < INR 7,500/night, 18 % if ≥ INR 7,500/night (CBIC Circular 168/24/2021-GST + amendments).
- **State excise + tourism**: Goa requires tourist trade licence under Goa Registration of Tourist Trade Act 1982 + DOT registration; some Kerala backwater + hill-station LGUs require Stay Registration.
- **Condominium / cooperative reality**: Mumbai prime societies (Worli, Bandra, Powai), Bengaluru tech-corridor gated communities, Goa villa estates increasingly lock-down sub-30-day letting via society bylaw amendment + RERA complaint.

**Practical reality**:
- Mumbai prime CHS: STR generally forbidden via society bylaws; enforcement variable; some buildings tolerate via NOC.
- Goa villa: extensive STR; 2024–2026 villa-licensing tightening + neighbour complaints driving regulation.
- Bengaluru / Hyderabad / Pune tech-corridor: variable; gated communities increasingly prohibit; standalone homes more permissive.
- Hill stations (Munnar, Mussoorie, Shimla, Manali): town-municipality + tourism-department licensing; enforcement variable.
- **Tax if legal STR**: GST 12/18 % if tariff threshold + slab PIT on net (or presumptive 50 % under §44ADA if PR < threshold and as a service); landlord must register GST if turnover > INR 20 lakh.

### Strategic notes

- Mumbai prime: ~2.5–4 % gross yield (Q4 2025 est. — listing rent ÷ listing price on MagicBricks/Housing.com; cross-check Anarock/Knight Frank India city-yield reports; high price/rent ratio); long-term lease dominant.
- Bengaluru / Pune / Hyderabad mid-tier: ~3–5 % gross (tech-corridor demand stable).
- Delhi NCR mid-tier: ~2.5–3.5 % gross.
- Tier-2 + tier-3 (Surat, Lucknow, Indore, Coimbatore): ~4–6 % gross.
- Goa villa STR (legal): 6–12 % gross peak; high seasonality + management overhead; legal-risk margin.

### Confidence

**HIGH** for income tax framework (Income Tax Act §22-§27 + §24). **MEDIUM** for STR enforcement intensity (society bylaws + LGU + state political cycle). **HIGH** for GST tariff slab framework (CBIC Circulars).

---

## Section: `--work=<profession>`

### Job platforms

- **Naukri.com** (InfoEdge) — [`https://www.naukri.com/`](https://www.naukri.com/) — largest by listings
- **LinkedIn India** — strong in tech, finance, multinationals
- **Indeed India** — [`https://in.indeed.com/`](https://in.indeed.com/)
- **Shine.com** + **TimesJobs** + **Monster India (Foundit)** — secondary
- **Hirect / Cutshort / AngelList Talent India** — startup-focused
- **Apna** — blue-collar + frontline
- **National Career Service (NCS)** — [`https://www.ncs.gov.in/`](https://www.ncs.gov.in/) Government of India

### Visa / work-permit pathway for foreign workers

**Foreign nationals working in India require an Employment Visa (E-visa)** sponsored by an Indian employer. Source: Ministry of Home Affairs + Bureau of Immigration [`https://boi.gov.in/`](https://boi.gov.in/) + Indian Mission visa portals.

| Visa | Threshold / Use | Validity |
|---|---|---|
| **Employment Visa (E)** | Sponsored by Indian employer; min annual gross income ≥ USD 25,000 (some exceptions: ethnic-cuisine chefs, language teachers, foreign-language translators, sports coaches with national federation) | typically 1-year initial, multi-entry, extendable annually up to 5 yrs total |
| **Business Visa (B)** | Visiting on business; not for employment | up to 5 yrs multi-entry |
| **Project Visa (P)** | Power / steel sector projects under MoU | per project; typically 1 yr |
| **Research Visa (R)** | Research at Indian institution | per project |
| **Intern Visa (I)** | Internship at Indian company | up to 1 yr |
| **OCI Card** | Person of Indian Origin (descent up to 4 generations, spouse) | lifetime multi-entry; visa-free; near-citizen rights except voting + government office |

**FRRO / FRO registration**: foreign nationals on long-stay visas must register at the Foreigners Regional Registration Office (FRRO) within 14 days of arrival if visa > 180 days. e-FRRO portal: [`https://indianfrro.gov.in/`](https://indianfrro.gov.in/).

### Restricted occupations + sector caps

- **Mass media** (publication, FM radio, TV news): FDI capped 26 %; print 26 % FDI through approval route
- **Insurance**: FDI raised to 74 % (2021)
- **Telecom**: 100 % FDI (auto route post-2021 reforms)
- **Banking — Private**: 74 % FDI (49 % auto + 25 % approval)
- **Defence**: 74 % FDI (auto route up to 49 %)
- **Real estate (construction development)**: 100 % FDI auto route subject to lock-in + min capital + min built-up area conditions (Press Note 10 / 2014 era + updates)
- **Real-estate brokerage / REIT**: 100 % FDI auto route
- **Print media**: 26 % FDI; broadcasting news 26 %; non-news 49 %+

### Salary benchmarks (metro-wide 2025–2026, INR LPA = lakh per annum gross)

| Role | Median LPA | USD est. (84 INR/USD) |
|---|---:|---:|
| Software engineer (mid-senior, top-tier MNC, Bengaluru/Hyderabad) | 25–60 LPA | $29,800–$71,400 |
| Product manager (mid, Bengaluru) | 35–80 LPA | $41,700–$95,200 |
| Investment banking analyst (Mumbai) | 25–50 LPA | $29,800–$59,500 |
| Chartered Accountant (mid-Big4) | 18–35 LPA | $21,400–$41,700 |
| Doctor (specialist, urban MNC hospital) | 15–40 LPA | $17,900–$47,600 |
| Median urban Indian formal-sector salary (PLFS 2023-24 proxy) | ~3.5–5 LPA | $4,170–$5,950 |
| **Minimum wage** | varies per state + skill class (range INR ~5,000–18,000/month for unskilled labour per state notifications) | $60–$215 |

Sources: PLFS (Periodic Labour Force Survey, MoSPI), Naukri JobSpeak Index, Glassdoor India, state Labour Department notifications.

### Confidence

**HIGH** for visa + FRRO framework (MHA + BOI primary). **HIGH** for FDI sector caps (DPIIT). **MEDIUM** for salary benchmarks (large MNC vs SME variance; PLFS vs private surveys diverge).

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **National Disaster Management Authority (NDMA)** | [`https://ndma.gov.in/`](https://ndma.gov.in/) | National hazard policy, disaster history |
| **IMD (India Meteorological Department)** | [`https://mausam.imd.gov.in/`](https://mausam.imd.gov.in/) | Cyclone tracks, rainfall, monsoon, climate normals |
| **NCS (National Centre for Seismology, MoES)** | [`https://riseq.seismo.gov.in/`](https://riseq.seismo.gov.in/) + [`https://seismo.gov.in/`](https://seismo.gov.in/) | Earthquake catalogue, fault map, real-time |
| **GSI (Geological Survey of India)** | [`https://www.gsi.gov.in/`](https://www.gsi.gov.in/) | Geological hazards, landslide, sinkhole |
| **CWC (Central Water Commission)** | [`https://cwc.gov.in/`](https://cwc.gov.in/) | Flood forecasting + river basin |
| **CPCB (Central Pollution Control Board)** | [`https://cpcb.nic.in/`](https://cpcb.nic.in/) | Air quality (CAAQM network, daily AQI) |
| **MoEFCC** | [`https://moef.gov.in/`](https://moef.gov.in/) | Environmental clearance, EIA, protected areas |
| **BIS (Bureau of Indian Standards)** | [`https://www.bis.gov.in/`](https://www.bis.gov.in/) | IS 1893 seismic zones + IS codes |
| **Bhuvan ISRO geo-portal** | [`https://bhuvan.nrsc.gov.in/`](https://bhuvan.nrsc.gov.in/) | National satellite + hazard mapping |

### Earthquake (BIS IS 1893:2016 seismic zoning)

- Five zones in IS 1893 (Part 1):2016 — **Zone V** highest risk, **Zone II** lowest:
  - **Zone V**: 🔴 NE states (Assam, Manipur, Mizoram, Nagaland, Tripura, Arunachal Pradesh), Jammu & Kashmir, Andaman & Nicobar Islands, parts of Bihar (Kosi region), Gujarat Kutch — historical M ≥ 8 risk
  - **Zone IV**: 🟠 Delhi NCT (most), Mumbai-Konkan-Goa coast, parts of UP/Bihar/Punjab/HP/Sikkim
  - **Zone III**: 🟡 Pune, Bengaluru (eastern parts), Chennai, Kolkata, Ahmedabad, most of southern India inland
  - **Zone II**: 🟢 Hyderabad core, most of Karnataka interior, Kerala backwaters, AP interior
- **Reference events**:
  - **2001 Bhuj (Gujarat) M 7.7** — ~20,000 fatalities; defining post-2001 BIS revision
  - **1991 Uttarkashi M 6.8**, 1999 Chamoli M 6.8, 1993 Latur M 6.2, 2005 Kashmir M 7.6 (cross-border)
  - **2023 Doda Kashmir M 5.4** + frequent Himalayan tremors
- **Building code enforcement**: NBC 2016 + IS 1893:2016 + IS 4326 + IS 13920 — enforcement is **state-municipal level + variable**; mid-rise informal construction (Tier-2 + Tier-3 cities + outer suburbs) often non-compliant. Verify structural engineer's stamp + RERA-mandated approvals.

### Cyclone (East + West coast)

- **East coast (Bay of Bengal)** 🔴: Andhra Pradesh, Odisha, Tamil Nadu N, West Bengal coastal, Andaman — highest cyclone frequency Oct–Dec.
- **West coast (Arabian Sea)** 🟠: Gujarat coastal, Maharashtra coast, Goa, Karnataka, Kerala — historically lower frequency but **increasing trend post-2018** (Cyclone Ockhi 2017, Tauktae 2021, Biparjoy 2023).
- **Reference events**:
  - **Hudhud 2014** (Vizag, AP — cat-3) · **Vardah 2016** (Chennai) · **Fani 2019** (Odisha — cat-4) · **Amphan 2020** (Bengal/Odisha — cat-5 super-cyclone) · **Tauktae 2021** (Gujarat coast — cat-3) · **Yaas 2021** (Bengal/Odisha) · **Mocha 2023** (Bay/Bangladesh) · **Biparjoy 2023** (Gujarat) · **Remal 2024** (Bengal/Bangladesh)
- **Storm surge**: post-Fani + Amphan, IMD + NDMA + IIT Madras coastal-vulnerability mapping; coastal villas/condos < 5 m elevation with cyclone exposure: budget cyclone-rated openings + structural elevation.

### Monsoon flood + urban flooding

- **Mumbai 2005** reference event: 944 mm in 24 hr (26 Jul 2005); ~1,000+ fatalities; landmark for BMC drainage upgrades (BRIMSTOWAD).
- **Kerala 2018 + 2019**: Periyar river floods; Idukki + Wayanad worst (Wayanad landslide 2024 — see Landslide).
- **Chennai 2015 + 2024**: NE monsoon driven; Adyar + Cooum river basin overflow.
- **Bengaluru 2022**: Bellandur lake basin — east Bengaluru tech corridor severely flooded (Mahadevapura, Whitefield, Bellandur).
- **Delhi 2023**: Yamuna flood (highest level since 1978).
- **Hyderabad 2020**: Musi river + monsoon flooding.
- **CWC + state Disaster Management Authority** flood forecast bulletins.

### Landslides (Himalayan + Western Ghats)

- **GSI National Landslide Susceptibility Mapping** ongoing — see [`https://gsi.gov.in/`](https://gsi.gov.in/).
- **Himalayan**: Himachal Pradesh (Mandi, Shimla, Kullu — frequent monsoon slides); Uttarakhand (Joshimath subsidence 2023 — town-scale; Char Dham route landslides); Sikkim (2023 South Lhonak GLOF + flood); Arunachal Pradesh.
- **Western Ghats**: Kerala (Wayanad July 2024 — major landslide ~250 fatalities), Maharashtra Konkan (Raigad 2021 Talye), Karnataka (Madikeri / Coorg), Goa hills.
- **Hill-station property buyers**: mandatory geological assessment + slope-stability report from a registered geologist + state PWD slope clearance.

### Air pollution (PM2.5)

- **🔴 Delhi NCR + Punjab + Haryana**: winter PM2.5 100–300+ μg/m³ (CPCB CAAQM network); structural exposure flag — major health + property-desirability factor; AQICN + SAFAR-India real-time
- **🟠 Lucknow, Kanpur, Patna, Kolkata, Mumbai, Ahmedabad**: PM2.5 60–120 μg/m³ winter
- **🟡 Bengaluru, Hyderabad, Chennai, Pune, Coimbatore**: PM2.5 30–70 μg/m³ winter (still 3–7× WHO 5 μg/m³ guideline)
- **🟢 Coastal Kerala, Goa hills, Ooty, Munnar, Coorg, NE hill stations**: PM2.5 < 25 μg/m³

### Build-era hazards

| Era | Hazards |
|---|---|
| Pre-1962 | No NBC; pre-IS 1893; lath-and-plaster; lead paint; informal foundations |
| 1962–2002 | NBC 1970 + IS 1893:1962/1970/1984/2002; pre-Bhuj seismic codes under-conservative; asbestos cement sheets common; cavity-wall construction |
| Post-2002 (post-Bhuj NBC + IS 1893:2002) | Improved seismic; many tier-2 cities not yet enforcing |
| Post-2016 (NBC 2016 + IS 1893:2016) | Stricter seismic + wind + fire; enforcement at corporation level variable |
| Post-RERA 2017 | Mandatory project registration + escrow (70 % of receipts in dedicated bank) + delivery timeline + structural defects 5-yr liability under RERA §14(3) |

### Mandatory pre-purchase diagnostics

| Document | Required because | Where |
|---|---|---|
| **Encumbrance Certificate (EC)** (15-yr+ ideal, 30-yr for major) | Confirms no pending mortgage, lien, charge, court order on title | State Sub-Registrar Office; e-portals for digitised states |
| **Title Deed Chain (Sale Deeds prior 30 yrs)** | Confirms unbroken ownership chain; identifies gaps / disputed transfers | Sub-Registrar archive |
| **Mutation Certificate / Khata** | Confirms ownership in revenue records (post-purchase mutation triggers property tax + utility transfer) | State Revenue Department / Tahsildar / municipal portal |
| **Property Tax receipts** (latest 3 yrs) | Confirms no arrears | ULB online portal |
| **Building Plan Approval / Occupancy Certificate (OC) / Completion Certificate (CC)** | Confirms legal construction; pre-OC sale = under-construction (GST applies); post-OC = ready (no GST) | State / municipal sanctioned plan office |
| **RERA Registration (project + agent)** | Mandatory for projects > 500 sqm or 8 units (RERA 2016) | State RERA portal (per state) |
| **Society NOC / AOA NOC** (CHS / apartment) | Confirms transfer is permitted by society bylaws + no pending society dues | Society Secretary |
| **Survey settlement record / cadastral plan** | Confirms boundary + measurement | State Survey Department |
| **NOC from Lender / Mortgage release** (if seller had loan) | Confirms charge satisfied | Lender bank |
| **Tax Identification (PAN) + KYC** + **PIO/OCI (foreign buyer)** | Required for sale-deed registration + TDS | Income Tax + MEA |
| **NOC from town planning / DTCP / state pollution control** (varies) | Town-and-country-planning clearance for layout / building | State DTCP / MoEFCC |

⚠️ **Title insurance is NOT mandatory in India + thin market** — issued by HDFC ERGO, Tata AIG, ICICI Lombard for premium urban properties; premium ~0.5–1 % of value one-time; not a substitute for due diligence; engage advocate for full title-due-diligence report.

### Confidence

**HIGH** for seismic / cyclone / monsoon hazard zoning (BIS + IMD + NCS + GSI primary). **HIGH** for RERA mandatory diagnostic framework. **MEDIUM** for sub-parcel landslide / flood inundation specificity (GSI mapping incomplete; ULB drainage master plans variable).

---

## Section: `--mains`

### Water supply

- **Urban (Class-I cities)**: state Water Supply & Sewerage Boards or municipal corporations:
  - Mumbai: **BMC Water Department** (Tansa, Vihar, Tulsi reservoirs) — `https://portal.mcgm.gov.in/`
  - Delhi: **Delhi Jal Board (DJB)** — `https://djb.gov.in/`
  - Bengaluru: **BWSSB** — `https://bwssb.karnataka.gov.in/`
  - Chennai: **CMWSSB** — `https://cmwssb.tn.gov.in/`
  - Hyderabad: **HMWSSB** — `https://hyderabadwater.gov.in/`
  - Kolkata: **KMC Water** + **PHED** for suburbs
  - Ahmedabad: **AMC Water** + **AUDA**
  - Pune: **PMC Water Supply** + **Pune Cantonment**
- **Reliability variable**: most metros have **scheduled supply (2–6 hours/day at fixed times)** — overhead tank + sump pump + booster standard; full 24/7 supply rare except Pune partial + select Bengaluru + Hyderabad zones.
- **Bore well + tanker**: Bengaluru + Hyderabad summer reliance on private bore wells (**state groundwater authority permits required**) + private tankers (~INR 800–1,500 per 6,000 L tanker, 2026 metro est. — verify with local operators; varies by season and ward).
- **Ministry of Jal Shakti**: [`https://jalshakti-ddws.gov.in/`](https://jalshakti-ddws.gov.in/) — Jal Jeevan Mission (rural piped supply to households).

### Sewer / wastewater

**India's mains sewerage coverage is mid-tier vs OECD baselines + highly uneven**:
- **Tier-1 metros (Mumbai, Delhi, Bengaluru, Chennai, Hyderabad, Kolkata, Pune, Ahmedabad)**: 60–90 % sewerage coverage in core wards; suburbs lower; **sewage treatment capacity gap**: per CPCB 2022 audit, urban India treats only ~ 28 % of generated sewage (verify current at CPCB).
- **Tier-2 + Tier-3 cities**: 30–60 % coverage typical.
- **Modern apartments**: under state building bye-laws + STP norms, residential complexes **>20–50 units** typically require on-site Sewage Treatment Plant (STP) (varies per state — Karnataka KSPCB norm >20 units; CPCB national gradient).
- **Standalone houses**: septic tank + soakaway is the universal default; older houses may have simple cesspits — non-compliant with CPCB Effluent Standards.
- **Wastewater regulator**: **CPCB** + **State Pollution Control Boards (SPCBs)** — Water (Prevention and Control of Pollution) Act 1974 + amendments. EIA + consent-to-establish + consent-to-operate required for STP.
- **Rural**: **Swachh Bharat Mission** since 2014 — significant rural toilet coverage gain; rural piped sewerage rare.

### Verification path

1. **Listing language**: "24/7 water supply" = check actual hours (often morning + evening only) · "with STP" = on-site society sewage treatment · "with bore well" = private + permit needed · "municipal connection" = piped from ULB.
2. Contact **ULB Water Department** + **State PCB** for the parcel's stated zone of supply.
3. **Standalone house**: assume septic; verify septic tank type (3-stage modern vs single chamber) + last desludging + soakaway functional.
4. **Apartment**: verify society STP commissioning certificate + last CPCB/SPCB consent renewal + maintenance cost in society dues.

### Cost benchmarks

| Scenario | Cost (INR) |
|---|---:|
| Municipal water + sewer connection (new) | 5,000–50,000 (per ULB tariff) |
| Monthly water bill (typical 2BHK metro) | 200–1,500 (slab tariff) |
| Bore well drill + pump (Bengaluru/Hyderabad 200–400 ft) | 1.5–4.5 lakh |
| Society STP — apartment dues uplift | 2,000–8,000/month included in society dues |
| Septic tank install (3-stage, 200 sqm villa) | 1.5–4 lakh |
| Septic desludging | 3,000–8,000 per visit |
| Tanker water (6,000 L delivery, summer Bengaluru/Hyderabad) | 800–1,500 per tanker |
| RO + UV filtration (residential whole-house) | 25,000–80,000 |

### Confidence

**HIGH** for ULB institutional structure (BMC/DJB/BWSSB/CMWSSB/HMWSSB/KMC/AMC/PMC). **MEDIUM** for parcel-level reliability + sewerage coverage (verification often requires phone + on-site visit; ULB GIS maps incomplete).

---

## Section: `--crime`

### Primary sources

- **National Crime Records Bureau (NCRB)** — annual Crime in India report (national + state + city aggregate; **no per-station / per-suburb open data**): [`https://ncrb.gov.in/`](https://ncrb.gov.in/)
- **State Police portals** + **Citizen FIR online services** (e.g., Maharashtra Mahapolice, Karnataka Police, Delhi Police e-FIR): per-state
- **MEA + UK FCDO + US Department of State** travel advisories
- **Press complaints filed under Indian Penal Code + state Police Acts**

### Key context

India is a **moderate crime environment by global standards** — NCRB 2022 Crime in India recorded ~58.24 lakh cognizable offences nationally (rate ~422 per lakh population). Intentional homicide rate ~2.0 per lakh (UN ODC 2018) — well below most Latin American + sub-Saharan African peers. Property crime + cybercrime + women's-safety crimes are the dominant urban concerns. **Premium gated communities** (Lutyens Delhi, South Mumbai, Bengaluru tech-park townships) — protected by 24-hr private security + perimeter + CCTV — operate at far lower risk than the average metropolitan rate.

### Specific risk vectors

- **Petty theft + chain-snatching**: urban arterials at night (Mumbai SV Road, Delhi nighttime arterials, Bengaluru ORR after-hours)
- **Burglary**: lower in gated apartments + societies; higher in standalone houses without compound + CCTV
- **Cybercrime + UPI fraud**: rising sharply 2022–2026 — "digital-arrest" scams, OTP frauds; verify banking-fraud awareness
- **Women's safety**: 🟠 Delhi NCR + UP + parts of MP/Bihar — NCRB rates above national average; metro-specific reality varies sharply by neighbourhood
- **Mob violence / communal tension**: episodic (state + religion-specific); rare property impact in mainstream urban locations
- **Naxalite / left-wing extremism (LWE)**: 🔴 specific districts in Chhattisgarh, Jharkhand, parts of Odisha, Andhra Pradesh's Visakhapatnam Agency — declining footprint 2022–2026 per MHA reports; not relevant to mainstream property buyers
- **Border / disputed area security**: Kashmir Valley + Ladakh + parts of NE — affects insurance + property liquidity

### Verdict bands (IN-specific — vs national average)

- 🟢 < 50 % national rate (premium gated apartment + tech-park townships with private security; e.g., Worli, Lutyens Delhi, BGC equivalent in metros)
- 🟡 50–110 % national rate (typical mid-tier urban residential — most metro suburbs)
- 🟠 110–200 % one+ category (urban arterials at night; lower-income Eastlands-equivalent zones; specific NCT areas)
- 🔴 > 200 % national in multiple categories (LWE-affected districts + specific high-crime urban pockets + women's-safety hotspots)

### Confidence

**MEDIUM**. NCRB does NOT publish per-station / per-suburb open data. Aggregate trends + travel advisories + neighbourhood inquiry + private security-firm coverage are the practical reference. **Walk the area at evening + verify private security response coverage + verify society CCTV coverage before any premium-property purchase**.

---

## Section: `--amenities`

Universal OSM Overpass logic per `shared/amenities-osm.md`. India-specific brand-chain conventions:

- **Supermarket / hypermarket**: **Reliance Retail** (Reliance Smart, Reliance Fresh, Reliance Trends, JioMart), **DMart** (Avenue Supermarts), **Spencer's**, **More**, **Big Bazaar (legacy / Future Group)**, **Star Bazaar (Trent)**, **Le Marche**, **Foodhall**, **Nature's Basket**; tag `shop=supermarket` / `shop=mall`
- **Convenience / kirana**: hyperlocal kirana stores (informal — typically not OSM-tagged); **24Seven**, **Daily Needs**, **Easy Day** (chain convenience)
- **Pharmacy**: **Apollo Pharmacy** (largest), **MedPlus**, **Wellness Forever**, **Netmeds (offline)**, **PharmEasy partners**, **1mg**, local "Medical Stores"; tag `amenity=pharmacy`
- **Hospital** (private): **Apollo Hospitals**, **Fortis**, **Manipal**, **Max Healthcare**, **Medanta**, **AIIMS Delhi (public)**, **PGIMER Chandigarh (public)**, **Tata Memorial Mumbai**; tag `amenity=hospital`
- **Schools**: **DPS** (Delhi Public School), **Modern**, **Springdales**, **Sanskriti**, **Mayo (boarding)**, **Doon (boarding)**, **Cathedral Mumbai**, **Bombay Scottish**, **Jamnabai Narsee**, **The International School Bangalore (TISB)**, **Indus**, **Inventure**; tag `amenity=school`
- **Public transport**: **Indian Railways** (IRCTC) — long-distance + metro suburban (Mumbai Western/Central/Harbour, Kolkata, Chennai); **Metro** systems (Delhi Metro, Bengaluru Namma Metro, Kolkata Metro, Chennai Metro, Hyderabad Metro, Mumbai Metro, Pune Metro, Kochi Metro, Lucknow Metro, Jaipur Metro, Nagpur Metro, Ahmedabad Metro); **MMRDA Mumbai Suburban** + **Mono Rail** + **AC bus (BEST)**; **DTC Delhi bus**; **BMTC Bengaluru**; **MTC Chennai**; private cab ecosystem (**Ola** + **Uber India** + **Rapido auto**)
- **Mosque / Temple / Church / Gurudwara**: dense across India; tag `amenity=place_of_worship`

### Verdict bands (IN — adjusted for metro car-vs-walking gradient)

- 🟢 < 1 km / < 12 min walk to supermarket + pharmacy + school + metro station (typical Andheri W, Bandra E, Indiranagar, Banjara Hills inner)
- 🟡 1–3 km: typical Powai, Whitefield apartments, Gachibowli, Anna Nagar (drive-dependent but high-quality amenities reachable)
- 🟠 3–10 km: outer suburbs, NCR Greater Noida, Sarjapur outer, OMR outer
- 🔴 > 10 km: peri-urban / pre-development sites

⚠️ **Car + cab dependency**: many premium Indian neighborhoods are **drive-only** for amenities (Lutyens Delhi, parts of South Mumbai); walkability is uneven. Metro proximity within 800 m is increasingly the operative urban-livability metric.

---

## Section: `--climate`

Universal logic per `shared/climate-projections.md`. India-specific overrides:

- **Köppen-Geiger**: Aw / Am (tropical savanna / monsoon) Kerala + Konkan + east-coast lowlands · BWh / BSh (arid / semi-arid) Rajasthan + Saurashtra · Cwa / Cfa (humid subtropical) Indo-Gangetic plain (Delhi NCR, UP, Bihar, Bengal, Assam) · Cwb (subtropical highland) Bengaluru, Pune, Hyderabad, hill stations · Dwa / Dfb / ET (high-elevation Himalaya)
- **Altitude effect dominant**: Bengaluru (920 m), Pune (560 m), Hyderabad (542 m), Mysuru, Coimbatore — temperate climate (15–32 °C year-round, AC seasonal); coastal Mumbai/Chennai (sea level) — 24–35 °C + humidity year-round (AC standard); Delhi NCR (220 m) — extreme summer 40–48 °C + cold winter 4–22 °C (full HVAC)
- **Monsoon dominance**: SW monsoon Jun–Sep (Kerala onset early Jun → withdrawal Sep); NE monsoon Oct–Dec (Tamil Nadu, southern AP, parts of Karnataka coastal); IMD seasonal forecasts at [`https://mausam.imd.gov.in/`](https://mausam.imd.gov.in/)
- **Reference baseline**: IMD 1991–2020 climatology + IMD long-period average (LPA) for monsoon
- **Key projections** (IPCC AR6 + IMD-IITM scaled):
  - Annual mean temperature **+1.5 → +4.5 °C** by 2100 (SSP2-4.5 → SSP5-8.5)
  - Monsoon variability + intensification: more extreme rain events; more dry spells; net rainfall projection 0–10 % increase by 2100 (high uncertainty)
  - Heat-wave frequency: increasing — Delhi 50 °C threshold breached May 2024 (Mungeshpur); Konkan + Indo-Gangetic exposure
  - Sea-level rise: +0.30 → +0.80 m by 2100 (Mumbai, Chennai, Visakhapatnam, Kolkata coastal exposure)
  - Glacial lake outburst (GLOF): rising risk in Uttarakhand + Sikkim (2023 South Lhonak Sikkim GLOF reference)
  - Cyclone trends: Arabian Sea cyclone frequency rising (2018–2024 trend)
- **Acute-event flags**:
  - 🔴 Coastal property < 5 m elevation in Mumbai SoBo + Chennai coastal + Kolkata + Visakhapatnam + Goa back-beach (SSP5-8.5)
  - 🔴 Riparian property along Yamuna (Delhi), Ganga (UP/Bihar), Brahmaputra (Assam), Krishna/Godavari (AP/Telangana), Mahanadi (Odisha)
  - 🟠 Wadi-channel-adjacent dry-river crossings (rainy-season flash-floods Rajasthan, Gujarat)
  - 🟠 Delhi NCR + Gurgaon + Noida — heat-stress + extreme summer + winter cold + chronic PM2.5
  - 🟡 Bengaluru / Pune / Hyderabad / Mysore — moderate climate exposure; primary stress urban-flooding + summer water shortages
  - 🟡 Kerala backwaters + Goa hills — climate + tourism trajectory; coastal SLR moderate

### Climate verdict (typical metro mid-rise apt > 5 m above local drainage)

🟡 **Watch** — most major Indian metros face combined exposure: heat-stress + monsoon-flood + air-quality (Delhi NCR + Indo-Gangetic) + SLR for coastal segments. Bengaluru / Pune highlands have material adaptive capacity.

### Confidence

**HIGH** for IPCC AR6 + IMD trend projections; **MEDIUM** for sub-parcel flood-inundation specificity (city-wise drainage master plans incomplete; Bhuvan + state DSS-portals partial coverage).

---

## Section: `--finance`

### Mortgage market

- **Regulator**: [Reserve Bank of India (RBI)](https://www.rbi.org.in/) — sets prudential + LTV + capital requirements via Banking Regulation Act 1949 + Master Directions
- **Mortgage law basis**: [Transfer of Property Act 1882](https://legislative.gov.in/) + [Indian Contract Act 1872](https://legislative.gov.in/) + state Stamp Acts; SARFAESI Act 2002 enables faster lender enforcement; recovery via DRT
- **Refinancer**: [National Housing Bank (NHB)](https://nhb.org.in/) — RBI subsidiary refinances Housing Finance Companies (HFCs) + provides Residex
- **Trade body**: [Indian Banks' Association (IBA)](https://www.iba.org.in/) + Foreign Exchange Dealers' Association of India (FEDAI)

### LTV caps (RBI Master Direction on Housing Finance Aug 2018 + amendments)

| Loan amount | LTV cap |
|---|---:|
| **≤ INR 30 lakh** | **90 %** |
| **INR 30 lakh – 75 lakh** | **80 %** |
| **> INR 75 lakh** | **75 %** |
| Stamp duty + registration | included in LTV calculation since 2020 amendment |

### Major lenders

- **Public-sector banks**: SBI (largest), Bank of Baroda, Punjab National Bank, Canara, Union Bank of India
- **Private-sector banks**: HDFC Bank (post-merger with HDFC Ltd Jul 2023 — now combined entity), ICICI Bank, Axis Bank, Kotak Mahindra Bank, IndusInd
- **Housing Finance Companies (HFCs)**: PNB Housing Finance, LIC Housing Finance, Bajaj Housing Finance (largest non-bank since 2024 IPO), Aadhar HFC, HomeFirst HFC, Aavas Financiers
- **NRI-friendly**: SBI NRI Home Loan, HDFC Bank NRI, ICICI NRI Home Loan, Axis NRI, Kotak NRI

### Rate structure

- **INR floating-rate residential (Q1 2026)**: ~8.4–10.5 % nominal (linked to RBI Repo Rate + Bank Spread under External Benchmark Lending Rate / EBLR framework, mandatory since 2019); top-tier credit + co-applicant + women + PSB rates lower; tier-2 HFC rates higher (up to 12 %).
- **RBI Repo Rate Q1 2026**: ~6.0–6.5 % range (verify current at RBI Monetary Policy).
- **NRI INR mortgage**: ~9–11 % typical; LTV 75–80 %; tenure up to 30 yrs; co-applicant Indian-resident relative often required.
- **NRI cannot avail certain fiscal subsidies** (PMAY-CLSS — Pradhan Mantri Awas Yojana Credit-Linked Subsidy is for resident citizens).
- **Fixed-rate residential**: rare; most are floating + reset.

### Foreign-buyer mortgages

- **NRI / OCI**: well-established mortgage market; banks have dedicated NRI desks; documentation requires NRE/NRO account, KYC + foreign income proof + Indian co-applicant.
- **Foreign national NOT NRI / OCI**: **effectively no Indian-bank mortgage** — mortgages tied to FEMA-eligible buyers; foreign nationals require RBI prior approval to even own + cannot easily obtain Indian-rupee finance. Cash purchase via inward remittance is the only realistic route.
- **Offshore-collateral lending**: HNW foreign buyers may borrow against home-country collateral via international private banks (HSBC Private, Standard Chartered Private, UBS, Deutsche Bank Wealth) and remit equity into India.

### Banking access

- **Account opening for NRI / OCI**: NRE (Non-Resident External — INR, fully repatriable) + NRO (Non-Resident Ordinary — INR, restricted repatriation up to USD 1M/FY) + FCNR(B) (Foreign Currency Non-Resident Bank — USD/EUR/GBP/etc., repatriable) — all require passport + OCI/PIO/NRI status proof + Indian PAN + foreign-address proof.
- **Account for foreign national in India**: only after FRRO registration + Indian PAN + employer letter (E-visa) or RBI approval (other).
- Major NRI desks: SBI NRI, HDFC NRI Banking, ICICI NRI, Axis NRI, Kotak Mahindra NRI.

⚠️ Foreign-buyer mortgage availability is essentially **NRI/OCI only**. Non-NRI/OCI foreign nationals must purchase via cash + RBI approval; no bank mortgage path.

---

## Section: `--currency`

### Indian Rupee (INR / ₹) — managed-float framework

- **Regime**: managed float; RBI actively intervenes via FX reserves + open-market operations + NDF (non-deliverable forward) market
- **Currency code**: INR; symbol ₹
- **Q1 2026 reference**: 1 USD ≈ INR 83–87 range (verify daily — INR depreciated from ~75 in 2020 to ~84–87 in 2024–2026 cycle, structural ~3–5 %/yr USD-trend); 1 EUR ≈ INR 90–95; 1 GBP ≈ INR 105–112
- **Inflation Q1 2026**: ~4–6 % CPI (RBI target 4 % ± 2 %; verify current at MoSPI [`https://mospi.gov.in/`](https://mospi.gov.in/))
- **FX reserves**: RBI maintains ~USD 650–700 B (~10–11 months import cover Q1 2026 — verify current at RBI Weekly Statistical Supplement)
- Source: RBI Reference Rate Archive [`https://www.rbi.org.in/Scripts/ReferenceRateArchive.aspx`](https://www.rbi.org.in/Scripts/ReferenceRateArchive.aspx)

### What this means for buyers

- **NRI/OCI USD-source buyers**: meaningful FX risk on purchase (INR depreciation reduces effective INR purchasing power of forward USD income); INR-denominated rental yield depreciates in USD terms over time
- **Foreign-currency hedging**: forward contracts via major banks (HDFC, ICICI, Axis, SBI) for USD/INR legs > USD 100k; typical 6–12-month forward bid-ask 50–150 bps
- **NRE deposits**: INR-denominated, fully repatriable; reasonable hedge if held in INR vs INR-spend mismatch
- **FCNR(B)**: foreign-currency-denominated; protects against INR depreciation; lower interest rates than INR

### Capital controls (FEMA + Liberalised Remittance Scheme)

- **Inward FX remittance for property purchase**: must be through normal banking channels via Authorised Dealer bank; FCNR/NRE/NRO sourcing accepted; cash rejected
- **Outward FX repatriation by Indian-resident sellers**: capped under **Liberalised Remittance Scheme (LRS) USD 250,000 / individual / FY** (RBI Master Direction LRS); higher amounts require specific RBI approval
- **Repatriation of sale proceeds by NRI**: NRE-funded purchase → fully repatriable (subject to lock-in equiv. of holding period); NRO-funded → up to USD 1M / FY; CA Form 15CA + 15CB + bank confirmation required
- **TCS (Tax Collected at Source) on outward remittance**: 5 % on LRS remittance > INR 7 lakh (2023 Finance Act, since Oct 2023); 20 % on overseas tour packages + non-medical/education abroad (verify current)
- **Reporting**: AD bank reports inward + outward FX > USD 50,000 to RBI under Foreign Exchange Management (Manner of Receipt and Payment) Regulations

⚠️ **INR depreciation cycle**: 2018–2024 sustained pressure (~74 → ~87 over 6 yrs); long-run 3–5 %/yr expectation; foreign buyers should price-in 2.5–4 %/yr currency drag on INR rental yield in USD terms.

---

## Section: `--visa`

### Immigration pathways most relevant for property buyers

Source: [Bureau of Immigration India](https://boi.gov.in/) + [MEA Visa Services](https://mea.gov.in/)

| Class | Description | Threshold | Validity |
|---|---|---|---|
| **e-Tourist Visa** | Short-stay tourism (eligible nationalities) | n/a | 30/90/365 days, single/multi |
| **Business Visa (B)** | Visit on business; not for employment | per profile | up to 5 yrs multi-entry |
| **Employment Visa (E)** | Sponsored by Indian employer; ≥ USD 25,000 / FY (exceptions: chefs, language teachers, sports coaches) | sponsor + min income | 1-yr initial, multi-entry, extendable |
| **OCI Card** | Person of Indian Origin (descent up to 4 generations, spouse, etc.) | per Citizenship Act §7A eligibility | **lifetime multi-entry; no FRRO; near-citizen rights except voting + public office + agricultural-land** |
| **Permanent Residence (PR)** | n/a — India does NOT have a separate PR regime; long-stay is through repeated visa renewal or citizenship | — | — |
| **Citizenship by Naturalisation** | After **12 years total residence in India (11 of 14 yrs + 1 yr immediately before) + character + sufficient knowledge of a Constitution-Schedule-8 language** | per Citizenship Act 1955 §6 + 3rd Schedule | full citizenship; **renunciation of prior nationality required (no dual)** |

### Property-linked visas — NONE in India

⚠️ **India has NO golden-visa / residency-by-investment / citizenship-by-investment via real-estate**. Property purchase by NRI/OCI does NOT confer additional visa right (OCI already has lifetime multi-entry; NRI can stay on Indian passport). Foreign buyers must independently qualify under E-visa, B-visa, OCI eligibility (descent), or naturalisation.

### NRI / OCI status — the practical foreign-buyer "visa"

- **NRI** = Indian citizen holding Indian passport but resident abroad — full Indian-citizen rights including agricultural land (FEMA residency-test only flags repatriation rules)
- **OCI** = registered cardholder under Citizenship Act §7A — eligible: persons of Indian origin (parents/grandparents/great-grandparents Indian), foreign spouse of Indian citizen (after 2 yrs marriage), minor children of OCI parents
- **OCI rights**: lifetime multi-entry; no FRRO; can buy residential + commercial property freely (FEMA 21); CANNOT buy agricultural / plantation / farmhouse; cannot vote; cannot hold government office; not Indian citizenship
- **Application**: OCI application via Indian Mission abroad or [`https://ociservices.gov.in/`](https://ociservices.gov.in/); typical processing 60–120 days

### Citizenship + dual citizenship

- **No dual citizenship in India** (Constitution Art. 9 + Citizenship Act §9): naturalised citizen must renounce prior nationality at oath; Indian citizen acquiring foreign citizenship automatically loses Indian citizenship.
- Naturalisation rare — typically for spouses of Indian citizens after 7+ yrs marriage + residence; for non-spouse foreign nationals, the 12-year residence threshold is rarely met.

### Special pathways

- **PIO Card** — **subsumed into OCI since Jan 2015**; legacy PIO cards converted to OCI on renewal. No new PIO issuance.
- **NRI passport renewal** — Indian passport renewal at consulate; no impact on FEMA NRI status (defined by physical residence).
- **Surrender of Indian Citizenship**: required if acquiring foreign citizenship; documented at Consulate; failure = OCI denial + future immigration friction.

---

## Section: `--insurance`

### Mandatory

- **Motor Third Party** (Motor Vehicles Act 1988): mandatory for all vehicles
- **Mortgage-tied home + life insurance**: required by all RBI-regulated mortgage lenders for loan term — most banks bundle Home Loan Protection Plan (life cover) + Property Insurance
- **Workers' Compensation (Employees' Compensation Act 1923)**: employers
- **Medical (ESIC)** — for organised-sector employees: ~3.25 % employer + 0.75 % employee (Employees' State Insurance Corporation, central scheme); private health insurance widespread
- **Ayushman Bharat-PMJAY** — health-cover scheme for poor (not relevant to mainstream buyers)

### Optional but standard

| Cover | Typical premium (2026, INR) |
|---|---:|
| **Home Buildings + Contents** (typical 250 sqm metro apt) | INR 5,000–25,000/yr |
| **Earthquake** | usually included in standard bundles (Zone IV/V properties verify sub-limit) |
| **Flood + monsoon damage** | usually included; verify sub-limit + exclusions for low-lying / riparian properties |
| **Burglary + theft** | standard inclusion |
| **All-risks (high-value contents, jewellery)** | additional premium |
| **Public liability (society common-area)** | typical INR 10–50 lakh cover ~INR 5,000–25,000/yr (society-paid often) |
| **Property landlord / loss-of-rent** | additional 10–25 % of base premium |
| **Cyclone-rated** add-on | required for east-coast + post-2014 west-coast exposure |

### Major insurers

- **Public-sector**: New India Assurance, Oriental Insurance, National Insurance, United India Insurance, GIC Re (reinsurer)
- **Private-sector general**: ICICI Lombard, Bajaj Allianz General, HDFC ERGO, Tata AIG General, Reliance General, SBI General, Liberty General, IFFCO Tokio
- **Private-sector life**: LIC (largest, public-sector), HDFC Life, ICICI Prudential, SBI Life, Max Life, Bajaj Allianz Life, Kotak Life
- **Health**: Star Health, Niva Bupa (formerly Max Bupa), ManipalCigna, Aditya Birla Health, public-sector portals
- Regulator: **Insurance Regulatory and Development Authority of India (IRDAI)** — [`https://www.irdai.gov.in/`](https://www.irdai.gov.in/)

### Catastrophe + climate trajectory note

⚠️ Indian home-insurance premiums rising **5–10 %/yr** 2023–2026 driven by:
- 2024 Wayanad landslide + Kerala/Karnataka monsoon floods catastrophic
- Cyclone Biparjoy 2023 + Remal 2024 + Tauktae 2021 west-coast claims
- Rising urban flooding (Bengaluru 2022 + Chennai 2024 + Mumbai recurrent)
- Heat-wave property impact (HVAC capex + grid load)
- Construction-quality loss-frequency in mid-tier informal-sector builds

Underwriters tightening sub-limits on flood + earthquake + cyclone; verify policy carefully for ground-floor + riparian + lake-shore + coastal-exposure properties.

---

## Section: `--notary`

### Conveyancing — common-law solicitor / advocate system

India inherits the **English common-law system** (vs civil-law notary). Property transfers are handled by **Advocates registered with the Bar Council** (state-level Bar Councils; apex Bar Council of India [`https://www.barcouncilofindia.org/`](https://www.barcouncilofindia.org/)). Notaries are appointed under the Notaries Act 1952 — for attestation only, NOT for title transfer (sale deed registration is at the Sub-Registrar's office).

**Key roles**:
- **Vendor's advocate**: drafts Sale Agreement (Agreement to Sell) + Sale Deed; supplies vendor's title chain
- **Purchaser's advocate**: conducts due diligence (Encumbrance Certificate + 30-yr title chain + RERA + Khata + property tax + society NOC); supervises stamp duty + registration
- **Sub-Registrar**: registers the Sale Deed under Registration Act 1908 §17; issues Registered Sale Deed + scanned copy
- **Notary** (Notaries Act 1952): attests affidavits + indemnities + GPA + L&L Agreement (not the sale deed itself)
- **State Stamps & Registration Department**: collects stamp duty + registration fee
- **State RERA Authority**: regulates project + agent registration + disputes

### Standard timeline (typical urban resale residential transfer)

| Step | Day | What happens |
|---|---|---|
| 1. Term Sheet / MOU / Letter of Intent | D0 | Token money (typically 1–5 % refundable) — non-binding pending due diligence |
| 2. Title due diligence | D0–D30 | EC 30 yrs, prior sale deeds, RERA verification, society NOC, property tax receipts, mutation records, building approvals + OC/CC, Khata, lender NOC if seller had loan |
| 3. Agreement to Sell (Sale Agreement) | D14–D30 | Drafted + executed on stamp paper; advance/earnest typically 10–20 % paid; locks in price + timeline |
| 4. Loan sanction (if applicable) | D14–D45 | Buyer's bank sanctions home loan; valuation + legal verification; disbursement to seller's account on registration |
| 5. Stamp duty + registration fee payment | D30–D60 | E-stamp via state portal (e.g., SHCIL e-Stamp) + e-payment of registration fee |
| 6. Sale Deed registration at SRO | D45–D75 | Buyer + seller + 2 witnesses appear at Sub-Registrar Office; biometric + scanned IDs; deed registered + signed; original returned in 1–4 weeks |
| 7. Mutation / Khata transfer | D60–D120 | Buyer applies to municipal corporation / revenue authority for ownership update in property-tax + revenue records |
| 8. Society NOC + Share Certificate transfer (CHS) | D60–D120 | Society admits buyer + transfers share certificate; pays transfer fee (society bylaw — typically INR 25,000–100,000) |
| 9. NRI seller TDS u/s 195 | D45–D75 | Buyer deducts TDS (12.5 % LTCG / slab STCG) + remits to IT Department + provides Form 16A |

### Costs

| Item | Cost |
|---|---|
| Advocate fees (advocate's professional fee + drafting + due diligence) | typically 0.5–1.5 % of value (negotiable) |
| Stamp Duty | 4–8 % per state (see `--tax`) |
| Registration Fee | 1 % typically; some states cap |
| E-stamp fee + scan + admin | INR 5,000–20,000 |
| Society transfer fee + NOC + share certificate (CHS only) | INR 25,000–100,000+ (society bylaw) |
| Mutation / Khata transfer fee | INR 1,000–10,000 (ULB) |
| Property valuation (banker's panel) | INR 5,000–20,000 |
| Title insurance (optional) | ~0.5–1 % of value one-time |
| Real estate broker (resale) | 1–2 % each side typically (negotiable; no statutory cap) |
| **Total transaction cost (cash buyer, urban residential)** | **~6–10 % of price** (mostly stamp duty + registration + advocate + broker) |
| **Total transaction cost (with mortgage)** | **~8–12 % of price** (loan-processing + valuation + insurance + GST on processing fee) |

### Title fraud + clouded titles — material risk

⚠️ **Clouded titles are widespread in India.** Documented in court rulings + government audits:
- **Forged Sale Deeds** + impersonation (despite biometric registration since ~2010)
- **Multiple parallel sales** of same parcel (especially older/legacy land-records areas)
- **Power of Attorney "sales"** that do not transfer title (per **Suraj Lamp 2011**) — many GPA-based transactions surface as clouded titles
- **Disputed inheritance** — especially in joint-family / HUF (Hindu Undivided Family) properties; Hindu Succession Act 1956 + 2005 amendment governs succession; daughters' rights in coparcenary post-2005 trigger retrospective claims
- **Land acquisition + government takeback** — land acquired under RFCTLARR Act 2013 (replaced Land Acquisition Act 1894) — verify government notifications
- **Ancestral / Benami property** — Benami Transactions (Prohibition) Act 1988 + 2016 amendment — beneficial-ownership disputes
- **Tribal-land restrictions** — many states restrict transfer of tribal land (e.g., Schedule V states + NE 6th Schedule) — separate consents required
- **Encroachment** — physical occupation different from titled boundary; verify on-site survey + match cadastral plan

Mitigants:
1. **30-year (minimum 12-year) title chain trace** through Sub-Registrar archive — verify each prior Sale Deed is registered + non-disputed
2. **Encumbrance Certificate (EC)** from SRO covering 15–30 yrs — confirms no charge, mortgage, lien, court order
3. **Public notice in 2 newspapers** before purchase — invites third-party claims; standard practice
4. **Physical site inspection + cadastral survey match** by registered surveyor
5. **Society NOC + share certificate verification** (CHS) — confirms society admits transfer
6. **RERA verification** for projects (project + promoter registered + complaints history) on state RERA portal
7. **Title insurance** (optional but recommended for premium transactions): HDFC ERGO, Tata AIG, ICICI Lombard
8. **Two independent advocates** (vendor + purchaser, never shared) — Bar Council standards favour separation

⚠️ **DILRMP digitisation since 2008** — Karnataka (Bhoomi RTC) + Maharashtra (MahaBhulekh) + Telangana (Bhu Bharati, ex-Dharani) + AP (MeeBhoomi) + TN (Patta Chitta) + Kerala (e-Rekha) + Delhi DORIS lead the digitisation; **digital records are the gold standard going forward**, but legacy paper records still dominate sub-rural districts; verify both digital + paper records.

---

## Section: `--compare`

### India vs South Asia + emerging-market peers (residential investment lens, Q1 2026)

| Country | Foreign-buyer rule | Acquisition cost (typical) | Annual recurring | Yield (Q4 2025) | Currency risk |
|---|---|---:|---:|---:|---|
| **🇮🇳 India** | NRI/OCI freely (residential + commercial); foreign nationals effectively barred without RBI | 6–10 % buyer side | ULB property tax 0.3–2.5 % varies | ~2.5–5 % gross (metro mid-tier) | INR managed-float — meaningful (3–5 %/yr USD trend) |
| **🇱🇰 Sri Lanka** | Restricted (Land Restrictions on Alienation Act); leasehold or company route | 6–12 % | Local rates | ~5–8 % | LKR managed |
| **🇧🇩 Bangladesh** | Restricted; foreign nationals require govt approval | 8–14 % | Holding tax | ~5–8 % | BDT managed |
| **🇳🇵 Nepal** | Restricted to Indian citizens (Nepal-India treaty); other nationals barred | 6–10 % | Land tax | ~5–7 % | NPR pegged to INR 1.6 |
| **🇵🇰 Pakistan** | Restricted; security-clearance required | 8–14 % | Property tax | ~5–8 % | PKR weak |
| **🇲🇻 Maldives** | Restricted to 99-yr lease only | 6–8 % | Resort lease fees | ~6–10 % | MVR pegged USD |
| **🇸🇬 Singapore** | Open with 60 % ABSD non-resident surcharge for residential since 2023 | 60 % ABSD + 4 % BSD | Property tax 0–32 % progressive | ~2.5–3.5 % | SGD strong, stable |
| **🇦🇪 UAE Dubai** | Open in designated freehold zones (foreigner) | 4 % DLD + 2 % broker | Service charge | ~6–8 % gross | AED USD-pegged |
| **🇹🇭 Thailand** | Condo only (49 % foreign quota); no land freehold | 6–8 % | Land tax | ~5–7 % | THB managed |

### India's distinctive position (2026)

- **NRI/OCI freely buy residential + commercial** — a structurally privileged path for ~30M-strong diaspora; not available to non-NRI foreign nationals
- **Press Note 3 (2020)** tightened FDI scrutiny for neighbouring-country beneficial owners — particular friction for Chinese + Pakistani capital
- **Decentralised cadastre + clouded titles** — material structural risk vs Singapore / UAE; mid-tier vs Thailand condo regime
- **No golden visa** — distinct from UAE Golden Visa, Singapore PR-via-investment, regional peers
- **Strong English common-law system + Bar Council advocate framework** — institutional familiarity for Anglo + diaspora buyers
- **State stamp duty 4–8 %** — among the higher in Asia for transaction tax
- **Finance Act 2024 LTCG 12.5 % flat without indexation** — structural reform; lower nominal rate but elimination of indexation may raise effective tax for long-held + highly-appreciated holdings (grandfathered for pre-23-Jul-2024 acquisitions)
- **GST 5 %/12 % on under-construction**, 0 % on ready/resale — careful comparison
- **RERA 2016 transparency revolution** — escrow + delivery accountability; enforcement variable per state
- **Counterbalance risks**: Press Note 3 friction for neighbouring nationals; clouded-title risk; INR depreciation drag on USD-denominated returns; air-pollution exposure in Delhi NCR; cyclone + earthquake exposure in BIS Zone IV/V

### Comparative reference

For **regional structural similarity**, see `countries/lk/playbook.md` (Sri Lanka — closest legal analog for foreign-buyer restriction) when added; `countries/sg/playbook.md` (Singapore — common-law sister but ABSD-heavy); `countries/ae/playbook.md` (UAE Dubai — common-law-flavour open-freehold zones).

---

## Section: `--retirement`

### Retirement to India scenario

India is **NOT a primary international retirement destination** (vs Portugal D7, Mexico, Costa Rica, Thailand). Most foreign retirees in India are **OCI cardholders** returning to India after careers abroad — a structurally different demographic from typical "retirement-migration" markets. **No foreign-pensioner-specific visa** exists.

### Visa pathway

- **OCI Card** — for persons of Indian origin (descent up to 4 generations + spouses) — lifetime multi-entry; the practical retirement vehicle for diaspora
- **Employment Visa or Business Visa** — short-to-medium term; not retirement-purpose
- **No "retirement visa" / "passive-income visa" / D7-equivalent** — material gap vs Mediterranean or SE-Asian peers
- **Citizenship by Naturalisation** — 12-yr residence requirement very rarely met by retirees
- **Foreign nationals who cannot qualify under OCI** — limited to repeated tourist + business visa renewal; long-stay residence requires E-visa or RBI approval pathway

### Cost-of-living for retirees (Q1 2026 — metro tier-1)

- **Mumbai 3-bed Bandra W rental**: INR 200,000–500,000/month (~USD 2,400–5,950)
- **Delhi 3-bed Vasant Vihar / South Ex rental**: INR 150,000–400,000/month
- **Bengaluru 3-bed Indiranagar / Whitefield rental**: INR 80,000–200,000/month (~USD 950–2,380)
- **Pune 3-bed Koregaon Park rental**: INR 80,000–180,000/month
- **Goa 2-bed villa Anjuna rental**: INR 60,000–250,000/month seasonal
- **Domestic help (cook + cleaner)**: INR 8,000–25,000/month each (separate maids common)
- **Eating out**: mid-range INR 800–2,000/meal; high-end INR 3,000+
- **Utilities (incl. internet + gas + water + electricity)**: INR 8,000–25,000/month for typical 3-bed metro

### Tax position for retirees

- **No tax on foreign pension income to NRI/OCI not resident in India** (FEMA / Income Tax Act §6 residency test); **once OCI becomes Indian-resident** (≥182 days physical presence + other tests) — global income taxable subject to DTAA
- **Foreign pension + DTAA**: India has DTAA with ~100 countries (US, UK, Germany, Canada, Australia, UAE, Singapore, Mauritius, etc.) — verify per pension origin
- **PIT applies to Indian-source income** at slab (top 30 % + surcharge up to 37 % + 4 % cess)
- **CGT 12.5 % LTCG / slab STCG** on Indian property disposal (post Finance Act 2024)
- **Stamp duty 4–8 %** on property purchase (state)
- **GST 5 %/12 %** on under-construction; 0 % ready/resale
- **No wealth tax** (Wealth Tax Act repealed 2015); **no inheritance tax** (Estate Duty Act repealed 1985); BUT inherited Indian property held at original cost basis for future CGT
- **Health-cover for OCI retiree-residents**: private health insurance dominant; ESIC not applicable; senior-citizen-specific policies (Star Senior, Bajaj Allianz Senior, HDFC ERGO Optima Senior) widely available

### Healthcare access

- **Public**: AIIMS Delhi (apex referral), AIIMS branches (post-2014 expansion), state government hospitals — variable quality; OPD long waits
- **Private**: world-class for cardiac + oncology + medical tourism — Apollo Group, Fortis, Manipal, Max, Medanta, Tata Memorial, Narayana Health — typical OPD INR 800–3,000/visit; specialist INR 1,500–6,000
- **Health insurance** widely available; senior-citizen plans (premium loading 50–100 % over young-adult) cover up to INR 50 lakh
- **International medical evacuation** insurance: Allianz, AXA Assistance, IMG — annual ~USD 800–3,000 for senior

### Verdict for retirement-first buyers

🟡 **Watch / Adapt** — India is excellent for **OCI returning diaspora retirees** (low cost of living relative to OECD; family + linguistic familiarity; world-class private healthcare in metros) but mediocre for **non-Indian-origin foreign retirees** (no retirement-named visa; long-stay friction; cultural + linguistic barrier; air-quality exposure Delhi NCR). Goa + Pondicherry + parts of Kerala (Fort Kochi) historically attract European retirees on tourist-visa-renewal patterns — legally tenuous + not a recommended structure. **🟢 Go** for OCI retirees in Bengaluru / Pune (climate + healthcare + cosmopolitan); **🟡 Watch** for general foreign retirees (visa pathway + air quality + climate trajectory).

---

## Section: `--digital-nomad`

### Visa pathway

India has **NO formal "digital nomad visa"** (a notable absence vs Mauritius PA, UAE Virtual Working visa, Estonia DNV, regional peers). Workable pathways for remote-working visitors:

1. **e-Tourist Visa** — 30/90/365 days; work technically prohibited; short remote-stay tolerated; portal [`https://indianvisaonline.gov.in/`](https://indianvisaonline.gov.in/)
2. **Business Visa (B)** — multi-year multi-entry; for visiting on business; some flexibility for remote work for foreign employer (grey zone — not strictly authorised)
3. **OCI** — for persons of Indian origin only; full work + stay rights
4. **Employment Visa (E)** — sponsored by Indian employer; not for remote-work-for-foreign-employer
5. **Project Visa / Research Visa** — niche

⚠️ Tourist + Business Visa is the **de facto channel** for short-stay remote workers in Goa / Bengaluru / hill-station co-living; for stays > 180 days or ongoing, no clean legal path for non-OCI foreign nationals.

### Connectivity

- **Internet**: fibre FTTH widespread in metros — Reliance Jio Fiber + Airtel Xstream + ACT Fibernet (Bengaluru/Hyderabad/Chennai) + Excitel + BSNL FTTH; gigabit available major cities; 5G live since 2022 (Reliance Jio + Airtel — pan-India rollout 2024–2026)
- **Mobile**: Reliance Jio (largest), Airtel, BSNL, Vi (Vodafone Idea); 5G live; cost: 100 Mbps home INR 700–1,500/month; mobile bundle 2–3 GB/day INR 250–500/month — among lowest data costs globally
- **Co-working**: WeWork India (50+ sites), 91springboard, Awfis, Smartworks, IndiQube, Innov8, Mumbai Coworking, Bombay Connect, Bengaluru BHIVE, Goa-specific (HQ Goa, Outpost, etc.); INR 6,000–20,000/month hot desk; INR 12,000–35,000/month dedicated desk
- **Time zone**: UTC+5:30 (IST) — favours EU + Asia-Pacific overlap; ~10-hour gap to US Pacific, ~10.5 to East Coast

### Cost-of-living for remote worker (Q1 2026)

- **Bengaluru 1-bed Indiranagar / HSR rental**: INR 25,000–60,000/month (~USD 300–710)
- **Goa 1-bed Anjuna / Assagao villa rental**: INR 30,000–120,000/month seasonal
- **Mumbai 1-bed Andheri / Bandra rental**: INR 35,000–80,000/month (~USD 415–950)
- **Pune 1-bed Koregaon rental**: INR 25,000–60,000/month
- **Hyderabad 1-bed Gachibowli rental**: INR 18,000–45,000/month
- **Mid-range eating-out**: INR 600–1,500/meal; budget INR 200–500
- **Domestic help**: INR 5,000–15,000/month
- **Monthly transport**: Ola/Uber/Rapido auto INR 8,000–25,000/month metro typical
- **Co-living**: emerging — Zolo, Stanza Living, Your-Space, Goa coliving (Outpost, Sundream); INR 25,000–80,000/month (incl. utilities + meals)

### Tax position

- **PIT applies to India-source income** for non-residents (residence threshold: 182 days physical presence in India OR 60 days in current year + 365 days in 4 prior years — Income Tax Act §6)
- **Tourist visit ≤ 180 days** → no PIT exposure if no India-source income
- **Crossing 182 days** triggers India tax residence on global income subject to DTAA reliefs (e.g., US/UK/AU treaties)
- **GST 18 %** on services + most consumption (5 % food + transport, 12 % some manufactured)
- **TCS 5 % on outward LRS remittance > INR 7 lakh** (since Oct 2023; verify current)

### Verdict for digital-nomad-first buyers

🟡 **Watch / Adapt** — India is favorable for established remote workers (excellent fibre + low data costs + cosmopolitan metros + low cost-of-living + warm-season Goa/Pondicherry), but **no DNV** + **182-day tax-residence trap** + **clouded-title risk + INR depreciation + monsoon disruption + Delhi NCR air quality** mean medium friction. **Goa** + **Bengaluru** + **Pondicherry** + **Hyderabad** are excellent metro/leisure bases; **Kerala (Fort Kochi, Varkala)** strong for European DNs but legally tenuous on tourist-visa renewals. Consider regional alternatives (UAE Virtual Working visa, Mauritius PA, Estonia DNV) for clean DNV + safer property regime if India-base is not specifically required.

---

## Section: `--macro`

### Headline 2024–2026

- **GDP growth 2024-25**: ~6.4–6.8 % (NSO Q4 2024-25 advance estimates + RBI projections)
- **GDP growth 2025-26**: ~6.5–7.0 % projected (RBI MPR + IMF WEO)
- **GDP growth forecast 2026-27**: ~6.5–7.0 % (IMF WEO Apr 2025; verify current)
- **GDP per capita 2025**: ~USD 2,800 (current); ~USD 11,000 (PPP) — lower middle-income
- **Inflation 2025**: ~4–6 % CPI (RBI target 4 % ± 2 %); core inflation moderating; food + commodity volatile
- **RBI Repo Rate Q1 2026**: ~6.0–6.5 % range (verify current at RBI Monetary Policy)
- **Unemployment** (PLFS): official ~3–4 % (PLFS narrow definition); broader measures higher; structural informal-sector underemployment
- **Public debt / GDP**: ~80–82 % (Centre + States combined; Centre alone ~57 %; high in EMDE comparison; FRBM Act framework)
- **Sovereign rating**: Moody's Baa3 (stable Aug 2024 upgrade outlook), S&P BBB- (stable), Fitch BBB- (stable) — verify current
- **Population**: ~1.428 B (UN World Population Prospects 2024 medium projection — most populous country in the world since 2023)

### Trend drivers (2024–2026)

- **Strong domestic demand + private capex cycle** post-2021 — driver of 6.5 %+ growth band
- **Government capex push** (Infrastructure Pipeline + roads, rail, ports under Gati Shakti National Master Plan)
- **PLI (Production Linked Incentive) schemes** for 14 sectors (electronics, pharma, auto, etc.) — manufacturing FDI tailwind
- **DPI (Digital Public Infrastructure) — UPI / Aadhaar / DigiLocker / ONDC / Account Aggregator** — globally referenced model
- **Real-estate**: strong post-COVID recovery 2022–2025 (premium luxury especially); RERA 2016 institutional improvement; upcoming REITs (Embassy Office Parks REIT, Mindspace REIT, Brookfield REIT, Nexus Select REIT) opened institutional access
- **Public-debt servicing + fiscal-deficit management**: Centre fiscal-deficit target 4.4 % GDP FY26 (FRBM glide path); state-level variable
- **External vulnerability**: oil-import dependence; current-account deficit ~1–2 % GDP; FX reserves comfortable USD 650–700 B
- **Geopolitical tailwind**: "China + 1" supply-chain diversification benefiting India (electronics + pharma + textiles)

### IMF Article IV 2024 + RBI MPR

[IMF 2024 Article IV](https://www.imf.org/en/Countries/IND) flags: (a) need to consolidate fiscal balance + raise tax/GDP; (b) inflation persistence in food; (c) FX reserve buffer adequate; (d) financial-stability strong post-2018 NPA cycle. Real-estate market: expanding cyclically with strong premium-luxury + tier-1 mid-tier + tier-2 emerging; affordability gap in metros widening.

---

## Section: `--demographics`

### Population structure (2011 Census + UN 2024 projection — **NB Census 2021 not yet executed as of May 2026**)

- **Total** (2024 prelim UN): ~1.428 B (most populous country in the world since 2023; 2011 Census recorded 1.21 B)
- **Median age** (2024): ~28 years (one of the world's youngest among large economies)
- **Age 0–14**: ~25 %
- **Age 15–64**: ~68 %
- **Age 65+**: ~7 % (rising)
- **Total fertility rate** (NFHS-5, 2019-21): 2.0 (below replacement; was 2.7 in NFHS-2 1998-99)
- **Urbanisation**: ~36 % urban (2024 UN proj; was 31 % in 2011); rising rapidly

### Geographic distribution

- **Top metros (UN-DESA 2024 projection)**:
  - **Delhi NCR (NCT + Gurgaon + Noida + Ghaziabad + Faridabad)**: ~33M
  - **Mumbai Metropolitan Region**: ~21M
  - **Kolkata Metro**: ~15M
  - **Bengaluru Metro**: ~13M
  - **Chennai Metro**: ~11M
  - **Hyderabad Metro**: ~10M
  - **Ahmedabad Metro**: ~8M
  - **Pune Metro**: ~7M
  - **Surat Metro**: ~7M
  - **Jaipur**: ~4M
  - Source: UN-DESA WUP 2024 + state metropolitan-development-authority projections
- **State population top-5 (Census 2011 base + projection)**: Uttar Pradesh ~240M (~17 % India), Maharashtra ~125M, Bihar ~122M, West Bengal ~99M, Madhya Pradesh ~85M

### Households

- ~330M households (2024 est. — verify Census 2021 when published)
- Average household size: ~4.4 persons (declining from 5.3 in 2001)
- **Owner-occupier rate**: ~87 % nationally (2011 Census); urban much lower (~70 %); metro ~50–65 % rental-dominant
- **NRI/OCI diaspora**: ~32M (Ministry of External Affairs estimate); ~12M NRIs + ~20M PIO/OCI

### Implication for property

- **Demand floor 2025–2050**: young population + urbanisation + new household formation + nuclear-family transition = sustained demand for affordable housing (INR 25–60 lakh segment) + mid-tier (INR 60 lakh–2 Cr); slowing 2050 onwards as TFR < replacement bites
- **Supply pipeline**: PMAY (Pradhan Mantri Awas Yojana — Urban + Gramin) target 4 Cr units by 2025; significant delivery 2015–2025; PMAY 2.0 announced 2024 with INR 10 lakh Cr outlay
- **Premium metro (Mumbai SoBo, Lutyens Delhi, Lavelle Road Bengaluru)**: limited new supply; replacement-only in most prime tracts; long-term scarcity premium
- **Tier-2 + Tier-3 cities** (Pune, Coimbatore, Indore, Lucknow, Surat): strong organic demand + diaspora-funded; tier-1 spillover
- **Diaspora flows**: total personal remittance inflow ~ USD 110–125 B/yr (RBI BOP, FY2023–24 — verify current); a portion flows to NRI/OCI property purchase (no official property-specific breakdown published) — supports diaspora housing demand in Mumbai/Bengaluru/Chennai/Hyderabad/Kerala/Punjab

---

## Section: `--esg`

### Climate-transition exposure

- **NDC (Nationally Determined Contribution) 2022 update**: 45 % reduction in emissions intensity of GDP by 2030 vs 2005; 50 % non-fossil installed electricity capacity by 2030; net-zero by 2070 (PM announcement Nov 2021 COP-26): [`https://moef.gov.in/`](https://moef.gov.in/)
- **National Action Plan on Climate Change (NAPCC) 2008** + 8 missions
- **Long-Term Low Emission Development Strategy (LT-LEDS)** 2022 — submitted at COP-27
- **Renewables share of installed capacity**: non-fossil installed capacity **304,334 MW (~304 GW)** as on **31 Aug 2026** (incl. nuclear + large hydro + wind + solar) per [MNRE](https://mnre.gov.in/en/physical-progress/); non-fossil share **51.93 %** of 513,730 MW total installed as on **31 Dec 2025** per [Ministry of Power / PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2223720&reg=3&lang=2) — the 50 % milestone was reached **June 2025**, five years ahead of the NDC target *(2026-09-18 verified, sources MNRE + Ministry of Power)*; target 500 GW non-fossil by 2030
- **Solar mission**: 100 GW installed cap target Mar 2022 (achieved partially); rooftop solar 40 GW target by 2026
- **Green building**: **IGBC (Indian Green Building Council)** + **GRIHA (Green Rating for Integrated Habitat Assessment)** + **EDGE (IFC)** voluntary schemes; LEED India also active
- **Energy-efficiency**: **ECBC (Energy Conservation Building Code) 2017** voluntary for residential; mandatory for commercial in many states; **Eco-Niwas Samhita 2018** for residential

### Property-level ESG considerations

- **Energy efficiency**: BEE (Bureau of Energy Efficiency) Star Rating (1–5) for AC + appliances mandatory; **Building energy code voluntary residential**; EDGE/IGBC certification growing in premium new-build
- **Solar PV residential**: Net-metering active (state-level — Karnataka, Maharashtra, Gujarat, AP, TN, Telangana lead); typical 5 kWp residential install ~INR 250,000–450,000 (2025–26 est., post-PM Surya Ghar Muft Bijli subsidies — verify current installer quotes); rooftop FiT variable per state
- **Water efficiency**: critical given urban water stress; rainwater harvesting mandatory in many states (e.g., Karnataka KSPCB rule; Tamil Nadu state rule); greywater recycling growing in premium new-build
- **District-level**: GIFT City Gandhinagar (greenfield IFSC), Kakkanad (Kerala IT corridor), Magarpatta (Pune), Hiranandani Powai (Mumbai), DLF Cybercity (Gurugram) — emerging master-planned ESG-marketed developments
- **Air quality**: 🔴 Delhi NCR + IGP belt — material livability + ESG concern; HEPA filters + sealed-envelope HVAC standard in premium homes
- **Heat-resilience retrofit**: increasingly critical for tier-1 metros given heat-wave intensification

### Climate-physical risk (cross-section to `--climate` + `--risks`)

- **Flood resilience**: critical for Mumbai SoBo + Chennai coastal + Bengaluru tech-corridor + Kolkata + Yamuna-corridor Delhi
- **Heat-stress + drought + water-stress**: rising in Indo-Gangetic plain + Rajasthan + Saurashtra; groundwater depletion crisis Punjab + Haryana + parts of TN
- **Coastal SLR**: Mumbai + Chennai + Visakhapatnam + Kolkata 0.3–0.8 m by 2100
- **Earthquake (BIS Zone IV/V)**: NE + Kashmir + Kutch + Indo-Gangetic + Western Ghats moderate; building-code compliance variable

### Social / governance factors

- **RERA 2016** — transparency + escrow + delivery accountability; **major positive ESG-G shift**; enforcement variable per state
- **Insolvency and Bankruptcy Code (IBC) 2016** — homebuyer rights as financial creditors via 2018 amendment; major shift
- **PMAY (affordable housing)** — central + state budget; meaningful supply tailwind
- **Beneficial-ownership disclosure** under Companies Act 2013 + Significant Beneficial Owner (SBO) Rules 2018 — improving corporate-vehicle transparency
- **Benami Transactions Act 1988 + 2016 amendment** — anti-money-laundering anchor
- **PMLA 2002** — strengthened post-2018 amendments; AML compliance for high-value real-estate

### Verdict (ESG lens for typical metro premium apt)

🟡 **Watch** — premium Indian stock has **strong renewable-electricity grid trajectory** (NDC 2030 50 % non-fossil) + reasonable solar-PV economics + RERA 2016 governance shift; **physical climate risk moderate-to-high** by metro (Delhi NCR air quality + heat + monsoon flood; Mumbai coastal SLR + monsoon flood; Bengaluru water stress; Chennai cyclone + flood); **governance / title risk** is the dominant ESG consideration over physical climate. GIFT City + master-planned new districts carry resilience premium. NRI/OCI diaspora investment drives mid-to-premium tier; non-NRI/OCI foreign nationals effectively excluded.

---

## Section: `--exit`

### Resale market liquidity

- **Average days on market 2025 Q4**: ~120–270 days (Mumbai mid-tier); ~180–360 days (Mumbai prime > INR 5 Cr); ~90–180 days (Bengaluru / Pune / Hyderabad mid-tier); ~150–300 days (Delhi NCR mid-tier); ~120–240 days (Goa villa) — per Anarock + Knight Frank India + Liases Foras Q4 2025
- **Cyclical sensitivity**: secondary market is **moderately liquid in metro mid-tier** + **less liquid in premium > INR 5 Cr**; thin in downcycle (2020 COVID + 2018-19 IL&FS / NBFC crisis saw transaction volumes drop materially per Anarock data)
- **NRI/OCI diaspora demand** drives Mumbai / Bengaluru / Chennai / Hyderabad / Kerala premium — concentrated in INR 1–5 Cr segment with USD-equivalent pricing perception
- **Cash-vs-mortgage split**: ~55–65 % of Indian transactions involve a mortgage (CRISIL + ICRA reports 2024); cash-dominant in tier-2/tier-3 and premium > INR 5 Cr (where mortgage LTV 75 % triggers larger downpayment)

### Exit-cost stack (seller side, 2026)

| Item | Cost |
|---|---|
| **Capital Gains Tax LTCG (>24 mo)** | 12.5 % flat without indexation OR 20 % with indexation (grandfathered for pre-23-Jul-2024 acquisitions) |
| **Capital Gains Tax STCG (≤24 mo)** | slab rate (top 30 % + surcharge up to 37 % + 4 % cess) |
| **TDS u/s 194-IA** | 1 % deducted by buyer if consideration ≥ INR 50 lakh — credit at filing |
| **TDS u/s 195 (NRI seller)** | 12.5 % LTCG / slab STCG + applicable surcharge + cess; Form 15CA + 15CB + lower-deduction certificate u/s 197 path |
| **Vendor's advocate fees** | 0.5–1.5 % of value |
| **Real estate broker commission (seller side)** | typically 1–2 % (negotiable; no statutory cap) |
| **Society NOC + share-certificate transfer** (CHS) | INR 25,000–100,000+ |
| **Mutation / Khata closure** | INR 1,000–10,000 |
| **Mortgage early-discharge fee** | per loan terms (typically 0–4 % outstanding) |
| **Section 54 / 54F / 54EC reinvestment cost** | timing-bound; reinvest in 1 residential / 1 NHAI-REC bond up to INR 50 lakh / 6-month / 2-year window |
| **Total exit cost** | **typically 4–7 % of sale price** (excluding CGT) |

### Trading-recharacterization risk

If individual seller is engaged in regular trading (multiple flips / short hold), **Income Tax Department may assess as business income** subject to:
- Slab tax (top 30 % + surcharge 37 % + cess 4 %) vs flat 12.5 % LTCG
- GST registration + 18 % on commercial-trader-margin
- Document genuine investment intent at purchase + multi-year holding

### Liquidity by sub-segment (qualitative, 2026)

| Segment | Liquidity | Notes |
|---|---|---|
| Mumbai mid-tier (INR 1.5–4 Cr) Andheri / Powai / Bandra / Khar | 🟢 strong | Strong NRI + corporate + family demand |
| Mumbai prime (INR 5–25 Cr) Worli / Lower Parel / Bandra W / Juhu | 🟡 selective | HNW Indian + diaspora; thinner pool |
| Mumbai ultra-luxe (INR 25 Cr+) Walkeshwar / Altamount / Malabar Hill | 🟠 thin | Limited buyer pool; ~24+ months sale time |
| Bengaluru mid-tier (INR 1–3 Cr) Indiranagar / HSR / Whitefield / Sarjapur | 🟢 strong | Tech-corridor demand; consistent buyer pool |
| Delhi NCR mid-tier (INR 1.5–4 Cr) South Ex / Gurugram apartments | 🟡 moderate | Strong demand but high stamp-duty + air-quality drag |
| Hyderabad mid-tier (INR 80L–2 Cr) Gachibowli / Hitech / Banjara | 🟢 strong | Tech + healthcare demand surge |
| Chennai mid-tier (INR 80L–2 Cr) OMR / Anna Nagar / Adyar | 🟡 moderate | IT + auto demand + cyclone-exposure premium |
| Pune mid-tier (INR 80L–2 Cr) Hinjewadi / Koregaon | 🟢 strong | Tech-corridor + Mumbai-spillover |
| Goa villa (INR 2–8 Cr) Anjuna / Assagao / Vagator | 🟡 selective | Foreign + diaspora + lifestyle buyers; villa-licensing tightening + thin in monsoon |
| Tier-2 / Tier-3 (Surat, Lucknow, Indore, Coimbatore) | 🟡 moderate | Local + diaspora demand; thinner foreign-buyer pool |
| Builder Floor Delhi NCR (INR 1.5–5 Cr) | 🟡 moderate | Specific to NCR; floor-wise structure |

### Verdict for exit risk

🟢 for typical metro mid-tier (Mumbai, Bengaluru, Pune, Hyderabad); 🟡 for Delhi NCR mid-tier (drag from air quality + stamp duty); 🟠 for Mumbai ultra-luxe + tier-3; 🟡 for Goa villa seasonal. **Document conveyancing chain meticulously at purchase** — sloppy purchase-side title chain compounds exit-side risk (title-buyer due diligence will surface the same gaps). **NRI/OCI selling: pre-clear lower-deduction certificate u/s 197 well in advance** to avoid TDS over-deduction holding sale proceeds for refund cycle (12–18 months typical).

---

## Cost benchmarks (India 2026)

| Item | Cost (INR) | USD est. (84 INR/USD) |
|---|---:|---:|
| **Stamp Duty (state — typical urban residential)** | 4–8 % of higher of consideration / Circle Rate | varies |
| **Registration Fee** | 1 % (some states cap) | varies |
| **GST (under-construction affordable)** | 5 % without ITC | varies |
| **GST (under-construction non-affordable)** | 12 % without ITC | varies |
| **GST (ready-possession + resale)** | 0 % | — |
| **TDS u/s 194-IA** (consideration ≥ INR 50L) | 1 % | varies |
| **TDS u/s 195** (NRI seller) | 12.5 % LTCG / slab STCG + surcharge + cess | varies |
| **CGT LTCG (post-Finance Act 2024)** | 12.5 % flat without indexation | varies |
| **CGT STCG** | slab + surcharge + cess (top ~42.7 %) | varies |
| **Advocate fees (full diligence + drafting)** | 0.5–1.5 % of value | varies |
| **Real estate broker commission** | 1–2 % each side | varies |
| **Society NOC + share-certificate transfer (CHS)** | INR 25,000–100,000+ | $300–$1,200 |
| **Mutation / Khata transfer fee** | INR 1,000–10,000 | $12–$120 |
| **Encumbrance Certificate (15–30 yr)** | INR 200–2,000 | $2.40–$24 |
| **Property valuation (banker's panel)** | INR 5,000–20,000 | $60–$240 |
| **Title insurance (optional)** | ~0.5–1 % of value one-time | varies |
| **Property tax (Mumbai BMC, 2BHK Bandra W typical)** | INR 80,000–200,000/yr | $950–$2,380 |
| **Property tax (Bengaluru BBMP, 1500 sqft house)** | INR 8,000–25,000/yr | $95–$300 |
| **Society dues / maintenance (Mumbai prime CHS)** | INR 25,000–80,000/month | $300–$950 |
| **Society dues (Bengaluru tech-corridor apt)** | INR 5,000–20,000/month | $60–$240 |
| **Solar 5 kWp install (post-Surya Ghar subsidy)** | INR 250,000–450,000 | $2,975–$5,360 |
| **Bore well drill + pump (Bengaluru/Hyderabad)** | INR 1.5–4.5 lakh | $1,790–$5,360 |
| **Septic install (3-stage residential)** | INR 1.5–4 lakh | $1,790–$4,760 |
| **Total transaction cost (cash buyer, urban resale residential)** | **~6–10 % of price** | — |
| **Total transaction cost (with mortgage)** | **~8–12 % of price** | — |

## Active fiscal incentives (2025–2026)

- **PMAY (Pradhan Mantri Awas Yojana — Urban 2.0)** — affordable housing for residents; INR 10 lakh Cr outlay; CLSS (Credit-Linked Subsidy Scheme) for first-time-buyers under EWS/LIG/MIG categories: [`https://pmaymis.gov.in/`](https://pmaymis.gov.in/)
- **PMAY-Gramin** — rural housing
- **Section 80EE / 80EEA**: home-loan interest deduction for first-time-buyers — verify current applicability + caps
- **Section 24(b)**: home-loan interest deduction up to INR 2 lakh / FY (self-occupied)
- **Section 80C**: principal repayment + stamp duty up to INR 1.5 lakh / FY
- **CLSS for MIG-I / MIG-II** under PMAY — 4 % subsidy on home loan up to INR 9 lakh principal — verify current tranche
- **Affordable Housing GST 5 %** vs 12 % standard — for projects meeting carpet area + price thresholds
- **PM Surya Ghar Muft Bijli Yojana** (Feb 2024) — rooftop solar subsidy: up to INR 78,000 + concessional loan; eligible for residential consumers
- **REIT framework (SEBI)**: institutional alternative to direct ownership; AT-tax pass-through; 90 % distribution mandatory
- **No Indian "golden visa"** via real estate — confirm via `--visa`
- **Indian-origin / OCI** — full property + 99 % FEMA equivalence; OCI is the practical "diaspora pathway"

## Common listing platforms

- **MagicBricks** — [`https://www.magicbricks.com/`](https://www.magicbricks.com/) (largest)
- **99acres** — [`https://www.99acres.com/`](https://www.99acres.com/)
- **Housing.com** — [`https://housing.com/`](https://housing.com/)
- **NoBroker** — [`https://www.nobroker.in/`](https://www.nobroker.in/) (FSBO)
- **CommonFloor** + **OLX Real Estate** — secondary
- **Square Yards** — [`https://www.squareyards.com/`](https://www.squareyards.com/)
- **PropertyWala** — [`https://propertywala.com/`](https://propertywala.com/)
- **Sulekha Property** — [`https://www.sulekha.com/`](https://www.sulekha.com/)
- **Knight Frank India**, **Anarock**, **JLL India**, **CBRE India**, **Cushman & Wakefield India** — premium agency portals
- **Developer direct sites**: DLF, Lodha, Godrej Properties, Prestige, Brigade, Sobha, Oberoi Realty, Mahindra Lifespaces, Tata Housing, Embassy, Brookfield, Mindspace, K Raheja Corp, Hiranandani

## Caveats unique to India

- **Adverse possession — the classic NRI absentee trap** 🔴 (2026-05-27 verified): **Limitation Act 1963** Schedule Art. 65 = **12-year limitation period** for adverse possession of private land (Art. 112 = 30-year against government); **s.27 uniquely extinguishes the owner's *right itself*, not just the remedy** — i.e., an absentee NRI flat / ancestral land / agricultural plot + occupant in open, continuous, hostile, exclusive possession ≥12 years can lose title outright. A *lawful* tenant cannot claim adverse possession; the risk is unauthorised occupants / "caretakers" without a written acknowledgement of owner's title. **Mitigants**: registered caretaker agreement acknowledging owner's title (defeats hostility), documented periodic inspections, mutation + property-tax kept current in owner's name, periodic legal notice. Source: Limitation Act 1963 [`https://indiacode.nic.in/bitstream/123456789/1565/5/A1963-36.pdf`](https://indiacode.nic.in/bitstream/123456789/1565/5/A1963-36.pdf).
- **NRI/OCI freely buy residential + commercial; foreign nationals (non-NRI/non-OCI) effectively barred** without RBI prior approval (FEMA 21 §7) + 182-day prior-FY residency; **Pakistani / Bangladeshi / Sri Lankan / Afghan / Chinese / Iranian / Nepalese / Bhutanese nationals require RBI prior approval EVEN for inheritance** (FEMA 21 §6 longstanding RBI restriction — distinct from Press Note 3/2020, which is a corporate-FDI gate for the 7 land-border countries PK/BD/BT/CN/NP/MM/AF)
- **No agricultural / plantation / farmhouse for any non-resident** including NRI/OCI (FEMA 21 §3 proviso)
- **Decentralised cadastre + clouded titles widespread** — engage advocate for 30-yr title chain + Encumbrance Certificate + RERA verification + society NOC; verify both digital (DILRMP / state portal) + paper records
- **Power of Attorney "sale" is NOT a transfer of title** per Suraj Lamp 2011 — only registered Sale Deed transfers title; reject any GPA-based "sale" structure
- **Stamp duty 4–8 % per state + 1 % registration** + endemic under-declaration — state revenue departments increasingly assertive on Circle Rate floor; assume declared = floor, not market clear
- **Finance Act 2024 LTCG 12.5 % flat without indexation** (sales on/after 23 Jul 2024) — major reform; grandfathering option for pre-23-Jul-2024 acquisitions allows 20 % with indexation; verify under current Finance Act
- **GST 5 %/12 % under-construction** (without ITC); 0 % ready/resale — verify "VAT-inclusive" vs "VAT-exclusive"
- **RERA 2016 mandatory** for projects > 500 sqm or 8 units — verify project + agent registration on state RERA portal (per state)
- **CHS Society NOC** mandatory for Mumbai/Pune cooperative-society apartments — society can refuse (subject to reasonable grounds + court appeal)
- **Apartment-vs-CHS structure** distinction (Maharashtra Apartment Ownership Act 1970 vs Maharashtra Cooperative Societies Act 1960) — affects share-certificate vs deed-of-apartment
- **Builder Floor (Delhi NCR)** — floor-wise undivided-share split; verify per-floor sale deed registered + freehold conversion if state-leasehold (DDA conversion required for many)
- **DDA leasehold-to-freehold conversion** in Delhi — pending for many parcels; affects loan eligibility + transferability
- **Air-pollution exposure 🔴 Delhi NCR + Indo-Gangetic** — material livability + property-desirability drag; HEPA filters + sealed-envelope HVAC standard in premium homes
- **Heat-wave + monsoon-flood + earthquake (BIS Zone IV/V) + cyclone (east coast + west coast trending up)** — multi-hazard environment; verify BIS IS 1893:2016 zone + RERA structural-engineer stamp + society STP + drainage
- **Goa villa "lease-cum-license" structures** — historically used to skirt foreigner-restriction; FEMA-compliant only for legitimately resident foreigners; risky for non-resident foreign nationals
- **Press Note 3 (2020) FDI gate** for Pakistani / Bangladeshi / Bhutanese / Chinese / Nepalese / Myanmarese / Afghan beneficial owners — applies to corporate vehicles
- **No dual citizenship** — Citizenship Act §9; OCI is NOT citizenship
- **No golden visa via real estate** — distinct from UAE / Singapore / regional peers
- **Liberalised Remittance Scheme (LRS) USD 250k/individual/FY cap** for outbound remittance — affects buying foreign property + remitting Indian sale proceeds (NRI repatriation rules layered on top)
- **TCS 5 %** on outbound LRS remittance > INR 7 lakh (since Oct 2023; verify current)
- **DILRMP digitisation** ongoing 2008–2026 — Karnataka + Maharashtra + Telangana + AP + TN + Kerala + Delhi lead; verify status per parcel

## Reddit / forum sources

- **r/india** — general (mixed; periodic property threads)
- **r/IndiaInvestments** — financial including real-estate sub-threads
- **r/Mumbai**, **r/bangalore**, **r/delhi**, **r/Chennai**, **r/Pune**, **r/hyderabad** — city-specific
- **r/NRI** — NRI/OCI-specific incl. property
- **r/RealEstateIndia** — focused
- **TeamBHP** — auto-forum but property sub-forums for NRI/OCI buying
- **MoneyControl Community** — financial forum
- **Indian Real Estate Forum** + various Facebook groups (anecdotal — treat with care)
- ⚠️ Forum-quality caveat: many anecdotes about "title verification I did myself" — title fraud is real + material; treat advocates as essential not optional

## Verification authorities

| Authority | When to call |
|---|---|
| **State Sub-Registrar Office (SRO)** | Sale Deed registration; Encumbrance Certificate |
| **State Revenue / Land Records Department** (Tahsildar / Mandal) | Mutation; RoR; Khata; survey records |
| **State RERA Authority** (per state) | Project + agent registration; complaints history |
| **Municipal Corporation / ULB** | Property tax; Khata / mutation; building approvals; Occupancy Certificate |
| **State Town Planning + Development Authority** | Layout sanctioning; FSI/FAR; building permission |
| **Income Tax Department + CBDT** | TDS u/s 194-IA / 195; CGT filing; lower-deduction certificate |
| **GST Council + State GST** | GST on under-construction; landlord's threshold compliance |
| **Reserve Bank of India (RBI)** | FEMA 21 approval; LRS reporting; foreign-buyer permission |
| **MEA + Bureau of Immigration** | OCI; visa; FRRO |
| **MoEFCC + State Pollution Control Board (SPCB)** | EIA; consent for STP; environmental clearance |
| **NHAI + State PWD** | Highway alignment; land acquisition under RFCTLARR Act 2013 |
| **CPCB + IMD + NCS + GSI** | Air quality; weather; seismic; geological |
| **SEBI** | REIT regulation |
| **IRDAI** | Insurer + title-insurance regulation |
| **Bar Council of India + State Bar Council** | Advocate registration |
| **Cooperative Department (state)** | CHS bylaws + transfer + society audit |
| **NDMA + state Disaster Management Authority** | Hazard maps; disaster history |
| **National Housing Bank (NHB)** | Residex; HFC refinance |
| **NCRB + State Police** | Crime stats; FIR registration |

## Quirks to know

- **Survey No. / Khata / Khasra / Patta — five different identifiers** depending on state; learn the state-specific identifier before any title work
- **CHS share-certificate vs Apartment deed** — Maharashtra cooperative-society vs apartment-deed distinction is material for transfer mechanics + ownership rights
- **Builder Floor (Delhi NCR specific)** — floor-wise sale deed + undivided-share split; not standard apartment-deed
- **DDA leasehold conversion** to freehold pending in many Delhi parcels; affects loan + transferability
- **Tax Identification (PAN)** mandatory for all transactions ≥ INR 50,000; foreign nationals: PAN issuance via Indian Mission abroad or e-PAN portal
- **Aadhaar (UID)** — biometric ID for Indian citizens; NRI/OCI eligible after 182-day residence; **NOT mandatory for foreign nationals** but Aadhaar-Sale Deed linkage being phased in
- **Ready Reckoner / Circle Rate / Guideline Value** is the stamp-duty floor — actual market typically 10–40 % higher; periodic state revisions
- **Affordable housing definition** under GST: carpet ≤ 60 sqm metro / ≤ 90 sqm non-metro AND price ≤ INR 45 lakh — verify both conditions
- **RERA carpet area** mandatory disclosure since 2016; pre-RERA listings used "super built-up" with 25–35 % loading
- **Power of Attorney + Will + Family Settlement** — common but NOT title-transferring per Suraj Lamp 2011
- **Hindu Undivided Family (HUF)** + Hindu Succession Act 1956 + 2005 amendment — daughters' coparcenary rights post-2005 trigger retrospective claims on ancestral property
- **Tribal-area land restrictions** (Schedule V + 6th Schedule states + specific NE) — separate consents required
- **Land-acquisition risk** under RFCTLARR Act 2013 — verify government notifications + NH/SH/metro alignment
- **RERA escrow 70 %** of project receipts must go to dedicated bank account (RERA §4(2)(l)(D)) — major fraud-mitigation since 2017
- **Top developers** (DLF, Lodha, Godrej, Prestige, Brigade, Sobha, Oberoi Realty, Embassy) dominate organised supply — pre-launch + under-construction from a top-10 carries less completion risk than a small unorganised developer

## Source URL templates

| Source | URL |
|---|---|
| Income Tax Department | [`https://incometaxindia.gov.in/`](https://incometaxindia.gov.in/) |
| RBI (Reserve Bank of India) | [`https://www.rbi.org.in/`](https://www.rbi.org.in/) |
| MCA (Ministry of Corporate Affairs) | [`https://www.mca.gov.in/`](https://www.mca.gov.in/) |
| MoHUA (Ministry of Housing and Urban Affairs) | [`https://mohua.gov.in/`](https://mohua.gov.in/) |
| MNRE (Ministry of New and Renewable Energy) | [`https://mnre.gov.in/`](https://mnre.gov.in/) |
| MoEFCC | [`https://moef.gov.in/`](https://moef.gov.in/) |
| MoSPI (Ministry of Statistics and Programme Implementation) | [`https://mospi.gov.in/`](https://mospi.gov.in/) |
| MoRTH (Ministry of Road Transport and Highways) | [`https://morth.nic.in/`](https://morth.nic.in/) |
| MEA (Ministry of External Affairs) | [`https://mea.gov.in/`](https://mea.gov.in/) |
| MHA (Ministry of Home Affairs) | [`https://www.mha.gov.in/`](https://www.mha.gov.in/) |
| Bureau of Immigration | [`https://boi.gov.in/`](https://boi.gov.in/) |
| Ministry of Jal Shakti | [`https://jalshakti-ddws.gov.in/`](https://jalshakti-ddws.gov.in/) |
| DPIIT | [`https://dpiit.gov.in/`](https://dpiit.gov.in/) |
| NHB (National Housing Bank) — Residex | [`https://residex.nhbonline.org.in/`](https://residex.nhbonline.org.in/) |
| NHAI | [`https://nhai.gov.in/`](https://nhai.gov.in/) |
| CBDT (TDS / CGT) | [`https://incometaxindia.gov.in/`](https://incometaxindia.gov.in/) |
| GST Council | [`https://gstcouncil.gov.in/`](https://gstcouncil.gov.in/) |
| CBIC | [`https://www.cbic.gov.in/`](https://www.cbic.gov.in/) |
| SEBI | [`https://www.sebi.gov.in/`](https://www.sebi.gov.in/) |
| IRDAI | [`https://www.irdai.gov.in/`](https://www.irdai.gov.in/) |
| BIS (Bureau of Indian Standards — IS 1893) | [`https://www.bis.gov.in/`](https://www.bis.gov.in/) |
| IMD (India Meteorological Department) | [`https://mausam.imd.gov.in/`](https://mausam.imd.gov.in/) |
| NCS (National Centre for Seismology) | [`https://seismo.gov.in/`](https://seismo.gov.in/) |
| GSI (Geological Survey of India) | [`https://www.gsi.gov.in/`](https://www.gsi.gov.in/) |
| CWC (Central Water Commission) | [`https://cwc.gov.in/`](https://cwc.gov.in/) |
| CPCB | [`https://cpcb.nic.in/`](https://cpcb.nic.in/) |
| NDMA | [`https://ndma.gov.in/`](https://ndma.gov.in/) |
| Bhuvan ISRO geo-portal | [`https://bhuvan.nrsc.gov.in/`](https://bhuvan.nrsc.gov.in/) |
| Census of India | [`https://censusindia.gov.in/`](https://censusindia.gov.in/) |
| DILRMP | [`https://dilrmp.gov.in/`](https://dilrmp.gov.in/) |
| OCI Services | [`https://ociservices.gov.in/`](https://ociservices.gov.in/) |
| e-FRRO | [`https://indianfrro.gov.in/`](https://indianfrro.gov.in/) |
| Indian Visa Online | [`https://indianvisaonline.gov.in/`](https://indianvisaonline.gov.in/) |
| PMAY-Urban | [`https://pmaymis.gov.in/`](https://pmaymis.gov.in/) |
| State RERA — Maharashtra | [`https://maharera.maharashtra.gov.in/`](https://maharera.maharashtra.gov.in/) |
| State RERA — Karnataka (KRERA) | [`https://rera.karnataka.gov.in/`](https://rera.karnataka.gov.in/) |
| State RERA — Tamil Nadu (TN-RERA) | [`https://rera.tn.gov.in/`](https://rera.tn.gov.in/) |
| State RERA — Delhi | [`https://rera.delhi.gov.in/`](https://rera.delhi.gov.in/) |
| State Land Records — Maharashtra MahaBhulekh | [`https://bhulekh.mahabhumi.gov.in/`](https://bhulekh.mahabhumi.gov.in/) |
| State Land Records — Karnataka Bhoomi | [`https://landrecords.karnataka.gov.in/`](https://landrecords.karnataka.gov.in/) |
| State Land Records — TN Patta Chitta | [`https://eservices.tn.gov.in/`](https://eservices.tn.gov.in/) |
| State Land Records — Telangana Bhu Bharati (formerly Dharani) | [`https://bhubharati.telangana.gov.in/`](https://bhubharati.telangana.gov.in/) |
| State Stamps & Registration — Maharashtra IGR | [`https://igrmaharashtra.gov.in/`](https://igrmaharashtra.gov.in/) |
| State Stamps & Registration — Karnataka Kaveri | [`https://kaveri.karnataka.gov.in/`](https://kaveri.karnataka.gov.in/) |
| Listing platforms | MagicBricks · 99acres · Housing.com · NoBroker · Square Yards |
| Anarock | [`https://www.anarock.com/`](https://www.anarock.com/) |
| Knight Frank India | [`https://www.knightfrank.co.in/`](https://www.knightfrank.co.in/) |
| Indian Banks' Association (IBA) | [`https://www.iba.org.in/`](https://www.iba.org.in/) |
| Bar Council of India | [`https://www.barcouncilofindia.org/`](https://www.barcouncilofindia.org/) |
| FEMA full text + RBI Master Directions | [`https://www.rbi.org.in/Scripts/BS_FemaNotifications.aspx`](https://www.rbi.org.in/Scripts/BS_FemaNotifications.aspx) |

## Status

**Confidence**: HIGH

**Last verified**: 2026-05-27 (non-fossil capacity + share corrected 2026-09-18 per MNRE physical-progress + Ministry of Power PIB; validation sweep — adverse possession Limitation Act 1963 Art. 65/112 + s.27 added to Caveats; FEMA 21 §6 8-list vs Press Note 3 7-list disambiguated; FEMA 21(R)/2018-RB lead-warning corrected)

**Researched by**: Sonnet 4.6 + Opus 4.7 (parallel-subagent batch, 2026-05)

**Notes**: Locked-in via primary government sources: FEMA Notification 21(R)/2018-RB + RBI Master Direction on Acquisition and Transfer of Immovable Property under FEMA (RBI primary — **foundational regime: NRI/OCI freely buy residential + commercial; foreign nationals (non-NRI/non-OCI) effectively barred without RBI §7 approval + 182-day prior-FY residency; Pakistani / Bangladeshi / Sri Lankan / Afghan / Chinese / Iranian / Nepalese / Bhutanese nationals require RBI prior approval EVEN for inheritance; NO non-resident may buy agricultural / plantation / farmhouse — flag prominently to any foreign buyer**); Citizenship Act 1955 + §7A OCI; Press Note 3 / 2020 (DPIIT FDI gate for neighbouring countries); Income Tax Act 1961 + Finance (No. 2) Act 2024 (**MAJOR REFORM: LTCG 12.5 % flat without indexation for sales on/after 23 Jul 2024 — supersedes prior 20 % with indexation; grandfathering option for pre-23-Jul-2024 acquisitions**); RERA 2016 (mandatory project + agent registration > 500 sqm / 8 units; per-state RERA portal verification); GST Act 2017 + CBIC Circulars (5 % affordable / 12 % non-affordable under-construction; 0 % ready/resale); state Stamp Acts + Registration Act 1908 (4–8 % stamp duty + 1 % registration per state); Indian Stamp Act 1899; Transfer of Property Act 1882; Suraj Lamp & Industries v. State of Haryana (Supreme Court 2011 — only registered Sale Deed transfers title, NOT GPA); BIS IS 1893:2016 (seismic zoning); IMD + NCS + GSI + CPCB + NDMA (multi-hazard primary). **CADASTRE IS DECENTRALISED PER STATE — no national cadastre; clouded titles widespread; engage advocate for 30-yr title chain + Encumbrance Certificate + RERA verification + Survey No. / Khata / Khasra / Patta state-specific identifier; verify both DILRMP digital + paper records.** **AGRICULTURAL / PLANTATION / FARMHOUSE LAND BARRED for ALL non-resident foreign nationals INCLUDING NRI/OCI** (FEMA 21 §3 proviso). **Title insurance NOT mandatory + thin market** — engage advocate for due-diligence as primary defence. **Watch list 2026**: Finance Act 2026 (Budget February 2026 may touch LTCG / GST / RBI policy); state stamp duty cuts (episodic state-budget tools); RERA enforcement cycle per state; DILRMP completion phase; Census 2021 publication delay (UN proj currently used); RBI repo rate path; INR depreciation cycle vs USD. State-level variance: Maharashtra (CHS-dominant + women's stamp-duty concession), Karnataka (RERA + Kaveri leadership), Tamil Nadu (Patta Chitta + 7 % stamp duty), Telangana (Dharani controversy), Delhi NCR (DDA leasehold-to-freehold + air pollution + Builder Floor specific), Goa (villa-licensing tightening + foreign-buyer scrutiny). **NRI/OCI is the ONLY clean path for diaspora foreign-buyers**; non-NRI/non-OCI foreign nationals face structural friction — recommend RBI permission inquiry + 182-day residency build before purchase intent.
