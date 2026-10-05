# Task: Stesura/verifica DPIA (art. 35 par. 7 GDPR)

Struttura una Valutazione d'Impatto sulla protezione dei dati (DPIA) o verifica una DPIA esistente, secondo i contenuti minimi dell'art. 35 par. 7 GDPR e le linee guida WP248 rev. 01.

## Obiettivo

Produrre una DPIA conforme con i 4 contenuti minimi obbligatori, articolati nelle sezioni operative tipiche delle DPIA italiane.

Pre-requisito: aver gia' eseguito `valuta-soglia-dpia.md` per stabilire che la DPIA e' richiesta.

## Input richiesti

- Nome / descrizione del trattamento
- Tipologia (tipologie Garante + criteri WP248 applicabili - dall'output di valuta-soglia-dpia.md)
- Finalita', base giuridica, categorie interessati, categorie dati
- Categorie destinatari, trasferimenti extra-UE
- Tecnologie usate, processi tecnici sottostanti
- Misure di sicurezza tecniche e organizzative gia' in atto
- Eventuali consultazioni con interessati (rappresentanti, sindacato, ecc.)

## Fonti

Leggere prima:
- `references/estratti/gdpr-art-35-36.md` - art. 35 par. 7 (4 contenuti minimi) + criteri WP248
- `references/estratti/garante-allegato1-prov467-2018.md` - 12 tipologie italiane

## Procedura

### Passo 1 - Sezione 1: Descrizione sistematica del trattamento (art. 35 par. 7 lett. a)

Includere:

- **Identificazione titolare e contitolari** (intestazione)
- **Nome/finalita' del trattamento** (allineata al Registro art. 30)
- **Base giuridica** (art. 6 + art. 9 se categorie particolari)
- **Descrizione del flusso dati**:
  - Come arrivano i dati (raccolta diretta? indiretta? terze parti?)
  - Dove vengono memorizzati (DB, datacenter, cloud, location)
  - Chi puo' accedervi (ruoli, profili, autorizzazioni)
  - Per quanto tempo vengono conservati
  - Come vengono cancellati / anonimizzati
- **Mappatura tecnica**:
  - Componenti software/hardware
  - Architettura (es. monolitico, microservizi, edge)
  - Tecnologie sensibili (AI/ML, biometria, IoT, video, geolocalizzazione)
  - Provider esterni e ruolo (responsabile, contitolare, autonomo titolare)
- **Trasferimenti extra-UE** se presenti
- **Decisioni automatizzate** (art. 22) se applicabili

Format raccomandato: tabella o flowchart testuale. Dettaglio tecnico piu' alto del Registro art. 30.

### Passo 2 - Sezione 2: Necessita' e proporzionalita' (lett. b)

Per ciascuna scelta progettuale, giustificare:

- **Necessita'**: il dato/funzione e' davvero necessario per la finalita'? Si potrebbe usare un dato meno invasivo?
- **Proporzionalita'**: l'intrusivita' nel diritto alla protezione dei dati e' proporzionata al beneficio per la finalita'?
- **Minimizzazione** (art. 5 par. 1 lett. c): si raccolgono solo i dati strettamente necessari?
- **Limitazione finalita'** (art. 5 par. 1 lett. b): non c'e' uso secondario non compatibile?

Esempio: per un sistema HR con video-sorveglianza, valutare alternative meno invasive (es. controlli campionari senza video, badge tracciabili, audit periodici).

### Passo 3 - Sezione 3: Valutazione dei rischi (lett. c)

Identificare:

- **Sorgenti di rischio**: chi potrebbe causare problemi? (operatore interno disonesto? attaccante esterno? errore di programmazione? terzo non autorizzato?)
- **Eventi temuti**: cosa potrebbe accadere? (data breach, accesso non autorizzato, alterazione, perdita, divulgazione)
- **Conseguenze per gli interessati**: discriminazione, danno reputazionale, perdita finanziaria, furto identita', impossibilita' di esercitare diritti, ecc.
- **Probabilita'** (1-4: trascurabile, limitata, significativa, massima)
- **Gravita'** (1-4: trascurabile, limitata, significativa, massima)
- **Rischio inerente** = matrice probabilita' x gravita'

Per ciascun evento di rischio, una riga di matrice. Utile la tabella:

| ID | Evento di rischio | Sorgente | Conseguenza per interessati | Probabilita' | Gravita' | Rischio inerente |
|----|---|---|---|---|---|---|
| R1 | Data breach via attacco SQL injection | Esterno | Divulgazione dati personali, possibile furto identita' | 2 | 3 | 6 (medio-alto) |
| R2 | Accesso non autorizzato da operatore interno | Interno | Accesso a dati sensibili colleghi | 2 | 4 | 8 (alto) |
| ... |

### Passo 4 - Sezione 4: Misure per affrontare i rischi (lett. d)

Per ciascun rischio identificato in passo 3, individuare misure:

- **Misure tecniche**:
  - Cifratura (at rest, in transit)
  - Pseudonimizzazione / anonimizzazione
  - Controllo accessi (RBAC, ABAC, MFA)
  - Logging e monitoring (SIEM)
  - Penetration test, vulnerability assessment
  - Backup e disaster recovery
  - Cancellazione sicura
  - Misure specifiche per AI (explainability, fairness, robustness)

- **Misure organizzative**:
  - Policy GDPR aziendale
  - Formazione dipendenti
  - NDA con terze parti
  - Audit periodici
  - Procedura incident response (entro 72h art. 33)
  - Designazione DPO (se obbligatorio art. 37)
  - Privacy by Design / Privacy by Default (art. 25)

Per ciascun rischio R1, R2, ..., riportare:

| Rischio | Misura preventiva | Misura mitigativa | Rischio residuo |
|---------|-------------------|-------------------|-----------------|
| R1 | WAF + parametrizzazione query | Logging + alert + IR plan | 3 (medio-basso) |
| R2 | RBAC + audit log + 4-eyes | Alert + revisione mensile log | 4 (medio) |

### Passo 5 - Consultazione interessati (par. 9)

Se applicabile, descrivere:
- Modalita' di consultazione (sondaggio, focus group, rappresentanti sindacali, comitato etico)
- Risultati raccolti
- Come sono stati incorporati nel trattamento

Se non e' stata fatta consultazione, motivarlo (es. "tutela degli interessi commerciali").

### Passo 6 - Conclusione e parere DPO

- Sintesi dei rischi residui dopo le misure
- Soglia di accettabilita': il rischio residuo e' accettabile o servono misure aggiuntive?
- Se il rischio residuo resta **elevato in assenza di misure aggiuntive non implementabili**, scatta l'obbligo di **consultazione preventiva del Garante (art. 36)** prima di iniziare il trattamento
- **Parere del DPO** (obbligatorio art. 35 par. 2): allegato firmato

### Passo 7 - Output strutturato

```markdown
# DPIA - Valutazione d'impatto sulla protezione dei dati

## Identificazione

**Titolare del trattamento**: [...]
**Trattamento valutato**: [...]
**Data DPIA**: [...]
**Versione**: [v1.0 - bozza per revisione DPO]
**DPO consultato**: [Si/No, nome se Si]

## 1. Descrizione sistematica del trattamento (art. 35 par. 7 lett. a)

[testo + flowchart + tabella mappatura tecnica]

## 2. Necessita' e proporzionalita' (lett. b)

[motivazione per ogni scelta progettuale rispetto a alternative meno invasive]

## 3. Valutazione dei rischi (lett. c)

| ID | Evento | Sorgente | Conseguenze | Probabilita' | Gravita' | Rischio inerente |
|----|---|---|---|---|---|---|
| ... |

## 4. Misure per affrontare i rischi (lett. d)

| Rischio | Misura preventiva | Misura mitigativa | Rischio residuo |
|---|---|---|---|
| ... |

## 5. Consultazione interessati

[Se effettuata: modalita' + risultati + impatto. Se non effettuata: motivazione]

## 6. Conclusioni

**Rischio residuo complessivo**: [Trascurabile / Basso / Medio / Alto]

**Esito**:
- [ ] Trattamento procedibile con misure descritte
- [ ] Consultazione preventiva del Garante richiesta (art. 36)
- [ ] Trattamento da rivalutare prima di procedere

## 7. Parere del DPO

[allegato firmato]

## Avvertenze

- DPIA e' documento di accountability del titolare ex art. 5 par. 2 + 35 GDPR.
- Va riesaminata in caso di variazioni (art. 35 par. 11).
- Va archiviata e messa a disposizione dell'autorita' di controllo su richiesta.
- La presente bozza richiede revisione formale del DPO e del consulente legale prima dell'adozione.

## Sanzioni di riferimento

Mancata DPIA quando obbligatoria: fino a 10M EUR o 2% fatturato globale annuo (art. 83 par. 4 GDPR).
```

## Verifica DPIA esistente (modalita' check)

Se l'utente fornisce una DPIA gia' redatta da verificare, applicare la procedura come check:

1. Verifica presenza dei 4 contenuti minimi (par. 7 lett. a-d)
2. Verifica struttura e completezza per ciascuna sezione
3. Verifica che il parere DPO sia allegato
4. Verifica matrice rischi-misure-rischio residuo
5. Identifica gap e raccomandazioni

## Casi limite

### Trattamento gia' avviato senza DPIA
La DPIA va fatta comunque, retroattivamente, e documentata. Non e' difesa "non l'avevamo pensata".

### Modifiche significative al trattamento
Riesaminare la DPIA esistente e aggiornarla. Cambia: tecnologia di base, scala, finalita', categorie dati, soggetti coinvolti.

### Cluster di trattamenti simili
L'art. 35 par. 1 consente una **singola** DPIA per **un insieme di trattamenti simili che presentano rischi elevati analoghi**. Utile per una piattaforma multi-tenant.

### DPIA con esito "consultazione preventiva richiesta"
Se i rischi residui restano elevati anche con misure, e' OBBLIGATORIO consultare il Garante prima di iniziare (art. 36 par. 1). Il Garante ha 8 settimane (prorogabili a 14) per parere.

## Limiti di questo task

- La struttura e' di supporto. La sostanza tecnica (specifiche misure, valutazione rischio) richiede competenze di dominio (legale, tecnico, di sicurezza) che la skill non sostituisce.
- Non sostituisce il parere obbligatorio del DPO (art. 35 par. 2).
- Non valuta la conformita' a settori specifici (sanita', telecom, banche) che possono avere requisiti aggiuntivi.

## Esempi

Vedi `examples/`:
- `dpia-richiesta-app-profilazione/` - DPIA per sistema scoring clienti
