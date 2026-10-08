# Greenland (Kalaallit Nunaat) — Property Due-Diligence Playbook

ISO2: `gl`. Status: ✅ Standalone playbook (DK autonomous territory under [Lov om Grønlands Selvstyre, 2009](https://www.retsinformation.dk/eli/lta/2009/473) — "Selvstyreloven"). Self-government covers most internal affairs incl. land use, taxation, housing; FX/currency/defence remain Danish.

## Country profile

- Population: ~56,000 (Statistics Greenland 2025); ~18,000 in Nuuk (capital) — verify against current [bank.stat.gl](https://bank.stat.gl/) population series
- Currency: Danish Krone (**DKK**) — pegged to EUR via ERM II
- Languages: **Kalaallisut** (Greenlandic, official) + **Danish** (administrative co-official). Primary legal acts often published in BOTH; only Danish text legally binding for Danish-realm-derived statutes
- ISO 3166-1 alpha-2: `gl` · alpha-3: `grl`
- Postal codes: 4-digit (`39XX`)
- Time zone: Most settlements UTC-2 (UTC-1 DST); Pituffik/Thule UTC-4; Ittoqqortoormiit UTC-1; Danmarkshavn UTC+0
- Cadastre / land registry: **Tinglysningsretten i Hobro** (DK) handles Greenland's tinglysning of buildings (see § Land registry below — verify the registry handles GL buildings)
- Geographic context: ~80% covered by ice cap; habitation concentrated on ice-free coastal fringe (~410,000 km² habitable). 17 towns + ~60 bygder (settlements). No interconnected roads between towns — domestic transport by boat / helicopter / Air Greenland.

---

## ⚠️ Foundational concept: there is no private land ownership

**This is the single most important fact about Greenland real estate, and is structurally unlike any other jurisdiction this skill covers.**

Under Greenlandic land law, **all land is owned in common ("offentligt ejet" / public)** — neither the state, the self-government, nor the municipality "owns" land in the cadastral sense. There is **no land cadastre that records private ownership of surface land**. What a buyer acquires is:

1. **Title to the building** (bygning) — a movable-like asset recorded under tinglysning
2. **Right of use to the land beneath** (`arealtildeling` / `brugsret`) — granted administratively, non-transferrable on its own, lapses if the building is removed or use is abandoned

Source: Inatsisartutlov nr. 17 af 17. november 2010 om planlægning og arealanvendelse (Planning and Land Use Act) — administered by **Departementet for Boliger og Infrastruktur (Naalakkersuisut**, the Government of Greenland) and the municipalities (Kommune Kujalleq, Kommuneqarfik Sermersooq, Qeqqata Kommunia, Avannaata Kommunia, Kommune Qeqertalik). Verify text at [nalunaarutit.gl (official gazette)](https://nalunaarutit.gl/arkiv/gh.gl-love/dk/2010/ltl/L_17-2010_arealanvendelse/L_nr_17-2010_dk.htm) / [retsinformation.dk](https://www.retsinformation.dk/).

**Verbatim primary confirmation** (Mineral Licence and Safety Authority — **MLSA**, hosted at govmin.gl, under Naalakkersuisut):

> "In Greenland there is no privately owned land, all rights to any use of land is administered by the Government of Greenland."

Source: [govmin.gl Mineral Resources Act page](https://govmin.gl/exploitation/get-an-exploitation-licence/mineral-resources-act/) — `primary-verified` (Tavily-confirmed verbatim; direct WebFetch failed TLS during research but the snippet is verbatim-attested by an independent search engine). Community corroboration: one on-topic r/greenland thread ([1cq7b5b](https://www.reddit.com/r/greenland/comments/1cq7b5b/buying_a_land_renting_in_greenland/)) where locals confirm "no one's able to buy land here" — anecdotal, not load-bearing but consistent with primary.

The system is sometimes summarised in legal commentary as a "legal anachronism" (Arctic Institute) because Greenland never developed Roman / feudal land-ownership concepts; land allocation is administrative-customary, descended from Inuit common-use practice and codified into the modern brugsret regime.

**Consequence for buyers**:

- You cannot sell "the land" — only the building + the transferred brugsret
- The municipality (or Naalakkersuisut for some bygder / outer areas, routed through the `bygdebestyrelse` / settlement council) must approve any transfer of the arealtildeling
- A foreign buyer's failure to use the building (extended vacancy) can trigger arealtildeling lapse + forced removal at owner's cost

---

## Section: `--ownership` (foreign buyer rules — LAW IN FORCE 1 JANUARY 2026)

**`Inatsisartutlov nr. 78 af 21. november 2025 om erhvervelse af adkomst eller brugsret til fast ejendom`** ("Act on acquisition of title or right of use to real property") was adopted by **Inatsisartut** (the Parliament of Greenland) on 21 November 2025 and **enters into force 1 January 2026** (§ 15 transition rule: applies to agreements + arealtildeling applications filed on or after 1 January 2026; pre-2026 agreements are grandfathered).

**Primary sources**:

- Statute text: [nalunaarutit.gl — Inatsisartutlov nr. 78 af 21.11.2025](https://nalunaarutit.gl/groenlandsk-lovgivning/2025/inatsisartutlov-nr-78-af-21_11_2025?sc_lang=da)
- Lovbemærkninger (forarbejder / explanatory remarks): [nalunaarutit.gl — fast-ejendom_lovbemaerninger_da.pdf](https://nalunaarutit.gl/-/media/lovfiler/2025/forarbejder/ina_78/fast-ejendom_lovbemaerninger_da.pdf)
- Original 3 Feb 2025 announcement (now superseded by the enacted statute, retained as policy-rationale source): [naalakkersuisut.gl Nyheder 2025/02/0302_fast_ejendom](https://naalakkersuisut.gl/Nyheder/2025/02/0302_fast_ejendom?sc_lang=da)
- Industry commentary: [2plus-revision.dk — Ny lov begrænser adgangen til ejendomskøb i Grønland](https://www.2plus-revision.dk/ny-lov-begraenser-adgangen-til-ejendomskoeb-i-groenland)

**§ 1 — General prohibition**: No physical or legal person may acquire title or right of use to real property in Greenland, nor an arealtildeling, **unless permitted by one of the eligibility classes below**. The prohibition extends to **indirect acquisition** via shares, voting rights, or pant (security interest) in legal persons that hold GL real property. Applies *mutatis mutandis* to arealtildeling under the Planning + Land Use Act.

**Eligibility classes (§§ 3-8)**:

| § | Class | Substantive criterion |
|---|---|---|
| § 3 | Natural persons with **dansk indfødsret** (Danish citizenship) | Unrestricted — may acquire freely |
| § 4 | Foreign nationals | ≥ 2 years fixed residence + `folkeregisteradresse` in Greenland **AND** ≥ 2 years full tax residency in Greenland |
| § 5 | Regulated financial institutions | DK / GL / FO-headquartered banks, mortgage institutions, investment firms, insurers, pension funds under [Finanstilsynet](https://www.finanstilsynet.dk/) (Danish FSA) supervision |
| § 6 | Greenlandic capital companies | 100% of capital **and** voting rights held directly by persons qualifying under §§ 3-4 |
| § 7 | Licensed sectoral operators | Holders of fishing / mineral / tourism / resource-extraction permits — for business use only |
| § 8 | Greenlandic associations | Non-commercial societies registered ≥ 2 years in CVR with Greenland HQ |

**§ 9 — Dispensation**: Naalakkersuisut may grant written conditional or time-limited permission to applicants who do not qualify under §§ 3-8. Discretionary, case-by-case. Dispensation channel: **Departementet for Boliger og Infrastruktur** — `box909@nanoq.gl`.

**§ 15 — Entry into force**: 1 January 2026. Applies to agreements + arealtildeling applications **filed on or after** 1 January 2026. Pre-2026 agreements are grandfathered.

**Stated policy rationale** (per 2025 forarbejder + announcement): prevent speculation-driven property acquisition following the opening of international airports in Nuuk (2024) and Ilulissat (2024) and increased international interest from foreign actors.

**Practical buyer paths for non-§ 3 persons**:

- **§ 4** is the principal natural-person route: requires the buyer to already be a 2-yr resident with full GL tax residency — i.e., you must move to Greenland and live there for two full years before transacting. There is no "acquire first, satisfy residency after" pathway.
- **§ 9 dispensation** is the only fast track; outcome is discretionary and not a buyer's right.
- The **brugsret** itself (not the building) is subject to the same §§ 3-8 gating: a non-qualifying buyer cannot acquire the brugsret even if they could somehow acquire the building. Carve-outs: the Act does not apply to a natural person acquiring a right of use (brugsret) to real property for their own dwelling, or a right of use of a temporary nature (§ 2 — so renting a home is outside the gate), and § 9 permission is not needed for acquisition by inheritance, undivided estate, division of joint marital property, or gift to lineal relatives (§ 10).

**Confidence**: **HIGH** — primary statutory source (nalunaarutit.gl), independently cross-validated against forarbejder and industry commentary. (Verified 2026-05-27.)

---

## Section: `--price`

**No equivalent of Etalab / Catastro / Land Registry open data exists for Greenland.** There is no public sold-price database.

**Data sources** (priority order):

1. **Statistics Greenland (Grønlands Statistik)** — quarterly + annual building permits + housing-cost indices:
   - Portal: [stat.gl](https://www.stat.gl/) (DA / EN / KAL toggles)
   - Statbank: [bank.stat.gl](https://bank.stat.gl/) — series include `BOXBYG` (building permits), housing-stock, dwellings
2. **Self-Government housing rents (Iserit A/S)** — sets the public-rental benchmark for towns: [iserit.gl](https://www.iserit.gl/)
3. **Listing platforms (private market — thin)**:
   - [boligportal.gl](https://www.boligportal.gl/) ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row — Nuuk + Sisimiut + Ilulissat (rentals + some sales)
   - [estate.gl](https://www.estate.gl/) ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row — agency listings (verify URL liveness)
   - DBA / dba.dk Greenland filter — secondhand market
   - Facebook Marketplace "Sælges i Nuuk" — private-sale signal
4. **Bank valuations**: [Grønlandsbanken](https://www.banken.gl/) + [BankNordik Grønland](https://www.banknordik.gl/) publish annual market commentary in Danish; treat as orientation, not transactional

**Typical price bands** (orientation only — `est.`; verify with current listings):

- Nuuk house/apartment: ~DKK 25,000–45,000 / m² (~€3,350–€6,030 / m² at 2026 DKK/EUR ≈ 7.46) — `est.` from listing scrape; verify
- Sisimiut / Ilulissat: ~DKK 15,000–28,000 / m² `est.`
- Bygder (small settlements): often nominal building values DKK 100,000–500,000 — wood houses, no land value
- `data not publicly available for parcel-level historical sale prices — verify with the bank's valuation desk or recent comparable on boligportal.gl`

**Caveat**: housing-shortage in Nuuk is structurally severe (Inatsisartutlov 78/2025 is partly a response). Listings turn over quickly; price discovery is opaque.

---

## Section: `--tax`

**Greenland sets its own tax law** under Self-Government (Selvstyreloven §§ 5-9). It is NOT part of Danish tax law for residents. Pension/insurance and customs aspects use limited Danish co-administration.

**Data sources**:

1. **Skattestyrelsen i Grønland** (`Akileraartarnermut Aqutsisoqarfik`): [aka.gl](https://www.aka.gl/) — single primary
2. **Skattetræk i Grønland** (Skattestyrelsen, **September 2026 edition — Danish only; the English edition has been withdrawn**), which states "Vejledningen indeholder de regler, der gælder pr. 1. januar 2025": index page [aka.gl — Vejledninger Skat](https://aka.gl/emner/borger/skat/vejledninger-skat) → current PDF `skattetraek-i-groenland-dk-sept26.pdf`. Cite the index page, not the media URL — aka.gl serves its PDFs off a rotating Umbraco Cloud host (2026 data, source aka.gl; 2026-09-18 verified)
3. **Sullissivik (citizen portal)**: [sullissivik.gl](https://sullissivik.gl/) — self-service tax + business
4. **Naalakkersuisut finance laws**: [naalakkersuisut.gl](https://naalakkersuisut.gl/) — annual Finanslov (`FFL`, the Finance Act)
5. **Nordic cooperation Greenland tax overview**: [norden.org / info-norden / taxation-greenland](https://www.norden.org/en/info-norden/taxation-greenland) — useful EN overview (HTTP 403 during research run — verify directly); cross-check with aka.gl
6. **Inatsisartut tax laws (DA full text)**: [ina.gl](https://ina.gl/) — Greenland's parliament; published FFL carry rate tables
7. **PwC Worldwide Tax Summaries — Greenland** (cross-reference, not primary): [taxsummaries.pwc.com/greenland](https://taxsummaries.pwc.com/greenland/individual/taxes-on-personal-income) — note PwC table reproduces 2020-era rate structure; use aka.gl 2025 PDF as the authoritative current source

### Income tax (resident)

- **Skat** = national tax (`landsskat`) + municipal tax (`kommuneskat`) + joint-municipal tax (`fælleskommunal skat`). No church tax in Greenland (verify).
- Combined rates by municipality — **primary source aka.gl 2025 EN PDF** (verify the per-municipality table on pp. 2-3 of the PDF; cross-reference PwC 2026 reproduction below):

  | Municipality | Kommuneskat | Landsskat | Fælleskommunal | **Total** |
  |---|---:|---:|---:|---:|
  | Kommune Kujalleq (south) | 28% | 10% | 6% | **44%** |
  | Kommuneqarfik Sermersooq (Nuuk + east) | 26% | 10% | 6% | **42%** |
  | Qeqqata Kommunia (Sisimiut, Maniitsoq) | 26% | 10% | 6% | **42%** |
  | Kommune Qeqertalik (Aasiaat, Qasigiannguit) | 28% | 10% | 6% | **44%** |
  | Avannaata Kommunia (Ilulissat, Uummannaq, Upernavik) | 28% | 10% | 6% | **44%** |
  | Outside municipal areas (national park, Pituffik) | n/a | 10% | n/a (effective ~36%) | **36%** |

  Authoritative: [aka.gl — Vejledninger Skat](https://aka.gl/emner/borger/skat/vejledninger-skat) → "Skattetræk i Grønland" (DA, September 2026 edition, rules as at 1 January 2025). **This guide no longer publishes the per-municipality combined-rate table** — the rates above are therefore uncited against it; re-verify against the Finanslov / Inatsisartut rate tables before reliance. Cross-reference: [PwC Worldwide Tax Summaries — Greenland](https://taxsummaries.pwc.com/greenland/individual/taxes-on-personal-income).

- **Personfradrag (personal allowance)**: `data current at aka.gl 2025 EN PDF — verify the 2025/2026 indexed amount; the 2016 baseline was DKK 48,000/year + DKK 10,000 supplemental for fully tax-liable persons`
- **Flat 35% special rate** for oil/gas/mineral/certain construction workers (no deductions) if not locally taxed in prior six months ([PwC](https://taxsummaries.pwc.com/greenland/individual/taxes-on-personal-income); cross-verify in aka.gl 2025 EN PDF)
- **Mandatory Greenlandic pension contribution**: 10% in 2024 → **11% in 2025 onwards** of A-tax basis (PwC; [Hire Me Greenland](https://hireme.gl/en/news/tax-in-greenland-as-a-dane-here-is-what-you-need-to-know))
- **Employer social charge**: 2.1% on payroll; **no employee social-security contribution** (PwC, 2025)

### Capital gains on real estate

- Per PwC: *"almost no assets are subject to capital gains taxation"* — residential property disposal generally NOT taxed
- Source: [PwC — Greenland Individual Other Taxes (2026)](https://taxsummaries.pwc.com/greenland/individual/other-taxes)
- Investment / business property and certain commercial dispositions may attract income-tax treatment — verify at [aka.gl](https://www.aka.gl/) under disposal-of-business-assets

### Property / land-use charges

- **No tax on property designated for private residential use in Greenland** (PwC, 2026)
- No equivalent of ejendomsværdiskat or grundskyld
- Communal arealtildeling may carry **modest annual fees** for connection / waste / dwelling (varies by kommune, set in municipal budgets — verify at the issuing kommune)
- Some commercial / industrial arealtildelinger carry a brugsret afgift — verify rate at the issuing kommune
- Source: [PwC Worldwide Tax Summaries — Greenland Other Taxes](https://taxsummaries.pwc.com/greenland/individual/other-taxes)

### VAT / sales tax

- **There is NO VAT (moms) in Greenland.** Verbatim PwC 2026: *"There is no Greenlandic value-added tax (VAT)."* ([source](https://taxsummaries.pwc.com/greenland/individual/other-taxes))
- Instead, **import duties** (Indførselsafgifter) apply to: alcohol, tobacco, sugar, chocolate, coffee, tea, soft drinks, meat, poultry, perfume, cosmetics, cars, mopeds, and snowmobiles (PwC 2026). Construction materials and most everyday goods are duty-free. Full schedule: [aka.gl Indførselsafgifter 2024](https://www.tusass.gl/assets/support/post/customs/Indforselsafgifter-2024-DANSK.pdf)

### Wealth tax

- **None.** *"There is no Greenlandic tax on net wealth."* (PwC 2026, [source](https://taxsummaries.pwc.com/greenland/individual/other-taxes))

### Transaction taxes (purchase)

- **Stamp tax (stempelafgift)**: **1.5% of the transfer sum** applies to real estate transfers, property mortgage registration, and ship transfers (incl. share transfers in ship-owning companies). Source: [PwC — Greenland Other Taxes (2026)](https://taxsummaries.pwc.com/greenland/individual/other-taxes).
- **No further "stamp duty" / "transfer tax"** — Greenland does not have an SDLT / IMT / IVA equivalent beyond the 1.5% above
- **Advokat (lawyer) fees**: typically DKK 8,000–25,000 `est.` for a standard transaction — set by hourly rate, not statutory tariff (no civil-law notarial tariff exists in Greenland)
- **Inheritance tax**: PwC notes inheritance provisions have *"limited application given that almost no assets are subject to capital gains taxation"* — verify at aka.gl for current-year specifics

---

## Section: `--registry` (Land + building title)

**There is NO Greenland land-title registry.** Land is not titled — primary-confirmed by MLSA (Mineral Licence and Safety Authority, govmin.gl, under Naalakkersuisut): *"In Greenland there is no privately owned land, all rights to any use of land is administered by the Government of Greenland."* ([govmin.gl Mineral Resources Act page](https://govmin.gl/exploitation/get-an-exploitation-licence/mineral-resources-act/)) — `primary-verified` via Tavily verbatim snippet.

For **buildings**, ownership + mortgages are recorded in the Danish national tinglysning system administered by:

- **Tinglysningsretten i Hobro** (Majsmarken 5, 9500 Hobro, DK) — [domstol.dk/tinglysningsretten](https://www.domstol.dk/tinglysningsretten/)
- Online portal: [tinglysning.dk](https://www.tinglysning.dk/) — public lookups, login via MitID
- The **Tingbog** (property register) records owner + easements + mortgages on registered real property; a **tingbogsattest** is the canonical excerpt
- Greenland building identifiers: data not publicly aggregated in English — verify the exact identifier scheme + whether tinglysning covers ALL Greenland buildings or only those in registered land-rolls, by contacting Tinglysningsretten directly

The brugsret / arealtildeling itself is NOT registered in tinglysning (it is administrative, held by the issuing kommune / Naalakkersuisut, via the local `bygdebestyrelse` for outer settlements). Loss / transfer of arealtildeling is therefore a separate, parallel process from any tinglysning act.

**Verification path for a buyer**:

1. Pull current **tingbogsattest** for the building from [tinglysning.dk](https://www.tinglysning.dk/)
2. Pull **arealtildelingsbrev / -tilladelse** from the issuing kommune (the five kommuner each maintain their own register; bygd arealtildeling is routed via the `bygdebestyrelse` to Naalakkersuisut)
3. Confirm both names align; confirm no use-condition breach (purpose of arealtildeling matches actual use)
4. Confirm no overlapping mineral / hydrocarbon licence via [govmin.gl](https://govmin.gl/)

---

## Section: `--rental` (residential + short-let)

**Residential rental** is regulated by **Greenland's own Inatsisartutlov om leje af boliger** (NOT the Danish Lejeloven). The current statute dates to 2005; a comprehensive replacement was put out for public consultation in **March 2026** (Naalakkersuisut høring): [naalakkersuisut.gl/Hoeringer/2026/03/0603_lejelov](https://naalakkersuisut.gl/Hoeringer/2026/03/0603_lejelov?sc_lang=da) — track this for the post-2026 regime. `Consultation phase as of 2026-05-27 — verify status before publish.`

Key features:

- Strong tenant protections — terms reducing tenant rights below statutory minimum are **invalid**
- Tenant cannot use dwelling for non-residential purposes / run a business from it without landlord consent
- **Boligklagenævnet** (Housing Appeals Board) handles disputes — competence being expanded under the 2026 reform to cover certain private-rental disputes
- Public housing (**Iserit A/S** in former Sermersooq-area + **INI A/S** in northern/southern Greenland) dominates the rental stock
- Private-market rentals are limited; rent levels approximately track public-rent benchmarks + premium
- Sources: [Iserit A/S](https://www.iserit.gl/) · [Atuisartoqarnermut Unammilleqatigiinnermullu Aqutsisoqarfik / AUA — Consumer Authority housing section](https://aua.gl/bolig/) · [Naalakkersuisut høring 2026 (proposal text + bemærkninger)](https://naalakkersuisut.gl/-/media/horinger/2026/03/0603_lejelov/bemrkninger---forslag-til-inatsisartutlov-om-leje-af-boliger.pdf)

**Short-term rental (Airbnb / cabin rental)**:

- No nationwide STR licensing law to date `(verify — fast-moving area)`
- Visit Greenland operator registration: [visitgreenland.com](https://visitgreenland.com/) for licensed operators
- Practical constraint: Inatsisartutlov 78/2025 + the brugsret regime mean **a non-resident foreign buyer of a "holiday rental" property is structurally implausible** absent § 9 dispensation
- Income tax on rental: rental income taxed as ordinary income at combined municipal+state rate (no STR special regime equivalent to FR's micro-BIC)

---

## Section: `--banking` / `--finance`

**Local banks**:

1. **Grønlandsbanken** (Bank of Greenland — only fully Greenland-domiciled bank): [banken.gl](https://www.banken.gl/) · listed on Copenhagen Nasdaq Main Market (ticker GRLA)
2. **BankNordik Grønland** (subsidiary of Faroese BankNordik P/F): [banknordik.gl](https://www.banknordik.gl/)

**Supervision**: dual — [Finanstilsynet (Danish FSA)](https://www.finanstilsynet.dk/) supervises capital + AML + conduct; Greenland-side conduct rules apply where adopted.

**Mortgages for foreign buyers**: structurally very rare. Reasons:

- Inatsisartutlov 78/2025 limits who can buy at all (and § 5 allows regulated financial institutions to acquire as lenders, but the underlying borrower still needs §§ 3-4 / § 9 status)
- Underlying asset is the building + brugsret, NOT land — narrower collateral than mainland DK / EU mortgages
- Brugsret can lapse → collateral risk for the bank
- Greenland has no realkredit (mortgage-bond) system equivalent to DK's; financing is via bank-balance-sheet term loans, ~10–25 yr `est.` — confirm tenor on the bank's term-sheet (Grønlandsbanken / BankNordik product terms)

`Recommended: get the bank's term-sheet BEFORE making any offer; foreign-buyer mortgages are case-by-case at both banks.`

---

## Section: `--risks`

### Permafrost / foundation engineering

- ~80–90% of habitable Greenland has discontinuous-to-continuous permafrost beneath, but **most BUILDINGS in Greenland are sited on solid bedrock** (Arctic Office / Cimpoiasu fieldwork report, Ilulissat 2024) — bedrock outcrops dominate coastal townsites in Nuuk, Sisimiut, Ilulissat etc.
- **Roads are the primary infrastructure exposure**: research found **39% of paved roads assessed in Ilulissat are on highly hazardous frost-susceptible terrain** (*Cardelli et al., Cold Regions Science & Tech 2024 — single-study figure; pre-purchase consult Asiaq for parcel-specific*) [doi link via sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0165232X2400017X); Ilulissat roads on permafrost require resurfacing every 2–3 years
- **Where permafrost-bearing building foundations DO exist** (older Ilulissat blocks, parts of east Greenland, Disko Bay margins), thaw-driven settlement is documented
- **Asiaq Greenland Survey** monitors permafrost via the ESA AALM4INFRAM project across 6 settlements incl. Ilulissat + Sisimiut + Kangerlussuaq, producing frost-susceptibility, frost-heave + active-layer-thickness maps: [asiaq.gl/forskningsprojekter/esa-aalm4infram-permafrost](https://www.asiaq.gl/forskningsprojekter/esa-aalm4infram-permafrost-english/)
- Polar Portal — DK national permafrost-monitoring portal: [polarportal.dk/en/greenland/frozen-ground](https://polarportal.dk/en/greenland/frozen-ground/)
- **Kangerlussuaq airport** lost major commercial traffic in 2024 due to permafrost-driven runway instability ([HighNorthNews 2024](https://en.highnorthnews.com/business/greenlands-kangerlussuaq-airport-to-close-for-major-commercial-traffic-in-2024-due-to-climate-change/100931)) — example of how thaw is reshaping transport
- **Pre-purchase**: ask for the building's foundation type (bedrock-bearing / ventilated crawl-space / piled / thermosyphon). Foundation-type uncertainty on a pre-1990 building in Ilulissat-zone = MEDIUM-to-HIGH risk
- Cost to remediate a thaw-settled foundation: data not publicly aggregated; demolition + rebuild often more economic than retrofit

### Coastal flooding / storm surge

- Many bygder are at-grade coastal settlements; sea-level rise + storm surge intensification documented
- Source: [DMI Klimaatlas Grønland](https://www.dmi.dk/klima/) (verify GL-specific section)
- No nationwide parcel-level flood-risk register equivalent to ERRIAL; verification path = ask Asiaq + the kommune's planlægningsafdeling

### Isolation costs

- No road network between towns. All transit by Air Greenland (helicopter to bygder) or Royal Arctic Line (sea freight)
- Construction materials must be shipped in season → freight is a 20–40% premium over Danish prices `est.`
- Emergency repairs to a winter-isolated bygd may need to wait until thaw — pre-stock parts

### Mineral / subsoil overlay

- **All subsoil + surface rights to land are administered by the Government of Greenland** under [Mineral Resources Act (Råstofloven) — Parliament Act No. 7 of 7 Dec 2009, in force 1 January 2010, consolidation as amended to Act No. 39 of 28 Nov 2019](https://govmin.gl/wp-content/uploads/2024/02/Unofficial-translation-of-unofficial-consolidation-of-the-Mineral-Resources-Act.pdf). Verbatim from MLSA: *"In Greenland there is no privately owned land, all rights to any use of land is administered by the Government of Greenland."*
- A mining or hydrocarbon licence can be granted across or under an area where a building stands; the licence-holder compensates impacted brugsret-holders but does not need their consent for licence issuance
- **Small-scale mining rights**: vest in local residents (Mineral Resources Act, special provisions); verify if buying near an active small-scale-mining locality
- **Unofficial consolidated EN translation** (2024): [govmin.gl/wp-content/uploads/2024/02/Unofficial-translation-of-unofficial-consolidation-of-the-Mineral-Resources-Act.pdf](https://govmin.gl/wp-content/uploads/2024/02/Unofficial-translation-of-unofficial-consolidation-of-the-Mineral-Resources-Act.pdf)
- Active-licence register: [govmin.gl](https://govmin.gl/) — check property coordinates against licensed areas pre-offer

### Build-era hazards

- Pre-1990 builds: PCB sealant + asbestos likely (DK construction practice imported); inspection required
- Wood-clad buildings: rot + moisture-bridge issues in coastal climates
- 1960s–1970s mass-housing (Blok P legacy, mostly demolished): poor envelopes; thermal bridge

---

## Section: `--mains` (utilities)

- **Water**: [Nukissiorfiit](https://www.nukissiorfiit.gl/) — sole utility; town supply potable; bygder often have water taps + tanker delivery
- **Electricity**: also Nukissiorfiit. ~70% renewable (hydropower in Nuuk / Sisimiut / Ilulissat); diesel-fired in smaller settlements
- **Heating**: typically oil-fired (Polaroil) + district heat in larger towns; verify connection
- **Sewage**: town-level treatment in Nuuk/Sisimiut; **night-soil collection** (`natrenovation`) still operative in many bygder for houses without sewer connection
- **Telecoms**: [Tusass A/S](https://www.tusass.gl/) (state-owned, sole operator); fibre in main towns, satellite/4G in bygder

**Verification**: Nukissiorfiit + Tusass + the kommune's tekniske forvaltning each maintain a connection register. Ask the seller for current bills.

---

## Section: `--transaction` (notary / advokat / conveyancing process)

Greenland uses **advokat (lawyer)** conveyancing, NOT a civil-law notary (no notarial system in Greenland — Anglo-Danish hybrid practice).

Typical sequence:

1. **Offer** (`købstilbud`) — usually subject to financing + arealtildeling transfer approval
2. **Købsaftale** (sale contract) — usually in Danish; Kalaallisut translation on request
3. **Application to kommune** to transfer arealtildeling — kommunal review period (weeks to months); for properties in bygder, the application is routed via the local **`bygdebestyrelse`** (settlement council) before reaching the kommune or Naalakkersuisut
4. **For non-§ 3 / non-§ 4 buyers under Inatsisartutlov 78/2025**: application to Departementet for Boliger og Infrastruktur for § 9 dispensation
5. **Tinglysning of building deed** at Tinglysningsretten — Danish system
6. **Mortgage tinglysning** (if any)
7. **Possession + key handover** + final settlement

Greenlandic-language documents are common in correspondence with municipal authorities (Kalaallisut). The legally binding text of standard købsaftale is usually Danish; ensure a translated copy is provided.

**Bar of Greenland**: [Grønlands Advokatforening](https://www.advokatsamfundet.dk/) (Greenland-section under Danish Bar). Limited local roster; many transactions handled by Nuuk-based or DK-based advokater.

---

## Section: `--work` (employment / remote work overlay)

Greenland's labour market is small (~28,000 jobs `est.` — verify against [bank.stat.gl](https://bank.stat.gl/) employment series; ~56,000 population per Statistics Greenland 2025, see § Country profile). Property purchase is generally tied to either (a) a posted position in a Greenlandic employer / public sector, or (b) a registered Greenland-resident self-employed activity.

**Posted-employee status**:

- Tax-treaty exception: Danish nationals posted to Greenland on contracts ≤ 6 months remain Danish-tax-resident (verify per current DK-GL tax convention)
- Greenland-domiciled employers handle A-skat withholding through [aka.gl](https://www.aka.gl/); see the [Skattetræk i Grønland guide (DA, Sept 2026 edition)](https://aka.gl/emner/borger/skat/vejledninger-skat)
- The 35% flat oil/gas/mineral/construction-worker rate applies if not locally taxed in prior 6 months (PwC 2026)

**Self-employed / remote-work**:

- Foreign remote-worker income (W-2 in another country) earned while sitting in Greenland: triggers full Greenland tax residency if ≥ 6 months / center-of-vital-interests in GL
- No digital-nomad visa programme equivalent — entry is governed by general Danish residence rules with Greenland-specific permit overlay
- Property ownership does NOT grant residence; Inatsisartutlov 78/2025 and immigration law operate independently — and § 4 is even stricter, requiring **prior** 2-year residence (you cannot acquire to obtain residence)

**Major employers in towns**:

- Public sector (Naalakkersuisut + kommuner) — largest single employer
- **Royal Greenland A/S** (state-owned seafood) — outside Nuuk
- **Air Greenland A/S** — Nuuk + airport hubs
- **Royal Arctic Line** — Nuuk + sea-freight
- **Tusass A/S** — telecom (Nuuk)
- **Grønlandsbanken** + **BankNordik Grønland** — Nuuk

Verify open positions: [job.gl](https://www.job.gl/) (national job board).

---

## Section: `--climate`

- Cold-climate: Nuuk mean ~Jan –7 °C, ~Jul +7 °C; Ilulissat ~Jan –13 °C, ~Jul +8 °C `est.` (monthly-mean normals — verify reference period against [DMI Klimaatlas](https://www.dmi.dk/klima/) / climatedata.dk)
- Heating-degree-days drive energy cost — annual heating bill in Nuuk house: ~DKK 30,000–60,000 `est.` (varies with insulation)
- Climate-change trajectory ([DMI Klimaatlas](https://www.dmi.dk/klima/)): +2–4 °C by 2100 likely; permafrost retreat northward; ice-cap melt sea-level contribution material
- Polar night / midnight sun: north of Arctic Circle (above ~66°N — Sisimiut, Ilulissat, Uummannaq, Upernavik, Qaanaaq) → ~2 months no-sun winter; ~2 months no-night summer. Affects mental-health, energy use, daylight-design of housing.

---

## Leaving Greenland — origin-jurisdiction deregistration entry points

For GL-resident buyers moving abroad. **Doorway only** — see [`shared/cross-border.md`](../../shared/cross-border.md) for framework + [`shared/home-tax.md`](../../shared/home-tax.md) for tax detail. Mandatory call-out: engage cross-border tax counsel in BOTH jurisdictions before moving the centre of vital interests; Greenland's separate tax system means even relocation back to mainland DK is a cross-border move for tax purposes.

| Register | Action | Authority | URL |
|---|---|---|---|
| Tax residence | File final-year Greenlandic return with foreign address; verify DK-GL inter-realm tax convention tie-breaker | Skattestyrelsen i Grønland | [aka.gl](https://www.aka.gl/) |
| Folkeregister (civil register) | Notify departure via kommune folkeregister | Local kommune | (commune-level) |
| Health insurance | Notify [Sundhedsvæsenet Grønland](https://www.peqqik.gl/) of departure; no S1 — Greenland is outside EU/EEA scope | Peqqissaaneq (Health Service) | [peqqik.gl](https://www.peqqik.gl/) |
| Mineral / hunting / fishing licences (if held) | Surrender or transfer | Departement for Fiskeri og Fangst | [naalakkersuisut.gl](https://naalakkersuisut.gl/) |
| Building disposition | Either transfer brugsret + tinglysning (subject to §§ 3-9 buyer-class gating on transferee), OR notify kommune of vacancy (which can trigger arealtildeling lapse) | Issuing kommune (bygder via `bygdebestyrelse`) | (kommune-level) |

**Cross-link**: invoke `--cross-border` for the DTA framework and `--home-tax` for GL-side annual / disposal / death / emigration detail.

---

## Visa / residence overlay (cross-link)

- **Greenland is NOT part of the EU** (despite the Kingdom of Denmark being a Member State). Greenland withdrew via the 1985 Greenland Treaty.
- **Greenland is also NOT part of the Schengen Area** and NOT part of the EU customs union. Entry is governed by Danish immigration law with Greenland-specific permits issued by [Udlændingestyrelsen (SIRI)](https://www.nyidanmark.dk/) on Greenland portal: [nyidanmark.dk/groenland](https://www.nyidanmark.dk/) (verify GL sub-section).
- Property ownership ≠ residency right. Inatsisartutlov 78/2025 and immigration law operate independently — § 4 even requires **prior** 2-year residence before acquisition.

---

## Common quirks unique to Greenland

- **No land cadastre** — orient using building register, not parcel register
- **No VAT** — pricing comparisons with mainland DK / EU are non-trivial; import duties replace it on many goods
- **Currency hedge**: DKK ↔ EUR is pegged (ERM II); cross-realm payments do not need FX hedging. Cross-realm CHIPS-style bank wires are within DK national payment system.
- **DK national grid for legal acts**: Danish-law statutes can apply in Greenland if Greenland has not adopted its own version; ambiguity is common — flag in advokat review
- **"Open-door" precedent** in some bygder (custom): historically, doors unlocked; not a security legal regime — be wary of any "open settlement" claims in listings
- **EU residence/citizenship pathway**: Greenland residence does NOT grant EU rights. Danish citizenship via Greenland residence requires meeting national naturalisation rules.
- **Bygd governance**: outer settlements are administered by a local `bygdebestyrelse` (settlement council) that mediates arealtildeling between residents and the kommune / Naalakkersuisut.

---

## Common listing platforms

- [boligportal.gl](https://www.boligportal.gl/) ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row — rentals + some sales
- [estate.gl](https://www.estate.gl/) ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row — verify URL
- [dba.dk](https://www.dba.dk/) (Greenland filter) — second-hand market incl. cabins (`hytter`)
- Facebook Marketplace "Sælges i Nuuk" — private-sale signal

## Reddit / forum sources for operator stories

- r/greenland — sparse but useful for expat anecdotes; on-topic land-ownership thread: [r/greenland — Buying a land/renting in Greenland (1cq7b5b)](https://www.reddit.com/r/greenland/comments/1cq7b5b/buying_a_land_renting_in_greenland/) — locals corroborate the structural no-land-ownership claim (community signal, not load-bearing)
- [The Arctic Institute — Greenland legal/land commentary](https://www.thearcticinstitute.org/) — non-government but credible analyst

## Source URL templates

| Topic | URL |
|---|---|
| Self-Government Act | [retsinformation.dk Selvstyreloven 2009](https://www.retsinformation.dk/eli/lta/2009/473) |
| Naalakkersuisut (Govt) | [naalakkersuisut.gl](https://naalakkersuisut.gl/) |
| **Inatsisartutlov 78/2025 (acquisition act, in force 1 Jan 2026)** | [nalunaarutit.gl — Inatsisartutlov nr. 78 af 21.11.2025](https://nalunaarutit.gl/groenlandsk-lovgivning/2025/inatsisartutlov-nr-78-af-21_11_2025?sc_lang=da) |
| Inatsisartutlov 78/2025 — forarbejder | [nalunaarutit.gl PDF](https://nalunaarutit.gl/-/media/lovfiler/2025/forarbejder/ina_78/fast-ejendom_lovbemaerninger_da.pdf) |
| 2025 buyer-restriction announcement (superseded source) | [naalakkersuisut.gl/Nyheder/2025/02/0302_fast_ejendom](https://naalakkersuisut.gl/Nyheder/2025/02/0302_fast_ejendom?sc_lang=da) |
| Tax authority (Skattestyrelsen) | [aka.gl](https://www.aka.gl/) |
| **aka.gl — Skattetræk i Grønland (DA, Sept 2026 edition; rules as at 1 Jan 2025)** | [aka.gl vejledninger](https://aka.gl/emner/borger/skat/vejledninger-skat) |
| Citizen portal | [sullissivik.gl](https://sullissivik.gl/) |
| Statistics Greenland | [stat.gl](https://www.stat.gl/) · [bank.stat.gl](https://bank.stat.gl/) |
| Tinglysning (DK system applies) | [tinglysningsretten.dk](https://www.tinglysningsretten.dk/) · [tinglysning.dk](https://www.tinglysning.dk/) |
| Asiaq Greenland Survey | [asiaq.gl](https://www.asiaq.gl/) |
| DMI Klimaatlas | [dmi.dk/klima](https://www.dmi.dk/klima/) |
| Mineral Licence and Safety Authority (MLSA) | [govmin.gl](https://www.govmin.gl/) |
| Bank of Greenland | [banken.gl](https://www.banken.gl/) |
| BankNordik Grønland | [banknordik.gl](https://www.banknordik.gl/) |
| Danish FSA | [finanstilsynet.dk](https://www.finanstilsynet.dk/) |
| Iserit A/S (public housing) | [iserit.gl](https://www.iserit.gl/) |
| Nukissiorfiit (utility) | [nukissiorfiit.gl](https://www.nukissiorfiit.gl/) |
| Tusass A/S (telecom) | [tusass.gl](https://www.tusass.gl/) |
| Visit Greenland (STR licensing) | [visitgreenland.com](https://visitgreenland.com/) |
| Inatsisartut (parliament) | [ina.gl](https://ina.gl/) |
| Nordic taxation overview | [norden.org info-norden taxation-greenland](https://www.norden.org/en/info-norden/taxation-greenland) |
| Immigration (SIRI / Greenland) | [nyidanmark.dk](https://www.nyidanmark.dk/) |

## Verification authorities

- **Kommune's arealtildelingsafdeling** (one of the five kommuner) — for the brugsret transfer; bygd files routed through the local `bygdebestyrelse`
- **Departementet for Boliger og Infrastruktur** (Naalakkersuisut) — for § 9 dispensation under Inatsisartutlov 78/2025
- **Tinglysningsretten** (Hobro, DK) — for building-title status
- **Advokat / advokatfirma** (Nuuk-based preferred) — for transaction supervision
- **Asiaq Greenland Survey** — for permafrost / ground-condition baseline
- **MLSA** (Mineral Licence and Safety Authority, govmin.gl) — for any mineral-licence overlay
- **Skattestyrelsen i Grønland** (aka.gl) — for tax residence + treatment

## Status

**Confidence**: **MEDIUM** overall

- **HIGH** on `--ownership` — Inatsisartutlov nr. 78 af 21. november 2025 verified against primary statute (nalunaarutit.gl) + forarbejder + industry commentary; §§ 3-9 eligibility table direct from statute
- **HIGH** on the structural facts (no land ownership — `primary-verified` via MLSA verbatim; brugsret regime; no VAT; dual banking + supervision)
- **MEDIUM** on specific tax rates and threshold figures (aka.gl 2025 EN PDF now cited as primary; PwC retained as cross-reference; verify per-municipality rates against the PDF before reliance)
- **LOW** on price/m² benchmarks (no open sales register equivalent to DVF; private-market data is opaque)
- **LOW** on parcel-level permafrost / flood data (no national parcel-risk register; case-by-case via Asiaq + kommune)

**Last verified**: 2026-05-27. Ownership tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).

**On PR merge — regulatory-watch.md addition required** (currently zero GL entries): Tier-1 entry for **Inatsisartutlov nr. 78 af 21. november 2025 om erhvervelse af adkomst eller brugsret til fast ejendom**, effective 1 January 2026, affecting all foreign-buyer rules across `--ownership`, `--banking`, `--transaction`, `--rental`, `--work`, `--visa` sections; revisit cadence 12 months; source URL [nalunaarutit.gl](https://nalunaarutit.gl/groenlandsk-lovgivning/2025/inatsisartutlov-nr-78-af-21_11_2025?sc_lang=da). Companion entries: 2026 rental-law (lejelov) consultation — tier 3, revisit 6 months; Mineral Resources Act 2010 (last amended 2019) — tier 4 informational anchor.

## ⚠️ Run quality notes

- Inatsisartutlov nr. 78/2025 was identified during validation (2026-05-27) as having been **enacted** on 21 November 2025 with effective date 1 January 2026 — superseding the 3 Feb 2025 FFL annotation that the original draft treated as the operative source. The `--ownership` section has been rewritten against the primary statute (nalunaarutit.gl) and forarbejder; the 3 Feb 2025 announcement is retained as a policy-rationale source.
- Tax-rate table sourced from PwC 2026 cross-reference; **primary citation now points to the aka.gl 2025 EN withholding guide (PDF, July 2025)** rather than PwC's reproduction. Re-verify the per-municipality column against the PDF before reliance.
- The govmin.gl "no privately owned land" quote is `primary-verified` via independent Tavily search returning the verbatim snippet from the live MLSA page, even though direct WebFetch failed TLS during research. Confidence on this structural fact is HIGH.
- Reddit signal: thin, as expected. Only one on-topic operator thread ([r/greenland 1cq7b5b](https://www.reddit.com/r/greenland/comments/1cq7b5b/buying_a_land_renting_in_greenland/)) corroborates the no-private-land claim; cited as community signal, not load-bearing.
- The 2026 Greenlandic rental-law reform (`forslag til Inatsisartutlov om leje af boliger`) was in public consultation as of March 2026 — `verify status as of publish date`.
- Price/m² figures in `--price` are orientation `est.` only — no sold-price register equivalent to DVF / Catastro exists for Greenland.
- norden.org taxation-greenland page returned HTTP 403 during this research run; tax structure restated from aka.gl 2025 EN PDF (primary) + PwC (cross-reference) + ina.gl FFL URLs.
- Cardelli et al. 2024 "39% of Ilulissat paved roads on highly hazardous frost-susceptible terrain" is a single-study figure — pre-purchase, consult Asiaq for parcel-specific frost-susceptibility data.
