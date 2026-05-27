---
name: api-acceptable-use-policy
title: API Acceptable Use Policy
description: Drafts a standalone API Acceptable Use Policy (AUP) for incorporation by reference into a master API license or terms-of-service agreement. Produces a publication-ready template with prohibited-use matrix, developer security checklist, graduated enforcement framework, AI/ML training restrictions, and versioning playbook. Trigger when a user needs to draft or update an API AUP, separate behavioral rules from core API terms, define prohibited API uses, add enforcement or change-management mechanics, or mentions acceptable use policy, developer security requirements, or API enforcement.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/api-acceptable-use-policy
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
tags: [drafting, policy, transactional]
---

# API Acceptable Use Policy

Standalone AUP designed to be incorporated by reference into a master agreement. Separates fast-changing behavioral and security rules from stable commercial terms, enabling independent update cadence without re-acceptance.

## Quick Start

1. Run **Pre-Draft Intake** to gather company details and policy positions
2. Map AUP vs. master agreement scope using the **Allocation Table**
3. Build the **Prohibited Use Matrix** and **Security Checklist**
4. Define the **Enforcement Framework** and **Versioning Playbook**
5. Generate the **Publication-Ready Template** with all `[BRACKETED]` placeholders
6. Run **Post-Draft Alignment** to validate with the user

## Pre-Draft Intake

Ask every time unless the user says "use defaults" or "just draft."

1. **Company/product** — legal name, API/product name(s)
2. **Auth method** — API keys, OAuth 2.0, JWT, mTLS, or combination
3. **Access model** — public/self-service, partner-vetted, or internal-only
4. **Use model** — internal only or commercial redistribution via developer apps
5. **Data categories** — personal data, PHI, PCI, children's, biometric, or none
6. **Policy positions** — allow scraping? benchmarking? AI/ML training? caching duration? bug bounty?
7. **Contacts** — `[SECURITY_EMAIL]`, `[SUPPORT_EMAIL]`, `[LEGAL_EMAIL]`
8. **Rate-limit docs URL** — reference link (never hard-code numbers)

**Defaults** (apply and label if user doesn't respond):

| Parameter | Default |
|---|---|
| Governing law | U.S. (state TBD); B2B developers |
| API category | General SaaS |
| Access model | Public / self-service |
| Data scope | Personal data possible; no PHI/PCI/children's |
| AI/ML training | Prohibited unless expressly authorized in writing |
| Effective date — routine | Upon posting |
| Effective date — material adverse | 30 days' advance notice |
| Effective date — emergency | Immediate |
| Enforcement | Graduated; immediate suspension for severe/security violations |

## Step 1: AUP-to-License Allocation

| Topic | AUP | Master | Note |
|---|---|---|---|
| Incorporation by reference | No | **Yes** | Master references AUP URL |
| Prohibited uses | **Yes** (detailed) | Optional summary | Detail in AUP for easy updates |
| AI/ML restrictions | **Yes** | Optional summary | Updateable as AI landscape evolves |
| Data handling / security | **Yes** | Optional baseline | Coordinate with DPA/Security Addendum |
| Rate limits / caching | **Yes** (link to docs) | No | Never hard-code numbers |
| Monitoring disclosure | **Yes** (detail) | Yes (high-level) | AUP details signals/uses |
| Suspension right | **Yes** (triggers/process) | **Yes** (contractual right) | Master grants right; AUP describes process |
| Change / notice mechanics | **Yes** | **Yes** | No conflicting notice periods |
| Canonical definitions | Incorporate by reference | **Yes** | Define in Master |

## Step 2: Prohibited Use Matrix

| Category | Examples | Severity | Enforcement |
|---|---|---|---|
| Illegal activity | Law violations; fraud; sanctions evasion | High | Immediate suspend / terminate |
| Security abuse | Vuln scanning; credential stuffing; malware; reverse engineering | High | Immediate suspend |
| Interference / DDoS | Excessive calls; DoS; multi-key rate-limit bypass | High | Throttle → suspend |
| Circumvention | Bypassing auth, paywalls, metering | High | Suspend |
| Data misuse | Unlawful collection; re-identification; doxxing | High | Suspend + data deletion |
| Prohibited content | CSAM; threats; non-consensual imagery; hate speech | High | Immediate suspend; legal escalation |
| AI/ML training | Training/fine-tuning competing models; bulk extraction for datasets | Medium–High | Throttle → suspend |
| Scraping / bulk extraction | Large-scale automated extraction of core data | Medium–High | Throttle → suspend |
| Spam | Automated messaging without consent | Medium–High | Throttle → suspend |
| Misrepresentation | Impersonation; false affiliation; deceptive naming | Medium | Require changes → suspend |
| Caching violations | Retaining data beyond permitted duration | Medium | Warning → suspend |
| Benchmarking abuse | Publishing benchmarks without permission | Medium | Takedown → suspend |

## Step 3: Developer Security Checklist

- [ ] Unique credentials per environment and per application
- [ ] Secrets in vault/env vars — never in client-side code, public repos, or mobile binaries
- [ ] Regular key rotation; immediate revocation on compromise
- [ ] Least-privilege scopes; no shared credentials across teams
- [ ] TLS 1.2+ for all connections; mTLS/request signing if documented
- [ ] Accurate User-Agent or App ID in all requests
- [ ] Audit logs sufficient for misuse investigation
- [ ] Rate-limit and back-off compliance; no multi-key evasion
- [ ] Report compromise to `[SECURITY_EMAIL]` within `[X]` hours
- [ ] If serving end users: maintain compliant privacy policy

## Step 4: Enforcement Framework

| Trigger | Response | Notes |
|---|---|---|
| Minor / first-time | Notice + cure window | 10–30 day cure period |
| Repeated / uncured | Throttle → suspend | Escalate after failed cure |
| Security / illegal / high-risk | Immediate suspension | No cure required |
| Termination | Per master agreement | AUP breach = termination trigger |
| Appeal | Contact `[SUPPORT_EMAIL]` | Commercially reasonable response time |

## Step 5: Versioning & Notice Playbook

| Item | Recommendation |
|---|---|
| Version label | Date-based (e.g., 2026-02-23) |
| Change log | Bullets on developer site; version-controlled repo |
| Notice channels | Email to account admin + dashboard banner |
| Material change standard | Materially reduces developer rights or imposes new material obligations |
| Routine changes | Effective upon posting |
| Material adverse changes | 30 days after posting (or longer if required by law) |
| Emergency changes | Immediate for security or legal compliance |
| Archive | Prior versions at `[ARCHIVE_URL]` |

## Step 6: Publication-Ready AUP Template

> Replace all `[BRACKETED]` placeholders. Publish as standalone web page with version and effective date at top.

**API Acceptable Use Policy**
**Effective date:** [DATE] | **Version:** [VERSION]

This AUP governs your access to and use of the APIs, developer tools, and credentials made available by **[COMPANY NAME]** ("Company"). This AUP is incorporated into and forms part of the Agreement governing your API use. Capitalized terms not defined here have the meanings in the Agreement.

**1. Scope.** This AUP applies to (a) your use of the API, (b) your applications or services that access the API ("Developer App"), and (c) all activity under your API keys, tokens, OAuth client IDs, or other access credentials ("Developer Credentials").

**2. General Responsibilities.** You are responsible for all use of the API under your Developer Credentials, your Developer App's compliance with this AUP and applicable law, and ensuring your personnel and permitted third parties comply with this AUP.

**3. Prohibited Uses.** You will not use (or allow others to use) the API, Developer Credentials, or data obtained through the API to:

1. **Violate Law or Rights.** Violate any applicable law or regulation, or infringe, misappropriate, or otherwise violate any person's or entity's rights.
2. **Compromise Security.** Probe, scan, test the vulnerability of, or compromise the security or availability of the API or related systems; introduce malware; reverse engineer or fuzz the API; or bypass authentication, authorization, or usage limits.
3. **Interfere or Abuse.** Interfere with or disrupt the API or related systems, including through denial-of-service attacks, excessive automated requests, or circumventing rate limits (including by distributing requests across multiple credentials).
4. **Circumvent Controls.** Access the API in a manner intended to avoid fees, evade usage limits, or bypass technical measures.
5. **Misuse Data.** Collect, use, disclose, or store API data in a manner that is unlawful or violates applicable privacy or data-protection requirements, including by re-identifying de-identified data.
6. **Train Models Without Authorization.** Use API output, responses, or data to train, fine-tune, distill, or otherwise develop machine-learning or AI models, unless expressly authorized in writing by the Company.
7. **Engage in Harmful or Deceptive Conduct.** Engage in phishing, spamming, impersonation, deception, or other conduct that harms end users, third parties, or the Company.
8. **Exceed Caching Limits.** Cache or store API responses beyond the duration permitted in the developer documentation.
9. **High-Risk Activities.** Use the API where failure could lead to death, personal injury, or severe physical or environmental harm, unless expressly permitted in writing.

**4. Security Requirements.** You must: (a) protect Developer Credentials using industry-standard controls, including TLS 1.2+ in transit and secure secret storage; (b) not embed credentials in client-side code, public repositories, or mobile app binaries; (c) use least-privilege access and rotate credentials as appropriate; (d) include an accurate, non-misleading User-Agent or App ID in API requests; and (e) notify the Company at **[SECURITY_EMAIL]** promptly upon any actual or suspected credential compromise or security incident affecting the API.

**5. Rate Limits; Caching; Fair Use.** You will comply with all rate limits, quotas, and usage limits described in the developer documentation or communicated by the Company. You may cache API responses only as permitted in the documentation; unless otherwise specified, cached data must not be retained for more than **[24]** hours. The Company may throttle or suspend access to protect the API, other customers, or the Company.

**6. Monitoring; Enforcement.** The Company may monitor and analyze API usage to operate and secure the API, prevent abuse, comply with law, and enforce this AUP. If you violate this AUP (or the Company reasonably believes a violation has occurred or is imminent), the Company may: notify you and request remediation; throttle or restrict access; suspend or disable Developer Credentials; require deletion of improperly obtained data; or terminate access per the Agreement. The Company may act immediately (including suspending without prior notice) to protect the API, users, third parties, or the Company, or to comply with law. To appeal, contact **[SUPPORT_EMAIL]**.

**7. Changes.** The Company may update this AUP from time to time. Updates are effective upon posting at **[AUP_URL]**, unless a later effective date is indicated. For changes that materially and adversely affect your obligations, the Company will provide at least **30 days'** advance notice, except where an earlier effective date is necessary for legal compliance or to address an imminent security risk. Continued use of the API after the effective date constitutes acceptance. Prior versions: **[ARCHIVE_URL]**.

**8. Contact.**
- General questions: **[LEGAL_EMAIL]**
- Security reports: **[SECURITY_EMAIL]**
- Enforcement appeals: **[SUPPORT_EMAIL]**

## Post-Draft Alignment

After delivering the draft, ask:

1. Do prohibited use categories and severity levels match your enforcement capabilities?
2. Should AI/ML training be permitted for any use cases (e.g., non-competing academic research)?
3. Are operational contact emails staffed and ready?
4. Does the material-change notice period align with your master agreement?

## Quality Checklist

- [ ] AUP-to-license allocation complete with no conflicting provisions
- [ ] All prohibited use categories have severity and enforcement action
- [ ] Security checklist covers credentials, TLS, and incident reporting
- [ ] Graduated enforcement with immediate suspension for severe violations
- [ ] Versioning playbook has notice channels, material-change standard, and archive URL
- [ ] All `[BRACKETED]` placeholders clearly marked in template
- [ ] AI/ML restriction present and aligned with commercial intent
- [ ] Rate limits reference docs URL — no hard-coded numbers
- [ ] Monitoring disclosure coordinated with master agreement
- [ ] No conflicting notice periods between AUP and master agreement

## Pitfalls

- **Hard-coded rate limits** — reference a docs URL; engineering updates independently
- **Conflicting notice periods** — ensure AUP and master agreement match
- **Missing suspension right in master** — AUP describes triggers only; master must grant the contractual right
- **Precedence gaps** — specify which document controls on conflict; avoid circular references
- **Assent mechanism** — browsewrap is common for B2B; clickwrap may be required for material changes in some jurisdictions
- **Regulated data** — PHI/PCI/COPPA/GLBA/FERPA require a separate annex
- **EU/UK** — GDPR and Digital Services Act need separate drafting with local counsel
- **Export controls** — add EAR/ITAR/OFAC language if applicable
- **Operational readiness** — confirm contact emails route to staffed queues before publishing

**Required disclaimer on every output:**

> THIS POLICY IS A DRAFTING AID AND REQUIRES REVIEW BY QUALIFIED LEGAL COUNSEL BEFORE PUBLICATION. IT DOES NOT CONSTITUTE LEGAL ADVICE.
