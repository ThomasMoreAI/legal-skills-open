# Estratto: D.Lgs. 9 settembre 2026, n. 160 - profili nazionali italiani dell'AI Act

**Fonte**: `sources.yaml` id `dlgs-160-2026-gu214` (trascrizione in `references/fonti/dlgs-160-2026.md`)
**Pubblicazione**: GU Serie Generale n. 214 del 15/09/2026, pp. 1-10
**Data consultazione**: 2026-09-27
**Hash SHA256**: `5da3dde091e115ec02a9275ad13455f83c478d4eb256d912d9f8e132c7779e75`

Decreto delegato ex art. 24 L. 132/2025. Non modifica gli obblighi del Reg. (UE) 2024/1689: aggiunge **conseguenze
penali, 231 e civili** alla loro violazione in Italia e disciplina l'uso dell'IA da parte delle Forze di polizia.

> **Entrata in vigore**: il decreto non contiene un articolo sull'entrata in vigore e non fissa alcuna data. Verificare
> la data su Normattiva prima di indicarla nell'output.

## 1. Definizioni (art. 11)

Per il Titolo II (penale e civile) valgono le definizioni dell'art. 3 del Reg. 2024/1689 (fornitore, deployer, sistema
di IA, immissione sul mercato, ecc.).

## 2. Reato di omessa sicurezza e alterazione di sistemi IA ad alto rischio (art. 12 -> art. 437-bis c.p.)

| Comma | Condotta | Evento di pericolo | Pena |
|---|---|---|---|
| 1, primo periodo | **Chiunque** omette le misure tecniche di sicurezza previste per progettazione, addestramento, produzione, immissione sul mercato di sistemi IA **ad alto rischio**, idonee a prevenire malfunzionamenti o alterazioni, **ovvero** omette misure di sorveglianza umana | pericolo per la vita o l'incolumità pubblica o individuale | reclusione 1-5 anni |
| 1, secondo periodo | stesse condotte | pericolo per la sicurezza dello Stato | reclusione 2-8 anni |
| 2 | Chiunque, fuori dai casi del c.1, **altera** sistemi IA ad alto rischio (salvo più grave reato) | vita o incolumità pubblica o individuale / sicurezza dello Stato | 2-6 anni / 3-10 anni |
| 3 | fatti del c.1 commessi per **colpa grave** | - | pena ridotta da un terzo a un sesto |
| 4 | **Utilizzatore professionale** di sistemi IA ad alto rischio che omette **intenzionalmente** misure di sorveglianza umana | vita o incolumità / sicurezza dello Stato | pene del c.1 (1-5 / 2-8 anni) |

Punti di attenzione (testuali):
- Il reato richiede un **pericolo concreto derivato** dall'omissione ("quando da tali omissioni derivi pericolo"): la
  sola non conformità documentale non basta.
- Le misure omesse sono quelle "previste" per le fasi di progettazione-immissione: il rinvio naturale sono i requisiti
  del capo III, sez. 2, del Reg. 2024/1689 (in particolare artt. 14-15). Il testo non elenca gli articoli: il collegamento
  è un'interpretazione.
- "Utilizzatore professionale" non è un termine definito dall'art. 3 del Reg. 2024/1689; la figura più vicina è il
  **deployer** (uso sotto la propria autorità, fuori da attività personale non professionale, art. 3 n. 4).
  **Interpretazione da segnalare**, non equivalenza testuale.
- Il c.1 si riferisce a "chiunque" e, nella parte "ovvero omette di adottare misure di sorveglianza umana", non è
  testualmente limitato al fornitore né richiede l'intenzionalità: può riguardare anche il deployer. Il c.4 prevede in
  aggiunta l'ipotesi specifica dell'utilizzatore professionale che omette **intenzionalmente** la sorveglianza umana.
- Il c.3 (colpa grave) richiama solo i fatti del **primo comma**, non il c.4.

## 3. Responsabilità degli enti (art. 15 -> art. 25-vicies D.Lgs. 231/2001)

- Reato 437-bis c.p.: sanzione pecuniaria **600-1000 quote**.
- Reato 612-quater c.p.: sanzione pecuniaria **200-700 quote** (il decreto non descrive la fattispecie del 612-quater).
- In entrambi i casi: **sanzioni interdittive** dell'art. 9, c.2, lett. b), c), d), e) D.Lgs. 231/2001.

Conseguenza operativa: il 437-bis entra nel catalogo dei reati presupposto; il modello 231 di fornitori e deployer di
sistemi IA ad alto rischio va aggiornato.

## 4. Azioni civili di risarcimento (artt. 16-20)

**Ambito (art. 16)**
- Art. 17 (accesso alle prove): ogni azione di risarcimento, contrattuale o extracontrattuale, per danno "cagionato
  nell'utilizzo di un sistema di intelligenza artificiale" (qualsiasi livello di rischio).
- Artt. 18-19 (presunzione e irrilevanza della sola conformità): solo quando il danno **deriva dalla violazione di uno o
  più obblighi del Reg. 2024/1689**.
- Restano fermi l'art. 82 GDPR e la normativa nazionale di recepimento della Dir. (UE) 2024/2853 (prodotti difettosi).
- Consumatore danneggiato: competente anche il giudice di residenza o domicilio del danneggiato.

**Accesso alle prove (art. 17)**
- Su istanza del danneggiato che rende **verosimile** la domanda (anche il collegamento output-danno), il giudice ordina
  alla controparte o al terzo l'esibizione degli elementi di prova pertinenti sul funzionamento del sistema.
- Rientrano espressamente (c.2): **a)** registri art. 12 (log); **b)** documentazione del sistema di gestione dei rischi
  art. 9; **c)** informazioni pertinenti della documentazione tecnica art. 11; **d)** parametri e modalità di
  supervisione umana art. 14.
- Ordine limitato a quanto necessario e proporzionato; tutela dei segreti commerciali (art. 121-ter CPI).
- Inadempimento della parte: argomenti di prova (art. 116 c.p.c.); **se riguarda i documenti del c.2, il giudice
  ritiene ammessi i fatti allegati dall'istante** (valutato ogni altro elemento).
- Inadempimento del terzo: pena pecuniaria da 1.500 a 10.000 EUR.

**Presunzione del nesso causale (art. 18)**: se il danno deriva dalla violazione di obblighi del Reg. 2024/1689, il
nesso di causalità tra violazione e danno è **presunto, salvo prova contraria**. Il testo non limita la presunzione a un
ruolo specifico (fornitore, deployer, ecc.): vale per il convenuto a cui è imputata la violazione.

**Conformità (art. 19)**: la conformità al Reg. 2024/1689, **anche se certificata** (capo III, sez. 5), non esclude di
per sé la responsabilità del convenuto.

**Assicurazione (art. 20)**
- Prima dell'azione il danneggiato può chiedere al presunto responsabile se ha una polizza RC per quel danno (non è
  condizione di procedibilità). Risposta **entro 30 giorni** con esistenza della polizza, estremi e compagnia. Omessa o
  incompleta risposta: argomenti di prova.
- **Azione diretta** contro l'assicuratore, nei limiti del massimale; opponibili le eccezioni contrattuali anteriori al
  sinistro; rivalsa dell'assicuratore verso l'assicurato; il responsabile è **litisconsorte necessario**; stessa
  prescrizione dell'azione verso il responsabile.

## 5. Forze di polizia (Titolo I, artt. 1-10, e art. 21)

- **Nessun nuovo obbligo** rispetto al Reg. 2024/1689 per i sistemi usati per finalità di polizia (art. 1 c.3; art. 3
  c.7).
- **Revisione umana qualificata** degli output prima del loro impiego in atti e provvedimenti incidenti sulla sfera
  giuridica degli interessati, documentata per la tracciabilità (art. 3 c.4); sorveglianza umana effettiva ex art. 14
  per l'alto rischio, con personale competente e formato (art. 3 c.5).
- Collaborazioni di ricerca con privati: clausole che escludono la condivisione di dati operativi sensibili e l'uso da
  parte del privato di sistemi addestrati per la polizia (salvo dati sintetici o pseudonimizzati); modelli addestrati su
  dati operativi sensibili di titolarità delle Forze di polizia (art. 4).
- Identificazione biometrica remota **in tempo reale** per prevenzione e ricerca di scomparsi o vittime (art. 8):
  autorizzazione del procuratore della Repubblica del capoluogo di distretto, massimo 15 giorni prorogabili di 15;
  urgenza con richiesta entro 24 ore e decisione nelle 24 ore successive; banca dati di riferimento formata per ogni
  utilizzo e cancellata a fine autorizzazione; **vietate banche dati alimentate con scraping non mirato**; in caso di
  violazione stop, cancellazione, risultati inutilizzabili.
- Per lo stesso uso (art. 8 o art. 359-ter c.p.p.): **FRIA preventiva** ex art. 27 e DPIA ex artt. 23-24 D.Lgs.
  51/2018; log non modificabili conservati 5 anni; notifica al Garante dopo l'uso previo nulla osta giudiziario (art. 9).
- Uso in procedimento penale (art. 13 -> art. 359-ter c.p.p.): delitti dell'allegato II al Reg. 2024/1689 puniti con
  reclusione non inferiore nel massimo a 4 anni, latitanti, vittime; autorizzazione del GIP, 15 giorni prorogabili.
- Videosorveglianza con riconoscimento facciale **a posteriori** (art. 10): autorizzazione GIP chiesta entro 48 ore
  dall'avvio e decisa nelle 48 successive, salvo identificazione iniziale dopo un reato (art. 26 par. 10 AI Act);
  titolare Ministero dell'interno - Dipartimento PS; dati conservati 7 giorni; log 5 anni; nessuna decisione con effetti
  giuridici negativi basata unicamente sul riconoscimento facciale; vietato l'uso non mirato. **Gestori di luoghi e
  organizzatori di eventi** possono installare e manutenere le componenti IA, concesse in comodato gratuito alla
  questura (c.13).
- **Transitorio (art. 21)**: sistemi già in uso, in contratto, in sviluppo o sperimentazione per finalità di polizia
  resi compatibili con il capo II del Titolo I (artt. 3-6) **entro un anno** dall'entrata in vigore del decreto; per le
  disposizioni che dipendono dal Reg. 2024/1689 valgono i termini di quest'ultimo.
