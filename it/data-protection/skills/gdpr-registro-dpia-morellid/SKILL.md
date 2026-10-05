---
name: gdpr-registro-dpia-morellid
title: GDPR Registro trattamenti + DPIA
description: Supporta la stesura e verifica del Registro delle attivita' di trattamento (art. 30 GDPR) e della Valutazione d'Impatto sulla protezione dei dati - DPIA (art. 35 GDPR), incluso il modulo per i tracking pixel nelle e-mail secondo le Linee guida Garante provv. 284/2026. Use when the user needs to draft a GDPR processing register, verify its completeness, decide whether a DPIA is required for a specific processing activity, structure a DPIA, or assess e-mail tracking pixel compliance. Target users are Italian data controllers, processors, DPO, and IT engineers building systems that process personal data, with reference to the Italian Garante Privacy provisions.
author: morellid
author_url: https://github.com/morellid/skill-per-ingegneri/tree/main/skills/gdpr-registro-dpia
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: data-protection
language: it
tags: [gdpr, dpia, garante-privacy, tracking-pixel, email-marketing]
sources:
- title: Garante Allegato1 Prov467 2018
  path: references/estratti/garante-allegato1-prov467-2018.md
- title: Garante Prov284 2026 Tracking Pixel
  path: references/estratti/garante-prov284-2026-tracking-pixel.md
- title: Gdpr Art 30
  path: references/estratti/gdpr-art-30.md
- title: Gdpr Art 35 36
  path: references/estratti/gdpr-art-35-36.md
- title: Wp248 Criteri
  path: references/estratti/wp248-criteri.md
- title: Garante Prov284 2026 Tracking Pixel
  path: references/fonti/garante-prov284-2026-tracking-pixel.md
- title: Garante Prov467 2018 Allegato1
  path: references/fonti/garante-prov467-2018-allegato1.md
- title: Gdpr It Garante 2018
  path: references/fonti/gdpr-it-garante-2018.md
- title: Wp248 Rev01
  path: references/fonti/wp248-rev01.md
---

# GDPR Registro trattamenti + DPIA

## Quando usare questa skill

Usare quando un titolare/responsabile del trattamento, DPO o ingegnere chiede di:
- Redigere o aggiornare il Registro delle attivita' di trattamento (art. 30 GDPR)
- Verificare la completezza di un Registro esistente
- Valutare se un trattamento richiede una DPIA (art. 35 GDPR + Provv. Garante 467/2018)
- Strutturare una DPIA secondo i contenuti minimi dell'art. 35 par. 7
- Censire nel Registro l'uso di tracking pixel nelle e-mail, valutarne la soglia DPIA e verificare la conformita' alle Linee guida Garante provv. 284/2026 (adeguamento entro il 29/10/2026)

**Non usare** quando l'utente chiede:
- Pareri legali su singole interpretazioni del GDPR (richiede legale specializzato)
- Risposte a richieste di esercizio diritti degli interessati (skill futura dedicata)
- Analisi di trasferimenti dati extra-UE in assenza di una specifica valutazione (skill dedicata futura)
- Stesura di privacy policy verso interessati (art. 13/14 - skill dedicata futura)

## Avvertenza

Questa skill e' uno strumento di supporto alla redazione/verifica di documentazione di compliance privacy. **Non sostituisce il giudizio del DPO, del titolare del trattamento o del consulente legale.** Output orientativo che richiede revisione e firma del responsabile della compliance. Sanzioni amministrative ex art. 83 GDPR (fino a 20M euro o 4% del fatturato globale annuo) si applicano in caso di violazione - la skill non fornisce difesa legale.

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il task file appropriato:

- **Stesura Registro trattamenti**: l'utente chiede "redigi il registro", "compila il registro art. 30" -> leggi [`tasks/draft-registro-trattamenti.md`](tasks/draft-registro-trattamenti.md)
- **Verifica Registro esistente**: l'utente chiede "controlla questo registro", "e' completo?" -> leggi [`tasks/check-registro-trattamenti.md`](tasks/check-registro-trattamenti.md)
- **Valutazione soglia DPIA**: l'utente chiede "serve una DPIA?", "e' obbligatoria la valutazione di impatto?" -> leggi [`tasks/valuta-soglia-dpia.md`](tasks/valuta-soglia-dpia.md)
- **Stesura/verifica DPIA**: l'utente chiede "struttura la DPIA", "verifica questa DPIA" -> leggi [`tasks/draft-dpia.md`](tasks/draft-dpia.md)
- **Tracking pixel nelle e-mail**: l'utente chiede "usiamo pixel di tracciamento nelle newsletter", "come ci adeguiamo alle linee guida del Garante sui tracking pixel", "voce di registro per il tracciamento e-mail" -> leggi [`tasks/tracking-pixel-email.md`](tasks/tracking-pixel-email.md)

Se la richiesta e' generica ("aiutami con il GDPR"), chiedi all'utente quale delle cinque azioni vuole svolgere.

## Processo generale

1. Identifica la sotto-attivita' richiesta.
2. Carica il task file specifico.
3. Acquisisci dagli input dell'utente i dati necessari (organizzazione, finalita', categorie dati, ecc.).
4. Applica la procedura del task.
5. Produci output strutturato (registro, checklist, valutazione, struttura DPIA).
6. Concludi sempre con rinvio alla revisione del DPO o consulente legale.

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:
- Reg. UE 2016/679 (GDPR), in particolare art. 30, 35, 36
- Provvedimento Garante Privacy n. 467/2018 - Allegato 1 - 12 tipologie soggette a DPIA
- Provvedimento Garante Privacy n. 284/2026 - Linee guida tracking pixel nelle e-mail (GU n. 98 del 29/04/2026)
- WP248 rev. 01 - Linee guida DPIA (Article 29 Working Party, endorsed EDPB)
- D.Lgs. 196/2003 come modificato dal D.Lgs. 101/2018

Estratti testuali in [`references/estratti/`](references/estratti/).

## Limiti

Questa skill NON fa:
- Non fornisce consulenza legale; l'output e' di supporto, non vincolante
- Non analizza le specifiche misure tecniche di sicurezza (rinvio art. 32)
- Non valuta trasferimenti extra-UE caso per caso (richiede analisi adeguatezza Paese o SCC)
- Non produce documenti pronti al deposito presso il Garante senza revisione DPO/legale
- Non sostituisce la designazione del DPO ove obbligatorio (art. 37)

**Ogni documento prodotto richiede revisione del DPO o del consulente legale prima dell'adozione formale.**
