---
name: leave-tracker-zekaisuni
title: /leave-tracker
description: Açık izin, rapor ve devamsızlık kayıtlarını Türk iş hukuku uygulamasına göre izler. Yıllık izin, iş göremezlik raporu, analık/süt izni, ücretsiz izin, mazeret izni, askerlik, devamsızlık ihtarı ve dönüş/aksiyon tarihleri için karar uyarısı üretir.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/employment-legal/skills/leave-tracker
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: employment
language: tr
---

# /leave-tracker

## Başlamadan

1. Employment `CLAUDE.md` dosyasını oku.
2. `## İzin ve Devamsızlık`, `## SGK / İŞKUR / İSG / KVKK Kapıları`, `## Çıktı Kuralları` bölümlerini yükle.
3. `~/.claude/plugins/config/claude-for-legal/employment-legal/leave-register.yaml` dosyasını oku veya kullanıcıdan izin listesini iste.

## İzlenen Kayıtlar

- yıllık ücretli izin,
- rapor / geçici iş göremezlik,
- analık, süt izni, ebeveynlik ve ücretsiz izin,
- mazeret izni,
- askerlik veya kamu görevi,
- devamsızlık ihtarı,
- iş kazası/meslek hastalığı bağlantılı izin,
- sağlık/engellilik uyarlaması gerektiren dönüşler.

## Uyarı Seviyeleri

| Seviye | Anlam |
|---|---|
| IMMEDIATE | 3 iş günü içinde karar veya aksiyon |
| THIS WEEK | 7 gün içinde aksiyon |
| COMING UP | 30 gün içinde izlenmesi gereken dönüş/son tarih |
| CLEAN | Aksiyon yok, kayıt güncel |

## Çıktı

```markdown
GİZLİ HUKUKİ / İŞ HUKUKU ÇALIŞMA TASLAĞI - HUKUKÇU İNCELEMESİNE TABİDİR

# İzin / Rapor Takip Raporu - [hafta/tarih]

**Açık kayıt:** [N]
**Aksiyon gereken:** [N]

## IMMEDIATE
- [çalışan/anonim ID] - [izin türü] - [aksiyon]

## THIS WEEK
- [kayıt]

## COMING UP
- [kayıt]

## CLEAN
- [kısa liste]

## Eksik Veri
- [rapor bitiş tarihi, dönüş teyidi, SGK/İK kaydı vb.]
```

## Kayıt Formatı

```yaml
- employee_id: "[anonim ID]"
  leave_type: "annual_leave | medical_report | maternity | unpaid | excuse | military | absence"
  start_date: "YYYY-MM-DD"
  expected_return: "YYYY-MM-DD"
  actual_return: null
  status: "open | returned | escalated | closed"
  documents: []
  sgk_related: true
  sensitive_health_data: true
  notes: ""
```

## Bu Skill Ne Yapmaz

- İzin onayı vermez.
- SGK/İŞKUR bildirimi yapmaz.
- Sağlık verisini gereksiz ayrıntıyla saklamaz.
