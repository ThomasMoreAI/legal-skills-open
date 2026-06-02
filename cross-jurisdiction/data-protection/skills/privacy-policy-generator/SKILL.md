---
name: privacy-policy-generator
title: Privacy Policy Generator
description: Gizlilik politikası şablonu, çerez politikası, veri işleme açıklamaları ve hak sahipleri.
author: mikailustuner
author_url: https://github.com/mikailustuner/OmniRule/tree/main/skills/privacy-policy-generator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: tr
---

# Privacy Policy Generator

**Odağ Alanı:** Dijital platformlar için kapsamlı gizlilik politikası (Privacy Policy / Gizlilik Bildirimi) şablonu oluşturma; çerez politikası, veri işleme amaçları, veri sahibi hakları ve uluslararası veri aktarımı açıklamalarının düzenlenmesi.

## Pattern 1: Gizlilik Politikası Zorunlu Bölümleri

```
1. ZORUNLU BÖLÜMLER LİSTESİ
├── A. VERİ SORUMLUSUNUN TANIMI (Data Controller Identity)
│   ├── Unvan, ticari ad, kayıtlı adres
│   ├── Vergi kimlik numarası (VKN)
│   ├── İletişim bilgileri (e-posta, telefon, posta adresi)
│   ├── Veri Sorumlusu Sicil Kayıt numarası (VRSKS)
│   ├── Kişisel Verileri Koruma Kurulu başvuru adresi
│   └── Potansiyel Veri İşleyen veya Temsilci atanmışsa bilgisi
│
├── B. İŞLENEN KİŞİSEL VERİLERİN KATEGORİZASYONU
│   ├── Kimlik verileri (ad, soyad, T.C. kimlik no, pasaport no)
│   ├── İletişim verileri (e-posta, telefon, adres)
│   ├── Finansal veriler (banka hesabı, kredi kartı bilgileri)
│   ├── İşlem güvenliği verileri (IP adresi, log kayıtları, cookie)
│   ├── Müşteri işlem verileri (satın alma geçmişi, tercihler)
│   ├── Sağlık verileri (tıbbi cihaz kullanımı, alerji bilgisi)
│   └── Biyometrik veriler (parmak izi, yüz tanıma – varsa)
│
├── C. VERİ İŞLEME AMAÇLARI VE HUKUKİ DAYANAKLAR
│   ├── Sözleşmenin ifası (TBK m. 112 / GDPR m. 6/1-b)
│   ├── Hukuki yükümlülük (vergi, muhasebe kayıtları)
│   ├── Meşru menfaat (güvenlik, dolandırıcılık önleme)
│   ├── Açık rıza (pazarlama, profil oluşturma)
│   └── Vital interest (acil tıbbi müdahale gerekliliği)
│
├── D. VERİ SAHİBİ HAKLARI (Data Subject Rights)
│   ├── Bilgi alma hakkı (KVKK m. 11/1-a / GDPR m. 15)
│   ├── Düzeltme hakkı (m. 11/1-b / GDPR m. 16)
│   ├── Silme hakkı (m. 11/1-c / GDPR m. 17) – "unutulma hakkı"
│   ├── İşlemenin engellenmesi hakkı (m. 11/1-d / GDPR m. 18)
│   ├── Veri taşınabilirliği hakkı (GDPR m. 20)
│   ├── Otomatik karar verme itirazı (GDPR m. 22)
│   └── İtiraz hakkı (KVKK m. 11/1-e / GDPR m. 21)
│
├── E. VERİ AKTARIMI (Data Transfer)
│   ├── Yurt içi aktarım (yeterli koruma tedbiri)
│   ├── Yurt dışı aktarım (ülke yeterlilik kararı / SCC / BCR)
│   └── Üçüncü taraf hizmet sağlayıcıları listesi
│
├── F. ÇEREZ VE İZLEME TEKNOLOJİLERİ
│   ├── Zorunlu çerezler (session cookies)
│   ├── Analitik çerezler (Google Analytics vb.)
│   ├── Pazarlama çerezleri (reklam, yeniden hedefleme)
│   ├── Sosyal medya çerezleri (Facebook Pixel, LinkedIn Insight)
│   └── Kullanıcı onay mekanizması açıklaması
│
├── G. VERİ GÜVENLİĞİ ÖNLEMLERİ
│   ├── Teknik önlemler (şifreleme, erişim kontrolü, TLS)
│   ├── Organizasyonel önlemler (eğitim, prosedürler)
│   └── Veri ihlali durumunda bildirim prosedürü
│
└── H. SAKLAMA SÜRELERİ VE İMHA POLİTİKASI
    ├── Her veri kategorisi için ayrı saklama süresi
    ├── Saklama süresi sona erdiğinde imha yöntemi
    └── İmha yöntemleri (fiziksel imha / digital erase)
```

## Pattern 2: Veri Sahibi Hakları Başvuru Mekanizması

```
VERİ SAHİBİ HAKLARI – BAŞVURU PROSEDÜRÜ

BAŞVURU YÖNTEMLERİ
┌──────────────────┬──────────────────────────────────┬──────────────────────────┐
│ Yöntem           │ Adres                             │ Süre                    │
├──────────────────┼──────────────────────────────────┼──────────────────────────┤
│ Yazılı başvuru   │ [Veri sorumlusu adresi]          │ 30 gün                  │
│ E-posta          │ kvkk@domain.com                  │ 30 gün                  │
│ Noter            │ Noter kanalıyla                    │ 30 gün                  │
│ Elektronik imza  │ [Kayıtlı e-imza adresi]           │ 30 gyun                  │
└──────────────────┴──────────────────────────────────┴──────────────────────────┘

BAŞVURU DEĞERLENDİRME İŞ AKIŞI
Başvuru alış (tarih + yöntem + kimlik doğrulama)
       ↓
Kimlik doğrulama (başvuru sahibi kimliğinin teyidi)
       ↓
Başvuru uygunluk kontrolü (süre, kapsam, yetki)
       ↓
│ Uygun bulundu ────→ Başvuru içeriğine göre işlem
│                        (bilgi verme / düzeltme / silme / itiraz)
│                        ↓
│                   Veri Sorumlusu Sicil Kayıt Sistemi'ne kayıt
│                        ↓
│                   Başvuru sahibine yanıt (30 gün içinde)
│                        ↓
│                   Ret durumunda: Ret gerekçesi + yasal başvuru yolları
│
└── Uygun bulunmadı → Ret gerekçesi açıklaması
                        + KVKK Kurulu'na şikayet hakkı bildirimi

YANIT FORMATI ZORUNLU UNSURLARI
├── Başvuru tarihi ve referans numarası
├── Başvuru konusu (talep edilen hak)
├── Yapılan işlemin açıklaması (veya ret gerekçesi)
├── Veri işleme faaliyetinin hukuki dayanağı
├── Veri sorumlusu yetkilisi imzası ve tarih
└── Hukuki başvuru yolları (KVKK Kurulu'na şikayet + yargı yolu)
```

## Pattern 3: Çerez Politikası Şablonu

```
ÇEREZ POLİTİKASI BÖLÜMLERİ

1. ÇEREZ TANIMI VE İŞLEYİŞİ
"Çerez, bir web sitesini ziyaret ettiğinizde cihazınıza (bilgisayar,
tablet veya telefon) yerleştirilen küçük metin dosyalarıdır. Çerezler,
web sitesinin düzgün çalışmasını sağlamak, güvenliği artırmak,
pazarlama faaliyetlerini gerçekleştirmek ve size daha iyi bir
kullanıcı deneyimi sunmak amacıyla kullanılmaktadır."

2. ÇEREZ TÜRLERİ MATRİSİ
┌────────────────┬──────────────┬────────────────────┬──────────────┬─────────────────────────┐
│ Çerez Türü     │ Örnek        │ Saklama Süresi     │ Onay Gerek. │ Kullanım Amacı          │
├────────────────┼──────────────┼────────────────────┼──────────────┼─────────────────────────┤
│ Zorunlu        │ Session ID  │ Oturum süresi      │ ❌ Hayır      │ Sitenin temel işlevleri │
│ çerezler       │ CSRF token  │                    │             │                         │
├────────────────┼──────────────┼────────────────────┼──────────────┼─────────────────────────┤
│ Performans     │ Google      │ 2 yıl               │ ❌ Hayır      │ Ziyaretçi davranış      │
│ çerezleri     │ Analytics   │                    │             │ analizi                 │
├────────────────┼──────────────┼────────────────────┼──────────────┼─────────────────────────┤
│ İşlevsellik   │ Dil tercihi │ 1 yıl               │ ❌ Hayır      │ Kullanıcı tercihlerini  │
│ çerezleri     │ Tema seçimi │                    │             │ hatırlama               │
├────────────────┼──────────────┼────────────────────┼──────────────┼─────────────────────────┤
│ Pazarlama/     │ Google Ads  │ 90 gün - 2 yıl      │ ✅ Evet       │ Reklam hedefleme,       │
│ hedefleme     │ Facebook Pix│                    │             │ yeniden hedefleme       │
├────────────────┼──────────────┼────────────────────┼──────────────┼─────────────────────────┤
│ Sosyal medya   │ LinkedIn    │ 90 gün - 2 yıl      │ ✅ Evet       │ Sosyal medya           │
│ çerezleri     │ Insight Tag │                    │             │ entegrasyonu            │
└────────────────┴──────────────┴────────────────────┴──────────────┴─────────────────────────┘

3. ONAY YÖNETİMİ (Consent Management)
├── İlk ziyarette çerez bannerı gösterimi
│   ├── Zorunlu olmayan çerezler için onay talebi
│   ├── "Kabul et" / "Yönet" / "Reddet" seçenekleri
│   └── Tercihlerin kaydedilmesi ve hatırlanması
│
├── Tercihler sayfası erişimi
│   └── Herhangi bir sayfadaki çerez ayarları bağlantısı
│
└── Onay geri çekme mekanizması
    └── Tercihler sayfasından onay iptali

4. ÜÇÜNCÜ TARAF ÇEREZ BİLDİRİMİ
┌──────────┬──────────────────────────────────────┬──────────────────┐
│ Çerez Adı │ Gönderen                             │ Amacı             │
├──────────┼──────────────────────────────────────┼──────────────────┤
│ _ga       │ Google Analytics                    │ Analitik          │
│ _gid      │ Google Analytics                    │ Analitik          │
│ _fbp      │ Facebook Pixel                      │ Pazarlama         │
│ IDE       │ Google DoubleClick                   │ Pazarlama         │
│ li_sugr   │ LinkedIn Insight Tag                │ Analitik          │
│ _pinterest│ Pinterest Tag                       │ Pazarlama         │
└──────────┴──────────────────────────────────────┴──────────────────┘
```

## Pattern 4: Veri İşleme Açıklamaları Detay Matrisi

```
VERİ İŞLEME DETAY MATRİSİ (Her veri kategorisi için ayrı satır)
┌────────────────┬────────────────┬──────────────┬─────────────┬────────────┬──────────────────┐
│ Veri Kategorisi │ Toplama Yöntemi│ İşleme       │ Saklama     │ Aktarım   │ Hukuki          │
│                │               │ Amacı        │ Süresi      │           │ Dayanak         │
├────────────────┼────────────────┼──────────────┼─────────────┼────────────┼──────────────────┤
│ Ad, Soyad      │ Form girişi    │ Hizmet       │ Sözleşme    │ Yok       │ Sözleşme ifası  │
│                │               │ sunumu       │ süresi +3yıl│           │                │
├────────────────┼────────────────┼──────────────┼─────────────┼────────────┼──────────────────┤
│ E-posta adresi │ Üyelik form   │ Hesap yönetimi│ Hesap       │ E-posta  │ Sözleşme ifası  │
│                │               │              │ aktifken    │ sağlayıcısı│               │
│                │               │              │ +6 ay       │ (ABD)     │                │
├────────────────┼────────────────┼──────────────┼─────────────┼────────────┼──────────────────┤
│ IP adresi      │ Web sunucusu   │ Güvenlik     │ 12 ay       │ Yok       │ Meşru menfaat  │
│                │ otomatik      │              │             │           │ (güvenlik)     │
├────────────────┼────────────────┼──────────────┼─────────────┼────────────┼──────────────────┤
│ Cookie verileri │ Tarayıcı      │ Tercih       │ 13 ay       │ Google   │ Açık rıza       │
│                │ otomatik      │ hatırlama,   │             │ (ABD, SCC)│                │
│                │               │ analitik     │             │           │                │
├────────────────┼────────────────┼──────────────┼─────────────┼────────────┼──────────────────┤
│ Ödeme bilgileri│ Ödeme          │ Ödeme        │ Muhasebe    │ Ödeme    │ Hukuki yükümlülük│
│                │ geçidi (PSP)  │ işlemi       │ yükümlülüğü  │ sağlayıcısı│               │
│                │               │              │ süresi +5yıl │          │                │
├────────────────┼────────────────┼──────────────┼─────────────┼────────────┼──────────────────┤
│ Kredi kartı    │ Ödeme geçidi   │ Kredi kartı  │ İşlem sonrası│ Ödeme    │ Hukuki yükümlülük│
│ bilgileri      │ (PCI-DSS)     │ doğrulama    │ silme        │ sağlayıcısı│ (ödeme yasağı) │
└────────────────┴────────────────┴──────────────┴─────────────┴────────────┴──────────────────┘
```

## Key Patterns (Özet)

| Bölüm | İçerik | Zorunluluk |
|---|---|---|
| A | Veri sorumlusu tanımı | ✅ KVKK m. 10 zorunlu |
| B | Veri kategorileri | ✅ KVKK m. 10 zorunlu |
| C | İşleme amaçları ve hukuki dayanak | ✅ KVKK m. 10 zorunlu |
| D | Veri sahibi hakları | ✅ KVKK m. 11 + GDPR m. 15-22 |
| E | Veri aktarımı | ✅ KVKK m. 9 + GDPR m. 44-49 |
| F | Çerez ve izleme | ✅ e-Privacy Regulation / Çerez Kanunu |
| G | Veri güvenliği | ✅ KVKK m. 12 |
| H | Saklama süreleri ve imha | ✅ KVKK m. 7 + GDPR m. 5/1-e |

## Anti-Patterns

```
❌ GENEL VE MUĞLAK DİL KULLANIMI
   "Topladığımız bilgileri geliştirmek için kullanabiliriz" gibi
   ifadeler bilgi verme yükümlülüğünü karşılamaz.
   → Her veri kategorisi için spesifik amaç ve yöntem belirt.

❌ ÇEREZ POLİTİKASINI AYRI YAZMAMA
   Çerezler, site trafiği analizi ve pazarlama için yaygın
   kullanıldığından ayrı bir politika veya gizlilik politikasının
   alt bölümü olarak açıkça belirtilmelidir.
   → Çerez matrisini ayrı bir tablo ile sun.

❌ SAKLAMA SÜRESİ BELİRTMEME
   "Süresiz saklarız" veya hiç süre belirtmemek KVKK m. 7'ye aykırıdır.
   Her veri kategorisi için saklama süresi mutlaka belirtilmelidir.
   → Saklama süresini veri kategorisi bazında tablo formatında sun.

❌ VERİ AKTARIMI AÇIKLAMAMAMA
   ABD'ye veri aktarımı için Shield yeterli değil (Schrems II kararı).
   SCC veya yeterlilik kararı olmadan aktarım KVKK/GDPR'ya aykırıdır.
   → Üçüncü ülke aktarımları için ayrı bölüm ve SCC referansı ekle.

❌ VERİ SAHİBİ HAKLARINI EKSİK LİSTELEME
   KVKK m. 11'deki 6 hak eksik listelenirse politika yetersiz kabul edilir.
   → Tüm hakları numaralandırılmış liste olarak ver ve her biri için
      başvuru yöntemini açıkla.

✅ DOĞRU YAPI
   Veri sorumlusu bilgisi → Veri kategorileri → İşleme amaçları →
   Hukuki dayanaklar → Veri sahibi hakları → Aktarım bilgisi →
   Çerez tablosu → Güvenlik önlemleri → Saklama/İmha →
   Değişiklik prosedürü → İletişim bilgisi
```

## Quick Reference

| Öğe | Standart | Yasal Dayanak |
|---|---|---|
| Veri sorumlusu bilgisi | Tam unvan, adres, VKN, VRSKS | KVKK m. 10/1-a |
| Veri kategorileri | Her kategori için ayrı satır | KVKK m. 10/1-b |
| Saklama süreleri | Veri kategorisi bazlı | KVKK m. 7, GDPR m. 5/1-e |
| Başvuru yanıt süresi | 30 gün | KVKK m. 13/1, GDPR m. 12/3 |
| e-posta gönderim rızası | Açık onay (double opt-in önerilir) | ETK m. 5/1, Spamming Yasağı |
| Veri ihlali bildirimi | 72 saat (GDPR) / 72 saat (KVKK) | KVKK m. 12/5 |
| Çerez onayı | Açık kullanıcı onayı | e-Privacy Directive |
| Üçüncü ülke aktarımı | SCC veya yeterlilik kararı | KVKK m. 9, GDPR m. 46 |
| Politika güncelleme | 15-30 gün önceden bildirim | GDPR m. 13/4 |
| İmha prosedürü | 30-90 gün arası imha süresi | KVKK m. 7 |

---

*Uyarı: Bu şablon KVKK ve GDPR uyumluluğu için genel rehberlik sağlar. Gerçek bir gizlilik politikası, işletmenizin spesifik veri işleme faaliyetlerine göre özelleştirilmelidir. Büyük ölçekli veya hassas veri işleme faaliyetleri için profesyonel gizlilik danışmanlığı alınmalıdır.*


## 🌍 Universal Language Support
- **Turkish Native:** This skill natively supports Turkish. If the user prompt is in Turkish, all analysis, formatting, and output MUST be entirely in Turkish. You do not need explicit "write in Turkish" instructions.
