# Email and SMS marketing

Status as at 2026-08-05.

**Email in the United States is opt-out. SMS is opt-in.** That asymmetry is the whole point of this file, and it is the opposite of the EU position where both require consent under Art 13 of Directive 2002/58/EC. A US company may lawfully send a first commercial email to a person who never asked for it; sending that same person a first marketing text without prior express written consent is a $500-to-$1,500-per-message exposure with a private right of action.

## Email — CAN-SPAM Act, 15 U.S.C. §§ 7701–7713; CAN-SPAM Rule, 16 CFR Part 316

No consent is required. Seven duties apply to every commercial email:

1. **No false or misleading header information** — the From, To, Reply-To and routing information must accurately identify the sender (§ 7704(a)(1)).
2. **No deceptive subject lines** — the subject must not mislead about the contents (§ 7704(a)(2)).
3. **Identify the message as an advertisement**, clearly and conspicuously, unless the recipient gave affirmative consent (§ 7704(a)(5)(A)(ii)).
4. **Include a valid physical postal address** (§ 7704(a)(5)(A)(iii)). A current street address, a post office box registered with the U.S. Postal Service, or a private mailbox registered with a commercial mail receiving agency all qualify. This is mandatory in **every** commercial message — it is the closest US analogue to an Impressum and the item most often missing.
5. **Tell recipients how to opt out**, clearly and conspicuously (§ 7704(a)(5)(A)(i)).
6. **Honour opt-outs promptly.** The opt-out mechanism must remain operable for at least **30 days** after the message is sent, and the request must be honoured within **10 business days** (§ 7704(a)(3)–(4)). No fee, no login, no information beyond an email address, and no navigating a preference centre requiring anything more than an email address and an opt-out choice may be required.
7. **Monitor what others do on your behalf.** Both the company whose product is promoted and the company that sends the message can be held liable (§ 7705).

Also prohibited: address harvesting, dictionary attacks, and open relay abuse (§ 7704(b)), which are the aggravated-violation provisions.

**Penalties.** Each separate email in violation is subject to a civil penalty; the FTC's compliance guide states up to **$53,088** per email. The FTC adjusts this figure annually for inflation and made **no adjustment for 2026** because of a gap in CPI data. Verify the current figure before quoting a number in client-facing text.

**Preemption.** CAN-SPAM preempts state statutes that regulate commercial email, **except** to the extent a state law prohibits falsity or deception in any portion of a commercial email or information attached to it (15 U.S.C. § 7707(b)(1)). Several states retain live anti-spam claims on that basis.

**Transactional messages** — order confirmations, shipping notices, account notices, warranty and recall information, and relationship-related messages — are not "commercial electronic mail messages" and are exempt from the advertising-identification, address and opt-out duties, provided the primary purpose really is transactional. Adding promotional content shifts the primary purpose analysis. 16 CFR § 316.3 sets out the primary-purpose test.

**Best practice beyond the statute.** Confirmed opt-in, suppression-list hygiene and one-click unsubscribe are not CAN-SPAM requirements, but they are enforced by mailbox providers and are the difference between a delivered list and a burnt domain. Do not present them to the user as legal obligations.

## SMS — TCPA, 47 U.S.C. § 227; FCC rules, 47 CFR § 64.1200

Text messages are "calls" for TCPA purposes. The statute carries a **private right of action with statutory damages of $500 per violation, trebled to $1,500 for wilful or knowing violations** (47 U.S.C. § 227(b)(3)), and is the most heavily litigated marketing statute in the country.

**Prior express written consent** is required for marketing texts sent using an automatic telephone dialing system or containing an artificial or prerecorded voice. 47 CFR § 64.1200(f)(9) defines it as a written agreement, bearing the signature of the person called, that clearly authorises the seller to deliver advertisements or telemarketing messages to the number the signatory designates. The agreement must disclose that consent is not a condition of purchase. In practice:

- A separate, unchecked checkbox at the point of collection, with the consent language visible on the same screen — not behind a link.
- The consent text must name the **specific seller**, describe the message type, and state that message and data rates apply and the expected frequency.
- Retain the consent record: timestamp, IP address, the exact wording displayed, the page URL, and the phone number. In litigation the record is the defence; without it there is none.

**"One-to-one consent" is dead.** *Insurance Marketing Coalition Ltd. v. FCC*, No. 24-10277 (11th Cir., 24 January 2025) **vacated** the part of the FCC's 2023 Second Report and Order that required consent to be given to no more than one identified seller at a time and that the subject matter be logically and topically related to the collecting site. The court held the FCC exceeded its authority: "the TCPA requires only 'prior express consent' — not 'prior express consent' *plus*." The standard reverted to the pre-2023 position. Do not build to the vacated rule and do not cite it as current — but equally, do not treat the vacatur as licence for lead-generation consent naming a hundred unidentified "marketing partners", which remains attackable on ordinary consent grounds. The **written**-consent requirement for marketing robotexts (47 CFR § 64.1200(a)(2)–(3), (f)(9)) was not touched.

**Quiet hours.** 47 CFR § 64.1200(c)(1) prohibits any "telephone solicitation" to a residential subscriber "before the hour of 8 a.m. or after 9 p.m. (local time at the called party's location)"; "telephone solicitation" is defined at § 64.1200(f)(15). A wave of class actions beginning in late 2024 applies this to marketing text messages, on the theory that prior consent does not waive the time restriction. The Ecommerce Innovation Alliance petitioned the FCC on 3 March 2025 for a declaratory ruling that consenting recipients cannot claim quiet-hours damages; the FCC sought comment on 11 March 2025. `[[UNVERIFIED: whether the FCC has ruled on the EIA petition by 2026-08-05]]` Until it is resolved, schedule marketing sends within 8 a.m.–9 p.m. **in the recipient's local time**, derived from something better than the area code where possible.

**Revocation — 47 CFR § 64.1200(a)(10).** A called party may revoke prior express consent, including prior express written consent, "by using any reasonable method to clearly express a desire not to receive further calls or text messages", and the revocation must be honoured "within a reasonable time not to exceed ten (10) business days from receipt". In force since **11 April 2025**. Standard opt-out keywords (STOP, QUIT, END, REVOKE, CANCEL, UNSUBSCRIBE) must work, and revocation communicated by other channels — a reply in words, an email, a phone call — counts.

One part of that rule is **waived until 31 January 2027**: the requirement to apply a revocation given in response to one type of message to *all* future robocalls and robotexts from the same sender on unrelated matters. The Consumer and Governmental Affairs Bureau extended the earlier waiver by Order **DA 26-12**, adopted and released 6 January 2026, while the FCC considers modifying or eliminating the cross-message duty in the 2025 TCPA FNPRM (FCC 25-76). So today: honour any reasonable revocation within 10 business days for the stream it relates to; cross-programme propagation is not yet compulsory. Build it anyway — the waiver may lapse, and the litigation risk of a narrow suppression is not worth the saving.

**Do Not Call.** Marketing calls, and in some readings texts, to numbers on the national registry require an exemption. Maintain an internal do-not-call list, honour it for five years, and scrub against the national registry.

## Template — SMS consent block

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<label>
  <input type="checkbox" name="sms_consent" value="1">
  I agree to receive recurring automated marketing text messages from
  [[SELLER LEGAL NAME]] at the mobile number provided. Consent is not a
  condition of any purchase. Message frequency varies — approximately
  [[NUMBER]] messages per [[PERIOD]]. Message and data rates may apply.
  Reply STOP to cancel or HELP for help. See our
  <a href="[[URL]]">Privacy Policy</a> and <a href="[[URL]]">SMS Terms</a>.
</label>
```

## Template — email footer block

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<p>
  You are receiving this message because [[REASON: e.g. you purchased from us
  / you signed up at example.com]].
</p>
<p>
  [[LEGAL ENTITY NAME]]<br>
  [[STREET ADDRESS OR REGISTERED PO BOX]]<br>
  [[CITY, STATE ZIP]], United States
</p>
<p><a href="[[UNSUBSCRIBE URL]]">Unsubscribe</a> from these emails.</p>
```

## Checkpoints

- [ ] Valid physical postal address present in every commercial email
- [ ] Opt-out link present, functional, and requiring nothing beyond an email address
- [ ] Opt-out mechanism operable for at least 30 days after send; requests processed within 10 business days
- [ ] Suppression list applied across every sending system and every ESP account
- [ ] Sender name, From address and subject line accurate and non-deceptive
- [ ] Promotional content in an otherwise transactional message assessed against the 16 CFR § 316.3 primary-purpose test
- [ ] Third-party senders and affiliates contractually bound and monitored
- [ ] SMS: separate unchecked checkbox, consent language on-screen, "consent is not a condition of purchase" present
- [ ] SMS consent records retained with timestamp, IP, wording and page URL
- [ ] STOP handling verified end to end, and revocations received by other channels routed to the same suppression list
- [ ] Sends scheduled within 8 a.m.–9 p.m. in the recipient's local time
- [ ] No reliance on the vacated FCC one-to-one consent rule, in either direction
- [ ] Internal do-not-call list maintained; national registry scrubbed if calls are made
