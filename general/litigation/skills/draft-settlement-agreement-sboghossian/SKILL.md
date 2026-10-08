---
name: draft-settlement-agreement-sboghossian
title: Settlement Agreement
description: Use when drafting a settlement agreement, release, or deed of settlement to resolve an existing or threatened dispute. Covers payment terms, release scope, confidentiality, non-disparagement, and dismissal mechanics across civil-law and common-law jurisdictions including UAE, DIFC, KSA, LB, UK, and EU. Flags non-waivable statutory rights, tax characterization, and the rule that bilateral releases always require dual counsel sign-off before execution.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-settlement-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Settlement Agreement

A settlement agreement is the definitive contractual resolution of a dispute — it replaces the underlying claims with a new set of mutual obligations and typically includes a release of liability. Because it extinguishes legal rights on both sides, it is a "do not execute without dual counsel review" document in every jurisdiction.

## When to use this

- Resolving commercial, employment, property, or personal-injury disputes before or after litigation commences
- Documenting a negotiated resolution of a regulatory investigation (with regulatory counsel)
- Closing out an arbitration by consent award
- Employment exits where the employee releases statutory claims in exchange for enhanced payment (in most MENA jurisdictions this is called a "mutual separation" agreement; in the UK it is a "settlement agreement" replacing the former "compromise agreement")

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Parties (plus third-party beneficiaries / releasees) | Defines who is released and who can enforce | Must provide; consider whether parent/subsidiary/affiliates should be included |
| Underlying dispute description | Grounds the release; parties typically agree on neutral characterization | Neutral factual description without admission |
| Settlement sum + payment terms | Core commercial term | Lump sum on execution; escrow if payer creditworthiness uncertain |
| Release scope | Specific claims listed only, or general release of all claims arising from the defined facts | Mutual general release for commercial disputes |
| Confidentiality | Is the existence and/or amount confidential? | Yes, with carved-out permitted disclosures |
| Non-disparagement | Mutual or one-way? | Mutual for employment settlements |
| Pending litigation | Is there a filed case that needs to be dismissed? | Dismissal with prejudice (bars relitigation) |
| Governing law | Determines non-waivable rights, tax treatment, enforcement | Jurisdiction where dispute arose or where Defendant operates |

## Optional inputs

- Cooperation clause (transition assistance, future litigation cooperation)
- Reference letter terms for employment settlements
- Regulatory reporting obligations
- Treatment of existing injunctions or interim orders
- Clawback provision (if settlement payments are contingent on ongoing cooperation)

## Document Structure

1. **Recitals** — brief, neutral description of the dispute and the parties' decision to settle without admission of liability; identify any pending proceedings by case number
2. **Settlement payment** — amount in figures and words; due date (typically 5-15 business days from execution); payment instructions; currency; allocation across causes (important for tax); late-payment interest at a specified rate
3. **Release** — the most negotiated clause:
   - Identify the releasing party / released party precisely
   - Specify whether the release is mutual or one-way
   - Define the scope: specific listed claims AND/OR all claims arising from the defined facts / dispute
   - Include "known and unknown" language where the jurisdiction permits waiver of unknown claims
   - Carve-outs: vested pension rights; indemnification rights under D&O or directors' indemnity; personal injury claims not yet manifested (jurisdiction-specific)
4. **No admission of liability** — standard; neither execution nor payment constitutes an admission
5. **Confidentiality** — strict mutual obligation; permitted disclosures to: tax advisors, legal counsel, auditors, regulatory bodies on compulsion, court (if enforcement required), and internal compliance officers on need-to-know basis; no social media or press disclosure
6. **Non-disparagement** — mutual; define as no public or private statements that would reasonably harm the other party's reputation or business relationships
7. **Withdrawal of proceedings** — if litigation is filed: mechanism for filing a consent order of dismissal with prejudice; allocate responsibility for filing; timing (typically concurrently with or on receipt of payment); cost orders
8. **Compliance with regulators** — if applicable (sanctions, antitrust, professional regulation); settlement does not affect any regulatory proceedings
9. **Tax treatment** — settlement is paid without withholding or tax gross-up unless expressly agreed; allocate settlement proceeds across employment income, damages, costs where relevant to the payer's deductibility and payee's taxable income
10. **Governing law and dispute resolution** — enforce the settlement itself through courts or arbitration (arbitration clause for multinational settlements)
11. **Entire agreement + amendment** — supersedes all prior negotiations and agreements; amendments in writing signed by both parties
12. **Counterparts and electronic signature** — document may be executed in counterparts; electronic signature valid where jurisdiction permits (DIFC, UK, US widely; UAE onshore increasingly)

## Release Scope — Getting It Right

The release is the instrument's commercial core. The key tensions:

| Issue | Releasing party wants | Released party wants |
|---|---|---|
| Scope | Narrow (only listed claims) | Broad (all claims from this relationship) |
| Known/unknown | Known claims only | Known and unknown |
| Time period | Claims arising to execution date | All claims from beginning of time |
| Related parties | Individual releasee only | Affiliates, officers, employees, agents |
| Carve-outs | Statutory rights, pension, personal injury | No carve-outs |

Best practice: define the "Released Claims" as a defined term in the definitions section, then use that defined term in the operative release clause — this avoids ambiguity when the release refers back.

## Jurisdictional Notes

### Non-waivable statutory rights

Several MENA jurisdictions protect certain claims from contractual waiver:

- **Lebanon**: End-of-service indemnity under Labor Code Article 50 cannot be waived in advance; waiver of amounts actually due at the time of settlement is permissible. Consumer protection rights (as applicable) cannot be waived.
- **KSA**: End-of-service award (EOSA) accrued rights cannot be waived. Settlement agreements in labor matters before the Labor Courts may require court approval to be effective against statutory rights.
- **UAE federal**: End-of-service gratuity (EOSG) under Decree-Law 33/2021 cannot be waived; settlement of amounts already accrued is permissible. Payments may require Ministry of Human Resources (MoHRE) clearance for expatriate visa cancellation.
- **DIFC**: DIFC Employment Law statutory minimum entitlements (EOSG under DEWS, notice, accrued leave) cannot be contractually waived below the minimum.
- **EU**: Consumer rights under Directive 2011/83/EU and national implementations cannot be waived by contract. Class action waiver provisions are void against EU consumers.
- **UK**: For employment settlements, the statutory requirements of a valid "settlement agreement" (formerly "compromise agreement") must be met: must be in writing, relate to a particular complaint, employee must receive independent legal advice, adviser must be identified and insured.

### Tax characterization matters

The allocation of settlement proceeds between different heads of loss has significant tax consequences:
- **Lost profits / business damages**: typically revenue receipt, taxable
- **Capital destruction / asset loss**: may be capital in nature
- **Employment discrimination / personal injury**: tax-free in many jurisdictions (UK, US) up to certain amounts
- **Costs awards**: deductible for payer; receipt taxable in some jurisdictions
- Getting the allocation wrong (or leaving it unspecified) can increase the after-tax cost of the settlement for one or both parties.

### Future claims and unknown claims

Under civil-law systems (LB, FR, UAE onshore), it is generally not possible to waive claims that do not yet exist or are not yet known — the general prohibition on contracting about future uncertain events limits the breadth of a release. Under common law (DIFC, ADGM, UK, US), a broad "known and unknown claims" waiver is generally enforceable with appropriate consideration, provided the releasing party understood the scope.

### Effective date vs payment date

Release effective only upon receipt of cleared funds is the standard for the payee. The payer prefers release on execution. The commercial solution: escrow (funds held by neutral third party, released to payee against evidence of executed and delivered release, with return to payer if settlement is not completed by a longstop date).

## Drafting Standards

- Use neutral characterization of the dispute in recitals — do not describe conduct as "wrongful," "fraudulent," or otherwise characterize liability; this is an admission in disguise
- Define "Released Claims" as a defined term and use it consistently
- Specify whether the settlement is intended to constitute full and final settlement of all disputes between the parties or only the enumerated dispute — overly broad full-and-final language may bar future unrelated claims unintentionally
- Include a clause that the settlement agreement itself may be produced in court proceedings solely to enforce its terms (notwithstanding the confidentiality clause) — without this, the confidentiality clause may prevent enforcement

## Do Not Draft Without

This document should always be reviewed by counsel of both sides before execution. The drafting lawyer's duty is to alert the client to:
- Claims that cannot be released under the applicable law
- Tax implications of the settlement allocation
- Whether the consideration is adequate for the release given (particularly for consumer or employment releases)

## Related skills

- [[draft-severance-agreement]]
- [[draft-statement-of-defense]]
- [[review-litigation-risk]]
- [[draft-nda-mutual]]
- [[kb-litigation-procedure-mena]]
