# Web accessibility — ADA

Status as at 2026-08-05.

There is **no federal web accessibility regulation for private businesses.** The obligation is a bare statutory prohibition on discrimination, enforced by private plaintiffs, with the technical standard supplied by settlements rather than by rule. This is the opposite of the EU position, where the European Accessibility Act imposes dated obligations and a published accessibility statement. A US site does not need an accessibility statement; it needs an accessible site, because the enforcement mechanism is a lawsuit, not an audit.

## ADA Title III — 42 U.S.C. § 12182

Prohibits discrimination on the basis of disability "in the full and equal enjoyment of the goods, services, facilities, privileges, advantages, or accommodations of any place of public accommodation". The categories of public accommodation are listed at 42 U.S.C. § 12181(7). There is no damages remedy under Title III for private plaintiffs — the relief is injunctive plus attorney's fees, which is precisely what sustains serial filing. State analogues do carry damages: California's Unruh Civil Rights Act (Cal. Civ. Code § 51) provides statutory damages of a minimum of $4,000 per violation and treats an ADA violation as an Unruh violation, and New York State and City human rights laws also allow damages. Most high-volume filings are Californian or New York for that reason.

**DOJ has never issued a Title III web accessibility regulation.** Rulemaking begun in 2010 was withdrawn without a rule. There is therefore no federal standard, no safe harbour, and no compliance date for private businesses.

## The circuit split

Whether a website is itself a "place of public accommodation", or only covered when it connects to a physical place, is unresolved.

| Position | Circuits |
|---|---|
| Website covered only where there is a **nexus** to a physical place of public accommodation | Ninth Circuit; district courts in the Third and Sixth Circuits |
| Website may itself be a place of public accommodation, no physical nexus required | District courts in the First, Second and Seventh Circuits |

The Eleventh Circuit's panel decision in *Gil v. Winn-Dixie Stores, Inc.* — which had held Title III applies only to physical locations — was **vacated as moot**, so it is not binding precedent. Do not cite Winn-Dixie as settled law in the Eleventh Circuit.

Practical consequence: a pure e-commerce business with no storefront has a real defence in the Ninth Circuit and essentially none in New York. Because filings concentrate in New York and California, plan for the plaintiff-friendly position.

## The Title II rule and why it does not apply

DOJ's final rule "Nondiscrimination on the Basis of Disability; Accessibility of Web Information and Services of State and Local Government Entities", 28 CFR Part 35, published 24 April 2024, adopts **WCAG 2.1 Level AA** as the technical standard. Compliance dates were extended by DOJ in April 2026 and now stand at:

- **26 April 2027** — public entities with a total population of 50,000 or more
- **26 April 2028** — public entities under 50,000 and special district governments

It applies to **state and local government entities under Title II only**. It does not bind private businesses. Agents routinely cite this rule and its dates at private clients; that is wrong, and the dates quoted are usually the superseded 2026/2027 dates.

The rule matters indirectly in two ways: it makes WCAG 2.1 AA the de facto federal reference point, and a private business that contracts with a covered public entity can inherit the obligation contractually.

## The working standard

**WCAG 2.1 Level AA** is what DOJ consent decrees and private settlements almost invariably require. WCAG 2.2 Level AA is the current W3C recommendation and adds requirements (target size, focus appearance, dragging alternatives, accessible authentication); building to 2.2 AA satisfies 2.1 AA and is the sensible target for new work. Neither is legally mandatory for a private site.

Do not deploy an accessibility overlay widget as the remedy. Overlays have been the subject of FTC enforcement over accessibility claims and do not prevent Title III suits; plaintiffs specifically target sites running them.

## Adjacent obligations that do carry standards

Three routes impose an actual technical standard where Title III does not:

- **Section 508 of the Rehabilitation Act, 29 U.S.C. § 794d**, binds federal agencies and, in practice, their suppliers. Selling software to the federal government means the solicitation will require conformance, evidenced by an accessibility conformance report.
- **Contracts with state and local government** flow the Title II obligation down. A vendor whose product is used to deliver a public entity's service is contractually on the hook for the same WCAG 2.1 AA standard and the same dates.
- **State civil rights statutes** — Unruh in California, the New York State and City human rights laws — supply the damages that Title III lacks, and are pleaded alongside it.

## Accessibility statement

Not required by US law. If one is published, it becomes a representation and must be accurate — an overstated statement ("this site is fully WCAG 2.1 AA compliant") is both an FTC Act § 5 deception exposure and a gift to a plaintiff. Publish a contact route for accessibility problems and a factual description of the conformance level actually achieved, or publish nothing.

## Template — accessibility contact block

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h2>Accessibility</h2>
<p>
  We aim to conform to the Web Content Accessibility Guidelines (WCAG)
  [[2.1 or 2.2]] Level AA. [[STATE THE ACTUAL CONFORMANCE POSITION, INCLUDING
  KNOWN GAPS — DO NOT CLAIM FULL CONFORMANCE UNLESS AUDITED]]
</p>
<p>
  If you encounter a barrier on this site, contact us at
  <a href="mailto:[[ADDRESS]]">[[ADDRESS]]</a> or [[PHONE]]. We will respond
  within [[NUMBER]] business days and will provide the information or
  transaction through an alternative accessible method.
</p>
<p>Last reviewed: [[DATE]].</p>
```

## Checkpoints

- [ ] Keyboard-only pass through signup, search, cart and checkout; visible focus indicator throughout
- [ ] Screen reader pass through the same flows
- [ ] All non-decorative images have meaningful alternative text
- [ ] Form inputs have programmatically associated labels; errors are described in text, not by colour alone
- [ ] Colour contrast measured, not estimated
- [ ] Video has captions; audio has transcripts
- [ ] Page reflows at 320 CSS pixels wide and at 200% zoom
- [ ] Third-party embeds (payment, chat, booking, review widgets) tested — they are the usual point of failure and the vendor is usually the one to fix it
- [ ] No accessibility overlay relied on as the remedy
- [ ] Any published accessibility statement matches the audited reality
- [ ] Remediation plan dated and owned; a documented, executing plan is the practical defence
