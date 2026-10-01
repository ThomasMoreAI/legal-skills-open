---
name: israeli-patent-guide-skills-il
title: Legal notice
description: 'Full guidance through the Israeli patent process: prior art search on ILPO database, national application filing, PCT international filing via ILPO, fees, and maintenance. Use when you need to check invention novelty, file a patent in Israel, track payment deadlines, or understand pharmaceutical patent term extension (PTE). Saves hours of research and prevents costly filing mistakes. Do NOT use for trademark registration, design patents, or legal advice replacing a licensed patent attorney.'
author: skills-il
author_url: https://github.com/skills-il/legal-tech/tree/master/israeli-patent-guide
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: ip
language: en
sources:
- title: Amendment 15
  path: references/amendment-15.md
- title: Domain Checklist
  path: references/domain-checklist.md
- title: Ilpo Fee Schedule
  path: references/ilpo-fee-schedule.md
- title: Pct Israel Checklist
  path: references/pct-israel-checklist.md
- title: Pte
  path: references/pte.md
- title: Service Inventions
  path: references/service-inventions.md
---

## Legal notice

This is a free information tool operated by an AI model. It explains patent procedure and helps you organise your own material. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by a patent attorney or advocate. The output is not a patent application prepared by a patent attorney and not a professional opinion, but an explanation and a draft only: it does not perform an exhaustive prior-art search and does not draft enforceable patent claims. An AI model may err, omit data, or present a wrong conclusion.

Drafting patent claims and representation before the Registrar of Patents are reserved by law to a patent attorney. Publication or faulty drafting can damage rights irreversibly, on deadlines that cannot be extended. Consult a patent attorney before any filing. All use of its output is the user's sole responsibility.
## Overview

This skill covers the end-to-end patent process in Israel as administered by the Israeli Patent Office (ILPO, also known as Rashut HaPatenTim - רשות הפטנטים). It is scoped to:

- National patent application filing under the Israeli Patents Law, 5727-1967
- Prior art search using ILPO's public database and international resources
- PCT international filing routed through ILPO as Receiving Office
- Official fee schedule, the 40% reduction for qualifying applicants, and maintenance fee structure
- Patent Term Extension (PTE) for pharmaceutical products under Israeli law
- Key deadlines, the Section 18 Notice prior to Examination, objection windows, and IDS (Information Disclosure Statement) obligations unique to Israeli practice

This skill does NOT cover trademark registration, industrial design registration, copyright, or utility model protection. It does not replace a licensed Israeli patent attorney for prosecution decisions.


## When to Use

- **Novelty check**: Before investing in a full application, search ILPO's database and WIPO PatentScope to assess whether an invention is likely new.
- **Filing guidance**: Step-by-step walkthrough of requirements for filing a national patent application in Israel.
- **PCT national phase entry**: Understanding timelines and requirements for entering the Israeli national phase from a PCT application.
- **Deadline tracking**: Calculating maintenance fee due dates, the 30-month PCT window, and the 3-month objection period after allowance.
- **PTE calculation**: Determining eligibility and maximum extension duration for pharmaceutical patents.
- **Fee estimation**: Checking whether you qualify for the 40% reduction and estimating total filing and prosecution costs.


## Israeli Patent Filing Process

### Who Owns the Invention: Service Inventions (Sections 132-135)

Section 132(a): an invention made by an employee during and in consequence of employment belongs to the employer by default. Section 134 routes compensation disputes to the Compensation and Royalties Committee at ILPO when the contract is silent. The employer loses title if the employee's s.131 notice says the invention will be the employee's absent a contrary reply within 6 months and the employer stays silent (s.132(b)); disputes over whether it is a service invention go to the Registrar (s.133). A contractor is not an employee, so the default does not apply to them: settle ownership in writing.

Detail, including the contractor trap and drafting guidance: `references/service-inventions.md`.

### Application Requirements

A complete patent application filed with ILPO must include:

1. **Request form** (Form P/1): applicant name, inventor name(s), title of invention, and claim of priority if applicable.
2. **Specification** structured as:
   - **Description**: technical field, background, summary, detailed description of embodiments, and reference to drawings.
   - **Claims**: numbered, beginning with an independent claim. Claims define the legal scope of protection.
   - **Abstract**: a short summary; not part of the legal scope but used for search purposes.
   - **Drawings** (if applicable): black-and-white line drawings, A4 format, referenced in the description.
3. **Priority document**: for Paris Convention priority, a certified copy of the earlier application; confirm the deadline with ILPO.

### Language

Hebrew and English are both accepted as filing languages. If the application is filed in any other language, a Hebrew or English translation is required; confirm the deadline with ILPO.

### Address in Israel

Foreign applicants (those without a place of business or domicile in Israel) must appoint a registered Israeli patent attorney or agent as their address for service in Israel. Correspondence from ILPO is sent to this address.

### IDS Duty (Section 18, Israeli Patents Law)

Under Section 18 of the Israeli Patents Law, an applicant has a **continuing duty** to disclose all material prior art known to the applicant throughout prosecution, up to and including the Notice of Acceptance. This duty is substantially broader than USPTO practice:

- The duty applies to all material prior art, including art discovered during foreign prosecution of the same or related applications.
- If the applicant gave misleading details or knowingly failed to update the list, the court or Registrar may revoke the patent or refuse it, grant a licence, or shorten its term (s.18C).
- There is no prescribed form for the IDS in Israel; a letter to the examiner listing the relevant documents is sufficient.
- Best practice: file an IDS when receiving Office Actions or Search Reports from the USPTO, EPO, or any other office examining a counterpart application.

### Examination is Queued Automatically (No Early Examination-Request Election)

Unlike the EPO (where the applicant actively files a request for examination) or systems with a deferred-examination election made at filing, in Israel substantive examination is **queued automatically**. The applicant does not file an early examination-request form at the time of filing, and there is no separate examination fee beyond the filing fee.

However, this does NOT mean the applicant has nothing to do before examination. Before substantive examination begins, ILPO issues a **Notice prior to Examination under Section 18** of the Israeli Patents Law. The notice sets a response deadline, which is extendable for a fee; docket the date printed on the notice. The Section 18 notice is also the trigger for an applicant who wants to **defer** examination to file a deferral request. See the dedicated section below.

So: examination is queued automatically, with no EPO-style request-for-examination filing, BUT the Section 18 Notice prior to Examination carries a real response deadline.


## Prior Art Search

### ILPO Database

The ILPO online patent search is available at **israelpatents.justice.gov.il**. It is free, publicly accessible, and bilingual (Hebrew and English). Key features:

- Full-text search of Israeli patent applications and granted patents
- IPC (International Patent Classification) code filtering
- Applicant/inventor name search
- Status information (pending, granted, lapsed, opposed)

### International Databases

| Database | URL | Coverage |
|---|---|---|
| WIPO PatentScope | patentscope.wipo.int | PCT applications and national collections |
| Google Patents | patents.google.com | Worldwide patents with machine-translated content |
| Espacenet (EPO) | worldwide.espacenet.com | European and international collections |
| USPTO Full-Text | patents.google.com or USPTO.gov | US patents and published applications |

### What the Examiner Will Test (Sections 3, 4, 5, 7)

An invention is patentable if it is new, useful, industrially applicable and involves an inventive step (s.3). It is new only if it was not published anywhere, in writing, orally, or by use or display, before the application date (s.4). Inventive step means it is not obvious to an average person skilled in the art (s.5). No patent is granted for a method of medical treatment of the human body, or for new plant or animal varieties other than non-natural microorganisms (s.7).

### Search Strategy

1. **IPC classification**: Identify the relevant IPC subgroups for your invention. ILPO search supports IPC filtering. Use WIPO's official IPC classification resource at https://www.wipo.int/en/web/classification-ipc to find the right codes.
2. **Keyword synonyms**: Draft a synonym list covering technical terms, trade names, and common alternatives. Run multiple keyword searches; do not rely on a single query.
3. **Assignee/inventor search**: If you know of competitors or related inventors, search by name in PatentScope and ILPO.
4. **Non-patent literature**: For biotech and pharma, also search PubMed, journal databases, and conference proceedings. Published scientific papers constitute prior art.
5. **Date cutoff**: Prior art includes anything publicly available before your priority date, anywhere in the world, in any language.


## PCT International Filing from Israel

### Before Filing Abroad: Defence-Related Inventions (Sections 94-113)

**Check this before any foreign or PCT filing.** Chapter Six of the Israeli Patents Law (sections 94 to 113) governs inventions of potential military significance. Under s.98, an Israeli citizen, permanent resident, or other person owing allegiance to the State may not file abroad, directly or indirectly, for an invention concerning weapons, ammunition or other military value (or of a class under s.95), unless **(1) the Minister of Defence gave prior written permission, or (2) an Israeli application was filed and 6 months have passed with no s.94 order in force**. Filing a national application at ILPO first and waiting 6 months is the usual lawful route; ask a patent attorney before relying on a PCT filing at RO/IL for this.

This bites disproportionately in Israel because so much of the startup base works in cyber, optics, UAV and drone systems, RF and communications, sensors, and advanced materials. An Israeli founder who files a US provisional or an ePCT application first, without clearance, may commit an offence rather than merely lose a right.

Practical rule: if the invention has any plausible military or security application, get an opinion from a licensed Israeli patent attorney on sections 94-113 **before** the first foreign filing, not after. This is a gate, not a formality, and no other section of this skill substitutes for it.

### ILPO as Receiving Office

Israel is a member of the Patent Cooperation Treaty (PCT). ILPO acts as a Receiving Office (RO/IL) for PCT applications filed by Israeli applicants (or applicants with a place of business or residence in Israel). Applications can also be filed directly with WIPO's IB as receiving office.

Filing via ePCT (pct.wipo.int) is strongly recommended over paper filing.

### International Searching Authority (ISA) Options

ILPO acts as an ISA and IPEA. Applicants filing through RO/IL can choose:

| ISA | Notes |
|---|---|
| ILPO (ISA/IL) | Often lower cost for Israeli applicants; examination in Hebrew or English; familiarity with Israeli practice |
| EPO (ISA/EP) | Widely respected; higher cost; English, French, or German required |
| USPTO (ISA/US) | Available for Israeli applicants; search report in English |

The choice of ISA affects search quality perception in national phases and the cost of the international phase. The **ISA/IL international search fee** is **4,203 ILS**, published by WIPO as **1,446 USD** in the version of the PCT Applicant's Guide, Israel chapter, valid as from **1 August 2026**. Always confirm the current PCT fee in the WIPO Applicant's Guide before filing, since WIPO updates the dollar-denominated fee periodically.

### National Phase Entry in Israel

For PCT applications designating Israel, national phase entry must occur within **30 months from the earliest priority date** (not the filing date of the PCT application). This is the absolute deadline under Israeli law. Specific steps:

1. File a national phase entry request with ILPO (Form PCT/IL/01 or equivalent).
2. Pay the national phase entry fee.
3. If the international application was not filed or published in English, submit a **verified English translation** (s.48D(b)(2)); otherwise the application is treated as withdrawn. The Registrar may extend this deadline by up to 3 months (s.48D(c)).
4. Appoint an Israeli address for service if required.

### Fee Payment in NIS

An Israeli patent protects only Israel. To protect other markets, use the 12-month Paris priority year to file abroad directly or through PCT, which defers national-phase costs to month 30.

All official ILPO fees are denominated in New Israeli Shekel (NIS). For foreign applicants paying from abroad, fees are converted at the Bank of Israel official exchange rate on the payment date.


## Section 18 Notice prior to Examination and Office Actions

### The Section 18 Notice

After filing, the application waits in the examination queue. Before substantive examination is scheduled to begin, ILPO sends a **Notice prior to Examination under Section 18** of the Israeli Patents Law. The notice both tells the applicant the estimated examination date and asks the applicant to bring relevant prior art (including foreign search/examination results on counterpart applications) to ILPO's attention.

- **Response deadline**: the period printed on the notice.
- **Extensions**: extendable on payment of NIS 240 per month or part thereof (fee notice item 9); confirm the maximum with ILPO.
- **Deferral option**: the Section 18 notice is also the point at which an applicant who wants to push examination later can ask to defer; ILPO decides the length. Deferral is an active choice made in response to the Section 18 notice, not an automatic state.

Docket the Section 18 response deadline like any other hard deadline.

### Office Action Response Deadlines

Respond by the deadline printed on each examination report; it is extendable for a fee.

### Current Examination Backlog

Israeli examination is queued, and the wait from filing to the end of substantive examination runs to years rather than months, with biotechnology and chemistry typically slower than mechanics, electronics and physics. ILPO publishes current pendency figures in its annual report (https://www.gov.il/he/departments/ilpo); read the current report rather than a figure quoted second hand. This is why accelerated examination (PPH, green-tech, competitor-on-market, age/health) is a real lever for applicants whose business cannot wait three to four years for an enforceable patent. They are also part of the policy backdrop for the pending Amendment 15 reform discussed below.


## Pending Patent Law Amendment No. 15 (2025-2026 reform)

On **30 December 2025** the Israeli government published the **Patents Law (Amendment No. 15) Bill, 5786-2025**, the most substantial overhaul of Israeli patent procedure in decades. The bill was published in Reshumot, Government Bills 1920, on 30 December 2025. It is a bill, not law, and it is not in force. Check the ILPO site and the Knesset legislation database for its current parliamentary stage before relying on any of it. Practitioners should track it because the proposed changes touch filing strategy, queue management, and grace-period reliance.

### Amendment 15 (proposed)

As of 13 September 2026 the Knesset legislation database lists the bill as tabled for first reading (status: הונחה על שולחן הכנסת לקריאה ראשונה), with no committee assigned and no publication as law. Not in force. Proposed changes and their filing implications: `references/amendment-15.md`.

### Practical implications for filing today (September 2026)

Keep docketing Section 18 deadlines and do not rely on the proposed grace period or provisional route. Filing-strategy implications: `references/amendment-15.md`.


## Divisional, Accelerated Examination, and the Absence of a True Provisional

### Divisional Applications

If an application claims more than one invention, or the applicant wants to pursue subject matter separately, a **divisional application** can be filed out of a pending parent. The divisional keeps the parent's filing date for the carved-out subject matter. Division may be requested only **while the parent has not yet been accepted** (s.24(a)), so it cannot be done during the opposition period; it carries its own filing fee.

### Accelerated (Expedited) Examination

ILPO can move an application to the front of the examination queue on an accepted ground, for example applicant age or health, a competing product on the market, an application that is the basis for others, green technology, or via the Patent Prosecution Highway (PPH) using favorable results from a partner office. Accelerated examination is requested with a dedicated fee. This is the route to use when the default queue wait is too long for the applicant's business needs.

### No True Provisional Application

Israel does not have a US-style provisional application **today**. The practical substitute is the **12-month Paris Convention priority year**: file a first application (in Israel or elsewhere), then file the full national or PCT application within 12 months while claiming priority back to that first filing. There is no separate cheaper "provisional" filing track at ILPO under the current law.

This may change. The pending **Patents Law (Amendment No. 15) Bill, 5786-2025** (published 30 December 2025) proposes a new Israeli domestic provisional application with relaxed formal requirements, with a staged effective date of one year after publication once enacted. See the dedicated "Pending Patent Law Amendment No. 15" section above. Until the bill is enacted and the effective date arrives, treat the lack of a domestic provisional as the binding rule.


## Fees and Cost Savings

### 40% Fee Reduction (pay 60% of the amount)

Applies to the FILING fee and the NOTICE-OF-ACCEPTANCE fee only, and only on a FIRST patent application for that invention. It does NOT apply to renewals, accelerated examination, PTE, oppositions, or extensions of time.

Eligible: (a) any applicant that is not a company or partnership; (b) a company or partnership whose turnover in the PRECEDING year did not exceed NIS 10 million; (c) an institution recognised under s.9 of the Council for Higher Education Law; (d) a technology-transfer company wholly owned by such an institution.

Full eligibility text and worked examples: `references/ilpo-fee-schedule.md`.

### Fee Structure Overview

ILPO fees are CPI-indexed and change at the start of each year. The figures below are transcribed from the **official fee notice dated 22 December 2025, in force from 1 January 2026** (https://www.gov.il/BlobFolder/news/ilpo-fees/ar/news_fees-2026.pdf, landing page https://www.gov.il/he/pages/ilpo-fees). Amounts are in NIS.

Substantive examination is **included in the filing fee**; there is no separate "examination fee" for a normal application. A separate fee applies only when **accelerated** examination is requested.

| Fee Type | Full Fee (2026, NIS) | With Reduction (60%) |
|---|---|---|
| National application filing, first 50 claims (examination included) | 2,402 | 1,441 |
| Additional fee per claim, from the 51st claim | 616 each | not reduced |
| PCT national phase entry (examination included) | 2,402 | 1,441 |
| Renewal, years 1-6 (due within 3 months of grant) | 961 | not reduced |
| Renewal, years 7-10 (due before end of year 6) | 1,921 | not reduced |
| Renewal, all periods at once (due within 3 months of grant) | 14,410 | not reduced |

Full 2026 schedule (all rows, PTE ladder, PCT-phase fees, inter partes): `references/ilpo-fee-schedule.md`. These are official fees only. Patent-attorney drafting and prosecution fees are private, are not set by ILPO, and usually dominate the budget; get a written quote.

The PCT claim and page supplements apply to international applications designating Israel as well, and are the most commonly missed line items on national phase entry.

For the ILPO fees in the PCT international phase (ISA search 4,203, transmittal 656, IPEA preliminary examination 1,801), the full PTE fee ladder, and the miscellaneous inter partes fees, see `references/ilpo-fee-schedule.md`.

### Maintenance Fee Structure

Patent maintenance (renewal) fees in Israel follow a unique schedule compared to most jurisdictions:

- **Years 1 through 6**: a lump sum of **NIS 961**, due **within 3 months of the grant date**, covering the first 6 years from the filing date.
- **Subsequent years**: fees are paid every 4 years in advance, covering years 7-10, 11-14, 15-18, and 19-20.
- **Each renewal is due before the END of the year PRECEDING the block it covers.** The renewal covering years 7-10 is due before the end of year 6, the one covering years 11-14 before the end of year 10, then before the end of year 14 and year 18. Paying "before the year-7 anniversary" is a full year late and the patent lapses.
- **All-inclusive option**: NIS 14,410 paid within 3 months of grant keeps the patent in force for its entire term. Band-by-band payment totals NIS 17,292, so the single payment saves NIS 2,882 and removes four dockets.
- **Grace period**: a 6-month grace period is available for late maintenance payments, subject to a surcharge. After the grace period the patent lapses. Restoration under section 59 costs NIS 841 and requires showing the fee was unpaid for reasonable causes, the lapse was unintended, and the request was filed as soon as possible after the non-payment became known (s.60); anyone who began using the invention after the lapse was published may keep doing so (s.63).
- **No small-entity discount**: the 40% reduction does not apply to any renewal fee.
- **Maximum term**: 20 years from the filing date (not the priority date).


## Objection Period

After an application is accepted, ILPO publishes the acceptance online (section 26). Any person may file an opposition within **3 months from the date of that publication** (section 30), not from the date the applicant received the notice, so docket from the publication date. The Registrar may not extend it (s.164(a) excludes s.30). If an opposition is filed, the patent enters opposition proceedings before ILPO before the patent can be granted. If no opposition is filed within 3 months, the patent is granted.


## Patent Term Extension (Pharma)

Sections 64A to 64Q of the Patents Law let the Registrar extend a basic patent covering a medicinal product or regulated medical device. Four rules drive most decisions:

- **Filing window**: no later than **90 days** from registration of the medicinal product under the Pharmacists Ordinance (s.64O(a)).
- **Recognized-country linkage**: where marketing approval was given in the United States or a recognized European state (First Schedule), a matching extension must also have been granted there and not expired (s.64D(5)-(7)). The Israeli extension lasts as long as the SHORTEST extension granted in the recognized countries (s.64I(a)).
- **Israel-only registration is not a bar**: if registration was sought only in Israel, the extension equals the period from filing the registration application to registration, provided it was pursued in good faith and with due diligence (s.64I(b)).
- **Caps** (s.64J): at most **5 years** beyond the s.52 term, and total protection ends no later than **14 years** from the first marketing approval in any recognized country.

Details, opposition, and the fee ladder: `references/pte.md` and `references/ilpo-fee-schedule.md`.


## Key Databases and Resources

| Resource | URL | Purpose |
|---|---|---|
| ILPO Patent Search | https://israelpatents.justice.gov.il/en | Search Israeli patent applications and grants |
| ILPO official site (gov.il) | https://www.gov.il/he/departments/ilpo | Official forms, fee notices, announcements, publications |
| PCT ePCT Filing | https://pct.wipo.int | Online PCT application filing and management |
| WIPO PatentScope | https://patentscope.wipo.int/search/en/search.jsf | International prior art search (129.5 million patent documents) |
| WIPO PCT Guide for Israel | https://pctlegal.wipo.int/eGuide/view-doc.xhtml?doc-code=IL | Country-specific PCT requirements for Israel |
| IPC Classification (WIPO) | https://www.wipo.int/en/web/classification-ipc | Find IPC codes for prior art searches |
| Bank of Israel Exchange Rates | https://www.boi.org.il/en/economic-roles/financial-markets/exchange-rates/ | Official exchange rates for fee conversion |


## Gotchas

### 0. There Is No Grace Period Today: Disclose Publicly and You Lose the Patent

Under **current** Israeli law there is no general grace period. Any public disclosure of the invention before the filing date destroys novelty, wherever in the world it happened, in any language, and **including a disclosure made by the inventors themselves**. A demo day pitch, a conference talk, a published paper, a public GitHub repository, a product launch, or a trade show booth can each end the possibility of a valid patent.

This is the most expensive mistake founders make, and it is invisible until years later when the patent is challenged.

- File first, disclose second. If timing forces disclosure first, use a signed NDA, which is not a public disclosure.
- The 12-month grace period described in the Amendment 15 section below is **proposed, not in force**. Do not rely on it.
- Even if Amendment 15 is enacted, most of the EU and China still have no equivalent grace, so a public disclosure would remain fatal in those markets.
- One asymmetry worth knowing: registered designs under the Designs Law, 5777-2017 **do** have a 12-month grace period. If a product has already been shown publicly, the patent route may be closed while the design route is still open. Ask a licensed Israeli patent attorney promptly rather than assuming everything is lost.

### 1. IDS Duty is Continuous Until Notice of Acceptance

Unlike USPTO practice, where an IDS is typically filed once at defined stages, Section 18 imposes a **continuing duty** of disclosure from filing through the Notice of Acceptance. If a US counterpart draws an Office Action citing new art after the Israeli IDS was filed, a supplemental disclosure must be filed in Israel. Failing to disclose material prior art known to the applicant can invalidate the patent even after grant.

### 2. No EPO-Style Examination Request, But the Section 18 Notice Still Has a Deadline

In Israel there is no EPO-style examination-request filing and no early deferred-examination election at filing. But it is equally wrong to tell a client "there is nothing to do until the first Office Action." Treat the **Section 18 Notice prior to Examination** as a hard, dockable deadline, and use it as the moment to file a deferral request if examination should be pushed later.

### 3. The 40% Fee Reduction Threshold is NIS 10M Turnover, Not Profit

The threshold is turnover (gross revenue) in the **preceding** year that **did not exceed** NIS 10 million, so exactly NIS 10 million still qualifies. Universities recognised under section 9 of the Council for Higher Education Law and their wholly-owned technology transfer companies also qualify, which covers every Israeli TTO. Two traps run the other way: the reduction applies **only to a first application for that particular invention**, not to divisionals, and it covers **only the filing fee and the notice of acceptance fee**. Verify eligibility at filing; the declaration cannot be added retroactively.

### 4. PCT 30-Month Deadline Runs From Priority Date, Not PCT Filing Date

The 30-month national phase entry window in Israel is measured from the **earliest priority date** claimed in the PCT application. Agents sometimes mistakenly calculate from the international (PCT) filing date, which can differ by up to 12 months from the priority date. A miscalculation here means a missed deadline whose only cure is a PCT Rule 49.6 reinstatement request under the strict "due care" test, which is not guaranteed.

### 5. Israeli PTE Is Capped by Foreign Extensions and a 14-Year Ceiling

Agents trained on US or EU practice miss that the Israeli extension is limited to the shortest extension granted in the recognized countries, and ends no later than 14 years from the first marketing approval in any of them (ss.64I, 64J). Do not quote a flat 5 years.



## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Israel Patent Office | https://www.gov.il/he/departments/ilpo | Official patent filing procedures, forms, fees, examiner contacts |
| Patents Law 5727-1967 (WIPO Lex) | https://www.wipo.int/wipolex/en/text/495413 | Patents Law 1967 and amendments, patentability requirements, ss.18, 94-113, 132-135 |
| WIPO PCT (international filings) | https://www.wipo.int/pct/en/ | Patent Cooperation Treaty, international application routes from Israel |
| Israel Patent Office search | https://israelpatents.justice.gov.il/en | Free Israeli patent database search, published applications |

## Recommended MCP Servers

These Model Context Protocol servers, available in the skills-il directory, pair well with this skill:

- **israel-law**: programmatic access to Israeli primary legislation. Use it to pull the current text of the Patents Law, 5727-1967, and its amendments when you need to confirm a section reference (for example Section 18 on the duty of disclosure and the Notice prior to Examination).
- **boi-exchange**: Bank of Israel exchange-rate data. Use it to convert ILPO fees to a foreign currency at the official rate when a foreign applicant is budgeting a filing.

Always confirm fee figures against the official ILPO portal, since the schedule is CPI-indexed and changes each year.

## Troubleshooting

**Problem**: ILPO database search returns no results for a known Israeli patent.
**Solution**: Try searching by publication number directly. The database can lag by 2-4 weeks for new publications. Also check whether the application was filed before the database's coverage start date; older patents may not be fully digitized.

**Problem**: ILPO rejected a priority document as insufficient.
**Solution**: The priority document must be a certified copy issued by the priority office. Uncertified copies, digital printouts, or WIPO DAS digital access codes may not satisfy ILPO's requirements in all cases. Confirm acceptable formats with an Israeli agent before relying on DAS.

**Problem**: Applicant is not sure whether they qualify for the 40% fee reduction (company is a subsidiary of a larger group).
**Solution**: ILPO applies the turnover test to the **applicant entity** as filed, not to a consolidated group. A wholly-owned subsidiary with its own financial statements showing under NIS 10M turnover may qualify even if the parent group is much larger. Verify with a licensed Israeli patent attorney, as this analysis can be fact-specific.

**Problem**: PCT national phase entry deadline appears to have passed.
**Solution**: Confirm the earliest priority date carefully (it may differ from the PCT filing date). Israel permits reinstatement of rights under PCT Rule 49.6 on the "due care" criterion, with a reinstatement fee of 240 ILS (WIPO PCT Applicant's Guide, Israel chapter, version applicable from 1 August 2026). "Due care" is a strict test, so reinstatement is not guaranteed; act immediately and have a patent attorney file the request.


## References

- Israeli Patents Law, 5727-1967 (as amended): WIPO Lex https://www.wipo.int/wipolex/en/text/495413 ; Hebrew consolidated text via Nevo https://www.nevo.co.il/law_html/law01/p187_002.htm
- ILPO Official Fee Notice 2026: https://www.gov.il/BlobFolder/news/ilpo-fees/ar/news_fees-2026.pdf (dated 22 December 2025, in force 1 January 2026; CPI-indexed). Landing page: https://www.gov.il/he/pages/ilpo-fees
- ILPO portal (English): https://www.gov.il/en/departments/ilpo
- ILPO annual report (filing-to-end-of-examination averages): see the publications listing at https://www.gov.il/he/departments/ilpo
- Patents Law (Amendment No. 15) Bill, 5786-2025, official text as published in Reshumot, Government Bills 1920, 30 December 2025: https://fs.knesset.gov.il/25/law/25_ls1_10491345.pdf
- WIPO PCT Applicant's Guide, Israel Chapter (version valid as from 1 August 2026; ISA/IL search fee 4,203 ILS / 1,446 USD): https://pctlegal.wipo.int/eGuide/view-doc.xhtml?doc-code=IL
- Patent Cooperation Treaty Regulations, Rule 49.6 (reinstatement)
- Israeli Patents Regulations, 5729-1969
- See also: `references/ilpo-fee-schedule.md`, `references/pct-israel-checklist.md`


## Disclaimer

This skill provides informational guidance only. It does not constitute legal advice and does not create an attorney-client relationship. Israeli patent law involves jurisdiction-specific nuances, fact-specific determinations, and professional judgment. For any specific patent matter, consult a licensed Israeli patent attorney registered with the Israeli Patent Office.
