# 대한민국 / South Korea 🇰🇷 — Property Due-Diligence Playbook

ISO2: `kr`. Status: ✅ Fully populated (researched 2026-05).

## Country profile

- **우편번호 (postcode)**: 5 digits since 2015 (e.g., `04524` for 서울 중구; `06236` for 강남구 역삼동; `48058` for 부산 해운대구). Pre-2015 6-digit format deprecated.
- **Admin levels**: 1 특별시 (Seoul) + 6 광역시 (metropolitan cities — Busan, Daegu, Incheon, Gwangju, Daejeon, Ulsan) + 1 특별자치시 (Sejong) + 8 도 (provinces) + 2 특별자치도 (Jeju, Gangwon, Jeonbuk) → 시 (city) / 군 (gun) / 구 (gu / autonomous district) → 동 (dong) / 읍 (eup) / 면 (myeon)
- **Currency**: KRW (₩). 1 EUR ≈ 1,450–1,550 KRW (variable Q1 2026); 1 USD ≈ 1,350–1,450 KRW
- **Languages**: Korean (한국어) — official; English usable in Seoul finance/legal services but contracts default to Korean
- **Cadastre**: **등기부등본 (deungibu deungbon — Real Estate Register)** maintained by **대한민국 법원 등기소** (Court Registry Office, Supreme Court of Korea) — online via **인터넷등기소 (IROS)** at `https://www.iros.go.kr/`; paid lookup ~₩700–₩1,000 per certified extract
  - Separate **건축물대장 (geonchungmuldaejang — Building Register)** + **토지대장 (toji daejang — Land Register)** maintained by 시·군·구청 — online via **정부24** (`https://www.gov.kr/`)
  - Single-portal real-estate disclosure: **부동산종합공부시스템 (일사편리)** at `https://kras.go.kr/`
- **Identifier**: 지번 (jibeon — lot number, e.g., `서울특별시 강남구 역삼동 678-1`) + post-2014 도로명주소 (doroname jusoroad name address, e.g., `서울특별시 강남구 테헤란로 152`); **고유번호** (19-digit unique property number) on 등기부
- **Title concept**: 소유권 (소유권 — freehold) is dominant; 전세권 (jeonseigwon — registered jeonse lump-sum lease right) and 임차권 (imchaigwon — rental right) are encumbrances on the title. **Foreigners can hold freehold** subject to notification (see below).
- **Foreign-buyer regime**: **외국인토지법 (Foreign Land Acquisition Act)** abolished 2017; replaced by **부동산 거래신고 등에 관한 법률 (Real Estate Transactions Reporting Act)** + **부동산 거래신고법 시행령** — open reciprocal regime. Foreigners (incl. EU/US/JP/CA/AU/UK nationals) may purchase freehold residential without permission, BUT must file **외국인 부동산 취득 신고** at city/gun/gu office within **60 days of contract** (MOLIT 국토교통부 form). ([source](https://www.law.go.kr/법령/부동산거래신고등에관한법률))
  - Restricted/permission-required zones: 군사기지 및 군사시설 보호구역 (military protection zones), 문화재 보호구역 (cultural property), 생태·경관 보전지역 (ecological), 자연환경보전지역 — confirm via **토지이음 (LURIS 후신)** at `https://www.eum.go.kr/`
  - Permission (허가) timeline if zone restricted: ~15 days
- **Recent reforms**:
  - **전세사기 피해자 지원 및 주거안정에 관한 특별법 (Jeonse Fraud Special Act)** — enacted 2023-05-25, effective 2023-06-01; extended Jun 2024; latest amendments through 2025 expanding compensation. ([MOLIT source](https://www.molit.go.kr/USR/policyData/m_34681/dtl.jsp?id=4694))
  - **공인중개사법 개정** (Licensed Real Estate Agent Act amendments 2024) — strengthened agent disclosure obligations re: jeonse risk, expanded fiduciary duty
  - **종합부동산세법 개정 2023** — Yoon administration cut multi-home surcharge rates and raised exemption thresholds (effective FY2023 onward)
  - **취득세법 시행령 개정 2024–2025** — multi-home acquisition tax restructuring; 8 %/12 % surcharge regime for 2nd/3rd+ homes in 조정대상지역 (regulated zones) modified
  - **반환보증보험 (Jeonse return-guarantee insurance) reform 2023–2024** via HUG (주택도시보증공사) — eligibility criteria tightened (공시가격 126 % cap on guarantee value)

## Section: `--price`

### Primary sources

- **국토교통부 실거래가 공개시스템 (RTMS — Real-estate Transaction Management System)** — mandatory disclosure of every contract price since 2006, residential apt; expanded to villa/officetel/single-family in stages
  - Portal: `https://rt.molit.go.kr/`
  - Granularity: 동 (dong) + 단지/번지 (apt complex / lot) + month + 전용면적 (exclusive area, 평형)
  - Update cadence: contracts must be filed within 30 days; data appears 30–60 days post-contract
  - **Major transparency advantage** vs JP/EU: every transaction publicly visible by complex
- **공시가격 (gongsi-gageok — Official Price)** — annual MOLIT/local-gov assessment, 1 January reference, published Q1
  - **공동주택 공시가격** (apartment): `https://www.realtyprice.kr/`
  - **개별주택 공시가격** (single-family) + **표준지 공시지가** (standard land): same portal
  - Used as base for property tax + comprehensive RE tax + jeonse insurance cap
- **한국부동산원 (Real Estate Board of Korea — REB)** — quasi-government statistics agency
  - Portal: `https://www.reb.or.kr/`
  - Publishes **전국주택가격동향조사** (monthly price trend index), **부동산 통계정보 R-ONE** at `https://www.reb.or.kr/r-one/`
- **KB부동산** (KB Kookmin Bank) — bank-aggregated index, weekly; widely cited in media; closed-ish dataset (`https://kbland.kr/`)
- **네이버 부동산 시세** — Naver aggregated asking-price ranges per complex: `https://land.naver.com/`

### Listing platforms (consumer-facing)

- **네이버 부동산 (Naver Real Estate)** — `https://land.naver.com/` — dominant aggregator; URL pattern `https://new.land.naver.com/complexes/<complexId>` for apt complexes
- **다방 (Dabang)** — `https://www.dabangapp.com/` — strong for villa/원룸/오피스텔; mobile-first
- **직방 (Zigbang)** — `https://www.zigbang.com/` — apt + officetel + villa; UX strong
- **호갱노노 (Hogangnono)** — `https://hogangnono.com/` — analytics-forward; integrates RTMS
- **부동산114** — `https://www.r114.com/` — legacy, agent-tilted
- **공실클럽** + **상가의신** — commercial / 상가

### Premium-area benchmarks (2025-Q4 / 2026-Q1 reference, RTMS + KB부동산 + 공시가격)

| Area | Apt ₩/m² range (₩/3.3m² 평) | Notes |
|---|---|---|
| 서울 강남구 (Gangnam) | ~₩30M–₩60M+/m² (~₩100M–₩200M+/평) | 압구정/대치/도곡 핵심 단지 (RTMS 2025; "압구정현대" routinely >₩70M/m²) |
| 서울 서초구 (Seocho) | ~₩28M–₩55M/m² | 반포/잠원 한강뷰 단지 premium |
| 서울 송파구 (Songpa) | ~₩20M–₩40M/m² | 잠실 핵심 단지 |
| 서울 용산구 (Yongsan) | ~₩22M–₩45M/m² | 한남/이촌 high-end; 한남더힐 ultra-premium |
| 서울 마포·성동·광진구 | ~₩15M–₩28M/m² | 신축 위주 |
| 서울 25개 구 평균 (2025) | ~₩14M–₩18M/m² (Seoul avg apt) | KB부동산 2025-12 시세 ([cite](https://kbland.kr/)) |
| 부산 해운대구 (Busan) | ~₩9M–₩20M/m² | 마린시티/엘시티 럭셔리 ₩25M+ |
| 인천 송도 (Songdo, Incheon) | ~₩7M–₩15M/m² | IFEZ free-zone effect |
| 대구 수성구 | ~₩7M–₩14M/m² | "대구 강남" 학군 |
| 세종특별자치시 | ~₩5M–₩10M/m² | 행정수도 효과 둔화 |
| 제주특별자치도 | ~₩3M–₩8M/m² | 외국인 매수 제한 별도 검토 |
| 지방 중소도시 평균 | ~₩2M–₩5M/m² | 지방 demographic decline 반영 |

⚠️ Korean convention is **₩/평** (1 평 = 3.3058 m²) for marketing; technical/legal docs use **₩/m²**. Conversion: ₩50M/평 ≈ ₩15.1M/m².

### Compute

1. Listing ₩/m² = listing price ÷ **전용면적 (jeonyong myeonjeok — exclusive/private area)** — NOT 공급면적 (gonggeup myeonjeok — supply area, includes proportional share of corridors/lobby) which Korean listings often headline
2. **Trap**: 전용 vs 공급 vs 계약면적 — supply area is typically ~25–30 % larger than exclusive; quoted "32평" usually = 공급 105.8 m² ≈ 전용 84 m² for typical 국민주택 (national-standard housing)
3. Compare to RTMS (last 6 months, same 단지 + same 평형 + same 동/층 if possible) — same-complex comps are unusually clean in KR vs other markets
4. Cross-check 공시가격 (typically 60–80 % of market for apt; closer to 70 % post-2024 reform)
5. **Trap**: 분양가 (bunyangga — pre-sale price for new builds) vs 시세 (sise — current market price) often diverges sharply post-입주 (move-in); 분양가상한제 (price cap) zones distort
6. **Trap**: **로열층/로열동** (royal floor/building) — same complex same-area units vary 10–20 % by floor + view; check unit-level RTMS
7. **Trap**: **재건축/재개발 (redevelopment)** premium baked into older 강남/목동/노원 complexes — the building's own valuation is partial; the redevelopment option value drives 30–50 % of price

### Trend Q4 2024 → Q1 2026

- BOK base rate cut from 3.50 % (peak 2023) → 3.25 % Oct 2024 → 3.00 % Nov 2024 → 2.75 % Feb 2025 → 2.50 % May 2025 (BoK MPC) → held through 2026-Q1; mortgage rates following slowly ([BOK source](https://www.bok.or.kr/eng/main/main.do))
- DSR (Debt Service Ratio) 40 % cap remains nationwide; **스트레스 DSR (stress DSR) 3단계** scheduled phasing — major LTV/DTI policy lever
- Seoul 25-ward apt prices: bull-flat through 2025; 강남3구 sustained mild gains; non-Seoul depopulation areas continuing decline
- Jeonse market: post-2022 fraud crisis caused jeonse-to-월세 (monthly rent) shift; jeonse premium decay continues; HUG insurance cap (₩7B then reformed) remains buyer's verification gate

---

## Section: `--traffic`

### Primary source

- **국토교통부 도로교통량 통계연보 (Annual Road Traffic Volume Statistics)** — published yearly by 도로공사 + 국토부
  - Portal: `https://www.its.go.kr/` (ITS National Transport Information Center)
  - Sub-portal: **교통량 정보제공시스템** at `https://www.road.re.kr/` (KICT — Korea Institute of Civil Engineering and Building Technology)
  - **고속도로 교통량** (expressway): 한국도로공사 (Korea Expressway Corp) at `https://www.ex.co.kr/`
- **TAAS (Traffic Accident Analysis System)** — `https://taas.koroad.or.kr/` — accident counts per road segment (도로교통공단 KoROAD)
- **시·도별 교통량조사** — Seoul + Busan + 광역시 publish per-district traffic counts; e.g., Seoul **TOPIS** at `https://topis.seoul.go.kr/`

### Key term

**AADT (연평균 일교통량)** — annual average daily traffic; directly equivalent to international AADT. Counted at fixed observation stations + manual surveys.

### Verdict bands (rough)

- 🟢 < 3,000 v/d (이면도로 / 주거지 이면 / 소로 — quiet residential)
- 🟡 3,000–15,000 v/d (보조간선 / 동내 주요로 — minor arterial)
- 🟠 15,000–50,000 v/d (간선도로 / 광로 — major urban arterial)
- 🔴 > 50,000 v/d (고속국도 / 자동차전용도로 / 도시고속화도로 — expressway / urban motorway)

### Coarse fallback

OSM `highway` class:
- motorway = 고속국도 (e.g., 경부고속도로, 서해안고속도로)
- trunk = 자동차전용도로 / 일반국도 (urban motorway / national highway)
- primary = 광역시도 / 주요지방도
- secondary = 시도 / 군도
- tertiary = 면도 / 이도
- residential = 이면도로

⚠️ Apt complexes near 강변북로, 올림픽대로, 동부간선도로, 내부순환로 (Seoul urban motorways) routinely exceed 100,000 v/d — request 방음벽 + 창호 등급 (sound-attenuation walls + window class) confirmation in 중요사항 disclosure.

---

## Section: `--tax`

### Annual property tax — 재산세 (jaesanse — Property Tax)

**Owner as of 1 June each year is liable.** Bills issued July (building share) + September (land share); paid in 2 instalments by July 31 and September 30 respectively (지방세법 § 114).

**Rates** ([Local Tax Act 지방세법 + 행정안전부 source](https://www.law.go.kr/법령/지방세법)):

| Property | 과세표준 (tax base) bracket | Rate |
|---|---|---|
| **주택 (housing — building+land combined)** | ≤ ₩60M | 0.1 % |
| | ₩60M–₩150M | ₩60K + 0.15 % on excess |
| | ₩150M–₩300M | ₩195K + 0.25 % on excess |
| | > ₩300M | ₩570K + 0.4 % on excess |
| **별장 (villa/second home — designated)** | flat | 4.0 % (punitive) |
| **나대지·별도합산토지** | progressive | 0.2 %–0.4 % |
| **분리과세토지 (separate-tax land)** | flat | 0.07 %–4.0 % depending on use |

- **과세표준** = 공시가격 × **공정시장가액비율 (fair market value ratio)** — currently **45 %** for primary residence ≤₩900M; **60 %** for higher-value/multi-home owners (lowered from 60 % in 2022 reform; reverts gradually)
- **도시지역분 (urban-area surcharge)**: **0.14 %** of 과세표준 in 도시지역 (urban planning zones)
- **지방교육세 (local education tax)**: **20 %** of 재산세 액 (i.e., property tax × 1.20 effectively)

### Comprehensive Real Estate Tax (종합부동산세 — 종부세)

Federal-level wealth tax on aggregate residential property value above thresholds, paid by individual to **국세청 (NTS — National Tax Service)** December each year.

**2025-2026 thresholds + rates** ([NTS source](https://www.nts.go.kr/), 종합부동산세법):

| Status | Exemption (공시가격 합산) | Progressive rate |
|---|---|---|
| **1세대 1주택자** (single-home household) | **₩1.2B (12억원)** | 0.5 %–2.7 % progressive (0.5/0.7/1.0/1.3/1.5/2.0/2.7) |
| **다주택자** (multi-home, **2주택 이하 outside 조정대상지역**) | ₩900M (9억원) | same scale |
| **3주택 이상 OR 조정대상지역 2주택 이상** | ₩900M | **0.5 %–5.0 %** punitive scale |

- Multi-home punitive rates were cut materially in 2023 reform (Yoon administration); had peaked at 6 % under previous regime
- **Surcharge bracket trigger**: 과세표준 multiplied by 공정시장가액비율 60 % (multi-home) or 45 % (single)
- 1세대 1주택 long-term-holding deduction: up to 80 % off 종부세 액 if held + occupied 15 + years and aged 70+
- **Foreigners**: subject to 종부세 same as residents on Korea-situs property

### Capital Gains Tax — 양도소득세 (yangdosodeukse)

Rates depend on holding period + property count + zone classification ([NTS source](https://www.nts.go.kr/english/cm/cntnts/cntntsView.do?mi=11195&cntntsId=8315main.do), 소득세법 § 104):

| Scenario | Rate |
|---|---|
| **1세대 1주택, 2-yr+ resident holding, sale price ≤ ₩1.2B** | **Exempt** |
| **1세대 1주택, 2-yr+ holding, sale price > ₩1.2B** | progressive 6–45 % on gain *above* ₩1.2B-equivalent base, with 장기보유특별공제 (long-term holding deduction) up to 80 % at 10 yrs |
| **General progressive (long-term, > 2 yrs)** | **6 %–45 %** national + 10 % local surcharge ≈ effective 6.6 %–49.5 % |
| **Short-term: < 1 year holding** | **70 %** national |
| **Short-term: 1–2 years** | **60 %** national |
| **다주택자 조정대상지역 2주택** | base + **20 %p** surcharge (suspended 2022→ rolling extensions; verify status) |
| **다주택자 조정대상지역 3주택+** | base + **30 %p** surcharge (similarly suspended/extended) |
| **비사업용토지 (non-business land)** | base + 10 %p |

- **장기보유특별공제 (long-term holding deduction)**: 6 %/yr from year 3 (max 30 % for non-residence) or 4 %/yr × 2 (max 80 % for owner-occupied 1세대 1주택)
- **양도세 multi-home surcharge moratorium EXPIRED 2026-05-09 without renewal** (Lee Jae-myung administration let it lapse). Multi-home owners selling **from 10 May 2026** face surcharges again, effective rate up to **82.5 %** (including local income surtax). (2026-05-27 verified, source [Seoul Economic Daily 2026-05-01](https://en.sedaily.com/finance/2026/05/01/koreas-capital-gains-tax-hike-on-multi-home-owners-returns) + [2026-05-09](https://en.sedaily.com/finance/2026/05/09/people-power-party-slams-end-of-multi-home-owner-tax)). Verify any one-off extensions at NTS pre-transaction.

### Acquisition Tax — 취득세 (chwideukse)

Local tax (지방세) levied at contract / acquisition; paid within 60 days to 시·군·구 (지방세법 § 11-12):

| Property + buyer status | Rate |
|---|---|
| **주택, 1세대 1주택, sale price ≤ ₩600M** | **1.0 %** |
| **주택, ₩600M–₩900M sliding** | **1.0 %–3.0 %** linear (formula: rate = (price/₩100M × 2/3 − 3) %) |
| **주택, > ₩900M** | **3.0 %** |
| **2주택 (조정대상지역)** | **8.0 %** (was 8 %, reduced 2024 to 1–3 % per non-조정 location) |
| **3주택+ (조정대상지역) OR 4주택+ anywhere** | **12.0 %** punitive |
| **법인 (corporate buyer) of housing** | **12.0 %** flat |
| **상가 / 토지** | **4.0 %** |
| **농지 (farmland)** | **3.0 %** |

- **농어촌특별세 (rural special tax)**: 0.2 % surcharge on housing acquisitions
- **지방교육세 (local education tax)**: 0.4 % surcharge (or 0.1 % if reduced rate)
- **인지세 (stamp duty)** on contract: **₩150K–₩350K** flat by price band (over ₩1B = ₩350K)
- **국민주택채권 (national housing bonds)** — buyer must purchase + immediately resell at market discount: effective cost ≈ 0.2–1.0 % of price depending on 시가표준액

⚠️ Multi-home **8 %/12 % surcharge regime is the single largest fiscal lever** in KR property. **Status (2026-05-27 verified)**: 조정대상지역 **re-EXPANDED 2025-10-15** to all **25 Seoul wards + 12 Gyeonggi cities** + 투기과열지구 re-designations; 강남/서초/송파/용산 retain 토지거래허가구역 status to 2026-12-31 (source [korea.kr policy news 148950973](https://www.korea.kr/news/policyNewsView.do?newsId=148950973)). Earlier "narrowed to 강남3구+용산" framing was Yoon-era and is now outdated. Verify current zone list via NTS at transaction time.

### Example calculations (worked, transparent inputs)

**Example A: ₩1.5B (15억원) 84 m² apt in 강남구, single-home owner-occupier, 공시가격 ₩1.05B (70 % of market)**

- **취득세** (1세대 1주택 > ₩900M): ₩1.5B × 3 % = **₩45M** + 농특세 0.2 % ₩3M + 교육세 0.4 % ₩6M = **~₩54M one-time**
- **재산세 + 도시지역분 + 교육세** (annual, 과세표준 = ₩1.05B × 45 % = ₩472.5M):
  - 재산세: ₩570K + 0.4 % × (₩472.5M − ₩300M) = ₩570K + ₩690K = **₩1.26M**
  - 도시지역분: ₩472.5M × 0.14 % = **₩661K**
  - 지방교육세: ₩1.26M × 20 % = **₩252K**
  - Subtotal: **~₩2.17M/yr**
- **종합부동산세** (1세대 1주택, exemption ₩1.2B, 공시 ₩1.05B): under threshold → **₩0**
- **Total Y1 transaction**: ~₩54M; **Annual recurring**: ~₩2.17M (~€1,400)

**Example B: ₩2.5B (25억원) 강남 apt, multi-home owner (2nd home, 강남구 = 조정대상지역)**

- **취득세** (조정 2주택, 8 % regime if active): ₩2.5B × 8 % = **₩200M** one-time
- **재산세** (공시 ₩1.75B × 60 % multi-home ratio = 과세표준 ₩1.05B): ₩570K + 0.4 % × ₩750M = **~₩3.57M/yr** + surcharges → **~₩4.6M/yr**
- **종부세** (multi-home, 공시 over ₩900M threshold; (₩1.75B − ₩900M) × 60 % = 과세표준 ₩510M; 1.3 % bracket): **~₩6.6M/yr** before various credits
- **Total Y1 transaction**: ~₩200M; **Annual recurring**: ~₩11M+ (~€7,100)

⚠️ Examples illustrative; final numbers depend on 공시가격 (annual MOLIT release), exact 조정대상지역 status, household composition, and active deductions. Numbers cross-checked against NTS calculation flowchart but TAX FILING REQUIRES CPA (세무사) for non-residents.

### Inheritance Tax — 상속세 + Gift Tax — 증여세

Progressive **10 %–50 %** on aggregate inheritance value above ₩1B–₩5B+ thresholds depending on heir relationship; among the world's higher inheritance regimes ([NTS source](https://www.nts.go.kr/english/cm/cntnts/cntntsView.do?mi=11195&cntntsId=8315main.do)):

| Bracket | Rate |
|---|---|
| ≤ ₩100M | 10 % |
| ₩100M–₩500M | 20 % |
| ₩500M–₩1B | 30 % |
| ₩1B–₩3B | 40 % |
| > ₩3B | 50 % |

- **일괄공제** (lump-sum exemption): ₩500M; 배우자공제 spouse exemption up to ₩3B
- **Non-resident heir of Korea-situs real estate**: taxable on KR property value regardless of residency; no spouse exemption if non-resident
- 2025 government proposed cutting top rate to 40 % + restructuring brackets — **National Assembly reportedly passed 2025-12-02** ⚠️ effective date + final bracket math NOT YET PRIMARY-VERIFIED; bracket table above still reflects pre-amendment 10–50 % regime — verify at [NTS 상속세 안내](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2273&cntntsId=7708) before relying on for inheritance planning (2026-05-27 stale-marker)
- **2025–2026 reform proposal**: 유산취득세 (acquisition-by-heir) regime under discussion to replace 유산세 (estate-level) regime — would lower effective rate

### Future risk

- 종부세 + 재산세 dual-layer continues to attract reform pressure; expect revisions every administration cycle
- 공시가격 현실화 로드맵 (gradual alignment of 공시 to market) was paused 2022–2025; Yoon administration extended moratorium; long-term direction is upward → recurring tax bills will rise
- 다주택자 양도세 중과세 (multi-home capital gains surcharge) suspension is rolling — verify status at any transaction
- **2026 종부세 reform** under National Assembly review may further cut multi-home punitive bands

---

## Section: `--rental`

### Long-term residential — 전세 (jeonse) vs 월세 (wolse)

Korea's rental market is bifurcated:

| System | Mechanism | Tenant cash flow |
|---|---|---|
| **전세 (jeonse)** | Lump-sum deposit, typically **50–80 % of property value**, refundable in full at end of 2-yr term; landlord earns by reinvesting deposit | Zero monthly rent; capital lockup |
| **월세 (wolse)** | Smaller deposit (~₩10M–₩100M) + monthly rent | Closer to global rental norm |
| **반전세 / 보증부월세** | Hybrid: medium deposit + reduced monthly | Common post-2022 jeonse decline |

### Jeonse legal framework + risks

- **주택임대차보호법 (Housing Lease Protection Act)** — tenant protection statute; 2-yr default term + **계약갱신청구권 (1× renewal right)** for additional 2 yrs (effective 2020-07-31, "임대차 2법")
- **전월세상한제** — rent/jeonse increase capped at **5 %** at renewal (within renewal-right window)
- **확정일자 + 전입신고** — date-confirmation stamp at 주민센터 + resident registration creates **우선변제권** (priority claim) at landlord default; CRITICAL step
- **전세권 등기 (jeonse-right registration)** at 등기소 — stronger than 확정일자, makes jeonse a registered encumbrance on title; ~0.2 % registration tax cost; **highly recommended for foreign tenants**

### Jeonse fraud crisis (2022–2024) — 전세사기

- Mass landlord defaults during 2022 rate-hike cycle; over 25,000+ identified victims as of 2024 ([MOLIT victim count](https://www.molit.go.kr/USR/policyData/m_34681/dtl.jsp?id=4694))
- Pattern: speculative landlord buys property with jeonse deposit ≈ purchase price; market dips → landlord can't refund + can't sell at original price
- **Special Act for Jeonse Fraud Victims** (2023-06-01) provides relief: government acquires victim claims; extended 2024 + 2025 with broader eligibility
- **Verification flow before signing jeonse**:
  1. **등기부등본** at IROS — check 근저당권 (mortgage) sum + 전세권 + 임차권 records on Section 을구
  2. Compute **깡통전세 risk**: jeonse deposit + outstanding mortgages > 70 % of market price = HIGH RISK
  3. **HUG 전세보증보험 (Housing & Urban Guarantee Corp jeonse-return insurance)** application — 2024 reform: insurable only if (mortgage + jeonse) ≤ **126 % of 공시가격** ([HUG source](https://www.khug.or.kr/))
  4. **국세 완납증명 + 지방세 완납증명** — landlord tax clearance certs (delinquent taxes can supersede tenant claim)

### Yields (Q1 2026, gross, residential apt typical)

> **est. ranges** — bands below are estimates from 월세 보증금→rent conversion at 전월세전환율 (no single REB/KB headline figure covers all these segments); verify per complex via RTMS 실거래가 + 임대 listings.

- **서울 강남3구 (Gangnam/Seocho/Songpa)**: gross yield ~2.0–3.0 % (월세 base; jeonse-only converts to ~0 yield by definition — capital gain play)
- **서울 외곽구 (outer Seoul wards)**: ~2.5–4.0 %
- **광역시 도심 (metro city centers)**: ~4.0–5.5 %
- **지방 중소도시 (regional)**: ~5.0–8.0 %
- **오피스텔 (officetel — mixed-use)**: typically ~4.5–7.0 % but higher vacancy + faster depreciation
- **상가 (commercial)**: ~5–9 % gross; legal vacancy + tenant-default risk material

⚠️ Yield calc is non-trivial in KR: need to convert jeonse-only or 반전세 to "rent equivalent" — convention is **전월세전환율 (jeonse-to-rent conversion rate)** capped at **BoK rate + 2 %p OR 5 %, whichever is lower** under 임대차보호법; market actual is often 3–5 %.

### Short-term rentals (Airbnb-style) — heavily restricted

**Three legal pathways**:

| Regime | Statute | Permitted area | Notes |
|---|---|---|---|
| **외국인관광 도시민박업** (Foreign-Tourist Urban B&B, "도시민박") | 관광진흥법 § 4 + 시행령 | Owner-occupied dwelling, **Korean nationals as guests prohibited — foreigners only** | Must be owner's primary residence; ≤ 230 m²; permit at 시·군·구 청 관광과 |
| **농어촌민박업** (Rural B&B) | 농어촌정비법 | 읍·면 areas only; ≤ 230 m²; owner-resident requirement | Some regions (제주) more permissive |
| **한옥체험업** (Hanok Experience) | 한옥건축물 specific | Designated hanok | Niche |
| **공유숙박업** (sharing-economy lodging) | 규제샌드박스 limited pilots | Seoul + select zones, capped nights | Pilot status; not yet permanent law |
| **호텔업/관광호텔/생활숙박시설** | 관광진흥법 호텔 | Permitted use only | Full hotel licensure |

⚠️ **NON-OWNER-OCCUPIED PURE-INVESTMENT AIRBNB IS ILLEGAL** in most of Korea. Many Seoul apt complexes operating Airbnb are doing so without 관광진흥법 도시민박 license — violations carry fines up to ₩2M + criminal liability.

- **생활숙박시설 (saenghwal sukbak siseol — "residential lodging")** loophole — specific zone, sold as pseudo-residential but legally lodging; widely missold 2018–2022; Government 2021 directive banned residential use (~₩100M fine if used as residence). 입주민 mass lawsuits ongoing 2024–2026.

### Tax + reporting (rental)

- **종합소득세 (comprehensive income tax)**: rental income reported on annual 5월 신고 + 6월 납부; small-scale exemption (월세 ≤ ₩20M/yr from up to 2 properties + single-home owner) ENDED 2019; current threshold-based simplified taxation only for sub-₩20M revenue
- **부가가치세 (VAT 10 %)**: residential lease VAT-EXEMPT; commercial lease VAT-able
- **사업자등록 (business registration)**: required if rental is "business activity"; default for multi-property landlords
- **임대사업자 등록제 (Registered Lease Business Operator)** — voluntary scheme with tax incentives + 8 yr / 10 yr 의무임대 (mandatory lease) — significantly tightened 2020 (4 yr type abolished); most existing registrations grandfathered

### Strategic notes

- Pure-investment Airbnb ARRangement requires either: (a) commercial-zoned 생활숙박 building in tourist hot zone, OR (b) 외국인관광 도시민박 with foreigner-only marketing + 거주 status, OR (c) full 관광호텔 license — none easy
- Jeonse arbitrage as investment strategy ("갭투자" gap-investment) became regulatorily disfavored post-2022 — surrounding tax + DSR penalties high
- Cleanest foreign-investor route: 강남3구 apt for capital appreciation + 월세 (monthly rent), **NOT** jeonse (need to redeposit at end)

---

## Section: `--work=<profession>`

### Job platforms

- **사람인 (Saramin)** — `https://www.saramin.co.kr/` — broadest mid-career
- **잡코리아 (JobKorea)** — `https://www.jobkorea.co.kr/` — peer leader
- **원티드 (Wanted)** — `https://www.wanted.co.kr/` — IT/스타트업 forward
- **링크드인 한국 (LinkedIn Korea)** — strong for foreign companies, English-language roles, executive
- **HelloWork Korea (워크넷)** — public service `https://www.work.go.kr/` (Korea Employment Information Service)
- **GET-Korea / Going Korea / Seoul Global Center** — English-language foreigner-friendly: `https://global.seoul.go.kr/`

### Self-employment regimes

- **개인사업자 (gaein sa-eopja — sole proprietor)**: register 사업자등록 at 세무서 within 20 days of starting; simple bookkeeping for revenue ≤ ₩48M (간편장부) → ₩48M+ (복식부기)
- **간이과세자 (kani-gwasaeja — simplified VAT taxpayer)**: revenue ≤ ₩80M (raised 2024 from ₩48M); reduced VAT rate ~1.5–4 % effective
- **일반과세자**: standard VAT 10 %
- **법인 (corporation)**: 주식회사 minimum capital ₩100 (effectively no minimum since 2009); 23 %–25 % corporate tax + local surcharge
- **국민건강보험 + 국민연금**: mandatory; rates ~7–9 % each on income up to caps

### Foreign-worker visa interface (cross-section to `--visa`)

- **E-7 (Special-Skilled)**: most common white-collar foreign worker; sponsor-based
- **D-8 (Corporate Investment)**: foreign-direct-investor visa; ≥ ₩100M KRW investment in registered KR corp
- **D-10 (Job Seeker)**: 6-month → 12-month renewable; conversion to E-7 standard route
- **F-2-7 (Long-term Resident, points-based)**: 80+ point system; 3-yr+ renewable; broad work rights
- **F-5 (Permanent Resident)**: after 5 yrs F visa; broad work rights; near-citizen
- **F-6 (Marriage)**: spouse of Korean citizen; broad work rights
- **F-4 (Overseas Korean / 재외동포)**: ethnic-Korean diaspora; broad work rights
- **D-2/D-4 (Student/Language)**: limited part-time work
- Property purchase does NOT trigger any visa upgrade in Korea (unlike Greek or Portuguese golden visas — see `--visa`)

### Salary benchmarks (2025 median monthly gross — 고용노동부 임금구조기본통계조사)

- **서울 (full-time regular employee, all-industry)**: ~₩4.0M–₩5.5M (median; high variance by industry — IT/finance ₩6M–₩9M+ for mid-career)
- **광역시 (Busan/Daegu/Incheon/Gwangju/Daejeon/Ulsan)**: ~₩3.5M–₩4.5M
- **지방 중소도시**: ~₩2.8M–₩3.8M
- **최저임금 2026 (national minimum wage)**: **₩10,320/hr** (+2.9 % from 2025 ₩10,030), effective 2026-01-01; monthly equivalent **₩2,156,880** at 209-hr standard month (2026-05-27 verified, source [Minimum Wage Council official notice](https://www.minimumwage.go.kr/english/introduce/minWage.do) + [Korea.net 274970](https://www.korea.net/NewsFocus/policies/view?articleId=274970)) — prior playbook ₩10,030 was the 2025 figure

### Catchment heuristics

- Within 60 min subway/KTX of 서울역 / 강남역: full white-collar catchment
- Within 60 min of 광역시 central station: regional employment access
- Beyond 60 min of nearest 광역시: thin labor market; remote-friendly + Korean-language critical
- Demographic decline regions (전남, 경북 외곽, 강원 산간): very thin

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **일사편리 — 부동산 통합 민원** (cadastral: 부동산종합증명서, 지적측량 민원) | `https://kras.go.kr/` | Parcel cadastral record + integrated property certificate (2026-09-18 verified) |
| **토지이음 (LURIS 후신)** | `https://www.eum.go.kr/` | Parcel-level zoning + use restrictions + 보호구역 designations |
| **재해정보지도 (Disaster Information Map)** — 행정안전부 | `https://www.safemap.go.kr/` | Multi-hazard overlay: 풍수해 (storm/flood), 지진, 산사태, 지반침하 |
| **기상청 (KMA — Korea Meteorological Administration)** | `https://www.weather.go.kr/` | Active hazard + climate data |
| **국립재난안전연구원 (NDMI)** | `https://www.ndmi.go.kr/` | Disaster research data |
| **한국지질자원연구원 (KIGAM)** + **기상청 지진화산정보** | `https://necis.kma.go.kr/` | Seismic catalogue + active fault data |
| **기후에너지환경부 홍수통제소** (한강 / 낙동강 / 금강 / 영산강) | `https://www.hrfco.go.kr/` | Flood forecast + water level — the flood-control offices are affiliated agencies of 기후에너지환경부 (formerly 환경부), not of 국토교통부 (2026-09-18 verified) |
| **국립환경과학원 — 라돈지도** | `https://iaqinfo.nier.go.kr/` | Indoor radon survey data |
| **산림청 산사태정보시스템** | `https://sansatai.forest.go.kr/` | Landslide hazard + warning |

### Seismic risk

Korea is **low-to-moderate seismic** — long considered stable but Pohang 2017 M5.4 + Gyeongju 2016 M5.8 events recalibrated risk perception:

- 🟢 < 0.05 g PGA-50yr (most of country, 수도권 inner)
- 🟡 0.05–0.10 g (남동권 fringe)
- 🟠 0.10–0.16 g (경상도 동남부, 양산단층대 — Yangsan Fault Zone, includes 부산·울산·경주·포항)
- 🔴 > 0.16 g (small zones near 양산단층 직접 노출 + 동해안 일부)

⚠️ Source: 국가지진위험지도 (KIGAM/KMA, last revision 2013; 2024 update under review) — `https://www.kigam.re.kr/`

### Build-era hazards (the watershed)

| Era | Code basis | Hazard rating |
|---|---|---|
| **Pre-1988 (구 내진설계 기준 적용 전)** | 1988 — 내진설계 기준 처음 도입 | 🔴 **Pre-seismic-code era** — buildings ≥ 6 storey only required 내진 from 1988; refit costly |
| **1988–2005 (초기 내진 기준)** | 1988 + 1995 amendments | 🟡 Limited seismic capacity (designed roughly to MMI 6) |
| **2005–2017** | 2005 expansion to 3 storey + 2009 KDS update | 🟡 More general but still pre-Pohang |
| **2017+ (Pohang post)** | 2017-12 모든 주택 (every dwelling) seismic-required | 🟢 Modern post-Pohang |
| **2017–present (KDS 41 17 00)** | Korean Design Standard | 🟢 Modern; integrates 2016 Gyeongju + 2017 Pohang lessons |

⚠️ The **1988 + 2017 watersheds are the single most material build-year datums** for KR. Confirm 사용승인일 (use-approval date) on **건축물대장**, NOT just 준공 (completion).

### Mandatory disclosures (at sale)

| Document | Required because | Source |
|---|---|---|
| **중개대상물 확인·설명서** | 공인중개사법 § 25 — agent must explain BEFORE contract | covers location, zoning, mortgage, defects, jeonse encumbrances |
| **등기부등본** | proves ownership + encumbrances | IROS (online), notarised for transactions |
| **건축물대장** | building specs + violations | gov.kr |
| **토지대장 + 토지이용계획확인원** | land use restrictions | gov.kr / 토지이음 |
| **재산세 납부증명** | seller property tax cleared | 정부24 |
| **국세 + 지방세 완납증명** | seller national + local tax cleared | 홈택스 + 위택스 |
| **하자담보책임 (defect warranty)** | 민법 § 580 + 건설산업기본법 + 공동주택관리법 | 2 yr (interior) / 5 yr (구조부 finishes) / 10 yr (구조내력) for new builds |

### Earthquake insurance (지진보험)

- **풍수해보험** (Wind/Flood Insurance) — government-subsidized via 행정안전부 + 5 private insurers; covers earthquake + flood + storm; subsidized 50–86 % depending on income tier
- **지진보험** standalone or 화재보험 add-on — limited adoption
- **건물 화재보험 (building fire)** is widely held; check 지진 담보 (earthquake rider) explicitly

### Climate change projections (KMA + IPCC AR6)

- KMA 한반도 기후변화 전망보고서 projects under SSP2-4.5: Korean Peninsula annual mean temperature **+2.3–3.6 °C** by 2071–2100 vs 1995–2014; under SSP5-8.5 +5.3–7.0 °C
- Heat-wave days (TX≥33°C 폭염일수): doubles by 2050
- 열대야 (tropical nights TN≥25°C): Seoul summer becomes near-continuous; southern coast 2x increase
- Typhoon intensity: rise; track shift northward — 한반도 직접 상륙 빈도 + 강도 증가
- Sea-level rise: +0.4–0.6 m by 2100 SSP2-4.5; +0.7–1.1 m SSP5-8.5 — 인천·서해안·낙동강 하구·제주 저지대 노출
- Precipitation: 집중호우 events (1-hour 50 mm+) +30–50 % frequency by 2050; **Seoul Aug 2022 floods** killed 14 + ₩300B damage — one-in-100-yr event likelihood rising
- Source: KMA 기후변화감시 + 기후정보포털 — `https://www.climate.go.kr/`

### Other hazards

- **싱크홀 (sinkholes)**: urban Seoul + 해운대 — aging sewer + groundwater drawdown; 행안부 산하 지반침하 모니터링 강화 2023+
- **산사태 (landslides)**: 산림청 위험지도 — 강원·경북 산간 + 도시 인근 절개지
- **미세먼지 (PM2.5)**: trans-boundary + domestic; AQI > 150 occasional Seoul winter days; check 에어코리아 `https://www.airkorea.or.kr/`
- **라돈 (radon)**: significant in 경기 남부 + 전북 + 충남 일부 화강암 지대; 환경부 라돈지도

---

## Section: `--mains`

### National database

- **상하수도정보시스템 (Water+Sewer Info System)** — 환경부: `https://www.waternow.go.kr/`
- **K-water (한국수자원공사)** — bulk water + some retail: `https://www.kwater.or.kr`
- **시·군·구 상하수도사업소** — retail operator per municipality

### Operators

- 상수도 (water supply): per **시·도 또는 시·군·구 상수도사업본부** — Seoul Waterworks Authority (아리수), 부산상수도사업본부, K-water (rural/regional)
- 하수도 (sewer): per 시·군·구 하수도사업소; 환경부 하수도법
- Coverage:
  - **상수도 보급률 (water supply)**: ~99 % nationally (2023, 환경부 상수도통계)
  - **하수도 보급률 (sewer)**: ~95 % nationally (2023, 환경부 하수도통계) — 도시: 99 %; 농어촌: 75–85 %
- Where mains sewer absent, individual treatment via **개인하수처리시설** (individual sewage treatment) — regulated under 하수도법 § 34

### Verification

1. Listing language:
   - **공공하수 / 본하수** = mains sewer
   - **개인하수처리시설** / **정화조 (jeonghwajo)** = individual treatment (older 단독주택 rural)
   - **상수도** = mains water
   - **간이상수도 / 마을상수도** = small village system (rural)
   - **지하수 (underground water — well)** = private well
2. Confirm via 시·군·구청 상하수도과
3. **중개대상물 확인·설명서 § 상하수도** must specify

### Costs (typical 2026)

> est. ranges — vary by 시·군·구; confirm with 상하수도과 + a contractor quote before budgeting.

| Scenario | Cost (₩) |
|---|---:|
| Connection where mains available | ₩1.5M–₩4M |
| Mains sewer extension to property (if road has trunk) | ₩5M–₩20M |
| 정화조 install (5인용 ~ 10인용, new) | ₩3M–₩8M |
| 정화조 → mains conversion | ₩6M–₩15M |
| 지하수 (well) → 상수 conversion | ₩2M–₩6M |
| Monthly water bill (typical apt 4-person) | ₩15K–₩35K |
| Monthly sewer bill | ₩8K–₩20K |

---

## Cost benchmarks (KR 2026)

> Tax/duty rows (취득세, 인지세, 수수료 cap, etc.) are statutory and shown with their rate formula inline. Non-statutory rows (법무사, 관리비, 장기수선충당금, demolition, renovation, totals) are **est. market ranges** — confirm per quote; not fixed by statute.

| Item | Cost (₩) |
|---|---:|
| 법무사 (judicial scrivener / 등기 transfer) | ₩400K–₩1.5M typical residential |
| 공인중개사 수수료 (max statutory, residential) | **0.4–0.9 %** by price band (≤₩50M: 0.6 %; ₩50M–₩500M: ₩250K + 0.5 %; ≥₩6B luxury: 0.7 % cap) — **negotiable** within statutory cap |
| 인지세 (stamp duty) | ₩150K–₩350K flat |
| 취득세 (1세대 1주택, ≤₩600M) | 1.0 % × 매매가 |
| 취득세 (1주택 ₩600M–₩900M sliding) | 1.0–3.0 % linear |
| 취득세 (1주택 > ₩900M) | 3.0 % |
| 취득세 (multi-home 조정) | 8 %–12 % punitive |
| 농특세 + 교육세 surcharges | +0.6 % typical |
| 국민주택채권 매입할인 effective cost | 0.2–1.0 % of price |
| 화재보험 (apt typical) | ₩100K–₩400K/yr |
| 풍수해보험 (gov-subsidized) | ₩30K–₩150K/yr after subsidy |
| 관리비 (apt monthly admin fee, 84 m² typical) | ₩200K–₩500K/mo |
| 장기수선충당금 (long-term repair fund, monthly) | ₩30K–₩100K/mo (rises with age) |
| Demolition (단독주택, ~100 m²) | ₩15M–₩40M |
| Renovation (interior gutting + remodel, 84 m²) | ₩50M–₩150M |
| **Total transaction cost (buyer side, residential 1세대 1주택)** | **~4–8 % of price** (multi-home 8–15 %+) |

## Active fiscal incentives (2025–26)

- **신혼부부·청년 디딤돌대출** — 주택도시기금 (Housing Urban Fund) low-rate first-home loan; ~2.0–3.5 % up to ₩550M loan, ≤₩600M home; eligibility income-capped ([HUG source](https://www.khug.or.kr/))
- **보금자리론 / 안심전환대출** — KHFC long-term fixed-rate (10/20/30/40-yr) at slight discount
- **신생아 특례대출** (2024+) — newborn-household ultra-low-rate up to ₩500M loan @ 1.6–3.3 % depending on income
- **양도세 비과세** (1세대 1주택, 2-yr 거주 + ₩1.2B 이하): full exemption on sale
- **재건축·재개발 입주권** — older-complex redevelopment option value; major Gangnam/Mokdong driver, but heavy regulatory + 분담금 risk
- **임대사업자 등록 세제혜택** — significantly trimmed 2020; some legacy registrations retain benefits (장기 임대 종부세 합산배제 + 양도세 중과 배제)

## Common listing platforms

- **네이버 부동산** (`https://land.naver.com/`) — biggest aggregator
- **다방** (`https://www.dabangapp.com/`)
- **직방** (`https://www.zigbang.com/`)
- **호갱노노** (`https://hogangnono.com/`) — analytics + RTMS overlay
- **부동산114** (`https://www.r114.com/`)
- **KB부동산** (`https://kbland.kr/`) — bank index + listings
- **한국공인중개사협회** (`https://www.kar.or.kr/`) — agent directory

## Caveats unique to KR

- **The 1988 (initial) and 2017 (Pohang post) seismic-code watersheds are the single most material build-year datums** — confirm 사용승인일 on 건축물대장
- **공시가격 vs 시세 vs RTMS 실거래가**: three different value concepts — 공시 (~70 % of market) is tax base; 시세 is asking; RTMS is recorded transaction. **Use RTMS for buy/sell decisions.**
- **전세 ≠ rent**: jeonse is an interest-free loan to landlord secured against the property; before signing, verify (mortgage + jeonse) ≤ **126 % of 공시가격** OR you can't get HUG insurance — and uninsured jeonse in 2026 = significant counterparty risk
- **다주택자 punitive regime (8 %/12 % 취득세 + 양도세 중과)**: structurally hostile to investor-multi-home portfolios; verify current 조정대상지역 list at NTS pre-purchase
- **분양가상한제 (price-cap zones)** — distort new-build pricing in 강남/서초/송파/용산 + select wards; resale at unlocked market triggers windfall tax
- **재건축 초과이익환수제 (Reconstruction Surplus Recovery Levy)** — up to 50 % tax on redevelopment windfall; shapes older-complex valuations
- **공동주택 관리비 + 장기수선충당금 trajectory**: older complexes' 장기수선충당금 rises sharply when 장기수선계획 (long-term repair plan) cycle hits; request 관리규약 + 장기수선계획서 + 회계감사보고서 for any ≥ 10-yr complex
- **외국인 부동산 취득 신고 60일 기한 (foreign-buyer 60-day notification)**: failure → 과태료 ₩3M (지방자치단체 부과); separate from contract registration
- **상속세 + 증여세 50 % top rate** is among the world's highest; estate planning critical for foreign owners with Korean assets
- **생활숙박시설 trap**: marketed as residential but legally lodging — residential use illegal since 2021 with retroactive enforcement; ongoing 입주민 lawsuits
- **DSR 40 % cap + LTV regime**: foreign non-resident buyers face stricter LTV (typically 40–50 % vs 70 % owner-occupier resident); KEB Hana, Woori, Shinhan, KB offer non-resident mortgages with constraints
- **KRW free-floating but BoK macroprudential intervention**: capital controls minimal post-1998 IMF reforms; ≥ USD10K outbound declaration; foreign-buyer purchase fund repatriation must trace via 외국환신고

## Reddit / forum sources

- **r/korea** — broad Korea-life topics
- **r/seoul** — Seoul-specific
- **r/movingtokorea** — pre-relocation
- **r/livingkorea** — daily life, housing posts
- **Wagle.net + Naver 카페** — Korean-language; 강남부동산 / 부동산스터디 카페 deep insights
- **Korea Real Estate Daily** — `https://www.kred.co.kr/`
- **Asia Property Awards / IPA Korea** — periodic market reports

## Verification authorities

| Authority | When to call |
|---|---|
| **법원 등기소 (Court Registry)** via **인터넷등기소 (IROS)** | 등기부등본 verification, 근저당권 + 전세권 + 가압류 records |
| **시·군·구청 — 세무과** | 재산세 평가액, 납세증명 |
| **시·군·구청 — 도시계획과** | 용도지역, 건폐율/용적률, 도시계획시설 |
| **시·군·구청 — 지적과** | 토지대장, 지적도 |
| **시·군·구청 — 건축과** | 건축물대장, 사용승인 history (pre/post 1988/2017) |
| **시·군·구청 — 상하수도과** | Mains coverage, connection cost |
| **시·군·구청 — 관광과** | 외국인관광 도시민박업 + 농어촌민박업 license |
| **국세청 (NTS) + 세무서** | 양도세, 종부세, 상속세, 증여세 |
| **법무사 (judicial scrivener)** | Final transfer + 등기 filing |
| **공인중개사 (Licensed Real Estate Agent)** | 중개대상물 확인·설명 (license verification at 한국공인중개사협회 KAR) |
| **HUG (주택도시보증공사)** | 전세보증보험 + 분양보증 verification |
| **법무부 출입국·외국인청** | foreigner registration status interface |
| **KOTRA / 외국인투자종합지원센터** | foreign-buyer guidance |

## Quirks to know

- **소유권 (freehold)** dominant; 전세권 / 임차권 / 근저당권 are encumbrances on title; check 등기부 sections 갑구 (ownership) + 을구 (encumbrances) carefully
- **평 (1 평 = 3.3058 m²)** still ubiquitous in marketing; legal docs and registry use m²
- **전용면적 vs 공급면적 vs 계약면적** — three different floor-area concepts; ₩/평 quoted on listing usually uses 공급 (larger) — under-states actual ₩/m²
- **등기부 표제부 (front section)** lists 대지권 (proportional land share for apt unit) — material for redevelopment value
- **Three different value concepts** for the same property:
  - **시세 (sise)** — current market asking
  - **실거래가 (RTMS)** — recorded transaction price
  - **공시가격** — official government value (~60–80 % of market for apt)
  - **감정평가액** (appraisal value) — bank/legal use
- **재건축 vs 재개발**: 재건축 (apt-led, individual-property ownership); 재개발 (district-led, often single-family); both have major upside potential AND 분담금 (additional contribution) risk
- **분양권 (bunyangkwon — pre-sale right)** vs **입주권 (ipjukwon — move-in right post-redevelopment)** — both are pre-completion contractual rights, traded actively; tax + transfer rules differ
- **전세권 등기 vs 확정일자**: registered jeonse-right is stronger but 0.2 % registration tax cost; 확정일자 (date stamp) at 주민센터 + 전입신고 is cheaper but slightly weaker
- **임대사업자 의무임대 8년/10년**: voluntary registered-landlord scheme — significant tax benefits for compliance period; tightening since 2020
- **갭투자 (gap-investment)**: speculative purchase financed by jeonse deposit gap; structurally disfavored 2020+ via tax + DSR + LTV regime
- **국민주택채권 매입의무** (national housing bonds compulsory purchase at acquisition): immediately resold at market discount → effective cost included in transaction
- **일조권 + 조망권 (sunlight + view rights)**: civil-law concepts adjudicated case-by-case; high-rise next-door construction has triggered material lawsuits
- **공동주택관리법 § 28 회계감사 (mandatory audit)**: ≥ 300-unit complex must file annual audit; recently expanded transparency

## Source URL templates

| Source | URL |
|---|---|
| MOLIT 실거래가 (RTMS) | `https://rt.molit.go.kr/` |
| 공시가격 알리미 | `https://www.realtyprice.kr/` |
| 한국부동산원 R-ONE | `https://www.reb.or.kr/r-one/` |
| 인터넷등기소 (IROS) | `https://www.iros.go.kr/` |
| 정부24 (gov24) | `https://www.gov.kr/` |
| 토지이음 (ex-LURIS) | `https://www.eum.go.kr/` |
| 부동산종합공부시스템 (일사편리) | `https://kras.go.kr/` |
| 국세청 (NTS) | `https://www.nts.go.kr/` |
| 홈택스 (Hometax) | `https://hometax.go.kr/` |
| 위택스 (Wetax — local taxes) | `https://www.wetax.go.kr/` |
| HUG 주택도시보증공사 | `https://www.khug.or.kr/` |
| 한국주택금융공사 (KHFC) | `https://www.hf.go.kr/` |
| 한국은행 (BoK) | `https://www.bok.or.kr/` |
| 기상청 (KMA) | `https://www.weather.go.kr/` |
| 기후정보포털 | `https://www.climate.go.kr/` |
| 안전디딤돌 / 재해정보지도 | `https://www.safemap.go.kr/` |
| 환경부 상하수도정보 | `https://www.waternow.go.kr/` |
| 에어코리아 (PM2.5) | `https://www.airkorea.or.kr/` |
| ITS National Transport | `https://www.its.go.kr/` |
| TAAS 교통사고분석 | `https://taas.koroad.or.kr/` |
| 한국도로공사 | `https://www.ex.co.kr/` |
| 네이버 부동산 | `https://land.naver.com/` |
| 다방 | `https://www.dabangapp.com/` |
| 직방 | `https://www.zigbang.com/` |
| 호갱노노 | `https://hogangnono.com/` |
| KB부동산 | `https://kbland.kr/` |
| 사람인 (jobs) | `https://www.saramin.co.kr/` |
| 잡코리아 | `https://www.jobkorea.co.kr/` |
| 워크넷 (public job) | `https://www.work.go.kr/` |
| 출입국·외국인청 (HiKorea) | `https://www.hikorea.go.kr/` |

## Status

**Confidence**: HIGH

**Last verified**: 2026-05-27 (cadastral/zoning portal identity and flood-control ministry corrected 2026-09-18 per kras.go.kr + eum.go.kr + mcee.go.kr)

**Researched by**: Sonnet 4.6 + Opus 4.7 (parallel-subagent batch, 2026-05)

**Notes**: Pricing/transaction-tax/cadastre/seismic-standard/RTMS sources all anchored to MOLIT / NTS / 법원 등기소 / KMA / BoK / HUG primary URLs with date-stamped numerics + transparent computations. HIGH for cadastre + national tax + RTMS transparency (single best transaction-price disclosure regime among the 62 covered countries) + seismic code watersheds (1988/2017) + jeonse legal framework. MEDIUM for current 다주택자 surcharge status (verify 조정대상지역 list at NTS pre-transaction; suspension extensions are rolling), exact ratios on 공정시장가액비율 (changes by Yoon administration ongoing), and short-let permitted scope (생활숙박 enforcement evolving 2024–2026). LOW only for unverifiable parcel-level claims (apt-complex-specific RTMS comps require live IROS lookup; 공시가격 changes annually each Q1).
