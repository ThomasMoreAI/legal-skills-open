---
name: dpa-review-zekaisuni
title: /dpa-review
description: Veri işleme sözleşmesi, veri işleyen sözleşmesi, DPA veya kişisel veri aktarımı içeren tedarikçi/müşteri ekini Türk KVKK uygulamasına göre inceler. Veri sorumlusu/veri işleyen rolünü, KVKK m.12 güvenlik yükümlülüklerini, alt işleyen, silme-iade, denetim, ihlal bildirimi, yurt dışına aktarım, standart sözleşme ve politika uyumunu kontrol eder. Kullanıcı "DPA incele", "veri işleyen sözleşmesi", "müşteri DPA gönderdi", "tedarikçi ekini kontrol et" dediğinde veya sözleşme metni eklediğinde kullanılır.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/privacy-legal/skills/dpa-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: data-protection
language: tr
---

# /dpa-review

## Başlamadan

1. `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` dosyasını oku.
2. `## Veri İşleyen / DPA Playbook`, `## Yurt Dışına Aktarım`, `## Aydınlatma / Politika Taahhütleri` ve `## Çıktı Kuralları` bölümlerini yükle.
3. Profil placeholder ağırlıklıysa önce `/privacy-legal:cold-start-interview` öner.
4. `references/currency-watch.md` dosyasını güncellik kontrol listesi olarak oku.
5. `## Matter Workspaces` açıksa aktif matter'ı yükle; kapalıysa practice-level çalış.

## Amaç

Bu skill, DPA'yı yabancı şablon olarak değil, Türkiye'de veri sorumlusu ve veri işleyen ilişkisini düzenleyen sözleşmesel kontrol dokümanı olarak inceler. DPA kısaltması kullanılabilir; çıktı dili "veri işleme sözleşmesi / veri işleyen eki" olmalıdır.

## Rolü Belirle

İlk karar şudur:

| Durum | İnceleme açısı |
|---|---|
| Biz veri sorumlusuyuz, tedarikçi verimizi işliyor | Koruyucu inceleme: talimat, güvenlik, alt işleyen, ihlal, silme-iade, denetim, aktarım |
| Biz veri işleyeniz, müşteri DPA gönderdi | Operasyonel savunma: uygulanabilir talimat, makul denetim, gerçekçi ihlal süresi, sorumluluk sınırı |
| Rol belirsiz veya karma | Önce faaliyet bazında veri sorumlusu/veri işleyen/ortak rol analizi yap; belirsizse hukuk incelemesine gönder |

Yanlış rol seçimi bütün önerileri tersine çevirir; belirsizlik varsa tek netleştirme sorusu sor.

## Önceki Çıktılar

Aynı tedarikçi, müşteri veya faaliyet için önceki çıktıları kontrol et:

- `use-case-triage` sonucu,
- `pia-generation` / VKED,
- önceki `dpa-review`,
- politika monitor bulgusu,
- ihlal veya Kurul/şikayet notu.

Önceki çıktının risk seviyesi tabandır. Kırmızı riskli bir faaliyet DPA incelemesinde açıklamasız yeşile düşürülemez.

## KVKK İnceleme Kapıları

Her sözleşmede şu kapıları kontrol et:

| Kapı | Kontrol |
|---|---|
| Rol ve taraflar | Veri sorumlusu, veri işleyen, alt işleyen ve alıcı rolleri fiili akışla uyumlu mu? |
| İşleme amacı ve talimat | İşleme yalnızca belgelenmiş amaç/talimatla sınırlı mı? |
| Veri kategorileri | Kişisel veri, özel nitelikli veri, çocuk/çalışan/sağlık/biyometri/konum verisi ayrımı var mı? |
| KVKK m.5/m.6 dayanağı | Veri sorumlusu tarafında işleme şartı ve açık rıza ihtiyacı belirlenmiş mi? |
| Aydınlatma | Aydınlatma metni ile DPA kapsamı ve VERBIS/envanter uyumlu mu? |
| Güvenlik | KVKK m.12 teknik/idari tedbirler, erişim, şifreleme, log, yetki, denetim ve olay müdahalesi yeterli mi? |
| Alt işleyen | Alt işleyen listesi, değişiklik bildirimi, itiraz mekanizması ve akış-aşağı yükümlülükleri var mı? |
| İhlal bildirimi | Veri işleyen, veri sorumlusuna gecikmeksizin ve Kurul 72 saat pratiğini destekleyecek hızda bildirim yapıyor mu? |
| Silme/iade/imha | Sözleşme bitiminde iade, silme, imha, yedek dönüş süresi ve tevsik düzenli mi? |
| Denetim | Bağımsız rapor, sertifika, audit hakkı, gizlilik ve maliyet dengesi makul mü? |
| Yurt dışına aktarım | KVKK m.9 mekanizması, standart sözleşme/taahhüt/yeterlilik/istisna, imza ve Kurum bildirimi süreci var mı? |
| Sorumluluk | Veri ihlali, idari para cezası, üçüncü kişi talepleri ve tazminat riskleri kabul edilebilir mi? |

## Türkiye'ye Özgü Özel Kontroller

- Açık rıza, aydınlatma metninden ayrı ve serbest iradeye uygun olmalıdır; battaniye rıza veya hizmet şartına gömülü rıza kırmızı bayraktır.
- Standart sözleşme kullanılacaksa Kurul metninin zorunlu yapısı, Türkçe metin, imza yetkisi ve imzadan itibaren beş iş günü içinde Kuruma bildirim kontrol edilir.
- Sektörel rejim varsa DPA tek başına yeterli sayılmaz: BDDK, SPK, TCMB, BTK, TİTCK, sağlık mevzuatı, kamu ihale/kamu bulutu veya e-ticaret/İYS gereklilikleri ayrıca işaretlenir.
- DPA, gizlilik politikası, aydınlatma, VERBIS/envanter, saklama-imha politikası ve teknik mimariyle çelişmemelidir.

## Redline Yaklaşımı

Küçük ve hedefli değişiklik öner:

- önce kelime/ibare,
- sonra cümle,
- en son tüm madde değişimi.

Karşı taraf metninin çalışan kısmını koru. Büyük madde değişimi gerekiyorsa "bu madde kapsamlı değişti; nedeni ..." diye açıklama yaz.

## Çıktı

```markdown
GİZLİ HUKUKİ / KVKK ÇALIŞMA TASLAĞI - HUKUKÇU İNCELEMESİNE TABİDİR

Reviewer note
- Kaynaklar:
- Okuma kapsamı:
- Doğrulanması gerekenler:
- Aksiyon öncesi:

# Veri İşleme Sözleşmesi İncelemesi - [Taraf]

**Rol:** [Biz veri sorumlusuyuz / Biz veri işleyeniz / karma]
**Belge:** [MSA eki / bağımsız DPA / sözleşme maddesi]
**Tarih:** [YYYY-MM-DD]

## Kısa Sonuç

[İmzalanabilir mi? Hangi koşullar değişmeli?]

**Bulgular:** [N] yeşil | [N] sarı | [N] turuncu | [N] kırmızı

## Kritik Bulgular

| Seviye | Madde | Sorun | Öneri |
|---|---|---|---|
| kırmızı/turuncu/sarı | [madde] | [gap] | [redline/aksiyon] |

## Kapı Bazlı İnceleme

| Kapı | Sözleşme ne diyor | Playbook / KVKK beklentisi | Gap | Önerilen redline |
|---|---|---|---|---|
| Rol | | | | |
| Güvenlik | | | | |
| İhlal | | | | |
| Aktarım | | | | |

## Politika ve Envanter Uyum Kontrolü

[Aydınlatma, gizlilik politikası, VERBIS/envanter, saklama-imha ve önceki VKED ile uyum.]

## Pazarlık Pozisyonu

- Kabul edilebilir:
- Pazarlık edilmeli:
- Hukuk onayı olmadan kabul edilmemeli:

## Sonraki Adımlar

- [ ] Redline hazırla
- [ ] Tedarikçi/müşteri ile netleştir
- [ ] VKED veya aktarım analizi başlat
- [ ] Hukuk/security onayı al
```

## İnsan Onayı Kapısı

DPA imzalamak veya imza talimatı vermek bağlayıcı hukuki işlemdir. Kullanıcı hukukçu değilse, imza öncesi şu özeti üret ve açık insan onayı olmadan ilerleme:

- taraflar ve rol,
- kişisel veri kategorileri,
- yurt dışına aktarım,
- kırmızı/turuncu bulgular,
- kabul edilen fallback pozisyonlar,
- hukukçuya sorulacak üç soru.

## Bu Skill Ne Yapmaz

- Sıfırdan DPA şablonu üretmez; mevcut metni inceler ve redline önerir.
- Kuruma standart sözleşme bildirimi veya VERBIS kaydı yapmaz.
- Teknik güvenlik kontrollerinin gerçekten uygulandığını kanıt olmadan varsaymaz.
