# Maryland — MODPA

**Citation form**: Maryland Online Data Privacy Act, Md. Code Com. Law §§ 14-4601 to -4612. Effective October 1, 2025. Enforced by the Maryland Attorney General (Consumer Protection Division).

> **MODPA is the strictest comprehensive state privacy law in the country.** Several provisions go materially beyond what any other state requires. A multi-state program built to MODPA generally exceeds all other state requirements with one exception (CA's notice-at-collection format).

## Applicability

Md. Code Com. Law § 14-4602. Applies to persons conducting business in Maryland or providing products/services targeted to MD residents AND during the preceding calendar year:

1. Controlled/processed PD of **at least 35,000** MD consumers (excluding solely-payment-transaction data); OR
2. Controlled/processed PD of **at least 10,000** MD consumers AND derived **at least 20%** of gross revenue from sale of PD.

Exemptions: standard.

## Strict data minimization standard — distinctive

§ 14-4607(a)(1). The collection of PD is limited to what is "**reasonably necessary AND proportionate**" to provide or maintain a specific product or service requested by the consumer.

> **This is materially stricter than the typical "necessary" or "necessary and proportionate" formulation** in other states. Practical effect: a controller may not collect PD for purposes the consumer has not specifically requested (e.g., generalized analytics, product improvement, third-party marketing) without separate justification or specific consent.
>
> **Operational impact**: privacy-by-default settings; reduced default tracking; tightened purpose statements; per-purpose consent flows. A privacy program targeting MD compliance must materially reduce default data collection.

## Sensitive data — strictest treatment

§ 14-4607(a)(2)–(4).
- **Flat ban on sale of sensitive data.** Consent does not cure the prohibition.
- **Consent required to process** sensitive data (cannot rely on legitimate interest or other grounds).
- Consumer health data (a defined subset) receives heightened treatment under MODPA's specific provisions.

## Minor protections — strictest in the country

§ 14-4607(a)(5).
- **Flat ban on sale of PD of consumers known to be under 18.**
- **Flat ban on processing of PD of consumers known to be under 18 for targeted advertising.**
- Heightened data minimization.
- No reliance on consent — these are flat prohibitions, not opt-out or opt-in defaults.

> The under-18 flat bans place MODPA significantly beyond any other state's minor regime. A controller serving a known minor audience cannot legally engage in sale or targeted advertising involving those consumers, regardless of consent.

## Consumer rights

§ 14-4605. Access, correct, delete, portability, opt-out of sale / targeted advertising / profiling with significant effects. **Right to obtain a list of categories of third parties** to whom controller has disclosed PD. **Right to appeal** within 60 days.

## Universal opt-out signal

§ 14-4606. Required at effective date (Oct 1, 2025).

## Controller duties

Beyond the standard set — privacy notice, security, processor contracts, data protection assessments — MODPA adds:
- The strict data minimization standard above.
- Consumer health data heightened protections.
- Specific notice obligations regarding processing of sensitive and minor data.
- Data protection assessments must address heightened risks under MODPA's standard.

## Enforcement

AG only. No private right of action. Civil penalties under MD CFA framework. Cure period: 60 days at enactment.

## MD-specific drafting considerations

1. **The strict data minimization standard is the single biggest operational lift.** Privacy programs built for other states generally fail MODPA on default data collection. Audit all collection points and tighten purposes; implement per-purpose consent for anything beyond providing the specifically requested service.
2. **Sale of sensitive data is flatly prohibited.** Adtech architectures that rely on consent for sensitive data (e.g., health-data adtech, financial-data sharing) cannot operate as designed for MD-resident consumers.
3. **Under-18 flat bans on sale and targeted advertising** require an age-gating or known-minor detection mechanism plus downstream suppression. Programs serving teens cannot rely on opt-in consent for sale or targeted ads of known minors.
4. UOOM mandatory at effective date.
5. **A program drafted to MODPA + CA exceeds all other state requirements.** This is the cleanest compliance posture for a national program.
