# Pre-launch checklist

Run before go-live. Every finding is reported with its provision and its location, not as a general remark. Anything technically testable is tested, not assessed from intent.

## Technical pass first

These four steps produce roughly half the findings and take minutes:

1. Load the site in a clean browser profile with the network tab recording. List every third-party domain contacted and what is sent to each.
2. Application tab: list every cookie, local storage and IndexedDB entry, with expiry.
3. Full-text search the whole project — including shop system strings, transactional email templates and PDF invoice templates — for: `GDPR`, `lawful basis`, `legitimate interest`, `data controller`, `data subject`, `right to erasure`, `right to be forgotten`, `DPO`, `72 hours`, `cooling-off`, `right of withdrawal`, `14 days`, `CAN-SPAM`, `opt out`, `no refund`, `store credit only`, `final sale`, `Impressum`, `TMG`, `ODR`, `EUR`, `£`.
4. Complete the signup and checkout flows with the keyboard only, then again with a screen reader.

## Privacy scope

- [ ] APP entity status determined: turnover figure recorded, every Privacy Act s 6D carve-out tested individually
- [ ] Opt-in status under s 6EA confirmed before any claim of Privacy Act compliance
- [ ] No claim of Privacy Act compliance by an exempt, non-opted-in entity
- [ ] EU, UK or California exposure assessed, with the trigger identified

## Privacy policy

- [ ] Reachable without login, payment or dismissing a banner
- [ ] All seven APP 1.4 items present with real content
- [ ] Information categories match the actual database and the network tab findings
- [ ] Recipients match the actual vendor list
- [ ] Overseas recipients named with countries, not "internationally"
- [ ] Access, correction and complaint routes named with a live contact
- [ ] OAIC named as the external complaint avenue with correct details
- [ ] Automated decision-making disclosure drafted or "not applicable" recorded, ahead of 10 December 2026 (APP 1.7–1.9)
- [ ] No GDPR vocabulary unless the section is explicitly marked as EU-facing

## Collection notices (APP 5)

- [ ] A notice at every collection point, checked against the actual forms in the codebase
- [ ] Each notice carries the APP 5.2 matters other than (g) and (h)
- [ ] Consequences of non-provision stated concretely
- [ ] Third-party collection notified, including list purchases and enrichment
- [ ] Notice appears before the submit control
- [ ] Marketing consent is a separate, unticked control

## Tracking

- [ ] No consent banner on an Australian-only site without a documented reason
- [ ] Where a banner exists, nothing fires before the decision and reject is as easy as accept
- [ ] Every vendor classified as personal information / not, use / disclosure, with country
- [ ] Analytics retention shortened from the default
- [ ] Session replay masks input and is off on payment, health and identity pages

## Data breach

- [ ] Response plan exists and names individuals with out-of-hours contacts
- [ ] Awareness timestamp captured automatically so the 30-day s 26WH(2) clock is provable
- [ ] Statement template ready with all four s 26WK matters
- [ ] Contractual and sector notification deadlines checked — several are shorter than the Act
- [ ] No "72 hours" anywhere in the documentation

## Consumer guarantees and returns

- [ ] No "no refunds", "store credit only", "final sale", "original packaging required" applied to faulty goods, anywhere including physical signage
- [ ] Consumer guarantee rights stated before the voluntary change-of-mind policy
- [ ] Change-of-mind policy labelled voluntary
- [ ] For a major failure the consumer chooses the remedy, and the text says so
- [ ] No stated expiry on the guarantees
- [ ] Customers not redirected to the manufacturer
- [ ] Any warranty against defects carries the reg 90 mandatory text verbatim in the correct version, plus name, address, phone, email, claim procedure, expenses, period, and the "in addition to other rights" statement
- [ ] No cooling-off period asserted for online purchases; the 10 business day period (ACL ss 76, 82) claimed only for genuine unsolicited consumer agreements

## Pricing and claims

- [ ] Every consumer price a GST-inclusive single figure at least as prominent as any component (ACL s 48)
- [ ] Mandatory fees inside the headline price
- [ ] Delivery charges disclosed before commitment
- [ ] "Was/now" and "RRP" claims backed by retained price history
- [ ] No permanent sale, no resetting countdown timers, no fabricated stock scarcity
- [ ] Testimonials genuine; review solicitation and moderation practices disclosed
- [ ] Paid, affiliate and influencer content disclosed clearly in the same medium
- [ ] Environmental, origin and health claims substantiated before publication
- [ ] Subscription sign-up, reminder and cancellation flows audited against the 1 July 2027 unfair trading practices regime

## Terms of service

- [ ] Acceptance is affirmative and unticked, with version and timestamp stored
- [ ] Explicit statement that the consumer guarantees are not excluded, placed before the liability cap (ACL s 64)
- [ ] Section 64A limitation used only for genuinely non-consumer-grade supplies
- [ ] Whole document reviewed against the unfair contract terms criteria (ACL ss 23–28, penalty-backed since 9 November 2023), with unilateral variation, auto-renewal, termination and indemnity clauses examined
- [ ] Small business counterparties considered, not only consumers
- [ ] Governing law and forum an Australian state or territory, named
- [ ] No mandatory arbitration or class action waiver against consumers
- [ ] No link to the EU ODR platform anywhere in the project
- [ ] Cancellation no harder than signup

## Marketing

- [ ] Every address traceable to a consent record or a defensible inference (Spam Act s 16)
- [ ] No purchased, rented, scraped or appended lists
- [ ] Consent control unticked, unbundled, not a condition of purchase
- [ ] Consent scope matches what is actually sent
- [ ] Sender identification carries legal entity, ABN and a contact route valid for 30 days (s 17)
- [ ] Unsubscribe is one click, requires no login or extra data, works for at least 30 days, and propagates to every system within 5 business days (s 18)
- [ ] Transactional messages carry no promotional content
- [ ] Telemarketing lists washed against the Do Not Call Register

## Business identification

- [ ] Legal entity name taken from ASIC or ABN Lookup, not from memory
- [ ] ABN present; ACN present for companies
- [ ] Registered business name current and linked to the correct ABN
- [ ] Contracting entity in the terms is the entity that issues invoices
- [ ] Company name and ACN or ABN on the first page of invoices, receipts and order confirmations (Corporations Act s 153)
- [ ] Address is a real geographic or deliberately chosen service address
- [ ] Licence numbers and regulators shown where the trade is licensed
- [ ] No imported Impressum or EU-style legal notice page

## Online safety

- [ ] Service category assessed and recorded
- [ ] Part 4A social media minimum age applicability assessed and documented (obligation live since 10 December 2025)
- [ ] Any age assurance data covered by an APP 5 notice, minimised, not retained
- [ ] Reporting route visible from the content
- [ ] Named monitored contact for eSafety and law enforcement
- [ ] Moderation rules specific, decisions logged
- [ ] No EU Digital Services Act machinery in Australian-facing terms

## Accessibility

- [ ] Conformance target agreed in writing, with version and level
- [ ] Claimed conformance level true — overstating it is an ACL s 18 problem
- [ ] Keyboard-only pass over signup and checkout
- [ ] Screen reader pass over the primary transaction flow
- [ ] Contrast measured
- [ ] Known limitations published with remediation dates
- [ ] Monitored accessibility contact route
- [ ] No EU accessibility statement wording or European Accessibility Act reference

## Housekeeping

- [ ] Image, font and content licences documented
- [ ] Third-party trade marks used only with authority
- [ ] Every `[[…]]` placeholder resolved or reported as `[[MISSING: …]]`
- [ ] Draft marker still present in every text that has not had legal sign-off

## Finding format

Report findings as a table, most severe first:

| Severity | Location | Provision | Finding | Fix |
|---|---|---|---|---|
| critical / high / medium | file:line or URL | e.g. ACL s 48 | what is missing or wrong | the concrete step |

**Critical** means penalty exposure, unenforceability, or a representation that is false on its face. That includes: "no refunds" wording, a warranty against defects without the reg 90 text, a price that excludes mandatory fees, marketing without a consent record, an unsubscribe that does not work, and a privacy policy claiming Privacy Act compliance for an entity that is not covered.
