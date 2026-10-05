---
name: rti-application-drafter-shashionline
title: RTI Application Drafter
description: Draft complete, legally precise RTI applications under Right to Information Act 2005 with specific information requests, proper addressing, and compliance with statutory format
author: shashionline
author_url: https://github.com/shashionline/indian-law-plugin/tree/master/skills/rti-application-drafter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: in
practice: administrative
language: en
---

# RTI Application Drafter

## Purpose
Generate legally compliant RTI applications under Right to Information Act 2005 with specific information requests, proper format, correct fee calculation, and statutory timeline invocation.

## Skill Workflow

### Step 1: Gather Application Parameters

When invoked, collect the following from user (or infer from context):

**Required**:
1. **Public Authority**: Which department/ministry/PSU/local body?
   - Examples: "Ministry of Home Affairs", "Delhi Municipal Corporation", "ONGC"

2. **Information Sought**: What specific information does user need?
   - Must be SPECIFIC (not vague "all files")
   - Numbered points preferred
   - Include timeframe if applicable

3. **Applicant Details**:
   - Name
   - Address
   - Phone/Email (for PIO to respond)

**Optional**:
4. **PIO Address**: If user knows specific PIO address (otherwise use generic)

5. **BPL Status**: Is applicant Below Poverty Line? (Fee exemption)

6. **Life/Liberty Matter**: Does information concern life or liberty? (48-hour timeline under Section 7(1) proviso)

7. **Form of Information**: How does user want information?
   - Certified copies (default)
   - Inspection of records
   - Electronic form (email/CD)
   - Photocopies

### Step 2: Validate Information Request Specificity

**Check if information request is SPECIFIC enough**:

**Too Vague** (Will be rejected/delayed):
- ❌ "Give all files on X project"
- ❌ "Provide complete information about scheme"
- ❌ "Send all correspondence related to my case"

**Good Specificity** (Likely to succeed):
- ✅ "Provide copy of project approval note dated [approx date] for X project"
- ✅ "Number of beneficiaries of X scheme in [district] during FY 2023-24, with total amount disbursed"
- ✅ "List of tenders awarded by department in [period] with contractor names and contract values"

**If User's Request Too Vague**: Prompt user to be more specific OR refine on their behalf:
- "Instead of 'all files', can you specify: approval orders, budget documents, contractor list?"
- "Instead of 'scheme information', what specifically: beneficiary count, fund allocation, implementation status?"

### Step 3: Determine Fee

**Central Government**: ₹10 (IPO/DD in favor of "Accounts Officer, [Ministry/Department]")

**State Government**: Varies by state (₹10-50 typically)
- Check state RTI rules (if known)
- If unknown, mention "₹10 or as applicable as per state RTI rules"

**BPL Applicants**: Fee WAIVED (Section 7(5))
- If user is BPL, mention: "Fee exempted as applicant is BPL (certificate enclosed)"

**Below Poverty Line**: If user mentions BPL status, include fee exemption clause

### Step 4: Draft RTI Application

Use the following template structure:

```
To,
The Public Information Officer
[Name of Department/Ministry/PSU/Local Body]
[Address - if known, otherwise generic: "Registered Office" or check authority website]

Subject: Application under Right to Information Act, 2005

Dear Sir/Madam,

Under the Right to Information Act, 2005, I request the following information from your office:

[INFORMATION POINTS - Numbered list, specific]

1. [Specific information request - point 1]
   [Add clarification if needed: e.g., "certified copy of", "number of", "list of", "date of"]

2. [Specific information request - point 2]

3. [Specific information request - point 3]

[Continue numbering - typically 3-7 points optimal, not more than 10]

**Period for which information sought**: [Specify timeframe: "Financial Year 2023-24" OR "From January 2023 to December 2023" OR "As on date" if current status]

**Form in which information sought**: [Certified copies / Photocopies / Inspection of records / Electronic form (email/CD)]

[IF LIFE/LIBERTY MATTER - Section 7(1) proviso]:
This RTI application concerns information relating to life and liberty of [person/applicant]. Under the proviso to Section 7(1) of the Right to Information Act, 2005, the Public Information Officer is required to provide the information within 48 hours of receipt of this application.

[FEE CLAUSE - STANDARD]:
I am enclosing [₹10 / applicable fee] as application fee by way of [Indian Postal Order / Demand Draft / Court Fee Stamp] [if IPO/DD: "in favor of 'Accounts Officer, [Ministry/Department]'"].

[IF BPL - Section 7(5)]:
I am a Below Poverty Line (BPL) applicant. BPL certificate issued by [Issuing Authority] on [date] is enclosed. As per Section 7(5) of the RTI Act, 2005, fee is exempted for BPL applicants.

[TIMELINE CLAUSE - STANDARD]:
Please provide the information within 30 days as mandated under Section 7(1) of the Right to Information Act, 2005.

[IF THIRD PARTY INFO POSSIBLE]:
If the information sought pertains to or has been supplied by a third party, kindly follow the procedure under Section 11 of the RTI Act.

[IF PIO NOT CORRECT - Section 6(3)]:
If the information sought does not pertain to your office, kindly transfer this application to the concerned Public Information Officer under Section 6(3) of the RTI Act and inform me of such transfer.

Thanking you,

Yours faithfully,

[Applicant Name]
[Complete Address]
[Phone Number]
[Email Address]
Date: [Current Date]

Enclosures:
1. [IPO/DD for ₹10 / Court Fee Stamp of ₹10 / BPL Certificate (if BPL)]
[If supporting documents needed: 2. Copy of [relevant document], 3. ...]
```

### Step 5: Add Application-Specific Guidance

After drafting, provide user with:

**Submission Instructions**:
1. **Mode of Submission**:
   - **In Person**: Visit PIO office during working hours, submit, obtain acknowledgment
   - **By Post**: Speed Post / Registered Post with Acknowledgment Due
   - **Online**: Some departments have online RTI portals (mention if applicable)

2. **Track Application**:
   - Keep copy + postal receipt / acknowledgment
   - If no reply in 30 days (or 48 hours if life/liberty), file First Appeal

3. **If PIO Misdirects (Section 6(3))**:
   - PIO should inform you if application transferred
   - If not informed, file RTI to original PIO asking transfer details

4. **Expected Timeline**:
   - **Normal**: 30 days from receipt
   - **Life/Liberty**: 48 hours
   - **If delay**: File First Appeal within 30 days OR within 45 days of filing RTI (if no response)

**Common Mistakes to Avoid**:
- ❌ Not keeping copy of RTI + postal receipt
- ❌ Being too vague in information request
- ❌ Not following up after 30 days
- ❌ Sending to wrong PIO (if unsure, send to head office, they should transfer)

### Step 6: Output Complete Application

Provide user with:
1. **Complete RTI Application Text** (ready to print)
2. **Submission Checklist**:
   - [ ] RTI application printed and signed
   - [ ] Fee attached (IPO/DD/Stamp) OR BPL certificate
   - [ ] Address envelope to PIO
   - [ ] Send by Registered Post / Submit in person
   - [ ] Keep copy + postal receipt
3. **Next Steps Timeline**:
   - Day 0: Submit RTI
   - Day 30 (or 48 hrs): PIO must respond
   - Day 31-45: File First Appeal if no response
   - Day 60: FAA must decide appeal
4. **Sample Appeal Format** (for reference, if PIO denies):
   ```
   If PIO denies/delays, file First Appeal to First Appellate Authority within 30 days.

   Format:
   To,
   The First Appellate Authority
   [Department]

   Subject: First Appeal under Section 19(1) of RTI Act, 2005

   Sir/Madam,

   I filed RTI application dated [date] seeking [brief description].

   The PIO [did not respond / denied citing Section 8 / provided incomplete information].

   Ground of Appeal: [PIO's denial is incorrect because...]

   Prayer: Direct PIO to provide information + impose penalty under Section 20.

   [Signature]
   Date: [Date]
   ```

## Reference Information

### Common Public Authorities & PIO Addresses

**Central Government** (Examples):
- Ministry of Home Affairs: PIO, Ministry of Home Affairs, North Block, New Delhi - 110001
- Ministry of External Affairs (Passport): PIO, Passport Seva, Patiala House Annexe, New Delhi
- EPFO: PIO, Employees' Provident Fund Organisation, Bhavishya Nidhi Bhawan, New Delhi
- Indian Railways: PIO, [Zonal Railway - e.g., Northern Railway, Baroda House, New Delhi]

**State Government**:
- Usually: PIO, [Department Name], [State Secretariat Address]
- District Level: PIO, Office of District Collector, [District]

**Local Bodies**:
- Municipal Corporation: PIO, [City] Municipal Corporation, [Address]
- Gram Panchayat: Gram Panchayat Secretary (usually designated PIO), [Village]

**PSUs**:
- ONGC, LIC, Air India, etc.: Check official website RTI section

**If PIO Address Unknown**: Use generic address (department's registered office) and rely on Section 6(3) transfer.

### Information That Can Be Sought

**✅ RTI Covers** (Examples):
- Government files, notings, correspondence
- Policies, circulars, orders
- Contracts, tenders awarded
- Budget allocations, expenditure
- Inspection reports
- Statutory records (birth, death, property)
- Public servant salaries, attendance, disciplinary records
- Reasons for government decisions
- Status of applications/cases

**❌ RTI Does NOT Cover**:
- Information exempt under Section 8 (security, commercial confidence, personal privacy, etc.)
- Information from private companies (unless "public authority")
- Courts/judiciary records
- Future decisions (RTI is for existing information)
- Opinions/interpretations (ask for records, not PIO's opinion)

### Section 8 Exemptions (Quick Reference)

If PIO cites exemption, check if valid:
1. **8(1)(a)**: Security, sovereignty (narrow - only strategic info)
2. **8(1)(d)**: Commercial confidence (third-party trade secrets)
3. **8(1)(e)**: Fiduciary relationship
4. **8(1)(j)**: Personal information (but public servant service info NOT exempt)

**Public Interest Override** (Section 8(2)): Even if exempt, disclosure in public interest overrides (except 8(1)(a) security info).

## Skill Invocation Example

**User Request**: "Draft RTI application to Ministry of Railways asking about contractor awarded contract for platform construction at Delhi station"

**Skill Output**:
```
To,
The Public Information Officer
Ministry of Railways
(Northern Railway)
Baroda House, New Delhi - 110001

Subject: Application under Right to Information Act, 2005

Dear Sir/Madam,

Under the Right to Information Act, 2005, I request the following information from your office:

1. Name and complete address of the contractor awarded the contract for platform construction/renovation at New Delhi Railway Station during the period January 2023 to December 2023.

2. Contract value awarded to the said contractor.

3. Date of contract award and expected date of completion as per contract.

4. Copy of the work order/contract agreement issued to the contractor (certified copy).

5. Number of contracts awarded to the same contractor by Northern Railway in the last 3 years (2021-2023) with brief description of work and contract values.

**Period for which information sought**: January 2023 to December 2023 (for point 1-4); 2021-2023 (for point 5)

**Form in which information sought**: Certified copies of documents (point 4); tabulated information (point 1, 2, 3, 5)

I am enclosing ₹10 as application fee by way of Indian Postal Order in favor of 'Accounts Officer, Northern Railway'.

Please provide the information within 30 days as mandated under Section 7(1) of the Right to Information Act, 2005.

If the information sought pertains to or has been supplied by a third party, kindly follow the procedure under Section 11 of the RTI Act.

If the information sought does not pertain to your office, kindly transfer this application to the concerned Public Information Officer under Section 6(3) of the RTI Act and inform me of such transfer.

Thanking you,

Yours faithfully,

[User Name]
[User Address]
[User Phone]
[User Email]
Date: [Current Date]

Enclosures:
1. Indian Postal Order for ₹10
```

**Submission Checklist**:
- [ ] RTI application printed and signed
- [ ] ₹10 IPO attached (in favor of "Accounts Officer, Northern Railway")
- [ ] Envelope addressed to PIO, Ministry of Railways, Northern Railway, Baroda House, New Delhi - 110001
- [ ] Send by Registered Post (keep postal receipt)
- [ ] Keep photocopy of entire application

**Timeline**:
- Day 0: Submit RTI
- Day 30: Railways PIO must respond
- Day 31-45: File First Appeal to FAA if no response

## Quality Assurance

Before finalizing RTI application, verify:
- [ ] Information requests are SPECIFIC (not vague)
- [ ] Public authority correctly identified
- [ ] Fee clause included (with correct amount) OR BPL exemption
- [ ] Section 7(1) timeline mentioned (30 days OR 48 hours if life/liberty)
- [ ] Applicant details complete (name, address, contact)
- [ ] Section 6(3) transfer clause included
- [ ] Section 11 third-party clause included (if applicable)
- [ ] Enclosures list matches fee/documents attached

## Integration with Agents

This skill is invoked by:
- **rti-specialist** agent when user requests RTI application drafting
- **india-civic-law-specialist** orchestrator for RTI matters

The skill returns complete RTI application text that user can directly print and submit.

---

**RTI is a fundamental right under Article 19(1)(a). This skill empowers citizens to exercise transparency rights with legally precise applications.**
