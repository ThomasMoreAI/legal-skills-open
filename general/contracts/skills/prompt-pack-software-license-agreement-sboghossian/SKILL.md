---
name: prompt-pack-software-license-agreement-sboghossian
title: Software License Agreement
description: Use when a software licensor needs to draft a license agreement granting a licensee rights to use specific software. Covers license scope, permitted users, use restrictions, fees and maintenance, IP ownership, warranties, limitation of liability, and termination. MENA-specific guidance addresses UAE copyright law treatment of software, enforceability of seat-of-use restrictions across MENA free zones and onshore entities, and the distinction between software license and SaaS agreements in Arab civil-law jurisdictions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-software-license-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Software License Agreement

## When to use this

Use this skill when:
- A software vendor is granting a customer the right to use software on a perpetual or term basis (as distinct from SaaS, where the customer accesses software hosted by the vendor — use [[prompt-pack-saas-terms-of-service]] for that).
- An enterprise is licensing a proprietary platform to another enterprise for internal deployment.
- An OEM arrangement requires one company to embed another's software in its products.
- A government entity or regulated institution requires on-premise software deployment (not cloud) for data sovereignty reasons.
- A software developer is licensing its product internationally and needs a jurisdiction-flexible license agreement.

**Distinguish from:**
- **SaaS/ToS:** access to cloud-hosted software; no software delivered or installed — use [[prompt-pack-saas-terms-of-service]].
- **Technology licensing:** broader rights in technology (patents, know-how, trade secrets) beyond software code — use [[prompt-pack-technology-licensing-agreement]].
- **Technology transfer:** permanent assignment or deep transfer of technology — use [[prompt-pack-technology-transfer-agreement]].

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Licensor and licensee identities** | Determines governing law and tax obligations | Ask |
| **Description of the software** | Precise name, version, modules; attach product description as Schedule | Ask |
| **License type** | Perpetual vs. term; exclusive vs. non-exclusive; single-user vs. enterprise-wide | Ask; default: non-exclusive, term license |
| **Permitted users / deployment scope** | Number of named users / concurrent users / enterprise-wide; on-premise vs. specified servers | Ask; drives the pricing and technical controls |
| **License fee and payment structure** | One-time vs. annual; per seat / per deployment / enterprise | Ask |
| **Jurisdiction / governing law** | Determines IP law, software copyright treatment, and enforceability of restrictions | Ask |

## Optional inputs

- **Source code escrow** — whether source code will be placed in escrow for release on licensor insolvency or abandonment.
- **Support and maintenance terms** — often in a separate SLA or maintenance schedule; flag if needed.
- **Customization rights** — whether the licensee may modify the software (rare in off-the-shelf licenses; common in enterprise licenses).
- **Sublicensing rights** — whether the licensee may license the software to affiliates, subsidiaries, or third parties.
- **Export control** — relevant for software subject to US EAR, EU dual-use controls, or other export regulations.

## Document structure

1. **Definitions**
   - **Software:** specific software described in Schedule 1, including all Updates, Upgrades, and Documentation provided under this Agreement.
   - **License:** the right to use the Software as specified.
   - **Authorized Users:** [named individuals / all employees of Licensee / specified number of concurrent users].
   - **Deployment:** [on-premise at Licensee's facilities at [address] / on Licensee's private cloud infrastructure / other].
   - **Updates:** bug fixes and minor releases.
   - **Upgrades:** major version releases (may require additional license fees — specify).
   - **Documentation:** user manuals, API documentation, technical specifications.
   - **Intellectual Property Rights:** patents, copyright, trade secrets, know-how.

2. **Grant of license**
   - Licensor grants to Licensee a [non-exclusive / exclusive], [perpetual / term], non-transferable, non-sublicensable license to use the Software solely:
     - By the Authorized Users.
     - At the Deployment location(s) specified.
     - For Licensee's own internal business purposes only.
     - Subject to the restrictions in this Agreement.
   - Exclusivity: if exclusive, state the territory and scope; note that exclusive software licenses are unusual except in OEM or white-label arrangements.
   - Sublicensing: expressly prohibited unless otherwise stated; if permitted to affiliates, specify conditions (execution of a Deed of Adherence; Licensor notification).
   - Deployment outside scope: any use beyond the licensed scope is infringement and may trigger audit rights and additional fees.

3. **License restrictions**
   - Licensee **shall not**:
     - Copy the Software except for a reasonable number of backup copies.
     - Modify, adapt, translate, or create derivative works from the Software (unless expressly permitted).
     - Decompile, disassemble, or reverse engineer the Software (except to the extent required by applicable law — EU Software Directive Art. 6, DIFC IP Law).
     - Remove or obscure proprietary notices.
     - Use the Software to provide time-sharing, hosting, or outsourcing services to third parties.
     - Transfer, assign, or sublicense the Software without Licensor's written consent.
     - Use the Software for unlawful purposes.
   - **Note on reverse engineering:** EU law (Software Directive) and some other jurisdictions provide limited reverse engineering rights for interoperability purposes; these cannot be contractually waived in those jurisdictions. Include a carve-out: "except as expressly permitted by applicable law which cannot be excluded by agreement."

4. **Delivery and installation**
   - Delivery method: download link / physical media / secure API / access credentials.
   - Delivery date: within [X] business days of agreement execution.
   - Installation: [Licensor to install and configure / Licensee to install; Licensor provides technical documentation].
   - Acceptance: Licensee has [10/20] business days post-delivery to confirm the Software materially performs as described in the Documentation. Defects must be reported in writing. If no notice of defects is given within the acceptance period, the Software is deemed accepted.

5. **Fees and payment**
   - License fee: [amount and currency]; due on [execution / delivery / per annual billing cycle].
   - Annual maintenance and support fee: [amount] per year, billed in advance; covers Updates and standard support.
   - Upgrade fees: major version upgrades are separately priced; Licensee may elect to upgrade or remain on current version.
   - Payment terms: net [30/45/60] days from invoice.
   - Late payment: interest at [rate]% per annum.
   - Price increases: annual price increases for maintenance/support capped at [CPI + X%] or [X%], whichever is lower.

6. **Audit rights**
   - Licensor has the right, on [30 days'] prior written notice, to audit Licensee's use of the Software to verify compliance with the license scope.
   - Audit: no more than once per year; conducted during business hours; minimally disruptive; Licensor's costs.
   - If audit reveals underpayment: Licensee pays the deficit plus [15%] of the underpayment as a compliance fee; if underpayment exceeds [X%], Licensor may terminate.

7. **Intellectual property ownership**
   - Licensor retains all IP rights in the Software.
   - This Agreement does not transfer any IP to Licensee; the license is a use right only.
   - Licensee feedback: if Licensee provides feedback or suggestions, Licensor may use them without obligation or compensation.
   - Customizations: if Licensor develops customizations for Licensee under a separate Statement of Work, IP ownership is to be addressed in that SoW (default: Licensor retains ownership; grants Licensee a license to use).

8. **Support and maintenance**
   - Support tier (if applicable): email support / phone support / 24/7 support.
   - Response times per tier: [e.g., Tier 1 critical: 4-hour response; Tier 2: 24-hour response; Tier 3: 5-business-day response].
   - Updates and patches: Licensor provides Updates during the maintenance term at no additional charge.
   - End-of-life notice: Licensor provides [12/24] months' notice before discontinuing support for a major version.

9. **Source code escrow** (optional)
   - Licensor will deposit the source code for the Software with [named escrow agent].
   - Release conditions: Licensor insolvency; Licensor ceasing to support the Software; material breach by Licensor uncured after [60] days.
   - Escrow fees: shared [50/50] or borne by Licensee.
   - On release: Licensee receives a license to use the source code solely to maintain and support the Software for its own internal use.

10. **Warranties**
    - Licensor warrants: (a) it has the right to grant this license; (b) the Software will materially conform to the Documentation for [12/24 months] after delivery; (c) the Software does not contain any known malicious code at the time of delivery.
    - Licensee's sole remedy for warranty breach: Licensor will use reasonable efforts to fix the defect; if unable within [30] days, Licensee may terminate and receive a refund of prepaid fees.
    - Disclaimer: except for express warranties, Software is provided "as is." No warranty of merchantability or fitness for a particular purpose.

11. **IP indemnification**
    - Licensor will defend and indemnify Licensee against third-party claims that the Software infringes that party's IP rights.
    - Licensor's options: modify the Software; obtain a license; replace with equivalent non-infringing software; refund prepaid fees and terminate.
    - Exclusions: infringement caused by Licensee's modifications, combination with third-party software, or use outside the permitted scope.
    - Licensee must: notify Licensor promptly; give Licensor sole control of defense; cooperate; not admit liability.

12. **Limitation of liability**
    - Mutual exclusion of indirect, consequential, incidental, and special damages.
    - Cap: aggregate direct liability limited to fees paid in the [12] months before the claim.
    - Carve-outs: IP indemnity obligations; death/personal injury; fraud.

13. **Term and termination**
    - Term: perpetual (subject to termination) or fixed term [1/3/5 years] with renewal.
    - Termination for cause: material breach with [30-day] cure period; insolvency.
    - Termination for convenience by Licensor: [90 days'] notice (unusual for perpetual licenses; more common for term licenses).
    - Effect of termination: Licensee must cease use; destroy or return all copies; certify destruction in writing.
    - Survival: provisions that survive termination: confidentiality, limitation of liability, IP ownership, audit for pre-termination period.

14. **Governing law and dispute resolution**
    - Governing law: [UAE / DIFC / English / other].
    - Dispute resolution: arbitration preferred for cross-border licenses.

## Jurisdictional notes

### UAE — Copyright and Software
- UAE Federal Decree-Law No. 38 of 2021 on Copyright and Related Rights: software is protected as a literary work.
- Reverse engineering restrictions are enforceable by contract; the UAE Copyright Law does not have a statutory interoperability exception equivalent to the EU Software Directive.
- On-premise deployment in a free zone vs. mainland: the license should specify whether cross-zone use is permitted (relevant for companies with offices in both mainland and a free zone).

### DIFC / ADGM
- IP protected under DIFC IP Law (Law No. 4 of 2019) and ADGM IP Regulations.
- Common-law contract principles apply; license restrictions are generally enforceable.
- Software Directive equivalent interoperability rights do not automatically apply.

### KSA
- Saudi IP law (Copyright Law, Royal Decree M/41 of 2004): software protected as an authored work.
- Arabic-language documentation is required for enforcement in Saudi courts; consider providing Arabic documentation.
- Export control: US-origin software subject to EAR; check whether BIS license is required for export/re-export to KSA.

### EU
- EU Software Directive (Directive 2009/24/EC): limited reverse engineering right for interoperability — cannot be contractually waived.
- GDPR: if the software processes personal data, a Data Processing Agreement is required.

## Drafting standards

- Describe the Software precisely — name, version, modules — in a Schedule; do not rely on generic descriptions in the body.
- The permitted use and restrictions section is the core of the agreement; be explicit about what is and is not permitted.
- For enterprise licenses: a concurrent-user or enterprise-wide model requires clear audit mechanics to verify compliance.
- For software with embedded open-source components: require Licensor to disclose open-source components and their licenses in Schedule 2 to avoid surprises.

## Common mistakes

- **Vague deployment restrictions.** "Licensed for use at Licensee's premises" — does that include Licensee's overseas offices? Remote employees? Cloud deployments? Be specific.
- **No acceptance period.** Without an acceptance procedure, the delivery date and the beginning of the warranty period are uncertain.
- **Open-source not addressed.** Software that incorporates open-source components may carry copyleft obligations (GPL, AGPL) that are incompatible with the proprietary license being granted; always audit and disclose.
- **Source code escrow not considered.** For mission-critical systems, failure to include escrow provisions leaves the licensee exposed if the licensor goes out of business.

## Related skills

- [[prompt-pack-saas-terms-of-service]]
- [[prompt-pack-technology-licensing-agreement]]
- [[prompt-pack-technology-transfer-agreement]]
- [[prompt-pack-research-collaboration-agreement]]
- [[heuristic-always-state-jurisdiction-first]]
