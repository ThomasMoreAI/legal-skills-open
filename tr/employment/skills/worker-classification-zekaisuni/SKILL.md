---
name: worker-classification-zekaisuni
title: /worker-classification
description: Çalışma ilişkisinin işçi, bağımsız çalışan/freelancer, danışman, stajyer, alt işveren işçisi, geçici iş ilişkisi veya hizmet alımı olarak sınıflandırılmasını Türk iş hukuku, SGK ve vergi/operasyon riski açısından inceler.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/employment-legal/skills/worker-classification
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: employment
language: tr
---

# /worker-classification

## Başlamadan

1. Employment `CLAUDE.md` dosyasını oku.
2. `## Kurum ve İşyeri Profili`, `## İşe Alım ve Sözleşme Playbook`, `## SGK / İŞKUR / İSG / KVKK Kapıları`, `## Çıktı Kuralları` bölümlerini yükle.
3. Sözleşme, iş tanımı, fiili çalışma, ödeme, ekipman ve yönetim bilgilerini iste.

## Sınıflandırma Kapıları

| Kapı | İşçi göstergesi | Bağımsız ilişki göstergesi |
|---|---|---|
| Bağımlılık | İşveren emir/talimatı, hiyerarşi, mesai | Sonuç odaklı, kendi organizasyonu |
| İşin entegrasyonu | İşverenin ana işine gömülü | Ayrı hizmet/çıktı |
| Zaman ve yer | Belirli mesai/lokasyon | Kendi çalışma düzeni |
| Ekipman | İşveren ekipmanı/sistemi | Kendi ekipmanı |
| Ücret | Düzenli maaş benzeri ödeme | Fatura/proje bazlı bedel |
| Münhasırlık | Tek işveren, izin sistemi | Birden çok müşteri |
| Risk ve organizasyon | Ticari risk yok | Ticari risk ve kendi personeli |

## Özel Türkiye Riskleri

- Muvazaalı alt işverenlik.
- Geçici iş ilişkisi/özel istihdam bürosu dışı işçi temini.
- Freelancer'ın fiilen çalışan gibi yönetilmesi.
- Stajyer/çırak/aday mühendis gibi statülerin ücret ve SGK etkisi.
- Uzaktan veya platform çalışanında bağımlılık göstergeleri.
- Yabancı danışmanda çalışma izni ve Türkiye'de fiili çalışma.

## Çıktı

```markdown
GİZLİ HUKUKİ / İŞ HUKUKU ÇALIŞMA TASLAĞI - HUKUKÇU İNCELEMESİNE TABİDİR

Reviewer note
- Kaynaklar:
- Okuma kapsamı:
- Doğrulanması gerekenler:
- Aksiyon öncesi:

# Çalışan Sınıflandırma Analizi - [Kişi/Rol]

**Önerilen sınıflandırma:** işçi / bağımsız çalışan / alt işveren / geçici iş ilişkisi / belirsiz
**Risk:** yeşil / sarı / turuncu / kırmızı

## Faktör Analizi

| Faktör | Bulgular | Etki |
|---|---|---|
| Bağımlılık | | |
| Entegrasyon | | |
| Zaman/yer | | |
| Ücret/ekipman | | |
| SGK/vergi | | |

## Riskler

- İşçilik alacağı:
- SGK prim/idari para cezası:
- Alt işveren/muvazaa:
- KVKK/İSG:

## Önerilen Yol

- [sözleşme/işe alma/payroll/tedarikçi modeli/yerel danışman]
```

## Bu Skill Ne Yapmaz

- SGK veya vergi sınıflandırmasını kesin bağlamaz.
- Muvazaa veya hizmet tespiti riskini mahkeme yerine karara bağlamaz.
