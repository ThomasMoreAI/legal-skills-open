---
claim_type: mechanic
source: "internal synthesis"
checked: 2026-09-14
---

# Lawful basis and collection: what has to be true before the first message

The unit here is **the basis record**: one person, one channel, one purpose, with what the permission rests
on, where it came from, the wording version, the proof and the lifetime. This file settles how a record
comes to exist, what it holds, and when it ends. What the person chooses afterward is
`preference-center-and-unsubscribe.md`; the uses of the data other than sending are
`processing-beyond-sending.md`.

## Entry conditions

Contacts enter the base through at least one point, and the program intends to send marketing to some of
them. The country of the person is known, can be inferred from the point, or is recorded as unknown. A
point that cannot say what it told the person is still a point; it is one the mechanic will find.

## Exit conditions

A registry of every point through which a contact enters, with the basis type each point produces per
channel and the handover state it writes. A wording version for every request in use, archived with its
dates. For every person, channel and purpose the program sends on, a basis record with its fields filled.
A decision per point on confirmed opt in. An expiry event or a review date on every record whose regime
gives it one. A refresh route that goes only where a message is still allowed. A test path from every
point to the record.

## Steps

**1. Inventory every way a contact enters.** Web forms and pop-ups, the checkout, account creation, the
app's sign-up, the in-store enrollment where staff keys the data, the kiosk, the phone script, the chat,
the event badge scan, the business card, the referral, the import from a previous platform, the partner
list, the acquired base, the sales rep's own address book. `onsite-capture` owns the on-site points and
their display rule; this inventory covers the whole base, because the points outside the site are where
records go missing. For each point write what the person sees or hears, what they do (tick, submit, say
yes, hand over a card, do nothing), what the point records, and the handover state it writes in
`onsite-capture`'s four values: requested message, marketing, pending, suppressed. A point that writes
"marketing" with no wording behind it is a finding, not an entry.

**2. Ask the ten questions for each point, and get a basis type.** Country; recipient type (a person or an
organization); channel; purpose of the message (marketing, transaction, service); source of the contact
(the person gave it to you, somebody else did, it was bought or found); the basis; the exception and all
of its conditions; the term; the withdrawal; the proof. The answers name one of four basis types per
channel:

- **express consent**: the person agreed, in a request written for it (the consent regimes, and every
  regime where the source is not the person);
- **an exception**: the regime allows sending without consent when every condition holds, and the
  conditions are events and facts you can record: contact details obtained by you in the course of a sale
  or negotiations, marketing of your similar products only, a refusal offered at collection and in every
  message (EU Article 13(2), UK regulation 22(3)); a purchase, lease or written contract within two
  years, or an inquiry within six months (Canada, section 10(10)). One condition missing and the
  exception does not exist, whatever the spirit;
- **an opt-out regime**: no prior permission, an honored opt-out and the message requirements (US
  commercial email);
- **requested message only**: the person asked for one named message and nothing beyond it (a stock
  alert, an order confirmation, a reply in chat). It is a basis for that message and for nothing else,
  and it is what `onsite-capture` hands over as the requested message state and `chat-and-bots` as the
  address taken in conversation.

A point produces at most one basis type per channel, and the type is written in the registry next to
the point. Where the country is unknown, the record says so and the program treats the person as if
express consent were required until a country is known; the library grants no permission on a guess.
For a texting channel in the United States the type is express written consent under the FCC's rule
for calls and texts made with an automatic telephone dialing system or a prerecorded voice, a separate
agreement naming the number; whether your sending setup falls under that definition is a question for
counsel, and email consent does not carry over to texts in any reading. In the United Kingdom
"electronic mail" includes texts, so the same basis rule applies to both; in the EU, the member state's
text decides.

**3. Write the request, and version it.** The wording is part of the basis: it fixes who is asking, what
for, in which channels, what kind of messages, how often, and how to withdraw. Contents by regime, all of
them in the request and none of them in a linked policy alone:

- the sender, and every other brand or company that will rely on this permission by name (the ICO: a
  category of third parties "will not be specific enough"; Canada: the person on whose behalf consent is
  sought);
- the purposes, one box per purpose where the regime wants separate consent (Recital 43), and the
  channels, one per channel where the rules differ (email and texts have different bases in the United
  States);
- the kind of message and the promised frequency. A promise of frequency binds like a purpose:
  `contact-orchestration` reads it as part of the basis, and sending more often than promised needs a new
  request or the person's own instruction;
- that the person can withdraw at any time, and how;
- for an exception, the refusal offered "at the time that the details were initially collected"
  (regulation 22(3)(c)): a prominent unticked box next to the field, not a line in the privacy policy,
  and not the order confirmation email.

The box is unticked (Recital 32; the CRTC on pre-checked boxes). The marketing request is separate from the
terms of the purchase and from the account terms (Article 7(2)); completing the purchase does not depend
on it (Article 7(4)). An incentive for subscribing, a discount or points, is stated in the request, and
the purchase stays possible without it; whether the incentive leaves consent freely given in your regime
is a question for counsel, and `loyalty-program-launch` carries the disclosure of the incentive on its
side. In a store, the person reads the wording themselves or hears it from a script with a version
number; a code sent to the number or the address confirms both that the address is theirs and that the
wording reached them. A form inside an email, a chat or an app carries the same wording as the web form
of the same version; `email-design` places it, this step writes it.

Every change of wording makes a new version with a start date, and the previous version stays archived
with its end date. The record stores the version, not the text; the archive is what a trace opens.

**4. Decide the proof per point, and whether to require confirmed opt in.** The record holds, per
person, channel and purpose: who (the identifier), when (a timestamp), through which point, which
wording version, how (a ticked box submitted, a code entered, a signature, a note of the call), on what
the permission rests (the basis type), and, for an exception, the event it rests on with its date (the
purchase, the inquiry) and the fact that the refusal was offered. The source of the contact (the person,
somebody else, bought or found) is a field of the record; `list-building`'s provenance, the intake
point, the date of the event that created the basis and what the person was told, is stamped on the row
at arrival, and the record points at the same three values rather than holding a second copy. The point
stores what the person saw; this record points at the version and the point. A ticked box on its own is
not a record, and neither is a flag on the platform.

Confirmed opt in is a second step in which the person acts on the address they gave. None of the regimes
opened here requires it; it answers the tenth question, the proof, and specifically that the address
belongs to the person who agreed. Require it where the point cannot establish that by any other means:
an open web form, a pop-up, a form filled in by staff, a phone call; do not require it where the address
was already proven by a code or a sign-in in the same session, or where the person is paying with it
and the message is the one they asked for. The confirmation message carries the confirmation and nothing
else: no offer, no second request. In Canada, a message asking for consent is itself a commercial electronic
message; a confirmation message rests on the person's own request a moment earlier, which is an inquiry
under section 10(10)(e), so keep it to the confirmation and let counsel say whether your wording is a
request for consent. Until the person confirms, the row is pending and gets no marketing. One reminder
inside the confirmation window, then the row stays pending; a pending row is deleted when the window
has passed and no other purpose holds the data (an order does), because storage is limited to the
purpose (Article 5(1)(e)). The step itself, the message and the pending state, is built by
`onsite-capture` and `list-building`; this step decides where it applies.

**5. Give every record a lifetime.** Three kinds, and the record says which:

- **until withdrawn, or until your own review date passes with no refresh**: express consent in Canada
  ("express consent is not time-limited"), consent in the UK ("for the time being"), and consent under
  the GDPR, which sets no term. The record carries a review date from your refresh policy (step 6), and
  the end at that date is a policy of yours, not a term of the law: the law ends this record only by
  withdrawal;
- **until an event-based term ends**: the Canadian existing business relationship, two years from the
  last purchase, lease or written contract, six months from the last inquiry. The record carries
  `expires_on`, computed from the latest qualifying event, and each new qualifying event moves it. A
  timer, not a person, reads it: on the day it passes the record ends and the person leaves every
  marketing selection in that channel, whatever their engagement. The timer reads events by their own
  date, not by the day they arrived: a purchase logged late recomputes the date from the purchase, and a
  purchase reversed later leaves the qualifying events (the edge cases say how);
- **while the exception's conditions hold**: the EU and UK customer exceptions have no term in the
  text; they end when a condition stops holding, when the marketing is no longer about similar products
  or the person refuses.

This is the answer to the question the library left open: the basis itself can end, and the record's
timer tells an ended basis from a silent person. A silent person on a live basis is `lapse-and-winback`'s
object; a person whose basis ended is nobody's to write to, however engaged they looked last month.
`welcome-and-activation` sets the lifetime of its series from the entry event for the same reason.

**6. Refresh or re-ask, only where a message is still allowed.** A refresh request is a request in the
sense of step 3, sent to people whose record is near its review date or its expiry, before the date and
never after it, or whose wording version predates a change of purpose. After the date the record has
ended, and the refresh is itself the unsupported send of the failure modes. It goes out only where the
current record still supports a message today: inside the live Canadian term, on a live consent, under a
live exception. To a person with no live basis it is marketing on no basis, in Canada by the CRTC's
words, and in the EU and UK a question for counsel that this library answers by not sending. The request
is one message, not a series, and it carries no offer beyond the request itself. Silence is not a
withdrawal: the person is not suppressed, the record ends on its own date, and the person can come back
through any point. A "no" is an instruction and goes to `preference-center-and-unsubscribe.md`. Your
refresh interval for consent with no statutory term is a policy: the ICO's "consider refreshing consent
every two years" is a starting point for the UK and a recommendation, not a limit; set yours by how
often you are in contact and record it once.

**7. A change of purpose, channel, brand or owner is a new request.** A new channel, a new brand under
the same roof, a partner who will send under their own name, a purpose the wording did not name: none
of these is covered by an old record, and a new request goes only where a message is allowed now
(step 6). An address obtained from somebody other than the person gets a record whose source says so and
a first message that states where the address came from (GDPR Article 14(3)(b) for the notice;
`b2b-lifecycle` writes that first message). The notice is a duty, not a basis, and the basis follows the
source, not the handover: a conspicuously published address, or one the person disclosed themselves, a
card handed over at an event, carries Canada's implied basis while the message is relevant to the
person's role (section 10(9)(b) and (c)); a colleague named by a champion disclosed nothing, carries no
implied basis there, and gets one message under the referral of the edge cases or waits for express
consent; in the EU and the UK the recipient type and the member state's text decide, and `b2b-lifecycle`
says the same from its side. A bought or scraped list has no basis in any regime opened here: the ICO's
"no such thing as a third-party marketing list that is compliant with the soft opt-in", and CAN-SPAM's
bar on transferring the addresses of people who opted out. An acquired base comes with its records or
it comes as a list with no basis; the CRTC's advice to a purchaser is to obtain the consent records, and
that is the test here too.

**8. Test the path from point to record like a send.** Run a test contact through every point in every
regime you serve: submit the form, complete the checkout with the box ticked and with it unticked, enroll
at the till, import a file of one row, let a sales rep add a contact. Open the record and check every
field of step 4, and the expiry or review date of step 5. A point that produces a flag with an empty
version field, or a "marketing" state from an unticked box, is defective, and the control metric will
read its sends as unsupported. Repeat the test when a form, a platform or an integration changes, and on
a period of your own: the capture point sits on `program-audit-and-ops`'s monitoring roster with
"contacts accepted" as its heartbeat, and that heartbeat does not see an empty version field, so the
path test runs beside it and is not replaced by it.

## Thresholds and timings

| Quantity | Where it comes from | Class |
|---|---|---|
| Canada: implied basis lasts two years from a purchase, lease or written contract, six months from an inquiry | statute, CASL section 10(10), opened 2026-09-14 | legal |
| Canada: express consent has no term; records kept for as long as you contact the person | CRTC guidance and FAQ, opened 2026-09-14 | legal |
| UK: consent "for the time being"; refresh interval "consider ... every two years" | PECR regulation 22(2) and ICO consent guidance, opened 2026-09-14; the interval is a recommendation | legal, as guidance |
| EU: age of consent for information society services 16, member states may set 13 to 16; UK 13 | GDPR Article 8(1); UK GDPR Article 8(1), opened 2026-09-14 | legal |
| US: a child is under 13 | 16 CFR 312.2, opened 2026-09-14 | legal |
| Confirmation window before a row stops waiting | your own distribution of time from submission to confirmation, by point; take the point where the tail flattens | parameter |
| Reminders to confirm | one, inside the window, as a starting point; none where the point already proved the address; revise when the reminder's own completion share reads as noise in your data | starting heuristic |
| Retention of a pending row | the confirmation window plus the time your review of pending rows takes; longer only where another purpose holds the data | parameter |
| Review date on consent with no statutory term | your refresh policy, set from how often you are in contact with the person | parameter |

The legal rows carry their sources and the people they do not bind in `SKILL.md`. The rest are yours.

## Edge cases

- **Guest checkout.** The address belongs to the transaction: service messages go there
  (`transactional-messaging`), and the record is requested message only. Marketing needs its own request, an
  unticked box next to the address with the wording of step 3, or the customer exception where the regime
  has one and every condition of it is met and recorded.
- **The person unticks the box on a later form.** That is not a second record; it is an instruction, a
  withdrawal for the scope the box named, and it goes to `preference-center-and-unsubscribe.md`. Do not
  write to them to ask whether they meant it.
- **An address already in the base with a live record submits a new form.** No second confirmation. Write
  a second record with the new wording version and point; the older one stays. When the two differ in
  scope, the permission is the narrower and the instruction, if any, is the wider.
- **Two records for one person after a merge.** `list-building` merges the rows and does not move a
  permission between them. Here: each record keeps its own channel, purpose and lifetime; a withdrawal
  taken on either address after the merge applies to the person, because the wording said "stop writing
  to me", not "to this address".
- **A group of brands.** Consent names the brands that rely on it (step 3). A record for brand A is no
  basis for brand B, and "the absence of a prohibition is not a permission" (`email-program`). One request
  can name several brands; then the record says so and a withdrawal that names the group reaches all of
  them.
- **The same person in two countries.** The regime follows the person's location and your knowledge of
  it, and it can change; the record holds the country with the date it was set. Where two regimes could
  apply and you cannot tell, apply the one that requires more.
- **In-store enrollment keyed by staff.** The person did not see a screen. The wording reaches them by a
  card they read, a screen turned toward them, or a script read aloud with a version number, and a code to
  their number or address proves both the address and that the wording arrived. A form filled in by staff
  with no code is a pending row. The age of the person at the till is asked before the record is written
  (`processing-beyond-sending.md`, step 4).
- **Consent by phone.** The script version and a note made at the time are the record (the ICO on oral
  consent). The call recording, where you keep one, is proof and a record of its own with a retention line.
- **A referral.** In Canada the first message may go to the referred person without consent when the
  referrer has an existing business, non-business, family or personal relationship with you and one of
  those with the person, the message discloses the referrer's full name, and it states that it follows
  a referral (Electronic Commerce Protection Regulations, section 4(1)); the record says "referral" as
  its source with the referrer's name, and the second message needs a basis of its own.
- **A B2B contact.** A corporate subscriber in the UK needs neither consent nor a soft opt-in for email;
  an individual subscriber does. In Canada a published or disclosed address gives an implied basis while
  the message is relevant to the person's role. In the EU the member state decides for legal persons. The
  record holds the recipient type as a field, because it changes the basis (`b2b-lifecycle` keeps the
  field on the contact).
- **A bot took the address.** Disclosure that the person is talking to a bot is not consent to anything
  (`chat-and-bots`); the address taken in the conversation is requested message only.
- **An imported historical base with no records.** Under a consent regime, no basis: the people are not
  sent marketing until a request reaches them through a point where a message is allowed, which for most
  of them means none. Under the Canadian rules, an existing business relationship from the last purchase
  date where you have it, with `expires_on` computed from it. Under the US email rule, the opt-out
  honored and the message requirements met. The import goes through step 8 before anything is sent.
- **A purchase reversed after it moved the timer.** An order canceled before delivery or refunded in
  full stops being a purchase for the timer: it leaves the qualifying events, and `expires_on` is
  recomputed from what remains, with that order kept as an inquiry from its own date (section 10(10)(e),
  six months), which is the reading that requires more; whether it could still count as a purchase is a
  question for counsel. A partial return leaves the purchase in place. The reversal shortens the record
  and never lengthens it, and a record already ended does not come back on a reversal. A late event
  recomputes the date from the event's own date and does not rewrite the reading of a period already
  read: the control metric reads the record as it stood at the send.
- **A person under the age your regime sets.** No record for marketing is written; the age gate and what
  the program may hold about a child are in `processing-beyond-sending.md`, step 4.

## Failure modes

**The flag without the record.** Signs: the trace sample cannot produce records for sends from one point
or one import; every contact from a date shows the same timestamp; the version field is empty; the
platform shows "subscribed" for people whose only event is an order. Remedy: step 4 for the fields,
step 8 for the path, and the import re-run through the same path as a form.

**The bundled request.** Signs: the opt-in share at a point sits near everyone, complaints and spam reports
concentrate among people from that point, and the wording in the archive is a line inside the terms or
a pre-ticked box. The counter-sign that tells it from a good point: a checkout with a separate unticked
box can also read high, and the difference is the wording, not the rate. Remedy: step 3, a new version,
and the records from the old version marked as resting on that version so a trace shows it.

**The ended basis that kept sending.** Signs: complaints from Canadian addresses whose last purchase is
older than two years; no `expires_on` field on records with an event-based basis; the timer of step 5
does not exist or does not remove people from selections. Remedy: step 5, and a one-time pass that
computes the date for every existing record.

**Confirmation that silently eats the volume.** Signs: the confirmation completion share falls after a
template change, a platform migration or a deliverability incident on the identity that sends the
confirmation; pending rows grow; the base looks like it stopped growing while the forms did not. Remedy:
read completion and pending age beside the metric. The confirmation message is this skill's: service
in `contact-orchestration`'s class, because it is the consequence of the person's own action, sent from
the service identity (`deliverability`), with a deadline you set here; `transactional-messaging` keeps
no row for it and says so.

**The refresh that is itself unsupported.** Signs: a re-permission campaign went to the whole base,
including records with no live basis; complaints from people who had no relationship; in Canada, a
request sent past the term. Remedy: step 6, the audience of a refresh is the set of live records near
their date, and nothing else.
