# Pre-launch checklist

Run before go-live. Every finding is reported with its norm and its location, not as a general remark. Anything technically checkable is checked technically, not judged by intention.

## Technical pass first

These four steps produce half the findings in a few minutes:

1. Load the site in a fresh profile with the network tab recording. List every third-party domain contacted **before** a consent decision.
2. Application tab: capture every cookie, LocalStorage and IndexedDB entry written before the decision.
3. Full-text search across the whole project — including shop-system strings, PDF terms and transactional email templates — for: `odr`, `consumers/odr`, `piattaforma europea`, `TMG`, `DDG`, `BDSG`, `Widerruf`, `Impressum`, `Amtsgericht`, `denuncia entro due mesi`, `sei mesi`, `art. 16 D.Lgs 70/2003`, `art. 17 D.Lgs 70/2003`.
4. Walk the whole order flow with the keyboard only, no mouse.

## Site identification

- [ ] Reachable from every page, without login and without passing the cookie banner
- [ ] Name or denominazione, sede legale, email and a second rapid contact channel (art. 7 lett. a, b, c D.Lgs 70/2003)
- [ ] REA number or registro delle imprese registration (art. 7 lett. d) — owed by ditte individuali too
- [ ] Supervisory authority and authorisation details where the activity is licensed (art. 7 lett. e)
- [ ] Regulated profession: ordine, registration number, title, conferring state, applicable rules with access (art. 7 lett. f)
- [ ] Partita IVA present (art. 7 lett. g) **and rendered on the home page** (art. 35 comma 1 DPR 633/1972)
- [ ] Prices clear as to taxes, delivery and additional elements (art. 7 lett. h)
- [ ] For S.p.A., S.a.p.a. and S.r.l. only: sede, registro delle imprese office and number, capitale versato, socio unico, stato di liquidazione (art. 2250 comma 7 c.c.)
- [ ] Those items **not** asserted as obligatory for s.n.c., s.a.s. or ditta individuale
- [ ] PEC registered in INI-PEC; administrator's PEC registered and different from the company's (art. 5 comma 1 D.L. 179/2012)
- [ ] SCIA filed with the comune's SUAP for online retail of goods (art. 68 comma 1 D.Lgs 59/2010), date and protocol on file

## Privacy

- [ ] Informativa reachable without consent and without login
- [ ] Every processing carries purpose, legal basis, recipients, retention
- [ ] No consent claimed where contract or legal obligation applies
- [ ] Legitimate interests named concretely
- [ ] Every service that actually loads appears in the notice — reconciled against the network capture
- [ ] Transfers outside the EEA listed individually with the safeguard
- [ ] Garante named as supervisory authority, Piazza Venezia n. 11, 00187 Roma
- [ ] Age of **14** used, not 16 (art. 2-quinquies Codice Privacy)
- [ ] Under-14 audience: parental consent mechanism built, notice drafted in language a minor can understand
- [ ] Registro delle attività di trattamento exists and matches the live services
- [ ] Art 28 GDPR agreement with every processor, signed before processing began
- [ ] Written designations under art. 2-quaterdecies for staff who process data
- [ ] DPO requirement assessed; if appointed, contact details filed through `servizi.gpdp.it/comunicazionerpd/s/` — the only accepted channel
- [ ] Breach procedure documented; internal breach register exists including non-notified breaches
- [ ] Every monitoring-capable IT tool classified under art. 4 comma 1 or comma 2 L. 300/1970
- [ ] Accordo sindacale or Ispettorato nazionale del lavoro authorisation obtained where comma 1 applies
- [ ] Comma 3 notice issued to workers covering how checks are carried out
- [ ] Email metadata retention set against provvedimento n. 364 del 6 giugno 2024 — the orientation is 21 days, the withdrawn draft said 7

## Cookies and trackers

- [ ] No non-technical request fires and no non-technical storage is written before a choice
- [ ] X inside the banner, top right, with graphic prominence equal to the accept command
- [ ] Closing with the X fires nothing and forces no navigation elsewhere
- [ ] First layer carries all five items of §7.2 of the linee guida
- [ ] All granular options preset to refusal; opt-in only on first access
- [ ] No cookie wall, or a genuinely equivalent no-consent alternative
- [ ] Banner not re-presented for at least six months after a recorded choice
- [ ] Consent and refusal both logged with timestamp and banner version
- [ ] Preference panel permanently reachable from the footer
- [ ] Technical-cookie-only site: no banner shown at all
- [ ] Analytics: fourth IPv4 octet masked, aggregate use only, no onward transmission
- [ ] Fingerprinting and passive identifiers treated as consent-requiring
- [ ] Third-party fonts local or behind consent; maps, video, captcha behind consent or click-to-load
- [ ] Email tracking pixels: separate consent and granular opt-out — provvedimento n. 284 del 17 aprile 2026, deadline **29 October 2026**

## Selling to consumers

- [ ] Which cut-over version is delivered is stated: current, or from 27.09.2026 (D.Lgs 30/2026)
- [ ] Order button reads *ordine con obbligo di pagare* or an unambiguous equivalent, and **nothing else** (art. 51 comma 2)
- [ ] Order summary immediately above the button carries art. 49 comma 1 lett. a), e), q), r)
- [ ] Delivery restrictions and payment means shown at the latest at the start of the ordering process (art. 51 comma 3)
- [ ] Total price including tax; delivery costs separate and shown before the order
- [ ] Concrete delivery period
- [ ] Input-error correction mechanism present (art. 12 D.Lgs 70/2003)
- [ ] Confirmation on a durable medium at the latest at delivery (art. 51 comma 7)
- [ ] No pre-ticked add-ons
- [ ] Reminder of the garanzia legale present — art. 49 comma 1 **lett. n)**, not lett. l)
- [ ] Price reduction claims backed by a 30-day lowest-price history per SKU (art. 17-bis comma 2)
- [ ] Reviews: verification statement present per art. 22 comma 5-bis, or reviews removed
- [ ] Marketplace: art. 49-bis items a) to d) published

## Withdrawal

- [ ] Online withdrawal function built, labelled *recedere dal contratto qui* (art. 54-bis comma 3) — mandatory for contracts concluded from 19 June 2026
- [ ] Confirmation control labelled *conferma recesso* (art. 54-bis comma 5)
- [ ] Function available throughout the withdrawal period, prominent, reachable without login
- [ ] Acknowledgment on a durable medium carrying content, date and time of transmission (art. 54-bis comma 6)
- [ ] Its existence and location stated in the pre-contractual information (art. 49 comma 1 lett. h)
- [ ] Term *recesso* used throughout; no *Widerruf*
- [ ] Modulo tipo from Allegato I parte B provided verbatim, downloadable and storable
- [ ] Period start matches the contract type (art. 52 comma 2); 30 days where art. 52 comma 1-bis applies
- [ ] Refund within 14 days including standard delivery costs; no clause limiting it
- [ ] Return cost allocation stated
- [ ] Exclusions cited by letter of art. 59, with no invented restrictions
- [ ] Digital content with immediate access: two separate unticked confirmations, timestamped (art. 59 comma 1 lett. o)

## Guarantee

- [ ] Two years stated for new goods (art. 133 comma 1)
- [ ] Burden-of-proof reversal stated as **one year** (art. 135 comma 1), not six months
- [ ] No *denuncia entro due mesi* anywhere — abolished by D.Lgs 170/2021
- [ ] Twenty-six month prescription stated and distinguished from the two-year liability period
- [ ] Remedy hierarchy correct; no general exclusion of termination
- [ ] No clause excluding or limiting the guarantee before notification — null under art. 135-sexies
- [ ] Goods with digital elements: update period stated (art. 130 comma 2)
- [ ] Free digital service paid with personal data: treated as inside the regime (art. 135-octies comma 4)
- [ ] Commercial guarantee, if offered, carries all five items of art. 135-quinquies comma 2, in Italian, in characters no less prominent than any other language
- [ ] Any paid extended warranty states the free legal guarantee with at least equal prominence

## Marketing

- [ ] Marketing, profiling and third-party communication each have their own unticked consent
- [ ] Third-party consent granular by category and recipient
- [ ] Double opt-in active; confirmation email free of advertising
- [ ] Consent record complete per subscriber, including the consent text version
- [ ] Soft spam, if relied on: email only, own similar services, address from an actual sale, notice at collection **and** in every message (art. 130 comma 4)
- [ ] One-click unsubscribe in every message, applied across all tools
- [ ] Sender identity not concealed; rights-contact address present (art. 130 comma 5)
- [ ] Commercial communications identifiable as such from the first transmission (art. 8 D.Lgs 70/2003)
- [ ] Telephone campaigns: RPO checked monthly and immediately before the campaign
- [ ] RPO registration treated as revoking earlier telephone consents

## Influencer and advertising

- [ ] Disclosure as the first item of information, within the first three hashtags where hashtags are used
- [ ] Wording taken from the Digital Chart edition of 30 ottobre 2024
- [ ] Gifted products and affiliate links disclosed in their own form
- [ ] Follower and view figures recorded for each collaborator, so the AGCOM threshold question is answered on evidence
- [ ] Relevant influencers: registration status confirmed
- [ ] Disclosure duty, wording, placement and an audit right written into the contract

## Accessibility

- [ ] Legge Stanca assessed: three-year average turnover above EUR 500 million?
- [ ] EAA assessed: is the service *commercio elettronico* or another covered category?
- [ ] Microenterprise exemption, if claimed, documented and not applied to a product
- [ ] Declaration generated through `form.agid.gov.it` where Regime 1 applies, reviewed by 23 September
- [ ] Keyboard-only pass through checkout succeeded, focus visible
- [ ] Contrast measured; form labels associated; error messages textual
- [ ] Conformity level claimed matches what was actually tested

## Platform

- [ ] DSA category determined and recorded
- [ ] Contact point published and monitored; legal representative appointed if not EU-established
- [ ] Notice and action mechanism reachable without an account
- [ ] Statement of reasons produced for every restriction, naming the specific ground
- [ ] Moderation rules disclosed in the terms in the form actually applied
- [ ] No citation of artt. 14-17 D.Lgs 70/2003 anywhere — abrogated 2 May 2024

## Dispute resolution and residual

- [ ] Project-wide search returns no ODR reference or link
- [ ] ADR position stated honestly: a named body on a competent authority's register, or none
- [ ] No exclusive forum clause at the trader's seat in B2C terms
- [ ] Image and font licences documented
- [ ] No German norms and no German authorities anywhere in the text
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
- [ ] Draft marker still present, since no lawyer has signed off

## Output format

Report findings as a table, most serious first:

| Severity | Location | Norm | Finding | Fix |
|---|---|---|---|---|
| critical / high / medium | file:line or URL | article | what is missing or wrong | the concrete step |

**Critical** means the contract does not bind, an administrative sanction is likely, or an AGCM or Garante proceeding is realistic. That covers: tracking before consent, an order button not carrying the payment wording, a missing online withdrawal function on a shop launched after 19 June 2026, a missing partita IVA on the home page, and a legal guarantee stated as one year or subject to a two-month notification.
