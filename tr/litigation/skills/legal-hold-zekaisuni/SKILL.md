---
name: legal-hold-zekaisuni
title: /legal-hold
description: Şirket içi kayıt/delil muhafaza talimatı yayımlar, yeniler, kaldırır veya raporlar — .docx formatında iç bildirim taslağı hazırlar, _log.yaml'deki legal_hold alanlarını günceller ve bir sonraki yenileme tarihini kaydeder. Aynı zamanda HMK m.400 uyarınca Delil Tespiti hazırlığı için çerçeve sunar. Kullanıcı "muhafaza talimatı gönder", "delil tespitine hazırla" veya portföy çapında "muhafaza durumu raporu" istediğinde kullanın.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/litigation-legal/skills/legal-hold
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: litigation
language: tr
---

# /legal-hold

1. Eğer `--status` ise (kısa ad yoksa): `_log.yaml` dosyasını oku, portföy çapında muhafaza/tespit durum raporu üret.
2. Aksi takdirde: `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[kisa-ad]/matter.md` ve log satırını yükle.
3. `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` yükle → gizlilik işaretleri, muhafaza şablonu işaretçisi, eskalasyon kuralları.
4. Aşağıdaki iş akışını ve referansları izle.
5. Bayrağa (flag) göre yönlendir:
   - `--issue`: Kapsam, ilgili kişiler (custodians), tarih aralığı, sistemleri topla. `legal-hold-v1.docx` (Şirket İçi Saklama Talimatı) taslağını oluştur. `legal_hold` alanlarını güncelle. Tarihçe dosyasına girdi ekle. `next_refresh` ayarla (varsayılan +6 ay).
   - `--refresh`: Kapsam/kişi değişikliklerini yakala. Sonraki versiyon taslağını oluştur. `last_refresh` + `next_refresh` güncelle. İşten ayrılan kişileri belirgin şekilde işaretle.
   - `--release`: Kaldırma tarihi, muhafaza sonrası silme talimatı. Kaldırma bildirimi (release notice) taslağı oluştur. `released:` alanını ayarla.
6. Yazmadan önce onayla. Kullanıcıya taslak bildirimi ve log farkını (diff) göster.

---

# Kayıt/Delil Muhafaza (Legal Hold / Retention)

## Amaç

ABD Hukukunda "Legal Hold" doğrudan bir zorunluluk (spoliation) iken; Türk Hukukunda süreç daha çok **şirket içi kurumsal veri saklama politikasının (retention)** işletilmesi, **KVKK m.7 veri imha yükümlülüğünün uyuşmazlık nedeniyle durdurulması** ve gerekirse **HMK m.400 uyarınca mahkemeden Delil Tespiti** istenmesi şeklinde yürür.
Hatalı işleyişler operasyoneldir: İlgili IT/İK birimine çok geç haber verilmesi, e-postaların rutin rotasyonla silinmesi, çok dar kapsam tutulması veya davanın bitmesine rağmen verilerin sonsuza dek tutulması (KVKK ihlali). Bu beceri tüm evreleri yönetir: **yayımla → yenile → (kaldır) → takip et**.

Portföy zaten eksik bildirimleri işaretler; bu beceri onları yazar.

## Yargı Alanı Varsayımı (Jurisdiction assumption)

Muhafaza yükümlülükleri ülkeye göre değişir. ABD'deki (Zubulake kararı, Rule 37e) katı "spoliation" kuralları yerine, Türk hukukunda **HMK m. 220 (Belge ibrazından kaçınma halinde karşı tarafın iddiasının doğru kabul edilmesi ihtimali)** ve **TCK m. 281 (Suç delillerini yok etme)** kuralları uygulanır. Ayrıca verilerin saklanabilmesi için KVKK m. 5 "Bir hakkın tesisi, kullanılması veya korunması" istisnasına dayanılır.

## Bağlamı Yükle

- `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` — log satırı (legal_hold alanları + durum)
- `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[kisa-ad]/matter.md` — dosya bağlamı (karşı taraf, olaylar, iç sorumlular)
- `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` — şablon işaretçisi, eskalasyon normları

**Güvenlik Kapısı (Gate).** Bir talimat yayımlamadan önce, `_log.yaml`'da kısa adın (slug) olup olmadığını kontrol et. Eğer yoksa reddet:

> "Dosya günlüğünde [kısa ad] bulamıyorum. Önce `/litigation-legal:matter-intake` çalıştırın ki dosya kurulsun. Kaydedilmemiş (intake yapılmamış) bir dosya için talimat/bildirim yayımlamam."

## Modlar (Modes)

Komut bir argüman alır: `--issue | --refresh | --release | --status`. Varsayılan (boş) → sor.

### `--issue` — İlk Bildirim (First issuance)

`legal_hold.issued == false` olduğunda ve uyuşmazlık aktif veya öngörülebilir olduğunda gerekir.

**Yayımlamadan Önce Onay:** Hukukçu olmayan bir rolse:
> Şirket içi saklama talimatı göndermenin operasyonel sonuçları vardır (KVKK yükümlülüklerinin askıya alınması, veri depolama maliyetleri). Bunu bir avukatla veya IT/KVKK yöneticinizle görüştünüz mü? Evet ise devam edin. Değilse, onlara sunacağınız bir özet:
> [1 sayfalık özet üret]

> **Dış Teslimat Notu:** Bu bildirim iç çalışanlara (custodians) ve IT/İK departmanlarına gider. Dışarı giden bildirimde `AVUKAT-MÜVEKKİL GİZLİLİĞİ` gibi iç başlıkları kullanmayın. 

**Girdiler:**
1. **Kapsam** — Sözleşmeler, e-postalar, finansal kayıtlar. (Çok geniş olursa IT yükü artar; çok dar olursa deliller yok olabilir).
2. **Kişiler (Custodians)** — Kayıtları elinde bulunduran isimler. (Dosyadan öner; Satış sorumlusu, İK partneri, CISO vb.)
3. **Tarih aralığı** — Hangi tarihten itibaren saklanacak.
4. **Sistemler** — Outlook, KEP, Slack/Teams, yerel bilgisayarlar, ortak diskler.
5. **Geçerlilik tarihi** — Talimat tarihi.

**Talimat Taslağını Yaz** (Eğer `CLAUDE.md` içinde şablon varsa onu kullan, yoksa aşağıdaki varsayılan Türk hukuku taslağını kullan).

**Varsayılan Şirket İçi Muhafaza Talimatı Şablonu:**

```
GİZLİ — İÇ YAZIŞMADIR

TARİH: [geçerlilik tarihi]
KİME: [kişi ismi / departman]
KİMDEN: [imzalayan — CLAUDE.md varsayılanına göre]
KONU: ŞİRKET İÇİ VERİ VE KAYIT SAKLAMA TALİMATI — [dosya kısa adı]

Bu bildirimi alıyorsunuz çünkü Şirketimiz, [uyuşmazlığın kısa bir cümlesi, yargılayıcı detaya girmeden] konusuyla ilgili hukuki bir süreçle karşı karşıyadır/süreci başlatacaktır. Olası bir yargılama veya inceleme nedeniyle ilgili bilgi ve belgelerin güvenli bir şekilde saklanması ve silinmemesi hukuki bir zorunluluktur. (HMK m. 220 ve KVKK m. 5/2-e "bir hakkın kullanılması/korunması" kapsamında).

DERHAL GEÇERLİ OLMAK ÜZERE, aşağıdakileri saklamalısınız:

1. [kapsam 1] ile ilgili tüm belgeler, e-postalar, Slack/Teams/WhatsApp mesajları,
2. [kapsam 2]
3. [kapsam 3]
...

Bu muhafaza yükümlülüğü şu sistemleri kapsar:
- E-posta hesapları (silinmiş öğeler dahil)
- Şirket telefonlarındaki mesajlaşma uygulamaları
- Ortak klasörler, OneDrive/Google Drive
- KEP (Kayıtlı Elektronik Posta) geçmişi
- Basılı/fiziki evraklar

YAPILMAMASI GEREKENLER:
- Potansiyel olarak ilgili hiçbir materyali SİLMEYİN, DEĞİŞTİRMEYİN veya İMHA ETMEYİN.
- Rutin "arşiv temizliği" veya otomatik silme (auto-delete) süreçlerini bu veriler için DURDURUN (Bilişim Teknolojileri departmanı ile koordine olun).

Bu bildirimle veya yükümlülüklerinizle ilgili sorularınızı doğrudan [hukuk irtibat kişisi]'ne iletin. Uyuşmazlığın kendisini veya hukuki stratejiyi şirket içinde yetkisiz kişilerle TARTIŞMAYIN.

BİR ŞEYİN KAPSAMDA OLUP OLMADIĞINDAN EMİN DEĞİLSENİZ, SİLMEK YERİNE SAKLAMAYI TERCİH EDİN.

Lütfen bu bildirimi aldığınızı [yanıt/link] yoluyla 3 iş günü içinde teyit edin. Bu bildirim, size kaldırıldığına dair yazılı bilgi verilene kadar geçerlidir.

[İmza bloğu]
```

**Yazılanlar:**
- `matters/[kisa-ad]/legal-hold-v1.docx`
- `history.md` günlüğü
- `_log.yaml` güncel satırı:
  ```yaml
  legal_hold:
    issued: true
    issued_date: [YYYY-MM-DD]
    scope: "[kısa özet]"
    custodians: [liste]
    last_refresh: [YYYY-MM-DD]
    next_refresh: [YYYY-MM-DD]   # varsayılan: + 6 ay
    released: null
  ```

### `--refresh` — Periyodik Yenileme

Dava uzun sürerse (Türkiye'de yıllar alabilir), saklama talimatının unutulmaması için yenilenmesi.
- Kapsam değişikliği var mı?
- İşten ayrılan personel var mı? (Ayrılan personelin e-postası veya bilgisayarı IT tarafından imha edilmeden yedeklenmeli — çok kritik KVKK/Delil kesişim noktası).

### `--release` — Muhafazayı Kaldır (Release)

Dava kesinleştiğinde veya risk kalktığında. KVKK gereği gereksiz yere kişisel verilerin veya eski kayıtların tutulmaması için çok önemlidir.

- Kaldırma onayı.
- Kaldırma sonrası IT/İK'ya ne olacağı talimatı (Rutin imha politikasına dön? Fiziki arşive gönder?)

### `--status` — Portföy Çapında Rapor

`_log.yaml` oku. Rapor üret:

```markdown
# Kayıt/Delil Saklama Durumu — [bugün]

## Aktif Muhafazalar

| Dosya | Yayımlanma | Son Yenileme | Sonraki Yenileme | Kişiler | Durum |
|---|---|---|---|---|---|
| [kisa-ad] | [tarih] | [tarih] | [tarih] | [N] | [ok / ⚠️ yenileme / ❌ gecikti] |

## ⚠️ Dikkat (Gecikmiş, KVKK Riski)

- **Yenilemesi gecikmiş:** [liste]
- **Kayıt altına alınmış ama muhafaza talimatı YAYIMLANMAMIŞ dosyalar:** [liste — delil kaybı riski]
- **Kapanmış ama talimatı KALDIRILMAMIŞ dosyalar:** [liste — KVKK imha yükümlülüğü ihlal riski]
```

## Bu Becerinin Yapmadığı Şeyler

- **Fiilen verileri kopyalamaz veya saklamaz.** IT departmanına talimat yazar.
- **Kapsama tek başına karar vermez.**
- Mahkemeden *fiilen* Delil Tespiti Kararı çıkartmaz. (Bu, ayrı bir dava şartıdır; beceri sadece avukata "Bu dosyada HMK m.400 uygulayalım mı?" sorusunu sorarak hatırlatır).
