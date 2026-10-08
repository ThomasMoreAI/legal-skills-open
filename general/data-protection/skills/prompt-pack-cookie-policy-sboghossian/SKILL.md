---
name: prompt-pack-cookie-policy-sboghossian
title: Cookie Policy
description: Use when a company needs to draft or update a Cookie Policy for its website or app, explaining the types of cookies used (essential, analytics, marketing), their purposes and durations, third-party cookies, and how users manage preferences. Must comply with the jurisdiction's applicable law — GDPR and ePrivacy Directive for EU; UAE PDPL and TDRA guidance; KSA NDMO regulations; DIFC/ADGM DP Law; Lebanon Law No. 81 of 2018 (where applicable). Requires a cookie consent mechanism to be implemented alongside the policy.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-cookie-policy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Cookie Policy

A Cookie Policy is a disclosure document, but it is also a legal instrument: in GDPR jurisdictions, an inadequate cookie notice can constitute a violation of the consent requirement, exposing companies to regulatory fines and private claims. In MENA jurisdictions, the law is evolving — but the direction of travel is consistent with the EU framework.

## When to use this

- A website or app is being launched and requires a Cookie Policy to comply with applicable privacy law.
- The company has changed its cookie practices (new analytics tools, new advertising networks, new consent management platform) and needs to update its policy.
- A regulatory audit or data protection review has identified the cookie notice as non-compliant.
- A company is expanding from a MENA-only operation to serving EU or UK users and must upgrade its cookie compliance to meet GDPR/UK GDPR standards.
- A company is implementing a Consent Management Platform (CMP) and needs the policy to align with the consent categories the CMP will manage.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Company name | The policy identifies the controller | Ask the user |
| Website or app name and URL | The policy is specific to a digital property | Ask the user |
| Jurisdiction(s) of users | The applicable legal standard (GDPR / UAE PDPL / KSA / other) | Ask the user — different standards apply |
| Types of cookies in use | Policy must describe cookies actually used; cannot be generic | Ask the user to provide their cookie audit or list of tools |
| Whether a consent mechanism exists | If no CMP exists, the policy must refer to alternative opt-out methods | Ask the user |

## Optional inputs

- Names of specific third-party cookies (Google Analytics, Meta Pixel, LinkedIn Insight Tag, etc.) — enhances transparency and regulatory compliance.
- Whether the site targets children under 13/16 (higher consent standards apply).
- Whether an existing Privacy Policy should be cross-referenced.
- Language requirements (Arabic version for MENA onshore users).

## Document structure

### 1. Introduction
- Identifies the company as the data controller.
- States the purpose of the policy (explain what cookies are and how the company uses them).
- States the effective date and when the policy was last updated.
- Provides a link to the company's Privacy Policy.

### 2. What are cookies?
Plain-language explanation:
- Cookies are small text files placed on the user's device by the website.
- They serve different purposes — from making the website function (essential) to tracking user behavior for analytics or advertising (non-essential).
- Distinguish between first-party cookies (set by the website itself) and third-party cookies (set by external services embedded in the website).
- Distinguish between session cookies (deleted when the browser closes) and persistent cookies (remain on the device for a set period).

### 3. Categories of cookies used

Present in a table:

| Category | Purpose | Examples | Duration | Can users opt out? |
|---|---|---|---|---|
| **Strictly necessary / essential** | Required for the website to function; cannot be disabled without breaking the site | Session tokens, login state, security cookies | Session or short-term persistent | No (essential function) |
| **Analytics / performance** | Measure how users interact with the site; help improve performance | Google Analytics, Hotjar, Amplitude | 30 days – 2 years typically | Yes (via CMP or opt-out tools) |
| **Functionality / preferences** | Remember user preferences (language, region, display settings) | Locale cookies, preference tokens | 30 days – 1 year typically | Yes |
| **Marketing / advertising** | Track users across sites to serve targeted advertising | Meta Pixel, Google Ads, LinkedIn Insight Tag | 90 days – 2 years typically | Yes (via CMP and opt-out) |

For each named third-party cookie, include the name of the provider and a link to their own privacy/cookie policy.

### 4. How we use cookies
Narrative description of the purposes for which each category is used, mapped to the company's specific use case.

### 5. Legal basis for cookies
State the legal basis per jurisdiction:

**GDPR (EU/UK) and DIFC/ADGM DP Law:**
- Essential cookies: legitimate interests (Art. 6(1)(f) GDPR) or contractual necessity. No prior consent required.
- Non-essential cookies: prior, freely given, specific, informed, and unambiguous consent (Art. 6(1)(a) GDPR and ePrivacy Directive). Consent must be obtained before non-essential cookies are placed.

**UAE PDPL (Federal Decree-Law No. 45 of 2021):**
- Consent is required for personal data processing unless another lawful basis applies.
- The TDRA has not yet issued detailed cookie-specific guidance as of 2026; align with GDPR best practice.

**KSA PDPL (Personal Data Protection Law, Royal Decree M/19, 2021):**
- Consent is the primary lawful basis for processing; NDMO guidance should be monitored.
- As of 2026, cookie-specific guidance is not yet published; GDPR-aligned consent is the conservative approach.

**Lebanon:**
- Law No. 81 of 2018 (Electronic Transactions) and access to information principles apply.
- GDPR alignment is recommended for companies also serving EU users.

### 6. Third-party cookies
- List each third party by name and describe the type of data collected.
- State that the company is not responsible for third-party cookie practices and link to each provider's policy.
- Note that some third parties may use the data for their own purposes (cross-context behavioral advertising) subject to their own policies.

### 7. How to manage cookie preferences
Describe all available mechanisms:
- **Consent Management Platform (CMP):** If the site has a CMP, describe how users access and change their consent preferences (banner, preference center, link in the footer).
- **Browser settings:** Most browsers allow users to block or delete cookies; provide links to the instructions for major browsers.
- **Opt-out tools:** For specific third parties (e.g., Google Analytics opt-out browser add-on, NAI opt-out, DAA opt-out).
- **Effect of opting out:** Be clear that opting out of non-essential cookies may affect site functionality.

### 8. Data transfers
If cookies cause personal data to be transferred to servers outside the jurisdiction (e.g., Google Analytics data transferred to the US, Meta Pixel data transferred to the US):
- Disclose the transfer.
- State the safeguard: adequacy decision (for EU to certain countries), Standard Contractual Clauses, or equivalent mechanism.
- In DIFC context: transfers outside DIFC require adequate protection per DIFC Data Protection Law.
- In UAE PDPL context: cross-border transfers require compliance with Chapter 6 of the PDPL.

### 9. Updates to this policy
- The company may update this policy to reflect changes in cookies or law.
- Users will be notified of material changes.
- The "last updated" date at the top of the policy reflects the most recent revision.

### 10. Contact information
- Data Protection Officer name or role (if a DPO is appointed).
- Email address for cookie-related queries.
- Postal address.
- How to exercise data subject rights (link to DSR procedure or Privacy Policy).

## Jurisdictional compliance notes

| Jurisdiction | Key requirement |
|---|---|
| EU / GDPR + ePrivacy | Prior opt-in consent for all non-essential cookies; "cookie walls" (no access without consent) are prohibited in most EU member state guidance; cookie banner must not use dark patterns |
| UK GDPR + PECR | Same as EU; ICO guidance published; similar prohibition on dark patterns |
| DIFC / ADGM | DIFC DP Law 2020 / ADGM DP Regulations 2021; equivalent to GDPR; consent required for non-essential processing |
| UAE PDPL | Consent required; TDRA and DIFC/ADGM-registered entities should align with GDPR pending specific guidance |
| KSA | NDMO implementing regulations; consent required; Arabic-language policy recommended |
| Lebanon | Law No. 81 of 2018; GDPR alignment recommended |

## Common mistakes

- Publishing a Cookie Policy without implementing a working Consent Management Platform — the policy is then legally meaningless because consent cannot be obtained before cookies are placed.
- Cookie Policy that lists generic categories but does not name the specific cookies and third parties in use — regulators and DPAs increasingly require specific disclosure.
- "Cookie walls" — blocking site access unless the user accepts all cookies — are likely non-compliant under GDPR and leading MENA frameworks.
- Not updating the policy when new tracking tools are added. Each new tool that places a cookie must be disclosed.
- Combining the Cookie Policy with the Privacy Policy in a way that makes neither readable — keep them as separate documents with cross-links.

## Related skills

- [[prompt-pack-data-processing-agreement]]
- [[prompt-pack-data-retention-policy]]
- [[prompt-pack-privacy-policy]]
- [[prompt-pack-cross-border-data-transfer-assessment]]
- [[prompt-pack-data-subject-access-request-procedure]]
