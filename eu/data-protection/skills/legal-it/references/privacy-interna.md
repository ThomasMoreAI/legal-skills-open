# Internal data protection compliance

None of this is published on the site. All of it is what the Garante asks for first when a complaint arrives.

## Registro delle attività di trattamento

Art 30 GDPR. The exemption for organisations under 250 employees is narrow and almost never available in practice: it falls away if the processing is not occasional, or is likely to result in a risk to rights and freedoms, or involves special categories. A webshop with customer accounts, a newsletter and a support inbox processes continuously — keep the register.

Minimum per entry: purpose, categories of data subject, categories of data, categories of recipient, transfers outside the EEA with the safeguard, retention period, and a description of the technical and organisational measures.

## Roles

- **Titolare del trattamento** (controller) — the legal person, not the founder personally
- **Responsabile del trattamento** (processor) — hosting, mailing platform, payment provider, CRM, accountant. Each needs an Art 28 GDPR contract before it starts processing, not afterwards
- **Soggetti designati / autorizzati al trattamento** — employees and collaborators who touch personal data. **Article 2-quaterdecies Codice Privacy**, verbatim, verified on garanteprivacy.it:

  > 1. Il titolare o il responsabile del trattamento possono prevedere, sotto la propria responsabilità e nell'ambito del proprio assetto organizzativo, che specifici compiti e funzioni connessi al trattamento di dati personali siano attribuiti a persone fisiche, espressamente designate, che operano sotto la loro autorità.
  > 2. Il titolare o il responsabile del trattamento individuano le modalità più opportune per autorizzare al trattamento dei dati personali le persone che operano sotto la propria autorità diretta.

  This is the Italian survival of the old *incaricati*. Designation letters per role, with scope and instructions, remain standard practice and are what an inspector asks to see.
- **Contitolarità** (Art 26 GDPR) — arises more often than expected, for example with social plugins and some advertising tools. It needs an arrangement, not silence

**New: art. 2-quaterdecies.1**, inserted by art. 12 comma 1 D.L. 19 febbraio 2026 n. 19, converted by L. 20 aprile 2026 n. 50. Firms with **fewer than five employees** get a dedicated simplified procedure for the Art 33 GDPR breach notification, to be defined by a Garante provvedimento with guided self-assessment tools.

[[UNVERIFIED: the implementing Garante provvedimento for art. 2-quaterdecies.1 could not be located. Check garanteprivacy.it before telling a micro-employer that the simplified route is operational.]]

## DPO / Responsabile della protezione dei dati

Mandatory under Art 37 GDPR where the core activities consist of regular and systematic monitoring of data subjects on a large scale, or of large-scale processing of special categories. There is **no headcount threshold** in Italian law — a small team running large-scale tracking can be caught while a bigger company doing routine processing is not.

If appointed, the contact details must be published and **notified to the Garante**. The Garante states that the online procedure at `https://servizi.gpdp.it/comunicazionerpd/s/` is **the only** channel for communicating, changing or revoking the DPO's contact details, and that communications sent by email or post will not be considered. Verified on garanteprivacy.it, live as at 2026-08-05.

Appointing a DPO and not notifying is a common and easily detected defect. There is no Codice article prescribing the procedure — it rests on Art 37(7) GDPR plus the Garante's designated telematic route.

## Data breach

Notification to the Garante within 72 hours of becoming aware, unless the breach is unlikely to result in a risk (Art 33 GDPR); communication to affected individuals where the risk is high (Art 34 GDPR). The Garante operates a dedicated online notification procedure — a plain email to the general inbox is not the prescribed route.

Keep an internal register of **all** breaches, including those not notified, with the reasoning for not notifying. Art 33(5) GDPR requires this and the absence of the register is itself a finding.

Prepare before the incident: who declares a breach, who assesses risk, who drafts the notification, who signs. A 72-hour clock is not the moment to design a process.

## DPIA

Art 35 GDPR. The Garante has published a list of processing types requiring a DPIA in Italy. Typical triggers for a web project: systematic profiling of users, large-scale processing of special categories, biometric identification, systematic monitoring of publicly accessible areas, processing of children's data on a large scale for profiling or marketing.

[[UNVERIFIED: the number and date of the Garante's provvedimento listing the processing types subject to mandatory DPIA in Italy. Confirm on garanteprivacy.it before citing it.]]

## Employee monitoring — the Italian layer that catches IT tooling

**Article 4 of the Statuto dei Lavoratori (Legge 20 maggio 1970 n. 300)**, wholly replaced by **art. 23 comma 1 D.Lgs 14 settembre 2015 n. 151**, then amended to move competence from the Direzione territoriale del lavoro to the **Ispettorato nazionale del lavoro**. Verbatim, verified on normattiva.it:

> **1.** Gli impianti audiovisivi e gli altri strumenti dai quali derivi anche la possibilità di controllo a distanza dell'attività dei lavoratori possono essere impiegati esclusivamente per esigenze organizzative e produttive, per la sicurezza del lavoro e per la tutela del patrimonio aziendale e possono essere installati previo accordo collettivo stipulato dalla rappresentanza sindacale unitaria o dalle rappresentanze sindacali aziendali. […] In mancanza di accordo, gli impianti e gli strumenti di cui al primo periodo possono essere installati previa autorizzazione delle sede territoriale dell'Ispettorato nazionale del lavoro […]
> **2.** La disposizione di cui al comma 1 non si applica agli strumenti utilizzati dal lavoratore per rendere la prestazione lavorativa e agli strumenti di registrazione degli accessi e delle presenze.
> **3.** Le informazioni raccolte ai sensi dei commi 1 e 2 sono utilizzabili a tutti i fini connessi al rapporto di lavoro a condizione che sia data al lavoratore adeguata informazione delle modalità d'uso degli strumenti e di effettuazione dei controlli e nel rispetto di quanto disposto dal decreto legislativo 30 giugno 2003, n. 196.

Criminal backstop: **art. 171 Codice Privacy** punishes breach of art. 4 comma 1 and art. 8 L. 300/1970 with the penalties of art. 38 of that law. This is not a purely administrative risk.

Why this bites a web team:

- **email and collaboration tooling** is a work instrument under comma 2 — until a log-retention or content-inspection layer is added on top, at which point it starts to look like comma 1 equipment
- **MDM, endpoint agents, DLP, VPN and proxy logs, badge systems beyond attendance, and analytics on internal tools** routinely fall under comma 1
- comma 3 applies in every case: without a written, distributed policy on how the tools are used and how checks are carried out, the data cannot lawfully be used against the worker — even where the tool itself was permitted
- the Garante construes the comma 2 exception strictly (*deve … essere oggetto di stretta interpretazione*)

**Leading enforcement precedent:** provvedimento **1 dicembre 2022 n. 409** (doc. web 9833530), *Regione Lazio*, **EUR 100,000**. Generalised collection and 180-day retention of employees' email metadata for generic IT-security purposes, later used to monitor staff messaging a trade union. Held to be unlawful indirect remote monitoring without the art. 4 comma 1 guarantees.

**Email metadata retention — the number that changed.** The Garante's preliminary document (provv. 21 dicembre 2023 n. 642) proposed **seven days plus 48 hours**. That was suspended by provv. 22 febbraio 2024 n. 127, which opened a public consultation. The final instrument is **provvedimento n. 364 del 6 giugno 2024** (doc. web 10026277), *Documento di indirizzo. Programmi e servizi informatici di gestione della posta elettronica nel contesto lavorativo e trattamento dei metadati*:

> …a titolo orientativo, tale conservazione non dovrebbe comunque superare i 21 giorni.

Read it correctly: **21 days is an accountability-based orientation, not a hard cap.** Longer retention for the same purpose is possible where particular conditions make it necessary and are adequately evidenced. What triggers the art. 4 comma 1 procedure is *generalised* extended log retention, because it can amount to indirect remote monitoring — not merely crossing day 21.

Anyone quoting "seven days" is quoting a withdrawn draft.

Practical consequence: before deploying any monitoring-capable tool, decide which comma it falls under, secure the accordo sindacale or the Ispettorato authorisation if comma 1 applies, and issue the comma 3 notice regardless.

## Sanctions

- **Art. 166 comma 2 Codice Privacy** applies the Art 83(5) GDPR ceiling to breaches of the Italian provisions that matter most for a website: **art. 122** (access to terminal equipment), **art. 130 commi 1-5** (unsolicited communications), art. 2-ter, art. 2-quinquies comma 1, art. 2-octies and others. Art. 166 comma 1 applies the Art 83(4) ceiling to a shorter list including art. 2-quinquies comma 2.
- **Art. 167** makes unlawful processing a **criminal** offence where there is specific intent to profit or to harm **and** actual *nocumento*: six months to one year and six months for breaches of artt. 123, 126 or 130; one to three years for special-category data processed in breach of artt. 2-sexies or 2-octies, and for third-country transfers outside Artt. 45, 46 or 49 GDPR.
- **Artt. 167-bis and 167-ter** cover unlawful communication or diffusion of a large-scale automated archive and fraudulent acquisition. **Art. 168** covers false statements to, or obstruction of, the Garante.

Point worth stating to a client planning a mailing programme: an art. 130 breach carries **both** the Art 83(5) administrative ceiling and criminal exposure under art. 167 comma 1.

## Retention

Retention has to be a decision, not a default. Common Italian anchors that constrain deletion:

- accounting and tax documents: ten years under civil law bookkeeping rules, with tax assessment periods running in parallel
- contractual claims: the ordinary limitation period
- consent evidence: for as long as the consent is relied on, plus the limitation period

Where a tax or accounting rule forces retention, that is a **legal obligation** basis for keeping the data — and an erasure request does not override it. Say so in the informativa rather than promising deletion the business cannot perform.

## Checkpoints

- [ ] Registro delle attività di trattamento exists and matches the services actually in use
- [ ] Art 28 agreement signed with every processor, before processing started
- [ ] Sub-processor lists reviewed, transfers outside the EEA identified with their safeguard
- [ ] Written designations for staff who process data, with scope and instructions
- [ ] Joint controllership assessed for social plugins and advertising tools
- [ ] DPO requirement assessed in writing; if appointed, contact details notified to the Garante
- [ ] Breach procedure documented with named roles and the 72-hour path
- [ ] Internal breach register exists, including non-notified breaches with reasoning
- [ ] DPIA assessed and, where required, carried out and dated
- [ ] Every monitoring-capable IT tool classified under art. 4 comma 1 or comma 2 L. 300/1970
- [ ] Accordo sindacale or Ispettorato authorisation obtained where comma 1 applies
- [ ] Comma 3 notice issued to workers, in writing, covering how checks are carried out
- [ ] Log retention periods defined per system and actually enforced
- [ ] Retention schedule reconciled with tax and accounting obligations
