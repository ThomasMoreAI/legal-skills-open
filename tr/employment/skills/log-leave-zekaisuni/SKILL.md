---
name: log-leave-zekaisuni
title: /log-leave
description: Leave register'a yeni yıllık izin, rapor, analık, ücretsiz izin, mazeret izni, askerlik, devamsızlık veya iş kazası bağlantılı izin kaydı ekler. KVKK sağlık verisi minimizasyonu ve dönüş/aksiyon tarihi alanlarını zorunlu kontrol eder.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/employment-legal/skills/log-leave
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: employment
language: tr
---

# /log-leave

## Akış

1. Employment `CLAUDE.md` dosyasını oku.
2. İzin türünü, başlangıç tarihini, beklenen dönüş tarihini, belge durumunu ve SGK/İSG bağlantısını çıkar.
3. Sağlık verisi varsa teşhis ayrıntısını kaydetme; sadece rapor/uygunluk durumu ve tarihleri tut.
4. `leave-register.yaml` dosyasına eklemeden önce kullanıcıya kayıt özetini göster.

## Eksik Bilgi

- çalışan için anonim ID,
- izin/rapor türü,
- başlangıç ve beklenen dönüş,
- ücretli/ücretsiz statü,
- belge var mı,
- iş kazası/meslek hastalığı bağlantısı,
- aksiyon sahibi.

## Çıktı

````markdown
# İzin Kaydı Ekleme

**Çalışan:** [anonim ID]
**Tür:** [izin/rapor]
**Başlangıç:** [tarih]
**Beklenen dönüş:** [tarih]
**KVKK notu:** [sağlık verisi minimizasyonu]

## Kayıt

```yaml
- employee_id: "[anonim ID]"
  leave_type: "[type]"
  start_date: "YYYY-MM-DD"
  expected_return: "YYYY-MM-DD"
  status: "open"
  documents: []
  sgk_related: false
  sensitive_health_data: false
  notes: ""
```
````

## Bu Skill Ne Yapmaz

- Sağlık raporunun tıbbi içeriğini analiz etmez.
- İzin/fesih kararı vermez.
