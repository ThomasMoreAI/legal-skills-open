# Ragionamento giuridico, tecniche avanzate e guardrail

Da incorporare nel prompt migliorato (Step 4). Queste istruzioni vanno **dentro il prompt che
produci**, in modo che l'IA destinataria le segua quando risponderà al quesito.

---

## Chain of Thought giuridico

Inserisci nel prompt l'istruzione di seguire, prima di rispondere, questo percorso di ragionamento:

**A. Mappatura normativa**
- Identifica l'istituto applicabile e le norme specifiche (non analoghe) che lo disciplinano.
- Verifica se le norme citate sono vigenti o se esistono norme transitorie.
- Distingui norme che disciplinano la stessa fattispecie in istituti/procedure diverse.

**B. Natura giuridica dell'istituto**
- Qualifica giuridicamente l'istituto su cui verte la questione (es. natura del TFR = retribuzione
  differita, non reddito periodico).
- Verifica se la qualificazione è unanime o dibattuta.
- Identifica le conseguenze pratiche della qualificazione adottata.

**C. Dialettica delle tesi**
- Esponi sistematicamente almeno due tesi (pro e contro l'istante).
- Per ciascuna, indica fondamento normativo e supporto giurisprudenziale.
- Confuta le tesi non condivisibili con argomenti normativi, sistematici e/o costituzionali.

**D. Coerenza sistematica**
- La soluzione è coerente con i principi generali dell'ordinamento?
- Esistono norme analoghe in altri settori richiamabili in via interpretativa?
- Esistono principi costituzionali pertinenti (es. artt. 2, 3, 24, 36, 38, 41, 47, 111 Cost.)?

**E. Rischi processuali**
- Quali rischi se la tesi sostenuta viene disattesa dal giudice?
- Esistono orientamenti di merito difformi che il giudice potrebbe seguire?
- Quali atti o istanze vanno depositati in via preventiva o cautelare?

---

## Tecniche avanzate (usa quando pertinenti)

- **Chain of Thought:** attivo per default in tutte le ricerche legali (vedi sopra).
- **Few-shot:** includi 1 esempio di struttura attesa nella forma [Quesito → Output minimo atteso]
  quando il task è particolarmente specifico o atipico.
- **Chained prompting:** per ricerche che coprono più istituti o più procedure, suddividi in prompt
  sequenziali:
  1. Mappatura normativa e qualificazione dell'istituto
  2. Ricerca giurisprudenziale mirata
  3. Analisi del caso concreto e conclusioni operative
- **Metaprompting:** se il quesito è ambiguo, il prompt deve chiedere chiarimenti prima di
  procedere, specificando (a) l'istituto/procedura applicabile, (b) la fase, (c) il soggetto
  richiedente. (Nella skill questo avviene già nello Step 1 dell'intent gate.)

---

## Guardrail di qualità

Inserisci nel prompt questi criteri minimi verificabili.

**Guardrail normativi**
- Ogni affermazione normativa indica: articolo, comma, lettera, testo normativo (codice / T.U. /
  d.lgs. / ecc.) e anno di emanazione.
- Ogni norma citata è vigente alla data del quesito, salvo diritto transitorio (da segnalare).
- Nessuna norma applicata a un istituto diverso da quello per cui è dettata senza esplicitare e
  giustificare l'analogia.

**Guardrail giurisprudenziali**
- Ogni riferimento indica: organo giudicante, sezione, anno, numero di sentenza (ove disponibile).
- Distingui giurisprudenza di legittimità (Cassazione / Consiglio di Stato) e di merito.
- Segnala se un orientamento è dominante, minoritario o contrastato.
- Non citare mai sentenze non verificabili; in caso di incertezza usa formule come "in senso
  analogo si è espressa la giurisprudenza di merito" senza inventare coordinate precise.

**Guardrail conclusivi**
- La risposta si chiude con un piano d'azione operativo (atti da depositare, termini, argomenti da
  invocare, rischi da presidiare).
- Il piano d'azione è differenziato per fase procedurale (prima / durante / dopo).
