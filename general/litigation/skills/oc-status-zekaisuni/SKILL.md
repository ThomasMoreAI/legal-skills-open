---
name: oc-status-zekaisuni
title: /oc-status (Dış Hukuk Bürosu Safahat Durumu)
description: Tüm aktif portföydeki dış hukuk bürolarına gönderilmek üzere haftalık/aylık durum (safahat) talep e-postası taslakları oluşturur — her dosya için markdown formatında ve (eğer MCP aktifse) Gmail taslağı olarak. Kullanıcı "dış bürolardan safahat iste", "haftalık raporları hazırla" veya portföy günlüğünden (log) dosya bazlı e-posta taslakları istediğinde kullanın.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/litigation-legal/skills/oc-status
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: tr
---

# /oc-status (Dış Hukuk Bürosu Safahat Durumu)

Haftalık çalıştırmak için `/litigation-legal:oc-status` komutunu anımsatıcıya ekleyin. Otomatik zamanlama (scheduling) eklentide yerleşik değildir.

1. `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` dosyasını yükle, kurallara göre filtrele.
2. `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` yükle → dış büro iletişim dili, imza varsayılanları, bütçe/avans duruşu.
3. Aşağıdaki iş akışını ve referansları izle.
4. Kapsamdaki her dosya için: `matter.md` + `history.md` oku, dosyaya özel e-posta taslağı hazırla.
5. Markdown'ı buraya yaz: `~/.claude/plugins/config/claude-for-legal/litigation-legal/oc-status/[YYYY-MM-DD]/[slug].md`.
6. Gmail MCP yetkilendirilmişse: Gmail taslakları oluştur. Değilse: Sadece markdown oluştur ve özette belirt.
7. Özet raporunu yaz `~/.claude/plugins/config/claude-for-legal/litigation-legal/oc-status/[YYYY-MM-DD]/_summary.md` — ne çalıştı, ne atlandı ve neden.

---

# Dış Hukuk Bürosu Safahat (OC Status)

## Amaç

5–15 dava dosyası için her hafta/ay dış hukuk bürosuna (outside counsel) aynı safahat talep e-postasını yazmak mekanik bir zihinsel yüktür. Dosya başına içerik tutarlıdır (son durum, kararlar, masraf/avans durumu). Hedef kitle tutarlıdır (ilgili dosya avukatı / sorumlu ortak). Ton tutarlıdır. Bu beceri, tüm taslakları hazırlar; şirket avukatı sadece inceler ve gönderir.

## Bağlamı Yükle

- `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` — filtreleme ve alan kaynağı
- `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[slug]/matter.md` — dosya bağlamı (mevcut aşama, açık sorular)
- `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[slug]/history.md` — ne sorulacağını belirlemek için son olaylar
- `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → kurumsal iletişim dili, imza sahibi, bütçe/masraf avansı duruşu

## Filtreleme — Hangi dosyalar?

Varsayılan filtre:

- `status != kapali` (Aktif davalar)
- `outside_counsel.firm != null` VE `outside_counsel.lead != null` (Dış büroya verilmiş olanlar)
- İkisinden biri: son güncelleme 10 günden eski VEYA 21 gün içinde bir `next_deadline` (kesin süre / duruşma) var.

Son 10 gün içinde zaten güncellenmiş (tekrar dürtmeye gerek olmayan) dosyaları ve log'da dış büro e-postası (`outside_counsel.email`) olmayanları atlar (ancak e-posta yoksa da markdown üretilir, sadece Gmail'e atılmaz).

Bayraklar:
- `--all` → güncelliğine bakılmaksızın tüm aktif dosyalar için taslak oluştur
- `--slug=[kisa_ad]` → sadece tek bir dosya için taslak oluştur (ad-hoc talep)
- `--no-gmail` → MCP olsa bile Gmail taslağı oluşturmayı atla

## Dosya Bazlı E-posta Taslağı

Her e-postanın iskeleti aynıdır; içerik dosyaya özeldir.

**Konu (Subject):** Kurumsal geleneğe göre (`CLAUDE.md` içinden alınır; yoksa: `[Dosya: [dosya adı]] — Safahat ve Durum Güncellemesi Talebi`)

**Gövde İskeleti:**

```
Sayın [Sorumlu Avukat / Büronun Adı],

[Doğal, şirket kültürüne uygun bir giriş cümlesi. Örn: "İyi haftalar/çalışmalar dilerim."]

[Dosya Adı] dosyasıyla ilgili durumu kontrol etmek istedim. Birkaç konumuz var:

1. **[history.md'deki son güncelleme tarihi]'nden bu yana Safahat** — UYAP'a yansıyan yeni bir evrak, bilirkişi raporu, tebligat veya karar var mı? Son görüşmemizden bu yana karşı tarafla veya mahkemeyle bir temas oldu mu?

2. **Yaklaşan Süreler ve Duruşmalar** — Kayıtlarımda [log'dan next_deadline + matter.md'deki süreler] görünüyor. Duruşmaya katılım durumunuzu ve beyan dilekçesi planımızı teyit edelim. Eklememiz gereken başka bir kesin süre var mı?

3. **Bekleyen Kararlar/Sorular** — [matter.md'den dış büronun girdisini gerektiren açık soruları çekin; yoksa bu maddeyi atlayın ve numaralandırmayı düzeltin]

4. **Masraf / Avans Durumu** — [Aylık / Üç aylık / CLAUDE.md bütçe duruşuna göre]. Harç, bilirkişi veya gider avansı için şirketimizden beklediğiniz bir ödeme var mı? [matter.md'den ayrılan bütçe varsa durumunu sorun].

[Eğer maddi ve gerekliyse: 5. Özel Talep — Örn: "Cevaba cevap dilekçesi taslağını [tarih] tarihine kadar iletmenizi rica ederim" — matter.md'deki açık sorulardan çekin.]

[Kapanış — isim, unvan, iletişim. `CLAUDE.md` içindeki imza varsayılanından.]
```

Tonu `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` dış büro iletişim stiline göre ayarlayın — bazı şirketler "Sayın Avukat" şeklinde resmidir, bazıları "Merhaba [İlk İsim]". Uyarlayın.

## Çıktı

### Markdown Taslakları

Yazılacak yer: `~/.claude/plugins/config/claude-for-legal/litigation-legal/oc-status/[YYYY-MM-DD]/[slug].md`

Her dosya bir e-postadır, şu formatta olur:

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — Eklenti ayarları ## Çıktılar bölümüne göre; bkz. `## Bunu Kim Kullanıyor`]

# [Dosya adı] — Dış Büro Safahat Talebi — [YYYY-MM-DD]

**Kime:** [log'dan outside_counsel.email] ([outside_counsel.lead], [outside_counsel.firm])
**Kimden:** [signer name / email `CLAUDE.md` üzerinden]
**Konu:** [konu satırı]

> Üstteki İş-Ürünü başlığı bu iç kayıt içindir. Aşağıdaki e-posta gövdesi, vekalet ilişkisi kurulan dış hukuk bürosuna gideceğinden, gönderilen e-postanın en üstüne kurumun gizlilik ibaresini (`Avukat-Müvekkil Gizliliği Kapsamındadır`) ekleyin.

---

[iskelete uygun gövde]
```

### Gönderim Kapısı (Her taslaktaki kapanış notu)

Aşağıdaki metni her markdown taslağının sonuna ekleyin (göndermeden önce silinmesi için):

> Bu, dış büroya gönderilmeden önce avukatın incelemesi için hazırlanmış bir taslaktır. Vekalet ilişkisi (engagement circle) dışına çıkmasını istemediğiniz stratejik bilgilerin (şirket sırları vs.) veya sert bir dilin yanlışlıkla e-postada kalıp kalmadığını kontrol edin. Rutin bir haftalık e-posta bile gönderenin niyet etmediği bir tavizi yazılı hale getirebilir. İncelemeden göndermeyin.

### Gmail Taslakları (MCP Varsa)

Eğer Gmail taslak oluşturma MCP'si yetkilendirilmişse:

- Kullanıcının Gmail'inde her dosya için `to`, `from`, `subject`, `body` (kime, kimden, konu, gövde) doldurulmuş bir taslak oluştur.
- Taslak Gmail "Taslaklar" klasöründe durur; kullanıcı Pazartesi sabahı inceler ve gönderir.
- Gmail MCP'si YOKSA veya hata verirse: Sadece markdown oluşturmaya geri dön (fallback) ve kullanıcıya bildir.

### Çalıştırma Özeti (Run summary)

Tüm dosyalar işlendikten sonra `~/.claude/plugins/config/claude-for-legal/litigation-legal/oc-status/[YYYY-MM-DD]/_summary.md` dosyasını yazın:

```markdown
# Dış Büro (OC) Safahat Çalıştırması — [YYYY-MM-DD]

**İşlenen Dosyalar:** [N]
**Oluşturulan Taslaklar:** [N]
**Gmail Taslakları:** [oluşturuldu / atlandı — neden]

## Taslak Hazırlananlar

| Dosya | Dış Büro (Sorumlu) | Son Güncelleme | Dahil Edilme Nedeni |
|---|---|---|---|
| [slug] | [lead] | [tarih] | [hareketsiz / yaklaşan duruşma / --all / --slug] |

## Atlananlar (Skipped)

| Dosya | Neden |
|---|---|
| [slug] | yakın zamanda güncellendi (son işlem [tarih]) |
| [slug] | log'da büro e-postası yok — `/matter-update [slug]` ile güncelleyin |

## Anomaliler

- Dış hukuk bürosu atanmamış dosyalar: [liste — yüksek/kritik riskli olanlar bayraklanır]
- Dış büro atanmış ama log'da e-postası olmayan dosyalar: [liste]
```

## Zamanlama (Scheduling)

Bu beceri haftalık çalıştırılmak üzere tasarlanmıştır. `/litigation-legal:oc-status` komutunu takviminize bir anımsatıcı (Örn: Pazartesi sabahı) olarak ekleyebilirsiniz.
Ad-hoc: İstenildiği zaman `/oc-status` çalıştırılabilir. Tek bir dosya için `/oc-status --slug=foo`.

## Bu Becerinin YAPMADIĞI Şeyler

- **E-postaları fiilen GÖNDERMEZ.** Sadece taslakları hazırlar. Avukat inceler ve gönder tuşuna basar.
- **Sahip olmadığı bir içeriği uydurmaz.** Eğer `matter.md` zayıfsa, e-posta kısa olur ve genel safahat sorar. Yoktan spesifik sorular icat etmez.
- **Hataları tekrar denemez (Retry).** Gmail yetkilendirmesi koparsa, hatayı loglar ve markdown üreterek devam eder. Kullanıcı yetkiyi düzeltip tekrar çalıştırabilir.
- **history.md dosyasını GÜNCELLEMEZ.** Sadece okur. (Dış büro cevap verdiğinde, UYAP gelişmelerini kaydetmek için `/matter-update [slug]` kullanın.)
- **Zorunlu bir şablon dayatmaz.** Eğer kurumun tarzı "Tek satır, ismini yaz, bitir" şeklindeyse, taslak buna uyar ve uzun madde işaretlerini atlar.
