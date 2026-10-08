# BuddaLaw — Schema completo tool MCP

Riferimento rapido per parametri, tipi e note operative di tutti i tool disponibili.

---

## check_access

Verifica che l'utente abbia un abbonamento attivo a BuddaLaw.

```
check_access()
```

Nessun parametro. Chiamare **una sola volta per sessione**, alla prima query.

---

## search_case_law

Ricerca sentenze e provvedimenti nelle banche dati giurisprudenziali.

| Parametro | Tipo | Obbligatorio | Note |
|---|---|:---:|---|
| `query` | string | SI | Linguaggio naturale giuridico italiano |
| `search_category` | string | SI | Vedi tabella sotto |
| `max_results` | integer | no | Default 5; usare 3 (mirato), 5 (default), 10 (esplorativo) |
| `semantic_weight` | float | no | Default 0.7; range 0.0–1.0 |
| `numero` | integer | no | Numero della sentenza (solo se noto) |
| `anno` | integer | no | Anno della sentenza (solo se noto) |
| `data_deposito` | string | no | Data minima deposito, formato `"YYYY-MM-DD"`. Usare per ricerche temporali ("sentenze recenti", "post-riforma") |
| `ufficio` | string | no | Es. `"Cassazione civile"`, `"Tribunale Milano"` |
| `giudice` | string | no | Nome del giudice estensore (raro) |

**Valori `search_category`:** `civile` · `penale` · `tributari` · `prassi` · `merito` · `privacy` · `amministrativo`

**Note operative sui risultati:**
- **Lo score è solo indicativo.** Il motore semantico restituisce sempre risultati
  (non torna mai a vuoto): uno score alto non garantisce pertinenza e uno score
  basso non implica irrilevanza — una pronuncia con score 0.30 può essere quella
  che enuncia il principio cardine. Valutare la pertinenza su `sintesi`/`caso_concreto`,
  non sul numero.
- **`data_deposito` non è garantito dal server.** Il filtro per data viene spesso
  ignorato silenziosamente: dopo una ricerca con `data_deposito`, verificare il
  campo `data_deposito` di ciascun risultato e scartare quelli anteriori al limite
  prima di presentarli.

---

## get_judgement

Recupera il testo completo di una sentenza o provvedimento.

| Parametro | Tipo | Obbligatorio | Note |
|---|---|:---:|---|
| `idatto` | string | no* | GUID del provvedimento — preferire quando disponibile |
| `dominio` | string | SI | Vedi tabella sotto |
| `numero` | integer | no* | Numero sentenza |
| `anno` | integer | no* | Anno sentenza |
| `ufficio` | string | no | Filtro opzionale |

*`idatto` OPPURE `numero`+`anno` — preferire GUID quando disponibile (più affidabile per Garante Privacy e CGT).

**Valori `dominio`:** `civile` · `penale` · `tributario` · `tributario-prassi` · `merito` · `amministrativo` · `privacy` · `lavoro` · `data-protection-authority`

**Nota Cassazione:** per sezioni lavoro, commerciale, tributaria (Sez. V) usare sempre `dominio="civile"`. Il dominio `lavoro` è disponibile per corti di merito. Il dominio `data-protection-authority` è alias di `privacy` per il Garante.

**Limite temporale (≥ 2019):** `get_judgement` recupera solo decisioni **dal 2019 in poi**. Per le decisioni anteriori restituisce **HTTP 400** e non trova nulla: non insistere. Quando la decisione ante-2019 è una pronuncia nomofilattica (Sezioni Unite, Adunanza Plenaria) rilevante per il quesito, applicare il **fallback** descritto in SKILL.md → «REGOLA QUALITÀ — Sezioni Unite e contrasti»: citarla come riportata nella sentenza che la richiama, in forma testuale e senza inventare un link.

---

## search_articles

Ricerca articoli di legge nella normativa italiana.

| Parametro | Tipo | Obbligatorio | Note |
|---|---|:---:|---|
| `query` | string | SI | Linguaggio naturale giuridico italiano |
| `domain` | string | SI | Vedi tabella sotto |
| `max_results` | integer | no | Default 5 |

**Valori `domain`:** `civil_code` · `civil_procedure` · `special_civil` · `special_civil_procedure` · `criminal` · `tax` · `privacy`

---

## search_contracts

Ricerca template contrattuali per parole chiave.

| Parametro | Tipo | Obbligatorio | Note |
|---|---|:---:|---|
| `query` | string | SI | Es. `"contratto di locazione commerciale"` |

---

## list_contract_categories

Elenca tutte le categorie di contratti disponibili. Nessun parametro.
Usare come **Step 1** nel workflow contratti per orientarsi sulle categorie.

---

## list_contracts

Elenca i contratti disponibili in una categoria.

| Parametro | Tipo | Obbligatorio | Note |
|---|---|:---:|---|
| `category_id` | string | SI | ID categoria da `list_contract_categories` |

---

## get_contract

Recupera il template completo di un contratto.

| Parametro | Tipo | Obbligatorio | Note |
|---|---|:---:|---|
| `contract_id` | string | SI | ID da `search_contracts` o `list_contracts` |

---

## get_contract_requirements

Recupera i requisiti normativi obbligatori per un tipo di contratto.

| Parametro | Tipo | Obbligatorio | Note |
|---|---|:---:|---|
| `contract_id` | string | SI | Stesso `contract_id` usato in `get_contract` |

**Nota:** i requisiti `general` vengono spesso restituiti in duplicato — deduplicare per `title` prima di presentarli. Il campo `reference_data` contiene la fonte normativa: citarla sempre.

---

## search_processual_acts

Ricerca atti processuali (citazioni, ricorsi, memorie, opposizioni, ecc.).

| Parametro | Tipo | Obbligatorio | Note |
|---|---|:---:|---|
| `query` | string | SI | Es. `"ricorso per decreto ingiuntivo"` |
| `max_results` | integer | no | Default 5 |

---

## list_processual_act_categories

Elenca tutte le categorie di atti processuali disponibili. Nessun parametro.
Usare come **Step 1** nel workflow atti processuali per identificare il tipo corretto.

---

## list_processual_acts

Elenca gli atti disponibili in una categoria.

| Parametro | Tipo | Obbligatorio | Note |
|---|---|:---:|---|
| `category_id` | string | SI | ID da `list_processual_act_categories` |

---

## get_processual_act

Recupera template completo e istruzioni di compilazione di un atto processuale.

| Parametro | Tipo | Obbligatorio | Note |
|---|---|:---:|---|
| `act_id` | string | SI | ID atto da `search_processual_acts` o `list_processual_acts` |

Il template include sempre istruzioni di compilazione: seguirle rigorosamente.
