# Output atteso - tracking pixel newsletter: scheda registro + soglia DPIA + checklist

## 1. Classificazione della finalita' (Passo 1)

Gli impieghi dichiarati NON rientrano nelle deroghe dell'art. 122 del Codice
(par. 5 Linee guida 284/2026):

- misurazione individuale delle aperture per campagna -> consenso preventivo (par. 6)
- sospensione invii in base all'interesse manifestato dal singolo -> consenso
  preventivo (par. 6: adattare frequenza/interrompere l'invio in base all'interesse)
- segmentazione per interesse incrociando aperture e storico acquisti -> consenso
  preventivo (par. 6: profili commerciali dai dati di lettura)

La deroga statistica (par. 5, caso 1) NON e' applicabile: il pixel e' univoco per
destinatario e IP/dispositivo non sono anonimizzati, quindi le misurazioni sono
personalizzate.

## 2. Scheda di Registro art. 30 (Passo 2)

| Voce | Contenuto |
|------|-----------|
| Nome interno | Tracciamento aperture newsletter tramite tracking pixel |
| Finalita' | Misurazione individuale delle aperture; ottimizzazione campagne; sospensione invii per disinteresse; segmentazione/profilazione per interesse (incrocio con storico acquisti CRM) |
| Base giuridica art. 6 | art. 6.1.a) consenso (richiesto ex art. 122 Codice, par. 5-6 Linee guida). ATTENZIONE: il consenso marketing raccolto prima del 2026 non menzionava il tracciamento - vedi checklist |
| Categorie interessati | Iscritti alla newsletter (~45.000) |
| Categorie dati | Evento apertura e-mail (anche aperture ripetute), indirizzo IP, tipo dispositivo, orario/tempo di consultazione, numero aperture, identificativo pixel univoco per destinatario, message ID/delivery ID; dato derivato: segmento di interesse |
| Destinatari | Piattaforma e-mail marketing SaaS (responsabile art. 28 - verificare contratto); marketing interno |
| Trasferimenti extra-UE | Fornitore UE dichiarato - verificare sub-responsabili e backup |
| Conservazione | Da definire e documentare (le Linee guida non fissano termini) |
| Misure sicurezza | GAP: identificativo pixel non verificato come inintelligibile/non sequenziale; corrispondenza pixel-indirizzo da confinare in layer separato della piattaforma (par. 6) |
| DPIA | VEDI SOTTO - esito: OBBLIGATORIA |

## 3. Soglia DPIA (Passo 3)

Tipologie Allegato 1 Provv. Garante 467/2018:

- **Tipologia 1** - SI: profilazione relativa a "preferenze o gli interessi personali
  ... il comportamento" su larga scala (45.000 interessati, attivita' continuativa
  settimanale, on-line).
- **Tipologia 3** - SI: monitoraggio sistematico con raccolta dati attraverso reti e
  trattamento di identificativi univoci rispetto alle abitudini d'uso per periodi
  prolungati (pixel univoco per destinatario, tracciamento continuativo).
- Tipologia 9 - DUBBIO: interconnessione dati di consumo (storico acquisti) con dati
  di comportamento e-mail; da approfondire.

Criteri WP248 rev. 01: n. 1 (valutazione/profilazione), n. 3 (monitoraggio
sistematico), n. 5 (larga scala), n. 6 (combinazione dataset: aperture + CRM) = 4
criteri.

**Esito: DPIA OBBLIGATORIA** (almeno 1 tipologia Allegato 1 attivata; in aggiunta 2+
criteri WP248). Procedere con `tasks/draft-dpia.md` prima di proseguire il trattamento
nella forma attuale. Consultazione del DPO/referente privacy obbligatoria in sede di
DPIA (art. 35 par. 2).

## 4. Checklist Linee guida 284/2026 (Passo 4) - adeguamento entro 29/10/2026

| # | Adempimento | Esito |
|---|-------------|-------|
| 1 | Informativa menziona i tracking pixel e le finalita' | **GAP** - l'informativa cita solo "marketing via e-mail" |
| 2 | Informativa multilivello/multichannel | **GAP** - da predisporre (sintesi nel form iscrizione + link a dettaglio) |
| 3 | Trattamento in corso: informativa con primo invio utile | **GAP** - inserire nel prossimo invio |
| 4 | Consenso preventivo per tracciamento individuale/profilazione | **GAP** - il consenso esistente non copre in modo consapevole il tracciamento; adeguare secondo il regime transitorio (par. 6) |
| 5 | Deroga statistica (pixel unico campagna + anonimizzazione) | N.A. - non invocabile nello scenario attuale |
| 6 | Consenso unico neutro e privo di forzature | **GAP** - da implementare per i nuovi iscritti |
| 7 | Revoca granulare (solo tracciamento, mantenendo la newsletter) | **GAP** - esiste solo "disiscriviti" (revoca totale); aggiungere link/area dedicata nel footer |
| 8 | Trattamenti in corso: revoca granulare resa nota, alta visibilita' | **GAP** - conseguente al punto 7 |
| 9 | Piena fruibilita' del servizio a chi rifiuta il tracciamento | **GAP** - garantire invio newsletter senza pixel ai revocanti |
| 10 | Registrazione delle scelte (art. 7 par. 1) | **GAP** - predisporre log consensi/revoche |
| 11 | Identificativo pixel inintelligibile e non sequenziale, layer separato | **DA VERIFICARE** con il fornitore della piattaforma |
| 12 | Ruoli definiti con il fornitore (art. 28) | **DA VERIFICARE** - contratto e configurazione di default del pixel |
| 13 | Registro aggiornato + DPIA | **GAP** - scheda sopra da adottare; DPIA obbligatoria da svolgere |

## Avvertenza

Bozza di supporto: la scheda di Registro, la valutazione di soglia e il piano di
adeguamento richiedono revisione del DPO o del consulente legale prima dell'adozione
formale. La riconducibilita' del caso concreto alle deroghe dell'art. 122 compete al
titolare.
