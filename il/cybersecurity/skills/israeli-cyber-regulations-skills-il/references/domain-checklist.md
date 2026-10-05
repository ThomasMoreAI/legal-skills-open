# Domain Coverage Checklist, israeli-cyber-regulations

Generated 2026-08-26 (v1.3.0 cycle). This skill had NO domain-checklist before
this cycle, which is part of why a repealed directive survived as the skill's
centrepiece: there was no artifact enumerating what the domain must cover, so
every gate reviewed the skill against itself.

**The drift class for this skill is regulatory reform (type D): an entire regime
can be replaced by one circular while nothing in the text looks stale.** The
mechanical gates are near-useless here. The evidence verifier extracted **0 facts
and 6 URLs** from this skill on both the pre-edit and post-edit runs, because the
skill's factual content is directive numbers, statute names and dates, none of
which the extractor recognises. A green evidence gate on this skill means nothing.
**Verification here is manual, and it is a per-instrument status check.**

## The standing check, to run EVERY cycle before anything else

For every directive, circular, regulation, statute and staff position the skill
cites, answer four questions from the regulator's own page:

0. **WHOM DOES IT BIND, in its own words?** Read the applicability clause, not the
   topic. This question was absent from the first draft of this checklist and its
   absence let the skill apply Bank of Israel BANKING directives to insurers for
   its entire life, and route non-bank payment providers to the wrong regulator.
   Directive 364 section 10.1 settles it in one sentence, and the word "ביטוח"
   appears nowhere in its 57 pages. A skill can be perfectly current and still
   send half its users to the wrong regulator.
1. **Is it still in force?** Not "does it exist" -- is it in force. A cancelled
   directive keeps its page.
2. **What is its current version, circular number and date?** Directive numbers
   are stable while their content is not.
3. **Was anything cancelled BY it, or does anything cancel IT?**

Record the answers with dates. A skill that names an instrument without a status
check is asserting that it is in force.

## Must cover (core)

- [x] **Addressee mapping: which regulator supervises which population.** Banking corporations and credit-card companies plus a systemically important payment provider: BOI (364 and the surrounding directives). Insurers, pension and provident bodies (גופים מוסדיים): Capital Market, Insurance and Savings Authority, Institutional Bodies Circular 2016-9-14. Non-bank payment and initiation licensees: Israel Securities Authority under the Payment Services and Payment Initiation Law, 5783-2023. Reporting corporations: ISA, regulation 36 and staff position 105-33. Designated bodies: their statutory guiding body under the Regulation of Security in Public Bodies Law, 5758-1998. **Added 2026-08-26 after the insurance and payments scoping errors.**

- [x] **BOI Directive 364 as the operative banking framework**, published 18/11/2024 (circular 2799), in force 18/05/2026 or on earlier adoption by the banking corporation. Source: boi.org.il/roles/supervisionregulation/nbt/nbt364/. Why core: it is the framework
- [x] **The repeal of 357, 361 and 363 on 18/05/2026**, stated on both the 364 page and the 361 page. Why core: **this is the single most important fact in the skill and v1.2.2 got it wrong.** The skill described 364 as future-dated and kept 361 as "the operative directive most agents reference", three months after 361 ceased to exist. Any answer citing 361 as live is wrong, and most models will reach for 361 by default because the repeal post-dates their training data
- [x] **Directive 366**, incident reporting, updated 17/06/2026 (circular 2848, update 4), including the duty to report a "serious security event" under section 31 of the Financial Information Service Law, 5782-2021, and the parallel change to reporting directive 880. Why core: it is where the banking reporting clock actually lives
- [x] **Directive 362**, cloud, updated 17/06/2026 (circular 2849, version 5). Why core: and specifically that it is **NOT a BOI pre-approval regime**. It requires a senior-management cloud policy, board approval for material cloud, and an annual report under reporting directive 881, and it states the supervisory approach is enabling ("Business enabler"). v1.2.2 asserted prior BOI approval twice; an agent repeating that stalls a bank's project on a requirement that does not exist
- [x] **Directives 367 and 368** (banking via communications; Open Banking in Israel, 01/09/2025, circular 2826). Why core: Open Banking is a directive now, not a roadmap
- [x] **ISA: regulation 36 of the Securities Regulations (Periodic and Immediate Reports), 5730-1970, and staff legal position 105-33 "Disclosure on Cyber"** (October 2018, updated 25 January 2023). Why core: these are the two instruments that govern, and v1.2.2 cited neither, substituting invented numeric thresholds instead
- [x] **Materiality is qualitative and there is no numeric trigger.** Why core: v1.2.2 told users to file if operational disruption exceeded 24 hours or loss exceeded 1% of equity. Neither figure appears in any ISA instrument. Both removed
- [x] **PPA immediate breach notification is regulation 11(d)(1) of the Privacy Protection (Data Security) Regulations, 5777-2017**, binding the owner and holder of a database at medium or high security level. Amendment 13 added the financial sanction under section 21 of the Third Schedule, it did not create the duty. Why core: v1.2.2 attributed the duty itself to Amendment 13 and stated it without the security-level scope
- [x] **The PPA's first enforcement of that duty**, 21.07.2026, 256,000 NIS, and its stated position that waiting to complete investigations empties the immediacy requirement of content. Why core: it converts "immediately" from a word into an operational constraint on the IR playbook
- [x] **DPO scope includes the systematic-monitoring limb**, not only public bodies and large-scale sensitive processing. Why core: the monitoring limb catches adtech, analytics and workforce-monitoring products that hold little sensitive data, and it is routinely dropped
- [x] **INCD publishes NO reporting deadline for any sector**, and reporting to INCD does not discharge a duty owed to a sector regulator. Why core: v1.2.2 asserted "within hours" for critical infrastructure plus a four-tier deadline ladder in the reference file. Neither is sourced. Removed
- [x] **The Severe Cyber Attacks in the Digital Services and Hosting Sector (Temporary Order) Law, 5784-2023** is the one binding civilian-sector reporting statute, cited by INCD's own reporting page. Why core: v1.2.2 said private-sector reporting is voluntary without qualification, which is wrong for digital-service and hosting providers
- [x] **National Cyber Defense Law status**: government bill 1955, published 27 May 2026, passed first reading, in the Foreign Affairs and Defense Committee preparing for second and third reading since 29 July 2026 (Knesset bill 1046714). NOT yet law. Why core: v1.2.2 called it a January 2026 draft memorandum. Its 24h/72h clocks must never be presented as current obligation
- [x] **MoH Director-General Circular 06/2022** as the citable health-sector instrument. Why core: an unnumbered "MoH circular" is unusable in a compliance document
- [x] **Ministry of Communications: the cyber duty is a LICENCE ANNEX**, via the administrative directive "Cyber Protection Management" (13.02.2023, updated 12.11.2024) and licence amendment 28 (effective 02.05.2022). Why core: searching for regulations will never find it
- [x] **INCD reporting channel: 119, 072-3990801, 119@cyber.gov.il, 24/7**

## Should cover (advanced)

- [x] Standards versions, since this is a declared drift class: ISO/IEC 27001:2022 with Amendment 1:2024, ISO/IEC 27002:2022, the Israeli standards SI 27001 and SI 27002 adopted 31 January 2023, NIST CSF 2.0 (26 February 2024), NIST SP 800-53
- [x] That reporting duties STACK rather than substitute across INCD, sector regulator and PPA
- [ ] Directive 364's own clause numbering, so control matrices can cite at clause level rather than mapping to 361's structure. **`[CARRY]` to the next cycle:** this cycle re-pointed the citations to 364 but did not read 364's full text, so the control rows are still 361-shaped. Read the 364 PDF and re-map

## Out of scope (explicit, with rationale)

- **Privacy compliance generally** (consent, database registration, data-subject rights): `israeli-privacy-compliance`. Only the cyber-facing breach-notification duty is carried here, because an IR playbook cannot be written without it
- **MALMAB / defence sector controls.** MALMAB directives are not published, so no classification ladder, control list or clearance requirement can be sourced. v1.2.2 carried a four-level ladder including a "Sodi Beyoter Beyoter / Top Secret" tier that matches no published Israeli scheme; it was removed rather than corrected, because substituting another unverified ladder repeats the error. The skill routes the user to their MALMAB security officer and the contract's security annex. **Do not reinstate a ladder without a published source**
- **IMPA as a cyber authority.** IMPA imposes AML/CFT obligations and publishes no cyber directive. The two duties are stated separately from their own instruments
- **Actual security engineering** (architecture, tooling, testing). This skill maps regulation; it does not design controls

## Authoritative sources

- https://www.boi.org.il/roles/supervisionregulation/nbt/ -- the directive index. Check every number here before citing it. **Note: boi.org.il is behind Radware bot protection and returns ~108 characters to curl or WebFetch. Use a real browser, and assert location.href in the same call that extracts the text**
- https://www.gov.il/he/service/cyber-event-report -- INCD's reporting channel and the statute it cites. Re-check whether any sector timeline has been published
- https://www.isa.gov.il/ -- staff position 105-33, regulation 36
- https://www.gov.il/he/pages/reporting_security_breach -- the regulation 11(d)(1) duty
- https://knesset.gov.il/Odata/ParliamentInfo.svc/KNS_Bill and KNS_Law -- machine-readable bill and law status. `KNS_Law` returning zero rows for a bill name is a positive check that it has not been enacted

## Re-check priorities for the next cycle

1. Whether the National Cyber Defense Law has been ENACTED. It was one committee stage from it on 29 July 2026. On enactment this skill needs a substantial rewrite: statutory clocks, "essential organisation" designation, mandatory CISO, the standards menu
2. Whether Directives 362, 366 and 367 have moved again. All three were updated on 17/06/2026, which is a clustered-update pattern worth watching
3. `[CARRY]` Read Directive 364's full text and re-map the control matrix to its clause numbers
4. Whether any sector reporting timeline has finally been published by INCD
5. Standards editions: ISO/IEC 27001 and 27002, NIST CSF
