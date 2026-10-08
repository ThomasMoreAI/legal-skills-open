# Phase 8 — Metadata Ingest v2 (Data Quality Fix)

> วันที่: 1 สิงหาคม 2568
> งาน: ใช้ประโยชน์จาก metadata ที่อยู่ใน `panya_ai_legal_data_v2_fixed.zip` ที่ผู้ใช้ส่งมา

## สรุปการแก้ไข

ก่อนหน้านี้ script ingest (`fresh_ingest_turso.py`) อ่านเฉพาะ `manifest.csv` ที่มีข้อมูลแค่ ID/Name/Folder โดยไม่ได้อ่าน **YAML front matter** ที่อยู่ในแต่ละไฟล์ `.md` — ทำให้ metadata ที่ผู้ใช้จัดไว้ให้ครบหมดไม่ถูกใช้

หลังจาก ingest ใหม่ด้วย `ingest_metadata_v2.py` (parse front matter) + `ingest_xref_http.py` (HTTP API สำหรับ cross_references ที่หลีกเลี่ยง libsql Python adapter crash):

## ผลลัพธ์

### 1. `laws` table — เพิ่ม rich metadata
- **krisdika_sysid**: 68 จาก 78 laws (88%) — สามารถ link กลับไปยัง krisdika.go.th
- **law_type**: 68 laws (พ.ร.บ. / พ.ร.ก. / ประมวลกฎหมาย / etc.)
- **law_group**: 68 laws (สวัสดิการสังคม / แรงงาน / อาญา / etc.)

### 2. `regulations` table — แก้ status ให้ถูกต้อง
- **active** (consolidated = true): 48 ฉบับ — ฉบับรวมแก้ไขล่าสุด
- **superseded** (consolidated = false): 567 ฉบับ — ฉบับที่ประกาศในราชกิจจาฯ แต่มีฉบับใหม่กว่าแทนที่แล้ว
- **category**: 615 ฉบับ มี category ครบ (ประกาศกรมสวัสดิการ / กฎกระทรวง / etc.)

### 3. `judgments` table — เพิ่ม rich metadata
- **topics** (JSON array): 502 คดี มี tags ครบ (เช่น `["เลิกจ้างไม่เป็นธรรม", "สินจ้างแทนการบอกกล่าวล่วงหน้า"]`)
- **laws_cited** (JSON array): 502 คดี มีการระบุมาตราที่อ้าง (เช่น `["พ.ร.บ.จัดตั้งศาลแรงงาน 2522 มาตรา 54"]`)
- **case_type_group**: 502 คดี มีกลุ่มคดี (คดีธุรกิจและเศรษฐกิจ / etc.)

### 4. `cross_references` table — จาก 0 → 10,950 แถว!
- 861 law-section cross-refs (จาก `cross_reference_map.csv`)
- 10,089 judgment citation cross-refs (cited_by)
- source_type: `contract_template` (ทั้งหมด เพราะ cross_reference_map.csv มี source = F1-F63)

## ไฟล์ที่เพิ่ม

| Script | หน้าที่ |
|---|---|
| `scripts/ingest_metadata_v2.py` | Parse YAML front matter จากทุกไฟล์ .md — อัปเดต laws/regulations/judgments |
| `scripts/ingest_metadata_per_folder.py` | Ingest ทีละ folder (แก้ libsql Python adapter crash) |
| `scripts/ingest_xref_step1.py` | Dump lookups → `/tmp/code_lookup.json` |
| `scripts/ingest_xref_step2.py` | พยายาม insert cross_refs (libsql crash — ไม่ใช้แล้ว) |
| `scripts/ingest_xref_http.py` | Insert cross_refs ผ่าน Turso HTTP API (ใช้งานได้จริง) |

## Known Limitations

1. **libsql Python adapter bug**: มีปัญหา segfault เมื่อทำหลาย UPDATE ติดต่อกัน — ต้องใช้ subprocess per folder หรือ HTTP API
2. **cross_references มีแค่ source_type='contract_template'**: เพราะ `cross_reference_map.csv` มีเฉพาะ template-to-law mapping — ยังขาด law-to-law และ judgment-to-law โดยตรง
3. **regulations 'superseded' status**: เป็น heuristic (ใช้ is_consolidated flag) — ยังไม่ได้ verify กับราชกิจจานุเบกษาว่ายกเลิกจริงหรือเปล่า

## การรัน

```bash
# 1. Update laws/regulations/judgments metadata
/home/z/.venv/bin/python3 /home/z/my-project/work/Panya-AI-final/scripts/ingest_metadata_per_folder.py \
  /home/z/my-project/work/legal_data_v2/panya_ai_legal_data/A_laws_labor laws

# 2. Build lookup table
/home/z/.venv/bin/python3 /home/z/my-project/work/Panya-AI-final/scripts/ingest_xref_step1.py

# 3. Ingest cross_references via HTTP API (with resume capability — change START_ROW)
/home/z/.venv/bin/python3 /home/z/my-project/work/Panya-AI-final/scripts/ingest_xref_http.py
```
