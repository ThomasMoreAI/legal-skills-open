# Türkiye 🇹🇷 — Property Due-Diligence Playbook

ISO2: `tr`. Status: ✅ Fully populated (researched 2026-05).

## Country profile

- **Posta kodu (postcode)**: 5 digits, no internal space (e.g., `34000` İstanbul, `06000` Ankara, `35000` İzmir, `07000` Antalya)
  - First 2 digits: il (province) plaka kodu (matches license-plate code 01–81)
  - Last 3 digits: ilçe + mahalle cluster
- **Admin levels**: 81 il (province) → 973 ilçe (district) → ~32,000 mahalle/köy (neighbourhood/village). 30 of the 81 are **Büyükşehir Belediyesi** (metropolitan municipality).
- **Currency**: TRY (Türk lirası). **Foreign-buyer transactions widely quoted in USD or EUR** because of TRY hyperinflation (CPI hit 85.51 % YoY Oct 2022, re-peaked ~75 % YoY May 2024, ~44 % by end-2024, low-30s by late 2025, ~32.6 % YoY May 2026, **31.51 % YoY Aug 2026** per TÜİK (2026 data, quoted in TCMB PPK summary 2026-42) — the June-2026 rent-cap 12-month-average TÜFE ceiling of 32.24 % corroborates; CBRT one-week repo rate peaked 50 % Mar 2024, eased through 2025–26 to **37.0 %** — held at the 10 Sep 2026 PPK per TCMB Basın Duyurusu 2026-38 (also held 23 Jul 2026, 2026-28); rates may have changed since — re-check TÜİK monthly). **Verify TRY vs FX pricing on every listing.** (2026-09-24 verified)
- **Languages**: Turkish (official); English usable in tourist zones (İstanbul, Antalya, Bodrum, Alanya, Fethiye); Kurdish substantial in southeast (admin Turkish only).
- **Cadastre**: **TKGM** (Tapu ve Kadastro Genel Müdürlüğü) — title is **`Tapu Senedi`**. Online: `https://www.tkgm.gov.tr/` + **Web Tapu** (e-Devlet integration at `https://webtapu.tkgm.gov.tr/`).
- **Identifier**: `Tapu Senedi` carries `il / ilçe / mahalle/köy / ada no / parsel no / bağımsız bölüm no` (last for apartments).
- **Major reforms**:
  - **2012**: Tapu Kanunu Article 35 reciprocity expanded — foreigners from ~183 countries permitted (previously narrow reciprocity; "mütekabiliyet" requirement softened to government discretion).
  - **2017**: Citizenship by Investment program created (Cumhurbaşkanlığı Kararı 2017/9601), property route at $1,000,000.
  - **2018**: **TBDY 2018** (Türkiye Bina Deprem Yönetmeliği) — new earthquake-resistant building code, in force **1 Jan 2019**. New AFAD seismic hazard map at `https://tdth.afad.gov.tr/`.
  - **Sept 2018 → Jun 2022**: CBI threshold dropped to $250 k → raised to **$400,000** (current).
  - **Nov 2023 → 1 Jan 2024**: **Law 7464** (Konutların Turizm Amaçlı Kiralanmasına ve Bazı Kanunlarda Değişiklik Yapılmasına Dair Kanun) — mandatory İzin Belgesi for short-term rentals.
  - **Feb 2023**: Kahramanmaraş twin earthquakes, 6 Feb 2023 — **AFAD official magnitudes Mw 7.7** (Pazarcık, 04:17 TSİ) + **Mw 7.6** (Elbistan, 13:24 TSİ); USGS catalogues the same pair as Mw 7.8 + Mw 7.5, but AFAD is the only body legally authorised to publish Türkiye earthquake magnitudes — quote the AFAD pair (2026-08-07 verified). ~50,000 deaths. Triggered regulatory tightening on building inspection, DASK, and "kentsel dönüşüm" (urban transformation) acceleration.

## Section: `--price`

### Primary sources (official)

- **TÜİK Konut Fiyat Endeksi** (House Price Index, monthly — based on appraisal reports, hedonic): `https://data.tuik.gov.tr/Bulten/Index?p=Konut-Fiyat-Endeksi` (verify URL/liveness — this refresh sourced prices from TCMB KFE)
- **TCMB Konut Fiyat Endeksi** (Central Bank, monthly, hedonic; bulletin also carries the **Yeni Kiracı Kira Endeksi** — new-tenant rent index): `https://www.tcmb.gov.tr/wps/wcm/connect/tr/tcmb+tr/main+menu/istatistikler/reel+sektor+istatistikleri/konut+fiyat+endeksi/` (verified live 2026-07-03)
- **TÜİK Konut Satış İstatistikleri** (sales count, monthly): `https://data.tuik.gov.tr/Kategori/GetKategori?p=insaat-ve-konut-116`

### Secondary / private benchmarks

- **REIDIN-GYODER Yeni Konut Fiyat Endeksi** (new-build price index, İstanbul focus): `https://gyoder.org.tr/` (paid pro tier; press releases free)
- **Endeksa** (machine-valuation, neighbourhood granularity): `https://www.endeksa.com/`
- **Hepsiemlak Konut Fiyat Endeksi** + **Sahibinden + Bahçeşehir Üniversitesi Endeksi**

### Listing platforms

- **sahibinden.com** — largest by far (≈ 65 % share of TR online property listings): `https://www.sahibinden.com/satilik/<il>-<ilce>` or `/kiralik/`
- **hepsiemlak.com** — full-broker: `https://www.hepsiemlak.com/<il>-<ilce>-satilik`
- **emlakjet.com**, **zingat.com**, **hurriyetemlak.com**

### Price benchmarks (Q4 2025 reference, TÜİK + Globalpropertyguide aggregations)

| Region / city | TRY/m² (Q4 2025 avg) | USD/m² (≈) | YoY change |
|---|---:|---:|---:|
| **Türkiye geneli** | ~45,447 | $973 | +26.0 % |
| **İstanbul** | ~74,101 | $1,587 | +24.5 % |
| **Ankara** | data not publicly available — verify TÜİK monthly bulletin | est. $850–$1,100 | +38.7 % |
| **İzmir** | data not publicly available — verify TÜİK monthly bulletin | est. $1,000–$1,400 | mid-20s % |
| **Antalya / Muğla coast** | est. mid-tier with foreign-buyer premium | est. $1,200–$2,000 | mid-20s % |

(Q4 2025 reference levels, source TÜİK KFE + GlobalPropertyGuide; the two index-row USD figures re-anchored at ~46.7 TRY/USD, 2026-07-02 rate — TRY/m² levels are inflation-eroded; est ranges are judgment bands; rates may have changed since — re-pull TCMB KFE monthly)

**By August 2026** (TCMB RPPI Aug-2026 bulletin, primary) nominal YoY had eased to **+23.0 % nationally** (İstanbul +26.3 %, Ankara +24.8 %, İzmir +23.3 %), but **real YoY was −6.5 %** (May 2026: +24.5 % nominal / −6.1 % real) — Turkish housing is rising in TRY yet losing value against inflation. Re-pull TCMB KFE monthly; cross-check TÜİK KFE. (2026-09-24 verified, TCMB RPPI Aug 2026)

### İstanbul district hierarchy (foreign-buyer relevant; verify per-district at sahibinden cenova haritası)

- **Premium**: Beşiktaş, Beyoğlu (Cihangir, Galata), Kadıköy, Üsküdar, Sarıyer, Bebek, Etiler — **est. $2,500–$5,000+/m²** for renovated or new
- **Mid (popular foreign buyer)**: Şişli, Kağıthane, Maltepe, Ataşehir — **est. $1,200–$2,500/m²**
- **Mid-affordable**: Esenyurt, Beylikdüzü, Başakşehir (heavy CBI inventory) — **est. $700–$1,500/m²**
- **Outer**: Pendik, Tuzla, Sultangazi, Esenler — **est. $500–$1,000/m²**

### Compute

1. Listing price/m² = listing price ÷ `brüt m²` (gross — includes wall thickness, common areas) OR `net m²` (interior only). **Clarify which on every listing — gap is typically 15–25 %**.
2. Compare to TÜİK KFE for the il (province-level only — not parcel-specific).
3. Compare to Endeksa neighbourhood machine-valuation (mahalle-level granularity).
4. **Trap**: `0+1` = studio (no separate bedroom), `1+1` = one bed, `2+1` = two bed + lounge, `3+1` etc. — Turkish convention.
5. **Trap**: TRY vs USD/EUR — many İstanbul/Antalya listings quote in **USD** even when only TRY is legally tender. Verify the deed (`Tapu Senedi`) declared value vs informal price.
6. **Trap**: KDV inclusive vs exclusive on yeni proje (newbuilds) — `KDV dahil` (VAT incl.) vs `KDV hariç` (VAT excl.); see § Tax for rate tiers.
7. **Trap**: "Kat irtifakı" (pre-occupancy title) vs "kat mülkiyeti" (post-occupancy/iskan complete) — pre-occupancy title means the building lacks the final occupancy permit and bank financing may be restricted.

---

## Section: `--traffic`

### Primary sources

- **KGM (Karayolları Genel Müdürlüğü) Trafik ve Ulaşım Bilgileri**: `https://www.kgm.gov.tr/Sayfalar/KGM/SiteTr/Trafik/TrafikHacimHaritasi.aspx`
  - Annual `Trafik Hacim Haritası` (traffic volume map) — coverage: D + O (otoyol/motorway) network primarily; some state roads
  - Latest published map: 2023 data (rates may have changed since)
- **İBB (İstanbul Büyükşehir Belediyesi) Açık Veri Portalı**: `https://data.ibb.gov.tr/` — İstanbul-only; real-time traffic feeds, bus loads, metro
- **Yandex Traffic / Google Traffic** — only commercial-grade real-time fallback

### Key term

**YOGT (Yıllık Ortalama Günlük Trafik)** — Annual Average Daily Traffic, equivalent to AADT.

### Verdict bands

- 🟢 < 1,500 v/d (rural devlet yolu, köy yolu)
- 🟡 1,500–8,000 v/d (small il/devlet yolu, urban side street)
- 🟠 8,000–30,000 v/d (busy devlet yolu, urban arterial, smaller D-road)
- 🔴 > 30,000 v/d (otoyol, major D-road, urban core, İstanbul boğaz köprüleri)

### Coarse fallback (OSM `highway` class)

- `motorway` = otoyol (O-prefix)
- `trunk`/`primary` = devlet yolu (D-prefix)
- `secondary` = il yolu
- `tertiary` = köy yolu / minor connector
- `residential` = mahalle içi yol

---

## Section: `--tax`

### Annual property tax — Emlak Vergisi (Law 1319)

**Administered by**: belediye (municipality) — not central tax authority.

| Property type | Rate (small belediye) | Rate (Büyükşehir, ×2) |
|---|---:|---:|
| **Residential (mesken/konut)** | **0.1 %** | **0.2 %** |
| **Commercial (işyeri)** | 0.2 % | 0.4 % |
| **Land with construction permit (arsa)** | 0.3 % | 0.6 % |
| **Agricultural land (arazi)** | 0.1 % | 0.2 % |

(source GİB Emlak Vergisi Kanunu mad. 8; rates confirmed **unchanged for 2026** — Büyükşehir ×2 also unchanged; only the base values were re-set, see below. 2026-07-03 verified)

**Büyükşehir multiplier**: rates are **doubled** within boundaries of the 30 metropolitan municipalities (İstanbul, Ankara, İzmir, Antalya, Bursa, Konya, Adana, Gaziantep, Kayseri, Şanlıurfa, Diyarbakır, Mersin, Eskişehir, Hatay, Manisa, Kahramanmaraş, Samsun, Aydın, Balıkesir, Denizli, Erzurum, Kocaeli, Malatya, Mardin, Muğla, Ordu, Sakarya, Tekirdağ, Trabzon, Van).

### Base value: Emlak Vergisi Değeri

Property tax base = **rayiç bedel** (declared/appraised value) updated every 4 years by belediye + annual yeniden değerleme oranı (revaluation coefficient, set by Hazine ve Maliye Bakanlığı per Resmi Gazete).

- Latest 4-year valuation cycle: **2026–2029**. 2026 increases are now **capped by statute** — Law 7566 (RG 2025-12-19 No. 33112) added **geçici mad. 23** to the Emlak Vergisi Kanunu: 2026 emlak vergisi değeri = 2025 değeri × **1.12745** (+12.745 %, half the 25.49 % revaluation), and any 2026 value computed from the new takdir-komisyonu arsa/arazi birim değerleri **may not exceed 2× the 2025 vergi değeri** (implemented by Emlak Vergisi Genel Tebliğ Seri No 89, RG 2025-12-31 No. 33124 5. mükerrer). 2027–2029 matrahs chain off these capped 2026 values. Note: Law 7566 md 11 also raises the annual uplift in non-takdir years from half to the **full** yeniden değerleme oranı going forward (verify effective year in the law text). Payment: 1st taksit by 31 May, 2nd by 30 Nov. Rates unchanged (see table above). (2026-07-03 verified)
- Annual yeniden değerleme oranı 2025: **43.93 %** (RG 2024-12-30)
- Annual yeniden değerleme oranı 2026: **25.49 %** (RG 2025-12-31, No. 33124 5. mükerrer)

### Example calculation

100 m² konut, rayiç bedel 4,000,000 TRY, in **İstanbul (Büyükşehir)**:
- Annual Emlak Vergisi = 4,000,000 × 0.002 = **8,000 TRY/yr** (~$171 at 1 USD ≈ 46.7 TRY, 2026-07 rate)

100 m² konut in **Bartın (small belediye, not Büyükşehir)**, rayiç 1,500,000 TRY:
- Annual Emlak Vergisi = 1,500,000 × 0.001 = **1,500 TRY/yr** (~$32 at ~46.7 TRY/USD, 2026-07 rate)

### Çevre Temizlik Vergisi (Environmental Cleaning / sanitation fee)

- Residential: **flat fee** by water consumption brand (collected via su faturası — water bill); typically 50–500 TRY/yr per household
- Commercial: progressive by m² + activity tier

### High-Value Residential Tax — Değerli Konut Vergisi (since 2020)

For residences with rayiç bedel > **15,709,000 TRY (2025 threshold per GİB Genel Tebliğ Seri No 86)** / **17,711,000 TRY (2026 threshold per GİB rehberi)** (2026-05-27 verified, source [GİB 2026 Değerli Konut Vergisi Rehberi PDF](https://cdn.gib.gov.tr/api/gibportal-file/file/getFile?objectKey=DUYURU/UNIVERSAL/2026/2026_Degerli_Konut_Vergisi_Rehberi.pdf)):

| Bracket 2026 (TRY rayiç bedel) | Rate |
|---|---:|
| 17,711,000 – 26,567,000 | 3.35 ‰ (0.335 %) on excess |
| 26,567,000 – 35,425,000 | 6.3 ‰ (0.63 %) on excess (+ tier above) |
| > 35,425,000 | 10 ‰ (1.0 %) on excess (+ tiers above) |

(2026 thresholds + rates per GİB Genel Tebliğ Seri No 88 / Emlak Vergisi Kanunu mad. 42; brackets revalued annually by yeniden değerleme oranı; rates expressed in per-mille ‰ in the official tebliğ)

### Transaction tax — Tapu Harcı (Title Deed Transfer Fee)

- **Total: 4 % of declared sale value** (Tapu Harçları Kanunu Ek Tarifesi 4.a)
- Statutory split: **2 % buyer + 2 % seller**; in practice, **buyer often pays full 4 %** (negotiable)
- Calculated on declared sale value (must be ≥ rayiç bedel — under-declaration triggers GİB audit + ceza)
- Paid at TKGM Tapu Müdürlüğü on transfer day

### KDV (VAT) on residential sales

For NEW property sold by developer (yapı müteahhidi):

| Property net m² + class | KDV rate |
|---|---:|
| Net ≤ 150 m², "lüks olmayan" (non-luxury) in low/mid-cost city | **1 %** |
| Net ≤ 150 m², standard in metropolitan areas | **10 %** |
| Net > 150 m² OR "lüks" classification (per arsa birim m² value tier) | **20 %** |

(2026 rates, source KDV Kanunu mad. 28 + BKK 2007/13033 + 7491 KDV reform Dec 2023; tier definitions revised — verify with developer's current `KDV oranı` declaration)

**Resale (ikinci el)**: generally KDV exempt unless seller is a registered KDV mükellefi.

### KDV exemption for foreign first-time buyers (KDV Kanunu mad. 13/i)

Conditions (cumulative):
1. Buyer is **non-Turkish citizen + non-resident in Türkiye** (≥6 months physical absence) — or Turkish citizen with valid yabancı oturma izni in another country and >6 months abroad
2. Property is **first sale** (ilk teslim) — direct from developer or from Turkish citizen who acquired ≥3 years earlier
3. Property purchase **paid in foreign currency, transferred from abroad** to Turkish bank account (proof: dekont)
4. Property is **konut (residential) or işyeri (commercial)** — not arsa (land)
5. **Holding period: minimum 3 years** from acquisition (was 1 year pre-2023; raised by Law 7456 of Jul 2023). Early sale triggers retroactive KDV + ceza + faiz.

Result: KDV **0 %** on qualifying purchase (saves up to 20 % on luxury new build).

### Capital gains tax (Değer Artış Kazancı)

- Residential property held **> 5 years**: **EXEMPT** (Gelir Vergisi Kanunu mük. mad. 80)
- Held ≤ 5 years: gain (sale − indexed acquisition cost − allowable expenses) added to other income; progressive **15–40 %** brackets (2026 non-wage: 15 % to 190k, 20 % to 400k, 27 % to 1M, 35 % to 5.3M, 40 % above — wage-income bands differ, 27 % band runs to 1.5M; GİB Gelir Vergisi Genel Tebliği Seri No 332)
- Annual istisna for capital gains (other-income): **150,000 TRY (2026)** (was 120,000 in 2025; GİB Tebliğ Seri No 332) — applies to non-residential gains primarily. (2026-07-03 verified)

### Inheritance + gift tax — Veraset ve İntikal Vergisi

- Inheritance progressive **1–10 %**; gift progressive **10–30 %** (Veraset ve İntikal Vergisi Kanunu)
- Spouse + children istisna: **2,907,136 TL per heir (2026)**; spouse alone, no descendants: **5,817,845 TL (2026)** (Veraset ve İntikal VK Genel Tebliği Seri No 57, RG 2025-12-31 No. 33124 5. mükerrer). Note: 2025 was 2,316,628 TL; the 1,609,552 TL previously shown here as "2025" was the 2024 figure. (2026-07-03 verified)

### Future risk

- **2026–2029 rayiç bedel cycle**: Law 7566 (geçici mad. 23) now caps 2026 increases **statutorily** — 2025 değer × 1.12745, and the matrah may not exceed 2× the 2025 vergi değeri (see § base value) — superseding the earlier case-by-case Anayasa Mahkemesi capping. Watch for challenges to the FULL-rate uplift that md 11 introduces for non-takdir years. Source: Resmi Gazete + belediye ilan/notification. (2026-07-03 verified)
- **KDV on housing** under continual reform pressure (especially the 1 % small-unit rate); verify Resmi Gazete + Hazine Bakanlığı bulletin annually.
- **Değerli Konut Vergisi** brackets revalued annually — luxury İstanbul buyers should track.

---

## Section: `--rental`

### Long-term residential — Gayrimenkul Sermaye İradı (GMSİ)

Gelir Vergisi Kanunu §70–74. Tax declared via annual Gelir Vergisi Beyannamesi (March).

#### Residential rental istisna (exemption) — 2026

- **58,000 TRY/yr** (mesken kira geliri istisnası, 2026; was 47,000 in 2025, 33,000 in 2024 — revalued annually by yeniden değerleme oranı)
- Applies once across all residential properties combined
- **Lost** if: (a) total income from all sources exceeds the high-bracket threshold, or (b) rental income not declared by deadline

(2026 threshold per GİB Gelir Vergisi Genel Tebliği Seri No 332, RG 2025-12-31 No. 33124 5. mükerrer; verify GİB annual update. 2026-07-03 verified)

#### Rent-increase cap (Türk Borçlar Kanunu mad. 344)

- Annual rent increases on existing residential leases are capped at the **12-month-average TÜFE** (CPI). The temporary 25 % ceiling (in force 2022 → 30 Jun 2024) **expired 1 Jul 2024**; the cap reverted to the TBK mad. 344 12-month-average TÜFE ceiling.
- **June 2026 legal ceiling: 32.24 %** (TÜİK 12-month-average TÜFE) — the applicable ceiling resets monthly; verify the renewal month's TÜFE 12-month average. (2026-07-03 verified)

#### Cost methods (must be uniform across all GMSİ)

- **Götürü Gider** (lump-sum): **15 % flat deduction** of gross — no documentation needed; simplest for non-resident foreigners. **Cannot revert to gerçek for 2 years once selected.**
- **Gerçek Usul** (actual): document all expenses (loan interest, insurance, repair amortization, depreciation, management fees) — better for high-cost properties

#### Rates — 2026 income brackets (non-wage / GMSİ)

| ZD bracket (TRY) | Rate |
|---|---:|
| 0 – 190,000 | 15 % |
| 190,001 – 400,000 | 20 % |
| 400,001 – 1,000,000 | 27 % |
| 1,000,001 – 5,300,000 | 35 % |
| > 5,300,000 | 40 % |

(2026 non-wage/GMSİ brackets per GİB Gelir Vergisi Genel Tebliği Seri No 332; revalued annually by yeniden değerleme oranı. **Wage-income upper bands differ** — the 27 % band runs to 1,500,000 and the 35 % band 1,500,000–5,300,000. 2026-07-03 verified)

#### Non-resident foreign owner

- Same GMSİ regime
- Beyanname filed via **Hazır Beyan Sistemi** at `https://hazirbeyan.gib.gov.tr/`
- No social security contribution on GMSİ (unlike Bağ-Kur for OSVÇ-equivalent)

### Short-term rentals (gunluk konut kiralama / Airbnb / Booking)

**Status as of 2026: heavily regulated. Law 7464 enforcement now mature.**

#### Law 7464 (Konutların Turizm Amaçlı Kiralanmasına Dair Kanun)

- Published Resmi Gazete **2 Nov 2023**, effective **1 Jan 2024**: `https://www.resmigazete.gov.tr/eskiler/2023/11/20231102-1.htm`
- Implementing regulation (Yönetmelik): RG 28 Dec 2023
- **Definition**: konut kiralama for ≤ 100 nights consecutively to same tenant for tourism purposes
- **Mandatory İzin Belgesi** (Turizm Amaçlı Kiralanan Konut İzin Belgesi) issued by **Kültür ve Turizm Bakanlığı** via e-Devlet
- Application portal: `https://www.ktb.gov.tr/` + e-Devlet integration

#### Conditions for İzin Belgesi

1. Building "kat malikleri kurulu" (apartment owners' assembly) **unanimous consent** in writing — single objection blocks the permit
2. Maximum **25 % of units** in any one apartment block can be turism amaçlı (some local exemptions for blocks built after 2023 designed for it)
3. Turkish citizen or registered legal entity as license holder (foreign owners use TR-resident company or attorney)
4. Building must have **iskan (Yapı Kullanma İzin Belgesi)** — no permit on kat irtifakı stage

#### Penalties (Law 7464 mad. 5)

| Violation | Fine (TRY) |
|---|---:|
| Operating without İzin Belgesi — **3-stage progressive ladder** (NOT discretionary range) | Statutory base **Stage 1: 100,000 TRY/property + 15-gün süre to obtain permit; Stage 2 (still no permit): 500,000 TRY/property + 15-gün süre; Stage 3 (continued violation): 1,000,000 TRY/property** (2026-05-27 verified, source [Lexpera Law 7464 consolidated text Mad. 4 §1(a-e)](https://www.lexpera.com.tr/mevzuat/kanunlar/konutlarin-turizm-amacli-kiralanmasina-ve-bazi-kanunlarda-degisiklik-yapilmasina-dair-kanun-7464)). **Base fines are revalued annually by yeniden değerleme oranı — 2026 applied amounts are 180,617 / 903,088 / 1,806,177 TRY per property** (uniform ×1.80617 factor; new figures land each January) (2026-07-02 verified, source [KTB Denizli İl Kültür ve Turizm Müdürlüğü 2026 idari para cezaları](https://denizli.ktb.gov.tr/TR-437107/turizm-amacli-kiralanan-konutlara-iliskin-mevzuat-hakki-.html) + Kaymakamlık ceza duyurusu) |
| Misleading property description (konum/nitelik/fiziksel özellikler) | **100,000 TRY** separate |
| Listing on platform without permit | **100,000 per property + access blocking after 24h notice** |
| Provisional permit lapse (post 31 Dec 2024 transition) | sanctions began Jan 2025 |
| Failure to remove unlicensed listing within 24h after Bakanlık notice | platform fine + listing removal |

#### Hosts on platforms (Airbnb, Booking)

- Platforms required to **verify İzin Belgesi number** before listing publishes
- Airbnb + Booking now request permit upload from TR hosts (post-2024); **Airbnb blocks listings lacking the Ministry İzin Belgesi number** (unverified listings cannot accept new bookings)
- Stays > 100 consecutive nights = pansiyon işletmeciliği regime (different licensing — Belediye İşyeri Açma Ruhsatı + Bağ-Kur)

#### Tax regime for short-term rental income

- **If Turkish-tax-resident**: rental income is "ticari kazanç" (commercial earnings) per Danıştay 2024 ruling — NOT GMSİ. Triggers Bağ-Kur (social security) registration; defter tutma; KDV mükellefi if revenue threshold; dafarbey gelir vergisi 15–40 %.
- **Non-resident foreign owner**: still GMSİ-eligible per practice; verify with mali müşavir.
- **Konaklama Vergisi** (accommodation tax, since 1 Jan 2023): **2 %** of accommodation revenue — collected by host, declared monthly to GİB

### Strategic notes

- **İstanbul, Antalya, Bodrum, Kapadokya, Alanya, Fethiye, Çeşme**: highest yields; biggest regulatory + kat malikleri consent challenge
- **Building-level consent is the single hardest gate** — buy in blocks designed/zoned for STR or accept LTR-only
- **Konut Tipi Site / Komplekss with on-site management**: typically pre-arranged consent; ask for "site yönetimi izni" before purchase
- **EU Reg 2024/1028 (STR transparency)**: does NOT apply to TR (non-EU) but may indirectly affect platform behaviour for cross-border bookings

---

## Section: `--work=<profession>`

### Job platforms

- **kariyer.net** — largest, white-collar focus: `https://www.kariyer.net/`
- **secretcv.com**, **eleman.net**, **yenibiriş.com**
- **indeed.com.tr**, **LinkedIn TR** (very active in IT, finance, holdings, big corporates)
- **İŞKUR** (Türkiye İş Kurumu, public employment service): `https://www.iskur.gov.tr/`

### Self-employment regimes

- **Şahıs Şirketi** (sole proprietorship) — simplest, registered at vergi dairesi; basit usul or gerçek usul gelir vergisi
  - Basit usul: cap on revenue (~3.4M TRY 2025); 15 % flat-ish; no defter tutma but yıl sonu defter beyan
  - Gerçek usul: full ledger; brackets 15–40 %
- **Limited Şirket (Ltd. Şti.)** — corporate, 50,000 TRY minimum capital (2025 floor); kurumlar vergisi **25 %** (30 % for finance; revalued); kar dağıtımı stopaj 10 %
- **Anonim Şirket (A.Ş.)** — joint stock, 250,000 TRY minimum; same kurumlar vergisi
- **Bağ-Kur (4-b SGK)** social security: mandatory for self-employed; 2025 monthly minimum ~6,500 TRY contribution

### Salaried benchmarks (2025 brüt avg)

- **Asgari ücret 2026 (minimum wage)**: **33,030.00 TRY/ay brüt** (net ~28,075.50 TRY, günlük brüt 1,101.00 TRY) — **+27 %** vs 2025 (22,104.67 brüt); Asgari Ücret Tespit Komisyonu Kararı, effective 1 Jan 2026 (RG Aralık 2025). 2026-07-03 verified.
- **Median brüt 2025**: data not publicly available — verify TÜİK Hanehalkı İşgücü Anketi
- **İstanbul beyaz yaka median**: est. 50,000–80,000 TRY/ay (mid-career, white-collar sectors)
- **IT/finance senior İstanbul**: est. 100,000–250,000 TRY/ay; FX-indexed comp common

### Foreign worker permit

- **Çalışma İzni** required from **Çalışma ve Sosyal Güvenlik Bakanlığı**
- Online application: `https://ecalismaizni.csgb.gov.tr/`
- Quota: typically 1 foreign worker per 5 TR-citizen workers in same employer
- Independent professional (e.g., remote work for foreign employer): use **kısa dönem ikamet izni** + register as serbest meslek with vergi dairesi

### Catchment heuristics

- Within 60 min of one of 30 Büyükşehir centres: meaningful labour market
- Outside Büyükşehir + > 60 min from major city: thin (tourism, agriculture, public sector dominant)
- **Tier-1 (best foreign-friendly job markets)**: İstanbul, Ankara, İzmir
- **Tier-2 (sectoral)**: Antalya (tourism + tech hub emerging), Bursa (auto), Gaziantep (industry), Mersin (logistics)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **AFAD Türkiye Deprem Tehlike Haritası** | `https://tdth.afad.gov.tr/` | Site-specific PGA, SS, S1, SDS, SD1, PGV per coordinates + soil class (ZA–ZE) |
| **AFAD ana portalı** | `https://www.afad.gov.tr/` + `https://deprem.afad.gov.tr/` | Real-time seismicity, historic catalog, fault maps |
| **MTA Diri Fay Haritası** (active fault map) | `https://www.mta.gov.tr/v3.0/hizmetler/yenilenmis-diri-fay-haritalari` | 1:25k active fault traces |
| **MTA Heyelan Envanteri** (landslide) | `https://www.mta.gov.tr/v3.0/hizmetler/heyelan-envanteri` | Historic landslide registry |
| **DSİ Taşkın Haritaları** (flood) | `https://www.dsi.gov.tr/` | River + flood plain mapping (district/basin level — parcel-level limited) |
| **Çevre Bakanlığı / Atlas** | `https://atlas.gov.tr/` | National geo-portal incl. zoning + protected areas |
| **MGM** (Meteoroloji Genel Müdürlüğü) | `https://www.mgm.gov.tr/` | Climate normals, extreme weather |
| **Tarım ve Orman Bakanlığı orman yangını** | `https://www.ogm.gov.tr/` | Wildfire risk + history |

### Earthquake — the single dominant risk

- **TR is one of the world's most seismically active countries** (North Anatolian + East Anatolian + Aegean fault systems)
- **2023 Kahramanmaraş twin earthquakes, 6 Feb 2023 — AFAD Mw 7.7 (Pazarcık, 04:17 TSİ) + Mw 7.6 (Elbistan, 13:24 TSİ)**: ~50,000 deaths, ~300,000 buildings collapsed/severely damaged — exposed widespread non-compliance with prior building codes. USGS catalogues the same pair as Mw 7.8 + Mw 7.5; AFAD is the only body legally authorised to publish Türkiye earthquake magnitudes, so quote the AFAD pair ([AFAD Kahramanmaraş Depremleri Ön Değerlendirme Raporu](https://deprem.afad.gov.tr/assets/pdf/Kahramanmaras%20%20Depremleri_%20On%20Degerlendirme%20Raporu.pdf), 2026-08-07 verified)
- **AFAD seismic hazard map (2018)** publishes site-specific PGA at `https://tdth.afad.gov.tr/` — input coords + soil class

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1975** | No earthquake-aware code; weak masonry; lead pipes; no insulation; asbestos in roofing common |
| **1975 (DBYBHY-75)** | First nationwide earthquake code — minimal by modern standards |
| **1998 (DBYBHY-98) post-Marmara prep** | Updated post-Erzincan; still inadequate vs Marmara 1999 reality |
| **1999 Marmara M7.6** | ~17,000 deaths — code revised 2007 (DBYBHY-2007) |
| **2007 (DBYBHY-2007)** | Improved but still using 1996 hazard map; widespread non-compliance |
| **2018 (TBDY-2018 — RG 18 Mar 2018 No. 30364 mükerrer, in force 1 Jan 2019)** | Site-specific spectra, modern hazard map, tall-building + base-isolation provisions; **the watershed code** — still the effective baseline, no successor code enacted (re-confirmed on AFAD's own page, 2026-08-07) |
| **Post-2023 Kahramanmaraş** | Yapı denetim tightening, "kentsel dönüşüm" (urban transformation) acceleration via Law 6306 |

**Practical rule**: pre-1999 buildings in seismic zones = high risk unless visibly güçlendirme (retrofit/strengthening) certified; post-2018 buildings designed to TBDY-2018 are substantially safer (subject to actual construction quality — verify yapı denetim raporu).

### Mandatory documents at sale

| Document | Required because | Notes |
|---|---|---|
| **Tapu Senedi (deed)** | Always — TKGM verifies ownership + encumbrances | Web Tapu allows e-verification |
| **DASK Poliçesi (earthquake insurance)** | Mandatory for residential (Zorunlu Deprem Sigortası) — still compulsory, enforced at electricity/water subscription and tapu/konut-kredisi checkpoints (2026-08-07 verified) | See cost block below; 2026 tariff live and ÜFE-indexed monthly |
| **Yapı Kullanma İzin Belgesi (iskan)** | Confirms building completed + permit-compliant | Older buildings may lack — flag |
| **Enerji Kimlik Belgesi (EKB)** | Mandatory at sale + rental since **1 Jan 2020** (was scheduled 2 May 2017, postponed) per Enerji Verimliliği Kanunu | 10-year validity; classes A–G |
| **İmar Durumu Belgesi** | Issued by belediye — confirms zoning + permitted use | Needed if buyer plans extension |
| **Kat Mülkiyeti vs Kat İrtifakı** | Tapu type — see Quirks | Pre-iskan → kat irtifakı |
| **Site/Apartman Aidat Borcu Yoktur Yazısı** | If kat mülkiyetli site/apartman | At signing |

**EKB penalty**: sale/rental forbidden without EKB since 1 Jan 2020 — but enforcement varies; buyer should insist.

### Climate change projections

- **MGM** + **EU Copernicus C3S**: TR Mediterranean climate warming faster than global average
- **Aegean / Mediterranean coast**: drought intensifying; heat days TX≥35°C rising sharply (Antalya, Adana, Mersin ~60+ such days/yr by mid-2020s, est. may rise toward ~90/yr by 2050 — figures not bound to a specific scenario/dataset year here; verify at MGM + Copernicus C3S)
- **İstanbul + Marmara**: heat island + irregular precipitation; flash floods rising
- **Eastern Anatolia**: temp rise + glacier loss in Doğu Karadeniz; heavy snow → rain transition
- **Wildfire**: 2021 Antalya/Muğla mega-fires (160k ha) presaging trend; Aegean coast highest risk

---

## Section: `--mains`

### Major water + sewer utilities (regional)

| Utility | Coverage | URL |
|---|---|---|
| **İSKİ** (İstanbul Su ve Kanalizasyon İdaresi) | İstanbul metro | `https://www.iski.istanbul/` |
| **ASKİ** (Ankara) | Ankara metro | `https://www.aski.gov.tr/` |
| **İZSU** (İzmir) | İzmir metro | `https://www.izsu.gov.tr/` |
| **ASAT** (Antalya) | Antalya metro | `https://www.asat.gov.tr/` |
| **BUSKİ** (Bursa) | Bursa metro | `https://www.buski.gov.tr/` |
| **KOSKİ** (Konya), **MUSKİ** (Muğla), **AYDEM** (Aydın), **MASKİ** (Mersin) | respective Büyükşehirs | per official portal |
| **DSİ** (Devlet Su İşleri) | National water resources, irrigation | `https://www.dsi.gov.tr/` |
| Local belediye | Smaller cities + rural | per belediye portal |

### Verification

1. Check **belediye portal** > "Su ve Kanalizasyon" or call belediye santral
2. Listing language:
   - "şehir suyu" / "belediye suyu" + "kanalizasyon" = mains water + mains sewer
   - "şehir suyu var, kanalizasyon yok" = mains water but no mains sewer (septik tank)
   - "kuyu suyu" = well water (rural, common)
   - "fosseptik" / "septik" = cesspit; "BÖSAS" / "bireysel arıtma" = individual treatment plant
3. **Most Büyükşehir districts have mains water + sewer**; **rural villages (köy) often lack mains sewer**, especially in Doğu Anadolu, Karadeniz, Güneydoğu Anadolu

### Costs (2026 typical, TRY)

| Scenario | Cost |
|---|---:|
| Connection fee (where mains exists at street) | 5,000–25,000 |
| Mains drain construction (rural property, trunk in village) | 30,000–150,000 |
| Septik tank install / replacement | 25,000–80,000 |
| Bireysel arıtma (modern compliant package plant) | 80,000–250,000 |
| Kuyu açtırma (bore well, depth-dependent) | 15,000–80,000 |

(2026 estimates from market reports + insaat platforms; verify current quotes — TRY inflation moves prices monthly)

---

## Cost benchmarks (TR 2026)

| Work | Cost (TRY) |
|---|---:|
| **DASK** (100 m² betonarme) | **~830–3,200/yr** by risk zone — computed: insured sum 1,135,700 (100 m² × 11,357 TL/m², 01.07.2026 birim) × zone rate 0.73–2.82‰; high-hazard Marmara/İstanbul at upper end (verify per address via dask.gov.tr adres kodu lookup; before renewal discounts). 2026-07-03 verified |
| **DASK** (200 m² betonarme) | **~1,660–6,400/yr** (same method; insured sum 2,271,400 TL) |
| **DASK azami teminat (July 2026)** | up to **2,407,723 TRY** total cover per policy — revalued **monthly** at TÜİK ÜFE (per DASK tarife; 01.01.2026 was 2,095,462; verify indexation start date at dask.gov.tr); betonarme birim ~11,357 TRY/m² (01.07.2026). 2026-07-03 verified |
| **Avukat / hukuki danışman** (transaction lawyer) | 1–3 % of price (negotiable) |
| **Tapu Harcı total** | 4 % of declared sale value |
| **Tercüman (sworn translator)** for foreign buyer at TKGM | 2,000–5,000/transaction |
| **EKB (Enerji Kimlik Belgesi)** for rodun tip residential | 500–2,500 |
| **Yapı Denetim raporu** (for newbuilds) | 1–4 % of construction cost (statutory) |
| **Bağımsız değerleme raporu** (SPK-licensed valuation, mandatory for CBI) | 5,000–25,000 depending on property |
| **Notary (noter)** for satış vaadi sözleşmesi (preliminary contract) | 1,500–8,000 |
| **Konut sigortası** (full home insurance, optional) | 2,000–10,000/yr per 100 m² |
| **Total transaction cost (foreign buyer side)** | **~5–8 % of price** (Tapu Harcı + lawyer + valuation + translator) |

(2025–2026 estimates; verify current quotes — TRY inflation rapidly outdates these)

## Active fiscal incentives (2025–2026)

- **KDV exemption for foreign first-time buyer** — see § Tax (KDV Kanunu mad. 13/i)
- **Citizenship by Investment** — $400,000 property route (3-year resale lock); see § Quirks
- **TOKİ (Toplu Konut İdaresi)** social housing programs — first-time buyer Turkish-citizen schemes (foreigners not eligible for most TOKİ): `https://www.toki.gov.tr/`
- **Konut Hesabı (Devlet Katkılı)** — government top-up savings for Turkish first-time buyers
- **Yeşil Bina Sertifikası / Yeşil Konut kredisi** — green-build mortgages from state banks (Ziraat, Halk, Vakıf) at preferential rates
- **Lisanssız Üretim (rooftop solar self-consumption)**: under EPDK Lisanssız Elektrik Üretim Yönetmeliği — net-metering via dağıtım şirketi; up to 25 kW per uninterrupted point
- **Kentsel Dönüşüm (Law 6306 urban transformation)**: subsidized loans + tax breaks for tearing down + rebuilding pre-2000 risky buildings; particularly active post-2023

## Common listing platforms

- **sahibinden.com** — largest by far, full extraction; subscription gating on contact info
- **hepsiemlak.com** — broker-listed, well-photographed
- **emlakjet.com**, **zingat.com**, **hurriyetemlak.com**
- **endeksa.com** — automated valuation + neighbourhood analytics
- **emlak8.com** (newbuilds)
- Foreign-buyer focus: **propertyturkey.com**, **antalyahomes.com**, **istanbulhomes.com** (typically markup-included)

## Caveats unique to TR

- **TRY hyperinflation makes long-term comparisons tricky** — always check date + USD-equivalent. CPI hit 85.51 % YoY Oct 2022, re-peaked ~75 % YoY May 2024, ~44 % end-2024, low-30s late 2025, ~32.6 % YoY May 2026, **31.51 % YoY Aug 2026** (TÜİK, quoted in TCMB PPK summary 2026-42); rates may have changed.
- **Foreign-buyer pricing premium est. ~15–35 %** in Antalya, Alanya, Bodrum, Fethiye — qualitative, based on the EN-language vs TR-language sahibinden listing spread, not a sourced benchmark; verify per listing.
- **CBI threshold + rules change frequently** — $1M (2017) → $250k (Sept 2018) → **$400k (June 2022, current)**. 3-year resale lock + once-only-per-property restriction; some districts excluded (İstanbul + Antalya have ilçe-level exclusions for tightening). Verify Cumhurbaşkanlığı + Resmi Gazete.
- **Earthquake risk dominates in Marmara, Aegean, Eastern Anatolia, southeast** — never skip AFAD lookup at `https://tdth.afad.gov.tr/`.
- **TBDY 2018 is the building-quality watershed**: post-2019 in-force = substantially safer in design; pre-1999 = high risk unless retrofit-certified.
- **Post-Kahramanmaraş 2023 regulatory tightening**: yapı denetim audits, DASK enforcement, kentsel dönüşüm acceleration via Law 6306 — buyers should expect more scrutiny on older buildings.
- **Web Tapu enables online deed transfer** (since 2018) but in-person at TKGM Tapu Müdürlüğü still standard for foreigners + transactions involving foreign currency.
- **KDV exemption for foreign first-time buyers** has strict conditions: (a) FX bring-in proof via dekont, (b) 3-year holding period (raised from 1 year July 2023), (c) first-sale (ilk teslim) only, (d) buyer non-resident.
- **Foreign-buyer 30-hectare cap nationwide per individual** (Tapu Kanunu mad. 35); plus military restricted zones (verify with Genelkurmay confirmation via TKGM).
- **Reciprocity list** (~183 countries permitted): some nationalities (e.g., Syria, Armenia, North Korea, Cuba) restricted; verify current list with TKGM + İçişleri Bakanlığı.
- **Kat irtifakı vs kat mülkiyeti** — buying a unit on kat irtifakı (pre-iskan) means the building lacks final occupancy permit; bank financing limited; resale risk; insist on iskan before close.
- **Money laundering (MASAK) regulations** since 2021 require all property purchases > 75,000 TRY to flow through bank with full documentation.

## Reddit / forum sources

- **r/Turkey**, **r/istanbul**, **r/turkishlearning** — bilingual mix
- **r/expats**, **r/expat_in_Turkey**, **r/IWantOut** (relocation discussions)
- **turkishliving.com** forum — long-time expat discussion (Aegean coast skew)
- **bodrumlife** + **antalya-expats** Facebook groups
- **eksisozluk.com** — Turkish public-discussion site; useful for sentiment on specific developers, sites, neighbourhoods (search "<developer> şikayet" or "<site adı> deneyim")
- **sikayetvar.com** — consumer complaint registry for developers/agents

## Verification authorities

| Authority | When to call |
|---|---|
| **TKGM Tapu Müdürlüğü** (district registry) | Tapu verification, encumbrance check, transfer |
| **TKGM Web Tapu** | Online verification + select online transactions |
| **Belediye İmar ve Şehircilik Müdürlüğü** | İmar Durumu (zoning), kentsel dönüşüm status, building permit history |
| **AFAD İl Müdürlüğü** | Seismic risk + DASK confirmation |
| **GİB (Gelir İdaresi Başkanlığı)** | Tax liability, rayiç bedel, KDV exemption application |
| **Çevre Şehircilik ve İklim Değişikliği Bakanlığı il müdürlüğü** | EKB issuing authority, environmental compliance |
| **Bakanlık Göç İdaresi (PMM)** | Foreign residency permit (ikamet) |
| **Kültür ve Turizm Bakanlığı il müdürlüğü** | Law 7464 İzin Belgesi for short-term rental |
| **DASK** (Doğal Afet Sigortaları Kurumu) | Earthquake insurance — `https://www.dask.gov.tr/` |
| **Bağımsız SPK-lisanslı değerleme uzmanı** | CBI valuation report |
| **Avukat (lawyer)** + **mali müşavir (CPA)** | Transaction + tax compliance |

## Quirks to know

- **Kat irtifakı vs kat mülkiyeti** (the most important quirk):
  - **Kat irtifakı** (construction servitude title) = pre-occupancy, building under construction or iskan not yet issued; you own the air-rights share but not the finished unit yet. Banks restrict lending; resale harder.
  - **Kat mülkiyeti** (condominium ownership) = post-iskan, full ownership of the bağımsız bölüm (independent section). This is what you want.
  - Conversion: must apply to TKGM after iskan issuance — sometimes delayed by years if developer disputes.
- **İmar Durumu** (zoning status): always pull from belediye before purchase — specifies allowed yapı yüksekliği, taban alanı katsayısı (TAKS), kat alanı katsayısı (KAKS); non-permitted extensions on existing buildings are common and unauthorised.
- **Iskan (Yapı Kullanma İzin Belgesi)** often missing on older buildings or kaçak ilave (illegal extensions); makes utility connection + sale harder.
- **Bağımsız değerleme uzmanı** (SPK-licensed valuer) — required for CBI; must be on SPK list; report binds the deed declared value upward.
- **Bilirkişi (court-appointed expert)** for property tax disputes (rayiç bedel itiraz).
- **Foreign-buyer 30-hectare cap nationwide per individual** under Tapu Kanunu mad. 35 — including all properties combined.
- **Military-restricted zones**: TKGM checks against Genelkurmay before transferring to foreigners; ~5 % of country area; verifiable only at transaction time.
- **MASAK (Mali Suçları Araştırma Kurulu)**: anti-money-laundering — purchases > 75 k TRY must flow through Turkish bank with FX dekont if foreign-funded.
- **Tapu cinsi**: residential ("mesken"), commercial ("dükkan", "büro"), agricultural ("tarla"), olive grove ("zeytinlik" — special legal protection), forest ("orman" — generally cannot be private title); always verify cinsi on the deed.
- **Site yönetimi** (gated community management): aidat (monthly fee) varies hugely 1,000–10,000+ TRY/ay; check site karar defteri for past disputes.
- **Vergi numarası**: foreign buyers must obtain a TR vergi numarası (tax ID) before TKGM transfer — issued same-day at any vergi dairesi with passport.

## Source URL templates

| Source | URL pattern |
|---|---|
| TKGM main | `https://www.tkgm.gov.tr/` |
| Web Tapu | `https://webtapu.tkgm.gov.tr/` |
| AFAD seismic hazard map | `https://tdth.afad.gov.tr/` |
| AFAD main | `https://www.afad.gov.tr/` |
| MTA active fault map | `https://www.mta.gov.tr/v3.0/hizmetler/yenilenmis-diri-fay-haritalari` |
| MGM (meteorology) | `https://www.mgm.gov.tr/` |
| TÜİK Konut Fiyat Endeksi | `https://data.tuik.gov.tr/Bulten/Index?p=Konut-Fiyat-Endeksi` |
| TCMB (CBRT) | `https://www.tcmb.gov.tr/` |
| GİB (tax authority) | `https://www.gib.gov.tr/` |
| GİB Hazır Beyan (rental income) | `https://hazirbeyan.gib.gov.tr/` |
| DASK | `https://www.dask.gov.tr/` |
| DSİ flood + water | `https://www.dsi.gov.tr/` |
| sahibinden | `https://www.sahibinden.com/satilik/<il>-<ilce>` |
| hepsiemlak | `https://www.hepsiemlak.com/<il>-<ilce>-satilik` |
| emlakjet | `https://www.emlakjet.com/satilik-konut/<il>-<ilce>/` |
| Endeksa | `https://www.endeksa.com/tr/analiz/<il>/<ilce>/satilik/konut` |
| Resmi Gazete | `https://www.resmigazete.gov.tr/` |
| Çalışma İzni başvurusu | `https://ecalismaizni.csgb.gov.tr/` |
| Kültür ve Turizm Bakanlığı (Law 7464 İzin Belgesi) | `https://www.ktb.gov.tr/` |
| TOKİ | `https://www.toki.gov.tr/` |
| e-Devlet (citizen portal) | `https://www.turkiye.gov.tr/` |

## Status

✅ **Fully populated** (initially populated 2026-05-01).

**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources (TKGM, TÜİK, AFAD, GİB, MTA, MGM, DSİ, Resmi Gazete) + cost benchmarks + caveats + 2025 rates date-stamped.

**Confidence**:
- **HIGH** for cadastre/foreign-buyer rules/CBI mechanics/Law 7464 STR rules (all sourced to primary law + RG + TKGM/Bakanlık portals).
- **MEDIUM** for current-year tax thresholds — TRY hyperinflation means yeniden değerleme oranı + GMSİ istisna + Değerli Konut Vergisi brackets revalue annually; 2026 figures verified against the December 2025 RG circulars (2026-07-03) but must be re-checked each January.
- **MEDIUM** for parcel-level price benchmarks — TÜİK KFE is province-level only; mahalle-level requires Endeksa or sahibinden cenova haritası lookup per address.
- **MEDIUM** for STR enforcement — Law 7464 mature but municipal enforcement variance; provisional permit transition (31 Dec 2024) closed but ongoing audit risk.

**Last verified**: 2026-08-07 (§ --risks re-verified — Kahramanmaraş magnitudes corrected to the AFAD official pair Mw 7.7 + Mw 7.6, TBDY 2018 confirmed as the current code with no successor enacted, DASK compulsory-cover checkpoints confirmed; balance of the 2026-07-03 Tier-A quarterly refresh unchanged). Macro tracker entries re-checked 2026-09-24 in the October regwatch wave (see shared/regulatory-watch.md).

## Extension TODOs (deepen on first real run)

- [ ] Per-Büyükşehir Emlak Vergisi rayiç bedel revaluation (2026–2029 cycle) — capture per-belediye new declared values
- [ ] Per-il KGM YOGT data extraction (latest published year)
- [ ] Mahalle-level Endeksa machine-valuation parsing for top 200 mahalleler
- [ ] CBI exclusion district list (İstanbul + Antalya have ilçe-level exclusions tightening; track Cumhurbaşkanlığı kararı + İçişleri Bakanlığı circulars)
- [ ] Post-Kahramanmaraş kentsel dönüşüm (Law 6306) per-il subsidy + risk-building list
- [ ] Yabancı uyruklu (foreign-buyer) transaction stats per il (TÜİK quarterly)
- [ ] DASK premium calculator integration for parcel-level estimate (gross m² × construction class × city-zone)
