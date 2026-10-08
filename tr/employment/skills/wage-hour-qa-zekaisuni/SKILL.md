---
name: wage-hour-qa-zekaisuni
title: /wage-hour-qa
description: 'Türk iş hukuku ücret ve çalışma süresi sorularını yanıtlar: asgari ücret, fazla çalışma, fazla sürelerle çalışma, hafta tatili, ulusal bayram ve genel tatil, gece/vardiya, denkleştirme, prim/bonus/komisyon, bordro, ücret kesintisi, uzaktan çalışma masrafı ve işçilik alacağı riski.'
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/employment-legal/skills/wage-hour-qa
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: employment
language: tr
---

# /wage-hour-qa

## Başlamadan

1. Employment `CLAUDE.md` dosyasını oku.
2. `## Ücret ve Çalışma Süresi`, `## Kaynak ve Güncellik`, `## Çıktı Kuralları` bölümlerini yükle.
3. `references/currency-watch.md` dosyasını kontrol et.
4. Soru tutar veya güncel eşik içeriyorsa resmi kaynakla doğrulanması gerektiğini işaretle.

## Girdi

Eksikse sor:

- Çalışan tipi ve lokasyon?
- Ücret türü ve bordro kalemleri?
- Haftalık/günlük çalışma düzeni?
- Fazla çalışma onayı var mı?
- Puantaj, bordro, giriş-çıkış ve yazılı kayıt var mı?
- Toplu iş sözleşmesi veya işyeri uygulaması var mı?

## Analiz Kapıları

| Konu | Kontrol |
|---|---|
| Asgari ücret | Brüt/net, SGK taban/tavan ve dönem doğrulaması |
| Fazla çalışma | 45 saat üstü, onay, ispat, ödeme/serbest zaman |
| Fazla sürelerle çalışma | 45 saat altı sözleşmesel haftalık süre üstü |
| Hafta tatili | Kesintisiz dinlenme ve ücret |
| UBGT | Ulusal bayram/genel tatil çalışma onayı ve ödeme |
| Gece/vardiya | Gece çalışması, postalar, sağlık/İSG etkisi |
| Bordro | İmzalı bordro, ihtirazi kayıt, banka ödemesi |
| Prim/bonus | Hak kazanma koşulu, objektiflik, fesihte ödeme |
| Ücret kesintisi | Yazılı dayanak, disiplin cezası, mahsup ve rıza |
| Uzaktan çalışma | Masraf, ekipman, çalışma süresi ve kayıt |

## Çıktı

```markdown
GİZLİ HUKUKİ / İŞ HUKUKU ÇALIŞMA TASLAĞI - HUKUKÇU İNCELEMESİNE TABİDİR

Reviewer note
- Kaynaklar:
- Okuma kapsamı:
- Doğrulanması gerekenler:
- Aksiyon öncesi:

# Ücret / Çalışma Süresi Yanıtı

**Soru:** [soru]
**Kısa yanıt:** [evet/hayır/belirsiz + neden]

## Analiz

| Kapı | Sonuç | Not |
|---|---|---|
| Çalışma süresi | | |
| Ücret/bordro | | |
| İspat/kayıt | | |
| Risk | | |

## Hesaplama Gerekirse

- Varsayımlar:
- Eksik veriler:
- Resmi kaynakla doğrulanacak tutarlar:

## Aksiyon

- [ ] Kayıt/bordro/puantaj iste
- [ ] Hukuk/bordro kontrolü
- [ ] Politika veya sözleşme güncellemesi
```

## Bu Skill Ne Yapmaz

- Bordro hesaplamasını nihai muhasebe çıktısı gibi onaylamaz.
- Güncel asgari ücret/kıdem tavanı/idari para cezasını resmi kaynak kontrolü olmadan kesinleştirmez.
