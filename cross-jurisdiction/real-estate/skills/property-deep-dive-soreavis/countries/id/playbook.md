# Indonesia 🇮🇩 — Property Due-Diligence Playbook

ISO2: `id`. Status: ✅ Fully populated (researched 2026-04 / 2026-05).

> **🇮🇩 LEAD WARNING — read before any other section.** Indonesia is a **foreign-restricted** market. **Foreigners cannot own freehold (Hak Milik) land** under Undang-Undang Pokok Agraria (UUPA) No. 5/1960 §21 and §26(2). The legal pathways for foreigners are: **Hak Pakai** (Right to Use; PP 18/2021 Pasal 69(1) requires a "dokumen keimigrasian" — visa, passport or stay permit per the Penjelasan), **strata-title condo (SHMRS)** in rumah susun on Hak Pakai or HGB land (PP 18/2021 Pasal 71(1)(b)), **Hak Sewa** (lease), or **PT PMA** (foreign-invested Indonesian company holding HGB). **Nominee structures** (Hak Milik bought via an Indonesian friend/spouse with side-letter giving the foreigner economic control) are illegal under UUPA §26(2) and are **void by operation of law** — the land falls to the State (UUPA §26(2)); there is no "Bali Provincial Court", and circulating 2023–2025 nominee case counts are unverified (check the Direktori Putusan manually); **Bali Perda 4/2026 (ditetapkan + diundangkan 24 Feb 2026) Pasal 14 bars anyone from acting as intermediary or facilitator, or providing the means, for a foreign national to control land through a nominee**, with **administrative** sanctions only (Pasal 20(2): warning, suspension, site closure, licence revocation, demolition, administrative fine; Pasal 20(5) leaves criminal liability to other statutes) — the Perda itself creates no prison term. The 5-year imprisonment + IDR 1 billion figure often quoted with it is UU 41/2009 Pasal 72(1), a penalty for converting designated LP2B farmland, which the Perda cites only as legal basis (2026-09-24 verified against the signed Perda on JDIH Bali). Six- to seven-figure decisions in Indonesia demand an Indonesian-licensed notary (PPAT) and a real-estate lawyer fluent in PP 18/2021 — non-negotiable. Skip the lawyer-fee line and you can lose the entire principal to nominee voidance, undisclosed adat (customary) claims, or pre-construction developer default.

## Country profile

- **Postcode (kode pos)**: 5 digits.
  - Jakarta metropolitan (DKI Jakarta): `10xxx`–`14xxx` (e.g., `10110` Gambir, `12190` Senayan, `14430` Pluit)
  - Bali (Badung/Denpasar/Gianyar/Tabanan): `80xxx` (e.g., `80361` Canggu/Kuta Utara, `80571` Ubud, `80228` Sanur, `80361` Seminyak/Kerobokan)
  - Bandung: `40xxx`; Surabaya: `60xxx`; Yogyakarta: `55xxx`; Medan: `20xxx`; Makassar: `90xxx`
  - Source: Pos Indonesia `https://www.posindonesia.co.id/`
- **Admin levels**: 38 provinsi → 514 kabupaten/kota (regencies + cities) → 7,277 kecamatan (districts) → 83,820+ desa/kelurahan (villages); customary banjar (Bali) and adat units operate inside or alongside village governance.
  - Source: Kemendagri (Ministry of Home Affairs) `https://www.kemendagri.go.id/` and BPS `https://www.bps.go.id/` (figures shift with administrative reorganisations; verify current count).
- **Currency**: IDR (rupiah, Rp). 1 USD ≈ 15,500–16,500 IDR; 1 EUR ≈ 16,800–17,800 IDR (Apr 2026 Bank Indonesia reference; FX volatile, verify at `https://www.bi.go.id/`).
- **Languages**: Bahasa Indonesia (official). English usable in Bali expat-property sector and Jakarta CBD. **All registered title documents (sertifikat) and notarial deeds (Akta Jual Beli, AJB) are in Bahasa Indonesia** — sworn translation (penerjemah tersumpah) required for foreign buyers; PPAT must read and explain the deed in person.
- **Cadastre / land registry**: **BPN — Badan Pertanahan Nasional**, operating under **Kementerian ATR/BPN** (Ministry of Agrarian Affairs & Spatial Planning). Public portal: `https://www.atrbpn.go.id/`
  - **BHUMI ATR/BPN** — public parcel / NIB map lookup: `https://bhumi.atrbpn.go.id/` (returns right type, area and parcel geometry; **not** the owner's name). "Sentuh Tanahku" no longer has a verifiable web page of its own — verify its current form with ATR/BPN (2026 data, source bhumi.atrbpn.go.id; 2026-09-18 verified)
  - BHUMI ATR/BPN public spatial viewer: `https://bhumi.atrbpn.go.id/` (parcel polygons + zoning where digitised)
  - Title verification (pengecekan sertifikat) must be requested at the kantor pertanahan (BPN office) of the kabupaten/kota where the parcel sits. PPAT can do this on behalf of the buyer — standard pre-AJB step.
- **Title types** (CRITICAL — only some are foreigner-eligible):

| Code | Indonesian | Type | Foreign use | Notes |
|---|---|---|---|---|
| **Hak Milik (HM)** | Hak Milik | Freehold (perpetual) | ❌ NEVER | UUPA §21 — reserved for Indonesian citizens; nominee transfer void by operation of law, land falls to the State (UUPA §26(2)) |
| **Hak Guna Bangunan (HGB)** | Hak Guna Bangunan | Right to Build (30 yr + 20 ext + 30 renew = 80) | ❌ direct / ✅ via PT PMA | UUPA §36 — only Indonesian citizens or Indonesian-incorporated entities (PT including PT PMA) |
| **Hak Guna Usaha (HGU)** | Hak Guna Usaha | Right to Cultivate (35 yr + ext) | ❌ direct / ✅ via PT PMA agribusiness | Plantation / agribusiness only |
| **Hak Pakai (HP)** | Hak Pakai | Right to Use (on state / HPL land 30 yr + 20 ext + 30 renew = up to 80 — PP 18/2021 Pasal 52(1); over Hak Milik max 30 yr, renewable by PPAT deed — Pasal 52(3)) | ✅ direct (holder of a dokumen keimigrasian — PP 18/2021 Pasal 69(1)) | The primary direct-ownership path for individual foreigners |
| **SHMRS** | Sertifikat Hak Milik atas Satuan Rumah Susun | Strata-title condo certificate | ✅ direct (dokumen keimigrasian — rumah susun on Hak Pakai or HGB land, PP 18/2021 Pasal 71(1)(b), in the zones listed in Pasal 71(2)) | Foreigners can own condos titled this way |
| **Hak Sewa** | Hak Sewa | Lease (typically 25–30 yr, contractual renewals) | ✅ direct | Contractual; not registered as a real right at BPN unless converted to leasehold deed |
| **Tanah Adat / Tanah Ulayat** | — | Customary / unregistered | ❌ NEVER | No sertifikat; cannot be transferred to non-village outsiders |
| **Tanah Ayahan Desa** (Bali specific) | — | Bali village land | ❌ NEVER | Communal village allotment; not transferable to foreigners under any structure |
| **Girik / Letter C / Petok D** | — | Pre-1960 informal proof of possession | ❌ never as final title | Must be upgraded to sertifikat at BPN before any foreign-relevant transaction |

- **Major reforms / regulatory landscape**:
  - **UUPA No. 5/1960** — foundational Basic Agrarian Law; §21 (Hak Milik for citizens only), §26(2) (nominee voidance), §36 (HGB), §41 (Hak Pakai). Source: `https://peraturan.bpk.go.id/Details/51078/uu-no-5-tahun-1960`
  - **PP 18/2021** (Peraturan Pemerintah 18/2021) — overhauled foreign Hak Pakai: 30 + 20 + 30 = up to 80 years on state / HPL land (Pasal 52(1)), max 30 yr renewable by deed over Hak Milik (Pasal 52(3)); condo SHMRS access; price floor + zoning rules per province. Source: `https://peraturan.bpk.go.id/Details/161834/pp-no-18-tahun-2021`
  - **PP 34/2017** + **Permenkeu 34/2017** — final-tax PPh 2.5 % on land/building disposal by sellers. Revenue Code base: UU PPh 36/2008 §4(2)(d).
  - **UU HKPD No. 1/2022** (Hubungan Keuangan Pusat–Daerah) — restructured local taxes including PBB-P2 (Pajak Bumi & Bangunan) and BPHTB (Bea Perolehan Hak atas Tanah dan Bangunan). Effective phase-in 2024–2025; final implementation ceiling rates apply 1 January 2024 onward. Source: `https://peraturan.bpk.go.id/Details/195696/uu-no-1-tahun-2022`
  - **Permenkumham 22/2023 — Second Home Visa (Visa Rumah Kedua)** — 5–10-year residence for foreigners depositing ≥ IDR 2 billion (~USD 130k) in an Indonesian state bank; a property route exists per secondary sources, but its qualifying value is contested (IDR 2B-equivalent vs IDR 5B vs ~USD 1M across 2026 secondary guides) — data not publicly available in primary text read; verify at Imigrasi. Source: `https://www.imigrasi.go.id/`
  - **Bali nominee voidance precedents** — Pengadilan Negeri Denpasar and Pengadilan Negeri Gianyar — asserted repeat nominee voidings since 2023 are unverified (the Direktori Putusan returns HTTP 403 to automated retrieval; check manually). By statute (UUPA §26(2)) such transfers are "batal karena hukum", the land falls to the State, and payments already received by the owner cannot be reclaimed. **Bali Perda No. 4/2026** ("Control of Productive Land Conversion and Prohibition of Nominee Land Ownership Transfer"), signed by Governor Wayan Koster and promulgated on **24 February 2026**, bars any person from being a "perantara, fasilitator, atau menyediakan sarana" through which a foreign national controls land by nominee (Pasal 14), and bars conversion of designated productive land (Pasal 13(2)). Its sanctions are **administrative** (Pasal 20(2): written warning, suspension, site closure, licence revocation or annulment, demolition, restoration, incentive withdrawal, administrative fine); Pasal 20(5) says only that criminal sanctions may apply under other legislation. It does **not** itself criminalise nominee arrangements. The **5 years imprisonment + IDR 1 billion fine** figure is UU 41/2009 Pasal 72(1), for an individual converting designated LP2B land, cited in the Perda's Mengingat only (2026-09-24 verified, source: signed Perda 4/2026 on JDIH Provinsi Bali `https://jdih.baliprov.go.id/` + UU 41/2009 on `https://peraturan.bpk.go.id/`). Verify case law via `https://putusan3.mahkamahagung.go.id/`
  - **Proposed reforms NOT enacted as of May 2026**: extension of Hak Pakai term beyond PP 18/2021 (under discussion); a "Bali special-zone" foreign-ownership pilot has been floated by provincial government but not legislated. Verify via `https://peraturan.bpk.go.id/`.

---

## 🇮🇩 LEAD SECTION: Foreign buyer eligibility

### Bottom line

Foreigners **cannot own freehold (Hak Milik) land in Indonesia**. The Basic Agrarian Law (UUPA) No. 5/1960 §21 reserves Hak Milik to Indonesian citizens; §26(2) voids any transfer (direct or indirect, including nominee arrangements) that has the effect of transferring Hak Milik to a foreigner. For residential property, the practical paths are:

1. **Hak Pakai (HP) on land or house** — direct foreign ownership, requires a dokumen keimigrasian (visa, passport or stay permit per PP 18/2021 Penjelasan Pasal 69(1)); 30 + 20 + 30 = up to 80 years on state / HPL land (Pasal 52(1)), max 30 yr renewable by PPAT deed over Hak Milik (Pasal 52(3))
2. **SHMRS strata-title condominium** — direct foreign ownership with a dokumen keimigrasian, in rumah susun on Hak Pakai or HGB land located in KEK / free-trade and free-port zones / kawasan industri / kawasan ekonomi lainnya (PP 18/2021 Pasal 71)
3. **Hak Sewa (lease)** — typically 25–30 years; renewable contractually but contractual renewals are weaker than registered real rights
4. **PT PMA (foreign-invested Indonesian limited company)** — holds HGB on land; useful for villa-with-land or commercial; minimum capital and reporting obligations apply
5. **Marriage to an Indonesian citizen** — Indonesian spouse may hold Hak Milik in their sole name only with a valid prenuptial agreement (perjanjian pisah harta) signed before marriage; without it, post-Constitutional-Court ruling 69/PUU-XIII/2015 spouses can sign during marriage but Hak Milik cannot be acquired from a non-spouse during a foreign-spouse marriage absent the agreement. Foreign spouse cannot acquire Hak Milik via the marriage.

### Path 1: Hak Pakai (recommended direct path for individual foreigners)

- **Legal basis**: UUPA §41–§43, PP 18/2021 §49–§52 (Hak Pakai) + §69–§73 (foreigner housing). Source: `https://peraturan.bpk.go.id/Details/161834/pp-no-18-tahun-2021`
- **Eligibility prerequisite**: PP 18/2021 Pasal 69(1) requires a **dokumen keimigrasian**, which the Penjelasan defines as "visa, paspor, atau izin tinggal". KITAS/KITAP is not a precondition in the PP text itself; Permen ATR/BPN 18/2021 implementing conditions were not read in primary, so confirm which document BPN accepts at the Kantor Pertanahan (Imigrasi `https://www.imigrasi.go.id/`). The Second Home Visa (Permenkumham 22/2023) also qualifies.
- **Term structure (PP 18/2021 §52(1) — Hak Pakai on state / HPL land; over Hak Milik max 30 yr renewable by PPAT deed, §52(3))**: 30 years initial + 20 years extension + 30 years renewal = **maximum 80 years** of effective use. Each step requires application + fee at BPN.
- **What it covers**: residential land (with house) AND standalone landed houses. NOT plantations or large agribusiness — those need HGU via PT PMA.
- **Price floor (PP 18/2021 §72(a) + Permen ATR/BPN 18/2021)**: provinces set a minimum-price floor for foreign Hak Pakai purchases. Indicative floors (verify current Permen by province):

| Province | Minimum landed-house price (IDR) | USD est. (15,500/USD) |
|---|---:|---:|
| **DKI Jakarta** | 5,000,000,000 | ≈ $322,500 |
| **Bali** | 3,000,000,000 | ≈ $193,500 |
| **Banten / Jawa Barat** (Bogor, Bekasi, Tangerang) | 3,000,000,000 | ≈ $193,500 |
| **Jawa Tengah / DI Yogyakarta** | 2,000,000,000 | ≈ $129,000 |
| **Jawa Timur** (Surabaya, Malang) | 2,500,000,000 | ≈ $161,300 |
| Other provinces | 1,000,000,000–1,500,000,000 | ≈ $64,500–$96,800 |

> Floors are minimums to qualify a foreign Hak Pakai purchase; actual market prices in Bali / Jakarta CBD are typically far above. Verify current Permen ATR/BPN schedule before relying on any specific number — `https://www.atrbpn.go.id/produk-hukum/peraturan`

- **Land area cap (PP 18/2021 §72(b) authorises a plot-area limit; the 2,000 m² figure is set by implementing Permen ATR/BPN 18/2021 — not read in primary this session)**: foreign Hak Pakai on landed house typically capped at **2,000 m²** per person (province may set tighter caps). Larger plots require special governor permission.
- **Conversion path**: a Hak Milik (Indonesian-owned) plot is converted to Hak Pakai at BPN at the time of transfer to the foreign buyer; the seller's HM ends, the buyer's HP starts. A new sertifikat is issued.

### Path 2: SHMRS strata-title condominium (cleanest for apartment buyers)

- **Legal basis**: UU Rumah Susun No. 20/2011 + PP 13/2021 (Penyelenggaraan Perumahan dan Kawasan Permukiman) + PP 18/2021. Source: `https://peraturan.bpk.go.id/Details/161834/pp-no-18-tahun-2021`
- Foreigners holding a dokumen keimigrasian (PP 18/2021 Pasal 69(1)) can own a condo unit titled **SHMRS** (Sertifikat Hak Milik atas Satuan Rumah Susun) — PP 18/2021 Pasal 71(1)(b) lets the rumah susun stand on Hak Pakai OR HGB land (over state, HPL or Hak Milik land), within the zones listed in Pasal 71(2). Practical effect: foreigner holds the unit, the building's land is HGB held by the developer/owners' association.
- **Project must be foreign-eligible**: only condos on land zoned and certified for foreign ownership qualify. Verify with the developer and PPAT before paying a deposit. Some buildings have a foreign-purchaser quota set per project.
- **Price floor**: SHMRS condo for foreign buyer subject to Permen ATR/BPN minimum:
  - DKI Jakarta: IDR 3,000,000,000 (~$193,500)
  - Bali, Banten, Jabar: IDR 2,000,000,000 (~$129,000)
  - Other provinces: IDR 1,000,000,000–1,500,000,000 (~$64,500–$96,800)
- **Marketing trap**: many Bali "villa condotel" / "studio in resort" projects are marketed to foreigners but do NOT actually have SHMRS issued — they are pre-sale on HGB held by the developer with no clear path to foreign-eligible strata title. Demand to see (1) the developer's Pertelaan (subdivision plan approved by mayor/regent), (2) IMB/PBG (building permit), (3) the model SHMRS for the project class. Without all three: do NOT pay deposit.

### Path 3: Hak Sewa (long-term lease)

- **Legal basis**: UUPA §44–§45 (Hak Sewa untuk Bangunan), KUH Perdata §1548–§1600 (lease provisions in the Indonesian Civil Code).
- **Term**: usually 25–30 years per lease deed; can be renewed contractually but successor landowners are not bound unless the lease is registered as a real right at BPN (rare for residential).
- **Bali villa reality**: most "buy a Bali villa" foreigner transactions are actually a **leasehold of land** (typically 25 or 30 years, sometimes "extendable" to 40–50 by pre-paid options) with the **building** notarised separately. The "purchase" is really a long lease prepaid in full. Resale value at year 15+ drops sharply.
- **Risk**: contractual extensions are weak. If the underlying landowner sells, dies, or the family disputes inheritance, the foreigner's "extension option" is often unenforceable. Most Bali courts require the renewal to be registered as a real right (notarial deed + BPN registration) to bind successors.
- **Best practice**: register the lease at BPN where possible (notarial Akta Sewa); use a reputable PPAT; insist on a "sub-lease and assign" right so you can resell during the term.

### Path 4: PT PMA (foreign-invested Indonesian company)

- **Legal basis**: UU Penanaman Modal No. 25/2007 + Perpres 10/2021 (Bidang Usaha Penanaman Modal) + the OSS-RBA business licensing system (`https://oss.go.id/`).
- A PT PMA is an Indonesian limited liability company with majority or full foreign ownership. It can hold **HGB** (Right to Build, 30 + 20 + 30 = 80 yr) on land — useful for villa rental businesses, hotels, F&B, co-living, etc.
- **Minimum capital**: IDR 10,000,000,000 (~USD 645k) committed investment **per business activity per location** (Perpres 10/2021); minimum paid-up share capital typically IDR 2,500,000,000 (~USD 161k). Source: BKPM/Kemenves `https://www.bkpm.go.id/`
- **Annual obligations**: LKPM (investment activity report) quarterly; corporate tax (22 %); compliance with sectoral and zoning rules.
- **Use case**: appropriate when you intend to RUN a business (villa rental, restaurant, surf school) — not as a workaround for residential ownership. Using PT PMA solely to hold a personal residence is functionally similar to a nominee structure if the company has no real operating business; tax authority and BKPM scrutiny is increasing 2024–2025.
- **DNI / Positive Investment List**: some sectors are closed or restricted to foreign capital (Perpres 10/2021 lists). Residential property holding by PT PMA is generally permitted as part of property/real-estate sector code KBLI 68 — verify the project KBLI matches.

### Path 5: Marriage to an Indonesian citizen

- **Default rule (KUH Perdata + UU Perkawinan No. 1/1974)**: marriage creates a community-property regime (harta bersama). If the Indonesian spouse acquires Hak Milik during the marriage, the foreigner has a community-property claim → which is a forbidden Hak Milik interest. Result: under MA (Mahkamah Agung) practice, the Hak Milik is at risk of being voided unless the couple has a **prenuptial agreement (perjanjian pisah harta)** — historically required to be signed *before* the wedding, but **MK ruling 69/PUU-XIII/2015** allows a postnuptial agreement to be made during marriage with notarial registration at the marriage office (Kantor Catatan Sipil / KUA).
- With a valid (pre- or post-nup) separation-of-property agreement, the Indonesian spouse can acquire Hak Milik in their sole name; the foreign spouse has no community claim.
- **On divorce**: Indonesian spouse keeps Hak Milik; foreign spouse has no land claim.
- **On Indonesian spouse's death**: foreigner can inherit but must dispose within **1 year** (UUPA §21(3)) — sale or conversion to Hak Pakai.

### The nominee trap (Hak Milik bought via Indonesian friend / family)

- **Mechanism**: foreigner pays an Indonesian "owner of record" (often a friend, driver, business partner) to buy Hak Milik in their name; side-letters give the foreigner economic control and a power of attorney to sell.
- **Why it is illegal**: UUPA §26(2) declares any transfer that has the *effect* of giving Hak Milik to a foreigner **null and void** (batal demi hukum). This is well-established by Mahkamah Agung jurisprudence.
- **2023–2025 enforcement reports (unverified)**: reports of Pengadilan Negeri Denpasar / Gianyar nominee voidings are unverified against the Direktori Putusan (HTTP 403 to automated retrieval) — do not cite a case count. By statute (UUPA §26(2)) the transfer is void by operation of law and the land falls to the State; Kanwil BPN Bali says nominee practice is hidden and generally surfaces only once a legal problem arises. Press coverage: `https://www.thejakartapost.com/` and `https://balidiscovery.com/` archived case reports. Verify case law via `https://putusan3.mahkamahagung.go.id/` (search "nominee Hak Milik" or specific case numbers).
- **Why "side-letters protect me" is wrong**: an Indonesian court asked to enforce the foreigner's side-letter will hold the underlying transaction void; the side-letter is unenforceable because it would give effect to a void transfer. Foreigner has no recourse.
- **Practical guidance**: any reputable Indonesian PPAT or lawyer will refuse to set up Hak Milik nominees post-2023. **Do not recommend** and walk away from any agent who proposes this structure.

### Bali-specific eligibility quirks

- **Tanah Ayahan Desa** (village allotment land) — communal land allocated to village families; even if a sertifikat exists in an Indonesian individual's name, the **village (desa adat)** retains an interest and can refuse alienation to outsiders. Common in inland Bali villages (Ubud, Tegallalang, Bedugul). NEVER buy without village banjar/desa pakraman approval in writing.
- **Subak irrigation system** — UNESCO-recognised Balinese rice terrace irrigation cooperative. Subak land has water-allocation rights tied to the parcel; converting subak rice fields to villa pads can require subak collective consent + an amendment to the provincial spatial plan (**RTRW Provinsi Bali 2023–2043**, with a successor RTRW 2028–2048 in preparation) + BPN reclassification. Source: `https://tarubali.baliprov.go.id` (Dinas PUPRKIM Provinsi Bali) and Bappeda Bali (2026 data; 2026-09-18 verified).
- **Provincial spatial plan (RTRW Bali) + RDTR (detailed)** — many tourist zones (Canggu, Seminyak) have construction moratoria or tighter setback rules updated 2023–2025. Verify zoning at the kabupaten one-stop service (DPMPTSP).
- **Religious / temple buffer** — distance from Pura (temple) regulated by adat law; foreign buyers have had villas demolished after temple-buffer violations. Consult banjar.

### Confidence

**HIGH** — UUPA, PP 18/2021, UU Rumah Susun, UU Penanaman Modal, Permenkumham 22/2023 (Second Home Visa) are all primary statutes published in the Lembaran Negara and on `https://peraturan.bpk.go.id/`. Nominee voidness is HIGH as statute (UUPA §26(2)); Bali nominee court precedents are LOW — no 2023–2025 ruling verified against the Direktori Putusan. **MEDIUM** for current province-specific Hak Pakai price floors (Permen ATR/BPN updated periodically; verify current schedule before quoting an exact threshold).

---

## Section: `--price`

### Primary sources

- **Bank Indonesia (BI) — Indeks Harga Properti Residensial (IHPR / RPPI)**: quarterly residential property price index, 18 major cities. `https://www.bi.go.id/id/publikasi/laporan/Default.aspx?subject=10` (Survei Harga Properti Residensial). Tracks both new + secondary market.
- **BPS (Badan Pusat Statistik) — Statistik Harga Perdagangan Besar Bahan Bangunan**: construction cost index (input to replacement cost). `https://www.bps.go.id/`
- **NJOP (Nilai Jual Objek Pajak)** — government-assessed property value used as the tax base for PBB-P2 and BPHTB. Set per zone (per kelurahan) by the kabupaten/kota. Lookup via local Bapenda website (e.g., DKI Jakarta `https://bapenda.jakarta.go.id/`, Badung `https://bapenda.badungkab.go.id/`). NJOP is ~30–60 % of market value in Jakarta CBD, and ~20–50 % in Bali tourist zones (est., based on observed NJOP-vs-listing gaps; verify per-zone via local Bapenda) — useful as a tax-base reference, NOT a price benchmark.
- **REI (Real Estate Indonesia) — DPP**: developer association market intelligence reports. `https://rei.or.id/site`
- **PPAT-issued AJB (Akta Jual Beli) records** — actual sale prices recorded by the notary at transfer; not centrally published, accessible per-parcel at the kabupaten BPN office.

### Listing platforms (secondary, listings = seller-controlled)

- **Rumah123** (largest, English+Indonesian): `https://www.rumah123.com/`
- **Lamudi Indonesia**: `https://www.lamudi.co.id/`
- **OLX Indonesia (Properti)**: `https://www.olx.co.id/properti_c5158`
- **PropertyGuru Indonesia**: `https://www.propertyguru.co.id/` ❌ DEPRECATED — link dead (verified 2026-06-13); verify with a current Indonesia portal (PropertyGuru/Rumah.com ceased Dec 2023)
- **99.co Indonesia**: `https://www.99.co/id/`
- **Rumah.com**: `https://www.rumah.com/`
- **Bali-specific (foreigner-marketed)**: `https://www.balirealty.com/`, `https://www.harcourtspurba.com/`, `https://www.exoticbali.com/`, `https://www.theagency-bali.com/` ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row — heavily marketed to foreign buyers; prices in USD or AUD; confirm SHMRS / Hak Pakai eligibility before relying on listing terms

### Price benchmarks (Q1 2026 reference)

> **Source warning**: Bali tourist-zone prices on foreigner-targeted platforms can run 20–40 % above Indonesian-rupiah-priced equivalents on Rumah123 / OLX. Always cross-check the same neighbourhood on an Indonesian-language platform. NJOP gives a tax-base floor only.

| Locality | Segment | IDR/m² range | USD/m² est. (15,500/USD) | Source |
|---|---|---|---|---|
| **Jakarta CBD** (Sudirman / Thamrin / SCBD / Kuningan) | New apartemen, branded | 50,000,000–100,000,000 | ≈ $3,225–$6,450 | BI IHPR + Rumah123 Q1 2026 |
| **Jakarta CBD** | Resale apartemen 5–10 yr | 30,000,000–60,000,000 | ≈ $1,935–$3,870 | Rumah123 / 99.co |
| **Jakarta secondary** (Pondok Indah, Kemang, Menteng landed) | Landed house (HM, citizen sale) | 25,000,000–60,000,000 | ≈ $1,610–$3,870 | Rumah123 |
| **Jakarta suburban** (Bekasi, BSD, Tangerang) | Cluster house | 8,000,000–20,000,000 | ≈ $515–$1,290 | Rumah123 |
| **Bali — Canggu / Berawa / Pererenan** | Villa (lease/Hak Pakai/PMA) | 25,000,000–80,000,000 (land) + build | ≈ $1,610–$5,160 land | Bali foreigner platforms Q1 2026 |
| **Bali — Seminyak / Petitenget** | Villa | 30,000,000–100,000,000 (land) | ≈ $1,935–$6,450 | Bali platforms |
| **Bali — Ubud / Tegallalang** | Villa with rice-field view | 8,000,000–30,000,000 (land) | ≈ $515–$1,935 | Bali platforms |
| **Bali — Sanur / Nusa Dua** | Villa / condo | 15,000,000–50,000,000 | ≈ $970–$3,225 | Bali platforms |
| **Bali — Uluwatu / Bingin / Pecatu** | Villa cliffside | 20,000,000–80,000,000 (land) | ≈ $1,290–$5,160 | Bali platforms |
| **Yogyakarta** | Landed house | 5,000,000–15,000,000 | ≈ $325–$970 | Rumah123 |
| **Surabaya** | Apartemen / landed | 8,000,000–25,000,000 | ≈ $515–$1,610 | Rumah123 |
| **Bandung** | Apartemen / landed | 8,000,000–22,000,000 | ≈ $515–$1,420 | Rumah123 |

> Ranges are listing-derived; verify realised vs listing using BI IHPR quarterly index and the NJOP appraised value as a tax-base floor. Bali villa listings often quote land separately from build (USD 1,500–2,500/m² build cost typical).

### Compute

1. Listing price/m² = listing IDR ÷ luas tanah (land area) OR luas bangunan (build area). **Trap**: many Bali villa listings quote a single price covering both; clarify whether it is land-only, build-only, or combined "all-in".
2. Compare to BI IHPR for the same kota (city-level granularity; not parcel-level).
3. Compare to nearest 3–5 same-area listings on Rumah123 / 99.co (Indonesian-language platforms).
4. Pull NJOP via the local Bapenda site for the kelurahan — informs the tax base, not the market value.
5. **Trap (foreign-buyer premium)**: villas marketed on foreigner platforms can be priced 20–40 % above Indonesian-rupiah listings of comparable assets. Always cross-check.
6. **Trap (pre-construction Bali)**: many Bali developers sell off-plan with deposits in escrow that is in practice not enforceable. Default scenarios in 2023–2025 (multiple Canggu projects) have left foreign buyers without recourse. Pay only against milestone completion verified independently.

### Confidence

**HIGH** for Jakarta apartemen ranges (BI IHPR + multiple platforms agree within ±10 %). **MEDIUM** for Bali villa pricing (foreigner-platform-dominated, less neutral indexing). **LOW** for rural / non-tourist Bali (Buleleng, Karangasem) and outer-island markets (Lombok / Flores / Sumba) — listings sparse and verification difficult.

---

## Section: `--traffic`

### Primary sources

- **Kementerian PUPR — Direktorat Jenderal Bina Marga** (Ministry of Public Works, Directorate General of Highways): national + provincial road data. `https://binamarga.pu.go.id/`
- **Korlantas POLRI** (Traffic Police HQ): national accident statistics. `https://korlantas.polri.go.id/`
- **Jasa Marga** (state-owned tollway operator): toll-road volumes and incident data. `https://www.jasamarga.com/`
- **Ditjen Intram — Direktorat Jenderal Integrasi Transportasi dan Multimoda** (Kementerian Perhubungan), established by **Perpres 173/2024** with a **national** multimodal-integration mandate, not a Jabodetabek-specific one: `https://ditjenintram.kemenhub.go.id/`. The former **BPTJ (Badan Pengelola Transportasi Jabodetabek)** domain `bptj.dephub.go.id` no longer resolves — verify BPTJ's current status with Kemenhub (2026 data, source ditjenintram.kemenhub.go.id; 2026-09-18 verified)
- **Dinas Perhubungan provincial / kabupaten**: local traffic counts where conducted (rare and inconsistent).
- **OpenStreetMap (OSM)** — fallback for road class when official AADT not available

### Verdict bands (vehicles per day, est.)

- 🟢 < 2,000 v/d: rural lane, gang, kampung road, Bali interior
- 🟡 2,000–10,000 v/d: kabupaten road, urban side street
- 🟠 10,000–40,000 v/d: provincial trunk (jalan provinsi), urban arterial, Bali main tourist artery (e.g., Jl. Raya Canggu, Jl. Sunset Road)
- 🔴 > 40,000 v/d: national highway / Jakarta arterial / tollway

### Coarse fallback (OSM `highway` tag)

- `motorway` / `trunk` = jalan tol (Jasa Marga toll roads, e.g., Jagorawi, Cipularang)
- `primary` = jalan nasional (jalan utama nasional)
- `secondary` = jalan provinsi
- `tertiary` = jalan kabupaten
- `residential` = jalan lingkungan / kompleks / gang

### Jakarta-specific quirks

- Jakarta has chronic congestion; AADT understates noise/pollution exposure due to stop-and-go. A 25,000 v/d arterial in Jakarta behaves worse in flow than a 50,000 v/d expressway.
- Elevated tollways over residential kompleks (e.g., Jakarta Inner Ring Road, Jakarta Outer Ring Road) generate noise + particulate exposure 24/7; flag any property within 100 m of a toll viaduct pillar.
- TransJakarta busway corridors are noisy at peak; MRT North–South Line and LRT Jakarta are quieter (electric).
- **Jakarta air quality (PM2.5)**: chronically poor (often 50–120 µg/m³ vs WHO guideline 15); Jakarta has been ranked among the most polluted megacities globally on multiple IQAir reports 2023–2025. Verify current AQ at **Kementerian Lingkungan Hidup (KLH) / Badan Pengendalian Lingkungan Hidup (BPLH)** — `https://ispu.kemenlh.go.id` (2026 data, source kemenlh.go.id; 2026-09-18 verified)

### Bali-specific quirks

- Bali has no toll roads outside the Bali Mandara (Nusa Dua–Benoa–Ngurah Rai airport tollway). Most traffic moves on jalan provinsi or jalan kabupaten that were not built for tourist-volume motorbike + minibus + tour-coach mix.
- Canggu / Seminyak / Kuta arteries (Jl. Raya Canggu, Jl. Sunset Road, Jl. Petitenget) experience severe congestion in dry-season tourist peak (Jul–Sep, Dec–Jan). Property on these streets has high noise + low walkability.
- Inland Bali (Ubud, Bedugul, Sidemen) significantly quieter; Karangasem and Buleleng are quietest.

### Confidence

**MEDIUM** — DGB Bina Marga publishes some national-highway data but coverage of provincial/kabupaten traffic is sparse and inconsistent. Bali municipal traffic data is fragmented across kabupaten. For most non-toll roads, OSM-class fallback is the realistic baseline.

---

## Section: `--tax`

### Annual property tax — PBB-P2 (Pajak Bumi dan Bangunan — Perdesaan dan Perkotaan)

**Primary statute**: UU HKPD No. 1/2022 §38–§50 (Hubungan Keuangan Pusat–Daerah), implementing local tax restructuring 2024 onward. Earlier base law: UU PDRD 28/2009. Administered by **kabupaten/kota** through local Bapenda. Source: `https://peraturan.bpk.go.id/Details/195696/uu-no-1-tahun-2022`

**Tax base**: NJOP (Nilai Jual Objek Pajak) — government-assessed value of land + building, set annually per zone by kabupaten/kota. Lookup via local Bapenda site:
- DKI Jakarta: `https://bapenda.jakarta.go.id/`
- Badung (Bali): `https://bapenda.badungkab.go.id/`
- Denpasar: `https://bpkad.denpasarkota.go.id/`
- Gianyar: `https://bpkad.gianyarkab.go.id/`

**Rate (UU HKPD §41)**: maximum **0.5 %** of NJOP-KP (NJOP minus NJOPTKP, the non-taxable portion). Each kabupaten sets its rate within the ceiling; common rates 2024–2026:

| Bracket (NJOP value) | Typical rate |
|---|---|
| ≤ 1,000,000,000 IDR | 0.10 %–0.20 % |
| 1,000,000,001–10,000,000,000 | 0.20 %–0.30 % |
| > 10,000,000,000 | 0.30 %–0.50 % (ceiling) |

> Verify exact bracket and rate via the local Perda (peraturan daerah) for the kabupaten — figures vary materially.

**NJOPTKP (non-taxable threshold)**: minimum IDR 10,000,000 per UU HKPD §40; many regions set IDR 12,000,000–15,000,000.

**Filing**: SPPT-PBB (notice) issued by Bapenda in early year; payment due typically by 30 September (date varies by region). Penalty 2 %/month late. Payable at bank, ATM, or via local government e-payment portal.

**Worked example** (Jakarta apartemen, NJOP IDR 5,000,000,000):
- (5,000,000,000 − 15,000,000) × 0.0025 = **12,462,500 IDR/yr** (~USD 800/yr — modest internationally, but materially higher than Thailand or Czech)

### Transaction taxes (one-time at purchase)

| Tax | Rate | Base | Who pays |
|---|---|---|---|
| **BPHTB** (Bea Perolehan Hak atas Tanah dan Bangunan) | **5 %** statutory ceiling (UU HKPD §47); kabupaten can set lower | Sale price OR NJOP, whichever higher, MINUS NJOPTKP-BPHTB (typically IDR 60,000,000–80,000,000) | Buyer |
| **PPh Final (Pajak Penghasilan Final atas Pengalihan Hak)** | **2.5 %** (1 % for affordable housing developers) | Sale price OR NJOP, whichever higher | Seller |
| **PPN (VAT)** | **11 % effective** (via DPP 11/12 mechanism under PMK 131/2024); **PPN 12 % applies ONLY to luxury properties** — apartemen / landed houses ≥ IDR 30 billion under PPnBM-aligned thresholds. Both rates derive from UU HPP 7/2021 (2026-05-27 verified, source: Baker McKenzie / ARMA Law / Kemenko Perekonomian 31-Dec-2024 statement). Verify at `https://www.pajak.go.id/`. | Sale price | Buyer, on new properties from a developer registered as PKP (taxable entrepreneur) |
| **PPnBM (luxury VAT)** | 20 % | Properties above luxury thresholds (apartemen > 30 billion IDR, landed houses > 30 billion IDR per Permenkeu thresholds) | Buyer |
| **Stamp duty (bea meterai)** | IDR 10,000 per document | Each notarial deed | Buyer (custom) |

**Notarial / PPAT fees**:
- **PPAT (Pejabat Pembuat Akta Tanah)** — fee for AJB drafting + BPN registration. Statutory cap **1 %** of transaction value (Permen ATR/BPN); negotiable. Typical: 0.5–1 % depending on value.
- **Notaris** — separate from PPAT for non-AJB documents (e.g., PPJB pre-sale agreement, kuasa). Fee per Indonesian Notary Code; typically IDR 5,000,000–25,000,000 per deed.
- **BPN sertifikat fee** — fixed admin fee, varies by transaction type. Typically IDR 50,000–500,000 per sertifikat issuance + PNBP fee per UU PNBP.

**Worked example** — foreign buyer of a IDR 5,000,000,000 (~USD 322k) Jakarta apartemen from an Indonesian individual seller (resale, no PPN):
- BPHTB: (5,000,000,000 − 60,000,000) × 5 % = **247,000,000 IDR** (~USD 16,000) — buyer
- PPh Final: 5,000,000,000 × 2.5 % = 125,000,000 IDR (~USD 8,065) — seller
- PPAT fee: 5,000,000,000 × 0.75 % = 37,500,000 IDR (~USD 2,420)
- BPN admin + bea meterai: ~IDR 2,000,000 (~USD 130)
- **Buyer side total**: ~5.5 % of price
- If buying a NEW unit from a developer, add 11 % PPN (~USD 35,500 on this example) — **buyer side ~16–17 %**

> If buyer also pays sworn translator + lawyer review (recommended for foreign buyer): add IDR 10,000,000–50,000,000 (~USD 645–$3,225).

### Foreign owner-specific

- **No foreign-buyer surcharge stamp duty** at the federal level (unlike Singapore ABSD or NSW Australia). BPHTB is the same rate for citizens and foreigners — but the underlying right being conveyed is different (Hak Pakai for foreigners vs Hak Milik for citizens).
- **Hak Pakai conversion fee at BPN** when converting from HM to HP at the foreign buyer's purchase: small admin fee, typically < IDR 5,000,000.
- **Annual NJOP review**: kabupaten can update NJOP zonally; sharp upward revisions in Bali tourist zones 2023–2025 (Badung, Gianyar) — verify current NJOP before estimating PBB.

### Capital gains for foreign sellers

- Same PPh Final 2.5 % as Indonesian sellers — withheld at PPAT before AJB.
- **Foreign-currency repatriation**: needs evidence of original inbound transfer (FX records); BI (Bank Indonesia) FX reporting for amounts ≥ USD 10,000.
- **Tax residency**: a foreigner in Indonesia ≥ 183 days in 12 months is a tax resident under UU PPh §2 — global income taxable; verify treaty provisions if applicable.

### Future risk

- **PPN 12 % is luxury-only** (apartemen / landed houses ≥ IDR 30 billion under President Prabowo's Dec-2024 adjustment + PMK 131/2024). All other VAT-able transactions remain **effectively 11 %** via the DPP 11/12 tax-base mechanism. Source: UU HPP 7/2021 + PMK 131/2024 (2026-05-27 verified).
- **NJOP zonal updates**: Bali tourist-zone NJOP is rising 2024–2026 — annual PBB will rise.
- **Local transaction-tax tweaks**: kabupaten may adjust BPHTB rate up to 5 % ceiling; verify the relevant Perda.
- **Property capital gains for foreign sellers**: subject to ongoing DJP interpretation; verify treaty benefits.

### Confidence

**HIGH** for the statutory framework (UU HKPD 1/2022, UU PPh, UU PPN published in Lembaran Negara). **MEDIUM** for current 2026 effective kabupaten rates (set by Perda; varies by region; verify the specific Perda before quoting an exact rate).

---

## Section: `--rental`

### Long-term residential rental income tax

**For foreign owners (typical Hak Pakai or SHMRS holder)**:
- **PPh Final atas sewa tanah dan bangunan (Final tax on rental of land and buildings)** — UU PPh §4(2)(d) + PP 34/2017: **10 % final tax** on gross rental income.
- Withheld by tenant if tenant is a corporate entity (PPh 23 / PPh 4(2) withholding); paid directly by landlord if tenant is an individual.
- "Final" means no further income tax owed on this revenue — but no expense deduction either; gross-up basis.
- Filing: SPT Tahunan (annual return) for tax-resident landlords; for non-resident, PPh withholding by tenant or self-assessment.

**For Indonesian owners (renting Hak Milik)**:
- Same 10 % final tax under PP 34/2017.

### Short-term rentals (Airbnb / Booking / Agoda)

**The headline rule**: **renting accommodation to tourists for stays under 30 days requires a hotel / pondok wisata / villa rental licence** under UU Kepariwisataan No. 10/2009 + Permenparekraf 4/2021 (Standar Usaha Pariwisata) + provincial regulations.

**Practical reality**:
- **Bali**: the Bali provincial government and Badung/Gianyar/Tabanan regencies have actively required villa rental licences (Pondok Wisata or TDUP — Tanda Daftar Usaha Pariwisata) and have been raiding unlicensed villas in Canggu / Berawa / Seminyak in 2023–2025. Foreign-owned villas without proper PT PMA + TDUP + IMB/PBG (building permit aligned with commercial use) are at risk of closure orders + tax back-assessment.
- **OTA platform NIB verification (2026, industry-reported)**: villas listed on Airbnb / Booking.com / Expedia are being pushed to show a verified **NIB (Nomor Induk Berusaha)** or risk delisting. The **31 Mar 2026** industry deadline was superseded: Kemenpar says OTAs will require **NIB + KBLI + NKU** checked against OSS through an API targeted to launch **June 2027** (Kemenpar siaran pers, primary), and the Minister announced on 26 May 2026 that ~1,600 verified unlicensed operators would be delisted from **1 Aug 2026** (ANTARA / Kontan, secondary); whether that delisting happened is not verified. Whether Permenpar 18/2016 bars foreigners from a Pondok Wisata licence, and whether a **PT PMA** may hold the villa code **KBLI 55193**, is data not publicly available in primary text read — verify at Kemenpar JDIH (`https://jdih.kemenpar.go.id/`), BKPM (`https://www.bkpm.go.id/`) and OSS (`https://oss.go.id/`), and with your PPAT.
- **Jakarta**: most condo bylaws (peraturan rumah tangga) forbid daily/short-stay use; enforcement via building management.
- **Yogyakarta**: provincial regulation requires Pondok Wisata licence; often enforced via regular inspection.

**Tax treatment for legal STR (with TDUP)**:
- **PPh Final 0.5 %** (UMKM regime under PP 55/2022 / UU HPP) for income < IDR 4.8 billion/yr — applies to small Indonesian entrepreneurs only; foreigners typically operate via PT PMA which uses the 22 % corporate tax regime instead.
- **PPN 11 %** on hotel/villa charges if turnover > IDR 4.8 billion/yr threshold.
- **Pajak Hotel 10 %** (regional tax under UU HKPD §50–§54): 10 % final on gross hotel/villa revenue, paid to the kabupaten. Bali has aggressive enforcement — Badung Bapenda audits villa booking records.
- **Pajak Hiburan, Pajak Restoran**: separate regional taxes if you offer ancillary services.

**Penalty risk for unlicensed STR in Bali**: Badung/Gianyar can close the property + back-assess Pajak Hotel for prior years + criminal referral if persistent. 2024–2025 Badung enforcement closed multiple Canggu villas operating without TDUP.

**Workaround often advertised**: "monthly rentals only" (≥ 30-day stays) escape Pondok Wisata licence — but you still owe PPh Final 10 % on the rental income.

### Strategic notes

- **Bali villa STR**: gross yields can theoretically reach 7–12 % in peak Canggu / Seminyak years — but only if (1) proper PT PMA + TDUP + IMB/PBG, (2) professional manager taking 25–35 % of revenue, (3) Pajak Hotel 10 % + corporate tax 22 % paid. Net yields 3–5 % more realistic after all-in costs and 50–60 % seasonal occupancy.
- **Jakarta apartemen long-let**: yields 4–6 % gross typical (CBD), 3–4 % outer; tenant pool is expat + corporate.
- **Yogyakarta / Bandung student lets**: yields 6–8 % gross but high turnover and management intensity.
- **Pre-construction yield projections**: developer projections of 12–15 % yields are routinely overstated by 50–100 %; treat with extreme scepticism.

### Confidence

**HIGH** for PPh Final framework (UU PPh + PP 34/2017). **MEDIUM** for STR enforcement intensity (varies by province and political cycle; Bali enforcement most active). **MEDIUM** for current Bali Pajak Hotel rate / villa licensing process (subject to Badung/Gianyar Perda updates).

---

## Section: `--work=<profession>`

### Job platforms

- **JobStreet Indonesia**: `https://www.jobstreet.co.id/` (SEEK group, largest)
- **LinkedIn Indonesia**: very active in Jakarta tech / finance / multinationals
- **Glints Indonesia**: `https://glints.com/id` (tech / startup focus)
- **Kalibrr**: `https://www.kalibrr.id/`
- **Karir.com**: `https://www.karir.com/`
- **Glassdoor Indonesia**, **Indeed Indonesia**

### Work permit & visa for foreigners

**Foreign nationals working in Indonesia require a work permit (RPTKA + IMTA; under Permenaker 8/2021 the integrated permit is now a Notifikasi Pengesahan RPTKA via the OSS-RBA portal `https://oss.go.id/`).** Tied to:
1. A specific employer (sponsoring Indonesian entity)
2. A specific job position (limited to roles on the foreign-eligible list)
3. A specific work location

**Restricted occupations**: Permenaker 349/2019 lists ~18 prohibited positions (HR director, HR manager, certain craft professions). Multiple sectors limited to expert/managerial roles only — manual / clerical / general worker positions reserved for Indonesians.

**Mandatory Indonesian counterpart (TKI Pendamping)**: each foreign worker must train an Indonesian successor under Permenaker rules.

**DPKK (Dana Kompensasi Penggunaan Tenaga Kerja Asing)**: USD 100/month per foreign worker; paid by sponsoring employer to the Ministry of Manpower fund.

### Visa pathways relevant to property buyers

| Visa | Duration | Income/asset threshold | Property angle |
|---|---|---|---|
| **KITAS** (Limited Stay Permit — work, family, study, investor) | 1–2 yr renewable | Sponsor-dependent (employer / spouse / investor company) | One of the dokumen keimigrasian accepted for Hak Pakai / SHMRS (PP 18/2021 Penjelasan Pasal 69(1) also lists visa and passport) — confirm BPN practice at the Kantor Pertanahan |
| **KITAP** (Permanent Stay Permit) | 5 yr renewable indefinitely | Typically after ≥ 3 yrs KITAS or marriage | Not a statutory precondition in PP 18/2021 (Pasal 69(1) requires a dokumen keimigrasian) — confirm BPN practice at the Kantor Pertanahan |
| **Second Home Visa (Visa Rumah Kedua, Permenkumham 22/2023)** | 5 + 5 yr | IDR 2,000,000,000 (~USD 130k) deposit in Indonesian state bank; property route value contested in secondary sources (IDR 2B-equivalent vs IDR 5B vs ~USD 1M) — verify at Imigrasi | Possible: property route exists per secondary sources — verify qualifying value with Imigrasi |
| **Investor KITAS** (Index B-211A → KITAS via PT PMA) | 1–2 yr renewable | PT PMA shareholder ≥ IDR 1,000,000,000 paid-up + KBLI alignment | Indirect: via PT PMA structure |
| **Retirement KITAS (Lansia)** | 1 yr renewable up to 5 | Age 55+, USD 1,500/mo passive income or USD 18,000/yr; insurance + accommodation arranged | No work right; allows long stay |
| **Digital Nomad / Remote Worker E33G** | 1 yr renewable | USD 60,000+/yr foreign-sourced employment income (verify current threshold at Imigrasi) | No Indonesian work; allows residence; potential foreign-source income tax exemption per recent guidance — verify with DJP |
| **Work + Family KITAS** (sponsored by Indonesian-incorporated employer) | 1–2 yr renewable | Sponsor-dependent | Path to KITAP after qualifying years |

- **Imigrasi portal (visa applications)**: `https://www.imigrasi.go.id/` and **e-Visa** `https://evisa.imigrasi.go.id/`
- **OSS-RBA (work-permit RPTKA via integrated business licensing)**: `https://oss.go.id/`
- **Source for the rules**: UU Keimigrasian No. 6/2011 + Permenkumham 22/2023 (Second Home Visa) + Permenaker 8/2021.

### Self-employment / freelance reality

- A freelance foreigner in Indonesia legally needs either a work permit (sponsored) OR to operate via a registered PT PMA. Pure freelancing on a tourist/social visa is **not permitted** and is a deportation risk.
- The **Digital Nomad Visa E33G (2024)** allows long-stay for remote work for a foreign employer — but ban on local Indonesian-sourced income remains; you cannot legally invoice Indonesian clients.
- **PT PMA for freelancing**: minimum capital + LKPM reporting + 22 % corporate tax — rarely cost-effective for sub-USD 100k/yr individual income.

### Salary benchmarks (Jakarta 2025–2026)

| Role | Median monthly gross IDR | USD est. (15,500/USD) |
|---|---:|---:|
| Software engineer (mid-senior, MNC / unicorn) | 25,000,000–60,000,000 | $1,610–$3,870 |
| Software engineer (senior, foreign-paid remote) | 60,000,000–150,000,000 | $3,870–$9,680 |
| English teacher (degree, certified, international school) | 15,000,000–35,000,000 | $970–$2,260 |
| Hotel mid-mgmt | 15,000,000–35,000,000 | $970–$2,260 |
| Bali villa manager (foreigner, with PT PMA) | 25,000,000–60,000,000 | $1,610–$3,870 |
| Jakarta median (all sectors, 2025) | ~5,500,000 | ~$355 |
| **UMP DKI Jakarta 2026** (provincial minimum wage) | 5,396,761 (2025 figure; verify 2026 SK Gubernur for adjustment) | ~$348 |
| **UMK Badung Bali 2026** | ~3,300,000 (2025 figure; verify SK Gubernur Bali for 2026) | ~$215 |

Sources: BPS `https://www.bps.go.id/`, JobStreet salary survey reports, Kementerian Ketenagakerjaan UMP/UMK SK Gubernur.

### Confidence

**HIGH** for visa thresholds and work permit framework (Imigrasi / Kemenaker primary). **MEDIUM** for restricted-occupation list (Permenaker 349/2019 updated periodically — verify current). **MEDIUM** for salary benchmarks (large MNC vs SME variance; UMP figures need annual SK Gubernur verification).

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **BNPB (Badan Nasional Penanggulangan Bencana)** | `https://www.bnpb.go.id/` | Disaster declarations, hazard maps, DesInventar incident database |
| **InaRISK BNPB** | `https://inarisk.bnpb.go.id/` | Per-kabupaten hazard index (gempa, tsunami, banjir, longsor, gunung api, kekeringan) |
| **BMKG (Badan Meteorologi, Klimatologi, dan Geofisika)** | `https://www.bmkg.go.id/` | Earthquake / tsunami warnings, weather, climate projection |
| **PVMBG / Badan Geologi** (Pusat Vulkanologi dan Mitigasi Bencana Geologi) | `https://magma.esdm.go.id/` | Volcanic activity (Indonesia has 127 active volcanoes); landslide hazard |
| **Kementerian PUPR — Direktorat Sumber Daya Air** | `https://sda.pu.go.id/` | Floodplain mapping, dam/river system |
| **InaTEWS (Indonesia Tsunami Early Warning System)** — under BMKG | `https://inatews.bmkg.go.id/` | Real-time tsunami alerts |
| **Kementerian Lingkungan Hidup (KLH) / BPLH** — successor to Kementerian LHK | `https://www.kemenlh.go.id/` and `https://ispu.kemenlh.go.id` (air quality) | Forest fires, air quality (ISPU) |
| **Bappeda Bali / Dinas PUPRKIM Provinsi Bali** (spatial planning; "Distarcip" no longer exists) | `https://tarubali.baliprov.go.id` · agency: `https://dispuprkim.baliprov.go.id` | RTRW provincial spatial plan; flood/landslide overlay (2026 data, source dispuprkim.baliprov.go.id; 2026-09-18 verified) |

### Earthquake (gempa)

- Indonesia sits on the Pacific Ring of Fire — Sunda Trench (Sumatra/Java/Bali subduction) + Banda + Halmahera arcs. Multiple M ≥ 7 events per decade.
- **Seismic-hazard map**: SNI 1726:2019 (Indonesian seismic design code) zonation; updated PUSGEN 2017 + 2022 hazard maps. Lookup via `https://magma.esdm.go.id/` and PUPR.
- **Bali**: moderate-to-high seismic exposure (M 7.0 Lombok 2018 felt strongly; M 6.4 Karangasem 2025 verify status); building stock highly variable — many older Bali villas are unreinforced masonry.
- **Jakarta**: low direct seismic source but **soft-soil amplification** in alluvial plain; distant mega-thrust events (Mentawai, Selat Sunda) projected to cause significant high-rise stress. Verify any Jakarta high-rise complies with SNI 1726:2019.
- **Sumatra megathrust risk**: Mentawai Gap (segment between 2007 and 2010 ruptures) carries unrelieved seismic moment; M 8.5+ tsunami event a recognised credible scenario per BMKG and BNPB.

### Volcanic activity (gunung api)

- 127 active volcanoes; PVMBG monitors via MAGMA Indonesia.
- **Bali**: Gunung Agung (last major eruption 2017–2019; 6 km exclusion zone during activity); Gunung Batur (less explosive but active). Properties within 10 km of Agung crater face periodic evacuation orders.
- **Java**: Merapi (Yogyakarta), Semeru (East Java), Krakatau (Selat Sunda) — periodic eruptions affecting nearby property; Kementerian ESDM hazard maps.
- **Lombok / Sumbawa / Flores / Sulawesi**: multiple active volcanoes; verify InaRISK for parcel-specific exposure.

### Tsunami

- **Andaman / Mentawai / Sunda Strait**: high tsunami exposure; 2004 Indian Ocean (Aceh + Nias), 2018 Selat Sunda (post-Krakatau collapse), 2018 Palu (Sulawesi) all generated catastrophic local tsunami.
- **Bali**: south-coast (Uluwatu, Nusa Dua, Sanur, Kuta) faces Sunda-trench-sourced tsunami exposure; InaTEWS sirens deployed but evacuation routes underdeveloped. Property at < 10 m elevation within 500 m of south-Bali shoreline = high tsunami risk.
- **Jakarta**: low direct tsunami risk (north-coast, sheltered); 2018 Selat Sunda event affected west-Java (Carita, Anyer) more than DKI proper.

### Flood (banjir)

- Jakarta has chronic flooding driven by upstream rainfall (Bogor highlands), ground subsidence (north Jakarta sinking ~5–25 cm/yr in places — among the most rapidly subsiding coastal urban areas; Pluit / Ancol especially affected; verify current rates via Kementerian PUPR Direktorat Sumber Daya Air), and tidal coupling. Major events 2007, 2013, 2020, 2024.
- **Bali**: localised flood in Kuta / Legian / Canggu lowland during peak rain (Nov–Mar); rapid storm-runoff in narrow valleys (Ubud).
- **Sumatra / Kalimantan / Sulawesi**: river-basin floods seasonal.
- Check InaRISK + provincial Bappeda hazard overlays per kabupaten.

### Air quality (PM2.5)

- Jakarta: chronically poor; ranks among most polluted megacities (IQAir reports 2023–2025); often 50–120 µg/m³ vs WHO guideline 15.
- South Sumatra / Riau / Kalimantan: severe haze events Aug–Oct from peatland and forest fires; PM2.5 > 300 µg/m³ in worst years.
- Bali: relatively clean coastal air; inland Ubud occasionally affected by agricultural burning.
- Source: ISPU `https://ispu.kemenlh.go.id` + IQAir.

### Climate-change projections (BMKG + IPCC AR6 + KLHK)

- **Temperature**: +1.0–2.5 °C by 2050 vs 1986–2005 baseline (RCP4.5 → RCP8.5). Source: BMKG downscaled CMIP6, IPCC AR6 Atlas.
- **Sea-level rise**: +20–60 cm by 2100; combined with Jakarta subsidence = compound risk. Government's response is to relocate the capital to **IKN Nusantara** (Kalimantan Timur, ongoing 2024–2030).
- **Extreme rainfall**: monsoon variability increasing; Bali wet-season intensity rising.
- **Drought**: NTT (Nusa Tenggara Timur) and parts of Java increasingly drought-affected — reservoir levels critical 2023.
- **Coral reef bleaching**: Indonesian Coral Triangle stress increasing; affects Bali / Lombok / Komodo tourism economy.

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1980s** | Unreinforced masonry, asbestos roofing, weak foundations on alluvial soil; minimal seismic design |
| **1980s–2000s** | SNI Gempa 1726:1989 / 2002 in force but enforcement variable; many villa builds informal with no permit |
| **Post-2002 SNI 1726:2002** | Improved seismic design for engineered buildings |
| **Post-2019 SNI 1726:2019** | Current seismic code, harmonised with IBC; well-enforced for engineered Jakarta high-rises, variably enforced elsewhere |
| **Bali villas (2010+ tourist boom)** | Quality highly variable; many unpermitted (no IMB/PBG), weak foundations, untested septic; "white villa" cosmetic builds on poor structural base common — independent structural inspection essential |

### Mandatory pre-purchase diagnostics

| Document | Required because | Where |
|---|---|---|
| **Sertifikat (Hak Milik / HGB / Hak Pakai / SHMRS) verification** | Confirm chain of title, no encumbrances | BPN kantor pertanahan kabupaten/kota — pengecekan sertifikat, via PPAT |
| **BPN encumbrance search (cek beban)** | Mortgages (hak tanggungan), liens, court orders | BPN |
| **PBB-P2 payment evidence (SPPT + bukti bayar)** | Confirm no arrears (BPHTB blocked if PBB unpaid) | Local Bapenda |
| **IMB / PBG (Persetujuan Bangunan Gedung — building permit)** | Confirm building was permitted | Kabupaten/kota DPMPTSP |
| **SLF (Sertifikat Laik Fungsi — fitness-for-use certificate)** | Confirm building approved for occupancy | DPMPTSP |
| **Pertelaan + AJB + sertifikat induk** (condo) | Confirm strata title and project approval | Developer + BPN |
| **For Bali villa land**: village banjar / desa pakraman approval letter (if village interest) | Confirm no adat / customary claim | Banjar head |
| **Subak letter of consent** (rural Bali if converting agricultural) | Subak retains water rights | Subak organisation |
| **For foreign buyer**: immigration-document copy (PP 18/2021 Pasal 69(1) dokumen keimigrasian — confirm which document BPN accepts at the Kantor Pertanahan) + PPAT verification of foreign-eligible price floor + zoning | Foreign Hak Pakai / SHMRS validity | Imigrasi + PPAT + BPN |

**Foreign buyers should commission an Indonesian-licensed PPAT + a separate due-diligence lawyer for title and encumbrance verification — DIY is not feasible because all BPN records are in Bahasa Indonesia and customary (adat) interests often unwritten.**

### Confidence

**HIGH** for earthquake / volcano / tsunami framework (BMKG / BNPB / PVMBG primary). **HIGH** for build-code statutory framework. **MEDIUM** for parcel-level adat/customary risk in Bali (often unrecorded; requires banjar consultation).

---

## Section: `--mains`

### Water supply

- **PDAM (Perusahaan Daerah Air Minum)** — local government water utility per kabupaten/kota. Coverage and quality varies dramatically.
  - DKI Jakarta: PAM Jaya `https://pamjaya.co.id/` (with private operator concessions)
  - Bali Badung: PDAM Tirta Mangutama `https://tirtamangutama.badungkab.go.id/`
  - Bali Denpasar: PDAM Tirta Sewakadarma
- **Rural / Bali interior**: many properties on private bore well (sumur bor) with storage tank (toren); PDAM coverage often unavailable.
- **Bali groundwater stress**: south Bali (Canggu, Seminyak, Pererenan) suffering aquifer drawdown — borehole water quality declining + saltwater intrusion in coastal areas. Independent water test recommended.

### Sewer / wastewater

**Indonesia has very limited centralised sewer coverage compared to OECD baselines.**

- **Jakarta**: centralised sewer reaches < 15 % of population (PD PAL Jaya `https://palyja.co.id/` and partner concessions). Most apartemen + landed houses use **on-site septic + soakaway**. Coverage expansion targeted but slow.
- **Bali**: virtually no centralised sewer outside small Sanur and Nusa Dua schemes. Every villa = on-site septic + soakaway. Many Canggu / Kuta soakaways are at saturation — groundwater quality testing routinely shows E. coli contamination. Bali provincial government (DLH Bali) is enforcing IPAL (Instalasi Pengolahan Air Limbah) requirements for new villa builds.
- **Other cities**: Surabaya, Yogyakarta, Bandung have small centralised systems but most properties on septic.

**Building Code requirement** (PP 16/2021 + Permen PUPR): on-site treatment (IPAL) required for buildings > 500 m² — typical for Bali villas, hotels, condos.

### Verification path

1. Listing language scan:
   - "PDAM" = mains water connection
   - "Sumur bor" = bore well
   - "IPAL" or "septic + sumur resapan" = on-site treatment
   - "Saluran kota" / "Sewer kota" = mains sewer (rare, urban only)
2. **Jakarta**: call PAM Jaya / Aetra / Palyja for water; PD PAL Jaya for sewer.
3. **Bali**: call PDAM kabupaten for water; DLH Bali / kabupaten DLH for IPAL compliance.
4. **Bali villa specifically**: ask seller for the IPAL design + last desludge date (sedot WC); verify soakaway not saturated (rainy-season test).

### Cost benchmarks

| Scenario | Cost (IDR) |
|---|---:|
| PDAM connection (Jakarta / Bali, where available) | 1,500,000–5,000,000 |
| Bore well + tank (sumur bor + toren) | 15,000,000–60,000,000 |
| Septic install (3-stage modern, Bali villa) | 25,000,000–80,000,000 |
| IPAL system (boutique villa scale) | 50,000,000–250,000,000 |
| Septic desludge (sedot WC) | 500,000–2,000,000 per service |
| RO / filter system (residential) | 5,000,000–25,000,000 |
| Backup water-storage (1,000 L tank) | 1,500,000–4,000,000 |

### Confidence

**HIGH** for the institutional framework (PDAM / PAL Jaya / DLH). **MEDIUM** for parcel-level coverage (sewer particularly variable; verification often requires telephone the local kabupaten + visit during rainy season).

---

## Cost benchmarks (ID 2026)

| Item | Cost (IDR) | USD est. |
|---|---:|---:|
| **Lawyer fees (foreign buyer condo SHMRS)** | 25,000,000–100,000,000 (or 0.5–1 % of price) | $1,610–$6,450 |
| **Lawyer fees (foreign buyer Bali villa, lease/PMA)** | 75,000,000–300,000,000+ | $4,840–$19,400+ |
| **PPAT fee (AJB drafting + BPN registration)** | 0.5–1 % of transaction value (cap 1 %) | varies |
| **Sworn translator (penerjemah tersumpah)** | 150,000–500,000/page | $10–$32/page |
| **Title verification (cek sertifikat at BPN)** | 50,000–500,000 admin + PPAT fee | $3–$32 + PPAT |
| **Building inspector (apartemen / condo)** | 3,000,000–15,000,000 | $195–$970 |
| **Building inspector (Bali villa, structural + IPAL)** | 10,000,000–50,000,000 | $645–$3,225 |
| **Land surveyor (BPN-licensed)** | 5,000,000–25,000,000 | $325–$1,610 |
| **BPHTB transfer tax** | 5 % of (sale value − NJOPTKP-BPHTB) | varies |
| **PPh Final (seller side)** | 2.5 % of sale value | seller pays |
| **PPN VAT (new from developer)** | 11 % effective (12 % luxury-only ≥ IDR 30 bn per PMK 131/2024) | buyer pays |
| **Notaris fees (PPJB, kuasa, etc.)** | 5,000,000–25,000,000 per deed | $325–$1,610 |
| **Common-area fees (apartemen, mid-range)** | 12,000–30,000 IDR/m²/month | $0.80–$2/m²/mo |
| **Common-area fees (luxury Jakarta apartemen)** | 25,000–80,000 IDR/m²/month | $1.60–$5/m²/mo |
| **Sinking fund (one-off, at handover)** | 200,000–500,000 IDR/m² | $13–$32/m² |
| **Typical apartemen refurb (60 m² full)** | 300,000,000–800,000,000 | $19,400–$51,600 |
| **Bali villa pool maintenance (chemicals + cleaner)** | 1,500,000–4,000,000/mo | $97–$258/mo |
| **Annual property tax (residential, NJOP < 1B IDR)** | 1,000,000–2,000,000 typical | $65–$130 |
| **Annual property tax (Jakarta apartemen, NJOP 5B IDR)** | ~12,500,000 | ~$800 |
| **Annual KITAS sponsorship (employer / family)** | 8,000,000–25,000,000 | $515–$1,610 |
| **Second Home Visa (Visa Rumah Kedua) deposit** | 2,000,000,000 (refundable) | ~$130,000 |
| **PT PMA setup (legal + capital + OSS)** | 30,000,000–80,000,000 (legal) + 2,500,000,000 paid-up | $1,935–$5,160 + $161k capital |
| **Total transaction cost (foreign buyer, all-in resale)** | ~6–8 % of price | — |
| **Total transaction cost (foreign buyer, all-in new from developer with PPN)** | ~17–19 % of price | — |

---

## Active fiscal incentives (2026)

- **Second Home Visa (Permenkumham 22/2023)** — IDR 2 billion deposit (refundable on visa exit) qualifies for 5-year residence, renewable; a property route is reported by secondary sources but its qualifying value is contested (IDR 2B-equivalent vs IDR 5B vs ~USD 1M) — verify at Imigrasi before relying on property as the qualifying asset.
- **PPh Final UMKM 0.5 %** (PP 55/2022) — small-business final tax for Indonesian-resident entrepreneurs with turnover < IDR 4.8 billion/yr; PT PMA does NOT qualify (uses 22 % corporate tax).
- **Tax holiday / tax allowance (BKPM)** — for pioneer industries via PT PMA in priority sectors (manufacturing, infrastructure, digital economy); residential property generally NOT a priority sector. `https://www.bkpm.go.id/`
- **IKN Nusantara incentives** — PP 12/2023 and Perpres 78/2023 provide tax holiday + import duty exemption + preferential land lease for investments in the new capital city (Kalimantan Timur). Real-estate development incentives are still being defined.
- **Rumah subsidi / FLPP** (subsidised first home) — applies only to Indonesian citizens for affordable housing (price cap by region); not relevant to foreigners.
- **EV charger / solar PV** — small VAT incentives for residential renewable installations under Permenkeu schemes; verify current rates.

---

## Common listing platforms

- **Rumah123** — `https://www.rumah123.com/` — largest Indonesian-language platform
- **Lamudi Indonesia** — `https://www.lamudi.co.id/`
- **OLX Indonesia (Properti)** — `https://www.olx.co.id/properti_c5158`
- **PropertyGuru Indonesia** — `https://www.propertyguru.co.id/` ❌ DEPRECATED — link dead (verified 2026-06-13); verify with a current Indonesia portal (PropertyGuru/Rumah.com ceased Dec 2023) — English-friendly, foreign-buyer caveat: many listings are by Indonesian agents marketing to foreigners, verify SHMRS / Hak Pakai eligibility before deposit
- **99.co Indonesia** — `https://www.99.co/id/`
- **Rumah.com** — `https://www.rumah.com/`
- **Bali foreign-buyer platforms** — `https://www.balirealty.com/`, `https://www.harcourtspurba.com/`, `https://www.exoticbali.com/`, `https://www.theagency-bali.com/` ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row, `https://www.ppbali.com/` — heavily marketed to foreign buyers in USD/AUD; verify legal structure independently; many "freehold villa" listings are technically leasehold or PT-PMA-held HGB

---

## Caveats unique to ID

- **Foreign Hak Milik prohibition is strict and unmoving** — UUPA §21 has stood since 1960; the only direct paths are Hak Pakai and SHMRS (condo) for holders of a dokumen keimigrasian (PP 18/2021 Pasal 69(1)), Hak Sewa (lease), or PT PMA holding HGB.
- **Nominee Hak Milik structures are illegal and void by statute** — UUPA §26(2) makes the transfer void by operation of law, the land falls to the State and payments received cannot be reclaimed (no "Bali Provincial Court" exists; 2023–2025 case counts unverified). Do NOT consider this path.
- **Bali-specific traps**: tanah ayahan desa (village allotment) cannot be sold to foreigners; subak irrigation rights affect rural plots; provincial spatial plan (RTRW Bali) updated 2023–2025 with construction moratoria in some Canggu / Seminyak zones; banjar (village council) approval may be required.
- **Pre-construction off-plan risk**: multiple Bali developer defaults 2023–2025; deposits often not in genuine escrow despite contract claims. Pay only against milestone completion verified by independent surveyor.
- **PPN 11 % effective (12 % luxury-only ≥ IDR 30 bn per PMK 131/2024)** on new properties from PKP-registered developers — adds materially to all-in cost for new builds.
- **BPHTB 5 % statutory ceiling** + PPh Final 2.5 % seller-side make total transaction cost meaningfully higher than Thailand or Czech.
- **Foreign Quota / SHMRS verification non-negotiable for condos** — confirm in writing from developer + verify project pertelaan + IMB/PBG before deposit.
- **Hak Sewa "30 + 30" leases** — only the first term is enforceable as a registered right; renewals are contractual options weakened against successor landowners.
- **STR (villa rental) in Bali requires TDUP / Pondok Wisata licence** — Badung / Gianyar enforcement intensified 2023–2025; unlicensed operation = closure orders + back-tax assessment. PT PMA + TDUP + IMB/PBG aligned for commercial use is the only clean path.
- **Pajak Hotel 10 %** regional tax on STR revenue — separate from PPh; Badung Bapenda actively audits villa booking records.
- **All sertifikat and AJB are in Bahasa Indonesia** — sworn translation + Indonesian-licensed PPAT mandatory for foreign buyers; do not skip.
- **Jakarta subsidence + sea-level rise** = compound flood-risk for north Jakarta; capital relocation to IKN Nusantara underway 2024–2030.
- **Immigration-document dependence** — PP 18/2021 Pasal 69(1) conditions foreign housing ownership on holding a dokumen keimigrasian (visa, passport or stay permit per the Penjelasan); separately, PP 18/2021 Pasal 50 obliges a Hak Pakai holder who no longer meets the Pasal 49 conditions to release or transfer the right within 1 year, failing which it is extinguished by law (hapus karena hukum), and Pasal 1 angka 14 defines Orang Asing as a non-citizen whose presence benefits, does business, works or invests in Indonesia — whether a lapsed stay permit alone triggers Pasal 50 is not stated in the PP; verify at the Kantor Pertanahan.
- **Inheritance disposal rule** — foreign inheritor of Indonesian land must dispose within 1 year (UUPA §21(3)).

---

## Reddit / forum sources

- **r/indonesia** — active Indonesian general
- **r/bali** — Bali-specific, mixed locals + expats
- **r/jakarta** — Jakarta general
- **r/IndonesiaProperty** — small but active for property questions
- **Bali Expat Forum** (various Facebook groups: "Canggu Community", "Living in Bali", "Bali Expats")
- **Bali Pod / Bali Living** — informal expat property-discussion threads
- **Indonesia Expat magazine forums**: `https://indonesiaexpat.id/`
- **The Bali Sun** (news + property): `https://thebalisun.com/`
- ⚠️ Forum-quality caveat: Bali expat forums contain many anecdotes about "my friend bought via nominee and it was fine for years" — but the exposure is statutory: UUPA §26(2) makes a nominee transfer void by operation of law and the land falls to the State, however long a structure has gone unchallenged (2023–2025 court-voidance precedents are unverified); treat "it was fine for years" threads as anecdote, not evidence of safety.

---

## Verification authorities

| Authority | When to call | Contact |
|---|---|---|
| **BPN — Kantor Pertanahan kabupaten/kota** | Sertifikat verification (cek sertifikat), encumbrance search, conversion HM → HP | Search by kabupaten at `https://www.atrbpn.go.id/` |
| **Kementerian ATR/BPN** | National land law, PP 18/2021 | `https://www.atrbpn.go.id/` |
| **PPAT (Pejabat Pembuat Akta Tanah)** | AJB drafting, BPN registration, conversion | Verify via Ikatan PPAT regional |
| **Notaris (Notary)** | PPJB, kuasa, PT PMA setup | Verify via Ikatan Notaris Indonesia (INI) |
| **DJP (Direktorat Jenderal Pajak)** | National tax (PPh, PPN) | `https://www.pajak.go.id/` |
| **Bapenda kabupaten/kota** | PBB-P2, BPHTB, NJOP lookup | Per region |
| **Imigrasi** | Visa, KITAS, KITAP, Second Home Visa | `https://www.imigrasi.go.id/` and `https://evisa.imigrasi.go.id/` |
| **OSS (Online Single Submission)** | PT PMA business licence, KBLI, RPTKA work permit | `https://oss.go.id/` |
| **BKPM (Badan Koordinasi Penanaman Modal) / Kementerian Investasi** | PT PMA setup, BoI promotions, LKPM | `https://www.bkpm.go.id/` |
| **Bank Indonesia** | FX rules, capital flow reporting | `https://www.bi.go.id/` |
| **OJK (Otoritas Jasa Keuangan)** | Mortgage / KPR rules (limited for foreigners) | `https://www.ojk.go.id/` |
| **DPMPTSP kabupaten** | IMB / PBG, SLF, TDUP villa rental licence | Per kabupaten |
| **DLH (Dinas Lingkungan Hidup) provincial / kabupaten** | IPAL compliance, environmental clearance | Per province |
| **Bali — Dinas PUPRKIM / Bappeda Bali** | RTRW Bali 2023–2043, RDTR, foreign-investment zoning | `https://tarubali.baliprov.go.id` |
| **Bali — Banjar / Desa Pakraman** | Village adat approval (especially rural / inherited land) | Per banjar |
| **BNPB / BMKG / PVMBG** | Disaster, weather, volcanic monitoring | `https://www.bnpb.go.id/`, `https://www.bmkg.go.id/`, `https://magma.esdm.go.id/` |

---

## Quirks to know

- **Hak Milik vs Hak Pakai vs HGB vs SHMRS**: never accept Hak Milik in your name as a foreigner — it will be voided. Hak Pakai for landed; SHMRS for condo; HGB only via PT PMA. Hak Sewa (lease) is contractual not a real right unless registered.
- **Sertifikat upgrade chain**: rural plots may be on Girik / Letter C / Petok D — these are pre-1960 informal proofs of possession, NOT title deeds. Must be upgraded to sertifikat at BPN before any foreign-relevant transaction; upgrade can take 6–18 months and may surface adat / customary claims.
- **AJB vs PPJB**: AJB (Akta Jual Beli) = the final notarial deed of sale signed at PPAT, transferring title at BPN. PPJB (Perjanjian Pengikatan Jual Beli) = the binding pre-sale agreement (commonly used for off-plan and for resale where seller documents not yet ready); does NOT transfer title — only obliges parties to complete AJB later. Many foreign buyers mistake PPJB for full title transfer; it is not.
- **PPAT scope**: PPAT is a notary specifically authorised to draft AJB and submit it to BPN for registration; not all notaris are PPAT. Verify the practitioner has both designations for property work.
- **Pertelaan + IMB/PBG + SLF (condo)**: pertelaan = the developer's subdivision plan approved by mayor/regent; IMB or PBG = building permit; SLF = certificate of fitness for use. All three must be in order for a condo to be foreign-eligible. Many "pre-launch" Bali condotels lack pertelaan — do NOT pay deposit.
- **Subak (Bali)**: UNESCO-recognised water cooperative system; subak land has water-allocation rights tied to the parcel and converting subak rice fields to villa pads requires subak collective consent + provincial spatial plan amendment + BPN reclassification. Skip these steps and your villa may be ordered demolished.
- **Tanah ayahan desa (Bali)**: village allotment; even if titled in an Indonesian individual's name, the desa adat retains a traditional interest. Foreign sale typically prohibited.
- **Banjar / desa pakraman approval**: in many Bali villages, the village council can refuse foreign occupancy/development even if BPN sertifikat is in order. Practice varies by banjar; Ubud / Tegallalang / Sidemen more conservative; Canggu / Seminyak more permissive.
- **NJOP under-pricing trap**: NJOP is often set ~30–60 % below market (est.; verify per-zone via local Bapenda); buyers under-declaring in the AJB to reduce BPHTB face audit risk and possible criminal sanction (DJP audit + back-tax + fine).
- **PT PMA used as residential proxy**: tax authority and BKPM scrutiny rising 2024–2025 for PT PMA companies that hold villas without genuine operating business — risk of being treated as nominee structure.
- **KITAS dependent ownership**: if you hold Hak Pakai while on KITAS, PP 18/2021 Pasal 50 gives a Hak Pakai holder who no longer meets Pasal 49 one year to release or transfer the right before it is extinguished by law; whether a lapsed KITAS alone triggers it is not stated in the PP — ensure visa continuity and confirm at the Kantor Pertanahan.
- **Off-plan escrow**: Indonesian "escrow" is often informal — funds may sit in developer's operating account, not a third-party trust. Insist on bank-administered escrow with clear release milestones; if developer refuses, walk away.

---

## Source URL templates

| Source | URL pattern |
|---|---|
| Kementerian ATR/BPN main | `https://www.atrbpn.go.id/` |
| BHUMI ATR/BPN (parcel lookup; ex-Sentuh Tanahku web) | `https://bhumi.atrbpn.go.id/` |
| BHUMI ATR/BPN (spatial viewer) | `https://bhumi.atrbpn.go.id/` |
| Peraturan BPK (statute database) | `https://peraturan.bpk.go.id/` |
| UUPA No. 5/1960 | `https://peraturan.bpk.go.id/Details/51078/uu-no-5-tahun-1960` |
| PP 18/2021 (foreign Hak Pakai) | `https://peraturan.bpk.go.id/Details/161834/pp-no-18-tahun-2021` |
| UU HKPD No. 1/2022 (local taxes) | `https://peraturan.bpk.go.id/Details/195696/uu-no-1-tahun-2022` |
| Putusan Mahkamah Agung (case search) | `https://putusan3.mahkamahagung.go.id/` |
| Imigrasi main | `https://www.imigrasi.go.id/` |
| Imigrasi e-Visa | `https://evisa.imigrasi.go.id/` |
| OSS-RBA (business + work permit) | `https://oss.go.id/` |
| BKPM / Kementerian Investasi | `https://www.bkpm.go.id/` |
| DJP (Tax Authority) | `https://www.pajak.go.id/` |
| OJK (Financial Services) | `https://www.ojk.go.id/` |
| Bank Indonesia | `https://www.bi.go.id/` |
| BPS (Statistics) | `https://www.bps.go.id/` |
| Pos Indonesia (postcodes) | `https://www.posindonesia.co.id/` |
| Bapenda DKI Jakarta | `https://bapenda.jakarta.go.id/` |
| Bapenda Badung (Bali) | `https://bapenda.badungkab.go.id/` |
| BNPB (Disaster) | `https://www.bnpb.go.id/` |
| InaRISK BNPB | `https://inarisk.bnpb.go.id/` |
| BMKG (Meteorology / Earthquake) | `https://www.bmkg.go.id/` |
| InaTEWS Tsunami | `https://inatews.bmkg.go.id/` |
| MAGMA Indonesia (Volcanology) | `https://magma.esdm.go.id/` |
| Kementerian PUPR (Public Works) | `https://www.pu.go.id/` |
| Bina Marga (Highways) | `https://binamarga.pu.go.id/` |
| Jasa Marga (Tollways) | `https://www.jasamarga.com/` |
| Kementerian Lingkungan Hidup (KLH) / BPLH | `https://www.kemenlh.go.id/` |
| ISPU (Air Quality Index) | `https://ispu.kemenlh.go.id` |
| Dinas PUPRKIM Provinsi Bali (Spatial Plan, ex-Distarcip) | `https://tarubali.baliprov.go.id` |
| PAM Jaya (Jakarta water) | `https://pamjaya.co.id/` |
| PD PAL Jaya (Jakarta sewerage) | (verify current site at PUPR Jakarta) |
| PDAM Tirta Mangutama (Badung Bali) | `https://tirtamangutama.badungkab.go.id/` |
| Kementerian Ketenagakerjaan | `https://kemnaker.go.id/` |
| Korlantas POLRI (traffic) | `https://korlantas.polri.go.id/` |
| Rumah123 | `https://www.rumah123.com/` |
| Lamudi Indonesia | `https://www.lamudi.co.id/` |
| OLX Indonesia Properti | `https://www.olx.co.id/properti_c5158` |
| PropertyGuru Indonesia | `https://www.propertyguru.co.id/` ❌ DEPRECATED — link dead (verified 2026-06-13); verify with a current Indonesia portal (PropertyGuru/Rumah.com ceased Dec 2023) |
| 99.co Indonesia | `https://www.99.co/id/` |

---

## Status

✅ **Fully populated** as of 2026-05-01.

**Coverage check**: foreign-buyer eligibility (LEAD), price, traffic, tax, rental, work, risks, mains all sourced to primary government / regulated entity URLs + cost benchmarks + caveats.

**Confidence**:
- **HIGH** — foreign-ownership rules (UUPA §21, §26(2), §41; PP 18/2021), Hak Pakai term and conversion mechanics, SHMRS condo eligibility, Second Home Visa IDR 2B deposit (Permenkumham 22/2023; the property-route value is MEDIUM at best — contested in secondary sources, verify at Imigrasi), BPHTB 5 % ceiling and PPh Final 2.5 % framework, BNPB / BMKG / PVMBG hazard sources, nominee voidance risk (statutory, UUPA §26(2); 2023–2025 court-precedent counts unverified — Direktori Putusan not machine-readable).
- **MEDIUM** — current 2026 effective Permen ATR/BPN price floors per province (verify each Permen before quoting), kabupaten-level BPHTB rate within statutory ceiling, NJOP zonal updates (Bali rising 2024–2026), villa STR enforcement intensity (Bali Badung most active), Bali RTRW spatial plan moratoria (revised 2023–2025), salary benchmarks (UMP/UMK SK Gubernur annual).
- **LOW** for none — every section has primary sources.

**Reform watch items** (track in `shared/regulatory-watch.md`):
1. **PP 18/2021 / Hak Pakai term extensions** — discussion of further extension beyond 80 yr; not enacted May 2026.
2. **Bali "special-zone" foreign-ownership pilot** — provincial proposal floated; no national legislation enacted.
3. **PPN structure** — effectively 11 % via the DPP 11/12 tax-base mechanism; 12 % applies luxury-only (≥ IDR 30 billion) under PMK 131/2024. Monitor for any move to apply 12 % broadly; verify current rate at DJP.
4. **NJOP zonal updates Bali** — Badung / Gianyar revising upward 2024–2026; verify Perda.
5. **Villa STR / TDUP enforcement framework** — Bali Badung tightening 2023–2025; verify current Perda.
6. **Digital Nomad Visa E33G evolution** — launched 2024; ongoing DJP guidance on foreign-source income remittance.
7. **IKN Nusantara real-estate incentives** — Perpres 78/2023 schedule still being implemented through 2030.

**Last verified**: 2026-05-27 (validation sweep — PPN 12% luxury-only ≥IDR 30bn (PMK 131/2024); Bali Perda 4/2026 nominee-facilitation ban signed 24 Feb 2026, sanctions administrative — corrected 2026-09-24 against the signed text; transport, Bali spatial-planning, environment-ministry and parcel-lookup authorities corrected 2026-09-18 per ditjenintram.kemenhub.go.id + dispuprkim.baliprov.go.id + kemenlh.go.id + bhumi.atrbpn.go.id). Second Home Visa property-route claim downgraded 2026-09-24 in the October regwatch wave (secondary sources conflict; no primary text read). 2026-09-24: Bali Perda 4/2026 re-read in its signed JDIH Provinsi Bali text (Pasal 1 angka 11 and Pasal 13, 14, 20, 26) and UU 41/2009 Pasal 72(1) — nominee facilitation carries administrative sanctions (Pasal 20(5) only defers to other legislation for criminal sanctions); the OTA NIB timeline was re-checked against Kemenpar's API release (June 2027) with the 1 Aug 2026 delisting date from ANTARA/Kontan (secondary); Pondok Wisata nationality bar and PT PMA/KBLI 55193 eligibility not re-verified (November regwatch wave, run early). Foreign-buyer / rental tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).
