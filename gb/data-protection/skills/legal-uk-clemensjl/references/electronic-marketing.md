# Electronic marketing

Email, SMS and automated calls are governed by PECR 2003, not by the UK GDPR alone. The UK GDPR still supplies the lawful basis and the consent standard; PECR supplies the prohibition and now the penalty.

## Reg 22 PECR — electronic mail

Status as at 2026-08-05: reg 22 as amended by DUAA 2025 s 114, in force 5 February 2026.

Reg 22(2): a person must not transmit, or instigate the transmission of, unsolicited communications for the purposes of direct marketing by means of electronic mail unless the recipient has previously notified the sender that they consent for the time being to such communications.

"Electronic mail" covers email, SMS, MMS, picture and video messages, voicemail and in-app messages.

**The soft opt-in, reg 22(3).** Consent is not required where all of the following hold:

- the sender obtained the recipient's contact details in the course of a sale or negotiations for a sale of a product or service to that recipient
- the direct marketing is in respect of the sender's similar products and services only
- the recipient was given a simple means of refusing, free of charge except transmission costs, when the details were collected, and is given that means in every subsequent message

Bought lists, event-badge scans and website sign-ups without a sale are not "negotiations for a sale". "Similar" is read against what the recipient was actually buying or discussing.

**The charity soft opt-in, reg 22(3A)**, inserted by DUAA s 114 with effect from 5 February 2026. A charity may send electronic mail direct marketing where:

- the sole purpose of the marketing is to further one or more of the charity's charitable purposes
- the sender obtained the contact details from the recipient in the course of the recipient expressing an interest in, or offering or providing support for, furthering those purposes
- the same simple, free means of refusing was given at collection and is given in every message

Reg 22(5) defines "charity" by reference to the charity legislation of England and Wales, Scotland and Northern Ireland.

Two limits that get missed: the exception applies only to contact details obtained on or after 5 February 2026 — it cannot be applied retrospectively to an existing supporter list — and it may not be used to promote other organisations, including other charities.

## Reg 23 PECR — sender identification

A person must not transmit, or instigate the transmission of, a communication for direct marketing by electronic mail where the identity of the sender has been disguised or concealed, or where a valid address to which the recipient may send an opt-out request has not been provided. Every message needs an identifiable sender and a working opt-out route.

## Regs 19–21 PECR — calls and faxes

Reg 19 covers automated calling systems: prior consent is always required, with no soft opt-in. Reg 21 covers live marketing calls: no calls to a subscriber who has objected or who is registered with the Telephone Preference Service, unless that subscriber has notified the caller that they do not object.

## Penalties

DUAA s 115 and Sch 13 replaced PECR Schedule 1 on 5 February 2026, applying DPA 2018 Parts 5–7. Reg 22 breaches attract the higher maximum under DPA 2018 s 157: £17.5 million or 4% of total annual worldwide turnover, whichever is higher. Historically the ICO issues more fines under PECR marketing rules than under data protection law; the exposure is now thirty-five times the old £500,000 cap.

## Advertising identification — CAP Code

The UK Code of Non-broadcast Advertising and Direct & Promotional Marketing (CAP Code), enforced by the ASA, section 2:

- rule 2.1: marketing communications must be obviously identifiable as such
- rule 2.2: unsolicited email marketing communications must be obviously identifiable as marketing communications without the need to open them
- rule 2.3: marketing communications must not falsely claim or imply that the marketer is acting as a consumer or for purposes outside its trade, business, craft or profession; marketing communications must make clear their commercial intent, if that is not apparent from the context
- rule 2.4: marketers and publishers must make clear that advertorials are marketing communications, for example by heading them "advertisement feature"

Influencer and affiliate content sits under these rules. The ASA expects a prominent, upfront label such as "Ad" or "Advertisement" — not a hashtag buried in a caption, not "sp", "spon", "collab", "gifted" alone, and not disclosure only in a bio. The same conduct is separately actionable as a misleading action or a banned practice under the DMCC Act 2024 (see `dmcc-trading.md`), which is why the ASA's influencer guidance is now framed on Chapter 1 of Part 4 of that Act rather than on the revoked CPUT 2008.

## Template

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h2>Newsletter sign-up</h2>
<form>
  <label for="email">Email address</label>
  <input id="email" type="email" required>

  <label>
    <input type="checkbox" name="marketing" value="yes">
    Yes, email me [[what you will actually send: e.g. product updates and offers, roughly monthly]].
    You can unsubscribe at any time using the link in every email.
  </label>

  <p>
    We will use your address only to send what you have asked for. We do not share it with anyone else
    for their own marketing. How we handle your data: <a href="[[url]]">Privacy notice</a>.
  </p>

  <button type="submit">Subscribe</button>
</form>
```

Email footer block:

```text
[[Registered name]], [[registered office address]].
Registered in [[part of the UK]], company number [[number]].
You are receiving this because [[you subscribed on [[date]] / you bought [[product]] from us on [[date]]]].
Unsubscribe: [[one-click link]]
```

## Checkpoints

- [ ] Marketing consent is a separate, unticked checkbox, never bundled with terms acceptance
- [ ] Consent wording names what will be sent and how often
- [ ] Consent evidence stored: timestamp, source, IP or equivalent, and the exact wording shown
- [ ] Where the soft opt-in is relied on: a sale or negotiation actually occurred, the products are similar, and the refusal option was offered at collection (reg 22(3))
- [ ] Charity soft opt-in only used for details obtained on or after 5 February 2026, and only for the charity's own purposes (reg 22(3A))
- [ ] Unsubscribe link in every message, working, one action, no login required (reg 23)
- [ ] Sender identity not concealed; valid reply address present (reg 23)
- [ ] Automated calls have prior consent (reg 19); live calls screened against the TPS (reg 21)
- [ ] Sender's registered details in the email footer (reg 25 SI 2015/17 applies to business communications)
- [ ] Influencer and affiliate posts labelled "Ad" upfront (CAP Code rules 2.1, 2.3, 2.4)
- [ ] Suppression list applied before every send, including unsubscribes from every channel
- [ ] No reliance on "legitimate interests" as a substitute for the PECR consent requirement
