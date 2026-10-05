---
claim_type: mechanic
source: "internal synthesis"
checked: 2026-09-14
---

# Processing beyond sending: the purposes the program runs on the data, and how each one stops

The unit here is **the purpose**: one reason the program holds or uses personal data other than to send a
message, with the data it needs, its basis, its retention line and the route by which the person stops
it. Selecting recipients, predicting, inferring, assigning to a test group, exporting an audience,
measuring, and keeping records are each a purpose. Sending is `lawful-basis-and-collection.md`'s basis;
what the person chose about sending is `preference-center-and-unsubscribe.md`. This file is where the
neighbors' "the legal side is `consent-and-preferences`" lands for everything that is not a send.

## Entry conditions

The program uses data beyond sending: a segment, a score, a recommendation, a test, a report, an export,
a log. A system map exists or can be made with `martech-stack`: the register of facts, each with its
owning system and its copies.

## Exit conditions

A purpose register: each purpose with the data it uses, the basis by regime, the retention line, the
owner, and the person's stop route. A rule for special categories and their proxies, applied to every
segment definition and model input. An age gate at every point and a rule for what the program holds
about a child. A retention line for every record class, including consent records, suppression entries,
test assignment logs and conversation records, with a deletion job. An erasure procedure that keeps the
suppression entry. A sale-and-sharing register with the routes an opt-out arrives through. Objection
propagation to selection, scoring, personalization and exports, inside the same deadline as a withdrawal.

## Steps

**1. List the purposes in the program's own words.** Selecting recipients (segments, RFM, lifecycle
stages); predicting (churn, propensity, next purchase); personalizing (`personalization`'s substitutions
and choices of content); testing (assignment to groups, holdouts); measuring (reports, attribution,
cohorts); exporting (audiences to advertising platforms, lists to partners); keeping (consent records,
suppression entries, contact history, conversation transcripts, incident logs). Each purpose is a line
with the fields it reads, the systems that run it, and the owner. A purpose not on the register does not
run: a new segment on a new field, a new score, a new export is a register line first. Personal data are
"collected for specified, explicit and legitimate purposes and not further processed in a manner that
is incompatible with those purposes" (GDPR Article 5(1)(b)); `metric-definitions` and `crm-reporting`
hand the question of the basis under a report here, and this line is the answer: measuring is a purpose,
and it reads only fields collected for a purpose it is compatible with. Sending people with no basis a
message is itself a processing event, and `program-audit-and-ops` logs it as one.

**2. Assign the basis per purpose and regime, and one stop route for all marketing purposes.** Under the
GDPR and UK GDPR the basis for a purpose is one of Article 6's, and which one your selection or scoring
rests on is a question for counsel that this library does not answer; what the library fixes is that the
sending regime and the data regime are two axes, and satisfying one does not satisfy the other. Whatever
the basis, "where personal data are processed for direct marketing purposes, the data subject shall have
the right to object at any time ... which includes profiling to the extent that it is related to such
direct marketing", and after the objection "the personal data shall no longer be processed for such
purposes" (Article 21(2) and (3)). So every marketing purpose on the register, selection, scoring,
personalization, marketing tests, marketing exports, has the same stop route: the objection, taken
through the routes of `preference-center-and-unsubscribe.md`, step 2, and written as an instruction with
the scope "marketing purposes". The right is stated "at the latest at the time of the first
communication", "clearly and separately" (Article 21(4)): the first message carries it, and
`email-design` places it. Under the California rules the stop routes are the opt-out of sale and sharing
and the limit on sensitive personal information (step 7). In Canada and under the US email rule the data
regime is a separate body of law not opened here; the register still holds the purpose, because the
retention and the erasure of step 5 and 6 need it.

**3. Keep special categories and their proxies out of selection.** The GDPR prohibits processing data
"revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, or trade
union membership", genetic and biometric data for identification, "data concerning health or data
concerning a natural person's sex life or sexual orientation" (Article 9(1)), subject to Article 9(2)'s
conditions, which are a question for counsel. The operational rule for the program: a segment
definition, a score input or a personalization rule may not use a field that names one of these, nor a
proxy that functions as one. The test for a proxy: would a reader of the segment definition infer one of
these about its members? "Bought a pregnancy test", "orders kosher", "filters by mobility aids", "reads
the diabetes guide", "donated to a party" each fail it, whatever the field is called. An attribute the
program inferred is treated as the category it predicts: a predicted "expecting" is a health inference
and does not enter a selection. `metric-definitions` and `segmentation` hand the question of an
indicator that indirectly reveals a category here, and this test is the answer. A special category the
person declared for service, an allergy on a food order, a condition on a pharmacy account, serves that
service and enters no marketing selection. In California, sensitive personal information (the Attorney
General's examples: "your social security number, financial account information, your precise
geolocation data, or your genetic data") gets the limit route of step 7.

**4. Put an age gate before the record, and hold nothing about a child for marketing.** The ages: under
the GDPR, 16 for information society services offered directly to a child, and each member state may set
13 to 16; 13 in the United Kingdom; under 13 is a child under COPPA in the United States; under 16 in
California for the sale of personal information, with the parent's opt-in under 13. Each point that may
reach children asks the age before it writes a record (`onsite-capture` places the gate; this step says
where the line runs by regime). Below the line: no marketing basis record, no marketing profile, no
selection, no assignment to a marketing test (`experiments-and-holdouts` hands this here), and no
export. A child's date of birth held on a parent's account for a birthday message is the parent's data
about the child, held on the parent's declared purpose: it produces the parent's message and no profile
of the child, and `triggered-messages` names it apart from other date triggers for that reason. Under
COPPA, collecting a child's online contact information without parental consent is allowed to "respond
directly on a one-time basis to a specific request from the child", with the information not used "to
re-contact the child" and "deleted ... promptly after responding"; a child's stock alert is that case and
nothing more. Non-essential push to a child in the UK is off by default (`push-notifications`).

**5. Give every record class a retention line and a deletion job.** Personal data are kept "for no
longer than is necessary for the purposes" (Article 5(1)(e)), and the CRTC sets no prescribed period and
asks for records "for as long as you will be contacting" the person. The lines:

- **consent records and wording archives**: the lifetime of the basis, plus the period during which a
  challenge can still be brought in your regime, which counsel names; the archive of wording versions
  lives at least as long as the last record that points at a version;
- **suppression entries**: kept for as long as the channel exists, because their purpose is to prevent
  a send, and erasing them re-enables it; kept as a hash where the regime lets the rest be erased;
- **test assignment logs**: as long as the result is being read, and no longer
  (`experiments-and-holdouts`'s own line); what survives is the aggregate;
- **conversation records**: the service window of the conversation's subject plus the dispute window
  your terms give, then deleted or stripped of identifiers (`chat-and-bots` hands the question here);
- **the source field of a contact**: as long as the record it belongs to, because it is part of the
  proof (`onsite-capture`);
- **incident logs** that name people: the incident's own retention, and they are personal data
  (`program-audit-and-ops`);
- **pending rows**: `lawful-basis-and-collection.md`, step 4.

Each line has an owner and a job that runs; a record class without a line is a finding. A retention
line that keeps data because "we might need it" names no purpose and fails Article 5(1)(e) on its face.

**6. Answer access and erasure requests, and keep the suppression entry.** The route: verify the person
without collecting more than the verification needs; find every system through the system map; delete
or anonymize in each; tell the processors that hold copies; write the outcome. The deadline is the regime's:
the California rules require a response "within 45 calendar days"; the GDPR sets its own in Article
12(3), which was not opened here, so open it before you set the timer. Exceptions are the regime's too
(the Attorney General's example: information the business is legally required to keep). The outcome for
marketing: the person is suppressed with the reason "erasure", the entry survives as a hash, and the
person can come back only through a new request at a point. A deletion that erases the suppression entry
is the failure this step exists for: the next import re-creates the person with no memory of the request.
`onsite-capture` hands the outcome of an erasure request here, and this is it.

**7. Register sale and sharing, and honor the signal.** Audiences exported to advertising platforms,
matched lists, data given to a partner who will use it for their own purposes: each is a register line
with the recipient named. Under the California rules a consumer may opt out of the sale or sharing of
their personal information, businesses that sell must show a "Do Not Sell or Share My Personal
Information" link, a browser signal like the GPC "must be honored ... as a valid consumer request", and a
business "must wait at least 12 months before asking you to opt back in." So the signal is a route in
`preference-center-and-unsubscribe.md`, step 2, with the scope "sale and sharing"; it stops the exports
for that person and does not by itself withdraw email consent, which is a different scope with a
different wording. Under the GDPR a recipient the request did not name is not covered by it
(`lawful-basis-and-collection.md`, step 3), and a new recipient is a new request. Sensitive personal
information in California gets the limit route: the person directs the business to use it "for limited
purposes, such as providing you with the services you requested", and the register line for any purpose
that reads such a field reads the instruction.

**8. Propagate the objection to everything on the register.** An objection to marketing, in any wording
("stop profiling me", "don't use my data for marketing", "delete my preferences"), is an instruction with
the scope "marketing purposes", and inside the same deadline as a withdrawal it stops: the sends
(`preference-center-and-unsubscribe.md`), the selections (the person leaves every marketing segment and
is not re-selected), the scores (no marketing score is computed or read for them), the personalization
(every place of `personalization`'s reads as empty for the person, and a message whose class there is
core is held rather than sent), the marketing tests (the person leaves the groups; whether their data may
still be read for the measurement of a test they were in is a question for counsel), and the exports.
For a B2B contact, the objection also removes their signals from the account's grade (`b2b-lifecycle`).
The register's stop route is one field on the person, and every purpose reads it before it runs.

**9. Route a disclosure immediately, and hold the record.** A wrong send that exposed data, an export to
the wrong recipient, a preference center that showed one person another's data: `program-audit-and-ops`
escalates at once to the organization's privacy owner, whose duty to notify a regulator is outside this
library. What this skill holds for them is the record: which purpose, which data, on what basis, since
when, and who received it.

## Thresholds and timings

| Quantity | Where it comes from | Class |
|---|---|---|
| EU: a child is under 16 for information society services on consent; member states may set 13 to 16 | GDPR Article 8(1), opened 2026-09-14 | legal |
| UK: 13 | UK GDPR Article 8(1), opened 2026-09-14 | legal |
| US: a child is under 13; parental consent before collection, use or disclosure | 16 CFR 312.2, 312.3(b) and 312.5, opened 2026-09-14 | legal |
| California: opt-in for the sale of a known under-16's information, the parent's under 13; a response to a request within 45 calendar days; 12 months before asking to opt back in | Attorney General's CCPA page, opened 2026-09-14 | legal |
| Canada: no prescribed period for records; keep them for as long as you contact the person | CRTC FAQ, opened 2026-09-14 | legal |
| Deadline for an objection to reach every purpose | the same as the withdrawal's in `preference-center-and-unsubscribe.md`, step 5 | legal and platform, as there |
| Retention of consent records | the basis lifetime plus the challenge period counsel names for your regime | parameter |
| Retention of test logs | until the reading is frozen (`experiments-and-holdouts`) | parameter |
| Retention of conversation records | the service window of the subject plus your dispute window | parameter |

The legal rows carry their sources and the people they do not bind in `SKILL.md`. The rest are yours.

## Edge cases

- **A parent's account with a child's birthday.** The parent's data about the child, on the parent's
  declared purpose; a birthday message to the parent, no profile of the child, no marketing to the child.
- **A special category declared for service.** An allergy, a mobility need, a medication: held for the
  service, absent from every selection, and absent from the fields a model can read.
- **An inferred attribute that is not a special category.** A gender inferred from a first name, an age
  band from behavior: an inference is personal data with the accuracy of a guess; `personalization`
  falls back rather than asserting it, and a person may object to it like any marketing profile.
- **A lookalike or matched audience.** Customer identifiers sent to an advertising platform are an export
  on the register with the platform as recipient; in California a sharing opt-out stops it for that
  person; under the GDPR the request named the recipient or did not.
- **Enrichment from a data broker.** Data about the person from a source other than the person: a
  purpose line with the source, and a first communication that says where the data came from (Article
  14(3)(b)); in Canada the basis for a message to that address is section 10(9)'s and not the
  enrichment's.
- **A B2B contact.** Their profiling objection removes their signals from the account grade
  (`b2b-lifecycle`); the account's own fields are the organization's data and stay.
- **A deceased person.** Suppressed on notice, with the reason; the record's retention follows the
  organization's rule for closed accounts, not the marketing line.
- **An employee, a supplier, a job applicant in the marketing base.** Their data came for another
  purpose; they are in the base on no marketing basis unless a point wrote one, and step 1's register
  shows the mismatch.
- **A holdout that contains a person who objected.** They leave the group on the day of the objection,
  and the assignment log records the removal with its date (`experiments-and-holdouts`); the measurement
  of the test they were in reads their earlier data or not on counsel's answer.

## Failure modes

**The proxy segment.** Signs: a segment or offer whose name or content tells the person what the program
inferred ("for your pregnancy", "kosher picks"); complaints that ask "how do you know"; a model input list
that includes a field a reader would recognize as one of Article 9(1)'s. Remedy: step 3's reader test on
every definition and input list, and the segment retired.

**Retention by default.** Signs: record classes with no line; consent records deleted by a cleanup job
while the contacts they supported stay, so the base holds people with no proof; wording archives purged
while records still point at their versions. Remedy: step 5, and the archive's line tied to the last
record that points at it.

**The erasure that erased the suppression.** Signs: a person who asked to be forgotten receives a
message after an import or a platform migration; the suppression entry is missing while the request is
logged. Remedy: step 6, the hashed entry that survives.

**The objection that stopped the send and not the selection.** Signs: a person who objected still
appears in exported audiences, still gets a score, still has a substitution value computed; a campaign
built on a segment includes them and the send is suppressed at the door, so the count of held sends rises
for them every period. Remedy: step 8, one field read by every purpose before it runs.

**The purpose that was never registered.** Signs: a report, a score or an export reads a field nobody
wrote a line for; the system map shows a copy in a system the register does not name. Remedy: step 1, the
line written before the purpose runs, and the copy either registered or removed.
