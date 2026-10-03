# US State Comprehensive Privacy Laws — Audit Reference

**Effective dates as of 2026-04-25.** Always confirm against the current statute and most recent AG rulemaking before issuing a Critical finding; this reference is for audit triage, not legal advice.

## Quick-reference matrix

| State | Statute | In effect | Applicability threshold (any one) | Right to opt-out of sale/share | Right to opt-out of targeted advertising | Sensitive data opt-in/opt-out | Universal opt-out (UOOM/GPC) honor required | Private right of action |
|---|---|---|---|---|---|---|---|---|
| CA | CCPA/CPRA (Cal. Civ. Code §1798.100 et seq.) | Yes (CCPA 2020; CPRA 2023) | Rev > $25M; or 100k+ CA consumers/households; or 50%+ revenue from sale/share | Yes | Yes | Opt-out (Limit Use of Sensitive PI) | Yes (CCPA Reg §7025) | Yes — data breach only (§1798.150) |
| VA | VCDPA (Va. Code §59.1-575 et seq.) | Yes (Jan 2023) | 100k+ consumers; or 25k+ consumers AND 50%+ revenue from sale | Yes | Yes | Opt-in for sensitive | Not required (statute silent — no enforcement of GPC) | No |
| CO | CPA (C.R.S. §6-1-1301 et seq.) | Yes (Jul 2023) | 100k+ consumers; or 25k+ AND any revenue from sale | Yes | Yes | Opt-in for sensitive | Yes (4 CCR 904-3, Rule 5.04) | No |
| CT | CTDPA (Conn. Gen. Stat. §42-515 et seq.) | Yes (Jul 2023) | 100k+ consumers; or 25k+ AND 25%+ revenue from sale | Yes | Yes | Opt-in for sensitive | Yes (effective Jan 2025) | No |
| UT | UCPA (Utah Code §13-61-101 et seq.) | Yes (Dec 2023) | Rev > $25M AND (100k+ consumers OR 25k+ AND 50%+ revenue from sale) | Yes | Yes | Opt-out for sensitive (notice required) | Not required | No |
| IA | ICDPA (Iowa Code §715D) | Yes (Jan 2025) | 100k+ consumers; or 25k+ AND 50%+ revenue from sale | Yes | Yes | Opt-out (notice) | Not required | No |
| IN | INCDPA (Ind. Code §24-15) | Yes (Jan 2026) | 100k+ consumers; or 25k+ AND 50%+ revenue from sale | Yes | Yes | Opt-in for sensitive | Not required | No |
| TN | TIPA (Tenn. Code §47-18-3201 et seq.) | Yes (Jul 2025) | Rev > $25M AND (175k+ consumers OR 25k+ AND 50%+ revenue from sale) | Yes | Yes | Opt-in for sensitive | Not required (statute silent) | No |
| TX | TDPSA (Tex. Bus. & Com. Code §541) | Yes (Jul 2024) | Conducts business in TX; processes consumer data; not a small business per SBA | Yes | Yes | Opt-in for sensitive | Yes (effective Jan 2025) | No |
| MT | MCDPA (Mont. Code §30-14-2801 et seq.) | Yes (Oct 2024) | 50k+ consumers; or 25k+ AND 25%+ revenue from sale | Yes | Yes | Opt-in for sensitive | Yes | No |
| OR | OCPA (ORS §646A.570 et seq.) | Yes (Jul 2024) | 100k+ consumers; or 25k+ AND 25%+ revenue from sale | Yes | Yes | Opt-in for sensitive | Yes (effective Jan 2026) | No |
| DE | DPDPA (6 Del. C. §12D-101 et seq.) | Yes (Jan 2025) | 35k+ consumers; or 10k+ AND 20%+ revenue from sale | Yes | Yes | Opt-in for sensitive | Yes (effective Jan 2026) | No |
| NH | NHPA (RSA 507-H) | Yes (Jan 2025) | 35k+ consumers; or 10k+ AND 25%+ revenue from sale | Yes | Yes | Opt-in for sensitive | Yes (effective Jan 2025) | No |
| NJ | NJDPA (N.J.S.A. 56:8-166.4 et seq.) | Yes (Jan 2025) | 100k+ consumers; or 25k+ AND any revenue from sale | Yes | Yes | Opt-in for sensitive | Yes (effective ~Jul 2025 per AG rule) | No |
| KY | KCDPA (KRS 367.3611 et seq.) | Yes (Jan 2026) | 100k+ consumers; or 25k+ AND 50%+ revenue from sale | Yes | Yes | Opt-in for sensitive | Not required | No |
| MD | MODPA (Md. Code Com. Law §14-4601 et seq.) | Yes (Oct 2025) | 35k+ consumers; or 10k+ AND 20%+ revenue from sale | Yes | Yes | Opt-in (sensitive minimization required) | Yes | No |
| MN | MCDPA (Minn. Stat. §325O) | Yes (Jul 2025) | 100k+ consumers; or 25k+ AND 25%+ revenue from sale | Yes | Yes | Opt-in for sensitive | Yes | No |
| RI | RIDTPPA (R.I. Gen. Laws §6-48.1) | Yes (Jan 2026) | 35k+ consumers; or 10k+ AND 20%+ revenue from sale | Yes | Yes | Opt-in for sensitive | Yes | No |
| FL | FDBR (Fla. Stat. §501.701 et seq.) | Yes (Jul 2024) | Rev > $1B AND (50%+ rev from ads, OR operates app store with 250k+ apps, OR operates smart speaker with virtual assistant) | Yes | Yes | Opt-in for sensitive | Yes | No |

**Audit shortcut:** If the user's privacy policy lacks any of (a) a "Do Not Sell or Share My Personal Information" link, (b) a documented response to a Global Privacy Control browser signal, (c) an enumerated sensitive-data category list, or (d) a specific opt-out response window (45 days CCPA/VA/CO/CT/UT; 60 days others typically) — file Critical findings against every state above where the company meets the threshold.

## Cross-cutting clauses every multi-state policy needs

### 1. Categories of personal data collected
- **CCPA §1798.100(a)(1):** must list categories of PI collected at or before collection.
- **VCDPA §59.1-578(C)(1), CPA §6-1-1308(1)(a), CTDPA §42-520(c)(1), and all post-2024 statutes:** require the same plus the categories of third parties shared with.

### 2. Purposes of processing
- All 19 state statutes require **specific** purposes. Catch-all language ("for our business purposes") fails uniformly. See worked example in main SKILL.md.

### 3. Consumer rights enumeration
Minimum rights to enumerate (universal across all 19 — only the timing and the "appeal" right vary):
- Right to access (CCPA §1798.110; VCDPA §59.1-577(A)(1); etc.)
- Right to delete (CCPA §1798.105; VCDPA §59.1-577(A)(3); etc.)
- Right to correct (NOT in CCPA originally — CPRA added §1798.106; in VA/CO/CT/etc.)
- Right to data portability
- Right to opt-out of sale/share
- Right to opt-out of targeted advertising (NOT in CCPA originally — added under CPRA "share")
- Right to opt-out of profiling that produces legal/significant effects
- Right to limit use of sensitive PI (CA-specific) OR right to opt-in for processing of sensitive PI (other states)
- Right to appeal a denial (NOT in CCPA — required by VA, CO, CT, UT, OR, TX, MT, IA, IN, TN, DE, NH, NJ, KY, MD, MN, RI)

### 4. Response timing
- **CCPA:** 45 days, +45-day extension with notice. Verifiable consumer request required.
- **VA/CO/CT/UT/most others:** 45 days, +45-day extension. Free first request per 12 months.
- **TX:** 45 days, +45-day extension.
- **OR/DE/NH/NJ/MD/MN/RI:** 45 days, +45-day extension; appeal must be answered within 60 days.

### 5. Children's data
- CCPA: opt-in for sale of data of consumers 13-15; parental consent for under 13 (COPPA stack).
- VCDPA, CPA, CTDPA, OR, DE, MD, MN, RI: minors under 13 are treated as sensitive data triggering opt-in. **MD additionally bans targeted advertising or sale of data from any consumer under 18 (§14-4607(a)(2)).**
- Many post-2024 statutes prohibit selling data of consumers known to be under 16 without consent.

### 6. Universal Opt-Out Mechanism (UOOM/GPC)
States that **require** honoring the Global Privacy Control browser signal: CA, CO, CT, TX, MT, OR, DE, NH, NJ, MN, MD, RI, FL. Audit finding: if the privacy policy doesn't say "We honor browser-based opt-out signals such as the Global Privacy Control," this is a Major finding (CA: Critical due to AG enforcement track record — see *Sephora* 2022 settlement, $1.2M).

### 7. Sensitive data categories
Each state defines slightly differently. Common minimum (covers VA/CO/CT/most post-2024): racial/ethnic origin, religious beliefs, mental/physical health diagnosis, sexual orientation, citizenship/immigration status, genetic data, biometric data processed for unique identification, precise geolocation (typically 1,750-foot radius), data of a known child.

CCPA's "sensitive PI" (§1798.140(ae)) is broader and includes: SSN, driver's license, financial account + access credential, geolocation, racial/ethnic origin, religious beliefs, union membership, contents of mail/email/text messages, genetic data, biometric, health, sex life, sexual orientation.

**Audit shortcut:** If the policy lists sensitive categories, check that it covers BOTH the CCPA list AND the common post-2024 list (e.g., precise geolocation is in both, but "contents of mail" is CA-only).

### 8. Data Protection Assessments / Risk Assessments
- VA, CO, CT, OR, TX, MT, NH, NJ, DE, IN, KY, MD, MN, RI: required for processing involving (a) targeted advertising, (b) sale, (c) sensitive data, (d) profiling with reasonably foreseeable risk of unfair/deceptive treatment or substantial injury, (e) other heightened-risk activities.
- CA (CPRA Reg, finalized 2025): required for high-risk processing including ADM/AI training on personal data.
- **Audit finding:** if policy mentions any of the trigger activities but doesn't reference DPA process internally, flag Major. (DPAs are not customer-facing, but the policy should not contradict their existence.)

## State-specific gotchas worth knowing

- **CCPA "share" definition** is broader than "sell" — covers cross-context behavioral advertising even without monetary exchange (§1798.140(ah)). Most pre-2023 policies still use "sell" only and miss this.
- **CO Rule 6.05** requires bona fide loyalty programs to disclose the data exchange explicitly.
- **CT** added a separate consumer health data section in 2024 (Public Act 23-56) — overlaps with WA "My Health My Data" (see below).
- **TX** uniquely defines "small business" by SBA standard, not revenue/consumer count — many SaaS startups think they're exempt and aren't.
- **MD MODPA** has the strictest data minimization standard in the US: collection limited to what is "reasonably necessary and proportionate" to provide the specific product the consumer requested. This is essentially a US version of GDPR Art. 5(1)(c).
- **NJ** AG rules treat any financial-incentive-for-data program as requiring explicit opt-in.

## Sector-specific overlay statutes

- **WA "My Health My Data Act"** (RCW 19.373): consumer health data, opt-in consent, geofencing ban around healthcare facilities. NOT limited to HIPAA-covered entities. Effective Mar 2024. Applies to anyone collecting "consumer health data" of a WA resident.
- **NV SB 220 / NV SB 370:** narrower — sale opt-out for specified PI categories.
- **IL BIPA** (740 ILCS 14/): biometric identifiers, written consent + retention schedule + private right of action with statutory damages ($1k/$5k per violation). Audit any biometric collection on a site serving IL residents.
- **NY SHIELD Act:** breach notification + reasonable security; no comprehensive privacy rights but security obligations apply.
- **CA Delete Act (SB 362):** data brokers must register and honor a single consumer deletion request via a CA-run portal beginning Aug 2026.

## Audit decision tree for state coverage

1. Does the company operate (or serve users) in any of the 19 states above?
2. For each state where YES, does it meet at least one threshold?
3. For each state where threshold met, walk the 8 cross-cutting clauses above and produce one finding per missing element.
4. For WA, IL, NY, NV — apply sector overlays based on data type.
5. Stack a CA Delete Act finding if the company qualifies as a data broker (sells PI of consumers it has no direct relationship with).
