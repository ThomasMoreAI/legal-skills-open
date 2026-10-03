# Cookies, trackers and tracking pixels

## The statutory hook

**Art. 122 Codice Privacy (D.Lgs 196/2003)**, transposing the ePrivacy Directive: storing information on, or accessing information already stored in, a user's terminal equipment requires consent, unless it is strictly necessary to transmit a communication or to provide a service explicitly requested by the user. Comma 2-bis states the position as a **general prohibition** subject to those derogations.

Two consequences that get missed:

- the rule is about **access to the terminal**, not about cookies. LocalStorage, IndexedDB, SDK identifiers, pixels, fingerprinting and any script that reads device characteristics are on the same footing.
- **legitimate interest is not available** for non-technical trackers. Art. 122 requires consent. A cookie policy claiming *interesse legittimo* for analytics or advertising is wrong on its face.

Breach of art. 122 carries the Art 83(5) GDPR ceiling under **art. 166 comma 2 Codice Privacy**.

## Linee guida cookie — provvedimento n. 231 del 10 giugno 2021

*Linee guida cookie e altri strumenti di tracciamento*, doc. web 9677876, **published in the Gazzetta Ufficiale n. 163 of 9 July 2021**. Verified on garanteprivacy.it. Status as at 2026-08-05: **not replaced, not amended**, still cited as governing law in the Garante's 2025 and 2026 decisions.

Compliance deadline as the Garante actually wrote it: *un termine pari a 6 mesi dal momento della loro pubblicazione in Gazzetta Ufficiale*. **The Garante never stated "10 gennaio 2022".** Six months from 9 July 2021 lands on a Sunday, which is why practitioners round. Phrase it as "six months from the G.U. publication of 9 July 2021", not as a hard calendar date.

Treat these guidelines as binding. They are more prescriptive on banner design than the EDPB's material, and where a generic EU template differs, the guidelines win for an Italian site.

### The X, not the reject button

This is the point most templates state wrongly. Verbatim:

> Tale comando dovrà avere una evidenza grafica pari a quella degli ulteriori comandi o pulsanti negoziali … Le modalità di prosecuzione nella navigazione senza prestare alcun consenso dovranno, in altre parole, essere immediate, usabili e accessibili quanto quelle previste per la prestazione del consenso.

The Italian requirement is an **X inside the banner, top right, of graphic prominence equal to the accept button**, allowing the user to continue without being forced onto another page or area. Closing with it leaves the defaults in force — no non-technical tracker fires.

A "Rifiuta tutti" button satisfies the substance and is good practice, but it is **not** the literal Italian requirement. Do not write a banner spec that says "Rifiuta tutti obbligatorio" while omitting the X.

### Mandatory content of the first layer

Verbatim, §7.2, the banner must contain, besides the X:

> i) l'avvertenza che la chiusura del banner mediante selezione dell'apposito comando contraddistinto dalla X posta al suo interno, in alto a destra, comporta il permanere delle impostazioni di default e dunque la continuazione della navigazione in assenza di cookie o altri strumenti di tracciamento diversi da quelli tecnici;
> ii) una informativa minima relativa al fatto che il sito utilizza … cookie o altri strumenti tecnici e potrà, esclusivamente previa acquisizione del consenso dell'utente …, utilizzare anche cookie di profilazione o altri strumenti di tracciamento …;
> iii) il link alla privacy policy, ovvero ad una informativa estesa posizionata in un second layer …;
> iv) un comando attraverso il quale sia possibile esprimere il proprio consenso …;
> v) il link ad una ulteriore area dedicata nella quale sia possibile selezionare, in modo analitico, soltanto le funzionalità, i soggetti cd. terze parti … ed i cookie …

### Scroll

Scroll alone is never consent:

> il semplice «scroll down» del cursore di pagina è inadatto in sé alla raccolta … di un idoneo consenso

It is not excluded as **one component** of a wider documented pattern producing *una scelta inequivoca e consapevole, che sia al tempo stesso registrabile e dunque documentabile*. In practice: do not build on scroll.

### Defaults and opt-in only

> il rispetto degli obblighi di privacy by default impone che le possibili scelte granulari siano inizialmente tutte preimpostate sul diniego

and the positive action available on first access must be *esclusivamente volta alla manifestazione del consenso (cd. opt-in) e non potrà mai riferirsi invece all'espressione di un diniego (cd. opt-out)*.

Preferences must be changeable at any time *in maniera semplice, immediata e intuitiva* through an area reachable from a **footer link**. A site using only technical cookies needs **no banner** at all — the information belongs in the privacy policy.

### Cookie wall

A take-it-or-leave-it mechanism is unlawful, *salva l'ipotesi – da verificare caso per caso – nella quale il titolare del sito offra all'interessato la possibilità di accedere ad un contenuto o a un servizio equivalenti senza prestare il proprio consenso*, and the alternative must itself comply with Art 5(1) GDPR.

### No re-prompting

Consent or refusal must be logged, and the banner may not be shown again except:

- when one or more conditions of the processing change significantly, for example a change of third parties
- when the operator cannot know that a cookie was already stored, for example because the user cleared storage
- *quando siano trascorsi almeno 6 mesi dalla precedente presentazione del banner*

A banner reappearing on every visit is a documented violation. A technical cookie storing the user's choice is expressly permitted and needs no consent.

### Analytics

Analytics cookies are **not** technical cookies, but are assimilated to them where used for site optimisation directly by the site's own controller to produce aggregate statistics. The guidelines' conditions:

- masking **at least the fourth octet** of the IPv4 address, with equivalent treatment for IPv6
- use limited to *produzione di statistiche aggregate*
- where a third party performs the statistical processing, the data must be minimised beforehand and *non potranno essere combinati con altre elaborazioni né trasmessi ad ulteriori terzi*

The Garante's FAQ permits cross-domain statistics across domains, sites or apps of the **same controller or corporate group**, whether run in-house or by a third party acting on the controller's mandate.

Self-hosted analytics can meet this. A third-party SaaS analytics tool on default settings generally cannot.

### Fingerprinting

Expressly in scope. The guidelines distinguish *identificatori attivi* (cookies) from *passivi* (mere observation) and state that *il fingerprinting e gli ulteriori strumenti di tracciamento devono dunque essere ricompresi nell'ambito di applicazione delle presenti Linee guida*. The Garante treats passive identifiers as more serious, because the user has no self-help remedy.

## Tracking pixels in email — provvedimento n. 284 del 17 aprile 2026

**New instrument, and any Italian deliverable produced after April 2026 that ignores it is incomplete.**

*Linee Guida in materia di utilizzo di tracking pixel nelle comunicazioni di posta elettronica*, doc. web 10241943, **published in the Gazzetta Ufficiale, Serie Generale n. 98 of 29 April 2026**. Verified on garanteprivacy.it.

- **Compliance deadline: six months from G.U. publication, i.e. 29 October 2026.**
- Addressees: information society service providers, anyone offering publicly accessible online services, email providers, bulk-mail platform operators, and *ogni altro soggetto che, a qualsiasi titolo, faccia uso di tracking pixel*.
- Basis: **art. 122 Codice Privacy**. Under comma 2-bis the Garante frames it as *un divieto generalizzato di trattamento*, save for consent, or necessity to carry out the transmission, or necessity to provide an online communication service requested by the user.
- **Consent is required** whenever open-rate measurement is individual and used to evaluate or optimise campaigns — changing subject lines on low open rates, adapting send frequency, suppressing after repeated non-opens — or to infer tastes and interests.
- Withdrawal must be **granular**: a standardised icon or footer link to an area where the recipient can stop the emails **or stop only the pixels while continuing to receive the messages**.
- Covert use is unlawful in itself: *il permanere del carattere occulto connesso all'impiego di tracking pixel determinerebbe l'illiceità del trattamento*.
- Privacy by design: use *un identificativo inintelligibile e non sequenziale* mapped to the address in a separate internal layer, so the address never travels in the pixel request.
- The soft-spam basis in art. 130 comma 4 may cover the underlying send, but **does not dispense with the art. 122 analysis for the pixel**.

Practical consequence for a mailing setup: open tracking is not a default to leave switched on. It is a separate consent, with its own opt-out, distinct from the newsletter subscription.

## Google Analytics

**Provvedimento n. 224 del 9 giugno 2022** (doc. web 9782890, *Caffeina Media S.r.l.*) held that Google Analytics as then configured transferred visitor data to Google LLC in the United States *in violazione degli artt. 44 e 46 del Regolamento*, with supplementary measures inadequate against FISA 702 and EO 12333. Warning, 90 days to comply, otherwise suspension of the flows.

What changed since:

- **Commission Implementing Decision (EU) 2023/1795 of 10 July 2023** established EU-US Data Privacy Framework adequacy.
- **T-553/23 Latombe v Commission**, General Court, judgment of **3 September 2025**: the annulment action was **dismissed**; the adequacy decision stands. The Court's finding is expressly tied to the position at the date of adoption.
- **Appeal C-703/25 P**, lodged 31 October 2025, is **pending as at 2026-08-05**. An appeal has no suspensory effect, so the adequacy decision remains in force.

[[UNVERIFIED: whether the Garante has formally updated or withdrawn its 2022 Google Analytics position. No post-DPF FAQ, revocation or restatement was found on garanteprivacy.it, but the site has no reliable full-text search — this is absence of evidence, not evidence of absence.]]

Two sentences that must both appear if Google Analytics comes up, and neither alone:

1. The 2022 provvedimento was decided on the pre-DPF legal position, and its Chapter V premise is superseded for DPF-certified recipients. It has not been formally withdrawn.
2. The transfer question is separate from the consent question. Google Analytics is not a technical tool, so it needs consent before it loads regardless of how the transfer analysis resolves.

Never tell a user "Google Analytics is banned in Italy" or "Google Analytics is fine now" without both.

## Enforcement reality

**Provvedimento n. 327 del 4 giugno 2025** (doc. web 10152729, *Confalonieri S.r.l.*) came out of a systematic sweep: the Garante delegated online checks to the **Nucleo speciale tutela privacy e frodi tecnologiche della Guardia di Finanza**, targeting a sample of **e-commerce sites selected by size and geography**, with an on-site inspection. The finding centred on a defective first-layer banner.

Banner defects are being enforced against ordinary SMEs, not only against large publishers.

## Template — cookie policy

```html
<!-- BOZZA – non approvata legalmente -->
<h1>Cookie policy</h1>
<p>
  Questo sito utilizza cookie e altri strumenti di tracciamento. Di seguito
  sono indicati gli strumenti utilizzati, le finalità e le modalità per
  esprimere, modificare o revocare il consenso.
</p>

<h2>Titolare del trattamento</h2>
<p>[[Denominazione]], [[sede legale]], P. IVA [[numero]], [[e-mail]], PEC [[indirizzo]]</p>

<h2>Strumenti tecnici e strumenti assimilati</h2>
<p>
  Gli strumenti tecnici non richiedono il consenso ai sensi dell'art. 122 del
  Codice in materia di protezione dei dati personali.
</p>
<table>
  <tr><th>Nome</th><th>Titolarità</th><th>Finalità</th><th>Durata</th></tr>
  <tr><td>[[nome]]</td><td>[[prima parte / terza parte]]</td><td>[[finalità]]</td><td>[[durata]]</td></tr>
</table>

<h2>Strumenti di profilazione e di tracciamento soggetti a consenso</h2>
<table>
  <tr><th>Nome</th><th>Fornitore</th><th>Finalità</th><th>Durata</th><th>Paese e base del trasferimento</th></tr>
  <tr><td>[[nome]]</td><td>[[fornitore]]</td><td>[[finalità]]</td><td>[[durata]]</td><td>[[Paese, decisione di adeguatezza o clausole contrattuali tipo]]</td></tr>
</table>

<h2>Tracking pixel nelle comunicazioni e-mail</h2>
<p>
  [[Se utilizzati: descrivere l'impiego di tracking pixel, la finalità, e il link
  all'area in cui il destinatario può disattivare i soli pixel continuando a
  ricevere i messaggi. Se non utilizzati, dichiararlo.]]
</p>

<h2>Come modificare le preferenze</h2>
<p>
  È possibile modificare o revocare il consenso in qualsiasi momento tramite
  <a href="[[link che riapre il pannello]]">il pannello delle preferenze</a>.
  La revoca non pregiudica la liceità del trattamento effettuato in precedenza.
</p>

<h2>Diritti dell'interessato</h2>
<p>
  Diritti previsti dagli articoli da 15 a 22 del Regolamento (UE) 2016/679.
  È possibile proporre reclamo al Garante per la protezione dei dati personali,
  Piazza Venezia n. 11, 00187 Roma,
  <a href="https://www.garanteprivacy.it">garanteprivacy.it</a>.
</p>
```

## Template — banner first layer

```html
<!-- BOZZA – non approvata legalmente -->
<div role="dialog" aria-modal="true" aria-labelledby="cb-title">
  <button aria-label="Chiudi">×</button>

  <h2 id="cb-title">Cookie e strumenti di tracciamento</h2>
  <p>
    Questo sito utilizza cookie e altri strumenti tecnici e, esclusivamente
    previo consenso, cookie di profilazione o altri strumenti di tracciamento
    per [[finalità]]. Chiudendo questo banner con il comando × in alto a destra
    restano attive le impostazioni di default e la navigazione prosegue in
    assenza di strumenti diversi da quelli tecnici.
    Maggiori informazioni nella <a href="/cookie-policy">cookie policy</a> e
    nell'<a href="/privacy">informativa privacy</a>.
  </p>

  <button>Accetta tutti</button>
  <button>Personalizza</button>
</div>
```

The X must render with the same graphic weight as the accept button, and every granular option in the *Personalizza* panel starts switched off.

## Checkpoints

- [ ] Loaded in a fresh profile with the network tab open: no non-technical request fires before a choice
- [ ] Application tab checked: no non-technical cookie, LocalStorage or IndexedDB entry before a choice
- [ ] X present inside the banner, top right, with graphic prominence equal to the accept command
- [ ] Closing with the X fires nothing and does not force navigation to another page
- [ ] First layer carries all five items of §7.2 of the guidelines
- [ ] All granular options preset to refusal; no opt-out-style controls on first access
- [ ] No cookie wall, or a genuinely equivalent no-consent alternative available
- [ ] Banner not re-presented for at least six months after a recorded choice
- [ ] Consent and refusal both logged, with timestamp and banner version
- [ ] Preference panel reachable permanently from the footer
- [ ] Site with technical cookies only: no banner shown, information in the privacy policy
- [ ] Analytics: fourth IPv4 octet masked, aggregate use only, no combination or onward transmission
- [ ] Fingerprinting and passive identifiers treated as consent-requiring
- [ ] Third-party fonts served locally or placed behind consent; maps, video and captcha behind consent or click-to-load
- [ ] No legitimate interest claimed for any non-technical tracker
- [ ] Email tracking pixels: separate consent, granular opt-out, disclosed — deadline 29 October 2026
- [ ] Cookie policy and privacy informativa reachable without passing the banner
- [ ] All `[[…]]` placeholders resolved or reported as open
