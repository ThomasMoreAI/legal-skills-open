---
claim_type: mechanic
source: "internal synthesis"
checked: 2026-09-14
---

# The preference center and the unsubscribe: what the person chose, how far it reaches, how fast it holds

The unit here is **the instruction**: one recorded choice by the person after the basis exists, about one
scope: a message type on or off, a frequency, a channel, a pause with an end date, or a withdrawal. Each
instruction has a route it was taken through, a scope it reaches, and a deadline by which every sending
system has to honor it. Which basis made the first message lawful is `lawful-basis-and-collection.md`;
applying the resulting suppression to an audience is `email-program`'s step; reading the frequency as a
cap is `contact-orchestration`'s.

## Entry conditions

Basis records exist, and at least one marketing stream sends. Every system that sends can read one
person-level field, or receive a write, within the deadline that applies. Without that, the mechanic can
record instructions and cannot honor them, and that gap is `martech-stack`'s to close before this file is
used.

## Exit conditions

The axes of choice the preference center offers, each mapped to a real stream. The routes an instruction
can be taken through, all writing the same instruction object. A scope for every route and wording. The
unsubscribe page and its order of elements. A propagation deadline per regime and platform, the shortest
applicable, and a honoring log per system. The rule for service rows and the point where their exemption
is lost. The frequency and pause instructions in a form `contact-orchestration` reads. The reading of
instructions per period.

## Steps

**1. Define what the person can choose, and map every choice to a stream.** Four axes:

- **message type**, named in the person's words, not the program's: "sales and offers", "new arrivals",
  "the weekly digest", "surveys and feedback requests" (`voice-of-customer` reads the "no surveys" choice
  here), "reminders about my points";
- **channel**: email, texts, push, messaging apps, each on or off, and push by category where the app
  has categories (`push-notifications`);
- **frequency**: a ceiling the person sets from options you offer, "at most once a week", "once a month",
  built from your own cadence so that each option corresponds to something the program can do;
- **pause**: silence for a term the person picks, with an end date and an automatic resume into the
  normal cadence.

And, at all times and on every page, **stop everything**: the withdrawal of all marketing from this
sender in this channel, in one action. The US rule allows a menu and requires the option to stop all; the
Canadian mechanism covers "any commercial electronic messages, or any specified class". Each type and
channel on offer corresponds to a stream that exists, and each stream that sends is covered by a type; a
type nobody sends is a lie, and a stream no type covers is one the person cannot switch off. Service rows
and mandatory notices are listed and marked as continuing, so the person knows the order updates will keep
coming, and they are not switchable here; a service row that carries promotion has left that list (step
6). One thing the person can set about a service row: the channel it is delivered in, where more than
one can carry it. That is a routing preference, not a switch; `transactional-messaging` reads it as the
row's default channel and fails over past it on a fact, and `push-notifications` keeps service and
marketing in separate categories so that switching one off does not switch off the other.

**2. Take the instruction through every route, and let every route write the same object.** The routes:

- the link in every marketing message to a page where the withdrawal completes in one action; the US
  rule allows no step beyond "sending a reply email or visiting a single page", no fee and no information
  beyond the email address; the Canadian mechanism uses "the same electronic means by which the message
  was sent" or, where not practicable, another electronic means; the CRTC's example of a path through a
  login and a "delete account" page is the path not to build;
- the reply: an email reply that says stop; for texts, the words the FCC lists ("stop," "quit," "end,"
  "revoke," "opt out," "cancel," "unsubscribe") as revocation per se, and any other words a reasonable
  person would read as a request to stop, treated the same;
- the account settings and the preference center reached from them;
- the mailbox provider's one-click, from the header `deliverability` owns; here, what it maps to: the
  widest scope for that channel, the sender as a whole;
- a person: support, a letter, a call, a message on a social account, the sales rep. The GDPR makes
  withdrawal "as easy ... as to give", and the ICO says to publicize the phone route too; under the
  FCC's rule a revocation by other means creates a rebuttable presumption. The person who receives it
  writes the instruction with the route "human", and the deadline runs from receipt;
- a spam complaint returned by a mailbox provider's feedback loop: `deliverability` reads it for the
  identity; here it is an instruction of the widest scope for that channel, written the day it arrives;
- a browser signal about sale and sharing (the GPC): an instruction with the scope "sale and sharing",
  not an email withdrawal, read in `processing-beyond-sending.md`, step 7.

Every route writes one instruction object: person, route, scope, timestamp, the wording the person saw
or said. A route that writes to a store of its own, the text provider's own opt-out list, the sales
tool's "do not email" box, is a propagation gap until it is copied into the person-level store; the
honoring log of step 5 is where it shows.

**3. Set the scope of each instruction from the wording it was taken under.** The scope values are
`email-program`'s five, the address or channel, the sender as a whole, one brand, one message type, one
program, plus one from `b2b-lifecycle`: the account. The scope is not chosen by the platform's list
structure; it is read from what the person was offered and what they answered:

- a one-click header, a reply "stop", a "stop everything" button: the sender as a whole, in that
  channel (`email-program`'s global scope). The sender is the identity the message went out under: the
  From identity the header names, the code or number the text came from. A brand that sends under its
  own identity is the sender; brands that share one identity are all the sender, whatever the platform's
  lists say;
- a type checkbox: that type, across the brand that holds the preference;
- a brand's own unsubscribe, where brands are separate senders holding separate permissions: that brand;
  a wording that names the group: every brand in it;
- a "stop" in reply to a text on a code that serves several programs: every text that rests on consent
  under the FCC's rule, marketing and service alike where the service texts rest on the consent of
  paragraph (a)(1), unless the person keeps some of them by answering the one confirmation text the rule
  allows (step 6);
- a request from a role with authority to speak for an organization, "do not write to anyone at X": the
  account, which suppresses the program's touches to every contact of that account; one contact's
  unsubscribe stays that contact's and does not suppress the account (`b2b-lifecycle`).

Ambiguous wording gets the wider reading. Scopes remove people; none of them widens a permission, and a
preference center that lets a person "subscribe" to a type they had no basis for is writing a basis
record, which needs the request of `lawful-basis-and-collection.md`, step 3, not a checkbox.

**4. Build the unsubscribe page in this order.** First the withdrawal completes: one click from the
message, no login, no reason required, no delay announced. Then the confirmation, on the page: what was
stopped, for which address, and that service messages continue. Then, after the fact and optional, the
alternatives: a type, a frequency, a channel, a pause. Then a way back: a link that starts a new request
(step 8). Then, optional, a reason as choices, one click each, with a free text field nobody has to fill.
No promotion on the page: an offer to stay is a step between the person and the route out, and the US
rule allows none. A forwarded message carries the original recipient's token, so the page names the
address it will affect before it acts, and the person who is not that address sees whose withdrawal they
are about to make. No confirmation email after an email withdrawal: the page confirmed, and a message
after a withdrawal is a send to read against the metric. For texts, the one-time confirmation text within
five minutes, confirming and nothing else, is allowed by the FCC's rule and is the one exception.

**5. Propagate inside the shortest applicable window, and log every system's write.** The instruction is
written to the person-level store first. From there it reaches every system that sends under the
company's name: the email platform, the text provider, push, messaging apps, the CRM's sequences, the
call list, the audience exports. The deadline is the shortest of the windows that apply to that channel
and that base: ten business days under the US email rule, the Canadian rule and the FCC's rule; two days
under Yahoo's requirement for mail to its users; "promptly" under the ICO; "as easy as to give" under
the GDPR. Where no window that applies to a channel is a number, set one of your own for that channel,
no longer than the shortest number that applies to any channel of yours, and record it once: the control
metric reads sends after an instruction against this deadline. Where any Yahoo address is in the base,
two days is the ceiling for email, and refreshing the suppression list faster than that is the practice,
because the law's window and the platform's are both in force and the platform enforces by filtering. A
withdrawal cancels marketing steps already queued for the person: flow steps scheduled for later, a
campaign segmented but not sent. A message in flight at the moment of the instruction cannot be
recalled; it is the cost of the lag, and the deadline is measured to the last system's write. The
honoring log holds, per instruction and per system, the time of the write; the maximum across systems is
the lag, and a system with no write by the deadline is the broken link.

**6. Leave service rows alone, and take them out of "always on" when they stop being service.** A
withdrawal does not stop service messages, the confirmation of an order, the code, the delay notice, nor
the mandatory notices of `contact-orchestration`'s class, a recall, a change of terms. The US email rule
exempts transactional and relationship messages from most of its provisions; the ICO says routine
customer service is not direct marketing; in Canada the service message is exempt from the consent
requirement and still carries an unsubscribe mechanism. What the person's unsubscribe from a Canadian
service message does is a question for counsel. Texts in the United States are the exception written in
the rule itself: a "stop" revokes consent for every text that rests on it under the FCC's rule, and a
service text sent with an automatic telephone dialing system to a wireless number rests on the prior
express consent of paragraph (a)(1). So on a code that carries both, the one confirmation text asks
which texts the person meant; an answer that keeps the service texts is written as the scope; silence
stops every text for which consent is required, and a required service row then goes by
`transactional-messaging`'s next channel. Whether your service texts fall under the federal definition
is the question for counsel named in `SKILL.md`; until it is answered, the program reads them as if they
did. The exemption is lost by content, in each regime by its own test (`transactional-messaging`, class
check at the template version and at the send). From the version that carried promotion, the row is a
marketing send for this skill: the instruction applies to it, and it leaves the "continuing" list of
step 1. The sign that this went wrong: a promotional block switched on by the recipient's consent flag
without a change of class, so the message goes out from the service identity, with no unsubscribe, to
people who withdrew.

**7. Write the frequency and the pause as instructions `contact-orchestration` can read.** "Less often"
is written as a value from the options of step 1; the cap reads it and lets it win when it is lower and
not when it is higher. A pause is written with its end date; during it, marketing to the person is
suppressed, not deferred, so the resume is into the normal cadence and not into the backlog. The resume
needs no new request: the basis persisted through the pause. If the basis ends during the pause, the
record ends on its own date, and nothing resumes. No message goes out to announce the end of a pause.

**8. Re-subscribe only through a request.** A person who withdrew comes back through a new request in
the sense of `lawful-basis-and-collection.md`, step 3, from any point, with a new record. A person who
asks support to put them back gives express consent by that request; the ticket is the record, with who,
when, how and what was said. Nobody is re-subscribed on the program's initiative, and a withdrawn person
is not written to with an offer to return (`lapse-and-winback` states the same from its side: refused
means no repeat attempt).

**9. Read the instructions each period.** Instructions by route and by scope; the kept share, instructions
that chose a type, a frequency, a channel or a pause instead of the withdrawal; the honoring lag per
system against the deadline; sends after an instruction, by system; complaints arriving as instructions.
A route with no instructions in a period is a route that does not work, not a happy base: test it with a
withdrawal of your own.

## Thresholds and timings

| Quantity | Where it comes from | Class |
|---|---|---|
| US email: honor an opt-out within 10 business days; the mechanism works for at least 30 days after the send; no fee, no information beyond the address, no step beyond a reply or a single page | FTC compliance guide, opened 2026-09-14 | legal |
| US texts: honor a revocation within ten business days; a one-time confirmation text within five minutes, with no marketing, is presumed to fall within consent | 47 CFR 64.1200(a)(10) and (a)(12), opened 2026-09-14 | legal |
| Canada: effect given without delay and no later than 10 business days; the address or page valid for at least 60 days after the send; no further action by the person | CASL section 11(2) and (3), opened 2026-09-14 | legal |
| Yahoo: honor unsubscribes within 2 days | Yahoo sender best practices, opened 2026-09-14; a platform rule | platform |
| UK and EU: "promptly"; "as easy to withdraw as to give" | ICO PECR guidance; GDPR Article 7(3), opened 2026-09-14 | legal |
| Options for frequency | your own cadence: the intervals the program can keep | parameter |
| Length of a pause | the person's choice from options you offer; offer terms shorter than the lifetime of your shortest event-based basis, so a pause does not outlive the record | parameter |
| Reason choices on the page | yours, one click each, optional | parameter |

The legal rows carry their sources and the people they do not bind in `SKILL.md`; the platform row binds
mail to that provider's users and nobody else. The rest are yours.

## Edge cases

- **The withdrawal arrives on paper, by phone or in a chat.** The person who receives it writes the
  instruction with route "human" and the time of receipt; the deadline runs from then, not from the
  moment somebody found the note.
- **An unsubscribe from one address of a merged person.** The scope is the person, not the address, when
  the wording said "stop writing to me"; the second address is suppressed with the first. A type
  preference set on one address is a preference of the person as well.
- **A spam complaint from a mailbox provider.** An instruction of the widest scope for that channel, the
  day it arrives, whatever the program thinks the person meant.
- **A withdrawal while a campaign is in flight.** The send that already left counts as the cost of the
  lag; the send scheduled for tomorrow is canceled. Read the two apart in the honoring log.
- **STOP on a short code that serves several programs.** Every text that rests on consent stops, the
  service texts on that code included where they rest on the consent of paragraph (a)(1); the one
  confirmation text may ask which, an answer that keeps some is the scope, and silence keeps them all
  stopped, with the required service rows moved to another channel (step 6).
- **A one-time code the person asks for after STOP.** The stop entry stays. The request is a requested
  message for that one code, sent at once and carrying nothing but the code; log the request and its
  time beside the stop entry. The FCC texts, the conditions and where counsel decides are in `SKILL.md`,
  the legal regime.
- **A one-click from a service message.** The header belongs on marketing and subscribed messages; a
  service message does not need it (`deliverability`). Where a service message carries one, the click
  is a withdrawal of the sender's marketing in that channel, and the service row continues.
- **A person whose basis ends during a pause.** No resume; the record ended. The person can come back
  through a point.
- **The preference center reached by somebody who is not the person.** The center changes preferences
  and withdraws; it does not show the person's data beyond the address or number it will act on, so a
  forwarded link cannot be used to read a profile.
- **A group of brands with one center.** Each brand's types are listed under the brand; "stop
  everything" names its scope on the button: this brand, or all brands of the group, as the request of
  `lawful-basis-and-collection.md`, step 3, named them. A one-click or a reply "stop" from a message
  of one brand reaches the identity that message went out under (step 3), and a shared center does not
  widen it to the group on its own.
- **A parent's instruction about a child's data.** Written as the parent's, with the scope of the child's
  record, and read in `processing-beyond-sending.md`, step 4.
- **An instruction from a role with authority in an organization.** Account scope; the record names the
  role and the date; `b2b-lifecycle` suppresses the program's touches and lets the account executive's
  correspondence on an open deal continue, which is not a touch of the program.

## Failure modes

**Honored in one system only.** Signs: sends after an instruction concentrate in one system, the text
provider, the sales sequences, a second email platform; the honoring log shows no write from that system
or a write past the deadline; complaints come from people who unsubscribed. Remedy: step 5, one
person-level store, a write per system with a log, and the system with no write taken off sending until
it reads the store.

**The page that adds steps.** Signs: the unsubscribe rate falls while complaints rise, because people
who cannot find the way out mark the message as spam; the page asks for a login, a reason before acting,
or announces a delay ("within 24 hours", to take a made-up wording); the CRTC's example path exists on your site. Remedy: step 4.

**The center that widens permission.** Signs: basis records whose source is the preference center and
whose wording version is empty; people with a requested message state shown marketing types ticked by
default and "saved" into marketing. Remedy: step 3, the center writes narrowing instructions freely and
widening ones only through a request.

**The pause that ends in a burst.** Signs: sends per person on the day a pause ends exceed the cadence;
deferred messages queued during the pause go out together. Remedy: step 7, suppression during the pause
and a resume into the cadence, not the backlog.

**The service row that lost its exemption unnoticed.** Signs: a promotional block appears in the order
confirmation of people who withdrew, from the service identity, without an unsubscribe link; the
change was made by content, not by a change of class. Remedy: step 6 and `transactional-messaging`'s
class check at the template version.
