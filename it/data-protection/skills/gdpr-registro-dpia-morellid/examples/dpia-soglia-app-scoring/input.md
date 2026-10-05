# Esempio - input per valuta-soglia-dpia (app di scoring credito)

> Sintetico, fittizio. Test della skill su un caso paradigmatico di trigger DPIA.

## Trattamento da valutare

**Nome**: Sistema "CreditScore Pro" - scoring affidabilita' creditizia per richieste di prestiti personali

**Titolare del trattamento**: FinanziaSubito Srl (fictional fintech italiana)

## Descrizione

L'azienda offre tramite app mobile la possibilita' a privati cittadini di richiedere prestiti personali fino a EUR 30.000. Per valutare l'affidabilita' creditizia, il sistema:

1. Raccoglie dati anagrafici, fiscali (CF), reddituali (busta paga, dichiarazione redditi via SPID)
2. Acquisisce dati da centrali rischi (CRIF, Experian, CTC) e Pubblica Amministrazione (Agenzia Entrate via SDI fattura, INPS posizione contributiva)
3. Analizza dati comportamentali raccolti dall'app (usage pattern, login times, device fingerprint)
4. Applica un **modello machine learning proprietario** che produce uno score 0-1000 di affidabilita'
5. Sulla base dello score, **decide automaticamente** l'erogazione (accept/reject) o invia a revisione umana

## Caratteristiche del trattamento

- **Volume**: ~5.000 richieste/mese, target 60.000/anno
- **Effetto delle decisioni**: l'erogazione/non erogazione del prestito e' decisione con effetti giuridici e finanziari rilevanti per l'interessato
- **Categorie di interessati**: persone fisiche maggiorenni (18-75 anni), residenti in Italia
- **Categorie di dati**:
  - Anagrafici: nome, CF, indirizzo, telefono, email
  - Finanziari: reddito, patrimonio, debiti, affidabilita' creditizia
  - Comportamentali: pattern uso app, geolocalizzazione, device data
  - **NON dati sanitari** (esplicitamente esclusi)
  - **Eventualmente** condanne penali (se l'utente le dichiara nella richiesta)
- **Trattamenti automatizzati**: si', con possibilita' di revisione umana solo per score nelle "fasce di confine" (es. score 400-600)
- **Profilazione**: si', il modello ML costruisce un profilo predittivo
- **Tecnologie**: ML proprietario (XGBoost + LSTM), provider cloud AWS Frankfurt
- **Trasferimenti extra-UE**: backup AWS in regioni multiple, possibile transito USA -> SCC
- **Base giuridica**: art. 6.1.b) (contrattuale - richiesta del cliente) + 6.1.f) (legittimo interesse per antifrode) + art. 22 par. 2 lett. a) (decisione automatizzata necessaria per conclusione contratto, con misure di tutela)

## Domanda

E' obbligatoria la DPIA prima di avviare il trattamento?
