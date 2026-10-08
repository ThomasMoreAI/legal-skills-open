# Template del prompt legale (struttura a tag)

Struttura completa da compilare per produrre il prompt migliorato. Adatta i contenuti al ramo del
diritto del quesito (civile, penale, tributario, del lavoro, amministrativo, crisi d'impresa…).
L'output finale deve restare **sotto le 750 parole** ed essere SOLO il prompt, senza meta-commenti.

---

## Step A — Analisi del prompt originale

Prima di scrivere, identifica:

- Obiettivo principale (esplicito o implicito).
- Elementi presenti: [ruolo | contesto | task | scopo | pubblico | vincoli | tono | stile |
  formato | esempi | tecniche avanzate].
- Elementi mancanti che migliorerebbero il risultato.
- Ambiguità o vaghezze da eliminare.
- **Rischi specifici del contesto legale:** confusione tra istituti, norme abrogate usate come
  vigenti, orientamenti minoritari presentati come dominanti, riferimenti inventati.

## Step B — Struttura completa del prompt

Compila questi tag. Le note tra parentesi sono istruzioni per te, non vanno nell'output.

```
<ruolo>
[Professione, specializzazione e sotto-settore dell'esperto che l'IA deve interpretare. In ambito
legale specifica sempre il sotto-settore (es. "avvocato specializzato in diritto del lavoro
italiano"). Il ruolo orienta lessico e livello tecnico, non conferisce competenza certificata.]
</ruolo>

<contesto>
[Background concreto. In ambito legale includi: tipo di soggetto coinvolto; istituto/procedura
applicabile e la sua fonte normativa; fatti rilevanti già accertati; momento procedurale;
eventuali provvedimenti già adottati.]
</contesto>

<task>
[Cosa deve produrre concretamente l'IA. Articola sempre in sotto-task numerati, es.:
1. Analisi del quadro normativo (con indicazione dell'istituto specifico)
2. Orientamento giurisprudenziale (legittimità + merito; dominante vs minoritario)
3. Analisi del caso concreto alla luce delle fonti
4. Valutazione delle tesi in campo (con confutazione delle tesi contrarie)
5. Impatto di eventuali riforme normative recenti
6. Conclusioni operative azionabili]
</task>

<scopo>
[Risultato finale a cui si mira: parere legale interno / istanza o atto difensivo / consulenza al
cliente / ricerca accademica / orientamento decisionale preliminare. Condiziona cautela, tono e
forma delle conclusioni.]
</scopo>

<pubblico>
[A chi è rivolto l'output: livello di expertise (avvocato specializzato / generalista / magistrato
/ cliente non esperto), familiarità col sotto-settore, esigenze particolari (indicazioni operative
immediate vs approfondimento dottrinale).]
</pubblico>

<vincoli>
[Negative prompting — cosa l'IA NON deve fare. Includi sempre:
- Non inventare riferimenti normativi o giurisprudenziali: citare solo fonti reali e verificabili.
- Non sovrapporre i regimi normativi di istituti distinti, né applicare la norma di un istituto a
  un istituto diverso senza esplicitare e giustificare l'analogia.
- Non presentare orientamenti minoritari come consolidati senza segnalarne la natura.
- Non omettere il dato normativo specifico (articolo, comma, lettera, testo di riferimento).
- Non fornire risposte generiche: ogni affermazione calibrata sui fatti del contesto.
- Non usare norme abrogate come vigenti senza segnalarne lo status.
- Evitare linguaggio burocratico e ridondante.]
</vincoli>

<tono>
[Professionale, diretto, analitico. Evita toni assertivi su questioni dibattute; segnala con
"l'orientamento prevalente", "si ritiene preferibile", "rimane controverso" i punti non uniformi.]
</tono>

<stile>
[Tecnico-giuridico, argomentativo, ragionamento per punti. Conclusioni dialettiche: esponi le tesi
in campo, confuta quelle non condivisibili, argomenta la soluzione preferibile.]
</stile>

<formato_risposta>
- Struttura: documento giuridico con sezioni titolate (adatta i titoli al quesito), tipicamente:
  I. Identificazione dell'istituto e quadro normativo applicabile
  II. Analisi delle norme rilevanti (con testo letterale degli articoli chiave)
  III. Orientamento giurisprudenziale (legittimità → merito, dal più recente)
  IV. Analisi del caso: tesi in campo e confutazione
  V. Impatto di riforme normative recenti
  VI. Conclusioni operative (piano d'azione per il professionista)
- Lingua: italiano
- Contesto normativo: diritto italiano — specifica sempre la fonte applicabile (codice, T.U.,
  d.lgs., ecc.) e, se rileva, l'eventuale regime transitorio.
- Lunghezza: completa ma non ridondante; ogni sezione sostanziale.
- Formattazione: Markdown con intestazioni di sezione.
</formato_risposta>
```

## Step C — Adattamento per ramo del diritto

Cala i tag sul ramo concreto. Esempi di sotto-settori e fonti tipiche:

- **Civile:** c.c., c.p.c.; obbligazioni, contratti, responsabilità, famiglia, successioni.
- **Penale:** c.p., c.p.p.; reati, misure, procedura.
- **Tributario:** T.U.I.R., d.P.R. 600/1973, d.lgs. 472/1997; prassi Agenzia Entrate, CGT.
- **Lavoro:** c.c. (libro V), Statuto dei lavoratori, d.lgs. settoriali; qualificazione del rapporto.
- **Amministrativo:** L. 241/1990, c.p.a.; provvedimento, processo amministrativo, TAR/Consiglio di Stato.
- **Crisi d'impresa:** CCII (d.lgs. 14/2019) e/o L.Fall. (R.D. 267/1942) per il transitorio — vedi
  `esempio-concorsuale.md`.

Per i passi di ragionamento e i guardrail di qualità da incorporare nel prompt, vedi
`reasoning-and-guardrails.md`.
