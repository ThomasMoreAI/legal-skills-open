# Classificazione — tassonomia, casi controversi, categorie di dati

Il ruolo va ipotizzato rispetto al rapporto con **il cliente dello studio
(titolare)**. Nota di metodo: la qualifica dipende dalla prestazione concreta
resa, che il mastrino non rivela — è uno screening da validare con cliente e
contratti; la Confidenza deve rifletterlo.

## Le tre categorie (una sola per fornitore)

### `responsabile` — Responsabile del trattamento (art. 28 GDPR)
Tratta dati personali PER CONTO del titolare, su sue istruzioni.
Esempi: cloud/hosting/SaaS, software gestionali con accesso ai dati, agenzie
marketing/adv che gestiscono liste o campagne del titolare, piattaforme di
e-mail marketing, payroll gestito per conto, manutentori IT con accesso ai
sistemi, call center, società di archiviazione/distruzione documenti.

### `titolare_autonomo` — Titolare autonomo
Determina autonomamente finalità e mezzi del trattamento.
Esempi: commercialista, avvocati e notai esterni, banche e istituti di
pagamento, assicurazioni, medico competente, agenzie interinali, e — di norma —
consulente del lavoro / studio paghe.

### `fuori_perimetro` — Fuori perimetro privacy
Non tratta dati personali per conto del cliente.
Esempi: fornitori di soli beni, cancelleria, utenze (luce/gas/acqua),
carburante, hardware senza accesso ai sistemi, manutenzioni edili/impianti,
ristorazione, pulizie (senza accesso sistematico a dati).

## Casi controversi — default + flag

Assegna il default, scrivi `controverso` in `note`, Confidenza MAI sopra `medio`:

| Fornitore | Default | Perché è controverso |
|-----------|---------|----------------------|
| Consulente del lavoro / studio paghe | `titolare_autonomo` | Prassi e giurisprudenza oscillano; se opera su istruzioni stringenti può essere responsabile |
| Corrieri / spedizionieri | `titolare_autonomo` | Trattano i dati dei destinatari con autonomia organizzativa propria |
| Recupero crediti | dipende dalla ricerca | Mandato su istruzioni = `responsabile`; acquisto del credito = `titolare_autonomo`. Confidenza `basso` |
| Telefonia / TLC business | `titolare_autonomo` | Titolari per i dati di traffico; ma servizi gestiti (centralino cloud) possono renderli responsabili |
| Software house locale con assistenza | `responsabile` | Se ha accesso anche solo occasionale ai sistemi/dati; verificare il contratto di assistenza |

## Categorie di dati presumibilmente trattate (per compilare `categorie_dati`)

- Responsabili IT/cloud: «dati di clienti/utenti/dipendenti del titolare
  ospitati o accessibili nei sistemi».
- Payroll/consulenti lavoro: «dati dei dipendenti, anche particolari
  (salute: assenze, visite) e giudiziari ove previsti».
- Marketing: «dati di contatto e comportamentali di clienti/prospect».
- Corrieri: «dati identificativi e di recapito dei destinatari».
- Professionisti (commercialista, legali): «dati contabili/fiscali/giudiziari
  pertinenti all'incarico».
- Fuori perimetro: «nessuno per conto del titolare» (o vuoto).
