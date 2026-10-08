---
name: prompt-pack-remote-work-policy-sboghossian
title: Remote Work Policy
description: Use when an employer needs to draft a remote work policy covering eligibility, equipment, working hours, communication expectations, data security, expense reimbursement, workspace safety, and performance monitoring. Particularly important in MENA jurisdictions where remote work intersects with UAE, Saudi, and Lebanese labour law requirements, visa/residency obligations, and data protection rules.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-remote-work-policy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Remote Work Policy

## When to use this

Use this skill when:
- A company is formalizing remote or hybrid work arrangements for the first time.
- An employer is updating a pandemic-era informal remote work arrangement into a binding policy.
- A company is expanding internationally and employees in new jurisdictions will work remotely from home countries.
- An employment lawyer is advising on whether an existing remote-work arrangement creates unintended employment law exposure (e.g., deemed permanent establishment, cross-border payroll obligations, data breaches from home offices).

**Critical MENA-specific note:** In UAE and KSA, remote work has visa and residency implications. An employee working permanently from outside the UAE may no longer qualify as a UAE-resident employee; their work permit and residence visa may be invalidated. The policy must address this explicitly.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Company name and jurisdiction of incorporation** | Determines which labour law applies and which regulatory body oversees employment | Ask |
| **Categories of employees covered** | Not all roles are eligible for remote work; eligibility criteria vary | Default: all permanent employees except those in roles requiring physical presence |
| **Remote work arrangement type** | Full remote / hybrid / occasional / cross-border | Default: hybrid (minimum days in office per week to be specified) |
| **Jurisdiction(s) where employees will work remotely from** | Cross-border remote work triggers separate tax, social security, and visa obligations | Ask |
| **Data classification** | Determines the data security section — some industries (financial services, health) face stricter home-office data handling rules | Ask |

## Optional inputs

- **Equipment provision policy** — whether the employer provides hardware and pays for internet, or whether the employee uses personal equipment with a stipend.
- **Expense reimbursement rules** — monthly stipend, actuals reimbursement, or no reimbursement.
- **Performance management framework** — whether remote workers are evaluated differently or with additional monitoring tools.
- **Collective agreement / works council requirements** — relevant in France and certain EU jurisdictions where remote work arrangements must be negotiated.

## Document structure

1. **Purpose and scope**
   - Why the policy exists: business continuity, employee well-being, productivity, regulatory compliance.
   - Who it applies to: full-time, part-time, contractors (confirm: contractors often have separate remote work terms).
   - What it does not cover: employees on secondment, business travel, or in-office roles.

2. **Definitions**
   - Remote work, hybrid work, approved remote location, home office, cross-border remote work.

3. **Eligibility criteria**
   - Role suitability (performance score, data security requirements, client-facing obligations).
   - Minimum tenure (e.g., after probation period completion).
   - Manager approval process.
   - Exclusions (e.g., roles in regulated environments, roles requiring physical presence for health and safety reasons).

4. **Application and approval process**
   - How to request remote work (form, system, timeline).
   - Manager approval criteria.
   - HR review and sign-off.
   - Trial period and review mechanism.
   - Revocation of remote work permission.

5. **Approved work locations**
   - **Within the jurisdiction of employment:** No additional approval needed beyond manager/HR sign-off.
   - **Cross-border remote work:** Requires specific legal clearance before commencement. The employer must assess: (a) immigration/visa implications, (b) payroll tax and social security implications in the remote country, (c) potential permanent establishment risk for the company, (d) applicable employment law in the remote country. This section must prohibit unauthorized cross-border remote work.

6. **Working hours and availability**
   - Core hours during which the employee must be reachable.
   - Overlap hours for cross-time-zone arrangements.
   - Rest periods and right to disconnect (mandatory in some jurisdictions: UAE Labour Law, French Code du Travail).
   - Compliance with applicable working hours limits (UAE: 8 hours/day, 48 hours/week maximum; Saudi Arabia: 8 hours/day, 48 hours/week).

7. **Communication requirements**
   - Response time expectations for messages and emails.
   - Required participation in meetings (video camera expectations).
   - Designated "not available" notification process.

8. **Equipment and technical requirements**
   - Employer-provided equipment: what is provided, who owns it, return obligation on termination.
   - Employee-provided equipment: minimum specifications, IT security standards (approved OS, encryption, VPN).
   - Internet connectivity: minimum speed requirements; employer's contribution (if any).

9. **Data security obligations**
   - Use of approved company VPN.
   - Prohibition on using public/unsecured networks for work.
   - Secure storage of physical documents.
   - Prohibition on using personal cloud storage for company data.
   - Incident reporting obligation if a device is lost, stolen, or compromised.
   - Applicable data protection law compliance (UAE PDPL, DIFC DP Law, GDPR where applicable).

10. **Workspace safety and ergonomics**
    - Employee's obligation to maintain a safe home workspace.
    - Employer's right to conduct a remote workspace risk assessment.
    - Work-related injury: coverage under workers' compensation / occupational injury schemes for home office injuries (varies by jurisdiction — clarify).

11. **Expense reimbursement**
    - Specify: internet allowance (if any), equipment purchase reimbursement procedure, office supply expenses.
    - Process: submission, approval, payment timeline.
    - Tax treatment: reimbursements that are taxable benefits in some jurisdictions (UK, EU).

12. **Performance monitoring**
    - This policy does not alter performance standards.
    - Monitoring tools (time-tracking, activity logging) if used: must comply with applicable data protection law and employee privacy rights; prior notice required.
    - Right of the employer to monitor company-owned devices.

13. **Policy violations and consequences**
    - Unauthorized cross-border remote work: immediate suspension of remote work arrangement, potential disciplinary action.
    - Data security breach caused by home-office non-compliance: disciplinary process up to termination.
    - Persistent performance issues: reversion to office-based work.

14. **Review and amendment**
    - Policy reviewed annually; material changes communicated to all employees with [30 days'] notice.

## Jurisdictional notes

### UAE (Federal Decree-Law No. 33 of 2021 on Labour Relations)
- UAE Labour Law Art. 7 permits remote work as a recognized work arrangement; employer must issue a work permit endorsement reflecting the arrangement.
- An employee working from outside the UAE without authorization may be treated as abandoning their employment; their residence visa tied to employment may be at risk.
- MOHRE's digital platform (MOHRE App) may require updating employment contracts to reflect remote work arrangements.
- The Wage Protection System (WPS) obligation applies regardless of where work is performed, as long as the employment contract is UAE-governed.

### KSA (Labour Law, Royal Decree M/51 of 2005)
- Saudi Labour Law Art. 40+ regulates working hours; remote work must not circumvent mandatory rest period rules.
- Non-Saudi employees: work permits (iqama) are tied to a specific employer and location; working remotely from outside KSA may constitute an unauthorized activity.
- Vision 2030 labor reforms have introduced flexible work arrangements; HRSD ministerial decisions may apply.

### Lebanon (Labour Code 1946 as amended)
- No specific remote work regulation; general labour law principles apply.
- Employer is still responsible for occupational health and safety for remote workers.
- Tax and social security (NSSF) obligations continue regardless of work location.

### UK (Employment Rights Act 1996 and related legislation)
- Employees have the right to request flexible working from day one of employment (Employment Relations (Flexible Working) Act 2023).
- Employer must give written response within 2 months; can only refuse on specified business grounds.
- Right to disconnect: not yet a statutory right in UK, but good practice to address in policy.
- GDPR / UK GDPR applies to processing of employee data for monitoring purposes.

### EU (generally)
- Right to disconnect: recognized at national level in France, Italy, Spain, Ireland; EU-level recommendation exists.
- Works council consultation required in Germany, France, Netherlands before implementing monitoring tools.
- Cross-border remote work within EU: posted workers rules may apply to short-term cross-border arrangements; bilateral social security agreements govern longer stays.

## Drafting standards

- Include a **signature/acknowledgment section** — employees should confirm they have read and agreed to the policy; this creates an evidentiary record.
- Be specific about cross-border prohibitions; vague language ("you must work from an approved location") is insufficient — specify that working from outside the country of employment requires specific prior written approval.
- Do not promise reimbursement amounts in the policy body — reference a separate expense schedule that can be updated without amending the policy.
- The right-to-disconnect provision should specify the mechanism (e.g., "employees are not expected to respond to communications outside core hours") rather than a blanket prohibition.

## Common mistakes

- **No cross-border remote work controls.** This is the highest-risk omission — employees who work from another country can trigger tax nexus, PE risk, and immigration violations for the employer.
- **Equipment return on termination not addressed.** Without a clear return obligation, recovering employer-issued equipment on accrual or termination becomes contentious.
- **Monitoring tools deployed without disclosure.** In the UAE, UK, EU, and most MENA jurisdictions, monitoring employees' digital activity requires prior notice; deploying tools without disclosure creates data protection liability.
- **Performance expectations unchanged but evaluation metrics not adjusted.** If remote workers are evaluated on the same in-office attendance metrics, the policy will create fairness and constructive dismissal risk.

## Related skills

- [[prompt-pack-termination-letter]]
- [[prompt-pack-severance-agreement]]
- [[prompt-pack-privacy-policy]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]
