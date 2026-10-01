# Notifiable Data Breaches

Part IIIC of the Privacy Act 1988 (Cth). Binds every APP entity, so an entity relying on the s 6D small business exemption is outside the scheme — until one of the carve-outs applies or it opts in. Status as at 2026-08-05. Source: OAIC, *Data breach preparation and response*, Part 4.

## The test — s 26WE(2)

An eligible data breach occurs where all three are satisfied:

1. there is unauthorised access to, unauthorised disclosure of, or loss of, personal information held by the entity;
2. a reasonable person would conclude the access, disclosure or loss would be **likely to result in serious harm** to one or more of the individuals to whom the information relates; and
3. the entity has not been able to prevent the likely risk of serious harm through remedial action.

"Likely" means more probable than not, judged objectively from the position of a reasonable person in the entity's position (s 26WG). The factors include the kind and sensitivity of the information, whether it was protected by security measures and how easily those could be overcome, who has obtained or could obtain the information, and the nature of the harm. Serious harm covers physical, psychological, emotional, financial and reputational harm.

Remedial action that genuinely removes the likely risk — recovering a device before access, a remote wipe that is confirmed, resetting credentials before use — means there is no eligible data breach. Record the reasoning, because the assessment itself is the evidence.

## Assessment — s 26WH

Where the entity is aware of reasonable grounds to **suspect** an eligible data breach but not to believe one, it must carry out a reasonable and expeditious assessment of whether there are reasonable grounds to believe it is an eligible data breach, and take all reasonable steps to complete it **within 30 calendar days** after becoming aware of the grounds to suspect (s 26WH(2)).

Thirty days is a maximum, not a target. The OAIC treats a full 30-day assessment for a simple incident as a compliance issue in itself. The clock starts on awareness of grounds to suspect, which is usually earlier than the incident being escalated to management.

There is no 72-hour rule. That is GDPR Art 33 and does not apply here.

## Notification — ss 26WK, 26WL

Once there are reasonable grounds to believe there has been an eligible data breach, the entity must **as soon as practicable**:

- prepare a statement and give a copy to the Commissioner (s 26WK), containing the entity's identity and contact details, a description of the breach, the kinds of information concerned, and the steps the entity recommends individuals take in response; and
- notify individuals (s 26WL) by one of three routes, in order of preference: notify each individual to whom the information relates; notify only those at likely risk of serious harm; or, if neither is practicable, publish the statement on the entity's website and take reasonable steps to publicise its contents.

Notification uses the entity's normal communication channel with the individual. A breach notice that is buried in a marketing newsletter is not a notification.

## Exceptions

Exceptions and modifications apply for breaches also notifiable under the My Health Records Act 2012, for enforcement bodies where notification would be likely to prejudice enforcement activities, where notification would be inconsistent with a secrecy provision, and where the Commissioner declares that notification need not be given (ss 26WD, 26WN, 26WP, 26WQ). Also relevant: where another entity has already notified in respect of the same breach.

## Response plan

The plan is an APP 1.2 obligation in substance — practices, procedures and systems to ensure compliance. It has to name people, not roles in the abstract.

1. **Contain** — stop the access, isolate the system, revoke credentials, preserve logs before they roll over.
2. **Escalate** — a named response lead and a deputy, reachable outside business hours, with authority to engage external help.
3. **Assess** — start the 30-day clock at the moment of awareness of grounds to suspect and record that moment. Document the s 26WG factors as you go.
4. **Notify** — Commissioner and individuals as soon as practicable once the belief is formed. Draft the statement in parallel with the assessment, not after it.
5. **Review** — root cause, control changes, and an update to the register.
6. **Adjacent obligations** — check separately: contractual notification deadlines with enterprise customers (often 24 or 48 hours and much shorter than the Act), payment scheme rules, ASX continuous disclosure for listed entities, the Security of Critical Infrastructure Act 2018 for regulated assets, and GDPR Art 33 where Art 3(2) applies. [[UNVERIFIED: SOCI Act reporting timeframes were not checked in this session]]

## Template — statement to the Commissioner and to individuals

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h1>Notification of a data breach</h1>
<p>[[Entity name]], ABN [[ABN]], [[address]]. Contact for this notification:
   [[name, role, email, phone]].</p>

<h2>What happened</h2>
<p>On [[date]] we became aware that [[description of the unauthorised access, unauthorised
   disclosure or loss]]. The incident occurred on or around [[date]] and affected
   [[number or estimate]] individuals.</p>

<h2>What information was involved</h2>
<p>[[Kinds of information: name, email address, postal address, phone number, date of
   birth, order history, hashed passwords, identity document numbers, health information.
   State what was not involved where that is material, e.g. full payment card numbers.]]</p>

<h2>What we have done</h2>
<p>[[Containment and remedial steps, with dates.]]</p>

<h2>What we recommend you do</h2>
<p>[[Concrete steps: change the password on this service and anywhere it was reused;
   enable multi-factor authentication; watch for phishing referencing this incident;
   contact IDCARE on 1800 595 160; place a ban on your credit report if identity
   documents were involved.]]</p>

<h2>How to contact us</h2>
<p>[[Channel, hours, expected response time.]] You may also complain to the Office of the
   Australian Information Commissioner at oaic.gov.au or 1300 363 992.</p>
```

## Checkpoints

- [ ] The entity's APP entity status confirmed — the scheme does not bind an exempt, non-opted-in small business operator
- [ ] Response plan exists, names individuals, and has been rehearsed
- [ ] Time of awareness of grounds to suspect is captured automatically, not reconstructed later
- [ ] Assessment documented against the s 26WG factors
- [ ] Assessment completed well inside 30 days, with the reason for any extension recorded
- [ ] Statement contains all four s 26WK matters
- [ ] Individual notification route chosen and justified, with publication used only where the first two are impracticable
- [ ] Recommended steps are specific and actionable, not "remain vigilant"
- [ ] Contractual and sector notification deadlines checked separately — several are shorter than the Act
- [ ] Log retention long enough to support an assessment
- [ ] Every `[[…]]` resolved or reported as `[[MISSING: …]]`
