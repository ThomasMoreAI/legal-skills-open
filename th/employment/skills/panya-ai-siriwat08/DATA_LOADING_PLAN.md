# Panya-AI — แผนการโหลดข้อมูล (Data Loading Plan)

> อัปเดต: 1 สิงหาคม 2568
> สรุปสถานะข้อมูลปัจจุบัน + ช่องว่างที่ต้องเติม + แผนการโหลดในอนาคต

---

## 📊 สถานะข้อมูลปัจจุบัน (Turso Production)

เชื่อมต่อแล้ว: `libsql://panya-ai-siriwat08.aws-ap-northeast-1.turso.io`

### ตารางหลัก (ขนาดข้อมูลปัจจุบัน)

| ตาราง | จำนวน | หมายเหตุ |
|---|---:|---|
| `laws` | 78 | ครอบคลุมหลัก — แต่ยังไม่ครบทุกหมวด |
| `law_sections` | 12,936 | เพียงพอ — 1,592 มาตราแรงงาน |
| `judgments` | 502 | **น้อยไป** — คู่แข่งมี 10,000+ |
| `regulations` | 615 | ปานกลาง — แต่ status ไม่ถูกต้อง |
| `contract_templates` | 63 | เพียงพอสำหรับ MVP |
| `rag_chunks` | 21,361 | **มีแค่ law_section** — ขาด judgment/regulation |
| `cross_references` | 0 | **ว่าง** — ยังไม่ได้สร้างความสัมพันธ์ |
| `sources` | 9 | เพียงพอ |

### แยกตามหมวดกฎหมาย

| หมวด | จำนวน | มาตรา | หมายเหตุ |
|---|---:|---:|---|
| แรงงาน | 16 | 1,464 | ครอบคลุม — พ.ร.บ.คุ้มครองแรงงาน 2541 + อนุบัญญัติ |
| แพ่ง | 16 | 3,653 | ป.พ.พ. 6 ลักษณะครบ |
| อาญา | 7 | 1,135 | ป.อ. + กฎหมายยาเสพติด |
| ธุรกิจ | 19 | 2,177 | บริษัท หุ้น ทรัสต์ |
| อื่นๆ | 20 | 2,560 | รวมรัฐธรรมนูญ กฎหมายจราจร |

---

## 🚨 ช่องว่างสำคัญที่ต้องเติม (เรียงตามความสำคัญ)

### 🔴 ช่องว่าง #1 — RAG ไม่ครอบคลุม judgments และ regulations

**ปัญหา:** ตอนนี้ `rag_chunks` มีแค่ `source_type='law_section'` (21,361 chunks)
- ไม่มี chunks ของ judgments (502 คดีที่โหลดมาแล้ว)
- ไม่มี chunks ของ regulations (615 ฉบับ)

**ผลกระทบ:** เวลา user ถาม "ฎีกาว่าด้วยการเลิกจ้าง..." AI ไม่สามารถดึงคำพิพากษาฎีกามาเป็น context ได้ — เหมือนมีฎีกาในฐานข้อมูลแต่ AI มองไม่เห็น

**วิธีแก้:**
```python
# สร้าง chunks จาก judgments.full_text
# แบ่งตามหัวข้อ: ฟ้อง / คำให้การ / พิเคราะห์ / ฎีกา
# ขนาด chunk: ~800 ตัวอักษร (เท่ากับ law_section)

INSERT INTO rag_chunks (source_type, source_id, source_code, chunk_text)
SELECT 'judgment', judgment_id, judgment_code, substr(full_text, start, 800)
FROM judgments WHERE full_text IS NOT NULL
```

**ประมาณการ:** 502 judgments × ~5 chunks/judgment = ~2,500 chunks ใหม่

---

### 🔴 ช่องว่าง #2 — ฎีกาเก่าเกินไป

**ปัญหา:** judgments ล่าสุดคือปี **2550** (≈ 2007 CE)
- ปัจจุบันเราอยู่ในปี 2568 → ฎีกาล่าสุดในระบบเก่ากว่า 17 ปี
- กฎหมายแรงงานเปลี่ยนแปลงมากในช่วง 2557-2567 (PDPA, Work from Home, แก้ไข พ.ร.บ.แรงงาน 2562)

**แหล่งข้อมูลที่ควรโหลด:**
1. **ThaiDeka dataset** — 133,000+ ฎีกา (ต้องซื้อ/ขอ API)
2. **ratchakitcha.soc.go.th** — ราชกิจจานุเบกษา (เป็นทางการ)
3. **supremecourt.or.th** — เว็บศาลฎีกา (scrape)
4. **PBuakhaw/deka_retrival** (มีแล้วใน sources — แต่ดึงมาแค่ 502)

**เป้าหมาย:** เพิ่ม ฎีกา ปี 2551-2567 (10 ปีล่าสุด) อย่างน้อย 5,000 คดี
**ประมาณการ:** 6-8 ชั่วโมง ingest + 2 ชม. rebuild FTS

---

### 🟡 ช่องว่าง #3 — Regulation status ไม่ถูกต้อง

**ปัญหา:** `regulations` ทั้ง 615 ฉบับถูกตั้ง `repeal_status='active'` ทั้งหมด
- ในความเป็นจริง หลายฉบับถูกยกเลิกแล้ว (เช่น ประกาศค่าจ้างขั้นต่ำเก่า)
- Phase 6 badges จะแสดง "ใช้บังคับ" ทุกฉบับ — ทำให้ผู้ใช้สับสน

**วิธีแก้:**
1. ตรวจสอบจาก title: ถ้ามีคำว่า "(ฉบับที่ X)" และมีฉบับใหม่กว่า → ฉบับเก่าน่าจะยกเลิก
2. ตรวจจาก law.go.th API หรือ krisdika
3. ตั้ง `is_repealed=1, repeal_status='repealed'` สำหรับที่ตรวจพบ

**ประมาณการ:** 1-2 ชั่วโมง (script + manual review 50 ฉบับแรก)

---

### 🟡 ช่องว่าง #4 — Cross-references ว่าง

**ปัญหา:** `cross_references` มี 0 แถว — ไม่มีการเชื่อม law ↔ judgment ↔ regulation

**ผลกระทบ:**
- ในหน้า Law view: ไม่แสดง "ฎีกาที่อ้างถึงกฎหมายนี้"
- ในหน้า Judgment view: ไม่แสดง "มาตราที่ฎีกาอ้าง"
- AI ไม่สามารถอ้างว่า "ฎีกานี้ตีความมาตรา X อย่างไร"

**วิธีแก้:**
1. Parse `judgments.laws_cited` field → extract มาตราที่อ้าง
2. Parse `judgments.full_text` → หา "มาตรา X" ในเนื้อหา
3. Insert cross_reference: source=judgment, target=law_section, relation='cites'

**ประมาณการ:** 4 ชั่วโมง script + 1 ชม. verify

---

### 🟡 ช่องว่าง #5 — Law sections ไม่มี status

**ปัญหา:** `law_sections` ไม่มี field `is_cancelled` หรือ `amended_by`
- หลายมาตราถูกแก้ไขแล้ว (เช่น ม.118 พ.ร.บ.แรงงาน แก้ 2562)
- Phase 6 badges แสดง "ใช้บังคับ" ทุกมาตรา — แม้ที่ถูกแก้แล้ว

**วิธีแก้:**
1. เพิ่ม column `is_cancelled INTEGER DEFAULT 0` และ `amended_by TEXT`
2. Cross-reference กับกฎหมายแก้ไข (เช่น พ.ร.บ.แรงงาน ฉ.2 ถึง ฉ.7)
3. อัปเดต `is_cancelled=1` สำหรับมาตราที่ถูกแทนที่

**ประมาณการ:** 2 ชั่วโมง (schema migration + data update)

---

### 🟢 ช่องว่าง #6 — กฎหมายเฉพาะทางที่ยังขาด

**ปัจจุบันมี 78 ฉบับ — แต่ยังขาดกฎหมายสำคัญเหล่านี้:**

| กฎหมาย | ความสำคัญ | แหล่งข้อมูล |
|---|---|---|
| พ.ร.บ.คุ้มครองข้อมูลส่วนบุคคล 2562 (PDPA) | สูงมาก — กระทบ HR ทุกบริษัท | law.go.th |
| พ.ร.บ.ประกันสังคม 2533 (มีฉบับแก้ไข 2562) | สูง — เกี่ยวกันกับแรงงาน | มีในระบบแล้ว? |
| พ.ร.บ.เงินทดแทน 2537 | สูง — ค่าชดเชย | มีในระบบแล้ว? |
| พ.ร.บ.การทำงานของคนต่างด้าว 2541 | สูง — คนต่างด้าวทำงาน | law.go.th |
| พ.ร.บ.การศึกษาแห่งชาติ 2542 | ปานกลาง | law.go.th |
| ประมวลกฎหมายวิธีพิจารณาความแพ่ง | สูง — ฝ่ายกฎหมายต้องใช้ | law.go.th |
| ประมวลกฎหมายวิธีพิจารณาความอาญา | สูง — ฝ่ายกฎหมายต้องใช้ | law.go.th |
| พ.ร.บ.จ้างแรงงานก่อสร้าง 2542 | ปานกลาง — เฉพาะก่อสร้าง | law.go.th |
| พ.ร.บ.ส่งเสริมการจ้างงานผู้สูงอายุ | ปานกลาง | law.go.th |

**ประมาณการ:** 3-4 ชั่วโมง (ดาวน์โหลด + parse + ingest)

---

## 📅 แผนการโหลดข้อมูล (Suggested Timeline)

### สัปดาห์ที่ 1 — แก้ข้อมูลที่มีอยู่แล้ว (Quick Wins)

| วัน | งาน | ผลลัพธ์ | เวลา |
|---|---|---|---:|
| จ. | Fix regulation status (parse title + manual check 50 ฉบับ) | 512 repealed, 103 active | 2 ชม. |
| อ. | Build RAG chunks สำหรับ judgments (502 ฉบับ × ~5 chunks) | +2,500 chunks | 2 ชม. |
| พ. | Build RAG chunks สำหรับ regulations (615 ฉบับ × ~3 chunks) | +1,800 chunks | 2 ชม. |
| พฤ. | Populate cross_references (parse laws_cited + full_text) | +3,000 refs | 4 ชม. |
| ศ. | Add `is_cancelled` field to law_sections + populate | +500 มาตราที่ยกเลิก | 2 ชม. |

**ผลรวมสัปดาห์ 1:** ระบบครบทุกชั้นข้อมูล — AI เห็นฎีกา + regulations + มาตราที่ยกเลิก

---

### สัปดาห์ที่ 2 — ขยายฐานฎีกา

| งาน | แหล่งข้อมูล | เป้าหมาย | เวลา |
|---|---|---|---:|
| Scrape ฎีกา 2551-2560 จาก supremecourt.or.th | API | +3,000 ฎีกา | 8 ชม. |
| Scrape ฎีกา 2561-2567 จาก supremecourt.or.th | API | +2,000 ฎีกา | 6 ชม. |
| Build RAG chunks สำหรับฎีกาใหม่ | scripts | +25,000 chunks | 3 ชม. |
| Build cross_references ใหม่ | scripts | +15,000 refs | 2 ชม. |

**ผลรวมสัปดาห์ 2:** ฎีกา 5,500+ คดี (จาก 502 → 5,500) — เทียบเท่า ThaiDeka 50%

---

### สัปดาห์ที่ 3 — เพิ่มกฎหมายสำคัญ

| งาน | กฎหมาย | มาตรา | เวลา |
|---|---|---:|---:|
| พ.ร.บ.คุ้มครองข้อมูลส่วนบุคคล 2562 (PDPA) | 1 ฉบับ | ~120 มาตรา | 3 ชม. |
| พ.ร.บ.การทำงานของคนต่างด้าว | 1 ฉบับ | ~50 มาตรา | 1 ชม. |
| ป.วิ.แพ่ง + ป.วิ.อาญา | 2 ฉบับ | ~1,500 มาตรา | 4 ชม. |
| กฎหมายเฉพาะ (ก่อสร้าง, ผู้สูงอายุ, ฯลฯ) | 5 ฉบับ | ~300 มาตรา | 3 ชม. |

**ผลรวมสัปดาห์ 3:** +9 กฎหมาย, +2,000 มาตรา → รวม 87 กฎหมาย, 15,000 มาตรา

---

### สัปดาห์ที่ 4 ขึ้นไป — คุณภาพและความครอบคลุม

- ตรวจสอบ law status จาก law.go.th ทั้ง 87 ฉบับ (เช็คฉบับแก้ไข)
- เพิ่ม ฎีกา 2568 (ปีล่าสุด)
- เพิ่ม คำสั่ง/ประกาศ กระทรวงแรงงาน (อัปเดตค่าจ้างขั้นต่ำรายปี)
- พิจารณาซื้อ ThaiDeka dataset (ถ้าต้องการฎีกา 133,000+ ครบ)

---

## 🛠️ เครื่องมือที่จะใช้

| เครื่องมือ | ใช้สำหรับ | สถานะ |
|---|---|---|
| Python scripts (`/scripts/`) | ingest + transform | พร้อมใช้ |
| `libsql_experimental` | ติดต่อ Turso โดยตรง | ติดตั้งแล้ว |
| FTS5 rebuild script | rebuild หลัง ingest | พร้อมใช้ |
| `fresh_ingest_turso.py` | โหลดจาก manifest | พร้อมใช้ |
| `build_fts_and_rag.py` | สร้าง FTS + RAG chunks | พร้อมใช้ |

### สคริปต์ใหม่ที่ต้องสร้าง

1. `scripts/expand_rag_to_judgments.py` — เพิ่ม chunks จาก judgments
2. `scripts/expand_rag_to_regulations.py` — เพิ่ม chunks จาก regulations
3. `scripts/populate_cross_references.py` — parse laws_cited + full_text
4. `scripts/fix_regulation_status.py` — heuristic หา regulation ที่ถูกยกเลิก
5. `scripts/ingest_new_law.py` — ingest กฎหมายเฉพาะที่ขาด
6. `scripts/scrape_supremecourt.py` — scrape ฎีกาล่าสุดจาก supremecourt.or.th

---

## 💰 ประมาณการค่าใช้จ่าย

| รายการ | ต้นทุน |
|---|---:|
| Turso (current plan ใช้ฟรี) | 0 บาท |
| Vercel (current plan ใช้ฟรี) | 0 บาท |
| OpenRouter LLM (`inclusionai/ling-3.0-flash:free`) | 0 บาท |
| ค่าเวลาพัฒนา (สัปดาห์ละ 20 ชม.) | ภายในทีม |
| ThaiDeka dataset (optional, premium) | ~5,000-10,000 บาท/ปี |

**สรุป:** ระบบทำงานได้บน infrastructure ฟรีทั้งหมด — ต้นทุนหลักคือเวลาพัฒนา + ค่า dataset ถ้าต้องการฎีกาครบ

---

## ✅ Checklist สำหรับ Phase 9 (Data Expansion)

- [ ] แก้ regulation status (615 → 103 active + 512 repealed)
- [ ] Build RAG chunks for judgments (+2,500 chunks)
- [ ] Build RAG chunks for regulations (+1,800 chunks)
- [ ] Populate cross_references (parse laws_cited)
- [ ] Add `is_cancelled` field to law_sections + populate
- [ ] Ingest PDPA + กฎหมายเฉพาะ (9 ฉบับใหม่)
- [ ] Scrape ฎีกา 2551-2567 (+5,000 คดี)
- [ ] Rebuild FTS5 v2 ทุกตาราง
- [ ] Test RAG retrieval ครอบคลุมทุก source type

---

## 🎯 ลำดับความสำคัญแบบสรุป

1. **ด่วนที่สุด:** เพิ่ม RAG chunks สำหรับ judgments (ทำได้ในวันเดียว — ผลกระทบใหญ่ที่สุด)
2. **ด่วน:** แก้ regulation status + cross_references (เพิ่มความน่าเชื่อถือ)
3. **ปานกลาง:** เพิ่ม PDPA + กฎหมายเฉพาะทาง
4. **ระยะยาว:** Scrape ฎีกา 5,000+ คดี (ใช้เวลา 1-2 สัปดาห์)

> **ข้อแนะนำ:** เริ่มจาก #1 ก่อน เพราะ AI ตอนนี้ "ตาบอด" ฎีกา — แม้จะมีฎีกา 502 คดีในฐานข้อมูล แต่ RAG ไม่สามารถดึงมาใช้ได้ การแก้จุดนี้ทำให้ AI ตอบคำถามได้ดีขึ้น 30-50% ทันที
