---
name: board-minutes-zekaisuni
title: Board Minutes
description: Türk şirketler hukuku için yönetim kurulu, müdürler kurulu, genel kurul ve komite toplantı tutanağı/karar taslağı hazırlar. Gündem, hazirun, toplantı şekli, nisap, karar metni, karar defteri, imza, tescil/ilan, MERSİS, KAP/MKK ve hukukçu incelemesi kontrollerini uygular. "tutanak hazırla", "yönetim kurulu tutanağı", "genel kurul tutanağı", "müdürler kurulu kararı", "komite tutanağı", "toplantı kararları" ve benzeri isteklerde kullanılır.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/corporate-legal/skills/board-minutes
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: tr
practice: corporate
language: tr
---

# Board Minutes

## Türk uyarlama notu

Bu skill, orijinal ABD `board minutes` akışını Türk şirketler hukuku pratiğine çevirir. Çıktı bir **tutanak/karar taslağıdır**; benimsenmiş karar, resmi defter kaydı, tescil başvurusu veya hukuki görüş değildir.

Kapsam:

- A.Ş. yönetim kurulu toplantı tutanağı ve karar taslağı
- Ltd. müdürler kurulu veya müdür kararı taslağı
- Genel kurul toplantı tutanağı taslak bölümleri
- Komite toplantı notları ve kararları
- Toplantı sonrası karar defteri, imza, tescil/ilan ve bildirim takip listesi

Toplantısız/sirküler karar için önce `/corporate-legal:written-consent` skill'ini düşün. Kullanıcının istediği şey toplantı tutanağı değil de yalnızca organ kararıysa bu skill yine taslak üretir; fakat formalite kontrolünü ayrıca gösterir.

## Matter context

`~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` içindeki `## Matter workspaces` bölümünü kontrol et. `Enabled` kapalıysa practice-level context ile çalış. Açıksa aktif matter `matter.md` dosyasını oku ve başka matter dosyasına kullanıcı açıkça istemedikçe bakma.

## Load context

Config'ten şu bölümleri oku:

- `## Şirket profili`: şirket türü, MERSİS, ticaret sicili, halka açıklık, sektör izinleri.
- `## Kurumsal yönetim`: organ yapısı, üye sayısı, temsil şekli, esas sözleşme/şirket sözleşmesi, iç yönerge, karar/tutanak formatı, karar defteri lokasyonu.
- `## Sermaye piyasası ve halka açık şirket`: SPK/KAP/MKK veya özel durum açıklaması tetikleyicileri.
- `## Çıktı kuralları`: reviewer note ve kaynak etiketi.

Profilde toplantı/tutanak formatı yoksa genel taslak üretebilirsin; ancak çıktıda bunu açıkça işaretle:

```text
Format notu: Bu taslak şirketin önceki tutanak formatından çıkarılmadı. Şirket içi format, karar defteri uygulaması ve hukukçu kontrolüyle uyarlanmalıdır.
```

## Step 1 - Toplantıyı belirle

Varsa takvim veya toplantı davetinden bilgileri çek. Yoksa kısa sor:

- Toplantı hangi organ için: yönetim kurulu, müdürler kurulu, genel kurul, komite?
- Şirket türü nedir: A.Ş., Ltd. Şti., şube veya başka yapı?
- Tarih, saat, yer veya elektronik toplantı platformu nedir?
- Toplantı olağan mı, olağanüstü mü?
- Gündem maddeleri ve varsa dayanak belgeler nelerdir?

Genel kurul ise ayrıca sor:

- Çağrı usulü ve ilan/davet belgeleri var mı?
- Hazirun listesi veya katılımcı pay sahipleri bilgisi var mı?
- Bakanlık temsilcisi, noter veya elektronik genel kurul gibi özel formalite var mı?
- Halka açık şirketse KAP/MKK veya SPK boyutu var mı?

Yönetim kurulu veya müdürler kurulu ise ayrıca sor:

- Toplantıya çağrı ve gündem nasıl iletildi?
- Üyelerden kimler katıldı, kimler katılmadı?
- Temsil veya imza yetkisi değişiyor mu?
- Kararın tescil/ilan veya MERSİS sonucu var mı?

## Step 2 - Katılım ve nisap kontrolü

Katılım listesini belgeye dayandırmaya çalış:

- takvim daveti,
- imza listesi,
- hazirun cetveli,
- elektronik toplantı kaydı,
- toplantı notu,
- kullanıcı beyanı.

Nisap için kesin hüküm kurma. Şu kontrolü uygula:

```text
Nisap kontrolü:
- Kaynak: [esas sözleşme / şirket sözleşmesi / iç yönerge / TTK kontrolü gerekli / kullanıcı beyanı]
- Toplantı nisabı: [doğrulandı / doğrulanmalı / uygulanmaz]
- Karar nisabı: [doğrulandı / doğrulanmalı / uygulanmaz]
- Çekimser/karşı oy/menfaat çatışması: [var / yok / belirsiz]
```

Nisap belirsizse tutanak taslağında kararın geçerli olduğunu söyleme. Şunu yaz:

```text
[review] Toplantı ve karar nisabı esas sözleşme/şirket sözleşmesi ve güncel mevzuat üzerinden doğrulanmadan bu taslak resmi karar gibi kullanılmamalıdır.
```

## Step 3 - Gündem ve materyalleri oku

Kullanıcıdan şunları iste:

- gündem,
- sunum veya yönetim notu,
- onaylanacak sözleşme veya işlem dokümanı,
- finansal tablolar veya faaliyet raporu,
- önceki tutanak/karar örneği,
- hazirun veya katılım listesi,
- karar defteri veya şirket içi format örneği.

Materyallerden çıkar:

- gündem maddeleri ve sırası,
- onay veya yetkilendirme gerektiren kararlar,
- bilgi amaçlı sunumlar,
- ek veya dayanak belgeler,
- tescil/ilan, MERSİS, KAP/MKK, Rekabet, KVKK veya sektör bildirimi ihtimali,
- menfaat çatışması veya ilişkili taraf işareti.

Materyal yoksa tartışma içeriği uydurma. Placeholder kullan:

```text
[PLACEHOLDER - Bu gündem maddesinde yapılan açıklama ve tartışma kullanıcı/hukukçu tarafından doldurulmalı.]
```

## Step 4 - Tutanak/karar taslağı üret

Şirketin önceki formatı varsa ona uy. Yoksa aşağıdaki genel iskeleti kullan.

### Yönetim kurulu / müdürler kurulu genel iskeleti

```text
[ŞİRKET UNVANI]
[YÖNETİM KURULU / MÜDÜRLER KURULU] TOPLANTI TUTANAĞI VE KARAR TASLAĞI

Karar No: [ ]
Toplantı Tarihi: [ ]
Toplantı Saati: [ ]
Toplantı Yeri / Şekli: [fiziki / elektronik / hibrit]
Katılanlar: [ ]
Katılmayanlar: [ ]
Toplantı Başkanı: [ ]
Tutanak Yazmanı / Sekreter: [ ]

Reviewer note:
- Kaynaklar: [ ]
- Nisap ve temsil kontrolü: [doğrulandı / doğrulanmalı]
- Karar defteri / imza / tescil / MERSİS / KAP-MKK kontrolü: [ ]
- Hukukçu incelemesi gereken alanlar: [ ]

GÜNDEM
1. [ ]
2. [ ]

GÖRÜŞMELER VE KARARLAR

Gündem 1 - [Başlık]
[Sunulan bilgi ve tartışmanın kısa özeti. Kişi atfı yalnızca hukuken gerekli olduğunda yapılır.]

Karar:
1. [Açık ve ölçülebilir karar metni.]
2. [Varsa yetkilendirme, imza, tescil, ilan, bildirim ve ek belge referansları.]

Oy durumu:
[oybirliği / oyçokluğu / karşı oy / çekimser / doğrulanmalı]

KAPANIŞ
Başka gündem maddesi kalmadığından toplantı saat [ ] itibarıyla sona ermiştir.

İmza:
[Ad Soyad - Unvan]
```

### Genel kurul taslak iskeleti

```text
[ŞİRKET UNVANI]
[OLAĞAN / OLAĞANÜSTÜ] GENEL KURUL TOPLANTI TUTANAĞI TASLAĞI

Toplantı Tarihi: [ ]
Toplantı Yeri: [ ]
Çağrı / İlan Bilgisi: [ ]
Hazirun: [ekli / doğrulanmalı]
Toplantı Başkanı: [ ]
Tutanak Yazmanı: [ ]
Bakanlık Temsilcisi / Noter / Elektronik Sistem: [var / yok / belirsiz]

Reviewer note:
- Hazirun ve nisap: [doğrulandı / doğrulanmalı]
- Pay sahipliği veya temsil belgeleri: [ ]
- Tescil/ilan, MERSİS, KAP/MKK: [ ]
- Açık hukuki kontrol: [ ]

GÜNDEM VE KARARLAR

1. [Gündem maddesi]
[Görüşme özeti ve karar metni.]

Oy durumu:
[ ]

KAPANIŞ VE İMZALAR
[ ]
```

## Drafting notes

- Tutanaklar karar defteri ve ileride due diligence dosyasında görülebilecek resmi/kurumsal kayıt niteliği taşıyabilir; gereksiz hukuki analiz veya avukat-müvekkil iletişimi ayrıntısı tutanağa konmamalıdır.
- Tartışma özeti, şirketin önceki tutanak derinliğine göre ayarlanır: kısa aksiyon tutanağı, karma format veya ayrıntılı anlatım.
- Kişi isimleriyle soru/yorum atfı yalnızca gerekli olduğunda yapılır. Hassas iç değerlendirmeler ayrı gizli hukuk notunda tutulabilir.
- Karar metni "işlem onaylandı" gibi belirsiz bırakılmaz; belge adı, tarih, taraf, tutar, versiyon, ek ve yetkilendirilen kişi mümkün olduğunca açık yazılır.
- Tescil/ilan gerektirebilecek kararlar için karar metninde yetki ve takip adımı ayrı gösterilir.
- Halka açık şirketlerde özel durum açıklaması, ilişkili taraf işlemi, içsel bilgi ve KAP/MKK etkisi reviewer note içinde işaretlenir.
- KVKK, Rekabet Kurumu, SPK veya sektör izni boyutu olan kararlar ayrı eskalasyon adayıdır.

## Consequential-action gate

Profilde kullanıcı hukukçu değilse veya karar resmi işleme gidecekse şunu sor:

```text
Bu tutanak/karar şirketi bağlayabilir, karar defterine işlenebilir, ticaret siciline tescil/ilan edilebilir veya KAP/MKK gibi resmi açıklama sonucu doğurabilir. Sorumlu avukat veya hukukçu bu taslağı inceleyecek mi?
```

"Evet" cevabı yoksa yalnızca "avukat/hukukçu incelemesine tabi taslak" üret; "imzaya hazır", "tescile hazır" veya "kabul edilmiş tutanak" dili kullanma.

Büyük işlem, sermaye değişikliği, birleşme/bölünme, tür değiştirme, tasfiye, halka açık şirket açıklaması, ilişkili taraf işlemi veya Rekabet Kurumu/SPK/KVKK etkisi varsa aynı kapıyı hukukçu kullanıcı için de reviewer note olarak göster.

## Output

Çıktı sırası:

1. Reviewer note
2. Tutanak/karar taslağı
3. Kontrol listesi
4. İmza ve takip listesi

Kontrol listesi:

```text
KONTROL LİSTESİ
□ Şirket türü ve organ doğru mu?
□ Gündem ve dayanak belgeler taslağa doğru işlendi mi?
□ Katılım/hazirun listesi doğrulandı mı?
□ Toplantı ve karar nisabı kontrol edildi mi?
□ Karşı oy, çekimser oy veya menfaat çatışması var mı?
□ Karar metni açık, uygulanabilir ve ekleri doğru referanslıyor mu?
□ Temsil/imza yetkisi ve imza sirküleri kontrol edildi mi?
□ Karar defterine işleme formatı uygun mu?
□ Ticaret sicili tescil/ilan veya MERSİS işlemi gerekiyor mu?
□ KAP/MKK/SPK/Rekabet/KVKK/sektör bildirimi gerekiyor mu?
□ Tutanakta kalmaması gereken gizli hukuki değerlendirme var mı?
```

Takip listesi:

```text
TAKİP LİSTESİ
İmza eksikleri: [ ]
Karar defteri: [işlenecek / işlendi / belirsiz]
Ticaret sicili: [gerekli / değil / belirsiz]
MERSİS: [gerekli / değil / belirsiz]
KAP/MKK/SPK: [gerekli / değil / belirsiz]
KEP / noter / e-imza: [ ]
Sorumlu kişi: [ ]
Hedef tarih: [ ]
```

## Written consents

Kullanıcı toplantı tutanağı değil, toplantısız/sirküler organ kararı istiyorsa `/corporate-legal:written-consent` skill'ine yönlendir veya onun karar taslağı kapılarını uygula. Aynı çıktıda iki farklı resmi formatı karıştırma.

## Bu skill ne yapmaz

- Toplantıya katılmış gibi gerçek zamanlı kayıt oluşturmaz.
- Toplantı veya karar nisabının sağlandığına belge olmadan kesin hüküm vermez.
- Esas sözleşme, şirket sözleşmesi, iç yönerge, imza sirküleri veya karar defteri kontrolünü kullanıcı belgesi olmadan tamamlanmış saymaz.
- Tutanakları kabul edilmiş, imzaya hazır veya tescile hazır ilan etmez.
- Ticaret sicili, MERSİS, KAP, MKK, noter, KEP veya başka resmi sisteme otomatik gönderim yapmaz.
- Şirket organları, avukat veya hukuk müşaviri yerine hukuki karar vermez.
