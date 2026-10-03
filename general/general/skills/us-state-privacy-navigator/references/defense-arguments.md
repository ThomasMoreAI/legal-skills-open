# Defense Arguments — What Controllers Can Argue When Challenged

**Purpose.** When AG enforcement, regulatory inquiry, or private litigation lands, the analytical question shifts from "how do we comply" to "what's our story." This reference catalogs the strongest, second-strongest, and unsuccessful defenses controllers have raised under US state privacy laws — including the cases or theories that supported or rejected each argument. Use this to:

1. Stress-test a compliance position before adopting it (if the defense for a borderline practice is weak, the practice itself is not defensible).
2. Frame the litigation-defense story in a memo so the GC understands not only the rule but the recovery posture.
3. Anticipate AG counter-arguments before they are made.

> **Caveat.** State privacy law's case-law base is thin — most matters settle without published rulings, and the federal-court decisions interpreting state privacy statutes are sparse. Where the analysis turns on adjacent caselaw (CIPA wiretap rulings, BIPA scope decisions, FTC § 5 frameworks), the analogy is identified expressly. Don't cite an adjacent doctrine as if it directly governed.

## Organization

Defenses are grouped by the violation theory most commonly invoked. For each:

- **The defense.** A short statement.
- **Strength.** Strong / Moderate / Weak / Failed (where tested).
- **Doctrinal basis.** Statutory, regulatory, or case-law support.
- **Counter-arguments.** What the AG or plaintiff will raise.
- **Operational fit.** When the defense is plausible vs. when it isn't.

---

## 1. Applicability defenses — "the law doesn't apply to us"

### 1.1 Threshold not met

**Defense:** The entity does not meet the applicable state's threshold (revenue, consumer count, sale-revenue percentage).

**Strength:** Strong — when the underlying numbers are documented and conservative.

**Doctrinal basis:** Each statute's threshold provision (e.g., Cal. Civ. Code § 1798.140(d); Va. Code § 59.1-575).

**Counter-arguments:** AGs may probe (a) consumer-counting methodology — whether all natural persons are counted, including employees and B2B in CA; (b) revenue scope — whether US-only or global is the proper measure; (c) joint-venture / affiliate aggregation under CCPA § 1798.140(d)(2)–(3); (d) prior-year vs. current-year data.

**Operational fit:** Document the threshold analysis with calculation methodology and source data preserved. A retroactive defense reconstructed under deadline pressure is much weaker than a contemporaneously-documented analysis.

### 1.2 Sectoral exemption — entity-level

**Defense:** The entity is exempt from the comprehensive privacy law because it is HIPAA-covered, GLBA-covered, FCRA-covered, or otherwise sectorally exempted at the entity level.

**Strength:** Strong — where the exemption is entity-level and the state recognizes entity-level exemptions.

**Doctrinal basis:** Each statute's exemption provisions (e.g., Va. Code § 59.1-576; UCPA § 13-61-102; TIPA § 47-18-3202).

**Counter-arguments:** (a) The exemption may be data-level rather than entity-level, in which case non-sectoral data remains in scope (CA's HIPAA exemption is data-level only, not entity-level — see CCPA Regs § 7000 and Cal. Civ. Code § 1798.146); (b) Mixed-purpose entities may not qualify as primarily sectoral; (c) GLBA-affiliate exemption depends on the affiliate's own status.

**Operational fit:** Strong defense for full-line HIPAA covered entities, GLBA financial institutions, and credit reporting agencies operating in their core functions. Weak when the entity's privacy-relevant data flows are outside the sectoral framework (e.g., a hospital's marketing website or a bank's prospect-data lead generation).

### 1.3 Non-profit exemption

**Defense:** The entity is a non-profit and is exempt from the state's comprehensive privacy law.

**Strength:** Strong in most states; weak in CA, OR, MD (no general non-profit exemption); MN partial; NJ partial.

**Doctrinal basis:** Most state acts (VA, CT, UT, TN, KY, IA, IN, NJ partial, TX, NE, MT, NH, RI) define "controller" as a person who conducts business for-profit or otherwise distinguishes for-profit. Non-profits are excluded from the definition.

**Counter-arguments:** California's CCPA covers any qualifying business, including (post-CPPA expansion) certain non-profit-adjacent activities. Oregon's OCPA covers non-profits effective July 2025. Maryland MODPA covers non-profits.

**Operational fit:** Non-profits with national consumer reach (e.g., universities, large healthcare systems with non-profit status) often have CA exposure even with non-profit status elsewhere.

### 1.4 Employment / B2B carve-out

**Defense:** The data at issue is employee, applicant, contractor, or B2B contact data, which is not "consumer" data under the state's act.

**Strength:** Strong — except in California, where employees, applicants, and B2B contacts ARE within CCPA scope.

**Doctrinal basis:** Va. Code § 59.1-575 ("consumer" excludes commercial or employment context); analogous provisions in 18 other states. Cal. Civ. Code § 1798.140(i) covers employees and B2B since the AB-1281 sunset.

**Counter-arguments:** California is the major exception. Mixed personal/employment data flows may not cleanly bifurcate. For applicants, the line between recruitment and an established commercial relationship is sometimes unclear.

**Operational fit:** Critical in HR-tech, B2B SaaS, and recruiting; the carve-out shrinks the compliance footprint dramatically outside California.

---

## 2. "Sale" / "sharing" / "targeted advertising" defenses

### 2.1 No sale because no monetary consideration

**Defense:** The data exchange does not constitute a "sale" because no money or other valuable consideration changed hands.

**Strength:** **Failed.** The CA AG has consistently rejected this. *In re Sephora* (2022) and *People v. DoorDash* (2024) establish that data-for-data exchanges, marketing-cooperative exchanges, and adtech-driven exchanges constitute sale even without direct monetary payment.

**Doctrinal basis:** Cal. Civ. Code § 1798.140(ad) defines "sell" to include exchange for "monetary or other valuable consideration." "Other valuable consideration" is read broadly.

**Counter-arguments:** AGs cite Sephora and DoorDash as direct authority. Plaintiffs add the public articulation that "free" pixel deployments still represent value exchange.

**Operational fit:** Do not rely on this defense for typical adtech, marketing-cooperative, or audience-data exchanges. It has been litigated to ground.

### 2.2 Service-provider / processor exception (CCPA § 1798.140(ag))

**Defense:** The disclosure is to a service provider / processor for a purpose specified in writing in the contract; it is not a "sale" or "sharing" because it falls within the service-provider exception.

**Strength:** Strong when the contract actually meets CCPA Regs § 7050–7053 specificity, the recipient operates within those purposes, and the service-provider relationship is documented.

**Doctrinal basis:** Cal. Civ. Code § 1798.140(ag); 11 CCR §§ 7050–7053. *In re Honda* (2024) addresses processor-contract specifics.

**Counter-arguments:** *Honda* establishes that a processor contract that does not contain the § 7051 required terms does not establish service-provider status. Stale or boilerplate contracts fail. The recipient's actual conduct must match the contract's written purpose; if the recipient uses data for its own commercial purposes (e.g., model training on customer data), the exception is lost.

**Operational fit:** Best when DPAs are current, restrictive, and audited. Worst when DPAs are old, generic, or when the vendor's business model (e.g., adtech, data enrichment, "AI" services) inherently involves repurposing data.

### 2.3 Cross-context behavioral advertising vs. contextual advertising

**Defense:** The ad targeting is *contextual* (based on the page content) rather than *cross-context behavioral* (based on the consumer's activity across non-affiliated services); contextual advertising is not regulated as "sharing" or "targeted advertising."

**Strength:** Strong when actually contextual.

**Doctrinal basis:** Cal. Civ. Code § 1798.140(j)(2) (cross-context behavioral advertising definition); analogous "targeted advertising" definitions in other states' acts excluding contextual ads.

**Counter-arguments:** The definitional line is narrow. If the ad serving uses any consumer-identifier-based audience targeting (lookalike audiences, retargeting, custom audiences), it is cross-context behavioral. Most "contextual" deployments today integrate identifier-based targeting at some layer.

**Operational fit:** Defensible for true contextual placements (e.g., Google Search ads on keyword match without persistent-identifier-based targeting). Indefensible for retargeting, audience-based campaigns, or any deployment that fires Meta/Google/TikTok pixels.

### 2.4 De-identified / aggregate data exception

**Defense:** The data shared is de-identified or aggregate and not "personal information" under the statute.

**Strength:** Moderate — depends on the rigor of de-identification.

**Doctrinal basis:** Cal. Civ. Code § 1798.140(m), (z) (de-identified information exclusion); analogous exceptions in other states.

**Counter-arguments:** "De-identified" requires technical, contractual, and operational safeguards. CCPA requires the business to (a) take reasonable measures to ensure data cannot be re-identified, (b) publicly commit to maintain and use only de-identified information, (c) contractually obligate recipients to comply. AGs scrutinize whether the data could be re-identified using auxiliary information available to the recipient.

**Operational fit:** Strong defense for properly de-identified data flows (research datasets, statistical reporting, certain internal analytics). Weak where the dataset retains hashed identifiers, IP addresses, or device fingerprints that could be re-identified.

---

## 3. Sensitive data defenses

### 3.1 Processing is solely for service delivery (CA limit-use § 7027(m))

**Defense:** Sensitive PI is used only for purposes within the CCPA Regs § 7027(m) safe harbor (security, fraud prevention, transient use, performing services, verification of quality), so the limit-use right and "Limit Use" link are not triggered.

**Strength:** Strong when the actual practices are confined to those purposes.

**Doctrinal basis:** 11 CCR § 7027(m).

**Counter-arguments:** AGs probe whether the controller's actual data uses extend beyond the safe harbor — particularly any use for personalization, marketing, profiling, or product improvement that is not narrowly tied to the consumer's specific request.

**Operational fit:** A defensible posture for many B2C controllers. The privacy notice should explicitly state that sensitive PI is used only for § 7027(m) purposes and the data flow inventory should support that claim.

### 3.2 Consent was specific and granular

**Defense:** Opt-in consent was obtained in compliance with state-specific consent standards (specific, informed, unambiguous, freely given, revocable).

**Strength:** Strong when the consent record is timestamped, granular per category and purpose, and revocable as easily as given.

**Doctrinal basis:** Per-state consent provisions (e.g., Va. Code § 59.1-575 (consent definition); CO 4 CCR § 904-3 § 7).

**Counter-arguments:** Pre-checked boxes; bundled consent (e.g., "by using our service you consent to all the things"); friction asymmetry between opt-in and opt-out flows; lack of consent record. CO Rules § 7 expressly cover dark patterns. Sephora-style enforcement extends UCL theories to consent failures.

**Operational fit:** Strongest when consent infrastructure was designed against CO Rules § 7 (the most prescriptive standard) and consent records are retained.

### 3.3 Data is not sensitive under the statute's definition

**Defense:** The data category at issue does not fall within the state's enumerated sensitive-data list.

**Strength:** Moderate — definitions vary; some are quite narrow.

**Doctrinal basis:** Each state's sensitive-data definition (e.g., Cal. Civ. Code § 1798.140(ae); Va. Code § 59.1-575).

**Counter-arguments:** Most states' definitions include "data revealing" or "data inferring" the protected category — meaning data that allows the inference of (e.g.) health status is sensitive even if the data is not formally a medical record. WA MHMDA's "consumer health data" definition is the broadest and reaches inferred health interest.

**Operational fit:** Defensible for clearly non-sensitive data. Weak where the data could support inferences (e.g., browsing data on health-related sites, fitness tracking, location near certain venues).

---

## 4. Rights-request defenses

### 4.1 Reasonable verification was required

**Defense:** The verification standard applied was reasonable in proportion to the sensitivity of the data and the risk of fraudulent requests.

**Strength:** Moderate — must not over-verify.

**Doctrinal basis:** 11 CCR §§ 7060–7062.

**Counter-arguments:** *In re Honda* establishes that requiring more verification information than necessary IS a violation. The CCPA Regs prohibit requiring sensitive PI as part of verification when the business does not already have it. Verification cannot be a de facto access barrier.

**Operational fit:** Documented verification procedures calibrated to data sensitivity, with multiple acceptable methods, are defensible. Single-method or excessive-information verification practices fail.

### 4.2 Statutory exception to deletion

**Defense:** Deletion was declined because a statutory exception applies — necessity to complete a transaction; fraud / security; legal obligation; another consumer's right; internal use aligned with consumer expectations; legal compliance.

**Strength:** Strong when narrowly invoked and documented per data element.

**Doctrinal basis:** Cal. Civ. Code § 1798.105(d); analogous provisions across states.

**Counter-arguments:** Blanket exception claims fail. AGs require element-level justification — "the consumer's billing data is retained for 7 years to comply with tax record-keeping" is defensible; "we keep all consumer data for fraud prevention" is not.

**Operational fit:** Strong when the controller has a documented deletion exception map per data element with the specific statute or business reason cited.

### 4.3 Data is not "personal" or has been de-identified

**Defense:** The data does not fall within the personal-information definition at the time of the request, having been de-identified or aggregated.

**Strength:** Moderate — and only if de-identification standards are met.

**Doctrinal basis:** Same as 2.4 above.

**Counter-arguments:** Same as 2.4. AGs are skeptical of "de-identification" claims that retain pseudonymous identifiers.

**Operational fit:** Useful narrowly — specific data flows that are genuinely de-identified can be excluded from rights-request response.

### 4.4 Request was manifestly unfounded or excessive

**Defense:** The request was manifestly unfounded, excessive, or repetitive, and was declined or charged a fee on that basis.

**Strength:** Weak unless documented carefully.

**Doctrinal basis:** Cal. Civ. Code § 1798.130(a)(2)(C); analogous provisions.

**Counter-arguments:** AGs read this exception narrowly. Pattern of similar requests from one consumer, requests that are technically impossible, or requests that would require the disclosure of trade secrets are the legitimate cases. "Inconvenient" or "broad" is not "manifestly unfounded."

**Operational fit:** Use sparingly. Document the specific basis for declination per request. Better practice is to fulfill in the form requested even when burdensome.

---

## 5. Wiretap / pixel / session-replay defenses (adjacent doctrine)

### 5.1 Party exception — operator is a "party" to the communication, not a wiretapper

**Defense:** Under CIPA § 631, the operator is a *party* to the communication with its own users; the third-party tracker assists the party's own data processing and is therefore not an unauthorized interception.

**Strength:** Mixed — district courts split.

**Doctrinal basis:** *Rogers v. Ulrich* (Cal. App. 1975) (party exception to § 631); subsequent CIPA case law.

**Counter-arguments:** Plaintiffs distinguish "party" from third-party-as-tool. Courts have held that adtech vendors processing data for their own commercial purposes (rather than as a vendor of the operator) are not within the party exception. The line turns on whether the vendor uses the data for its own purposes.

**Operational fit:** Defense is plausible when the third-party vendor is contractually limited and operationally a vendor. Weak when the vendor (e.g., Meta) uses pixel data for its own audience modeling.

### 5.2 Consent — privacy notice authorized the tracking

**Defense:** Consumers consented to the tracking via the privacy notice and continued use of the service.

**Strength:** Weak under CIPA's heightened "all parties" consent standard.

**Doctrinal basis:** Cal. Penal Code § 631.

**Counter-arguments:** CIPA requires explicit consent of all parties to the communication. Continued-use boilerplate does not satisfy CIPA's standard. Meaningful consent requires an affirmative action specific to the wiretap-equivalent activity.

**Operational fit:** Generally a losing argument. Better posture: implement granular CMP consent, deploy pixels only after consent, or remove the pixel.

### 5.3 The pixel does not capture content

**Defense:** The pixel only captures metadata (URLs visited, button clicks) and not the "content" of communications protected by CIPA § 631.

**Strength:** Mixed — some courts have credited the argument; others have not.

**Doctrinal basis:** § 631 distinguishes "contents of any message" from non-content metadata.

**Counter-arguments:** Plaintiffs argue that URL paths, search queries, and form inputs reveal content. Healthcare-portal cases (*Doe v. Meta*) treat patient-portal interactions as content.

**Operational fit:** A defense to consider when the deployment is genuinely metadata-only. Weak when URLs reveal sensitive content (e.g., specific medication names, search queries).

### 5.4 VPPA — transmitted information is not "personally identifiable information" (the Solomon defense)

**Defense:** The information transmitted via the Pixel does not constitute "personally identifiable information" under VPPA § 2710(a)(3) because the strings of code (Facebook ID + URL) would not "readily permit an ordinary person to identify a specific individual's video-watching behavior."

**Strength:** Strong in the Second Circuit, Third Circuit, and Ninth Circuit (which apply the "ordinary person" standard); weaker in the Sixth Circuit (which applies "reasonable foreseeability"). Active circuit split.

**Doctrinal basis:** *Solomon v. Flipps Media, Inc.*, No. 24-1199 (2d Cir. May 1, 2025), en banc denied July 28, 2025; *Hughes v. NFL*, companion case; the court itself observed that *Solomon* "effectively shut the door for Pixel-based VPPA claims" in the Second Circuit. *Salazar v. Paramount Global* (6th Cir.) takes the opposite view — likely candidate for Supreme Court review.

**Counter-arguments:** Plaintiffs argue (a) the Sixth Circuit's "reasonable foreseeability" standard governs in their forum; (b) the technical specifics of the deployment matter — if the transmission includes human-readable PII (email, name) along with the video identifier, *Solomon* doesn't apply; (c) the Second Circuit's *Salazar v. NBA* still gives an expansive read in some configurations.

**Operational fit:** Strong defense for Meta-Pixel-only deployments where transmitted data is opaque code. Weakens when the deployment also transmits human-readable subscriber information. Forum selection matters: filing or removing to a Second/Third/Ninth Circuit forum where possible substantially improves outcomes. Many plaintiffs are now electing the Sixth Circuit to avoid *Solomon*'s reach. Defendants should also evaluate the underlying state-law theories (CIPA, state wiretap, MHMDA, state UDAP) that remain viable even where VPPA is foreclosed.

### 5.5 VPPA — defendant is not a "video tape service provider"

**Defense:** Defendant does not engage in the rental, sale, or delivery of "prerecorded video cassette tapes or similar audio visual materials" within the meaning of VPPA § 2710(a)(4).

**Strength:** Mixed — circuits divide on whether websites that incidentally host video content qualify.

**Doctrinal basis:** § 2710(a)(4); *Salazar v. NBA* (2d Cir. 2024) (broad construction); *Vizio* settlement (different posture but informative).

**Counter-arguments:** Plaintiffs read "similar audio visual materials" expansively to include any streaming or downloadable video. Most defendants with substantial video content lose this argument at motion to dismiss.

**Operational fit:** Best for sites where video is genuinely incidental (e.g., a single embedded explainer video on a primarily textual product page). Weak for media, education, or entertainment sites with substantial video catalogs.

### 5.6 VPPA — plaintiff is not a "subscriber" or "consumer"

**Defense:** Plaintiff did not pay for or formally subscribe to the service and therefore is not a "consumer" within § 2710(a)(1).

**Strength:** Mixed — some courts require payment; some do not.

**Doctrinal basis:** *Yershov v. Gannett Satellite Info. Network* (1st Cir. 2016) (broad reading of subscriber); *Ellis v. Cartoon Network* (11th Cir. 2015) (narrower reading).

**Counter-arguments:** Plaintiff may argue subscription via account creation, newsletter signup, or app installation.

**Operational fit:** Useful when the user accessed content as an unregistered visitor without account creation. Weak where any account or profile was created.

---

## 6. Affirmative defenses — privacy program defensibility

### 6.1 NIST Privacy Framework alignment (TIPA affirmative defense)

**Defense:** The controller maintains a privacy program documented to NIST Privacy Framework standards; this provides an affirmative defense under TIPA.

**Strength:** Strong in TN; supportive in other states' penalty determinations.

**Doctrinal basis:** Tenn. Code § 47-18-3213(c) (affirmative defense); other states consider documented privacy programs in penalty assessment.

**Counter-arguments:** The program must be actually implemented and maintained, not merely documented. Recent updates and evidence of operationalization are required.

**Operational fit:** A documented NIST-PF-aligned program is a high-leverage compliance investment — the marginal cost is modest, and the defensibility benefit is substantial across states.

### 6.2 Substantial compliance

**Defense:** The controller has a comprehensive privacy program and substantially complied with the statute; minor or technical gaps should not trigger penalty exposure.

**Strength:** Moderate — supportive in penalty assessment but not a complete defense.

**Doctrinal basis:** Most state acts grant the AG discretion in penalty assessment.

**Counter-arguments:** Penalties remain available for any violation; the question is the magnitude.

**Operational fit:** A privacy program with documented governance, training, and incident response demonstrates good-faith effort. AGs uniformly indicate that programs of this kind reduce penalty exposure even when violations occur.

### 6.3 Cooperation and prompt remediation

**Defense:** Upon learning of the alleged violation, the controller promptly cooperated with the AG, remediated, and provided full disclosure.

**Strength:** Moderate — never a complete defense but consistently reduces penalty exposure.

**Doctrinal basis:** AG enforcement discretion.

**Counter-arguments:** Cooperation cannot cure underlying systemic deficiencies that AGs view as evidence of broader program failure.

**Operational fit:** Always preserve the cooperation posture. Volunteer remediation; attest to fixes; provide documentation. Settlement leverage with cooperative controllers is materially better than with adversarial ones.

---

## 7. Constitutional / preemption defenses

### 7.1 First Amendment — commercial speech protection

**Defense:** The challenged practice is protected commercial speech under the First Amendment; the privacy law's restrictions are content- or viewpoint-based and fail intermediate scrutiny.

**Strength:** Strong only in narrow circumstances. Used successfully in *NetChoice v. Bonta* (challenging CA's AB-2273 / Age-Appropriate Design Code) — preliminary injunction granted on commercial-speech grounds.

**Doctrinal basis:** *Sorrell v. IMS Health* (2011) (commercial speech protection for data restrictions); *Central Hudson* test.

**Counter-arguments:** Most state privacy laws restrict commercial *conduct* (data processing) rather than *speech*; commercial-speech doctrine generally inapplicable to data-flow regulation. AGs distinguish AB-2273 (which restricted *content* available to children) from comprehensive privacy laws (which regulate *processing*).

**Operational fit:** Narrow. Don't rely as a primary defense; potentially relevant as one element of a multi-pronged challenge to a specific provision.

### 7.2 Federal preemption

**Defense:** Federal law preempts the state privacy provision (e.g., COPPA, FCRA, GLBA, CAN-SPAM, ECPA).

**Strength:** Narrow — federal preemption is limited and most state privacy laws are designed around it.

**Doctrinal basis:** Express preemption clauses where they exist (e.g., FCRA's preemption of state credit reporting; COPPA's preemption of state-level rules conflicting with COPPA).

**Counter-arguments:** State acts generally include savings clauses for federal sectoral law. Preemption of consumer privacy rights is limited.

**Operational fit:** Useful for the specific data flows that fall within a federal sectoral framework; not a global defense to state privacy law applicability.

### 7.3 Dormant Commerce Clause

**Defense:** The state privacy law unconstitutionally burdens interstate commerce.

**Strength:** Generally Failed. Courts have rejected DCC challenges to state privacy laws because the laws regulate the processing activities directed at the state's residents, not interstate commerce as such.

**Doctrinal basis:** *Pike v. Bruce Church* balancing test; *Healy v. Beer Inst.* extraterritoriality.

**Counter-arguments:** Most state privacy statutes apply by residency of the consumer, not residence of the controller; this avoids the extraterritoriality concern.

**Operational fit:** Not a viable defense; cited here only because it occasionally surfaces in motion practice.

---

## 8. Litigation-strategy defensive framing

When challenged, the most successful defensive postures combine substantive and procedural elements:

1. **Lead with the documentation.** Show the privacy program, the data inventory, the DPAs, the rights-request log. AGs settle more favorably with documented controllers than undocumented ones.
2. **Surface the cure-period (where available) immediately.** Even where the cure period has sunset, AGs retain discretion and reward early remediation.
3. **Distinguish the specific allegation from general program adequacy.** "Yes, this one form was outdated; here is the rest of our compliant program" reframes the matter.
4. **For private actions, raise standing and damages early.** CIPA, BIPA, and CCPA-PRA cases turn on whether the plaintiff has Article III injury and statutorily-cognizable damages. *TransUnion v. Ramirez* (2021) tightened the federal-court standing analysis.
5. **For PRA actions, raise the statutory basis carefully.** CCPA's PRA is limited to data-breach failures (§ 1798.150). Most CCPA-related class actions try to bootstrap UCL § 17200; UCL standing requires economic injury and is mixed.
6. **For pixel/wiretap class actions, attack class certification.** Individual consent inquiries often defeat predominance.

---

## 9. Defenses that are usually weak (avoid relying)

- "We're a small business" — most state thresholds already reflect this; below-threshold is the defense (#1.1), not an excuse to ignore the law if applicable.
- "We didn't know" — actual knowledge for minor data is a sliding standard; lack of knowledge does not excuse other violations.
- "Industry practice" — what other companies do is not a defense; AGs may treat widespread non-compliance as a motivating reason for enforcement priority.
- "The privacy notice covered it" — for sensitive data, sale, profiling, and minor data, notice is insufficient where consent or opt-in is required.
- "The user didn't object" — most state rights are opt-out (or opt-in for sensitive data); silence does not establish consent.
- "We use a vendor for that" — controllers retain liability for processor conduct; the vendor's existence is not a defense.
- "It was a third-party error" — liability for processor conduct flows to the controller; downstream-vendor errors are within the controller's accountability.
