---
claim_type: definition
source: "internal synthesis"
source_type: internal
checked: 2026-09-14
---

# Vocabulary of consent and preferences

The three mechanics assume these terms. The first three, *basis record*, *instruction* and *purpose*, are
the reason arguments about "whether we have consent" do not settle: one side means a flag, the other
means a record that would survive a challenge, and a third means whether the churn model may run at all.
Several words here are shared with neighbors, and those are marked at the end.

## The units

**Basis record.** One person, one channel, one purpose, with: what the permission rests on (the basis
type), where it came from (the point and the source of the contact), the wording version, the proof
(who, when, how), and the lifetime (an expiry event or a review date). The unit of
`lawful-basis-and-collection.md`. `onsite-capture` calls the proof part of it the *consent record*: what
the person saw, when, on which page, through which point, which version of the wording. The basis record
is that plus the basis type, the scope and the lifetime.

**Instruction.** One recorded choice by the person after the basis exists, about one scope: a message
type on or off, a frequency, a channel, a pause with an end date, a withdrawal, or an objection. It has a
route, a scope, a timestamp and a deadline. The unit of `preference-center-and-unsubscribe.md`.

**Purpose.** One reason the program holds or uses personal data other than to send a message: selecting,
predicting, personalizing, testing, measuring, exporting, keeping. It has the data it reads, a basis by
regime, a retention line, an owner and a stop route. The unit of `processing-beyond-sending.md`.

## The basis

**Basis.** What makes a message to a person lawful in a channel: express consent, an exception whose
conditions all hold, an opt-out regime's requirements met, or a requested message. It answers "may we",
not "can we prove it"; the proof is a separate field of the record.

**Express consent.** The person agreed to marketing in a request written for it: an affirmative action
on an unticked box, a signature, a spoken yes on a script, a code entered. Under the FCC's rule for
marketing texts, an agreement in writing bearing the person's signature and naming the number.

**Exception.** A regime's permission to send without consent when every named condition holds: contact
details obtained by you in a sale or negotiations, marketing of similar products only, a refusal offered
at collection and in every message (EU, UK); a purchase, lease or written contract within two years, an
inquiry within six months (Canada, the *existing business relationship*). One condition missing and the
exception does not exist. Called *soft opt-in* in the UK and *implied consent* in Canada; the library uses
*exception* for both and names the regime.

**Opt-out regime.** A regime in which no prior permission is needed and the message requirements plus an
honored opt-out are the basis (US commercial email under CAN-SPAM).

**Requested message.** A basis for one named message the person asked for and nothing beyond it. A
handover state in `onsite-capture`'s sense, and the state of an address taken in a conversation in
`chat-and-bots`'.

**Recipient type.** Whether the address belongs to a person or to an organization, in the sense the
regime uses (the UK's individual and corporate subscribers). A field of the record, because it changes
the basis.

**Wording version.** The text of a request as it stood between two dates, with an identifier. The
record stores the identifier; the archive stores the text. A change of text is a new version.

**Proof.** Who, when, through which point, how, on which wording version. What a trace opens. Not the
basis: a message can rest on a basis you cannot prove, and on no basis you can prove perfectly.

**Confirmed opt in.** A second step in which the person acts on the address they gave. It proves the
address belongs to the person who agreed; no regime opened here requires it. `onsite-capture` builds the
step and uses the same words.

**Expiry event.** The event a lifetime is counted from when the regime counts one: the last purchase, the
last inquiry. The record holds the date computed from it, and a timer reads the date.

**Review date.** The date a basis with no statutory term is due for a refresh under your own policy. A
passed review date with no refresh recorded ends the record: a policy of yours, which the control metric
reads as it reads the law's terms.

**Refresh.** A new request to a person with a live record near its date or an old wording version. It
goes only where a message is allowed now. Silence is not a withdrawal; the record ends on its own date.

**Point.** Any way a contact enters: a form, a checkout, a till, a script, a card, an import, a partner
list. `onsite-capture` owns the on-site points; the inventory here covers all of them.

## The instruction

**Preference.** An instruction that narrows without withdrawing: a type, a channel, a frequency, a pause;
and one that routes without narrowing, the channel a service row is delivered in. `voice-of-customer`
sends an answer about what to receive and how often here under this name.

**Withdrawal.** An instruction that ends the basis for a scope: the unsubscribe, the "stop", the
objection to marketing. The scope comes from the wording it was taken under.

**Objection.** A withdrawal with the scope "marketing purposes": it stops selection, scoring,
personalization, marketing tests and exports, as well as sends (GDPR Article 21(2) and (3)).

**Route.** Where an instruction was taken: the link, the reply, the settings, the one-click header, a
person, a feedback loop, a browser signal. Every route writes the same instruction object.

**Scope.** How far an instruction reaches: the address or channel, the sender as a whole
(`email-program`'s global), one brand, one message type, one program (`email-program`'s five), the
account (`b2b-lifecycle`'s), marketing purposes, sale and sharing. Read from the wording, and ambiguous
wording gets the wider reading. The sender is the identity the message went out under.

**Pause.** An instruction with an end date. During it, marketing to the person is suppressed, not
deferred; the resume is into the cadence and needs no new request.

**Propagation deadline.** The time by which every sending system has honored an instruction: the
shortest of the windows that apply to the channel and the base. Measured to the last system's write.

**Honoring log.** Per instruction and per system, the time of the write. Its maximum is the lag; a
system with no write by the deadline is the broken link.

**Kept share.** Instructions that chose a preference instead of a withdrawal, over all instructions of
the period. Read beside the control metric, never promoted.

**Preference signal.** A browser setting that expresses an opt-out (the GPC). A route with the scope
"sale and sharing" where the regime recognizes it; not an email withdrawal.

## The purpose

**Purpose register.** The list of purposes, one line each: data read, systems, basis by regime, retention
line, owner, stop route. A purpose not on it does not run.

**Special category.** Data the GDPR names in Article 9(1): racial or ethnic origin, political opinions,
religious or philosophical beliefs, trade union membership, genetic data, biometric data for
identification, health, sex life or sexual orientation. In California, *sensitive personal information*
is the neighboring term with its own list.

**Proxy.** A field that is not named as a special category and from which a reader of a segment
definition would infer one. Treated as the category.

**Inference.** An attribute the program computed rather than the person declared. Personal data with the
accuracy of a guess; a health inference is health data for the purposes of selection.

**Age gate.** The question of age asked at a point before a record is written, with the line by regime.
`onsite-capture` places it; this skill sets the line.

**Retention line.** Per record class: how long, on which purpose, who owns it, which job deletes. A class
without a line is a finding.

**Suppression entry.** The record that a person is not to be sent to, with reason and scope. Survives
erasure as a hash, because its purpose is to prevent the next send.

**Sale and sharing.** Exports of personal data to a recipient for the recipient's purposes, in the sense
the California rules use; a register line with the recipient named, and a scope an instruction can
carry.

## The reading

**Marketing send.** One message to one person in one channel whose class in `contact-orchestration`'s
terms is campaign, automated flow, or perishable and personal; service rows and mandatory notices are
out, and a row of either that carried promotion is in from that version. The unit of the control
metric's denominator.

**Unsupported send.** A marketing send with no covering record at the moment of the send, or a record
whose lifetime had ended, or an instruction in effect whose scope covered it with the channel's
propagation deadline passed. The numerator of the join line. A send after an instruction and inside the
deadline is the cost of the lag, read beside.

**Trace.** A person opening the record behind a sampled send and checking its fields against the
archive. Its failures over the sampled sends are the trace line of the control metric, by capture point,
never added to the join line. A period with no trace reports the line as "not read", not as zero.

**Covering record.** A record whose person, channel and purpose match the send, whose fields resolve
(the basis type present; the point and date resolving to a wording version in the archive; under an
exception the event date inside the term and the refusal-offered flag; under an opt-out regime the
source), and whose regime's definition of a basis is met: request and proof under consent; event and all
conditions under an exception; source and honored opt-out under an opt-out regime. A record with a
field that does not resolve is no record for the join.

## Words shared with neighbors

- **Consent record, handover state, requested message, confirmed opt in, age gate:** `onsite-capture`,
  in its sense; the basis record here contains the consent record.
- **Hard suppression, program suppression, suppression scope:** `email-program`; the five scopes are
  used here unchanged, with the account added from `b2b-lifecycle`.
- **Suppression** as a technical hold on an address: `deliverability`, in its sense.
- **Cap, message class, exemption, reachability loss, quiet hours:** `contact-orchestration`. An
  unsubscribe is a reachability loss event there and an instruction here; the two count the same event
  for different reasons.
- **Display permission, marketing opt-in for push, ask budget:** `push-notifications`.
- **Preference:** `voice-of-customer` uses the word for the answers it sends here, in this sense.
- **Service row, class check, content contract:** `transactional-messaging`.
- **Provenance, merge, deduplication:** `list-building`; its provenance (the intake point, the date of
  the basis event, what the person was told) is stamped on the row there, and the basis record here
  points at the same values; the source of the contact (the person, somebody else, bought or found) is
  a field here.
- **Place, core, fallback:** `personalization`, in its sense; an objection reads every place of the
  person as empty and holds a core message.
- **Account, account executive, handoff:** `b2b-lifecycle`.
- **Assignment log, holdout:** `experiments-and-holdouts`.
- **Disclosure, missed obligation, escalation:** `program-audit-and-ops`.
- **System map:** `martech-stack`, the register of facts with their owning systems and copies.
