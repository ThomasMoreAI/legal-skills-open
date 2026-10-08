# 中華民國 / Taiwan 🇹🇼 — Property Due-Diligence Playbook

ISO2: `tw`. Status: ✅ Fully populated (researched 2026-05).

> Scope note: this playbook describes the legal-administrative framework as it operates from Taipei (中華民國 / Republic of China legal system). It does not take a position on cross-strait sovereignty.

## Country profile

- **郵遞區號 (postal code)**: 3+2 (or 3+3) digits. 3-digit base = 直轄市/縣市/鄉鎮市區 cluster (e.g., `100` 中正區 Taipei, `110` 信義區 Taipei, `220` 板橋區 New Taipei, `404` 北區 Taichung, `800` 新興區 Kaohsiung); the additional 2 digits (`100-01` etc.) refine to 里 (li) / 鄰 (lin). Format guide: 中華郵政 `https://www.post.gov.tw/post/internet/Postal/`
- **Admin levels**:
  - 6 直轄市 (special municipalities): 臺北市 / 新北市 / 桃園市 / 臺中市 / 臺南市 / 高雄市
  - 13 縣 (counties) + 3 市 (provincial cities — 基隆/新竹/嘉義)
  - Below: 鄉/鎮/縣轄市/區 (townships/districts) → 里 (li) → 鄰 (lin)
  - 福建省 (Lienchiang/Kinmen) and 連江縣 (Matsu) operate under same framework with frontier-zone overlays
- **Currency**: TWD (NT$). 1 EUR ≈ 33–35 TWD; 1 USD ≈ 31–33 TWD (variable Q1 2026)
- **Languages**: 國語 / 華語 (Mandarin Chinese) — official; 臺語 (Taiwanese Hokkien), 客語 (Hakka), 原住民族語 (Indigenous languages) recognised under 國家語言發展法 2019
- **Cadastre**: **內政部地政司 (Department of Land Administration, MOI)** — central authority. Per-county/city operations at **地政事務所 (Land Office)**. 32 land offices nationwide.
  - Online portal: **內政部不動產資訊平台** `https://pip.moi.gov.tw/`
  - Land registry: **地籍圖資網路便民服務系統** (cadastral map-and-data public service system, 內政部地政司 — free, no login; address/parcel/coordinate lookup, area, 公告土地現值 and 公告地價) `https://easymap.land.moi.gov.tw/Home`
  - Real-price disclosure: **不動產交易實價查詢服務網** `https://lvr.land.moi.gov.tw/`
- **Identifiers**:
  - 地號 (parcel number) — formatted as 鄉鎮市區 + 段 + 小段 + 地號 (e.g., 信義段三小段 0123-0000)
  - 建號 (building number) — separate from parcel; condos have 主建物 + 共有部分 + 附屬建物 split
  - **所有權狀** (ownership certificate) — paper title issued at 地政事務所 transfer
- **Title concept**: 所有權 (freehold) is the dominant form. 地上權 (superficies / surface right, typically 50–70 years) is used for some new BOT-style developments — material price discount and finite end-of-life value. 所有權 is what most listings advertise; 地上權 must be flagged separately on 不動產說明書.
- **Recent reforms**:
  - **房地合一稅 2.0** (Real-Estate Combined Tax 2.0) — effective 2021-07-01 (Income Tax Act §4-4, §14-4 to §14-8). Tightens short-term holding penalty (45 % <2 yrs / 35 % 2–5 yrs / 20 % 5–10 yrs / 15 % >10 yrs), closes profit-via-corporation loopholes, applies to land + building combined gain. ([MoF source](https://www.mof.gov.tw/multiplehtml/2074))
  - **房屋稅 2.0** (House Tax 2.0) — effective 2024-07-01 (taxable from FY2025, first bills May 2025). 多屋族 (multi-home owners) taxed 2.0–4.8 % on non-self-use, nationally aggregated (was 1.5–3.6 % with per-municipality counting). Self-use cap ≤3 homes nationwide at 1.0–1.2 %. ([MoF source](https://www.mof.gov.tw/house/multiplehtml/41e7424fa26e4d41905ed1800fd9fabc); [Act amendment 2023-12-19](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=G0340054))
  - **平均地權條例修正** (Equalization of Land Rights Act amendment) — effective 2023-07-01. Tightens 預售屋 (pre-sale) contract transfer (assignment of pre-sale unit now requires application + restricted to limited grounds), introduces 私法人 (private legal entity) residential-purchase approval requirement, fines 100 K – 5 M TWD for hoarding/false advertising. ([MOI source](https://www.moi.gov.tw/News_Content.aspx?n=4&s=281267))
  - **臺灣地區與大陸地區人民關係條例 §69** — PRC nationals' real-estate ownership: case-by-case 內政部 approval; max 1 residential per person; 5-year hold/sale lock; banned in defense-sensitive zones. Tightened review since 2024. ([MOI source](https://www.moi.gov.tw/News_Content.aspx?n=8&s=14670))
  - **氣候變遷因應法 (Climate Change Response Act)** — effective 2023-02-15, replacing 溫室氣體減量及管理法. Net Zero 2050 statutory goal; 碳費 (carbon fee) collection from 2024; relevant to building energy code (建築技術規則 has been progressively tightening insulation + façade requirements). ([Climate Change Response Act — MOJ law database](https://law.moj.gov.tw/ENG/LawClass/LawAll.aspx?pcode=O0020098))

## Section: `--price`

### Primary sources

- **內政部不動產交易實價查詢服務網 (Real-Price Registration / Real Estate Information Platform)** — mandatory transaction-price disclosure since 2012-08, individual-address resolution since **2021-07** (Real-Price Registration 2.0). Surveys actual closed transactions (NOT listings).
  - Portal: `https://lvr.land.moi.gov.tw/`
  - Data download (open data): `https://plvr.land.moi.gov.tw/DownloadOpenData`
  - Update cadence: monthly batches; 30-day disclosure deadline post-transfer
  - Coverage: 買賣 (sale-purchase) + 租賃 (lease) + 預售屋 (pre-sale)
- **內政部不動產資訊平台 (MOI Real Estate Information Platform)** — index series, 房價負擔能力指標 (housing affordability index), regional price stats
  - Portal: `https://pip.moi.gov.tw/`
- **公告土地現值 / 公告地價 (announced land present value / announced land value)** — set by 直轄市/縣市 政府 annually (公告地價 every 3 years). Used as 土地增值稅 + 地價稅 base. Historically ~80–90 % of market in recent years (2023 nationwide adjustment narrowed gap).
  - Portal: `https://lvr.land.moi.gov.tw/` → 公告現值/地價 search
- **房屋現值 (assessed house value)** — set by local 稅捐稽徵處 (local tax authority); base for 房屋稅 (house tax). est. ~20–40 % of market value (significant gap; varies materially by municipality and build era — verify the actual 評定現值 on the 房屋稅 bill / 稅捐稽徵處 for a specific unit; House Tax 2.0 reform did NOT raise the underlying 評定現值 directly — it raised the rate).
- **內政部營建署 (Construction and Planning Agency)** statistics on 住宅供需資訊 (housing supply/demand): `https://www.cpami.gov.tw/`

### Listing platforms (consumer-facing)

- **591房屋交易** — `https://www.591.com.tw/` — dominant: rentals, sale, pre-sale; URL pattern e.g. `https://sale.591.com.tw/home/house/detail/2/<id>.html`
- **樂屋網 (Rakuya)** — `https://www.rakuya.com.tw/`
- **好房網 (HouseFun)** — `https://www.housefun.com.tw/`
- **信義房屋 / 永慶房屋 / 住商不動產 / 太平洋房屋 / 21世紀** — major brokerage chains, each with own listings portal:
  - 信義房屋 `https://www.sinyi.com.tw/`
  - 永慶房屋 `https://buy.yungching.com.tw/`
  - 住商不動產 `https://www.hbhousing.com.tw/`
- **DDproperty Taiwan** — `https://www.ddproperty.com/zh-tw/` — English UI partial
- **Foreigner-friendly English platforms**: limited; main route is 591 + brokerage chains. **Sinyi Realty no longer operates an English front-end** — `en.sinyi.com.tw` no longer resolves and both `/en` and `/english` return 404 on the live Chinese site [sinyi.com.tw](https://www.sinyi.com.tw/) (2026-09-18 verified). Budget for a Chinese-reading agent or translator.

### Premium-area benchmarks (Q1–Q2 2025 reference, MOI 實價登錄 + 信義/永慶 房價指標)

| District / area | 2025 trend | Sale price (TWD/坪 — 1 坪 ≈ 3.306 m²; ~per m² in parens) |
|---|---|---:|
| 臺北市 信義區 (Xinyi, Taipei) | ~+5–8 % YoY | est. 1.0–2.5 M TWD/坪 (≈ 302–756 K/m²) prime |
| 臺北市 大安區 (Daan) | ~+5–8 % | est. 1.1–2.4 M/坪 (≈ 333–726 K/m²) |
| 臺北市 中正區 (Zhongzheng) | ~+4–6 % | est. 0.9–1.8 M/坪 (≈ 272–544 K/m²) |
| 臺北市 中山區 (Zhongshan) | ~+4–6 % | est. 0.8–1.5 M/坪 (≈ 242–454 K/m²) |
| 臺北市 內湖區 (Neihu) | ~+5–7 % (tech corridor) | est. 0.7–1.2 M/坪 (≈ 212–363 K/m²) |
| 新北市 板橋區 (Banqiao) | ~+6–9 % | est. 0.55–0.95 M/坪 (≈ 166–287 K/m²) |
| 新北市 新莊區 / 三重區 | ~+7–10 % | est. 0.45–0.8 M/坪 (≈ 136–242 K/m²) |
| 桃園市 中壢區 / 桃園區 | ~+8–12 % (TSMC + AI corridor heat) | est. 0.30–0.55 M/坪 (≈ 91–166 K/m²) |
| 新竹市 / 新竹縣 竹北市 (Hsinchu Science Park) | ~+10–15 % YoY (highest national heat 2024–25) | est. 0.55–0.95 M/坪 竹北 (≈ 166–287 K/m²); est. 0.65–1.3 M/坪 新竹市 prime |
| 臺中市 西屯區 (七期) | ~+8–12 % | est. 0.55–1.0 M/坪 (≈ 166–302 K/m²) |
| 臺中市 北屯區 / 北區 | ~+7–10 % | est. 0.30–0.55 M/坪 |
| 臺南市 安平區 / 東區 | ~+6–9 % | est. 0.25–0.50 M/坪 (≈ 75–151 K/m²) |
| 高雄市 鼓山區 / 苓雅區 | ~+6–10 % (post-S-curve 半導體 corridor) | est. 0.30–0.65 M/坪 (≈ 91–196 K/m²) |
| 花蓮 / 臺東 (east coast) | mixed; post-2024 quake softness | est. 0.15–0.35 M/坪 (≈ 45–106 K/m²) |

⚠️ All per-坪 ranges above are **est.** ranges synthesized from 信義房價指標 + 永慶房屋市場分析 + 591 listing aggregates Q1–Q2 2025; verify any specific address against 實價登錄 last 12 months same 街/巷 + 大樓.

### Compute

1. Listing price → TWD/坪 = listing price ÷ 主建物坪數. **Critical**: distinguish 主建物 (main building, exclusive) vs 公設坪數 (common-area share, often 25–35 % of total registered area on 大樓 condos). Pre-2018 buildings: 雨遮 (eave) + 屋簷 (cornice) historically counted; post-2018 reform: 雨遮不登記不計價 (eaves no longer registered or priced).
2. Compare to 實價登錄 last 4 quarters, same 路段 / 大樓 / 同棟 → most reliable comp baseline.
3. Compare to 公告土地現值 for 土地增值稅 base (sets the LVIT floor).
4. Cross-check 房屋現值 (house tax base) at 稅捐稽徵處 — reveals official assessed value for House Tax 2.0 calculation.
5. **Trap**: 公設比 (common-area ratio) — older 公寓 (5-floor walk-ups, pre-1985) often 5–10 %; newer 大樓 with gym/pool/lobby 30–35 %. A "30 坪" listing with 32 % 公設 = ~20 坪 actually exclusive. ALWAYS pull 不動產說明書 to see the breakdown.
6. **Trap**: 預售屋 (pre-sale, off-plan) prices average ~10–20 % above 新成屋 (new completed) and ~20–35 % above 中古 (resale) at same district — partially because of forward-pricing build-cost inflation, partially developer margin. 房地合一稅 2.0 since 2021-07 + 平均地權條例 2023-07 reform tightened pre-sale assignment to curb 紅單 flipping.
7. **Trap**: 違建 (illegal build) — rooftop additions (頂樓加蓋) and balcony enclosures common; older buildings sometimes >50 % of unit. 違建 has zero registered value, may be priority demolition target, NOT mortgageable; insist on 建物登記謄本 cross-check vs site visit.

### Trend Q4 2024 → Q1 2026

- 2024-07 House Tax 2.0 took effect; first bills issued May 2025 → multi-home owners saw material increase, some sell-down pressure on non-self-use inventory in 2025
- 央行 (CBC) successive macroprudential tightening rounds (Jun 2023, Jun 2024, Sep 2024) cooled investor leverage particularly in Taipei + New Taipei
- TSMC + 台積電 supply-chain expansion in 新竹 / 高雄 / 嘉義 / 桃園 → southern + northwest corridor outperforms Taipei core 2024–25
- 2024-04-03 Hualien M7.4 earthquake: localized softness east coast; minimal national-level impact

---

## Section: `--traffic`

### Primary source

- **交通部統計處 (Department of Statistics, MOTC)** — annual + quarterly traffic data
  - Portal: `https://www.motc.gov.tw/en`
  - Statistical yearbook (交通統計要覽): `https://www.motc.gov.tw/ch/home.jsp?id=63&parentpath=0,6`
- **交通部公路局 (Highway Bureau, MOTC)** — provincial highway 省道 + national freeway 國道 traffic
  - Portal: `https://www.thb.gov.tw/`
  - Real-time + 12-hour averages: 公路防救災通報處置系統
- **臺灣高速公路局 (National Freeway Bureau)** — 國道 (national freeways: 國道1號 中山高 / 國道3號 福高 / 國道5號 蔣渭水 / 國道6號 水沙連 etc.)
  - Real-time portal: `https://1968.freeway.gov.tw/`
- **直轄市/縣市 交通局** — municipal road registers (Taipei 交通局 `https://www.dot.gov.taipei/`, Kaohsiung 交通局 `https://www.tbkc.gov.tw/`, etc.)

### Key term

**日交通量 (daily traffic volume)** — measured at 偵測器 (detector loops) on major roads. **小時交通量 (hourly volume)** for peak analysis. Functionally equivalent to AADT.

### Verdict bands (rough)

- 🟢 < 1,000 v/d (quiet 巷弄 / residential lane)
- 🟡 1,000–10,000 v/d (collector road / 次要幹道)
- 🟠 10,000–40,000 v/d (主要幹道 / 省道 inland)
- 🔴 > 40,000 v/d (urban arterial / 國道 / 快速道路 / 環河快速)

### Coarse fallback

OSM `highway` class:
- motorway = 國道 (national freeway)
- trunk = 省道 / 快速公路 (provincial highway / expressway)
- primary = 縣道 + urban arterial
- secondary = 鄉道 / 市區次幹道
- tertiary = 鄰里道路 main
- residential = 生活巷弄

⚠️ Apartment-on-arterial 噪音 is the primary mid-band concern. 二環 (Second Ring) and 高架橋 (elevated highway) noise carries 15–30 m beyond façade. 鼎泰豐-busy night-market lanes have low traffic count but high pedestrian/scooter noise — the count alone misses this.

---

## Section: `--tax`

### Annual property tax — three-layer system

**Owner as of 8/31 (assessment date, 房屋稅 starting 2024-07-01 reform) and 11/1 (地價稅) is liable.** Bills:

- **地價稅 (Land Value Tax)** — annual, billed November, payable by 11/30
- **房屋稅 (House Tax 2.0)** — annual, billed May (first 2.0 bills May 2025), payable by 5/31
- **地價稅 + 房屋稅** are SEPARATE; the building portion of a parcel is taxed by 房屋稅, the land portion by 地價稅

### 地價稅 (Land Value Tax — 土地稅法 §16-§22)

Base: 課稅地價 (taxable land value) = 公告地價 (set every 3 years, current cycle 2023–2025).

| Use | Rate |
|---|---|
| **自用住宅用地** (self-use residential, ≤700 m² urban / ≤1,500 m² rural, ≤2 lots per household, owner+spouse+minor-children residence registered) | **0.2 %** (1‰ statutory minimum × 2) |
| 一般用地 (non-self-use residential, base) | **1 %** progressive lower band |
| 一般用地 (累進稅率 progressive) | up to **5.5 %** at top band |
| 公共設施保留地 | 0.6 % |
| 工業用地 / 加油站 | 1 % |

Source: [財政部稅務入口網 — 地價稅](https://www.etax.nat.gov.tw/etwmain/web/ETW113W/), [土地稅法](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=G0340001).

### 房屋稅 2.0 (House Tax 2.0 — 房屋稅條例, effective 2024-07-01)

Base: 房屋現值 (assessed house value) — set by 直轄市/縣市 不動產評價委員會 every 3 years; revaluation cycle currently being accelerated under House Tax 2.0 to push base toward market rate.

| Use | Rate (House Tax 2.0, post-2024-07-01) |
|---|---|
| **自用住宅 — ≤3 homes nationwide (single household)** | **1.0 %** (county-set; statutory range 1.0–1.2 %) |
| **自用住宅 — 4th home onwards** | **2.0–4.8 %** progressive on non-self-use band (varies by 縣市) |
| **公益出租人 (registered subsidized landlord)** | 1.2 % |
| **一般出租住家 (commercial rental, non-subsidized)** | **1.5–2.4 %** (was 1.5–3.6 % pre-2.0; 2.0 narrowed top to discourage hoarding-via-rental) |
| **多屋族 非自住** | **2.0–4.8 %** (was 1.5–3.6 %); aggregated NATIONALLY across all 縣市 (was per-municipality pre-2024) |
| **空置住宅** (vacant, no occupancy proof) | top-band **4.8 %** at owner's third unit upwards |
| **營業用** (commercial) | 3.0 % |
| **私人醫院/事務所** | 1.5–2.0 % |
| **建商餘屋** (developer leftover, ≤2 yrs) | reduced 2.0 % cap; >2 yrs → standard non-self-use rate (this clause closed the developer-hoarding loophole) |

Source: [財政部 — 房屋稅2.0](https://www.mof.gov.tw/htmlList/103), [房屋稅條例 (latest 2023-12-19)](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=G0340102).

### Example calculations (worked, transparent inputs)

**Example A: 30-坪 (~99 m²) 信義區 condo, market price 30 M TWD, 房屋現值 5 M, 公告地價 of land share 1.5 M, single self-use first home**

- 地價稅 (self-use 0.2 %): 1.5 M × 0.2 % = **3,000 TWD/yr**
- 房屋稅 (self-use 1.0 % under 2.0): 5 M × 1.0 % = **50,000 TWD/yr**
- **Total ~53,000 TWD/yr (~1,580 EUR/yr)** for self-use 1st home
- *If the same unit is the owner's 4th non-self-use home in 2025+ assessment*: 房屋稅 jumps to 5 M × 4.8 % = **240,000 TWD/yr** under House Tax 2.0 top band
- *Plus*: ground-rent equivalent in a 50-yr 地上權 product → additional monthly fee, not applicable for 所有權

**Example B: 25-坪 (~83 m²) 板橋區 公寓 (5-storey walkup, no elevator, 1985 build), market price 12 M TWD, 房屋現值 1.2 M, 公告地價 of land share 1.0 M, owner-occupied first home**

- 地價稅 (self-use): 1.0 M × 0.2 % = **2,000 TWD/yr**
- 房屋稅 (self-use 1.0 %): 1.2 M × 1.0 % = **12,000 TWD/yr**
- **Total ~14,000 TWD/yr (~420 EUR/yr)** — older buildings have low 房屋現值 (depreciated), driving low effective rate

### Transaction taxes (one-time)

| Tax | Rate | Base |
|---|---|---|
| **契稅 (Deed Tax — buildings only, paid by buyer)** | **6 %** standard sale; 4 % auction; 2 % rebuild → 1 % gift, 0.5 % exchange | 房屋現值 (assessed building value, NOT market) — typically 20–40 % of market, so effective burden ~1.2–2.4 % of market |
| **印花稅 (Stamp Duty)** | **0.1 %** on contract value (公定契紙) | contract face |
| **登記費 (Land Registration Fee)** | **0.1 %** | 申報地價 + 房屋現值 |
| **書狀費 (certificate fee)** | NT$80 / certificate | flat |
| **代書費 (Land Administration Agent fee — 地政士)** | typically NT$15,000–NT$50,000 residential | flat schedule |
| **仲介服務報酬 (broker commission, max statutory)** | **buyer 1–2 %** + **seller 4 %** typical, capped at **6 % combined** by 不動產經紀業管理條例 §19 | sale price |

Source: [財政部稅務入口網 — 契稅](https://www.etax.nat.gov.tw/), [契稅條例](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=G0340075), [不動產經紀業管理條例](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0060073).

### 土地增值稅 (Land Value Increment Tax — LVIT, paid by SELLER, on land portion only)

Triggered on every land transfer. Base: 漲價總數額 (total appreciation) = current 公告土地現值 − previous-transfer 公告現值 × CPI factor − qualified improvement costs.

| Holding bracket | Rate (general) | Rate (self-use 自用住宅 once-per-lifetime + repeat) |
|---|---|---|
| Tier 1 (≤100 % appreciation vs base) | **20 %** | 10 % (self-use) |
| Tier 2 (100–200 %) | **30 %** | 10 % (self-use) |
| Tier 3 (>200 %) | **40 %** | 10 % (self-use) |

⚠️ 自用住宅 LVIT 10 % discount: once-per-lifetime preferential rate, with conditions: ≤300 m² urban / ≤700 m² rural, owner+spouse+minor-children registered residence ≥1 yr pre-sale, NOT used for rent/business in past year. Repeat-use after 2010 amendment: subsequent self-use sales also qualify for 10 % under specific conditions.

Source: [土地稅法 §28-§40](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=G0340001), [財政部 LVIT briefing](https://www.mof.gov.tw/htmlList/2074).

### 房地合一稅 2.0 (Real-Estate Combined Tax 2.0, paid by SELLER, on building + land combined gain — effective 2021-07-01)

Applies to real estate acquired on or after **2016-01-01** (ie. mostly all current transactions). 2.0 reform (effective 2021-07-01) extended punitive short-hold rates from 1 yr to 2 yr, closed 私法人 corporate loophole, expanded scope to pre-sale unit assignments.

| Holding period (residents — individual) | Rate |
|---|---|
| ≤2 years | **45 %** |
| 2–5 years | **35 %** |
| 5–10 years | **20 %** |
| > 10 years | **15 %** |
| Self-use 自住 (owner+spouse+minor-child registered ≥6 yrs, gain ≤4 M TWD) | **10 %** + 4 M TWD exemption |

| Holding (FOREIGN individuals — non-residents) | Rate |
|---|---|
| ≤2 years | **45 %** |
| > 2 years | **35 %** flat (no further taper) |

| 私法人 (private legal entity) | Rate |
|---|---|
| ≤2 years | 45 % |
| 2–5 years | 35 % |
| > 5 years | 20 % (post-2.0; was 17 % pre-reform) |

Source: [所得稅法 §4-4, §14-4 to §14-8](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=G0340003), [財政部 房地合一稅2.0 explainer](https://www.mof.gov.tw/multiplehtml/2074).

### Inheritance tax (遺產稅) — moderate exposure

Progressive **10 % → 15 % → 20 %** on net estate above exemption. Basic exemption: **13.33 M TWD (single)** + **spouse deduction 5.33 M (FY2025, raised from 4.93 M in FY2024)** + adult dependant 50 K each + minor child increments + funeral 1.38 M (indexed; verify yearly at 國稅局) (2026-05-27 verified, source: [eTax Portal MOF — Exemption and Deduction Table](https://www.etax.nat.gov.tw/etwmain/en/announcement/alien-individual-income-tax/exemption-deduction-table); [NTBT Estate and Gift Tax](https://www.ntbt.gov.tw/English/multiplehtml/a0c8c4ba5dbd4cc882bcc1bc1ef49ffa))

Source: [遺產及贈與稅法](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=G0340072), [財政部國稅局 inheritance briefing](https://admin.taiwan.net.tw/english).

### Future risk

- **House Tax 2.0** roll-out: 房屋現值 (assessed base) revaluation cycles being accelerated 2025–2027 in some 縣市 (current base set in 2024 cycle for many municipalities) — owner can see effective bill jump 1.5–3× even at unchanged rate
- 房地合一稅 third-tier amendment under discussion to align 私法人 short-hold rate with individual; not yet enacted
- **Pre-sale market squeeze**: 平均地權條例 2023-07 reform effectively killed 紅單 (red-slip pre-sale flipping); ongoing enforcement strengthens
- **Foreigner CGT**: 35 % flat (>2 yrs) is significantly stiffer than resident long-term 15–20 % — non-trivial buyer-side consideration

---

## Section: `--rental`

### Long-term residential (出租住宅 / 租賃住宅)

- **租賃住宅市場發展及管理條例** (2018-06-27, effective 2018-06-27) — modernized residential lease framework: defines 包租代管 (sub-lease/management) operators, requires registration, creates 公益出租人 reduced-tax tier
- **民法 §421-§463** — civil-code base of 租賃 contract; standard 1–2 yr term; 押金 (deposit) statutory cap 2 months
- **內政部不動產資訊平台 — 租金實價登錄** since 2024-07-01 — mandatory rent disclosure for properties brokered/managed by 不動產經紀業 + 包租代管, plus household-direct lease above certain thresholds. Portal `https://lvr.land.moi.gov.tw/`.
- **Customary tenant payments at signing**:
  - 押金 (deposit): 2 months — statutory cap is **土地法 §99** (Land Act Art. 99), mirrored by 租賃住宅市場發展及管理條例; 民法 §432 covers tenant's duty of care, NOT deposits (2026-05-27 verified, source: [law.moj.gov.tw — 土地法](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=G0060001))
  - 仲介費 (agent fee): typically **half-month each side** (negotiable; cap 1.5 months total per 不動產經紀業管理條例)
  - 保證人 (guarantor): often required — 連帶保證 (joint guarantor) or 履約保證金 (performance deposit) substitution
  - 公證費 (notarization): optional but increasingly used for high-rent leases; ~3,000–10,000 TWD
- **Income tax on rental** — personal **綜合所得稅** progressive 5–40 %; **公益出租人** registration drops effective rate via 0.43× revenue assumption (vs default 0.43× expenses-deduction; specifics annual)
- Yields (Q1 2026, gross — derived ratio of 實價登錄租金 ÷ 實價登錄買賣 price):
  - **臺北市 大安/信義/松山**: **est. 1.8–2.5 %** (yields among lowest in OECD-comparable markets)
  - **臺北市 outer + 新北市 板橋/中和/新莊**: **est. 2.5–3.2 %**
  - **桃園/新竹/竹北 (科技走廊)**: **est. 2.8–3.5 %**
  - **臺中 西屯/北屯**: **est. 3.0–4.0 %**
  - **臺南/高雄 prime**: **est. 3.5–4.5 %**
  - **東部 花蓮/臺東**: **est. 4.0–5.5 %** but illiquid
  - ⚠️ All yield bands above are **est.** rent-÷-price ratios; verify any specific address by pairing the same 街/巷/大樓 rent and sale 實價登錄 records (租金實價登錄 portal cited above) over the last 12 months.

### Short-term rentals (民宿 + 旅館業)

**Three legal pathways**:

| Regime | Statute | Cap | Notes |
|---|---|---|---|
| **民宿 (B&B-style, ≤8 rooms / ≤240 m² combined)** | 民宿管理辦法 (2017 amendment) under 發展觀光條例 | no nightly cap | OWNER-OCCUPIED requirement in many zones; strict zone/use restrictions — only in 風景特定區 / 觀光地區 / 原住民族地區 / 偏遠地區 / 離島地區 / 休閒農業區 / 國家公園 / 非都市土地使用分區. **Forbidden in pure 都市計畫住宅區** unless specific overlay. License at 觀光署 (formerly 觀光局) via 縣市政府觀光局 |
| **旅館業 (Hotel/Inn) + 一般旅館 / 觀光旅館** | 發展觀光條例 §24 + 旅館業管理規則 | no cap | Full hotel zoning required (商業區/旅館用地). Building must satisfy 旅館 facility code (fire, accessibility). Hard for residential conversion |
| **公寓大廈管理條例 §16** override | n/a | n/a | Apartment-building 管理委員會 (HOA) can ban any commercial / minpaku-style use via 規約 majority vote — very common in modern 大樓; check 規約 BEFORE buying intending STR |

⚠️ **KEY TRAP**: pure 都市計畫住宅區 condos in Taipei/New Taipei/Taichung/Kaohsiung **CANNOT legally operate Airbnb-style STRs**. Most listings on Airbnb in central Taipei marked "Apartment" are operating either (a) without license = illegal, fines NT$100K–NT$500K under 發展觀光條例 §55-2 + crackdown active 2023-2026 (b) under 民宿 license in zones that don't actually qualify (also illegal). Actually-legal urban STR generally requires 旅館業 license + commercial-zoned building — high barrier.

### Tax + reporting obligations (民宿)

- **Income**: 不動產租賃收入 if traditional lease; **執行業務 / 營業 income** if running 民宿 with services
- **營業稅 (5 % VAT)**: registered if revenue > NT$200K/month (mandatory 營業人); below = 小規模營業人 1 % rate
- **觀光旅館登記證 / 民宿登記證** must be displayed on every Airbnb/Booking/Agoda listing — observably enforced via platform takedowns since 2022
- **觀光署 民宿管理資訊系統**: `https://taiwanstay.net.tw/` — license verification

### Strategic notes

- **Airbnb in Taipei City limits**: assume regulatorily borderline; due-diligence MUST verify 規約 + zoning + license; treat any "passive STR yield" pitch as red flag
- **Legitimate STR routes**: 民宿 in 宜蘭/花蓮/臺東/南投/臺南安平/澎湖/金門/馬祖 destinations are well-trodden; permit timeline 2–6 months
- **Hualien/Taitung post-2024 quake**: tourism-driven recovery; STR pipeline is large but require seismic-retrofit verification

---

## Section: `--work=<profession>`

### Job platforms

- **104人力銀行** — `https://www.104.com.tw/` — dominant; broadest mid-career
- **1111人力銀行** — `https://www.1111.com.tw/`
- **518熊班** — `https://www.518.com.tw/` — entry-level + service sector strong
- **CakeResume / Cake** — `https://www.cake.me/` — tech-leaning, English-friendly, startup-tilt
- **Yourator** — `https://www.yourator.co/` — startup/digital
- **LinkedIn Taiwan** — strong for IT, finance, multinational, English-language
- **公部門徵才** — `https://web3.dgpa.gov.tw/want03front/AP/WANTF00001.ASPX` (civil service) + `https://www.taiwanjobs.gov.tw/` (台灣就業通, MoL public)

### Self-employment regimes

- **小規模營業人** (small-scale operator, monthly revenue ≤ NT$200K): 1 % monthly business tax, simplified bookkeeping
- **營業人** (general business person, monthly revenue > NT$200K): 5 % 營業稅 (VAT), 統一發票 (uniform invoice) requirement, double-entry bookkeeping
- **執行業務所得 (professional practice income)**: 律師/會計師/醫師/建築師 etc. — 9305 expense rate by default
- **個人綜合所得稅** progressive **5/12/20/30/40 %** (2024 brackets); standard deduction NT$131,000 single, itemised alternative
- **勞健保 (Labor + National Health Insurance)**: self-employed enrol via 公會 (professional association) or 國民年金/國保 minimum tier; ~NT$1,000–NT$2,500/month at base
- **二代健保補充保費**: 2.11 % surcharge on certain non-salary income types

### Foreign worker visa interface (cross-section to `--visa`)

- **Employment Gold Card (就業金卡)** — Employment Service Act §46 + 外國專業人才延攬及僱用法. 4-yr work + residency + tax discount (50 % deduction on income > NT$3M for first 5 yrs, 外國專業人才減免). 8 talent fields: Science/Tech, Economics, Education, Culture-Arts, Sports, Finance, Law, Architecture+Design — plus a National Development Council "specialty" route. **No investment requirement.** ([NDC source](https://goldcard.nat.gov.tw/))
- **APRC (Alien Permanent Resident Certificate)** — 5 yrs continuous residence ≥183 d/yr; salary requirement (typically ~2× minimum wage); no investment requirement
- **Investment Visa (投資居留簽證)** — NT$6 M minimum capital invested in approved Taiwan business; 居留證 issued, path to APRC at 5 yrs
- **Plum Blossom Card / 紫梅花卡** — special-talent permanent residence for senior professionals (proof of contribution/recognition)
- **Entrepreneur Visa (創業家簽證)** — startup founders; lower capital threshold
- **就業金卡 Gold Card** is increasingly the favored route for tech/finance/professional foreign buyers

### Salaried benchmarks (median monthly gross 2024–2025, 主計總處)

- 臺北市: ~NT$50,000–NT$70,000 (median FT, all-industry, pre-tax); top quartile NT$80K–NT$120K
- 新北市/桃園/新竹: ~NT$45,000–NT$65,000
- 臺中: ~NT$40,000–NT$55,000
- 高雄/臺南: ~NT$38,000–NT$50,000
- 東部 (花蓮/臺東): ~NT$32,000–NT$42,000
- **基本工資 (national minimum wage, 2026-01-01)**: **NT$29,500/month, NT$196/hr** (+3.18 %; announced 2025-09-26 by Minimum Wage Deliberation Committee; the NT$28,590 / NT$190 figures applied through 2025) (2026-05-27 verified, source: [Ministry of Labor news release no. 84](https://english.mol.gov.tw/21139/40790/87087/))
- **TSMC + 半導體 corridor**: well above median; senior engineers NT$2M–NT$4M annual all-in incl. RSU is common

### Catchment heuristics

- Within 60 min HSR (高鐵) of 台北車站: full white-collar catchment (Taipei + New Taipei + 桃園 + 新竹 corridor)
- Within 60 min 捷運 (MRT) Taipei station: prime catchment, salary +20 % vs corridor
- 臺中/臺南/高雄 metro 60 min: regional employment access; cost-of-living benefit
- East coast (花蓮/臺東) + outlying islands: thin labour market; remote-friendly + Mandarin critical

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **內政部消防署 災害潛勢地圖** (NFA disaster-potential map) | `https://www.nfa.gov.tw/` | Earthquake / flood / landslide / debris-flow potential — overlay any address |
| **災害潛勢資料整合應用平台 (CDPP) — 國家災害防救科技中心** | `https://dmap.ncdr.nat.gov.tw/` | NCDR consolidated multi-hazard portal — primary one-stop tool |
| **中央氣象署 (CWA)** — 地震 + 颱風 + 即時氣象 | `https://www.cwa.gov.tw/` | Active hazard + historical typhoon track + real-time seismic |
| **國家地震工程研究中心 (NCREE)** — 土壤液化潛勢 (soil liquefaction potential) | `https://www.liquid.net.tw/` and `https://www.ncree.org/` | Soil liquefaction maps — critical post-2016 美濃地震 + 2018 花蓮地震 + 2024 花蓮地震 |
| **經濟部地質調查及礦業管理中心** (CGS-MMA) — 活動斷層 (active fault) | `https://www.geologycloud.tw/` | 36 documented active faults; nationwide 1:25,000 map |
| **農業部農村發展及水土保持署 (ARDSWC — Rural Development and Soil and Water Conservation Agency, Ministry of Agriculture)** — 山坡地 + 土石流 (slope land + debris flow) | `https://246.ardswc.gov.tw/` (土石流及大規模崩塌防災資訊網) | Debris-flow torrent identification; **1,753 土石流潛勢溪流** (debris-flow potential torrents) registered (2026 data, source 農業部農村發展及水土保持署; 2026-09-18 verified) |
| **經濟部水利署** — 淹水潛勢圖 (flood potential map) | `https://fhy.wra.gov.tw/` | Flood inundation depth/recurrence at 1:25,000 |
| **環境部 (MOENV)** — 土壤污染 (soil contamination) | `https://sgw.moenv.gov.tw/public` | Contaminated/listed-control sites + groundwater |
| **TCCIP (Taiwan Climate Change Information Platform)** — Academia Sinica + NCDR | `https://tccip.ncdr.nat.gov.tw/` | Climate projections, downscaled scenarios SSP1-2.6 / SSP5-8.5 |

### Earthquake — verdict bands (rough, by 中央氣象署 設計地震動 + Academia Sinica seismic-hazard mapping)

- 🟢 西部離島 (澎湖/金門/馬祖) — lowest historical seismicity
- 🟡 西部平原 (彰化/雲林/嘉義 inland, 桃園 north) — medium
- 🟠 北部 (Taipei Basin) — moderate but **soft-basin amplification** is the key concern (2024 Hualien-event shaking in Taipei amplified ~2× over rock outcrop)
- 🔴 東部 (花蓮/臺東) + 中央山脈西緣 (車籠埔 / 梅山 / 屯子腳) + 高雄 旗山-美濃 fault zone — high

### 2024-04-03 花蓮地震 (M7.4) — calibration

- Largest Taiwan event since 1999 集集 (M7.6, 921 quake)
- Epicentre: 花蓮縣 ~25 km offshore east coast
- Casualties: **19 deaths** (final confirmed Jan 2025 after last 2 missing AU/SG dual-national tourists declared deceased + remains located; 7+ via mountain landslide; 11 Taroko Gorge tourists; magnitude per CWA Mw 7.4 / USGS M 7.4, local ML 7.2) (2026-05-27 verified, source: [Wikipedia: 2024 Hualien earthquake — cross-references CWA + Hualien County Govt + AP](https://en.wikipedia.org/wiki/2024_Hualien_earthquake))
- Damage: 花蓮市 several mid-rise tilt/collapse (建築物軟弱層 + soft-storey patterns); national signal that **pre-1997 + soft-storey + lateral-asymmetric ground floors remain leading collapse mode**
- ⚠️ Implication for buyers: building inspection report (耐震評估報告) for any pre-1999 building is now de-facto market standard; some banks have started conditioning on it

### Typhoon

- 1–2 direct strikes typical per year (May–Nov peak Aug–Sep); one in 5 years a Cat-4-equivalent landfall
- Coastal east + south + Hengchun Peninsula highest exposure; central mountain spine deflects west-coast urban centres
- 2024 typhoons: 凱米 Gaemi (Jul 2024) — Kaohsiung major flood; 山陀兒 Krathon (Oct 2024) — Hengchun southern impact

### Build-era hazards (the watershed)

| Era | Code basis | Hazard rating |
|---|---|---|
| **Pre-1974 (no modern seismic code)** | first 建築技術規則 1974 onward | 🔴 **Significant risk** — no statutory seismic provision; many 公寓 walkups in central Taipei/Tainan/Kaohsiung urban cores |
| **1974–1989** | 1974 規則 + initial seismic provisions | 🟠 Old code; 1989 revision strengthened lateral resistance |
| **1989–1997** | post-1989 + post-1995 revision | 🟡 Improved but still **pre-921 code** |
| **1997–1999 boundary** | 1997 revision | 🟡 Last pre-921 revision |
| **Post-1999 (post-921, late 1999 emergency revision)** | post-1999 集集 quake emergency code amendment, 2003 code | 🟢 Modern; enforces capacity-design + ductile detailing; **THE 1999 watershed is the single most material datum** |
| **Post-2011** | 2011 + 2015 + 2019 progressive revisions | 🟢 Stricter near-fault zones, soft-storey checks |

⚠️ **Soft-storey 軟弱層 (loose ground floor with retail/parking)** is endemic to Taiwan condo design and the dominant pre-1999 collapse pattern; structural 牽引補強 retrofit required in many older buildings — public retrofit subsidy programs from 內政部 + 縣市政府 ongoing.

### Soil liquefaction

- After 2016 美濃 earthquake, 經濟部 published nationwide 土壤液化潛勢 map 2017
- High-potential zones: 南臺灣 (Tainan, Kaohsiung, Pingtung coastal alluvium); 東部 (Yilan plain, Hualien-Taitung valleys); 臺北 西區 (Wanhua, Datong — old riverbed); 嘉南平原 coastal
- Portal: `https://www.liquid.net.tw/` — address-level lookup
- ⚠️ Zone designation does NOT mean "will liquefy" — it indicates vulnerability under specific shaking + groundwater conditions; nonetheless material on disclosure

### Mandatory disclosures (at sale)

| Document | Required because | Source |
|---|---|---|
| **不動產說明書** | 不動產經紀業管理條例 §22 — broker-prepared, must be presented BEFORE contract | Cover: ownership, mortgage, urban planning, 違建 status, 凶宅/事故宅, leak history, 嫌惡設施 within radius |
| **不動產現況確認書** (Current Condition Confirmation) | broker standard | seller's known defects, leaks, mortgages, neighbour disputes |
| **建物登記謄本 + 土地登記謄本** | 地政事務所 issued | ownership, encumbrances, area, area-vs-actual variance |
| **使用執照 + 建造執照** | 建築管理 | original use permit, last large reno permit |
| **土壤液化查詢報告** | optional but increasingly requested | liquefaction zone status |
| **耐震評估報告** | optional, increasingly demanded for pre-2000 | seismic assessment, often the basis of bank LTV decision |
| **公寓大廈規約 + 區分所有權人會議紀錄** (for condos) | 公寓大廈管理條例 | HOA rules, fund balance, recent meeting minutes |

Source: [不動產經紀業管理條例](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0060073), [公寓大廈管理條例](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0070118).

### Earthquake insurance (住宅地震保險)

- Run by **臺灣住宅地震保險基金 (TREIF)** — public-private scheme, government as ultimate backstop. Mandatory bundle with 火險 for mortgaged residential.
- Coverage: 150 萬 TWD building total-loss + 20 萬 temporary accommodation; premium ~NT$1,350/yr flat regardless of building (uniform pricing)
- Voluntary excess (擴大版地震險): 200 萬–600 萬+ buildings, ~NT$3,000–NT$15,000/yr depending on area + age
- Source: [TREIF](https://www.treif.org.tw/)

### Climate change projections (TCCIP + 氣候變遷因應法)

- TCCIP RCP4.5: Taiwan annual mean temperature **+1.0–1.5 °C** by 2050, **+1.5–2.0 °C** by 2100; RCP8.5: **+1.8–2.5 °C** by 2050, **+3.5–4.5 °C** by 2100
- Heat-wave days TX≥35 °C: Taipei expected 2–3× by 2050; Kaohsiung 1.5–2×
- Typhoon intensity: rising; track shift slightly northward; Cat-4-equivalent frequency rising
- Sea-level rise: +0.3–0.5 m by 2100 RCP4.5; +0.5–0.9 m RCP8.5 — Tainan-Kaohsiung coast + Yilan plain + west-coast estuaries most exposed
- Precipitation: extreme rain (1-hr 50 mm+) +20–30 % frequency by 2050; dry-season prolonged
- Source: [TCCIP](https://tccip.ncdr.nat.gov.tw/), [國家氣候變遷調適行動計畫 2023-2026](https://www.cca.gov.tw/)

---

## Section: `--mains`

### National database

- **內政部營建署 — 公共設施管理資訊系統** + **經濟部水利署** + **公共給水普及率統計**: `https://www.cpami.gov.tw/`, `https://www.wra.gov.tw/`
- **臺灣自來水公司 (Taiwan Water Corporation)** — operates 自來水 in all of Taiwan EXCEPT Taipei City
  - Portal: `https://www.water.gov.tw/`
  - Coverage: ~98 % nationwide for drinking water (2023, MOEA)
- **臺北自來水事業處 (Taipei Water Department)** — Taipei City only
  - Portal: `https://www.water.gov.taipei/`
- **下水道 (Sewer)**:
  - 直轄市 + 縣市 公共下水道系統 — most operated by city/county 工務/水利 局
  - **公共污水下水道接管率 (sewer connection rate, MOEA / CPAMI)**: ~63 % nationwide (2023); but **heavily skewed**:
    - 臺北市: 99 %
    - 新北市: ~85 %
    - 桃園/臺中/高雄: 60–80 %
    - 臺南: ~55 %
    - 鄉村縣市: 20–40 %
- Where mains sewer absent: 化糞池 (septic tank, 三化糞池) — regulated by 建築技術規則 + 環境部; periodic clean-out required.

### Verification

1. Listing language:
   - 自來水 / 公水 = mains water
   - 山泉水 / 井水 = spring/well water (rural; verify potability + flow)
   - 公共下水道 / 接管 = mains sewer
   - 化糞池 / 自設化糞池 = septic tank (most non-Taipei older properties)
2. Confirm via 直轄市/縣市 工務局 / 自來水公司 営業所 / 衛生下水道工程處 — request 接管證明 (connection certificate) or 水費繳費紀錄 (water bill record)
3. **不動產說明書** § 給排水 must specify

### Costs (typical 2026)

| Scenario | Cost (TWD) |
|---|---:|
| Connection where mains available | NT$8,000–NT$30,000 |
| Mains sewer extension to property (if road has trunk, residential) | NT$50,000–NT$200,000 |
| 化糞池 install (5-人標準, new) | NT$60,000–NT$150,000 |
| 化糞池 annual clean-out + maintenance | NT$3,000–NT$10,000 every 1–3 yrs |
| 化糞池 → mains sewer conversion | NT$80,000–NT$250,000 |
| 井水 / 山泉水 → 自來水 conversion (rural) | NT$30,000–NT$200,000 + main extension cost (variable, road-dependent) |

---

## Cost benchmarks (TW 2026)

| Item | Cost (TWD) |
|---|---:|
| 代書 (Land Administration Agent, residential transfer) | NT$15,000–NT$50,000 |
| 仲介服務報酬 (broker, max statutory combined) | up to **6 %** combined buyer+seller |
| 印花稅 (stamp duty) | 0.1 % × contract value |
| 契稅 (deed tax) | 6 % × 房屋現值 |
| 登記費 (registration) | 0.1 % × (申報地價 + 房屋現值) |
| 履約保證 (escrow / settlement guarantee, 0.05–0.1 %) | NT$5,000–NT$30,000 typical |
| 火險 + 地震基本險 (mortgaged property; standard) | NT$3,000–NT$15,000/yr equivalent |
| 火險擴大條款 / 颱風洪水險 add-on | NT$5,000–NT$30,000/yr per coverage tier |
| 公寓大廈管理費 (HOA monthly) | NT$1,000–NT$5,000/mo (typical 大樓 NT$50–NT$120/坪/mo) |
| 修繕基金 / 公共基金 (sinking fund, monthly per 公寓大廈管理條例 §18) | NT$200–NT$1,500/mo typical |
| Light renovation (interior cosmetic, 30 坪) | NT$1.5M–NT$3M |
| Mid-renovation (replumb + rewire + finishes, 30 坪) | NT$3M–NT$6M |
| Full structural retrofit (耐震補強, pre-1999 condo) | NT$2M–NT$6M (per unit pro-rata of 整棟工程) |
| **Total transaction cost (buyer side, residential)** | **~3–5 % of price** (lower than JP/EU; commission paid by both sides splits load) |

## Active fiscal incentives (2025–26)

- **青年安心成家購屋優惠貸款 (First Home Loan for Young Households)** — 3 banks (土地銀行 / 中信房貸 etc.) under 內政部 program; up to NT$10M loan, 0.265–0.4 % below benchmark, 30-year term, max NT$10M loan, eligible 18–45 yrs first-home. ([內政部 source](https://www.moi.gov.tw/))
- **新青安貸款 (New Young Households Plan)** — 2023-08 launched; more aggressive subsidy: NT$10M cap, 40-yr term, 5-yr interest grace, 0.25–0.5 % rate cut. **Modified Aug 2024 + Jun 2025** to limit speculative use.
- **危老建築重建獎勵 (Aged + Hazardous Building Reconstruction Incentive)** — 都市危險及老舊建築物加速重建條例 (2017, amended 2020 + 2023): up to **30 % FAR bonus + 1.3× building bulk** for qualifying old-building rebuilds; faster permit; combined with 都更 (urban renewal). ([CPAMI source](https://www.cpami.gov.tw/最新訊息/危老重建專區/))
- **都市更新 (Urban Renewal)** — 都市更新條例; 容積獎勵 + 稅捐減免 for qualifying integrated rebuilds; lengthy 4–10+ yr timeline due to 100 % consent or 法定多數 thresholds
- **節能家電貨物稅退減** — energy-star A/C + fridge buyback NT$2,000/unit (rolling)
- **綠建築標章** — EEWH-RN (residential renovation) certified upgrades qualify for some 都更 / 危老 bonus calculations
- **房屋稅自住 1.0 % 優惠** — House Tax 2.0 self-use ≤3 nationwide preferential rate (vs 2.0 % standard) is the single biggest standing incentive

## Common listing platforms

- **591房屋交易** (`https://www.591.com.tw/`) — dominant; sale + rental + pre-sale
- **樂屋網** (`https://www.rakuya.com.tw/`)
- **好房網** (`https://www.housefun.com.tw/`)
- **信義房屋** (`https://www.sinyi.com.tw/`)
- **永慶房屋** (`https://buy.yungching.com.tw/`)
- **住商不動產** (`https://www.hbhousing.com.tw/`)
- **DDproperty Taiwan** (`https://www.ddproperty.com/zh-tw/`) — partial English UI
- **內政部不動產交易實價查詢服務網** (`https://lvr.land.moi.gov.tw/`) — primary closed-deal source

## Caveats unique to TW

- **Foreign buyers face a reciprocity test** — 土地法 §17–§19 restricts foreign nationals to citizens of countries that grant Taiwan citizens reciprocal real-estate rights; 內政部 publishes the reciprocity list annually. Forbidden categories (regardless of reciprocity): 林地, 漁地, 狩獵地, 鹽地, 礦地, 水源地, 要塞軍備區, 邊境地. Confirm current reciprocity status for your nationality at 內政部 BEFORE offer. ([Land Act §17–§19 — law.moj.gov.tw](https://law.moj.gov.tw/ENG/LawClass/LawAll.aspx?pcode=D0060001))
- **PRC nationals**: 臺灣地區與大陸地區人民關係條例 §69 applies — case-by-case 內政部 approval, max 1 residential per individual, 5-yr hold/sale lock, banned in defense-sensitive areas. Tightened since 2024.
- **房地合一稅 2.0 35 % flat rate for foreigners holding >2 yrs** vs 15–20 % for residents long-term — material drag on foreign-buyer ROI; factor BEFORE offer
- **公設比 (common-area ratio)** is a Taiwan-specific quirk: a "30 坪" listing with 33 % 公設 = ~20 坪 actually exclusive; ALWAYS demand the breakdown on 不動產說明書
- **The 1999 (post-921, post-集集) seismic-code watershed is the single most material datum** in build-year diligence — confirm 建造執照 date NOT 完工 date
- **凶宅 (incident home / haunted house)** disclosure is contractually required (不動產說明書 §13) — non-disclosure is a common dispute basis; 凶宅查詢網 + 591 凶宅標記 for cross-check; pricing discount est. ~20–40 % (market-anecdotal — no central registry of 凶宅 discounts; figure varies widely by case severity, locality, and time since incident)
- **違建 (illegal additions)** are widespread — rooftop builds, balcony enclosures, pillared shop awnings; 違建 has zero registered area, may be priority demolition target; insist on 建物登記謄本 vs site visit cross-check
- **Pre-sale 預售屋 unit assignment heavily restricted post-2023-07** — 紅單 flipping effectively dead; buyers must hold to handover or qualify for 5 strict carve-outs
- **Mortgage CBC macroprudential** (post Sep 2024 7th-round selective credit control): **2nd-home LTV cap 50 % NATIONWIDE** (was 60 % in specific areas only); **3rd-home + high-value LTV 30 %** (was 40 %); **no grace period (寬限期) on 1st-home loans if borrower already owns another property**; tightening waves Jun 2023 + Jun 2024 + Sep 2024 (2026-05-27 verified, source: [CBC 2024-09-19 7th-round release](https://www.cbc.gov.tw/dl-212229-22f1e175e8ca45d7949c8f29dd777ce4.html))
- **No real-estate-based golden visa** — Investment Visa requires NT$6M actual operating-business capital, NOT property; buying a NT$30M condo for visa does NOT work
- **No estate-based residency**: APRC requires **physical presence** ≥ 183 d/yr × 5 yrs continuous; Gold Card is the favored white-collar path
- **典型住宅貸款 "宽限期" 5-yr interest-only** is common but tightening; CBC moral suasion 2024+ has narrowed bank tolerance for 寬限期 stacking with multi-property buyers
- **建商保固 (developer warranty)**: 1 yr structure-watertight + 5 yr structure standard; 預售屋 履約保證 required since 2007 reform — verify which of 5 mechanisms (價金信託/同業連帶/公會連帶/履約保證金/不動產開發信託) before signing
- **居住正義 (housing justice)** is an active political theme (2025–26); expect more rounds of macroprudential + tax tightening on multi-property holders

## Reddit / forum sources

- **r/Taiwan** + **r/taiwanese** — broad Taiwan expat
- **r/taiwan_living** — practical living, occasional housing
- **PTT 房屋板 (home-sale)** — `https://www.ptt.cc/bbs/home-sale/index.html` — most active TW housing forum (Mandarin); high signal-to-noise for buyer experiences + agent reviews
- **PTT Realestate 板** — `https://www.ptt.cc/bbs/home-sale/index.html` — investor-tilt
- **Mobile01 居家房事討論區** — `https://www.mobile01.com/topiclist.php?f=356` — broad consumer; renovation + dispute heavy
- **Forumosa.com** — `https://forumosa.com/` — long-running English expat forum
- **FB Group: Taiwan Foreign Real Estate Buyers / 在台外國人買房** — practical FB groups (verify activity)

## Verification authorities

| Authority | When to call |
|---|---|
| **內政部地政司** + **地政事務所** | 不動產登記 verification, ownership + 抵押權 (mortgage liens) + 地籍 query |
| **直轄市/縣市 稅捐稽徵處** | 房屋現值, 房屋稅 status, 地價稅 status |
| **直轄市/縣市 工務局 + 都市發展局** | 建造執照 / 使用執照 history, 違建 status, 都市計畫使用分區 |
| **建築管理工程處 / 都發局 違建查報隊** | 違建 enforcement queue priority |
| **直轄市/縣市 工務局 衛生下水道工程處** | Mains sewer coverage, connection certificate |
| **觀光署 (formerly 觀光局)** + 縣市觀光單位 | 民宿 / 旅館業登記 verification |
| **財政部國稅局** + **地方稅務局** | 房地合一稅, 土地增值稅, 契稅 |
| **代書 / 地政士** | Final transfer, registration filing — TW does NOT use notary system |
| **不動產經紀人 / 經紀營業員** (licensed) | 不動產說明書 — must be prepared and explained by licensed broker |
| **中華民國不動產仲介經紀商業同業公會全國聯合會** | Broker licensing verification |
| **公寓大廈管理委員會** (for condos) | 規約, 公共基金 status, 主任委員會 minutes, 整修紀錄 |
| **內政部 (大陸事務 office)** | PRC-national approval (Cross-Strait Act §69) |
| **中央銀行 (CBC) 業務局** | Foreign-exchange settlement procedures, FX bring-in declarations |

## Quirks to know

- **坪 (ping)** = 3.30579 m² — universal property-area unit; 1 坪 = ~6 榻榻米 (tatami) heritage unit. ALWAYS convert from 坪 to m² for cross-country comparison.
- **公設比 (common-area ratio)** is a TW invention — 主建物 + 附屬建物 + 公設 split on 建物登記; 公設 typically counted in price but not exclusive. Older 公寓 (5-flr walk-up): 5–10 % 公設; modern 大樓 with gym/pool/lobby: 30–35 %. **A 30-坪 listing with 33 % 公設 = ~20 坪 actually private.**
- **三種價值 / Three value concepts** for the same parcel:
  - **公告土地現值 (announced present value)** — annual, set by 直轄市/縣市, used for 土地增值稅 (LVIT) base
  - **公告地價** (announced land value) — every 3 years, used for 地價稅 (Land Value Tax) base
  - **房屋現值** (assessed house value) — set by local 不動產評價委員會 every 3 years, used for 房屋稅 + 契稅 base
  - **市場價** (market price) — actual; 實價登錄 closes the gap between assessed and market
- **所有權 vs 地上權 (freehold vs surface right)** — 地上權 50–70 yr products on BOT-style developments traded at est. ~30–50 % discount vs 所有權 (discount depends heavily on remaining lease term — a 地上權 with ~20 yr left discounts far more than one with ~65 yr left); finite end-of-life; check 地上權契約 carefully before offer
- **預售屋 / 新成屋 / 中古屋** language: 預售屋 = pre-sale (off-plan, paid in instalments during construction); 新成屋 = new completed (≤2 yrs); 中古屋 = secondhand
- **都市更新 / 危老重建** ("urban renewal" / "aged + hazardous rebuild") — adjacent old buildings often combine into integrated rebuild for FAR bonus; participating units get larger replacement unit but timeline 4–10+ yrs and tens of thousands of consents to assemble
- **凶宅 (incident home)** disclosure: 不動產說明書 §13 requires disclosure of suicides/homicides/unnatural deaths; 凶宅查詢網 + 591 community markings can verify
- **建商保固** (developer warranty): 1 yr structure-watertight + 5 yr structure on 預售屋; demand 履約保證 evidence
- **房屋稅 + 地價稅** are 兩套單 different bills + different schedules; do not confuse — and remember they can be in name of different family member if 戶籍 is split
- **契約自簽 vs 履約保證** — TW historically had escrow gaps; current standard is 履約保證 (settlement guarantee) for purchase price flow via designated trustee; verify which of 5 mechanism types is used
- **戶籍 (household registration)** is critical — 自用住宅 tax preferential rates require 戶籍 of owner/spouse/minor-child registered at the address; one transfer of 戶籍 to claim self-use status is a common audit trigger
- **2024 央行 RMBS pull-back**: banks tightened LTV + scrutiny; some require dual income proof for second home; treat any "easy financing" pitch as red flag

## Source URL templates

| Source | URL |
|---|---|
| 內政部不動產資訊平台 | `https://pip.moi.gov.tw/` |
| 實價登錄 (real-price) | `https://lvr.land.moi.gov.tw/` |
| 實價登錄 open data download | `https://plvr.land.moi.gov.tw/DownloadOpenData` |
| 內政部地政司 | `https://www.land.moi.gov.tw/` |
| 地籍圖資網路便民服務系統 | `https://easymap.land.moi.gov.tw/Home` |
| 財政部稅務入口網 | `https://www.etax.nat.gov.tw/` |
| 財政部 (MoF) | `https://www.mof.gov.tw/` |
| 全國法規資料庫 (laws) | `https://law.moj.gov.tw/` |
| 內政部 (MOI) | `https://www.moi.gov.tw/` |
| 中央氣象署 (CWA) | `https://www.cwa.gov.tw/` |
| 國家災害防救科技中心 (NCDR) | `https://www.ncdr.nat.gov.tw/` |
| CDPP 災害潛勢平台 | `https://dmap.ncdr.nat.gov.tw/` |
| 國家地震工程研究中心 (NCREE) 土壤液化 | `https://www.liquid.net.tw/` |
| 經濟部水利署 淹水潛勢 | `https://fhy.wra.gov.tw/` |
| TCCIP (climate) | `https://tccip.ncdr.nat.gov.tw/` |
| 觀光署 (民宿/旅館) | `https://taiwanstay.net.tw/` |
| 內政部營建署 (CPAMI) | `https://www.cpami.gov.tw/` |
| 中央銀行 (CBC) | `https://www.cbc.gov.tw/` |
| Employment Gold Card | `https://goldcard.nat.gov.tw/` |
| 國家發展委員會 (NDC) | `https://www.ndc.gov.tw/` |
| 591房屋交易 | `https://www.591.com.tw/` |
| 信義房屋 | `https://www.sinyi.com.tw/` |
| 永慶房屋 | `https://buy.yungching.com.tw/` |
| 住商不動產 | `https://www.hbhousing.com.tw/` |
| 樂屋網 | `https://www.rakuya.com.tw/` |
| 好房網 | `https://www.housefun.com.tw/` |
| DDproperty Taiwan | `https://www.ddproperty.com/zh-tw/` |
| TREIF (earthquake insurance) | `https://www.treif.org.tw/` |
| PTT home-sale | `https://www.ptt.cc/bbs/home-sale/index.html` |

## Status

**Confidence**: HIGH

**Last verified**: 2026-05-27 (debris-flow agency and torrent count, cadastral-portal name and Sinyi English front-end corrected 2026-09-18 per 246.ardswc.gov.tw + moi.gov.tw + sinyi.com.tw)

**Researched by**: Sonnet 4.6 + Opus 4.7 (parallel-subagent batch, 2026-05)

**Notes**: All headline tax rates (房屋稅 2.0, 房地合一稅 2.0, 土地增值稅, 契稅), the 1999 (post-921) seismic-code watershed, the foreign-buyer reciprocity framework (土地法 §17-§19), Cross-Strait §69 PRC restrictions, the 平均地權條例 2023-07 pre-sale assignment reform, and 公設比 mechanics are anchored in 全國法規資料庫 + 財政部 + 內政部 + 央行 primary sources with date-stamped numerics. Per-district price benchmarks (信義/大安/竹北/西屯/苓雅 etc.) are 2025-Q1/Q2 estimates synthesized from 信義房價指標 + 永慶房屋 + 591 listings + 實價登錄 — flagged `est.` and bounded; verify any specific address against 實價登錄 last 12 months same 路段/大樓 before offer. STR (民宿) urban viability assessment treats apartment-zoned units as regulatorily borderline and recommends 規約 + zoning verification before any STR-yield assumption — pure 都市計畫住宅區 condos generally cannot legally operate Airbnb-style STR. Foreigner CGT 35 % flat rate for >2-yr holding is a non-trivial drag vs resident 15–20 % long-term; 6 M TWD Investment Visa is the property-adjacent (but NOT property-based) residency route, with Gold Card the favored white-collar alternative. 2024-04-03 花蓮 M7.4 earthquake (Taiwan's largest since 1999 集集) reinforced post-1999 build-era as the single most material seismic datum.

## Extension TODOs (deepen on first real run)

- [ ] Per-縣市 公告地價 + 公告現值 query tooling (內政部 publishes annual tables)
- [ ] 違建 priority-list scrape (each 直轄市 工務局 publishes 違建查報隊 priority queue separately)
- [ ] 凶宅查詢網 + 591 凶宅 cross-reference automation for 不動產說明書 §13 verification
- [ ] 公寓大廈規約 standard-clause extraction (STR ban / pet ban / renovation rule patterns)
- [ ] 危老重建 + 都更 eligibility flag from 建造執照 date + 結構安全評估 result
- [ ] 土壤液化潛勢 polygon overlay (NCREE publishes 1:25,000 zone maps as web service; address-level lookup TODO)
- [ ] 實價登錄 open-data delta watcher (monthly batches → comp-list refresh per address)
- [ ] Foreign-buyer reciprocity-list change watcher (內政部 annual update)
- [ ] CBC macroprudential round tracker (Jun 2023 / Jun 2024 / Sep 2024 → ongoing tightening cadence)
