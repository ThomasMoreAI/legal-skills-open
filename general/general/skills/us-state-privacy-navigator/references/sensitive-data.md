# Sensitive Data — Definitions, Structures, and Operational Implications

**Purpose.** A consolidated reference to "sensitive data" / "sensitive personal information" across US state privacy laws as defined in Cal. Civ. Code § 1798.140(ae), Va. Code § 59.1-575, Colo. Rev. Stat. § 6-1-1303(24), and Md. Code Com. Law § 14-4601(cc) — and as a category of personal data, the single most variable concept across these statutes (definitions, structures (opt-in vs. opt-out), and exceptions diverge materially).

## Two structural models

| Model | States | Mechanism |
|---|---|---|
| **Opt-in / consent before processing** | VA, CO, CT, TX, OR, MT, IN, TN, DE, NJ, NH, NE, KY, MD, MN, RI, FL | Controller may not process sensitive data without affirmative consumer consent. Meets GDPR-style opt-in standard. |
| **Opt-out + notice (CA structure)** | CA | Controller may process sensitive PI; consumer has right to limit use to that necessary to provide goods/services reasonably expected (Cal. Civ. Code § 1798.121; CCPA Regs § 7027). Notice and "Limit Use of Sensitive PI" link required. |
| **Opt-out + notice (UT/IA structure)** | UT, IA | Controller must provide clear notice and opportunity to opt out *before* processing. Less prescriptive than CA's "limit use" framework. |

> **The structural difference matters operationally.** A program designed for opt-in (the majority approach) over-satisfies CA's limit-use framework on the legal substance but may not satisfy CA's specific notice-and-link mechanics. A program designed only for opt-out (CA-style) fails in 17 other states. Default to opt-in for the multi-state baseline, then add CA's specific notice and link.

## Categories — common baseline

Most states' "sensitive data" definitions converge on the following categories (illustrative provisions: Va. Code § 59.1-575; Colo. Rev. Stat. § 6-1-1303(24); Conn. Gen. Stat. § 42-515(28)):

1. Racial or ethnic origin.
2. Religious beliefs (and, in some states, philosophical beliefs).
3. Mental or physical health diagnosis or condition.
4. Sex life or sexual orientation.
5. Citizenship or immigration status.
6. Genetic data.
7. Biometric data **processed for the purpose of uniquely identifying an individual** (the qualifier matters — biometric data not used for unique ID is generally not "sensitive").
8. Precise geolocation (typically defined as location data accurate within ~1,750 feet or ~1,000 feet, depending on the state).
9. Personal data of a known child (under 13 in most states).

## State-specific additions

Beyond the baseline, several states add categories. Always cross-reference the per-state file.

| State | Additional sensitive data categories |
|---|---|
| **CA** | Government identifiers (SSN, driver's license, passport, state ID); account login + access credentials; contents of mail/email/text (unless business is intended recipient); union membership |
| **OR** | Status as a victim of crime; transgender or non-binary status |
| **NJ** | Financial information (account number, credit/debit card number with security/access code); transgender or non-binary status |
| **MD** | Consumer health data (defined subset); national origin |
| **CT** | Status as a member of a specific group when combined with other PD; broader treatment of biometric data |
| **MN** | Citizenship or immigration status broadly; biometric data treatment |
| **FL** | Biometric, genetic, geolocation explicitly enumerated alongside health, race, religion, sex orientation |

## Children — separate but overlapping rule

Sensitive data definitions universally include "personal data of a known child." (See, e.g., Cal. Civ. Code § 1798.140(ae)(1); Va. Code § 59.1-575; Colo. Rev. Stat. § 6-1-1303(24)(g).) This means:
- Processing PD of a known child = processing sensitive data = consent required (in opt-in states) or limit-use applies (in CA).
- The relevant consent standard is **parental consent** under COPPA for under-13. State laws layer state-specific consent and design obligations.
- See `references/kids-and-teens.md` for the full overlay.

## Health data — the most contested category

Health data is one of the most operationally complex sensitive categories.

- **HIPAA-covered data** is generally exempted at either the entity or data level (varies by state). HIPAA-covered entities and BAs processing PHI are largely outside state privacy laws for that data.
- **Non-HIPAA health data** (e.g., wellness apps, fitness wearables, period trackers, telehealth platforms outside HIPAA scope, employer wellness programs, search-history-derived health inferences) is sensitive data under most state laws.
- **Washington's My Health My Data Act** (RCW 19.373) imposes additional sectoral rules for non-HIPAA "consumer health data" — not a comprehensive privacy law, but layered on top.
- **Nevada SB 370** and **Connecticut's amendments** also address consumer health data specifically.
- **Maryland MODPA** treats consumer health data as a heightened subset within sensitive data.

When a controller processes health-related data outside HIPAA, the analysis must layer:
1. Federal HIPAA (if applicable).
2. State comprehensive privacy law sensitive-data rules.
3. State-specific consumer-health-data laws (WA, NV, CT amendments).
4. State biometrics laws (BIPA, CUBI, etc.) where biometric health data is involved.

## Biometric data — a sub-discipline

Biometric data is sensitive *only when processed for the purpose of uniquely identifying an individual*. The qualifier excludes:
- Demographic biometric analysis (e.g., aggregate face-detection for occupancy counting) where unique ID is not the purpose.
- Biometric data used for liveness detection only.

But the qualifier does NOT exclude:
- Storage of biometric templates for future re-identification.
- Cross-referencing biometric data with identity records.
- Use of biometric data in surveillance contexts.

State biometrics laws (separate from comprehensive privacy laws) apply additionally:
- **Illinois BIPA** (740 ILCS 14): private right of action with statutory damages; consent and disclosure requirements for biometric identifiers (face, fingerprint, voice, retina, hand). Most-litigated biometric statute in the country.
- **Texas CUBI** (Tex. Bus. & Com. Code § 503.001): similar in substance; AG enforcement only.
- **Washington biometric law** (RCW 19.375).
- **NY biometric privacy law** (NYC Admin. Code) for commercial establishments using biometrics.

A multi-state privacy program processing biometric data must layer state biometric-specific laws on top of comprehensive state privacy laws. The most exposed risk is BIPA's private right of action with statutory damages.

## Operational requirements — what consent looks like

Where opt-in consent is required, "consent" in most states means (see, e.g., Va. Code § 59.1-575 (definition of "consent"); Colo. Rev. Stat. § 6-1-1303(5); Conn. Gen. Stat. § 42-515(6)):
- **Affirmative**: clear act manifesting agreement.
- **Specific**: tied to the specific processing purpose.
- **Informed**: based on disclosure of the purpose, categories, and consequences.
- **Unambiguous**: not inferred from inaction or pre-checked boxes.
- **Freely given**: not bundled with non-sensitive consents; revocable.

**Dark patterns** (interfaces designed to manipulate consent) are explicitly prohibited in CO, CT, CA Regs, and others. Common dark patterns to avoid:
- Pre-checked consent boxes.
- Unequal-prominence "Accept" / "Reject" buttons (e.g., "Accept" prominent and bright; "Reject" gray and small).
- Confusing or contradictory language.
- Forcing consent to access non-related services.
- Repeated re-prompting after declination.

CCPA Regs § 7004 and CO CPA Rules § 7 are the most prescriptive on dark-pattern prohibitions.

## Notice and disclosure requirements

| State | Sensitive data notice requirements |
|---|---|
| CA | Notice in privacy policy; notice-at-collection identifying sensitive PI categories; "Limit Use" link on homepage |
| Most others | Notice in privacy policy of categories and purposes; explicit consent flow before processing |
| MD | Heightened notice obligations; disclosures of consumer health data treatment |
| FL | Specific "DO NOT SELL MY SENSITIVE PERSONAL DATA" disclosure for sale practices |
| TX | Specific notice text required for sensitive data sale |

## When in doubt — treat as sensitive

If a category is borderline (e.g., inferred health interest based on browsing, demographic data, location data not technically "precise"), the conservative posture is to treat as sensitive and obtain consent (or apply CA's limit-use). The downside risk of treating as sensitive when not legally required is minimal (overcollection consent); the downside risk of treating as non-sensitive when legally required is per-instance violation exposure.

## Cross-cutting drafting considerations

1. **Build a single sensitive-data category map.** Identify each data element processed and tag with the union of state-specific sensitive-data classifications. The output is the controller's "sensitive data inventory" — required by some states and good practice everywhere.
2. **Default to opt-in.** Multi-state programs should default to opt-in consent for sensitive data, layered with CA's limit-use mechanics. This is the cleanest architecture.
3. **Tier consent**. Different sensitive categories may merit different consent flows (e.g., health data warrants more granular flow than precise geolocation). Don't bundle.
4. **Do not sell sensitive data without affirmative review.** MD bans it outright; many states require opt-in for sale even if generally allowed; AG enforcement focuses heavily on undisclosed sensitive-data sale.
