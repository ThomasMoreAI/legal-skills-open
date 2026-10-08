# Note di dominio - caso `classifica-chatbot-cs`

## Cosa stiamo testando

Che la skill identifichi correttamente un caso comune (chatbot CS con LLM) come **rischio limitato (trasparenza art. 50)**, e che riconosca la dualita' di ruoli: provider del sistema integrato + deployer del modello GPAI sottostante.

## Scelte progettuali del caso

- **Caso "limitato ma frequente"**: chatbot CS e' uno dei deployment piu' diffusi di LLM in azienda. La skill deve gestirlo correttamente senza falsi positivi.
- **GPT-4 sottostante**: introduce la sinergia con GPAI (obblighi del provider del modello, non del deployer).
- **Dati personali coinvolti**: trigger sinergia con skill GDPR.
- **Trasferimento extra-UE**: complessita' GDPR su OpenAI USA, SCC, TIA, DPF.
- **Customer-facing**: rilevanza primaria art. 50 par. 1 (chatbot).

## Output atteso

`TRASPARENZA art. 50` per AssistAI; **non** high-risk; **non** vietato; GPAI (con rischio sistemico) si applica a OpenAI per GPT-4 ma non a NegozioOnline.

Lista di obblighi reali:
- Trasparenza art. 50 par. 1
- AI literacy art. 4
- Sinergia GDPR (Registro, DPIA, trasferimento extra-UE)

## Cose che la skill DOVREBBE fare

- **Distinguere classificazione del sistema vs del modello**: questo e' frequentemente confuso. AssistAI e' rischio limitato. GPT-4 e' GPAI con rischio sistemico. NegozioOnline ha solo gli obblighi del proprio sistema.
- **Proporre i 6 pattern di compliance** (label, disclaimer, ecc.) come operativizzazione concreta dell'art. 50.
- **Riconoscere il par. 4 bis come NON applicabile** (testo per informazione pubblica != chatbot 1-a-1).
- **Riconoscere il par. 2 come marginalmente applicabile** (testo conversazionale non e' contenuto sintetico nel senso di deepfake).
- **Trigger sinergie GDPR**: registro + DPIA + trasferimenti.

## Cose che la skill NON dovrebbe fare

- **Falso positivo high-risk**: il chatbot CS NON rientra in Allegato III. Servizi e-commerce non sono "servizi pubblici essenziali" art. 5.a.
- **Confondere ruoli**: NegozioOnline non e' provider GPAI. Non si applicano gli obblighi art. 53/55.
- **Pretendere conformity assessment art. 43**: e' obbligo per high-risk, non per trasparenza.
- **Sottovalutare sinergia GDPR**: il chatbot tratta dati personali (storico ordini), GDPR e' centrale.

## Ambiguita' rilevanti

- **"Ovvieta'" eccezione art. 50 par. 1**: zona grigia. Una persona ragionevolmente attenta capisce che AssistAI e' AI? Forse, ma la prassi raccomandata e' RENDERE ovvio (label, disclaimer).
- **Trasferimento extra-UE**: 2026 - DPF UE-USA potrebbe essere annullato (Schrems III?). La skill cita come opzione, non da' garanzie.
- **Decisioni automatizzate**: se il chatbot decide rimborsi automatici (oltre i casi standard), si entra in territorio decisioni automatizzate art. 22 GDPR e potenzialmente Allegato III par. 5 lett. a (servizi pubblici essenziali, ma non e' caso di e-commerce). La skill segnala come scenario da monitorare.

## Cosa imparare

- Il caso "chatbot generico CS" e' tipico di trasparenza art. 50, non high-risk.
- La complessita' principale per il deployer e' GDPR (trasferimento extra-UE OpenAI), non AI Act.
- I 6 pattern di compliance sono semplici da implementare ma vanno fatti per default.
- AI literacy art. 4 e' obbligo gia' in vigore (02/02/2025) ma spesso ignorato - vale la pena segnalarlo.

## Fonte della struttura

Caso fittizio realistico per e-commerce italiano. Pattern molto comune nel 2026.
