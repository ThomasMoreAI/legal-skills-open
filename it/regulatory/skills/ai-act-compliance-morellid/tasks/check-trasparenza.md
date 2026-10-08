# Task: Verifica obblighi di trasparenza (art. 50)

Per sistemi che presentano "rischi specifici di trasparenza" (chatbot, generazione contenuti, riconoscimento emozioni, deepfake, testo AI per informazione pubblica), verifica gli obblighi di trasparenza dell'art. 50.

## Obiettivo

Checklist conforme degli obblighi di trasparenza per fornitori e/o deployer del sistema, con riferimenti normativi e raccomandazioni operative.

## Input richiesti

- Descrizione del sistema (cosa fa, come si presenta all'utente)
- Tipologia: chatbot? generazione audio/immagine/video/testo? riconoscimento emozioni? categorizzazione biometrica? deepfake? testo per informazione pubblica?
- Ruolo organizzazione (provider del sistema, deployer)
- Eccezioni applicabili (attivita' contrasto autorizzate, contenuto artistico, testo con responsabilita' editoriale)

## Fonti

Leggere prima: `references/estratti/ai-act-art-50-trasparenza.md`

## Procedura per categoria di sistema

### A) Sistema interagente con persone fisiche (chatbot, assistente vocale)

**Soggetto obbligato**: fornitore (provider).

- [ ] Sistema progettato e sviluppato in modo che le persone interessate **siano informate di interagire con un'AI**
- [ ] Eccezione "ovvieta'": l'obbligo non si applica se ovvio dal punto di vista di persona ragionevolmente informata, attenta e avveduta
- [ ] Eccezione attivita' di contrasto autorizzate: non applicabile (con tutele)

Pattern raccomandati:
- Disclaimer iniziale: "Sto parlando con un assistente AI"
- Label visibile nel prodotto (es. "AI Assistant")
- Risposta a domanda diretta "sei umano?" deve essere sincera

### B) Generazione contenuti audio/immagine/video/testo (anche da GPAI)

**Soggetto obbligato**: fornitore (provider) - **anche per GPAI**.

- [ ] Output **marcati in formato machine-readable** come generati/manipolati artificialmente
- [ ] Soluzioni tecniche **efficaci, interoperabili, robuste, affidabili** nella misura tecnicamente fattibile

Pattern tecnici di riferimento:
- C2PA (Coalition for Content Provenance and Authenticity)
- Watermarking robusto invisibile
- Metadati EXIF/IPTC con segnatura

Lasciate da pubblicare: standard armonizzati specifici per AI-generated content.

### C) Riconoscimento emozioni o categorizzazione biometrica (non vietato)

**Soggetto obbligato**: deployer (utilizzatore).

- [ ] Persone fisiche esposte **informate del funzionamento del sistema**
- [ ] Trattamento dati personali conforme a GDPR + LED
- [ ] Eccezione attivita' di contrasto autorizzate: non applicabile (con tutele)

**Importante**: l'art. 5 lett. f vieta riconoscimento emozioni in **luoghi di lavoro e istituti di istruzione**. Quindi questo task si applica solo a contesti diversi (es. retail, sanita', sicurezza pubblica con eccezione).

### D) Deepfake (immagini/audio/video manipolati artificialmente)

**Soggetto obbligato**: deployer.

- [ ] Divulgazione che il contenuto e' generato/manipolato artificialmente
- [ ] Eccezioni:
  - Attivita' di contrasto autorizzate
  - Contenuto **manifestamente artistico, creativo, satirico, fiction o analoghi**: divulgazione limitata, modo che non ostacoli la fruizione

Pattern raccomandati:
- Watermark visibile/invisibile
- Caption "Contenuto AI-generated" o "Immagine sintetica"
- Per uso satirico in pubblicazione editoriale: nota a pie' di articolo o caption

### E) Testo AI per informazione pubblica

**Soggetto obbligato**: deployer.

- [ ] Divulgazione che il testo e' generato/manipolato artificialmente
- [ ] Eccezioni:
  - Attivita' di contrasto autorizzate
  - Testo **soggetto a revisione editoriale umana** con responsabilita' editoriale identificata

In pratica:
- Articoli giornalistici editati e firmati: eccezione applicabile
- Bollettini AI auto-generati senza revisione: divulgazione richiesta
- Comunicati ufficiali di enti pubblici: dipende dalla revisione editoriale

### F) Modalita' di informazione (par. 5 - tutti i casi)

- [ ] Informazione fornita **al piu' tardi alla prima interazione/esposizione**
- [ ] Modo **chiaro e distinguibile**
- [ ] Conforme a requisiti di **accessibilita'** (WCAG, screen reader, lingua semplice)

## Output strutturato

```markdown
# Verifica obblighi trasparenza art. 50 - [nome sistema]

**Data verifica**: [data]
**Sistema**: [descrizione]
**Organizzazione**: [...]
**Ruolo**: [provider / deployer / entrambi]

## Categorie applicabili

| Categoria | Si/No | Soggetto obbligato |
|-----------|-------|---------------------|
| A) Chatbot / interazione persone | [SI/NO] | Provider |
| B) Generazione contenuti sintetici | [SI/NO] | Provider |
| C) Riconoscimento emozioni / cat. biometrica | [SI/NO] | Deployer |
| D) Deepfake | [SI/NO] | Deployer |
| E) Testo AI per informazione pubblica | [SI/NO] | Deployer |

## Verifica obblighi per ciascuna categoria applicabile

[per ogni Si dalla tabella, riportare gli specifici obblighi e lo stato]

### Categoria [X]
- [ ] Obbligo 1: stato + note
- [ ] Obbligo 2: stato + note

## Eccezioni applicabili?

- Attivita' di contrasto autorizzate: [Si/No + base]
- Ovvieta' (cat. A): [Si/No + valutazione]
- Contenuto artistico (cat. D): [Si/No + valutazione]
- Revisione editoriale (cat. E): [Si/No + valutazione]

## Modalita' di informazione (par. 5)

- [ ] Tempistica (prima interazione)
- [ ] Chiarezza e distinguibilita'
- [ ] Accessibilita' (WCAG, lingua, screen reader)

## Gap rilevati

[Lista]

## Raccomandazioni

[Lista]

## Sinergie

- **GDPR**: trattamento dati personali (informativa art. 13/14)
- **DSA** (Digital Services Act): per piattaforme online, obblighi paralleli
- **Direttiva ePrivacy**: per cookie/tracking nelle interazioni utente
- **Copyright DSM Directive 2019/790**: per generazione contenuti

## Sanzioni

Violazione art. 50: fino a **15M EUR o 3% del fatturato globale** (art. 99 par. 4).

## Limiti

- Standard tecnici per marcatura sintetici (cat. B) in via di sviluppo
- Linee guida Commissione su art. 50 attese
```

## Casi tipici

### ChatBot di customer service basato su GPT-4 in sito ecommerce
- Categoria A applicabile: provider del chatbot (azienda) deve informare
- Pattern: label "AI Assistant" + disclaimer iniziale = ovvieta' soddisfatta
- Categoria B applicabile su GPT-4 (provider Meta/OpenAI): marcatura output a carico del fornitore del modello

### Sistema di videosorveglianza retail con analisi sentiment cliente
- Lecito? L'art. 5 lett. f vieta in lavoro e istruzione, non in retail
- Categoria C applicabile: deployer (retailer) informa clienti del funzionamento
- Cartello visibile + privacy policy

### App che genera deepfake video per intrattenimento (TikTok-like)
- Categoria D applicabile per deployer (app)
- Watermark visibile + caption "AI-generated"
- Per contenuti satirici: nota appropriata

### Newsletter AI-generated di azienda B2B (no revisione editoriale)
- Categoria E applicabile (testo per informazione pubblica)
- Footer "Questo testo e' stato generato con AI"
- Se editato e firmato: eccezione editoriale applicabile

### Software di customer support AI per banche con voice biometrics per autenticazione
- Categoria A si (chatbot voce)
- Categoria C: verifica biometrica 1:1 NON e' categorizzazione, NON ricade in art. 50 par. 3
- Trattamento biometrico GDPR + AI Act (se non in Allegato III biometria)

## Limiti

- Standard tecnici (C2PA, watermarking) in evoluzione
- Linee guida Commissione attese
- Eccezione "ovvieta'" e "responsabilita' editoriale" hanno margine interpretativo

## Esempi

(Esempi specifici da costruire iterativamente)
