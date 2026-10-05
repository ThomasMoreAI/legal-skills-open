---
name: nda-review-open-legal-products
title: NDA Review
description: Review the uploaded non-disclosure agreement and produce a comprehensive table-based legal review from the perspective of the party represented by the user/client.
author: open-legal-products
author_url: https://github.com/open-legal-products/mike-workflows/tree/main/assistant-workflows/nda-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# NDA Review

## Instructions

Review the uploaded non-disclosure agreement and produce a comprehensive table-based legal review from the perspective of the party represented by the user/client. If the user has not already identified which party they represent, ask them to clarify that party before producing the review.

Once the represented party is clear, provide exactly one Markdown result table. Use one row for each material issue found in the agreement, guided by the review checklist below, and add a final row called **Overall Risk Rating**. The result table must have exactly these columns:

- Issue
- Summary
- Recommended Change

Use these risk ratings inside the **Summary** column: Low means standard or minimal concern; Medium means a manageable negotiation concern; High means a material legal, commercial, operational, or enforceability concern requiring negotiation; Critical means a severe issue that may block signing unless resolved. Start each summary with the risk rating, e.g. "High - confidential information definition is too narrow".

The **Summary** column should include only the relevant points from the **General** checklist column and the party-specific checklist column for the represented party, together with clause references where available. Do not include issues that are adverse only to another party unless they also create risk for the represented party. The **Recommended Change** column must be drafted from the represented party's perspective. Also flag general drafting errors that may affect the represented party, including inconsistent defined terms, inconsistent entity names, cross-reference errors, numbering issues, duplicated provisions, missing schedules, and internal inconsistencies. Keep the response concise and avoid long prose outside the table.

## Result Table Format

Use this result table structure. Cite the relevant clause, section, schedule, or page directly in the **Summary** and **Recommended Change** columns. The example rows are illustrative only; tailor the actual rows to the uploaded agreement and represented party.

| Issue | Summary | Recommended Change |
| --- | --- | --- |
| Definition of Confidential Information | Medium - Clause [x] covers broad categories of information but does not clearly address oral disclosures. The general definition point and the disclosing-party checklist point indicate a protection gap. | For the disclosing party, add oral and visual disclosures and require written confirmation within a defined period. |
| Drafting Consistency | Medium - Clauses [x] and [y] use inconsistent defined terms or party names. The general drafting point indicates ambiguity that may affect the represented party's rights or obligations. | For the represented party, align the defined terms, party names, numbering, and cross-references before signing. |

## Review Checklist

Use this checklist as guidance for what to review and flag. It is not the result-table template and should not be reproduced verbatim. For each checklist issue, consider both the **General** column and the party-specific column for the represented party (Disclosing Party or Receiving Party).

| Issue | General | Disclosing Party | Receiving Party |
| --- | --- | --- | --- |
| Parties | Identify each party and their role. Confirm whether the NDA is mutual or one-way and that obligations are correctly allocated. Flag missing affiliates, mismatched roles, or obligations inconsistent with the agreed structure. | | |
| Purpose | Summarize the permitted purpose for which confidential information may be used. | Flag overly broad purpose language that permits use beyond the intended transaction. | Flag unclear or narrow purpose that prevents legitimate use of information in connection with the transaction. |
| Definition of Confidential Information | Explain what information is protected, including oral, visual, derived, or pre-existing information. | Flag definitions too narrow to protect all disclosed information, or no protection for oral or unmarked information. | Flag definitions overbroad, capturing publicly available information or information not actually sensitive. |
| Exclusions | Identify standard exclusions such as public domain, independently developed, already known, or third-party received information. | Flag missing standard exclusions that would allow the receiving party to escape obligations too easily. | Flag missing standard exclusions (public domain, independently developed, already known) or exclusions that are too difficult to prove. |
| Disclosure Obligations | Summarize confidentiality obligations, standard of care, and use or disclosure restrictions. | Flag standards of care too weak to adequately protect the information. | Flag strict liability, vague standards, or obligations higher than own-information standards that expose the receiving party disproportionately. |
| Permitted Recipients | Identify who may receive confidential information, including affiliates, representatives, advisers, financing sources, or investors. | Flag recipient categories too broad, or no requirement for recipients to be bound by equivalent obligations. | Flag missing adviser, affiliate, or financing source access rights needed to evaluate the transaction. |
| Recipient Liability | State whether the receiving party is responsible for breaches by permitted recipients. | Flag absence of receiving party responsibility for breaches by permitted recipients. | Flag uncapped liability for actions of recipients outside the party's direct control. |
| Compelled Disclosure | Summarize disclosure required by law, regulation, court order, stock exchange, or governmental authority. | Flag no notice right, no cooperation obligation, or overly broad compelled disclosure permissions. | Flag overly burdensome notice requirements or obligations to resist disclosure beyond what is practicable. |
| Term | State the agreement term and the duration of confidentiality obligations. | Flag obligations that expire too soon or unclear continuation of obligations after agreement end. | Flag indefinite obligations or unusually long terms for non-trade-secret information. |
| Return or Destruction | Summarize return, destruction, retention, and archival copy obligations. | Flag no return obligation or inadequate destruction mechanics. | Flag no carve-out for archival, compliance, backup, or legal retention copies. |
| Residual Knowledge | Identify whether unaided memory or residual knowledge may be used. | Flag broad residual knowledge rights that could undermine confidentiality protections. | Flag absence of a residual knowledge carve-out that prevents legitimate use of unaided memory. |
| Non-Solicit / Standstill | Identify non-solicitation, non-circumvention, standstill, exclusivity, or similar restrictions. | Flag absence of non-solicitation or standstill protections where commercially expected. | Flag hidden restrictive covenants, long durations, broad covered persons, or restrictions unrelated to confidentiality. |
| No Warranty / No Obligation | Summarize disclaimers about accuracy, completeness, warranties, or obligation to proceed. | Flag missing disclaimers that could create liability for the accuracy or completeness of disclosed information. | Flag disclaimers that conflict with fraud or intentional misrepresentation, or that expressly exclude reliance. |
| Remedies | Identify injunctive relief, equitable remedies, indemnities, liquidated damages, or enforcement provisions. | Flag absence of injunctive relief or inadequate remedies for breach. | Flag automatic injunction language, broad indemnities, or liquidated damages without adequate safeguards. |
| Assignment | Summarize restrictions on assignment or transfer. | Flag free assignment rights that could transfer obligations to unknown parties. | Flag restrictions that block legitimate affiliate transfers needed for the deal process. |
| Governing Law and Dispute Resolution | State governing law, forum, arbitration provisions, and submission to jurisdiction. Flag unfamiliar law, asymmetric process, inconvenient forum, or missing service provisions. | | |

Deliver the review inline in your chat response. Do not generate a downloadable Word document unless the user explicitly asks for one.
