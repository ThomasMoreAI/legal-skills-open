# Health data and biometrics

Status as at 2026-08-05.

Two of the sharpest private rights of action in US privacy law sit here: Illinois BIPA and Washington's My Health My Data Act. Neither depends on HIPAA, and both catch ordinary consumer businesses that would not describe themselves as handling health or biometric data.

## HIPAA — 45 CFR Parts 160, 162, 164

HIPAA applies to **covered entities** (health plans, health care clearinghouses, and health care providers who transmit health information electronically in connection with a covered transaction) and to their **business associates**. A wellness app, a supplement shop, a fitness tracker or a symptom quiz is not a covered entity merely because it handles health information. Selling a HIPAA-styled "HIPAA compliant" claim without being covered is an FTC Act § 5 deception risk in its own right.

**Tracking technologies on covered-entity websites.** OCR's December 2022 bulletin asserted that an IP address combined with a visit to an unauthenticated public webpage about a health condition or provider could be protected health information. In *American Hospital Association v. Becerra* (N.D. Tex., 20 June 2024) the court declared that portion unlawful and **vacated** it — specifically the position that HIPAA obligations are triggered where an online technology connects an individual's IP address with a visit to an unauthenticated public webpage addressing specific health conditions or health care providers. HHS withdrew its appeal on 29 August 2024, so the vacatur stands. The rest of the guidance survives, and tracking on **authenticated** patient portals remains squarely within HIPAA. Do not tell a client that pixels on hospital sites are now unproblematic — state privacy and wiretap claims over exactly this conduct are unaffected by the vacatur.

`[[UNVERIFIED: status of the January 2025 HIPAA Security Rule NPRM — whether a final rule has issued by 2026-08-05. Check hhs.gov/hipaa before advising on security-rule obligations.]]`

## FTC Health Breach Notification Rule — 16 CFR Part 318

The gap-filler for health apps **not** covered by HIPAA. Amendments effective **29 July 2024** confirm that health apps and similar technologies that draw health information from multiple sources are vendors of personal health records, expand the notification content, and make clear that unauthorised disclosure — including disclosure to advertising platforms via a pixel — can itself be a "breach of security" requiring notification to affected individuals, the FTC, and in some cases the media. This is how the FTC has reached consumer health apps that shared data with advertisers.

## Washington My Health My Data Act — chapter 19.373 RCW

The most demanding consumer health statute in the country, and the one with teeth.

- Effective **31 March 2024** for regulated entities; **30 June 2024** for small businesses; the geofencing prohibition took effect earlier, on 23 July 2023.
- **Consumer health data** is defined far more broadly than health data in the ordinary sense: it covers bodily functions, symptoms, diagnoses, gender-affirming and reproductive care, precise location that could indicate an attempt to obtain health services, health-related purchases, and **inferences** drawn from any non-health data to associate a consumer with the above. A supplements retailer, a period tracker, a fitness app and a mental-wellness newsletter are all in scope.
- **RCW 19.373.020** — a regulated entity and a small business "shall prominently publish a link to its consumer health data privacy policy on its homepage." This is a **separate link and a separate document**. Folding consumer health data into the general privacy policy does not satisfy it. This is the single most commonly missed requirement in the statute.
- **RCW 19.373.030** — consent required to collect; consent to share must be "separate and distinct from the consent obtained to collect consumer health data."
- **RCW 19.373.070** — selling requires a **valid authorization** with prescribed content, separate from consent, signed and time-limited.
- **RCW 19.373.080** — unlawful to implement a geofence around an entity providing in-person health care services to identify consumers, collect health data, or send health-related messages.
- **RCW 19.373.090** — a violation is an unfair or deceptive act under the Consumer Protection Act, chapter 19.86 RCW, which carries a **private right of action**. That is the reason this statute matters more than its state's size suggests.

**Nevada** — SB 370 (2023), codified in chapter 603A NRS, effective **31 March 2024**. Parallel structure: published health-data privacy policy, consent to collect and share, separate authorisation to sell, geofencing ban. Enforcement is by the Attorney General as a deceptive trade practice; **no private right of action**.

**Connecticut** — the CTDPA amendments effective **1 October 2023** fold consumer health data into "sensitive data" (Conn. Gen. Stat. § 42-526), requiring consent, prohibiting sale without consent, and banning geofences within 1,750 feet of mental health, reproductive or sexual health facilities. Attorney General enforcement only.

## Illinois BIPA — 740 ILCS 14

Applies to "biometric identifiers" (retina or iris scan, fingerprint, voiceprint, scan of hand or face geometry) and biometric information derived from them. Photographs and information derived from them are excluded from the definition, but face-geometry scans derived from photographs are not — that is the fault line in the case law.

- **§ 15(a)** — publish a written retention schedule and destruction guidelines; destroy on the earlier of purpose satisfaction or three years after the last interaction.
- **§ 15(b)** — before collection: inform the subject in writing that biometric data is being collected and stored, inform in writing of the purpose and the retention period, and obtain a **written release**.
- **§ 15(c)** — no selling, leasing, trading or otherwise profiting from biometric data.
- **§ 15(d)** — no disclosure without consent or a listed exception.
- **§ 20** — private right of action: **$1,000 or actual damages for negligent violations, $5,000 or actual damages for reckless or intentional violations**, plus attorney's fees.

**The 2024 amendment matters.** SB 2979, Public Act 103-0769, signed and effective **2 August 2024**: a private entity that collects or discloses biometric data from the same person using the same method of collection is liable for **a single violation per person**, not one per scan. The Seventh Circuit has held the amendment applies retroactively to pending cases. The amendment also confirms that a "written release" may be executed by **electronic signature**. Damages are now bounded, but the exposure is still real and the notice-and-release mechanics are unchanged.

## Texas CUBI — Tex. Bus. & Com. Code § 503.001

Notice and consent required before capturing a biometric identifier for a commercial purpose; limits on sale and disclosure; reasonable care in storage; destruction within a reasonable time and no later than one year after the purpose expires. Civil penalty up to **$25,000 per violation**, enforceable **only by the Texas Attorney General** — there is no private right of action. The absence of a private right of action does not make it low-risk: the AG's 2024 settlement with Meta over facial recognition was $1.4 billion.

Other states with biometric provisions: Washington RCW 19.375 (AG enforcement), Colorado's 2024 biometric amendments to the CPA, and the sensitive-data consent requirements in every state comprehensive privacy law, which treat biometric data processed for identification as sensitive and require opt-in consent.

## Sensitive data under the state comprehensive privacy laws

Independently of the health and biometric statutes, every state comprehensive privacy law treats health data and biometric data processed for identification purposes as **sensitive data**. The consequence differs by state and the difference is not cosmetic:

- Most states require **opt-in consent** before processing sensitive data at all.
- **California** instead gives a right to **limit** the use and disclosure of sensitive personal information (Cal. Civ. Code § 1798.121), surfaced through the "Limit the Use of My Sensitive Personal Information" link.
- **Texas** requires the verbatim notice "NOTICE: We may sell your sensitive personal data." and, separately, "NOTICE: We may sell your biometric personal data.", in the same location and manner as the privacy notice (Tex. Bus. & Com. Code § 541.102(b), (c)). Small businesses otherwise outside the Texas act still may not sell sensitive data without prior consent (§ 541.107).
- **Maryland** prohibits the sale of sensitive data outright rather than conditioning it on consent — see `state-privacy-scope.md`.

Sensitive-data processing also triggers the data protection assessment duty in most states.

## Template — Washington consumer health data privacy policy

This is a **separate document** from the general privacy policy, with its own prominent homepage link (RCW 19.373.020). Do not merge it.

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h1>Consumer Health Data Privacy Policy</h1>
<p>Effective date: [[DATE]].</p>

<h2>Categories of consumer health data we collect</h2>
<p>[[LIST, INCLUDING ANY DATA FROM WHICH HEALTH STATUS IS INFERRED]]</p>

<h2>Sources</h2>
<p>[[DIRECTLY FROM THE CONSUMER / DEVICE / THIRD PARTY — NAME EACH]]</p>

<h2>Purpose of collection and how the data is used</h2>
<p>[[PURPOSE PER CATEGORY]]</p>

<h2>Categories of consumer health data we share</h2>
<p>[[CATEGORIES]]</p>

<h2>Third parties and affiliates we share it with</h2>
<p>[[NAME THE SPECIFIC THIRD PARTIES AND AFFILIATES]]</p>

<h2>Your rights</h2>
<p>
  You may confirm whether we collect, share or sell your consumer health data
  and access it; obtain a list of the third parties and affiliates with whom
  we have shared or sold it, including contact information for each; withdraw
  consent to collection and to sharing; and request deletion. Contact
  [[EMAIL]] or [[URL]]. We will respond within [[NUMBER]] days and you may
  appeal a refusal at [[APPEAL ROUTE]].
</p>
```

## Checkpoints

- [ ] Determined whether the business is a HIPAA covered entity or business associate — and if not, no "HIPAA compliant" claim appears anywhere
- [ ] If a covered entity: tracking on authenticated portals removed or covered by a business associate agreement
- [ ] Assessed whether any processed data is "consumer health data" under RCW 19.373.010 — including inferences from purchases, search terms and location
- [ ] If in scope for Washington: a **separate** consumer health data privacy policy exists, with its own prominent homepage link (RCW 19.373.020)
- [ ] Consent to collect and separate consent to share captured and logged (RCW 19.373.030)
- [ ] Valid authorization obtained before any sale of consumer health data (RCW 19.373.070)
- [ ] No geofence around health facilities in any advertising platform (RCW 19.373.080; Conn. Gen. Stat. § 42-526)
- [ ] Any face, fingerprint, voice or iris processing checked against BIPA § 15(b) — written notice, purpose, retention period, written release captured before first collection
- [ ] Public biometric retention and destruction schedule published (BIPA § 15(a))
- [ ] Texas notice and consent satisfied if biometric identifiers are captured from Texans (§ 503.001)
- [ ] Non-HIPAA health app: FTC Health Breach Notification Rule process documented, including who notifies the FTC and within what period
