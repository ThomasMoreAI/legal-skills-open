# Normattiva MCP Skill

Normattiva (`dati.normattiva.it`) è la banca dati ufficiale della normativa italiana consolidata. Il server MCP espone le sue API REST: tutti i nomi dei tool e dei campi sono in italiano. Questa skill spiega come scegliere e combinare i tool — per i dettagli su parametri e formati, fare riferimento alle descrizioni dei singoli tool MCP.

---

## Identificatori

Due identificatori ricorrono in tutta l'API:

- **`codiceRedazionale`**: codice alfanumerico come `"056U0675"` — chiave primaria di un atto in Normattiva. Viene restituito dai risultati di ricerca.
- **URN**: stringa strutturata come `urn:nir:stato:legge:1975-05-23;654` — utile quando l'utente ha già un riferimento da una fonte esterna.

---

## Scegliere l'approccio di ricerca

| Situazione | Tool | Note |
|---|---|---|
| Query in linguaggio naturale ("legge sulla privacy") | `ricercaSemplice` | Passare `testoRicerca` |
| Criteri strutturati (tipo atto, date, numero, ente) | `ricercaAvanzata` | Chiamare prima i tool tipologici per valori validi |
| Atto citato per numero ("Legge 300/1970") | `ricercaAvanzata` | Usare `numeroProvvedimento` + `annoProvvedimento` — più preciso della ricerca libera |
| Atti modificati in un intervallo di date | `ricercaAttiAggiornati` | Per export bulk, concatenare con il flusso asincrono |
| Nessuna query specifica, voglia di sfogliare | `ricercaPredefinita` | Restituisce categorie predefinite |

---

## Flusso di lavoro tipico

1. **Cercare** → scegliere il tool di ricerca appropriato dalla tabella sopra.
2. **Leggere i risultati** → `listaAtti` contiene i risultati; ogni elemento ha `codiceRedazionale` e `dataGU`.
3. **Recuperare il testo** → `getDettaglioAtto` (per codice) o `getDettaglioAttoByUrn` (per URN).
4. **Offrire l'URI ELI** → chiamare sempre `getEliUri` dopo aver recuperato un atto — fornisce un link permanente, navigabile e citabile, senza costo aggiuntivo.

---

## Esportazione bulk (flusso asincrono)

Per esportare molti atti contemporaneamente, usare il flusso in 4 passi:

`nuovaRicercaAsincrona` → `confermaRicercaAsincrona` → polling `checkStatus` → `scaricaCollezioneAsincrona`

Fare polling di `checkStatus` a intervalli ragionevoli (qualche secondo). I codici `stato` da 0 a 6 rappresentano fasi diverse; `descrizioneStato` indica il progresso o eventuali fallimenti.

In alternativa, per dataset curati: `ottieniCollezioniPredefinite` → `scaricaCollezionePreconfezionata`.

---

## Note operative

- L'API è solo in italiano; rispondere all'utente nella sua lingua sapendo che parametri e risposte dei tool sono in italiano.
- Controllare sempre `listaAtti` nei risultati di ricerca e `codiceRedazionale` su ciascun elemento.
