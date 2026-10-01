# Pre-launch checklist

Run before go-live. Report each finding with its provision and its location, not as a general observation. Anything technically testable is tested, not judged by intent.

## Technical pass first

These four steps produce half the findings and take minutes:

1. Load the site in a clean browser profile with the network tab recording. Note every third-party domain contacted **before** any consent decision.
2. Application tab: capture every cookie, localStorage and IndexedDB entry present before the decision.
3. Full-text search across the project, including shop system strings and email templates, for: `odr`, `online dispute resolution`, `GDPR` used as the name of the applicable law, `Regulation (EU) 2016/679`, `Article 77`, `right of withdrawal`, `Consumer Protection from Unfair Trading`, `Companies (Trading Disclosures) Regulations 2008`, `TMG`, `Impressum`, `European Accessibility Act`, `Digital Services Act`, `CCPA`.
4. Complete the order or sign-up flow using the keyboard only.

## Website disclosures

- [ ] Reachable from every page, no login, no consent gate in front
- [ ] Registered name matches Companies House exactly
- [ ] Part of the UK of registration, registered number, registered office (reg 25(2) SI 2015/17)
- [ ] Geographic address of establishment, not a PO box (reg 6(1)(b) ECR 2002)
- [ ] Email address plus a second contact channel (reg 6(1)(c) ECR 2002)
- [ ] Supervisory authority where an authorisation scheme applies (reg 6(1)(e))
- [ ] Regulated profession block complete (reg 6(1)(f))
- [ ] VAT number if registered (reg 6(1)(g))
- [ ] Prices state whether tax and delivery are included (reg 6(2))
- [ ] Sole trader or partnership: proprietors' names and UK address for service (CA 2006 s 1201)
- [ ] Insolvency status disclosed if applicable (reg 26 SI 2015/17)

## Data protection

- [ ] Privacy notice present, reachable without consent
- [ ] Purpose, lawful basis, recipients and retention for every processing operation (Arts 13, 14)
- [ ] Legitimate interests named specifically
- [ ] Recognised legitimate interests only claimed where UK GDPR Annex 1 actually covers the case
- [ ] Services listed match the network log
- [ ] Transfers listed individually with a named mechanism
- [ ] Automated decision-making paragraph written to Arts 22A–22D, not the old Art 22
- [ ] Complaints paragraph routes to the controller first (DPA 2018 s 164A), then the Commissioner (s 165); no reference to Art 77
- [ ] Electronic complaint form live; 30-day acknowledgement built into the process
- [ ] Children: UK GDPR Art 8(1) age-13 threshold applied, not 16; Age Appropriate Design Code assessed where under-18s are likely users
- [ ] ICO fee paid at the correct tier, renewal diarised (reg 3 SI 2018/480)
- [ ] Record of processing, Art 28 contracts, breach process, DPIA where required — see `accountability-and-fee.md`
- [ ] EEA-facing exposure assessed; Art 27 EU representative flagged if EU GDPR Art 3(2) applies

## Cookies and tracking

- [ ] No non-exempt storage or access before a consent decision (PECR reg 6)
- [ ] Every pre-decision cookie mapped to a Schedule A1 exception, with the paragraph identified
- [ ] "Reject all" on the first layer, visually equal to "Accept all"
- [ ] No pre-ticked categories, no consent implied from continued browsing
- [ ] Granular choice per purpose; withdrawal as easy as consent
- [ ] Cookie table verified against the network log
- [ ] Paragraph 5 or 6 claims checked against vendor terms for third-party own-purpose use
- [ ] Consent log with timestamp, banner version and choices
- [ ] Embedded maps, video and fonts self-hosted or behind consent

## Marketing

- [ ] Marketing consent separate and unticked, wording describes what will be sent (PECR reg 22(2))
- [ ] Soft opt-in claims backed by an actual sale or negotiation, similar products only (reg 22(3))
- [ ] Charity soft opt-in only for details obtained on or after 5 February 2026 (reg 22(3A))
- [ ] Consent evidence stored with timestamp, source and wording
- [ ] Unsubscribe in every message, one action, working (reg 23)
- [ ] Sender identifiable, valid reply address (reg 23)
- [ ] Automated calls consented (reg 19); live calls TPS-screened (reg 21)
- [ ] Company details in email footers
- [ ] Influencer and affiliate content labelled "Ad" upfront (CAP Code 2.1, 2.3, 2.4; DMCC Sch 20 para 12)

## Selling to consumers

- [ ] Order button reads "order with obligation to pay" or equivalent (reg 14(4) CCRs 2013)
- [ ] Order summary directly above the button, total price inclusive of taxes (reg 14(2))
- [ ] Delivery restrictions and payment methods stated at the start of the ordering process (reg 14(6))
- [ ] All Schedule 2 information given before the consumer is bound (reg 13)
- [ ] Cancellation notice present, term "cancel" used, correct period start (regs 29, 30)
- [ ] Model cancellation form from Schedule 3 Part B provided and saveable
- [ ] Order confirmation on a durable medium (reg 16)
- [ ] Digital content immediate access: express consent and acknowledgement captured separately (reg 37)
- [ ] Cancellation exclusions only where reg 28 applies
- [ ] Return costs disclosed pre-contract if the consumer bears them (reg 35(5))
- [ ] Statutory rights described under CRA 2015 ss 9–11, 34–36, 49 and not excluded (ss 31, 47, 57)
- [ ] Terms reviewed against CRA 2015 Part 2 and Sch 2; no compulsory consumer arbitration
- [ ] Headline price includes every unavoidable charge (s 230 DMCC)
- [ ] Urgency and scarcity claims true and evidenced
- [ ] Reviews: incentivised ones labelled, no misleading filtering, removal process documented (Sch 20 para 13)
- [ ] No clause asserting a DMCC subscription duty — Chapter 2 is not in force

## Online safety

- [ ] Scope decision recorded, with the Schedule 1 paragraph if exempt
- [ ] Illegal content risk assessment completed and stored (OSA ss 9, 23)
- [ ] Safety measures implemented and proportionate (s 10)
- [ ] Children's access assessment done and repeated annually (s 36)
- [ ] Children's risk assessment and measures where children are likely users (ss 11, 12)
- [ ] Reporting route usable without an account (s 20); complaints procedure live (s 21)
- [ ] Terms of service explain the protections

## Accessibility

- [ ] Keyboard-only pass on the main flows, focus visible
- [ ] Screen reader pass on the primary conversion flow
- [ ] Labels associated, errors in text, contrast measured against WCAG 2.2 AA
- [ ] Zoom to 200% and 320px reflow tested; `prefers-reduced-motion` respected
- [ ] Public sector body: accessibility statement published and accurate (reg 8 SI 2018/952)
- [ ] Private sector: no published accessibility claim that testing does not support

## Complaints and dispute resolution

- [ ] No ODR link and no mention of the EU ODR platform anywhere in the project
- [ ] No citation of SI 2015/542 — revoked 6 April 2026
- [ ] ADR information built into the complaint response itself (DMCC s 308)
- [ ] Any named ADR body verified as one the trader actually belongs to
- [ ] Sector ombudsman named where membership is compulsory

## Sweep

- [ ] No EU, German or US provisions cited as UK law
- [ ] No invented company details — every unknown is `[[MISSING: …]]`
- [ ] Image and font licences documented
- [ ] Third-party trade marks used only with permission
- [ ] Draft marker `<!-- DRAFT – NOT LEGALLY APPROVED -->` still present wherever sign-off has not been given

## Reporting format

Findings as a table, most serious first:

| Severity | Location | Provision | Finding | Fix |
|---|---|---|---|---|
| critical / high / medium | file:line or URL | section or regulation | what is missing or wrong | the concrete step |

**Critical** means: regulatory penalty exposure, an unenforceable contract, or a consumer not bound. That covers missing service-provider information, tracking before consent, a mis-labelled order button, an absent cancellation notice, an unperformed illegal content risk assessment, and an unpaid ICO fee.
