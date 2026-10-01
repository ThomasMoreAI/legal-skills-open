# Pre-launch checklist

Run before anything goes live, and again whenever the tag stack, the subscription model, or the customer footprint changes. Every finding is reported with its norm and its location, not as general advice. Findings that can be tested technically are tested technically, not assessed from intent.

## Technical pass first

These five steps produce most of the findings and take minutes:

1. Load the site in a clean browser profile with the network tab recording. List every third-party domain contacted **before** any consent action. That list is the ground truth for the privacy policy's sale/share section.
2. Application tab: record every cookie, localStorage and IndexedDB entry set before a consent action.
3. Send a Global Privacy Control signal and confirm, in the network log and in the vendor's own console, that advertising and sale/share processing actually stopped.
4. Full-text search the project — including CMS content, shop system strings, transactional email templates and PDF terms — for: `GDPR`, `legitimate interest`, `data controller`, `right to be forgotten`, `Data Protection Officer`, `supervisory authority`, `withdrawal`, `14 days`, `Click-to-Cancel`, `one-to-one consent`, `ODR`, `Art. `, `TMG`. Each hit is either a copied foreign template or an obsolete rule.
5. Complete signup, checkout and cancellation with the keyboard only.

## Scope

- [ ] Customer states enumerated; consumer counts and revenue recorded
- [ ] Applicability determined for **each** state comprehensive privacy law, with the threshold cited, and the determination written down
- [ ] Texas checked separately: Tex. Bus. & Com. Code § 541.002 has **no volume or revenue threshold** — it applies to any entity doing business in Texas or producing a product or service consumed by Texans that processes or sells personal data and is not an SBA small business
- [ ] CalOPPA (Cal. Bus. & Prof. Code § 22575 et seq.) applied regardless of size
- [ ] Sectoral triggers checked: COPPA, HIPAA, GLBA/Safeguards, FERPA, FCRA, VPPA
- [ ] EU/UK exposure assessed under GDPR Art 3(2); Art 27 representative considered if goods or services are offered into the EU

## Privacy policy and notices

- [ ] Privacy policy reachable from every page, without login, not blocked by a consent banner
- [ ] Last-updated date within 12 months (Cal. Civ. Code § 1798.130(a)(5))
- [ ] Categories, purposes, recipients and retention stated per category
- [ ] Sale/share statement verified against the network capture, not against the client's belief
- [ ] Notice at collection delivered at or before the point of collection, separate from the policy (Cal. Civ. Code § 1798.100(a); 11 CCR § 7012)
- [ ] Texas: verbatim notice "NOTICE: We may sell your sensitive personal data." where applicable, and "NOTICE: We may sell your biometric personal data." where applicable, in the same location and manner as the privacy notice (Tex. Bus. & Com. Code § 541.102(b), (c))
- [ ] CalOPPA Do Not Track disclosure present and truthful (Cal. Bus. & Prof. Code § 22575(b)(5)), and the equivalent Delaware disclosure (6 Del. C. § 1205C) — both apply with no threshold
- [ ] No GDPR vocabulary unless the business is genuinely GDPR-exposed and the section is correct
- [ ] No absolute security claim
- [ ] Washington consumer health data: a **separate** policy with its own prominent homepage link (RCW 19.373.020)

## Rights and opt-outs

- [ ] "Do Not Sell or Share My Personal Information" link on the homepage, or a compliant combined link (Cal. Civ. Code § 1798.135)
- [ ] "Limit the Use of My Sensitive Personal Information" link where required
- [ ] Both links work without an account and without a banner in the way
- [ ] Global Privacy Control detected and honoured — tested, not assumed
- [ ] Request intake channels live; California requires two, including a toll-free number unless the online-only exception applies (§ 1798.130(a)(1))
- [ ] Response deadlines operationally achievable (California: 45 days, extendable once by 45 with notice)
- [ ] Appeal process built where a state requires one, with the state attorney general's contact route disclosed
- [ ] Deletion propagates to service providers, backups policy documented, and to advertising platforms

## Tracking

- [ ] No third-party advertising, analytics, session-replay, chat or fingerprinting script fires before a consent action
- [ ] Every third-party vendor identified by name and covered by a contract with the statutory service-provider or processor terms
- [ ] Consent record retained: timestamp, banner version, choice, scripts blocked
- [ ] Video pages with an advertising pixel: standalone VPPA consent (18 U.S.C. § 2710(b)(2)(B)) or the pixel removed
- [ ] CIPA exposure assessed for California traffic; pen-register theory (Cal. Penal Code § 638.51) considered, not only wiretapping
- [ ] No reliance on any CIPA statutory exemption that has not actually been enacted

## Children and teens

- [ ] Child-directed determination made against 16 CFR § 312.2 and written down
- [ ] If covered: verifiable parental consent before collection, and a **separate** consent for disclosure to third parties including advertising
- [ ] No advertising or analytics SDK on child-directed surfaces without that separate consent
- [ ] Retention policy published; children's data security programme written
- [ ] "We do not knowingly collect information from children under 13" verified against actual audience data before publication
- [ ] For 13–17: state-law restrictions on targeted advertising and sale checked at the correct age for each state

## Email and SMS

- [ ] Valid physical postal address in every commercial email (15 U.S.C. § 7704(a)(5)(A)(iii))
- [ ] Opt-out present, functional, requiring nothing beyond an email address; operable 30 days; honoured within 10 business days
- [ ] Suppression list applied across every sending system
- [ ] Headers, sender name and subject lines accurate (§ 7704(a)(1)–(2))
- [ ] SMS: separate unchecked consent checkbox with on-screen language, "consent is not a condition of purchase", frequency and rates disclosed (47 CFR § 64.1200(f)(9))
- [ ] SMS consent records retained with timestamp, IP, exact wording and page URL
- [ ] STOP handling tested; revocation by other channels routed to the same suppression list (47 CFR § 64.1200(a)(10), 10 business days)
- [ ] Sends confined to 8 a.m.–9 p.m. in the recipient's local time (47 CFR § 64.1200(c)(1))

## Subscriptions

- [ ] No reference anywhere to the FTC "Click-to-Cancel" Rule or 16 CFR Part 425 as a live obligation
- [ ] Material terms disclosed before billing information is collected (15 U.S.C. § 8403(1))
- [ ] Separate unchecked consent to the renewal terms, distinct from terms-of-service acceptance (Cal. Bus. & Prof. Code § 17602(a)(4))
- [ ] Retainable post-purchase acknowledgment with cancellation instructions (§ 17602(a)(3))
- [ ] Online cancellation in the same place as enrolment, completing in the flow, no live-agent requirement (§ 17602(d), (f); 815 ILCS 601/10; Va. Code § 59.1-207.46)
- [ ] Reminder cadence set to the strictest state in the footprint (Colorado C.R.S. § 6-1-732 requires 25–40 days before **each** renewal)
- [ ] Consent records retained at least 3 years or 1 year after termination, whichever is longer

## Advertising and reviews

- [ ] Every claim substantiated before publication
- [ ] No fabricated, sentiment-purchased or undisclosed insider reviews (16 CFR §§ 465.2, 465.4, 465.5)
- [ ] Review display not filtered to suppress negatives while implying completeness (§ 465.7)
- [ ] No purchased followers or engagement (§ 465.8)
- [ ] Influencer and affiliate disclosures in the endorsement itself, above the fold (16 CFR § 255.5)
- [ ] "Made in USA" claims tested against all three conditions of 16 CFR § 323.2
- [ ] Reference prices are genuine former prices; total price with mandatory fees shown before the final step
- [ ] Consent and cancellation interfaces checked for dark patterns — an asymmetric interface invalidates the consent it collects

## Selling

- [ ] No claim of a statutory cooling-off period or a 14-day right to cancel an online purchase
- [ ] Return policy published, linked before payment, honoured as written
- [ ] Cal. Civ. Code § 1723 display satisfied where the policy is less generous than a 7-day full refund or exchange
- [ ] Shipping timeframe stated with a reasonable basis; 16 CFR Part 435 delay/refund process implemented

## Terms and platform

- [ ] Terms accepted through an unchecked checkbox or equivalently conspicuous mechanism adjacent to the action button
- [ ] Link to terms visually identifiable as a link; notice states that the action is assent
- [ ] Acceptance records and all historical versions retained
- [ ] Arbitration clause reviewed against *Heckman v. Live Nation*; no bellwether provision binding non-participating claimants
- [ ] Severability drafted so a failed arbitration clause does not void the agreement
- [ ] If UGC is hosted: DMCA agent registered electronically with the Copyright Office, contact published on the site, **renewal diarised within three years** (37 CFR § 201.38(c)(4))
- [ ] Repeat-infringer policy written and actually enforced (17 U.S.C. § 512(i)(1)(A))

## Accessibility

- [ ] Keyboard and screen-reader passes through signup, search, cart and checkout
- [ ] Contrast measured; labels associated; errors described in text
- [ ] Third-party embeds tested — they are the usual failure point
- [ ] No overlay widget relied on as the remedy
- [ ] Any published accessibility statement matches audited reality
- [ ] No citation of the DOJ Title II rule or its compliance dates as binding on a private business

## Health and biometrics

- [ ] Consumer health data assessed under RCW 19.373.010, including inferences
- [ ] Separate consent to collect and to share; valid authorization before any sale (RCW 19.373.030, .070)
- [ ] No geofence around health facilities in any ad platform (RCW 19.373.080; Conn. Gen. Stat. § 42-526)
- [ ] Any face, fingerprint, voice or iris processing checked against BIPA § 15(b) before first collection, with a published retention schedule under § 15(a)
- [ ] Texas notice and consent satisfied for biometric identifiers (Tex. Bus. & Com. Code § 503.001)

## Closing out

- [ ] Every `[[MISSING: …]]` either resolved or reported to the user as outstanding
- [ ] Every `[[UNVERIFIED: …]]` either verified against an official source or carried forward in the report
- [ ] Draft marker `<!-- DRAFT – NOT LEGALLY APPROVED -->` still present in every generated text
- [ ] Legal review obtained where the obligation matrix flags it as mandatory

## Reporting format

Report findings as a table, most severe first:

| Severity | Location | Norm | Finding | Fix |
|---|---|---|---|---|
| critical / high / medium | file:line or URL | citation | what is missing or wrong | the concrete step |

**Critical** means class-action exposure, civil-penalty exposure, or an unenforceable contract: no privacy policy, third-party trackers firing before consent in California, a false "we do not sell" statement, missing DMCA agent registration on a UGC site, an unenforceable terms acceptance flow, a subscription with no online cancellation, or marketing SMS without prior express written consent.
