# Esempio - input per draft Registro art. 30 (PMI servizi)

> Sintetico, fittizio. Test della skill su uno scenario PMI realistico italiano.

## Profilo organizzazione

- Ragione sociale: **Esempio Servizi Srl**
- Sede: Via dei Fittizi 12, 57100 Livorno
- P.IVA: 01234567890
- 50 dipendenti
- Settore: software gestionale per PMI
- Cliente target: aziende italiane (B2B), 200-300 clienti attivi

## DPO

Designato in via facoltativa: dott. Mario Esempio (consulente esterno), dpo@esempio.it.

## Trattamenti da censire (richiesta utente)

L'utente fornisce 6 trattamenti da inserire nel Registro:

### Trattamento 1 - Gestione del personale dipendente

- Finalita': gestione del rapporto di lavoro subordinato (assunzione, retribuzione, contributi, sorveglianza sanitaria, formazione)
- Base giuridica: contratto art. 6.1.b) + obblighi legali art. 6.1.c) + cat. particolari art. 9.2.b) per medicina del lavoro
- Interessati: dipendenti (50), ex-dipendenti (mantenuti per obblighi conservazione), candidati selezionati
- Categorie dati: anagrafici, contatto, fiscali, contributivi, retributivi, sanitari (medicina del lavoro), curricula
- Destinatari: HR interno, IT, direzione; consulente del lavoro Studio Pinco; payroll Inaz Srl; medico competente; INPS; Agenzia Entrate
- Trasferimenti extra-UE: nessuno (tutti provider in UE)
- Conservazione: anagrafici 10 anni post cessazione (art. 2220 c.c.), buste paga 5 anni, sanitari 30 anni (cartella sanitaria) presso medico competente, curricula non assunti 12 mesi
- Sicurezza: HDD cifrati AES-256, accesso ad area HR via MFA, log accessi 24 mesi, NDA dipendenti HR, formazione GDPR annuale

### Trattamento 2 - Gestione clienti B2B (CRM)

- Finalita': gestione anagrafica clienti, esecuzione contratti, fatturazione, supporto post-vendita
- Base giuridica: art. 6.1.b) contratto + 6.1.c) obblighi fiscali
- Interessati: referenti aziendali clienti (~600 persone fisiche)
- Categorie dati: nome, ruolo aziendale, email lavoro, telefono lavoro, dati fatturazione (riferiti a P.IVA cliente)
- Destinatari: ufficio commerciale, supporto, amministrazione; cloud Salesforce (provider EU)
- Trasferimenti extra-UE: dati su backup Salesforce eventualmente in USA -> SCC + Transfer Impact Assessment, decisione adeguatezza DPF se applicabile
- Conservazione: 10 anni post chiusura contratto (Cod. Civ. + obblighi fiscali)
- Sicurezza: Salesforce SOC 2, accesso role-based, log audit Salesforce, MFA

### Trattamento 3 - Gestione fornitori

- Finalita': gestione contratti, ordini, pagamenti fornitori
- Base giuridica: art. 6.1.b) + 6.1.c)
- Interessati: referenti aziendali fornitori (~150)
- Categorie dati: nome, ruolo, email, dati fatturazione
- Destinatari: amministrazione, ERP esterno (gestionale aziendale, provider IT)
- Trasferimenti: nessuno
- Conservazione: 10 anni
- Sicurezza: ERP cifrato, MFA per amministrazione

### Trattamento 4 - Newsletter marketing B2B

- Finalita': invio comunicazioni commerciali ai clienti consenzienti (newsletter mensile, eventi, prodotti)
- Base giuridica: consenso art. 6.1.a) per nuovi contatti, soft opt-in art. 130 D.Lgs. 196/2003 per clienti esistenti
- Interessati: referenti aziendali clienti + lead consenzienti (~1500 indirizzi)
- Categorie dati: nome, email lavoro, azienda
- Destinatari: marketing interno, MailChimp (provider EU - data residency in UE confermata)
- Trasferimenti: backup MailChimp -> USA, base giuridica SCC
- Conservazione: fino a revoca consenso (link unsubscribe in ogni email), pulizia annuale dei lead inattivi > 24 mesi
- Sicurezza: piattaforma MailChimp ISO 27001, accesso solo marketing manager via MFA

### Trattamento 5 - Videosorveglianza sede

- Finalita': sicurezza beni e persone, prevenzione furti
- Base giuridica: legittimo interesse art. 6.1.f) - bilanciamento eseguito (LIA)
- Interessati: dipendenti, visitatori, clienti in visita (~100/mese)
- Categorie dati: immagini video aree comuni
- Destinatari: solo direzione (in caso di evento), forze dell'ordine su richiesta legale
- Trasferimenti: nessuno
- Conservazione: 7 giorni rolling (cancellazione automatica)
- Sicurezza: NVR cifrato, accesso protetto da credenziali su sistema separato dalla rete office, log accessi
- **Nota**: avviso conformi Provv. Garante 8/4/2010 affissi all'ingresso

### Trattamento 6 - Sito web + cookie analytics

- Finalita': funzionamento sito istituzionale + statistiche aggregate uso (Matomo on-prem)
- Base giuridica: cookie tecnici senza consenso; analytics anonimizzati (no pseudonimizzazione necessaria)
- Interessati: visitatori sito (~5000/mese)
- Categorie dati: indirizzo IP anonimizzato (ultimi 2 byte azzerati), pagine visitate, durata sessione
- Destinatari: marketing interno (solo aggregati)
- Trasferimenti: nessuno (Matomo on-premise nel datacenter aziendale a Milano)
- Conservazione: log analytics 13 mesi, IP anonimizzati immediatamente
- Sicurezza: Matomo dietro VPN, accesso solo via SSO + MFA
