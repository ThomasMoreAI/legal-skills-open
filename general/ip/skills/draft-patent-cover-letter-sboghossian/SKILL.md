---
name: draft-patent-cover-letter-sboghossian
title: Patent Application Cover Letter
description: Use when drafting a cover letter for a patent application submission to a national or regional patent office — USPTO, EPO, PCT (WIPO), GCC Patent Office, SAIP (Saudi Arabia), UAE federal, or Lebanese MOET. Covers required components, priority claim mechanics, document list, power of attorney, publication requests, and MENA-specific filing requirements. Triggers on "patent application", "patent cover letter", "patent filing", "filing a patent", or "patent submission" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-patent-cover-letter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Patent Application Cover Letter

## When to use this

A patent application cover letter accompanies the formal patent application documents when they are submitted to a patent office. It identifies the application, confirms the enclosures, makes any required declarations, and transmits payment. While the cover letter itself is not the legally critical component (the claims, specification, and drawings are), it is the administrative instrument through which the filing is made official — errors here cause filing date losses, which can be catastrophic for priority.

This skill covers the cover letter. It does not cover drafting the patent claims (which requires a qualified patent attorney and deep technical analysis) or the patent specification. AI can assist with the cover/structural materials but claim language demands specialist input.

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Applicant (and inventors) | Legal identification; must match the assignment chain if applicant ≠ inventor |
| Title of invention | Exact title as used in the specification and claims |
| Jurisdiction (patent office) | Each office has its own form requirements |
| Type of application | Utility / design / plant (US); or equivalent |
| Priority claim | If claiming priority from an earlier national filing (12-month window under Paris Convention) |
| Power of Attorney | Required for foreign counsel to act before the office |
| Filing date target | Determines urgency and whether rush filing fees apply |

## Optional inputs
- Request for non-publication (USPTO only — available if no foreign filing is contemplated)
- Provisional application reference (for US non-provisional claiming benefit of a provisional)
- Claims to small-entity or micro-entity fee status (USPTO)
- Specific examiner request (rarely granted but permissible in some offices)

## Cover letter content — standard elements

### 1. Office heading
```
[Full name of patent office]
[Address / online submission portal reference]
Date: [Date of filing]
```

### 2. Applicant and inventor identification
```
Applicant:     [Full legal name of Applicant, if different from inventor]
Inventor(s):   [Full legal name(s) of all inventors]
Address:       [Applicant's mailing address]
Email:         [Applicant / Agent contact]
Agent/Attorney:[Name, registration number, address — if filing through a patent agent]
```
If the applicant is a company and not the inventor: the assignment from the inventor(s) to the applicant must have been executed before filing (or simultaneously) and should be referenced here.

### 3. Title of invention
State exactly: "Title of Invention: [Exact title as in the specification]."

### 4. Type of filing
Specify precisely:
- US: "Non-provisional utility patent application under 35 U.S.C. § 111(a)" or "PCT national phase entry under 35 U.S.C. § 371"
- EPO: "European patent application under Article 75 EPC"
- PCT: "International application under Article 11 of the Patent Cooperation Treaty"
- GCC / national: "Patent application under [applicable Law]"

### 5. Priority claim
If the application claims priority from an earlier filing:
```
Priority claim:
   Earlier application number: [Application No.]
   Filing date of earlier application: [Date — Gregorian and Hijri if KSA]
   Country/office of earlier application: [Country]
   Paris Convention priority under Article 4 PCT / Article 87 EPC
```
**Critical timing**: The Paris Convention 12-month priority window runs from the earliest filing date. Missing this deadline permanently loses the priority benefit. Flag this urgency at the top of any filing communication.

### 6. List of accompanying documents
Enumerate every document enclosed — the office will use this to verify completeness:
1. [Title page / cover sheet / Form PTO-1390 or equivalent]
2. Abstract [page count]
3. Specification (description) [page count]
4. Claims [number of independent and dependent claims]
5. Drawings / figures [number of sheets; figures numbered]
6. Oath or Declaration of Inventorship [signed; inventors identified]
7. Power of Attorney [signed by Applicant / Inventors]
8. Priority document [certified copy of earlier application, if available; or request to retrieve from WIPO DAS]
9. [Any assignment document, if Applicant ≠ Inventor]
10. Payment tender: [amount; payment method — credit card authorization / check / deposit account]

### 7. Power of Attorney (POA)
When a patent agent or attorney is filing on behalf of the applicant:
- The POA authorizes the agent to act before the specified patent office in connection with this application
- Must be signed by each named Applicant (or by the corporate officer with authority)
- Some offices (USPTO) require a new POA per application; others (EPO) allow a general authorization

### 8. Publication request / non-publication request
**Standard**: patent applications publish 18 months from the earliest priority date. This is automatic under PCT and EPO.

**Non-publication request** (US only): If the applicant does not intend to file outside the US, a non-publication request may be filed concurrently with a US non-provisional application. If the applicant later decides to file internationally, the non-publication request must be rescinded. Important: if a non-publication request is filed and the applicant later files abroad without rescinding, the US application goes abandoned. Track carefully.

### 9. Fee tender
- Identify the applicable fee schedule and amounts: USPTO schedules vary by entity size (large entity / small entity / micro entity)
- Specify payment: "Applicant hereby authorizes charge to Deposit Account No. X for all applicable fees" or enclose check / credit card authorization
- List each fee component: basic filing fee; search fee; examination fee; claims fees for excess independent/dependent claims

### 10. Certification / signature
Signed by:
- The patent attorney / agent (if any)
- Or the Applicant directly (for pro se filings — very rare for commercial applicants)
"I hereby certify that the attached application and documents are being transmitted to [Office] on [Date]."

## Jurisdictional notes

| Office | Key requirements |
|---|---|
| **USPTO** | 35 U.S.C. (Patent Statute); 37 C.F.R. (Patent Rules); USPTO Application Data Sheet (ADS) is the modern cover sheet; non-provisional must be filed within 12 months of any provisional; non-publication request available; electronic filing via EFS-Web / Patent Center required for agents |
| **EPO** | European Patent Convention; designation of EPC Contracting States must be included; EP application results in a bundle of national patents upon grant; language requirements (English, French, or German); European Patent Attorneys must be registered with EPO |
| **PCT (WIPO)** | Patent Cooperation Treaty international application; 30-month national phase entry window (from earliest priority date) in each designated state; e-filing via ePCT portal; search and examination by designated International Searching Authority (ISA) |
| **GCC Patent Office (Riyadh)** | Regional patent protection across GCC member states; Arabic language required; national representative in Riyadh required for foreign applicants; GCC patent grants patent protection in all GCC member states simultaneously |
| **Saudi SAIP** | Saudi Authority for Intellectual Property; national filings; Arabic language application; Saudi patent agent required for foreign applicants; Industrial Property Protection Law (Royal Decree M/27/1425) governs |
| **UAE federal (MOEC)** | Ministry of Economy patents office; Federal Law on Industrial Property; Arabic application; UAE registered agent; filing in Arabic with translation if originally in another language |
| **Lebanon (MOET)** | Ministry of Economy and Trade intellectual property office; Law 240/2000 on patents; Arabic or French filings accepted; Lebanese IP attorney recommended; less established examination process than GCC/EPO |

## Best practices

- **Priority deadline is hard**: the 12-month Paris Convention window from the earliest filing date is absolute — no extension available except in extraordinary circumstances in some offices. Calendar this immediately upon any national filing.
- **Inventors must be correctly named**: inventor is the person who conceived the invention; failing to name all inventors (or naming non-inventors) can invalidate the patent in many jurisdictions — especially the US
- **Foreign filing licence** (UK, France, other countries): some countries require a foreign filing licence before filing abroad; the home country office issues it (or it is deemed granted after a period). Relevant for applications originating in France or UK before PCT filing.
- **AI-generated inventions**: as of 2025, most patent offices require a human inventor; AI cannot be listed as an inventor. If AI tools were used in the inventive process, disclose appropriately in accordance with current guidance from the relevant office.
- **Claim drafting**: the cover letter is administrative; the claims are the legal scope of the patent. Do not rely on this skill to draft patent claims — engage a qualified patent attorney.

## Common mistakes

- Wrong filing date: the date the complete application (with all required parts) is received by the office determines the filing date — an incomplete filing gets a later date
- Missing assignment from inventor to corporate applicant before filing — creates ownership gaps
- Non-publication request combined with later foreign filing without rescission — automatic abandonment of US application
- Incorrect fee payment: under-payment (wrong entity size) → office action; over-payment can usually be credited but requires follow-up

## Related skills

- [[draft-ip-licensing]]
- [[draft-ip-assignment]]
- [[review-ip-clearance]]
- [[draft-licensing-agreement]]
