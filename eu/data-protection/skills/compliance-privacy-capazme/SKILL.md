---
name: compliance-privacy-capazme
title: Compliance Privacy GDPR
description: Assessment completo di compliance GDPR con analisi base giuridica, verifica DPIA, registro trattamenti, informativa privacy e DPA. Usa quando l'utente chiede compliance privacy, adeguamento GDPR, informativa privacy, registro trattamenti, DPIA, valutazione impatto, data breach o contratto con responsabile del trattamento.
author: capazme
author_url: https://github.com/capazme/mcp-legal-it/tree/main/plugin/skills/compliance-privacy
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: it
---

# Compliance Privacy GDPR

Assessment completo: base giuridica, DPIA, registro, informativa, DPA.

## Workflow

### 1. Analisi base giuridica

Chiama `legal-it:analisi_base_giuridica` con tipo_trattamento e contesto.
Identifica la base ex art. 6 GDPR. Se dati particolari (art. 9), attiva flag.

### 2. Verifica necessita DPIA

Chiama `legal-it:verifica_necessita_dpia` con i criteri applicabili.
Valuta: profilazione, dati sensibili, monitoraggio sistematico, larga scala, soggetti vulnerabili, nuove tecnologie, scoring, incrocio dataset.

Se >= 2 criteri soddisfatti (WP248): DPIA obbligatoria.

### 2b. DPIA (se necessaria)

Chiama `legal-it:genera_dpia` con rischi e misure di mitigazione.

### 3. Registro trattamenti

Chiama `legal-it:genera_registro_trattamenti` per scheda art. 30 GDPR.

### 4. Informativa privacy

Chiama `legal-it:genera_informativa_privacy` per informativa art. 13 GDPR.

Varianti disponibili:
- `legal-it:genera_informativa_cookie` (cookie policy)
- `legal-it:genera_informativa_dipendenti` (dipendenti)
- `legal-it:genera_informativa_videosorveglianza` (videosorveglianza)

### 5. DPA (se responsabili esterni)

Chiama `legal-it:genera_dpa` per contratto art. 28 GDPR.

## Output atteso

### Checklist compliance
- [ ] Base giuridica identificata e documentata
- [ ] DPIA eseguita (se necessaria)
- [ ] Registro trattamenti aggiornato
- [ ] Informativa privacy redatta
- [ ] DPA stipulati con responsabili
- [ ] Misure di sicurezza (art. 32)
- [ ] Procedura data breach (artt. 33-34)
