# Output atteso - check-profili-nazionali-italia

# Profili nazionali D.Lgs. 160/2026 - "TriageAssist"

**Data verifica**: 2026-09-27
**Sistema**: assegnazione priorità di pronto soccorso - alto rischio, Allegato III punto 5 lett. d
**Ruolo**: deployer (uso sotto la propria autorità in attività professionale, art. 3 n. 4 Reg. 2024/1689)
**Ente soggetto a D.Lgs. 231/2001**: SI (Srl con modello 231)

## Esito sintetico

| Area | Esposizione | Motivazione |
|---|---|---|
| Penale 437-bis c.p. | ALTA | Nessuna sorveglianza umana effettiva (art. 26 par. 2 / art. 14), in un contesto dove l'errore crea pericolo per la vita o l'incolumità individuale. La circolare che scoraggia le modifiche può essere letta come omissione **intenzionale** (c.4) |
| 231 art. 25-vicies | ALTA | 437-bis reato presupposto: 600-1000 quote + interdittive art. 9 c.2 lett. b)-e); modello 231 non aggiornato |
| Civile - prova (art. 17) | ALTA | Log dell'accesso già cancellati: se il giudice ne ordina l'esibizione, l'inadempimento sui registri art. 12 porta a ritenere ammessi i fatti allegati dal paziente |
| Civile - presunzione (art. 18) | ALTA | Violazione di obblighi AI Act (sorveglianza umana, conservazione log >= 6 mesi art. 26 par. 6): nesso causale presunto salvo prova contraria |
| Assicurazione (art. 20) | MEDIA | Richiesta del legale ricevuta 10 giorni fa: restano circa 20 giorni per rispondere; copertura dei danni da IA da verificare |
| Polizia (Titolo I) | N/A | - |

## Analisi

### Penale - art. 437-bis c.p.

- Il sistema è **ad alto rischio**, condizione necessaria del reato.
- La struttura non ha designato persone alla sorveglianza umana e ha chiesto di non modificare la priorità: le misure di
  sorveglianza umana sono di fatto omesse.
- Nel triage l'errore di priorità può creare **pericolo per la vita o l'incolumità individuale**: il caso concreto lo
  mostra.
- Il c.1 punisce "chiunque" ometta misure di sorveglianza umana, senza richiedere l'intenzionalità (con riduzione per
  colpa grave, c.3): la struttura può rientrarvi anche se la circolare non fosse ritenuta intenzionale.
- La struttura agisce come deployer. Il c.4 punisce inoltre l'**utilizzatore professionale** che omette **intenzionalmente** la
  sorveglianza umana, con le pene del c.1 (reclusione 1-5 anni). "Utilizzatore professionale" non è definito dal Reg.
  2024/1689: l'accostamento al deployer è un'**interpretazione** da far valutare a un penalista, così come
  l'intenzionalità della circolare.

### 231

Il 437-bis è reato presupposto: l'art. 25-vicies prevede per l'ente 600-1000 quote e le sanzioni interdittive dell'art.
9 c.2 lett. b), c), d), e) D.Lgs. 231/2001. I criteri generali di imputazione all'ente non sono coperti da questa skill
(rinvio all'organismo di vigilanza). Il modello 231 del 2022 non copre il processo.

### Civile

- **Art. 17**: il paziente deve rendere verosimile la domanda, anche nel collegamento tra la priorità assegnata e il
  danno. Se poi la struttura non esibisce i registri art. 12, il giudice ritiene ammessi i fatti allegati. La
  cancellazione dopo 30 giorni è anche una violazione dell'art. 26 par. 6 (almeno 6 mesi).
- **Art. 18**: il danno deriva da violazioni di obblighi AI Act, quindi il nesso causale è presunto salvo prova
  contraria.
- **Art. 19**: la marcatura CE e la dichiarazione di conformità di MedAlgo non escludono di per sé la responsabilità.
- **Art. 20**: la richiesta sull'assicurazione non è condizione di procedibilità, ma se la struttura non risponde entro
  30 giorni (esistenza della polizza, estremi, compagnia) il giudice può trarne argomenti di prova. Il paziente ha
  **azione diretta** verso l'assicuratore entro il massimale di 2 milioni; la struttura sarà litisconsorte necessaria.
- **Art. 16 c.4**: se il paziente agisce come consumatore, è competente anche il giudice del suo luogo di residenza.

## Azioni immediate (per priorità)

1. **Entro 20 giorni**: rispondere alla lettera ex art. 20 con esistenza, estremi e compagnia della polizza; denunciare
   il sinistro all'assicuratore e verificare se la polizza copre i danni da sistemi di IA.
2. **Subito**: sospendere la cancellazione automatica dei log e portare la conservazione ad almeno 6 mesi (art. 26 par.
   6); conservare ogni documento rimasto sull'accesso.
3. **Subito**: revocare la circolare. Designare persone alla sorveglianza umana con competenza, formazione e autorità
   di modificare la priorità (art. 26 par. 2), e documentare le modifiche.
4. **A breve**: aggiornare il modello 231 (mappatura del rischio 437-bis, protocollo sulla sorveglianza umana
   dei sistemi ad alto rischio).
5. Chiedere a MedAlgo la documentazione utile a difendersi (istruzioni d'uso, parametri di sorveglianza umana): è la
   stessa che il giudice può ordinare di esibire (art. 17 c.2 lett. d).

## Interpretazioni da validare

- Qualificazione della struttura come "utilizzatore professionale" (art. 437-bis c.4) e intenzionalità dell'omissione:
  parere penale.
- Data di entrata in vigore del D.Lgs. 160/2026: il decreto non la fissa, verificarla su Normattiva. Rileva per la
  disciplina applicabile ai fatti già avvenuti.

## Rinvio

- Penalista per il 437-bis; organismo di vigilanza 231; legale e broker assicurativo per la gestione del sinistro.
- Obblighi AI Act del deployer e FRIA: `check-deployer-obligations.md`.
