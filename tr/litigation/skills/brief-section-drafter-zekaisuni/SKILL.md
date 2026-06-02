---
name: brief-section-drafter-zekaisuni
title: /brief-section-drafter
description: Draft Turkish petition sections, such as maddi vakıalar, hukuki nedenler, deliller, usuli itirazlar, talep ve sonuç, or appeal sections, consistent with the matter theory, evidence record, and office style. Every factual assertion must be source-tied and every legal point marked for verification when needed.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/litigation-legal/skills/brief-section-drafter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: litigation
language: tr
---

# /brief-section-drafter

Türk yargı pratiğine uygun dilekçe bölümü taslaklar. Çıktı avukat incelemesine tabi taslaktır; dosyada bulunmayan vakıa veya doğrulanmamış içtihat kesin ifade edilmez.

## Instructions

1. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md`.
2. If matter workspace is active, load `matter.md`, theory, chronology, pleadings, and evidence references.
3. Identify the requested section.
4. Draft in the configured office style.
5. Attach drafting notes and verification flags.

## Section Types

- maddi vakıalar,
- usuli itirazlar,
- hukuki nedenler,
- deliller,
- açıklamalar,
- talep ve sonuç,
- ihtiyati tedbir / ihtiyati haciz talebi,
- cevap dilekçesi bölümü,
- istinaf / temyiz nedeni,
- bilirkişi raporuna itiraz,
- ara beyan.

## Evidence Fidelity

Every factual assertion must tie to a source:

```text
[Vakıa] (Kaynak: [belge adı], [tarih], [sayfa/madde])
```

If a fact is plausible but unsupported, mark:

> [doğrulanmalı - kaynak yok]

Do not create witness narratives in a witness's voice. For witness evidence, identify the expected topic and HMK witness framework, but do not fabricate testimony.

## Legal Authority

Use Turkish legal sources:

- HMK,
- TBK,
- TTK,
- İİK,
- İş Kanunu,
- KVKK,
- relevant special laws,
- Yargıtay / Danıştay / AYM decisions where verified.

If case law is not verified from a current source, mark `[içtihat doğrulanmalı]`.

## Weak Arguments

Do not hide weak points. Add a drafting note:

```markdown
## Taslak Notları
- [Riskli argüman]: [why weak / what evidence or authority is missing]
- [Doğrulama]: [what must be checked before filing]
```

## Output

```markdown
[AVUKAT ÇALIŞMA ÜRÜNÜ - TASLAK]

# [Bölüm Başlığı] - [Matter]

[Draft section text]

---

## Kaynak ve Doğrulama Notları
| Cümle / konu | Kaynak | Durum |
|---|---|---|
| [fact/legal point] | [source] | doğrulandı / doğrulanmalı |

## Zayıf Noktalar
[risks]
```

## Turkish Drafting Rules

- Use court format: `[Şehir] [Sıra No]. [Tür] Mahkemesi`.
- Use Turkish party labels: davacı, davalı, alacaklı, borçlu.
- Do not file or finalize.
- Do not overstate claims beyond evidence.
- Keep talep ve sonuç precise and tied to the theory.

## What this skill does not do

- It does not draft a full pleading unless the user asks for all sections.
- It does not invent facts, citations, or witness testimony.
- It does not file through UYAP.
- It does not replace attorney judgment.
