# Accessibility

Two regimes stack. They have different triggers, different scope and different authorities. Deciding that one does not apply says nothing about the other.

## Regime 1 — Legge Stanca

**Legge 9 gennaio 2004 n. 4** (*Disposizioni per favorire e semplificare l'accesso degli utenti e, in particolare, delle persone con disabilità agli strumenti informatici*, the Italian accessibility act). Status as at 2026-08-05.

Article 3 comma 1-bis, inserted by **D.L. 76/2020** (converted by L. 120/2020), extends the duties to private operators: entities offering services to the public through websites or mobile applications with an **average turnover over the last three years of operation exceeding EUR 500 million** (*fatturato medio, negli ultimi tre anni di attività, superiore a cinquecento milioni di euro*). Source: agid.gov.it.

Consequences for a covered private operator:

- publish a **dichiarazione di accessibilità** and review it **by 23 September of each year**; it is valid from 24 September to 23 September of the following year
- the declaration is generated **exclusively** through the AgID application at `https://form.agid.gov.it` — a hand-written page does not satisfy the model requirement
- on a website: link in the footer. On an app: the declaration URL goes into the store listing
- AgID performs technical verification and imposes sanctions; the procedure sits in **Determinazione AgID n. 355/2022**
- **Article 9 L. 4/2004** carries the penalty for failing to publish

The turnover threshold means most SMEs are outside Regime 1. That is not the end of the analysis.

## Regime 2 — European Accessibility Act

**D.Lgs 27 maggio 2022 n. 82**, *Attuazione della direttiva (UE) 2019/882 del Parlamento europeo e del Consiglio, del 17 aprile 2019, sui requisiti di accessibilità dei prodotti e dei servizi*. Status as at 2026-08-05.

Article 1 comma 1 fixes the application date: products placed on the market and services supplied **from 28 giugno 2025**. There is **no turnover threshold**.

Covered services relevant to a website project: **commercio elettronico** (e-commerce, meaning B2C sale of goods or services concluded through a website or app), electronic communications services, e-books, banking services for consumers, and passenger transport services.

**Microenterprise exemption.** Microenterprises that supply services are exempt (Directive (EU) 2019/882 art. 4(5)). *Microimpresa* means fewer than 10 persons employed and an annual turnover or annual balance sheet total not exceeding EUR 2 million. Two traps:

- the exemption covers **services only**. A microenterprise that manufactures, imports or distributes a covered **product** is not exempt.
- the exemption is claimed, not granted. Keep the headcount and turnover figures on file with a date, so the position can be shown if AgID asks.

[[UNVERIFIED: the individual article numbers of D.Lgs 82/2022 for the microenterprise exemption, the designation of the market surveillance authority and the sanction amounts. The decree's title, its 28.06.2025 application date and the fact that AgID acts on accessibility were confirmed on agid.gov.it and normattiva.it; the internal article numbering was not readable from an official source. Check the consolidated text on normattiva.it before citing an article number of D.Lgs 82/2022 in an output.]]

## Technical standard

**UNI CEI EN 301 549** is the harmonised standard against which conformity is assessed (agid.gov.it). For web content it references **WCAG 2.1 level AA**. Do not promise "WCAG 2.2 AAA" in a declaration — over-claiming in a published statement is itself a misrepresentation.

## Template — dichiarazione di accessibilità

The declaration must be generated through `form.agid.gov.it` when Regime 1 applies. The text below is the accessibility statement for a site outside Regime 1 that still wants to state its EAA position, and the wording to hand to the AgID form.

```html
<!-- BOZZA – non approvata legalmente -->
<h1>Dichiarazione di accessibilità</h1>

<p>
  [[Denominazione]] si impegna a rendere il proprio sito web accessibile,
  conformemente al decreto legislativo 27 maggio 2022, n. 82 (attuazione della
  direttiva (UE) 2019/882) e, ove applicabile, alla legge 9 gennaio 2004, n. 4.
</p>

<h2>Stato di conformità</h2>
<p>
  Questo sito web è [[conforme / parzialmente conforme / non conforme]] ai
  requisiti previsti dalla norma UNI CEI EN 301 549, corrispondente al livello AA
  delle WCAG 2.1.
  [[Se parzialmente conforme: indicare che alcune parti non sono conformi per i
  motivi elencati di seguito.]]
</p>

<h2>Contenuti non accessibili</h2>
<p>[[Elenco puntuale dei contenuti non accessibili, con il criterio WCAG non soddisfatto e la ragione]]</p>

<h2>Alternative accessibili</h2>
<p>[[Descrizione delle alternative offerte, oppure: nessuna alternativa disponibile]]</p>

<h2>Redazione della dichiarazione</h2>
<p>
  Dichiarazione redatta il [[data]] sulla base di
  [[autovalutazione / valutazione effettuata da un soggetto terzo: indicare quale]].
  Ultima revisione: [[data]].
</p>

<h2>Modalità di invio delle segnalazioni</h2>
<p>
  Segnalazioni di contenuti non accessibili: <a href="mailto:[[indirizzo]]">[[indirizzo]]</a>.
  Rispondiamo entro [[termine]] giorni.
</p>

<h2>Procedura di attuazione</h2>
<p>
  In caso di risposta insoddisfacente o di mancata risposta è possibile rivolgersi
  all'Agenzia per l'Italia digitale (AgID), [[recapito indicato da AgID al momento della pubblicazione]].
</p>
```

## Checkpoints

- [ ] Regime 1 assessed: is the three-year average turnover above EUR 500 million? Figure and date recorded
- [ ] Regime 2 assessed: is the service one of the covered categories, in particular *commercio elettronico*?
- [ ] Microenterprise status, if claimed, documented with headcount and turnover as at a stated date
- [ ] Microenterprise exemption not applied to a product
- [ ] If Regime 1 applies: declaration generated through `form.agid.gov.it`, not hand-written
- [ ] Declaration reviewed and updated by 23 September, footer link present
- [ ] Conformity level stated honestly, with the non-conforming content actually listed
- [ ] Feedback channel is a monitored address with a stated response time
- [ ] Keyboard-only pass through the checkout or signup flow completed
- [ ] Contrast measured, not estimated
- [ ] Form fields have associated labels and textual error messages
- [ ] No claim of a conformity level that has not been tested
- [ ] All `[[…]]` placeholders resolved or reported as open
