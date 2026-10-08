# Universal `--auction-registry` Section — Distressed / Judicial / Foreclosure Auction Discovery & System Classification

Where DISTRESSED property is actually published per country — judicial / foreclosure / mortgagee / tax-seizure auctions — and, more importantly, **which kind of system** the country runs, because that determines whether a single official portal exists at all. Loaded when `--auction-registry` is invoked.

**Snapshot**: June 2026.

**Scope**: this is a **discovery + system-classification** layer, not a how-to-bid-at-auction guide. It answers *"is there an official registry where a foreign buyer can see upcoming distressed sales, and can it be trusted as a primary source?"* — and classifies the country into one of five system types so the answer is honest even where no portal exists. **Distinct from `--type=auction`** (the buyer-journey template for the mechanics/risks of *buying* at auction — deposit rules, vacant possession, caveat emptor, gazumping); distinct from `--scams` (fraud taxonomy) and `--notary`/`--remote` (deed execution). It pairs with `--type=auction` (this tells you *where*; that tells you *how*) and with `--finance` (auction purchases are usually cash / pre-approved, no finance-subject clause).

## Universal contract

For the property's country, return:

1. **System type** (classify first — see the spine below): PRIMARY-OFFICIAL central portal · REGULATED-ENTITY-OFFICIAL (notary/bailiff-chamber portal) · PRIMARY-OFFICIAL-but-split/gazette · FRAGMENTED (per-county/court, no central) · AGGREGATOR-ONLY (commercial houses, no official registry) · NONE-CONFIRMED (no public registry confirmed)
2. **The channel** — the named official portal + URL where one exists, OR the honest fallback ("advertised in the `<X>` Official Gazette + press — no central registry; verify with the competent court"). Never invent a portal.
3. **What it publishes** — upcoming lots / auction date / reserve or opening price / property detail / online vs in-room bidding
4. **The foreigner gate — on three independent axes** (do not merge): (a) *mechanism access* (national e-ID / digital certificate / in-person registration often blocks a non-resident even where bidding is legal); (b) *legal eligibility to bid*; (c) *underlying foreign land-ownership limit* (the binding constraint in much of APAC/MENA — a foreigner may be able to bid but not to own the land)
5. **Source tier** — PRIMARY (official/regulated) · SECONDARY (commercial aggregator, seller-controlled, cross-check) · or "no citable registry"
6. **Confidence** — HIGH / MEDIUM / LOW per the skill's contract

## The system spine (classify first)

Whether a single trustworthy registry exists is set by the country's enforcement architecture, not by how digital it looks:

- **🟢 PRIMARY-OFFICIAL central portal** — one government/court/gazette-agency site lists effectively all judicial/foreclosure real-estate auctions nationwide, searchable, citable as fact. The civil-law judicial-auction model (continental Europe + much of APAC + parts of LATAM): ES, DE, AT, IT, PT, GR, MT, SE, IS, SI, HR, LT, LV, RS, GE, TR, JP, KR, MO, TH, ID, VN, IN, CL, PE, EC, etc.
- **🟡 REGULATED-ENTITY-OFFICIAL, or PRIMARY-but-split/gazette** — official, but run by a notary/bailiff chamber rather than a ministry (NL, BE, CZ, PL, HU, RO, BG, EE, MD, AD), OR official but spread across a gazette / federal-and-state / app-only channel rather than one searchable portal (DK + MC Journal officiel; DK Statstidende; AR national-plus-provincial; MX state-plus-SAT; CO/UY/CR/BB gazette; QA app-only; SA/JO enforcement portals). Cite the named channel; it is primary but not a single slick search UI.
- **🟠 FRAGMENTED, or AGGREGATOR-ONLY** — no official central registry. Either per-county/per-court/per-bailiff (US sheriff sales, CA provinces, CH cantons, ZA sheriff, IL receivers, the Western Balkans) or sold through **commercial** auction houses / licensed auctioneers (UK, IE, AU, NZ, HK, SG, NG, KE, GH, MA, BZ). The listing channels here are **SECONDARY** (seller-controlled) — quote them, never present them as official.
- **🔴 NONE-CONFIRMED** — no public auction registry could be confirmed; sales are advertised case-by-case in the official gazette / local press or handled privately by banks/courts (LU, SM, the Crown Dependencies, several GCC + African + small-island markets). The honest output is *"verify with the competent court / official gazette"*, never a fabricated URL.

## Verdict bands

| Band | Trigger | Read |
|---|---|---|
| 🟢 | One official, searchable government/court portal lists distressed sales nationwide | "Search the official portal directly; it is your primary source — but check the foreigner gate before relying." |
| 🟡 | Official but split/gazette/app/regulated-chamber — primary, not one search UI | "Use the named official channel(s); set up the e-ID / certificate early — that, not nationality, is the usual block." |
| 🟠 | No official registry — per-county/court fragmentation OR commercial auction houses | "There is no official registry; the named channels are seller-controlled/secondary — cross-check every figure, never treat as authoritative." |
| 🔴 | No public registry confirmed | "Do not rely on a portal — engage local counsel to watch the competent court / official gazette; treat any 'national auction site' claim as unverified." |

## ⚠️ 7 cross-cutting traps

1. **"There's a digital portal" ≠ "there's an official registry."** The single biggest fabrication risk. The US, UK, AU, NZ, IE, HK, SG have busy auction *websites* — every one is **commercial** (EIG, auction.com, Xome, BidX1, domain.com.au, Knight Frank). They are seller-controlled secondary sources, not government registries. Conversely a country can have a pristine official portal (JP BIT, ID lelang.go.id) you'd never find by searching English-language listing sites. Classify the *system* before trusting the *site*.
2. **The foreigner gate is three things, not one.** (a) *Mechanism access* — most official portals require a national e-ID / digital certificate / in-person registration (HR FINA token, SI/LV/LT e-ID, ES FNMT cert, CY CyLogin, HU in-person, CN a Chinese bidding agent) that blocks a non-resident even though bidding is legal. (b) *Legal eligibility* to bid. (c) *Underlying land-ownership limit* — in TH/ID/VN/PH/KH/CN a foreigner may bid but cannot own the land (condo quotas / leasehold only); in CH (Lex Koller), LI/MT/AD, the OECS/BVI (Alien/Non-Belonger Landholding Licence), BM (licence + high ARV) ownership is gated. Winning the bid is worthless if axis (c) bars you.
3. **Judicial-foreclosure ≠ tax-seizure ≠ state-asset sale — different channels.** Court foreclosures and tax-authority seizures are usually published on *separate* portals (ES subastas.boe.es covers both, but PT Finanças, GR AADE, SI FURS, BE finshop, MX SAT, TW MOJ-AEA, MO DSF run tax sales apart from the judicial portal). EG `auctions.realestate.gov.eg` is a **state real-estate MLS, not a foreclosure registry** — a classic mis-cite. UZ `davaktiv.uz` is the State Assets Agency platform; the court-enforcement path may sit on `e-auksion.uz` (E-IJRO) — confirm which. Name the right channel for the right kind of distress.
4. **Mind the official-vs-lookalike domain.** Private aggregators mirror official data on near-identical domains: KR `courtauction.co.kr` (private) vs `.go.kr` (official); JP `981.jp` (private) vs `bit.sikkou.go.jp` (Supreme Court); IN `bankeauctions.com` (private) vs `ibapi.in`/`baanknet.com` (official); MX "REM@JU" is **Peru's** national portal (`remaju.pj.gob.pe`), not Mexico's. One character of domain decides primary-vs-secondary.
5. **Gazette-official is real but it is not a search portal.** In DK, BB, the OECS (LC/GD/AG/KN), DO, JM, and much of the common-law Caribbean, the *official* channel is the Official/Government Gazette (statutory notice), with no filterable property search. That is a legitimate PRIMARY source — but a buyer must read the gazette/press, and commercial sites that re-list those notices are SECONDARY.
6. **A "vesting" procedure is not an auction.** Jersey *dégrèvement* / *réalisation* and Guernsey *saisie* are customary-law procedures that **vest** the realty in a secured creditor by Royal Court order — there is no public auction and no auction registry to watch. Do not describe them as auctions. (Greenland has **no private land ownership** at all — only building + land-use rights — so a conventional land auction is conceptually inapplicable.)
7. **Below-market price is the bait; the encumbrances are the hook.** Distressed lots commonly open at 50–70% of assessed value, but typically sell *voetstoots* / as-is, often without vacant possession, with the buyer taking unpaid charges/occupants/title defects. The registry tells you *where* to look; due diligence (title, occupancy, arrears, `--type=auction`) decides whether the discount is real. This section is discovery, not a green light.

## Regional patterns + country one-liners

The 6 region blocks below span all 126 supported countries. Each line: **band · system type · channel (URL where confirmed) · foreigner gate**. Where no official registry was confirmable it is marked 🔴 honestly rather than guessed.

---

## Western Europe + EFTA + microstates + UK + Crown Dependencies

- **ES** Spain — 🟢 PRIMARY-OFFICIAL — **Portal de Subastas del BOE** ([subastas.boe.es](https://subastas.boe.es)), the State Gazette agency: all judicial + AEAT tax auctions nationwide, ~20-day online windows, opening often 70% of value. Gate: FNMT digital cert + ES bank transfer.
- **IT** Italy — 🟢 PRIMARY-OFFICIAL — **PVP — Portale delle Vendite Pubbliche** ([pvp.giustizia.it](https://pvp.giustizia.it), Min. Giustizia; the ROADMAP's "TPC" label was wrong). All court-ordered sales; online offers via SPID/PEC or a delegate.
- **DE** Germany — 🟢 PRIMARY-OFFICIAL — **ZVG-Portal** ([zvg-portal.de](https://www.zvg-portal.de), joint Länder judicial administrations). Nationwide Zwangsversteigerung dates + appraisals/photos; ~10% security at the Amtsgericht, no residency bar.
- **AT** Austria — 🟢 PRIMARY-OFFICIAL — **Ediktsdatei** ([edikte.justiz.gv.at](https://edikte.justiz.gv.at), Federal Min. of Justice), online-exclusive. ~10% Vadium at the Bezirksgericht; no nationality bar.
- **PT** Portugal — 🟢 PRIMARY-OFFICIAL — **e-Leilões** ([e-leiloes.pt](https://www.e-leiloes.pt), Ordem dos Solicitadores e Agentes de Execução; CPC Art. 837). Open to foreigners abroad on the same terms. (Tax seizures separately via Finanças.)
- **GR** Greece — 🟢 PRIMARY-OFFICIAL — **eauction.gr** (notary-operated, MoJ-supervised): since 2018 all foreclosures here, ≥45-day notice; foreign individuals + companies may participate. (State/tax sales separately via AADE.)
- **MT** Malta — 🟢 PRIMARY-OFFICIAL — **Malta eCourts — Judicial Sales** ([ecourts.gov.mt/onlineservices/JudicialSales](https://ecourts.gov.mt/onlineservices/JudicialSales)). Remote bidding via PoA; AIP permit to own is a separate axis.
- **FR** France — 🟡 no single state portal — judicial sales (*ventes aux enchères judiciaires*) run at the *tribunal judiciaire*; **bidding is only through a mandatory avocat**; cahier des conditions at the court. `licitor.com` aggregates (SECONDARY); `encheres-publiques.com` is a commercial aggregator, **not** an official portal. Cite the avocat/tribunal channel.
- **NL** Netherlands — 🟡 REGULATED-ENTITY-OFFICIAL — **veilingnotaris.nl** (KNB, Royal Dutch Notaries); statutory ≥30-day publicity. `veilingbiljet.nl` and other veiling sites are commercial. Identify with the auction-notary to bid.
- **BE** Belgium — 🟡 REGULATED-ENTITY-OFFICIAL — **Biddit** ([biddit.be](https://www.biddit.be), Fednot — Belgian notaries), the only official notary-sale platform incl. forced sales; e-ID/itsme auth. (Tax seizures via finshop.belgium.be.)
- **CH** Switzerland — 🟠 FRAGMENTED — no national registry: federal SchKG, published via the **SOGC/SHAB** ([shab.ch](https://www.shab.ch)) + 26 cantonal gazettes + the competent **Betreibungsamt** (≥1-month notice). Aggregators (localauction.ch) are SECONDARY. **Lex Koller** restricts foreign residential ownership — a hard gate.
- **IE** Ireland — 🟠 AGGREGATOR-ONLY — no central registry; lender/receiver sales via **BidX1** ([bidx1.com](https://bidx1.com)), iamsold (SECONDARY). Tailte Éireann records transactions, not auctions. No nationality bar; AML with the house.
- **UK** United Kingdom — 🟠 AGGREGATOR-ONLY — no government foreclosure registry; mortgagee/receiver lots via commercial auction houses, de-facto aggregated by **EIG** ([eigpropertyauctions.co.uk](https://www.eigpropertyauctions.co.uk), private). HMLR/Registers of Scotland record sales, not listings. SDLT non-resident surcharge is a tax, not an access bar.
- **CY** Cyprus — 🟠 FRAGMENTED — creditor-led since 2022, no single portal: **ACB E-Auctions** (Cyprus Banking Association) + **KEDIPES** ([kedipes.com.cy](https://kedipes.com.cy)) + Gordian/Themis/Altamira on the CyLogin/Ariadne layer; ≥45-day notice. Non-EU buyers may need a Council-of-Ministers permit to own.
- **SE** Sweden — 🟢 PRIMARY-OFFICIAL — **Kronofogden** (Swedish Enforcement Authority, auktionstorget/auktion.kronofogden.se): executive sales of seized real estate; no nationality bar.
- **DK** Denmark — 🟡 PRIMARY-OFFICIAL (gazette) — **Statstidende** ([statstidende.dk](https://www.statstidende.dk)), the Official Gazette: statutory ≥14-day notice of every *tvangsauktion*; process at the Fogedret (domstol.dk). Non-EU may face an acquisition permit (separate). tvangsauktioner.dk is commercial.
- **FI** Finland — 🟠 AGGREGATOR (govt-conducted) — the **Enforcement Authority (Ulosottolaitos)** conducts forced sales but lists/runs them on the **commercial Huutokaupat.com**; there is no `.fi` government auction portal. Cite the authority for status, the platform for listings (SECONDARY).
- **NO** Norway — 🟠 FRAGMENTED — no central listing portal; the District Court appoints a *medhjelper* who markets each *tvangssalg* via ordinary channels (commonly finn.no). domstol.no is process-only. Do not cite a "national NO auction portal."
- **IS** Iceland — 🟢 PRIMARY-OFFICIAL — **island.is** District Commissioners' auctions ([island.is/en/o/district-commissioner/auctions](https://island.is/en/o/district-commissioner/auctions)), *nauðungarsala*. Non-EEA acquisition is restricted (separate axis).
- **LU** Luxembourg — 🔴 NONE-CONFIRMED — notary-conducted forced sales (*saisie immobilière*, Loi 1889) published in the official journals + notary sites; **no single central registry confirmed** (ventespubliques.lu / clicpublic.lu are commercial, unverified). Verify with the conducting notaire.
- **LI** Liechtenstein — 🟡 PRIMARY-OFFICIAL (qualified) — **Fürstliches Landgericht** ([gerichte.li](https://www.gerichte.li)) enforcement auctions + Amtsblatt; online real-estate listing not fully surfaced. Compulsory-auction acquisition needs **Land Transfer Act** authorisation — a real foreign-buyer gate.
- **AD** Andorra — 🟡 REGULATED-ENTITY-OFFICIAL — **BOPA** gazette ([bopa.ad](https://www.bopa.ad)) + the **saig** (Chamber of Bailiffs, saigandorra.com); start 70% of valuation (50% at 2nd auction). Foreign-investment authorisation to own is separate.
- **MC** Monaco — 🟡 PRIMARY-OFFICIAL (gazette) — **Journal de Monaco** ([journaldemonaco.gouv.mc](https://journaldemonaco.gouv.mc)) + Tribunal de Première Instance. Non-residents **must** bid through a Monégasque Avocat-Défenseur.
- **SM** San Marino — 🔴 NONE-CONFIRMED — the **Tribunale Unico** ([tribunale.sm](https://www.tribunale.sm)) conducts auctions; no central online registry confirmed; heavy foreign-ownership restriction. Verify with the court.
- **JE** Jersey — 🔴 NONE-CONFIRMED — Royal Court **dégrèvement / réalisation** *vests* realty in creditors (a procedure, **not an auction**); notices in the Jersey Gazette. No auction registry to watch.
- **GG** Guernsey — 🔴 NONE-CONFIRMED — Royal Court **saisie** *vests* realty in a creditor (**not an auction**); La Gazette Officielle + 28-day Greffe register. No auction registry.
- **IM** Isle of Man — 🔴 NONE-CONFIRMED — mortgagee power of sale (Conveyancing Act 1960) to the open market; no Manx official gazette for this. Verify with the selling lender / advocate.
- **GI** Gibraltar — 🔴 NONE-CONFIRMED — English-style Supreme Court mortgagee sale; the Gibraltar Gazette carries government notices only (no realty-auction registry; the organised judicial-sale stream is Admiralty *ship* arrest).
- **FO** Faroe Islands — 🔴 NONE-CONFIRMED — forced sale via the local *Fógd*/court; notices in local press (Dimmalætting/Sosialurin). Sits **outside** the Danish Statstidende model.
- **GL** Greenland — 🔴 NONE-CONFIRMED — forced sale via the Kredsret; **no private land ownership exists** (building + land-use rights only), so a conventional land auction is inapplicable; foreign acquisition is being tightened.

### Confidence
HIGH for ES/IT/DE/AT/PT/GR/MT/NL/BE/SE/DK/IS/CH/IE/UK/CY/MC/AD; MEDIUM for FR (no-central-portal structure confirmed), LI (listing caveat), FI/NO (govt-conducted-but-no-portal); LOW/NONE-CONFIRMED for LU, SM and the 6 Crown Dependencies/territories (correctly downgraded, not guessed).

---

## CEE + Western Balkans + Baltics + Caucasus + Central Asia

- **CZ** Czechia — 🟡 REGULATED-ENTITY-OFFICIAL — **Portál dražeb** ([portaldrazeb.cz](https://www.portaldrazeb.cz), Czech Bailiffs Chamber) + Central Register of Enforcements; AML ID to bid.
- **SK** Slovakia — 🟢 PRIMARY-OFFICIAL — executor (judicial) auctions in the **Obchodný vestník** ([obchodnyvestnik.justice.gov.sk](https://obchodnyvestnik.justice.gov.sk), Min. of Justice); voluntary/pledge auctions in the **NCRdr** notary register (notar.sk). Don't conflate the two.
- **PL** Poland — 🟡 REGULATED-ENTITY-OFFICIAL — **licytacje.komornik.pl** (National Council of Court Bailiffs) + e-licytacje for e-auctions.
- **HU** Hungary — 🟡 REGULATED-ENTITY-OFFICIAL — **MBVK EÁR** ([arveres.mbvk.hu](https://arveres.mbvk.hu), Chamber of Judicial Officers). Bidding needs in-person registration at a HU judicial officer (~6,600 HUF) — a non-resident hurdle; ag-land restricted.
- **SI** Slovenia — 🟢 PRIMARY-OFFICIAL — **SodneDrazbe.si** (Supreme Court platform; online since 1 Feb 2021), accessible worldwide with SI-PASS/qualified cert; anonymous bidding. (Tax sales via FURS separately.)
- **HR** Croatia — 🟢 PRIMARY-OFFICIAL — **FINA e-Dražba** ([edrazba.fina.hr](https://edrazba.fina.hr), state financial agency; statutory monopoly), ≥60-day notice. Gate: FINA digital certificate on an e-card/token.
- **EE** Estonia — 🟡 REGULATED-ENTITY-OFFICIAL — **oksjonikeskus.ee** (Chamber of Bailiffs) + statutory notice in **Ametlikud Teadaanded** (ametlikudteadaanded.ee, ≥10 days); timed bidding, pre-registration.
- **LT** Lithuania — 🟢 PRIMARY-OFFICIAL — **evarzytynes.lt** (statutory single e-auction portal since 2013; redirects to the consolidated eaukcionai.lt). Login needs LT-compatible e-ID — a non-resident hurdle.
- **LV** Latvia — 🟢 PRIMARY-OFFICIAL — **izsoles.ta.gov.lv** (Court Administration, .gov.lv) + the **Latvijas Vēstnesis** gazette. Register via latvija.lv (eID/eIDAS) or via the bailiff.
- **RO** Romania — 🟡 REGULATED-ENTITY-OFFICIAL — **licitatii.executori.ro** (UNEJ, National Union of Court Bailiffs), statutory publicity registry; 10% deposit; ag-land restricted (separate).
- **BG** Bulgaria — 🟡 REGULATED-ENTITY-OFFICIAL — **sales.bcpea.org** (Chamber of Private Enforcement Agents / ЧСИ); STATE bailiffs + tax seizures are a *separate* channel (court / Държавен вестник). Foreign land acquisition restricted.
- **RS** Serbia — 🟢 PRIMARY-OFFICIAL — **e-Aukcija** ([eaukcija.sud.rs](https://eaukcija.sud.rs), MoJ/courts): since 1 Sep 2020 all enforcement bidding is exclusively here. Gate: RS qualified e-signature.
- **ME** Montenegro — 🔴 NONE-CONFIRMED / FRAGMENTED — per-public-bailiff (*javni izvršitelj*); the Chamber site is a directory, licitacije.me is a commercial aggregator. Verify with the appointed bailiff / Osnovni sud.
- **BA** Bosnia & Herzegovina — 🔴 NONE-CONFIRMED / FRAGMENTED — entity-level courts (FBiH / RS / Brčko), no state-wide portal (ejn.gov.ba is *procurement*, not auctions; javneprodaje.com is an aggregator). Verify with the competent entity court.
- **MK** North Macedonia — 🔴 NONE-CONFIRMED / FRAGMENTED — per-bailiff (*извршител*), 3-round auctions; no central portal. Verify with the bailiff / Chamber.
- **AL** Albania — 🔴 NONE-CONFIRMED / FRAGMENTED — private bailiffs (*përmbarues*); chamber register + newspaper notices; SIAIP is an internal case system, not a public listing. Verify with the bailiff.
- **GE** Georgia — 🟢 PRIMARY-OFFICIAL — **eauction.ge** (National Bureau of Enforcement, NBE; since 2011). Foreigners cannot own agricultural land (separate axis); non-ag is open — verify registration.
- **MD** Moldova — 🟡 REGULATED-ENTITY-OFFICIAL — **unej.md** (National Union of Judicial Executors), de-facto central; immovable lots at /licitatii. Foreigners barred from ag/forest land.
- **AM** Armenia — 🟡 PRIMARY-OFFICIAL (authority) — the **Compulsory Enforcement Service** ([cesa.am](https://cesa.am), MoJ) runs forced e-auctions; the exact public listing URL is unconfirmed — **do not use armeps.am** (that is the procurement portal). Note a post-sale eviction-claim window of up to 1 year (buyer risk).
- **AZ** Azerbaijan — 🟡 PRIMARY-OFFICIAL (state e-auction) — **e-Herrac** ([eherrac.gov.az](https://eherrac.gov.az), ASAN Login), the central state/MoJ-linked platform; confirm judicial-foreclosure coverage. Foreigners can own buildings, not land.
- **KZ** Kazakhstan — 🟡 PRIMARY-OFFICIAL — the state enforcement-proceedings e-trading platform ([aisoip.adilet.gov.kz](https://aisoip.adilet.gov.kz), via egov.kz / Republican Chamber of Private Bailiffs), ≥10-day notice, 5% fee. Apartments yes; land restricted.
- **UZ** Uzbekistan — 🟡 PRIMARY-OFFICIAL — the State Assets Agency e-auction (**E-IJRO AUKSION**; the court-seized-property path is on e-auksion.uz, with davaktiv.uz the broader State-Assets platform — confirm the enforcement route). Foreigner land ownership heavily restricted.

### Confidence
HIGH for CZ/SK/PL/HU/SI/HR/EE/LT/LV/RO/BG/RS/GE/MD; MEDIUM for AM/AZ/KZ/UZ (official authority confirmed, exact listing URL or judicial-scope flagged to verify); 🔴 NONE-CONFIRMED for ME/BA/MK/AL (reported honestly, no portal invented).

---

## MENA + GCC + Israel + Türkiye

- **TR** Türkiye — 🟢 PRIMARY-OFFICIAL — **UYAP E-Satış** ([esatis.uyap.gov.tr](https://esatis.uyap.gov.tr)): court enforcement/bankruptcy property, 7-day e-bidding, 10% deposit. Gate: e-Devlet account (verify foreigner path); military-zone/reciprocity ownership limits.
- **AE** UAE — 🟢 PRIMARY-OFFICIAL — Dubai: **eMart by DLD** + Dubai Courts (operated via emiratesauction.com/PropertyDXB); Abu Dhabi: **ADJD Auctions** ([adjd.gov.ae](https://www.adjd.gov.ae), ADJD app). Foreign buyers bid in freehold zones.
- **IL** Israel — 🟠 FRAGMENTED — foreclosure via the **Enforcement & Collection Authority** (Hotza'a LaPoal, gov.il — process owner, not a listing site); a court-appointed receiver (*kones nechasim*) sells via newspaper tenders + commercial boards. No nationality bar on bidding.
- **QA** Qatar — 🟡 PRIMARY-OFFICIAL (app-only) — the **Court Mzadat** app (Judicial Executions & Auctions Admin, Supreme Judiciary Council); no web portal. Foreign freehold limited to designated zones — verify per session.
- **SA** Saudi Arabia — 🟡 PRIMARY-OFFICIAL — **Najiz** ([najiz.sa](https://najiz.sa), MoJ) → Enforcement package → "View auction announcements" (national SSO). (The name is Najiz, not "Enfaz".) Non-GCC ownership limits gate eligibility.
- **JO** Jordan — 🟢 PRIMARY-OFFICIAL — **MoJ e-Auctions** ([auctions.moj.gov.jo](https://auctions.moj.gov.jo)): movable + immovable execution sales, [10% deposit](https://auctions.moj.gov.jo/UsagePolicy.aspx), 15-day re-offer, judge confirms. Foreign ownership needs Council-of-Ministers approval.
- **OM** Oman — 🔴 NONE-CONFIRMED — e-justice exists (Omanuna) but no central public real-estate auction registry confirmed. Verify with the courts.
- **BH** Bahrain — 🔴 NONE-CONFIRMED — MoJ e-services cover execution files + auctioneer licensing, but no confirmed central property-auction registry. Verify with the courts/MoJ.
- **KW** Kuwait — 🔴 NONE-CONFIRMED — no confirmed central judicial property-auction listing portal. Verify with the MoJ/courts.
- **LB** Lebanon — 🔴 NONE-CONFIRMED — judicial execution via the courts' Execution Department (*دائرة التنفيذ*); no confirmed central online portal. Verify with the Execution Dept.

### Confidence
HIGH for TR/AE/JO; MEDIUM for QA (app-only), SA (portal confirmed, foreigner eligibility per case), IL; 🔴 NONE-CONFIRMED for OM/BH/KW/LB.

---

## APAC + South Asia

- **JP** Japan — 🟢 PRIMARY-OFFICIAL — **BIT** ([bit.courts.go.jp](https://www.bit.courts.go.jp/), Supreme Court; migrated from the retired `bit.sikkou.go.jp`) for court auctions (*keibai*); `981.jp` is a private mirror. Foreigners may bid (no nationality bar); residency/qualification cert + often a concierge.
- **KR** South Korea — 🟢 PRIMARY-OFFICIAL — **courtauction.go.kr** (Court Auction Information System); `.co.kr` is a private aggregator. Notably, **court auctions are exempt from Korea's 2025 foreign-buyer Land-Transaction-Permit regime** (re-confirm against statute).
- **TW** Taiwan — 🟡 PRIMARY-OFFICIAL (split) — Judicial Yuan court-auction announcements ([aomp109.judicial.gov.tw](https://aomp109.judicial.gov.tw/judbp/wkw/WHD1A02.htm), 法拍屋) + MOJ Administrative Enforcement Agency (tax/admin). Foreign land ownership is **reciprocity-gated** (Land Act art. 18) — verify eligibility first.
- **HK** Hong Kong — 🟠 AGGREGATOR-ONLY — foreclosure needs a court order but **no requirement to sell by auction**; distressed stock moves via agents / commercial auctioneers (Memfus Wong). No official auction registry.
- **MO** Macau — 🟢 PRIMARY-OFFICIAL — **Tribunais da RAEM — Venda Judicial** ([court.gov.mo](https://www.court.gov.mo)), often sealed-bid (*propostas em carta fechada*). (Tax-seized via DSF separately.)
- **SG** Singapore — 🟠 AGGREGATOR-ONLY — mortgagee sales via licensed houses (Knight Frank, Edmund Tie, JLL); no central government registry. Non-landed open to foreigners; landed needs LDAU approval.
- **TH** Thailand — 🟢 PRIMARY-OFFICIAL — **Legal Execution Department** ([led.go.th](https://www.led.go.th), Min. of Justice): condos/land/commercial. Ownership law gates the buyer — foreigners cannot own land freehold; condos within the 49% foreign quota only.
- **MY** Malaysia — 🟡 PRIMARY-OFFICIAL (court) + bank-channel — **e-Lelong, High Court** ([elelong.kehakiman.gov.my](https://elelong.kehakiman.gov.my)); bank "lelong" foreclosures run via panel auctioneers (aggregators, SECONDARY). State minimum-price + consent rules; some lots citizen/Bumiputera-only.
- **ID** Indonesia — 🟢 PRIMARY-OFFICIAL — **Lelang Indonesia** ([lelang.go.id](https://lelang.go.id), DJKN / Min. of Finance), via KPKNL offices: all state/judicial/foreclosure (*eksekusi hak tanggungan*) auctions. Foreigners cannot hold *Hak Milik* freehold (Hak Pakai/strata only); registration needs KTP+NPWP.
- **VN** Vietnam — 🟢 PRIMARY-OFFICIAL — **MoJ Asset Auction Portal** ([dgts.moj.gov.vn](https://dgts.moj.gov.vn)): judgment-enforcement forced sales + land-use-right auctions. Foreign individuals can't own land-use rights; dwelling ownership is quota-limited.
- **PH** Philippines — 🟠 FRAGMENTED + 🟡 regulated — sheriff/extrajudicial sales (Act 3135) are per-court/LGU (no national portal); the state housing fund runs **Pag-IBIG Online Public Auction** ([pagibigfundservices.com](https://www.pagibigfundservices.com/OnlinePublicAuction)). Foreigners constitutionally barred from land; condos to 40%.
- **CN** China — 🟡 court-supervised on a commercial platform — judicial auctions (*司法拍卖*) run **under court supervision on sf.taobao.com** (+ JD), per the SPC's 2016 rules — describe it as court-supervised, not a government site. A foreigner must appoint a **Chinese bidding agent** and disclose identity to the court.
- **KH** Cambodia — 🔴 NONE-CONFIRMED — court-ordered sale by auction/tender exists; no official central portal confirmed. Foreigners can't own land; condos (above ground floor) to 70%.
- **VU** Vanuatu — 🔴 NONE-CONFIRMED — **there is no freehold to auction**: the 1980 Constitution (Ch. 12, Arts 73–75) abolished freehold and **vested all land permanently in indigenous custom owners**, so a foreigner holds land only via a **registered lease (≤75-yr ceiling) under the Land Leases Act [Cap 163]** — any distress is a *lease-charge enforcement / lease forfeiture*, not a conventional land auction (cf. trap #6 / Greenland). **No central distressed-lease registry confirmable from the playbook** (2026-06-13); the discovery + control point is the **Department of Lands, Survey & Registry** (lessor's consent to transfer), so verify lease status there. Final court: **Court of Appeal of Vanuatu** (no Privy Council). The binding diligence item is **lease years-remaining**, not portal access.
- **IN** India — 🟢 PRIMARY-OFFICIAL — government-backed central portals: **IBAPI** ([ibapi.in](https://ibapi.in) — an initiative of the **Indian Banks' Association (IBA)** under the policy of the **Department of Financial Services, Ministry of Finance**; the portal does not name its operating agency, so the "via MSTC" attribution is data not publicly available — verify with IBA / DFS. 2026-09-18 verified), **eBKray** (ebkray.in), **BAANKNET** (baanknet.com, IBBI/PSB Alliance) — SARFAESI bank-foreclosure + liquidation/DRT sales. `bankeauctions.com` is **private**. NRIs/OCIs may bid; non-resident foreigners restricted under FEMA.
- **PK** Pakistan — 🔴 NONE-CONFIRMED — land records are **provincial (no national cadastre)** and title is a **presumptive Record of Rights** (*jamabandi*/*fard* mutation + a registered deed), **NOT a Torrens guaranteed title** — so any court-ordered enforcement sale is **fragmented per province/court** and **no central distressed-sale registry was confirmable from the playbook** (2026-06-13); verify with the relevant Board of Revenue + the competent court. Final court: **Supreme Court of Pakistan** (constitutional jurisdiction moved to the new Federal Constitutional Court by the 27th Amendment, signed 13 Nov 2025). Foreigner gate is multi-layered: the realistic diaspora route is **NRP/POC via SBP Roshan Apna Ghar**, while a **non-origin foreign national needs prior Ministry-of-Interior approval** (1980 Order under s.3 Foreigners Act 1946) + security clearance for cantonment/border zones, and FX moves under **SBP exchange controls** — winning a bid is worthless without clearing the acquisition NOC first.
- **LK** Sri Lanka — 🟠 FRAGMENTED — parate execution (Recovery of Loans Act 4/1990) + judicial sale, mandatorily published in the **Government Gazette** + press (3 languages), sold by licensed auctioneers; no e-portal. (Parate reinstated Apr 2025.) Foreigners restricted on freehold.
- **MV** Maldives — 🔴 NONE-CONFIRMED — foreclosure via the Civil Court (Property Act); no central listing portal. Foreign freehold largely barred (lease/SEZ only).

### Confidence
HIGH for JP/KR/MO/TH/ID/VN/IN; MEDIUM for TW (reciprocity gate), MY (court vs bank channels), PH (split), CN (platform nuance), LK; 🔴 NONE-CONFIRMED for KH/MV + VU (no freehold to auction — leasehold-only over custom land) + PK (provincial, no national cadastre, presumptive non-Torrens title; the Interior-NOC acquisition gate binds the non-origin foreigner). Across APAC + South Asia the binding constraint is usually the *land-ownership / tenure* axis, not portal access.

---

## LATAM + Caribbean

- **MX** Mexico — 🟡 PRIMARY-OFFICIAL (split) — **no single national portal**: state-judiciary *remates* portals (e.g. PJENL [pjenl.gob.mx/RematesJudiciales](https://www.pjenl.gob.mx)) + the federal judiciary's electronic remates + SAT tax-seized assets. ("REM@JU" is **Peru's** portal, not Mexico's.) Verify per court.
- **BR** Brazil — 🟠 FRAGMENTED — *leilão judicial* editais per tribunal (each state TJ + Federal TRF); CNJ sets the rules (Res. 236/2016) but there is no single national registry; run by credentialed *leiloeiros*.
- **AR** Argentina — 🟡 PRIMARY-OFFICIAL (split) — national: **CSJN Oficina de Subastas** ([subastaselectronicasjudiciales.csjn.gov.ar](https://www.csjn.gov.ar/novedades/detalle/11787), mandatory for CABA federal courts since 1 Oct 2025) + provincial portals (PBA scba.gov.ar, Córdoba, etc.). No all-Argentina registry.
- **CR** Costa Rica — 🟡 PRIMARY-OFFICIAL (gazette) — court *remates* in the **Boletín Judicial** (poder-judicial.go.cr), ≥8 days before; 50%-of-base deposit. A sequential gazette, not a search UI.
- **PA** Panama — 🟠 FRAGMENTED — Órgano Judicial ([organojudicial.gob.pa](https://www.organojudicial.gob.pa)) per-court/circuit edictos; state banks also publish their lots. No central registry.
- **CO** Colombia — 🟡 PRIMARY-OFFICIAL (notices) — Rama Judicial *avisos de remate* ([ramajudicial.gov.co](https://www.ramajudicial.gov.co/web/unidad-de-asistencia-legal/avisos-de-remate)) + per-court pages + wide-circulation press ([Law 1564/2012 art. 450](http://www.secretariasenado.gov.co/senado/basedoc/ley_1564_2012_pr015.html)); virtual auctions expanding in 2026.
- **UY** Uruguay — 🟡 PRIMARY-OFFICIAL (gazette) — judicial edictos in the **Diario Oficial**, aggregated by **IMPO** ([impo.com.uy/remates](https://www.impo.com.uy/remates)); conducted by licensed *martilleros*.
- **CL** Chile — 🟢 PRIMARY-OFFICIAL — **Oficina Judicial Virtual** ([oficinajudicialvirtual.pjud.cl](https://oficinajudicialvirtual.pjud.cl), "Remates") + TGR/DICREP (remates.tgr.cl); ≥3× Diario Oficial. Practically gated by **Clave Única** (Chilean state ID) — verify foreign path.
- **PE** Peru — 🟢 PRIMARY-OFFICIAL — **REM@JU** ([remaju.pj.gob.pe](https://remaju.pj.gob.pe)), the national electronic judicial-auction platform; 10% guarantee at Banco de la Nación. Account shown via DNI — verify foreigner path.
- **EC** Ecuador — 🟢 PRIMARY-OFFICIAL — **Remates Judiciales en Línea** ([remates.funcionjudicial.gob.ec](https://remates.funcionjudicial.gob.ec), Consejo de la Judicatura): daily nationwide. Official text admits **"any natural or legal person, national or foreign"** with civic rights — the cleanest foreigner-inclusive case in the corpus. (SATJE is case-tracking, separate.)
- **PY** Paraguay — 🟠 FRAGMENTED — no national portal; edictos in a national daily + each court's auction-hall board; the Poder Judicial sets rules; auctions run by the *Asociación de Rematadores* (asorematespy.com, regulated-entity channel).
- **BS** Bahamas — 🟠 FRAGMENTED — per-bank power-of-sale lists (Scotiabank/RBC/BOB/CIBC/BDB) + the Dept of Inland Revenue tax-sale list (s.25A Real Property Act) + Supreme Court sales in the press. Int'l Persons Landholding Act permit for many purchases.
- **DO** Dominican Republic — 🟠 FRAGMENTED — court-supervised *embargo inmobiliario*; auction *edicto* in a national-circulation newspaper 20 days ahead; no central online registry (the Poder Judicial site has no subastas portal). Near-equal foreign property rights.
- **JM** Jamaica — 🟠 FRAGMENTED — bank mortgagee power-of-sale lists (Scotiabank, JN Bank) + Supreme Court judicial sales in the **Jamaica Gazette** + press. No foreign-ownership restriction.
- **TT** Trinidad & Tobago — 🟠 FRAGMENTED — English common-law mortgagee **power of sale** + High Court foreclosure; **no central auction registry** — distressed lots surface via bank repo channels + legal notices in the press/Gazette (verify with the attorney). Two structural traps: (a) **dual title** — most land (~75–80%, *est. per Fitzwilliam Stone*) is **Old-Law deeds with NO state title guarantee**, so an attorney must trace the chain of title (the minority is RPA/Torrens, indefeasible); (b) the **Foreign Investment Act licence gate applies to a distressed purchase too** — a foreign buyer of **any Tobago land (any size)** or **Trinidad residential >1 acre** needs a **President's licence** (FIA + the 2007 Tobago Order), with settlement in hard currency through an authorised dealer (FIA s.10); a licence-free buyer below the Trinidad thresholds still files a Third-Schedule notice with the Minister of Finance (s.8(2)). (Any special distressed-acquirer/mortgagee-in-possession licence treatment — verify in the FIA / Regulations at [laws.gov.tt](https://laws.gov.tt/); not confirmed in the playbook.) Final court: **UK Privy Council (JCPC)**, not the CCJ. (Exit risk: a real USD shortage means authorised dealers ration forex — repatriating proceeds can be slow.)
- **BB** Barbados — 🟡 PRIMARY-OFFICIAL (gazette) — court judicial sales advertised by the **Registrar in the Official Gazette** + a newspaper (CAP 372E, sale ≥3 months after first notice); bank repos; BRA land-tax auctions (CAP 78A). Register the transaction with the Central Bank (exchange control).
- **BZ** Belize — 🟠 AGGREGATOR-ONLY — mortgagee auctions consolidated commercially by a single licensed auctioneer ([belizepropertyauctions.com](https://www.belizepropertyauctions.com)) + bank pages + the statutory **DFC** (govt finance corp) foreclosure list + Amandala press. No foreign-ownership restriction.
- **KN** St Kitts & Nevis — 🟡 PRIMARY-OFFICIAL (gazette) — ECSC judicial sales in the **Official Gazette** + press; bank repos. **Alien Land Holding Licence** needed to own.
- **AG** Antigua & Barbuda — 🟡 PRIMARY-OFFICIAL (gazette) — ECSC judicial sales in the **Official Gazette** + press; bank repos. **Non-Citizen Land Holding Licence** needed.
- **LC** Saint Lucia — 🟡 PRIMARY-OFFICIAL (gazette) — ECSC judicial sales advertised 3× in the **Official Gazette** + press; commercial sites (caribbeanforeclosure.com, michalanders.com) re-list (SECONDARY). **Alien Landholding Licence** needed.
- **GD** Grenada — 🟡 PRIMARY-OFFICIAL (gazette) — ECSC judicial sales in the **Official Gazette** + press. **Alien Landholding Licence** needed.
- **AW** Aruba — 🟡 REGULATED-ENTITY-OFFICIAL — bank-instructed **executieveiling** run by a civil-law notary; terms posted ≥30 days ahead on the notary's site; Landscourant gazette; some lots on biedboek.nl (SECONDARY). Check *erfpacht* (long-lease) tenure.
- **CW** Curaçao — 🟡 REGULATED-ENTITY-OFFICIAL — notary-run **executieveiling** (e.g. Fung-A-Loi & Samandar, PALM), ≥30-day notice; Landscourant. No general foreign-ownership restriction.
- **SX** Sint Maarten — 🟡 REGULATED-ENTITY-OFFICIAL — notary-run **executieveiling**, ≥30-day notice; Landscourant; thin market — ask local notaries directly.
- **BQ** Bonaire (BES) — 🟡 REGULATED-ENTITY-OFFICIAL — notary-run **executieveiling** (e.g. Bonaire Notaris), ≥30-day notice; very small market.
- **KY** Cayman Islands — 🟠 FRAGMENTED — mortgagee power of sale (settled Grand Court practice = public auction) + Grand Court foreclosure; bank repos surfaced via the **CIREBA** MLS + press. Notably foreigner-friendly (no ownership restriction, no property tax).
- **BM** Bermuda — 🟠 FRAGMENTED — mortgagee power of sale + Supreme Court enforcement via the **Provost Marshal General**; legal notices in **The Royal Gazette**; bank/agent repos. Foreign buyers severely restricted (licence + high ARV threshold) — the binding gate.
- **TC** Turks & Caicos — 🔴 NONE-CONFIRMED — mortgagee power of sale + Supreme Court foreclosure; legal notices in the **Government Gazette** + press; no dedicated auction registry. Foreigner-friendly ownership.
- **VG** British Virgin Islands — 🔴 NONE-CONFIRMED — power of sale / court foreclosure (order nisi→absolute); legal notices in the **BVI Official Gazette** + press; no auction registry. **Non-Belonger Land Holding Licence** needed.

### Confidence
HIGH for CL/PE/EC + the gazette-official set (CR/CO/UY/BB) + the Dutch-Caribbean notary model (AW/CW/SX/BQ) + the OECS gazette channel (KN/AG/LC/GD); MEDIUM for MX/AR (split), BR/PA/PY (fragmented), BS/DO/JM/KY/BM/TT (fragmented common-law — TT adds a dual Old-Law/RPA title trap + a Foreign-Investment-Act licence gate that applies to a distressed purchase too); 🔴 NONE-CONFIRMED for TC/VG. Foreigner participation positively confirmed only for **EC**; elsewhere verify (and mind the Landholding-Licence / FIA-licence / Central-Bank gates).

---

## Africa + Anglo-non-EU

- **ZA** South Africa — 🟠 FRAGMENTED — **Sales in Execution** by the Sheriff after judgment; the official channel is the **Government Gazette** (per case), with no national portal; commercial aggregators (sasheriff.co.za, auctionwatch.co.za) re-list from the Gazette. Foreigners can buy.
- **NA** Namibia — 🔴 NONE-CONFIRMED — **Roman-Dutch common-law + customary** jurisdiction inherited from South Africa (final court: **Supreme Court of Namibia**), operating the same Deeds-Registries-Act-1937 deeds system as ZA — but **no central distressed-sale registry was confirmable from the playbook** (2026-06-13): treat the ZA-style Sheriff/Government-Gazette path as a structural parallel only, and **verify with the competent court / conveyancer**, never assume a portal. Binding foreigner axes: urban/residential freehold is **open** (no enacted ban; the consolidating Land Bill re-tabled Oct 2025 is a BILL, not law), but **agricultural land needs Ministerial consent + a State preferent right** (ACLRA 6/1995 s.58(1)(a)), and FX **outside the CMA is exchange-controlled** by the Bank of Namibia.
- **BW** Botswana — 🔴 NONE-CONFIRMED — **Roman-Dutch common-law + customary** (final court: **Court of Appeal of Botswana**), freehold + state-land deeds at the Registrar of Deeds — **no central distressed-sale registry confirmable from the playbook** (2026-06-13); verify with the competent court / conveyancer. The binding foreigner constraint is **tenure, not portal access**: non-citizens take **freehold (scarce) or ~50-yr state-land leasehold only**, **tribal land is closed** to foreign freehold, and **agricultural land needs Ministry-of-Agriculture consent** (Land Control Act 1975). Exchange controls were **abolished (9 Feb 1999)** → sale proceeds freely repatriable.
- **MA** Morocco — 🟠 AGGREGATOR-ONLY — court-ordered judicial auctions (20–60% below market, 5–10% deposit) with no confirmed central court portal; practical channels are commercial (enchere.ma, avito.ma). Foreigners can buy non-agricultural property.
- **EG** Egypt — 🔴 NONE-CONFIRMED — judicial forced sale (*بيع جبري*) via the courts, gazetted/newspaper per case; **`auctions.realestate.gov.eg` is a state real-estate MLS, NOT a foreclosure registry** — do not cite it as such. Foreign ownership capped (Law 230/1996).
- **TN** Tunisia — 🔴 NONE-CONFIRMED — judicial execution exists; no confirmed central property-auction portal. Verify with the courts.
- **NG** Nigeria — 🟠 AGGREGATOR-ONLY — mortgagee/court-ordered sales by **licensed auctioneers** (Auctioneers Law; s.19(1) notice is mandatory or the sale voids); advertised per state, no central portal. Foreigners typically hold via leasehold/company.
- **KE** Kenya — 🟠 AGGREGATOR-ONLY — mortgagee sales by **licensed auctioneers** (Auctioneers Act Cap 526; 45-day statutory notice); commercial channels + bank boards. Foreigners can hold leasehold (not agricultural land).
- **MU** Mauritius — 🟠 FRAGMENTED — Supreme Court *vente forcée / vente judiciaire* per case (mixed FR/EN law); the Financial Crimes Commission auctions *confiscated* assets separately (not foreclosure). Foreigners buy via approved schemes (PDS/IRS/smart city).
- **CV** Cape Verde — 🔴 NONE-CONFIRMED — no central judicial property-auction portal confirmed. Verify with the Tribunais.
- **SC** Seychelles — 🔴 NONE-CONFIRMED — judicial sales court-ordered per case; the Judiciary e-service is case scheduling, not listings. Foreign ownership needs government Sanction.
- **GH** Ghana — 🟠 AGGREGATOR-ONLY — mortgagee/court-ordered sales by **licensed auctioneers**; no central portal. Foreigners hold leasehold (max 50 years).
- **RW** Rwanda — 🔴 NONE-CONFIRMED — no central judicial property-auction portal confirmed. Verify with the courts / Rwanda Governance Board.
- **US** United States — 🟠 FRAGMENTED — **no national portal**; sheriff sales + tax-deed/tax-lien sales run county-by-county (3,000+ counties), many via the **RealAuction** vendor (per-county subdomains) or commercial **auction.com / Xome** (SECONDARY). Generally no nationality bar (some states/HOAs restrict). Search per county.
- **CA** Canada — 🟠 FRAGMENTED — **no national portal**; power of sale (ON/NB/NL/PEI) vs judicial sale (BC/AB/SK/MB/QC/NS), province-by-province; most distressed stock on MLS via realtors; Ontario municipal tax sales quasi-aggregated at ontariotaxsales.ca. Generally open to foreigners (mind provincial/federal foreign-buyer rules).
- **AU** Australia — 🟠 AGGREGATOR-ONLY — mortgagee-in-possession lots via ordinary agent/auction channels (domain.com.au, realestate.com.au); Domain publishes auction *results*, not a distressed registry. Foreign buyers need **FIRB** approval.
- **NZ** New Zealand — 🟠 AGGREGATOR-ONLY — mortgagee sales marketed by the mortgagee's chosen agent on Trade Me / Bayleys; **REA** (rea.govt.nz) is regulator *guidance*, not a listing portal. The **Overseas Investment Act** generally bars non-resident foreigners from buying existing homes (AU/SG carve-outs).

### Confidence
HIGH for ZA/US/CA/AU/NZ (FRAGMENTED/AGGREGATOR structure well-documented) + the licensed-auctioneer markets (MA/NG/KE/GH) + MU; 🔴 NONE-CONFIRMED for EG (judicial)/TN/CV/SC/RW + NA/BW (Roman-Dutch Southern Africa — ZA-style Sheriff/Gazette path is a structural parallel, not a playbook-confirmed registry; the binding axis is the tenure/agricultural-consent gate). In Anglo-non-EU markets the lesson is the same: there is no official registry — the named channels are commercial/secondary; cross-check.

---

## Universal mitigations

Applicable across all 126 countries:

1. **Classify the system before trusting any website** — 🟢 official portal / 🟡 regulated-or-gazette / 🟠 fragmented-or-commercial / 🔴 none. It decides whether the listing you found is a primary source or a seller-controlled aggregator.
2. **Go to the official portal/gazette named above, not the first English-language listing site** — the slick site is usually the commercial aggregator; the authoritative one is often a plain government/court page (or a print gazette).
3. **Clear the foreigner gate on all three axes before bidding** — (a) can you get the e-ID/certificate to register; (b) are you legally eligible to bid; (c) can you, as a foreigner, actually *own* this land (the binding constraint in APAC/MENA and the OECS/BVI/BM)? Resolve (c) first.
4. **Confirm which kind of distress you're searching** — court foreclosure vs tax seizure vs state-asset sale are usually different channels; don't search the tax portal for a judicial foreclosure (or cite a state-MLS as a foreclosure registry).
5. **In 🔴/🟠 markets, retain in-country counsel to watch the competent court + official gazette** — there is no portal to subscribe to; the gazette + the major banks' repo pages + (Dutch islands) the executing notary are the real discovery channels.
6. **Treat the opening price as the start of diligence, not the deal** — distressed lots sell as-is (often no vacant possession, unpaid charges/occupants run with the property). Pair this section with `--type=auction` (mechanics) + a title/occupancy/arrears check before committing.
7. **Re-verify the portal URL + the foreigner rules within 30 days of decision-day** — auction portals and foreign-ownership/permit regimes change (KR's 2025 permit-regime carve-out, AR's 2025 CSJN portal, LK parate reinstated Apr 2025). URL-liveness ≠ data-still-current.

## Status

**Confidence**: HIGH for ~45 countries with a confirmed PRIMARY-OFFICIAL or REGULATED-ENTITY-OFFICIAL portal (continental Europe, much of APAC, CL/PE/EC, AE/TR/JO, IN); MEDIUM for ~45 with split/gazette/fragmented official channels or app-only portals (DK/MC/CO/UY/CR/BB/AR/MX, the GCC enforcement portals, the Caucasus/Central-Asia state platforms, the common-law Caribbean gazette channel); LOW / NONE-CONFIRMED for ~31 where no public registry was confirmable (LU/SM, the 6 Crown Dependencies/territories, OM/BH/KW/LB, EG-judicial/TN/CV/SC/RW, MV/KH, ME/BA/MK/AL, TC/VG) — these are honestly downgraded, never slot-filled with an invented portal.

**Last verified**: 2026-06-03 (JP and TW court-auction host labels corrected 2026-09-18 per bit.courts.go.jp + aomp109.judicial.gov.tw).

**Pairs strongly with**:
- `--type=auction` — the buyer-journey template for *how* to buy at auction (deposit, vacant possession, caveat emptor); this section is *where* to find them
- `--scams` — distressed-sale and "below-market auction" fraud vectors (cross-reference the pre-deed taxonomy)
- `--finance` — auction purchases are usually cash / pre-approved with no finance-subject clause; LTV + timing matter
- `--notary` / `--remote` — deed execution + remote bidding via PoA (NL/BE notary auctions; MC mandatory avocat; FR mandatory avocat)
- `--permits` — the foreign land-ownership / Landholding-Licence axis that can bar a winning bidder from owning
- `--title-monitoring` — the registry-system classification that determines post-purchase title security

**Methodology note**: researched via 7 parallel region agents + a Crown-Dependencies pass, then an independent 4-agent liveness+correctness audit that GET-verified the official portal URLs and caught several fabrication-adjacent errors before shipping (IT PVP not "TPC"; MX "REM@JU" is Peru's, not Mexico's; FR encheres-publiques is commercial not official; NL veilingnotaris official vs veilingbiljet commercial; HR edrazba.fina.hr; UZ enforcement path on e-auksion.uz; EG realestate.gov.eg is an MLS not a foreclosure registry; SA Najiz not "Enfaz"; KZ aisoip.adilet.gov.kz; QA Mzadat app-only; IN ibapi/baanknet official vs bankeauctions private). Anti-hallucination posture: where no official central registry could be confirmed, the country is marked 🔴 NONE-CONFIRMED with a "verify with the competent court / official gazette" instruction rather than a guessed URL; commercial aggregators are always tagged SECONDARY and never presented as official; the foreigner question is split into mechanism-access / legal-eligibility / land-ownership axes so a "yes, you can bid" is never confused with "yes, you can own."
