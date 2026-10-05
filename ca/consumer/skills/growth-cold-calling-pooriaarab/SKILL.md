---
name: growth-cold-calling-pooriaarab
title: growth-cold-calling
description: Plan a B2B cold-calling campaign under Canada's CRTC Unsolicited Telecommunications Rules — when a human may dial versus when a machine may (ADAD/auto-dialer express-consent rule with no existing-business-relationship exemption, the opposite of CASL email's conspicuous-publication implied consent), where the National DNCL does and does not apply (business-to-business calls are exempt from DNCL but still bound by the Telemarketing and ADAD Rules), permitted calling hours, mandatory identification and callback-number display, and why an AI voice agent looks cheap but is illegal without prior express consent at first-campaign volumes. Also covers call recording (Criminal Code one-party rule versus the OPC's notice-and-purpose requirement), reaching buyers email cannot (gatekeepers, role addresses, contact-form firms), the single qualifying question, logging call outcomes so the prospect list improves, and sharing one suppression list with the email channel. Pairs with growth-cold-email
  and growth-prospect-list. Use when planning phone outreach, deciding between human dialling and an AI voice agent, checking whether a call list is callable, or handling gatekeepers and callbacks.
author: pooriaarab
author_url: https://github.com/pooriaarab/skills/tree/main/growth-cold-calling
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ca
practice: consumer
language: en
---

# growth-cold-calling

How to run B2B phone outreach in Canada without building an illegal robocaller.
Pairs with `growth-cold-email` (the email channel and its CASL rules) and
`growth-prospect-list` (building and scoring the list you will call).

Every legal claim below is **Canada**. Other countries run their own regimes —
do not assume any of this travels.

## The failure this skill prevents

A team wires up an AI voice agent because it looks cheap, points it at a list
of businesses, and assumes the email logic carries over: published business
contact, prior customer, surely callable. Under CASL s. 10(9)(b) a
conspicuously published business address *can* imply consent to a commercial
electronic message. For an automated telemarketing call the rule is the
opposite: Part IV, s. 2 of the CRTC Unsolicited Telecommunications Rules (UTRs)
says a telemarketer shall not initiate a telemarketing telecommunication via
an ADAD unless **express consent** has been provided by the consumer — and
industry's request for an existing-business-relationship exemption to that
rule was considered and kept out (see Compliance and Enforcement Regulatory
Policy CRTC 2014-155). Getting the two backwards — email logic on a voice
agent — is the common failure, and it produces the exact fact pattern the
CRTC penalizes (e.g. the GoodLife $300,000 ADAD enforcement).

**ADAD** means automatic dialing-announcing device: equipment that stores or
produces numbers and delivers a prerecorded or synthesized voice message. An
AI voice agent that places calls and talks to whoever answers is, at minimum,
in ADAD territory for consent purposes. Treat it as one until a lawyer tells
you otherwise on your specific facts.

## What the CRTC rules actually require

Primary source throughout: the [Unsolicited Telecommunications
Rules](http://crtc.gc.ca/eng/trules-reglest.htm) (UTRs). Three parts matter,
and they apply differently:

- **National DNCL Rules (Part II).** Do not call numbers on the National DNCL
  unless you hold express consent or the call fits an exemption (existing
  business relationship, etc.). **Business-to-business calls are exempt from
  the National DNCL Rules** (confirmed in the [National DNCL consumer
  FAQs](https://lnnte-dncl.gc.ca/en/Consumer/Frequently-Asked-Questions)) —
  this is the one place B2B gets relief.
- **Telemarketing Rules (Part III).** Apply **whether or not** the call is
  exempt from the DNCL Rules, and to personal *and* business numbers (see
  Compliance and Enforcement Decision CRTC 2018-483, which dismissed DNCL
  counts against business numbers but kept the Telemarketing-Rule analysis).
  So a B2B call skips the DNCL scrub but keeps every other obligation:
  - **Calling hours:** 9:00 a.m.–9:30 p.m. weekdays, 10:00 a.m.–6:00 p.m.
    weekends, in the *called party's* local time ([CRTC compliance
    summary](http://www.crtc.gc.ca/eng/info_sht/t1032.htm)). A
    cross-timezone list needs per-number scheduling, not one dial window.
  - **Identification:** state who you are and the call's purpose at the
    start; provide a number where someone can be reached about the call on
    request; display a reachable calling number — intentional blocking of
    call display violates the Rules.
  - **Internal DNCL:** even DNCL-exempt callers must keep their own do-not-call
    list and honor requests ([Understand telemarketing rules for
    compliance](https://crtc.gc.ca/eng/phone/telemarketing/reg.htm)).
- **ADAD Rules (Part IV).** No telemarketing via ADAD without the called
  party's **express consent to be contacted via ADAD by you**. No
  existing-business-relationship exemption, no published-number exemption. A
  prior customer you may lawfully dial by hand is still off-limits to the
  voice agent until they expressly agree to automated calls.

Non-solicitation ADAD calls (appointment reminder, outage notice — no sales
pitch) sit under a different, conditional section (Part IV, s. 4), not the
prohibition. The moment the message sells or promotes, you are back under the
express-consent rule. Do not smuggle a pitch into a "reminder."

## When a human dials and when a machine may

- **Human dials a B2B list:** the default legal path. Scrub personal numbers
  against the DNCL anyway (mixed lists happen), keep hours and ID discipline,
  log everything. No express consent needed up front — the consent regime
  that bites is the ADAD one, which you are not triggering.
- **Machine places the call (voice agent, robodialer, prerecorded drop):**
  allowed only to people who gave **express consent to automated calls from
  you**. Practically, that means existing opt-ins (a signup checkbox for
  automated calls, a written agreement) — never a scraped or bought list.
- **The economics rarely favour the machine first.** A voice agent carries
  fixed setup and compliance cost (consent capture, logging, review) that a
  first campaign spreads over very few calls, while its only advantage —
  per-call cost near zero — pays off at volumes you do not have yet. A human
  with a 50-number list learns the objections in an afternoon; a machine with
  a 50-number list learns nothing and risks 50 violations. Automate the
  *follow-up* (logging, scheduling, suppression) before you automate the
  *voice*.

This skill does not hold past the consent line: if you believe you have
express ADAD consent for a list, have counsel confirm the consent wording
covers automated telemarketing before you dial.

## Recording the call

Two different laws, two different bars — clear both:

- **Criminal law (Canada):** intercepting a private communication is an
  offence under [Criminal Code s. 184](https://laws-lois.justice.gc.ca/eng/acts/c-46/section-184.html),
  but s. 184(2)(a) excludes interceptions with the consent of the originator
  or intended recipient — so recording a call **you participate in** is
  lawful on your own consent alone (one-party consent).
- **Privacy law (Canada):** recording *collects personal information*, so the
  [OPC's guidance on recording customer
  calls](https://www.priv.gc.ca/en/opc-news/news-and-announcements/2018/an_180418/)
  expects the caller to be told the recording is happening **and what it is
  for**, with consent before taping — enforced in findings such as PIPEDA
  Case Summary #2007-384 (outgoing marketing calls recorded without notice).
  State the purpose ("recording so I can log your answer accurately"), not
  just the fact.

And the sentence that causes the confusion: a blanket "this call may be
recorded" announcement is **notice of recording, not consent to the call**.
It satisfies neither the ADAD express-consent requirement nor a DNCL
exemption. Do not point at the announcement as your permission to dial.

## Reaching the buyers email cannot

Phone earns its place by defeating email's failure modes — plan for each:

- **Gatekeepers.** The receptionist's job is filtering interruptions. Do not
  pitch them; ask for *routing help* ("who looks after shop-floor
  scheduling?") and treat a name as the win. Call back outside peak
  switchboard hours for the named person directly.
- **Role addresses.** `info@` and `sales@` inboxes are triaged or ignored;
  the same firm often answers its phones. One listed switchboard number plus
  a named buyer beats ten role-address emails.
- **Contact-form firms.** Businesses that hide addresses behind forms still
  publish phone numbers. A call is the legitimate cold channel where email
  has no door — which is exactly why the list in `growth-prospect-list`
  should flag per-record whether phone is the *only* channel.

## The qualifying question and the log

A cold call has one job: decide whether a second conversation is warranted.
Write **one qualifying question** before you dial — answerable in under a
minute, disqualifying most of the list (e.g. "who decides your tooling
spend, and is that review happening this quarter?"). Anything the answer
cannot kill is not a qualifier, it is small talk.

Log every call the same day, in the same fields, or the list never improves:

- outcome: `connected-qualified` / `connected-not-qualified` /
  `gatekeeper-name` / `voicemail` / `no-answer` / `wrong-number` /
  `do-not-call-request` (honor immediately, add to the internal DNCL);
- the qualifier asked and the verbatim answer;
- agreed next step with a date, or explicit no-next-step.

Review the log weekly: which segment connects, which qualifier actually
discriminates, which numbers are dead. That review is the list-building input
for `growth-prospect-list` — a second pull of lookalike numbers beats a
second pass over dead ones.

## Suppression is shared with email, not duplicated

One suppression list serves both channels. A do-not-call request, a bounce
that reveals a dead business, an "email me instead" — each suppresses or
redirects **the record**, not the channel. Keep suppression keyed on the
business/contact in the shared list store from `growth-prospect-list`, with a
per-channel flag (`phone-suppressed`, `email-suppressed`) plus reason and
date. Two separate blocklists guarantee the failure where email opts out and
the dialer calls the next day.

## Limits of this skill

- Voice-agent vendor pricing moves too fast to document — evaluate vendors
  against the consent bar above, not their feature pages.
- Email content, CASL beyond the s. 10(9)(b) contrast, and list-building live
  in `growth-cold-email` and `growth-prospect-list`.
- Penalties, exemptions on unusual facts, and whether your consent wording
  qualifies as express are counsel questions, not skill questions.
