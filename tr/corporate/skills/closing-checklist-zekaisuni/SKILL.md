---
name: closing-checklist-zekaisuni
title: /closing-checklist
description: Türk M&A işlemleri için kapanış checklist'i oluşturur ve günceller. Pay devri, malvarlığı devri, birleşme, bölünme, tür değiştirme, yatırım ve JV işlemlerinde imza/kapanış koşulları, organ kararları, ticaret sicili/MERSİS, Rekabet Kurumu, SPK/KAP/MKK, sözleşme onayları, teminat fekki, KVKK, ruhsat, vergi/SGK ve kapanış belgelerini izler. "closing checklist", "kapanış listesi", "kapanışta ne kaldı", "CP status", "checklist status" isteklerinde kullanılır.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/corporate-legal/skills/closing-checklist
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: tr
practice: corporate
language: tr
---

# /closing-checklist

## Amaç

Bu skill, Türk M&A ve şirket işlemleri için kapanış checklist'i tutar. Due diligence bulgularından, işlem sözleşmesinden, disclosure schedule'dan ve deal-team notlarından gelen kapanış aksiyonlarını tek listede toplar; neyin kapanışı engellediğini, kimin sorumlu olduğunu ve hangi belgenin kanıt olarak beklendiğini gösterir.

Çıktı bir kapanış sertifikası veya "işlem kapanabilir" hukuki görüşü değildir. Avukat/hukukçu incelemesine tabi çalışma listesidir.

## Bağlamı yükle

1. `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` dosyasını oku.
2. Varsa `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/deal-context.md` dosyasını oku.
3. Checklist dosyası varsa oku:
   `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/closing-checklist.yaml`
4. Matter workspace açıksa aktif matter `matter.md` dosyasını oku; başka matter dosyasına kullanıcı açıkça istemedikçe bakma.

İşlem kodu veya checklist yoksa kısa sor:

- İşlem türü nedir: pay devri, malvarlığı devri, birleşme, bölünme, tür değiştirme, yatırım, JV?
- İmza tarihi ve hedef kapanış tarihi var mı?
- İşlem sözleşmesi veya kapanış listesi taslağı var mı?
- Hangi taraftayız: alıcı, satıcı, hedef şirket, yatırımcı?

## Checklist dosyası

Yol:

`~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/closing-checklist.yaml`

Şema:

```yaml
deal_code: "[İşlem kodu]"
transaction_type: "[pay devri | malvarlığı devri | birleşme | bölünme | tür değiştirme | yatırım | JV | diğer]"
side: "[alıcı | satıcı | hedef | yatırımcı | grup şirketi]"
signing_date: "[YYYY-MM-DD veya belirsiz]"
target_close: "[YYYY-MM-DD veya belirsiz]"
last_updated: "[YYYY-MM-DD]"

items:
  - id: "CP-001"
    item: "Rekabet Kurumu izin/bildirim değerlendirmesi"
    category: "Regulatory"
    phase: "pre-closing"
    responsible: "Hukuk / dış danışman"
    due: "[YYYY-MM-DD veya belirsiz]"
    status: "not_started | in_progress | waiting_counterparty | waiting_authority | complete | waived | post_closing | blocked | unknown"
    blocking: true
    evidence_required: "Kurul izni/görüşü, başvuru kaydı veya dış danışman notu"
    source: "İşlem sözleşmesi m. [ ] / DD bulgusu / kullanıcı sağladı"
    notes: ""

  - id: "CD-001"
    item: "Hedef şirket imza sirküleri ve temsil yetkisi kontrolü"
    category: "Corporate"
    phase: "signing"
    responsible: "Hedef şirket / hukuk"
    due: "[YYYY-MM-DD veya belirsiz]"
    status: "in_progress"
    blocking: true
    evidence_required: "Güncel imza sirküleri, iç yönerge veya yetki belgesi"
    source: "VDR / Kurumsal kayıtlar"
    notes: ""
```

## Modlar

- Checklist yoksa veya kullanıcı işlem sözleşmesi verdiyse: Mode 1 - initialize.
- Upstream bulgu veya handoff varsa: Mode 2 - ingest.
- Kullanıcı item güncellemesi verdiyse: Mode 3 - status update.
- Aksi halde: Mode 4 - status report / what's blocking.

## Mode 1 - İşlem sözleşmesinden başlat

İmzalanmış veya near-final işlem sözleşmesini oku. Başlık adı değişebilir; madde numarasına değil fonksiyona bak:

- kapanış koşulları,
- imza ve kapanış belgeleri,
- kapanış öncesi taahhütler,
- tescil/ilan, izin ve bildirim yükümlülükleri,
- üçüncü kişi onayları,
- beyan/garanti bring-down, MAC/MAE veya önemli olumsuz değişiklik koşulları,
- ödeme, escrow, holdback, fiyat düzeltmesi,
- post-closing olarak bırakılan işler.

Her koşul veya teslim belgesi için checklist item oluştur. Kaynak maddeyi belirt; belge yoksa kullanıcı beyanı olarak etiketle.

### Türkiye kapanış kategorileri

Varsayılan kategoriler:

- **Corporate:** organ kararları, genel kurul/yönetim kurulu/müdürler kurulu kararları, pay defteri, karar defteri, imza sirküleri, iç yönerge, vekaletname.
- **Registry:** ticaret sicili tescil/ilan, MERSİS, TTSG, unvan/merkez/sermaye/yönetim/temsil değişiklikleri.
- **Regulatory:** Rekabet Kurumu, SPK, KAP, MKK, BDDK, BTK, EPDK, Sağlık Bakanlığı, Ticaret Bakanlığı veya sektör izinleri.
- **Contracts:** sözleşme devri, karşı taraf onayı, kontrol değişikliği bildirimi, fesih/yenileme, teminat/kefalet/garanti.
- **Finance:** fon akışı, escrow/holdback, borç kapama, payoff, rehin/ipotek/haciz fekki, teminat mektubu.
- **Tax/Accounting:** damga vergisi, KDV/stopaj, fatura, muhasebe kapanış, vergi borcu veya inceleme evrakı.
- **Employment/SGK:** çalışan devri, işyeri devri, SGK kayıtları, kilit çalışan belgeleri, ibra/feragat riski.
- **KVKK/Data:** veri aktarımı, veri işleme sözleşmesi, yurt dışına aktarım, entegrasyon erişimleri, VERBİS/KVKK kayıtları.
- **IP/Tech:** marka/patent/yazılım devirleri, lisans onayları, alan adı, açık kaynak remediation.
- **Real Estate/Licenses:** tapu, kira, ruhsat, çevre, işyeri açma, üretim veya işletme izinleri.
- **Disputes:** dava/icra/tahkim/arabuluculuk, sulh, feragat, teminat, ihtiyati tedbir/haciz.

### Hukuki güncellik

Rekabet Kurumu eşikleri, SPK/KAP/MKK yükümlülükleri, sektör izinleri, tescil formaliteleri, vergi/SGK sonuçları veya resmi süreler güncel kaynak gerektirir. Resmi kaynak veya dış danışman notu yoksa item'ı `unknown` veya `needs_verification` olarak bırak; takvim varsayımı uydurma.

MAC/MAE veya "önemli olumsuz değişiklik" koşullarını işlem sözleşmesindeki tanıma göre takip et. Türk hukukunda veya yabancı hukukta yorum ayrı olabilir; governing law ve dış danışman kontrolü olmadan "tetiklendi/tetiklenmedi" sonucuna varma.

## Mode 2 - Due diligence ve schedule handofflarını işle

Şu upstream çıktıları oku:

- `diligence-issue-extraction` bulguları,
- `material-contract-schedule` sözleşme devri/kontrol değişikliği/onay maddeleri,
- `deal-team-summary` kritik aksiyon özeti,
- dış danışman closing listesi veya e-posta notu.

Handoff şeması:

```yaml
handoff:
  item: "[Tek satır aksiyon]"
  category: "[Corporate | Registry | Regulatory | Contracts | Finance | Tax/Accounting | Employment/SGK | KVKK/Data | IP/Tech | Real Estate/Licenses | Disputes]"
  phase: "[signing | pre-closing | closing | post-closing]"
  source: "[Sözleşme maddesi / VDR yolu / DD bulgusu / kullanıcı sağladı]"
  blocking: true
  severity: "[Kırmızı | Sarı | Yeşil]"
  responsible: "[kişi/ekip/dış danışman]"
  evidence_required: "[hangi belgeyle tamam sayılacak]"
  due: "[YYYY-MM-DD veya belirsiz]"
  notes: ""
```

Kapanış listesine eklenecek tipik handofflar:

- Rekabet Kurumu, SPK/KAP/MKK veya sektör izni/bildirimi,
- ticaret sicili tescil/ilan, MERSİS veya TTSG aksiyonu,
- yönetim kurulu, müdürler kurulu, genel kurul veya pay sahibi kararı,
- imza sirküleri, iç yönerge, temsil yetkisi veya vekaletname düzeltmesi,
- sözleşme devri, kontrol değişikliği bildirimi, karşı taraf onayı,
- teminat, kefalet, garanti, rehin, ipotek, haciz veya payoff,
- KVKK/veri işleme/yurt dışına aktarım ve entegrasyon erişimi,
- çalışan/SGK/işyeri devri ve kilit çalışan belgeleri,
- ruhsat/lisans devri veya kurum bildirimi,
- dava/icra/tahkim/arabuluculuk kaynaklı sulh, feragat, teminat veya ibra.

Dedup kuralı: aynı item adı yerine `(kategori + kaynak + aksiyon tipi + karşı taraf)` üzerinden dedupe yap. Aynı karşı taraf için hem sözleşme devir onayı hem teminat değişikliği gerekiyorsa iki ayrı item kalır.

Mevcut item ile yeni handoff birleşiyorsa bilgi kaybetme: yeni handoff `evidence_required`, `due`, `responsible` veya `notes` alanı ekliyorsa satırı zenginleştir.

## Mode 3 - Status update

Kullanıcı item ID veya açıklama verirse ilgili satırı bul ve güncelle.

Örnek:

```text
/corporate-legal:closing-checklist
CP-004: Rekabet başvurusu yapıldı, Kurum evrak numarası eklendi, cevap bekleniyor.
```

Güncelle:

- status,
- last_updated,
- source/evidence,
- notes,
- blocker değiştiyse blocking.

Hukuki sonuç doğuran "tamamlandı" güncellemesinde kanıt sor:

```text
Bu item'ı complete yapmak için hangi belgeye dayanıyoruz? Örn. imzalı karar, ticaret sicili ilanı, KAP açıklaması, Kurum yazısı, karşı taraf onayı, ödeme dekontu, fek yazısı.
```

Kanıt yoksa `complete` yerine `in_progress` veya `waiting_evidence` kullan.

## Mode 4 - Status report

```markdown
GİZLİ HUKUKİ ÇALIŞMA TASLAĞI - AVUKAT/HUKUKÇU İNCELEMESİNE TABİDİR

# Kapanış Checklist Durumu - [İşlem kodu] - [tarih]

Reviewer note
- Kaynaklar: [işlem sözleşmesi, DD bulguları, schedule, kullanıcı güncellemeleri]
- Okuma kapsamı: [checklist item sayısı ve son güncelleme]
- Doğrulanması gerekenler: [resmi kaynak, dış danışman, imza yetkisi, tescil, izin]
- Aksiyon öncesi: ["ready to close" denmeden önce hukukçu kontrolü gerekir]

Target close: [tarih] ([N] gün)
Toplam item: [N] - tamamlanan [N], devam eden [N], başlamayan [N], blokaj [N]

## Kırmızı - kapanışı bloke eden / riskli

| ID | Item | Sorumlu | Due | Status | Kanıt | Gün |
|---|---|---|---|---|---|---:|
| [CP-001] | [item] | [responsible] | [date] | [status] | [evidence] | [N] |

## Sarı - bloke edebilir / takipte

[aynı tablo]

## Yeşil - tamamlandı

[kısa liste veya collapsed count]

## Post-closing / bilgi amaçlı

[kapanış sonrası bırakılan işler]

## Critical path

[Gecikirse kapanışı kaydıracak 1-5 item]
```

## Critical path analizi

Her blocking item için şu mantığı uygula:

- Due date yoksa `unknown timing` olarak üstte göster.
- Tamamlama süresi bilinmiyorsa kullanıcıdan veya sorumlu ekipten sor.
- Resmi kurum izni, ticaret sicili, karşı taraf onayı, teminat fekki ve fon akışı genellikle kritik path adayıdır; ancak somut işlem sözleşmesi belirleyicidir.
- `target_close - today` süresi item'ın gerçekçi tamamlama süresinden azsa `at_risk` yap.

Takvim hesabında resmi tatil, hafta sonu, kurum iş günü ve belge eksikliği etkisi varsa kesin son gün üretme; risk azaltıcı şekilde erken aksiyon öner.

## Consequential-action gate

"Ready to close", "all CPs satisfied", "kapanışa hazır", "şartlar tamam" veya kapanış sertifikası istendiğinde dur:

```text
Kapanış koşullarının tamamlandığını söylemek hukuki ve finansal sonuç doğurur. Bu listeye göre status raporu hazırlayabilirim; ancak "kapanışa hazır" sonucunu sorumlu avukat/hukukçu ve işlem sözleşmesi kontrolü olmadan kesinleştirmem.

Kontrol edilmesi gerekenler:
- Her CP için tamamlanma kanıtı var mı?
- Waiver veya side letter gereken item var mı?
- Eksik kalan resmi izin, tescil, KAP/MKK, Rekabet, vergi/SGK, teminat veya sözleşme onayı var mı?
- Funds flow ve imza paketindeki belgeler son versiyon mu?
```

Kullanıcı hukukçu değilse ayrıca avukat/hukukçu incelemesi onayı iste. Hukukçu kullanıcıda da "ready to close" ifadesini reviewer note içinde kanıta bağla.

## Dashboard / export

10'dan fazla item varsa veya kullanıcı isterse dashboard/CSV teklif et. CSV hücrelerinde dış kaynaktan gelen metin `=`, `+`, `-`, `@`, tab veya yeni satırla başlıyorsa güvenli hale getir.

CSV kolonları:

```text
ID, Item, Category, Phase, Responsible, Due, Status, Blocking, Evidence Required, Source, Notes
```

## Dataroom watcher entegrasyonu

`agents/dataroom-watcher.md` ileride VDR'a yeni yüklenen belgeleri izleyip bu checklist'e öneri item gönderecek. Agent önerileri otomatik complete yapmaz; her ekleme kaynak ve kanıt gerektirir.

## Bu skill ne yapmaz

- Resmi başvuru, tescil, KAP/MKK bildirimi, Rekabet başvurusu, ödeme veya imza işlemi yapmaz.
- Kapanış koşullarının hukuken tamamen sağlandığına tek başına karar vermez.
- İşlem sözleşmesinde olmayan veya kullanıcı/avukat tarafından kabul edilmeyen item'ı kendiliğinden CP ilan etmez.
- Resmi süre, izin veya eşik konusunda güncel kaynak olmadan kesin tarih üretmez.
- Waiver, side letter, escrow, tazminat veya beyan-garanti metnini nihai hale getirmez.
