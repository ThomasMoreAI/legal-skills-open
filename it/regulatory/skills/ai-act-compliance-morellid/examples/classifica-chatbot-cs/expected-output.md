# Output atteso - classifica-sistema

# Classificazione AI Act - "AssistAI" Chatbot CS

**Data valutazione**: 2026-04-25
**Sistema valutato**: chatbot customer service basato su GPT-4 con RAG, integrato su e-commerce
**Organizzazione**: NegozioOnline Srl (ITA)

## Esito sintetico

**Classificazione del sistema integrato**: **TRASPARENZA art. 50** (rischio limitato)
- Categoria art. 50 par. 1: chatbot interagente con persone fisiche

**Classificazione del modello sottostante (GPT-4 di OpenAI)**: **GPAI con rischio sistemico** - obbligo di OpenAI, non di NegozioOnline

**Ruolo NegozioOnline**:
- **Provider del sistema "AssistAI"** (lo sviluppa e mette in servizio sotto proprio nome/marchio - art. 25 par. 1 puo' applicarsi)
- **Deployer del modello GPAI** GPT-4 (lo usa)

**Date di applicazione rilevanti** (post accordo provvisorio Digital Omnibus 7 maggio 2026):
- art. 50 par. 1 (disclosure chatbot - obbligo provider): **02/08/2026**
- art. 50 par. 2 (watermarking output sintetici a carico provider GPAI a monte): **02/12/2026** (rinviato di 4 mesi - Omnibus)
- art. 4 (AI literacy): **02/02/2025** - gia' applicabile

## Motivazione

### In scope dell'AI Act?
**SI**. AssistAI rientra nella definizione art. 3 par. 1 (sistema basato su macchine, autonomo, deduce output da input). Non e' tra le esclusioni art. 2.

### Pratica vietata art. 5?
**NO**. Il chatbot non rientra in nessuna delle 8 pratiche vietate:
- a) manipolazione: chatbot CS standard, no tecniche subliminali con danno significativo
- b) sfruttamento vulnerabilita': non target specifico
- c) social scoring: non valuta persone su comportamento sociale
- d) predictive policing: N/A
- e) scraping facciale: N/A
- f) emozioni in lavoro/istruzione: N/A (e-commerce)
- g) categorizzazione biometrica sensibile: N/A
- h) identificazione biometrica remota: N/A

### GPAI?
**NO** per il sistema AssistAI (e' un sistema specifico, non un modello generale).
**SI** per il modello sottostante GPT-4 - ma e' obbligo del fornitore (OpenAI), non di NegozioOnline.

### High-risk?
**NO**. Verifiche:

- Via 1 (art. 6 par. 1 + Allegato I): N/A. Il chatbot non e' componente di sicurezza di prodotto regolamentato.
- Via 2 (art. 6 par. 2 + Allegato III): nessuno degli 8 settori si applica:
  - 1 Biometria: no
  - 2 Infrastrutture critiche: no
  - 3 Istruzione: no
  - 4 Occupazione/HR: no
  - 5 Servizi essenziali: no (e-commerce non e' "servizio pubblico essenziale" ne' credit scoring ne' insurance)
  - 6 Contrasto: no
  - 7 Migrazione: no
  - 8 Giustizia/elezioni: no

### Trasparenza art. 50?
**SI - Categoria A (sistema interagente con persone fisiche)**.
Il chatbot AssistAI interagisce con clienti finali. NegozioOnline come provider deve garantire che gli utenti siano informati di interagire con AI.

Eccezione "ovvieta'" applicabile? Probabilmente parzialmente - il fatto che sia un assistente AI puo' essere ovvio se ben labelizzato, ma una persona ragionevole potrebbe inizialmente confondere. **Buona pratica: rendere ovvio**.

### Categoria art. 50 par. 2 (generazione contenuti)?
Le risposte del chatbot sono testuali e potrebbero rientrare in "contenuti generati artificialmente". Tuttavia:
- L'art. 50 par. 2 mira principalmente a "deepfake", AI-generated media (audio/immagine/video)
- Per il testo, par. 4 bis si applica solo a "testo pubblicato per informare il pubblico su questioni di interesse pubblico", che non e' il caso di un chatbot CS
- Conclusione: par. 2 (marcatura machine-readable) **non si applica** in modo significativo qui

### Categoria art. 50 par. 4 bis (testo per informazione pubblica)?
**NO**. Conversazione 1-a-1 con utente, non testo pubblicato per informare il pubblico.

## Obblighi applicabili a NegozioOnline

### Come provider del sistema AssistAI
1. **Trasparenza art. 50 par. 1**: garantire che gli utenti sappiano di interagire con AI
2. **AI literacy art. 4** (gia' in vigore dal 02/02/2025): garantire un livello adeguato di alfabetizzazione AI tra il personale che usa/sviluppa il sistema

### Come deployer del modello GPT-4
1. **Conformita' alle istruzioni d'uso e ai termini di OpenAI** (le condizioni che OpenAI da' per l'uso del modello includono limitazioni di responsabilita')
2. **NO obblighi specifici art. 26-27** (quelli si applicano solo a deployer di sistemi high-risk)

### Sinergie GDPR (probabilmente piu' rilevanti)
- **Registro art. 30** GDPR per il trattamento "supporto clienti via AI" (vedi skill `gdpr-registro-dpia`)
- **Valutazione DPIA** (vedi `gdpr-registro-dpia` task `valuta-soglia-dpia`):
  - Trattamento online via app: tipologia 3 Garante? Possibile ma non automatica
  - Tecnologie innovative (AI): tipologia 7 + altro criterio
  - **Probabile DPIA RACCOMANDATA**, da approfondire
- **Trasferimento extra-UE**: GPT-4 e' di OpenAI USA; tramite API i dati cliente fluiscono a OpenAI. Servono SCC + TIA + verifica DPF UE-USA + scelta data residency UE se possibile

### Eccezione interessante: testo pubblicato + revisione editoriale
N/A - chatbot e' interazione 1-a-1, non pubblicazione

## Pattern raccomandati per compliance art. 50

1. **Onboarding chatbot**: prima frase: "Ciao, sono AssistAI, l'assistente virtuale di NegozioOnline. Posso aiutarti con info ordini, resi, prodotti."
2. **Label visibile**: icona "AI" accanto al nome del bot in chat
3. **Risposta sincera**: se l'utente chiede "sei umano?", il bot risponde "No, sono un assistente AI"
4. **Footer**: "Powered by AI - per richieste complesse, posso passare a un operatore umano"
5. **Privacy notice**: link informativa GDPR + comunicazione che le conversazioni sono usate solo per il servizio (non training del modello)
6. **Accessibilita'**: testo chiaro, non gergo tecnico

## Sinergia con GDPR

Per dati personali nel sistema (anagrafica clienti + storico ordini + conversazioni), attivare la skill `gdpr-registro-dpia`:
- Trattamento "Supporto clienti via AI" da inserire nel Registro art. 30
- DPIA da valutare (probabile RACCOMANDATA per uso di AI/innovative tech in modo strutturale)
- Trasferimento extra-UE OpenAI USA: SCC + TIA + valutazione DPF

## Limiti di questa classificazione

- La classificazione potrebbe cambiare se il sistema evolve verso decisioni automatizzate con effetti giuridici (es. blocchi account, rimborsi automatici).
- Linee guida Commissione su art. 6 (in preparazione, scadenza 02/02/2026) potrebbero precisare alcuni casi.
- Norme nazionali italiane in via di sviluppo (Garante, AgID) potrebbero aggiungere requisiti.

## Rinvio al consulente legale

**Pur trattandosi di un caso a rischio limitato, raccomandato consultare**:
- Consulente legale per validare classificazione (in particolare l'eccezione "ovvieta'")
- DPO (interno o esterno) per Registro/DPIA GDPR collegati
- Esperto cyber per valutazione integrazione API OpenAI (data leakage, prompt injection, ecc.)

Sanzioni potenziali: trasparenza art. 50 viola = fino a 15M EUR o 3% fatturato.

## Prossimi step suggeriti per NegozioOnline

1. Implementare i 6 pattern di compliance trasparenza prima del go-live
2. Aggiornare Registro GDPR per il nuovo trattamento (skill `gdpr-registro-dpia`)
3. Valutare DPIA (skill `gdpr-registro-dpia` task `valuta-soglia-dpia`)
4. Documentare la valutazione AI Act svolta con questa skill (anche per eventuale verifica autorita')
5. Pianificare AI literacy training per il team CS (art. 4 - gia' applicabile)
