---
name: initial-contact-summary
title: Initial Contact Summary
description: Generates a structured initial contact summary memorandum from a potential client's first interaction with the firm. Captures case facts, liability indicators, damages, insurance details, and screening criteria. Use during client intake to support conflict checks, case evaluation, and engagement decisions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/initial-contact-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: personal-injury
language: en
tags: [litigation, summarization, summary]
---

# Initial Contact Summary

Produces a privileged internal memo from a potential client's first contact — the foundation for conflict checking, case evaluation, and engagement decisions. Mark all output as **PRIVILEGED AND CONFIDENTIAL**.

## Required Inputs

Gather from intake interview, referral, or initial documents:

1. **Contact info** — name, phone, email, address, preferred contact method
2. **Incident details** — date, location, description of events
3. **Injuries/damages** — physical, financial, emotional, property
4. **Parties involved** — opposing parties, witnesses, employers, insurers
5. **Insurance** — client's and adverse party's coverage
6. **Prior legal actions** — existing attorneys, filed claims, administrative complaints
7. **Referral source** — how client found the firm
8. **Statute of limitations** — calculate deadline; flag if < 6 months

## Output Sections

### 1. Contact Information

Table with: Name, Phone, Email, Address, Preferred contact, Intake date, Intake by, Referral source.

### 2. Conflict Check

- List all parties to check: potential client, opposing parties, employers, insurers, witnesses, related entities (parent companies, subsidiaries)
- Flag: conflict check **completed** or **pending**

### 3. Incident Summary

- Date/time, location (address + jurisdiction), matter type
- Chronological narrative in client's own words (use quotation marks for key statements)
- Police/incident report: number, agency, obtained/requested status

### 4. Liability Assessment

- Client's theory of fault
- Adverse party conduct (specific negligent/wrongful acts)
- Comparative fault concerns
- Available evidence: photos, video, documents, electronic data
- Witnesses: names, contact info, relationship, anticipated testimony
- Preservation needs: surveillance footage, vehicles, medical devices — **flag deadlines**

### 5. Damages

**Physical**: injuries, treatment to date (providers, facilities), ongoing needs, pre-existing conditions

**Economic**: medical expenses (current + estimated future), lost wages (dates, rate, employer), property damage, out-of-pocket costs

**Non-economic**: pain/suffering indicators, daily activity impact, emotional distress factors

### 6. Insurance

Table with rows for Client, Adverse, and UM/UIM. Columns: Carrier, Policy #, Limits, Claim #, Adjuster.

### 7. Critical Dates

- Date of incident
- **Statute of limitations** — calculate and prominently display; **flag if < 6 months**
- Government claim deadline (if applicable)
- Insurance claim deadline
- Evidence preservation deadline

### 8. Screening Assessment

- **Case strength**: Strong / Moderate / Weak — with brief explanation
- **Damages potential**: High / Medium / Low
- **Recommended action**: Accept / Decline / Further investigation needed
- **Conflicts**: Clear / Potential conflict identified

### 9. Follow-Up Checklist

- [ ] Conflict check completed
- [ ] Statute of limitations calendared
- [ ] Evidence preservation letter sent
- [ ] Medical records authorization obtained
- [ ] Police report requested
- [ ] Insurance claims filed/confirmed
- [ ] Engagement letter prepared
- [ ] Declined letter prepared (if not accepting)

## Pitfalls

- **Statute of limitations**: always calculate and display prominently — missed deadlines are malpractice risk
- **Conflict check gaps**: include all parties and related entities, not just named opponents
- **Narrative inconsistencies**: flag contradictions for follow-up rather than resolving them
- **Declining representation**: document reason and confirm declination letter includes limitations warning
- **Client demeanor**: note emotional state and communication style — relevant to case evaluation
