# Tooling e installazione minima

Apri questo reference solo quando BuddaLaw o Perplexity non sono disponibili,
oppure quando l'utente chiede setup/installazione.

## Regola di comportamento

Se mancano skill o MCP, non fermare il memo salvo che la verifica live sia
essenziale. Procedi con una bozza e marca chiaramente i punti da verificare.

Solo al primo lancio della skill in un ambiente nuovo chiedere:

> Hai un abbonamento BuddaLaw e/o Perplexity? Vuoi che prepari o installi le
> relative skill e configurazioni MCP?

Non ripetere la domanda nella stessa sessione.

## BuddaLaw

Uso: sentenze italiane, provvedimenti, prassi, contratti e atti processuali.

Repository skill:

- `https://github.com/avvocati-e-mac/skill-legali`
- cartella sorgente: `buddalaw/buddalaw`
- file Claude installabile: `buddalaw/buddalaw.skill`

Regole minime:

- l'MCP BuddaLaw richiede abbonamento/configurazione locale;
- non inventare endpoint o credenziali;
- in Claude/Claude Code usare i tool MCP esposti dal runtime;
- in Codex/OpenAI usare namespace MCP disponibili, ad esempio `mcp__buddalaw`
  se presente;
- chiamare il gate di accesso previsto dalla skill BuddaLaw una sola volta per
  sessione;
- se non disponibile, non citare sentenze specifiche dalla memoria.

## Perplexity Web MCP

Uso: ricerche web, dottrina, fonti di contesto, confronto di strutture,
aggiornamenti non coperti da banche dati legali.

Skill:

- nome: `perplexity-web-mcp`
- CLI: `pwm`
- MCP server: `pwm-mcp`

Comandi minimi per assistente a riga di comando:

```bash
pwm --ai
pwm login --check
pwm usage
```

Configurazione MCP Claude Code:

```bash
claude mcp add perplexity pwm-mcp
```

Uso minimo:

```bash
pwm ask "query" --intent quick
pwm ask "query" --intent standard
```

Regole:

- controllare quota prima della prima query;
- usare quick/Sonar per ricerche semplici;
- non usare Deep Research senza richiesta esplicita;
- non usare Perplexity per fondare da solo una citazione giurisprudenziale
  italiana se BuddaLaw/GestioLex o fonte ufficiale non l'hanno verificata.

## Fallback senza abbonamenti

Se BuddaLaw e Perplexity non sono disponibili:

1. usare documenti forniti dall'utente;
2. usare Normattiva/GestioLex se disponibili;
3. usare fonti ufficiali o web aperto solo se il runtime lo consente;
4. marcare il memo come bozza da verificare;
5. inserire una checklist finale delle ricerche da fare.
