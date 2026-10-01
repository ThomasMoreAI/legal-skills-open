# Accessibility — BFSG and BFSGV

Status as at 05.08.2026. The **BFSG** (Barrierefreiheitsstärkungsgesetz) transposes Directive (EU) 2019/882. Its requirements apply to products placed on the market and to services provided to consumers **since 28.06.2025**. The technical detail sits in the **BFSGV** (Verordnung über die Barrierefreiheitsanforderungen für Produkte und Dienstleistungen nach dem Barrierefreiheitsstärkungsgesetz).

Do not call the required text an "Erklärung zur Barrierefreiheit". That is public-sector vocabulary from § 12b BGG and the BITV 2.0, with a different content catalogue and a different feedback mechanism. Private business owes the information under **§ 14 Abs 1 Nr 2 BFSG in conjunction with Anlage 3 Nr 1 BFSG**.

## Who is covered

Services in scope include, among others, e-commerce services, consumer banking services, e-book services, telecommunications services, and elements of passenger transport services. **Dienstleistungen im elektronischen Geschäftsverkehr** — a webshop, an online booking flow, an app selling to consumers — are the common case.

**§ 3 Abs 3 BFSG:** the accessibility requirement of § 3 Abs 1 BFSG does **not** apply to Kleinstunternehmen that offer or provide services. A Kleinstunternehmen employs fewer than 10 persons and has either an annual turnover of at most 2 million euro or an annual balance sheet total of at most 2 million euro.

Three traps in that exemption:

- It covers **services only**. A micro-enterprise that manufactures, imports or distributes a covered **product** is not exempt.
- It is a snapshot that has to be documented. Crossing the threshold ends the exemption; there is no grandfathering.
- Pure B2B offerings are outside the scope from the start, but a shop that also sells to consumers is inside it.

**§ 15 BFSG:** the Bundesfachstelle Barrierefreiheit advises Kleinstunternehmen on the BFSG free of charge.

## § 14 BFSG — duties of the service provider

**Abs 1:** the provider may only offer or provide the service where

1. the service meets the accessibility requirements of the regulation issued under § 3 Abs 2 BFSG, and
2. the provider has prepared the information under **Anlage 3 Nummer 1** and made it publicly accessible in an accessible form.

**Abs 2:** the information must be kept for as long as the service is offered or provided.

**Abs 3:** the provider must ensure the requirements are met continuously and take account of changes in the way the service is provided, changes to the requirements, and changes to the harmonised standards or technical specifications referred to.

**Abs 4:** on non-conformity the provider must take corrective measures and inform the market surveillance authority without undue delay, with detail on the nature of the non-conformity and the measures taken.

**Abs 5:** the provider must supply the market surveillance authority, on reasoned request, with all information needed to demonstrate conformity, and cooperate with measures taken.

## Anlage 3 Nr 1 BFSG — what the published text must contain

- a general description of the service in an accessible format
- descriptions and explanations necessary to understand how the service works
- a description of how the service meets the applicable accessibility requirements of the regulation under § 3 Abs 2 BFSG
- the identification of the competent market surveillance authority

## Technical requirements — BFSGV

- **§ 3 BFSGV:** the state of the art applies; the Bundesfachstelle Barrierefreiheit publishes the relevant standards and compliance tables.
- **§ 12 BFSGV:** general requirements for services.
- **§ 19 BFSGV:** additional requirements for **Dienstleistungen im elektronischen Geschäftsverkehr** — the relevant section for a webshop.
- **§ 20, § 21 BFSGV:** functional performance criteria, applicable where no standard covers a case.

In practice the reference standard is EN 301 549, which maps onto WCAG 2.1 level AA for web content. Conformance with a harmonised standard published in the Official Journal produces a presumption of conformity; departing from it means proving equivalence.

## Market surveillance

Market surveillance for services is carried out by the Länder through the **Marktüberwachungsstelle der Länder für die Barrierefreiheit von Produkten und Dienstleistungen (MLBF)**, based in Magdeburg. It acts ex officio and on complaints from consumers and associations. The BFSG contains Bußgeld provisions and, ultimately, the power to prohibit provision of the service.

## Template

```html
<!-- ENTWURF – juristisch nicht freigegeben -->
<h1>Informationen zur Barrierefreiheit</h1>
<p>Informationen gemäß § 14 Abs. 1 Nr. 2 BFSG in Verbindung mit Anlage 3 Nr. 1 BFSG.</p>

<h2>Beschreibung der Dienstleistung</h2>
<p>[[general description of the service in plain, accessible language]]</p>

<h2>Funktionsweise</h2>
<p>[[explanations needed to understand how the service works: ordering process,
   payment, account, support channels]]</p>

<h2>Erfüllung der Barrierefreiheitsanforderungen</h2>
<p>Die Dienstleistung erfüllt die Anforderungen der §§ 12 und 19 BFSGV.
   Angewandter Standard: [[EN 301 549 / WCAG 2.1 AA, with version]].
   Stand der Prüfung: [[date]]. Prüfverfahren: [[self-assessment / external audit,
   with the tested flows]].</p>
<p>Bekannte Einschränkungen: [[list, or: keine bekannt]].
   Geplante Behebung: [[date or measure]].</p>

<h2>Barriere melden</h2>
<p>Wenn Ihnen eine Barriere auffällt: [[e-mail]] · [[telephone]]. Wir antworten
   innerhalb von [[period]].</p>

<h2>Zuständige Marktüberwachungsbehörde</h2>
<p>Marktüberwachungsstelle der Länder für die Barrierefreiheit von Produkten und
   Dienstleistungen (MLBF), [[current address and website — verify before publishing]]</p>
```

## Checkpoints

- [ ] Scope decided: is the offering a service in electronic commerce to consumers
- [ ] Kleinstunternehmen status checked against both criteria and documented with the reference date
- [ ] Product side checked separately — the micro-enterprise exemption does not cover products
- [ ] § 14 Abs 1 Nr 2 BFSG information published, in an accessible form, permanently reachable
- [ ] All four Anlage 3 Nr 1 items present, including the market surveillance authority
- [ ] Named standard and version, with the date and method of the assessment
- [ ] Known limitations disclosed honestly rather than omitted
- [ ] Keyboard-only pass through the main flows, focus visible at every step
- [ ] Contrast measured, not estimated
- [ ] Form fields have associated labels, errors reported as text, not colour alone
- [ ] Screen reader pass through the order or sign-up flow
- [ ] Information retained for as long as the service is offered (§ 14 Abs 2 BFSG)
- [ ] Text not labelled "Erklärung zur Barrierefreiheit" and not built from a BITV 2.0 public-sector template
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
