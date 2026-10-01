# Accessibility

Switzerland has no European Accessibility Act. Digital accessibility is mandatory for authorities and concession holders; private providers owe only a non-discrimination duty with a capped remedy. A Swiss shop selling into the EU is nevertheless caught by the EAA. Wording from BehiG Stand am 1. Juli 2020 and BehiV Stand am 1. Januar 2021. Status as at 2026-08-05.

## Scope of the BehiG — Art. 3

The Behindertengleichstellungsgesetz (SR 151.3) applies to publicly accessible buildings and installations, public transport facilities and vehicles, residential buildings with more than eight units and buildings with more than 50 workplaces (in each case where a building permit is granted after entry into force), to education and training, to federal employment relationships, and under lit. e to:

> e. grundsätzlich von jedermann beanspruchbare Dienstleistungen Privater, der Unternehmen mit einer Infrastrukturkonzession nach Artikel 5 des Eisenbahngesetzes vom 20. Dezember 1957 oder einer Personenbeförderungskonzession nach Artikel 6 des Personenbeförderungsgesetzes vom 20. März 2009, weiterer konzessionierter Unternehmen und des Gemeinwesens;

## Private providers — Art. 6 and Art. 11 BehiG

> Art. 6 BehiG: Private, die Dienstleistungen öffentlich anbieten, dürfen Behinderte nicht auf Grund ihrer Behinderung diskriminieren.

This is a prohibition of discrimination, not a positive duty to build an accessible website. The remedy is limited: Art. 11 Abs. 2 BehiG caps compensation under Art. 8 Abs. 3 BehiG at **CHF 5,000**, taking account of the circumstances, the severity of the discrimination and the value of the service. Art. 11 Abs. 1 BehiG additionally bars an order to remove a disadvantage where the expected benefit is disproportionate to the economic burden.

There is therefore **no Swiss legal requirement for a private webshop to conform to WCAG**. Say so plainly, and say the rest of it too: the cap does not bar an Art. 8 Abs. 1 BehiG claim to desist from discrimination, litigation under the BehiG is free of court costs (Art. 113 Abs. 2 lit. b ZPO), disability organisations have standing under Art. 9 BehiG and Art. 5 BehiV, and an inaccessible checkout is a business problem independent of the statute.

## Web accessibility for authorities — Art. 14 Abs. 2 BehiG, Art. 10 BehiV

> Art. 14 Abs. 2 BehiG: Soweit sie ihre Dienstleistungen auf Internet anbieten, müssen diese Sehbehinderten ohne erschwerende Bedingungen zugänglich sein. Der Bundesrat erlässt die nötigen technischen Vorschriften. Er kann technische Normen privater Organisationen für verbindlich erklären.

The addressees of Art. 14 BehiG are **die Behörden** — authorities. Art. 10 Abs. 1 BehiV extends the technical requirement to information, communication and transaction services on the internet and to people with speech, hearing, visual and motor disabilities, and requires internet offerings to be set up in accordance with international IT standards, in particular the W3C guidelines on web accessibility, and subsidiarily national IT standards. Art. 10 Abs. 2 BehiV assigns the task of issuing the necessary directives to the Federal Chancellery's digital transformation and ICT steering unit for the federal administration units, and to the responsible bodies of the other units, organisations and federally licensed undertakings for their own fields. Abs. 3 requires the directives to be developed with disability organisations and IT specialists and kept current.

## eCH-0059

eCH-0059 is the Swiss e-government accessibility standard. The current version is **3.0, approved 25 June 2020**, replacing version 2.0 of 2011; it is based on WCAG 2.1. It binds public bodies and concession holders through the directives issued under Art. 10 Abs. 2 BehiV rather than of its own force, and is the natural reference point for any project performing a public task. For private projects it is a good target, not a duty.

## Pending legislation

A partial revision of the BehiG (Botschaft of December 2024) and an Inklusionsgesetz as indirect counter-proposal to the Inklusions-Initiative (Botschaft of 25 February 2026) are before Parliament, both addressing work and services. Nothing from either package is in force as at 2026-08-05. `[[UNVERIFIED: whether the pending BehiG revision or the Inklusionsgesetz would impose digital accessibility duties on private providers, and on what timetable — check the current parliamentary dossier before advising a client that private-sector duties are imminent]]`

## What a private provider is actually exposed to

The Art. 6 BehiG duty is enforced through Art. 8 BehiG. Art. 8 Abs. 3 BehiG gives a person discriminated against by a private provider a claim for compensation, capped by Art. 11 Abs. 2 BehiG at CHF 5,000. Art. 9 BehiG and Art. 5 BehiV give standing to disability organisations of national importance that have existed for at least ten years, which is how such cases usually reach a court. Art. 113 Abs. 2 lit. b ZPO means no court costs are awarded in BehiG proceedings, so the cost barrier to bringing a claim is low even though the award is small.

The exposure is therefore reputational and injunctive rather than financial. Treat an inaccessible checkout as a commercial defect and, where the client is public-facing, quantify it that way rather than arguing about whether WCAG is legally binding.

## The EAA trap for EU-facing shops

Directive (EU) 2019/882 (European Accessibility Act) applies from **28 June 2025** (Art. 31(2)). It covers, among other things, e-commerce services — the websites and mobile applications through which consumer contracts are concluded. It binds economic operators placing products on or providing services in the EU market, irrespective of where they are established. A Swiss shop that ships to the EU and addresses EU consumers therefore has to make the EU-facing offering conform to the accessibility requirements of the Member State implementations.

Art. 4(5) EAA exempts **microenterprises providing services** from the accessibility requirements; a microenterprise employs fewer than 10 persons and has an annual turnover not exceeding EUR 2 million or an annual balance sheet total not exceeding EUR 2 million (Art. 3(23) EAA). The exemption does not extend to products. Art. 32(1) EAA provides a transitional period ending 28 June 2030 for services provided using products lawfully used before that date, and lets service contracts agreed before 28 June 2025 continue unchanged until expiry, but no longer than five years from that date.

In practice the EAA is what forces accessibility on Swiss e-commerce, not Swiss law. Build to WCAG 2.1 AA and the question resolves itself in both jurisdictions.

## Template

Only publish an accessibility statement where a duty exists or where the project chooses to commit. An empty statement is a misleading statement.

```html
<!-- ENTWURF – juristisch nicht freigegeben -->
<h1>Erklärung zur Barrierefreiheit</h1>
<p>Diese Website wird von [[Stelle]] betrieben. Wir orientieren uns an
[[eCH-0059 Version 3.0 / WCAG 2.1 Stufe AA]].</p>
<h2>Stand der Übereinstimmung</h2>
<p>[[vollständig / teilweise konform – mit Auflistung der bekannten Ausnahmen]]</p>
<h2>Nicht barrierefreie Inhalte</h2>
<ul><li>[[Bereich, Grund, geplante Behebung, Datum]]</li></ul>
<h2>Rückmeldungen</h2>
<p>Melden Sie Barrieren an [[E-Mail]]. Wir antworten innert [[Frist]].</p>
<h2>Erstellung dieser Erklärung</h2>
<p>Diese Erklärung wurde am [[Datum]] erstellt, gestützt auf
[[Selbstbewertung / externe Prüfung durch …]].</p>
```

## Checkpoints

- [ ] Determined whether the operator is an authority, a concession holder, or a private provider
- [ ] For authorities and concession holders: Art. 10 BehiV applied, and the applicable directive identified
- [ ] For private providers: no claim made that Swiss law mandates WCAG
- [ ] EU customers assessed; if served, EAA conformity of the EU-facing offering planned
- [ ] Microenterprise status under Art. 3(23) EAA documented if the Art. 4(5) exemption is relied on
- [ ] Keyboard walkthrough of the main flows completed, focus visible
- [ ] Contrast measured, not estimated
- [ ] Form fields have associated labels and textual error messages
- [ ] Screen reader test of the order or sign-up flow performed
- [ ] Any published accessibility statement is accurate about what is and is not conformant
