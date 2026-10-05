# Task: Tracking pixel nelle e-mail - voce di Registro, soglia DPIA e checklist Linee guida Garante 284/2026

Supporta il censimento nel Registro art. 30 GDPR del trattamento "tracking pixel nelle
comunicazioni di posta elettronica", la valutazione della soglia DPIA per tale
trattamento e la verifica di conformita' alle Linee guida del Garante (provv. n. 284 del
17 aprile 2026, GU Serie Generale n. 98 del 29/04/2026).

**Termine di adeguamento**: le Linee guida fissano un termine di sei mesi dalla
pubblicazione in GU (29/04/2026), quindi **29 ottobre 2026** (estratto
`garante-prov284-2026-tracking-pixel.md`, sezione "Dispositivo").

## Obiettivo

Produrre, a seconda della richiesta dell'utente:
1. una **scheda di Registro art. 30** per il trattamento tramite tracking pixel;
2. una **valutazione di soglia DPIA** specifica per l'uso dei pixel;
3. una **checklist di conformita'** agli adempimenti delle Linee guida (informativa,
   presupposto giuridico/consenso, revoca granulare, privacy by design).

## Input richiesti

- Tipologie di messaggi inviati con pixel: newsletter, DEM, transazionali/automatici,
  di servizio (classificazione par. 3 delle Linee guida)
- Finalita' del pixel: statistica aggregata (deliverability/antispam), sicurezza
  autenticazione, messaggi con obbligo giuridico di invio, misurazione individuale
  delle aperture, personalizzazione, profilazione commerciale
- Il pixel e' univoco per destinatario o unico per campagna? I dati tecnici correlati
  (IP, client) sono anonimizzati?
- Soggetti coinvolti: invio in-house o tramite fornitore di servizi emailing /
  noleggio liste / fornitore tecnologia di tracciamento
- Numero destinatari e frequenza invii (per la valutazione di larga scala)
- I dati di apertura sono combinati con altri dati (CRM, navigazione, acquisti)?
- Trattamento gia' in corso al 29/04/2026 o avviato dopo?

## Fonti

Leggere prima:
- `references/estratti/garante-prov284-2026-tracking-pixel.md` - Linee guida 284/2026
- `references/estratti/gdpr-art-30.md` - contenuti minimi del Registro
- `references/estratti/garante-allegato1-prov467-2018.md` - 12 tipologie DPIA Italia
- `references/estratti/wp248-criteri.md` - 9 criteri WP248 rev. 01

## Procedura

### Passo 1 - Classificare la finalita' del pixel (determina il presupposto giuridico)

Ai sensi dell'art. 122, comma 2-bis, del Codice vige un divieto generalizzato salvo
deroghe (Linee guida, par. 5). Classificare ogni impiego del pixel dichiarato
dall'utente in una delle due colonne:

| Impiego (par. 5-6 Linee guida) | Presupposto |
|---|---|
| Conteggio statistico della percentuale globale di apertura, con pixel unici per campagna (non differenziati per utente) e anonimizzazione dei dati tecnici correlati (IP, client) | Deroga - consenso non necessario (par. 5, caso 1) |
| Pixel funzionale a misure di sicurezza del processo di autenticazione (conferma account, modifica password, esercizio diritti) | Deroga - consenso non necessario (par. 5, caso 2) |
| Messaggi istituzionali o di servizio con obbligo giuridico di invio, per i quali rileva l'effettiva presa di conoscenza | Deroga - consenso non necessario (par. 5, caso 3) |
| Misurazione individuale e analisi del tasso di apertura per valutare/migliorare le performance delle campagne sulla base dei comportamenti osservati | Consenso preventivo obbligatorio (par. 6) |
| Adattamento di frequenza/oggetto o interruzione invii in base all'interesse manifestato dal singolo destinatario | Consenso preventivo obbligatorio (par. 6) |
| Uso del dato di lettura per inferire gusti/interessi/preferenze e creare profili commerciali, anche per iniziative diverse | Consenso preventivo obbligatorio (par. 6) |

Attenzione: la deroga statistica vale SOLO se le misurazioni non sono personalizzate.
Se il pixel e' univoco per destinatario e i dati non sono anonimizzati, la fattispecie
ricade nella colonna "consenso" (par. 5, caso 1, a contrario).

### Passo 2 - Scheda di Registro art. 30

Se l'uso di tracking pixel costituisce un trattamento di dati personali (cioe' fuori
dal caso statistico pienamente anonimizzato), il trattamento va censito nel Registro.
Usare lo schema di `tasks/draft-registro-trattamenti.md` (Passo 3), popolato con i
contenuti tratti dalle Linee guida:

```
SCHEDA TRATTAMENTO N. [N]
Nome interno: Tracciamento aperture e-mail tramite tracking pixel

b) Finalita' (distinguere - par. 2 e 5-6 Linee guida):
   [ ] misurazione statistica aggregata apertura campagne (deliverability, antispam)
   [ ] sicurezza del processo di autenticazione
   [ ] verifica presa di conoscenza di messaggi con obbligo giuridico di invio
   [ ] misurazione individuale aperture / ottimizzazione campagne
   [ ] personalizzazione della comunicazione in base all'interesse rilevato
   [ ] profilazione commerciale (gusti, interessi, preferenze)

   Base giuridica: per le finalita' soggette a consenso ex art. 122 Codice ->
   consenso art. 6.1.a) GDPR (raccolto secondo par. 6 Linee guida: consenso unico
   con quello promozionale ammesso, se richiesta neutra e priva di forzature).
   Per le finalita' in deroga -> indicare la deroga art. 122 applicabile
   (par. 5, casi 1-3) e la base art. 6 del trattamento sottostante.

c) Categorie di interessati: destinatari delle comunicazioni e-mail (iscritti
   newsletter, clienti, utenti registrati - par. 3 Linee guida)

c) Categorie di dati personali (par. 1 Linee guida, GU pag. 96):
   - evento di apertura/consultazione dell'e-mail (anche aperture successive)
   - indirizzo IP del destinatario
   - tipo di dispositivo utilizzato
   - tempo di consultazione del messaggio e numero di aperture
   - identificativo del pixel (di regola univoco per destinatario), user ID,
     message ID, delivery ID (time stamp dell'invio), eventuali token di sicurezza

d) Categorie di destinatari (par. 3 Linee guida):
   - fornitore di servizi di invio e-mail / piattaforma emailing (SaaS)
   - eventuale fornitore di servizi di noleggio liste di distribuzione
   - eventuale fornitore della tecnologia di tracciamento
   (definire i ruoli: responsabile ex art. 28, o contitolare ex art. 26 - le Linee
   guida richiamano la definizione dei ruoli caso per caso ex art. 5, par. 2)

e) Trasferimenti extra-UE: verificare dove il fornitore emailing/tracciamento
   tratta i dati (schema standard del task draft-registro-trattamenti)

f) Termini di conservazione: [da policy del titolare - le Linee guida non fissano
   termini; documentare la scelta in ottica accountability]

g) Misure di sicurezza (par. 6 Linee guida + art. 32):
   - identificativo del pixel inintelligibile e non sequenziale
   - corrispondenza identificativo/indirizzo e-mail in layer interno e separato
     della piattaforma (l'indirizzo non transita nella richiesta del pixel)
   - per la finalita' statistica: pixel unico per campagna + anonimizzazione di
     IP e dati client
   - registrazione delle scelte di consenso/revoca (art. 7, par. 1 GDPR)

DPIA effettuata: [SI / NO / IN VALUTAZIONE - vedi Passo 3]
```

### Passo 3 - Valutazione soglia DPIA

Le Linee guida 284/2026 non impongono di per se' una DPIA (vedi "Nota di perimetro"
nell'estratto). La soglia si valuta con il task `valuta-soglia-dpia.md`, applicando le
fonti generali ai fatti descritti dalle Linee guida. Elementi istruttori specifici:

- **Tipologia 3 Allegato 1 Provv. 467/2018** (monitoraggio sistematico, raccolta dati
  attraverso reti, "trattamento di identificativi univoci in grado di identificare gli
  utenti di servizi della societa' dell'informazione ... rispetto alle abitudini d'uso
  ... per periodi prolungati"): pertinente perche' le Linee guida accertano che "di
  regola i tracciatori sono univoci per singolo destinatario" (par. 1, GU pag. 96).
  Verificare sistematicita' e durata del monitoraggio nel caso concreto.
- **Tipologia 1 Allegato 1** (profilazione su larga scala relativa a "preferenze o
  interessi personali ... comportamento"): pertinente se il pixel serve a creare
  profili commerciali dai dati di lettura (par. 6, GU pag. 100).
- **Tipologia 4 Allegato 1** (dati a carattere estremamente personale, tra cui "i dati
  relativi alle comunicazioni elettroniche dei quali occorre tutelare la riservatezza"),
  se su larga scala: le Linee guida qualificano la posta elettronica come servizio "per
  sua stessa natura destinato a veicolare contenuti privati" (par. 1, GU pag. 96),
  fermo restando che i pixel monitorano solo l'evento di apertura, non il contenuto.
- **Criteri WP248** da vagliare: n. 1 (valutazione/profilazione), n. 3 (monitoraggio
  sistematico), n. 5 (larga scala: numero interessati, volume, durata, estensione
  geografica), n. 6 (combinazione di dataset, se i dati di apertura sono incrociati con
  altri dati raccolti per finalita' diverse).

Esiti secondo le soglie gia' definite in `valuta-soglia-dpia.md`: anche 1 sola
tipologia dell'Allegato 1 attiva la DPIA obbligatoria in Italia; 2+ criteri WP248 la
rendono richiesta. Il conteggio va fatto sul caso concreto, non in astratto: una
newsletter con solo conteggio statistico anonimizzato (deroga par. 5, caso 1) di regola
non attiva ne' tipologie ne' criteri; un sistema di profilazione individuale delle
aperture su ampia base utenti attiva tipicamente tipologia 1 e/o 3 + criteri 1, 3, 5.

### Passo 4 - Checklist di conformita' alle Linee guida (adeguamento entro 29/10/2026)

| # | Adempimento | Riferimento | Esito |
|---|-------------|-------------|-------|
| 1 | Informativa che rende noto preventivamente l'impiego di tracking pixel e la finalita' del loro utilizzo, qualunque sia lo scopo della comunicazione | par. 4; dispositivo, punto (i) | [OK/GAP] |
| 2 | Informativa su piu' livelli (sintesi nel modulo di raccolta indirizzo + link a dettaglio, anche in cookie policy) o multichannel | par. 4 | [OK/GAP] |
| 3 | Per trattamenti gia' in corso: informativa resa con il primo invio utile o primo momento di discontinuita' | par. 4 | [OK/GAP/N.A.] |
| 4 | Per ogni impiego del pixel: deroga art. 122 documentata (par. 5, casi 1-3) oppure consenso preventivo informato, libero, specifico e inequivocabile | par. 5-6; dispositivo, punto (ii) | [OK/GAP] |
| 5 | Se deroga statistica: pixel unico per campagna (non per utente) + anonimizzazione dati tecnici correlati (IP, client) | par. 5, caso 1 | [OK/GAP/N.A.] |
| 6 | Consenso unico (promozionale + pixel) formulato in modo neutro e privo di forzature | par. 6 | [OK/GAP/N.A.] |
| 7 | Meccanismo di revoca agevole e granulare: revoca totale oppure del solo tracciamento, es. icona/link nel footer di ogni e-mail verso area diritti | par. 6; dispositivo, punto (iii) | [OK/GAP] |
| 8 | Per trattamenti gia' in corso: meccanismo di revoca granulare reso noto, con massima riconoscibilita', visibilita' e facilita' d'uso | par. 6 | [OK/GAP/N.A.] |
| 9 | Piena fruibilita' del servizio garantita a chi rifiuta il tracciamento | par. 6 | [OK/GAP] |
| 10 | Registrazione delle scelte dell'interessato ai fini di prova (art. 7, par. 1 GDPR) | par. 6 | [OK/GAP] |
| 11 | Privacy by design: identificativo pixel inintelligibile e non sequenziale; corrispondenza con l'indirizzo e-mail in layer interno e separato | par. 6; dispositivo, punto (iv) | [OK/GAP] |
| 12 | Ruoli privacy definiti con i fornitori coinvolti (emailing, noleggio liste, tecnologia di tracciamento): art. 26/28 GDPR | par. 3 | [OK/GAP] |
| 13 | Trattamento censito nel Registro art. 30 (Passo 2) e soglia DPIA valutata e documentata (Passo 3) | art. 30 GDPR; art. 35 GDPR | [OK/GAP] |

### Passo 5 - Output

Comporre il documento finale: scheda di Registro + esito soglia DPIA + checklist con
i GAP evidenziati e il termine del 29/10/2026 per la chiusura degli adempimenti delle
Linee guida. Chiudere sempre con il rinvio alla revisione del DPO o consulente legale.

## Casi limite

- **Solo e-mail transazionali con pixel di sicurezza**: deroga par. 5, caso 2; il
  trattamento sottostante va comunque censito nel Registro se non anonimo.
- **ESP che impone il pixel di default**: il mittente resta il soggetto cui compete la
  scelta sull'uso dei pixel e sulle finalita' (par. 3); non puo' delegare la
  compliance al fornitore. Verificare configurazione della piattaforma e contratto
  art. 28.
- **Client di posta che blocca le immagini**: il pixel non viene scaricato se il
  download immagini e' disabilitato (par. 1, GU pag. 96); cio' non riduce gli obblighi
  del titolare, perche' il blocco non e' selettivo per singolo pixel.

## Limiti di questo task

- Non fornisce parere legale sulla riconducibilita' del caso concreto alle deroghe
  dell'art. 122: la valutazione compete al titolare (par. 5 Linee guida) con il
  supporto del DPO/legale.
- Non copre l'invio promozionale in se' (consenso ex art. 130 Codice, soft spam):
  perimetro limitato al tracciamento tramite pixel.
- La quantificazione di "larga scala" e "periodi prolungati" richiede
  contestualizzazione caso per caso (vedi `references/estratti/wp248-criteri.md`).

## Esempi

Vedi `examples/`:
- `registro-tracking-pixel-newsletter/` - newsletter PMI con misurazione individuale
  delle aperture: scheda registro + checklist con GAP tipici pre-adeguamento
