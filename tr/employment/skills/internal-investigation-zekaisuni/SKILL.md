---
name: internal-investigation-zekaisuni
title: /internal-investigation
description: Türk iş hukuku uygulamasına göre iç soruşturma playbook'u. Taciz, mobbing, ayrımcılık, disiplin, hırsızlık, çıkar çatışması, veri ihlali, İSG olayı, iş kazası veya çalışan şikayetinde dosya açma, delil/görüşme kaydı, KVKK minimizasyonu, savunma, haklı fesih süresi ve iç memo üretimi için kullanılır.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/employment-legal/skills/internal-investigation
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: employment
language: tr
---

# /internal-investigation

## Guardrails

- İddia ve kapsam yazılı tanımlanır.
- Sağlık, disiplin, kamera, e-posta ve özel nitelikli veri için KVKK minimizasyonu yapılır.
- Görüşme notları tarihli ve kaynaklı tutulur; kanaat ile olgu ayrılır.
- Haklı fesih ihtimali varsa öğrenme tarihi ve süre kontrolü kırmızı bayraktır.
- Disiplin/fesih öncesi savunma ve eşit işlem kontrol edilir.
- Dışa gidecek özet iç hukuk değerlendirmesinden ayrılır.

## Dosya Yapısı

```text
~/.claude/plugins/config/claude-for-legal/employment-legal/investigations/<slug>/
├── investigation.md
├── evidence-log.md
├── interview-notes.md
├── timeline.md
├── memo.md
└── summaries/
```

## Intake

- Şikayet/olay nedir?
- İlgili kişiler ve roller?
- Olay tarihi, öğrenme tarihi, bildirim kanalı?
- Deliller: e-posta, kamera, Slack/Teams, cihaz, tanık, bordro, rapor?
- Acil tedbir gerekir mi: uzaklaştırma, erişim kapatma, İSG, KVKK ihlali?
- Potansiyel yaptırım: uyarı, disiplin, fesih, eğitim, politika değişikliği?

## Memo Formatı

```markdown
GİZLİ HUKUKİ / İŞ HUKUKU ÇALIŞMA TASLAĞI - HUKUKÇU İNCELEMESİNE TABİDİR

# İç Soruşturma Notu - [Konu]

## Kapsam

## Kronoloji

| Tarih | Olay | Kaynak |
|---|---|---|

## Delil Özeti

| Delil | Ne gösteriyor | Sınır / güvenilirlik |
|---|---|---|

## Görüşme Özeti

| Kişi | Rol | Özet | Çelişki |
|---|---|---|---|

## İş Hukuku Değerlendirmesi

- Disiplin:
- Savunma:
- Fesih/haklı neden:
- Eşit işlem:
- KVKK:
- İSG/regülatör:

## Önerilen Aksiyon

- [aksiyon, sahip, tarih]
```

## Bu Skill Ne Yapmaz

- Çalışana yaptırım uygulamaz.
- Kolluk/savcılık/regülatör bildirimi yapmaz.
- Kamera/e-posta gibi kaynaklara yetkisiz erişim önermez.
