---
name: draft-licensing-agreement-software-sboghossian
title: Software License Agreement
description: Use when drafting a software license agreement for a commercial software product — covering license grant, license type (perpetual/subscription/term), user-definition model, updates and maintenance, IP indemnification, liability cap, and open-source disclosure. Applies to both on-premise and SaaS deployments. Includes attention to MENA-specific issues (data localization, PDPL compliance, SaaS regulation). Triggers on "software license", "saas agreement", "end user license", "EULA", or "software subscription" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-licensing-agreement-software
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Software License Agreement

## When to use this

Use this skill when a software vendor is granting a customer the right to use a software product. The license agreement defines what the customer may do with the software, on what terms, and what happens if they breach those terms.

Distinct from an MSA (which is a framework for ongoing services with SOWs): a software license agreement is the primary instrument when the main deliverable is the right to use software, not the delivery of custom professional services.

If the software is delivered as a service (SaaS), you will typically combine this with a DPA (data processing addendum) — see [[draft-dpa-gdpr]] or [[draft-dpa-ksa-pdpl]]. If custom development work is also involved, consider [[draft-msa]] with this as an exhibit.

## Required inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Licensor (vendor) + Licensee (customer) | Parties to the agreement | — must supply |
| Software description | What exactly is being licensed (product name, version, module) | — must supply |
| License type | Perpetual / subscription / term — see below | Subscription (annual) |
| User definition | How "use" is measured — see below | Named users |
| Territory | Where the software may be deployed/used | Worldwide or specified country |
| Governing law | Law of the agreement | Vendor's home jurisdiction |
| Fee structure | License fee, support fee, payment schedule | — must supply |

## License types — choose one

| Type | Characteristics | Best for |
|------|----------------|---------|
| **Perpetual** | One-time fee; customer owns the right to use the current version forever; updates are separate | On-premise enterprise software |
| **Subscription / SaaS** | Annual or monthly recurring fee; includes updates; terminates if subscription lapses | Cloud-hosted software, SaaS |
| **Term** | Fixed-duration license; auto-renews unless cancelled; customer must migrate off at end of term | Enterprise deals with defined project horizons |

## User-definition models

| Model | Measurement | Risks |
|-------|------------|-------|
| **Named users** | Fixed list of authorized individuals | Easy to audit; limits flexibility; customer over-provisions to avoid renegotiation |
| **Concurrent users** | Maximum simultaneous sessions | Harder to audit; customer-friendly; monitor with software controls |
| **Server / processor license** | Based on number of servers or CPU cores | Enterprise-friendly; disconnected from actual usage |
| **Site license** | Unlimited use at a defined location | Simple; vendor accepts location-risk |
| **Enterprise / company-wide** | All employees of the customer entity | Highest price; easiest to manage for large customers |

State the user definition precisely and specify:
- Who counts as a "User" (employees only? contractors? affiliated entities?)
- What constitutes "use" (accessing, querying, loading, executing)
- Audit rights to verify compliance with the user definition

## Document structure

1. **Definitions** — Software, Documentation, User(s), Permitted Use, Updates, Upgrades, Modifications, Authorized Territory, License Fees, Support Terms, Confidential Information

2. **Grant of license**
   - Scope: non-exclusive (standard), non-transferable (standard), revocable (for subscription), irrevocable (for perpetual)
   - Permitted acts: install, execute, access, display, store
   - Restriction on copying beyond authorized backup copies
   - Restriction on reverse engineering, decompilation, disassembly (subject to statutory rights in EU/UK)
   - Restriction on modifying or creating derivative works without vendor's written consent

3. **License restrictions (what licensee may NOT do)**
   - Access the software to build a competing product (important for SaaS)
   - Sublicense, sell, resell, rent, or transfer the license without consent
   - Remove or alter any proprietary notices
   - Use the software beyond the licensed scope or for more than the licensed number of users
   - Use the software for the benefit of third parties (service bureau or time-sharing) without separate agreement

4. **Delivery and installation** (on-premise)
   - Delivery method, media, timeframe
   - Customer's installation obligations
   - Acceptance testing period (typically 30 days) and acceptance criteria

5. **Updates and maintenance**
   - Define "Updates" (bug fixes, security patches, minor improvements) vs "Upgrades" (major version releases)
   - Subscription: Updates included; Upgrades may require additional fee
   - Perpetual: Updates for X years included; Upgrades at upgrade pricing
   - Support SLA: response time by severity (P1 critical: 1 hour; P2 major: 4 hours; P3 minor: 1 business day)
   - Support channels (email, phone, portal)
   - End-of-life / sunset notice period (typically 12-24 months' notice before discontinuing supported version)

6. **Limited warranty**
   - Vendor warrants that the software will materially conform to its Documentation for 30-90 days post-delivery
   - Vendor warrants it has the right to grant the license
   - Remedy for warranty breach: vendor will correct or replace; if unable to cure within a reasonable period, refund of fees
   - DISCLAIMER: THE SOFTWARE IS PROVIDED "AS IS" BEYOND THE EXPRESS WARRANTY PERIOD; vendor disclaims implied warranties of merchantability and fitness for a particular purpose (tailor for jurisdiction — implied warranties cannot be disclaimed for consumers in EU, UK, and some US states)

7. **Liability cap**
   - Vendor's aggregate liability capped at: fees paid in the preceding 12 months (standard); or a fixed multiple thereof for IP indemnification claims
   - Mutual exclusion of consequential, indirect, special, and punitive damages
   - Carve-outs from cap (these are never capped): IP indemnification (often capped separately at a higher amount), confidentiality breaches, fraud, willful misconduct, personal injury
   - Note: liability caps and consequential-damage exclusions are interpreted more narrowly in MENA civil-law courts than in common-law jurisdictions — verify enforceability per governing law

8. **IP indemnification**
   - Vendor indemnifies Licensee against third-party claims that the Software (as delivered, without modification) infringes a third party's IP
   - Vendor's sole obligation: (a) obtain a license, (b) modify the Software to avoid infringement, or (c) terminate the license and refund prepaid fees
   - Carve-outs from indemnification: Licensee modifications, use outside the licensed scope, combination with third-party products not authorized by Vendor
   - Licensee's reciprocal indemnification for claims arising from Licensee-provided data or Licensee modifications

9. **Confidentiality**
   - Software, source code, and Documentation are Vendor's Confidential Information
   - Customer data is Licensee's Confidential Information
   - Standard NDA-grade protection (see [[draft-nda-mutual]] for benchmarks)
   - Obligations survive termination for 5 years (trade secrets: indefinitely)

10. **Data processing / privacy**
    - If the Software processes personal data: attach a Data Processing Addendum (DPA) — see [[draft-dpa-gdpr]] (EU), [[draft-dpa-ksa-pdpl]] (KSA), [[draft-dpa-uae-pdpl]] (UAE)
    - For SaaS specifically: DPA is mandatory for EU/UK customers under GDPR/UK GDPR

11. **Open source disclosure**
    - Vendor must disclose all open-source components incorporated in the Software and their applicable licenses (GPL, LGPL, MIT, Apache, etc.)
    - Copyleft licenses (GPL) require particular attention: if the Software includes GPL code, distribution of the whole may require source-code disclosure
    - Include a schedule listing all OSS components and their licenses
    - Vendor represents that its use of OSS does not conflict with the license grant to Licensee

12. **Term and termination**
    - Subscription: auto-renews at end of each period unless either party gives X days' notice
    - Termination for breach: material breach with 30-day cure period
    - Termination for insolvency: immediate at non-breaching party's option
    - Licensee's obligation on termination: uninstall, delete all copies, certify deletion in writing
    - Vendor's obligation on termination: data portability / export for SaaS (export customer data in a standard format within 30 days)

13. **Governing law and dispute resolution**

14. **Boilerplate** — see [[draft-boilerplate-clauses]]

## MENA-specific issues

**Data localization (KSA, EG)**
KSA PDPL and EG Law 151/2020 have data-localization preferences for sensitive data. SaaS agreements for customers in these jurisdictions should specify the data hosting region and include an obligation to notify if hosting region changes.

**UAE PDPL (Federal Decree-Law 45/2021)**
Cross-border transfers of personal data require either adequacy or contractual safeguards; standard contractual clauses (SCCs) are the mechanism in practice.

**SaaS regulation in KSA**
Saudi Authority for Data and Artificial Intelligence (SDAIA) and Communications, Space & Technology Commission (CST) both regulate cloud services and may require local hosting or registration for regulated sectors (financial services, healthcare).

**Sharia and uncertainty**
For KSA-governed software licenses: pricing must be certain — open-ended licensing models tied to indeterminate future events may face gharar challenges. Structure pricing as fixed or formula-based with determinable inputs.

## Common mistakes

- Allowing reverse engineering without restriction (may be permissible by statute in EU/UK beyond contractual terms — address explicitly)
- No open-source schedule — exposes vendor to GPL contamination risk and customer to unexpected obligations
- Omitting the DPA for SaaS products that process any personal data
- Liability cap below vendor's insurance coverage — misalignment creates exposure
- No data-export obligation on termination — customer data is stranded

## Related skills

- [[draft-licensing-agreement]]
- [[draft-msa]]
- [[draft-msa-extension]]
- [[draft-dpa-gdpr]]
- [[draft-ip-licensing]]
