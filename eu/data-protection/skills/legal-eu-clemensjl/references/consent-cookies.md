# ePrivacy, cookies and consent

Status as at 2026-08-05.

Two instruments stack. **Directive 2002/58/EC (ePrivacy Directive)** governs access to the terminal equipment; **Regulation (EU) 2016/679 (GDPR)** governs what happens to any personal data afterwards. The ePrivacy Directive is a **Directive** — it reaches the user only through national transposition, and the enforcing authority, the sanction and sometimes the consent lifetime are national. The consent *standard* is not national: Art 2(f) ePrivacy Directive refers to the definition of consent in EU data protection law, which since 2018 means Art 4(11) and Art 7 GDPR.

**The ePrivacy Regulation is dead.** The Commission announced the withdrawal of the 2017 proposal in its 2025 work programme on 11.02.2025, formally decided the withdrawal on 16.07.2025, and published the withdrawal notice in the Official Journal on 06.10.2025. Directive 2002/58/EC and its national transpositions remain in force. Any text that says "until the ePrivacy Regulation arrives" is stale.

A pending Commission proposal, the Digital Omnibus Regulation COM(2025) 837 of 19.11.2025, would move terminal-equipment access into the GDPR via a new Art 88a. It is **not adopted** — still tabled in Parliament as of mid-2026. Do not draft to it.

## Art 5(3) ePrivacy Directive — the operative rule

Storing information, or gaining access to information already stored, in the terminal equipment of a subscriber or user is only allowed on condition that the user has given consent, having been provided with clear and comprehensive information in accordance with data protection law.

Two exemptions, both narrow:

1. transmission exemption — storage or access for the **sole** purpose of carrying out the transmission of a communication over an electronic communications network
2. strict necessity exemption — **strictly necessary** in order to provide an information society service **explicitly requested** by the user

Strictly necessary means necessary for the service the user asked for, not necessary for the business. Analytics, A/B testing, audience measurement, personalisation, fraud scoring beyond the session, and consent-state persistence for marketing purposes are not covered.

**Art 5(3) does not depend on personal data.** It applies to any information stored on or read from the device, personal or not. This is why "we anonymise it" is never an answer to a cookie question.

## What counts as terminal-equipment access — EDPB Guidelines 2/2023

Guidelines 2/2023 on the technical scope of Art 5(3) of the ePrivacy Directive, **version 2.0, adopted 16.10.2024, final**. The EDPB reads Art 5(3) as technology-neutral. Covered, among others:

- cookies of every flavour, including first-party
- `localStorage`, `sessionStorage`, IndexedDB and any other client-side store
- tracking pixels and beacons, in web pages **and in emails**
- URL-based and cache-based tracking where an identifier is passed or read
- device fingerprinting — reading device characteristics counts as "gaining access", even where nothing is stored
- IoT and connected-device reporting back to a server
- unique identifiers embedded in software or firmware

Consequence: replacing cookies with `localStorage`, server-side tagging, fingerprinting or pixel-only tracking does **not** escape the consent requirement. Nor does a first-party analytics script.

## The consent standard

Art 4(11) GDPR: freely given, specific, informed and unambiguous, expressed by a statement or by a **clear affirmative action**. Art 7 GDPR adds:

- 7(1) the controller must be able to **demonstrate** consent — log it
- 7(2) a consent request bundled with other matters must be clearly distinguishable, intelligible, in plain language
- 7(3) withdrawal must be possible **at any time** and must be **as easy as giving** consent
- 7(4) whether consent was freely given must take account of conditionality — tying a service to consent that is not necessary for it

Guidelines 05/2020 on consent under Regulation 2016/679, adopted 04.05.2020, is the reference text. Scrolling, continued browsing and inactivity are not clear affirmative action. Pre-ticked boxes and default-on sliders are not consent. [[UNVERIFIED: Case C-673/17 Planet49, judgment of 01.10.2019, is the CJEU authority usually cited for pre-ticked boxes — case number and date not re-verified against curia.europa.eu in this pass; do not cite it in a filing without checking]]

## Banner requirements — EDPB Cookie Banner Taskforce

"Report of the work undertaken by the Cookie Banner Taskforce", adopted **18.01.2023**. Not binding, but it is the common enforcement checklist national DPAs apply to complaints. Its positions were an agreed **minimum**; several DPAs go further.

| Issue | Taskforce position |
|---|---|
| Reject option on the first layer | No unanimous position on whether it is legally compelled, but the baseline holds: no non-exempt cookie may be set without consent. In practice most DPAs treat an accept-only first layer as non-compliant. |
| Pre-ticked boxes | Invalid for consent. Acceptable only where they concern strictly necessary processing that needs no consent at all. |
| Deceptive link design | The banner must clearly inform, and must not suggest that accepting is required to access the site. A refuse option hidden inside body text is non-compliant. |
| Button colour and contrast | No fixed contrast ratio imposed; assessed case by case. A refuse button rendered illegible is non-compliant. |
| Legitimate interest for cookie placement | Not available. Placement requires consent; and where valid consent is missing, subsequent processing cannot be rescued by legitimate interest. |
| "Essential" classification | No stable EU list exists. The controller bears the burden of documenting and proving strict necessity per cookie. |
| Withdrawal icon | No uniform requirement for a floating icon. A visible, standardised, permanently reachable link satisfies Art 7(3) GDPR. |

**Consent duration is not set at EU level.** Neither the ePrivacy Directive nor the GDPR fixes a lifetime. Several national DPAs do (the widely cited 6 or 13 month figures are national practice, not EU law). Do not state a number without naming the member state that set it — that belongs in the national skill.

Deceptive design more broadly: EDPB Guidelines 03/2022 on deceptive design patterns in social media platform interfaces, **version 2.0 adopted 14.02.2023**. Written for social media but applied by analogy to any interface that steers a data-protection choice.

## Cookie walls and pay-or-consent

A pure cookie wall — no access without consent to non-essential tracking — fails Art 7(4) GDPR because the consent is not freely given.

**EDPB Opinion 08/2024 on valid consent in the context of consent or pay models implemented by large online platforms, adopted 17.04.2024.** Non-binding, but it is the reference position. In most cases a large online platform cannot obtain valid consent by confronting users with only a binary choice between consenting to processing for behavioural advertising and paying a fee. The EDPB expects a further alternative that is free of charge and involves no, or substantially less, personal data processing. Offering only a paid alternative should not be the default.

The Opinion is formally limited to **large online platforms**. It does not automatically settle the position for a small publisher, but a small publisher relying on a binary wall is arguing against the EDPB's reasoning, not around it.

## Direct marketing — Art 13 ePrivacy Directive

Art 13(1): unsolicited communications for direct marketing by automated calling systems, fax or **electronic mail** (including SMS and comparable messaging) require **prior consent**.

Art 13(2) soft opt-in: an existing customer relationship permits marketing of the sender's own **similar** products or services without fresh consent, where three conditions are met cumulatively —

1. the electronic contact details were obtained **in the context of the sale** of a product or service to that customer,
2. the marketing concerns the sender's own similar products or services,
3. the customer is given the opportunity to object, **clearly and distinctly, free of charge and easily**, both when the details are collected and in **every** subsequent message.

**Case C-654/23 Inteligo Media, judgment of 13.11.2025.** The CJEU held that "sale" does not require direct monetary payment — creation of a free account granting limited content access can constitute a sale within Art 13(2), indirect remuneration being sufficient. It further held that where the Art 13(2) conditions are met, the soft opt-in itself supplies the legal basis; no separate Art 6 GDPR basis is required.

Art 13(4): in any event, sending marketing email that disguises or conceals the sender's identity, or without a valid address to which the recipient may send an opt-out request, is prohibited.

Soft opt-in is transposed nationally with variations — some member states restrict it further, some require an opt-out box at collection in a particular form. Check the national layer.

## Consent record — what to log

Art 7(1) GDPR requires demonstrability. A defensible record contains, per consent event:

- timestamp
- the identifier tying the record to the browser/user
- the exact banner version and the exact text shown
- the categories accepted and refused, individually
- the mechanism (button clicked)
- the withdrawal event, when it happens

## Template — consent banner text

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<div role="dialog" aria-modal="true" aria-labelledby="c-h">
  <h2 id="c-h">Cookies and similar technologies</h2>
  <p>
    We use technically necessary storage to run this site. With your consent we
    also use [[CATEGORIES: analytics, marketing, embedded media]], which store or
    read information on your device and process personal data for the purposes
    described in our <a href="[[PRIVACY URL]]">privacy notice</a>.
    Some providers are located in [[THIRD COUNTRY]] — see
    <a href="[[PRIVACY URL]]#transfers">international transfers</a>.
  </p>
  <p>You can withdraw your consent at any time with the same effort.</p>

  <button type="button" data-action="reject-all">Reject all</button>
  <button type="button" data-action="accept-all">Accept all</button>
  <button type="button" data-action="settings">Individual settings</button>
</div>
```

Both primary buttons on the **first** layer, same size, same weight, same contrast. No dark-on-dark reject. No "Accept" as the only styled button.

## Checkpoints

- [ ] Loaded in a fresh profile with the network tab open: no non-exempt request fires before a decision
- [ ] Application tab checked: no non-exempt cookie, `localStorage`, `sessionStorage` or IndexedDB entry written before a decision
- [ ] Reject on the first layer, visually equivalent to Accept
- [ ] No pre-ticked categories, no default-on sliders
- [ ] Per-purpose granularity, not a single all-or-nothing toggle
- [ ] Withdrawal reachable permanently and in as few steps as granting (Art 7(3) GDPR)
- [ ] "Strictly necessary" list documented per cookie with the reason (burden of proof is on the controller)
- [ ] Legitimate interest not claimed for any terminal-equipment access
- [ ] Fingerprinting, pixels, `localStorage` and server-side tagging treated as in scope (EDPB Guidelines 2/2023 v2.0)
- [ ] Email tracking pixels behind consent
- [ ] Consent log captures timestamp, banner version, text version, per-category choice
- [ ] No cookie wall without a genuine alternative; pay-or-consent assessed against EDPB Opinion 08/2024
- [ ] Consent lifetime: no number stated unless the national rule that sets it is named
- [ ] Marketing email: prior consent, or all three Art 13(2) conditions satisfied and documented
- [ ] Unsubscribe in every message, free of charge and easy (Art 13(2))
- [ ] No reference to the ePrivacy Regulation as forthcoming law
- [ ] All `[[…]]` placeholders resolved or reported as open
