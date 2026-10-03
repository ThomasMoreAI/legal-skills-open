# Enforcement — AGs, Private Rights, Cure Periods, Penalties

**Purpose.** Consolidated reference to enforcement mechanics across US state comprehensive privacy laws. Use this when scoping risk, prioritizing remediation, or advising on enforcement defense posture.

> **Caveat.** Enforcement priorities and AG-issued guidance shift more frequently than the statutes themselves. When a question turns on a specific AG action or recent settlement, verify against current sources. The enforcement actions cited below are illustrative of AG priorities, not an exhaustive list.

## Master matrix — enforcement framework

| State | Enforcer | Penalty per violation | Cure period | PRA |
|---|---|---|---|---|
| CA | CPPA + AG | $2,500 / $7,500 (intentional or minor) | None (CPRA sunset) | Limited (data breach only — § 1798.150) |
| VA | AG | $7,500 | 30 days | None |
| CO | AG + DAs | $20,000 (cap $500k per series) | Sunset Jan 2025 | None |
| CT | AG | $5,000 (CUTPA framework, willful) | Sunset Jan 2025 | None |
| UT | AG (after Div. of Consumer Protection referral) | $7,500 | 30 days | None |
| TX | AG | $7,500 | 30 days | None |
| OR | AG | $7,500 | Sunset Jan 2026 | None |
| MT | AG | $7,500 | Sunset April 2026 | None |
| IA | AG | $7,500 | 90 days | None |
| IN | AG | $7,500 | 30 days at enactment | None |
| TN | AG | $7,500 + treble for willful | 60 days | None |
| DE | DOJ Consumer Protection | Per DE CFA framework | 60 days | None |
| NJ | AG (Div. of Consumer Affairs) | $10k first / $20k subsequent (NJ CFA) | 18-month grace at enactment | None |
| NH | AG | Per NH consumer protection framework | 60 days at enactment | None |
| NE | AG | $7,500 | 30 days at enactment | None |
| KY | AG | $7,500 | 30 days | None |
| MD | AG (CPD) | Per MD CFA framework | 60 days at enactment | None |
| MN | AG | $7,500 | 30 days for documented programs | None |
| RI | AG | Per RI consumer protection framework | At enactment | None |
| FL | AG (Dept. of Legal Affairs) | $50k / **$150k tripled** for minor/dark-pattern violations | 45 days | None |

## California — enforcement detail

### Authority

Two parallel enforcers:
- **CPPA**: administrative authority via the California Privacy Protection Agency. Rulemaking, enforcement, and audit power. Cal. Civ. Code § 1798.199.10 et seq.
- **California Attorney General**: parallel civil enforcement authority.

The two coordinate but operate independently. The CPPA's enforcement focus has been GPC handling, sensitive-data notices, and minor-data treatment.

### Notable enforcement actions

- ***In re Sephora* (2022)**: $1.2M settlement with the CA AG. First major CCPA enforcement. Core issues: failing to disclose that PI was sold; failing to provide the "Do Not Sell" link; failing to honor user requests submitted via GPC. Established that GPC handling is enforceable.
- ***In re DoorDash* (2024)**: $375k AG settlement. Marketing data exchanges with other businesses constituted "sales" under CCPA without proper notice or opt-out.
- ***CPPA v. Honda* (2024)**: ~$632k settlement. Issues with rights-request verification (requiring excessive verification), opt-out flows, and processor contract requirements.
- **CPPA pursued first administrative actions in 2024** under its independent authority.

### Private right of action

Cal. Civ. Code § 1798.150 — limited PRA only for unauthorized access and exfiltration, theft, or disclosure of certain non-encrypted/non-redacted PI as a result of the business's failure to implement reasonable security. Statutory damages **$100–$750 per consumer per incident** or actual damages, whichever is greater. Pre-litigation 30-day notice requirement.

### Litigation patterns

CCPA-related class actions have proliferated. Common theories: data-breach PRA, plus indirect theories framing CCPA violations as predicates under Cal. Bus. & Prof. Code § 17200 (Unfair Competition Law) — though courts have been mixed on UCL standing.

## Texas — aggressive enforcement posture

The Texas AG has been notably more active than other state AGs under the comprehensive privacy framework, alongside aggressive enforcement under companion laws.

- **TX AG vs. Meta (2022/2024)**: $1.4B settlement on biometric privacy under Tex. Bus. & Com. Code Ch. 503 (CUBI) — *not* under TDPSA, but reflective of aggressive AG posture.
- **TX AG vs. Google (2024)**: $1.375B settlement on geolocation, biometrics, and incognito-mode tracking — combined CUBI + DTPA theories.
- **TDPSA enforcement**: AG launched specific enforcement initiatives at TDPSA's effective date, focused on website privacy notices, sensitive-data handling, and minor protections under SCOPE Act. AG sent broad investigatory demands to large platforms.
- **TX AG SCOPE Act enforcement**: pursued multiple platforms over alleged failures to provide parental tools, age-appropriate experiences, and minor protections.

> **Operational implication**: TX is the most aggressively-enforced state privacy regime currently. Compliance posture for TX-targeted services should assume scrutiny.

## Colorado — rulemaking-focused enforcement

The CO AG has emphasized rulemaking and clear guidance over headline-grabbing enforcement actions. The CPA Rules (4 Colo. Code Regs. § 904-3) are the most prescriptive rules in any state, and enforcement has tracked rule-specific issues:

- Notice content (CPA Rules § 6).
- Consent specificity and dark patterns (CPA Rules § 7).
- UOOM recognition (CPA Rules § 5.06).
- Profiling and DPAs (CPA Rules §§ 8–9).
- Loyalty programs (CPA Rules § 6.04).

Cure period sunset Jan 2025 — AG enforcement now without statutory cure right.

## Connecticut — AG reports and "violations of concern"

The CT AG has issued enforcement reports identifying common violations encountered in compliance reviews. Common themes: missing or inadequate privacy notices; failure to provide opt-out methods; processor contract gaps; sensitive-data consent failures; dark-pattern consent flows.

## Federal Trade Commission — overlapping authority

Although not a state enforcer, the FTC's enforcement of "unfair or deceptive practices" (15 U.S.C. § 45) in the privacy context overlaps with state law. Notable FTC actions intersecting state privacy:

- **GoodRx (2023)**: $1.5M civil penalty + injunction. First HBNR action; addresses health-data sharing with third-party advertisers — issues that also implicate state sensitive-data rules.
- **BetterHelp (2023)**: $7.8M settlement; sharing of mental-health-related data for advertising.
- **Avast (2024)**: $16.5M settlement; sale of browsing data after representing it would not be sold.

Many state privacy enforcements parallel FTC theories. A controller settling with the FTC may face state AG follow-on actions.

## Companion-law enforcement to track

State comprehensive privacy laws are not the only enforcement risk. Privacy programs must also account for:

- **Wiretap / privacy of communications laws**: California's CIPA (Cal. Penal Code §§ 630–637.9) has been extensively litigated for use of session-replay / chat-based tracking technology. Plaintiff-side litigation focuses on alleged "wiretapping" via third-party analytics. Currently a high-volume class-action area.
- **Biometric privacy laws**: BIPA (IL), CUBI (TX), Washington biometric law, NY biometric law. BIPA's PRA + statutory damages drives extensive class-action litigation.
- **Telephone Consumer Protection Act (TCPA)**: federal, but heavily plaintiff-driven; intersects with state privacy programs around marketing consent.
- **Video Privacy Protection Act (VPPA)**: federal; recent litigation against video-on-demand platforms over Meta Pixel disclosing video-watching data.
- **Health-data sectoral laws**: WA MHMDA (private right of action), CT amendments, NV health data law.
- **Children's privacy**: COPPA, plus state-specific minor protection laws.
- **Data-breach notification laws** (all 50 states + DC + territories).

## Cure periods — current state

The clear trend is sunset, not extension.

| State | Cure status |
|---|---|
| CA | None (CPRA removed; AG/CPPA discretion) |
| VA | 30 days, in effect |
| CO | Sunset Jan 1, 2025 |
| CT | Sunset Jan 1, 2025 |
| UT | 30 days, in effect |
| TX | 30 days, in effect |
| OR | Sunset Jan 1, 2026 |
| MT | Sunset April 1, 2026 |
| IA | 90 days, in effect |
| IN | 30 days at enactment; verify current |
| TN | 60 days, in effect |
| DE | 60 days at enactment |
| NJ | 18-month grace at enactment (through approx. July 2026 for non-willful) |
| NH | 60 days at enactment |
| NE | 30 days at enactment |
| KY | 30 days, in effect |
| MD | 60 days at enactment |
| MN | 30 days for documented programs |
| RI | At enactment |
| FL | 45 days |

> **Practical implication**: cure periods are a temporary cushion at most, not a structural feature. Plan compliance as if no cure period existed.

## Defensibility — what reduces enforcement risk

### Documented privacy program

A written privacy program describing the controller's practices, governance, training, and incident response is the most defensibility-positive single artifact. TN provides an explicit affirmative defense; other states consider good-faith effort in penalty assessment.

### NIST Privacy Framework alignment

NIST PF is referenced in TIPA's affirmative defense and is a defensible benchmark elsewhere. A privacy program drafted to NIST PF demonstrates a structured approach to risk identification, governance, and continuous improvement.

### Risk assessments

Most states require DPAs for high-risk activities. A controller that has conducted DPAs and addressed identified risks demonstrates the kind of "considered risk management" that AGs view favorably. The reverse — conducting an activity that obviously triggers a DPA without having one — is a tell that compounds penalty exposure.

### Vendor management

Processor / service-provider contracts that meet state-specific requirements demonstrate that the controller is actively managing third-party risk. Stale or boilerplate contracts are a frequent enforcement finding.

### Rights-request fulfillment

Documented, audited rights-request workflows with response-time tracking demonstrate operational maturity. Rights-request failures (missed deadlines, inadequate verification, denials without basis) are easy AG findings.

### Cooperation

AGs uniformly indicate that early cooperation, voluntary disclosure, and remediation reduce penalty exposure. This is not a substitute for compliance but matters in how an investigation resolves.

## Penalty calculation — practical framing

Most state penalties are stated as "up to $X per violation." The "per violation" question is consequential and contested:

- **Per consumer**: each affected consumer's data treated as a separate violation. Multiplies penalties by user count.
- **Per practice**: each non-compliant practice (e.g., missing notice, missing opt-out link) treated as one violation. More modest penalties.
- **Per record**: each non-compliant data record as a separate violation.

States vary in how penalty cumulation is calculated. AGs have discretion to count aggressively. Settlements typically negotiate against the most aggressive count and resolve at a substantial discount, but the headline count drives leverage.

## Risk-tier summary

For prioritizing remediation:

- **Tier 1 (highest exposure)**: CA (CPPA + AG, no cure, large user base, active enforcement); TX (aggressive AG, companion-law exposure); FL (highest per-violation penalty for minor-related issues, narrow applicability but harsh penalties when triggered).
- **Tier 2 (substantial exposure)**: CO (prescriptive rules, no cure post-Jan 2025); CT (sunset cure, AG reports highlighting violation patterns); MD (strictest substantive standards once effective Oct 2025).
- **Tier 3 (moderate exposure)**: VA, OR, MT, NJ, MN — established AG enforcement frameworks but moderate penalty caps.
- **Tier 4 (lower exposure)**: UT, IA, IN, KY, NE, TN, NH, DE, RI — newer or weaker regimes; AG enforcement still developing.

A multi-state compliance program should address Tier 1 first, layer Tier 2 next, and treat Tiers 3–4 as substantially addressed by the upper-tier work.
