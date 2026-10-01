# Online Safety Act 2021

Regulator: the eSafety Commissioner (esafety.gov.au). The Act binds a wide range of online services, not only large platforms — but most ordinary business websites fall outside the heaviest obligations. Establish which category the service is in before assuming anything. Status as at 2026-08-05.

## Service categories

The Act distinguishes **social media services**, **relevant electronic services** (messaging, email, chat, online games with communication features) and **designated internet services** (websites and apps generally, including app stores). A brochure website with no user interaction is a designated internet service but attracts almost nothing beyond the general content schemes. A comments section, a forum, user profiles, reviews with replies, or direct messaging moves the service into a category where reporting and moderation obligations bite. [[UNVERIFIED: the definitional section numbers (ss 13, 13A, 14) were not confirmed against legislation.gov.au in this session]]

## The complaints and removal schemes

eSafety operates statutory schemes for cyberbullying material targeted at an Australian child, adult cyber abuse, non-consensual intimate images, and illegal and restricted content. Where material is hosted on or provided by a service, eSafety can issue removal notices with short compliance windows, and can escalate to link deletion and app removal notices. Any service that hosts user content needs an internal route for receiving and acting on such a notice fast, with a named recipient and an out-of-hours path.

## Basic Online Safety Expectations

The Basic Online Safety Expectations are set by ministerial determination and apply to social media services, relevant electronic services and designated internet services. They are not directly enforceable as obligations, but eSafety can require a provider to report on how it meets them, and non-response is itself an enforceable failure. The determination was amended in 2024 to strengthen expectations around generative AI, recommender systems and reporting. [[UNVERIFIED: the exact title and dates — Online Safety (Basic Online Safety Expectations) Determination 2022 and its 2024 amendment — were not confirmed against legislation.gov.au in this session]]

## Industry codes and standards

Industry codes developed by sections of the online industry, and standards made by eSafety where a code is inadequate, regulate access to class 1 and class 2 material. A second phase of codes extending age assurance obligations beyond social media — to app stores, device manufacturers, search engines and other service categories — was developed and registered during 2025 and 2026. Any service that hosts, distributes or gives access to age-inappropriate material should check the current register of codes and standards on esafety.gov.au before relying on this summary. [[UNVERIFIED: the registration and commencement dates of the Phase 2 codes were not confirmed in this session]]

## Social media minimum age — Part 4A

The Online Safety Amendment (Social Media Minimum Age) Act 2024 (Cth) inserted Part 4A into the Online Safety Act. The obligation **started on 10 December 2025**.

- An **age-restricted social media platform** must take **reasonable steps** to prevent Australians under 16 from having an account.
- eSafety's assessment criteria: the sole or a significant purpose of the service is to enable online social interaction between two or more end-users; end-users can link to or interact with other end-users; end-users can post material; and the service has an account-based recommender feature or, while logged in, at least one of a set of design features such as feedback signals (likes, upvotes) or time-limited content (stories).
- Legislative rules exclude categories of service — including messaging, online gaming, and services whose primary purpose is health or education support. Check the current eSafety list of assessed platforms rather than reasoning from the criteria alone.
- **The obligation falls on the platform.** No obligation and no penalty attaches to a child or a parent.
- eSafety published regulatory guidance on 16 September 2025 setting out what reasonable steps look like. Government-issued identity documents are not required; platforms must offer alternatives, and the guidance addresses proportionality, accuracy, privacy and the handling of age assurance data.
- An independent review of the operation of the regime must be initiated within two years of 10 December 2025.

[[UNVERIFIED: the section numbers within Part 4A and the maximum civil penalty in penalty units were not confirmed against legislation.gov.au in this session; the commencement date, the obligation, the assessment criteria and the guidance date are confirmed from eSafety and the Department of Infrastructure]]

**Age assurance data is personal information.** Anything collected to verify age falls under the APPs, and for many services under the Children's Online Privacy Code once it is registered — due by 10 December 2026. Collect the minimum, do not retain the evidence, and write the APP 5 notice for it.

## Restricted content and age verification beyond Part 4A

Separate from the social media minimum age, obligations attach to services that make pornographic or other age-inappropriate material available to Australians. These sit in the industry codes and standards rather than in the Act itself, and they reach commercial pornography services, app stores and, through the later codes, search engines. A general business website does not encounter them; a service with adult content, gambling content, or an app distribution function does. Check the registered codes rather than reasoning by analogy.

## If the service hosts user content

Build these regardless of category, because they are what every regime asks for:

1. **Terms that state the moderation rules** — what is prohibited, what happens on breach, and how a decision is appealed. Vague "we may remove anything" clauses are unfair contract term candidates.
2. **A reporting route** for users, visible from the content itself, not buried in a help centre.
3. **A named contact for eSafety and law enforcement**, with an address that is monitored.
4. **A record of moderation decisions** — what was removed, when, on what basis, and who decided.
5. **An age gate assessment** — if the service can be reached by under-16s and has social features, document why Part 4A does or does not apply.
6. **Nothing borrowed from the EU Digital Services Act.** The DSA's notice-and-action mechanism, statement of reasons, trusted flaggers and out-of-court dispute settlement have no Australian counterpart. If the business also serves EU users, run the DSA obligations as a separate, EU-facing layer.

## Template — reporting and moderation section

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h2>Reporting content</h2>
<p>If you see content on [[service]] that breaches our rules, report it using the report
   control on the content, or email [[abuse contact]]. We aim to review reports within
   [[period]] and will tell you the outcome.</p>
<p>If the content involves cyberbullying of a child, adult cyber abuse, or an intimate
   image shared without consent, you can also report it to the eSafety Commissioner at
   esafety.gov.au.</p>

<h2>What we do about it</h2>
<p>[[What can be removed, what can be restricted, when accounts are suspended, how a
   decision can be appealed, and to whom.]]</p>

<h2>Contact for regulators and law enforcement</h2>
<p>[[Monitored email address]] · [[postal address]]</p>
```

## Checkpoints

- [ ] Service category assessed and the reasoning written down
- [ ] Part 4A applicability assessed and documented, even where the conclusion is "not an age-restricted social media platform"
- [ ] Current eSafety list of assessed platforms checked rather than inferred
- [ ] Any age assurance data flow covered by an APP 5 notice, minimised, and not retained
- [ ] Reporting route visible from the content, not only in a help centre
- [ ] Named, monitored contact for eSafety and law enforcement
- [ ] Moderation rules stated in the terms in specific language
- [ ] Moderation decisions logged
- [ ] Removal notice handling path exists with an out-of-hours escalation
- [ ] No EU Digital Services Act machinery imported into Australian-facing terms
- [ ] Every `[[…]]` resolved or reported as `[[MISSING: …]]`
