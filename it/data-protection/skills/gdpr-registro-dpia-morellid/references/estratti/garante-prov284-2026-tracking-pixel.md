# Estratto: Provv. Garante n. 284/2026 - Linee guida tracking pixel nelle e-mail

**Fonte**: `sources.yaml` id `garante-prov-284-2026-tracking-pixel`
**Documento**: Provvedimento del Garante per la protezione dei dati personali n. 284 del
17 aprile 2026 - "Linee guida in materia di utilizzo di tracking pixel nelle
comunicazioni di posta elettronica" [doc. web n. 10241943]
**Pubblicazione**: Gazzetta Ufficiale Serie Generale n. 98 del 29 aprile 2026 (codice
redazionale 26A02030, pagg. 95-101 del fascicolo)
**Data consultazione**: 2026-07-11 (SHA256 del PDF GU verificato - coincide con hash dichiarato)
**Hash SHA256**: `df04bc934ff408a65e7845f5797425afcff1bf053768e64d8ca44811a0f1f544`
**Licenza**: provvedimento amministrativo italiano in pubblico dominio.
**Testo di riferimento**: `references/fonti/garante-prov284-2026-tracking-pixel.md`

I riferimenti "par. N" citano i paragrafi numerati del provvedimento; "GU pag. N" la
pagina del fascicolo GU n. 98/2026.

---

## Cosa sono i tracking pixel e quali dati generano (par. 1, GU pagg. 95-96)

- Immagini "spesso trasparenti e di dimensioni molto ridotte, pari appunto a un solo
  pixel, non direttamente contenute nell'e-mail in questione, ma ospitate su server
  remoti" (par. 1, GU pag. 95).
- Ad ogni apertura del messaggio (prima o successive), un codice HTML inoltra una
  richiesta al server del mittente; l'immagine viene scaricata dal client e archiviata
  nella memoria del terminale (par. 1, GU pag. 96).
- Informazioni ottenibili dal mittente o da un suo partner: avvenuta apertura/
  consultazione dell'e-mail da parte di un utente specifico, "informazioni ulteriori che
  possono ricavarsi dall'indirizzo IP del destinatario, relative al tipo di dispositivo
  utilizzato, fino al tempo di consultazione del messaggio e al numero di aperture
  successive della stessa e-mail" (par. 1, GU pag. 96).
- L'inclusione del pixel e' un'istruzione al terminale di inviare informazioni
  specifiche: "l'identificativo del pixel, l'indirizzo IP, lo user ID, il message ID, il
  delivery ID sotto forma di time stamp in relazione all'invio effettivo, eventuali
  token di sicurezza" (par. 1, lett. b, GU pag. 96).
- "Di regola i tracciatori sono univoci per singolo destinatario" (par. 1, GU pag. 96).
- I pixel non attengono al contenuto dei messaggi: "monitorano esclusivamente l'evento
  dell'avvenuta apertura della e-mail"; la loro pervasivita' e' correlata innanzitutto
  alla mancata consapevolezza del destinatario (par. 1, GU pag. 96).

## Disciplina applicabile (par. 1, GU pagg. 96-97)

- L'inserimento del pixel e la lettura delle informazioni che ne conseguono sono
  operazioni conformi alla fattispecie di accesso al terminale disciplinata
  dall'**art. 122 del Codice Privacy** (D.Lgs. 196/2003), nella duplice modalita'
  "archiviazione delle informazioni nell'apparecchio terminale" e "accesso a
  informazioni gia' archiviate" (par. 1, lett. a, GU pag. 96).
- La qualificazione e' conforme alle Linee guida EDPB 2/2023 sull'ambito di applicazione
  tecnico dell'art. 5, par. 3, della direttiva e-Privacy (par. 1, GU pag. 96).
- L'art. 122, comma 2-bis, del Codice vieta l'uso di una rete di comunicazione
  elettronica per accedere a informazioni archiviate nel terminale, per archiviare
  informazioni o per monitorare le operazioni dell'utente, salvo quanto previsto dal
  comma 1 (testo integrale dell'art. 122 riportato in fonte, GU pagg. 96-97).

## Finalita' rilevate e soggetti coinvolti (par. 2-3, GU pagg. 97-98)

- Finalita' accertate in sede ispettiva (ottobre 2025 e febbraio 2026): deliverability,
  contrasto allo spam, misurazione di audience e performance (apertura/lettura,
  download allegati), personalizzazione della comunicazione in base all'interesse
  rilevato, identificazione di phishing, esigenze di formattazione. I pixel "vengono
  utilizzati pressoche' nella totalita' dei casi" (par. 2, GU pag. 97).
- Soggetti coinvolti, che devono definire i propri ruoli privacy caso per caso ex
  art. 5, par. 2, e - eventualmente - art. 26 GDPR (contitolarita'): mittente;
  fornitore di servizi di invio e-mail (piattaforma, spesso SaaS); fornitore di servizi
  di noleggio liste di distribuzione e invio; fornitore della tecnologia di
  tracciamento; content creator; destinatario (par. 3, GU pagg. 97-98).
- Tipologie di messaggi: newsletter, DEM (Direct E-mail Marketing), e-mail
  transazionali e messaggi automatici, e-mail di servizio (par. 3, GU pag. 98).

## Obblighi di informativa (par. 4, GU pagg. 98-99)

- L'impiego di tracking pixel, per qualificarsi lecito, "debba essere preventivamente
  reso noto al destinatario della e-mail, qualunque sia lo scopo della comunicazione o
  la tipologia del soggetto mittente" (par. 4, GU pag. 98).
- Obbligo di informativa per tutti i titolari che usano o intendono usare pixel, ex
  art. 5, par. 1, lett. a) e artt. 12 ss. GDPR, "pena la loro inutilizzabilita'"
  (par. 4, GU pag. 98).
- Informativa su piu' livelli (forma sintetica nel modulo di raccolta dell'indirizzo +
  link a informazione dettagliata, anche nella cookie policy) o multichannel (canali
  video, pop-up, interazioni vocali, assistenti virtuali, telefono, chatbot) (par. 4,
  GU pagg. 98-99).
- Trattamenti gia' in corso: l'informativa puo' essere resa con "l'inoltro del primo
  messaggio utile ovvero il primo momento di discontinuita' eventualmente esistente"
  (par. 4, GU pag. 99).

## Presupposti giuridici: divieto generale e deroghe al consenso (par. 5, GU pagg. 99-100)

Divieto generalizzato ex art. 122, comma 2-bis, salvo: a) previo consenso informato,
libero, specifico e inequivocabile; b) trattamento necessario alla trasmissione della
comunicazione elettronica; c) operazioni necessarie alla fornitura di un servizio
richiesto dall'utente (par. 5, GU pag. 99).

Casi esemplificativi in cui il Garante ritiene applicabile la **deroga al consenso**
(par. 5, GU pagg. 99-100):

1. **Conteggio statistico** della percentuale globale di apertura (per deliverability e
   antispam), a condizione di adottare tecniche di anonimizzazione che non consentano
   misurazioni personalizzate: pixel univoci "non differenziati per ciascun utente, ma
   uguali per tutti i destinatari di una stessa campagna" e anonimizzazione dei dati
   tecnici correlati (indirizzo IP, client etc.); richiamato il parere WP29 05/2014
   sulle tecniche di anonimizzazione.
2. **Misure di sicurezza** sul processo di autenticazione (conferma attivazione account,
   modifica password, esercizio dei diritti tra cui portabilita').
3. **Messaggi istituzionali o di servizio** che il titolare ha l'obbligo giuridico di
   inoltrare e per i quali rileva l'effettiva presa di conoscenza (prevenzione phishing/
   frodi, modifiche contrattuali, informative privacy, notifiche di incidenti di
   sicurezza, campagne istituzionali, reminder su scadenze e adempimenti).

## Consenso: quando serve e come gestirlo (par. 6, GU pagg. 100-101)

- **Consenso preventivo obbligatorio** in tutti i casi non coperti da deroga; ad
  esempio: misurazione individuale e analisi del tasso di apertura per valutare e
  migliorare la performance delle campagne sulla base dei comportamenti osservati
  (modifica oggetto, adattamento frequenza, interruzione invii in base all'interesse);
  uso del dato di lettura "per ricavarne informazioni presunte circa i potenziali gusti,
  gli interessi e le preferenze attribuibili all'utente allo scopo di creare dei profili
  commerciali utilizzabili anche per iniziative diverse" (par. 6, GU pag. 100).
- Nuovi trattamenti: consenso raccolto preferibilmente al momento dell'acquisizione
  dell'indirizzo e-mail, previa informativa (par. 6, GU pag. 100).
- **Consenso unico**: il consenso alla ricezione dei tracking pixel puo', in linea di
  principio, essere ricompreso in quello piu' generale alla ricezione delle
  comunicazioni promozionali, purche' la richiesta sia "formulata in modo neutro e privo
  di forzature" (par. 6, GU pag. 100).
- **Revoca agevole e granulare**: revoca del consenso unico (stop a ulteriori messaggi)
  oppure revoca parziale del solo tracciamento; attuabile ad es. con icona
  standardizzata o link nel footer di ogni e-mail verso un'area dedicata all'esercizio
  dei diritti, dove chiedere di cessare solo la ricezione dei pixel continuando a
  ricevere le e-mail senza marcatori (par. 6, GU pag. 100).
- **Regime transitorio per trattamenti gia' in corso**: informativa con il primo invio
  utile + implementazione di un meccanismo di revoca anche granulare, con soluzioni di
  massima riconoscibilita', visibilita' e facilita' d'uso (par. 6, GU pag. 100).
- Chi rifiuta il tracciamento deve mantenere "la piena fruibilita' del servizio", senza
  alcuna limitazione (par. 6, GU pag. 100).
- **Registrazione delle scelte** dell'interessato da parte del titolare, ai fini di
  prova (cfr. art. 7, par. 1, GDPR) (par. 6, GU pag. 101).
- **Privacy by design e by default (art. 25 GDPR)**: il mittente generi "un
  identificativo inintelligibile e non sequenziale" associato all'indirizzo e-mail del
  destinatario, mantenendo la corrispondenza "in un layer interno e separato della
  piattaforma"; il conteggio delle aperture avviene tramite l'identificativo, senza che
  l'indirizzo e-mail transiti nella richiesta tecnica (par. 6, GU pag. 101).

## Dispositivo e termine di adeguamento (GU pag. 101)

- Linee guida adottate ai sensi dell'art. 154-bis, comma 1, lett. a), del Codice.
  Destinatari: fornitori di servizi della societa' dell'informazione, soggetti che
  offrono servizi on-line accessibili al pubblico, provider di posta elettronica,
  gestori di piattaforme per l'inoltro massivo di e-mail e "ogni altro soggetto che, a
  qualsiasi titolo, faccia uso di tracking pixel".
- Quattro ambiti del dispositivo: (i) informativa (artt. 12 ss. GDPR, par. 4);
  (ii) consenso (art. 122 Codice; artt. 4, punto 11, e 7 GDPR, par. 6); (iii) diritto di
  revoca anche granulare (art. 7, par. 3, GDPR, par. 6); (iv) privacy by design e by
  default (art. 25 GDPR, par. 6).
- **Termine di adeguamento: sei mesi dalla pubblicazione nella Gazzetta Ufficiale**.
  Essendo il provvedimento pubblicato nella GU n. 98 del 29 aprile 2026, il termine
  scade il **29 ottobre 2026**.

## Nota di perimetro (rilevante per questa skill)

Il provvedimento NON menziona il Registro delle attivita' di trattamento (art. 30 GDPR)
ne' la DPIA (art. 35 GDPR): disciplina informativa, presupposti giuridici/consenso,
revoca e privacy by design per l'uso dei tracking pixel. Le ricadute su Registro e
DPIA trattate in `tasks/tracking-pixel-email.md` derivano dall'applicazione delle fonti
generali gia' catalogate nella skill (art. 30 GDPR; art. 35 GDPR; WP248 rev. 01;
Allegato 1 Provv. Garante 467/2018) ai fatti descritti in queste Linee guida (categorie
di dati raccolti, univocita' dei tracciatori, finalita' di monitoraggio e profilazione).
