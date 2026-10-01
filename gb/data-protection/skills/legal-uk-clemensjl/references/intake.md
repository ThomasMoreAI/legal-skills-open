# Intake

Answer before the first legal text is drafted. Unanswered items become `[[MISSING: …]]` in the draft and in the report back to the user. Never guessed, never filled with something plausible.

## Legal entity

1. Legal form — private company limited by shares, company limited by guarantee, LLP, sole trader, ordinary partnership, limited partnership, CIC, charity, unincorporated association?
2. Registered name exactly as it appears on the register, including "Limited" or "Ltd" as registered
3. Trading name, if different from the registered name
4. Company or LLP registration number, and the part of the UK of registration (England and Wales, Scotland, Northern Ireland) — reg 25(2) SI 2015/17
5. Registered office address as filed at Companies House
6. Geographic address of establishment, if different from the registered office — reg 6(1)(b) Electronic Commerce (EC Directive) Regulations 2002
7. For a sole trader or partnership trading under a name other than the proprietors' surnames: the proprietors' names and an address for service in the UK — CA 2006 s 1201
8. Email address, plus at least one further channel allowing rapid, direct and effective communication — reg 6(1)(c) ECR 2002
9. VAT registration number, if registered — reg 6(1)(g) ECR 2002
10. Is the business in liquidation, administration or receivership? Reg 26 SI 2015/17 requires disclosure

## Regulation and profession

11. Is the activity subject to an authorisation scheme? Name the supervisory authority — reg 6(1)(e) ECR 2002
12. Is a regulated profession involved (solicitor, accountant, architect, healthcare, financial services, estate agency)? Give the professional body, the professional title, the member state or country in which it was granted, and where the applicable professional rules can be consulted — reg 6(1)(f) ECR 2002
13. FCA, Ofgem, CQC, SRA or other sector registration numbers
14. Have all directors and PSCs completed Companies House identity verification? Compulsory since 18 November 2025 under the Economic Crime and Corporate Transparency Act 2023

## Data protection

15. What personal data is collected — contact form, account, order, newsletter, support, server logs, session recording, CCTV?
16. Purpose and lawful basis for each processing operation (UK GDPR Art 6): contract, legal obligation, legitimate interests, recognised legitimate interests under Art 6(1)(ea) and Annex 1, consent
17. Retention period, or the criteria used to set it, per category
18. Recipients: hosting, payments, fulfilment, email sending, analytics, CRM, cloud, support tooling
19. Transfers outside the UK — which country, which mechanism (adequacy regulations, IDTA, UK Addendum, UK Extension to the EU–US DPF)
20. Processor contracts under UK GDPR Art 28 — with whom, stored where?
21. Profiling, scoring, automated decisions with legal or similarly significant effects (UK GDPR Arts 22A–22D as substituted by DUAA s 80)?
22. Special category data under UK GDPR Art 9, or criminal offence data under Art 10 and DPA 2018 Sch 1?
23. Children under 18 in the audience? Is the service likely to be accessed by children for the purposes of the ICO Age Appropriate Design Code?
24. Is a Data Protection Officer required under UK GDPR Art 37, or appointed voluntarily?
25. Is the ICO data protection fee paid, and at which tier? Registration number?
26. Does the business offer goods or services to, or monitor, people in the EEA? If yes, EU GDPR Art 3(2) applies in parallel and an Art 27 representative is needed

## Selling

27. Consumers, businesses, or both? The consumer regime turns on this
28. Goods, digital content, digital services, services performed in person, or subscriptions?
29. Target countries and languages — determines which consumer law applies alongside UK law
30. Payment methods and payment service providers
31. Delivery charges, delivery timescales, delivery restrictions — reg 14(6) CCRs 2013 requires restrictions and accepted payment means to be stated at the latest at the start of the ordering process
32. For digital content supplied immediately: is the consumer's express request and acknowledgement of loss of the right to cancel captured? Reg 37 CCRs 2013
33. Auto-renewing subscription? Note the DMCC subscription regime is not yet in force — see `dmcc-trading.md`
34. Commercial guarantee offered in addition to statutory rights?
35. Are reviews displayed? Are they incentivised, filtered, moderated or aggregated? DMCC Act 2024 Sch 20

## Content, platform and marketing

36. Does the service let users encounter content generated, uploaded or shared by other users — forum, chat, profiles, marketplace listings, direct messages? OSA 2023 s 3
37. If the only user content is comments and reactions on the provider's own content, the limited functionality exemption in OSA 2023 Sch 1 para 4 may apply — confirm precisely what users can post and to whom
38. Is pornographic content shown or allowed? OSA 2023 Part 5 and Sch 1 para 6
39. Email, SMS or automated-call marketing planned? Existing list, and how the addresses were obtained
40. Is the organisation a charity as defined in PECR reg 22(5)? Only then does the charity soft opt-in apply
41. Influencer, affiliate or paid-partnership content? CAP Code section 2
42. Environmental or "sustainable" claims made? CMA Green Claims Code and DMCC Act 2024 s 226

## Size and sector

43. Staff numbers and annual turnover — sets the ICO fee tier under reg 4 SI 2018/480
44. Is the organisation a public sector body within reg 4 SI 2018/952? Then the accessibility regulations apply in full
45. Regulated sector with a statutory ombudsman (financial services, energy, telecoms, property, legal services)? Determines the ADR body named under DMCC s 308

## What already exists

46. Are there existing legal texts on the site? Where did they come from — a solicitor, a template generator, a previous developer, a translation of an EU or German original?
47. Do any of them mention: "GDPR" as the applicable law, Regulation (EU) 2016/679, Article 77, the EU online dispute resolution platform, "right of withdrawal", the Consumer Protection from Unfair Trading Regulations 2008, the Companies (Trading Disclosures) Regulations 2008, § 5 TMG, or an EU representative? Any hit means the text was built on a foreign or superseded base and is rewritten, not patched.
48. When were they last reviewed, and by whom?
49. Is there a consent management platform? Which one, and who configured the categories?
50. Has a solicitor previously signed anything off? Which documents, and on what date?

## How the answers are used

| Answer | Drives |
|---|---|
| Legal form, registration details | `website-disclosures.md` |
| Processing inventory, recipients, transfers | `privacy-notice.md`, `international-transfers.md` |
| Turnover and staff numbers | ICO fee tier in `accountability-and-fee.md` |
| Tags and storage actually used on the site | `cookies.md` |
| Marketing channels and list provenance | `electronic-marketing.md` |
| Consumer or business customers, product type | `consumer-terms.md`, `cancellation.md` |
| Pricing structure, reviews, subscriptions | `dmcc-trading.md` |
| What users can post, and to whom | `online-safety.md` |
| Public sector status | `accessibility.md` |
| Sector and ombudsman membership | `complaints-adr.md` |

## Checkpoints

- [ ] Every answer either supplied or recorded as `[[MISSING: …]]`
- [ ] Registered name checked character for character against the Companies House register
- [ ] Part of the UK of registration recorded, not just "UK"
- [ ] Consumer or business status of the customer base settled before any terms are drafted
- [ ] EEA exposure assessed — if yes, EU GDPR Art 3(2) and Art 27 flagged as a separate workstream
- [ ] User-generated content question answered precisely enough to apply OSA 2023 Sch 1
- [ ] ICO fee status and tier confirmed
