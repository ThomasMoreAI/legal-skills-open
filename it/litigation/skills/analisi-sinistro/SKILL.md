---
name: analisi-sinistro
title: Analisi Sinistro
description: Analizza sinistri stradali, sanitari e lavorativi con quantificazione del danno non patrimoniale (unitario, ex art. 2059 c.c.), rivalutazione ISTAT e interessi compensativi. Usa quando l'utente descrive un incidente, un sinistro, chiede risarcimento danni per invalidita o quantificazione danni da lesioni personali.
author: capazme
author_url: https://github.com/capazme/mcp-legal-it/tree/main/plugin/skills/analisi-sinistro
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: litigation
language: it
---

# Analisi Sinistro

Quantificazione del danno NON PATRIMONIALE da sinistro stradale, sanitario o lavorativo.

**Principio (Cass. SS.UU. 26972/2008, «San Martino»)**: il danno non patrimoniale è UNITARIO
(art. 2059 c.c.). Biologico, morale ed esistenziale sono aspetti di un unico pregiudizio, NON
poste autonome da sommare. Le Tabelle di Milano liquidano un valore COMPLESSIVO che già incorpora
la componente morale.

## Workflow

### 1. Danno non patrimoniale (valore complessivo, unitario)

Chiama UNA SOLA VOLTA `legal-it:danno_non_patrimoniale` con `percentuale_invalidita` (intero) e
`eta_vittima` (intero). Usa le Tabelle di Milano (macro >9%) o l'art. 139 Cod. Ass. (micro ≤9%).
Il valore restituito è GIÀ comprensivo del danno morale.

NON chiamare in aggiunta un tool di "danno morale" da sommare: duplicherebbe la componente già
inclusa (unitarietà del danno non patrimoniale).

### 2. Personalizzazione (solo se motivata da circostanze eccezionali)

Solo in presenza di circostanze peculiari documentate, applica una personalizzazione ENTRO i tetti
massimi della tabella (calcolata sulla componente biologica), tramite `personalizzazione_pct`. NON
è una seconda voce cumulata: è un incremento del valore tabellare entro i limiti. In base al tipo:
- **Stradale**: dinamica relazionale (mobilità, lavoro, sport)
- **Sanitario**: sofferenza iatrogena da errore medico
- **Lavoro**: incidenza sulla capacità lavorativa specifica

### 3. Rivalutazione monetaria (debito di valore)

Chiama `legal-it:rivalutazione_monetaria` dalla data del sinistro a oggi.

### 4. Interessi compensativi (Cass. SS.UU. 1712/1995)

NON calcolare gli interessi sul capitale INTERAMENTE rivalutato all'attualità: sarebbe la
sovra-compensazione censurata dalle SS.UU. Calcolali sulla somma PROGRESSIVAMENTE rivalutata anno
per anno o, in via semplificata, sul VALORE MEDIO tra somma originaria e somma finale rivalutata:
chiama `legal-it:interessi_legali` sulla base `(somma_originaria + somma_rivalutata) / 2`.

## Output atteso

| Voce | Importo |
|------|---------|
| Danno non patrimoniale (valore complessivo, morale incluso) | ... |
| Personalizzazione (se ricorrente, entro i tetti) | ... |
| Rivalutazione monetaria | ... |
| Interessi compensativi (su base media/progressiva) | ... |
| **TOTALE RISARCIMENTO** | **...** |

## Avvertenze da includere

- Danno non patrimoniale UNITARIO: una sola voce comprensiva del morale (SS.UU. 26972/2008) — non sommare biologico e morale come poste distinte.
- Interessi compensativi sulla somma progressivamente rivalutata / valore medio, MAI sul capitale già interamente rivalutato (SS.UU. 1712/1995).
- Valori INDICATIVI (Tabelle di Milano macro >9% / art. 139 Cod. Ass. micro ≤9%) — non sostituiscono la valutazione medico-legale.
- Per ITT/ITP, danno emergente e lucro cessante servono dati aggiuntivi.
- Citare sempre la fonte tabellare e normativa.
