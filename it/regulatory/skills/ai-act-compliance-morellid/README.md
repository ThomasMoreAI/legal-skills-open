# AI Act Compliance (Reg. UE 2024/1689)

> Versione: 0.2.0 (alpha)
> Stato: in sviluppo

Skill di supporto alla compliance al Regolamento UE 2024/1689 (AI Act) per fornitori, deployer e fornitori di modelli GPAI.

## Target

- **Fornitori (provider)** di sistemi di IA, in particolare quelli a rischio elevato (Allegato III) o componenti di sicurezza di prodotti (Allegato I)
- **Deployer** (utilizzatori) di sistemi di IA high-risk, in particolare organismi pubblici, fornitori di servizi pubblici, banche/assicurazioni
- **Fornitori di modelli GPAI** (general purpose AI)
- **DPO, consulenti privacy, ingegneri** che progettano o adottano sistemi AI

## Cosa fa

Sei sotto-attivita' distinte:

1. **Classifica sistema AI** (`classifica-sistema.md`) - vietato / high-risk / trasparenza / minimo / GPAI
2. **Check obblighi provider high-risk** (`check-high-risk-provider.md`) - art. 8-22 + conformity assessment
3. **Check obblighi deployer** (`check-deployer-obligations.md`) - art. 26-27 incluso FRIA
4. **Check obblighi GPAI provider** (`check-gpai-provider.md`) - art. 53-55
5. **Check obblighi trasparenza** (`check-trasparenza.md`) - art. 50
6. **Profili nazionali Italia** (`check-profili-nazionali-italia.md`) - D.Lgs. 160/2026: reato art. 437-bis c.p., 231 art. 25-vicies, prova e nesso causale nelle azioni di risarcimento, assicurazione, Forze di polizia

Vedi [SKILL.md](SKILL.md) per il dettaglio.

## Fonti consultate

- Reg. UE 2024/1689 (AI Act) - testo italiano OJ 12/07/2024
- D.Lgs. 9 settembre 2026, n. 160 - GU Serie Generale n. 214 del 15/09/2026 - hash SHA256 registrato

Vedi [references/sources.yaml](references/sources.yaml).

## Sinergie

Per uso integrato:
- **GDPR**: skill `gdpr-registro-dpia` per Registro art. 30, DPIA art. 35, FRIA integrato
- (futuro) NIS2 per cybersicurezza enterprise

## Limiti noti

- **Alpha**: non validata da consulente legale specializzato
- Linee guida Commissione (es. su classificazione art. 6) sono in via di pubblicazione
- Norme armonizzate ETSI/CEN-CENELEC in sviluppo
- Code of Practice GPAI in via di adozione
- Non sostituisce conformity assessment di organismo notificato
- D.Lgs. 160/2026: data di entrata in vigore non fissata dal testo; decreti attuativi del Titolo I e L. 132/2025 non catalogati

Vedi [SKILL.md](SKILL.md) sezione "Limiti".

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).

## Disclaimer

Strumento di supporto. **Ogni output richiede revisione di consulente legale specializzato in diritto digitale UE prima di decisioni di immissione sul mercato o di compliance.** Sanzioni AI Act fino a 35M EUR o 7% del fatturato globale annuo (pratiche vietate art. 5).
