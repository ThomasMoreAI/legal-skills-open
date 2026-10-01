# Online Safety Act 2023

The Online Safety Act 2023 (c. 50) regulates user-to-user services and search services with links to the UK. Ofcom is the regulator. There is no small-business exemption: the duties are proportionate to size and risk, but they apply from the first user post.

This is not the Digital Services Act. Do not import DSA vocabulary — trusted flaggers, statements of reasons, DSA points of contact, transparency database — into a UK service.

## Scope

**Section 3** defines a regulated user-to-user service as an internet service by means of which content generated, uploaded or shared by a user may be encountered by another user. A search service is one that includes a search engine. Both need a link with the UK: a significant number of UK users, the UK as a target market, or content presenting a material risk of significant harm to UK users.

**Schedule 1 exemptions.** Read this before concluding that a small site is in scope:

| Para | Exempt |
|---|---|
| 1 | Email, where emails are the only user-generated content |
| 2 | SMS and MMS only |
| 3 | One-to-one live aural communications |
| 4 | Limited functionality services — where the only user content is comments or reviews on content published by the provider, sharing of such comments elsewhere, and expressions of view by likes, dislikes, emoji, ratings or voting |
| 5 | Combinations of the content in paras 1–5 |
| 7–8 | Internal business services |
| 9 | Services provided by public bodies |
| 10 | Education and childcare services |

Paragraph 6 removes the paras 1–5 exemptions for services on which pornographic content is displayed.

The practical dividing line: a blog with a comment section under the provider's own posts is normally exempt under para 4. A forum, a chat feature, user profiles with user-to-user visibility, direct messaging, or a marketplace with user listings is not. Establish exactly what users can post, and to whom, before deciding.

## Duties for in-scope user-to-user services

Part 3 Chapter 2. Status as at 2026-08-05: in force.

- **s 9** — illegal content risk assessment duties: a suitable and sufficient assessment covering the user base, the risk of encountering priority illegal content, the risk of the service being used to commit priority offences, and the design features affecting that risk. It must be kept up to date and redone before a significant change
- **s 10** — safety duties about illegal content: proportionate measures to prevent users encountering priority illegal content, to mitigate risk, and to take down illegal content swiftly once aware of it; terms of service must explain how users are protected
- **ss 11–12** — children's risk assessment and safety duties, where the service is likely to be accessed by children, including age verification or age estimation for primary priority content
- **s 20** — duty about content reporting: an easy-to-use route for users and affected persons to report illegal content and content harmful to children
- **s 21** — duties about complaints procedures: an accessible complaints system covering takedowns, restrictions, and failures to act
- **s 22** — duties regarding freedom of expression and privacy
- **s 23** — record-keeping and review duties, including a written record of each risk assessment

## Children's access assessment

Sections 35–37, Part 3 Chapter 4. Section 36 requires the provider to carry out a children's access assessment. The service is "likely to be accessed by children" (s 37) where children can access it and the child user condition is met — a significant number of children are users, or the service is of a kind likely to attract a significant number of child users. A provider may only conclude that children cannot access the service where age verification or age estimation is used with the result that children are not normally able to access it. Assessments must be repeated annually and before significant changes.

## Ofcom deadlines that have passed

| Duty | Deadline |
|---|---|
| First illegal content risk assessment | 16 March 2025 |
| Illegal content safety measures in place | 17 March 2025 |
| First children's access assessment | 16 April 2025 |
| Children's risk assessment | 24 July 2025 |
| Children's safety measures in place | 25 July 2025 |
| Highly effective age assurance for services allowing pornography | 25 July 2025 |

A service that launched after these dates does not get a fresh window: the assessment must be done before the duty bites. A service that never did one is already non-compliant, and the risk assessment is the document Ofcom asks for first.

Ofcom's Codes of Practice supply the measures a provider can adopt to be treated as complying. Departing from a Code is permitted but the provider must then demonstrate that its alternative measures meet the duty.

## Enforcement

Ofcom may require information, issue confirmation decisions, and impose penalties of up to the greater of £18 million or 10% of qualifying worldwide revenue. Senior managers can face criminal liability for failures to comply with information notices. Business disruption measures against payment and access providers are available for serious cases.

## Template — terms of service block for a small user-to-user service

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h2>Content rules and how we enforce them</h2>
<p>
  You may not post content that is illegal, including [[list the priority offence categories relevant
  to the service]]. We remove illegal content when we become aware of it.
</p>

<h2>Reporting content</h2>
<p>
  Anyone can report content they believe is illegal or harmful to children using [[link to the
  reporting route]]. You do not need an account to report. We will tell you what action we have taken.
</p>

<h2>Complaints</h2>
<p>
  If we remove your content, restrict your account, or you believe we have not acted on a report,
  you can complain using [[link]]. We will respond within [[period]].
</p>

<h2>Children</h2>
<p>
  [[Age requirement, how it is checked, and what age assurance is used — or the recorded conclusion
  of the children's access assessment.]]
</p>
```

## Checkpoints

- [ ] Scope decision recorded in writing, with the Schedule 1 paragraph relied on if the service is exempt
- [ ] Illegal content risk assessment completed, dated, and stored (s 9, s 23)
- [ ] Safety measures proportionate to the assessment and actually implemented (s 10)
- [ ] Children's access assessment completed and repeated annually (s 36)
- [ ] Where children are likely users: children's risk assessment and safety measures in place (ss 11–12)
- [ ] Highly effective age assurance where pornographic content is allowed
- [ ] Content reporting route reachable without an account (s 20)
- [ ] Complaints procedure covering takedowns and failures to act (s 21)
- [ ] Terms of service explain the protections and are clear and accessible (s 10)
- [ ] Records of assessments and decisions retained (s 23)
- [ ] No DSA terminology, no reference to trusted flaggers or an EU point of contact
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
