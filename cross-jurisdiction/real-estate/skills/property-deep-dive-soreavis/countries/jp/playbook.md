# 日本 / Japan 🇯🇵 — Property Due-Diligence Playbook

ISO2: `jp`. Status: ✅ Fully populated (researched 2026-05).

## Country profile

- **郵便番号 (postcode)**: 7 digits in `〒NNN-NNNN` format (e.g., `〒100-0001` for 千代田区千代田 / Imperial Palace; `〒150-0002` for 渋谷区渋谷)
  - First 3 digits: 都道府県 + 市区町村 cluster
  - Last 4: chōme / banchi cluster
- **Admin levels**: 47 都道府県 (todōfuken — 1 都 Tokyo, 1 道 Hokkaidō, 2 府 Ōsaka/Kyōto, 43 県 ken) → 市町村 (shi/chō/son — cities, towns, villages); 23 特別区 (tokubetsu-ku — special wards) within Tokyo metro; 政令指定都市 (designated cities, e.g., Yokohama, Ōsaka, Nagoya) have ku sub-divisions
- **Currency**: JPY (¥). 1 EUR ≈ 165–175 JPY (variable Q1 2026)
- **Languages**: Japanese (de facto official; no statutory designation)
- **Cadastre**: **法務局 (Hōmukyoku — Legal Affairs Bureau)** maintains 不動産登記簿 (real-estate register); online query via **登記情報提供サービス** (paid, ~¥332/extract) and **登記・供託オンライン申請システム** for application
  - Ministry of Justice operates 法務局; municipalities maintain 固定資産課税台帳 (fixed-asset tax ledger) separately
- **Identifier**: 不動産番号 (13-digit real estate number) + 所在 (location) + 地番/家屋番号 (parcel/building number); 公図 (kōzu — cadastral map) and 地積測量図 (chiseki sokuryō-zu — survey diagram)
- **Title concept**: 所有権 (shoyūken — freehold) vs 借地権 (shakuchiken — leasehold) — confirm before any offer. Foreign owners can hold freehold with no nationality restriction.
- **Recent reforms**:
  - **重要土地等調査法 2021** (Act No. 84 of 2021) — restricts land use within ~1 km of defense facilities, US bases, border islands. Enacted 2021-06-23; fully effective 2022-09-20. ([source](https://www.cao.go.jp/tochi-chosa/))
  - **民法・不動産登記法改正 (Act 24/2021, 不動産登記法)** — **two limbs, phased**: (a) **inheritance registration mandatory since 2024-04-01** — within **3 years of knowing of the acquisition**, penalty **up to ¥100,000** (10万円以下の過料, 不登法164① — **not** ¥50,000); pre-2024 inheritances backstop **2027-03-31**. (b) **address-change registration IN FORCE only since 2026-04-01** (not 2024) — within **2 years of the change**, penalty **up to ¥50,000** (不登法164②); pre-2026 changes backstop **2028-03-31**. Aimed at solving 所有者不明土地 (unidentified-owner land, ~23 % of all JP land per gov't survey); both limbs are foreign-heir traps. ([法務省](https://www.moj.go.jp/MINJI/minji05_00599.html), 2026-08-07 verified · [MOJ 2024 reform overview](https://www.moj.go.jp/MINJI/minji05_00343.html))
  - **空家等対策特別措置法改正 2023** (effective 2023-12) — new category 管理不全空家 (mismanaged vacant home); removal of the fixed-asset tax residential-land special exemption (住宅用地特例) once the municipality issues a 勧告 (recommendation, after unheeded 指導). ([MLIT source](https://www.mlit.go.jp/jutakukentiku/house/jutakukentiku_house_tk3_000138.html))
  - **住宅宿泊事業法 2018** (Minpaku Law, effective 2018-06-15) — short-term rental national framework, 180 nights/year cap.

## Section: `--price`

### Primary sources

- **国土交通省 不動産価格指数 (MLIT Real Estate Price Index)** — monthly composite index, residential land + condominium + commercial separate series
  - Portal: `https://www.mlit.go.jp/totikensangyo/totikensangyo_tk5_000085.html`
  - English summary: `https://www.mlit.go.jp/en/totikensangyo/totikensangyo_fr5_000014.html`
  - Latest cited series: residential price index +5.00 % YoY (Nov 2025 release, MLIT)
- **国土交通省 不動産情報ライブラリ (Real Estate Information Library)** — actual recorded transaction prices, surveyed from real transaction parties (NOT listings or estimates); replaced the 土地総合情報システム, which MLIT abolished at the end of March 2024, and carries ~5.47M cumulative records as at 31 Mar 2025 (2025 data, source MLIT; 2026-09-18 verified)
  - Portal: `https://www.reinfolib.mlit.go.jp/realEstatePrices`
  - ⚠️ **No dedicated English site** — MLIT retired the English land-price service at the end of March 2024 and published no English replacement URL; the library's own in-page language control is the only English route (2026-09-18 verified)
  - Update cadence: quarterly with 3–6 month lag
- **公示地価 (kōji chika — Public Land Price)** — annual, MLIT, 1 January reference, published late March; ~26,000 standard sites (基準地)
  - Portal: `https://www.reinfolib.mlit.go.jp/landPrices`
- **路線価 (rosenka — Route Land Value)** — annual, **国税庁 (NTA — National Tax Agency)**, used for inheritance + gift tax base
  - Portal: `https://www.rosenka.nta.go.jp/`
  - Note: 路線価 is typically ~80 % of 公示地価 (deliberate gap for tax buffer)
- **REINS (不動産流通標準情報システム)** — closed agent-only system; agents must register listings (per 宅地建物取引業法). Buyer-side agents pull comps here. Public sees only aggregated REINS Market Information at `http://www.reins.or.jp/`.

### Listing platforms (consumer-facing)

- **SUUMO** — `https://suumo.jp/` — Recruit-owned, largest by inventory; URL pattern `https://suumo.jp/jj/bukken/ichiran/JJ010FJ001/?ar=030&bs=010&ta=13&jspIdFlg=patternShikugun&sc=13104` (ar=region, ta=todōfuken code, sc=ward code)
- **at home / アットホーム** — `https://www.athome.co.jp/`
- **HOME'S / LIFULL HOME'S** — `https://www.homes.co.jp/`
- **Yahoo!不動産** — `https://realestate.yahoo.co.jp/`
- **GaijinPot Apartments** + **Real Estate Japan / RealEstate.co.jp** — English-language, foreigner-friendly: `https://apartments.gaijinpot.com/en/rent` ❌ DEPRECATED — primary source removed; verify with GaijinPot Housing (commercial listings aggregator, not a government source) and `https://realestate.co.jp/`

### Premium-area benchmarks (Q1-Q2 2025 reference, MLIT 公示地価 + Recruit Suumo new-build aggregates)

| Ward / area | 2025 公示地価 trend | New-build apt (¥/m², est.) |
|---|---|---:|
| 港区 (Minato) | +13.7 % YoY residential ([PLAZA HOMES analysis of MLIT 2025 公示地価](https://www.realestate-tokyo.com/news/standard-land-prices-tokyo-2025/)) | ~¥3.0–6.4M/m² central |
| 千代田区 (Chiyoda) | central wards +12.0 % avg | ~¥2.5–5.0M/m² |
| 中央区 (Chūō) | central wards +12.0 % avg | ~¥2.0–4.0M/m² |
| 渋谷区 (Shibuya) | central wards +12.0 % avg | ~¥2.0–4.5M/m² |
| 新宿区 (Shinjuku) | central wards +12.0 % avg | ~¥1.5–3.0M/m² |
| 23 区 average residential | +7.9 % YoY | new-build avg ~¥1.7M/m² (Statista 2025 series) |
| 23 区 highest land point | ¥5.9M/m² (赤坂, Minato-ku, 2025 公示地価) | — |
| Tokyo metro greater area new-build (Mar 2025) | — | avg ¥104.85M total unit (+37.5 % YoY, MLIT-affiliated Recruit aggregate) |
| Tokyo 23-ward new-build (Apr 2025) | — | avg ¥90M total unit (–7 % YoY post-March spike) |
| Tokyo 23-ward used apt (Apr 2025) | — | avg ¥44.51M total (+28.3 % YoY) |
| Hokkaidō (Sapporo, Niseko ex-resort) | regionally mixed; Niseko +20–30 % resort surge | ~¥0.5–1.5M/m² Sapporo central |
| 京都市 (Kyoto) | +6–10 % core | ~¥1.0–2.5M/m² central; landmark/景観 zones restricted |
| 沖縄県 (Okinawa) | +5–8 % | ~¥0.4–1.0M/m² Naha; **重要土地等調査法 注視区域 designated near US bases** |

### Compute

1. Listing ¥/m² = listing price ÷ 専有面積 (senyū menseki, exclusive floor area for condos) — clarify whether 専有面積 (Carrez-equivalent) or 壁芯 (wall-center, slightly larger) is quoted on the listing
2. Compare to 不動産情報ライブラリ (last 4 quarters, same 駅 station + 区 ward)
3. Compare to 路線価 (NTA) for inheritance-tax-equivalent valuation
4. Cross-check 公示地価 for 1 Jan reference benchmark on the same 区
5. **Trap**: 新築 (shinchiku — new) carries a 10–30 % premium over equivalent 築浅 (chiku-asa — recently built) — disappears within 5–10 years for wood-frame; persists longer for RC tower
6. **Trap**: 専有面積 vs 登記面積 (registered area, often smaller — net of internal walls, used for tax). Confirm both before per-m² math
7. **Trap**: 共用部分 (common-area share) charges 管理費 + 修繕積立金 are NOT in the listing price — sum monthly cost separately

### Trend Q4 2024 → Q1 2026

- BoJ rate normalization (NIRP exit Mar 2024 → 0.25 % Jul 2024 → 0.5 % Jan 2025 → 0.75 % Dec 2025, [BoJ MPM 251219](https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2025/k251219a.pdf); held Jan–Apr 2026 → 1.0 % 16 Jun 2026 (31-yr high since 1995, 7-1 vote), [BoJ MPM 260616](https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260616a.pdf); held 31 Jul 2026 (8-1) → 1.25 % 18 Sep 2026 (7-2 vote, effective 24 Sep 2026; 2026 data, source [BoJ MPM 260918](https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260918a.pdf)); next mtg 29–30 Oct 2026) is gradually feeding through to mortgage variable rates
- Tokyo central wards remain bull market (foreign + domestic flight-to-quality); rural Honshū/Shikoku/Kyūshū continue depopulation-led decline
- 円安 (weak yen) cycle Q4 2024 → 2025 sustained foreign-buyer interest in Tokyo + Niseko + Kyōto

---

## Section: `--traffic`

### Primary source

- **国土交通省 全国道路・街路交通情勢調査 (zenkoku dōro/gairo kōtsū jōsei chōsa) — "道路交通センサス" (Road Traffic Census)**:
  - 5-yearly nationwide survey, MLIT 道路局 (Road Bureau)
  - Latest published: 平成27年度 (FY2015) and partial 令和3年度 (FY2021) results
  - Portal: `https://www.mlit.go.jp/road/census/h27/`, FY2021: `https://www.mlit.go.jp/road/census/r3/`
  - English statistics index: `https://www.mlit.go.jp/road/road_e/statistics.html`
  - e-Stat (national stats portal): `https://www.e-stat.go.jp/en/statistics/00600580`
- **道路統計年報 (Annual Report of Road Statistics)** — yearly companion publication, MLIT
- **NEXCO 東日本 / 中日本 / 西日本** — expressway operators publish daily traffic on national expressway segments
- **都道府県 + 政令市 道路台帳** — prefectural/city road registers (variable digitization quality)

### Key term

**12時間 / 24時間 自動車類交通量** — 12-hour and 24-hour vehicle traffic volume, measured at 観測地点 (observation points). Functionally similar to AADT.

### Verdict bands (rough)

- 🟢 < 1,000 v/d (quiet residential street, non-arterial)
- 🟡 1,000–10,000 v/d (minor arterial, secondary urban)
- 🟠 10,000–40,000 v/d (major prefectural road, urban arterial)
- 🔴 > 40,000 v/d (national highway 国道 / urban core / 環状 ring road segment)

### Coarse fallback

OSM `highway` class:
- motorway = 高速道路 (expressway)
- trunk = 国道 (national highway)
- primary = 主要地方道
- secondary = 一般都道府県道
- tertiary = 市町村道 (main)
- residential = 生活道路

⚠️ Always cross-check sound-attenuation walls (防音壁), elevated structures, or 25-mph-equivalent (時速40km) limits — rural 国道 can be quieter than urban 市道.

---

## Section: `--tax`

### Annual property tax — 固定資産税 + 都市計画税

**Owner as of 1 January each year is liable.** Bills issued April–June, payable in 4 instalments (June, September, December, February of the following year).

**Standard rates** ([NTA / JETRO / multiple municipal sources](https://www.jetro.go.jp/en/invest/setting_up/section3/page8.html)):

| Tax | Standard rate (標準税率) | Cap (制限税率) | Base (課税標準額) |
|---|---|---|---|
| **固定資産税 (kotei shisanzei — fixed asset tax)** | **1.4 %** | none — municipalities may set higher (e.g., 一部 1.5–1.7 %) | 固定資産税評価額 (assessed value, ~60–70 % of market) |
| **都市計画税 (toshi keikaku zei — city planning tax)** | **0.3 %** | 0.3 % | same base; only inside 市街化区域 (urbanization promotion zone) |

### Special land exemption (住宅用地特例)

- **小規模住宅用地** ≤ 200 m²: 課税標準額 reduced to **1/6** for 固定資産税 and **1/3** for 都市計画税
- **一般住宅用地** > 200 m²: 1/3 / 2/3 reduction

⚠️ **2023 反映**: revoked for 管理不全空家 (mismanaged vacant homes) once a municipal 勧告 (recommendation, after unheeded 指導) is issued under the 2023-amended 空家特措法 and not remedied by the 1 Jan 賦課期日 — the 固定資産税 land taxable base rises up to **4.2×** on the ≤200 m² portion (1/6 → the 70%-of-price cap for 住宅用地以外; up to 2.1× above 200 m²); the actual first-year rise is est. lower where 負担調整措置 phases it in — verify with the municipal 固定資産税 office. ([MLIT](https://www.mlit.go.jp/jutakukentiku/house/jutakukentiku_house_tk3_000138.html))

### Example calculations (worked, transparent inputs)

**Example A: 70 m² Tokyo Minato-ku condo, market price ¥150 M, 評価額 ¥90 M (60 % of market) — ¥80 M building / ¥10 M land share (20 m² land share via senshū-shoyū equivalent)**

- 固定資産税 building: ¥80 M × 1.4 % = **¥1,120,000/yr** before depreciation adjustments
- 固定資産税 land: ¥10 M × 1/6 (small-site exemption) × 1.4 % = **¥23,333/yr**
- 都市計画税 building: ¥80 M × 0.3 % = **¥240,000/yr**
- 都市計画税 land: ¥10 M × 1/3 × 0.3 % = **¥10,000/yr**
- **Total ~¥1.39 M/yr (~€8,400/yr)** — figures are illustrative; actual depends on 評価額 from local 課税課

**Example B: 100 m² akiya in rural 町, market ¥3 M (renovation needed), 評価額 ¥1.5 M (50 % of market) split ¥1 M building / ¥0.5 M land 250 m²**

- 固定資産税 building: ¥1 M × 1.4 % = **¥14,000/yr**
- 固定資産税 land: ¥0.5 M × 1/3 (>200 m² portion partial) × 1.4 % ≈ **~¥2,500/yr**
- 都市計画税 typically not applicable in non-市街化区域 rural town
- **Total ~¥16,500/yr (~€100/yr)** — if a 管理不全空家 勧告 removes the 住宅用地特例, the land line rises to at most ¥0.5 M × 70 % × 1.4 % = ¥4,900/yr, total ≤ ~¥18,900/yr (computed; first-year est. lower where 負担調整措置 phases it in)

### Transaction taxes (one-time)

| Tax | Rate | Base |
|---|---|---|
| **不動産取得税 (real-estate acquisition tax)** | **3 %** residential, **4 %** non-residential (residential reduced rate effective until 2027-03-31, [Housing Japan summary](https://housingjapan.com/blog/property-taxes-in-japan-2025/)) | 固定資産税評価額 |
| **登録免許税 (registration tax)** — land transfer | 2 % standard; **1.5 % reduced rate** until 2026-03-31 | 評価額 |
| **登録免許税** — building (新築 owner-occupied) | 0.4 % standard; **0.15 %** reduced (residential, until 2027-03-31) | 評価額 |
| **登録免許税** — building (中古 owner-occupied) | 0.3 % reduced (residential, until 2027-03-31) | 評価額 |
| **印紙税 (stamp duty)** | flat ¥10,000–¥60,000 typical for residential contracts ¥10M–¥500M | contract face value |
| **司法書士 (judicial scrivener) fee** | ~¥50,000–¥150,000 typical residential | flat schedule |
| **仲介手数料 (agent commission, max)** | **3 % + ¥60,000 + 消費税 10 %** when sale price > ¥4 M | sale price; statutory cap per 宅建業法 |

⚠️ Flat-rate ¥60,000 is the simplified equivalent of the tiered 5 %/4 %/3 % bands on the first ¥4 M ([Plaza Homes guide](https://www.realestate-tokyo.com/news/agents-commission/), 宅建業法 § 46).

### Capital gains (譲渡所得税)

| Holding period | Rate (national + local + reconstruction surtax) |
|---|---|
| **Short-term** (≤5 years as of 1 Jan of sale year) | **39.63 %** (30.63 % national income tax + 復興特別所得税 + 9 % 住民税) |
| **Long-term** (> 5 years) | **20.315 %** (15.315 % national + 5 % 住民税) |
| **超長期** (>10 years, 自己居住用 with conditions) | partial reductions; up to ¥30 M owner-occupied gain exemption (居住用財産特別控除) |

Source: [PwC Worldwide Tax Summaries — Japan](https://taxsummaries.pwc.com/japan/individual/income-determination); [Housing Japan 2025](https://housingjapan.com/blog/property-taxes-in-japan-2025/).

### Inheritance tax (相続税) — significant exposure

Progressive **10 % → 55 %** on each statutory heir's allotted share. Basic exemption: **¥30 M + ¥6 M × number of statutory heirs**.

- **Non-resident heir of Japan-situs real estate**: always taxable on the JP property regardless of residency or visa status — among the world's strictest inheritance regimes for foreign heirs of JP assets ([NTA No.15001](https://www.nta.go.jp/english/taxes/others/02/15001.htm); [PwC Japan Other Taxes](https://taxsummaries.pwc.com/japan/individual/other-taxes))
- **路線価 (NTA route-land value)** is the inheritance-tax base, ~80 % of 公示地価
- Foreign heirs without Japan-resident statutory representative face procedural complications + possible Japanese-language notarized translation requirements

### Future risk

- **2024 民法改正** mandatory inheritance registration (3 years from **knowing of the acquisition**; penalty **up to ¥100,000** if unregistered without justification — 10万円以下の過料, 不登法164①, **not** ¥50,000; pre-2024 inheritances backstop **2027-03-31**) hits non-resident heirs hardest — easy to miss ([法務省](https://www.moj.go.jp/MINJI/minji05_00599.html), 2026-08-07 verified)
- Discussion of 2026–2027 tax reform on luxury condominium revaluation (Tokyo central wards 評価額 increases proposed)
- **管理不全空家 勧告** — extra annual fixed-asset tax = the land's 評価額 × 70% × 1.4% minus the current land bill (computed upper bound before 負担調整措置; Example B above: ≈ ¥4,900 − ¥2,500 = +¥2,400/yr) once a 勧告 is issued and not remedied by the 1 Jan 賦課期日 (applies from the following fiscal year's bill, not retroactively)

---

## Section: `--rental`

### Long-term residential (賃貸 / chintai)

- **借地借家法 (Land and Building Lease Act)** — strong tenant protection: standard 普通借家契約 makes refusing renewal nearly impossible without 正当事由 (valid cause); 定期借家契約 (fixed-term) allows clean exit
- **Customary tenant payments at signing** (declining in newer leases but still 60–80 % of Tokyo市場):
  - **敷金 (shikikin — security deposit)**: 1–2 months
  - **礼金 (reikin — key money, gift to landlord)**: 0–2 months — falling fast in 2020s; many Tokyo 23-ward newbuilds zero-礼金
  - **更新料 (kōshinryō — renewal fee)**: ~1 month every 2 years (regional; uncommon in Kansai)
  - **保証会社費用 (guarantor company)**: 0.5–1 month + annual fee — replacing 連帯保証人 (personal guarantor) requirement
  - **Agent fee**: typically 1 month + 消費税 (statutory cap, 宅建業法)
- **Income tax on rental** — 不動産所得 (real-estate income) reported on 確定申告 (annual tax return); progressive 5 %–45 % national + 10 % 住民税 + 復興特別所得税
- Yields (Q1 2026, Tokyo 23 ward, est. — inference: rent comps ÷ asking price):
  - **Central 5 ward (港・千代田・中央・渋谷・新宿)**: gross yield 3.0–4.0 %
  - **Outer 23 ward**: 4.0–5.5 %
  - **Tokyo metro outside 23 ward**: 5.5–7.0 %
  - **Rural 政令市 (Sapporo, Sendai, Hiroshima, Fukuoka)**: 6.0–9.0 %
  - **Akiya districts**: technically high yield but liquidity zero — exit risk dominant

### Short-term rentals (民泊 / minpaku)

**Three legal pathways**:

| Regime | Statute | Cap | Notes |
|---|---|---|---|
| **住宅宿泊事業 (jūtaku shukuhaku jigyō)** — Minpaku Law Type 1 | 住宅宿泊事業法 art.2(3) (2018-06-15) | **180 nights/year** (一年間で百八十日; Apr 1 → Apr 1, counted by nights) — **unchanged and in force**, re-checked against the e-Gov consolidated text (2026-08-07 verified) | National regime; register with prefecture/政令市 health centre 保健所 |
| **国家戦略特区民泊 (tokku minpaku)** — Special Zone | 国家戦略特別区域法 | min 2-night stay; no annual cap in designated zones | Zones: Tokyo Ōta-ku, Ōsaka-shi/Ōsaka-fu, Niigata-shi, Kitakyūshū-shi, etc. **Ōsaka temporarily halted new applications May 2026** ([source](https://www.aiaig.com/en/investment-news/japan-airbnb-special-zone-minpaku-policy-2025)) |
| **旅館業法 (Ryokan Gyōhō)** — Hotel/Inn Business Act | 1948 + 2018 reform | no nightly cap | Full hotel/旅館 or 簡易宿所 (kani shukusho — simplified guesthouse) license; municipal 保健所 license; building must satisfy 旅館業法 facility standards (washbasins, fire systems) |

**Municipal-level overlay** — 住宅宿泊事業法 **art.18** lets 都道府県 / 保健所設置市 cut the operating period below the national 180 nights by 条例, so the municipal layer can be stricter than the statute (2026-08-07 verified, source [観光庁 民泊制度ポータル](https://www.mlit.go.jp/kankocho/minpaku/)):
- **東京都 (Tokyo)**: each 23 ward sets supplementary rules; 新宿区, 渋谷区, 中野区 restrict residential-zone minpaku to weekends + Friday only; some wards prohibit altogether in 第一種低層住居専用地域 (2026-05-01 verified — carried forward, NOT re-verified 2026-08-07; confirm with the ward 保健所)
- **京都市 (Kyoto)**: 住居専用地域 minpaku permitted **only 15 Jan noon → 16 Mar noon** (off-season) under 2018 city ordinance — effectively non-viable for most addresses. **Enforcement escalating**: a late 2-monthly report draws immediate 公表 / 過料 / 業務停止命令 / 廃止命令 from Feb 2026, and night + early-morning spot inspections expand from Apr 2026; a 条例改正 proposal targeted **within FY2026** (京都市会だより No.149, 2026-04-15) now has a 31 Aug 2026 素案 per press reports (secondary — Yomiuri 2026-09-01 / Traicy 2026-09-07): **0 operating days for NEW 届出住宅 in 住居専用地域 and 工業地域** (host-present or absent; existing facilities exempt) + on-site / adjacent-building staff presence for minpaku and 簡易宿所; 3rd expert meeting scheduled 2 Nov 2026, public comment Nov 2026, bill aimed at the Feb 2027 市会 — **proposed, NOT enacted** (2026-08-07 verified, source [京都市 市長記者会見 2026-01-29](https://www.city.kyoto.lg.jp/hokenfukushi/cmsfiles/contents/0000351/351332/04_2kisyakaiken.pdf))
- **大阪市 (Ōsaka)**: 2025–2026 oversight tightening; new 特区民泊 applications paused (2026-05-01 verified — carried forward, NOT re-verified 2026-08-07; confirm with the 大阪市 特区民泊 registration office)
- **沖縄県** (some municipalities): seasonal restrictions

### Tax + reporting obligations (民泊)

- **Income**: 不動産所得 if passive minpaku-host operator only; **事業所得 (jigyō shotoku — business income)** if running multiple units / providing meals / employing staff (event-based test)
- **消費税 (consumption tax 10 %)**: registered if revenue > ¥10 M/year (mandatory 課税事業者); below threshold → 免税事業者 default. Inbound インボイス制度 (qualified invoice system, effective 2023-10) raised pressure to register
- **個人事業主開業届** at 税務署 (tax office) within 1 month of starting business
- **宿泊税 (lodging tax)**: Tokyo, Ōsaka, Kyoto, Fukuoka, Kanazawa. **Kyoto reform 1 March 2026** (top band ¥1,000 → ¥10,000 = 10×): tiers **¥200 (<¥6,000/night) / ¥400 / ¥1,000 / ¥4,000 / ¥10,000 (≥¥100,000/night)** (2026-05-27 verified, source [Kyoto City announcement](https://kyoto.travel/en/news/tax-change/) + [Japan Travel](https://en.japantravel.com/news/kyoto-lodging-taxes-to-increase-from-march-2026/71333)). **Tokyo FY2027 reform (proposed)**: shift from current ¥100/¥200 fixed band to **3 % of room charge** with exemption threshold raised to ¥13,000/night — subject to Metropolitan Assembly + MIC approval (2026-05-27 verified, source [Japan Times 2025-11-25](https://www.japantimes.co.jp/news/2025/11/25/japan/accommodation-tax-fixed-rate-tokyo/)). Other cities: ¥100–¥1,000/night pre-reform. **Ōsaka 特区民泊 新規受付 closed 2026-05-29** (Habikino/Kaizuka/Izumisano still accept; existing licences may operate) (2026-05-27 verified, source: Nippon.com / Jiji 2025-11-17 — original article no longer reachable; verify current status with Ōsaka City 特区民泊 (minpaku) registration office)
- **観光庁 民泊制度ポータルサイト**: `https://www.mlit.go.jp/kankocho/minpaku/`
- **届出番号 (notification number)** from prefecture must be displayed on every Airbnb/Booking listing — platforms enforce since 2018-06-15 cleanup

### Strategic notes

- **Tokyo central + Kyoto + Niseko + Okinawa resort coast**: high gross yields but heaviest regulatory load
- **Ōsaka 特区 (until policy resumes)**: was favored for higher cap; pause makes 旅館業法 簡易宿所 the practical entry route
- **Local "近隣説明" (neighbour notification)** required pre-launch — failure is the most common ground for license revocation

---

## Section: `--work=<profession>`

### Job platforms

- **doda** — `https://doda.jp/` (Persol-owned, broadest mid-career)
- **マイナビ転職** — `https://tenshoku.mynavi.jp/`
- **リクルートエージェント / リクナビNEXT** — `https://www.r-agent.com/`, `https://next.rikunabi.com/`
- **BizReach** — `https://www.bizreach.jp/` (executive / ¥7M+ JPY)
- **LinkedIn Japan** — strong for IT, finance, foreign companies, English-language
- **GaijinPot Jobs** — `https://jobs.gaijinpot.com/` (English-speaking foreigner-friendly)
- **ハローワーク (Hello Work)** — public job centre, `https://www.hellowork.mhlw.go.jp/`

### Self-employment regimes

- **個人事業主 (kojin jigyōnushi — sole proprietor)**: register 個人事業の開業・廃業等届出書 at 税務署 within 1 month
- **青色申告 (blue-form filing)**: best regime — ¥650,000 special deduction (e-Tax + double-entry); apply within 2 months of opening
- **白色申告**: simpler bookkeeping, no special deduction
- **消費税 (10 %)**: 課税事業者 mandatory if revenue > ¥10 M/yr (lookback); voluntary registration possible to claim input credits; 免税事業者 default below threshold
- **インボイス制度 (qualified invoice system, effective 2023-10-01)**: B2B clients increasingly require qualified-invoice issuer status → pushes small earners to register early
- **国民健康保険 (kokuho — national health insurance)** + **国民年金 (kokumin nenkin — national pension)** mandatory; rates set by 市区町村 (varies, typically combined ~15–25 % of income up to caps)

### Foreign worker visa interface (cross-section to `--visa`)

- **Highly Skilled Professional (HSP, 高度専門職)** — 70-point system; fastest PR (1–3 years)
- **Engineer/Specialist in Humanities/International Services (技人国)** — most common white-collar
- **Business Manager (経営・管理)** — for self-employed / company owners; ¥5 M JPY capital + office
- **Skilled Worker (技能)** — trades, e.g., chef
- Applicable visa determines mortgage eligibility (banks demand PR or stable JP income history)

### Salaried benchmarks (median monthly gross 2025, MHLW 賃金構造基本統計調査 — pending 2025 release; 2024 cited)

- 東京都: ~¥360,000–¥420,000 (median FT regular employee, all-industry)
- 政令市: ~¥310,000–¥360,000
- 地方都市: ~¥260,000–¥310,000
- **最低賃金 (minimum hourly wage, FY2025 national weighted avg)**: ¥1,055/hr; 東京都: ¥1,163/hr ([MHLW source](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/minimumichiran/))

### Catchment heuristics

- Within 60 min train of 東京駅: full white-collar catchment
- Within 60 min of 政令市 central station: regional employment access
- Beyond 60 min of nearest 政令市: thin labor market; remote-friendly + JP-language critical
- Hokkaidō, 東北 outside Sendai, 山陰: depopulation → very thin catchment

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **国土交通省ハザードマップポータル** (consolidated MLIT hazard portal) | `https://disaportal.gsi.go.jp/` | Flood, landslide, tsunami, storm surge, volcano — overlay any address |
| **MLIT 重ねるハザードマップ** (overlay map) | `https://disaportal.gsi.go.jp/maps/?ll=35.681236,139.767125&z=12` | Multi-hazard layered visualization |
| **J-SHIS (Japan Seismic Hazard Information Station)** — 防災科学技術研究所 / 地震調査研究推進本部 (HERP) | `https://www.j-shis.bosai.go.jp/` | Probabilistic seismic hazard maps; 30-year probability of JMA seismic intensity 5+, 5-, 6-, 6+ |
| **気象庁 (JMA)** 緊急地震速報 + 過去地震データ | `https://www.jma.go.jp/` | Active hazard + historical |
| **気象庁 津波警報・注意報** + 海岸線図 | `https://www.data.jma.go.jp/eqev/data/en/tsunami/tsunami_warning.html` | Tsunami zones |
| **海上保安庁 海岸線地形図** | `https://www.jha.or.jp/` | Coastal elevation |
| **国土地理院 (GSI)** 活断層データベース | `https://gbank.gsj.jp/activefault/` | Active fault traces |
| **Land Bureau 河川局 浸水想定区域図** | `https://www.mlit.go.jp/river/bousai/bousai-portal/en/index.html` | Flood inundation zones (河川 + 内水 + 高潮) |

### J-SHIS verdict bands (30-year probability of JMA震度6弱以上, 確率論的地震動予測地図)

- 🟢 < 3 % (interior Honshū, Hokkaidō ex-Tokachi)
- 🟡 3–6 % (most western Japan inland)
- 🟠 6–26 % (太平洋沿岸 — Tōkai, Nankai trough catchment)
- 🔴 > 26 % (静岡, 高知, 和歌山, 千葉房総, 宮城沿岸 — Nankai/Tōnankai/関東 trough)

⚠️ Source: [J-SHIS portal](https://www.j-shis.bosai.go.jp/en/shm); 確率論的地震動予測地図 ("Probabilistic Seismic Hazard Maps") at the link.

### Build-era hazards (the watershed)

| Era | Code basis | Hazard rating |
|---|---|---|
| **Pre-1981 (旧耐震基準)** | 1950 建築基準法 (original) | 🔴 **Significant risk** — designed only to withstand JMA 5– without collapse; banks often refuse mortgage; ~25–40 % discount est. (inference: mortgage-refusal + collapse-risk depresses resale) |
| **1981–2000 (新耐震基準)** | 1981 amendment effective 1981-06-01 | 🟡 Acceptable — withstand JMA 5+ without significant damage, JMA 6+ without collapse (per [building-code reference](https://resources.realestate.co.jp/buy/earthquake-building-codes-and-technology-in-japan/)) |
| **2000+ (改正新耐震 / for wood-frame: 平成12年改正)** | 2000 amendment, particularly tightened wood-frame foundation + connector requirements | 🟢 Modern; introduced 住宅性能表示制度 with 耐震等級 1/2/3 (1.0×/1.25×/1.5× legal min) |
| **2008+ tower 高層 RC** | 2007 改正 + JSCA-led base-isolation diffusion | 🟢 Many use 免震 (base isolation) or 制震 (damping) — outperform code |

⚠️ The **1981 watershed is the single most material datum** in JP building diligence. Confirm 建築確認申請日 (building permit date — pre vs post 1981-06-01) on registry/contract; 完成 (kanseii — completion) date alone misleads.

### Mandatory disclosures (at sale)

| Document | Required because | Source |
|---|---|---|
| **重要事項説明書 (jūyō jikō setsumeisho)** | 宅建業法 § 35 — must be explained by 宅地建物取引士 (Takken Shujisha) BEFORE contract | covers location, zoning, water/sewer, mortgage, defect history |
| **物件状況等報告書** (property condition disclosure) | 宅建業法 standard practice | seller's known defects |
| **設備表 (setsubi-hyō — equipment table)** | standard | what's included / functional status |
| **既存住宅状況調査 (kichūshin)** | 2018 改正 宅建業法 § 34-2 — agent must offer + report results | not mandatory, but agents must inform buyer; ¥50,000–¥150,000 cost |
| **既存住宅瑕疵保険 (existing-home defect insurance)** | optional, 5-year defect coverage typical | available post-kichūshin pass |
| **管理に係る重要事項調査報告書** (for condos) | required for 区分所有 | 管理組合 financials, 修繕積立金 status, 大規模修繕 history |

Source: [MLIT 既存住宅状況調査](https://www.mlit.go.jp/jutakukentiku/jutaku-kentiku.files/kashitanpocorner/jigyousya/inspection.html), [Plaza Homes guide](https://www.realestate-tokyo.com/news/use-of-home-inspection/).

### Earthquake insurance (地震保険)

- Run by JER (Japan Earthquake Reinsurance) — public-private scheme, government as ultimate backstop
- **Add-on to 火災保険 (fire insurance)** — cannot be standalone
- Coverage cap: 50 % of fire-policy sum; max ¥50 M building / ¥10 M contents
- Premiums vary 2–10× by 都道府県 (highest: 千葉, 東京, 神奈川, 静岡, 高知, 徳島, 和歌山, 三重)

### Climate change projections (JMA 気候変動監視レポート + IPCC AR6)

- JMA 気候予測情報 (Climate Change Projections) projects under RCP4.5: Tokyo annual mean temperature **+2.0–2.5 °C** by 2050 vs 1981–2010; under RCP8.5 +3.0–3.5 °C
- Heat-wave days (TX≥35°C 猛暑日): central Tokyo expected 2–3× increase by 2050
- 熱帯夜 (tropical nights TN≥25°C): Tokyo summer becomes near-continuous tropical-night
- Super-typhoons: intensity rise; track shift northward; Kyūshū, 紀伊半島, 関東 increasing exposure
- Sea-level rise: +0.3–0.6 m by 2100 RCP4.5; +0.5–1.0 m RCP8.5 — Tokyo Bay, Ōsaka Bay coastal land + Kanagawa湾岸 + 沖縄 low-lying atolls
- Precipitation: extreme rain events (1-hour 50 mm+) +20–30 % frequency by 2050
- Source: JMA reports — `https://www.data.jma.go.jp/cpdinfo/monitor/index.html` and IPCC AR6 East Asia Atlas

---

## Section: `--mains`

### National database

- **公益社団法人 日本水道協会 (JWWA)**: `http://www.jwwa.or.jp/` — sector data
- **国土交通省 下水道統計**: `https://www.mlit.go.jp/mizukokudo/sewerage/index.html` — sewer coverage statistics

### Operators

- 上水道 (water supply): per **市町村 水道事業者** (municipal water utility) — ~1,300 entities. Major: 東京都水道局, 大阪市水道局, 横浜市水道局
- 下水道 (sewer): per 市町村 公共下水道; some 流域下水道 (basin-wide) operated by 都道府県
- Coverage:
  - **上水道 普及率 (water coverage)**: ~98 % nationally (2023, MLIT)
  - **下水道 普及率 (sewer coverage)**: ~81 % nationally (2023, MLIT) — **but heavily skewed**: 政令市 95–99 %, rural 町村 often 30–60 %, some <20 %
- Where mains sewer absent, individual treatment via **浄化槽 (jōkasō)** — combined-flow septic system, regulated by 浄化槽法 (1983); 5-人槽 to 50-人槽; annual maintenance contract with 保守点検業者 + 法定検査

### Verification

1. Listing language:
   - 公共下水 / 本下水 = mains sewer
   - 浄化槽 = individual treatment system
   - 汲み取り (kumitori) = pit toilet (rare; rural older)
   - 上水 公営 = mains water; 井戸 = well
2. Confirm via 市役所 / 町村役場 — 上下水道課 (Water/Sewer Bureau)
3. **重要事項説明書** § 上下水道整備状況 must specify

### Costs (typical 2026)

| Scenario | Cost (JPY) |
|---|---:|
| Connection where mains available | ¥300,000–¥800,000 |
| Mains sewer extension to property (if road has trunk) | ¥1,000,000–¥3,000,000 |
| 浄化槽 install (5-人槽, new) | ¥800,000–¥1,500,000 |
| 浄化槽 annual maintenance + 法定検査 | ¥30,000–¥60,000/yr |
| 浄化槽 → mains conversion (full demolish + reconnect) | ¥1,500,000–¥3,500,000 |
| 井戸 (well) → 上水 conversion | ¥500,000–¥1,500,000 |

---

## Cost benchmarks (JP 2026)

| Item | Cost (JPY) |
|---|---:|
| 司法書士 (judicial scrivener, residential transfer) | ¥50,000–¥150,000 |
| 仲介手数料 (agent commission, max statutory) | 3 % + ¥60,000 + 消費税 |
| 印紙税 (stamp duty, ¥10M–¥50M contract) | ¥10,000–¥30,000 |
| 不動産取得税 (residential, until 2027-03-31) | 3 % × 評価額 |
| 登録免許税 (land 1.5 %; building 0.15–0.3 %) | reduced rates until 2026/2027 |
| 既存住宅状況調査 (kichūshin home inspection) | ¥50,000–¥150,000 |
| 火災保険 (fire ins. 5-yr lump for ¥30M structure) | ¥30,000–¥80,000/yr equivalent |
| 地震保険 add-on (varies by 都道府県) | ¥10,000–¥120,000/yr |
| 管理費 (condo monthly admin fee) | ¥10,000–¥40,000/mo |
| 修繕積立金 (sinking fund, condo monthly) | ¥10,000–¥30,000/mo (rises sharply with age) |
| Akiya renovation (interior+system, 100 m² wood) | ¥5M–¥15M typical |
| Akiya full structural rebuild | ¥15M–¥30M |
| Demolition (100 m² wood) | ¥1.5M–¥3M |
| **Total transaction cost (buyer side, residential)** | **~6–10 % of price** |

## Active fiscal incentives (2025–26)

- **【フラット35】(Flat 35)** — JHF (住宅金融支援機構) long-term fixed-rate residential mortgage; **Flat 35 S(ZEH)** offers ~1.0 % rate reduction first 5 years for ZEH (zero-energy housing) certified properties combined with 長期優良住宅 (long-life housing). Q3 2025 applications +50 % YoY. ([JHF flat35](https://www.flat35.com/), [JHF Flat35 S(ZEH)](https://www.flat35.com/loan/lineup/flat35s_zeh/index.html))
- **Flat 50** — JHF pilot 50-year fixed-rate; expanding nationwide 2026
- **住宅ローン控除 (mortgage tax deduction)** — 0.7 % of outstanding balance × 13 years (qualifying new ZEH/long-life), capped per category
- **子育てエコホーム支援事業** — household-with-children + young-couple grants for energy-efficient new build / renovation: up to ¥1M new, ¥600K renovation (FY2024 ongoing 2025–26 reapply)
- **空き家バンク (akiya bank)** — municipal-level akiya databases + grants. Discoverable via `https://www.akiya-athome.jp/` (LIFULL aggregator) and individual 自治体 sites
- **既存住宅 リフォーム補助金** — 都道府県 + 市町村 retrofit grants (耐震補強 ¥1M–¥1.5M typical; 省エネ retrofit ¥500K–¥1.2M)
- **耐震診断 + 耐震改修 補助金** — pre-1981 buildings: 耐震診断 ¥30K–¥60K cost, ~50–100 % subsidized; retrofit subsidy ~¥500K–¥1.5M depending on 自治体

## Common listing platforms

- **SUUMO** (Recruit) — broadest national coverage
- **at home / アットホーム**
- **HOME'S / LIFULL HOME'S**
- **Yahoo!不動産**
- **REINS Market Information** (aggregated public view of agent-only system) — `http://www.reins.or.jp/`
- **GaijinPot Apartments**, **RealEstate.co.jp** (English / foreigner-friendly)
- **空き家バンク** — municipal sites + LIFULL akiya aggregator

## Caveats unique to JP

- **The 1981 (新耐震) and 2000 (改正) seismic-standard watersheds are the single most material data points** in build-year diligence — confirm 建築確認 date, not 完成 date
- **Akiya cheapness is real, but liability + renovation cost + remoteness usually offset purchase savings** — verdict: only pursue with a local 工務店 (kōmuten) on side and confirmed end-use plan (residence vs minpaku vs demolition)
- **Condos lose 評価額 over decades** unlike European apartments — wood-frame accounting life 22 years (now 30 for new), RC 47 years; structural value approaches 0 by mid-life
- **Foreigner mortgages**: PR or 5+ years JP income history typical; some banks (Shinsei, SMBC Trust, Tokyo Star, Aozora) offer non-resident loans at 50–60 % LTV with JP guarantor
- **重要事項説明** is mandatory but reads as legalese; insist on written translation if not Japanese-fluent — agents are not required to translate
- **相続 (succession) for foreign heirs**: no English-language wills for JP property recognised by 法務局; use 公正証書遺言 (notarized JP will) prepared by 公証人; 2024 mandatory inheritance registration heightens stakes
- **Minpaku regulation is multi-layer**: national (180 days) + 特区 + municipal — verify ALL three before buy
- **管理費 + 修繕積立金 trajectory**: older condos see 修繕積立金 rise sharply once 大規模修繕 cycle hits — request 長期修繕計画書 (long-term repair plan) for any condo > 10 years old
- **重要土地等調査法 注視区域**: residential ownership not blocked; in 特別注視区域 the contract parties must file a notification for an ownership transfer (art. 13, plots below a 政令 size threshold of not less than 200 m² excluded; 2026 data, source [e-Gov 503AC0000000084](https://laws.e-gov.go.jp/law/503AC0000000084)); in 注視区域 the state investigates land use and can issue 勧告/命令 against 機能阻害行為 — check 内閣府 designated zones map
- **国土利用計画法 事後届出 (Act 92/1974 — 昭和49年法律第92号)**: a buyer acquiring land ≥2,000 m² (市街化区域) / ≥5,000 m² (other 都市計画区域) / ≥10,000 m² (outside 都市計画区域) files the 利用目的 (use purpose) + price within 2 weeks of contract, **via the 市町村長 (municipality)** to the prefectural governor; the governor reviews the use purpose and may issue a **勧告 (recommendation)** if it conflicts with the land-use plan. Pre-acquisition notification (事前届出) applies only in designated 監視区域. **Applies to all buyers regardless of nationality — foreign buyers are not exempt and not specially gated**; a 2026-04-01 施行規則 amendment merely *records* a corporate acquirer's representative nationality (data capture, not an approval gate). Source: [e-Gov 法令検索 349AC1000000092](https://laws.e-gov.go.jp/law/349AC1000000092) · [MLIT 土地取引規制制度](https://www.mlit.go.jp/totikensangyo/totikensangyo_tk2_000019.html)
- **農地法 §3 (Act 229/1952 — 昭和27年法律第229号)**: acquiring ownership/lease of 農地 (farmland) requires **農業委員会 (agricultural committee) permission** — without it the contract is **void**; acquirer must farm essentially all the land (≥150 days/yr farming engagement). **Land-type-specific, not nationality-specific** — standards contain no nationality bar; a foreigner meeting the farming-utilisation conditions can be approved. Since 2023-09-01 the application form *records* nationality (data capture, not a foreigner-only gate). For rural plots also expect a 非法定 (non-statutory) **近隣説明会 (community-explanation meeting)** + local-consent practice under 都市計画法 §29/§33 + 市町村開発条例 — meetings are routine; a foreigner-only "justification hearing" is **not a statutory requirement** and would, if applied, be a discrimination concern, not a legal step. Source: [e-Gov 法令検索 327AC0000000229](https://laws.e-gov.go.jp/law/327AC0000000229) · [MAFF 農地をめぐる事情](https://www.maff.go.jp/j/keiei/koukai/wakariyasu.html)
- **借地権 (leasehold) vs 所有権 (freehold)**: 借地権 ~30–40 % est. price reduction vs 所有権 equivalent; 旧法借地権 (pre-1992) has stronger tenant protection but is muddier on inheritance
- **建ぺい率 (kenpeiritsu — building coverage)** + **容積率 (yōseki-ritsu — FAR)** zoning: rebuild rights may be smaller than current footprint if 既存不適格 (legally non-conforming) — material for plot-only / rebuild scenarios
- **円安 currency exposure**: foreign-denominated buyers riding a strong-USD/EUR wave should hedge purchase + ongoing tax bills

## Reddit / forum sources

- **r/japanlife** — most active expat community, real ownership posts
- **r/movingtojapan** — pre-relocation
- **r/JapanFinance** + wiki at `https://wiki.japanfinance.org/` — best English-language tax + mortgage primer; high-quality
- **Tokyo Cheapo** — `https://tokyocheapo.com/`
- **Real Estate Japan blog** — `https://resources.realestate.co.jp/`
- **Plaza Homes blog** — `https://www.realestate-tokyo.com/news/`
- **Housing Japan blog** — `https://housingjapan.com/blog/`

## Verification authorities

| Authority | When to call |
|---|---|
| **法務局 (Hōmukyoku — Legal Affairs Bureau)** | 不動産登記簿 verification, ownership + 抵当権 (mortgage liens) |
| **市役所 / 町村役場 — 課税課** | 固定資産税評価額, 固定資産税納税証明 |
| **市役所 / 町村役場 — 都市計画課** | 用途地域, 建ぺい率/容積率, 市街化区域/調整区域, 都市計画税 applicability |
| **市役所 / 町村役場 — 上下水道課** | Mains coverage, connection cost |
| **市役所 / 町村役場 — 建築指導課** | 建築確認 history (pre/post 1981), 既存不適格 status |
| **保健所 (hokenjō)** | 民泊 license verification + 旅館業 license |
| **国税庁 + 税務署** | 路線価, 確定申告, 譲渡所得 |
| **司法書士 (judicial scrivener)** | Final transfer, registration filing |
| **宅地建物取引士 (Takken Shujisha)** | 重要事項説明 — must be explained by licensed agent in person |
| **全国宅地建物取引業協会連合会 (ハトマーク)** + **全日本不動産協会 (ウサギマーク)** | Agent licensing verification |
| **マンション管理組合** (for condos) | 修繕積立金 status, 長期修繕計画, 大規模修繕 history |
| **内閣府 — 重要土地等調査法担当** | 注視区域 / 特別注視区域 designation check |

## Quirks to know

- **木造 (mokuzō — wood-frame)** statutory accounting life: 22 yrs (legacy) / 30 yrs (post-1989 typical); **鉄筋コンクリート造 (RC)**: 47 yrs (residential); **重量鉄骨造 (heavy steel)**: 34 yrs — these are tax depreciation lives, NOT physical longevity
- **新築 (shinchiku — brand new)** vs **築浅 (chiku-asa — recently built)** vs **中古 (chūko — secondhand)**: language matters; new-build premium is real but evaporates in 5–10 years for wood
- **Three different value concepts** for the same parcel:
  - **公示地価 (kōji chika)** — MLIT official, 1 Jan reference, ~26,000 sites
  - **路線価 (rosenka)** — NTA, ~80 % of 公示地価, used for inheritance/gift
  - **固定資産税評価額 (kotei shisanzei hyōkagaku)** — municipal, ~70 % of 公示地価, used for fixed-asset tax (revalued every 3 years; latest cycle 2024)
  - **実勢価格 (jissei kakaku)** — actual market, sometimes 1.0–1.5× 公示地価 in hot Tokyo wards
- **借地権 (shakuchiken — land leasehold)** vs **所有権 (shoyūken — freehold)**: confirm on 登記簿; 借地権 has 30–60 yr typical original term; renewal may demand 更新料 ~5–10 % land value
- **建ぺい率 / 容積率 over-build (既存不適格)**: previously legal builds may exceed current zoning — rebuild allowed only at smaller footprint
- **マンション 大規模修繕 cycle**: every ~12–15 years; if 修繕積立金 fund inadequate at the time, owner-association levies 一時金 (one-time assessment) — material risk for older condos
- **隣地境界確認 (adjacent boundary confirmation)**: many JP parcels lack clean modern survey; 確定測量図 (definitive survey diagram) recommended pre-purchase, ~¥300K–¥800K
- **道路幅員 (road width) + 接道義務 (frontage obligation, 2 m on 4 m+ road)**: 既存不適格 frontage may block rebuild — checked at 建築指導課
- **民法・不動産登記法改正 (Act 24/2021) — two separate clocks**: new owners must register an inherited property within **3 yr** of knowing of the acquisition (mandatory since **2024-04-01**; penalty up to **¥100,000**, 不登法164①; pre-2024 inheritances backstop **2027-03-31**), and owners must register an **address change within 2 yr** — that limb is **IN FORCE only since 2026-04-01**, not 2024 (penalty up to **¥50,000**, 不登法164②; pre-2026 changes backstop **2028-03-31**) ([法務省](https://www.moj.go.jp/MINJI/minji05_00599.html), 2026-08-07 verified)

## Source URL templates

| Source | URL |
|---|---|
| MLIT 不動産価格指数 | `https://www.mlit.go.jp/totikensangyo/totikensangyo_tk5_000085.html` |
| MLIT 不動産情報ライブラリ (旧 不動産取引価格情報検索) | `https://www.reinfolib.mlit.go.jp/realEstatePrices` |
| MLIT 公示地価 | `https://www.reinfolib.mlit.go.jp/landPrices` |
| NTA 路線価 | `https://www.rosenka.nta.go.jp/` |
| REINS Market Information | `http://www.reins.or.jp/` |
| 国土交通省ハザードマップポータル | `https://disaportal.gsi.go.jp/` |
| J-SHIS 確率論的地震動予測地図 | `https://www.j-shis.bosai.go.jp/` |
| 気象庁 (JMA) | `https://www.jma.go.jp/` |
| 法務局 (Hōmukyoku) | `https://houmukyoku.moj.go.jp/homu/` |
| 登記情報提供サービス | `https://www1.touki.or.jp/` |
| 国税庁 (NTA) | `https://www.nta.go.jp/` |
| 観光庁 民泊制度ポータル | `https://www.mlit.go.jp/kankocho/minpaku/` |
| 内閣府 重要土地等調査法 | `https://www.cao.go.jp/tochi-chosa/` |
| 法務省 不動産登記法改正 | `https://www.moj.go.jp/MINJI/minji05_00343.html` |
| 法務省 相続登記・住所変更登記 義務化 | `https://www.moj.go.jp/MINJI/minji05_00599.html` |
| MLIT 空家特措法 | `https://www.mlit.go.jp/jutakukentiku/house/jutakukentiku_house_tk3_000035.html` |
| MLIT 道路交通センサス | `https://www.mlit.go.jp/road/census/r3/` |
| 住宅金融支援機構 / Flat 35 | `https://www.flat35.com/` |
| 住宅性能評価・表示協会 | `https://www.hyoukakyoukai.or.jp/` |
| Bank of Japan | `https://www.boj.or.jp/` |
| SUUMO | `https://suumo.jp/` |
| at home | `https://www.athome.co.jp/` |
| HOME'S / LIFULL | `https://www.homes.co.jp/` |
| Yahoo!不動産 | `https://realestate.yahoo.co.jp/` |
| GaijinPot Apartments | `https://apartments.gaijinpot.com/en/rent` ❌ DEPRECATED — primary source removed; verify with GaijinPot Housing (commercial listings aggregator, not a government source) |
| LIFULL 空き家バンク aggregator | `https://www.akiya-athome.jp/` |

## Status

✅ **Fully populated** as of 2026-05-01.
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all anchored in MLIT / NTA / 法務局 / 国税庁 / J-SHIS / JMA / BoJ primary sources with date-stamped numerics + transparent computations.
**Confidence**: **HIGH** for cadastre/seismic-standard/national-tax/transaction-cost (all 国税庁 + MLIT primary, multi-source corroborated). **MEDIUM** for current akiya market dynamics (highly local, 1,700+ municipalities — start with municipal akiya bank for parcel-level), municipal-level minpaku rules (per-ward overlay on top of national 180-day cap; verify via 保健所), and condominium 修繕積立金 trajectory (per-building, requires 管理組合 financials review).
**Last verified**: 2026-08-07 (the two `--price` MLIT primary-source bullets re-verified 2026-09-18 — 不動産情報ライブラリ replaced the 土地総合情報システム from 1 Apr 2024; the +5.00 % YoY figure on the same section was not re-checked). BoJ policy-rate path and 重要土地等調査法 notification duty re-verified 2026-09-24 in the October regwatch wave; Flat 35 figures not re-checked. Finance / rental / tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).

## Extension TODOs (deepen on first real run)

- [ ] Per-都道府県 路線価 extraction tooling (NTA publishes annual JSON-ish PDF maps July)
- [ ] 23-ward minpaku ordinance scrape (each Tokyo 区 has its own supplementary rule)
- [ ] 自治体 akiya bank aggregator (LIFULL covers ~700+; ~1,000 municipalities still self-host)
- [ ] 1981 vs 2000 build-era flag automation from 不動産登記簿 (建築確認年月日 field)
- [ ] 重要土地等調査法 注視区域 polygon overlay (内閣府 publishes zone maps as PDF; geocoding TODO)
- [ ] 浄化槽 vs mains sewer signal extraction from listing 重要事項説明 boilerplate
- [ ] 旧法借地権 vs 新法借地権 inheritance complications playbook
