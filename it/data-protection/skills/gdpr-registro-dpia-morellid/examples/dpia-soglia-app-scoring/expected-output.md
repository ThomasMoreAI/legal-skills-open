# Output atteso - valuta-soglia-dpia

# Valutazione soglia DPIA - "CreditScore Pro"

**Data valutazione**: 2026-04-25
**Trattamento valutato**: Sistema di scoring affidabilita' creditizia con decisioni automatizzate
**Titolare**: FinanziaSubito Srl

## Esito

**DPIA OBBLIGATORIA**

Motivazione: il trattamento rientra **simultaneamente** in piu' tipologie esplicitamente previste dal Garante italiano (Provv. 467/2018) e in piu' criteri WP248 rev. 01. Inoltre, e' espressamente catturato dall'art. 35 par. 3 lett. a) GDPR.

## Motivazione

### Tipologie italiane Provv. Garante 467/2018

| Tipologia | Applicabile? | Note |
|-----------|--------------|------|
| **1 - Scoring/profilazione su larga scala** | **SI** | Il sistema fa esplicitamente scoring e profilazione predittiva (situazione economica, affidabilita', comportamento), 60.000 interessati/anno = larga scala. |
| **2 - Decisioni automatizzate con effetti giuridici** | **SI** | L'erogazione/diniego del prestito incide significativamente sull'interessato (impossibilita' di ottenere il bene/servizio). E' esattamente il caso citato come esempio nella tipologia 2 (screening clienti banca centrali rischi). |
| 3 - Monitoraggio sistematico online/app | SI | App con tracking comportamentale, geolocalizzazione, identificativi univoci |
| 4 - Dati estremamente personali su larga scala | Parziale | Dati finanziari rientrano (rischio frodi). Larga scala soddisfatta. |
| 5 - Controllo dipendenti | NO | Non applicabile |
| 6 - Soggetti vulnerabili | Borderline | Non specifico, ma persone in difficolta' finanziaria possono essere vulnerabili |
| **7 - Tecnologie innovative + altro criterio** | **SI** | ML/AI proprietario + tipologia 1 e 2 - rientra perfettamente (AI + altro criterio) |
| 8 - Scambio dati tra titolari | SI | Centrali rischi (CRIF, Experian, CTC) + PA (Agenzia Entrate, INPS) sono titolari distinti |
| **9 - Interconnessione di dataset** | **SI** | Il modello incrocia anagrafici + finanziari + reddituali + centrali rischi + PA + comportamentali |
| 10 - Cat. particolari interconnesse | Borderline | Condanne penali se dichiarate (art. 10) interconnesse con altri dati |
| 11 - Biometrici sistematici | NO | Non dichiarati |
| 12 - Genetici sistematici | NO | Non applicabile |

**Tipologie attivate (primarie)**: 1, 2, 7, 9 (4 tipologie esplicite)

**Anche solo 1 sola tipologia** rende la DPIA obbligatoria in Italia. **Quattro contemporaneamente** rende la decisione blindatissima.

### Criteri WP248 rev. 01

| Criterio | Soddisfatto? | Note |
|----------|--------------|------|
| **1 - Scoring/profilazione** | **SI** | Esplicito (modello ML produce score 0-1000) |
| **2 - Decisioni automatizzate con effetti giuridici** | **SI** | Erogazione automatica del prestito |
| **3 - Monitoraggio sistematico** | **SI** | Tracking app + identificativi |
| 4 - Dati sensibili o altamente personali | SI | Dati finanziari di natura altamente personale |
| **5 - Larga scala** | **SI** | 60.000 interessati/anno, ambito nazionale |
| **6 - Combinazione/raffronto dataset** | **SI** | Multi-source: anagrafici + finanziari + centrali rischi + PA + comportamentali |
| 7 - Vulnerabili | Borderline | Non e' criterio centrale ma elemento di attenzione |
| **8 - Tecnologie innovative** | **SI** | ML proprietario, decisioni automatizzate |
| **9 - Trattamenti che impediscono uso servizio/contratto** | **SI** | Decisione di rifiuto blocca l'accesso al prestito |

**7 criteri WP248 soddisfatti su 9** (la soglia e' 2). Il caso e' **estremamente al di sopra** della soglia di obbligatorieta'.

### Casi espliciti art. 35 par. 3 GDPR

- **lett. a)** valutazione sistematica e globale di aspetti personali basata su trattamento automatizzato (profilazione), su cui si fondano decisioni con effetti giuridici/analoghi: **SI** - questo e' esattamente il caso in esame
- lett. b) trattamento su larga scala di cat. particolari art. 9: NO (non sanitari)
- lett. c) sorveglianza sistematica zona pubblica: NO

L'art. 35 par. 3 lett. a) **da solo** rende DPIA obbligatoria.

### Esenzioni art. 35 par. 10

NON applicabili. Il trattamento non e' fondato su obbligo legale o interesse pubblico, ma su rapporto contrattuale con il cliente.

## Raccomandazione

**Procedere con DPIA strutturata PRIMA dell'avvio del trattamento.** Vedi task `draft-dpia.md`.

Punti di attenzione specifici per la DPIA di questo caso:

1. **Diritto a revisione umana significativa** (art. 22 par. 3): documentare con quali criteri scattano revisioni umane (oggi solo "fasce di confine" 400-600). Valutare se basta o serve estensione.

2. **Bilanciamento legittimo interesse** (art. 6.1.f) per antifrode: deve essere documentato (LIA - Legitimate Interest Assessment) come parte della DPIA.

3. **Trasparenza dell'algoritmo** (art. 22 par. 2 lett. a) + Cons. 71): l'interessato ha diritto a conoscere "informazioni significative sulla logica utilizzata". Un modello XGBoost+LSTM proprietario richiede strategia di explainability.

4. **Bias mitigation**: il dataset di training non deve produrre discriminazioni (cfr. Garante - sanzioni per bias in modelli HR).

5. **Trasferimenti extra-UE**: anche se AWS Frankfurt e' UE, valutare con TIA il backup USA.

6. **Centrali rischi + PA**: ciascuna interazione deve avere base giuridica autonoma e rispettare i protocolli specifici (es. CRIF Codice di Condotta).

7. **Diritti degli interessati art. 13/14**: informativa specifica con tutti i dettagli su scoring e decisione automatizzata. Valutare consulto preventivo art. 36 in fase di progettazione.

8. **DPO consultato**: obbligatorio art. 35 par. 2.

9. **Possibile consultazione preventiva Garante** (art. 36): se la DPIA evidenzia rischi residui elevati anche dopo misure, scattare consultazione PRIMA dell'avvio.

## Limiti di questa valutazione

- Si basa sulle informazioni fornite. Cambiamenti significativi (es. include dati sanitari, riduzione drastica scala) richiederebbero nuova valutazione.
- La valutazione completa dei rischi residui spetta alla DPIA effettiva.
- Il giudizio finale sulla necessita' di consultazione preventiva del Garante (art. 36) emerge dalla DPIA, non da questa pre-valutazione.

## Rinvio al DPO

**La consultazione del DPO e' obbligatoria** quando il titolare svolge una DPIA (art. 35 par. 2). Il presente report di soglia e' di supporto, non sostituisce la valutazione del DPO o del consulente privacy specialistico (in particolare per le specificita' del settore creditizio - vigilanza Banca d'Italia, Codice di Condotta CRIF, Codice di deontologia dei sistemi informativi creditizi del Garante).
