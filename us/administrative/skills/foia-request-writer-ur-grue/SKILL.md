---
name: foia-request-writer-ur-grue
title: FOIA & Public Records Request Writer
description: Drafts legally complete public records requests (federal FOIA and all 50 state laws), administrative appeals, and redaction challenge strategies for U.S. government records.
author: ur-grue
author_url: https://github.com/ur-grue/autopunk-media-skills/tree/main/skills/magazine-journalism/investigation/foia-request-writer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: administrative
language: en
tags: [journalism, investigation, foia, research, public-records, state-records, appeals, redaction]
---

# FOIA & Public Records Request Writer

## What This Skill Does
Drafts formal, legally complete public records requests to U.S. federal and state government agencies. Also drafts administrative appeal letters when requests are denied, and analyzes redactions to identify improperly applied exemptions with specific challenge strategies.

## When To Use This Skill
- You need government records, contracts, communications, or internal reports for a story — at the federal or state level
- You are beginning an investigation and want to establish a paper trail through official channels
- You need a request that maximizes the chance of a full, timely response and minimizes the chance of blanket denial
- You want to request a fee waiver as a journalist or news organization
- Your federal or state records request has been denied or heavily redacted and you need to draft an administrative appeal
- You received redacted documents and want to identify which exemptions are likely misapplied and how to challenge them
- You need to file parallel requests to federal and state agencies for the same investigation

## What You Need To Provide

### For a new request (federal or state)
**Required:** The name of the agency (federal or state); a description of the records you want (dates, subjects, document types); your name and contact information; your stated purpose as a journalist; the state (if filing a state-level request)
**Optional:** The specific FOIA or public records office address; any known document numbers, case IDs, or reference numbers; the name of the news organization; a deadline tied to publication; specific officials or offices whose records you want

### For an appeal
**Required:** The original request (date and tracking number); the denial or adverse determination (date, exemptions cited, name of the FOIA officer who issued it); a brief explanation of why you believe the denial is improper
**Optional:** Any evidence that the records exist (news reports, other agency disclosures, congressional references); whether you want to request mediation through OGIS

### For redaction analysis
**Required:** The exemption codes cited in the redactions (e.g., (b)(5), (b)(7)(A)); a description of the document type and subject matter
**Optional:** Whether this is a federal or state record; whether the underlying investigation is known to be closed; any public statements or disclosures by the agency about the same subject matter

## How the Assistant Approaches This

### Federal FOIA Request
1. Identifies the correct statutory citation (5 U.S.C. § 552) and formats the letter as an official legal request, not a general inquiry
2. Drafts a precise records description that is narrow enough to be actionable but broad enough not to miss relevant material — avoiding vague language that agencies use to justify denials
3. Includes a journalist fee waiver request under the "representative of the news media" category, a request for expedited processing if applicable, and a clear statement of willingness to appeal
4. Closes with a firm but professional tone, with a response deadline reminder citing statutory 20-business-day requirement
5. Provides a "Next Step" note: find the agency's specific FOIA portal or mailing address, send via certified mail or the online portal and log the submission date, and calendar a follow-up for day 21 if no acknowledgment is received

### State Public Records Request
1. Identifies the correct state statute and its official name (see State Public Records Laws table below) — never refers generically to "FOIA" for a state request
2. Adapts the records description to state-specific conventions and terminology
3. Cites the state's actual response deadline (not the federal 20-day rule) and any applicable penalty provisions for non-compliance
4. Includes a state-specific fee waiver request where the state law provides one — notes honestly when a state has no journalist fee waiver provision
5. Flags residency restrictions if the state requires the requester to be a resident (seven states do — see table)
6. Provides the state-specific appeal or complaint process

### Administrative Appeal
1. References the original request by date, tracking number, and agency FOIA office
2. Identifies the adverse determination — the denial date, the exemptions cited, and the name of the officer who issued it
3. Argues specifically why each exemption is improperly applied, citing relevant case law where applicable
4. Demands a Vaughn Index if redactions are at issue — requiring the agency to justify each withheld document individually (*Vaughn v. Rosen*, D.C. Cir. 1973)
5. Notes the requester's right to seek mediation through OGIS (Office of Government Information Services)
6. States that litigation under 5 U.S.C. § 552(a)(4)(B) is the next step if the appeal is denied
7. Cites the 90-day appeal window and the agency's 20-business-day obligation to respond to the appeal

### Redaction Analysis
1. Identifies which of the nine FOIA exemptions ((b)(1) through (b)(9)) are cited
2. Provides a specific challenge strategy for each exemption — not just a description of what it covers, but how journalists have successfully challenged it
3. Flags Glomar responses (neither confirm nor deny) and explains the official acknowledgment doctrine as a counter-strategy
4. Recommends whether to appeal administratively, seek OGIS mediation, or proceed directly to litigation based on the strength of the challenge

## Output Format

### For requests (federal or state)
Single formal letter, 350–600 words. Structured as: sender block, date, agency addressee, subject line, opening paragraph (legal basis with correct statutory citation), records description section, fee waiver section, expedited processing request (if applicable), closing paragraph (appeal statement), sign-off. Business letter formatting throughout. Output ends with a "Next Step" note.

### For appeals
Single formal letter, 400–700 words. Structured as: sender block, date, appeals office addressee, subject line referencing original request, opening paragraph (identifying the adverse determination), argument section (one paragraph per exemption challenged), Vaughn Index demand (if redactions), OGIS mediation reference, litigation statement, sign-off.

### For redaction analysis
Structured analysis document, 300–800 words depending on the number of exemptions cited. Organized as: summary of redactions, analysis per exemption with challenge strategy, recommended next action (appeal, OGIS, litigation).

## Quality Criteria
- [ ] Federal requests cite 5 U.S.C. § 552 explicitly
- [ ] State requests cite the correct state statute by its official name — never "state FOIA" generically
- [ ] Records description is specific enough to be processed but not so narrow it misses related documents
- [ ] Journalist fee waiver claim uses statutory language appropriate to the jurisdiction (federal or state)
- [ ] Response deadline cites the correct statutory timeframe for the jurisdiction
- [ ] Contains a statement of intent to appeal any improper denial or withholding
- [ ] Appeals include all seven required elements (original reference, adverse determination, exemption arguments, Vaughn Index demand, OGIS reference, litigation statement, deadline)
- [ ] Redaction analysis provides challenge strategies, not just exemption descriptions
- [ ] Professional, formal register throughout — no hedging or apologetic language
- [ ] Output includes at least one concrete next action the user can take immediately
- [ ] Residency restrictions are flagged when filing in a restricted state
- [ ] Known limitations are stated honestly — this is a starting point, not legal advice

---

## State Public Records Laws

Each state has its own public records statute with a distinct name, response deadline, fee structure, and appeal process. The table below covers all 50 states and the District of Columbia.

**Important:** State laws change. This table reflects the law as of early 2026. Verify deadlines and procedures with the relevant state attorney general's office or press association before filing.

| State | Law Name | Statutory Citation | Response Deadline | Residency Restriction | Journalist Fee Waiver | Notes |
|-------|----------|-------------------|-------------------|----------------------|----------------------|-------|
| Alabama | Open Records Act | Ala. Code § 36-12-40 | "Promptly" (no fixed limit) | **Yes — residents only** | No specific provision | Non-residents may be denied; use in-state stringer or news org with AL presence |
| Alaska | Public Records Act | Alaska Stat. § 40.25.110 | 10 business days | No | No specific provision | |
| Arizona | Public Records Law | Ariz. Rev. Stat. § 39-121 | "Promptly" | No | No specific provision | No fixed deadline — agencies interpret broadly |
| Arkansas | Freedom of Information Act | Ark. Code § 25-19-105 | 3 business days | **Yes — citizens only** | No specific provision | "Citizens of Arkansas" — journalists elsewhere need workaround |
| California | California Public Records Act (CPRA) | Cal. Gov. Code § 7920.000 et seq. | 10 calendar days (extendable to 24) | No | Fee waiver for public interest | Recodified in 2022 from § 6250 et seq. — use current citation |
| Colorado | Colorado Open Records Act (CORA) | Colo. Rev. Stat. § 24-72-201 | 3 business days | No | No specific provision | |
| Connecticut | Freedom of Information Act | Conn. Gen. Stat. § 1-200 | 4 business days | No | Fee waiver at commission discretion | Strong FOI Commission for appeals |
| Delaware | Freedom of Information Act | Del. Code tit. 29, § 10001 | 15 business days | **Yes — citizens only** | No specific provision | |
| District of Columbia | Freedom of Information Act | D.C. Code § 2-531 | 15 business days | No | Fee waiver for news media | |
| Florida | Sunshine Law / Public Records Act | Fla. Stat. § 119.01 | "Promptly" (no fixed limit) | No | No specific provision | One of the broadest access laws in the country |
| Georgia | Open Records Act | Ga. Code § 50-18-70 | 3 business days | No | No specific provision | |
| Hawaii | Uniform Information Practices Act (UIPA) | Haw. Rev. Stat. § 92F | 10 business days | No | Fee waiver for public interest | |
| Idaho | Public Records Act | Idaho Code § 74-101 | 3 business days (10 for complex) | No | No specific provision | |
| Illinois | Freedom of Information Act | 5 ILCS 140/ | 5 business days (extendable to 10) | No | Fee waiver for news media | Penalties: $2,500–$5,000 per breach |
| Indiana | Access to Public Records Act (APRA) | Ind. Code § 5-14-3 | "Within a reasonable time" | No | No specific provision | |
| Iowa | Open Records Act | Iowa Code § 22.1 | "Promptly" | No | Fee reduction for news media | |
| Kansas | Open Records Act (KORA) | Kan. Stat. § 45-215 | 3 business days (extendable) | No | No specific provision | |
| Kentucky | Open Records Act | Ky. Rev. Stat. § 61.870 | 5 business days | **Yes — residents only** | No specific provision | "Any person" in statute but AG opinions limit to KY residents |
| Louisiana | Public Records Act | La. Rev. Stat. § 44:1 | 3 business days (5 for complex) | No | No specific provision | |
| Maine | Freedom of Access Act | Me. Rev. Stat. tit. 1, § 400 | 5 business days | No | Fee waiver at agency discretion | |
| Maryland | Public Information Act (MPIA) | Md. Code, Gen. Prov. § 4-101 | 30 business days | No | Fee waiver for news media | Longest statutory deadline in the country |
| Massachusetts | Public Records Law | Mass. Gen. Laws ch. 66, § 10 | 10 business days | No | Fee waiver for news media | |
| Michigan | Freedom of Information Act | Mich. Comp. Laws § 15.231 | 5 business days (extendable to 10) | No | Fee waiver for news media | Penalties: $2,500–$7,500 per instance |
| Minnesota | Government Data Practices Act (MGDPA) | Minn. Stat. § 13.01 | "Immediately" if available; 10 days for complex | No | No fee waiver but cost limits | Unique: data classified as public, private, or nonpublic |
| Mississippi | Public Records Act | Miss. Code § 25-61-1 | 7 business days (14 for complex) | No | No specific provision | |
| Missouri | Sunshine Law | Mo. Rev. Stat. § 610.010 | 3 business days (end of 3rd day) | No | Fees limited to actual cost | |
| Montana | Constitution Art. II, § 9 | Mont. Code § 2-6-1002 | "Promptly" (no fixed limit) | No | No specific provision | Constitutional right of access |
| Nebraska | Public Records Act | Neb. Rev. Stat. § 84-712 | 4 business days | No | No specific provision | |
| Nevada | Public Records Act | Nev. Rev. Stat. § 239.010 | 5 business days (extendable) | No | No specific provision | |
| New Hampshire | Right to Know Law | N.H. Rev. Stat. § 91-A | 5 business days | No | No specific provision | |
| New Jersey | Open Public Records Act (OPRA) | N.J. Stat. § 47:1A-1 | 7 business days | **Yes — citizens only** | No specific provision | Penalties: $1,000–$2,500; up to 10 years jail for repeat offenses |
| New Mexico | Inspection of Public Records Act (IPRA) | N.M. Stat. § 14-2-1 | 15 calendar days | No | No specific provision | |
| New York | Freedom of Information Law (FOIL) | N.Y. Pub. Off. Law § 84 | 5 business days (acknowledge); 20 to respond | No | Fee waiver for news media | Two-step: acknowledgment then response |
| North Carolina | Public Records Act | N.C. Gen. Stat. § 132-1 | "As promptly as possible" | No | No specific provision | |
| North Dakota | Open Records Act | N.D. Cent. Code § 44-04-18 | "Promptly" (1 business day reasonable) | No | No specific provision | |
| Ohio | Sunshine Law / Public Records Act | Ohio Rev. Code § 149.43 | "Promptly" (but must respond "within a reasonable period of time") | No | No specific provision | |
| Oklahoma | Open Records Act | Okla. Stat. tit. 51, § 24A.1 | "Promptly" | No | No specific provision | |
| Oregon | Public Records Law | Or. Rev. Stat. § 192.311 | "As soon as practicable and without unreasonable delay" | No | Fee waiver at agency discretion | |
| Pennsylvania | Right-to-Know Law (RTKL) | 65 Pa. Stat. § 67.101 | 5 business days (extendable to 30) | No | No specific provision | Strong Office of Open Records for appeals |
| Rhode Island | Access to Public Records Act (APRA) | R.I. Gen. Laws § 38-2 | 10 business days | No | No specific provision | |
| South Carolina | Freedom of Information Act | S.C. Code § 30-4-10 | 10 business days (extendable to 30) | No | No specific provision | |
| South Dakota | Open Records Act | S.D. Codified Laws § 1-27-1 | "Promptly" | No | No specific provision | |
| Tennessee | Public Records Act | Tenn. Code § 10-7-503 | 7 business days | **Yes — citizens only** | No specific provision | "Tennessee citizen" requirement |
| Texas | Texas Public Information Act (TPIA) | Tex. Gov. Code § 552.001 | 10 business days | No | Fee waiver for news media | AG ruling required for denials — strong enforcement |
| Utah | Government Records Access and Management Act (GRAMA) | Utah Code § 63G-2-101 | 10 business days (extendable to 25) | No | Fee waiver at agency discretion | Unique classification system: public, private, controlled, protected |
| Vermont | Public Records Act | Vt. Stat. tit. 1, § 315 | 2 business days (shortest in the country) | No | No specific provision | |
| Virginia | Freedom of Information Act (VFOIA) | Va. Code § 2.2-3700 | 5 business days | **Yes — citizens only** | No specific provision | "Citizens of the Commonwealth" |
| Washington | Public Records Act (PRA) | Wash. Rev. Code § 42.56 | 5 business days (acknowledge); "reasonable estimate" for response | No | No specific provision | Among the strongest enforcement; per-day penalties for non-compliance |
| West Virginia | Freedom of Information Act | W. Va. Code § 29B-1-1 | 5 business days | No | No specific provision | |
| Wisconsin | Open Records Law | Wis. Stat. § 19.31 | "As soon as practicable and without delay" (10 days for elected officials) | No | Fee waiver for news media | |
| Wyoming | Public Records Act | Wyo. Stat. § 16-4-201 | "Promptly" | No | No specific provision | |

### Key Patterns for Journalists

**Fastest response deadlines:** Vermont (2 days), Colorado/Georgia/Idaho/Kansas/Louisiana/Missouri (3 days).

**Slowest response deadlines:** Maryland (30 days), South Carolina (up to 30 with extension), Utah (up to 25 with extension).

**States with no fixed deadline:** Arizona, Florida, Indiana, Iowa, Montana, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, South Dakota, Wyoming — and several others that use "promptly." File and immediately calendar a follow-up. If no response within 10 business days, escalate.

**Residency-restricted states (7):** Alabama, Arkansas, Delaware, Kentucky, New Jersey, Tennessee, Virginia. If you are based out of state, use a local stringer, file through a news organization with an in-state office, or consult press freedom organizations for workaround strategies.

**States with strong enforcement/penalties:** New Jersey ($1,000–$2,500, up to jail time), Michigan ($2,500–$7,500), Illinois ($2,500–$5,000), Washington (per-day penalties). Cite these penalties in your request — agencies that know the penalty exists respond faster.

**States with strong independent appeals bodies:** Connecticut (FOI Commission), Pennsylvania (Office of Open Records), Texas (Attorney General rulings on denials). These states give journalists a faster path to resolution than federal court.

---

## Administrative Appeal Template

When a federal FOIA request is denied — in whole or in part — the requester has 90 days to file an administrative appeal. An appeal is not optional: federal courts generally require exhaustion of administrative remedies before litigation.

### Required Elements

Every appeal letter must include these seven components:

1. **Original request reference** — date filed, tracking number, agency FOIA office that processed it
2. **Adverse determination** — denial date, name of the officer who issued it, the specific exemptions cited for each withheld record or redaction
3. **Exemption challenge** — a specific argument for why each cited exemption is improperly applied (see Redaction Analysis below for challenge strategies per exemption)
4. **Vaughn Index demand** — if redactions are at issue, demand that the agency produce a detailed index describing each withheld document and the specific exemption justifying each redaction (*Vaughn v. Rosen*, D.C. Cir. 1973). This forces the agency to justify secrecy redaction by redaction rather than in bulk
5. **OGIS mediation reference** — note the requester's right to seek mediation through the Office of Government Information Services (5 U.S.C. § 552(h)), a non-binding but often effective alternative to litigation
6. **Litigation statement** — state that if the appeal is denied, the requester will file suit under 5 U.S.C. § 552(a)(4)(B) in the appropriate federal district court
7. **Deadline and response obligation** — cite the agency's 20-business-day obligation to respond to the appeal (5 U.S.C. § 552(a)(6)(A)(ii))

### When to Appeal

- Any full or partial denial of records
- Inadequate search (the agency claims records do not exist, but evidence suggests otherwise)
- Excessive or unjustified redactions
- Denial of fee waiver request
- Failure to respond within the statutory timeframe (constructive denial — the lack of a response IS the adverse determination you can appeal)

### After the Appeal

- The agency has 20 business days to respond
- If the appeal is denied, the requester can file suit in any federal district court where the requester resides, where the agency records are located, or in the District of Columbia
- OGIS can mediate before litigation — voluntary and non-binding, but agencies often engage when they know litigation is the alternative
- Many agencies settle after receiving a well-argued appeal because litigation is expensive for the agency too

---

## Redaction Analysis — FOIA Exemptions and Challenge Strategies

The nine FOIA exemptions ((b)(1) through (b)(9)) are the only legal basis for withholding federal records. Each has specific boundaries and specific challenge strategies.

### (b)(1) — Classified National Security Information

**What it covers:** Records properly classified under Executive Order 13526 (or its successors) in the interest of national defense or foreign policy.

**Challenge strategy:** Request a mandatory declassification review (MDR) under E.O. 13526 § 3.5. An MDR is separate from FOIA and forces the agency to re-evaluate whether the classification is still justified. Records over 25 years old are presumptively declassifiable. If the agency classified the records after receiving the FOIA request (a tactic agencies sometimes use), challenge the timing — retroactive classification to avoid disclosure is improper.

### (b)(2) — Internal Personnel Rules and Practices

**What it covers:** Records related solely to the internal personnel rules and practices of an agency.

**Challenge strategy:** Narrowed significantly by *Milner v. Department of the Navy* (2011). The Supreme Court eliminated "High (b)(2)" — agencies can no longer use this exemption for law enforcement techniques, security measures, or operational procedures. Only genuinely trivial internal administrative matters (parking rules, cafeteria hours) qualify. If an agency applies (b)(2) to anything substantive, cite *Milner* and challenge.

### (b)(3) — Exempted by Other Statute

**What it covers:** Records specifically exempted from disclosure by another federal statute, provided that statute either leaves no discretion on the matter or establishes particular criteria for withholding.

**Challenge strategy:** The agency must identify the specific statute. Challenge if: the cited statute does not actually exempt the specific records at issue, the statute grants discretion and the agency has not explained its exercise of that discretion, or the statute has been amended or repealed since the agency last reviewed its applicability.

### (b)(4) — Trade Secrets and Confidential Commercial Information

**What it covers:** Trade secrets and commercial or financial information obtained from a person that is privileged or confidential.

**Challenge strategy:** Tightened by *Food Marketing Institute v. Argus Leader Media* (2019) — the Supreme Court held that information is "confidential" if it is both customarily and actually treated as private by its owner. Challenge if: the information was publicly filed or disclosed elsewhere, the submitter did not actually treat it as confidential, or the government generated the information itself (government-generated data is not "obtained from a person"). Request that the agency consult the submitter under Executive Order 12600 (the "submitter notice" process) — submitters sometimes do not object to disclosure.

### (b)(5) — Deliberative Process, Attorney-Client, Attorney Work Product

**What it covers:** Inter-agency or intra-agency memoranda or letters that would not be available by law to a party other than an agency in litigation. In practice, three privileges: deliberative process, attorney-client, and attorney work product.

**Challenge strategy:** The most overused exemption. For deliberative process: the document must be both **pre-decisional** (created before the agency made a decision) AND **deliberative** (part of the decision-making process). Challenge if: the document reflects a final decision or policy (final decisions are never exempt), the document is purely factual (facts segregable from deliberative content must be released), or the deliberative process is complete and the decision has been made (the privilege weakens significantly after the decision is final). For attorney-client: the communication must be between an attorney and client for the purpose of legal advice — not every email that happens to include agency counsel qualifies. For attorney work product: the material must be prepared in anticipation of litigation — routine legal review of policy is not litigation preparation.

### (b)(6) — Personal Privacy

**What it covers:** Personnel and medical files and similar files the disclosure of which would constitute a clearly unwarranted invasion of personal privacy.

**Challenge strategy:** This is a balancing test — the public interest in disclosure must be weighed against the privacy interest. Challenge by arguing: the public interest is substantial (the records reveal government misconduct, waste, or abuse of authority), the individuals are government officials acting in their official capacity (officials have reduced privacy expectations for their official conduct — *Department of Justice v. Reporters Committee*, 1989, but applied narrowly), or the information is already publicly available (no remaining privacy interest in information the person has already disclosed publicly).

### (b)(7) — Law Enforcement Records

This exemption has six sub-parts. The most relevant for journalists:

**(b)(7)(A) — Could reasonably be expected to interfere with enforcement proceedings.**
**Challenge strategy:** Challenge if the investigation is closed — once proceedings are complete, (b)(7)(A) no longer applies. Challenge if the agency cites "proceedings" that are speculative or indefinite ("we might investigate someday" is not a pending proceeding). Request that the agency identify the specific proceeding at risk — vague references to "ongoing matters" are insufficient.

**(b)(7)(C) — Could reasonably be expected to constitute an unwarranted invasion of personal privacy.**
**Challenge strategy:** Similar balancing test to (b)(6) but with slightly stronger privacy protection. Challenge using the same public-interest arguments. Note that the names of federal employees acting in their official capacity are generally not protected by (b)(7)(C) when the public interest in oversight is strong.

**(b)(7)(D) — Could reasonably be expected to disclose the identity of a confidential source.**
**Challenge strategy:** The agency must demonstrate that the source was actually promised confidentiality. Implied confidentiality is weaker than express confidentiality. If the source is a government agency (inter-agency referral), the confidentiality claim is weaker.

**(b)(7)(E) — Would disclose law enforcement techniques or procedures.**
**Challenge strategy:** Challenge if the technique is already publicly known (published in agency manuals, described in court filings, reported in media). Publicly known techniques have no remaining secrecy interest.

### (b)(8) — Financial Institution Examination Records

**What it covers:** Records related to the examination, operating, or condition reports prepared by, on behalf of, or for the use of an agency responsible for regulation or supervision of financial institutions.

**Challenge strategy:** Rarely encountered outside financial regulation. Challenge if the records are not actually examination records (agency correspondence about a bank is not the same as examination data).

### (b)(9) — Geological and Geophysical Information

**What it covers:** Geological and geophysical information and data, including maps, concerning wells.

**Challenge strategy:** Extremely narrow. Only applies to oil and gas well data. If an agency applies (b)(9) to anything else, challenge immediately — it is almost certainly misapplied.

### Glomar Responses

A Glomar response is when the agency refuses to confirm or deny whether responsive records exist. Named after *Phillippi v. CIA* (1976) regarding the Hughes Glomar Explorer.

**Challenge strategy — the Official Acknowledgment Doctrine:** If the government has publicly acknowledged the information elsewhere — in press briefings, congressional testimony, court filings, declassified documents, or official statements — a Glomar response is improper. The agency cannot claim that the existence of records is itself classified or exempt when it has already confirmed the underlying activity publicly. Compile every public reference to the subject and include them in the appeal.

---

## Example

### Example 1: Federal FOIA Request

#### Input
Agency: U.S. Department of Transportation, Federal Aviation Administration
Records wanted: All communications between FAA safety inspectors and executives at a regional aircraft maintenance contractor (Meridian Aviation Services) between January 2022 and December 2023, including emails, inspection reports, violation notices, and any waivers or exemptions granted
Purpose: Investigating a pattern of alleged safety violations at the contractor
Organization: Freelance journalist, publishing in a national aviation trade magazine

#### Output

Jane Harlow
Investigative Journalist
[Address]
[City, State, ZIP]
jane.harlow@email.com
[Phone]

March 16, 2026

FOIA Request
FAA Office of the Chief Counsel, AGC-200
800 Independence Avenue SW
Washington, DC 20591

**Re: Freedom of Information Act Request — FAA Communications and Inspection Records, Meridian Aviation Services, 2022–2023**

Dear FOIA Officer,

Pursuant to the Freedom of Information Act, 5 U.S.C. § 552, I am requesting access to the records described below. I am a journalist working on an investigation for publication in a national aviation trade magazine, and this request is made in the public interest.

**Records Requested**

I request copies of all records created between January 1, 2022, and December 31, 2023, related to FAA oversight of Meridian Aviation Services, including but not limited to:

1. All written and electronic communications (emails, memoranda, letters) between FAA safety inspectors or oversight staff and any officer, employee, or representative of Meridian Aviation Services
2. All inspection reports, surveillance records, and audit findings related to Meridian Aviation Services facilities or operations
3. All notices of violation, corrective action plans, or enforcement actions issued to or against Meridian Aviation Services
4. All waivers, exemptions, or extensions of compliance deadlines granted to Meridian Aviation Services

If any records are withheld in full or in part, please identify each withheld record by type and date, and state the specific FOIA exemption(s) claimed. I will consider a response that withholds records without adequate justification to be a denial and will appeal accordingly.

**Fee Waiver Request**

I request a waiver of all fees associated with this request. I qualify as a representative of the news media under 5 U.S.C. § 552(a)(4)(A)(ii)(II). The requested records will be used to prepare a news article for public distribution by a national aviation trade publication. Disclosure of this information is in the public interest, as it concerns aviation safety oversight, a matter of direct concern to the traveling public. Any fees in excess of duplication costs should be waived as the information is not sought for commercial purposes.

**Expedited Processing**

I request expedited processing under 5 U.S.C. § 552(a)(6)(E), as this investigation concerns aviation safety — a matter in which there is an urgent need to inform the public about actual or alleged federal government activity.

**Response Timeline**

The FOIA statute requires a response within 20 business days of receipt. Please acknowledge receipt of this request in writing. If you anticipate any delay, please notify me immediately.

I am willing to discuss the scope of this request to facilitate prompt processing. Please direct all correspondence to the contact information above.

Sincerely,

Jane Harlow
Investigative Journalist

---

### Example 2: State Public Records Request (Texas)

#### Input
Agency: Texas Department of Criminal Justice
Records wanted: All use-of-force incident reports from the Eastham Unit between July 2024 and June 2025, including staff reports, medical assessments, and any resulting disciplinary actions
State: Texas
Purpose: Investigating use-of-force patterns at a state prison facility
Organization: Staff reporter, regional newspaper in East Texas

#### Output

Marcus Rivera
Staff Reporter, East Texas Herald
[Address]
[City, State, ZIP]
m.rivera@easttexasherald.com
[Phone]

April 3, 2026

Open Records Division
Texas Department of Criminal Justice
P.O. Box 99
Huntsville, TX 77342

**Re: Texas Public Information Act Request — Use-of-Force Records, Eastham Unit, July 2024–June 2025**

Dear Public Information Coordinator,

Pursuant to the Texas Public Information Act, Tex. Gov. Code § 552.001 et seq., I am requesting access to the following records.

**Records Requested**

All use-of-force incident reports generated at the Eastham Unit between July 1, 2024, and June 30, 2025, including but not limited to:

1. Incident reports completed by correctional officers documenting each use of force, including the type of force used, the officer(s) involved, and the circumstances
2. Medical assessments or injury reports generated following each use-of-force incident, for both staff and incarcerated persons
3. Any internal review or disciplinary actions resulting from use-of-force incidents during this period
4. Summary reports or statistical compilations of use-of-force incidents at the Eastham Unit, if maintained

Under § 552.021, government information is public unless specifically excepted. If any responsive records are withheld, please submit a request for an Attorney General ruling under § 552.301 within 10 business days, as required by law.

**Fee Waiver Request**

I request a fee waiver under § 552.267. The requested information is for use by a newspaper and will be used to inform the public about the operations of a state correctional facility. The East Texas Herald qualifies as a representative of the news media.

**Response Deadline**

The Texas Public Information Act requires a response within 10 business days of receipt (§ 552.221). If you intend to withhold any records, you must seek an Attorney General ruling within 10 business days of receiving this request or the records are presumed public.

Please direct all correspondence to the contact information above.

Sincerely,

Marcus Rivera
Staff Reporter, East Texas Herald

**Next Step:** File via the TDCJ Open Records request portal or by mail. Log the submission date. Calendar day 11 for a follow-up if no acknowledgment is received. If the agency seeks an AG ruling, the AG has 45 business days to decide — calendar that too. Texas enforcement is strong; agencies that miss AG ruling deadlines lose the ability to withhold.

---

### Example 3: Administrative Appeal

#### Input
Original request: Filed March 16, 2026, tracking number FAA-2026-00472, to the FAA regarding communications and inspection records for Meridian Aviation Services
Denial: Received April 28, 2026. The FAA released 47 pages with redactions under (b)(5) (deliberative process) and (b)(7)(A) (law enforcement — pending proceedings). 112 pages were withheld entirely under (b)(7)(A).
Why improper: The FAA's enforcement action against Meridian was concluded in January 2026 with a consent order. There are no pending proceedings. The (b)(5) redactions cover emails between inspectors discussing findings — these are factual observations, not policy deliberations.

#### Output

Jane Harlow
Investigative Journalist
[Address]
[City, State, ZIP]
jane.harlow@email.com
[Phone]

May 15, 2026

FOIA Appeals Officer
Federal Aviation Administration
Office of the Chief Counsel, AGC-200
800 Independence Avenue SW
Washington, DC 20591

**Re: Administrative Appeal — FOIA Request FAA-2026-00472, Denied in Part April 28, 2026**

Dear FOIA Appeals Officer,

I am writing to appeal the partial denial of my Freedom of Information Act request, tracking number FAA-2026-00472, dated March 16, 2026. The adverse determination was issued on April 28, 2026. I received 47 pages with redactions under Exemptions (b)(5) and (b)(7)(A), and 112 pages were withheld entirely under (b)(7)(A).

I request that your office reverse this determination for the reasons set forth below.

**Exemption (b)(7)(A) — No Pending Proceedings**

The FAA withheld 112 pages in their entirety and redacted additional material under (b)(7)(A), which protects records whose disclosure "could reasonably be expected to interfere with enforcement proceedings." This exemption requires a pending or reasonably anticipated enforcement proceeding.

The FAA's enforcement action against Meridian Aviation Services concluded in January 2026 with a consent order. There are no pending proceedings. A completed enforcement action cannot support a (b)(7)(A) withholding. I request that all 112 withheld pages be released and that the (b)(7)(A) redactions on the 47 released pages be removed.

**Exemption (b)(5) — Factual Content Is Not Deliberative**

The (b)(5) redactions appear to cover emails between FAA safety inspectors discussing their inspection findings. Factual observations by inspectors — what they saw, what they measured, what conditions they documented — are not deliberative. The deliberative process privilege protects only the agency's decision-making process, not the factual inputs to that process. Facts are segregable from deliberative content and must be released (EPA v. Mink, 1973; Vaughn v. Rosen, 1973).

**Vaughn Index**

I request that the FAA produce a Vaughn Index for all 112 withheld pages and all redacted portions of the 47 released pages. Each withheld document or redaction must be individually described and individually justified by a specific exemption, with enough detail to allow meaningful review.

**Mediation and Litigation**

I am aware of my right to seek mediation through the Office of Government Information Services (OGIS) under 5 U.S.C. § 552(h). If this appeal is denied, I intend to file suit under 5 U.S.C. § 552(a)(4)(B).

The agency is required to respond to this appeal within 20 business days under 5 U.S.C. § 552(a)(6)(A)(ii).

Sincerely,

Jane Harlow
Investigative Journalist

**Next Step:** Send by certified mail and via the agency's online appeal submission portal (if available). Log the submission date. Calendar day 21 for follow-up. If the appeal is denied, consult a media law attorney about filing suit or contact the Reporters Committee for Freedom of the Press for legal assistance.

---

## Known Limitations
- This skill drafts requests and appeals under U.S. law only — federal FOIA (5 U.S.C. § 552) and state public records laws. It is not suitable for records requests in other countries.
- The 50-state table reflects the law as of early 2026. State legislatures amend public records statutes regularly — response deadlines, fee structures, and appeal procedures change. Verify current requirements with the state's attorney general office, press association, or a current legal reference before filing.
- FOIA and state public records laws do not compel agencies to create records, analyze data, or answer questions — only to produce existing documents. If the records do not exist, the agency can legally say so.
- The skill cannot predict agency response times. Federal agencies routinely exceed the statutory 20-day limit. State compliance varies widely. The statutory deadlines are legal tools — they give you grounds to escalate, not guarantees of timely response.
- Journalist fee waiver eligibility depends on how each agency interprets its statute. Freelancers without a formal publication affiliation face challenges at both the federal and state level. Some states have no journalist fee waiver provision at all.
- The redaction analysis and challenge strategies are based on established case law and standard FOIA practice. They are a starting point for an appeal, not legal advice. Complex challenges — particularly those involving classified information, ongoing litigation, or national security claims — should be reviewed by a media law attorney.
- Residency restrictions in seven states (Alabama, Arkansas, Delaware, Kentucky, New Jersey, Tennessee, Virginia) are actively enforced. Workarounds exist but vary in reliability. Consult press freedom organizations (Reporters Committee for Freedom of the Press, Society of Professional Journalists) for current guidance.
- State-level redaction analysis is not covered in the same depth as federal exemptions. State exemption frameworks vary significantly and are less standardized than the federal nine-exemption structure.

## Related Skills
- [source-research-brief](../source-research-brief/SKILL.md)
- [document-analysis-summary](../document-analysis-summary/SKILL.md)
- [investigation-timeline-builder](../investigation-timeline-builder/SKILL.md)
