# Esempio worked: diritto della crisi d'impresa

Esempio di applicazione del template a un ramo particolarmente insidioso, dove è facile sovrapporre
istituti distinti. Vale come modello, non come vincolo: la skill è generale.

## Perché è insidioso

Nel diritto della crisi d'impresa convivono procedure diverse con norme diverse, anche quando il
principio sottostante è analogo. Va identificata con precisione **la procedura specifica**:

- **Liquidazione giudiziale** (art. 121 ss. CCII — ex fallimento, per imprenditori commerciali
  sopra-soglia)
- **Liquidazione controllata** (art. 268 ss. CCII — per soggetti sovraindebitati: consumatori,
  professionisti, imprenditori minori, start-up innovative)
- **Concordato preventivo** (art. 84 ss. CCII)
- **Concordato minore** (art. 74 ss. CCII)
- **Ristrutturazione dei debiti del consumatore** (art. 67 ss. CCII)

E va indicata la **normativa di riferimento primaria**: Legge Fallimentare (R.D. 267/1942), CCII
(d.lgs. 14/2019) o entrambe (per il diritto transitorio).

> ⚠️ Avvertenza critica: non sovrapporre mai il regime della liquidazione giudiziale con quello
> della liquidazione controllata. Sono istituti distinti con norme diverse, anche quando il
> principio è analogo (es. art. 146 CCII per la liquidazione giudiziale ≠ art. 268 c. 4 CCII per la
> liquidazione controllata).

## Come si riflette nel prompt

- **Step 0 dell'analisi:** prima di tutto identifica la procedura concorsuale specifica e la fonte
  normativa (L.Fall. / CCII / transitorio).
- **`<vincoli>`:** aggiungi esplicitamente "Non applicare l'art. 268 CCII a una liquidazione
  giudiziale e viceversa; non usare la L.Fall. per fatti regolati dal CCII senza segnalare il
  regime transitorio".
- **Chain of Thought, punto A:** distingui le norme che disciplinano la stessa fattispecie in
  procedure diverse (es. art. 146 vs art. 268 CCII).
- **Metaprompting:** se il quesito non chiarisce procedura, fase e soggetto richiedente, chiedi
  prima questi tre dati.

## Mini-esempio few-shot da inserire nel prompt

```
[Quesito] Il TFR maturato dal debitore va versato all'organo della procedura?
[Output minimo atteso]
- Qualificazione del TFR (retribuzione differita) e procedura applicabile (liq. giudiziale ex art.
  121 ss. CCII oppure liq. controllata ex art. 268 ss. CCII: indicarla).
- Norma specifica della procedura individuata (non quella dell'altra procedura).
- Orientamento di legittimità e di merito, con grado di consolidamento.
- Conclusione operativa differenziata per fase.
```
