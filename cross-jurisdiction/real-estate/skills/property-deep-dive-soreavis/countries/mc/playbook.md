# Monaco (MC) — Property Due-Diligence Playbook

**Status**: ✅ fully populated as of 2026-05-01
**Currency**: EUR (Monetary Convention with France, 24 Dec 2001 / in force 2002 — Monaco mints euro coins under EU agreement; not an EU member state)
**Lang**: French (sole official); Monégasque (heritage / signage); Italian + English commonly understood. **Notarial acts are drawn in French.**

---

## Country profile

Microstate of ~2.08 km² on the Côte d'Azur (~38,367 residents end-2023, IMSEE — see `--demographics`). Constitutional monarchy under House of Grimaldi. **Most expensive resale market in the world**: 2024 IMSEE "Marché Immobilier Monégasque" weighted-average resale **€51,418/m²** (2023: €51,103). Civil-law jurisdiction descended from French Code Napoléon — notarial transfer process tracks France closely (notaire monégasque mandatory). **Three structural quirks set Monaco apart from every neighbour**: (1) NO annual property tax (taxe foncière), (2) NO capital-gains tax on resale, (3) NO personal income tax for Monaco residents (except French nationals under the 1963 bilateral). All three are stable since the 1963 fiscal convention with France and confirmed by `gouv.mc` 2024-25. Critical 2024 reform: **Loi n° 1.560 (3 December 2024)** closed the SCI loophole that historically let buyers pay 7.5% via opaque civil-society structures — now uniformly 4.5% droits d'enregistrement on the underlying property whether the vehicle is direct or SCI. Foreign-buyer regime is **OPEN** (no nationality restriction in the private sector / domaine privé); the SECTEUR DOMANIAL (state-owned social housing reserved for Monégasques) is closed to non-Monégasques and irrelevant to foreign-buyer analysis.

---

## Section: `--price`

**Primary index**: **IMSEE — Observatoire de l'Immobilier**, "Marché Immobilier Monégasque" (annual + quarterly resale & new-build series).
- https://www.monacostatistics.mc/Logement-Immobilier (publication landing)
- Latest annual report cited: "Le Marché Immobilier Monégasque 2024" (published 2025)

**2024 figures (IMSEE 2024 annual, published 2025)**:
- **Resale**: 469 transactions; aggregate value €2.789 bn; weighted-average **€51,418/m²** (vs €51,103 in 2023, +0.6% nominal)
- **New-build sales (ventes neuves)**: thinly populated cohort; recent programmes (Mareterra, Testimonio II tranches) have asked >€100,000/m² on the apex floors per agency reporting — verify per-listing
- **Rental market**: same observatoire publishes a parallel rental volume series (loyers "secteur libre" outside the rent-controlled secteur protégé / domaine domanial)

**By quartier** (IMSEE 2024 weighted-average resale €/m², where sample size permitted publication):

| Quartier | 2024 resale €/m² (~) | Note |
|---|---|---|
| Monte-Carlo | ~€60,000 | highest band; Carré d'Or (around the Casino) higher still |
| La Rousse / Saint Roman | ~€55,000 | tower stock (Le Roccabella, Le Mirabeau, Le Millefiori) |
| Larvotto / Bas Moulins | ~€50,000 | beachfront; affected by Mareterra extension |
| Monaco-Ville (Le Rocher) | ~€45,000 | thin cohort; heritage stock, very few sales |
| La Condamine | ~€45,000 | port, mid-decile turnover |
| Fontvieille | ~€42,000 | reclaimed land (1970s); modern apartments |
| Moneghetti / Saint-Michel | ~€40,000 | edge of principality, larger units |

(per IMSEE 2024 quartier breakdown — exact figures vary by ±5-10% depending on which quartiles are aggregated; **always pull the latest IMSEE PDF before quoting**)

**⚠️ Sample-size warning**: at ~470 resale transactions/yr across 9 quartiers, several quartier-quarter cells fall below IMSEE's publication threshold (n<5 may be suppressed). For low-volume quartiers (Monaco-Ville, Saint-Michel) the annual figure is the only stable signal.

**Listings**:

| Portal | URL | Notes |
|---|---|---|
| Chambre Immobilière Monégasque (CIM) | https://www.chambre-immobiliere-monaco.mc/ | Official agents' chamber; member directory, not a listings aggregator |
| Savills Monaco | https://www.savills.mc/ | Established in market |
| Knight Frank Monaco | https://www.knightfrank.com/property-for-sale/monaco | Cross-references KF Wealth Report data |
| Monte-Carlo Sotheby's International Realty | https://www.montecarlo-sothebysrealty.com/ | Luxury / Carré d'Or focus — agency tier, seller-controlled |
| La Costa Properties | https://www.lacosta-properties-monaco.com/ | Mid-large local independent |
| Dotta Immobilier | https://www.dotta.mc/ | Established local family office |

(Listing claims tagged `(per listing — verify with notaire monégasque)` — Monaco has no public cadastre lookup; even price/m² requires CIM member to pull comp data.)

**Verdict bands** (Monaco-specific, given concentrated market):
- 🟢 within ±10% of IMSEE quartier weighted-average for the year
- 🟡 ±20%
- 🟠 ±30%
- 🔴 >±30% — verify whether seller is pricing in trophy floor / sea view / private terrace; Monaco's intra-building variance can legitimately reach +50% for top floor vs ground floor in the same tower

---

## Section: `--traffic`

- **Direction de la Prospective, de l'Urbanisme et de la Mobilité (DPUM)** within the Département de l'Équipement, de l'Environnement et de l'Urbanisme — owns roads + traffic data
- **Compagnie des Autobus de Monaco (CAM)**: https://www.cam.mc/ — bus network
- Real-time via Google Maps / Waze (well-covered)
- OSM Overpass universal — see `shared/amenities-osm.md`
- **Monorail / lifts (ascenseurs publics)**: est. ~80 free public lifts and travelators connect quartiers across the steep terrain (no published Mairie/DPUM inventory cited — count is an estimate; verify with the Mairie de Monaco public-lift inventory) — relevant for "walkability" assessment of Moneghetti / Monte-Carlo upper streets

**Traffic context**: ~50,000 cross-border commuters daily from FR (Beausoleil, Roquebrune-Cap-Martin, Menton) and IT (Ventimiglia, Bordighera). Peak 8-10am inbound, 5-7pm outbound. Tunnel + boulevard Princesse Charlotte saturated. **Implication for noise**: any street-front apartment on a corniche or at A8 spurs (Tunnel Rainier III) carries elevated traffic-noise exposure.

---

## Section: `--tax`

### Transfer tax on purchase (droits d'enregistrement)

- **Standard 4.5%** of the higher of price / market value, on resale acquisition by a private buyer (residents and non-residents alike). Source: Code de l'enregistrement; rate confirmed `monservicepublic.gouv.mc` 2024-25 (2026-05-27 verified, source `monservicepublic.gouv.mc` — post-PR #184 portal rename from `service-public-particuliers.gouv.mc`).
- **Reduced 1%** for acquisitions by Monégasques and certain qualifying residents (specific schemes — verify per-buyer with the notaire; do NOT assume).
- **Loi n° 1.560 du 3 décembre 2024**: closed the SCI / civil-society loophole that historically let opaque vehicles attract 7.5% (the higher rate that applied when the vehicle owner was anonymous / non-named). After the reform, **transfers via SCI / société civile particulière are taxed at the same 4.5%** as direct acquisitions, **provided beneficial owners are identified to the tax administration**. Where beneficial ownership cannot be identified (anonymous foreign trusts, opaque offshore vehicles), the **7.5% rate continues to apply** as the punitive default — verify the exact rate applicable to any non-SCI / non-direct vehicle with the notaire monégasque before signing the compromis. Source: Journal de Monaco published text — verify exact effective date and transitional regime with the notaire for any SCI-held transaction in 2024-25 (2026-05-27 verified, source Cases & Lacambra + Journal de Monaco).
- **Notaire fees (émoluments)**: regulated by **Loi n° 1.014 du 4 mai 1981** governing the profession of notaire monégasque + subsequent grand-ducal-equivalent ordinances. Practitioner-quoted band: **~1.5% of price** all-in for typical resale (variable by price tranche; degressive scale similar to French notarial barème). **Always request the notaire's projet d'émoluments before signing the compromis**.
- **Total acquisition cost** (resale, private buyer, no SCI): typically ~6% all-in (4.5% droits + ~1.5% notaire + minor débours). New-build: see VAT below — TVA 20% replaces droits d'enregistrement on first sale by promoter to end-buyer.

### Annual property tax (taxe foncière)

- **NONE.** Monaco does NOT levy any recurring annual property tax on owners. **This is structural and confirmed multiple sources** (gouv.mc fiscalité pages 2024; PwC Worldwide Tax Summaries Monaco; OECD profile). No municipal equivalent either — there is no commune separate from the principality.
- A small **taxe d'habitation** does NOT exist in Monaco (FR-style). The only annual levy adjacent to property is the rental-related taxe sur les contrats locatifs (see Rental).

### Capital Gains Tax (CGT) on resale

- **NONE** for resident or non-resident sellers on Monaco real estate. Monaco does NOT tax personal capital gains. Source: gouv.mc fiscalité; PwC Monaco summary 2024.
- **Caveat — French nationals**: under the **Convention fiscale franco-monégasque du 18 mai 1963**, French nationals resident in Monaco remain liable to French income tax (and therefore French CGT mechanics on real estate, including the FR plus-value immobilière regime) as if they were French residents. **This is a Monaco-side fiscal-citizenship feature unique to FR nationals** — does NOT extend to other nationalities. Verify with FR-MC dual-tax adviser if the seller carries a French passport.

### Personal income tax

- **NONE for non-French Monaco residents.** Confirmed at `gouv.mc` 2024 + Convention 1963.
- French nationals resident in Monaco: **subject to French income tax** under Article 7 of the 1963 Convention. (Italian, UK, German, Russian, US, etc. residents pay no Monaco income tax — but their home-country tax residency rules still apply, e.g., US worldwide taxation regardless of Monaco residency.)
- **Société-side**: Impôt sur les Bénéfices (ISB) at **25%** (gouv.mc fiscalité entreprises 2024) applies to companies deriving >25% of turnover outside Monaco; pure-Monaco companies generally exempt. Property-investment SCIs are typically tax-transparent; verify with notaire.

### Rental income & rental-side levies

- **Taxe sur les contrats locatifs (rental contract tax)**: ~**1%** of annual rent, payable on registration of the lease at the Direction des Services Fiscaux. Standard practice is **landlord-paid** but custom may shift to tenant — verify per-lease.
- **No rental-income personal tax** for non-French Monaco resident landlords (income tax = 0%). French national landlords pay French income tax on Monaco rental income via the 1963 Convention.
- **Non-resident landlords** (resident outside Monaco renting out Monaco property): no Monaco income tax, but home-country reporting + tax residency rules apply.

### VAT (TVA)

- **20% standard rate** on new-build first sale (promoter → end-buyer), aligned with French VAT. Reduced rates exist for some categories (5.5% certain renovation works) — verify per-project. Confirmed `gouv.mc` 2024.
- **Resale of existing property = exempt** (TVA does not apply on second-hand transactions; droits d'enregistrement applies instead).

### Inheritance & gift duty (droits de succession et de donation)

- **Direct line (parent ↔ child, spouse)**: **0%**
- **Sibling**: 8%
- **Uncle/aunt/nephew/niece**: 10%
- **Other relatives**: 13%
- **Unrelated**: 16%
- Source: gouv.mc fiscalité succession 2024. Worth knowing because Monaco's "0% for direct line" is more permissive than France's barème (which taxes >€100k spouse-and-child transfers at 5-45%).

---

## Section: `--rental`

### Long-let market

- Monaco rental market is bifurcated into **secteur libre** (free market — almost all foreign tenants) and **secteur protégé / secteur domanial** (rent-controlled stock reserved for Monégasques and long-term residents under specific eligibility rules). **Foreign-buyer investment thesis applies only to secteur libre** — domanial is not transferable.
- Yields are structurally low — Knight Frank / Savills market reports place gross **prime-residential yield at ~2-3%** (consistent with London W1 / Geneva centre / Paris VIIIe). Compute: typical 2-bed apartment €4M acquisition, asking rent ~€10-12k/month → ~3.0-3.6% gross.
- Rental contracts: standard 1-year renewable for furnished, 3-year for unfurnished (loi monégasque tracks French civil custom). Registered at Direction des Services Fiscaux (1% taxe — see above).

### STR / Airbnb (short-term lets)

- **Hôtellerie** is regulated by the **Direction du Tourisme et des Congrès (DTC)** + **Direction de l'Expansion Économique** under the **Loi n° 1.482 du 17 décembre 2019** and accompanying ordonnances on hébergement touristique.
- **Short-term tourist letting requires declared activity / autorisation** — practical effect: Airbnb-style operation by a private apartment owner is heavily restricted; most non-hotel short-let supply comes through licensed serviced-apartment operators. Inside Airbnb (snapshot date not recorded here — verify against the current Inside Airbnb snapshot) shows ~150-300 active Monaco listings (small absolute count) — most are serviced-apartment hybrids, not private-host short-lets.
- **Condominium consent** universally required (règlement de copropriété typically forbids tourist activity in residential towers).
- Tax: STR receipts are subject to ISB if vehicle is corporate, or rental-tax if individual; consult local fiscaliste.
- **Practical**: STR is NOT a viable yield strategy for foreign buyers in Monaco residential — the structural answer is buy-and-hold for capital + lifestyle, not BnB.

---

## Section: `--work=<profession>`

Banking + family-office (~120+ regulated banks/private banks per CCAF), insurance, superyacht industry (Port Hercule), gaming (SBM — Société des Bains de Mer, Casino + hotels group), cruise tourism, light services. Workforce ~58,000 (IMSEE 2023) of which ~75% are cross-border commuters (FR/IT). **Job market for new arrivals is residency-permit-gated** — see `shared/visa-programs.md` for Monaco residency mechanics; a property purchase or rental + bank deposit is the typical entry path.

---

## Section: `--risks`

### Seismic

- Mediterranean seismic exposure; Monaco lies on the **Ligurian Basin margin**. **Eurocode 8 zone**: low-to-moderate. Last significant felt event in the area: **23 February 1887 Ligurian (Imperia) earthquake** (M~6.3-6.5), which caused damage along the Riviera including Mentone-Monaco. **No major seismic event since.**
- Modern construction (most stock 1960s-2020s reinforced concrete towers on bedrock) is well-engineered for the hazard; older Rocher / Condamine masonry has lower intrinsic resistance.

### Flood

- **Negligible riverine flood**: no major river within Monaco; the Vallon de Sainte-Dévote and Vallon des Gaumates are short, mostly culverted channels. The **Roya/Var** basins are >20 km west and unaffect Monaco directly (Roya 2020 floods devastated FR Roya valley but did not reach Monaco).
- **Coastal storm surge / wave overtopping**: relevant for Larvotto / Bas Moulins / Mareterra at Mediterranean storm peaks. Mareterra (delivered 2024) is engineered to current sea-level + storm-surge projections; older Larvotto stock has lower freeboard.
- Source: gouv.mc Plan Climat / Plan Bleu Monaco; Mediterranean Sea-Level Rise Service Climate Central tools cover Monaco coast.

### Climate / sea-level rise

- **Plan National pour l'Énergie et le Climat (PNEC)** + **Plan Climat-Énergie** under Monaco's Net Zero 2050 commitment. https://transition-energetique.gouv.mc/
- Sea-level rise: Monaco has limited low-elevation footprint (most stock is on bedrock cliff faces); flagship coastal exposure is **Larvotto / Bas Moulins / Fontvieille port-side / new Mareterra** — climate-risk underwriting will increasingly differentiate by elevation above MSL over 30-50 yr horizon.

### Wildfire

- Negligible — almost no wildland-urban interface inside the principality. Adjacent FR Riviera vegetation fires (Esterel, Cap-Martin maquis) do not threaten Monaco built stock directly. AC/HVAC supply continuity is a more relevant heat-related risk.

### Mandatory diagnostics

- **Diagnostic de Performance Énergétique (DPE Monaco)**: Monaco does NOT have an EPC regime equivalent to French DPE for transactional disclosure as of 2025 — energy assessments are voluntary / promoter-supplied for new builds, not a sale-blocking diagnostic. **(Verify with notaire — possible regulatory evolution under PNEC; surface as confidence: MEDIUM.)**
- **Asbestos / lead / termite / radon**: no consolidated mandatory diagnostic pack at point of sale equivalent to French CREP/ERP/amiante. Pre-1997 buildings should still trigger asbestos awareness during renovation works (Code de la construction monégasque).
- **Building safety**: Direction de la Prospective, de l'Urbanisme et de la Mobilité (DPUM) controls planning permits; buyer should verify all extensions / facade works carry valid autorisation de construire (look-through risk on older Carré d'Or apartments where facade modifications were unpermitted).

---

## Section: `--mains`

### Cadastre & Land Registry — RESTRICTED ACCESS

- **NO public online cadastre** equivalent to French `cadastre.gouv.fr`. The cadastral plan is held by **Direction du Domaine** + **Direction du Contrôle des Concessions et Tarifications** under the Département des Finances et de l'Économie. https://service-public-entreprises.gouv.mc/
- Property transactions are registered at the **Direction des Services Judiciaires** + **Notaires de Monaco**. Title chain is established by notarial-deed history, NOT by a self-serve title search.
- **Foreign-buyer practical**: you cannot self-serve a title search; instruct the notaire monégasque to pull the full historical chain at the Direction de l'Enregistrement et du Timbre. Cost: typically included in notarial émoluments.
- **Notaires**: small profession (~3-5 active notarial offices); buyer chooses notaire (single-notaire model — one notaire can act for both sides, distinct from FR two-notaire common practice). Member directory: **Chambre des Notaires de Monaco** (verify URL with the Chambre — historical: chambredesnotaires.mc).

### Utilities

- **Electricity**: **Monaco Distribution (SMEG — Société Monégasque de l'Électricité et du Gaz)**: https://www.smeg.mc/ — single national distributor. Tariffs aligned with French CRE-set wholesale + Monaco surcharge.
- **Gas**: SMEG also distributes piped natural gas (Monaco connects to French ENGIE GRTgaz network); LPG bottle for any non-mains pocket.
- **Water**: **Société Monégasque des Eaux (SMEaux)** — https://www.smeaux.mc/ — single operator. Treated water sourced from FR Roya / Var basin via long-distance pipeline; supply continuity is interconnect-dependent.
- **Wastewater**: Direction de l'Aménagement Urbain operates the sewer; full coverage in built-up areas. New connections at construction permit.
- **District cooling / heating**: SMEG operates district networks (e.g., **thalassothermie** seawater heat-pump network — Monaco harvests Mediterranean seawater for HVAC of major buildings since 1960s; Mareterra and Fontvieille districts heavily networked).
- **Internet / fibre**: **Monaco Telecom** (incumbent, EE/Iliad-owned) — near-universal FTTH coverage. Public-private competition limited (small market).

---

## Section: `--crime`

See `shared/crime-sources.md`. Monaco uses:
- **Direction de la Sûreté Publique (DSP)**: https://service-public-entreprises.gouv.mc/ + IMSEE annual security indicators
- Monaco's per-capita policing density is one of the highest in the world (est. ~520 sworn officers for ~38k residents — officer headcount is an estimate, no source cited; verify with the DSP annual report). Crime rate against persons / property is structurally low; main residential-buyer relevance is bag-snatch / pickpocket in Casino quartier tourist concentration.

---

## Section: `--amenities`

Universal — see `shared/amenities-osm.md`.

Monaco-specific amenities note: est. ~80 public lifts/travelators bridge the elevation difference between quartiers; "walking distance" to a quartier 200m horizontally but 80m vertically away may require a 5-min lift transit. Encode elevation in OSM Overpass output for Monaco amenity calculations.

---

## Section: `--climate`

Universal — see `shared/climate-projections.md`.

Monaco anchors on Plan National Énergie-Climat 2050 (carbon neutral commitment); coastal-elevation overlay is the parcel-level climate-risk lens (see `--risks` § Climate above).

---

## Section: `--finance` (Monaco-specific overlay)

Universal logic in `shared/finance.md`. Monaco-specific:

- **Mortgage market = private-bank-led**, NOT retail-bank like FR/DE. Lenders require an **AUM relationship** (typical floor €500k–€1M deposited liquid assets at the same bank for retail mortgage; substantially higher for full wealth-management).
- **Active lenders 2024-25**: BNP Paribas Wealth Management Monaco, Société Générale Private Banking Monaco, **Crédit Foncier de Monaco** (CFM Indosuez Wealth — Crédit Agricole group), EFG Bank Monaco, J. Safra Sarasin Monaco, **CMB Monaco** (Compagnie Monégasque de Banque — Mediobanca group). Verify member list at **CCAF**: https://ccaf.mc/
- **Typical LTV**: ~60% non-resident, ~70% resident. Tenor 15-25 yr. Rates trail EURIBOR + private-bank margin (~150-300 bps depending on relationship).
- **Lombard / pledge-back structure** common: lend against deposited portfolio rather than pure mortgage of property; effective LTV can be higher when pledged AUM is robust.
- **No FX-loan exposure** — EUR is local currency (Monetary Convention 2002).

---

## Section: `--currency` (Monaco-specific overlay)

Universal logic in `shared/currency.md`. Monaco-specific:

- **EUR (€)** under Monetary Convention France-Monaco 24 Dec 2001 (in force 2002). Monaco mints **euro coins** with national side under EU agreement; volume capped (~€2.34m face value/yr typical mint). No banknote issuance.
- Capital-controls: **none** — full free movement of capital. SEPA member.
- FX volatility: zero against EUR (same currency); USD/CHF/GBP exposure depends on buyer's home currency. CHF-Monaco residents historically a meaningful cohort (Swiss-tax planning lever).

---

## Section: `--visa` (Monaco-specific overlay)

Universal logic in `shared/visa-programs.md`. Monaco-specific (see also `--mains` § Foreign-buyer rules above for fuller treatment):

- **Carte de Résident** — three tiers (temporaire 1yr → ordinaire 3yr after 3yr → privilégiée 10yr after 10yr). Source: Direction de la Sûreté Publique — Service de Résidence.
- **Statutory requirements** (gouv.mc): proof of accommodation (owned or rented in Monaco), proof of financial means (Monaco-licensed bank attestation), clean criminal record (apostilled), health insurance.
- **Practitioner bar (NOT statutory)**: ~€500k+ bank deposit (varies by bank); ~€1M property purchase OR equivalent rental contract. Treat as `est.`
- **No CBI** (citizenship-by-investment). Naturalisation is rare sovereign-discretion grant; property purchase does NOT entitle to citizenship.
- **Convention fiscale FR-MC 1963** — French nationals do NOT benefit from Monaco's 0% PIT as residents; remain liable to French income tax.

---

## Section: `--insurance` (Monaco-specific overlay)

Universal logic in `shared/insurance.md`. Monaco-specific:

- **No catastrophic-risk reinsurance scheme equivalent to French CatNat** (Monaco is not in the FR CCR pool). Earthquake / flood / storm coverage is via private market.
- Mediterranean storm + earthquake exposure is low-to-moderate; mandatory mortgage insurance is lender-imposed (private banks typically require multi-risk habitation + life insurance for the borrower).
- Climate-risk underwriting is starting to differentiate by elevation above MSL for Larvotto / Bas Moulins / Fontvieille port-side coastal stock; expect premium drift up over 2025-2035.
- **Public health cover**: residents working in Monaco enrol in **CSM (Caisse de Sécurité Sociale Monégasque)**; non-working residents must hold private cover (mandatory for residency renewal).

---

## Section: `--notary` (Monaco-specific overlay)

Universal logic in `shared/notary-process.md`. Monaco-specific:

- **Civil-law notarial process** — notaire monégasque mandatory for all real-estate transfers. **Single-notaire model** (one notaire can act for both buyer and seller — distinct from French two-notaire common practice).
- Profession governed by **Loi n° 1.014 du 4 mai 1981** + accompanying ordonnances. Small profession (~3-5 active études).
- **Timeline**: compromis de vente → 6-10 weeks notarial searches → acte authentique. 10% deposit standard at compromis.
- **Title search**: notaire pulls full historical chain at Direction de l'Enregistrement et du Timbre; buyer cannot self-serve (no public cadastre).
- **Closing costs**: ~6% all-in resale (4.5% droits + ~1.5% émoluments + minor débours). New-build: 20% TVA replaces droits; émoluments lower.
- **Cooling-off**: not codified the same way as FR's loi SRU 10-day window — negotiate explicitly in the compromis.
- **Title insurance**: not customary (notaire's chain-of-deeds search is the warranty); UK/US-style title insurance not in market.

---

## Section: `--macro` (Monaco-specific overlay)

Universal logic in `shared/macro.md`. Monaco-specific (IMSEE 2023 + Monegasque Budget 2024-25):

- **GDP**: ~€8.6 bn nominal 2023 (IMSEE Comptes Économiques). Per-capita >€220,000 — among the world's highest.
- **Sectoral mix**: Finance & insurance (~17%), real-estate (~15%), construction (~10%), retail/hospitality (~12%), professional services (~10%), public administration & SBM tourism/casino (~rest).
- **Inflation**: tracks French CPI under monetary union (EUR + SEPA). 2024 Monaco IPC trended slightly above eurozone average (housing weight effect).
- **Sovereign**: AA+ Standard & Poor's (stable); no public debt issuance — Monaco does not borrow on capital markets.
- **Public finances**: budget surplus norm; ~€1.5-1.8 bn annual state revenue (TVA shared with FR + local taxes + concessions + SBM dividends).

---

## Section: `--demographics` (Monaco-specific overlay)

Universal logic in `shared/demographics.md`. Monaco-specific (IMSEE Recensement 2023 + Bilan Démographique 2024):

- **Population end-2023**: ~38,367 (IMSEE).
- **By nationality**: ~9,500 Monégasques (~25%); ~28,500 foreign nationals — predominantly **French (~24%), Italian (~19%), British, Swiss, German, Russian, US, Belgian** in declining order.
- **Median age**: ~46 — older than EU median; high-net-worth retirement cohort skew.
- **Workforce**: ~58,000 (IMSEE 2023) — ~75% are cross-border commuters from FR (Beausoleil, Roquebrune-Cap-Martin, Menton) + IT (Ventimiglia, Bordighera).
- **Schooling**: French national curriculum dominant (Lycée Albert 1er, Collège Charles III); two international schools — **International School of Monaco (ISM)** in Carré d'Or (English curriculum) — relevant for foreign-family buyers.
- **Healthcare**: **Centre Hospitalier Princesse Grace (CHPG)** is the principality's main hospital; CHPG relocation/rebuild project under way for completion 2025-2030 — relevant for adjacent-quartier construction noise.

---

## Section: `--exit` (Monaco-specific overlay)

Universal logic in `shared/exit.md`. Monaco-specific:

- **Time on market**: variable by quartier and price tier; trophy Carré d'Or units can sit 12-24 months; mid-market La Rousse / Larvotto typically 3-9 months. **No public TOM database** — agency-side reporting only (CIM members).
- **Agent commissions**: typically **5-7%** of sale price + TVA, **seller-paid**. Specific custom: split agency arrangements common; verify mandate type (mandat exclusif vs simple).
- **Sell-side fiscal**: **0% CGT on Monaco property resale** for resident or non-resident sellers. **Exception: French national sellers remain liable to FR plus-value immobilière regime** under the 1963 Convention — large gap vs all other nationalities.
- **Notarial side**: same notaire model; seller's deed-side closing costs minimal (buyer pays droits + émoluments).
- **Liquidity context**: ~470 resale transactions/yr across the entire principality (IMSEE 2024) — **structurally illiquid** at the unit level; pricing is comp-thin and discretionary; expect 5-15% price negotiation off asking in normal markets.

---

## Cost benchmarks (May 2026)

| Item | Range / typical |
|---|---|
| Resale weighted avg €/m² | ~€51,400 (IMSEE 2024 annual) |
| Monte-Carlo €/m² | ~€60,000 (Carré d'Or trophy higher) |
| Larvotto €/m² | ~€50,000 |
| Fontvieille €/m² | ~€42,000 |
| New-build apex floors (Mareterra / Testimonio II) | >€100,000/m² (per agency, verify per listing) |
| Prime gross rental yield | ~2-3% |
| Droits d'enregistrement (resale, private) | 4.5% |
| Notaire émoluments | ~1.5% |
| TVA on new-build first sale | 20% |
| Taxe foncière (annual) | €0 (none) |
| Personal income tax | 0% (except FR nationals) |
| CGT on Monaco property resale | 0% |
| Inheritance, direct line | 0% |
| Total acquisition costs (resale) | ~6% all-in |

---

## Active fiscal incentives (May 2026)

- **No annual property tax** — structural, no application needed
- **No personal income tax** — structural for non-French residents
- **No CGT** on Monaco property resale — structural
- **0% inheritance/gift tax direct line + spouse** — structural
- **Reduced 1% droits d'enregistrement** for Monégasques and qualifying residents (specific schemes — verify per buyer)
- **Fewer renovation restrictions than FR DPE regime** (no Loi Climat F/G rental ban equivalent — but PNEC 2050 may evolve)

---

## Foreign-buyer rules

**Open regime** — no nationality restriction on private real-estate acquisition in **secteur libre / domaine privé**. EU and non-EU buyers treated identically for ownership rights.

- **No quota, no preapproval, no foreign-buyer surcharge.** Same 4.5% droits d'enregistrement applies to all private buyers.
- **Restricted segment**: **secteur domanial / secteur protégé** (state-owned and rent-controlled stock for Monégasques and long-term residents) — closed to non-Monégasques and not relevant to foreign-buyer transactional analysis.
- **Mortgage practice (lender-imposed, not legal restriction)** — Monaco's mortgage lending is **private-bank-led** (BNP Paribas Wealth Management Monaco, Société Générale Private Banking Monaco, Crédit Foncier de Monaco, EFG Bank Monaco, J. Safra Sarasin Monaco, CMB Monaco):
  - Non-resident foreign buyer: typical **LTV ~60%** subject to bank's wealth/AUM relationship; commonly conditioned on **assets-under-management** at the same bank
  - Resident: typical **LTV up to ~70%**
  - Tenor: 15-25 years; rates trail ECB/EURIBOR with private-bank margin
  - **AUM-pledge structure** (Lombard-style) common — bank lends against deposited liquid assets rather than pure mortgage of property; Monaco buyers often blend the two

### Residency (Carte de Résident) — NOT formally investment-pegged

- **Three permit tiers**:
  - **Carte de séjour temporaire**: 1 year, renewable annually for first 3 years
  - **Carte de séjour ordinaire**: 3 years, after 3 years of continuous residence
  - **Carte de séjour privilégiée**: 10 years, after 10 years of continuous residence
- **Statutory requirements** (Direction de la Sûreté Publique — Service de Résidence; gouv.mc):
  - Proof of accommodation in Monaco — owned property OR rental contract (no statutory minimum value but practitioner-quoted bar of ~€1M for owned stock OR a long-term rental at typical Monaco rates)
  - Proof of financial means — a Monaco-licensed bank's attestation of deposited funds. **No statutory threshold** in published Monaco law; **practitioner-quoted bar ~€500,000** at the chosen bank (varies by bank, by applicant profile, by AUM relationship). Treat as `est.` calibration: ≥€500k typical floor, often higher (€1M+) for some banks.
  - Clean criminal record (apostilled + translated to French)
  - Health insurance (Monaco public CSM if working; private if not)
- **Source**: https://monservicepublic.gouv.mc/en/events-in-your-life/settling-in-monaco — verify before any application.
- **No minimum-stay quota** for the temporary card initially, but the privilégiée tier requires **continuous residence ≥10 years** with `presence` evidence.
- **No CBI (citizenship-by-investment)** in Monaco — naturalisation is at the discretion of the Sovereign (Prince) and exceedingly rare (est. ~3-5 grants per year — no official annual naturalisation publication exists; verify against Journal de Monaco naturalisation ordonnances). Property purchase does NOT entitle to citizenship.

(Cross-reference: `shared/visa-programs.md` MC entry — confirm current state before quoting to user.)

---

## Country-specific quirks

- **Mareterra (delivered 2024)** — 6-hectare offshore extension at Anse du Portier; mixed residential + park + harbour; flagship 2020s programme. Per-listing prices reported in €100,000-200,000/m² range for top units. **Verify per listing** — only ~110 units; stratospheric headline figures are not representative of the broader resale market.
- **Carré d'Or** — informal trophy quartier centred on Avenue de Monte-Carlo / Place du Casino / Avenue des Beaux-Arts; pricing premium of +20-40% vs broader Monte-Carlo. Properties on this perimeter trade thinly; comp data may be 1-2 transactions/year.
- **No public cadastre** — buyers cannot self-serve title search the way they can in FR/UK/DE; **the notaire is the single source of truth** for title chain. Budget 2-4 weeks for notarial searches before deed (acte authentique).
- **Single-notaire transaction model** — one notaire can act for both buyer and seller (vs FR's typical 2-notaire arrangement). Buyer-side legal review by an avocat conseil is standard for non-French-speaking buyers.
- **Compromis de vente (preliminary contract) → acte authentique (final deed)**: typical timeline 6-10 weeks; deposit 10% standard; rétractation cooling-off period not codified the same way as FR's 10-day SRU window — **negotiate explicitly in the compromis**.
- **French national fiscal exception** — Convention 1963 makes France-passport residents the only nationality not benefiting from Monaco's 0% PIT. Investment thesis for FR-passport buyers is materially different (Monaco residency does NOT shield from FR income tax). Naturalisation to a non-FR citizenship before establishing Monaco residency is a recurring tax-planning lever — discuss with FR-MC dual-tax adviser.
- **SCI ownership** — historically routed through SCI to anonymise beneficial owner and (pre-2024) reduce certain transactional friction; **Loi n° 1.560 (Dec 2024) closed the rate-arbitrage** between direct and SCI acquisition (now both 4.5%). SCI still useful for succession-planning continuity; consult notaire.
- **Bank-of-residency dependency** — opening a Monaco-licensed bank account is a prerequisite for residency, mortgage, and rent payment; banks operate selectively (KYC-heavy, AUM minimums commonly €500k-€1M for retail private bank, higher for full wealth-management). Choosing the bank is a strategic decision that long-precedes the property choice.
- **Domaine privé vs secteur domanial** — strictly separate stock; foreign buyers cannot acquire domanial units regardless of price offered. Listings on the open market are by definition domaine privé.
- **Earthquake of 1887 Ligurian** — last significant felt event; damage to Mentone-Monaco coastal masonry. Eurocode 8 enforced for new builds; older Rocher / Condamine stock built to pre-modern seismic standards.
- **No central heating tradition for older stock** — Mediterranean climate; older La Condamine / Monaco-Ville apartments may rely on individual electric / split-AC heating, with material Q1 utility bills in cold winters.
- **Helipad-tower premium** — a handful of towers (Le Roccabella, Mirabeau pent floors) carry private helipad access; commands premium and adds annual concession/maintenance levies.

---

## Verification authorities

| Item | Authority | URL |
|---|---|---|
| Statistics (incl. Marché Immobilier) | IMSEE | https://www.monacostatistics.mc/ |
| Cadastre / Domaine | Direction du Domaine | https://service-public-entreprises.gouv.mc/ |
| Tax / Enregistrement | Direction des Services Fiscaux | https://monservicepublic.gouv.mc/Fiscalite |
| Residency | Direction de la Sûreté Publique (Section Résidence) | https://monservicepublic.gouv.mc/en/themes/nationality-and-residency/residency/new-entrants/how-to-apply-for-a-residence-permit |
| Notaires | Chambre des Notaires de Monaco | (verify with the Chambre — small profession; CIM directory cross-references members) |
| Real-estate agents | CIM (Chambre Immobilière Monégasque) | https://www.chambre-immobiliere-monaco.mc/ |
| Urbanism / planning permits | DPUM | https://service-public-entreprises.gouv.mc/ |
| Energy & Climate (Plan Climat) | Mission pour la Transition Énergétique | https://transition-energetique.gouv.mc/ |
| Tourism (STR licensing) | Direction du Tourisme et des Congrès (DTC) | https://www.visitmonaco.com/ + service-public-entreprises.gouv.mc |
| Electricity & Gas | SMEG | https://www.smeg.mc/ |
| Water | SMEaux | https://www.smeaux.mc/ |
| Telecom | Monaco Telecom | https://www.monaco-telecom.mc/ |
| Police | Direction de la Sûreté Publique | https://monservicepublic.gouv.mc/ |
| Banking regulator (cross-ref) | Commission de Contrôle des Activités Financières (CCAF) | https://ccaf.mc/ |

---

## Source URL templates

| Field | Template |
|---|---|
| IMSEE Marché Immobilier | https://www.monacostatistics.mc/Logement-Immobilier |
| Fiscalité particuliers | https://monservicepublic.gouv.mc/Fiscalite |
| Résidence (foreign-buyer) | https://monservicepublic.gouv.mc/en/events-in-your-life/settling-in-monaco |
| Loi n° 1.560 (SCI reform) | https://journaldemonaco.gouv.mc/ (search by loi number) |
| Convention fiscale FR-MC 1963 | https://www.legifrance.gouv.fr/ + https://gouv.mc/Gouvernement-et-Institutions |
| Plan Climat | https://transition-energetique.gouv.mc/ |
| Real-estate agent directory | https://www.chambre-immobiliere-monaco.mc/ |

---

## Status

**Confidence**: MEDIUM — HIGH on foundational legal framework (Code Civil + Loi 1.014 notarial barème + Ordonnance Souveraine droits d'enregistrement 4.5% / 7.5% trust+offshore vehicles, monservicepublic.gouv.mc portal as primary admin gateway, EUR adoption via 2001/2011 monetary agreement, no income tax for residents except French nationals under 1963 convention). MEDIUM for notarial émolument exact bands (verify per deal at Chambre des Notaires), practitioner-quoted LTV bands (no public mortgage-stats publication), and CAP 39's interaction with parcel-level cadastre. LOW on residential listing-price currentness (luxury market with high deal-to-deal variance — pull current asking from agent at point of analysis).

**Last verified**: 2026-05-27

**Researched by**: Sonnet 4.6 + Opus 4.7 (parallel-subagent batch, 2026-05)

**Notes**: HIGH on no annual property tax (gouv.mc + PwC + OECD multi-source), no CGT on Monaco real estate, 4.5% droits d'enregistrement standard rate, Convention fiscale franco-monégasque 1963 carving French nationals out of the PIT exemption, IMSEE 2024 weighted-average resale ~€51,400/m², open foreign-buyer regime in secteur libre / domaine privé. MEDIUM on per-quartier €/m² figures (IMSEE publishes weighted averages but small-cohort quartiers like Monaco-Ville have wide CIs — always pull latest IMSEE PDF before quoting), exact Loi n° 1.560 transitional regime for SCI transactions in 2024-25 (verify with notaire monégasque), residency financial-means bar of ~€500k bank deposit (practitioner-quoted, NOT statutory; varies by bank). LOW on DPE / energy-diagnostic mandatoriness (Monaco does not yet have an EPC regime equivalent to French DPE for sale disclosure as of 2025; PNEC may evolve — confirm with notaire). LOW on per-listing new-build apex prices (Mareterra / Testimonio II >€100k/m² figures originate from agency reporting, not IMSEE — `(per listing — verify with notaire monégasque)`).

---

## Extension TODOs

- IMSEE per-quartier resale series tracker (auto-pull the annual PDF, extract weighted averages per quartier with sample-size flag)
- Loi n° 1.560 SCI-reform follow-up: monitor 2025-26 Journal de Monaco for transitional-regime amendments
- Mareterra delivery cohort price tracker (programme just delivered 2024 — first resale liquidity 2026-2028)
- Convention fiscale FR-MC 1963 ratification monitor (no current renegotiation announced, but periodic FR-side noise about updating the bilateral)
- DPE / EPC regulatory introduction monitor (Plan Climat 2050 may pull energy-disclosure mandate forward)
- Bank-of-residency AUM minimums benchmarking (currently practitioner-quoted, not centrally published — would need primary survey of CCAF members)
