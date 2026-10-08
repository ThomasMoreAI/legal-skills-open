---
name: customize-commercial-legal-zekaisuni
title: /customize
description: 'Guided customization of the commercial contracts practice profile. Adjust one setting at a time: Turkish-law playbook positions, risk posture, escalation contacts, NDA triage preferences, KVKK posture, renewal tracking, house style, or matter workspace behavior without re-running the whole cold-start interview.'
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/commercial-legal/skills/customize
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: commercial
language: tr
---

# /customize

Kullanıcı mevcut ticari hukuk profilinde tek bir ayarı değiştirmek istediğinde çalışır. Amaç, `CLAUDE.md` dosyasını elle düzenletmeden kontrollü, kaydedilebilir ve tutarlı bir güncelleme yapmaktır.

## What to do

1. **Read config.** Load:
   - `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`
   - `~/.claude/plugins/config/claude-for-legal/company-profile.md`

   If missing or placeholder-heavy:

   > Henüz kurulum yapılmamış. Önce `/commercial-legal:cold-start-interview` komutunu çalıştırın; `customize` mevcut profili ayarlamak içindir.

2. **Show customizable map.** List current values in groups:
   - Company / profile: name, industry, jurisdictions, practice setting.
   - Turkish law posture: governing law, courts, arbitration, KVKK, competition, mediation.
   - Risk posture: conservative / middle / aggressive.
   - People and approvals: escalation chain, signatories, thresholds in TL.
   - Playbook positions: liability caps, indemnity, cezai şart (TBK m.179-185), IP, data protection, termination, renewal, bakiye hükümler, residuals/hafızada kalan bilgi, damga vergisi, price escalation.
   - NDA triage: GREEN / YELLOW / RED positions.
   - Review preferences: redline style, depth, stakeholder summary.
   - House style: memo format, signature block, KEP/e-signature/CLM preferences.
   - Workflow: matter workspace, intake path, renewal watcher cadence.
   - Integrations: CLM, document storage, KEP, e-signature, UYAP if relevant.

3. **Ask one change.**

   > Hangi alanı güncellemek istersiniz? Bölüm adı seçebilir veya değişikliği kendi kelimelerinizle tarif edebilirsiniz.

4. **Make the change.** Show current value, ask for new value, explain downstream impact, ask for confirmation, then write.

5. **Shared profile changes.** If company identity, industry, jurisdictions, or practice setting changes, write to `company-profile.md` and warn that other plugins may be affected.

6. **Record the change.** Add or append a change log entry where the profile keeps history:

```yaml
profil_degisiklik_kaydi:
  tarih:
  degisen_alan:
  onceki_deger:
  yeni_deger:
  etkilenen_skilller:
  not:
```

## Turkish-Law Customization Notes

- `baro` or `baro_sicil_no` applies to lawyers/firms, not ordinary in-house company identity.
- Approval thresholds are TL unless the profile explicitly stores another currency with conversion practice.
- KVKK, yurt dışına aktarım, KEP, e-imza, arabuluculuk/6325, TTK m.18/3 notice methods, damga vergisi (DVK/488), TBK m.179-185 cezai şart posture, and Turkish court/tahkim preferences are first-class profile fields.
- Do not translate command names or config file paths unless the whole repo has been renamed.

## Guardrails

- Never delete a section. Set it to `[Not configured]` and explain behavior.
- Flag inconsistent changes, such as aggressive risk posture plus "every redline needs GC approval."
- Do not silently weaken guardrails: work-product header, mesleki sır warning, source verification, attorney-review gates, conflicts notes.
- One change at a time unless the user explicitly asks for a bundled profile overhaul.

## What this skill does not do

- It does not invent legal positions.
- It does not override attorney-required guardrails without explicit informed confirmation.
- It does not run the whole cold-start interview.
- It does not rename plugin commands or folders.
