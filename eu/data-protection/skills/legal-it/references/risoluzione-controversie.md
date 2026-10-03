# Dispute resolution

## The ODR platform is gone. Delete every reference to it.

The EU Online Dispute Resolution platform was shut down by **Regulation (EU) 2024/3228**; operation ended **20 July 2025**. A link to `ec.europa.eu/consumers/odr` is today a dead link presented to consumers as a right they can exercise, which is itself a misleading commercial practice risk under artt. 20-22 Codice del Consumo.

Rules that follow from this and admit no exception:

- if an existing text, footer, order confirmation email, shop plugin or PDF terms mentions the *piattaforma ODR*, *piattaforma europea di risoluzione delle controversie online*, or links `ec.europa.eu/consumers/odr`, it is **removed**, not rewritten
- never re-add it, whatever an Italian shop template, a plugin default or a stale guide says
- search the whole project, not just the terms page: `odr`, `consumers/odr`, `risoluzione delle controversie online`, `piattaforma europea`
- replace it with a reference to a real, currently operating ADR body — or with nothing, if the trader is not bound to one

## Italian ADR framework

**Codice del Consumo (D.Lgs 6 settembre 2005 n. 206), Parte V Titolo II-bis, articles 141 to 141-decies**, inserted by **D.Lgs 6 agosto 2015 n. 130** transposing Directive 2013/11/EU. Status as at 2026-08-05, confirmed on mimit.gov.it.

Eight authorities keep the registers (*elenchi*) of accredited ADR bodies, split by sector:

| Authority | Sector |
|---|---|
| Ministero delle Imprese e del Made in Italy (MIMIT) | general consumer disputes |
| Ministero della Giustizia | organismi di mediazione |
| CONSOB | financial markets |
| IVASS | insurance |
| ARERA | energy, water, waste |
| AGCOM | electronic communications |
| Banca d'Italia | banking and credit |
| ART | transport |

Practical consequence: "the ADR body" is not one national institution. Which body is competent depends on the sector, and for a general online shop it is an ADR body listed by MIMIT — not an authority the trader gets to name freely.

Instruments in practice:

- **conciliazione paritetica** — a negotiated procedure run jointly by a company and consumer associations under a protocol. Only available if the trader has signed such a protocol. A trader that has not signed one must not claim it.
- **mediazione** before an organismo registered with the Ministero della Giustizia, often hosted at a **Camera di Commercio**. The Camere di Commercio also run consumer conciliation services.
- **arbitrato** — binding, and for that reason not something to impose on a consumer in standard terms.

## Information duty

Article **49 comma 1** Codice del Consumo requires the trader, before a distance contract is concluded, to inform the consumer of the possibility of recourse to an out-of-court complaint and redress mechanism to which the trader is subject, and how to access it.

[[UNVERIFIED: the exact lettera of art. 49 comma 1 carrying this item, and the exact comma of art. 141-sexies obliging a trader that adheres to an ADR body to state that on its website and in its general terms. The range 141 to 141-decies and D.Lgs 130/2015 were confirmed on mimit.gov.it; the sub-numbering was not. Verify on normattiva.it before citing a lettera or comma in an output.]]

Two positions, and only two:

1. **The trader adheres to an ADR body.** Name the body, give its address and website, and state how the consumer starts the procedure. Do this on the site and in the general terms.
2. **The trader adheres to no ADR body.** Say so plainly, point to the ordinary courts and to the consumer's forum rule. Do not invent an adherence to sound compliant.

## Consumer forum

For a consumer contract the competent court is the one of the consumer's place of residence or elected domicile — a mandatory rule of Italian consumer law. A choice-of-forum clause in standard terms fixing the trader's seat is **vessatoria** and unenforceable against the consumer (unfair terms regime, artt. 33 ff Codice del Consumo).

Do not write "Foro competente in via esclusiva: [[città della sede]]" into B2C terms. It reads as authoritative, it is void, and the clause itself is an unfair-practice exposure.

## Template — clause for general terms

```html
<!-- BOZZA – non approvata legalmente -->
<h2>Reclami e risoluzione delle controversie</h2>

<p>
  I reclami possono essere inviati a
  <a href="mailto:[[indirizzo]]">[[indirizzo]]</a>. Rispondiamo entro
  [[termine]] giorni dal ricevimento.
</p>

<!-- Variante 1: il professionista aderisce a un organismo ADR -->
<p>
  Per la risoluzione stragiudiziale delle controversie il consumatore può
  rivolgersi a [[denominazione dell'organismo ADR]], iscritto nell'elenco
  tenuto da [[autorità competente]], con sede in [[indirizzo]],
  sito web [[URL]]. La procedura si avvia [[modalità]].
</p>

<!-- Variante 2: nessuna adesione -->
<p>
  [[Denominazione]] non aderisce ad alcun organismo di risoluzione
  extragiudiziale delle controversie. Resta impregiudicato il diritto del
  consumatore di rivolgersi all'autorità giudiziaria ordinaria.
</p>

<h2>Legge applicabile e foro competente</h2>
<p>
  Il contratto è regolato dalla legge italiana. Restano applicabili le
  disposizioni imperative più favorevoli previste dalla legge del Paese di
  residenza abituale del consumatore. Per le controversie con i consumatori è
  competente il giudice del luogo di residenza o di domicilio eletto del
  consumatore.
</p>
```

## Checkpoints

- [ ] Project-wide search for `odr`, `consumers/odr`, `risoluzione delle controversie online`, `piattaforma europea` returns nothing — including shop plugin templates and transactional emails
- [ ] The ADR position is one of the two honest variants, not an invented adherence
- [ ] If a body is named, it is actually on the register of the competent authority
- [ ] Complaint address is a monitored inbox with a stated response time
- [ ] No exclusive forum clause at the trader's seat in B2C terms
- [ ] Choice-of-law clause preserves mandatory consumer protections of the consumer's country
- [ ] No arbitration clause imposed on consumers
- [ ] All `[[…]]` placeholders resolved or reported as open
