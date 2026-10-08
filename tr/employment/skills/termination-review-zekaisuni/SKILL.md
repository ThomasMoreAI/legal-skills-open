---
name: termination-review-zekaisuni
title: /termination-review
description: Türk iş hukuku kapsamında fesih, ikale, istifa, performans/discipline çıkışı, haklı nedenle derhal fesih, geçerli nedenle fesih, toplu işçi çıkarma ve işçilik alacakları riskini inceler. İş güvencesi, savunma, kıdem/ihbar, yıllık izin, SGK çıkış kodu, ibraname ve zorunlu arabuluculuk kapılarını uygular.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/employment-legal/skills/termination-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: employment
language: tr
---

# /termination-review

## Başlamadan

1. Employment `CLAUDE.md` dosyasını oku.
2. `## Fesih ve Arabuluculuk`, `## Ücret ve Çalışma Süresi`, `## İzin ve Devamsızlık`, `## SGK / İŞKUR / İSG / KVKK Kapıları`, `## Çıktı Kuralları` bölümlerini yükle.
3. Çalışan dosyası, sözleşme, bordro, izin, performans, savunma, ihtar, rapor, disiplin ve önceki şikayet kayıtlarını iste.

## Fesih Kapıları

| Kapı | Kontrol |
|---|---|
| Fesih türü | İstifa, ikale, işveren feshi, geçerli neden, haklı neden, toplu işçi çıkarma |
| İş güvencesi | Kıdem, çalışan sayısı, belirsiz süreli sözleşme, işveren vekili istisnası |
| Gerekçe | Somut, tutarlı, ispatlanabilir ve yazılı mı? |
| Savunma | Savunma alınması gereken halde usule uygun davet ve süre var mı? |
| Zamanlama | Şikayet, izin, rapor, hamilelik, sendika, iş kazası, KVKK başvurusu sonrası yakınlık var mı? |
| Alacaklar | Kıdem, ihbar, ücret, fazla çalışma, UBGT, hafta tatili, yıllık izin, prim, masraf |
| SGK kodu | Fesih gerekçesiyle uyumlu, risk yaratmayan çıkış kodu seçildi mi? |
| İbraname/ikale | TBK ve Yargıtay uygulaması bakımından geçerlilik koşulları kontrol edildi mi? |
| Arabuluculuk | İşe iade veya işçilik alacağı uyuşmazlığı için zorunlu arabuluculuk riski işaretlendi mi? |

## Kırmızı Bayraklar

- Hamilelik, doğum, rapor, sağlık, engellilik, sendika, şikayet, mobbing/taciz bildirimi veya iş kazası sonrası fesih.
- Savunma alınmadan davranış/performans feshi.
- İspatsız devamsızlık veya usulsüz ihtar.
- SGK çıkış kodu ile fesih metni çelişiyor.
- İkale için makul ek menfaat yok.
- Toplu işçi çıkarma eşiği olabilecek yeniden yapılanma.
- Haklı fesihte öğrenme tarihi ve süre kontrolü yapılmamış.

## Çıktı

```markdown
GİZLİ HUKUKİ / İŞ HUKUKU ÇALIŞMA TASLAĞI - HUKUKÇU İNCELEMESİNE TABİDİR

Reviewer note
- Kaynaklar:
- Okuma kapsamı:
- Doğrulanması gerekenler:
- Aksiyon öncesi:

# Fesih İncelemesi - [Çalışan/Rol]

**Fesih türü:** [geçerli/haklı/ikale/istifa/toplu]
**İş güvencesi:** kapsamda / kapsam dışı / belirsiz
**Risk:** yeşil / sarı / turuncu / kırmızı

## Kısa Sonuç

[Fesih bugün ilerleyebilir mi? Önce hangi eksikler kapanmalı?]

## Risk Bulguları

| Seviye | Konu | Bulgular | Aksiyon |
|---|---|---|---|
| kırmızı/turuncu/sarı | | | |

## Alacak ve Belge Checklist

- [ ] Kıdem tazminatı
- [ ] İhbar tazminatı veya ihbar süresi
- [ ] Ücret/prim/masraf
- [ ] Kullanılmayan yıllık izin
- [ ] Fazla çalışma/UBGT/hafta tatili
- [ ] SGK çıkış kodu
- [ ] Fesih bildirimi
- [ ] İbraname/ikale taslağı

## Arabuluculuk / Dava Öngörüsü

[İşe iade, işçilik alacağı, ayrımcılık, sendikal tazminat, mobbing, kötü niyet vb.]

## Sonraki Adımlar

- [ ] Eksik belgeyi tamamla
- [ ] Savunma / ihtar sürecini işlet
- [ ] Hesaplamayı doğrula
- [ ] Hukuk onayı al
```

## İnsan Onayı Kapısı

Fesih, SGK kodu, ikale veya ibraname gönderimi bağlayıcı ve yüksek riskli işlemdir. Non-lawyer kullanıcıda nihai işlem talimatı verme; hukukçuya götürülecek bir sayfalık karar notu üret.

## Bu Skill Ne Yapmaz

- Fesih bildirimini göndermez.
- SGK çıkış bildirimi yapmaz.
- Arabuluculuk/dava stratejisini nihai karara bağlamaz.
