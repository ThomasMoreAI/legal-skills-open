# Türkiye Regulatory Source Catalog

Bu katalog `reg-feed-watcher` için başlangıç listesidir. Kaynak URL'leri Mayıs 2026 itibarıyla resmi alan adlarından kontrol edilmiştir; kurum siteleri duyuru yapısını değiştirebilir. Bir kaynak çalışmazsa URL'yi kurum sitesinden yeniden doğrulayın.

## Okuma Kılavuzu

- **Birincil kaynak:** Resmi Gazete, Mevzuat Bilgi Sistemi veya düzenleyici kurumun kendi sitesi.
- **İkincil kaynak:** Hukuk bürosu bülteni, haber, newsletter, ticari veri tabanı özeti. Bunlar lead üretir; işlemden önce birincil kaynağa gidilir.
- **Format:** JSON/API, RSS, HTML, PDF, e-posta veya manuel.

## Genel Resmi Kaynaklar

| Kaynak | URL | Format | Kapsam | Not |
|---|---|---|---|---|
| Resmi Gazete | `https://www.resmigazete.gov.tr/` | HTML/PDF | Kanun, yönetmelik, tebliğ, karar, kurul kararları | Bağlayıcı yayımların ilk kontrol noktası. |
| Mevzuat Bilgi Sistemi | `https://www.mevzuat.gov.tr/` | HTML | Konsolide yürürlükteki mevzuat | Yürürlükteki metin ve değişiklik kontrolü için kullan. |
| Cumhurbaşkanlığı Mevzuat / e-Mevzuat bağlantıları | `https://www.mevzuat.gov.tr/` | HTML | Kanun, CBK, yönetmelik, tebliğ | Resmi Gazete metniyle birlikte doğrula. |

## Kurum Kaynakları

| Kurum | URL | Format | Kapsam | Not |
|---|---|---|---|---|
| KVKK | `https://www.kvkk.gov.tr/` | HTML | Kurul kararları, ilke kararları, rehberler, veri ihlali duyuruları | Kurul kararları ve rehberler için birincil kaynak. |
| Rekabet Kurumu | `https://www.rekabet.gov.tr/` | HTML/PDF | Kurul kararları, duyurular, kılavuzlar, soruşturmalar | Kararlar ve kılavuzlar sektör etkisi bakımından izlenir. |
| SPK | `https://www.spk.gov.tr/` | HTML/PDF | Tebliğler, ilke kararları, bültenler, idari yaptırımlar | SPK Bülteni ayrı takip edilebilir. |
| BDDK | `https://www.bddk.org.tr/` | HTML/PDF | Kurul kararları, yönetmelikler, duyurular | Bankacılık/fintech uyumu için ana kaynak. |
| BTK | `https://www.btk.gov.tr/` | HTML/PDF | Elektronik haberleşme, internet, tüketici, yetkilendirme | Duyuru ve kurul kararları takip edilir. |
| EPDK | `https://www.epdk.gov.tr/` | HTML/PDF | Enerji piyasası kararları, lisans, tarifeler, duyurular | Sektör etkisi yüksek olabilir. |
| TCMB | `https://www.tcmb.gov.tr/` | HTML/PDF | Ödeme sistemleri, finansal piyasa duyuruları, düzenlemeler | Ödeme/finans ekipleri için izlenir. |
| Ticaret Bakanlığı | `https://ticaret.gov.tr/` | HTML/PDF | Tüketici, e-ticaret, reklam, gümrük, dış ticaret duyuruları | Reklam Kurulu ve tüketici tarafı için önemli. |
| MASAK | `https://masak.hmb.gov.tr/` | HTML/PDF | AML/CFT rehberleri, duyurular, mevzuat | Finans, kripto ve yükümlü gruplar için izlenir. |
| TİTCK | `https://www.titck.gov.tr/` | HTML/PDF | İlaç, tıbbi cihaz, kozmetik duyuruları ve mevzuat | Sağlık/life sciences için ana kaynak. |
| Çalışma ve Sosyal Güvenlik Bakanlığı | `https://www.csgb.gov.tr/` | HTML/PDF | İş hukuku, İSG, sosyal güvenlik duyuruları | HR/compliance izleme listesine eklenebilir. |
| SGK | `https://www.sgk.gov.tr/` | HTML/PDF | Sosyal güvenlik genelgeleri ve duyurular | Bordro/HR süreçleri için. |
| Kamu İhale Kurumu | `https://www.ihale.gov.tr/` | HTML/PDF | Kamu ihale mevzuatı ve kurul kararları | Kamu ile iş yapan şirketler için. |

## İkincil / Yardımcı Kaynaklar

| Kaynak türü | Örnek | Kullanım |
|---|---|---|
| Hukuk bürosu müşteri bültenleri | Firma duyuruları/newsletter | Gelişme yakalamak için; birincil kaynağa dönmeden uyum sonucu çıkarma. |
| Ticari hukuk veri tabanları | Lexpera, Kazancı, Legalbank vb. | Mevzuat ve karar araştırmasını destekler; erişim kullanıcı aboneliğine bağlıdır. |
| Sektör birlikleri | TBB, TSPB, TOBB, TÜSİAD, DEİK vb. | Sektör görüşleri ve taslak değerlendirmeleri için lead kaynağı. |
| KAP/MKK/Borsa İstanbul | `https://www.kap.org.tr/`, `https://www.mkk.com.tr/`, `https://www.borsaistanbul.com/` | Sermaye piyasası duyuru ve piyasa altyapısı takibi. |

## Başlangıç Paketleri

**Genel şirket compliance:**
Resmi Gazete, Mevzuat, KVKK, Rekabet, Ticaret Bakanlığı, ilgili sektör kurumu.

**Fintech / finans:**
Resmi Gazete, Mevzuat, TCMB, BDDK, MASAK, SPK, KVKK, Rekabet.

**Telekom / internet / SaaS:**
Resmi Gazete, Mevzuat, BTK, KVKK, Rekabet, Ticaret Bakanlığı.

**Enerji:**
Resmi Gazete, Mevzuat, EPDK, Rekabet, Ticaret Bakanlığı.

**Sağlık / life sciences:**
Resmi Gazete, Mevzuat, TİTCK, KVKK, Rekabet, Sağlık Bakanlığı.

## Kaynak Ekleme

1. Kurumun resmi sitesinde duyuru/karar/mevzuat sayfasını bul.
2. RSS/API yoksa HTML sayfa izleme veya manuel giriş olarak kaydet.
3. `CLAUDE.md -> Feed configuration` tablosuna kurum, URL/metot, format ve kapsam ekle.
4. İkincil kaynak ise `[ikincil kaynak]` etiketi zorunludur.
