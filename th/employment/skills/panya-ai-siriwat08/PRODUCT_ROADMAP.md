# Panya-AI Product Roadmap & Competitor Analysis

> อัปเดตล่าสุด: 30 กรกฎาคม 2568
> แหล่งข้อมูล: การวิเคราะห์คู่แข่ง + UX/UI recommendations

---

## 🎯 Positioning ปัจจุบัน

> **Panya-AI คือ Thai Legal AI Workspace สำหรับนายจ้างและทีมกฎหมายภายใน ที่รวมการค้นกฎหมาย, คำตอบพร้อม citation, การประเมินความเสี่ยง, การตรวจสัญญา และการสร้างเอกสารไว้ในที่เดียว**

### 5 เสาหลักของผลิตภัณฑ์
1. ค้นและตอบกฎหมาย (AI Chat + RAG)
2. อ้างอิงหลักฐาน (Citation-first)
3. ประเมินความเสี่ยง (Risk Matrix 5×5)
4. ตรวจสัญญา (Contract Analysis)
5. สร้างเอกสารจาก template (PDF Builder)

---

## 📊 Competitor Matrix

| ผู้เล่น | ตำแหน่ง | จุดเด่น | สิ่งที่เราเรียนรู้ |
|---|---|---|---|
| **ThaiDeka** | Legal research workspace | 133k+ ฎีกา, note/highlight/export, alerts | retention + research workflow |
| **Thanoy** | Broad legal AI | persona onboarding, LINE distribution | onboarding + low friction |
| **SLegalTools** | Evidence-first search | law status checker, 2-step retrieval | trust architecture |
| **Kelomn** | Business legal research | IA ตาม use case ธุรกิจ | information architecture |
| **Firmly** | Contract drafting | step-by-step wizard, pricing | guided workflow + ความไม่แข็ง |
| **KHORN AI** | Law firm OS | case workflow, task management | enterprise operation layer |
| **FourCorners** | Grounded answers | คำตอบผูกมาตราชัด | citation presentation |

### Positioning Matrix

|  | Consumer/General | Enterprise/Internal |
|---|---|---|
| **Search-heavy** | ThaiDeka, Thanoy | SLegalTools |
| **Workflow-heavy** | Firmly | **← Panya-AI ควรยืนตรงนี้** |

---

## 🎨 UX/UI Direction

### แนวที่เลือก: "Warm Professional"
- 70% Notion (soft, approachable)
- 20% Microsoft Fluent (modern enterprise)
- 10% Atlassian (structured workflow)

### สิ่งที่ต้องปรับ

**ระยะ 1: ปรับความรู้สึก (ทำก่อน)**
1. ลด border/card density 30-40%
2. เพิ่ม spacing และ hierarchy
3. หน้าแรกเริ่มจาก "งานที่อยากทำ" ไม่ใช่ "ระบบมีอะไร"
4. ทำ AI panel ให้เป็นมิตรขึ้น
5. ลดความมืด/หนักของสี

**ระยะ 2: ปรับ flow**
1. chat → source → action
2. contract upload → red flags → fix suggestions
3. risk matrix → explanation → ask AI
4. template → fill → preview → export

**ระยะ 3: ปรับให้เป็น product ใหญ่**
1. Persona onboarding (HR / Legal / Executive)
2. Save workspaces
3. Notes + highlights + export PDF
4. Law status badges (ใช้บังคับ/ยกเลิก)
5. Internal company knowledge

### หลีกเลี่ยง
- หน้าดำเข้มตลอด
- กล่องเยอะเกิน
- เส้นเยอะเกิน
- legal jargon ตั้งแต่หน้าหลัก

---

## ✅ สถานะปัจจุบัน (Phase 1-7 เสร็จแล้ว)

| Phase | สถานะ | รายละเอียด |
|---|---|---|
| Phase 1 | ✅ เสร็จ | AI Prompt + Legal Strategist + Sub-skills (4 skills) |
| Phase 2 | ✅ เสร็จ | Design System + Sidebar + Logo + Fonts |
| Phase 3 | ✅ เสร็จ | AI Chat 3-column + Typewriter Hero + Employer Section |
| Phase 4 | ✅ เสร็จ | PDF Builder + Risk Matrix + Contract Analysis + Mascot |
| Phase 5 | ✅ เสร็จ | 4 Action Buttons on home page (ถาม/สร้าง/วิเคราะห์/Risk) |
| Phase 6 | ✅ เสร็จ | Law status badges (ใช้บังคับ/ยกเลิกแล้ว) |
| Phase 7 | ✅ เสร็จ | Persona onboarding — HR / Legal / Owner + role-aware AI prompt + skill routing |

## ⬜ ขั้นต่อไป

### Phase 8: Retention & Discovery
- Latest/Popular/Recommended judgments บนหน้าคำพิพากษา
- Notes + highlights + export PDF (per section/judgment)
- Save chat sessions + recently viewed
- Bookmark folders + tags

### Phase 9: Data Expansion (สำคัญมาก)
- **RAG coverage expansion**: เพิ่ม judgments + regulations เข้า rag_chunks (ปัจจุบันมีแค่ law_section)
- **Cross-references**: เชื่อม law ↔ judgment ↔ regulation (ตาราง cross_references ยังว่าง)
- **Newer judgments**: ingest ฎีกา 2557-2567 (2014-2024) — ปัจจุบันล่าสุด 2550
- **Regulation status fix**: re-ingest ด้วย is_repealed flag ที่ถูกต้อง (ตอนนี้ active ทั้ง 615)
- **Law sections status**: เพิ่ม field is_cancelled สำหรับมาตราที่ถูกแก้ไข/ยกเลิก

### Phase 10: Enterprise
- Contract deviation check (compare uploaded contract vs template)
- Internal company knowledge ingestion
- Role-based access control (RBAC)
- Approval workflow + audit trail
