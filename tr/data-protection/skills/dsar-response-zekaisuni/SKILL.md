---
name: dsar-response-zekaisuni
title: /dsar-response
description: KVKK kapsamında ilgili kişi başvurusunu sınıflandırır ve yanıt taslağı üretir. Erişim, silme/yok etme/anonim hale getirme, düzeltme, itiraz, aktarım bilgisi, işleme amacını öğrenme ve zarar giderimi taleplerinde KVKK m.11, m.13 ve Veri Sorumlusuna Başvuru Usul ve Esasları Tebliği çerçevesinde kimlik doğrulama, sistem arama, istisna, 30 günlük süre ve yanıt mektubu akışını kurar.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/privacy-legal/skills/dsar-response
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: tr
practice: data-protection
language: tr
---

# /dsar-response

## Başlamadan

İlgili kişi başvurusu kişisel veri içerir. Gereksiz kimlik belgesi, özel nitelikli veri ve üçüncü kişi verisini yapıştırmadan önce maskele. Dosya adında ilgili kişinin adını kullanma.

1. `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` dosyasını oku.
2. `## İlgili Kişi Başvurusu`, `## KVKK Çekirdek Kontrolleri`, `## Çıktı Kuralları` bölümlerini yükle.
3. Matter workspace açıksa aktif matter'ı yükle.
4. Sistem listesi, kimlik doğrulama yöntemi veya sorumlu ekip eksikse bunu ilk bulgu olarak yaz.

## Amaç

Yabancı erişim talebi terminolojisi yerine Türk hukukundaki "ilgili kişi başvurusu" akışını uygular. Temel çerçeve KVKK m.11 hakları ve m.13'teki veri sorumlusuna başvuru sürecidir. Kanuni süre en kısa sürede ve en geç 30 gün olarak ele alınır; farklı sektör veya özel durum varsa güncel kaynakla doğrulanır.

## İş Akışı

### 1. Başvuruyu Sınıflandır

Başvuru birden fazla hak içerebilir:

| Talep | KVKK karşılığı |
|---|---|
| Hangi verilerim var? | Kişisel veri işlenip işlenmediğini öğrenme; işlenmişse bilgi talep etme |
| Verilerimi gönderin | İşlenen veriler ve aktarılan üçüncü kişiler hakkında bilgi |
| Verimi silin | Silme, yok etme veya anonim hale getirme talebi |
| Yanlış veriyi düzeltin | Eksik/yanlış verinin düzeltilmesi |
| Pazarlamayı durdurun | İşleme amacına ve hukuki sebebe göre itiraz / iletişim izni iptali |
| Otomatik karar/profil | Kişi aleyhine sonuç doğuran analizlere itiraz |
| Zararımı giderin | Kanuna aykırı işleme nedeniyle zararın giderilmesi talebi |

Başvuru açık değilse tek netleştirme sorusu sor; süre takibini yine de başlat.

### 2. Kimlik ve Yetki Kontrolü

- Başvuru kanalı geçerli mi?
- Başvuran ilgili kişi mi, veli/vası/vâkil mi?
- Vekalet veya temsil belgesi gerekir mi?
- E-posta/KEP/fiziki başvuru kaydı var mı?
- Düşük riskli bilgi talebi ile hesap silme/özel nitelikli veri talebi aynı doğrulama seviyesinde değildir.

Kimlik doğrulanamazsa veri ifşa etme. Eksik doğrulama talebini kısa ve açık şekilde gönder.

### 3. Sistem Araması

Profildeki sistem listesini tek tek gez:

| Sistem | Arandı mı? | Veri bulundu mu? | Not |
|---|---|---|---|
| Üretim sistemi | | | |
| CRM / satış | | | |
| Destek kayıtları | | | |
| E-posta / pazarlama / İYS | | | |
| Log / güvenlik kayıtları | | | |
| İnsan kaynakları | | | |
| Tedarikçi / veri işleyen | | | |
| Yedekler | | | |

Şirket veri işleyen konumundaysa başvurunun asıl veri sorumlusu müşteriye yönlendirilmesi gerekip gerekmediğini kontrol et.

### 4. İstisna ve Red Analizi

Her veri/talep için şu soruları sor:

- Üçüncü kişilere ait veri var mı; maskeleme gerekir mi?
- Saklama için kanuni yükümlülük, zamanaşımı, dava/uyuşmazlık veya denetim gereği var mı?
- Ticari sır, güvenlik riski, iç soruşturma, avukat-müvekkil gizliliği veya hukuki menfaat etkileniyor mu?
- Talep aynı konuda tekrar eden, ölçüsüz veya açıkça kötüye kullanım niteliğinde mi?
- Veri teknik olarak yedekte ise imha takvimi ve erişim kısıtı nasıl belgelenecek?

Red veya kısmi red hukuki gerekçe ister. Yakın kararları hukukçuya eskale et.

### 5. Taslak Yanıt

Dışa gidecek yanıta gizli çalışma başlığı koyma. İç değerlendirme notuna `## Çıktı Kuralları` başlığındaki çalışma taslağı uyarısını ekle.

```markdown
# İlgili Kişi Başvurusu - İç Değerlendirme

**Başvuru tarihi:** [YYYY-MM-DD]
**Yasal son gün:** [YYYY-MM-DD]
**Talep türü:** [erişim / silme / düzeltme / itiraz / karma]
**Kimlik doğrulama:** [tamam / eksik / temsil belgesi gerekli]

## Sistem Arama Özeti

| Sistem | Sonuç | Aksiyon |
|---|---|---|
| [sistem] | [veri bulundu/bulunmadı] | [üret/sil/düzelt/sakla] |

## Hukuki Değerlendirme

| Talep | Sonuç | Gerekçe | Hukukçu kontrolü |
|---|---|---|---|
| [talep] | kabul/kısmi kabul/red | [KVKK/Tebliğ/kanuni saklama vb.] | evet/hayır |

## Yanıt Taslağı

Sayın [Ad Soyad],

[tarih] tarihli başvurunuz alınmıştır. Başvurunuzda [talep özeti] talep edilmiştir.

[Kabul edilen talepler ve yapılan işlem.]

[Kısmi red/red varsa açık gerekçe.]

[Üçüncü kişi verisi, kanuni saklama veya teknik yedek açıklaması.]

Kanun kapsamındaki başvuru yollarına ilişkin bilgilendirme: [kurum içi başvuru/iletişim ve gerekli ise Kurul şikayet yoluna dair kısa metin].

Saygılarımızla,
[Veri sorumlusu]
```

## Log Kaydı

Her başvuru için kaydet:

- başvuru tarihi ve kanalı,
- talep türü,
- kimlik doğrulama durumu,
- aranan sistemler,
- cevap tarihi,
- kabul/red gerekçesi,
- silme/düzeltme/aktarım aksiyonları,
- hukukçu onayı.

## Eskalasyon

Şunlarda hukuk ve gerekiyorsa security/DPO incelemesi iste:

- gazeteci, avukat, düzenleyici kurum veya dava tarafı başvurusu,
- çalışan, eski çalışan veya disiplin/soruşturma bağlantısı,
- özel nitelikli veri,
- çocuk verisi,
- veri ihlali iddiası,
- toplu/seri başvuru,
- aktif dava veya delil saklama yükümlülüğü,
- önceki cevaba itiraz.

## Bu Skill Ne Yapmaz

- Sistemleri doğrudan sorgulamaz.
- Nihai red/kısmi red kararını hukukçu yerine vermez.
- Başvuruyu göndermez; taslak üretir ve insan onayına bırakır.
