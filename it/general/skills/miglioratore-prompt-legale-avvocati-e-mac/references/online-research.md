# Ricerca online opzionale (gate "chiedere prima")

La ricerca online serve **solo a informare il prompt** — a colmare lacune che ne migliorerebbero la
qualità — **mai a rispondere al quesito** al posto dell'utente. L'output della skill resta SOLO il
prompt migliorato.

## Principio: chiedere prima, mai cercare in silenzio

Di **default lavora offline**. Valuta una ricerca online solo se uno di questi dati ti manca e
servirebbe a rendere il prompt più preciso:

- una **riforma normativa recente** che potrebbe aver cambiato il quadro;
- l'**orientamento giurisprudenziale attuale** su un punto controverso;
- la **conferma di un dato normativo** (numero di articolo, vigenza, abrogazione) di cui non sei
  certo.

Quando ne ricorre uno, **proponi** la ricerca all'utente nominando lo strumento, e procedi solo
dopo conferma. Esempio:

```
Per rendere il prompt più preciso mi servirebbe verificare se [dato/riforma/orientamento] è
aggiornato. Vuoi che faccia una breve ricerca online con [strumento]? (Altrimenti procedo offline
segnalando il punto come da verificare.)
```

Se l'utente rifiuta o non risponde, costruisci comunque il prompt e **segnala nel prompt** il punto
come "da verificare" (coerente con i guardrail).

## Routing degli strumenti

Usa il primo disponibile, dichiarando sempre quale stai usando:

1. **Skill `ricerca-web-searXNG`** — ricerca web privata e ottimizzata, con routing legale italiano
   (BuddaLaw per sentenze, Normattiva per norme, SearXNG per dottrina). Preferita per query legali.
2. **Skill `perplexity-web-mcp`** — se installata, per ricerca/deep-research con modelli premium.
3. **Ricerca web nativa** — fallback, con parametri di lingua/recency meno controllati.

Per la verifica puntuale di sentenze o articoli, se disponibili, sono preferibili gli MCP legali
dedicati (BuddaLaw, GestioLex Corpus) rispetto alla ricerca web generica.

## Rami runtime

- **Se stai operando in Claude Desktop, Claude for Work/Cowork o Claude Code:** invoca la skill
  `ricerca-web-searXNG` o `perplexity-web-mcp` se presenti; in mancanza, usa `WebSearch` nativo
  dichiarandolo (`[WebSearch fallback]`). Non configurare né autenticare MCP a pagamento senza il
  consenso dell'utente.
- **Se stai operando in Codex o in un ambiente OpenAI:** usa i tool MCP/web disponibili
  nell'ambiente Codex (es. namespace `mcp__searxng`), mantenendo lo stesso routing logico; se la
  ricerca web non è disponibile, chiedi conferma all'utente per procedere offline o per
  configurare SearXNG.

In nessun caso usare un fallback in modo silenzioso: il cambio di strumento va sempre dichiarato.

## Confidenzialità

Se il quesito contiene dati personali reali (cliente, dipendente, casella di posta, dati di
contenzioso), **non inviarli a servizi online** senza il consenso esplicito dell'utente.
Astrai il quesito (rimuovi nomi e dettagli identificativi) prima di qualsiasi ricerca, oppure
chiedi se procedere. Non considerare riservato un documento solo perché *parla* di lavoro o email:
guarda i dati personali effettivamente presenti.
