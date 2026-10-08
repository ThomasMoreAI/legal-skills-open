---
name: ai-act-compliance-morellid
title: AI Act Compliance (Reg. UE 2024/1689)
description: Verifica la conformita' di un sistema di IA al Reg. UE 2024/1689 (AI Act). Classifica il sistema (vietato / alto rischio / rischio limitato / GPAI), identifica gli obblighi applicabili per fornitore e deployer, e guida la redazione dei documenti richiesti. Copre i profili nazionali italiani del D.Lgs. 160/2026 (reato art. 437-bis c.p., 231, prova e nesso causale nelle azioni di risarcimento, uso da parte delle Forze di polizia). Use when user asks to assess an AI system for EU AI Act compliance, identify applicable obligations, or classify a system under the regulation.
author: morellid
author_url: https://github.com/morellid/skill-per-ingegneri/tree/main/skills/ai-act-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: regulatory
language: it
tags: [ai-act, reg-ue-2024-1689, gpai]
sources:
- title: Ai Act Allegato Iii
  path: references/estratti/ai-act-allegato-iii.md
- title: Ai Act Art 26 27 Deployer Fria
  path: references/estratti/ai-act-art-26-27-deployer-fria.md
- title: Ai Act Art 5 Pratiche Vietate
  path: references/estratti/ai-act-art-5-pratiche-vietate.md
- title: Ai Act Art 50 Trasparenza
  path: references/estratti/ai-act-art-50-trasparenza.md
- title: Ai Act Art 51 55 Gpai
  path: references/estratti/ai-act-art-51-55-gpai.md
- title: Ai Act Art 6 9 Classificazione High Risk
  path: references/estratti/ai-act-art-6-9-classificazione-high-risk.md
- title: Dlgs 160 2026 Profili Nazionali
  path: references/estratti/dlgs-160-2026-profili-nazionali.md
- title: Ai Act It Eurlex
  path: references/fonti/ai-act-it-eurlex.md
- title: Dlgs 160 2026
  path: references/fonti/dlgs-160-2026.md
---

# AI Act Compliance (Reg. UE 2024/1689)

## Quando usare questa skill

Usa questa skill quando un ingegnere o un team tecnico deve:
- Classificare un sistema di IA secondo il Reg. UE 2024/1689 (vietato / alto rischio Allegato III / rischio limitato / GPAI)
- Identificare gli obblighi applicabili come fornitore (provider) o deployer di un sistema di IA
- Verificare la conformita' agli obblighi di trasparenza (art. 50)
- Valutare se un modello rientra nella categoria GPAI con rischio sistemico (art. 51)
- Supportare la redazione della FRIA (Fundamental Rights Impact Assessment, art. 27)
- Valutare le conseguenze nazionali italiane (D.Lgs. 160/2026): reato art. 437-bis c.p., responsabilità dell'ente 231, azioni civili di risarcimento, uso dell'IA da parte delle Forze di polizia

Non e' adatta a:
- Sostituire consulenza legale per casi complessi o contenziosi
- Coprire la L. 132/2025, i decreti attuativi previsti dal D.Lgs. 160/2026 e le linee guida AgID: non ancora catalogati tra le fonti
- Certificazione o audit ufficiale

**Target**: ingegneri software, product manager, responsabili tecnici che sviluppano o mettono in servizio sistemi di IA nell'Unione europea.

## Avvertenza

Questa skill e' uno strumento di supporto tecnico alla verifica di conformita'. **Non sostituisce il giudizio del professionista legale.** Gli output sono orientativi e devono essere validati da un consulente legale prima di decisioni operative. La skill non produce documenti pronti al deposito o alla firma.

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il file task appropriato:

- **Classificazione sistema**: quando l'utente chiede di classificare un sistema di IA (vietato? alto rischio? rischio limitato?), leggere `tasks/classifica-sistema.md`
- **Obblighi fornitore alto rischio**: quando l'utente e' fornitore di un sistema ad alto rischio e chiede quali obblighi deve rispettare, leggere `tasks/check-high-risk-provider.md`
- **Obblighi deployer alto rischio**: quando l'utente deployer vuole verificare i propri obblighi (art. 26, 27), leggere `tasks/check-deployer-obligations.md`
- **Obblighi GPAI provider**: quando l'utente sviluppa o distribuisce un modello GPAI (es. LLM), leggere `tasks/check-gpai-provider.md`
- **Trasparenza (art. 50)**: quando l'utente vuole verificare gli obblighi di disclosure per chatbot, deep fake, emozioni, contenuti sintetici, leggere `tasks/check-trasparenza.md`
- **Profili nazionali Italia (D.Lgs. 160/2026)**: quando l'utente chiede delle conseguenze penali, 231 o civili in Italia (reato 437-bis c.p., risarcimento danni, prova, assicurazione) o fornisce o usa sistemi IA per le Forze di polizia, leggere `tasks/check-profili-nazionali-italia.md`

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita' desidera o proponi la classificazione come primo step.

## Processo generale

1. Identifica il ruolo dell'utente (fornitore / deployer / entrambi) e il tipo di sistema (IA system, GPAI model, sistema integrato)
2. Esegui prima la classificazione (`tasks/classifica-sistema.md`) se il sistema non e' gia' classificato
3. Carica il task file pertinente al ruolo e alla categoria del sistema
4. Richiedi gli input necessari come specificato nel task (descrizione del sistema, finalita' prevista, settore di utilizzo)
5. Applica la procedura descritta nel task
6. Produci l'output nel formato atteso
7. Indica sempre le date di applicazione pertinenti (le obbligazioni entrano in vigore in date diverse)
8. Includi sempre un rinvio alla verifica del professionista legale per i punti critici

## Date di applicazione (art. 113, come modificato da Digital Omnibus)

| Obblighi | Applicazione |
|----------|-------------|
| Pratiche vietate (art. 5), alfabetizzazione (art. 4) | 2 febbraio 2025 - **gia' in vigore** |
| GPAI (capo V), governance, sanzioni GPAI | 2 agosto 2025 - **gia' in vigore** |
| Obblighi di trasparenza art. 50 (chatbot, deepfake, emozioni, testo informativo) | 2 agosto 2026 |
| Watermarking art. 50 par. 2 (output sintetici machine-readable) | **2 dicembre 2026** (rinvio Omnibus) |
| Divieto sistemi generazione CSAM / deepfake sessuali non consensuali | **2 dicembre 2026** (nuovo Omnibus) |
| Alto rischio Allegato III, FRIA art. 27 | **2 dicembre 2027** (era 2 agosto 2026, rinvio Omnibus) |
| Alto rischio Allegato I (componenti sicurezza prodotti) | **2 agosto 2028** (era 2 agosto 2027, rinvio Omnibus) |

> **Nota Omnibus (accordo provvisorio 7 maggio 2026)**: l'accordo Parlamento-Consiglio sul Digital Omnibus che rinvia le scadenze sopra **non e' ancora stato pubblicato in GUUE**. Mancano endorsement formale, revisione legale-linguistica e pubblicazione. Le date sopra riflettono l'accordo politico ma vanno riconfermate alla pubblicazione finale. Per casi operativi prima di tale data: pianificare conservativamente sulla data piu' breve fra quella originale del Reg. 2024/1689 e quella Omnibus.

## Fonti normative

Riferimenti completi in `references/sources.yaml`. Trascrizioni fedeli delle fonti in `references/fonti/ai-act-it-eurlex.md` (Reg. 2024/1689) e `references/fonti/dlgs-160-2026.md` (D.Lgs. 9 settembre 2026, n. 160, GU n. 214 del 15/09/2026; il decreto non fissa la data di entrata in vigore, verificarla su Normattiva). Estratti tematici in `references/estratti/`.

## Limiti

Cosa questa skill NON fa:
- Non produce dichiarazioni di conformita' CE
- Non sostituisce valutazioni di conformita' da parte di organismi notificati
- Non copre la normativa settoriale di armonizzazione dell'Allegato I (dispositivi medici, macchine, ecc.)
- Non interpreta normativa ambigua senza rinvio al professionista legale
- Non tiene aggiornamento automatico per atti delegati della Commissione che modificano Allegato III o soglie art. 51
