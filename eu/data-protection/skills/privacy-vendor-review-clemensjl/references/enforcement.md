# Regulatory landmines — decisions and positions with citations

Cite the decision, not the vibe. Sources marked **[P]** are the issuing body's own publication or the statutory text; **[S]** is secondary. noyb is reliable for publishing decision documents but is a party to many of these cases — treat it as secondary.

Status as at 2026-08-05.

## Google Analytics — the transfer line

| Body | Date | Reference | Holding |
|---|---|---|---|
| Austrian Datenschutzbehörde | published 12.01.2022 | 2021-0.586.257 (D155.027) | Transfer of visitor data to the US via Google Analytics unlawful. Google's contractual and organisational measures rejected — "it is not apparent to what extent [they] are effective" against FISA 702 and EO 12333. Unique identifiers still singled out the user, so **IP truncation did not make the data non-personal**. [S — noyb, publishing the decision] |
| Garante (Italy) | 09.06.2022 | **Provvedimento n. 224, doc-web 9782890**, Caffeina Media S.r.l. | Transfer to Google LLC unlawful; supplementary technical and contractual measures **insufficient** against FISA 702. Remedy: conform within **90 days** or the flows to Google LLC are suspended. [P — garanteprivacy.it] |
| IMY (Sweden) | 03.07.2023 | Audit of CDON, Coop, Dagens Industri, Tele2 | **Tele2 fined SEK 12 m, CDON SEK 300,000**, three ordered to stop. Data personal because they "can be linked with other unique data that is transferred"; no supplementary measure achieved protection "essentially corresponding to that guaranteed within the EU/EEA". [P — imy.se] |
| CNIL (France) | — | Proxy guidance, still live | Sets the conditions under which a **proxyfied** deployment can be lawful: no IP transmitted to the tool, the proxy replaces the user identifier, external referrer removed, URL parameters (UTM, internal routing) removed, fingerprinting data such as the user-agent reprocessed, no cross-site or deterministic identifiers, any other re-identifying data deleted, and the proxy itself hosted so that the data it handles is not transferred outside the EU. Expressly insufficient: "la seule modification du paramétrage des conditions de traitement de l'adresse IP ne suffit pas", and encryption is rejected as inadequate. [P — cnil.fr] |

`[[UNVERIFIED: the CNIL mise en demeure of February 2022, its follow-up and the CNIL Google Analytics Q&A — those pages have been removed from cnil.fr and no archive was reachable. Do not cite dates or figures for them.]]`
`[[UNVERIFIED: the EDPS decision on the European Parliament's COVID testing site (January 2022) — decision text, date and case number could not be retrieved from any primary source. Do not cite a case number.]]`
`[[UNVERIFIED: whether any authority has decided specifically on GA4 as opposed to Universal Analytics. None found, but the search tooling was limited — treat as "no evidence found", not a verified negative. Note that the whole enforcement wave concerned pre-GA4 deployments.]]`

Usable substitute for the same teaching point: **EDPS, 08.03.2024** — the European Commission's use of **Microsoft 365** infringed the EU institutions' data protection regulation: transfers outside the EEA without adequate safeguards, insufficient purpose specification in the Microsoft contract, and ungoverned sub-processor processing. The Commission was ordered to suspend all data flows to Microsoft and its affiliates and sub-processors in non-adequate countries by 09.12.2024. [P — edps.europa.eu] This is the benchmark for processor-contract review: purpose specification, sub-processor governance, transfer safeguards.

What the reviewer takes from the whole line:

1. **Pseudonymous online identifiers are personal data** where they single out a user. "We anonymise the IP" is not an answer.
2. **Organisational supplementary measures do not cure a legal power to compel access.** A TIA resting on a transparency report is not a TIA.
3. The DPF removed the *transfer* argument, not the *consent* argument. ePrivacy Art 5(3) and its national transposition are untouched by any adequacy decision, and CNIL's proxy guidance was never withdrawn.

## ePrivacy Art 5(3) — the technical scope

**EDPB Guidelines 2/2023 on Technical Scope of Art. 5(3) of ePrivacy Directive, Version 2.0, adopted 07.10.2024** [P]. Three criteria (information / terminal equipment / storage or access). Para 6: "It should be noted that the term used is not 'personal data', but 'information'." Para 12: the notion of information "includes both non-personal data and personal data, regardless of how this data was stored and by whom". Quoting **CJEU 01.10.2019, C-673/17 Planet49** at para 10: protection "applies to any information stored in such terminal equipment, regardless of whether or not it is personal data".

Use cases analysed: URL and pixel tracking; local processing; tracking based on IP only; intermittent and mediated IoT reporting; unique identifier. Expressly non-exhaustive.

Corollaries from the same text: read-only access needs consent even where the accessing party did not store the value (para 11, citing WP29 Opinion 9/2014 on device fingerprinting); instructing software on the device to generate and send information is storage (para 36); no minimum duration or size (para 37); purely local processing is out of scope only until the information "or any derivation of this information" leaves the device (para 44). Full detail in `device-access.md`.

## Cookie banners and dark patterns

- **Austrian Bundesverwaltungsgericht, 21.05.2026, W171 2303402-1/7E** — upheld the DSB's October 2024 finding on ORF.at: a colour-highlighted "Accept" against a less prominent "Reject" is a dark pattern; the two must be **designed equally**. Adding a quieter reject option is not enough for unambiguous consent. [S — noyb, the complainant] The Austrian authority for "refuse must be as easy and as visible as accept".
- **EDPB Binding Decision 1/2026, Art 65(1)(a) GDPR, adopted 28.05.2026, published 14.07.2026** [P] — dispute submitted by the Belgian SA concerning **Vlaamse Radio- en Televisieomroeporganisatie (VRT)**. The Belgian SA as lead authority proposed to dismiss a noyb cookie-banner complaint as an abuse of Arts 77 and 80(1); the Austrian SA objected; the EDPB found neither the objective nor the subjective component of abuse made out and **ordered the Belgian SA to decide the complaint on the merits** and submit a new Art 60(3) draft. Practical effect: procedural dismissal of NGO-driven cookie complaints is no longer available.
- **Consent-signal proposal:** the Commission's Digital Omnibus proposed an Art 88b replacing banners with an automated consent signal. The Council's 18.06.2026 position removed it; Parliament had not positioned itself and the trilogue was open. **Not law.** Do not defer a consent implementation on it.

## Consent or pay

**EDPB Opinion 08/2024, adopted 17.04.2024** [P]: confronting users with only a binary choice between consenting to behavioural advertising and paying a fee will in most cases not produce valid consent under Art 4(11) and Art 7 GDPR **for large online platforms**. Any paid alternative must be a genuine equivalent in scope, functionality and experience, and a further equivalent alternative without behavioural advertising should normally be offered.

No full guidelines have followed: the EDPB register for 2025-2026 lists only Guidelines 01/2025 (Pseudonymisation), 02/2025 (Blockchain), Recommendations 2/2025 (legal basis for user accounts on e-commerce sites), Guidelines 1/2026 (Scientific Research), 02/2026 (Anonymisation), 03/2026 (Web Scraping) and the breach-notification template. **Opinion 08/2024 remains the reference.** It is an Art 64(2) opinion addressed to large online platforms — do not over-extend it. This is a business-model question; it does not change whether a vendor's tag needs consent.

## Joint controllership for embedded third-party code — CJEU [P, CURIA press releases]

- **C-40/17 Fashion ID, 29.07.2019 (PR 99/19)** — the site operator embedding a Like button is a joint controller **only** "in respect of the operations involving the **collection and disclosure by transmission** to Facebook Ireland of the data at issue", and **not** for the processing Facebook Ireland carries out **after** transmission. Prior consent must be obtained solely for the operations it jointly controls, and each joint controller must pursue its own legitimate interest in the collection and transmission.
- **C-210/16 Wirtschaftsakademie, 05.06.2018 (PR 81/18)** — a fan-page administrator is a joint controller because it "takes part, by its definition of parameters … in the determination of the purposes and means", with no access to the underlying data. The local supervisory authority may act against both.
- **C-604/22 IAB Europe, 07.03.2024 (PR 44/24)** — the **TC String is personal data** when combined with an identifier such as the device IP, and IAB Europe is a **joint controller** for recording consent preferences in it, but **not** for processing that happens after the string is recorded unless it influenced the purposes and means. The same temporal cut as Fashion ID, applied to consent-management infrastructure.
- **C-446/21 Schrems v Meta, 04.10.2024 (PR 166/24)** — data minimisation "precludes all of the personal data obtained by a controller … collected either on or outside that platform, from being aggregated, analysed and processed for the purposes of targeted advertising **without restriction as to time and without distinction as to type of data**". On Art 9: a public statement about one's own sexual orientation may make *those* data manifestly public, but "that fact alone does not authorise the processing of **other** personal data relating to that data subject's sexual orientation". The press release expressly discusses cookies, social plug-ins and pixels, and notes that merely loading a page containing a plug-in suffices to transmit cookies, the URL and log data including the IP.
- **C-311/18 Schrems II, 16.07.2020 (PR 91/20)** — Privacy Shield invalid; SCCs valid but the exporter must assess third-country law and suspend where equivalence fails.
- **C-394/23 Mousse, 09.01.2025 (PR 2/25)** — collecting a customer's title is not "objectively indispensable" for contract performance; legitimate interest fails where the interest was not disclosed at collection, where processing exceeds strict necessity, or where the data subject's rights prevail.

Applied to the Meta pixel: Meta's own Business Tools Terms allocate **joint controllership under Art 26** for event data from user interactions on the advertiser's site (see `vendors.md`). A notice describing Meta as a processor contradicts the platform's own terms.

## Meta Pixel and special-category data — the most useful recent precedent

**IMY (Sweden), 03.07.2025** [P — imy.se] — fines against **Apoteket AB (SEK 37 m)** and **Apohem AB (SEK 8 m)** for transferring **health data** to Meta through a Meta Pixel sub-feature: purchases of over-the-counter medicines tied to specific conditions, self-testing kits, STI treatments and sex toys. Framed as a failure to implement appropriate technical and organisational measures (Art 32) over Art 9 data, with IMY stressing that the companies "did not have the necessary procedures in place to detect these deficiencies themselves."

This is the case to cite when a reviewer is told a pixel "only sends page views". A page view is Art 9 data when the page is `/pharmacy/hiv-self-test`. It also establishes that **failing to detect your own tag configuration** is itself the breach.

## Remotely loaded fonts

- **LG München I, Endurteil 20.01.2022, 3 O 17493/20** [P — gesetze-bayern.de] — dynamic embedding transmits the visitor's dynamic IP to Google without consent, infringing the general right of personality, and is unjustified because "das Angebot von Google Fonts auch genutzt werden kann, ohne dass beim Aufruf der Webseite eine Verbindung zu einem Google-Server hergestellt wird." **The bases are split**: injunction on § 823(1) with § 1004 BGB by analogy, information on Art 15 GDPR, and the **EUR 100 damages on Art 82(1) GDPR** — not § 823. EUR 100 per claimant, not per visitor. `[[UNVERIFIED: whether the judgment became final]]`
- **The mass warning-letter wave collapsed.** **LG München I, 30.03.2023, 4 O 13063/22** [P — gesetze-bayern.de] — note the case number, **not** "4 HKO 13063/22" — was a **negative declaratory action brought by a warned site operator against the warning lawyer**, holding he had neither an injunction nor a damages claim: the site had been accessed by an automated crawler so no human was affected, and, under § 242 BGB, "Wer einen Verstoß gegen sein Persönlichkeitsrecht gezielt provoziert, um daraus hernach Ansprüche zu begründen, verstößt gegen das Verbot selbstwidersprüchlichen Verhaltens." The court noted at least 100,000 letters had been sent.
- **Austria has its own line.** A 2022 wave charged EUR 190 per site; the WKO ran a test case. The **Landesgericht für Zivilrechtssachen Wien, 30.12.2025** dismissed the claim: systematic warnings sent to generate profit are abusive, the GDPR gives no general preventive injunction, damages need concrete demonstrable harm, and the claimant had accessed the sites automatically to provoke the breach. **Not final; appeal announced.** [S — wko.at, updated 13.01.2026] `[[UNVERIFIED: Geschäftszahl — not published anywhere reachable]]`
- **The Austrian DSB reached a narrower conclusion than the German courts.** In an own-initiative examination concluded in November 2023 it found that dynamic embedding does **not in all cases** transmit to Google servers in the US — it depends on the responding server's location, so the analysis is case-by-case — that Fonts data is not linked to a Google account or used for advertising, and that **no unlawful processing by Google LLC was established**; only information-duty shortcomings were criticised. **No Bescheid, no fine.** [S — the DSB's own publication page is dead; only a law-firm rendering is reachable] `[[UNVERIFIED: GZ]]`
- **Damages threshold: CJEU C-300/21 UI v Österreichische Post, 04.05.2023 (PR 72/23)** [P] — "Der bloße Verstoß gegen die DSGVO begründet keinen Schadensersatzanspruch": damage, infringement and causation must be shown cumulatively; but there is **no de minimis threshold** for non-material damage; Art 82 is compensatory, not punitive.

**The reviewable point does not depend on any of it: self-hosting the font files removes the transfer, the Art 5(3) question and the notice entry in one step.** The same applies to icon fonts, CSS frameworks and JS libraries loaded from public CDNs.

## US pixel litigation — a separate reason to gate the same tags

**Statute** [P — leginfo]. Cal. Penal Code **§ 638.51(a)**: "a person may not install or use a pen register or a trap and trace device without first obtaining a court order". The textual hook is in the definitions: **§ 638.50(b)** defines a pen register as "a **device or process** that records or decodes dialing, routing, addressing, or signaling information", and **§ 638.50(c)** defines a trap and trace device the same way. **§ 631(a)** adds the fourth prong — "or who aids, agrees with, employs, or conspires with any person or persons to unlawfully do" the foregoing — which is what reaches the site operator that installs the vendor's tag.

- **Greenley v. Kochava, Inc.**, S.D. Cal., **27.07.2023**, No. 3:22-cv-01327-BAS-AHG, 684 F. Supp. 3d 1024 [P] — "The definition is specific as to the type of data a pen register collects … but it is vague and inclusive as to the form of the collection tool — 'a device or process.'" Software and SDKs can therefore be pen registers. A § 631 contents claim over search terms and in-app activity also survived.
- **Javier v. Assurance IQ, LLC**, 9th Cir., **31.05.2022**, No. 21-16351, **unpublished**, 2022 WL 1744107 [P] — "we conclude that the California Supreme Court would interpret Section 631(a) to require the **prior consent of all parties** to a communication." This is the sentence that makes a pre-consent tag a CIPA problem.
- **Mirmalek v. Los Angeles Times**, N.D. Cal., 12.12.2024 — followed Greenley; IP-collecting trackers can be pen registers. **No appellate court has rejected Greenley, and no California appellate court has ruled on the pen-register theory at all** — it remains an untested district-court line.
- **Vita v. New England Baptist Hospital**, Mass. SJC, **24.10.2024, SJC-13542, 494 Mass. 824** [P] — the Massachusetts Wiretap Act's "communication" is ambiguous as applied to web browsing, a concept historically centred on "person-to-person conversations and messaging"; under the rule of lenity the claims failed. Wendlandt J. dissenting. The counterweight to the California line.
- **Cook v. GameStop**, 3d Cir., **07.08.2025, precedential** — no Article III standing for interception of non-sensitive browsing: "[M]ost of us understand that what we do on the Internet is not completely private." Pennsylvania is now the harder forum.
- **Briskin v. Shopify**, 9th Cir. **en banc, 21.04.2025**, 135 F.4th 739 — personal jurisdiction over an out-of-state processor in California. Jurisdictional, but the most consequential published tracker ruling of 2025 for vendors.
- **California SB 690 has been materially rewritten.** As amended in the Assembly on **02.07.2026** it strikes the earlier "commercial business purpose" exemption; what remains amends Penal Code § 637.2 so that an action against a private actor for a **§ 638.51** violation arising from a website or app "may be brought under this section **only by the Attorney General**". It targets the private right of action for the pen-register theory specifically, not CIPA generally. **Not enacted as at 2026-08-05**; last action 02.07.2026, re-referred to Assembly Appropriations, hearing 05.08.2026 [P — leginfo].
- `[[UNVERIFIED: filing and demand-letter volumes. No citable publisher figure could be retrieved. A self-run docket count of federal filings mentioning the statute is a floor only, because most of these cases are filed in Los Angeles Superior Court and demand letters never appear on a docket.]]`

Why this belongs in a GDPR skill: the mitigation is identical. A tag that does not load before an affirmative opt-in captures nothing from a US visitor either. Where the product has US traffic, gate for both reasons and record both.

## E-mail tracking pixels — new and directly actionable

**CNIL recommendation on tracking pixels in electronic mail, adopted 14.04.2026; FAQ published 22.07.2026** [P — cnil.fr]. Applies Art 82 loi Informatique et Libertés (the French ePrivacy transposition) to e-mail pixels: **consent is required by default**. Narrow exemptions: (a) deliverability pixels strictly limited to detecting inactive recipients, where the e-mail was explicitly requested, only the last-open date is collected, and inactive recipients are removed or their frequency reduced; (b) security pixels protecting authentication flows such as password-reset mails; (c) mixed-purpose pixels may pursue both. Transitional rule: for addresses collected before 14.04.2026, three months to inform recipients of their right to object. Obligations: clear purpose information, easy withdrawal, deletion on withdrawal, documented compliance.

Newsletter and transactional e-mail tooling is squarely in scope. Cross-check the open-tracking default recorded in `vendors-saas.md` — some vendors ship it off, others on.

## Transfers — the current pressure point

**US Supreme Court, 29.06.2026, Trump v. Slaughter** held that the FTC cannot be constitutionally independent. noyb reports the 2023 DPF adequacy decision relies on the "independent" FTC 259 times, has written to the Commission asking for withdrawal, and has announced a CJEU annulment action [S — noyb]. The reasoning also reaches the PCLOB and the Data Protection Review Court, the bodies most US transfer impact assessments cite for redress. No Commission or EDPB response is documented. Consequence: US vendors relying **solely** on the DPF should be recorded with a fallback mechanism. See `transfers.md`.

`[[UNVERIFIED: General Court, T-354/22 Bindl v Commission, reportedly 08.01.2025, reportedly awarding EUR 400 for transmitting a visitor's IP to Meta in the US via a "Sign in with Facebook" button on a Commission site. Could not be verified from CURIA or any secondary source. Do not cite the figure.]]`

## Current EDPB output to check before a review

- **08.07.2026** — **Guidelines 02/2026 on Anonymisation** (three-criterion test: no singling out of a record, no linkability, no inference; contextual and simplified approaches) and **Guidelines 03/2026 on Web Scraping in the Context of Generative AI** (the GDPR applies wherever personal data are collected or stored; prefer reliable sources; measures aligned with data minimisation), plus **Guidelines 02/2025 on Blockchain v2.0 final**. Both new guidelines open for consultation to **30.10.2026** — read them for an AI or analytics review, but do not cite them as settled.
- **10.06.2026** — common personal data breach notification template, with predefined options to make Art 33 notifications complete and comparable. **Not mandatory on adoption**; consultation ran to 05.08.2026, after which the EDPB decides the implementation timeline.
- Also adopted and directly relevant: **Guidelines 01/2025 on Pseudonymisation**, **Guidelines 3/2025 on the Interplay Between the DSA and the GDPR**, **Recommendations 2/2025 on the Legal Basis for User Accounts on E-commerce Websites**.

Check `edpb.europa.eu/news/news_en` at the start of any review; the EDPB adopts guidance faster than any vendor file can track.

## Checkpoints

- [ ] Every decision cited with body, date and reference — not "the DPAs have said"
- [ ] Primary and secondary sources distinguished; advocacy sources labelled
- [ ] Anything marked `[[UNVERIFIED]]` here resolved against a primary source before it reaches a deliverable
- [ ] EDPB news page checked at the start of the review
- [ ] Where a pixel can see a URL revealing health, finance or sexuality, the Apoteket/Apohem analysis applied before approval
- [ ] Where the product has US traffic, the CIPA exposure recorded alongside the GDPR finding
- [ ] For e-mail tooling, the open-tracking default checked against the CNIL pixel recommendation
- [ ] Remotely loaded assets checked for a self-hosting alternative before any consent gate is designed around them
