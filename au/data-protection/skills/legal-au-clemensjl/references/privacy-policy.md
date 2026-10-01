# APP privacy policy

Required of every APP entity. Status as at 2026-08-05. Source for the APP text and guidance: OAIC, *Australian Privacy Principles Guidelines*, Chapters 1, 6, 7, 8, 11, 12, 13.

## APP 1 — open and transparent management

- **APP 1.2:** take reasonable steps to implement practices, procedures and systems that ensure compliance with the APPs and enable the entity to deal with inquiries and complaints. This is an operational obligation, not a document.
- **APP 1.3:** have a clearly expressed and up-to-date APP privacy policy about how the entity manages personal information.
- **APP 1.5:** make the policy available free of charge and in an appropriate form — in practice a plain HTML page, not a PDF download, not behind a login, not behind a banner.
- **APP 1.6:** on request, provide the policy in the form the person asks for, if reasonable.

**APP 1.4 — mandatory contents.** The policy must contain:

| | Content |
|---|---|
| (a) | the kinds of personal information the entity collects and holds |
| (b) | how personal information is collected and held |
| (c) | the purposes for which personal information is collected, held, used and disclosed |
| (d) | how an individual may access their personal information and seek its correction |
| (e) | how an individual may complain about a breach of the APPs or a registered APP code, and how the entity will deal with the complaint |
| (f) | whether the entity is likely to disclose personal information to overseas recipients |
| (g) | if so, the countries in which those recipients are likely to be located, if it is practicable to specify them |

"If it is practicable" is not an escape hatch. If the recipient list is known — and for a website it always is, because the vendor contracts exist — the countries are specified.

## APP 1.7 to 1.9 — automated decisions, from 10 December 2026

Inserted by the Privacy and Other Legislation Amendment Act 2024, commencing **10 December 2026**. Where the entity has arranged for a computer program to use personal information to make, or to do a thing substantially and directly related to making, a decision that could reasonably be expected to significantly affect an individual's rights or interests, the privacy policy must state the kinds of personal information used and the kinds of decisions made.

Scope this now: credit and eligibility decisions, automated pricing that varies by person, fraud scoring that blocks orders, automated account suspension, automated content moderation with consequences, and AI-assisted triage that determines an outcome. Write the disclosure before the date, not after.

## The other APPs the policy has to reflect truthfully

- **APP 3** — collection. Personal information may be collected only if reasonably necessary for, or directly related to, the entity's functions or activities. Sensitive information additionally requires consent (APP 3.3). Collect from the individual unless an exception applies (APP 3.6).
- **APP 6** — use and disclosure. Only for the primary purpose, or for a secondary purpose the individual would reasonably expect and that is related (directly related, for sensitive information), or with consent, or under one of the permitted general or health situations. Reasonable expectation is measured against what the collection notice said.
- **APP 7** — direct marketing. An organisation must not use or disclose personal information for direct marketing unless an exception applies: APP 7.2 where the information came from the individual, they would reasonably expect the use, and a simple opt-out is provided; APP 7.3 where it came from a third party or the expectation is absent, requiring consent or impracticability plus a prominent opt-out statement in each message. Sensitive information requires consent (APP 7.4). Individuals may ask the entity to stop, and to identify the source (APP 7.6). **APP 7.8: APP 7 does not apply to the extent that the Do Not Call Register Act 2006, the Spam Act 2003 or other prescribed legislation applies** — so email and SMS marketing is governed by the Spam Act, and APP 7 governs what those Acts leave uncovered, such as postal mail and in-app messaging that falls outside the Spam Act.
- **APP 8** — cross-border disclosure. Before disclosing to an overseas recipient, take reasonable steps to ensure the recipient does not breach the APPs (APP 8.1) — in practice an enforceable contract that also binds subcontractors. Exceptions in APP 8.2 include a reasonable belief that the recipient is subject to a substantially similar law with accessible enforcement (8.2(a)), and express informed consent after telling the individual APP 8.1 will not apply (8.2(b)). **Section 16C:** where APP 8.1 applies and no exception is engaged, an act of the overseas recipient that would breach the APPs is taken to have been done by the disclosing entity and is a breach by it. Reasonable steps do not transfer the liability.
- **Use versus disclosure for cloud services:** providing personal information to an overseas cloud provider can be a use rather than a disclosure where the entity retains effective control — a binding contract limiting handling to the entity's purposes, equivalent control over subcontractors, and rights of retrieval and deletion. Absent that, it is a disclosure and APP 8 applies. Decide this per vendor and record the reasoning.
- **APP 11.1** — take reasonable steps to protect personal information from misuse, interference and loss, and from unauthorised access, modification or disclosure.
- **APP 11.2** — take reasonable steps to destroy or de-identify personal information once it is no longer needed for any permitted purpose, unless it is a Commonwealth record or retention is required by an Australian law or a court or tribunal order. This is the closest thing Australia has to erasure and it is not a right exercisable on request.
- **APP 12** — access. On request, give the individual access to their personal information (12.1). Agencies must respond within 30 days; organisations within a reasonable period (12.4). An organisation may refuse on the grounds in APP 12.3, must not charge for making a request, and may charge for giving access only if the charge is not excessive (12.8). Written reasons and the complaint avenues must be given on refusal (12.9).
- **APP 13** — correction. Correct on request or on becoming aware the information is inaccurate, out of date, incomplete, irrelevant or misleading; on refusal, give written reasons and, if asked, associate a statement of the individual's position with the record.

## Template

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h1>Privacy Policy</h1>
<p>[[Legal entity name]] (ABN [[ABN]]) ("we", "us") is bound by the Privacy Act 1988 (Cth)
   and the Australian Privacy Principles. This policy explains how we manage personal
   information. Last updated: [[date]].</p>

<h2>What we collect</h2>
<p>We collect: [[list the actual categories — name, email, postal address, phone, order
   history, payment token, support correspondence, IP address, device and browser data,
   pages viewed]]. We do not collect sensitive information except: [[list or state "we do
   not collect sensitive information"]].</p>

<h2>How we collect it and where we hold it</h2>
<p>We collect personal information directly from you when you [[create an account, place an
   order, subscribe, contact us]], and automatically through our website and app when you
   use them. We hold it in [[hosted systems, named]] located in [[countries]].</p>

<h2>Why we collect, hold, use and disclose it</h2>
<p>[[Purpose by purpose. One line each: fulfilling orders; processing payments; providing
   support; sending service messages; sending marketing where you have consented;
   preventing fraud; meeting record-keeping obligations under [[named law]].]]</p>

<h2>Who we disclose it to</h2>
<p>[[Named categories with the actual vendors: hosting, payment processing, delivery,
   email delivery, analytics, customer support.]] We do not sell personal information and
   we do not disclose it for another organisation's marketing.</p>

<h2>Overseas disclosure</h2>
<p>We are likely to disclose personal information to recipients located in [[countries]].
   Before doing so we take reasonable steps to ensure they handle it consistently with the
   Australian Privacy Principles.</p>

<h2>Automated decisions</h2>
<p>[[From 10 December 2026, if applicable: the kinds of personal information used by
   computer programs to make, or to do something substantially and directly related to
   making, decisions that could significantly affect your rights or interests, and the
   kinds of those decisions. Otherwise: "We do not use computer programs to make decisions
   that significantly affect your rights or interests."]]</p>

<h2>Security and retention</h2>
<p>We take reasonable steps to protect personal information from misuse, interference and
   loss and from unauthorised access, modification or disclosure, including [[actual
   measures]]. We keep [[category]] for [[period or criterion]] and then destroy or
   de-identify it, unless we are required to keep it by law.</p>

<h2>Access and correction</h2>
<p>You may ask us for access to the personal information we hold about you, and ask us to
   correct it. Contact [[privacy contact]]. We will respond within a reasonable period. If
   we refuse, we will tell you why in writing and how to complain.</p>

<h2>Marketing</h2>
<p>[[If marketing: We send marketing messages only where you have consented or where the
   Spam Act 2003 (Cth) otherwise permits it. Every message contains an unsubscribe
   facility, and we action unsubscribes within 5 business days.]]</p>

<h2>Complaints</h2>
<p>Complaints go to [[privacy contact, email and postal address]]. We will acknowledge
   within [[period]] and respond within [[period]]. If you are not satisfied, you may
   complain to the Office of the Australian Information Commissioner at oaic.gov.au,
   GPO Box 5218, Sydney NSW 2001, or 1300 363 992.</p>
```

## Checkpoints

- [ ] Reachable without login, without payment and without dismissing anything
- [ ] All seven APP 1.4 items present, each with real content rather than a placeholder sentence
- [ ] Categories of information match what the site actually collects, verified against the network tab and the database schema
- [ ] Recipients match the vendors actually in use
- [ ] Overseas countries named, not "may be transferred internationally"
- [ ] No GDPR lawful bases, no "legitimate interest", no "data controller" unless the entity is genuinely also GDPR-bound and the section is marked as EU-facing
- [ ] No promise of a deletion right unless the business intends to honour it as a contractual commitment
- [ ] Access and correction routes named with a real contact, not a generic form
- [ ] OAIC named as the external complaint avenue, with correct contact details
- [ ] Automated decision-making disclosure drafted or an explicit "not applicable" recorded, ahead of 10 December 2026
- [ ] Every `[[…]]` resolved or reported as `[[MISSING: …]]`
