# Esempio - input per classifica-sistema (chatbot customer service)

> Sintetico, fittizio. Test della skill su un caso realistic per ingegneri SW italiani.

## Sistema da classificare

**Nome**: "AssistAI" - Chatbot di customer service per piattaforma e-commerce italiana

## Descrizione

L'azienda **NegozioOnline Srl** (e-commerce italiano, 200K utenti registrati) sta valutando di sostituire il proprio sistema di customer service con un chatbot AI integrato sul sito web e nell'app mobile. Caratteristiche:

- **Integrazione GPT-4** via API OpenAI
- Il chatbot risponde a domande su: stato ordini, politiche di reso, info prodotti, problemi pagamento
- Accede a database clienti (anagrafica, storico ordini) per personalizzare risposte
- Escalation a operatore umano se confidenza bassa o richieste sensibili (es. reclami legali, problemi finanziari)
- Disponibile 24/7
- Lingua: italiano + inglese

## Tecnologie

- LLM upstream: GPT-4 (OpenAI) - integrato via API
- Wrapper proprietario in Python con prompt engineering, retrieval augmented generation (RAG) su knowledge base prodotti
- Database CRM clienti separato
- Logging conversazioni per audit e training

## Persone interessate

- Clienti finali (consumatori, B2C)
- Operatori CS umani (per escalation)

## Stato dati

- Conversazioni: trattenute 6 mesi (per audit)
- Dati cliente: usati come contesto del prompt, non per fine-tuning del modello
- Nessuna profilazione automatizzata o decisione con effetti giuridici

## Mercato

UE, principalmente Italia. Piattaforma anche disponibile a clienti svizzeri.

## Domanda

Come e' classificato questo sistema sotto l'AI Act? Quali obblighi si applicano a NegozioOnline Srl?
