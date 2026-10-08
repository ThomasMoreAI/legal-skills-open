# 中国 / China (Mainland PRC) 🇨🇳 — Property Due-Diligence Playbook

ISO2: `cn`. Status: ✅ Fully populated (researched 2026-05).

> **Scope**: Mainland People's Republic of China only. **Hong Kong SAR** has its own playbook (`countries/hk/playbook.md`); **Macao SAR** has its own playbook (`countries/mo/playbook.md`); **Taiwan (ROC)** has its own playbook (`countries/tw/playbook.md`). Each operates a separate legal, tax, currency, and land-tenure system. This playbook does not cover any of them.

## Country profile

- **Population**: ~1.408 billion (2025 estimate, [National Bureau of Statistics — NBS](https://www.stats.gov.cn/english/)); first sustained natural decline began 2022; UN median projection ~1.39B by 2030
- **GDP per capita**: ~US$13,300 nominal (2024, NBS / IMF); real GDP +5.0 % full-year 2024 (NBS); +4.6–5.0 % 2025 official target
- **Currency**: **CNY / RMB (¥, 人民币)** — managed-float against undisclosed CFETS basket; PBOC publishes daily central parity ([PBOC fixings](http://www.pbc.gov.cn/)); USD/CNY trading band ±2 % around fix; offshore deliverable variant **CNH** trades freely in Hong Kong / Singapore / London. 1 EUR ≈ 7.7–8.0 CNY (Q1–Q2 2026 indicative); 1 USD ≈ 7.1–7.3 CNY
- **Languages**: Standard Mandarin / Putonghua 普通话 (de jure national common language under the [国家通用语言文字法](http://www.moe.gov.cn/jyb_sjzl/sjzl_zcfg/zcfg_jyfl/202606/t20260605_1438880.html), passed 31 Oct 2000 and **revised 27 December 2025 by the 19th session of the 14th NPC Standing Committee, in force 1 January 2026** — 5 chapters, 32 articles; art. 2 now states that Putonghua and standardised Chinese characters 是国家法定全国通用的语言文字) (2026 data, source 中华人民共和国教育部 / 国家法律法规数据库; 2026-09-18 verified); written **Simplified Chinese (简体)** in mainland use since the 1956–1986 reforms; recognised regional / minority languages (Cantonese 粤语, Wu 吴语, Tibetan, Uyghur, Mongolian, Zhuang, etc.) coexist locally
- **Postcode**: 6 digits (e.g., Beijing CBD `100020`, Shanghai Pudong Lujiazui `200120`, Shenzhen Futian `518000`); first 2 digits identify the province / municipality
- **Admin levels**: 4 国家直辖市 (province-level municipalities — 北京 Beijing, 上海 Shanghai, 天津 Tianjin, 重庆 Chongqing) + 23 省 (provinces) + 5 自治区 (autonomous regions: 内蒙古 Inner Mongolia, 广西 Guangxi, 西藏 Tibet, 宁夏 Ningxia, 新疆 Xinjiang) + 2 SARs (HK + Macao, separate playbooks). Below province: 地级市 (prefecture-level city) → 区/县/县级市 (district / county / county-level city) → 乡/镇/街道 (township / town / sub-district) → 村/居委会 (village / residential committee)
- **Cadastre**: **自然资源部 (Ministry of Natural Resources, MNR)** — `https://www.mnr.gov.cn/` — operates the **不动产登记 (Real-Estate Unified Registration)** system since 2015 reform; per-property record at the **不动产权证书 (Real-Estate Title Certificate)** level. Day-to-day searches at the **不动产登记中心 (district-level Real-Estate Registration Center)** in person; online lookup via local **政务服务网** portals (e.g., Beijing: `https://banshi.beijing.gov.cn/`)
  - Pre-2015 legacy paperwork: **房产证 (House Property Certificate)** + **国有土地使用证 (State-Owned Land Use Right Certificate)** — being merged into unified 不动产权证书; verify both still match
- **Identifier**: 不动产单元号 (real-estate unit number) at the parcel + building + unit level; older records carry separate 房屋所有权证 + 土地使用证 numbers
- **Title concept** — **THE CRITICAL POINT**: there is **NO private freehold over land** in the People's Republic of China. All urban land is owned by the **state** ([1982 Constitution Art. 10 § 1](https://www.gov.cn/guoqing/2018-03/22/content_5276318.htm)); all rural / collective land is owned by **village collectives**. Private actors hold a **time-limited 土地使用权 (Land Use Right, LUR)** granted by 出让 (grant / paid transfer) — typical residential term **70 years** (commercial 40, industrial 50). Buildings on top are owned outright; land is leasehold-equivalent
  - **Statutory hierarchy** (2026-05-27 verified, source: NPC database): Constitution Art. 10 (1982) → **土地管理法 (Land Administration Law 1986, last amended 2019)** → **城市房地产管理法 (Urban Real Estate Administration Law 1994, last amended 2019; short form 房地产管理法)** → **民法典 Book II 物权 (Civil Code 2021)** — the latter **absorbed the prior 物权法 (Property Rights Law 2007)**, which is no longer in force as a standalone statute.
  - **Civil Code (民法典) Art. 359 § 1** (effective 2021-01-01): when residential LUR expires, it **shall be automatically renewed**; renewal-fee provisions deferred to "future laws and administrative regulations" — i.e., **the renewal mechanism is statutorily promised but the price is undefined**. Verify: [Civil Code text 中国人大网](http://www.npc.gov.cn/npc/c30834/202006/75ba6483b8344591abd07917e1d25cc8.shtml); analysis: [Cushman & Wakefield 2024](https://www.cushmanwakefield.com/en/greater-china/insights/blog/navigating-mainland-chinas-land-use-right-renewal-landscape)
  - Commercial / mixed-use 40-year LURs do NOT enjoy automatic renewal under Art. 359; renewal terms negotiated with local government on expiry, with documented precedents requiring a fresh land-grant payment
- **Foreign-buyer rule** — governed by [建设部/商务部/外汇局 171号文 2006 (Opinion No. 171 of 2006)](http://www.mohurd.gov.cn/) plus local-government implementation. Headline regime, post-September 2024 nationwide easing:
  - Foreign individual must **live, work or study in China continuously for ≥ 1 year** to be eligible (residence permit Z / X / Q1 / R-class typically required; tourist L visa not eligible)
  - **One residential property per foreign individual nationwide**, for **own residential use only** — no rental as a foreign-individual landlord under 171号文; in practice rental enforcement varies by city, but the rule is on the books
  - Local overlay in tier-1 cities (post-Sept 2024 easing; verify with the relevant 住建委 — local Housing Bureau):
    - **北京 (Beijing)**: non-Beijing-Hukou residents (incl. foreigners) require **1 consecutive year** of social-security or individual-income-tax payment **citywide** — 京建发〔2026〕400号 (issued 7 Aug 2026, in force 8 Aug 2026 — [北京市人民政府](https://www.beijing.gov.cn/zhengce/zhengcefagui/202608/t20260807_4814015.html)) cut the inside-5th-Ring requirement from 2 yrs to 1 yr, superseding the 2-yr-inside / 1-yr-outside split of 京建发〔2025〕565号 (in force 24 Dec 2025); unit counts unchanged — **1 unit** inside the 5th Ring (+1 for multi-child families), and parents gifting a Beijing home to their children no longer trigger a qualification check on the child; the **5-year** figure is the PRE-reform value (cut to 3 yrs inside / 2 yrs outside from 1 Oct 2024, then to 2 / 1 yrs, then to 1 yr citywide). Since **8 Aug 2025** purchases **outside** the 5th Ring are unlimited in number for 1-yr payers (400号 limb verified 2026-09-24 on beijing.gov.cn; unit counts per the Beijing Housing Commission page + beijing.gov.cn interpretation; earlier limbs 2026-08-07 verified)
    - **上海 (Shanghai)**: **1 year** continuous social security / individual-income-tax, now **citywide** — outside the outer ring cut 3 yrs → 1 yr from **1 Oct 2024** (unit cap removed 26 Aug 2025, 沪建房管联〔2025〕417号); inside the outer ring cut 3 yrs → 1 yr only from **26 Feb 2026** (沪七条). 3-yr payers may buy **1 extra** unit inside the outer ring; holders of a 5-yr 《上海市居住证》 may buy **1 home citywide with no social-security or IIT proof**. Foreigners follow the same rule plus the 171号文 1-year residence requirement (2026-08-07 verified, source: Shanghai Housing Bureau)
    - **深圳 (Shenzhen)**: **1-year** social security, **not 3** — 深建字〔2024〕284号 (eff. 1 Oct 2024) required 1 yr only in 福田 / 罗湖 / 南山 and 宝安 新安+西乡 streets, and nothing elsewhere; 深建字〔2025〕199号 (eff. 6 Sep 2025) made 罗湖, 宝安 (excl. 新安), 龙岗, 龙华, 坪山 and 光明 **unlimited in number** for 1-yr payers, capped non-payers at **2 units** there, kept 福田 / 南山 / 宝安-新安 at **1 unit** for 1-yr payers, and dropped purchase-qualification checks entirely in 盐田 and 大鹏; 深建字〔2026〕86号 (eff. 30 Apr 2026) then let qualifying families (hukou, and non-hukou with ≥1 yr social security / IIT) buy **1 additional unit** in 福田 / 南山 / 宝安-新安 (so **2 units** there for 1-yr non-hukou payers) and let non-hukou families holding a valid 深圳经济特区居住证 buy **1 unit** there (2026-08-07 verified; 深建字〔2026〕86号 limb added 2026-09-24, source: Shenzhen Housing Bureau)
    - **广州 (Guangzhou)**: **all home-purchase restrictions abolished** from **30 Sep 2024 00:00** (穗府办函〔2024〕65号) — no purchase-qualification check and **no unit cap** citywide; confirmed still in force (2026-08-07 verified, source: Guangzhou municipal notice) ([CNBC 2024-09-30](https://www.cnbc.com/2024/09/30/china-property-stocks-rally-after-major-cities-ease-homebuying-restrictions.html)); only the foreign-individual 171号文 1-year rule remains
    - All other Tier-1+/Tier-2/Tier-3 cities: home-purchase restrictions **fully removed** as of late 2024–2025 ([China Index Academy via gov.cn](https://english.www.gov.cn/policies/policywatch/202412/22/content_WS67675cbac6d0868f4e8ee30f.html)) — foreigners still subject to 171号文 1-year rule and one-property-nationwide cap
  - **HK / Macao / Taiwan residents**: treated more favourably than foreign-passport holders under [国发办 2001/12 + 2019 G-B-A 港澳台居民居住证 reforms](http://www.gov.cn/) — broadly equivalent to mainland citizens for residential purchase (no 1-year rule; subject to local Hukou-style rules only)
  - **HK + Macao FX-settlement preferential rule** (formerly HK / Macao residents only) was **rolled out nationwide 15 Sep 2025** (SAFE Notice on Cross-Border Investment Reform; see § `--currency`) — overseas individuals lawfully resident and working in China can settle FX for property purchase based on the contract at the initial stage. Verify against [SAFE 国家外汇管理局 announcements](https://www.safe.gov.cn/en/)
- **Visa**: NO citizenship-by-investment. Property ownership does NOT confer residence rights. Property-relevant pathways:
  - **Z visa / Work Residence Permit (居留许可)** — for employed foreigners; renewed with employer; counts toward 1-year 171号文 residence
  - **X visa** (X1 long-term study, X2 short-term) — student stay; X1 holders eligible for 171号文 1-year rule
  - **Q1 / Q2 / S1 / S2 visas** — family reunion; long-term spouse / dependant of citizens or PRs counts toward 1-year residence
  - **R visa** — high-talent (科技人才 / "Foreign High-End Talent" A-class); fast-tracked; no statutory threshold but minimum salary, qualification, or innovation criteria via [科技部 (MOST)](http://www.most.gov.cn/) — the 国家外国专家局 / SAFEA nameplate is retained externally but SAFEA ceased to be a standalone body in the 2018 State Council reorganisation, and work-permit processing moved to MOHRSS at [12333.gov.cn](https://www.12333.gov.cn/) on 3 Jun 2024
  - **Permanent Residence (永久居留, "Chinese Green Card", 中国绿卡)** — administered by **国家移民管理局 (NIA, National Immigration Administration)** via `https://www.nia.gov.cn/`; eligibility tracks (investment ≥ US$500K continuous 3 yrs in encouraged sectors; key R&D / talent; family reunion; 4-yr work + tax-payment in China). Total grants since 1985 estimated at < 30,000 individuals through 2024 — extremely selective in absolute terms
  - PR holders: roughly equivalent to citizens for property purchase (no 1-year rule; may purchase multiple properties subject to local restrictions)

## Section: `--price`

### Primary sources

- **国家统计局 (NBS, National Bureau of Statistics)** — `https://www.stats.gov.cn/english/`
  - **70-City Newly-Built Commercial Residential Sales Price Index** — monthly, the canonical official Chinese house-price gauge; published ~15th of each month; 70 sample cities split Tier-1 / Tier-2 / Tier-3
  - English releases: `https://english.www.gov.cn/archive/statistics/`
  - Latest monthly press release (e.g., Mar 2026 [scio.gov.cn](http://english.scio.gov.cn/pressroom/2026-04/16/content_118441356.html)): 70-city new-home prices –3.4 % YoY, –0.2 % MoM
- **住房和城乡建设部 (MoHURD, Ministry of Housing & Urban-Rural Development)** — `https://www.mohurd.gov.cn/` — sector policy, transaction volumes, "保交楼" (delivered-housing) progress reports
- **人民银行 (PBOC)** — `http://www.pbc.gov.cn/` — mortgage rates (LPR-linked since Aug 2019), household leverage, credit data
- **中指研究院 / China Index Academy (CIA)** — `https://industry.fang.com/` — private but widely cited; 100-city price index, transaction volume tracking
- **克而瑞 / CRIC (China Real-estate Information Corporation)** — `https://www.cric.com/` — private; developer-side league tables
- **中房网 / China Real Estate Association** — `http://www.fangchan.com/` — semi-official sector body data

### Listing platforms (consumer-facing)

- **贝壳找房 / Beike (Beike Zhaofang)** — `https://www.ke.com/` — KE Holdings; merged 链家 (Lianjia) self-operated brokerage + open-platform agency network; **transaction-data overlay (成交价) via 历史成交查询** is the closest mainland equivalent to a public caveat database; coverage strong in Tier-1 / new Tier-1 cities, thinner in Tier-3/4 *(per listing — verify against 不动产登记中心 records)*
- **链家 / Lianjia** — `https://www.lianjia.com/` — KE Holdings owned-brokerage brand; same data backend as Beike *(per listing — verify)*
- **安居客 / Anjuke** — `https://www.anjuke.com/` — 58.com-owned (now part of 58 Tongcheng); aggregated agency listings *(per listing — verify)*
- **58同城 / 58.com** — `https://www.58.com/` — classifieds; high noise *(per listing — verify; widely flagged for stale and re-posted listings)*
- **房天下 / Fang.com (formerly SouFun)** — `https://www.fang.com/` — long-running portal; new-home developer marketing strong *(per listing — verify)*
- **Q房网 / Q-Fang** — `https://www.qfang.com/` — Shenzhen / Guangzhou strong *(per listing — verify)*
- **我爱我家 / 5i5j** — `https://www.5i5j.com/` — Beijing / Shanghai strong *(per listing — verify)*

> ⚠️ Platform listings in mainland China are seller- / agent-controlled and contain a **non-trivial share of "sham listings"** (假房源) — units no longer for sale, deliberately mispriced for lead generation, or never on market. The 2018 MoHURD crackdown (虚假房源治理) modestly improved data quality on Beike/Lianjia (which back-checks against own-brokerage transaction database), but fewer than 5–10 % of listings on most portals are guaranteed live-and-priced-as-stated. Always cross-check with at least 2 platforms + an in-person agent visit + the registered transaction price (成交价) at 不动产登记中心.

### Tier-1 city benchmarks (Q1–Q2 2026 reference, NBS 70-city index + Beike/Lianjia transaction overlays — listing platforms; verify with cadastre)

| Tier-1 city | New-home price band (¥/m², central districts est.) | Resale band (¥/m², est.) | YoY trend Mar 2026 (NBS) |
|---|---|---|---|
| 北京 (Beijing — 西城/东城/朝阳/海淀 core) | ~70,000–150,000 ¥/m² (¥7-15万) | ~60,000–130,000 ¥/m² | new –2.1 %; resale –4 to –6 % YoY |
| 上海 (Shanghai — 黄浦/静安/徐汇/浦东陆家嘴) | ~90,000–180,000+ ¥/m² (Lujiazui prime up to ¥20万+) | ~80,000–150,000 ¥/m² | new +3.7 % (only Tier-1 still positive); resale flat-to-down |
| 深圳 (Shenzhen — 福田/南山/罗湖) | ~80,000–150,000 ¥/m² (南山科技园区 highest) | ~70,000–130,000 ¥/m² | new –5.5 %; resale –6 to –8 % |
| 广州 (Guangzhou — 天河/越秀/海珠) | ~40,000–80,000 ¥/m² (CBD 珠江新城 top) | ~35,000–70,000 ¥/m² | new –4.7 %; resale –5 to –7 % |

| New-Tier-1 / strong Tier-2 (Yicai 2025 ranking, **unofficial**) | Indicative new-home (¥/m²) | Note |
|---|---|---|
| 杭州 Hangzhou | ~30,000–60,000 (CBD) | Tech / Alibaba HQ premium; resale active |
| 成都 Chengdu | ~15,000–30,000 (CBD) | Largest single-city stock among Tier-2 |
| 苏州 Suzhou | ~25,000–45,000 (CBD) | Yangtze Delta tier; foreign-buyer-friendly |
| 南京 Nanjing | ~25,000–45,000 (CBD) | Government / education base |
| 武汉 Wuhan | ~12,000–25,000 (CBD) | Central China hub |
| 西安 Xi'an | ~12,000–25,000 (CBD) | Northwest hub |
| 重庆 Chongqing (municipality) | ~12,000–22,000 (CBD) | One of two property-tax pilot cities |
| 天津 Tianjin (municipality) | ~15,000–28,000 (CBD) | Beijing satellite |

> All values are **wide indicative bands** drawn from NBS 70-city index trend + Beike / Lianjia / Anjuke listing aggregates Q1–Q2 2026. **Sham-listing risk is material** — always cross-verify with: (a) NBS 70-city ratio for the city, (b) at least 5 recent Beike 历史成交 transactions in the same compound (小区), (c) an on-the-ground agent visit. Listing platforms typically run **5–15 % above last transacted price** because asking ≠ done.
> **Tier classification is unofficial.** The Chinese government does not publish a tier-system. The most-cited list comes from **Yicai (第一财经)** annually, and is widely accepted but is not a regulatory definition. Use tiers for benchmarking only, not for legal categorisation.

### Compute

1. ¥/m² = listing price ÷ **建筑面积 (gross built area)** — Chinese convention; includes the unit's share of common space (公摊面积) for apartments. Newer Tier-1 stock typically 75–80 % efficiency (套内 / 建筑); older 1990s–2000s stock can drop to 60–70 %
2. Cross-check: pull last 5–10 成交 (closed transactions) for the same 小区 (residential compound) on Beike 历史成交 → median ¥/m² gives instant fairness band
3. **Trap**: 建筑面积 (gross) vs 套内面积 (interior, tile-to-tile) vs 实用面积 (usable) — listings mix these freely; older listings often understate by quoting only 套内. Always reconcile both
4. **Trap**: developer brochures quote 总价 + 单价 (total price + per-area); the 单价 is on 建筑面积; effective interior ¥/m² is 25–35 % higher
5. **Trap**: 学区房 (school-district property) carries 30–80 %+ premium — but the underlying schooling rights are subject to 多校划片 (multi-school zoning), 9年一户 (one household-per-flat-per-9-years), and frequent district-policy revisions; verify the policy of the destination 教育局 (Education Bureau) within the last 12 months — a "premium school district" entitlement can be administratively withdrawn
6. **Trap**: 公寓 / 商住 (40-year-LUR commercial-residential) properties trade 30–50 % below adjacent residential 70-year-LUR units of equivalent specification because of: shorter LUR (no auto-renewal under Art. 359), higher 40-year deed tax, no school-district rights, higher utility tariff (commercial), no 燃气 town-gas (electric only), and weaker mortgageability (max 50 % LTV typical, max 10-yr term). **Always confirm 70-year residential LUR before underwriting any per-m² benchmark**
7. **Trap**: 公摊面积 (shared common-area share) is part of 建筑面积 for tax + transaction but is owned collectively — owners pay for 30 %+ that they cannot occupy. Reform discussions ([MoHURD 2024 study group](https://www.mohurd.gov.cn/)) have explored 套内面积 (interior-only) as the future basis but no nationwide change announced; some new pilots (e.g., 2024 张家界, Hunan) trial 套内 sale
8. **Trap**: 70-yr LUR remaining < 20 yrs creates mortgage + resale headwinds even before Art. 359 auto-renewal mechanics tested. Verify the **LUR start date** on the 不动产权证书 (Real-Estate Title Certificate); subtract from 70 to get remaining

### Trend 2021 → Q2 2026 (post-Evergrande market context)

- **Sustained bear cycle 2021 → 2024**: 4–5 consecutive years of declining new-home prices in lower-tier cities; cumulative real-terms decline of 25–35 % in Tier-3/4 markets ([Bloomberg 2025-11](https://www.bloomberg.com/news/articles/2025-11-24/china-property-crisis-why-market-is-a-mess-what-stimulus-measures-are-planned))
- **Developer-side defaults**: Evergrande 恒大 (US$300B+ liabilities; HKEx delisted Aug 2025; court-ordered liquidation Jan 2024 — [CNBC 2025-08](https://www.cnbc.com/2025/08/25/evergrandes-rise-and-fall-leaves-scars-on-chinas-property-sector.html)); Country Garden 碧桂园 (winding-up petition 2024; hearing extended Jan 2025); Sunac 融创, Shimao 世茂, Kaisa 佳兆业, Sino-Ocean 远洋 — bulk of top-50 developers in distress / restructuring
- **保交楼 ("delivered-housing-promise") policy**: launched Aug 2022 ([NBS 国家统计局 Q&A (Aug 2022 data) — 保交楼稳民生 · 国常会19项接续政策](https://www.stats.gov.cn/sj/sjjd/202302/t20230202_1896678.html)); expanded 2023–2024; ~1.2 trillion ¥ developer liabilities cleared via court-supervised restructuring through 2025 ([gov.cn 2025-12](https://www.gov.cn/)); priority is finishing **pre-sold but not delivered** units (the 烂尾楼 "unfinished-tail" inventory) — buyers of distressed-developer pre-sales should verify 保交楼 inclusion AND timeline before completion
- **Sept 2024 stimulus package** ([gov.cn 2024-09](https://english.www.gov.cn/news/202409/25/content_WS66f3602ec6d0868f4e8eb3c0.html)): minimum down-payment cut to 15 % first-home / 15 % second-home; mortgage rate floor abolished for most cities; tier-1 cities relaxed Hukou / social-security rules (see § Foreign-buyer overlay above); Guangzhou fully removed all home-purchase restrictions
- **Nov 2024 deed-tax + LVAT reductions** ([gov.cn 2024-11-14](https://english.www.gov.cn/news/202411/14/content_WS673591d5c6d0868f4e8eceeb.html)): see § `--tax`
- **2025 stabilisation skewed**: Shanghai +3.7 % YoY March 2026 (only Tier-1 still positive); Beijing –2.1 %, Guangzhou –4.7 %, Shenzhen –5.5 % March 2026 (NBS); 70-city aggregate –3.4 % YoY ([scio.gov.cn 2026-04](http://english.scio.gov.cn/pressroom/2026-04/16/content_118441356.html))
- **2026 outlook**: PBOC + MoHURD signalling "stop the decline, restore stability" 止跌回稳; further fiscal/monetary support expected; developer-side consolidation continues. Buyer base structurally smaller (demographic peak passed; Hukou-constrained tier-1 demand); Tier-3/4 inventory still elevated ~2024–2030 absorption horizon

---

## Section: `--traffic`

### Primary source

- **交通运输部 (Ministry of Transport, MoT)** — `https://www.mot.gov.cn/` — national road & transport statistics; annual 公路交通量调查 (Highway Traffic Volume Survey) per province
- **中国统计年鉴 (China Statistical Yearbook, NBS)** — `https://www.stats.gov.cn/sj/ndsj/` — annual transport tables
- **省/市 交通运输厅/局** — provincial / municipal transport bureaus publish AADT counts on national + provincial highways (国道 G-roads / 省道 S-roads). Coverage is uneven; major highways (e.g., G1, G2, G3, G4 expressways) well-documented; urban arterials less so
- **百度地图 / 高德地图 (Baidu Maps / Amap / AutoNavi)** — real-time congestion + heatmap; not formal AADT but **the only practical real-time tool inside mainland China** (Google Maps blocked); Amap publishes annual urban congestion reports

### Key term

China uses **AADT (年平均日交通量)** for highway counts. Inside cities, **道路饱和度 (road saturation ratio)** + **路段服务水平 (level of service)** classifications are common in municipal transport-bureau reports.

### Verdict bands (residential-noise scale, mainland-Chinese arterial context)

- 🟢 < 5,000 v/d (interior estate road inside a 小区, neighbourhood lane)
- 🟡 5,000–25,000 v/d (district feeder, secondary city street)
- 🟠 25,000–80,000 v/d (urban arterial, e.g., 长安街 Beijing, 中山路 Shanghai, 深南大道 Shenzhen)
- 🔴 > 80,000 v/d (urban expressway / 二/三/四/五环路 ring-road, intercity G-expressway; saturation > 150,000 on inner ring roads typical)

### Coarse fallback (OSM `highway`)

- motorway = 高速公路 (G-class, S-class expressways)
- trunk = 城市快速路 / 一级公路
- primary = 主干道 (principal arterial)
- secondary = 次干道 (secondary arterial)
- residential = 支路 / 小区内道
- service = 内部道路

### Notes

- Tier-1 cities (Beijing / Shanghai / Shenzhen / Guangzhou) cap private-vehicle registration via 牌照摇号 (licence-plate lottery, Beijing since 2011; Shanghai 拍牌 auction, average plate price ~¥80k–100k Q1 2026); Shenzhen + Guangzhou hybrid lottery+auction; result is **plate scarcity**, not road saturation reduction — congestion remains heavy
- **Trap**: properties advertised "near subway" (近地铁) — verify **walking** distance via Amap pedestrian routing; "10-min walk" claims often translate to 800-1200 m and 15+ min in practice
- **Trap**: ring-road properties — inner-ring noise + air-quality penalty; outer-ring (4环 / 5环 outer Beijing, S-roads Shanghai) often combined with elevated viaducts amplifying nighttime noise. Request developer-supplied **声环境检测报告 (Acoustic Environment Test Report)** for new-build within 100 m of arterial / expressway — required under [GB 3096-2008 Acoustic Environment Standard](https://www.mee.gov.cn/) but rarely volunteered

---

## Section: `--tax`

### Annual property charges (recurring)

Mainland China has **NO nationwide recurring property tax** for residential property held by individuals as of May 2026. Two pilot programs only:

| Pilot city | Effective | Scope | Rates (2024 reference) | Source |
|---|---|---|---|---|
| **上海 (Shanghai)** | 28 Jan 2011 | Newly-purchased 2nd+ residential by Shanghai-Hukou residents AND any newly-purchased residential by non-Shanghai-Hukou (incl. foreigners). 60 m² per family member exemption | **0.4 %** if unit price ≤ 2× prior-year city avg new-home price; **0.6 %** if above 2× | [Shanghai Tax Bureau](https://shanghai.chinatax.gov.cn/) |
| **重庆 (Chongqing)** | 28 Jan 2011 | Newly-purchased high-end villas + newly-purchased 2nd home by non-Chongqing-Hukou + apartments above price threshold | **0.5 %** below 2× city avg; **1.0 %** 2–3×; **1.2 %** > 3× city avg | [Chongqing Tax Bureau](http://chongqing.chinatax.gov.cn/) |

> Both pilots launched simultaneously 2011-01-28 ([State Council Notice on Pilot Reform](http://www.gov.cn/)). Coverage is narrow (newly-purchased, mostly upper segment); revenue is small (< 5 % of municipal own-source revenue in either city, 2024 estimates). Academic estimates ([Lincoln Institute 2024](https://www.lincolninst.edu/publications/articles/chinas-property-tax-reform/)) put the **Shanghai price effect at –11 to –15 %** in covered segments and **Chongqing at +10–12 %** in luxury (sustained demand offset).
>
> **No nationwide rollout has occurred or been formally scheduled.** A 2021 NPC Standing Committee resolution authorised expanded pilots; that authority **lapsed in 2026** per [Caixin / SCMP coverage 2024–2025] without expansion. Repeated official statements 2023–2025 indicate the property-tax expansion is "paused" while the property market stabilises. Reverify via [State Taxation Administration (STA) — chinatax.gov.cn](http://www.chinatax.gov.cn/) before relying on absence of a tax in any specific city.

**Other recurring charges** (not "property tax" per se):

| Charge | Base | Typical rate | Note |
|---|---|---|---|
| **物业管理费 (property management fee)** | per m² built area per month | ¥1.5–6.0 /m²/mo low-mid; ¥8–15 /m²/mo luxury / international Tier-1 | Paid to 物业管理公司; covers security, cleaning, lifts, garden |
| **取暖费 (heating fee — northern cities only, October–March)** | per m² built area per heating season | ¥18–30 /m²/season (e.g., Beijing ~¥30/m², Shanghai exempt by latitude convention) | Mandatory for centralised-heating buildings north of Yangtze line |
| **卫生 / 垃圾费 (sanitation)** | per household | ¥10–60 /yr | Marginal |

### Transaction taxes (one-time at purchase)

**契税 / Deed Tax** — buyer pays; nationwide; **MoF + STA + MOHURD Announcement 2024 No.16** (issued 12 Nov 2024, effective **1 Dec 2024**, repealing Cai Shui [2016] No.23) ([STA policy text](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qs/202411/t474016.html); [gov.cn 2024-11-14](https://english.www.gov.cn/news/202411/14/content_WS673591d5c6d0868f4e8eceeb.html); [Caixin 2024-11-15](https://www.caixinglobal.com/2024-11-15/china-cuts-property-tax-102257509.html)):

| Property scenario | Unit ≤ 140 m² | Unit > 140 m² |
|---|---:|---:|
| 1st residential (家庭唯一住房) | **1 %** | **1.5 %** |
| 2nd residential (家庭第二套住房) | **1 %** | **2 %** |
| 3rd+ residential | **3–5 %** (province-set statutory rate; no concession) | 3–5 % |
| Non-residential (commercial / office) | 3–5 % (province-set statutory rate) | 3–5 % |

(Pre-Dec-2024 schedule had 1 % / 1.5 % / 3 % first-home + 1 % / 2 % / 3 % second-home cliff at 90 m² — replaced by the 140 m² single-cliff above.)

> The **140 m² break applies uniformly nationwide — there is no city-tier differentiation left.** Announcement 2024 No.16 expressly brought **Beijing, Shanghai, Guangzhou and Shenzhen INSIDE the family-second-home concession**, so the pre-Dec-2024 tier-1 3 % second-home treatment is **abolished**. Exactly 140 m² sits in the **1 %** band (140平方米及以下). Only third-and-subsequent homes and other non-qualifying transfers fall outside the concession, at the **province-set statutory rate within the 3–5 % band** (Deed Tax Law art. 3) — **verify the destination province's rate with the local 税务局 (Tax Bureau)** before underwriting. Status 全文有效 on the STA policy-law library as at 2026-08-07.

**增值税 / Value-Added Tax (VAT) — seller pays** (or passed to buyer in seller's-net agreements):

| Holding period | Pre-2026 rate | From 1 Jan 2026 |
|---|---:|---:|
| < 2 years | **5 % of full sale price** | **3 %** (MoF & STA Announcement 2025 No.17 / 财政部 税务总局公告2025年第17号, issued 29 Dec 2025, eff. 1 Jan 2026 — [gov.cn 2025-12-30](https://english.www.gov.cn/news/202512/30/content_WS6953dc2dc6d00ca5f9a08574.html); [Caixin 2025-12-31](https://www.caixinglobal.com/2025-12-31/china-trims-vat-on-short-held-home-sales-as-property-easing-continues-102399207.html)) |
| ≥ 2 years (普通住宅 ordinary housing) | **0 % (exempt)** | 0 % (exempt) |
| ≥ 2 years (非普通住宅 non-ordinary / luxury, Tier-1 only) | 5 % on price-cost margin | 5 % on price-cost margin (verify; reform language ambiguous) |

> "普通住宅" (ordinary housing) vs "非普通住宅" definitions are city-specific (combination of unit area, plot ratio, and unit price relative to city benchmark). Tier-1 cities historically applied stricter "non-ordinary" floors that captured most central-district stock — **Shanghai abolished the 普通/非普通 distinction Nov 2024**; **Beijing and Shenzhen aligned Dec 2024**; **Guangzhou aligned 2024**. Verify per city before computing VAT.

**个人所得税 / Individual Income Tax on capital gain — seller pays**:

| Method | Rate | Note |
|---|---:|---|
| **Verifiable cost basis** (buyer purchase price + verified renovation + interest + transaction taxes documented) | **20 % × (sale price − cost basis)** | Used when full purchase paperwork available |
| **Deemed (核定) method** (no documentation) | **1 %** of full sale price (residential, most cities) | Default fallback; rates 1 %–3 % vary by city; Beijing 1 %, Shanghai 1 %, Shenzhen 1.5 % — verify |
| **Family-only-home + ≥ 5 yr held exemption** | **0 %** | If seller can prove the unit is the family's only residential property AND held ≥ 5 yrs, full IIT exemption applies under [STA Notice 国税发 2006/108] |

**土地增值税 / Land Value-Added Tax (LVAT)** — applies to **sale by enterprises / developers**, not individuals selling personal residence (individual-seller LVAT is **exempt** under [Cai Shui 2008/137]). Developer side: progressive 30–60 % on the appreciation portion (value-add over cost) per [LVAT Provisional Regulations](https://fgk.chinatax.gov.cn/zcfgk/c100010/c5194433/content.html).

**印花税 / Stamp Duty**: residential individual sale **exempt** since 2008 (Cai Shui 2008/137).

**Other transaction-side costs**:

| Item | Cost |
|---|---|
| **不动产登记费 / Real-estate registration fee** | ¥80 per property (residential) — ¥550 (non-residential) — fixed nationwide [MoF / NDRC schedule] |
| **测绘费 / Survey fee** (if not yet completed) | ¥1.36 / m² typical, capped per locality |
| **公证费 / Notary fee** (if elected — not mandatory for resale) | 0.3 % of price (older 2008 schedule, capped); declining due to non-mandatory status |
| **中介费 / Agent commission** | typically **2–3 % of price**, split buyer + seller (commonly 1.5 + 1.5 % or 2 % buyer / 1 % seller); Beike publishes 2 % platform fee with rebates; capped voluntarily by 2018 industry agreement at 2.7 % combined |
| **银行评估费 / Bank valuation fee** (if mortgaged) | ¥500–¥3,000 per property |
| **律师费 / Lawyer fee** (optional but recommended for foreign buyers) | ¥3,000–¥30,000 depending on complexity |

### Capital gains / income tax on sale by foreign individual

- IIT 20 % on capital gain; same rule as PRC citizens (no separate non-resident schedule for property gain) — **but** if foreign-individual seller is a non-resident (< 183 days in PRC in tax year), withholding may differ — verify with [STA Non-Resident Tax page](http://www.chinatax.gov.cn/) and any applicable bilateral tax treaty
- **No exit tax** at sale per se, but FX repatriation requires SAFE quota / approval (see § `--currency`)

### Rental income tax (individual landlord)

- **Individual Income Tax (IIT)** on rental: per [PwC 2025 China Tax Facts](https://www.pwccn.com/en/tax/publications/people-republic-of-china-tax-facts-2025.pdf) ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row and [PwC Tax Summaries](https://taxsummaries.pwc.com/peoples-republic-of-china/individual/income-determination):
  - Standard rate: **20 % flat** on rental income
  - Allowable deduction: ¥800 if monthly gross ≤ ¥4,000; **20 % deemed deduction** if monthly gross > ¥4,000
  - Effective rate on rental > ¥4,000/mo: **20 % × 80 % = 16 %**
- **VAT** on rental by individual: 5 % nominal, with **¥100,000/month threshold** exempting most small landlords (since 2023; verify current threshold)
- **Property Management surcharge**: paid by lessor / lessee per contract
- **房产税 (House Property Tax) on individual let-out residential**: **12 % flat on rental** under [Provisional Regulations on House Property Tax 1986](http://www.chinatax.gov.cn/) — long-standing law but selectively enforced for individual residential lessors; commercial lessors / tenants more aggressively enforced. Some cities (e.g., Beijing) reduce the 12 % to **4 %** for individual let-out residential (verify locally). **Tax authorities are tightening enforcement 2024–2025 via tenant-side withholding pilots** — assume full liability when underwriting
- **Foreign-individual landlord under 171号文**: rental of foreign-purchased residential is **technically not permitted under 171 (one-property-for-own-use)**; in practice enforcement varies, but tax / regulatory exposure exists. **Do not underwrite a buy-to-let plan as a foreign individual without local tax / legal advice.**

### Future risk

- **Nationwide property tax**: pilots since 2011 (Shanghai / Chongqing); 2021 NPC pilot-expansion authority **lapsed unused 2026**; near-term rollout suspended pending market recovery — but the legal framework remains and a 2027–2030 reintroduction is a meaningful long-horizon risk
- **VAT cut to 3 % for < 2-yr holds (eff. 2026-01-01)** signals continued easing; further developer-side concessions plausible; demand-side stamp / IIT tweaks frequent (4× in 2024 alone)
- **Hukou + social-security / IIT thresholds** continue to ease in tier-1 cities; foreigner 171号文 1-year rule has not been amended since 2006 — has been considered for tightening (2017) and easing (2025) but stable as of 2026-05
- **40-yr LUR commercial-residential 公寓** segment faces structural headwinds: no Civil Code Art. 359 auto-renewal, no school-district rights, no Hukou attachment. Resale market for 40-yr stock fragile

---

## Section: `--rental`

### Long-term residential

- **Tenancy law**: [NPC 中国人大网 合同法释义 第十三章 租赁合同 (合同法第214条 / 第215条 — superseded by 民法典第705条 / 第707条)](http://www.npc.gov.cn/zgrdw//npc//flsyywd/minshang/2000-11/25/content_8375.htm) — minimum statutory protections; max single lease term **20 years** (合同法第214条, carried into 民法典第705条 — verify the Civil Code article text at 中国人大网 / 司法部); written contracts mandatory for terms of **6 months or more** (六个月以上); deposit + advance payment customary
- **Standard tenancy structure**: 12-month fixed term most common; **1-month deposit + 1-month or 3-month advance** in mainland use (押一付三 — "one deposit + 3-month advance" Tier-1 standard); landlord typically pays property-tax / management-fee portion attributable to 公摊; tenant pays utilities + heating
- **Rent-control**: no nationwide statutory rent control; tier-1 cities monitor "fair rent guidance" indices but enforcement light for private-residential. Rent caps in some 公租房 (public-rental housing) categories — irrelevant to foreign-buyer scenarios
- **Foreign-individual letting**: technically restricted under 171号文 (one property for own residential use); enforcement varies — see § `--tax` above

### Yields (Q4 2025, Tier-1 city aggregates from Beike 历史成交 + Lianjia rental boards; verify per project)

| Tier-1 city | Gross rental yield (avg) |
|---|---:|
| 北京 (Beijing) | ~1.4–1.8 % |
| 上海 (Shanghai) | ~1.6–2.2 % |
| 深圳 (Shenzhen) | ~1.5–2.0 % |
| 广州 (Guangzhou) | ~1.8–2.4 % |
| New Tier-1 (Hangzhou / Chengdu / Suzhou) | ~2.0–3.0 % |
| Tier-2 (Wuhan / Xi'an / Chongqing) | ~2.5–3.5 % |
| Tier-3+ | ~3.0–4.5 % gross (but capital-value risk + low liquidity) |

> Mainland Chinese gross residential yields are **structurally low** by emerging-market standards because (a) capital-value compounding 2010–2021 outpaced rents; (b) rental income is disfavoured culturally vs ownership ("买房" mentality); (c) school-district premium inflates capital values without commensurate rent. Net yields after property management fee + heating + IIT + house-property-tax + vacancy + agent + repair sit **0.5–1.5 % below gross** in Tier-1, somewhat higher in Tier-2.

### Short-term rentals (短租 / 民宿 / Airbnb)

**Status (2026)**: regulated; Airbnb withdrew from mainland China retail bookings effective **30 July 2022** ([Airbnb press release 2022-05-23](https://news.airbnb.com/)) due to operational complexity + COVID-era policy; outbound Chinese travel still served. Domestic platforms 木鸟民宿 / 途家 / 美团民宿 / 小猪短租 / 飞猪 / Booking now dominate.

- **Hotel & Accommodation Operating Licence (公安 + 文旅 双证)**: short-term commercial accommodation strictly requires 公安 (Public Security Bureau) **特种行业许可证** + **文化旅游 (Tourism) registration**; many residential-zoned units **cannot legally operate Airbnb-style nightly** because the 物业 (HOA-equivalent) and the 业主大会 (owners assembly) of the building must consent + zoning must permit
- **公寓 (40-yr commercial-residential)**: typically the only legal short-term-let asset class; many residential 70-yr 小区 ban transient rental in their 业主公约
- **Foreign guest registration**: hosts must register foreign guests at the local 派出所 (police station) within 24 hrs of check-in under [Exit & Entry Administration Law 2012 Art. 39](http://www.gov.cn/) — non-compliance = ¥2,000 fine + potential operating-licence loss
- **Tier-1 city overlay**: Beijing + Shanghai have intermittent Airbnb-style enforcement sweeps; Shenzhen + Guangzhou somewhat more relaxed; Hainan has resort-licensed 民宿 frameworks; Niche tourist destinations (Yunnan, Tibet, Xinjiang) more permissive but with separate public-security registration burdens
- **Strategic conclusion**: a credible mainland short-let strategy is **legitimate-licensed 民宿 in tourist-zoned 公寓** (40-yr LUR), **not** Airbnb-style nightly in 70-yr residential. Returns net of regulatory / licensing / management cost rarely beat long-let in Tier-1; some Tier-2 tourist cities (Sanya, Dali, Kunming, Lijiang, Chengdu) work seasonally

### Tax + reporting on rental

- IIT 20 % on rental (effective 16 % after 20 % deemed deduction) — see § `--tax`
- House Property Tax 12 % flat (Beijing 4 %); enforcement intensifying 2024–2025
- VAT 5 % above ¥100,000/month threshold (most individual landlords exempt)
- Annual settlement via [STA myTax mobile app 个税 APP](http://www.chinatax.gov.cn/) by 30 June for prior calendar year
- Foreign-individual landlord: see 171号文 caveats above

### Strategic notes

- Foreign individual buying for **own-use only** (consistent with 171号文): structurally easier; no rental tax / regulatory complexity; pure capital-value exposure
- Foreign individual buying for **family-member's use**: legally grey; depends on 171号文 interpretation in destination city — verify with local 房屋管理局 (Housing Bureau)
- Foreign individual buying for **rental yield**: **highly inadvisable** without local PRC entity (WFOE) ownership structure; structural complexity often outweighs return; PRC tax-treaty position for the home country must be checked
- Foreign individual buying for **capital appreciation + future relocation**: most common profile; underwrite at the lowest yield band + assume nominal capital appreciation ≤ inflation through 2030 absorption cycle

---

## Section: `--work=<profession>`

### Job platforms

- **智联招聘 / Zhaopin** — `https://www.zhaopin.com/` — largest mainstream job board
- **前程无忧 / 51job** — `https://www.51job.com/`
- **BOSS直聘 / Boss Zhipin** — `https://www.zhipin.com/` — boss-direct chat model; mid-market dominant
- **拉勾 / Lagou** — `https://www.lagou.com/` — tech / internet sector
- **猎聘 / Liepin** — `https://www.liepin.com/` — mid-to-senior market
- **LinkedIn China**: `https://www.linkedin.com/` — operates as 领英 since 2014; reduced functionality post-2021 reform; primary use is foreign / MNC roles + cross-border outreach
- **Government sector**: 国家公务员考试 (national civil-service exam, NEA at `http://bm.scs.gov.cn/`); provincial civil-service portals — citizenship-restricted (Chinese passport required)

### Self-employment regimes

- **个体工商户 (sole proprietorship / individual industrial-commercial household)** — register at local 市场监督管理局 (Market Regulation Administration); ~¥0 statutory fee; **personal income tax on profits + social insurance**; foreign individuals can register if holding work-residence permit + sectoral approval
- **个人独资企业 (sole proprietorship enterprise)** — slightly larger entity; same IIT treatment
- **有限责任公司 (Limited Liability Company, LLC) / 有限合伙 (LP)** — most common SME vehicle; **CIT 25 %** standard, **20 % small-and-low-profit** rate for taxable profit ≤ ¥3M with reduced effective rate ~5 % via current concession (verify [STA SME concession 2024–2027](http://www.chinatax.gov.cn/))
- **WFOE (外商独资企业, Wholly Foreign-Owned Enterprise)** — full foreign ownership in non-restricted sectors per [Foreign Investment Negative List 2024](https://www.ndrc.gov.cn/); minimum capital deregulated; CIT 25 %
- **VAT 增值税**: standard 13 % (goods); 9 % (transport, real-estate); 6 % (services); 3 % small-scale taxpayer; small-scale annual turnover ≤ ¥5M
- **社保 (Social Insurance — 五险) + 公积金 (Housing Provident Fund — 一金)**: combined "五险一金" — pension + medical + unemployment + work-injury + maternity + housing fund; employer ~30–40 % of salary, employee ~20 %; foreigners covered since 2011 nationally (some city-level concessions)

### Salaried benchmarks (Tier-1 city, 2024 release; NBS Annual Average Wage of Urban Non-Private Employed)

- **All-China urban non-private avg annual wage 2024**: ~¥124,110 (~¥10,343/mo); **urban private avg** ~¥69,800 (NBS 2024 release)
- **Beijing avg annual non-private**: ~¥218,000+ (top Tier-1)
- **Shanghai avg annual non-private**: ~¥215,000+
- **Shenzhen / Guangzhou avg annual non-private**: ~¥160,000–180,000
- **Tech sector mid-career Tier-1**: ¥30,000–80,000/mo (¥360k–960k/yr); senior FAANG-equivalent (Tencent / Alibaba / ByteDance / Huawei P7+) ¥600k–2M+/yr including stock
- **Finance Tier-1**: ¥25,000–80,000/mo mid; senior PM / IBD ¥1M–5M/yr
- **Foreign teachers / English-language**: ¥18,000–35,000/mo Tier-1; ¥12,000–22,000 Tier-2 (post-2021 双减 "double-reduction" policy compressed K-12 tutoring market — international-school, university, business-English remain)
- **Statutory minimum wage**: city-set; Tier-1 ranges ~¥2,420 (Shanghai 2024) / ¥2,420 (Shenzhen) / ¥2,420 (Beijing) /mo; provincial floor ~¥1,800

### Catchment heuristics

- Tier-1 city core: 30-min metro reaches full white-collar catchment (e.g., Beijing 国贸 / Shanghai 陆家嘴 / Shenzhen 福田 / Guangzhou 珠江新城)
- 60-min metro: most second-ring corporate / R&D campuses (Beijing 望京 / 中关村, Shanghai 张江 / 漕河泾, Shenzhen 南山 / 龙华, Guangzhou 天河 / 番禺)
- New-Tier-1 (Hangzhou, Chengdu, Suzhou, Nanjing): ~45-min metro core; city-state-style commute reach
- Tier-2 / Tier-3: subway expansion ongoing 2024–2030; verify the destination metro line operating + latest extension via [中国城市轨道交通协会 (China Urban Rail Transit Association)](https://www.camet.org.cn/)

### Visa / residence pathway for working foreigners

- See § Country profile / Visa above (Z, X, Q, R, PR)
- **Z visa pathway dominant** for employed foreigners; converted to **居留许可 (work-residence permit)** within 30 days of arrival
- **R visa (high talent)**: A-class top talent track (科技人才 / Outstanding Foreign Talent) — fast-track, multiple-entry, easier renewal; managed via 中华人民共和国外国人来华工作许可制度. The **外国人来华工作管理服务系统** has been run by **人力资源和社会保障部 (MOHRSS)** on the 全国人社政务服务平台 since **3 June 2024** ([www.12333.gov.cn](https://www.12333.gov.cn/)); the former 科技部政务服务平台 (fuwu.most.gov.cn) no longer serves it. 国家外国专家局 (SAFEA) has not been a standalone body since the **2018 State Council reorganisation**, which merged its functions into 科学技术部 while retaining the SAFEA nameplate externally (2026 data, source MOST migration notice 2024-05-31 + MOHRSS 全国人社政务服务平台 + 国务院机构改革方案 18 Mar 2018; 2026-09-18 verified)
- PR (永久居留 / "Chinese Green Card"): selective; investment / talent / family / 4-yr-work tracks; through 2024 cumulative grants estimated < 30,000 individuals total
- **Tax residency**: 183-day rule per [IIT Law 2018 + 个税法实施条例 2018]; foreign individuals < 183 days/yr taxed only on China-sourced income; ≥ 183 days for 6 consecutive years are taxed on worldwide income (with 6-year reset rule via 30+-day single absence)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **应急管理部 (Ministry of Emergency Management, MEM)** | `https://www.mem.gov.cn/` | National disaster registry, risk assessment, dam safety |
| **中国地震局 (China Earthquake Administration, CEA)** | `https://www.cea.gov.cn/` | Seismic intensity / fortification zoning; [GB 18306-2015 Seismic Ground Motion Map](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=EC0585F90CA21ABE02826394F266B623) |
| **中国气象局 (China Meteorological Administration, CMA)** | `https://www.cma.gov.cn/` | Typhoon, flood, drought, climate projections; CMIP6 downscaled atlas |
| **水利部 (Ministry of Water Resources, MWR)** | `http://www.mwr.gov.cn/` | Flood-prone area maps; major river-basin hazard zones |
| **生态环境部 (Ministry of Ecology & Environment, MEE)** | `https://www.mee.gov.cn/` | Air quality (PM2.5), soil contamination zones, environmental-impact assessments |
| **自然资源部 (Ministry of Natural Resources, MNR)** | `https://www.mnr.gov.cn/` | Geological hazard zones (landslide, debris flow, ground subsidence) |
| **中国地质环境监测院 (China Institute of Geo-Environmental Monitoring)** | `http://www.cigem.cgs.gov.cn/` | Geological hazard inventory, ground-subsidence monitoring |
| **省/市 自然资源局 / 应急管理局 / 住建局** | Provincial / municipal portals | Local hazard zoning; project-level EIA; building-code compliance |

### Natural-hazard profile (highly geographically variable)

China spans **22 climate zones + 5 seismic-fortification intensity bands**; risk profile differs sharply by city. Headline patterns:

- **Earthquakes**: high-seismic belts include 西部 (Sichuan-Yunnan-Tibet), 西南 (Hengduan ranges), 京津唐 (Beijing-Tianjin-Tangshan), 东北 (NE China). [GB 18306-2015](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=EC0585F90CA21ABE02826394F266B623) maps fortification intensity 6–8+ for most populous regions; major historical events: 2008 汶川 (M8.0; ~70k deaths), 1976 唐山 (M7.5–7.8; ~242k deaths). All Tier-1 cities sit in 7+ design intensity. Verify property's **抗震设防烈度 (seismic-fortification intensity)** + structure type via developer documentation + 住建部 supervisory records
- **Typhoons / coastal storms**: SE coast (Guangdong / Fujian / Zhejiang / Shanghai / Hainan / Taiwan Strait facing) hit ~5–9 typhoons/season July–October; Hainan + south Guangdong highest exposure; Shanghai metro vulnerable to peripheral effects
- **Floods**: Yangtze, Yellow, Huai, Pearl river basins flood-prone; 2020 catastrophic Yangtze + 2021 Henan (Zhengzhou subway flood, ~398 deaths) recent reference points; urban pluvial flooding intensifying with climate change
- **Air quality**: long-term PM2.5 elevated relative to WHO guidelines; northern industrial belt (HBJ — Hebei, Shanxi, Henan, Beijing) historically highest. **2024 nationwide annual avg PM2.5 ≈ 29.3 µg/m³** (MEE data; vs WHO 2021 AQG of 5 µg/m³); Tier-1 averages: Beijing ~33, Shanghai ~26, Shenzhen ~22, Guangzhou ~24 (2024). Continued multi-decadal improvement vs 2013 (Beijing then ~89 µg/m³) but still 5–7× WHO guideline. Sandstorms episodic in Beijing March–May
- **Ground subsidence**: Shanghai, Tianjin, North-China-Plain agricultural belt — multi-decade groundwater-extraction-driven subsidence (Shanghai cumulative 2.5+ m since 1921; rate slowed to ~5–10 mm/yr with extraction controls). Pearl Delta also subsiding; affects long-term coastal-flood + structural integrity
- **Landslides / debris flow**: SW China (Sichuan / Yunnan / Guizhou); rural / mountainous; less material for urban / Tier-1 buyers
- **Drought**: northern China structurally water-stressed; South-North Water Transfer Project (南水北调) operational since 2014 East/Middle routes
- **Extreme heat**: rising frequency of 35°C+ days in lower Yangtze + South China; 2022 was record (Chongqing, Wuhan exceeded 40°C multiple consecutive days)

### Build-era hazards (mainland Chinese residential stock)

| Era | Hazard rating | Notes |
|---|---|---|
| **Pre-1980** | 🟠 | Pre-reform era; thin walls, no central heating south of Yangtze; asbestos likely; many already demolished or pending 城中村 / 棚改 redevelopment |
| **1980–2000 (early reform-era)** | 🟠 | First-generation commodity housing post-1998 housing reform; varied seismic compliance; mortgage-marketed but quality variable |
| **2000–2012 (boom era)** | 🟡 | Bulk of current stock; most followed [GB 50011-2010 Code for Seismic Design]; 公摊 ratios often opaque; check structural inspection records |
| **2012–2020** | 🟢 | Code [GB 50011-2010] strictly applied; energy-efficiency standards (北方居住建筑节能 1995, JGJ 26-95 successive updates); [Green Building Standard 绿色建筑 GB/T 50378] increasingly mandatory |
| **2020+** | 🟢 | Current code: [GB 50011-2010 + 2024 amendments]; mandatory pre-sale escrow tightening post-Evergrande; "保交楼" supervision |
| **Pre-sold by distressed developer 2020–2024** | 🔴 | "烂尾楼" risk: pre-paid units never delivered; verify 保交楼 inclusion + completion date before any pre-sale purchase |

**Asbestos**: prevalent pre-1990 build; demolition / renovation must use licensed contractor under [GBZ/T 222-2009 Workplace Asbestos Sampling Guideline]; pre-purchase test recommended for any pre-1990 stock
**Radon**: regional variation; some southern provinces with granitic geology elevated; [GB 50325-2020 Civil Building Indoor Air-Quality Code] mandatory radon limits at delivery (build-quality measure)

### En bloc / 棚改 / 城中村 redevelopment (拆迁) risk

- **棚改 (shantytown redevelopment)** + **城中村改造 (urban-village reform)**: government-led demolition + relocation of older / sub-standard stock. From 2024 the 城中村改造 programme was expanded to **35 mega-cities** ([gov.cn 2023-07-21 Politburo + State Council], with 2025 acceleration) — buyers in older / village-style stock could face compulsory acquisition with cash compensation OR replacement-housing — terms set by local government. Both upside (compensation often above market) AND downside (timing uncertain, dispute risk)
- Verify **拆迁 risk status** via local 自然资源局 / 住建局 zoning portal + 控制性详细规划 (Controlled Detailed Plan) overlay before underwriting

### Mandatory documents at sale (resale residential)

| Document | Required because | Source |
|---|---|---|
| **不动产权证书 (Real-Estate Title Certificate)** | Title verification | 不动产登记中心 (district-level Real-Estate Registration Center) |
| **国有土地使用证 (State-Land Use Certificate, pre-2015)** | Where unified certificate not yet issued | 自然资源局 |
| **房屋所有权证 (House Property Certificate, pre-2015)** | Where unified certificate not yet issued | 房产管理局 |
| **税单 (recent property-related tax payment records)** | Verify outstanding tax / fees | 税务局 / 12366 |
| **物业 (HOA-equivalent) management records, sinking-fund balance** | Strata-titled compound | 物业 management + 业主大会 |
| **抵押状态证明 (mortgage status certificate)** | Mortgage discharge if any | seller's bank |
| **婚姻状况 (marital status) + 共有人同意 (co-owner consent)** | Civil Code 1062 marital-property rules | seller declaration + civil-affairs verification |
| **预售合同备案 (pre-sale contract filing) — pre-sale stock only** | Verify original developer pre-sale | 住建局 |
| **保交楼 inclusion confirmation — distressed-developer pre-sale only** | Verify completion timeline | 住建局 + 保交楼 task force |
| **学区 confirmation letter (where applicable)** | School-district status | 教育局 |
| **税务清算 (final tax clearance) at deed-transfer** | Required by 不动产登记中心 | 税务局 |

### Climate change projections (CMA + IPCC AR6 China downscaled)

- **Annual mean temperature**: +1.5 to +3.0°C nationwide by 2050 SSP2-4.5; +2.0 to +5.0°C by 2100 SSP5-8.5 ([CMA Third National Climate Assessment Report 第三次气候变化国家评估报告](https://www.cma.gov.cn/))
- **Heatwaves**: 35°C+ day count to double by 2050 in lower Yangtze
- **Extreme rainfall**: +15–30 % intensity by 2100 in south + east
- **Sea-level rise (Chinese coast)**: +0.4 to +1.2 m by 2100 high-end (CMA + IPCC AR6); Pearl Delta + Yangtze Delta + Bohai Bay especially exposed
- **Drought**: northern China stress intensifying; South-North Water Transfer expansion likely
- **Air quality co-benefits**: continued PM2.5 decline path through 2030+ from "carbon-peak" targets, but progress slowing in last 20 % to WHO guideline

### Air quality

- **MEE national air-quality monitoring portal**: `https://air.cnemc.cn:18007/` (中国空气质量在线监测分析平台)
- **City-level AQI**: real-time at `https://www.aqistudy.cn/`
- **Foreign-friendly**: [US Embassy Beijing AQI](https://china.usembassy-china.org.cn/embassy-consulates/beijing/air-quality-monitor/) (closed several times due to political friction; verify availability)
- **Policy**: [Air Pollution Prevention & Control Law 2015 + 2018 amendments]; [大气污染防治行动计划 "Air Ten" 2013-2017 → 蓝天保卫战 "Blue Sky Defense" 2018-2020 → 持续深入打好蓝天保卫战 2024+]

---

## Section: `--mains`

Mains water + electricity + gas + sewerage are **near-universal in urban mainland China** — every legally completed urban residential development since 1990 has all four. **Rural / peri-urban (城乡结合部) properties may have partial provision** — verify per parcel.

### Operators

| Utility | Operator | Notes |
|---|---|---|
| **Water + sewerage** | 自来水公司 (city-level water utility) — e.g., 北京市自来水集团, 上海城投水务, 深圳水务 | Tariffs city-set; subsidised residential; commercial higher tier |
| **Electricity** | **国家电网 (State Grid)** for ~88 % of national territory + **南方电网 (Southern Grid)** for Guangdong / Guangxi / Yunnan / Guizhou / Hainan | Tariff: residential ~¥0.50–0.62 /kWh tier 1, rising to ~¥0.80 /kWh tier 3 (peak); commercial ~¥0.85+ /kWh |
| **Gas (town gas)** | 中燃 / 港华燃气 / 北京燃气 / 上海燃气 — mostly partly-state mixed-ownership | Pipeline gas in most Tier-1/2 urban; some peri-urban LPG cylinder |
| **Heating (winter only — north of Yangtze)** | 集中供暖 (district heating) network — operator varies by city | Mandatory billing for connected buildings; opt-out limited |
| **Telecoms / fibre** | China Telecom 中国电信, China Unicom 中国联通, China Mobile 中国移动 — state-owned big-3 | Fibre-to-home universal in Tier-1/2; Gigabit common Tier-1 |

### Verification

- For new-build (商品房) post-2010: utility connection certified at 验收 (inspection) before 五证齐全 (five-certificate completion) — assume all four mains present
- For older stock (pre-1998 housing-reform legacy units, 房改房, 单位福利房): verify each utility individually with the 物业 (property management) and the building 居委会 (residential committee)
- For 公寓 (40-yr commercial-residential): often **commercial-tier electricity tariff** (~30–50 % higher than residential) + **no town-gas in some cities** (electric cooking only) + **commercial water tariff** + **no district heating in northern cities** — material total-cost-of-ownership impact; verify before underwriting
- **Trap**: rural villas / 农村自建房 / 小产权房 ("small-property-right" houses on rural collective land — **NOT legal commodity housing for foreign or non-Hukou-village buyers**) — utility provision often informal; 小产权房 is a separate non-purchasable category; **never buy 小产权房 as a foreign individual**

### Costs (Tier-1 city, 2025 reference)

| Scenario | Cost |
|---|---|
| Water (residential, < tier 1 cap, urban) | ~¥4–6 /m³; capped tier 1 typically 220 m³/yr/household |
| Electricity (residential, tier 1) | ¥0.50–0.62 /kWh; cap ~2,160 kWh/yr; tier 3 reaches ¥0.78–0.85 /kWh |
| Town gas (residential) | ¥2.5–3.5 /m³ |
| Northern district heating (winter) | ¥18–30 /m²/season (Beijing ~¥30, Tianjin ~¥25, Harbin ~¥40+) |
| Average household monthly utility bill (Tier-1, 2 occupants, 90 m² apartment) | ~¥400–800/mo (excl. winter heating) |
| Property management fee | ¥1.5–6.0 /m²/mo standard; ¥8–15 /m²/mo luxury / international |

(Verify all current tariffs at the city utility's website at the time of bill date — tier ladders are city-set and revised periodically.)

---

## Section: `--currency` (China-specific override — material to all foreign-buyer scenarios)

### RMB capital controls — the operative constraint

Mainland China operates a **partially closed capital account**. **The single most material constraint for foreign property buyers is FX inflow / outflow**.

### SAFE individual FX quota

- **State Administration of Foreign Exchange (SAFE / 国家外汇管理局)** — `https://www.safe.gov.cn/en/` — administers RMB convertibility
- **Individual annual FX purchase / sale quota: equivalent of US$50,000 per person per year** ([SAFE 个人外汇管理办法实施细则 第二条, 2007 — verify annual increase if any](https://www.safe.gov.cn/tianjin/2024/0430/2464.html))
- **PRC citizens** sending CNY abroad: subject to the US$50K equivalent annual quota; aggregation across family members or split-transactions is **outright illegal** (split-purchase by 5+ named individuals on linked transactions = 蚂蚁搬家 "ants moving" — flagged by SAFE and bank AML monitoring)
- **Foreign individuals** bringing FX into China to buy property: **separate inflow rules** under [SAFE 2025-09-15 Notice on Cross-Border Investment Reform](https://www.safe.gov.cn/) (汇发〔2025〕43号 / Huifa [2025] No.43) — the Greater Bay Area HK/Macao 'settle-first' (先结后补) home-purchase FX facilitation was extended nationwide, so overseas individuals lawfully resident and working in China can settle FX for property purchase based on the contract at the initial stage (rolled out nationwide 15 Sep 2025; previously HK/Macao residents only). This is a **bank-settlement procedure optimization only** — SAFE clarified it does **NOT** change existing foreign-individual purchase-qualification rules (the 171号文 1-yr residence requirement, one-property-nationwide cap, own-use restriction, and local Hukou / social-security overlays all remain in force; the "restriction lifted" reading was a misreading) (2026-07-02 verified, source: State Council policy Q&A gov.cn + SAFE). **Foreign buyers must keep all FX-inflow records** (inbound bank wire receipts, declaration to local SAFE branch)
- **Sale-side repatriation** (foreign individual selling PRC property and converting CNY proceeds back to FX for outflow): **highly process-heavy** — requires:
  1. Original FX-inflow proof (bank receipts, original SAFE inbound declaration)
  2. Property tax-clearance certificate at sale
  3. Original purchase contract + sale contract notarised
  4. SAFE 个人结售汇 (individual FX purchase/sale) approval at the local SAFE branch
  5. Bank-level execution
- **Repatriation timeline**: 1–6 months typical for clean cases; can extend > 12 months in complex cases (missing receipts, cross-decade ownership, marital-property disputes)
- **Repatriation FX rate**: spot CNY/foreign currency at execution day — exchange-rate movement risk between sale and outflow is real (CNY weakened ~12 % vs USD 2022–2024)
- **Key risk**: **if FX-inflow documentation was incomplete at original purchase, repatriation may be impossible or delayed indefinitely**. Foreign buyers MUST keep meticulous FX-inflow records from day 1

### CNH (offshore renminbi) and HKD-pegged context

- Onshore CNY and offshore CNH typically trade within ±300 bps of each other; can diverge in stress events (e.g., 2015 deval, 2022 Q3-Q4)
- Hong Kong CNH market provides limited deliverable hedging for property-sale-proceeds FX risk; not all retail Chinese banks support CNH transactions
- **Foreign buyers should consider FX-hedging the sale-side (CNY → home-currency) at planned exit**, especially for sub-5-year holds — the cost of NDF / CNH-DF hedging is small relative to a 10–20 % FX move

### CNY trend 2022 → 2026

- USD/CNY climbed from ~6.35 (Q1 2022) → ~7.30+ (Q3 2024) → ~7.10–7.30 (Q1–Q2 2026 range, PBOC fix)
- PBOC managed-float kept depreciation orderly; no full free-float planned
- Long-term: structural CNY softening probable as growth gap with US narrows but capital-account controls retained — foreign property holders bear the carry-cost of the closed capital account

### Practical foreign-buyer FX checklist

1. Keep ORIGINAL inbound bank wire receipts AND original SAFE inbound declaration paperwork — store off-PRC copies
2. Confirm purchase contract is in your individual name (NOT a relative / nominee — repatriation requires owner = original FX-inflow declarant)
3. Pay all property-related taxes from **the same SAFE-declared account** to maintain audit trail
4. At sale, expect 2–6+ months between transaction completion and FX repatriation
5. Hedge or lock CNY → home-currency at sale-contract signing if exit is < 5-year horizon

---

## Cost benchmarks (CN 2025–2026, Tier-1 reference)

| Item | Cost (¥) |
|---|---:|
| 不动产登记 (real-estate registration fee, residential) | ¥80 / property |
| 不动产权证书 (Real-Estate Title Certificate) issuance | included in registration fee |
| 公证费 (notary, optional resale) | ~0.3 % of price (capped) |
| 测绘费 (survey, if needed) | ¥1.36 / m² built area, capped per city |
| 银行评估费 (bank valuation, mortgaged) | ¥500–¥3,000 |
| 中介费 (agent commission) | 2–3 % of price (split buyer + seller; Beike default ~2 %) |
| 律师费 (lawyer, optional, recommended for foreigners) | ¥3,000–¥30,000 |
| Renovation (mid-spec, 90 m² Tier-1 apt, 全装修硬装) | ¥150,000–¥400,000 (~¥1,700–4,500 /m²) |
| Renovation (luxury Tier-1) | ¥800,000–¥3M+ (¥10,000+/m² possible) |
| 物业管理费 (HOA) — standard Tier-1 | ¥1.5–6.0 /m²/mo |
| 物业管理费 — luxury / international | ¥8–15 /m²/mo |
| Northern winter heating (Beijing typical) | ¥30 /m²/season |
| 学区房 premium (Tier-1 prime school district) | +30–80 % over equivalent non-学区 stock — verify school-policy still attached |
| **Deed tax (1st residential, ≤140 m²)** | **1 % of price** |
| **Deed tax (1st residential, >140 m²)** | **1.5 %** |
| **Deed tax (2nd residential, ≤140 m²)** | **1 %** |
| **Deed tax (2nd residential, >140 m²)** | **2 %** |
| **Deed tax (3rd+ residential)** | **3–5 %** (province-set statutory rate) |
| **VAT on sale by individual <2 yrs hold** | **3 %** of price (from 2026-01-01; was 5 %) |
| VAT on sale by individual ≥2 yrs hold | 0 % (ordinary housing) |
| IIT on sale (verifiable basis) | 20 % × gain |
| IIT on sale (deemed method) | 1 %–3 % of price (city-set; Beijing 1 %) |
| House Property Tax on individual rental | 12 % flat (Beijing 4 %) of rent — selectively enforced |
| IIT on rental | 20 % nominal (effective ~16 % after 20 % deduction) |

## Active fiscal incentives (2025–26)

- **Sept 2024 stimulus**: 15 % minimum down-payment first home + second home; mortgage-rate floor abolished (most cities); tier-1 residency / social-security thresholds eased
- **Nov 2024 deed tax**: 1 % uniform first/second home ≤ 140 m²; 1.5 %/2 % > 140 m²; LVAT pre-collection rate cuts (developer side)
- **Dec 2025 VAT cut to 3 % for short-held (< 2-yr) individual sales** (eff. 2026-01-01)
- **Pre-2026 普通/非普通住宅 distinction abolished** in tier-1 cities for VAT exemption purposes
- **"白名单" project-funding scheme**: developers' selected projects receive credit-line support to ensure 保交楼 delivery
- **SAFE cross-border FX reform (15 Sep 2025, 汇发〔2025〕43号)**: two distinct measures — (a) the capital-account FX-income negative-list bar on using such funds (enterprise / FIE capital-account funds) to buy **non-self-use residential** property was removed; (b) the GBA HK/Macao 'settle-first' (先结后补) contract-stage FX-settlement facilitation was extended nationwide to overseas individuals. **Procedural only — foreign-individual purchase-qualification rules unchanged (SAFE "misreading" clarification)**
- **Mortgage rate cuts cycle**: 5-year LPR cut multiple times 2024–2025 (PBOC); existing-mortgage repricing applied to most outstanding mortgages

## Common listing platforms

- **贝壳 / Beike + 链家 / Lianjia**: `https://www.ke.com/`, `https://www.lianjia.com/` *(per listing — verify against 不动产登记中心)*
- **安居客 / Anjuke**: `https://www.anjuke.com/` *(per listing — verify)*
- **58同城 / 58.com**: `https://www.58.com/` *(per listing — high noise; verify thoroughly)*
- **房天下 / Fang.com**: `https://www.fang.com/` *(per listing — verify)*
- **Q房网 / Q-Fang** (SZ/GZ strong): `https://www.qfang.com/` *(per listing — verify)*
- **我爱我家 / 5i5j** (BJ/SH strong): `https://www.5i5j.com/` *(per listing — verify)*
- **中原地产 / Centaline (mainland operations)**: `https://www.centanet.com/` (also a Hong Kong brand) *(per listing — verify)*

## Caveats unique to mainland CN

- **No private freehold over land** — 70-year Land Use Right (residential) is leasehold-equivalent; 40-year (commercial-residential) shorter and without auto-renewal under Civil Code Art. 359
- **Civil Code Art. 359 auto-renewal residential — but renewal-fee mechanics statutorily undefined** (deferred to "future regulations"); no large-scale 70-yr-LUR-expiry test has occurred yet (the first commercial 1990s grants will expire ~2060+, residential ~2090+); a small Wenzhou 2016 case set partial precedent but not nationally binding
- **Foreign-individual one-property-nationwide rule under 171号文 (2006)** + **1-year residence prior to purchase** — unchanged 2024–2026
- **Local Hukou / social-security overlay** in tier-1 cities (2026-08-07 verified; Beijing 400号 + Shenzhen 86号 limbs 2026-09-24): Beijing **1-yr citywide** (京建发〔2026〕400号, in force 8 Aug 2026, superseding the 2-yr-inside-5th-Ring band of 京建发〔2025〕565号; outside-5th-Ring purchases unlimited in number for 1-yr payers since 8 Aug 2025); Shanghai **1-yr citywide** (outside the outer ring from 1 Oct 2024, inside it only from 26 Feb 2026 per 沪七条); Shenzhen **1-yr** with district-differentiated unit caps (深建字〔2025〕199号, eff. 6 Sep 2025; no qualification check at all in 盐田 / 大鹏; +1 unit in 福田 / 南山 / 宝安-新安 and a residence-permit route to 1 unit there per 深建字〔2026〕86号, eff. 30 Apr 2026); Guangzhou no restriction (穗府办函〔2024〕65号, from 30 Sep 2024) — verify with each city's 住房保障和房产管理局 / 住建委 at time of offer
- **No nationwide property tax** for individuals (May 2026); Shanghai + Chongqing pilots only; nationwide rollout suspended pending market recovery
- **Deed tax restructured Dec 2024** (Announcement 2024 No.16): 1 % / 1.5 % / 2 % per scenario, **uniform nationwide including tier-1** — the tier-1 3 % second-home treatment is abolished; only 3rd+ homes and non-qualifying transfers pay the province-set **3–5 %** statutory rate
- **VAT on sale**: 3 % from 2026-01-01 for < 2-yr holds (was 5 %); ≥ 2-yr exempt (普通住宅 city-defined; 普通/非普通 distinction abolished in tier-1 2024)
- **IIT 20 % on sale gain** OR 1 %/1.5 % deemed of price; 5-yr-only-family-home exemption available
- **House Property Tax 12 % on rental** by individual (Beijing 4 %); enforcement intensifying 2024–2025
- **Foreign-individual rental** technically restricted under 171号文 (own-use only) — assume exposure
- **SAFE individual annual FX quota US$50,000** (PRC residents converting RMB out); foreign-buyer FX inflow has separate route post-Sept 2025 reform
- **Sale-side FX repatriation** is process-heavy (2–6+ months); requires complete original FX-inflow paperwork
- **Pre-sale (期房) risk**: 烂尾楼 / undelivered units — verify 保交楼 inclusion + completion timeline; bias toward 现房 (already-completed) inventory or major-state-developer pre-sale
- **Sham listings (假房源)** prevalent across all consumer platforms (Beike/Lianjia best-controlled, 58.com worst); always cross-verify
- **公摊面积 (common-area share)** inflates 建筑面积 by 20–35 % over interior; Tier-1 luxury may have 30 %+; ¥/m² benchmarking must distinguish
- **学区房 (school-district)** premium 30–80 %+ — but school-zoning policy revisions are frequent and entitlement can be administratively withdrawn; verify within 12 months
- **公寓 (40-yr commercial-residential)** mortgage / liquidity / utility cost penalties — discount of 30–50 % vs 70-yr residential adjacent
- **小产权房 ("small-property-right" rural-collective housing)** is **legally non-purchasable** by foreign or non-Hukou-village individuals — never buy
- **Currency: CNY managed-float**; CNH offshore differs; closed capital account = real holding cost
- **Hukou-attached benefits** (school, healthcare): foreign owners do **not** receive Hukou via property purchase — purely independent regimes
- **PRC tax residency 183-day rule** + 6-year reset: foreign owners spending substantial time in China must monitor tax-residency exposure on worldwide income
- **PR (永久居留 / "Chinese Green Card")**: extremely selective; total grants since 1985 < ~30,000 individuals through 2024
- **Weak owners-association rights**: 业主大会 / 物业管理 disputes common; contracts often weighted toward developer-affiliated 物业 company; 业主自治 (owner self-governance) reform 2009+ has improved but uneven
- **Pre-Evergrande inventory overhang**: Tier-3/4 absorption horizon 2024–2030; foreign capital structurally absent from Tier-3/4
- **Niseko-equivalent foreign-tourist resort markets** in mainland CN are limited (Sanya / Hainan free-trade zone has the most material foreign-friendly residential market; ski resorts e.g., 长白山, 万达 at Changbai or 北大壶 at Jilin niche)

## Reddit / forum sources

- **r/china** (general) — politically charged; useful for high-level signal
- **r/Sino** — China-positive editorial slant; not for property due diligence
- **r/shanghai**, **r/Beijing**, **r/Shenzhen**, **r/Guangzhou** — city-specific expat communities
- **r/expats** — relocation logistics, FX, taxation
- **小红书 / Xiaohongshu (Red, RedNote)** — `https://www.xiaohongshu.com/` — user-generated property reviews, neighbourhood guides; valuable but subject to platform censorship and sponsored-content noise
- **知乎 / Zhihu** — `https://www.zhihu.com/` — Q&A; long-form property discussions; expert + amateur mixed
- **microsegment forums**: 看房网, 买房网 — niche
- **微信公众号 (WeChat Official Accounts)**: numerous property-focused accounts run by 中介 / KOLs; vary widely in quality

## Verification authorities

| Authority | When to call / visit |
|---|---|
| **不动产登记中心** (district level) | Title verification, encumbrance check, ownership transfer |
| **住房和城乡建设部 / 住建局 (MoHURD / local Housing Bureau)** | Pre-sale licence, 保交楼 inclusion, building-quality inspection |
| **税务局 (Tax Bureau)** + 12366 hotline | Deed tax, VAT, IIT calculation; rental-income reporting |
| **国家外汇管理局 / SAFE branch** | FX-inflow declaration, FX-outflow approval at sale |
| **公安局出入境管理 (Public Security Bureau Exit-Entry)** | Visa, residence permit, foreign-guest registration |
| **国家移民管理局 / NIA** | PR application |
| **银行 (mortgage bank)** | Mortgage origination, valuation, discharge |
| **物业管理 (HOA)** | Sinking fund, AGM minutes, planned major works, approval letters |
| **居委会 (residential committee)** | Local-level certifications, inventory of permanent-residents |
| **教育局 (Education Bureau)** | School-district 学区 status verification within last 12 months |
| **自然资源局 (Natural Resources Bureau)** | LUR remaining, geological hazard zoning, control plan overlay |
| **人社局 (Human Resources & Social Security Bureau)** | Social-security record for purchase eligibility |
| **公证处 (Notary Office)** | Marital-property + co-owner consent if elected |

## Source URL templates

| Source | URL |
|---|---|
| NBS English statistics portal | `https://www.stats.gov.cn/english/` |
| MoHURD | `https://www.mohurd.gov.cn/` |
| PBOC | `http://www.pbc.gov.cn/` |
| SAFE English | `https://www.safe.gov.cn/en/` |
| State Taxation Administration English | `http://www.chinatax.gov.cn/eng/` |
| Ministry of Natural Resources | `https://www.mnr.gov.cn/` |
| Ministry of Emergency Management | `https://www.mem.gov.cn/` |
| China Earthquake Administration | `https://www.cea.gov.cn/` |
| Ministry of Ecology & Environment | `https://www.mee.gov.cn/` |
| China Meteorological Administration | `https://www.cma.gov.cn/` |
| Ministry of Water Resources | `http://www.mwr.gov.cn/` |
| State Council English (gov.cn) | `https://english.www.gov.cn/` |
| China Real Estate Association | `http://www.fangchan.com/` |
| China Index Academy (private) | `https://industry.fang.com/` |
| Beike / 贝壳 | `https://www.ke.com/` |
| Lianjia / 链家 | `https://www.lianjia.com/` |
| Anjuke / 安居客 | `https://www.anjuke.com/` |
| Fang.com / 房天下 | `https://www.fang.com/` |
| 58.com / 58同城 | `https://www.58.com/` |
| State Grid (electricity) | `https://www.sgcc.com.cn/` |
| Southern Grid | `https://eng.csg.cn/` |
| NIA (immigration / PR) | `https://www.nia.gov.cn/` |
| Civil Code (NPC text) | `http://www.npc.gov.cn/npc/c30834/202006/75ba6483b8344591abd07917e1d25cc8.shtml` |

## Quirks to know

- **Reform cycle**: property + tax + Hukou rules in mainland China are revised on average **every 12–24 months** since 2010. Verify every numeric claim against current local-bureau publication before any decision
- **Tier classification is journalistic**, not legal; the State Council does not publish a "tier-1/2/3" list. Use Yicai (第一财经) annual ranking for benchmarking only
- **Mainland vs HK / Macao / Taiwan distinction**: never combine. Each is a separate legal regime (separate playbooks)
- **70-year LUR remaining ≠ remaining ownership horizon**: Civil Code Art. 359 auto-renewal residential gives strong-but-untested promise; underwrite with appropriate hedge
- **40-year vs 70-year LUR**: structural pricing gap of 30–50 % — never benchmark across types
- **公摊 (common-area share)**: always reconcile 建筑面积 vs 套内面积; expect 20–35 % shrinkage to interior
- **学区房 (school-district)**: a high premium that can evaporate via local Education Bureau policy revision; verify within 12 months
- **保交楼 inclusion** for distressed-developer pre-sale stock is the difference between getting your unit and an indefinite "烂尾楼" wait
- **SAFE FX inflow paperwork** must be perfect on day 1 for sale-side repatriation to work later
- **Tax-residency 183-day + 6-year rule**: if you spend > 6 months/yr in PRC, you become a tax resident
- **No nominee / split-name purchases** under 171号文; foreign-individual must be the named buyer
- **Pre-purchase inspection**: independent surveyors / 验房师 industry exists but is small; budget ¥3,000–¥10,000 for a credible inspection of pre-sale or older stock
- **"5 + 1 + 1" mortgage stress-test framework** (2017+) constrains LTV — varies by city; foreign-individual mortgageability depends on income proof + local bank policy + may require co-applicant or higher down payment
- **Mortgage product structure**: variable-rate LPR-linked since Aug 2019; reset annually on borrower-chosen reset date; fixed-rate options limited
- **Down-payment minimums (post-Sept 2024)**: 15 % first home + 15 % second home for most cities; tier-1 (BJ/SH/SZ) some districts retain 20–25 % thresholds

## Status

**Status**: ✅ fully populated as of 2026-05-07
**Confidence**: MEDIUM — primary sources (NBS, PBOC, MoHURD, SAFE, STA) are authoritative for tax / regulatory / price-index claims; tier-1 city benchmark prices are wide indicative bands drawn from Beike / Lianjia / Anjuke listing aggregates and NBS 70-city index trend, NOT parcel-level transactions; foreign-buyer 171号文 + tier-1 social-security overlay rules are city-administered and revised at 12–24-month cadence — re-verify with destination city 住建委 / 房屋管理局 before any offer; SAFE FX-inflow / outflow rules eased Sept 2025 but operational implementation varies by branch — verify; property-tax rollout suspended (May 2026) but politically live; Civil Code Art. 359 auto-renewal residential is statutorily promised but renewal-fee mechanics undefined and untested at scale.
**Last verified**: 2026-08-07 (`--tax` and `--foreign-buyer` re-verified — the MoF/STA/MOHURD Announcement 2024 No.16 deed-tax regime, and the tier-1 non-local social-security/IIT purchase thresholds for Beijing, Shanghai, Shenzhen and Guangzhou; balance of the 2026-05-27 pass unchanged; national common-language law revision and work-permit administering authority corrected 2026-09-18 per moe.gov.cn + MOHRSS 12333.gov.cn). Foreign-buyer / tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).

**Researched by**: Opus 4.7 (1M context, parallel-subagent batch, 2026-05).

**Notes**: Deed tax (Announcement 2024 No.16 — 1%/1.5%/2% uniform nationwide incl. tier-1; 3rd+ and non-qualifying transfers at the province-set 3–5% statutory rate, eff. 2024-12-01), VAT cut (5%→3% for <2yr holds, eff. 2026-01-01), Sept 2024 stimulus (15% down + tier-1 residency easing), Civil Code Art. 359 auto-renewal residential (eff. 2021-01-01, renewal-fee TBD), 171号文 1-year residence + one-property-nationwide rule (2006, unchanged), Shanghai/Chongqing property-tax pilot (eff. 2011-01-28; 2021 NPC pilot-expansion authority lapsed 2026), SAFE Sept 2025 cross-border investment reform (汇发〔2025〕43号; GBA HK/Macao 'settle-first' FX-settlement facilitation extended nationwide; capital-account negative-list bar on FIE funds buying non-self-use residential removed — procedural only, foreign-individual purchase-qualification rules unchanged per SAFE clarification), Tier-1 city home-purchase restrictions (re-verified 2026-08-07 against the city Housing Bureaux): Beijing 1-yr SS citywide (京建发〔2026〕400号, in force 8 Aug 2026, superseding the 2-yr-inside / 1-yr-outside split of 京建发〔2025〕565号 — the previously-recorded 5-yr figure was the pre-reform value), Shanghai 1-yr SS citywide (outside the outer ring from 1 Oct 2024, inside it from 26 Feb 2026 per 沪七条), Shenzhen 1-yr SS with district-differentiated unit caps (深建字〔2025〕199号, eff. 6 Sep 2025 — not the previously-recorded 3-yr; core-district +1 unit and residence-permit route per 深建字〔2026〕86号, eff. 30 Apr 2026), Guangzhou abolished (穗府办函〔2024〕65号, from 30 Sep 2024); tax / FX / price claims verified against PBOC / MoHURD / NBS / SAFE / STA / State Council English releases as of 2026-05. **Re-verify before any live decision**: city-level Hukou / social-security rules (revised every 12–24 months); current 普通/非普通 housing definitions per tier-1 city; school-district 学区 policy of destination unit's 教育局 within last 12 months; 保交楼 inclusion for any pre-sale (期房) purchase; foreign-buyer mortgage policies of destination city's banks; LUR remaining on the 不动产权证书 + projected renewal mechanics; SAFE local-branch operational implementation of Sept 2025 cross-border investment reform; current PR (Chinese Green Card) eligibility from National Immigration Administration. **Special caution**: Hong Kong / Macao / Taiwan are separate playbooks with separate legal regimes — never combine. Mainland-Chinese property tax / regulatory environment is among the most rapidly-evolving globally; this playbook is a framework, not parcel-level data. Confidence is MEDIUM (not HIGH) because (a) parcel-level pricing requires Beike 历史成交 / 不动产登记中心 lookup not feasible from outside, (b) sham-listing prevalence on consumer platforms reduces listing-data trustworthiness, (c) Civil Code Art. 359 renewal-fee mechanics remain statutorily undefined and untested at scale, (d) tier-1 city Hukou / social-security overlay rules are revised at 12–24-month cadence, (e) the post-Evergrande recovery cycle is mid-stream with continued policy support but uncertain absorption horizon for Tier-3/4 inventory.
