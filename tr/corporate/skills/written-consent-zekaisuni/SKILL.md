---
name: written-consent-zekaisuni
title: /written-consent
description: Türk şirketler hukuku için karar taslağı hazırlama skill'i. Komut adı geriye dönük uyumluluk için written-consent olarak kalır; içerikte yönetim kurulu, müdürler kurulu, genel kurul, komite veya toplantısız/sirküler karar taslağı hazırlanır. Karar konusu, organ, şirket türü, esas sözleşme, imza/temsil, tescil/ilan, MERSİS, KAP/MKK ve karar defteri kontrolleri için kullanılır.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/corporate-legal/skills/written-consent
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: tr
practice: corporate
language: tr
---

# /written-consent

## Türk uyarlama notu

Bu skill'in adı orijinal plugin uyumluluğu için `written-consent` olarak kalır. Türk hukukunda ABD'deki `unanimous written consent` kavramı birebir varsayılmaz. Skill'in işlevi, somut şirkete ve organa uygun **karar taslağı** üretmektir:

- A.Ş. yönetim kurulu kararı
- Ltd. müdürler kurulu / müdür kararı
- Genel kurul kararı veya tutanağı taslak bölümü
- Komite kararı
- Hukuken mümkünse toplantısız/sirküler karar taslağı

Toplantısız karar mekanizması, karar nisabı, imza şekli, tescil/ilan ve defter formaliteleri; TTK, esas sözleşme, şirket sözleşmesi, iç yönerge ve somut belgeye göre hukukçu tarafından doğrulanır.

## İş akışı

1. `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` dosyasını oku.
2. `## Kurumsal yönetim` ve `## Şirket profili` bölümlerinden şirket türü, organ yapısı, temsil yetkisi, karar formatı ve tescil sürecini al.
3. Karar konusunu sınıflandır: rutin / önemli işlem / hukukçu veya dış danışman incelemesi gereken işlem.
4. Uygun karar türünü seç: toplantı kararı, toplantısız/sirküler karar, genel kurul kararı, müdürler kurulu kararı veya komite kararı.
5. Örnek karar/tutanak varsa formatı ona göre uygula. Yoksa kullanıcıdan örnek iste veya açıkça genel taslak ürettiğini belirt.
6. Taslak + formalite kontrol listesi + imza/tescil takip listesi üret.

## Precedent yoksa dur

Kurumsal karar formatı şirketten şirkete değişir. Şu ikisi de yoksa:

- profilde çıkarılmış karar/tutanak formatı,
- bu oturumda paylaşılan önceki karar/tutanak örneği,

taslaklamadan önce kullanıcıya sor:

> Elimde bu şirketin karar/tutanak formatı yok. İsterseniz önce bir örnek kararı paylaşın; formatı ona göre çıkarayım. Ya da "genel taslakla başla" deyin, ben de formatın şirket içi ve noter/sicil uygulamasına göre hukukçu tarafından düzeltilmesi gerektiğini işaretleyerek taslak üreteyim.

Kullanıcı açıkça "genel taslakla başla" demedikçe sign-ready metin üretme.

## Büyük işlem + acil imza kapısı

Aşağıdaki konularda aynı gün imza, tescil, KAP bildirimi veya kapanış baskısı varsa dur ve hukukçu/dış danışman incelemesi iste:

- birleşme, bölünme, tür değiştirme,
- pay devri veya pay sahipliği yapısını değiştiren işlem,
- sermaye artırımı, azaltımı, yeni pay ihracı veya imtiyaz değişikliği,
- önemli malvarlığı devri,
- M&A kapanış kararı,
- halka açık şirkette özel durum, ilişkili taraf işlemi veya SPK/KAP hassasiyeti,
- Rekabet Kurumu izni veya kapanış koşulu olan işlem,
- tasfiye, sona erme, konkordato/iflas bağlantılı karar,
- yönetim kontrolünü veya temsil yetkisini değiştiren karar.

Çıktı:

```text
Büyük işlem + acil imza/tescil kapısı
Bu karar [işlem türü] ile ilgili ve aynı gün imza/tescil/bildirim baskısı var. Taslak hazırlayabilirim; ancak hazır-imza metni olarak işaretlemem. Esas sözleşme, TTK, temsil yetkisi, tescil/ilan ve varsa SPK/Rekabet/KVKK boyutu dış danışman veya sorumlu hukukçu tarafından kontrol edilmeli.
```

Kullanıcı "taslakla, hukukçu inceleyecek" derse taslak üret; "hazır gönder" şeklinde davranma.

## Intake

Karar taslağına başlamadan önce eksik olanları sor:

- Şirket türü: A.Ş., Ltd., şube veya başka yapı?
- Karar organı: yönetim kurulu, müdürler kurulu, genel kurul, komite?
- Karar toplantıda mı alınacak, toplantısız/sirküler karar mı isteniyor?
- Karar konusu tek cümleyle nedir?
- Dayanak belge var mı: sözleşme, işlem dokümanı, yönetim notu, KAP taslağı, sicil talebi?
- Esas sözleşme, şirket sözleşmesi veya iç yönerge özel nisap/temsil kuralı içeriyor mu?
- İmzalayacak kişiler ve temsil şekli nedir?
- Ticaret sicili tescil/ilan, MERSİS, KAP/MKK, noter veya karar defteri işlemi bekleniyor mu?
- Menfaat çatışması, ilişkili taraf, hakim şirket/bağlı şirket veya yönetici çıkarı var mı?

## Sınıflandırma

### Rutin karar adayları

- imza yetkilisi veya banka talimatı güncellemesi,
- rutin sözleşme onayı,
- iç yönergeye uygun yetkilendirme,
- şube/temsilci işlem talimatı,
- olağan genel kurul hazırlığı,
- pay defteri veya kayıt güncellemesi,
- ticaret sicili evrakı için yetki verilmesi,
- geçmiş işlem onayı veya uygulama yetkilendirmesi.

### İnceleme bayrağı gereken kararlar

- sermaye yapısını değiştiren işlem,
- pay devri kısıtları veya imtiyazlara temas eden karar,
- birleşme, bölünme, tür değiştirme, tasfiye,
- önemli varlık devri veya önemli borçlanma,
- ilişkili taraf işlemi,
- rekabet, KVKK, SPK/KAP/MKK veya sektörel izin etkisi olan işlem,
- yönetim kontrolü, temsil yetkisi veya şirket organlarını değiştiren karar,
- sonraki due diligence dosyasında kritik belge olacak karar.

İnceleme bayrağı varsa taslak başında bunu reviewer note içinde göster.

## Karar taslağı yapısı

Formatı profildeki örneğe göre uyarla. Örnek yoksa aşağıdaki iskeleti kullan ve "genel taslak" olduğunu belirt.

```text
[ŞİRKET UNVANI]
[YÖNETİM KURULU / MÜDÜRLER KURULU / GENEL KURUL / KOMİTE] KARAR TASLAĞI

Karar No: [ ]
Karar Tarihi: [ ]
Toplantı Yeri / Şekli: [fiziki / elektronik / toplantısız karar taslağı]
Katılanlar / İmzalayanlar: [ ]
Gündem / Konu: [ ]

Reviewer note:
- Şirket türü ve organ: [ ]
- Dayanak belgeler: [ ]
- Kontrol edilecek formaliteler: [esas sözleşme, nisap, temsil, karar defteri, tescil/ilan, MERSİS, KAP/MKK]
- Doğrulanması gerekenler: [ ]

KARAR

[Kısa arka plan ve karar gerekçesi; belge varsa belge adı, tarih ve taraflar açıkça yazılır.]

1. [Onaylanan işlem açık ve ölçülebilir şekilde yazılır.]
2. [Varsa belirli sözleşme, ek, tutar, karşı taraf, tarih ve versiyon belirtilir.]
3. [Kimlerin hangi belgeleri imzalamaya veya işlemleri yürütmeye yetkili olduğu belirtilir.]
4. [Tescil, ilan, MERSİS, KAP/MKK, noter, KEP veya bildirim adımları için yetki verilir.]
5. [Önceden yapılan işlemler onaylanacaksa kapsamı dar ve açık tutulur.]

İmza:
[İmzalayan adları ve unvanları]
```

## Formalite kontrol listesi

Her çıktıdan sonra şu listeyi üret:

```text
FORMALİTE KONTROL LİSTESİ
□ Şirket türü ve karar organı doğru mu?
□ Esas sözleşme / şirket sözleşmesi özel nisap veya usul içeriyor mu?
□ Toplantı veya karar nisabı kontrol edildi mi?
□ Temsil ve imza yetkisi imza sirküleri/iç yönerge ile uyumlu mu?
□ Menfaat çatışması veya ilişkili taraf işlemi var mı?
□ Karar defterine işlenmesi gereken format doğru mu?
□ Ticaret sicili tescil/ilan veya MERSİS işlemi gerekiyor mu?
□ KAP/MKK/SPK/Rekabet/KVKK veya sektörel bildirim gerekiyor mu?
□ Ekler ve dayanak belgeler karara doğru referanslandı mı?
□ Hukukçu/dış danışman incelemesi gereken işaretli konu kaldı mı?
```

## İmza ve tescil takip listesi

Gerekiyorsa ayrıca üret:

```text
TAKİP LİSTESİ
Karar konusu: [ ]
İmzalayacaklar: [ ]
Eksik imza: [ ]
Karar defteri işlemi: [gerekli / değil / belirsiz]
Ticaret sicili: [tescil / ilan / gerek yok / belirsiz]
MERSİS: [gerekli / değil / belirsiz]
KAP/MKK/SPK: [gerekli / değil / belirsiz]
Noter / KEP / e-imza: [ ]
Sorumlu kişi: [ ]
Hedef tarih: [ ]
```

## Hukukçu olmayan kullanıcı kapısı

Profilde kullanıcı hukukçu değilse sign-ready veya tescile verilecek metin üretmeden önce sor:

> Bu karar şirketi bağlayabilir ve resmi kayıt/defter/sicil sonucu doğurabilir. Sorumlu avukat veya hukukçu ile görüştünüz mü? Görüşmediyseniz, önce şu kısa inceleme notunu onlara iletelim: karar konusu, dayanak belgeler, organ, imza yetkisi, tescil/ilan ihtiyacı ve açık sorular.

Kullanıcı "evet, hukukçu kontrol edecek" demeden nihai dolaşım dili kullanma.

## Bu skill ne yapmaz

- Kararın hukuken geçerli olduğuna kesin hüküm vermez.
- Esas sözleşme, şirket sözleşmesi, imza sirküleri veya karar defteri kontrolünü kullanıcı belgesi olmadan tamamlanmış saymaz.
- Ticaret siciline, KAP'a, MERSİS'e, KEP'e veya notere otomatik gönderim yapmaz.
- Yönetim kurulu, genel kurul veya müdürler kurulu yerine karar vermez.
- Vergi, damga vergisi, SPK, Rekabet, KVKK veya sektör lisansı etkisini uzman kontrolü olmadan kesinleştirmez.
