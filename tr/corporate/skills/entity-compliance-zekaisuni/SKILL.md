---
name: entity-compliance-zekaisuni
title: /entity-compliance
description: Türk şirketler hukuku için tüzel kişi ve şirket kayıt takip skill'i. MERSİS, ticaret sicili, faaliyet belgesi, imza sirküleri, karar defterleri, pay defteri, VERBİS, vergi/SGK, KEP/e-imza ve sektörel izin kayıtlarını izler. Init, rapor, güncelleme, sağlık denetimi ve CSV/table export modları için kullanılır.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/corporate-legal/skills/entity-compliance
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: tr
practice: corporate
language: tr
---

# /entity-compliance

## Amaç

Bu skill, bir şirketin veya grup şirketlerinin Türkiye uygulamasındaki temel kurumsal kayıtlarını tek takip dosyasında tutar. Orijinal ABD `annual report / franchise tax / Secretary of State` mantığı kullanılmaz. Türk uyarlamanın odağı şunlardır:

- MERSİS ve ticaret sicili kayıtları,
- Türkiye Ticaret Sicili Gazetesi ilanları,
- faaliyet belgesi, sicil tasdiknamesi ve imza sirküleri,
- yönetim kurulu, müdürler kurulu, genel kurul kararları,
- karar defteri, pay defteri ve diğer yasal defter kayıtları,
- sermaye, pay sahipliği, temsil ve imza yetkisi değişiklikleri,
- VERBİS, KVKK envanteri ve veri işleme kayıtları,
- vergi, SGK, e-defter, e-fatura/e-arşiv ve mali kayıt takipleri,
- SPK/KAP/MKK veya sektör lisansı gerektiren özel durumlar.

Skill resmi başvuru veya tescil yapmaz; kayıtların görünürlüğünü ve açık işleri yönetir.

## Çalışma dosyası

Tracker:

`~/.claude/plugins/config/claude-for-legal/corporate-legal/entities/compliance-tracker.yaml`

Config:

`~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md`

Her modda önce config'teki `## Entity management`, `## Şirket profili` ve varsa aktif matter bağlamını oku.

## Güncellik uyarısı

Ticaret sicili, SPK/KAP, MKK, VERBİS, vergi, SGK, sektör lisansı ve defter formaliteleri değişebilir veya olay bazında farklılaşabilir. Bu skill güncel resmi kaynağı doğrulamadan kesin son tarih, tescil gerekliliği veya uyum sonucu vermez. Resmi kaynak okunmadıysa tracker'da kayıt `verify`, raporda "doğrulanmalı" olarak işaretlenir.

## Tracker şeması

Yapısal veri standardı için corporate `CLAUDE.md` dosyasındaki `## Yapısal veri standardı` bölümünü uygula. Yeni veya yeniden yazılan tracker dosyalarında YAML anahtarları ASCII `english_snake_case` olmalıdır. Kontrol edilen durum değerleri ASCII makine token'ı olarak tutulur. Kullanıcıya görünen rapor ve tablo başlıkları Türkçe kalır.

```yaml
metadata:
  company: "[Şirket / grup adı]"
  generated: "[YYYY-MM-DD]"
  last_updated: "[YYYY-MM-DD]"
  last_audit: "[YYYY-MM-DD veya null]"
  source_note: "Kayıtlar kullanıcı belgeleri ve/veya manuel resmi kaynak kontrollerinden derlenmiştir."

entities:
  - legal_name: "[Şirket unvanı]"
    short_name: "[opsiyonel]"
    entity_type: "[anonim_sirket / limited_sirket / branch / liaison_office / foreign_subsidiary / other]"
    status: "[active / inactive / liquidation / deregistered / unknown]"
    mersis_no: "[no veya belirsiz]"
    trade_registry:
      registry_office: "[İstanbul / Ankara / vb.]"
      registry_no: "[no]"
      last_gazette_date: "[YYYY-MM-DD veya unknown]"
      source: "[TTSG / user_provided / verify]"
    tax:
      tax_office: "[ ]"
      tax_no: "[ ]"
      status: "[current / verify]"
    capital:
      amount_try: "[ ]"
      paid_in: "[yes / no / unknown]"
      last_change_date: "[YYYY-MM-DD veya unknown]"
    ownership:
      shareholder_source: "[share_ledger / KAP / MKK / user_statement / verify]"
      notes: ""
    representation:
      signature_method: "[sole / joint / limited / unknown]"
      signature_circular_date: "[YYYY-MM-DD veya unknown]"
      internal_directive: "[exists / none / unknown]"
    statutory_books:
      board_resolution_book: "[current / missing / verify]"
      share_ledger: "[current / missing / verify / not_applicable]"
      general_assembly_book: "[current / missing / verify]"
    compliance_records:
      verbis: "[registered / exempt / unknown / verify]"
      kvkk_inventory: "[exists / missing / unknown]"
      sgk: "[current / verify]"
      e_ledger: "[exists / missing / unknown]"
      sector_licenses: []
    follow_ups:
      - topic: "[olağan genel kurul / faaliyet belgesi yenileme / imza sirküleri / VERBİS / vb.]"
        owner: "[kişi/ekip]"
        target_date: "[YYYY-MM-DD veya unknown]"
        status: "[current / upcoming / overdue / unknown]"
        source: "[official_source / user_provided / verify]"
        note: ""
```

Eski tracker dosyalarında Türkçe anahtarlar varsa okurken kabul et ve eşleştir: `unvan -> legal_name`, `kisa_ad -> short_name`, `tur -> entity_type`, `durum -> status`, `ticaret_sicili -> trade_registry`, `vergi -> tax`, `sermaye -> capital`, `sahiplik -> ownership`, `temsil -> representation`, `defterler -> statutory_books`, `uyum_kayitlari -> compliance_records`, `takipler -> follow_ups`. Dosyayı yeniden yazarken yalnızca canonical anahtarları kullan.

## Mod yönlendirme

- Flag yok veya `--init`: Mode 1 - tracker oluştur.
- `--report`: Mode 2 - açık iş ve yaklaşan takipleri raporla.
- `--update`: Mode 3 - manuel veya rapordan güncelle.
- `--sweep`: Mode 4 - `unknown`, `verify`, `overdue` veya `upcoming` kayıtlarını tek tek sor.
- `--audit`: Mode 5 - sağlık denetimi.
- `--export`: Mode 6 - CSV veya markdown tablo üret.

## Mode 1 - Init

1. Config'teki entity tablosunu oku.
2. Tablo yoksa kullanıcıdan grup şirketleri listesi, organizasyon şeması, ticaret sicili dökümü veya mevcut tracker iste.
3. Her şirket için zorunlu alanları çıkar: unvan, tür, MERSİS, ticaret sicili, vergi no, durum, sahiplik, temsil.
4. Tracker'a yazarken canonical `english_snake_case` alan adlarını kullan; raporda Türkçe alan adlarını göster.
5. Belgeyle doğrulanmayan alanları boş uydurma; şemada `unknown` veya `verify` yaz.
6. Tracker dosyasını oluştur.

Init özeti:

```text
Entity tracker oluşturuldu.
Şirket sayısı: [N]
Doğrulanmış kayıt: [N]
Doğrulanması gereken alan: [N]
Gecikmiş/açık takip: [N]
Sonraki adım: /corporate-legal:entity-compliance --report
```

## Mode 2 - Report

Varsayılan rapor 90 günlük görünüm verir. `--days N` varsa o aralığı kullan.

Rapor formatı:

```text
ENTITY COMPLIANCE REPORT - [tarih]

KIRMIZI - Gecikmiş veya kritik ([N])
- [Şirket] / [konu] / [hedef tarih] / [not]

SARI - Yaklaşan takipler ([N])
- [Şirket] / [konu] / [hedef tarih] / [sorumlu]

BELİRSİZ - Doğrulama gereken kayıtlar ([N])
- [Şirket] / [alan] / [neden doğrulanmalı]

GÜNCEL - Son doğrulananlar ([N])
- [Şirket] / [alan] / [kaynak] / [tarih]

ÖNERİLEN AKSİYONLAR
1. [en kritik aksiyon]
2. [sonraki aksiyon]
```

10'dan fazla satır varsa dashboard veya CSV export teklif et; otomatik dosyalama yapma.

## Mode 3 - Update

### Manuel güncelleme

Kullanıcı örneğin şöyle der:

```text
ABC A.Ş. imza sirküleri 2026-05-01 tarihinde yenilendi.
```

Tracker'da ilgili alanı güncelle:

- tarih,
- kaynak,
- durum,
- varsa belge yolu,
- `last_updated`.

### Rapordan güncelleme

`--update --from-report` ile kullanıcı faaliyet belgesi, sicil dökümü, TTSG kaydı, KAP linki, MERSİS ekran çıktısı, vergi/SGK yazısı veya danışman raporu verebilir.

İşle:

- belgeyi oku,
- şirket adıyla eşleştir,
- farklı unvan/yazım varsa onay iste,
- doğrulanan alanları güncelle,
- raporda olup tracker'da olmayan şirketleri "eklenecek aday" olarak listele.

## Mode 4 - Sweep

`unknown`, `verify`, `overdue` veya `upcoming` kayıtlarını tek tek sor. Eski tracker'dan gelen `belirsiz`, `doğrulanmalı`, `gecikmiş` veya `yaklaşıyor` değerlerini okurken aynı şekilde ele al:

```text
[Şirket] / [alan] şu anda [durum].
Güncel belge veya tarih var mı? Yoksa bu alanı doğrulanmalı olarak bırakıyorum.
```

Her cevap sonrası tracker'ı güncelle ve kısa özet ver.

## Mode 5 - Audit

Sağlık denetimi yalnızca kayıt ve süreç eksiklerini görünür yapar. Hukuki geçerlilik kararı vermez.

Kontrol başlıkları:

- MERSİS ve ticaret sicili bilgileri tutarlı mı?
- Ticaret unvanı, merkez, sermaye, temsil ve yönetim bilgileri güncel mi?
- İmza sirküleri ve iç yönerge güncel mi?
- Karar defteri, genel kurul defteri ve pay defteri kayıtlarında boşluk var mı?
- Olağan genel kurul, yönetim kurulu/müdürler kurulu kararları ve tescil gerektiren kararlar izleniyor mu?
- Pay sahipliği, sermaye artırımı/azaltımı ve devir kayıtları tutarlı mı?
- VERBİS ve KVKK envanteri durumu biliniyor mu?
- Vergi, SGK, e-defter/e-fatura ve mali kayıtlar için sorumlu ekip belli mi?
- Halka açık veya regüle şirketlerde KAP/MKK/SPK/sektör lisansı takipleri var mı?
- Pasif veya tasfiye halinde şirketler için kapanış planı var mı?

Audit çıktısı:

```text
ENTITY HEALTH AUDIT - [tarih]

KRİTİK AÇIKLAR
- [bulgu]

KAYIT TUTARSIZLIKLARI
- [bulgu]

DOĞRULANMASI GEREKENLER
- [bulgu]

ÖNERİLEN AKSİYON PLANI
1. [aksiyon]
2. [aksiyon]
3. [aksiyon]
```

## Mode 6 - Export

`--export --format csv` veya `--export --format table` desteklenir.

CSV kolonları:

```text
Unvan, Tür, Durum, MERSİS No, Ticaret Sicili Müdürlüğü, Sicil No, Vergi Dairesi, Vergi No, Sermaye TL, Temsil Şekli, İmza Sirküleri Tarihi, VERBİS, Son İlan Tarihi, Takip Konusu, Hedef Tarih, Takip Durumu, Kaynak, Not
```

CSV/Excel güvenliği:

- Kullanıcı belgesi veya dış kaynaktan gelen hücre `=`, `+`, `-`, `@`, tab veya yeni satırla başlıyorsa metin olarak güvenli hale getir.
- CSV'de virgül, çift tırnak ve yeni satırları RFC 4180'e uygun kaçır.

## Hukukçu olmayan kullanıcı kapısı

Kullanıcı hukukçu değilse ve kayıt "filed/tescil edildi/bildirildi" gibi hukuki sonuç doğuran bir güncelleme yapmak istiyorsa sor:

> Bu kayıt resmi temsil, tescil, bildirim veya uyum sonucu doğurabilir. Sorumlu avukat, hukuk müşaviri, mali müşavir veya kayıt sorumlusu belgeyi doğruladı mı?

"Evet" cevabı yoksa sadece araştırma notu ve yapılacaklar listesi üret; tracker'da sonucu kesinleştirme.

## Bu skill ne yapmaz

- Ticaret siciline, MERSİS'e, KAP'a, MKK'ya, VERBİS'e, SGK'ya veya vergi sistemlerine başvuru yapmaz.
- Tescil veya ilan gerekip gerekmediğine kesin hukuki görüş vermez.
- Faaliyet belgesi, iyi hal belgesi, imza sirküleri veya karar defteri kaydını kullanıcı belgesi olmadan doğrulanmış saymaz.
- Vergi, muhasebe, SGK veya damga vergisi sonucunu kesin hesaplamaz.
- Şirket organları yerine karar vermez veya imza yetkisi yaratmaz.
