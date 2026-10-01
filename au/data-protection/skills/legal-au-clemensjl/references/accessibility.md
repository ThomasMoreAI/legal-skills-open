# Accessibility

Australia has **no European Accessibility Act equivalent**. There is no statute that mandates WCAG conformance for private sector websites, no accessibility statement requirement, no notified deadline, and no market surveillance authority. Anyone porting an EU accessibility statement template into an Australian site is inventing an obligation. Status as at 2026-08-05.

What exists instead is a discrimination duty that is broader in principle and vaguer in specification.

## Disability Discrimination Act 1992 (Cth)

The Act makes it unlawful to discriminate against a person on the ground of disability in the provision of **goods, services and facilities** (s 24). A website or app through which goods or services are offered is a service for this purpose. Discrimination includes indirect discrimination: imposing a requirement or condition with which a person with a disability cannot comply, where the requirement is not reasonable in the circumstances — which is what an inaccessible interface does.

The Act contains an **unjustifiable hardship** defence, assessed on the benefit and detriment to all affected, the effect of the disability, the financial circumstances of the respondent, and the availability of financial assistance. Cost alone is not the test, and the defence gets harder to run as accessible development becomes standard practice.

Enforcement runs through individual complaints to the Australian Human Rights Commission, conciliation, and then proceedings in the Federal Court or Federal Circuit and Family Court. There is no regulator issuing fines, and there is no compliance certificate. The exposure is a complaint, remediation under time pressure, damages and adverse publicity.

[[UNVERIFIED: the section numbers cited above (s 24 for goods, services and facilities; the unjustifiable hardship provision) were not confirmed against legislation.gov.au in this session]]

## AHRC guidance and WCAG

The Australian Human Rights Commission has published advisory notes on web accessibility under the Disability Discrimination Act, recommending conformance with the Web Content Accessibility Guidelines as the practical way to discharge the duty and to support an unjustifiable hardship argument. The advisory notes are guidance, not law: conformance is not a legal safe harbour, and non-conformance is not automatically unlawful — but a documented conformance target and testing regime is the strongest available evidence that the service was designed reasonably.

[[UNVERIFIED: the current version number and date of the AHRC "World Wide Web Access: Disability Discrimination Act Advisory Notes", and which WCAG version and conformance level they recommend, could not be retrieved in this session — humanrights.gov.au blocked automated access. Check humanrights.gov.au before quoting a version.]]

**Practical target:** WCAG 2.2 Level AA. It is the current W3C recommendation, it is what Australian government procurement and most enterprise contracts now specify, and adopting the latest version removes the argument about which version applied when.

## Government services

Australian Government digital services are subject to the Digital Service Standard under the Digital Experience Policy, administered by the Digital Transformation Agency, which sets an accessibility requirement referencing WCAG. State and territory governments run their own equivalents, and several state procurement frameworks impose WCAG conformance contractually on suppliers.

[[UNVERIFIED: the current WCAG version and conformance level required by the Digital Service Standard, and the date the current version of the Standard took effect, could not be retrieved in this session — digital.gov.au did not respond. Confirm at digital.gov.au before stating a level in a tender response or a contract.]]

If the project is government-facing or delivered under a government contract, the contractual standard governs and it is usually stricter than the discrimination duty.

## What to actually do

An accessibility statement is optional in Australia. Publishing one is still worthwhile: it gives a person who hits a barrier a route other than a complaint, and it evidences intent.

The engineering work is where the risk sits:

- keyboard operability of every flow that leads to a transaction, tested without a mouse
- visible focus indicators that are not removed by a CSS reset
- form labels programmatically associated with their inputs, and errors described in text rather than by colour
- text contrast measured, not estimated
- alternative text that conveys purpose, empty alt for decorative images
- headings in a real hierarchy, landmarks present
- video captions and transcripts
- no reliance on hover, drag or motion as the only way to do something
- reduced-motion preference respected
- interactive components built from native elements or a tested pattern, not divs with click handlers

Automated tools find a minority of issues. A screen reader pass over the signup and checkout flows finds the rest.

## Template — accessibility statement

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h1>Accessibility</h1>
<p>[[Entity name]] aims to make [[service]] usable by as many people as possible,
   including people with disability.</p>

<h2>Standard we work to</h2>
<p>We aim to conform to the Web Content Accessibility Guidelines (WCAG) [[version]] at
   Level [[AA]]. We last assessed [[service]] on [[date]] using [[method: manual keyboard
   and screen reader testing, automated scanning, external audit by {{auditor}}]].</p>

<h2>Known limitations</h2>
<p>[[List them honestly, with the reason and the date by which each will be fixed.
   Overstating conformance is a misleading representation.]]</p>

<h2>If you hit a barrier</h2>
<p>Contact [[name or team]] at [[email]] or [[phone]]. We aim to respond within
   [[period]] and to provide the information or service you need in another way while we
   fix the issue.</p>
<p>If you are not satisfied, you can make a complaint to the Australian Human Rights
   Commission at humanrights.gov.au.</p>
```

## Checkpoints

- [ ] No imported EU accessibility statement wording, no reference to the European Accessibility Act, EN 301 549, or a national enforcement body
- [ ] Conformance target agreed in writing with the business, with a version and a level
- [ ] Claimed conformance level is true — an overstated claim is a misleading representation under ACL s 18
- [ ] Signup and checkout flows completed with keyboard only
- [ ] Screen reader pass over the primary transaction flow
- [ ] Contrast measured against the target level
- [ ] Form errors conveyed in text and programmatically associated
- [ ] Known limitations listed with remediation dates rather than hidden
- [ ] A real human contact route for accessibility problems, monitored
- [ ] Government or enterprise contract accessibility clauses checked separately — they usually bind harder than the Act
- [ ] Every `[[…]]` resolved or reported as `[[MISSING: …]]`
