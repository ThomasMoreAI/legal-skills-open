# Email, SMS and telemarketing

Spam Act 2003 (Cth), Spam Regulations 2021, Do Not Call Register Act 2006 (Cth). Regulator: ACMA. Status as at 2026-08-05.

The Spam Act applies regardless of the Privacy Act small business exemption. APP 7 (direct marketing) does not apply to the extent the Spam Act or the Do Not Call Register Act applies (APP 7.8), so for email and SMS the Spam Act is the operative regime and APP 7 governs the gaps.

## Scope

The Spam Act regulates **commercial electronic messages** with an Australian link. That covers email, SMS, MMS and instant messaging. Voice telephony and fax are outside it — fax marketing sits in Part 2 of the Do Not Call Register Act regime and voice calls in the Do Not Call Register scheme. [[UNVERIFIED: the precise definitional sections of the Spam Act (the "electronic message" and "commercial electronic message" definitions in Part 1) were not confirmed against the text of the Act in this session; the operative sections 16, 17 and 18 below are confirmed from the Act's own section headings on legislation.gov.au]]

A message is commercial if, having regard to its content, any links, and the sender's identity, it would be concluded that its purpose is to offer, advertise or promote goods, services, land, a business or investment opportunity, or to assist a person to dishonestly obtain property or a gain. A transactional message — order confirmation, shipping notice, password reset, service outage notice — is not commercial. Adding an offer to a transactional message makes it commercial.

**Designated commercial electronic messages** are exempt from the consent and unsubscribe rules: factual messages with only limited permitted additional content, and messages from government bodies, registered political parties, registered charities and educational institutions to their own constituencies. The exemption is narrower than the sector labels suggest — a charity's fundraising appeal to its own supporters is treated differently from a commercial offer.

## The three rules

**Consent — s 16.** A commercial electronic message must not be sent without the consent of the account holder or the relevant electronic addressee.

- **Express consent** — the person actively opted in. The consent record has to show what wording they saw, when, from where, and to what they agreed. A pre-ticked box, a bundled "I agree to the terms and to receive marketing" control, and a mandatory checkbox to complete a purchase are not consent.
- **Inferred consent** — much narrower than marketers assume. It arises from the conduct and the business or other relationships between the parties, and from conspicuous publication of a work-related electronic address where the address is not accompanied by a statement that unsolicited commercial messages are not wanted **and** the message is directly relevant to the recipient's work role. It does not arise from someone giving you a business card, entering a competition, buying something once, or having their address appear on a public website in a personal capacity.
- Consent is not perpetual. A long-dormant relationship no longer supports inference.
- Purchased, rented, scraped or appended lists do not carry consent. Nor does consent given to another business, unless it expressly covered your messages and you can produce that record.
- The sender bears the burden of proving consent. Keep the record for as long as you keep the address, plus a limitation period.

**Identification — s 17.** The message must clearly and accurately identify the sender and include accurate information about how to contact the sender. In practice: the legal entity name (and trading name if different), ABN, and a working contact route that remains valid for at least 30 days after sending. A no-reply-only footer with no other contact route does not satisfy this.

**Unsubscribe — s 18.** The message must contain a functional unsubscribe facility. It must be presented clearly, be low-cost or free, remain functional for at least 30 days after the message was sent, and **the request must be actioned within 5 business days**. It must not require the person to log in, create an account, provide additional personal information, or state a reason. A single-click link that confirms removal is the safe design. Preference centres are permitted only if unsubscribing entirely is available in the same place and in the same number of steps.

## Penalties

The Spam Act is enforced by ACMA through formal warnings, infringement notices, enforceable undertakings and Federal Court penalty proceedings, and penalties scale with repetition and prior contact from ACMA. [[UNVERIFIED: current maximum penalty amounts under Part 4 of the Spam Act were not confirmed against the Act in this session]] ACMA publishes its enforcement actions; recent matters have involved large retail, ticketing and gambling brands over unsubscribe failures and consent records.

## Do Not Call Register

The Do Not Call Register Act 2006 prohibits making, or causing to be made, unsolicited telemarketing calls to a number on the Register, and marketing faxes to a registered number. Registration does not expire. A business that telemarkets must wash its call lists against the Register through an ACMA-accredited washing service before calling, and must comply with the Telecommunications (Do Not Call Register) (Telemarketing and Research Calls) Industry Standard on calling hours, identification and call termination. [[UNVERIFIED: the current title, year and permitted calling hours of the industry standard were not confirmed in this session]]

Permitted callers — including registered charities, educational institutions contacting current or former students or their households, government bodies, registered political parties and independent members, and market or social research callers — may call registered numbers, but consent-based rules and the industry standard still bind them.

Washing is not a one-off. Lists go stale.

## Template — consent capture and footer

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<label>
  <input type="checkbox" name="marketing" value="yes">
  Yes, email me [[what: new product releases and offers]] from [[entity]].
  About [[frequency]]. Unsubscribe any time.
</label>
```

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<footer>
  <p>[[Legal entity name]] (trading as [[trading name]]), ABN [[ABN]],
     [[street address, suburb, state, postcode]].
     [[email]] · [[phone]]</p>
  <p>You are receiving this because [[you subscribed on our website on {{date}} /
     you bought from us on {{date}}]].
     <a href="[[one-click unsubscribe URL]]">Unsubscribe</a> —
     we action unsubscribe requests within 5 business days.</p>
</footer>
```

Store against every subscriber: address, consent type (express or inferred), the exact wording shown, timestamp, source URL or channel, IP address where captured online, confirmation event if double opt-in is used, and the unsubscribe timestamp when it happens. Double opt-in is not required by the Act but is the cheapest way to discharge the burden of proof.

## Checkpoints

- [ ] Every address in the sending list traceable to a consent record or a defensible inference
- [ ] No purchased, rented, scraped or appended addresses
- [ ] Consent control unticked, unbundled, and not a condition of purchase
- [ ] Consent wording matches what is actually sent — scope creep from "product updates" to "partner offers" is a fresh consent question
- [ ] Sender identification carries legal entity, ABN and a working contact route valid for 30 days
- [ ] Unsubscribe is one click, needs no login and no extra data, works for at least 30 days
- [ ] Unsubscribes propagate to every sending system within 5 business days, including CRM, ESP, ad platform audiences and SMS gateway
- [ ] Transactional messages carry no promotional content, or are treated as commercial if they do
- [ ] SMS messages carry sender identification and an unsubscribe route despite the character limit
- [ ] Telemarketing lists washed against the Do Not Call Register before every campaign
- [ ] APP 5 collection notice present at the signup point, separate from the consent control
- [ ] Every `[[…]]` resolved or reported as `[[MISSING: …]]`
