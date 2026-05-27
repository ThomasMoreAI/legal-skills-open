---
name: employee-confidentiality-agreement
title: Employee Confidentiality and Security Agreement
description: Drafts enforceable Employee Confidentiality and Security Agreements protecting trade secrets, proprietary information, and digital assets. Incorporates DTSA whistleblower notice, state-specific enforceability, NLRA carveouts, and data privacy compliance. Use when onboarding employees, updating confidentiality policies, or creating security agreements for data privacy and cybersecurity contexts.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/employee-confidentiality-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
---

# Employee Confidentiality and Security Agreement

Drafts an enforceable confidentiality and security agreement protecting company trade secrets and digital assets while satisfying employment, trade secret, and data protection law.

## Prerequisites

Gather before drafting:

1. **Governing jurisdiction** — state law drives enforceability, cure periods, blue-pencil doctrine
2. **Employee role and access level** — determines CI scope and post-employment restrictions
3. **Existing policies** — handbooks, IT security policies, prior agreements to incorporate or supersede
4. **Regulated industry flags** — HIPAA, GLBA, ITAR, or other sector-specific overlays
5. **Consideration context** — new hire (employment = consideration) vs. existing employee (additional consideration required in some states)

## Agreement Structure

### 1. Definitions

**Confidential Information (CI)** — all non-public information in any medium, whether marked or not:

| Category | Examples |
|---|---|
| Technical/IP | Trade secrets, source code, algorithms, R&D, manufacturing processes |
| Business strategy | Business plans, pricing, margins, financial projections, M&A targets |
| Customer/relationship | Customer lists, contract terms, supplier relationships |
| Financial/operational | Budgets, revenue, compensation structures, performance metrics |
| Derivative works | Analyses, compilations, summaries employee prepares using CI |

**Exceptions** (employee bears burden of proof by clear and convincing evidence):
- Public domain through no employee breach
- In employee's possession pre-disclosure (written evidence required)
- Received from unrestricted third party
- Independently developed without reference to CI (contemporaneous documentation required)

Exceptions apply to specific qualifying information only — not combinations incorporating CI.

### 2. Confidentiality Obligations

- **Non-disclosure**: No disclosure without written authorization; applies during and post-employment
- **Survival**: Trade secrets → indefinite (UTSA/DTSA); other CI → [3–5 years] post-termination
- **Limited use**: CI solely for assigned duties; no personal or third-party benefit
- **Standard of care**: At least reasonable care; never less than employee's own confidential information
- **Need-to-know**: Access limited to those bound by equivalent obligations
- **Secure storage**: Encryption for electronic CI; locked storage for physical; secure disposal
- **Prompt notification**: Report unauthorized disclosure or suspected compromise immediately

**Compelled disclosure**: Notify Legal immediately upon subpoena/court order; cooperate with protective order efforts; disclose only what counsel advises is legally required.

**DTSA Whistleblower Notice** *(18 U.S.C. § 1833(b) — required)*:
> No criminal or civil liability under Federal or State trade secret law for disclosure made in confidence to a government official or attorney solely to report/investigate a suspected legal violation, or in a sealed court filing.

**NLRA Carveout**: Agreement does not prohibit discussing wages, hours, or working conditions or engaging in other NLRA-protected concerted activity.

### 3. Security Responsibilities

**Access controls**: Unique strong passwords (12+ chars, mixed), MFA where available, no sharing/reuse, lock unattended workstations, change on suspected compromise.

**Acceptable use**: Business purposes; limited personal use permitted if non-interfering. Prohibited: unauthorized software, circumventing security, unauthorized devices, malicious code, pirated content.

**BYOD/Remote**: Company-approved MDM required; remote wipe consent for company data; approved VPN only.

**Monitoring**: Employee has no expectation of privacy on company systems; company may monitor without notice.

**Incident reporting**: Report breaches, unauthorized access, malware, phishing, lost devices, or unusual behavior to IT Security within [2–4] hours. Preserve evidence; cooperate fully. Non-retaliation for good-faith reporting.

### 4. Termination Obligations

**Return of property**: All company equipment, physical/electronic CI, copies on personal devices/cloud. Written certification of return/deletion before final compensation release.

**Company rights**: Remote wipe of MDM-enrolled devices; inspect company-issued devices; failure to return = conversion.

**Post-employment restrictions**:
- Ongoing CI obligations per §2
- **Employee non-solicitation**: [12–24 months] — no recruiting company employees
- **Customer non-solicitation**: [12–24 months] — no soliciting customers with material contact during final [12–24 months]
- Limited to active solicitation; does not prohibit competitor employment or responding to unsolicited inquiries

**New employer notice**: Employee must inform prospective employer of confidentiality obligations and notify company of new employment.

### 5. Legal Framework

| Provision | Standard |
|---|---|
| Governing law | Laws of [State]; exclusive jurisdiction in [County, State] |
| Equitable relief | Irreparable harm presumed; injunction without bond |
| Attorneys' fees | Prevailing party recovers fees, costs, investigation expenses |
| Severability | Blue-pencil authorized; invalid provisions reformed to minimum extent |
| Integration | Supersedes prior agreements; amendments require written officer signature |
| Assignment | Company may assign to successor; employee may not |
| E-signatures | Electronic signatures have same force as originals |

### 6. Employee Acknowledgments

Employee expressly acknowledges:
- Read and understood agreement; opportunity to consult counsel
- Voluntary execution; no duress
- Will access CI that company could not share without these protections
- Restrictions reasonable in scope, duration, geography
- Violations may result in termination, civil liability, injunctive relief, criminal prosecution
- DTSA whistleblower rights and NLRA protections not waived
- Adequate consideration received (specify if post-hire)
- Received executed copy

### 7. Signature Block

```
EMPLOYEE                          COMPANY
Signature: ___________________    By: ___________________
Print Name: __________________    Name: _________________
Date: ________________________    Title: ________________
                                  Date: _________________
```

## Pitfalls and Checks

- **Jurisdiction-first**: Verify state enforceability of non-solicitation; CA, ND, MN broadly restrict; others apply reasonableness tests
- **Consideration**: Existing employees may require additional consideration beyond continued employment
- **Duration tiers**: Indefinite for statutory trade secrets; fixed term for other CI — draft explicitly
- **DTSA notice**: Required for exemplary damages and attorney fees under 18 U.S.C. § 1836
- **NLRA compliance**: Overly broad CI definitions can violate NLRA; carve out wage/working condition discussions
- **Sector overlays**: HIPAA, GLBA, ITAR — add exhibits if employee accesses regulated data
- **FTC Non-Compete Rule**: Monitor enforceability developments for related restrictive covenants
