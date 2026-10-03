---
name: cold-start-interview-zekaisuni
title: 'Cold start interview'
description: Cold-start interview for the litigation plugin, adapted for Turkish law and practice. Builds the litigation CLAUDE.md profile by role, party posture, Turkish court system, deadlines, evidence, UYAP/UETS/KEP/e-signature, writing style, and risk calibration.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/litigation-legal/skills/cold-start-interview
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: litigation
language: en
---

# /cold-start-interview

Bu skill `litigation-legal` profilini Türk yargı sistemi ve Türk avukatlık pratiğine göre kurar. Var olan profil doluysa `--redo` olmadan üzerine yazmadan önce onay ister.

## Flags

- `--redo`: re-run and overwrite after confirmation.
- `--check-integrations`: only check integrations and report gaps.

## Instructions

1. Check `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md`.
2. If populated and no `--redo`, ask before overwriting.
3. Run role and party branching.
4. Capture Turkish litigation profile.
5. Write `CLAUDE.md` and summarize what was configured.

## Section 0 - User Identity and Role

Ask who is using the plugin:

- `hukuk-musaviri`: in-house litigation / disputes.
- `buro-avukati`: private practice / law firm.
- `serbest-avukat`: solo practitioner.
- `stajyer-yardimci`: works under lawyer supervision.
- `egitim-klinik`: law school or clinic context.

Then ask default party posture:

- davacı,
- davalı,
- alacaklı,
- borçlu,
- üçüncü kişi,
- şikayetçi / mağdur,
- şüpheli / sanık,
- portfolio / mixed.

## Branch: In-house Counsel

Capture:

- company and sector,
- litigation portfolio categories,
- outside counsel management,
- reserve / disclosure methodology,
- management or board reporting cadence,
- authority thresholds in TL,
- preferred summary format,
- UYAP/UETS/KEP/e-signature access model,
- settlement and escalation gates.

## Branch: Law Firm / Private Practice

Capture:

- office / lawyer identity,
- baro sicil no for responsible lawyer,
- practice areas,
- conflicts process status,
- vekaletname intake practice,
- matter workspace preference,
- document storage and confidentiality,
- drafting style,
- court and jurisdiction footprint,
- client reporting cadence.

## Branch: Solo Practitioner

Capture:

- workload and deadline tracking,
- retainer/fee agreement practice,
- AAÜT awareness,
- client communication rules,
- evidence intake,
- limitation / hak düşürücü süre tracking,
- filing and UYAP workflow.

## Turkish Litigation Setup

Record:

```yaml
yargi_yollari:
  - hukuk
  - ticaret
  - is
  - tuketici
  - idare
  - icra
  - ceza
  - tahkim
  - arabuluculuk
mahkemeler:
  format: "[Şehir] [Sıra No]. [Tür] Mahkemesi"
deadline_policy:
  teblig_tarihi_required: true
  son_gun_tatil_kontrolu: true
  kesin_deadline_without_source: false
```

## Core Turkish Guardrails

Configure standing instructions:

- Outputs are drafts for attorney review.
- No filing, service, or sending without explicit human approval.
- UYAP No is used only where there is an actual court/enforcement file.
- Arabuluculuk dava şartı is checked by dispute type.
- Cevap dilekçesi süresi: HMK m.127, tebliğden itibaren 2 hafta, extension may be requested.
- Deliller: belge ibrazı, delil tespiti, tanık, bilirkişi, keşif, yemin.
- Mesleki sır: Av. K. m.36.
- Conflicts: Av. K. m.38.
- Advertising/solicitation guardrails: Av. K. m.55.

## Integrations - Türkiye

Ask status:

- UYAP,
- UETS / e-tebligat,
- KEP,
- e-imza,
- Yargıtay/Danıştay/AYM decision sources,
- mevzuat source,
- document archive,
- calendar/deadline system.

If `--check-integrations`, report only:

```markdown
## Entegrasyon Kontrolü
| Kaynak | Durum | Not |
|---|---|---|
| UYAP | bağlı / yok / manuel | [note] |
```

## Output Profile Sections

Write `CLAUDE.md` with:

- Who's using this.
- Role and party posture.
- Turkish court and procedure defaults.
- Deadline policy.
- Matter workspaces.
- Confidentiality and conflicts.
- Evidence and document sources.
- Drafting style.
- Escalation and approval.
- Output formats.
- Integration status.

## What this skill does not do

- It does not provide legal advice for a specific matter.
- It does not run conflicts checks.
- It does not connect to UYAP/UETS by itself.
- It does not create filings or send documents.
