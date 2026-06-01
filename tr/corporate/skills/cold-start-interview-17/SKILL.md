---
name: cold-start-interview-17
title: /cold-start-interview
description: Türk şirketler hukuku için corporate-legal başlangıç mülakatı. Şirket profili, aktif modüller, M&A, kurumsal yönetim, sermaye piyasası ve entity management bilgilerini toplar; Türk uygulamasına uygun CLAUDE.md profilini yazar. Fresh install, [PLACEHOLDER] bulunan config, yeni işlem, modül yenileme veya entegrasyon kontrolü için kullanılır.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/corporate-legal/skills/cold-start-interview
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: corporate
language: tr
---

# /cold-start-interview

## Amaç

Bu skill, `corporate-legal` plugin'ini Türk şirketler hukuku ve Türkiye uygulamasına göre yapılandırır. Orijinal ABD modülleri şu karşılıklara çevrilir:

| Orijinal modül | Türk uyarlaması |
|---|---|
| M&A | Hisse/pay devri, malvarlığı devri, birleşme, bölünme, tür değiştirme, yatırım, JV ve kapanış yönetimi |
| Board & Secretary | Yönetim kurulu, müdürler kurulu, genel kurul, karar/tutanak, karar defteri ve imza süreci |
| Public Company | SPK, Borsa İstanbul, KAP, MKK, özel durum açıklaması ve kurumsal yönetim |
| Entity Management | MERSİS, ticaret sicili, faaliyet belgesi, imza sirküleri, karar defteri, VERBİS, vergi/SGK takipleri |

Komut adları geriye dönük uyumluluk için İngilizce kalır; profil ve çıktı içeriği Türk hukukuna göre yazılır.

## Dosya yolları

- Config: `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md`
- Ortak şirket profili: `~/.claude/plugins/config/claude-for-legal/company-profile.md`
- Yeni işlem bağlamı: `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/deal-context.md`

Config yoksa veya `[PLACEHOLDER]` içeriyorsa mülakatı başlat. Populated config varsa `--redo`, `--module` veya `--new-deal` yoksa kullanıcıya zaten kurulu olduğunu söyle ve neyi güncellemek istediğini sor.

## Başlangıç mesajı

Kısa ve doğrudan başla:

> `corporate-legal`, Türk şirketler hukuku iş akışları için profil kurar: M&A, yönetim kurulu/genel kurul, halka açık şirket uyumu ve tüzel kişi kayıt takibi.  
> Hızlı kurulum 2-3 dakika sürer; tam kurulumda örnek karar, tutanak, due diligence listesi ve entity tablosu da alınır.  
> Hızlı mı, tam mı ilerleyelim?

Kullanıcı cevap vermeden uzun soru listesine geçme.

## Entegrasyon kontrolü

`--check-integrations` kullanılırsa sadece kaynak durumunu kontrol et ve `## Entegrasyonlar` tablosunu güncelle.

Bağlantı durumu için:

- `✓` yalnızca araç gerçekten yanıt verdiyse.
- `manuel` kaynak doğrudan bağlı değil ama kullanıcı belge/link/ekran çıktısı sağlayabiliyorsa.
- `✗` kaynak yoksa.

Türkiye uygulamasında özellikle sor:

- VDR veya belge arşivi var mı?
- Drive, SharePoint, Box, iManage veya yerel klasör mü kullanılıyor?
- KAP/MKK kayıtları nasıl kontrol ediliyor?
- MERSİS, ticaret sicili ve faaliyet belgesi kimden geliyor?
- KEP/e-imza/noter kayıtları nerede tutuluyor?
- KVKK/VERBİS ve Rekabet Kurumu takipleri kimde?

## Mülakat akışı

Bir turda en fazla 2-3 kısa soru sor. Belge varsa kullanıcıyı yazmaya zorlamadan belge/link istemeyi tercih et.

### Part 0 - Rol ve bağlam

Sor:

1. Bu profili kim kullanacak: avukat, hukuk müşaviri, hukuk operasyonu, avukat gözetiminde çalışan veya hukukçu olmayan kullanıcı?
2. Çalışma bağlamı nedir: şirket içi hukuk, hukuk bürosu, grup hukuk operasyonu, tekil danışmanlık?
3. Hangi modüller aktif: M&A, kurumsal yönetim, sermaye piyasası, entity management?

Hukukçu olmayan kullanıcı varsa profilde şunu işaretle:

```text
Çıktılar araştırma ve taslak niteliğindedir. İmza, tescil, bildirim, dosyalama veya bağlayıcı işlem öncesinde avukat/hukukçu kontrolü gerekir.
```

### Part 1 - Şirket profili

Ortak şirket profili varsa oku ve tek satırda teyit et. Yoksa sor:

- Şirket veya grup adı nedir?
- Şirket türü nedir: A.Ş., Ltd. Şti., şube, irtibat bürosu, halka açık A.Ş. veya grup şirketi?
- Sektör ve ana faaliyet nedir?
- Ticaret sicili, MERSİS ve vergi no bilgileri var mı?
- Halka açıklık, SPK/Borsa İstanbul/KAP/MKK durumu var mı?
- Hukuk ekibinde karar/escalation kime gider?

Şirketin internet sitesi, faaliyet raporu, KAP sayfası, ticaret sicili kaydı, imza sirküleri veya organizasyon şeması paylaşılırsa bilgiyi oradan çıkar ve teyit ettir.

### Part 2M - M&A ve işlem yönetimi

Yalnızca M&A modülü aktifse sor.

Önce belge iste:

> Standart due diligence talep listeniz, önceki issue memo'nuz, kapanış checklist'iniz veya disclosure schedule örneğiniz varsa paylaşın. Bunlardan kategori, eşik ve formatı çıkarırım.

Belge yoksa sor:

- Tipik işlem türleri neler: pay devri, hisse alımı, malvarlığı devri, birleşme, bölünme, tür değiştirme, yatırım, JV?
- Genelde hangi taraftasınız: alıcı, satıcı, yatırımcı, hedef şirket veya değişken?
- Önemlilik eşiği TL veya stratejik kategori olarak nasıl belirleniyor?
- VDR nerede tutuluyor?
- Dış danışman ve işlem lideri kim?
- Rekabet Kurumu, SPK/KAP/MKK, KVKK, çalışma, vergi veya sektör izni hangi durumda otomatik eskalasyon?

Profile yaz:

- işlem türleri,
- due diligence kategori listesi,
- önemlilik eşikleri,
- issue memo formatı,
- kapanış listesi sahibi ve güncelleme periyodu,
- dış danışman/escalation yolu.

### Part 2G - Kurumsal yönetim

Yalnızca governance modülü aktifse sor.

Önce örnek belge iste:

> 2-3 önceki yönetim kurulu, müdürler kurulu veya genel kurul kararı/tutanağı paylaşabilirsen formatı çıkarırım. Paylaşamazsan standart taslak profiliyle başlarız.

Sor:

- Şirket türü ve organ yapısı nedir?
- Yönetim kurulu veya müdürler kurulu kaç kişiden oluşuyor?
- Temsil şekli ve imza yetkisi nasıl: münferit, müşterek, sınırlı yetki, iç yönerge?
- Esas sözleşme veya şirket sözleşmesinde özel toplantı/karar nisabı var mı?
- Toplantısız/sirküler karar kullanılıyor mu, yoksa toplantı tutanağı mı tercih ediliyor?
- Karar defteri, pay defteri, genel kurul tutanakları ve imza sirküleri nerede tutuluyor?
- Tescil/ilan gerektiren kararları kim takip ediyor?

Profile yaz:

- organ yapısı,
- karar/tutanak formatı,
- temsil ve imza yetkisi,
- karar defteri ve sicil takibi,
- menfaat çatışması ve ilişkili taraf eskalasyonu.

### Part 2P - Sermaye piyasası / halka açık şirket

Yalnızca public modülü aktifse sor.

- Şirket SPK'ya tabi mi, Borsa İstanbul'da işlem görüyor mu?
- KAP açıklaması kim tarafından hazırlanır ve kim onaylar?
- MKK/pay kayıt süreçlerini kim izler?
- Özel durum açıklaması, içsel bilgi, işlem yasağı ve ilişkili taraf işlemleri için iç politika var mı?
- Kurumsal yönetim komitesi, denetim komitesi veya yatırımcı ilişkileri birimiyle çalışma akışı nasıl?

Bu bölümde SEC/NYSE/Nasdaq veya Form 4 soruları sorma. Türkiye profilini SPK, KAP, MKK ve şirketin açıklama politikası üzerinden kur.

### Part 2E - Entity management

Yalnızca entities modülü aktifse sor.

Önce tablo iste:

> Grup şirketleri listesi, organizasyon şeması, ticaret sicili dökümü veya entity tracker varsa paylaşın. Şirket adı, tür, MERSİS, sicil, vergi no, sahiplik ve durum alanlarını oradan çıkarırım.

Belge yoksa sor:

- Kaç aktif tüzel kişi izleniyor?
- Şirket türleri neler: A.Ş., Ltd., şube, irtibat bürosu, yurt dışı bağlı ortaklık?
- MERSİS ve ticaret sicili kayıtları kimde?
- Faaliyet belgesi, imza sirküleri, karar defteri ve pay defteri nerede tutuluyor?
- VERBİS/KVKK envanteri, vergi, SGK, e-defter/e-fatura ve sektör izinleri kim tarafından takip ediliyor?
- Pasif/tasfiye/dormant şirket var mı?

Profile yaz:

- entity tablosu,
- takip edilen kayıt türleri,
- sorumlu kişi/ekip,
- periyodik kontrol takvimi,
- tracker dosyası yolu.

## Yeni işlem kurulumu (`--new-deal`)

`--new-deal` yalnızca M&A/işlem bağlamı kurar; şirket profili aynı kalır.

Sor:

- İşlem kod adı
- İşlem türü ve taraf rolü
- Karşı taraf / hedef şirket / yatırımcı adı
- VDR veya belge klasörü
- İmza ve kapanış hedef tarihleri
- Dış danışman ve işlem lideri
- Bu işlemde farklı önemlilik eşiği veya özel risk var mı?

Yaz:

`~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/deal-context.md`

## Yazmadan önce kalite kontrol

Config'i yazmadan önce eksikleri göster:

- Hangi modüller aktif?
- Hangi örnek belgeler eksik?
- Hangi kaynaklar manuel doğrulanacak?
- Hangi alanlarda `[PLACEHOLDER]` kalacak?

Kullanıcı açıkça "şimdilik böyle kalsın" demeden kritik boşluğu sessizce geçme.

## Yazılacak profil

`CLAUDE.md` template'indeki başlıkları koru; sadece aktif modülleri doldur. Kullanılmayan modülleri silebilir veya "aktif değil" olarak işaretleyebilirsin.

Şunları kesinlikle yapma:

- Delaware, SEC, NYSE/Nasdaq, Secretary of State veya franchise tax varsayımı yazma.
- `unanimous written consent` kavramını Türk hukukunda birebir geçerliymiş gibi kullanma.
- Resmi kaynak kontrol edilmeden kesin süre, eşik, bildirim veya tescil sonucu üretme.
- Kullanıcı belgesi olmadan imza yetkisi veya temsil şekli uydurma.

## Kapanış mesajı

Kısa kapat:

> Profil yazıldı. Aktif modüller: [liste]. İlk kullanabileceğiniz komutlar: [2-3 öneri]. Eksik kalan örnek belgeler: [liste veya yok].

Sonra en doğal ilk komutu öner:

- Aktif M&A varsa: `/corporate-legal:closing-checklist` veya `/corporate-legal:diligence-issue-extraction`
- Aktif governance varsa: `/corporate-legal:written-consent`
- Aktif entities varsa: `/corporate-legal:entity-compliance --init`
