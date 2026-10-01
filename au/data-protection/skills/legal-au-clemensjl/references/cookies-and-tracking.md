# Cookies, analytics and tracking

**There is no cookie consent law in Australia.** No ePrivacy Directive Art 5(3) equivalent, no TTDSG, no TKG § 165, no consent requirement for storing or reading information on a user's device, and no regulator that issues cookie banner decisions. Status as at 2026-08-05.

A GDPR consent banner installed on an Australian-only site solves nothing that Australian law asks about, and it creates two new problems: it delays access to the privacy policy and collection notice, which are the things that actually are required, and it makes a compliance representation that may be false.

What Australian law does ask is a different question: **is this personal information, and if so, did you comply with APP 3, APP 5, APP 6, APP 8 and APP 11?**

## When tracking data is personal information

Personal information means information or an opinion about an identified individual, or an individual who is reasonably identifiable, whether or not true and whether or not recorded in a material form. The test is practical: could this entity, with the means available to it, connect the data to a person?

| Data | Usually personal information? |
|---|---|
| Aggregate page view counts with no identifiers | No |
| First-party analytics cookie ID, not joined to an account | Arguable; treat as personal information if it can be joined to an account, an order or an email |
| Analytics ID joined to a logged-in user | Yes |
| IP address | Depends on what else the entity holds and can link; treat as personal information where a linkage is realistic |
| Advertising pixel that returns a hashed email or a match key | Yes |
| Session replay recording form input or screen content | Yes, and frequently sensitive information as well |
| CRM or CDP profile keyed to an email address | Yes |

Where it is personal information, the APPs apply in full, whether or not the identifier is stored in a cookie, local storage, a fingerprint or a server log.

## What the APPs require of a tracking stack

- **APP 3.** Collect only what is reasonably necessary for, or directly related to, the entity's functions or activities. "We turned on every event because the tool has them" is not a function or activity. Sensitive information — health, sexual orientation, religion, political opinion, biometric data — requires consent, and a session replay tool recording a health enquiry form collects sensitive information whether or not anyone intended it.
- **APP 5.** Notify at or before collection. For passive collection the practical form is a short layered notice reachable from every page, plus specific notices at forms and checkout. See `collection-notice.md`.
- **APP 6.** Use only for the primary purpose or a related secondary purpose the individual would reasonably expect. Analytics data collected to improve the site and later used to build advertising audiences is a fresh purpose. What the notice said determines what is reasonably expected.
- **APP 7.** Building an audience for direct marketing from tracking data is a direct marketing use. Where the message is email or SMS, the Spam Act governs (APP 7.8).
- **APP 8 and s 16C.** Most tracking vendors are offshore. Assess each: does the entity retain effective control under contract (a use), or is it a disclosure? Where it is a disclosure, APP 8.1 requires reasonable steps, and s 16C leaves the entity liable for the recipient's acts regardless. Advertising platforms that use the data for their own purposes are disclosures — the contract says so.
- **APP 11.1 and 11.2.** Secure it, and set retention. Analytics tools default to long retention windows; shorten them deliberately and record the decision.

## Consent, where it is genuinely needed

Consent under the Privacy Act must be voluntary, informed, current, specific and given by a person with capacity. It is required for sensitive information (APP 3.3), for some direct marketing (APP 7.3, 7.4), and for the APP 8.2(b) cross-border exception. Where consent is the basis, the interface has to meet those criteria — which is a stricter bar than the average cookie banner, not a looser one.

If a consent interface is built for another reason — an EU audience under GDPR Art 3(2), a global product decision, or an ad platform's own contractual requirement — then it must actually work: no tags firing before a decision, reject as easy as accept, granular purposes, and withdrawal as easy as giving. A broken banner is worse than none, because it represents a level of control the site does not deliver, which is an ACL s 18 problem.

## Practical position for an Australian-only site

1. No consent banner. Instead, a persistent, plainly linked privacy page and a short collection notice at every collection point.
2. A written inventory of every third-party request the site makes, produced from the network tab in a fresh browser profile, not from what the CMS plugin list claims.
3. Each vendor classified: purpose, personal information yes/no, use or disclosure, country, contract in place, retention.
4. IP anonymisation and shortened retention where the tool supports it.
5. Session replay and heatmap tools configured to mask all input fields by default, and switched off entirely on pages that handle payment, health or identity data.
6. Advertising pixels reviewed for what they actually transmit — conversion value, product identifiers, hashed emails — and disclosed in the privacy policy and the checkout notice by name.
7. Embeds (video, maps, fonts, chat widgets) treated as third-party disclosures and listed.

## Template — tracking section of the privacy policy

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h2>Cookies and analytics</h2>
<p>Our website uses cookies and similar technologies. Australian law does not require us
   to obtain your consent to use them, but we want you to know what they do.</p>
<p>We use:</p>
<ul>
  <li><strong>Essential</strong> — [[session, cart, security, load balancing]]. The site
      does not work without these.</li>
  <li><strong>Analytics</strong> — [[named tool]], to understand how the site is used.
      [[Retention period]]. [[Whether IP is truncated.]] Data is held by [[vendor]] in
      [[country]].</li>
  <li><strong>Advertising</strong> — [[named platforms]], to measure and target our
      advertising. These platforms receive [[what is actually sent]] and use it for
      their own purposes. They are located in [[countries]].</li>
</ul>
<p>You can block or delete cookies in your browser settings. Blocking essential cookies
   will stop parts of the site working. [[If an opt-out mechanism exists, link it.]]</p>
```

## Checkpoints

- [ ] No consent banner on an Australian-only site unless there is a specific reason, documented
- [ ] Where a banner exists, no tag fires before the decision and reject is as easy as accept
- [ ] Network tab inventory produced from a clean profile, matching the vendor list in the privacy policy exactly
- [ ] Each identifier classified as personal information or not, with reasoning recorded
- [ ] Each vendor classified as use or disclosure for APP 8 purposes
- [ ] Offshore vendors listed with country, and contracts in place
- [ ] Analytics retention shortened from the tool's default
- [ ] Session replay masks inputs and is disabled on payment, health and identity pages
- [ ] No tracking on pages that collect sensitive information without consent
- [ ] Advertising audience building disclosed in the collection notice, not only in the policy
- [ ] Privacy policy and collection notices reachable without dismissing anything
- [ ] Every `[[…]]` resolved or reported as `[[MISSING: …]]`
