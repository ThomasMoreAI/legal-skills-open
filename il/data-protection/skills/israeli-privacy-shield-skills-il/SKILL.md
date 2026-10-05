---
name: israeli-privacy-shield-skills-il
title: Israeli Privacy Shield
description: Israeli Privacy Protection Law compliance guidance including Amendment 13 (effective August 14, 2025), database registration, consent requirements, data security, cross-border transfers, breach notification, privacy protection officer appointment, and AI governance. Use when user asks about Israeli privacy law, "haganat pratiut", "tikun 13", data protection in Israel, GDPR compliance for Israeli companies, privacy policy requirements, or database registration. Covers the Privacy Protection Law 1981, Amendment 13, and 2017 Security Regulations. Do NOT use for EU GDPR-only questions without Israeli context.
author: skills-il
author_url: https://github.com/skills-il/security-compliance/tree/master/israeli-privacy-shield
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: data-protection
language: en
sources:
- title: Consent Banner Implementation
  path: references/consent-banner-implementation.md
- title: Consent Ui Anti Patterns
  path: references/consent-ui-anti-patterns.md
- title: Privacy Law Requirements
  path: references/privacy-law-requirements.md
---

# Israeli Privacy Shield

## Legal notice

This is a free information tool operated by an AI model. It explains the law and the procedure and helps you organise your own documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion, but a general explanation and a template only: it does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. Before starting proceedings, signing a document, or filing with an authority or a court, consult an advocate. All use of its output is the user's sole responsibility.


## Critical Note
This skill provides compliance GUIDANCE. It does not replace legal counsel.
Recommend consulting a privacy attorney (orech din specializing in prati'ut)
for specific compliance decisions.

## Instructions

### Step 1: Assess Security Level
The 2017 regulations define three security levels:

| Level | Criteria | Key Requirements |
|-------|----------|-----------------|
| Basic | < 10,000 records, non-sensitive | Access controls, logging, backup |
| Medium | 10,000+ records OR sensitive data | + Encryption, security officer appointment |
| High | Government, health, financial, 100K+ records, or authorized access for 100+ people | + Incident response plan, DPO, plus a security risk assessment and a penetration test at least once every 18 months with documented findings and remediation |

Sensitive data includes: especially-sensitive data. **Do not work from the old section 7 list.** Amendment 13 replaced "sensitive data" with the defined term "מידע בעל רגישות מיוחדת", and its schedule is WIDER than the pre-Amendment health/genetics/sexual-orientation/political-views/criminal-record list this skill used to print. **The current list is not carried in this skill**: read the definition in the amended Law before answering yes or no, because that single flag drives both the security level and the 100,000-record notification duty, so getting it wrong under-implements twice.

### Step 2: Database Registration Check
Under the Amendment 13 regime, registration with the Privacy Protection Authority (PPA) is required only if:
- Database owned or managed by a public body, OR
- Database contains data on 10,000+ individuals AND the primary purpose is collecting and disclosing personal data to third parties as a business or for value (data brokers)

The broad pre-Amendment requirement covering any database with sensitive data (and the old "Form 1" five-trigger list) no longer applies.

**Notification tier (separate from registration).** Even where registration is not required, a controller holding especially-sensitive data on more than 100,000 individuals must notify the PPA within 30 days, including the controller's and privacy officer's details and the database definition document.

Registration and notification are handled through the PPA: https://www.gov.il/en/departments/the_privacy_protection_authority

### Step 3: Consent Requirements
Israeli law requires consent for:
- Collection of personal data
- Use beyond the original purpose
- Transfer to third parties
- Cross-border transfer

Consent must be: Informed, specific, freely given
Exceptions: Legal obligation, vital interests, public interest, legitimate interest (limited)

### Step 4: Cross-Border Transfer Rules
Personal data transfer outside Israel requires:
- Recipient country has adequate protection (EU, UK, few others), OR
- Contractual safeguards (similar to GDPR SCCs), OR
- Data subject consent (informed and specific), OR
- Listed exemptions (necessary for contract, legal proceedings, etc.)

Note on direction, which the skill previously had backwards: the EU adequacy decision authorises transfers FROM the EU TO Israel. What permits an Israeli controller to send data OUT to the EU is the Israeli Transfer of Data to Databases Abroad Regulations, whose whitelist includes EU member states. Do not cite adequacy as the basis for an Israel-to-EU transfer.

### Step 5: Breach Notification
Israel requires IMMEDIATE notification of a Severe Security Incident under the 2017 Data Security Regulations (no fixed-hours deadline):
1. **Notify the Privacy Protection Authority immediately upon discovering a Severe Security Incident.** The Data Security Regulations (2017), regulation 11(d), require notification "immediately" (miyad); there is NO fixed 72-hour deadline in Israeli law.

**The PPA has now said what "immediately" means, and it is the answer to the question every compliance officer actually asks.** Fining Meuhedet in July 2026 it held that the duty arises **when you learn that a severe security incident has occurred**, and must be performed close to the moment of discovery and without delay. Critically: **a position that you should wait until all your checks are complete empties the immediacy requirement of meaning.** The required report is an INITIAL report based on what is known at the time, and further details are supplied in a supplementary report later. So the sequence is report first on partial information, investigate second. An organisation that investigates first and reports a complete picture two months later has breached the duty even though it eventually reported fully. Cover what happened, the categories and rough number of affected individuals, the likely impact, and the steps taken. The PPA may then direct the controller to notify affected data subjects.
2. **Notify affected data subjects only if the PPA directs you to.** Under the Data Security Regulations that duty arises from a PPA direction after you report, NOT from the controller's own GDPR-style "high-risk" self-assessment. If directed, the notice must be in clear, plain Hebrew covering the breach, the data affected, the consequences, and protective steps.
3. **Severe Security Incident standard:** an incident (unauthorized access, disclosure, loss, alteration, or destruction of personal data) that poses a risk to the rights of the affected individuals.
4. **Document:** all incidents, response actions, and decisions, regardless of whether they cross the reporting threshold.

### Step 6: Compliance Checklist
For each assessed entity, verify:
- [ ] Database registration (if required)
- [ ] Privacy policy published (Hebrew, accessible)
- [ ] Consent mechanisms in place
- [ ] Security measures per level (basic/medium/high)
- [ ] Data processing agreements with processors
- [ ] Cross-border transfer safeguards
- [ ] Breach response plan with notification template
- [ ] Data subject request workflow (Section 13 access, Section 14 correction, 30-day response)
- [ ] DPIA process for high-risk processing (large-scale sensitive data, systematic monitoring, AI decisions)
- [ ] Minors' data policy (parental consent under Capacity and Guardianship Law, ed-tech safeguards)
- [ ] Employee training
- [ ] **Notice at the point of collection (section 11)**: whenever personal data is collected, tell the person whether there is a legal duty to provide it or it is voluntary, the purpose it will be used for, and to whom it will be delivered and for what purpose. This is the duty the PPA fined a company NIS 12,000 for breaching in August 2026, and it was previously documented in this skill only as an enforcement anecdote and never as a requirement to perform
- [ ] Privacy Protection Officer appointed (if required under Amendment 13)
- [ ] AI governance policy for automated decision-making (if applicable)
- [ ] Personal data inventory includes IP addresses, geolocation, and online identifiers

### Step 7: Amendment 13 (Effective August 14, 2025)

Amendment 13 is the most significant reform of Israeli privacy law since 1981. It took effect on August 14, 2025 and expands the Privacy Protection Authority's enforcement powers, broadens the definition of personal data, and introduces new obligations for data brokers and AI systems.

**Expanded definition of personal data.** Amendment 13 explicitly includes digital identifiers:
- IP addresses
- Geolocation data
- Device identifiers and online identifiers
- Biometric and genetic data (already sensitive)

Standard web analytics, session logs, and mobile app telemetry now fall within the scope of the Privacy Protection Law.

**Mandatory Privacy Protection Officer (PPO / DPO).** Under Amendment 13, the following entities must appoint a Privacy Protection Officer:
- Public bodies (government ministries, municipalities, universities, HMOs and similar), except national-security entities
- External suppliers and processors acting for those public bodies
- Data brokers, with a concrete threshold: a controller whose database holds personal data on more than 10,000 individuals AND whose main purpose is collecting personal data to disclose it to third parties as a business or for value (including direct-mailing services)
- Entities that systematically monitor individuals on a large scale, or whose core business includes processing especially-sensitive data on a large scale

**The PPA published its FINAL opinion (gilui daat) on the appointment on 26 July 2026, updated 27 July.** Anything written before that date about the scope of the duty or the officer's qualifications is superseded, and this is the document to work from. Its substance:

- The officer's purpose is not merely to secure compliance with the Law in the organisation but **to promote and improve privacy protection and information security beyond the statutory minimum**. Treating the role as a compliance checkbox is not the regulator's reading of it.
- The duties it enumerates: promote a privacy culture in the organisation, advise management and employees, train, audit compliance with the Law, handle data-subject requests, and act as the contact point with the Privacy Protection Authority.
- The qualifications: **deep knowledge of privacy law, an adequate understanding of technology and information security, and familiarity with the organisation's own areas of activity.** All three, which rules out both a lawyer with no technical grasp and a security engineer with no privacy-law background.

The PPO is the contact point with the Privacy Protection Authority and is responsible for monitoring compliance. A non-enforcement window running to 31 October 2025 was previously stated here. **It is not supported by the source that was cited for it and is withdrawn**, and in any case it would have expired long before the PPA's July 2026 final opinion, which is the current guidance.

**AI governance, enforcement powers and the fine structure** (per-violation bands, the doubling for continuing violations, the aggregate ceiling, the 5-percent-of-turnover cap with its lower ceiling for small and micro businesses, the private right of action for statutory damages without proof of harm, and the criminal exposure) are set out in `references/privacy-law-requirements.md`. Read that file before quoting any number, because the bands and the caps interact.

### Step 8: Data Subject Rights (DSR) Workflow

The Privacy Protection Law grants individuals enforceable rights. A controller must have a documented workflow so requests do not slip past the statutory deadline (which is short and judicially enforceable).

**Rights granted by the PPL:**

| Right | Statute | Practical form |
|-------|---------|----------------|
| Inspection (access) | Section 13 | Receive a copy of personal data held in the database, in Hebrew, English, or Arabic |
| Correction | Section 14 | Request correction or deletion of inaccurate, incomplete, unclear, or out-of-date data |
| Removal from direct-mail database | Section 17F | Demand removal; controller must comply and confirm |
| Withdrawal of consent | Section 8C (Amendment 13) | Must be as easy as granting consent |

**Response timeline.** Under the Privacy Protection Regulations, controllers must respond to inspection and correction requests **within 30 days**. If the controller fails to respond within 30 days, the data subject may appeal to a Magistrate's Court (this is the fastest enforcement path open to individuals, faster than waiting for PPA enforcement).

**Workflow template:**
1. **Intake channel** that is published in the privacy policy (email to the DPO, in-app form, or postal address). The PPO is the named contact when one is required under Amendment 13.
2. **Identity verification** proportionate to the sensitivity (do not over-collect to verify; a national-ID copy is excessive for a basic profile-data request).
3. **Log the request** with timestamp on receipt. The 30-day clock starts from receipt, not from when the team gets around to it.
4. **Triage by right type:** access vs correction vs direct-mail removal vs withdrawal. Each has a different operational path.
5. **Response template in Hebrew, English, or Arabic** as the user chose. Refusals must be reasoned and cite the legal basis.
6. **Document the response** in the request log. This is your evidence of compliance.

**Refusal grounds (narrow):** refuse inspection only on specific statutory grounds (unjustified trade-secret disclosure, prejudice to an active investigation). Default to disclosure when in doubt.

### Step 9: Data Protection Impact Assessment (DPIA)

A DPIA is a structured pre-processing assessment documenting privacy risks, the alternatives
considered and the mitigations chosen. **The Privacy Protection Law contains no GDPR-Article-35
style statutory DPIA duty**, so do not tell an Israeli controller the law requires one by name.
What the PPA does say, in its AI guidance, is that a DPIA is expected practice for higher-risk
processing and that the Privacy Protection Officer conducts it. The full method, when to trigger
one and what it must contain are in `references/privacy-law-requirements.md`.

### Step 10: Minors' and Children's Data

The Privacy Protection Law does not have a dedicated minors' provision, but other statutes and PPA guidance create heightened obligations whenever a controller processes data on individuals under 18.

**Consent rules:**
- The Legal Capacity and Guardianship Law, 1962 provides that legal acts of a minor (under 18) may be cancelled if performed without parental or guardian consent. Privacy consent obtained from a minor is therefore exposed to retroactive invalidation. Default rule: **obtain parental consent for processing personal data of users under 18**, especially for marketing, analytics, and behavioral profiling.
- Age verification mechanism matters: a simple "I am 18" checkbox is not a defensible consent record for a children-targeted service.

**Biometric data:**
- Under the Inclusion of Biometric Means of Identification in Identity Documents and in an Information Database Law, 5770-2009 (the biometric ID-card framework), fingerprints are not collected from applicants under age 12; only facial photographing is performed. Other biometric processing involving minors is subject to heightened restrictions and typically requires both parental and minor consent (for ages where the minor can understand).

**Ed-tech and school services:**
- The PPA treats schools and ed-tech vendors as high-scrutiny processors. A PPA cross-sector audit of educational websites and applications for minors (supervision in 2018-2019, report published January 2020) found defects in 23 of 24 audited entities. The takeaway: ed-tech is on the enforcement priority list, and "everybody does it this way" is not a defense.

**Practical controls for products with minor users:**
- Tag minor accounts/profiles in the data inventory.
- Disable behavioral advertising and cross-site tracking for minor profiles by default.
- Log parental-consent evidence (timestamp, IP, method).
- When schools are the controller, the school obtains parental consent; the vendor supports that flow.
- Offer a parental access/deletion channel and respond within the same 30-day DSR window.

## GDPR vs Israeli Law Key Differences
| Aspect | Israeli Law (post Amendment 13) | GDPR |
|--------|------------|------|
| Legal basis | Consent primary, limited exceptions | 6 legal bases |
| Privacy officer requirement | Public bodies (and their processors), data brokers (10,000+ records), large-scale sensitive-data processors, and large-scale systematic monitors | Broader requirement |
| Breach notification | Immediately to the PPA on a Severe Security Incident (no fixed hours); data subjects as the PPA directs | 72 hours |
| Administrative fines | Fixed per-violation amounts: NIS 150,000 under s.23כו(a) and NIS 300,000 doubled, up to NIS 320,000 for data-security breaches and NIS 640,000 doubled, plus criminal liability | Up to 4% global revenue |
| Right to erasure | Limited | Comprehensive (right to be forgotten) |
| Database registration | Public bodies and data brokers only (10,000+ records) | Not required (replaced by ROPA) |
| Personal data scope | Includes IP, geolocation, online identifiers (Amendment 13) | Includes online identifiers |
| AI governance | Required for automated decision-making (Amendment 13) | Article 22 automated decision-making rules |
| Extra-territorial scope | Limited | Broad |

## Examples

### Example 1: SaaS Startup Compliance
User says: "I'm building a SaaS with Israeli customers, what privacy requirements apply?"
Result: Assessment of security level, database registration need, privacy policy requirements, recommended consent mechanisms.

### Example 2: Data Breach Response
User says: "We discovered a data breach affecting Israeli users"
Result: Step-by-step breach response: contain, assess, notify authority, notify users if significant harm, document.

### Example 3: Cross-Border Data Transfer
User says: "We need to transfer Israeli customer data to our US servers"
Actions:
1. Assess data types for sensitivity level
2. Check if destination country has adequate protection
3. Determine the transfer basis under the Israeli Transfer of Data to Databases Abroad Regulations. **A basis alone is not sufficient**: those regulations impose further conditions on the transferor that THIS SKILL DOES NOT CARRY IN FULL, including obligations owed by the recipient. Read the regulations, or take advice, before transferring; do not treat a whitelist entry or a consent as the end of the analysis
4. Document compliance steps
Result: Transfer compliance checklist with specific steps for US data transfer under Israeli Privacy Protection Law.

## Bundled Resources

### Scripts
- `scripts/compliance_checker.py`, Runs a full Privacy Protection Law compliance assessment: determines security level (basic/medium/high), checks database registration requirements, and generates a compliance checklist with all applicable controls. Run: `python scripts/compliance_checker.py --help`

  **Use `--json` and use the exact key names.** Interactive mode reads stdin and cannot be driven
  by an agent. The valid keys are `record_count` (required), `has_sensitive`, `is_government`,
  `is_health_finance`, `is_direct_marketing`, `is_credit_service`, `has_cross_border`. The script
  now REFUSES an unrecognised key rather than defaulting it away: before this, passing `records`
  and `sensitive` instead of `record_count` and `has_sensitive` returned BASIC with 9 checklist
  items for a 150,000-record sensitive health database that in fact requires HIGH with 25, silently
  and with no warning. A downgrade like that walks an organisation into exactly the fines this
  skill documents, so a typo must fail loudly rather than answer quietly.

### References
- `references/privacy-law-requirements.md`, Detailed breakdown of the Privacy Protection Law 1981 and 2017 Security Regulations including database registration process, security level requirements, consent rules, cross-border transfer rules, breach notification procedures, and penalties. Consult when you need specific legal requirements, section numbers, or GDPR comparison details beyond what the instructions cover.
- `references/consent-banner-implementation.md`, Copy-pasteable TypeScript/React code for an Amendment 13 + GDPR compliant consent banner: pub-sub store with SSR sentinel, localStorage + companion cookie (12-month TTL, `CONSENT_VERSION`-bumped re-prompt), cross-tab sync via `storage` event, server-side cookie check for SSR gating, Sentry pre-init hydration pattern and mid-session Replay attach, essential-event allowlist, dismissal-as-refusal handling. Consult when the user wants to ship the consent UI itself, not just understand the law.

## Implementing a Compliant Consent Surface

The Privacy Protection Law after Amendment 13, GDPR for EU visitors, and the 2017 Security Regulations all require **explicit, opt-in, granular consent** before collecting personal data beyond what is strictly necessary to deliver the service. The consent surface is where that requirement becomes code. A banner copy-pasted from a generic template almost always fails one of the legal tests below. This section covers the UI patterns that satisfy all three legal frames at once.

### State Model

Model consent as three layers:

1. **Essential** (always on, never toggled): session auth, CSRF, consent cookie itself, bot protection (Turnstile), accessibility preferences, anything required to deliver the requested service. The user has no choice here, by design.
2. **Optional categories** (explicit opt-in): analytics, session replay (Clarity / Hotjar / FullStory), error monitoring with user data (Sentry Session Replay), marketing, personalization.
3. **No consent yet** (first visit): distinct from "rejected all" and from "accepted all". Treat as null.

The persisted state is a tagged version + category map + timestamp:

```ts
interface ConsentState {
  version: number;          // bump to force re-prompt when adding a category
  categories: {
    analytics: boolean;
    session_replay: boolean;
    error_monitoring: boolean;
    // add categories as needed; each gets its own opt-in
  };
  timestamp: string;        // ISO; used for 12-month re-prompt
}
```



### Cross-Tab Sync

Users open multiple tabs. If they reject consent in one, the others must respect that immediately. Listen for the `storage` event, which fires across tabs sharing the same origin:

```ts
function onStorageEvent(e: StorageEvent) {
  if (e.key === null || e.key === CONSENT_STORAGE_KEY) notify();
}
// Attach in subscribe() when first listener is added, detach when last leaves.
```

### Dismissal-As-Refusal

GDPR Article 4(11) and the EDPB guidance require that dismissing a consent banner counts as refusal. Amendment 13 is aligned. That means:

- **Escape key** = reject all
- **Close button (X)** = reject all
- **Clicking outside the banner** = leave banner visible (do NOT treat as accept)

```tsx
// ESC handler inside the banner component
useEffect(() => {
  if (!promptOpen) return;
  function onKey(e: KeyboardEvent) {
    if (e.key === 'Escape') rejectAll();
  }
  window.addEventListener('keydown', onKey);
  return () => window.removeEventListener('keydown', onKey);
}, [promptOpen, rejectAll]);
```

### Visual Equal Weight for Reject and Accept

Multiple European DPA enforcement decisions require that Reject and Accept carry equal visual weight. (This was previously attributed to GDPR Recital 42, which does not say it; Recital 42 covers demonstrability and freely-given consent, and the 'clear affirmative act' language is Recital 32.) In practice:

- Same button style (both primary, or both outline)
- Same width
- Same position (side by side, not one hidden behind "Customize")
- "Customize" is a third action, not a replacement for "Reject"

```tsx
<div className="grid grid-cols-3 gap-2">
  <Button size="sm" variant="outline" onClick={rejectAll}>{dict.rejectAll}</Button>
  <Button size="sm" variant="outline" onClick={openPreferences}>{dict.customize}</Button>
  <Button size="sm" onClick={acceptAll}>{dict.acceptAll}</Button>
</div>
```

### Gating the Trackers

The consent state must actually prevent non-consented trackers from running. A banner that does not stop scripts is worse than no banner (it creates a paper trail of false compliance).

```tsx
// components/consent/consent-gated-trackers.tsx
export function ConsentGatedTrackers() {
  const { isAllowed } = useConsent();
  return (
    <>
      {isAllowed('analytics') && <Analytics />}
      {isAllowed('analytics') && <SpeedInsights />}
      {isAllowed('session_replay') && <ClarityScript />}
    </>
  );
}
```

Also gate the client-side `trackEvent` helper, events emitted before consent is granted should be dropped, not queued:

```ts
const ESSENTIAL_EVENTS = new Set([
  'consent_banner_shown', 'consent_accepted', 'consent_rejected',
  'consent_customized', 'consent_reopened', 'auth_sign_in',
]);

export function trackEvent(event: string, data?: Record<string, unknown>) {
  if (!ESSENTIAL_EVENTS.has(event) && !window.__consent?.analytics) return;
  // ...send to analytics backend
}
```

The essential-event allowlist is for legally transactional events (the consent choice itself, auth), not a general escape hatch.


### Server Component Gating

Server Components can read the companion cookie directly:

```ts
// lib/consent/server.ts
import { cookies } from 'next/headers';
import { CONSENT_COOKIE_NAME } from './store';

export async function isAnalyticsAllowedServerSide(): Promise<boolean> {
  const store = await cookies();
  return store.get(CONSENT_COOKIE_NAME)?.value === '1';
}
```

Use it to gate `after()` calls that increment analytics counters:

```tsx
if (await isAnalyticsAllowedServerSide()) {
  after(() => incrementBundleViews(slug));
}
```

### Audit Trail

Amendment 13 and GDPR require you to demonstrate consent on demand. Emit five analytics events through your existing pipeline:

- `consent_banner_shown` (first show only)
- `consent_accepted`
- `consent_rejected`
- `consent_customized`
- `consent_reopened` (user re-opens from the footer link)

Store them through the same `analytics_events` pipeline you already have, no new table needed. These are the events the allowlist in `trackEvent` lets through even when consent is denied, precisely so you have the refusal on record.

See `references/consent-banner-implementation.md` for complete copy-pasteable code covering the pub-sub store, the `ConsentProvider`, the banner, the preferences dialog, the tracker gate, and the Sentry hydration hook.

## Consent UI Anti-Patterns

See `references/consent-ui-anti-patterns.md`.

Consent-banner engineering detail (persistence, the Sentry integration and the SSR sentinel pattern) is in `references/consent-banner-implementation.md`.

## Gotchas

- Amendment 13 took effect on August 14, 2025 and is live law, not a pending proposal. Agents trained on pre-2025 data may treat Amendment 13 as a future change or miss it entirely. Always assume it applies when advising on Israeli privacy compliance today.
- Amendment 13 expands "personal data" to include IP addresses, geolocation, and online identifiers. This pulls standard web analytics and mobile telemetry into scope. Agents may still apply the older narrower definition and underestimate what counts as personal data.
- Administrative fines are per-violation statutory amounts (NIS 150,000 for the Section 23כו(a) list, doubled for databases of 1,000,000+ people; NIS 320,000 for specified data-security breaches), with per-person components of NIS 50 or 100 for unlawful approaches (floor NIS 30,000) and NIS 2 or 4 per person in the database for other violations, and a request-based reduction to 5% of turnover where the penalty exceeds that. Section 15א allows court-awarded damages without proof of harm up to NIS 10,000 per violation, alongside criminal liability.
- Israel does NOT have a GDPR-style 72-hour breach deadline. Under the Data Security Regulations (2017, predating Amendment 13), a "Severe Security Incident" is reported to the PPA "immediately" (miyad) on discovery, and the PPA may direct notifying affected data subjects. Agents often wrongly import GDPR's 72-hour rule, do not.
- Israeli Privacy Protection Law predates GDPR (1981 vs 2016) and still has key differences even after Amendment 13: a narrower right to erasure, and database registration still exists (though narrowed to public bodies and data brokers, plus a separate 100,000-record especially-sensitive notification tier). Agents may incorrectly apply GDPR rules to Israeli contexts.
- **The EU adequacy decision runs the other way, and earlier versions of this skill stated it backwards.** Adequacy authorises transfers FROM the EU TO Israel. An Israeli controller sending data OUT to the EU relies on the Israeli Transfer of Data to Databases Abroad Regulations instead, whose whitelist covers EU member states. Naming the wrong instrument in a transfer assessment is the kind of error that survives review because the conclusion happens to be permissive either way. Agents may incorrectly flag Israel-to-EU transfers as requiring additional safeguards.
- The 2017 Security Regulations define three security levels (basic/medium/high) based on record count and data sensitivity. Agents may apply a one-size-fits-all approach instead of the tiered model.
- Penalties under Israeli privacy law include criminal liability in addition to administrative fines, but the five-year figure belongs to a specific offence and should not be attached to any breach. Section 5 sets five years for WILFULLY invading another person's privacy, and section 16 the same for breach of the confidentiality duty. The offences Amendment 13 itself added are lower: six months for obstructing the Authority (s.23נג), two years for misleading it (s.23נד), and three years for processing without authorisation or for misleading a person into handing over personal data (ss.23נה-23נז). Agents may understate the severity by comparing only to GDPR's monetary penalties, or overstate it by quoting five years for a registration failure.

## Troubleshooting

### Error: "Unsure about security level"
Cause: Borderline case between basic/medium/high
Solution: When in doubt, apply the higher level. The cost difference is small compared to non-compliance risk.

### Error: "Borderline DPO appointment threshold"
Cause: The 10,000-individual threshold for the data-broker DPO trigger is a count of distinct individuals in the database, but the legal text is silent on counting methodology (active vs historical accounts, deduplicated identities vs raw rows, multi-database aggregation).
Solution: Count distinct individuals across all linked databases under the same controller, including historical records you have not purged. When the count is near the threshold, appoint a DPO defensively; the cost of appointing is low compared to the cost of an enforcement finding that you were over-threshold and unrepresented. Document the counting methodology so a PPA inspector can audit it.

### Error: "Cross-border transfer to a country without an adequacy decision"
Cause: The destination country (US, India, Singapore, most non-EU jurisdictions) does not have PPA-recognized adequate protection, so the default ban on transfer applies.
Solution: Pick the strongest available alternative basis in this order: (1) controller-to-controller or controller-to-processor data transfer agreement with privacy obligations equivalent to Israeli law (Israeli equivalent of GDPR SCCs), (2) explicit informed consent of the data subject naming the destination country and the risks, (3) statutory exception (contract performance, legal proceedings, vital interests). Do NOT rely on "legitimate interest" alone for cross-border transfer; the PPA reads that exception narrowly. Document the basis in the data inventory.

## Reference Links

| Source | URL | What to check |
|---|---|---|
| Privacy Protection Authority (gov.il) | https://www.gov.il/en/departments/the_privacy_protection_authority | Enforcement, database registration and notification, guidance |
| Amendment 13 page (gov.il) | https://www.gov.il/he/pages/13_amendment | Overview of the reform and its obligations |
| Amendment 13 professional guide (gov.il) | https://www.gov.il/he/pages/guide_tikon13_professional | Detailed implementation guidance for controllers and processors |
| Amendment 13 FAQ (gov.il) | https://www.gov.il/he/pages/tikun13_qa | Common questions on registration, DPO, breach reporting |
| Protection of Privacy Law, 5741-1981 (consolidated) | https://www.nevo.co.il/law_html/law00/71631.htm | Primary statute text. The gov.il slug previously listed here is DEAD (it renders to /he/error) and was removed; do not restore it |

gov.il pages may return HTTP 403 to automated clients; open them in a browser.

## Recommended MCP Servers

- `israel-law` MCP, surfaces Israeli primary legislation and regulations (including the Protection of Privacy Law and related regulations). Use it to pull the current statutory text when a compliance question turns on exact wording. Verify the live gov.il pages above for PPA guidance and forms, which an MCP statute index does not cover.
