# Pre-launch checklist

Status as at 2026-08-05.

Run before go-live and before any material change. Every finding is reported with its instrument and article, not as a general remark. Anything technically verifiable is verified technically, not judged from intent.

## Technical pass first

These five steps produce roughly half the findings and take minutes:

1. Load the site in a **fresh browser profile** with the network tab recording. List every third-party domain contacted **before** any consent decision.
2. Application tab: capture every cookie, `localStorage`, `sessionStorage` and IndexedDB entry written before the decision.
3. Project-wide full-text search, including CMS content, shop-system defaults, email templates and invoice templates, for: `odr`, `ec.europa.eu/consumers/odr`, "online dispute resolution", "ODR platform", "Privacy Shield", "Safe Harbor", "ePrivacy Regulation", "§ 5 TMG", "§ 312k", "BDSG", "CCPA", "Do Not Sell".
4. Walk the full purchase or signup flow **with the keyboard only**, then again with a screen reader.
5. Compare the vendor list in the privacy notice against the domains found in step 1. Every mismatch is a finding in one direction or the other.

## Instrument classification

- [ ] Recorded for each obligation whether the source is a **Regulation** (direct) or a **Directive** (national transposition), and no consumer-facing text cites a directive article (Art 288 TFEU; Case C-91/92 Faccini Dori)
- [ ] Every national dependency listed as an explicit `[[MISSING: … — member state]]` item rather than defaulted
- [ ] Target member states identified; the list of national skills that must still run is stated

## Data protection

- [ ] Privacy notice reachable without consent and without login, from every page
- [ ] Purpose, **legal basis**, recipients, retention stated **per processing**, not once for the site (Art 13(1)(c), 13(2)(a) GDPR)
- [ ] Legitimate interests named concretely with a written balancing test on file (Art 6(1)(f), Art 13(1)(d))
- [ ] Recipients named and reconciled with the network trace
- [ ] Art 14 processings covered, including the **source** of the data and the one-month / first-communication / first-disclosure timing (Art 14(2)(f), 14(3))
- [ ] Special categories identified including by inference; an Art 9(2) exception exists per purpose
- [ ] Child-consent age stated per member state with the national statute (Art 8(1)) — no single EU-wide figure
- [ ] Full rights list, consent-withdrawal notice and complaint right present (Art 13(2)(b)–(d))
- [ ] Correct supervisory authority named with a working address
- [ ] Automated decision-making either ruled out explicitly or described with logic and consequences (Art 13(2)(f), Art 22)
- [ ] Data subject request process meets the one-month deadline with the documented two-month extension route (Art 12(3))
- [ ] Records of processing exist for controller and, where applicable, processor roles (Art 30(1), 30(2))
- [ ] Every processor has a contract with all eight Art 28(3) letters
- [ ] Breach procedure with a named awareness trigger, the 72-hour clock and an all-breaches register (Arts 33(1), 33(5))
- [ ] DPIA screening against Art 35(3) and the national authority's Art 35(4) list; prior consultation planned where residual high risk (Art 36(1))
- [ ] DPO test run against Art 37(1) and any national rule under Art 37(4)
- [ ] Art 3(2) assessed; Art 27 representative designated and named where required
- [ ] No text describing the Digital Omnibus proposal as if it were law

## Transfers

- [ ] Every non-EEA recipient listed with country and Chapter V basis, including remote access
- [ ] Adequacy claims checked against the Commission list as at the drafting date — UK renewed 12/2025, Brazil added 02/2026
- [ ] Data Privacy Framework relied on only for recipients actually certified, for the right data category, and with a fallback basis (appeal pending, Case C-703/25 P)
- [ ] SCC module matches the real relationship; pre-GDPR SCCs absent
- [ ] Transfer impact assessment written and dated per destination (EDPB Recommendations 01/2020)
- [ ] No "Privacy Shield" or "Safe Harbor" reference anywhere

## Terminal equipment and consent

- [ ] No non-exempt request fires and no non-exempt storage occurs before a decision (Art 5(3) Dir 2002/58/EC)
- [ ] Reject on the first banner layer, visually equivalent to Accept
- [ ] No pre-ticked categories or default-on sliders
- [ ] Per-purpose granularity
- [ ] Withdrawal permanently reachable and no harder than granting (Art 7(3) GDPR)
- [ ] "Strictly necessary" list documented per item, with the reason
- [ ] Legitimate interest not claimed for any terminal-equipment access
- [ ] Fingerprinting, pixels, `localStorage` and server-side tagging treated as in scope (EDPB Guidelines 2/2023 v2.0)
- [ ] Email tracking pixels behind consent
- [ ] Consent log records timestamp, banner version, text version and per-category choice (Art 7(1))
- [ ] Any pay-or-consent model assessed against EDPB Opinion 08/2024
- [ ] Consent lifetime stated only with the national rule that sets it

## Marketing

- [ ] Prior consent for marketing email and SMS, **or** all three Art 13(2) Dir 2002/58/EC soft opt-in conditions met and documented
- [ ] Double opt-in with a marketing-free confirmation message, and proof of consent retained
- [ ] Unsubscribe in every message, free of charge and easy (Art 13(2))
- [ ] Sender identity never disguised, valid opt-out address present (Art 13(4))
- [ ] Absolute right to object to direct marketing honoured and advertised (Art 21(2)–(3) GDPR)

## Selling to consumers

- [ ] Order button carries the **national** statutory wording and nothing else (Art 8(2) Dir 2011/83/EU) — the sanction is that the consumer is not bound
- [ ] Order summary immediately above the button with Art 6(1)(a), (e), (o), (p)
- [ ] Total price including taxes; delivery charges separate and disclosed before the order (Art 6(1)(e), 6(6))
- [ ] Trader identity, geographical address, telephone **and** email present (Art 6(1)(c))
- [ ] Personalised pricing disclosed where automated decision-making sets the price (Art 6(1)(ea))
- [ ] Withdrawal instruction with the national period and terminology, plus the model form (Art 6(1)(h), Annex I(B))
- [ ] **Withdrawal function present, continuously available, with a separate confirmation step and durable-medium acknowledgement (Art 11a, mandatory since 19.06.2026)**
- [ ] Digital content with immediate access: two separate, non-pre-ticked declarations logged with timestamps (Art 16(m))
- [ ] No invented withdrawal exceptions
- [ ] Data-funded free services: no withdrawal exclusion claimed under Art 16(a) or (m)
- [ ] Legal-guarantee reminder present (Art 6(1)(l)); plan in place for the 27.09.2026 additions under Dir (EU) 2024/825
- [ ] Conformity periods stated per member state, not as a flat EU figure (Arts 10, 11 Dir (EU) 2019/771)
- [ ] Repair extends the liability period by 12 months, and the pre-remedy information duty is implemented (Arts 10(2a), 13(2a), since 31.07.2026)
- [ ] Update period stated and honoured (Art 8(2) Dir (EU) 2019/770 / Art 7(3) Dir (EU) 2019/771)
- [ ] Commercial guarantee on a durable medium with the express statement that statutory rights are unaffected (Art 17(2))
- [ ] Price reduction percentages computed against the 30-day low (Art 6a Dir 98/6/EC; Case C-330/23, 26.09.2024)
- [ ] Review authenticity steps actually taken and described, or the claim removed (Annex I 23b, Art 7(6) Dir 2005/29/EC)
- [ ] No paid ranking presented as organic (Annex I 11a)
- [ ] Marketplace disclosures complete: ranking parameters, trader status, non-application of consumer law, split of obligations (Art 6a Dir 2011/83/EU)

## Terms

- [ ] No unilateral change clause without a valid reason specified in the contract (Annex (j) Dir 93/13/EEC)
- [ ] No blanket liability exclusion — a struck clause is not read down (Case C-618/10)
- [ ] No non-statutory arbitration or disadvantageous forum clause (Annex (q))
- [ ] Auto-renewal opt-out deadlines reasonable and disclosed (Annex (h))
- [ ] Cancellation no harder than signup (Art 9 Dir 2005/29/EC)
- [ ] National blacklists checked — Dir 93/13/EEC is minimum harmonisation (Art 8)

## Platform

- [ ] Tier classified in writing, and the correct micro/small relief identified — **Arts 19, 29 and 15(2) DSA are three separate provisions**
- [ ] Two distinct points of contact published: authorities (Art 11) and recipients (Art 12), the latter not relying solely on automated tools
- [ ] Non-EU provider has a designated legal representative (Art 13)
- [ ] Terms state restrictions, moderation policy, algorithmic decision-making, human review and the complaint procedure, machine-readable (Art 14)
- [ ] Notice-and-action mechanism live with receipt confirmation (Art 16)
- [ ] Statement of reasons issued for every restriction, and pushed to the Transparency Database where a platform (Art 17, Art 24(5))
- [ ] Misuse policy with examples and suspension durations in the terms (Art 23(4))
- [ ] Ads labelled; no profiling-based ads using Art 9(1) GDPR data; none to known minors (Arts 26(3), 28(2))
- [ ] Marketplace: full Art 30(1) trader dataset held and (a), (d), (e) published on the offer page (Art 30(7))
- [ ] No VLOP obligations drafted in for a non-designated service

## AI

- [ ] Inventory of AI systems with the role taken for each: provider or deployer
- [ ] Art 5 prohibited practices ruled out in writing, including emotion inference at work
- [ ] Annex III screening done; where in a category, the Art 6(3) filter assessed and documented
- [ ] Chatbot discloses AI at first interaction, inside the interface (Art 50(1), 50(5))
- [ ] Generative outputs marked machine-readably by the provider of the generating system (Art 50(2))
- [ ] Deepfake and public-interest-text disclosures where applicable (Art 50(4))
- [ ] AI literacy measures documented (Art 4)
- [ ] Compliance plan uses the post-omnibus dates: Annex III 02.12.2027, Annex I 02.08.2028, Art 50 02.08.2026
- [ ] DPIA run for any profiling or scoring feature (Art 35(3)(a) GDPR) — not replaced by the AI Act analysis

## Accessibility

- [ ] EAA scope assessed against Art 2(2) and the Art 3(30) e-commerce definition
- [ ] Microenterprise status assessed against the EAA's own Art 3(23) definition and documented; not relied on for products
- [ ] **Annex V information published in the terms or an equivalent document, in written and oral format** — not a public-sector-style accessibility statement (Art 13(2))
- [ ] No claim of a presumption of conformity from EN 301 549 under the EAA
- [ ] Keyboard-only and screen-reader walkthroughs of the main flows completed
- [ ] Contrast measured, focus visible, labels associated, errors described in text
- [ ] Notification route to national authorities on discovering non-conformity in place (Art 13(4))

## Products, data and security

- [ ] Physical products: EU responsible person identified, with postal **and electronic** address on the product or packaging (Arts 16(1), 16(3) Reg (EU) 2023/988)
- [ ] Product listings carry manufacturer details, responsible person, identifier including a picture, and warnings in the right language (Art 19)
- [ ] Marketplace: Safety Gate registration and the two- and three-working-day clocks (Art 22)
- [ ] Software or connected hardware: vulnerability reporting and coordinated disclosure live before **11.09.2026** (Reg (EU) 2024/2847)
- [ ] Business users under contract: P2B terms, 15-day change notice, statement of reasons, ranking disclosure, with the correct small-enterprise relief
- [ ] Connected products or cloud services: Data Act Chapter II duties or a documented Art 7 exemption; switching terms with the 30-day transitional period; **zero switching charges from 12.01.2027**
- [ ] NIS2 scope test against Annexes I and II and the size cap, with the **national** commencement date checked

## Dispute resolution and residue

- [ ] **Zero occurrences of any ODR-platform reference project-wide** (Reg (EU) 2024/3228; repealed with effect from 20.07.2025)
- [ ] National ADR entity named where a participation duty exists (Dir 2013/11/EU Art 13, as transposed)
- [ ] No provision of another member state's law cited
- [ ] No US-law concepts imported (CCPA notice-at-collection, "Do Not Sell", arbitration waivers)
- [ ] Image, font and content licences documented
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
- [ ] Draft marker still present wherever legal sign-off has not been confirmed

## Reporting format

Findings as a table, most severe first:

| Severity | Location | Instrument and article | Finding | Fix |
|---|---|---|---|---|
| critical / high / medium | file:line or URL | e.g. Art 8(2) Dir 2011/83/EU | what is missing or wrong | concrete step |

**Critical** means the contract fails, the processing is unlawful, or an administrative fine or injunction is realistic. That includes: tracking before consent; a wrongly labelled order button, where the consumer is simply not bound; a missing withdrawal instruction, which extends the period by twelve months; a missing withdrawal function since 19.06.2026; a missing EU responsible person for a physical product, which bars placing it on the market at all; and a live ODR link, which states a redress route that no longer exists.
