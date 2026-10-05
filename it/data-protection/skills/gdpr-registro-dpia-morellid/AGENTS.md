# AGENTS.md - gdpr-registro-dpia

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Compliance GDPR italiana per:
- **Registro delle attivita' di trattamento** (art. 30 Reg. UE 2016/679)
- **Valutazione d'Impatto sulla protezione dei dati - DPIA** (art. 35 Reg. UE 2016/679)

Target utente: titolari del trattamento, responsabili del trattamento, DPO, ingegneri dell'informazione che progettano sistemi che trattano dati personali in azienda italiana.

## Fonti autoritative

- **Reg. UE 2016/679 (GDPR)** - testo italiano arricchito Garante (catalogato in `sources.yaml` con hash `16c0bb35...`). Articoli rilevanti: 6, 9, 10 (basi giuridiche), 13-14 (informativa), 25 (privacy by design), 30, 32, 33-34 (data breach), 35-36 (DPIA), 37-39 (DPO), 44-49 (trasferimenti extra-UE), 83-84 (sanzioni)
- **Provvedimento Garante n. 467/2018 - Allegato 1** - 12 tipologie di trattamenti soggette a DPIA in Italia (catalogato con hash `6ece43c2...`)
- **Provvedimento Garante n. 284/2026** - Linee guida tracking pixel nelle e-mail, GU n. 98 del 29/04/2026 (catalogato con hash `df04bc93...` sul PDF del fascicolo GU)
- **WP248 rev. 01** EDPB-endorsed - 9 criteri per identificare trattamenti ad alto rischio
- **D.Lgs. 196/2003** modificato dal **D.Lgs. 101/2018** - Codice Privacy italiano coordinato col GDPR
- **Garante** - FAQ Registro, decisioni puntuali, codici di deontologia (es. sistemi informativi creditizi - Allegato A.5 Cod. Privacy)

## Articoli e punti chiave

- **Art. 30 GDPR**: 7 contenuti minimi del Registro (titolare); 4 contenuti minimi (responsabile)
- **Art. 30 par. 5**: deroga organizzazioni < 250 dipendenti - in pratica raramente applicabile in Italia
- **Art. 35 par. 3**: 3 casi espliciti DPIA (profilazione con effetti, larga scala cat. particolari, sorveglianza pubblica)
- **Art. 35 par. 7**: 4 contenuti minimi DPIA (descrizione, necessita'/proporzionalita', rischi, misure)
- **Provv. Garante 467/2018 Allegato 1**: 12 tipologie italiane (anche 1 sola tipologia attiva DPIA)
- **WP248 criteri**: 2+ criteri = DPIA richiesta; 1 criterio = DPIA raccomandata caso per caso
- **Art. 122 Codice Privacy**: disciplina l'accesso al terminale; per i tracking pixel nelle e-mail vale il divieto del comma 2-bis salvo deroghe o consenso (Linee guida 284/2026, par. 5-6)
- **Provv. 284/2026**: adeguamento entro sei mesi dalla pubblicazione in GU (29/04/2026), quindi 29/10/2026. Il provvedimento NON impone di per se' Registro o DPIA: il collegamento passa da art. 30/art. 35/WP248/Allegato 1

## Convenzioni specifiche

### Cosa NON fare
- Non fornire pareri legali. La skill produce drafts e gap analyses; il DPO o consulente legale firma.
- Non confondere ruoli: titolare (decide finalita' e mezzi) vs responsabile (tratta per conto del titolare). Cambia tutto.
- Non saltare la consultazione del DPO per la DPIA (art. 35 par. 2 - obbligatoria).
- Non valutare singoli trasferimenti extra-UE in profondita' senza Transfer Impact Assessment dedicato.

### Cosa fare
- Citare l'articolo (e paragrafo) preciso per ogni affermazione.
- Per la soglia DPIA: applicare in cascata (a) tipologie italiane Garante 467/2018, (b) art. 35 par. 3 GDPR, (c) criteri WP248. Anche un solo trigger basta.
- Distinguere chiaramente Registro titolare (par. 1) da Registro responsabile (par. 2) - sono due documenti diversi quando l'organizzazione e' entrambi.
- Per la DPIA: usare la struttura art. 35 par. 7 + matrice rischi (categorie interessati x rischio x severita' x probabilita') + parere DPO obbligatorio.
- Sanzioni di riferimento: fino a 10M EUR / 2% fatturato (art. 83 par. 4) per art. 30, 35; fino a 20M / 4% (art. 83 par. 5) per violazioni piu' gravi.

## Validatori

- Da identificare. Profilo target: DPO esperto + ingegnere informazione con esperienza compliance privacy (non Vitale - settore diverso).

## Stato attuale

- v0.2.0 (alpha)
- 5 task files: `draft-registro-trattamenti`, `check-registro-trattamenti`, `valuta-soglia-dpia`, `draft-dpia`, `tracking-pixel-email`
- 4 estratti normativi
- 3 esempi (registro PMI base, DPIA app scoring credito, tracking pixel newsletter)
- Skill non testata su Registro/DPIA reale - validazione Livello 2 prioritaria
