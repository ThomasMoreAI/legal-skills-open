# Note di dominio - caso `dpia-soglia-app-scoring`

## Cosa stiamo testando

Che la skill identifichi un caso flagrante di trigger DPIA: app di scoring creditizio con decisioni automatizzate. E' il caso paradigmatico citato come esempio nella tipologia 2 del Garante (screening clienti centrali rischi) ed evidente sotto multipli criteri WP248.

## Scelte progettuali del caso

- **Caso "no-brainer"**: deliberatamente esempio dove la DPIA e' chiarissimamente obbligatoria. Test che la skill non confonda la chiarezza del caso con minimizzazione.
- **Multi-tipologia + multi-criterio**: 4 tipologie italiane + 7 criteri WP248. Ogni "porta" da sola e' sufficiente ad attivare l'obbligo.
- **Settore fintech**: realistico per il pubblico di ingegneri informatici (target SW della commissione).
- **Tecnologie attuali**: AWS Frankfurt + ML proprietario - scenario contemporaneo.
- **Decisioni automatizzate**: punto critico di art. 22 GDPR + art. 35 par. 3 lett. a).

## Output atteso

**DPIA OBBLIGATORIA** con 4 tipologie e 7 criteri attivati. Riferimento all'art. 35 par. 3 lett. a) come trigger autonomo. Lista di 9 punti di attenzione per la DPIA effettiva.

## Cose che la skill DOVREBBE fare

- Identificare TUTTE le tipologie applicabili, non solo la prima.
- Citare i riferimenti normativi precisi (provvedimento, articolo, lettera).
- Distinguere tra tipologie italiane e criteri WP248.
- Suggerire punti di attenzione SPECIFICI per il dominio (centrali rischi, codici di deontologia).
- Segnalare la possibilita' di consultazione preventiva del Garante (art. 36).
- Evidenziare l'esigenza di explainability per AI/ML.

## Cose che la skill NON dovrebbe fare

- **Cercare di "salvare" il trattamento**: con 4 tipologie e 7 criteri, la decisione e' netta.
- **Confondere ruoli**: AWS Frankfurt e' UE (responsabile in UE) - il problema sono i backup USA, non il datacenter primario.
- **Pretendere di fare la DPIA**: questo task e' di SOGLIA, non di DPIA. Rinvio a draft-dpia.md.

## Ambiguita' rilevanti che la skill deve gestire

- **Vulnerabili** (criterio 7): persone in difficolta' finanziaria possono essere considerate vulnerabili in senso lato. La skill segnala come "borderline" senza forzare.
- **Cat. particolari** (tipologia 10): se l'utente dichiara condanne penali, scatta. Non e' chiaro a priori - la skill segnala come "possibile".
- **DPF UE-USA**: stato di adeguatezza puo' cambiare - la skill cita come opzione presente ma non vincolante.

## Cosa imparare

- I trigger DPIA sono cumulativi: anche se UNA categoria si applica, e' sufficiente. La skill deve essere "generosa" nel segnalare, non parsimoniosa.
- Le decisioni automatizzate con effetti giuridici sono il caso piu' chiaro di obbligo DPIA (art. 35 par. 3 lett. a esplicito).
- Per AI/ML, il problema non e' solo GDPR ma anche AI Act (Reg. UE 2024/1689) - per credit scoring, alto rischio art. 6 + Allegato III.

## Fonte della struttura

Caso fittizio ma realistico. Ispirato a casi reali di fintech italiana. Nessun riferimento concreto.

## Limiti del test

- L'AI Act non e' ancora coperto da questa skill. Andra' aggiunta in iterazioni successive una skill dedicata o estensione.
- Il Codice di Deontologia dei sistemi informativi creditizi del Garante (Allegato A.5 al Codice Privacy) ha regole specifiche che andrebbero integrate per casi reali.
