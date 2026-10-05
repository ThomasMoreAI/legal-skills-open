# Note di dominio - caso `registro-pmi-base`

## Cosa stiamo testando

Che la skill produca un Registro art. 30 strutturato e completo per una PMI italiana realistica (50 dipendenti, software gestionale B2B), e che il check di completezza identifichi correttamente i punti di attenzione.

## Scelte progettuali del caso

- **6 trattamenti tipici di una PMI**: HR, CRM, fornitori, marketing, videosorveglianza, sito web. Coprono i casi piu' frequenti che un consulente trova in pratica.
- **Trasferimenti extra-UE realistici**: Salesforce e MailChimp con backup USA, gestiti via SCC. Test della skill su trattamento moderno con SaaS.
- **Trattamento "trappola" T5 videosorveglianza**: deliberatamente ambiguo (perimetro vs posti lavoro). La skill deve segnalare l'ambiguita' e raccomandare DPIA condizionata.
- **Trattamento "non trigger" T6 analytics**: anonimizzato correttamente. La skill non deve falsamente classificare come trigger DPIA.
- **PMI a 50 dipendenti**: art. 30 par. 5 applicabile in teoria (< 250) ma in pratica obbligo del Registro per il combinato (rischio + non occasionale + cat. particolari sanitari medicina lavoro).
- **DPO facoltativo**: scenario realistico per PMI tech che ha designato un consulente esterno per buona pratica.

## Output atteso

`CONFORME CON NOTE MINORI` con 1 nota alta (T5 da chiarire), 1 media (T2 SCC documentate), 2 basse (T1 legale rappresentante, T1 DR).

## Cose che la skill DOVREBBE fare

- Riconoscere i 7 contenuti minimi per ciascun trattamento.
- Distinguere base giuridica art. 6 da art. 9 (necessaria per cat. particolari).
- Catturare correttamente i trasferimenti extra-UE come elemento separato.
- Differenziare conservazione per categoria di dato (non trattamento globale).
- Triggerare check DPIA per ciascun trattamento.
- Segnalare ambiguita' come T5 senza forzare decisione.

## Cose che la skill NON dovrebbe fare

- **Falso positivo per T6**: dato anonimizzato non e' "dato personale" - non rientra in cat. particolari ne' in trigger DPIA.
- **Falso negativo per T5**: deve almeno SOLLEVARE il dubbio anche se non puo' decidere senza piu' info.
- **Pretendere certezza sulla data adequacy USA (DPF)**: la decisione adeguatezza UE-USA del DPF puo' essere annullata in futuro - la skill deve citarla come opzione condizionale.

## Ambiguita' progettuale

- **Conservazione 10 anni** per anagrafici dipendenti: art. 2220 c.c. parla di scritture contabili, ma per analogia si applica a tutti i documenti. Una skill troppo pignola direbbe "10 anni e' eccessivo per anagrafici puri" - in pratica accetta lo standard di mercato italiano.
- **MailChimp con backup USA**: c'e' DPF? Quando la skill e' eseguita (2026) il DPF UE-USA e' attivo, ma vale la pena citare anche le SCC come fallback. La skill deve farlo.

## Cosa imparare

- Un Registro ben fatto e' conciso ma completo. Tabella + schede e' formato adeguato.
- Le ambiguita' DPIA (come T5) sono frequenti e vanno segnalate, non risolte di forza.
- I trasferimenti extra-UE e i provider cloud sono il punto piu' fragile della maggior parte dei Registri reali.

## Fonte della struttura

Caso fittizio. Pattern realistico per PMI italiana del settore software B2B. Nessun riferimento reale.
