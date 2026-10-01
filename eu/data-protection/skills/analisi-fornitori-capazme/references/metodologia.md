# Metodologia — estrazione, dedup, identificazione, confidenza

## Contratto (record canonico per fornitore)

```json
{
  "denominazione_mastrino": "obbligatorio — come appare nel mastrino",
  "piva_cf": "11 cifre P.IVA o 16 caratteri CF, oppure null",
  "fonte_piva": "mastrino | vies | web | null",
  "attivita": "sintesi dalla ricerca (con fonte)",
  "classe_attivita": "obbligatorio — etichetta breve minuscola del TIPO di fornitore (es. giornalista, social media manager, hosting/cloud, ristorazione). Riusa SEMPRE, identica, un'etichetta già in uso quando il fornitore vi rientra: mai un sinonimo o una variante più specifica (`giornalista`, non `giornalista freelance`). Fornitori dello stesso tipo DEVONO avere la stessa qualificazione: il tool rifiuta il lotto se una classe ne porta due — ma confronta le etichette per stringa esatta, quindi un sinonimo gli nasconde l'incoerenza.",
  "categorie_dati": "categorie di dati presumibilmente trattate",
  "qualificazione": "responsabile | titolare_autonomo | fuori_perimetro",
  "motivazione": "obbligatoria, sintetica",
  "probabilita_responsabile": "alta | media | bassa — SOLO se responsabile",
  "dpa_proprio": "si | no | da_verificare — SOLO se responsabile",
  "confidenza": "alto | medio | basso",
  "fonti": ["URL"],
  "note": "flag controverso, omonimie, VIES indisponibile, ecc."
}
```

Valori in snake_case minuscolo: il tool `genera_report_fornitori` valida e
rifiuta tutto il lotto elencando le righe errate.

## Estrazione per formato

- **Excel/CSV** (export gestionali: TeamSystem, Zucchetti, Danea…): cerca le
  colonne denominazione/ragione sociale/fornitore e P.IVA/CF/partita IVA. Righe
  di subtotale, saldo o riporto NON sono fornitori. Un file può avere più fogli.
- **PDF nativo**: tabelle estraibili come testo; attenzione alle denominazioni
  spezzate su due righe (ricomponile).
- **Scansione**: OCR; i numeri di P.IVA sono i più soggetti a errori OCR (0/O,
  1/I, 8/B) — se il checksum fallisce, trascrivi in `note` il dubbio invece di
  «correggere» a caso.
- **Corpo mail / elenco libero**: estrai le denominazioni così come scritte.
- In OGNI formato: gli importi si ignorano; l'IBAN non è un identificativo del
  ruolo privacy.

## Dedup e normalizzazione

1. Chiave primaria: **P.IVA/CF** quando presente (stessa P.IVA = stesso
   fornitore, qualunque sia la grafia).
2. Altrimenti **denominazione normalizzata**: maiuscole, senza punteggiatura,
   senza forme societarie (SRL, S.R.L., SPA, SNC, SAS, SS, DITTA, SOC. COOP.),
   spazi compressi.
3. Unifica le varianti evidenti («ACME», «ACME SRL», «ACME S.R.L. — MILANO»),
   registrandole in `varianti`. NON unificare nomi simili ma plausibilmente
   diversi («ROSSI SRL» vs «ROSSI COSTRUZIONI SRL»): meglio due voci che una
   fusione sbagliata.

## Identificazione (ricerca web)

- Query utili: `"{denominazione}" partita iva`, `"{denominazione}" {città se
  nota}`, `"{denominazione}" sito ufficiale`.
- Fonti preferite, in ordine: sito ufficiale del fornitore; directory camerali
  (ufficiocamerale.it, registroimprese.it e derivati); pagine social aziendali
  solo in mancanza d'altro.
- Se trovi una P.IVA via web: confermala con `verifica_partita_iva_vies` e, se
  valida e compatibile con la denominazione, imposta `fonte_piva: "web"` (o
  `"vies"` se è il VIES a fornire la denominazione decisiva).
- **Omonimia** (più soggetti plausibili) o nome generico: NON scegliere a caso.
  Categoria più probabile, `confidenza: "basso"`, alternative in `note`.

## Confidenza (taratura)

| Livello | Quando |
|---------|--------|
| `alto` | Identificazione univoca E confermata: P.IVA dal mastrino con VIES valido/denominazione compatibile, oppure P.IVA reperita e confermata senza soggetti alternativi |
| `medio` | Identificazione probabile ma non certa (nome distintivo, attività coerente, nessuna conferma P.IVA) |
| `basso` | Nome comune/generico, ambiguo, non identificato, o solo fonti deboli |

Nel dubbio, abbassa. Il VIES indisponibile non alza né abbassa: annota e procedi.
