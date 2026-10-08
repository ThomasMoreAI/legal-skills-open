# Estratto: AI Act Art. 50 - Obblighi di trasparenza

**Fonte**: `sources.yaml` id `ai-act-it-eurlex`
**Data consultazione**: 2026-04-25
**Hash SHA256**: a61b61706aee6676e3988ab696162d71d759c3debd48b2ecccac3555207f2b0c

---

## Articolo 50 - Obblighi di trasparenza per i fornitori e i deployer di determinati sistemi di IA

L'art. 50 si applica a sistemi che, pur non essendo high-risk, presentano **rischi specifici di trasparenza** verso le persone fisiche.

**Date di applicazione**:
- Par. 1 (chatbot), par. 3 (emozioni/categorizzazione biometrica), par. 4 (deepfake), par. 4 bis (testo informazione pubblica): **2 agosto 2026**.
- Par. 2 (marcatura machine-readable di output sintetici / watermarking): **2 dicembre 2026** (rinviato di 4 mesi dall'accordo provvisorio Digital Omnibus del 7 maggio 2026; accordo non ancora pubblicato in GUUE).

### Par. 1 - Sistemi che interagiscono con persone (chatbot, assistenti)

I fornitori garantiscono che i sistemi di IA destinati a interagire con persone fisiche:
- Siano **progettati e sviluppati** in modo che le persone interessate siano informate del fatto che stanno interagendo con un sistema di IA, **a meno che cio' non sia ovvio** dal punto di vista di una persona fisica ragionevolmente informata, attenta e avveduta, considerando le circostanze e il contesto d'uso.

**Eccezione**: l'obbligo non si applica ai sistemi di IA autorizzati per legge per **rilevamento, prevenzione, indagine e perseguimento di reati**, fatte salve le tutele appropriate.

### Par. 2 - Contenuti generati o manipolati (deepfake e simili) - lato fornitore

I fornitori di sistemi di IA, **inclusi sistemi di IA per finalita' generali (GPAI)**, che generano contenuti audio, immagine, video o testo sintetici, **garantiscono che gli output siano marcati in un formato leggibile dalla macchina** e **rilevabili come generati o manipolati artificialmente**.

I fornitori garantiscono che le loro **soluzioni tecniche siano efficaci, interoperabili, robuste e affidabili** nella misura tecnicamente fattibile, considerando le specificita' e i limiti dei diversi tipi di contenuti.

### Par. 3 - Sistemi di emozioni o categorizzazione biometrica - lato deployer

I deployer di sistemi di **riconoscimento emozioni** o **categorizzazione biometrica** (non vietati dall'art. 5):
- Informano le persone fisiche esposte al sistema del **suo funzionamento**
- Trattano i dati personali ai sensi di GDPR e LED

**Eccezione**: per attivita' di contrasto autorizzate dalla legge.

### Par. 4 - Deepfake - lato deployer

I deployer di sistemi di IA che generano o manipolano immagini/audio/video che costituiscono un **deepfake** (es. immagine palesemente artificiale di una persona reale) **divulgano** che il contenuto e' stato generato o manipolato artificialmente.

**Eccezioni**:
- Uso per attivita' di contrasto autorizzate
- Quando il contenuto fa parte di un'**opera o programma manifestamente artistici, creativi, satirici, di fiction o analoghi**, l'obbligo si limita a divulgare l'esistenza del contenuto generato/manipolato in **modo appropriato che non ostacoli la fruizione dell'opera**

### Par. 4 (bis) - Testo per informazione pubblica

I deployer di sistemi di IA che **generano o manipolano testo** pubblicato per **informare il pubblico su questioni di interesse pubblico** divulgano che il testo e' stato generato o manipolato artificialmente.

**Eccezioni**:
- Attivita' di contrasto autorizzate
- Quando il contenuto e' soggetto a **revisione editoriale umana** e una persona fisica/giuridica detiene la **responsabilita' editoriale** della pubblicazione

### Par. 5 - Modalita' di informazione

Le informazioni di cui ai par. 1-4 sono fornite alle persone fisiche **al piu' tardi al momento della prima interazione o esposizione**, in modo:
- **Chiaro e distinguibile**
- Conforme ai requisiti di accessibilita' applicabili

### Par. 6 - Conservazione obblighi piu' rigorosi

Le disposizioni dell'art. 50 lasciano impregiudicati gli **obblighi piu' rigorosi** di altre normative UE (es. GDPR per dati personali, DSA per piattaforme online, copyright).

---

## Sintesi rapida - chi fa cosa

| Sistema | Obbligo | Soggetto |
|---------|---------|----------|
| Chatbot/assistente che interagisce con utente | Disclosure "stai parlando con AI" | Fornitore |
| Generazione contenuti sintetici (audio/immagine/video/testo) | Marcatura tecnica machine-readable | Fornitore (anche GPAI) |
| Riconoscimento emozioni / categorizzazione biometrica (non vietato) | Informare persone esposte al funzionamento | Deployer |
| Deepfake | Divulgare che e' artificiale | Deployer |
| Testo AI per informazione pubblica | Divulgare generazione AI | Deployer |

## Note operative per ingegneri

- **Chatbot**: anche uno bot "ovvio" (es. su sito ecommerce con label "AI Assistant") soddisfa il requisito di "ovvieta'". La regola e' lo standard del **ragionevolmente informato**.
- **Marcatura tecnica deepfake** (par. 2): standard emergente. C2PA, watermarking robusto, metadati EXIF. La Commissione preparera' standard di riferimento.
- **Eccezione editoriale** (par. 4 bis): un articolo scritto con AI ma editato e firmato da un giornalista non richiede disclosure speciale. Cambia se il testo e' pubblicato come "opinione/news" senza intervento editoriale.
- **Accessibilita'**: la disclosure deve essere accessibile (screen reader, lingua semplice). Un footer minuto in 8pt non basta.

## Sanzioni

Violazione art. 50: fino a **15 milioni EUR o 3% del fatturato globale annuo** (art. 99 par. 4).
