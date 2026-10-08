---
name: employment-agreement-review-open-legal-products
title: Employment Agreement Review
description: Review the uploaded employment agreement and produce a comprehensive table-based legal review from the perspective of the party represented by the user/client.
author: open-legal-products
author_url: https://github.com/open-legal-products/mike-workflows/tree/main/assistant-workflows/employment-agreement-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Employment Agreement Review

## Instructions

Review the uploaded employment agreement and produce a comprehensive table-based legal review from the perspective of the party represented by the user/client. If the user has not already identified which party they represent, ask them to clarify that party before producing the review.

Once the represented party is clear, provide exactly one Markdown result table. Use one row for each material issue found in the agreement, guided by the review checklist below, and add a final row called **Overall Risk Rating**. The result table must have exactly these columns:

- Issue
- Summary
- Recommended Change

Use these risk ratings inside the **Summary** column: Low means standard or minimal concern; Medium means a manageable negotiation concern; High means a material legal, commercial, operational, or enforceability concern requiring negotiation; Critical means a severe issue that may block signing unless resolved. Start each summary with the risk rating, e.g. "High - restrictive covenant scope is excessive".

The **Summary** column should include only the relevant points from the **General** checklist column and the party-specific checklist column for the represented party, together with clause references where available. Do not include issues that are adverse only to another party unless they also create risk for the represented party. The **Recommended Change** column must be drafted from the represented party's perspective. Also flag general drafting errors that may affect the represented party, including inconsistent defined terms, inconsistent entity names, cross-reference errors, numbering issues, duplicated provisions, missing schedules, and internal inconsistencies. Keep the response concise and avoid long prose outside the table.

## Result Table Format

Use this result table structure. Cite the relevant clause, section, schedule, or page directly in the **Summary** and **Recommended Change** columns. The example rows are illustrative only; tailor the actual rows to the uploaded agreement and represented party.

| Issue | Summary | Recommended Change |
| --- | --- | --- |
| Restrictive Covenants | High - Clause [x] imposes a long non-compete with broad geographic scope. The general covenant position and the employee-specific checklist point indicate enforceability and mobility risk for the employee. | For the employee, reduce the duration, territory, and restricted activities to what is necessary for legitimate business protection. |
| Drafting Consistency | Medium - Clauses [x] and [y] use inconsistent defined terms or party names. The general drafting point indicates ambiguity that may affect the represented party's rights or obligations. | For the represented party, align the defined terms, party names, numbering, and cross-references before signing. |

## Review Checklist

Use this checklist as guidance for what to review and flag. It is not the result-table template and should not be reproduced verbatim. For each checklist issue, consider both the **General** column and the party-specific column for the represented party (Employer or Employee).

| Issue | General | Employer | Employee |
| --- | --- | --- | --- |
| Parties and Role | Identify employer and employee with correct legal names. Confirm job title, reporting line, work location, and employment type. Flag incorrect entities, unclear role scope, or terms creating unintended employment relationships. | | |
| Start Date and Term | State commencement date, probation period, fixed term, renewal mechanics, and conditions precedent. | Flag unclear commencement mechanics or terms that limit employer flexibility during the probation period. | Flag long probation periods, unclear renewal mechanics, or employer-only extension rights. |
| Duties | Summarize duties, working hours, exclusivity, travel requirements, and flexibility clauses. | Flag overly narrow duties that restrict operational flexibility or the employer's ability to change the role. | Flag open-ended duties, excessive hours, broad travel requirements, or unilateral employer change rights. |
| Compensation | Identify salary, payment frequency, reviews, bonus, commission, allowances, and discretion. | Flag discretionary compensation arrangements that may create enforceable entitlement expectations. | Flag fully discretionary compensation, unclear bonus criteria, or missing payment timing. |
| Benefits | Summarize pension, insurance, leave, expenses, equity incentives, and employer discretion. | Flag benefit commitments that may be difficult to modify or withdraw without breach. | Flag benefits that can be withdrawn without notice or that conflict with the offer letter. |
| Holiday and Leave | State annual leave, sickness absence, statutory leave, notice requirements, and carry-over rules. | Flag carry-over obligations or leave accrual that creates significant financial liability. | Flag entitlements below statutory minimums, unclear carry-over rules, or inadequate sick pay. |
| Policies and Handbook | Identify incorporated policies, contractual status, and amendment rights. | Flag policies incorporated as contractual that cannot be changed unilaterally without employee consent. | Flag policies incorporated as contractual while the employer retains unilateral amendment rights. |
| Confidentiality | Summarize confidentiality obligations during and after employment. | Flag confidentiality obligations too narrow to protect business-critical information. | Flag overbroad confidential information definitions or indefinite restrictions beyond legitimate business interests. |
| Intellectual Property | Identify ownership, assignment, inventions, works, moral rights waivers, and assistance obligations. | Flag gaps in IP assignment covering inventions or works made during employment or using company resources. | Flag assignment of unrelated personal inventions, works outside employment scope, or unpaid post-employment assistance obligations. |
| Data Protection and Monitoring | Summarize monitoring, privacy, processing, and consent provisions. | Flag monitoring arrangements that may expose the employer to data protection liability. | Flag intrusive monitoring, blanket consent provisions, or missing privacy notice references. |
| Conflicts and Outside Activities | Identify restrictions on outside work, directorships, investments, conflicts, and disclosure duties. | Flag insufficient restrictions on outside activities or conflicts that could harm business interests. | Flag broad bans on passive investments, restrictions on unrelated outside work, or disclosure obligations for non-conflicting activities. |
| Termination | State notice periods, payment in lieu, garden leave, summary dismissal, severance, and survival terms. | Flag notice periods or severance obligations that unduly limit employer termination flexibility. | Flag one-sided notice rights, broad summary dismissal triggers, or unclear payment in lieu treatment. |
| Restrictive Covenants | Summarize non-compete, non-solicit, non-dealing, non-poach, and confidentiality covenants. | Flag covenants too narrow in scope, too short in duration, or likely to be unenforceable. | Flag excessive duration, broad geographic scope, wide covered customers, or covenants that may be unenforceable restraints. |
| Return of Property | Identify obligations to return devices, documents, data, confidential information, and property. | Flag unclear scope of return obligations or no mechanism to enforce retrieval of business property. | Flag no carve-out for personal materials or obligations that require returning statutory record retention copies. |
| Governing Law and Dispute Resolution | State governing law, courts, tribunal forum, arbitration, and mandatory procedures. Flag unfamiliar law, unclear mandatory procedures, or arbitration clauses that may limit statutory rights. | | |

Deliver the review inline in your chat response. Do not generate a downloadable Word document unless the user explicitly asks for one.
