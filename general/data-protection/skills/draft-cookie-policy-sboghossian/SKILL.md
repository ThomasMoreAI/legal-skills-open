---
name: draft-cookie-policy-sboghossian
title: Draft — Cookie Policy
description: Use when asked to draft a Cookie Policy for a website or application. Covers all five cookie categories (strictly necessary, functional, analytics, advertising, social media), the required consent mechanism and granular opt-in standards under EU ePrivacy/GDPR, California CCPA opt-out requirements, and notes for UAE, KSA, and Lebanon. Should be paired with a Privacy Policy and Terms of Service.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-cookie-policy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Draft — Cookie Policy

## When to use this

Use this skill when a website or mobile application uses cookies, pixel trackers, local storage, or other tracking technologies, and a Cookie Policy is required to:
- Satisfy the EU ePrivacy Directive and GDPR requirements for consent before placing non-essential cookies.
- Comply with the California Consumer Privacy Act (CCPA) and CPRA opt-out requirements.
- Meet the transparency obligations of UAE, KSA, and Lebanese data privacy frameworks.
- Pair with a Privacy Policy and Terms of Service to form a complete compliance set.

## Required inputs

| Input | Notes |
|---|---|
| Organization name | Exact legal name |
| Website / application URL(s) | All domains and subdomains using cookies |
| Jurisdiction of primary users | Determines the consent standard — opt-in (EU/UK) vs opt-out (US) |
| Cookie inventory | List of cookies in use: name, provider, purpose, duration, type |
| Consent management platform (CMP) | OneTrust, Cookiebot, Osano, etc. — or describe the mechanism |
| Contact email for cookie inquiries | Data protection contact or general contact |

## Cookie categories

Enumerate all five categories, even if the site does not currently use all of them:

### Category 1 — Strictly necessary
- **Consent required**: No (these are exempt from consent under GDPR/ePrivacy).
- **Purpose**: authentication, session management, load balancing, security (CSRF protection), shopping cart (e-commerce), cookie consent preferences storage.
- **Examples**: `session_id`, `csrf_token`, `auth_token`, `cookie_consent`.
- **Duration**: session or short-term.
- **Note**: do not abuse this category by classifying analytics or marketing cookies as "necessary." Regulators actively scrutinize this.

### Category 2 — Functional / preferences
- **Consent required**: Yes if non-essential (language preference, UI settings beyond basic session needs).
- **Purpose**: remember user preferences (language, theme, region, accessibility settings).
- **Examples**: `lang_pref`, `theme_mode`, `timezone`.
- **Duration**: typically 1 year or until cleared.
- **Consent mechanism**: opt-in recommended even where technically debatable.

### Category 3 — Analytics / performance
- **Consent required**: Yes under GDPR/ePrivacy (even for "anonymous" analytics — CNIL guidance applies).
- **Purpose**: measure website traffic, user behavior, page performance, conversion tracking.
- **Providers**: Google Analytics (GA4), Mixpanel, PostHog, Amplitude, Heap, Hotjar.
- **Note**: if using GA4, IP anonymization alone is insufficient — consent is still required in the EU/UK.
- **Duration**: varies; GA4 standard: 2 years.
- **California**: analytics cookies are typically not "sales" of personal information but disclose them under the CCPA notice requirement.

### Category 4 — Advertising / marketing / targeting
- **Consent required**: explicit opt-in required under GDPR; opt-out under CCPA ("Do Not Sell or Share My Personal Information").
- **Purpose**: behavioral advertising, retargeting, lookalike audience building, cross-site tracking.
- **Providers**: Google Ads, Meta Pixel, LinkedIn Insight Tag, Twitter/X Pixel, TikTok Pixel, programmatic ad networks.
- **Duration**: typically 90 days to 2 years.
- **Highest risk**: advertising cookies are the primary target of DPA enforcement actions; get this category right.

### Category 5 — Social media / embedded content
- **Consent required**: Yes; social media embeds (YouTube, Twitter, LinkedIn) place cookies on load.
- **Purpose**: share buttons, embedded posts/videos, social login.
- **Providers**: Facebook/Meta, LinkedIn, Twitter/X, YouTube/Google.
- **Technique**: lazy loading (load embed only after consent) avoids pre-consent cookie placement.

## Document structure

### Section 1 — What are cookies?
One short, plain-language paragraph. Example:
> "Cookies are small text files placed on your device when you visit our website. They help us recognize your device on subsequent visits, remember your preferences, understand how you use our site, and deliver advertising and social media features. Similar technologies including web beacons, pixels, and local storage serve comparable purposes."

### Section 2 — Cookies we use
Present as a table for each category:

```
| Cookie name | Provider | Purpose | Duration | Category |
|---|---|---|---|---|
| _ga | Google Analytics | Analytics — unique visitor ID | 2 years | Analytics |
| _gid | Google Analytics | Analytics — session ID | 24 hours | Analytics |
| session | Our platform | Authentication — session token | Session | Strictly Necessary |
| fbp | Meta (Facebook) | Advertising — pixel tracking | 90 days | Advertising |
| lang_pref | Our platform | Remember language selection | 1 year | Functional |
```

Maintain this table up to date. An out-of-date cookie table is a compliance violation.

### Section 3 — How we obtain your consent
- **EU/UK**: describe the consent management platform (CMP) used; how users can granularly accept or reject categories; how to withdraw consent at any time.
- **US (California)**: describe the "Do Not Sell or Share My Personal Information" mechanism and any Global Privacy Control (GPC) signal honored.
- Example:
> "When you first visit our website, we present a cookie banner that allows you to accept all cookies, accept only strictly necessary cookies, or customize your preferences by category. You can change your preferences at any time by clicking the 'Cookie Settings' link in the footer."

### Section 4 — Managing and withdrawing consent
- Browser settings: how to block or delete cookies.
- Platform-specific links (Google Analytics opt-out, NAI opt-out for advertising).
- Your CMP's preference center link.
- Note: withdrawing consent does not affect lawfulness of processing before withdrawal.

### Section 5 — Third-party cookies and links to provider policies
For each major third-party provider:
- Name and purpose.
- Link to their privacy/cookie policy.
- Note that Louis/the organization has no control over third-party cookies once placed.

Common providers to list: Google (Analytics + Ads), Meta, LinkedIn, Twitter/X, Hotjar, Intercom, Stripe (if used for payments — Stripe has its own cookie policy), Cloudflare.

### Section 6 — Updates to this policy
> "We update this Cookie Policy periodically to reflect changes in our use of cookies or applicable law. The 'Last updated' date at the top of this page indicates when the policy was last revised. We encourage you to review this policy regularly."

### Section 7 — Contact
> "For questions about our use of cookies, contact us at: [data-protection@company.com / privacy@company.com]."

## Jurisdictional notes

### EU + UK (ePrivacy Directive + GDPR)
- **Opt-in consent** required for all non-strictly-necessary cookies before placement.
- Consent must be: freely given, specific, informed, and unambiguous (GDPR Article 7).
- Pre-ticked boxes do not constitute valid consent.
- The consent banner must not use dark patterns (making "reject all" harder to find than "accept all"); CNIL and ICO have issued specific guidance on this.
- **Record of consent**: keep records of what consent was given, when, and how; auditable.

### California (CCPA / CPRA)
- No opt-in consent requirement for non-advertising cookies.
- "Do Not Sell or Share My Personal Information" opt-out link required if cookies serve advertising that constitutes "sharing" of personal information (broadly interpreted post-CPRA).
- Global Privacy Control (GPC) signal: businesses are required to honor GPC as an opt-out signal under California law.

### UAE
- UAE Personal Data Protection Law (Federal Decree-Law 45/2021) requires informing users about cookie use; consent-based approach is increasingly expected.
- No specific cookie law yet; GDPR best-practice alignment is the recommended standard.

### KSA
- Saudi Personal Data Protection Law (PDPL — Royal Decree M/19 2021) requires transparency and consent for processing personal data; cookies tracking users are within scope.
- Sector-specific guidance from SDAIA (Saudi Data and AI Authority) may provide additional direction.

### Lebanon
- No specific data protection or cookie law; GDPR best-practice applies for international visitor compliance and is widely used by Lebanese companies with EU exposure.

## Pairing with other documents

- **Privacy Policy**: the Cookie Policy covers cookies specifically; the Privacy Policy covers all personal data processing. Cross-reference both. See [[draft-privacy-policy]].
- **Terms of Service**: users accept the Terms (which incorporate the Cookie Policy by reference). See [[draft-terms-of-service]].

## Common mistakes

- **Listing cookies as "strictly necessary" when they are not**: CNIL and ICO target overcategorization in enforcement.
- **Out-of-date cookie table**: new third-party scripts (A/B testing, live chat) add cookies; run a monthly audit.
- **Pre-ticked consent boxes in the EU/UK**: invalidates the entire consent; start with nothing ticked.
- **No withdrawal mechanism**: users must be able to withdraw consent as easily as they gave it.
- **US website with EU visitors ignoring GDPR**: if EU visitors are targeted or systematically served, GDPR applies regardless of the company's location.

## Related skills

- [[draft-privacy-policy]]
- [[draft-terms-of-service]]
- [[draft-boilerplate-clauses]]
