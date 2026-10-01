# Scope: which state privacy laws apply

Status as at 2026-08-05.

This is the first step of every engagement and the one that is skipped. Roughly twenty states have enacted comprehensive consumer privacy statutes. They share an architecture and differ in every detail that matters: the thresholds, the vocabulary, the consent model for sensitive data, the appeal duty, the treatment of minors, and whether an opt-out preference signal must be honoured.

**Applicability is decided by where the consumers are, not by where the company is.** A three-person company in Ohio with 100,000 Colorado users is a controller under the Colorado Privacy Act. Ohio has no comprehensive law, and that is irrelevant.

## The determination procedure

For **each** state where consumers live:

1. Does the business conduct business in the state, or produce or deliver products or services targeted to residents of the state?
2. Does it meet or exceed that state's threshold — consumer numbers, revenue, or percentage of revenue from selling data? Compute per state; do not use a national figure.
3. Does an entity-level or data-level exemption apply (non-profit, GLBA financial institution, HIPAA covered entity, FCRA data, employment and B2B data)? Note the difference: some states exempt the **entity**, some only the **data**, and that distinction decides whether the whole programme falls away or only part of it.
4. Record the answer with the citation. The determination is the foundation of everything downstream and is the first document a regulator asks for.

Then, independently of every comprehensive law:

- **CalOPPA** (Cal. Bus. & Prof. Code § 22575 et seq.) applies to any commercial site collecting personally identifiable information from Californians, **with no threshold at all**.
- **Sectoral federal law** — COPPA, HIPAA, GLBA, FERPA, FCRA, VPPA, CAN-SPAM, TCPA — applies on its own triggers regardless of size.
- **FTC Act § 5** applies to everyone.

## The common architecture

Nearly every state statute follows the Virginia model and gives consumers:

- rights of **access, correction, deletion, portability**;
- a right to **opt out of the sale** of personal data, of **targeted advertising**, and of **profiling** in furtherance of decisions producing legal or similarly significant effects;
- **opt-in consent for sensitive data** (California is the outlier: it uses a right to *limit* use rather than opt-in consent);
- a **response deadline** (commonly 45 days, extendable) and, in most states, a mandatory **appeal process** with a route to the attorney general if the appeal is refused;
- controller duties of purpose limitation, data minimisation, security, and **data protection assessments** for higher-risk processing;
- processor contracts with prescribed terms.

Enforcement is by the state attorney general, in California also by the CPPA. **No state comprehensive privacy law has a general private right of action** — the CCPA's data-breach action (Cal. Civ. Code § 1798.150) is the narrow exception. That is why the private-right-of-action statutes in `tracking-and-wiretapping.md` and `health-and-biometrics.md` drive more litigation than the comprehensive laws do.

## Verified thresholds

Cited against the statutory text. Verify anything not on this list before putting it in client-facing work.

| State | Citation | Threshold |
|---|---|---|
| California | Cal. Civ. Code § 1798.140(d) | Any one of: annual gross revenue over **$25,000,000** in the preceding calendar year, as inflation-adjusted under § 1798.199.95(d); or buying, selling or sharing the personal information of **100,000 or more consumers or households**; or deriving **50 percent or more** of annual revenue from selling or sharing personal information. Note the household count and the standalone revenue trigger — both are unique to California. |
| Virginia | Va. Code § 59.1-576(A) | **100,000 consumers**; or **25,000 consumers** plus over **50 percent** of gross revenue from the sale of personal data. **No revenue threshold.** |
| Colorado | C.R.S. § 6-1-1304(1) | **100,000 consumers** in a calendar year; or deriving revenue from the sale of personal data of **25,000 consumers**. **No revenue threshold.** |
| Texas | Tex. Bus. & Com. Code § 541.002 | **No consumer-number and no revenue threshold.** Applies to a person that conducts business in Texas or produces a product or service consumed by Texans, processes or engages in the sale of personal data, and **is not a small business as defined by the United States Small Business Administration** — except that § 541.107 still applies to small businesses, prohibiting the sale of sensitive data without prior consent. |
| Oregon | ORS 646A.572 | **100,000 consumers**, excluding personal data controlled or processed solely to complete a payment transaction; or **25,000 consumers** plus **25 percent or more** of annual gross revenue from selling personal data. Operative 1 July 2024. |
| Nebraska | Neb. Rev. Stat. §§ 87-1101 to 87-1130; applicability at **§ 87-1103** | **No consumer-number and no revenue threshold.** § 87-1103(1)(c) requires only that the person "is not a small business as determined under the federal Small Business Act, **as such act existed on January 1, 2024**, except to the extent that section 87-1118 applies". § 87-1118 prohibits a small business from selling sensitive data without prior consent. Note the frozen federal reference date and the absence of any Nebraska-specific size test. |
| New Jersey | N.J.S.A. § 56:8-166.5 | **100,000 consumers**, excluding personal data processed solely to complete a payment transaction; or **25,000 consumers** plus the controller "derives revenue, **or receives a discount on the price of any goods or services**, from the sale of personal data". **No percentage and no dollar floor on the second limb** — a single discount from a data buyer triggers it. Effective 15 January 2025. The statutory cure period at § 56:8-166.17(b) **expired 1 July 2026** and is no longer available. |

Two structural points to carry into every scoping conversation:

- **The absence of a revenue threshold is the norm, not the exception.** Virginia, Colorado, Texas and Oregon all reach a company of any size once the consumer count is met, and Texas reaches it without any count at all. "We're too small for state privacy laws" is almost always wrong.
- **California's revenue-only trigger** means a large enterprise with a single Californian customer is a "business" under the CCPA. The other direction of the same error.

## States whose citations must be verified before use

The following have enacted comprehensive consumer privacy statutes. Their exact section numbers, effective dates and thresholds could **not** be verified against an official source in this session and must be checked before they appear in any deliverable:

`[[UNVERIFIED: statutory citation, effective date and thresholds for Connecticut, Utah, Montana, Delaware, Iowa, New Hampshire, Tennessee, Minnesota, Maryland (thresholds only), Indiana, Kentucky, Rhode Island, Florida, Louisiana and Vermont. Verify each against the state legislature's own code site before citing. Do not state a section number from memory.]]`

Points to check specifically when verifying:

- **Maryland** — the Maryland Online Data Privacy Act was enacted as **Chapter 455 of the 2024 Laws of Maryland (SB 541)**, approved 9 May 2024, **effective 1 October 2025**, adding §§ **14-4601 through 14-4614** to the Commercial Law Article and amending § 13-301. Verified against the General Assembly's bill record; controller duties sit at **§ 14-4607**. The General Assembly's online statute viewer is unreliable for this range and has returned unrelated forensic-nursing text — read the chapter law rather than the code display. Substantively Maryland is the strictest state on two points, and both must be read in the enrolled text before being relied on: a **data minimisation** standard limiting collection to what is reasonably necessary and proportionate to provide or maintain the specific product or service the consumer requested — a genuine substantive limit, not a notice duty, and unique among the state laws — and a **flat prohibition on the sale of sensitive data** rather than a consent requirement. `[[UNVERIFIED: the operative wording of the minimisation and sensitive-data provisions, the applicability thresholds, the § 14-4607(a)(5) consent carve-out, and the provisions on consumers under 18]]`
- **Montana** — reported to have lowered its consumer threshold by amendment. Verify the current figure and the amending chapter's effective date.
- **Minnesota** — reported to add a right to question the result of profiling and to be told the reason for it. Verify the section and the effective date.
- **Louisiana and Vermont** — later-enacted statutes that are frequently missing from tracker lists. `[[UNVERIFIED: citations, thresholds and effective dates for Louisiana SB 386 and Vermont S.71]]`
- **Florida** — the Digital Bill of Rights has an unusually high applicability threshold keyed to annual global gross revenue in the billions plus additional conditions. It does not reach ordinary businesses. Verify before either applying or dismissing it.

## Non-comprehensive state website statutes

- **CalOPPA**, Cal. Bus. & Prof. Code § 22575 et seq. — in force, no threshold, requires a conspicuously posted privacy policy and a disclosure of how the operator responds to Do Not Track signals. See `california-ccpa.md`.
- **Delaware Online Privacy and Protection Act**, **6 Del. C. § 1205C**, "Posting of privacy policy by operators of commercial online sites and services" — verified and in force. It mirrors CalOPPA: any operator of a commercial website, online service or app collecting personally identifiable information from Delaware users must post a policy identifying the categories collected and the third parties they may be shared with, the review-and-correction process, the process for notifying users of material changes, the effective date, **how the operator responds to browser Do Not Track signals**, and whether third parties may collect information across sites. The policy must be conspicuously available on the homepage or the first significant page after entry. Like CalOPPA, it has **no threshold** — a small business outside every comprehensive law still owes it.
- **Nevada**, chapter 603A NRS — in force, current through the 2025 (83rd) session. **The commonly cited "NRS 603A.340" is the wrong section for the opt-out**, and this error is widespread:
  - **NRS 603A.340** is the **notice** duty — "Notice regarding covered information collected by operator: Operator required to make available to consumers; contents; exception". Subsection 2 carries a small-operator exception (located in Nevada, revenue primarily from a source other than online sales, fewer than 20,000 unique visitors per year).
  - **NRS 603A.345** is the **opt-out of sale**: a consumer "may, at any time, submit a verified request through a designated request address to an operator directing the operator not to make any sale of any covered information", and the operator "shall respond to a verified request … within 60 days after receipt thereof", extendable "by not more than 30 days" with notice to the consumer.
  - **NRS 603A.346** imposes the same duty on **data brokers**, with the same 60 + 30 day structure. Cite .345 and .346 together where the text covers brokers.
  - Enforcement is **NRS 603A.360** — Attorney General only, up to **$5,000 per violation**, no private right of action. Cure provisions at .347, .348 and .349.
  - Amendment history to get right: the data-broker definitions (NRS 603A.323, .338) came from **SB 260 (2021)**, Ch. 292. **SB 370 (2023)**, Ch. 525, is the separate **consumer health data** act at NRS 603A.400–.550 — see `health-and-biometrics.md`. The two are routinely conflated.

## Practical scoping shortcuts

- If the site sells nationally and has any meaningful traffic, assume **California, Colorado, Virginia, Connecticut, Texas and Oregon** apply, then verify. Building to the union of these covers most of the rest.
- Build to the **strictest** applicable requirement rather than maintaining state-specific variants. The exceptions where a per-state variant is genuinely needed are the California links, the Texas verbatim sensitive-data notice, and the Washington consumer health data policy.
- Recount the thresholds annually. Crossing 100,000 consumers is a compliance event, not just a growth milestone.
- Where the business is close to a threshold, document the count and the method. Regulators ask.

## Checkpoints

- [ ] Consumer counts computed per state, not nationally
- [ ] Revenue figures recorded, and the California figure checked against the current inflation-adjusted threshold
- [ ] Applicability determination written down with the citation for each state
- [ ] Entity-level versus data-level exemptions distinguished and recorded
- [ ] CalOPPA applied regardless of size
- [ ] Texas assessed separately — no threshold, SBA small-business test only (§ 541.002), and § 541.107 applies even to small businesses
- [ ] Sensitive-data handling checked against the applicable state's model: opt-in consent in most states, limitation right in California, prohibition on sale in Maryland
- [ ] Appeal process built where a state requires one
- [ ] Opt-out preference signal handling built (see `opt-outs-and-gpc.md`)
- [ ] Every citation used in the deliverable verified against the state's own code site, and every `[[UNVERIFIED: …]]` either resolved or reported to the user
- [ ] Threshold review diarised annually
