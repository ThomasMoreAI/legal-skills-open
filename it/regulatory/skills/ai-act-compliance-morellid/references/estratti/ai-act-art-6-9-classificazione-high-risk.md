# Estratto: AI Act Art. 6 (classificazione high-risk) + Art. 9 (sistema gestione rischi)

**Fonte**: `sources.yaml` id `ai-act-it-eurlex`
**Data consultazione**: 2026-04-25
**Hash SHA256**: a61b61706aee6676e3988ab696162d71d759c3debd48b2ecccac3555207f2b0c

---

## Articolo 6 - Regole di classificazione per i sistemi di IA ad alto rischio

### Par. 1 - Componenti di sicurezza di prodotti regolamentati (Allegato I)

Un sistema di IA e' alto rischio se entrambe le condizioni:
- **a)** e' destinato a essere usato come **componente di sicurezza di un prodotto** disciplinato dalla normativa di armonizzazione UE (Allegato I), oppure e' esso stesso il prodotto;
- **b)** il prodotto e' soggetto a **valutazione di conformita' da parte di terzi** ai fini dell'immissione sul mercato secondo l'Allegato I.

Esempi tipici Allegato I (parziale): macchine, giocattoli, ascensori, dispositivi medici, equipaggiamenti radio, prodotti pirotecnici, attrezzature pressione, automotive, aviazione, ferrovie, marittimo.

### Par. 2 - Casi d'uso elencati nell'Allegato III

Anche i sistemi di IA elencati nell'**Allegato III** (vedi estratto dedicato) sono ad alto rischio.

### Par. 3 - Eccezione: sistema in Allegato III ma a basso rischio

Un sistema di Allegato III **non** e' alto rischio se non presenta rischio significativo per salute, sicurezza, diritti fondamentali, e si applica almeno UNA delle:
- **a)** compito **procedurale limitato** (es. trasforma dati non strutturati in strutturati, classifica documenti)
- **b)** **migliora il risultato** di un'attivita' umana gia' completata
- **c)** rileva **schemi decisionali o deviazioni** senza sostituire la valutazione umana
- **d)** compito **preparatorio** per valutazioni dei casi Allegato III

**ECCEZIONE all'eccezione**: un sistema di Allegato III e' SEMPRE alto rischio se effettua **profilazione di persone fisiche**.

### Par. 4 - Documentazione dell'auto-classificazione

Se un fornitore ritiene che il proprio sistema (in Allegato III) NON sia alto rischio, deve **documentare la valutazione** prima dell'immissione sul mercato. Soggetto a **registrazione art. 49 par. 2** e disponibilita' della documentazione su richiesta dell'autorita'.

### Par. 5 - Linee guida Commissione

La Commissione, entro **02/02/2026**, fornisce orientamenti pratici con elenco esaustivo di esempi.

---

## Articolo 9 - Sistema di gestione dei rischi

### Par. 1
Per ogni sistema high-risk e' istituito, attuato, documentato e mantenuto un **sistema di gestione dei rischi**.

### Par. 2 - Processo iterativo continuo

Il sistema copre l'**intero ciclo di vita** del sistema IA e include:

- **a) identificazione e analisi** dei rischi noti e ragionevolmente prevedibili
- **b) stima e valutazione** dei rischi che possono emergere quando il sistema e' usato secondo finalita' prevista
- **c) valutazione** di altri rischi possibili sulla base dei dati raccolti dal post-market monitoring (art. 72)
- **d) adozione di misure** appropriate e mirate di gestione del rischio per i rischi identificati

### Par. 3 - Misure mirate

I rischi affrontati sono solo quelli **ragionevolmente mitigabili o eliminabili** tramite progettazione del sistema, considerando lo **stato dell'arte**.

### Par. 5 - Misure di gestione rischio appropriate

- Riduzione/eliminazione tramite **progettazione e sviluppo**
- Quando rischi non possono essere eliminati: **misure di mitigazione e controllo**
- Fornire **informazioni** ai deployer (istruzioni d'uso art. 13) e, se del caso, **formazione**

### Par. 5-9 - Test, dataset, persone vulnerabili

- Test su rischi e prestazioni in condizioni il piu' simili possibile a quelle reali (par. 6)
- Test in condizioni reali permessi solo entro limiti art. 60 (par. 7)
- Considerazione speciale per **gruppi vulnerabili e minori** (par. 9)

### Par. 10 - Integrazione con altri requisiti

Per fornitori soggetti a **gestione del rischio prevista da altre normative settoriali UE** (es. dispositivi medici), il sistema gestione rischi AI Act puo' essere parte di / integrato con quello esistente.

---

## Note operative

- **Il sistema gestione rischi (art. 9) e' un processo, non un documento**. La documentazione tecnica (art. 11 + Allegato IV) deve dimostrare l'esistenza e la robustezza del processo.
- Cross-reference con altri articoli: art. 10 (governance dati), art. 11 (documentazione tecnica), art. 14 (sorveglianza umana), art. 15 (accuratezza/robustezza/cybersicurezza).
- Per fornitori UE che gia' hanno **ISO/IEC 23894** (AI risk management), questa puo' essere base solida ma serve adattamento ai requisiti specifici art. 9.
