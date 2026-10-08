---
name: reg-gap-analysis-zekaisuni
title: /reg-gap-analysis
description: Yeni veya değişen KVKK, Kurul kararı, Resmi Gazete düzenlemesi, rehber, ilke kararı, sektör düzenlemesi veya mahkeme/regülatör gelişmesini mevcut privacy programı ile karşılaştırır. Aydınlatma, açık rıza, VERBIS/envanter, yurt dışına aktarım, veri işleyen, ihlal, çerez/İYS, saklama-imha ve sektör kontrolleri için gap listesi ve aksiyon planı üretir.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/privacy-legal/skills/reg-gap-analysis
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: tr
practice: data-protection
language: tr
---

# /reg-gap-analysis

## Amaç

Bu skill, yeni bir Türkiye veri koruma gelişmesini mevcut uygulama ile karşılaştırır. Varsayılan çalışma alanı KVKK/Kurul/Resmi Gazete ve Türkiye sektör regülasyonlarıdır. Yabancı privacy rejimleri yalnızca profilin `## Kurum Profili` bölümündeki regülatör ayak izi gerçekten kapsamda gösteriyorsa ikincil analiz olur.

## Başlamadan

1. `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` dosyasını oku.
2. Şu bölümleri yükle: `## KVKK Çekirdek Kontrolleri`, `## Yurt Dışına Aktarım`, `## Aydınlatma / Politika Taahhütleri`, `## İlgili Kişi Başvurusu`, `## Veri İhlali`, `## Çıktı Kuralları`.
3. `references/currency-watch.md` içindeki güncellik başlıklarını kontrol et.
4. Düzenleme kaynağı kullanıcı tarafından verilmemişse birincil kaynağı iste veya resmi kaynağa göre doğrulanması gerektiğini belirt.

## Kapsam Soruları

- Düzenleme kimlere uygulanıyor?
- Şirket/müvekkil bu kapsama giriyor mu?
- Yürürlük tarihi, geçiş süresi veya bildirim son tarihi var mı?
- Mevcut politika, envanter, VERBIS, DPA, VKED veya teknik süreç hangi kısmı karşılıyor?
- Değişiklik sadece metin güncellemesi mi, yoksa ürün/teknik süreç/tedarikçi sözleşmesi değişikliği mi gerektiriyor?

Kapsam dışı ise kısa bir "uygulanmaz" notu yaz; yine de nedenini belgele.

## Gereklilikleri Çıkar

Her gerekliliği ayrı satıra ayır:

| # | Gereklilik | Kaynak | Kategori | Tarih |
|---|---|---|---|---|
| 1 | [gereklilik] | [KVKK/Kurul/Resmi Gazete/link] | [kategori] | [yürürlük/son tarih] |

Kategoriler:

- aydınlatma ve açık rıza,
- işleme şartı,
- özel nitelikli veri,
- yurt dışına aktarım,
- veri işleyen/alt işleyen,
- veri ihlali bildirimi,
- ilgili kişi başvurusu,
- VERBIS/envanter,
- saklama-imha,
- çerez/elektronik ileti/İYS,
- güvenlik tedbirleri,
- sektör düzenleyici etkisi,
- AI/profil çıkarma/otomatik karar.

## Mevcut Durumla Karşılaştır

```markdown
### Gereklilik [N]: [kısa başlık]

**Kaynak:** [resmi kaynak ve tarih]
**Yeni beklenti:** [özet]
**Bizdeki mevcut durum:** [profil/politika/envanter/DPA/VKED ne diyor]
**Gap:** yok / kısmi / tam / bilinmiyor
**Eksik:** [somut eksik]
**Kapatma tipi:** politika | sözleşme | teknik ürün | süreç | kayıt/envanter | eğitim | dış danışman
**Risk:** düşük / orta / yüksek
```

## Önceliklendirme

Önce şunları öne al:

- açık son tarih veya yürürlük tarihi olanlar,
- Kurul bildirimi veya resmi bildirim gerektirenler,
- yurt dışına aktarım veya özel nitelikli veri etkileyenler,
- ihlal/şikayet/idari para cezası riskini artıranlar,
- canlı ürün veya çalışan/müşteri operasyonunu durdurabilecek eksikler.

## Çıktı

```markdown
GİZLİ HUKUKİ / KVKK ÇALIŞMA TASLAĞI - HUKUKÇU İNCELEMESİNE TABİDİR

Reviewer note
- Kaynaklar:
- Okuma kapsamı:
- Doğrulanması gerekenler:
- Aksiyon öncesi:

# KVKK / Regülasyon Gap Analizi - [Gelişme]

**Kaynak:** [resmi kaynak/link]
**Tarih:** [yayım/yürürlük]
**Şirkete etkisi:** uygulanır / uygulanmaz / belirsiz

## Kısa Sonuç

[2-4 cümle]

## Gap Listesi

| Öncelik | Gereklilik | Mevcut durum | Gap | Aksiyon | Sahip | Son tarih |
|---|---|---|---|---|---|---|
| yüksek/orta/düşük | | | | | | |

## Zaten Uyumlu Alanlar

- [madde]

## Açık Hukuki Sorular

- [soru ve doğrulanacak kaynak]

## Aksiyon Planı

- [ ] [aksiyon] - [sahip] - [tarih]

## Sonraki Adımlar

- Politika/doküman güncelle
- DPA veya tedarikçi ekini güncelle
- VKED/use-case triage çalıştır
- Teknik/security backlog aç
- Dış hukuk görüşü al
```

## Kaynak Disiplini

- Birincil kaynak olarak KVKK/Kurum, Resmi Gazete, mevzuat.gov.tr ve ilgili düzenleyici kurum sayfasını kullan.
- Lexpera, Lextera, Kazancı ve kurum içi araştırma araçları ikincil doğrulama olarak etiketlenir.
- Model bilgisinden gelen madde numarası, tarih veya karar sayısı `doğrulanacak` olarak işaretlenir.
- Resmi kaynak bulunamıyorsa bunu açık yaz; görünmez şekilde model bilgisinden doldurma.

## Bu Skill Ne Yapmaz

- Düzenleyici değişiklikleri kendiliğinden takip etmez; kullanıcı bir gelişme veya metin verdiğinde çalışır.
- Belirsiz düzenlemeyi nihai hukuk görüşü gibi sunmaz.
- Aksiyonları uygulamaz; takip planı üretir.
