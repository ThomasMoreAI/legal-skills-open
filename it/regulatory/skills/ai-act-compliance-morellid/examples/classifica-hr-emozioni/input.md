# Esempio - input per classifica-sistema (HR con sentiment analysis)

> Sintetico, fittizio. Test su scenario potenzialmente VIETATO.

## Sistema da classificare

**Nome**: "TalentMatchPro" - piattaforma SaaS per HR di video-interview con AI

## Descrizione

L'azienda **TalentTech Srl** (Italia) sviluppa una piattaforma per le aziende clienti che permette di:

1. Caricare un job description e i CV di candidati
2. Inviare un link di video-interview asincrono ai candidati
3. Il candidato registra le risposte a domande standard pre-impostate
4. **Il sistema analizza il video e produce uno score** che combina:
   - Trascrizione testuale + valutazione di **rilevanza delle risposte** (NLP)
   - **Analisi facciale** per **rilevare emozioni** (entusiasmo, calma, tensione)
   - **Tono di voce** per stimare **fiducia, ansia, energia**
5. Lo score complessivo (0-100) e' presentato al recruiter, con breakdown per dimensione

## Tecnologie

- LLM per scoring linguistico delle risposte (modello proprietario fine-tuned)
- Computer vision per facial emotion recognition (proprietario su frame video)
- Audio analysis per voice features
- Deployment cloud AWS Frankfurt

## Mercato target

Aziende italiane ed europee per processi di selezione del personale.

## Caratteristiche

- ~500 aziende clienti potenziali
- Volumi: 10.000+ video interview/mese a regime
- Categorie candidati: tutti i livelli di esperienza, tutti i settori
- Lingue: italiano, inglese, francese, tedesco

## Domanda

E' lecito immettere sul mercato questo sistema sotto l'AI Act?
