# Pre-launch checklist

Run before go-live. Every finding is reported with the article and the location, not as a general remark. Findings that are technically verifiable are verified technically, not judged from intent.

## Technical pass first

Four steps, a few minutes together, and they produce half the findings:

1. Load the site in a fresh browser profile with the network tab recording. Note every third-party domain contacted **before** any cookie decision.
2. Application tab: record every cookie, localStorage and IndexedDB entry present before the decision.
3. Full-text search the whole project — including shop system texts, PDF terms and email templates — for: `odr`, `Streitbeilegungsplattform`, `Online-Streitbeilegung`, `TMG`, `DDG`, `RStV`, `BDSG`, `Widerrufsrecht`, `Widerrufsbelehrung`, `Rücktrittsrecht`, `FAGG`, `ECG`, `Amtsgericht`, `Landgericht`, `Handelsregister HRB`, `USt-IdNr`, `DSGVO Art. 6 Abs. 1`.
4. Walk the order flow once with the keyboard only, no mouse.

## Impressum

- [ ] Reachable from every page, no login, no consent dialog in front of it
- [ ] Full registered Firma or full personal name (Art. 3 Abs. 1 lit. s Ziff. 1 UWG, Art. 954a OR)
- [ ] Geographic address, not a PO box
- [ ] Email address present as a mailto link
- [ ] Legal form, Sitz, Handelsregisteramt, UID for registered entities
- [ ] MWST number present or expressly marked not applicable (Art. 26 Abs. 2 lit. a MWSTG for invoices)
- [ ] Sector-specific supervisory disclosure checked against the actual sector act
- [ ] Present in every language of address
- [ ] No § 5 TMG, § 5 DDG, § 5 ECG, MedienG, Offenlegung or Blattlinie wording

## Data protection

- [ ] Datenschutzerklärung reachable without consent and without login
- [ ] Controller identity and contact (Art. 19 Abs. 2 lit. a DSG)
- [ ] Purpose per processing (lit. b)
- [ ] Recipients or categories named (lit. c), reconciled against the network trace
- [ ] Each transfer abroad: state named plus the Art. 16 Abs. 2 safeguard or the Art. 17 exception (Art. 19 Abs. 4 DSG)
- [ ] Retention per category or the criteria for it
- [ ] Express consent where Art. 6 Abs. 7 DSG requires it
- [ ] Automated individual decisions addressed or expressly excluded (Art. 21 DSG)
- [ ] Rights stated with Swiss articles; GDPR articles only where the GDPR also applies
- [ ] EDÖB named with the correct address
- [ ] Art. 14 DSG representative assessed against all four cumulative conditions
- [ ] Art. 27 GDPR representative appointed where Art. 3(2) GDPR applies
- [ ] Register of processing kept, or the Art. 24 DSV exemption documented with headcount and both carve-outs
- [ ] Processor contracts in place (Art. 9 DSG); sub-processor approvals recorded
- [ ] DSFA where Art. 22 Abs. 2 DSG is met, filed under Art. 14 DSV
- [ ] Breach process names the assessor, the notifier and the channel (databreach.edoeb.admin.ch)

## Cookies and tracking

- [ ] No non-essential cookie or tracking request fires before the user can refuse
- [ ] Refusal option on the first banner level, reachable in a few clicks on later visits
- [ ] Purposes named per category, cookie table verified against the technical trace
- [ ] Withdrawal path shown prominently after consent
- [ ] Third-party fonts, maps, video and captcha self-hosted or behind the refusal mechanism
- [ ] EU-facing visitors get a GDPR-grade consent banner with logging, if the site targets the EU

## Shop and contract

- [ ] Binding-offer position resolved against Art. 7 Abs. 3 OR
- [ ] Technical steps to contract described (Art. 3 Abs. 1 lit. s Ziff. 2 UWG)
- [ ] Input-error correction available before the order (Ziff. 3)
- [ ] Immediate electronic order acknowledgement sent (Ziff. 4), and it says whether it is an acceptance
- [ ] AGB presented before ordering and saveable
- [ ] Unusual clauses highlighted separately
- [ ] Consumer AGB reviewed against Art. 8 UWG
- [ ] No pre-ticked add-ons
- [ ] Geoblocking behaviour checked against Art. 3a UWG for customers in Switzerland
- [ ] No Swiss "Bestellbutton" duty asserted

## Warranty and returns

- [ ] No statutory withdrawal right asserted for online orders
- [ ] Any return policy labelled voluntary, with its own conditions
- [ ] Telephone sales, if any, carry a separate Art. 40d OR notice and the CHF 100 threshold is checked
- [ ] Art. 201 OR notification duty stated
- [ ] Limitation period correct, with the used-goods distinction (Art. 210 Abs. 1, 4 OR)
- [ ] Any Art. 199 OR exclusion explicit and checked against Art. 8 UWG
- [ ] No shortening below two years for new consumer goods
- [ ] Garantie and Gewährleistung kept linguistically separate

## Prices

- [ ] Every consumer-facing price is the actual price payable in CHF including VAT (Art. 3 Abs. 1 PBV)
- [ ] Non-optional surcharges inside the price; only shipping shown separately (Art. 4 Abs. 1 PBV)
- [ ] Sales unit unambiguous (Art. 9 PBV); unit prices where Art. 16a UWG applies
- [ ] Advertising prices are actual prices payable (Art. 13 Abs. 1 PBV)
- [ ] Every comparison price satisfies Art. 16 Abs. 1 PBV, with evidence retained
- [ ] Display duration of comparison prices within Art. 16 Abs. 3 PBV
- [ ] Post-purchase rebates disclosed separately and quantified (Art. 4 Abs. 2 PBV)
- [ ] No EU "lowest price of the last 30 days" wording

## Marketing

- [ ] Newsletter consent separate, not pre-ticked, naming sender and content
- [ ] Consent evidence stored with timestamp, IP, wording version, confirmation event
- [ ] Correct sender and free one-click unsubscribe in every mailing
- [ ] Existing-customer route satisfies all four elements of Art. 3 Abs. 1 lit. o UWG
- [ ] Telephone campaigns screened against directory markers; unlisted numbers excluded (lit. u)
- [ ] Advertising calls display a directory-registered number the caller may use (lit. v)
- [ ] Climate and environmental claims substantiated objectively and verifiably (lit. x)
- [ ] Competition mechanics checked against lit. t

## Accessibility

- [ ] Operator classified as authority, concession holder or private provider
- [ ] Art. 10 BehiV applied where it binds; eCH-0059 3.0 used as the standard
- [ ] No claim that Swiss law mandates WCAG for a private shop
- [ ] EAA conformity planned for the EU-facing offering, or microenterprise exemption documented
- [ ] Keyboard walkthrough passed, focus visible, contrasts measured, labels associated

## Platform and dispute resolution

- [ ] No DSA-derived obligations asserted for a Swiss-only service
- [ ] Moderation rules in the AGB, with reporting route, notice and appeal
- [ ] Marketplace VAT position checked against Art. 20a MWSTG
- [ ] Dispute clause references Art. 197 ZPO conciliation, not a non-existent ADR body
- [ ] Consumer jurisdiction under Art. 32 ZPO not contracted away
- [ ] No ODR link and no mention of the EU dispute resolution platform, project-wide

## Cross-border

- [ ] EU targeting decided explicitly, with the evidence recorded
- [ ] 14-day withdrawal right granted to EU consumers where targeted, with model form
- [ ] Choice of Swiss law does not purport to strip EU mandatory consumer protection (Art. 6(2) Rome I)
- [ ] Jurisdiction clause checked against the Lugano Convention
- [ ] EU responsible person under Art. 16 GPSR named on the offer where products are shipped to the EU

## Closing

- [ ] Image and font licences documented
- [ ] Third-party trade marks and logos used only with authorisation
- [ ] No German or Austrian provisions and no foreign authorities in the text
- [ ] All `[[…]]` placeholders resolved or expressly reported as open
- [ ] Draft marker still present while legal sign-off is outstanding

## Result format

Report findings as a table, most severe first:

| Severity | Location | Norm | Finding | Fix |
|---|---|---|---|---|
| critical / high / medium | file:line or URL | article | what is missing or wrong | concrete step |

**Critical** means criminal exposure, an actionable unfair-competition claim, or invalidity of the contract term. That includes a missing Impressum (Art. 3 Abs. 1 lit. s, Art. 23 UWG), prices excluding VAT (Art. 24 UWG), an asserted statutory withdrawal right that does not exist, an unlawful transfer abroad (Art. 61 lit. a DSG), and mass advertising without consent (Art. 3 Abs. 1 lit. o UWG).
