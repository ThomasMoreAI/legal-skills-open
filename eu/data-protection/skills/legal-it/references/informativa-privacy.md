# Informativa privacy

## Informativa is not consenso

The single most common defect in Italian privacy texts, and the one that survives every review because it looks diligent.

- **Informativa** = the notice under Art 13 GDPR (data collected from the data subject) or Art 14 GDPR (data obtained elsewhere). It is owed for **every** processing operation, whatever the legal basis. It is not a permission slip.
- **Consenso** = one of the six legal bases in Art 6(1) GDPR, and the weakest one. It must be freely given, specific, informed, unambiguous, provable and withdrawable at any time without detriment.

An Italian shop that asks the customer to tick "acconsento al trattamento dei dati personali" before it can ship an order has made three mistakes at once: the processing runs on Art 6(1)(b) contract and needs no consent; the "consent" is not free because the order cannot proceed without it, so it is invalid; and the customer can withdraw it at any moment, which would notionally strip the shop of the basis it does not actually need.

Legal basis per purpose, decided before drafting:

| Processing | Basis |
|---|---|
| Order handling, delivery, account | Art 6(1)(b) contract |
| Invoicing, accounting and tax retention | Art 6(1)(c) legal obligation |
| Server logs, IT security, fraud prevention | Art 6(1)(f) legitimate interest, with the interest named concretely |
| Newsletter and other electronic direct marketing | Art 6(1)(a) consent, plus art. 130 Codice Privacy |
| Non-technical cookies and trackers | Consent under art. 122 Codice Privacy |
| Soft-spam mailing to own customers | art. 130 Codice Privacy exception, opt-out |

Never write "consenso" next to a processing that runs on contract or legal obligation. Never write "interesse legittimo" next to a tracker.

## Italian deviations on top of the GDPR

**Codice in materia di protezione dei dati personali, D.Lgs 30 giugno 2003 n. 196**, as amended by **D.Lgs 10 agosto 2018 n. 101** to align it with the GDPR. It survives as a national complement, not as a replacement.

**Age of digital consent: 14.** **Article 2-quinquies Codice Privacy**, verbatim, verified on garanteprivacy.it:

> 1. In attuazione dell'articolo 8, paragrafo 1, del Regolamento, il minore che ha compiuto i quattordici anni può esprimere il consenso al trattamento dei propri dati personali in relazione all'offerta diretta di servizi della società dell'informazione. Con riguardo a tali servizi, il trattamento dei dati personali del minore di età inferiore a quattordici anni, fondato sull'articolo 6, paragrafo 1, lettera a), del Regolamento, è lecito a condizione che sia prestato da chi esercita la responsabilità genitoriale.
> 2. In relazione all'offerta diretta ai minori dei servizi di cui al comma 1, il titolare del trattamento redige con linguaggio particolarmente chiaro e semplice, conciso ed esaustivo, facilmente accessibile e comprensibile dal minore … le informazioni e le comunicazioni relative al trattamento che lo riguardi.

Two details that get lost in translation:

- **fourteen**, not the 16 of Art 8(1) GDPR. An Italian service must not copy a German or generic-EU template stating 16
- below 14 the consent must be **given by** the holder of parental responsibility (*prestato da chi esercita la responsabilità genitoriale*), which is stronger than merely being authorised by them

Comma 2 is a drafting obligation, not a disclaimer: where the service is directed at minors, the notice itself must be written so a minor can understand it. Breach of comma 1 carries the Art 83(5) GDPR ceiling, breach of comma 2 the Art 83(4) ceiling, under art. 166 commi 1 and 2 Codice Privacy.

If the audience includes under-14s, this is a product decision affecting signup, checkout and marketing, not a paragraph in the informativa.

Other Italian layers a website project touches:

- **art. 122** — consent for access to the terminal equipment, covered in `cookie-tracker.md`
- **art. 130** — unsolicited communications, covered in `marketing-diretto.md`
- **art. 2-quaterdecies** — designation of authorised persons, covered in `privacy-interna.md`
- **art. 4 L. 300/1970** — employee monitoring, covered in `privacy-interna.md`
- the Garante's **provvedimenti generali** operate as binding rules in practice, not as commentary

## Supervisory authority

Garante per la protezione dei dati personali, Piazza Venezia n. 11, 00187 Roma. Email `protocollo@gpdp.it`, PEC `protocollo@pec.gpdp.it`, telephone (+39) 06.696771, `https://www.garanteprivacy.it`. Verified on garanteprivacy.it, status as at 2026-08-05.

Name the Garante as the authority to which a complaint may be made (Art 13(2)(d) GDPR). Do not name a foreign authority because the hosting sits abroad.

## Mandatory content, Art 13 GDPR

Every one of these, per processing, not once in general:

1. identity and contact details of the controller, and of its representative where applicable
2. contact details of the DPO, where one exists
3. purposes and **legal basis** for each processing
4. where legitimate interest is relied on, **which** interest — concretely, not "il regolare svolgimento dell'attività"
5. recipients or categories of recipients
6. transfers outside the EEA, the country, and the safeguard relied on
7. retention period, or the criteria used to determine it
8. rights: access, rectification, erasure, restriction, portability, objection
9. where consent is the basis: the right to withdraw at any time, without affecting the lawfulness of prior processing
10. the right to lodge a complaint with the Garante
11. whether providing the data is a statutory or contractual requirement, and the consequences of not providing it
12. the existence of automated decision-making including profiling, with meaningful information about the logic and the consequences

Art 14 adds: the categories of data, the **source** the data came from, and whether it came from publicly accessible sources — required when data was not obtained from the data subject.

## Trasferimenti extra-UE — il DPF dopo Trump v. Slaughter

Point 6 above wants the safeguard named per recipient. For a US recipient, the EU-US Data Privacy Framework — decisione di esecuzione (UE) 2023/1795 del 10.07.2023 — covers only an organisation actually on `dataprivacyframework.gov/list` and only within its certified scope. Check the entity that invoices you, not the brand.

On **29.06.2026** the US Supreme Court held in *Trump v. Slaughter* that the removal protections for FTC commissioners are unconstitutional. Decision 2023/1795 relies on that independence: the FTC enforces the DPF principles, and independent supervision is part of the adequacy test under art. 45, par. 2, lett. b) GDPR. Status as at 05.08.2026: noyb asked the Commission on 29.06.2026 for an orderly repeal and announced an annulment action (no filing confirmed); the EDPB wrote to Commissioner McGrath on 31.07.2026 asking for a close assessment; the Commission has not acted.

- The decision **is still in force** — it falls only when the Commission repeals it or the Court of Justice annuls it. Do not write that US transfers have become unlawful.
- **DPF alone no longer carries the transfer.** Add clausole contrattuali tipo under art. 46, par. 2, lett. c) GDPR as a documented fallback plus a transfer impact assessment covering oversight and redress.
- This matters more in Italy than elsewhere: **provvedimento n. 224 del 9 giugno 2022** (doc. web 9782890, *Caffeina Media*) held the Google Analytics transfer contrary to artt. 44 and 46 GDPR because supplementary measures did not answer FISA 702 and EO 12333. Its Chapter V premise was superseded for DPF-certified recipients, not withdrawn — and what supersedes it is the very oversight-and-redress construction *Trump v. Slaughter* puts in doubt. See `cookie-tracker.md`.
- The published informativa still names recipient, country and safeguard. The fallback belongs in the registro delle attività di trattamento and in the art. 28 contract.

## Template

```html
<!-- BOZZA – non approvata legalmente -->
<h1>Informativa sul trattamento dei dati personali</h1>
<p>Ai sensi degli articoli 13 e 14 del Regolamento (UE) 2016/679.</p>

<h2>Titolare del trattamento</h2>
<p>
  [[Denominazione]]<br>
  [[Sede legale completa]]<br>
  P. IVA [[numero]] – C.F. [[numero]]<br>
  E-mail: [[indirizzo]] – PEC: [[indirizzo PEC]]
</p>

<h2>Responsabile della protezione dei dati</h2>
<p>[[Nominativo e recapito, oppure: non è stato designato un responsabile della protezione dei dati.]]</p>

<h2>Trattamenti, finalità e basi giuridiche</h2>
<table>
  <tr><th>Trattamento</th><th>Dati</th><th>Finalità</th><th>Base giuridica</th><th>Conservazione</th></tr>
  <tr>
    <td>Esecuzione dell'ordine</td>
    <td>[[dati anagrafici, indirizzo, contatto, dati dell'ordine]]</td>
    <td>Conclusione ed esecuzione del contratto</td>
    <td>Art. 6, par. 1, lett. b) GDPR</td>
    <td>[[durata]]</td>
  </tr>
  <tr>
    <td>Fatturazione e adempimenti contabili</td>
    <td>[[dati di fatturazione]]</td>
    <td>Adempimento di obblighi di legge</td>
    <td>Art. 6, par. 1, lett. c) GDPR</td>
    <td>[[durata prevista dalla normativa fiscale e civilistica]]</td>
  </tr>
  <tr>
    <td>Log di sistema e sicurezza</td>
    <td>[[indirizzo IP, user agent, timestamp]]</td>
    <td>[[interesse legittimo indicato in concreto: es. difesa da attacchi automatizzati]]</td>
    <td>Art. 6, par. 1, lett. f) GDPR</td>
    <td>[[durata]]</td>
  </tr>
  <tr>
    <td>Newsletter</td>
    <td>[[indirizzo e-mail]]</td>
    <td>Invio di comunicazioni commerciali</td>
    <td>Art. 6, par. 1, lett. a) GDPR e art. 130 del Codice</td>
    <td>[[fino alla revoca]]</td>
  </tr>
</table>

<h2>Destinatari</h2>
<p>[[Categorie di destinatari: hosting, spedizioniere, prestatore di servizi di pagamento, piattaforma di invio e-mail, consulente contabile]]</p>

<h2>Trasferimenti verso Paesi terzi</h2>
<p>[[Paese, destinatario, base del trasferimento: decisione di adeguatezza o clausole contrattuali tipo. Se non vi sono trasferimenti, dichiararlo.]]</p>

<h2>Natura del conferimento</h2>
<p>[[Quali dati sono necessari per il contratto e quali sono facoltativi, con le conseguenze del mancato conferimento]]</p>

<h2>Minori</h2>
<p>
  I servizi non sono destinati a minori di quattordici anni. Ai sensi
  dell'articolo 2-quinquies del Codice in materia di protezione dei dati
  personali, il consenso del minore di età inferiore a quattordici anni è
  valido solo se prestato o autorizzato da chi esercita la responsabilità
  genitoriale. [[Se il servizio si rivolge anche a minori: descrivere le
  modalità di verifica adottate.]]
</p>

<h2>Processi decisionali automatizzati</h2>
<p>[[Descrizione, logica e conseguenze, oppure: non sono effettuati processi decisionali automatizzati, compresa la profilazione.]]</p>

<h2>Diritti dell'interessato</h2>
<p>
  L'interessato può esercitare i diritti previsti dagli articoli da 15 a 22 del
  Regolamento scrivendo a [[indirizzo]]. Ove il trattamento sia fondato sul
  consenso, questo può essere revocato in qualsiasi momento; la revoca non
  pregiudica la liceità del trattamento effettuato in precedenza.
</p>

<h2>Reclamo</h2>
<p>
  È possibile proporre reclamo al Garante per la protezione dei dati personali,
  Piazza Venezia n. 11, 00187 Roma,
  <a href="https://www.garanteprivacy.it">garanteprivacy.it</a>.
</p>

<h2>Aggiornamenti</h2>
<p>Versione [[numero]] del [[data]].</p>
```

## Checkpoints

- [ ] Reachable without consent, without login, from every page
- [ ] Every processing has a purpose, a basis, recipients and a retention period
- [ ] No consent claimed where contract or legal obligation applies
- [ ] Legitimate interests named concretely, not as a formula
- [ ] Every service that actually loads appears in the notice — reconciled against the network capture
- [ ] Transfers outside the EEA listed individually with their safeguard
- [ ] Garante named as supervisory authority with the correct address
- [ ] Age of 14 used, not 16
- [ ] Where under-14s are in the audience: parental consent mechanism described and built
- [ ] Withdrawal right stated wherever consent is a basis
- [ ] Version number and date present
- [ ] All `[[…]]` placeholders resolved or reported as open
