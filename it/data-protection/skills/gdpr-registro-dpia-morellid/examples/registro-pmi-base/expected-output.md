# Output atteso - Registro art. 30 + verifica completezza

# Registro delle attivita' di trattamento

**Titolare**: Esempio Servizi Srl
**Sede**: Via dei Fittizi 12, 57100 Livorno
**P.IVA**: 01234567890
**Data**: 2026-04-25
**Versione**: v1.0 (bozza per revisione DPO)

## Identificazione titolare

| Campo | Valore |
|-------|--------|
| Denominazione | Esempio Servizi Srl |
| Sede legale | Via dei Fittizi 12, 57100 Livorno |
| P.IVA | 01234567890 |
| Email | privacy@esempio.it |
| Legale rappresentante | (da inserire) |
| DPO | dott. Mario Esempio - dpo@esempio.it (designazione facoltativa) |

## Schede trattamenti

### T1 - Gestione del personale dipendente

| Voce | Contenuto |
|------|-----------|
| Finalita' | Gestione del rapporto di lavoro subordinato (assunzione, retribuzione, contributi, sorveglianza sanitaria, formazione) |
| Base giuridica art. 6 | art. 6.1.b) contratto + 6.1.c) obblighi legali |
| Base giuridica art. 9 | art. 9.2.b) obblighi del diritto del lavoro (per dati sanitari medicina del lavoro) |
| Categorie interessati | Dipendenti (50), ex-dipendenti, candidati selezionati |
| Categorie dati | Anagrafici, contatto, fiscali, contributivi, retributivi, sanitari (medicina del lavoro), curricula |
| Destinatari interni | HR, IT, direzione |
| Destinatari esterni | Studio del Lavoro Pinco, Inaz Srl (payroll), medico competente, INPS, Agenzia Entrate |
| Trasferimenti extra-UE | Nessuno |
| Conservazione | Anagrafici 10 anni post cessazione (art. 2220 c.c.); buste paga 5 anni (DPR 600/73); sanitari 30 anni presso medico competente; curricula non assunti 12 mesi |
| Misure sicurezza | Tecniche: HDD AES-256, MFA accesso area HR, log accessi 24 mesi. Organizzative: NDA dipendenti HR, formazione GDPR annuale, policy need-to-know |
| DPIA | NON RICHIESTA - non rientra in tipologie Garante; criteri WP248 soddisfatti: 7 (vulnerabili - dipendenti) ma da solo non sufficiente |

### T2 - Gestione clienti B2B (CRM)

| Voce | Contenuto |
|------|-----------|
| Finalita' | Gestione anagrafica clienti, esecuzione contratti, fatturazione, supporto |
| Base giuridica art. 6 | art. 6.1.b) contratto + 6.1.c) obblighi fiscali |
| Categorie interessati | Referenti aziendali clienti (~600) |
| Categorie dati | Nome, ruolo, email lavoro, telefono lavoro, dati fatturazione |
| Destinatari interni | Commerciale, supporto, amministrazione |
| Destinatari esterni | Salesforce (responsabile, provider EU) |
| Trasferimenti extra-UE | Backup Salesforce -> USA. Base: SCC (Decisione 2021/914 UE) + DPF se applicabile + TIA documentato |
| Conservazione | 10 anni post chiusura contratto (Cod. Civ. + obblighi fiscali) |
| Misure sicurezza | Salesforce SOC 2, accesso role-based, log audit, MFA |
| DPIA | NON RICHIESTA - dati professionali, non profilazione, no decisioni automatizzate |

### T3 - Gestione fornitori

| Voce | Contenuto |
|------|-----------|
| Finalita' | Gestione contratti, ordini, pagamenti fornitori |
| Base giuridica art. 6 | art. 6.1.b) + 6.1.c) |
| Categorie interessati | Referenti aziendali fornitori (~150) |
| Categorie dati | Nome, ruolo, email, dati fatturazione |
| Destinatari interni | Amministrazione |
| Destinatari esterni | ERP esterno (provider IT - responsabile) |
| Trasferimenti | Nessuno |
| Conservazione | 10 anni |
| Misure sicurezza | ERP cifrato, MFA amministrazione |
| DPIA | NON RICHIESTA |

### T4 - Newsletter marketing B2B

| Voce | Contenuto |
|------|-----------|
| Finalita' | Invio comunicazioni commerciali B2B (newsletter mensile, eventi, prodotti) |
| Base giuridica art. 6 | art. 6.1.a) consenso per nuovi contatti; soft opt-in art. 130 D.Lgs. 196/2003 per clienti esistenti |
| Categorie interessati | Referenti aziendali (clienti + lead consenzienti) ~1500 |
| Categorie dati | Nome, email lavoro, azienda |
| Destinatari interni | Marketing |
| Destinatari esterni | MailChimp (responsabile, EU residency) |
| Trasferimenti extra-UE | Backup MailChimp -> USA. Base: SCC |
| Conservazione | Fino a revoca consenso (unsubscribe link); pulizia annuale lead inattivi > 24 mesi |
| Misure sicurezza | MailChimp ISO 27001; accesso marketing manager via MFA |
| DPIA | NON RICHIESTA - finalita' marketing standard, non profilazione automatizzata |

### T5 - Videosorveglianza sede

| Voce | Contenuto |
|------|-----------|
| Finalita' | Sicurezza beni e persone, prevenzione furti |
| Base giuridica art. 6 | art. 6.1.f) legittimo interesse - LIA documentato |
| Categorie interessati | Dipendenti, visitatori, clienti (~100 visite/mese) |
| Categorie dati | Immagini video aree comuni |
| Destinatari interni | Direzione (solo in caso di evento) |
| Destinatari esterni | Forze dell'ordine su richiesta legale |
| Trasferimenti | Nessuno |
| Conservazione | 7 giorni rolling (cancellazione automatica) |
| Misure sicurezza | NVR cifrato, accesso credenziali su rete separata, log accessi. Avvisi conformi Provv. Garante 08/04/2010 |
| **DPIA** | **DA VALUTARE** - tipologia Garante 5 (controllo dipendenti via tecnologia) potrebbe applicarsi se la sorveglianza copre aree di lavoro. Se solo perimetro/aree comuni e non posti di lavoro, non rientra. |

### T6 - Sito web + cookie analytics

| Voce | Contenuto |
|------|-----------|
| Finalita' | Funzionamento sito + statistiche aggregate uso |
| Base giuridica | Cookie tecnici: nessun consenso (art. 122 Cod. Privacy); analytics anonimizzato: nessun consenso necessario |
| Categorie interessati | Visitatori sito (~5000/mese) |
| Categorie dati | IP anonimizzato (ultimi 2 byte azzerati), pagine visitate, durata sessione |
| Destinatari | Marketing interno (aggregati) |
| Trasferimenti | Nessuno (Matomo on-prem Milano) |
| Conservazione | Log analytics 13 mesi, IP anonimizzati immediatamente |
| Misure sicurezza | Matomo dietro VPN, SSO + MFA |
| DPIA | NON RICHIESTA - dati anonimizzati immediatamente |

## Verifica completezza (post-stesura, da check-registro-trattamenti.md)

### Esito sintetico

**CONFORME CON NOTE MINORI**

Trattamenti completi: 5/6
Trattamenti con voci da approfondire: 1/6 (T5 - DPIA da chiudere)

### Note di verifica

| # | Trattamento | Voce | Note | Priorita' |
|---|-------------|------|------|-----------|
| 1 | T1 | a) | Inserire nominativo legale rappresentante (richiesto dal Garante per identificazione) | Bassa |
| 2 | T2 | e) | Specificare versione esatta delle SCC (Decisione 2021/914 UE) e modalita' DPF (decisione adeguatezza UE-USA) | Media |
| 3 | T5 | DPIA | Decidere su DPIA: chiarire se sistema riprende posti di lavoro. Se SI -> tipologia 5 Garante -> DPIA obbligatoria. Se solo aree comuni di sicurezza -> non rientra | **Alta** |
| 4 | T1 | g) | Aggiungere descrizione dei backup e procedura disaster recovery | Bassa |

### Verifica trigger DPIA

| Trattamento | Tipologia Garante | Criteri WP248 | Esito |
|-------------|-------------------|---------------|-------|
| T1 personale | Nessuna esplicita | 7 (vulnerabili) | Non richiesta |
| T2 clienti | Nessuna | 0 | Non richiesta |
| T3 fornitori | Nessuna | 0 | Non richiesta |
| T4 newsletter | Nessuna | 0 | Non richiesta |
| T5 videosorveglianza | **5 (controllo dipendenti) - SE riprende posti lavoro** | 3 (monitoraggio sistematico) + 7 (vulnerabili dipendenti) | **DA VALUTARE** |
| T6 analytics | Nessuna | 0 (dati anonimizzati) | Non richiesta |

## Raccomandazioni

1. **T5**: chiarire l'ambito della videosorveglianza (perimetrale vs posti di lavoro) e procedere con DPIA se rientra in tipologia 5 Garante.
2. **T2**: documentare puntualmente le SCC e il TIA per il trasferimento Salesforce->USA.
3. Avviare ciclo annuale di review del Registro (calendario maggio).
4. Considerare nomina formale del legale rappresentante nel Registro.

## Avvertenze

- Il presente Registro e' bozza redatta con strumento di supporto. **Va revisionato e validato dal DPO dott. Mario Esempio** prima dell'adozione formale.
- Aggiornare ogni volta che cambiano: trattamenti, categorie dati, destinatari, finalita', misure tecniche, fornitori (provider esteri).
- Tenere disponibile per richieste dell'autorita' di controllo (Garante).

Sanzioni connesse a violazione art. 30: **fino a 10M EUR o 2% del fatturato globale annuo** (art. 83 par. 4).
