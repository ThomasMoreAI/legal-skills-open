---
name: panya-ai-siriwat08
title: 'Panya-AI: Thai Legal AI for Employers (ฝั่งนายจ้าง/บริษัท)'
description: Comprehensive Thai legal AI for company/employer side. Covers 50+ Thai laws (labor, criminal, civil), 1,000+ judgments, contract review, risk assessment (5x5 matrix), employer defense against unfair employee claims. Use for Panya-AI - Thai Labor Law AI assistant focused on protecting employers from labor exploitation while staying 100% compliant with Thai law.
author: Siriwat08
author_url: https://github.com/Siriwat08/Panya-AI
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: th
practice: employment
language: th
---

# Panya-AI: Thai Legal AI for Employers (ฝั่งนายจ้าง/บริษัท)

## 🎯 Mission Statement

Panya-AI คือ **Thai Legal AI ฝั่งนายจ้าง** ที่ออกแบบมาเพื่อ:

1. ✅ **ปกป้องนายจ้างอย่างถูกกฎหมาย** — รู้กฎหมายครบทุกด้าน ป้องกันการถูกฟ้องร้องโดยไม่เป็นธรรม
2. ✅ **ป้องกัน "ลูกจ้างหัวหมอ"** — รู้ trick ที่ลูกจ้างชอบใช้ เพื่อหลีกเลี่ยงการตกหลุมพราง
3. ✅ **ตรวจสัญญาตามกฎหมายไทย** — ประเมินความเสี่ยงทุกข้อ พร้อมข้อเสนอแก้ไข
4. ✅ **ยกระดับปัญหาที่ซับซ้อน** — ส่งต่อทนายเมื่อเกินขอบเขต AI
5. ✅ **100% สอดคล้องกับกฎหมายไทย** — ไม่แนะนำวิธีที่ผิดกฎหมาย

> ⚠️ **คำเตือน**: Panya-AI ไม่ได้ช่วย "หาช่องโหว่" แต่ช่วยให้บริษัท "รู้กฎหมายดีพอ" เพื่อปฏิบัติตามอย่างถูกต้อง — วิธีนี้คือการป้องกันที่ดีที่สุด

---

## When to Use This Skill

Use this skill when the user asks to:

- **Review a contract** (ตรวจสอบสัญญา) — employment, NDA, lease, sale, service, loan
- **Assess legal risk** (ประเมินความเสี่ยงทางกฎหมาย) — for any business decision
- **Defend against employee claim** (ป้องกันการถูกฟ้องจากลูกจ้าง)
- **Draft employment documents** (ร่างเอกสารแรงงาน) — contracts, warnings, termination letters
- **Check compliance** (ตรวจสอบการปฏิบัติตามกฎหมาย) — LPA, SSO, WC, OSH, PDPA
- **Answer Thai law questions** (ตอบคำถามกฎหมายไทย) — labor, civil, criminal
- **Train a Legal AI** (ฝึก AI) — Thai legal domain
- **Build contract review system** (สร้างระบบตรวจสัญญา)

---

## 📚 Section 1: Legal Knowledge Base (50+ Laws)

### 1.1 Tier 1 — Critical for Employer Defense (MUST HAVE)

| # | Law | Year | Why critical | Status |
|---|-----|------|--------------|--------|
| 1 | พ.ร.บ. คุ้มครองแรงงาน (LPA) | 2541 | Employment contract core | ✅ Have |
| 2 | ประมวลกฎหมายแพ่งและพาณิชย์ (CCC) | 2468 | All contract types | ✅ Have |
| 3 | ประมวลกฎหมายอาญา (Penal Code) | 2499 | Employee fraud, theft, forgery | ✅ Have |
| 4 | พ.ร.บ. ว่าด้วยข้อสัญญาที่ไม่เป็นธรรม (UCTA) | 2540 | **Criteria for unfair terms** | ❌ **Need to add** |
| 5 | พ.ร.บ. ความลับทางการค้า (Trade Secrets) | 2545 | **NDA-specific law** | ❌ **Need to add** |
| 6 | พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล (PDPA) | 2562 | **Personal data in contracts** | ❌ **Need to add** |
| 7 | พ.ร.บ. คุ้มครองผู้บริโภค | 2522 | B2C contracts | ❌ **Need to add** |
| 8 | พ.ร.บ. ธุรกรรมทางอิเล็กทรอนิกส์ | 2544 | e-Contracts, e-Signatures | ❌ **Need to add** |
| 9 | ประมวลกฎหมายวิธีพิจารณาความแพ่ง (CPC) | 2478 | Civil procedure | ✅ Have |
| 10 | ประมวลกฎหมายวิธีพิจารณาความอาญา (CrPC) | 2478 | Criminal procedure | ✅ Have |
| 11 | **พ.ร.บ. วิธีพิจารณาคดีแรงงาน** | **2522** | **Labor court procedure** | ❌ **Need to add** |
| 12 | **พ.ร.บ. ความปลอดภัย อาชีวอนามัย และสภาพแวดล้อมในการทำงาน (OSH)** | **2554** | **🔥 Critical for employer** | ❌ **Need to add** |
| 13 | **พ.ร.บ. ส่งเสริมการพัฒนาฝีมือแรงงาน** | **2545** | Training levy 1% | ❌ **Need to add** |
| 14 | **พ.ร.บ. แรงงานรัฐวิสาหกิจสัมพันธ์** | **2543** | State enterprise labor | ❌ **Need to add** |
| 15 | **พ.ร.บ. การทำงานของคนต่างด้าว** | **2551** | Foreign workers | ❌ **Need to add** |

### 1.2 Tier 2 — Important (Labor + Business)

| # | Law | Year | Use case | Status |
|---|-----|------|----------|--------|
| 16 | พ.ร.บ. แรงงานสัมพันธ์ | 2518 | Unions, strikes | ✅ Have |
| 17 | พ.ร.บ. ประกันสังคม (SSO) | 2533 | Social security | ✅ Have |
| 18 | พ.ร.บ. เงินทดแทน (Workmen's Comp) | 2537 | Work injury | ✅ Have |
| 19 | พ.ร.บ. คุ้มครองผู้รับงานไปทำที่บ้าน | 2553 | Home-worker contracts | ✅ Have |
| 20 | พ.ร.บ. จัดหางานและคุ้มครองคนหางาน | 2528 | Agency employment | ✅ Have |
| 21 | พ.ร.บ. การเช่าอสังหาริมทรัพย์เพื่อพาณิชยกรรม | 2542 | Commercial lease | ❌ **Need to add** |
| 22 | ประมวลกฎหมายที่ดิน | 2497 | Land-related | ✅ Have |
| 23 | พ.ร.บ. ลิขสิทธิ์ | 2537 | IP in contracts | ❌ **Need to add** |
| 24 | พ.ร.บ. หลักประกันทางธุรกิจ | 2558 | Security/mortgage | ❌ **Need to add** |
| 25 | พ.ร.บ. บริษัทมหาชนจำกัด | 2535 | Corporate contracts | ❌ **Need to add** |
| 26 | พ.ร.บ. ห้างหุ้นส่วนและบริษัทจำกัด | 2525 | **All companies** | ❌ **Need to add** |
| 27 | พ.ร.บ. ล้มละลาย | 2483 | Bankruptcy | ❌ **Need to add** |
| 28 | พ.ร.บ. การแข่งขันทางการค้า | 2560 | Non-compete | ❌ **Need to add** |
| 29 | พ.ร.บ. อนุญาโตตุลาการ | 2530 | Arbitration | ❌ **Need to add** |
| 30 | พ.ร.บ. ขายตรงและตลาดแบบตรง | 2545 | Direct sales | ❌ **Need to add** |
| 31 | พ.ร.บ. ป้องกันและปราบปรามการฟอกเงิน (AML) | 2542 | KYC | ❌ **Need to add** |
| 32 | พ.ร.บ. ว่าด้วยการกระทำความผิดเกี่ยวกับคอมพิวเตอร์ | 2560 | **Cyber crime** | ❌ **Need to add** |

### 1.3 Tier 3 — Reference (Procedural + Sectoral)

| # | Law | Year | Use case | Status |
|---|-----|------|----------|--------|
| 33 | รัฐธรรมนูญแห่งราชอาณาจักรไทย | 2560 | Constitutional rights | ❌ |
| 34 | พ.ร.บ. จัดตั้งศาลแรงงาน | 2522 | Labor court | ❌ |
| 35 | พ.ร.บ. วิธีพิจารณาคดีผู้บริโภค | 2551 | Consumer court | ❌ |
| 36 | ประมวลรัษฎากร (Tax Code) | - | Stamp duty, withholding | ❌ |
| 37 | พ.ร.บ. ยาเสพติดให้โทษ | 2522 | (existing) | ✅ |
| 38 | พ.ร.บ. จราจรทางบก | 2522 | (existing) | ✅ |
| 39 | พ.ร.บ. ควบคุมการเช่าเคหะและที่ดิน | 2504 | (existing) | ✅ |
| 40 | พ.ร.บ. แรงงานต่างด้าว (ฉบับใหม่) | 2564 | New foreign worker | ❌ |
| 41 | พ.ร.บ. คุ้มครองแรงงานในงานประมง | 2562 | Fishery | ❌ |
| 42 | พ.ร.บ. ส่งเสริมและพัฒนาคุณภาพชีวิตคนพิการ | 2550 | Disability 1:100 | ❌ |
| 43 | พ.ร.บ. กองทุนสำรองเลี้ยงชีพ | 2541 | PVD | ❌ |
| 44 | กฎกระทรวงแรงงาน (สำคัญ 10 ฉบับ) | - | Min wage, OT, work rules | ❌ |
| 45 | ประกาศกระทรวงแรงงาน (สำคัญ 5 ฉบับ) | - | ค่าจ้าง, OT, งานอันตราย | ❌ |
| 46 | คำวินิจฉัยกรมสวัสดิการและคุ้มครองแรงงาน | - | DLP opinions | ❌ |
| 47 | คำวินิจฉัยกฤษฎีกา (Council of State) | - | Legal interpretation | ❌ |
| 48 | หนังสือตอบข้อหารือ (ตามหน่วยงาน) | - | Practical law | ❌ |
| 49 | พ.ร.บ. ตั๋วเงิน | 2559 | Checks/Bills | ❌ |
| 50 | พ.ร.บ. ทะเบียนพาณิชย์ | 2502 | Commerce registration | ❌ |

**Total**: **50+ laws** — Currently have 14, need to add **36 more**

---

## 📄 Section 2: Required Documents (Templates) — 65+ Documents

### 2.1 Employment Documents (CRITICAL — Must Have)

| ID | Document | Why critical |
|---|---|---|
| F1 | สัญญาจ้างงาน (Employment Contract) | **🔴 Most critical** |
| F2 | สัญญาทดลองงาน (Probation) | **🔴 Critical — 119 days max** |
| F3 | ข้อบังคับเกี่ยวกับการทำงาน (Work Rules) | **🔴 Must file สนร. within 15 days** |
| F4 | ระเบียบวินัย/คู่มือพนักงาน (Disciplinary Rules) | **🔴 Required for fair termination** |
| F5-F7 | หนังสือเตือนพฤติกรรม 1-2-3 (Warning Letters) | **🔴 Required 3x before termination** |
| F8 | หนังสือบอกเลิกสัญญาจ้าง (Termination Letter) | **🔴 Required proper notice** |
| F9 | หนังสือจ่ายค่าชดเชย (Severance Payment) | **🔴 Required ณ วันเลิกจ้าง** |
| F10 | ใบลาออก (Resignation Form) | **🔴 Protects against forced-resignation claims** |
| F11 | ใบรับทรัพย์สินคืน (Asset Return) | Protects company property |
| F12 | หนังสือรับรองการทำงาน (Work Certificate) | Required by law |
| F13 | TOR/Job Description | Defines scope |
| F14 | สัญญา NDA (Confidentiality) | **🔴 Protects trade secrets** |
| F15 | สัญญาไม่แข่งขัน (Non-Compete) | Max 5 years |
| F16 | สัญญาจ้างที่ปรึกษา (Consultant) | Independent contractor |
| F17 | สัญญาจ้าง Outsource | Outsource labor |
| F18 | สัญญาฝึกงาน (Internship) | Intern |
| F19 | บันทึกข้อตกลงการทำงาน | Work agreement |
| F20 | หนังสือแจ้งลดค่าจ้าง | Wage reduction |
| F21 | หนังสือแจ้งย้ายตำแหน่ง | Transfer |
| F22 | หนังสือแจ้งพักงาน | Suspension |
| F23 | หนังสือแจ้งเลิกสัญญาทดลองงาน | Probation fail |

### 2.2 Accounting/Payroll Documents

| ID | Document | Use |
|---|---|---|
| F24 | สลิปเงินเดือน (Payslip) | Monthly pay |
| F25 | สมุดจ่ายค่าล่วงเวลา (OT log) | OT tracking |
| F26 | สมุดลงเวลาทำงาน (Time clock) | Attendance |
| F27 | ทะเบียนลูกจ้าง (สนร.1) | Required |
| F28 | ทะเบียนค่าจ้าง (สนร.2) | Required |
| F29 | แบบแจ้งเปลี่ยนแปลงสภาพการจ้าง (สนร.3) | Status change |
| F30-F32 | แบบ สปส./กท./ภ.ง.ด. | Tax & SS |

### 2.3 Business Contracts (Thai-style)

| ID | Document | Use |
|---|---|---|
| F33 | สัญญาซื้อขาย (Sale) | Sale of goods |
| F34 | สัญญาเช่า (Lease) | Office/warehouse |
| F35 | สัญญาเช่าซื้อ (Hire-purchase) | Car/equipment |
| F36 | สัญญาตัวแทน (Agency) | Sales agent |
| F37 | สัญญากู้ยืม (Loan) | Loan |
| F38 | สัญญาค้ำประกัน (Surety) | Guarantee |
| F39 | สัญญาจำนำ (Pledge) | Pawn |
| F40 | สัญญาจำนอง (Mortgage) | Real estate |
| F41 | สัญญา License (อนุญาตใช้สิทธิ) | IP/software |
| F42 | สัญญาแฟรนไชส์ (Franchise) | Franchise |
| F43 | สัญญาร่วมทุน (JV) | Joint venture |
| F44 | สัญญาประนีประนอม (Settlement) | Settle dispute |
| F45 | หนังสือมอบอำนาจ (POA) | Power of attorney |
| F46 | เช็ค/ตั๋วแลกเงิน/ตั๋วสัญญาใช้เงิน | Payment |
| F47 | ใบเสร็จรับเงิน (Receipt) | Receive money |
| F48 | ใบกำกับภาษี (Tax Invoice) | Tax |
| F49 | ใบเสนอราคา/ใบสั่งซื้อ (Quotation/PO) | Trade |
| F50 | ใบแจ้งหนี้ (Invoice) | Billing |

### 2.4 Court Documents (If sued)

| ID | Document | When |
|---|---|---|
| F51 | คำฟ้อง (ตัวอย่าง) (Complaint template) | If sued |
| F52 | คำให้การ (Answer template) | If sued |
| F53 | คำร้องขอเลิกจ้าง (ตัวอย่าง) | If employee sues |
| F54 | คำร้องต่อศาลแรงงาน (ตัวอย่าง) | Labor court |
| F55 | อุทรณ์/ฎีกา (แบบฟอร์ม) | Appeal |
| F56 | หนังสือร้องเรียน กรมแรงงาน | If accused |
| F57 | คำให้การต่อพนักงานตรวจแรงงาน | If inspected |

### 2.5 SSO Documents (แบบ สปส.)

| ID | Document | When |
|---|---|---|
| F58 | สปส. 1-03 (แจ้งรับลูกจ้าง) | New hire |
| F59 | สปส. 1-04 (แจ้งลาออก) | Resignation |
| F60 | สปส. 1-05 (แจ้งเลิกจ้าง) | Termination |
| F61 | สปส. 1-07 (แจ้งเปลี่ยนค่าจ้าง) | Wage change |
| F62 | สปส. 1-08 (แจ้งลูกจ้างออก) | Employee leave |
| F63 | สปส. 6-10 (เคลมประโยชน์ทดแทน) | SS benefits claim |

---

## 🛡️ Section 3: Employer Defense Knowledge (ป้องกัน "ลูกจ้างหัวหมอ")

### 3.1 Common Employee Tricks & Counter-Measures

| # | Trick | Law they cite | Counter-measure |
|---|---|---|---|
| T1 | **อ้างว่าถูกบังคับให้ลาออก** (ไม่ได้ลาออกเอง) | LPA ม.17 | ใบลาออกที่มีลายเซ็น + พยาน 2 คน + ลงวันที่ชัด |
| T2 | **อ้างว่าไม่เคยผิดวินัย** (ไม่เคยถูกเตือน) | ฎีกาทั่วไป | ต้องมีหนังสือเตือน 3 ครั้ง เก็บไว้ + ลงนามรับ |
| T3 | **อ้างว่าทำ OT แต่ไม่จ่าย** | LPA ม.61 | ระบบบันทึกเวลาเข้า-ออกที่ลูกจ้างยืนยันรายวัน |
| T4 | **อ้างว่าเลิกจ้างไม่เป็นธรรม** | LPA ม.49, 118, 122 | เหตุผลครบ + เอกสารครบ + ขั้นตอนถูก |
| T5 | **อ้างว่าถูกลดค่าจ้าง** | LPA ม.70-71 | หนังสือแจ้งล่วงหน้า 3 วัน + ความยินยอม |
| T6 | **อ้างว่าถูกคุกคาม/กลั่นแกล้ง** | OSH 2554 | นโยบายชัด + ช่องทางร้องเรียน + สอบสวนเป็นลายลักษณ์อักษร |
| T7 | **ฟ้องศาลแรงงานฟรี (เรื่องเล็ก)** | LPA วิธีพิจารณา | ต้องมีทนายฝั่งนายจ้าง + เอกสารครบ |
| T8 | **อ้างว่าไม่มีข้อบังคับ** | LPA ม.108 | ต้องแจ้ง สนร. ภายใน 15 วันหลังใช้ + เก็บหลักฐาน |
| T9 | **อ้างว่าไม่ได้รับค่าชดเชย** | LPA ม.118 | จ่าย ณ วันเลิกจ้าง + หลักฐานการจ่าย |
| T10 | **อ้างว่าถูกบังคับใจ** | ฎีกาทั่วไป | ใช้แบบฟอร์มมาตรฐาน + ลายเซ็นในที่สาธารณะ |
| T11 | **อ้างว่าถูกเลือกปฏิบัติ** | รัฐธรรมนูญ + LPA | นโยบายไม่เลือกปฏิบัติ + หลักฐานการปฏิบัติเท่าเทียม |
| T12 | **อ้างว่าถูกเลิกจ้างเพราะตั้งครรภ์** | LPA + รัฐธรรมนูญ | ห้ามเลิกจ้างหญิงตั้งครรภ์ ยกเว้นเหตุพิเศษ |
| T13 | **อ้างว่าถูกเลิกจ้างเพราะเป็นสมาชิกสหภาพ** | LRA 2518 | ห้ามเลิกจ้างเพราะสหภาพแรงงาน |
| T14 | **อ้างว่าไม่ได้รับค่าล่วงเวลา** | LPA ม.61 | บันทึก OT รายวัน + ลายเซ็นยืนยัน |
| T15 | **อ้างว่าข้อบังคับไม่เป็นธรรม** | UCTA 2540 | ตรวจสอบข้อบังคับด้วย UCTA criteria |
| T16 | **อ้างว่าถูกเลิกจ้างเพราะไปฟ้องร้อง** | LPA | ห้ามเลิกจ้างเพราะใช้สิทธิ์ตามกฎหมาย |
| T17 | **อ้างว่าถูกลงโทษทางวินัยไม่เป็นธรรม** | LPA | มีขั้นตอนลงโทษชัด + แจ้งเป็นลายลักษณ์อักษร |
| T18 | **อ้างว่าลาออกแต่ไม่ได้รับค่าจ้างค้าง** | LPA ม.70 | จ่ายค่าจ้างค้างภายใน 7 วันหลังลาออก |
| T19 | **อ้างว่าถูกบังคับให้ทำงานล่วงเวลา** | LPA + ป.อ. ม.312 | ระบบ OT ที่ลูกจ้างยินยอม + จ่าย OT ตามกฎหมาย |
| T20 | **อ้างว่าไม่ได้รับสวัสดิการ** | LPA บรรพ 4 | ให้สวัสดิการครบตามที่กฎหมายกำหนด |

### 3.2 Employer Protection Strategy

**Golden Rules for Employer Defense:**

1. ✅ **เอกสารครบ** — 14 เอกสารแรงงานตามที่กฎหมายกำหนด
2. ✅ **แจ้ง สนร. ทุกครั้ง** — ข้อบังคับ, เปลี่ยนแปลง, เลิกจ้าง
3. ✅ **เตือน 3 ขั้น** — ก่อนเลิกจ้างทุกครั้ง
4. ✅ **จ่ายค่าชดเชย ณ วันเลิกจ้าง** — ห้ามจ่ายล่าช้า (โดนปรับ 6 เท่า)
5. ✅ **ลายเซ็นชัดเจน** — ทุกเอกสารที่ลูกจ้างเซ็น ต้องมีพยาน
6. ✅ **เก็บหลักฐาน 10 ปี** — เอกสารทุกชิ้น
7. ✅ **มีทนายประจำ** — ตรวจก่อนเลิกจ้างทุกครั้ง
8. ✅ **ไม่มี "แรงงานสัมพันธ์" ที่ไม่ดี** — สร้าง positive work environment
9. ✅ **สุขภาพและความปลอดภัย** — ปฏิบัติตาม OSH 2554
10. ✅ **PDPA compliance** — ข้อมูลลูกจ้าง/ลูกค้า

---

## 🎯 Section 4: Legal Risk Assessment (5x5 Matrix)

### 4.1 Severity Scale (ความรุนแรง)

| Level | Name (TH) | Description | Example |
|-------|-----------|-------------|---------|
| 1 | **เล็กน้อย** (Negligible) | ไม่มีผลกระทบทางกฎหมาย | ใช้คำผิดในสัญญา |
| 2 | **น้อย** (Minor) | ช่องว่างเล็กน้อยในสัญญา แก้ไขง่าย | ขาดคำจำกัดความ |
| 3 | **ปานกลาง** (Moderate) | ขาด clause ที่แนะนำ ความเสี่ยงฟ้องร้องต่ำ | ไม่มี Force Majeure |
| 4 | **มาก** (Major) | น่าจะผิดกฎหมาย ความเสี่ยงฟ้องร้องสูง | Non-compete > 5 ปี |
| 5 | **วิกฤต** (Critical) | ผิดกฎหมายชัดเจน อาจถูกดำเนินคดีอาญา | ยึดบัตรประชาชน |

### 4.2 Likelihood Scale (ความน่าจะเป็น)

| Level | Name (TH) | Probability | Example |
|-------|-----------|-------------|---------|
| 1 | **ห่างไกล** (Rare) | < 5% | ไม่เคยเกิดขึ้น |
| 2 | **ไม่น่าจะเกิด** (Unlikely) | 5-25% | เคยเกิดในอุตสาหกรรมอื่น |
| 3 | **เป็นไปได้** (Possible) | 25-50% | เคยเกิดในอุตสาหกรรมเดียวกัน |
| 4 | **น่าจะเกิด** (Likely) | 50-75% | เคยเกิดในบริษัท |
| 5 | **เกือบแน่นอน** (Almost Certain) | > 75% | เกิดทุกครั้ง |

### 4.3 Risk Score = Severity × Likelihood (1-25)

| Score | Risk Level (TH) | Action | Escalation |
|-------|-----------------|--------|------------|
| 1-5 | 🟢 **ต่ำ** (Low) | ใช้ได้ | ไม่ต้อง |
| 6-10 | 🟡 **ปานกลาง** (Medium) | แนะนำแก้ไข | ผู้จัดการ |
| 11-15 | 🟠 **สูง** (High) | ส่งฝ่ายกฎหมาย | Legal team |
| 16-20 | 🔴 **สูงมาก** (Very High) | ส่งผู้บริหาร + ฝ่ายกฎหมาย | Executive + Legal |
| 21-25 | ⚫ **วิกฤต** (Critical) | **ต้องให้ทนายตรวจ** | Lawyer (mandatory) |

### 4.4 Risk Assessment Workflow

```
Step 1: ระบุปัญหา (Identify Issue)
  ↓
Step 2: ให้คะแนนความรุนแรง (Score Severity 1-5)
  ↓
Step 3: ให้คะแนมความน่าจะเป็น (Score Likelihood 1-5)
  ↓
Step 4: คำนวณ Risk Score = S × L
  ↓
Step 5: ระบุระดับสี (Color) และ Action
  ↓
Step 6: ระบุปัจจัยเสี่ยง (Risk Factors)
  ↓
Step 7: ระบุปัจจัยบรรเทา (Mitigating Factors)
  ↓
Step 8: ทางเลือก (Alternatives)
  ↓
Step 9: เรียก Escalation ที่เหมาะสม
```

### 4.5 Example: Risk Assessment Output

```markdown
## ⚠️ การประเมินความเสี่ยง: สัญญาจ้างงานนี้

**คะแนนความเสี่ยงรวม: 16/25** 🔴 **สูงมาก**

| ความเสี่ยง | ความรุนแรง | ความน่าจะเป็น | คะแนน | ระดับ |
|---|---|---|---|---|
| การจำกัดความรับผิด | 4 (Major) | 4 (Likely) | 16 | 🔴 |
| การต่ออายุอัตโนมัติ | 4 (Major) | 4 (Likely) | 16 | 🔴 |
| การบอกเลิกสัญญา | 3 (Moderate) | 3 (Possible) | 9 | 🟡 |
| ค่าสินไหมและการชดใช้ | 3 (Moderate) | 3 (Possible) | 9 | 🟡 |
| การรักษาความลับ | 2 (Minor) | 2 (Unlikely) | 4 | 🟢 |
| กฎหมายที่ใช้บังคับ | 2 (Minor) | 2 (Unlikely) | 4 | 🟢 |

**ปัจจัยเสี่ยง:**
- การจำกัดความรับผิดเกินขอบเขตที่ ป.พ.พ. ม.458 อนุญาต
- การต่ออายุอัตโนมัติอาจขัดกับหลักความยินยอม (ป.พ.พ. ม.369)
- บทลงโทษอาจถูกลดโดยศาล (ป.พ.พ. ม.383)

**ปัจจัยบรรเทา:**
- สัญญาเป็นภาษาไทย
- มีการระบุกฎหมายที่ใช้บังคับ
- มีพยานในการลงนาม

**ทางเลือก:**
1. แก้ไข clause การจำกัดความรับผิด
2. เปลี่ยนการต่ออายุอัตโนมัติเป็นต้องยินยอมทั้งสองฝ่าย
3. ระบุค่าเสียหายเป็นตัวเลขที่เหมาะสม

**⚠️ ต้องส่งเรื่องถึง: ที่ปรึกษากฎหมายอาวุโส + ที่ปรึกษากฎหมายภายนอก**
```

---

## 📋 Section 5: Contract Review Output Format (Thai-style)

### 5.1 Standard Output Structure

เมื่อตรวจสอบสัญญา ให้ใช้รูปแบบนี้:

```markdown
# 📋 ผลการตรวจสอบสัญญา [ประเภทสัญญา]

## 1. ข้อมูลทั่วไป
- **ประเภทสัญญา:** ...
- **คู่สัญญา:** ...
- **วันที่ตรวจสอบ:** ...
- **ผู้ตรวจสอบ:** Panya-AI v3.0

## 2. สรุประดับความเสี่ยง

| ระดับความเสี่ยง | จำนวน |
|---|---|
| 🔴 สูงมาก (16-25) | X ข้อ |
| 🟠 สูง (11-15) | X ข้อ |
| 🟡 ปานกลาง (6-10) | X ข้อ |
| 🟢 ต่ำ (1-5) | X ข้อ |
| **รวม** | **X ข้อ** |

## 3. ผลวินิจฉัยโดยรวม
[สรุปสั้น 2-3 บรรทัด เน้นประเด็นหลัก]

## 4. การวิเคราะห์ข้อกำหนด

| ความเสี่ยง | ระดับ | ข้อความอ้างอิง | ผลกระทบ | ข้อเสนอแนะ (กฎหมายไทย) |
|---|---|---|---|---|
| ... | ... | "...ข้อความจากสัญญา..." | ... | ... |

## 5. การตรวจสอบความครบถ้วน
- ✅ มี / ❌ ไม่มี [ข้อกำหนด]

## 6. จัดลำดับการเจรจา

### 🔴 ต้องแก้ไข (Must Fix)
- [ ] ...

### 🟠 ควรแก้ไข (Should Fix)
- [ ] ...

### 🟡 ปรับปรุงเพิ่มเติมได้ (Could Improve)
- [ ] ...

## 7. หมายเหตุเกี่ยวกับกฎหมายไทย
- **ข้อกำหนดที่อาจเป็นโมฆะ:** ...
- **ข้อกำหนดที่อาจเป็นโมฆียะ:** ...
- **ข้อกำหนดที่อาจใช้บังคับไม่ได้:** ...

## 8. การยกระดับ
- ✅ ตรวจสอบภายใน (Panya-AI) | ❌ ต้องส่งทนาย
```

### 5.2 Contract-Specific Prompts

ใช้ prompt เหล่านี้เพื่อตรวจสอบ:

```text
"ตรวจสอบสัญญาจ้างงานนี้"          → Employment contract review
"ตรวจสอบ NDA ตามกฎหมายไทย"        → NDA review
"ตรวจสอบสัญญาซื้อขาย"             → Sale contract review
"ตรวจสอบสัญญาเช่า"                 → Lease contract review
"ตรวจสอบสัญญาบริการ"               → Service contract review
"ตรวจสอบสัญญาผู้รับเหมา"           → Contractor review
"ชี้ข้อกำหนดที่มีความเสี่ยง"       → Highlight risky clauses
"สรุปเงื่อนไขสัญญา"                → Summarize contract
"เสนอข้อความแก้ไขตามกฎหมายไทย"     → Suggest Thai-law-compliant revisions
```

### 5.3 Output Example: Employment Contract Review

| ความเสี่ยง | ระดับ | ข้อเสนอแนะ (กฎหมายไทย) |
|---|---|---|
| การจำกัดความรับผิด | สูง | ตรวจสอบว่าข้อจำกัดความรับผิดไม่ขัดต่อความสงบเรียบร้อยหรือศีลธรรมอันดี และไม่เป็นการยกเว้นความรับผิดจากการจงใจหรือประมาทเลินเล่ออย่างร้ายแรง (ป.พ.พ. ม.458) |
| การต่ออายุอัตโนมัติ | สูง | กำหนดให้ต้องมีหนังสือยินยอมจากทั้งสองฝ่ายก่อนต่ออายุ หรือกำหนดสิทธิการบอกเลิกที่ชัดเจน (ป.พ.พ. ม.369) |
| การบอกเลิกสัญญา | ปานกลาง | ระบุเหตุบอกเลิก ระยะเวลาบอกกล่าว และผลของการบอกเลิกให้สอดคล้องกับประมวลกฎหมายแพ่งและพาณิชย์ (ป.พ.พ. ม.387-394) และ พ.ร.บ. คุ้มครองแรงงาน ม.17 |
| ค่าสินไหมและการชดใช้ | ปานกลาง | จำกัดขอบเขตเฉพาะความเสียหายที่เกิดจากการผิดสัญญา การกระทำโดยประมาท หรือการกระทำโดยจงใจของคู่สัญญา (ป.พ.พ. ม.383, 438) |
| การรักษาความลับ | ต่ำ | กำหนดระยะเวลาที่เหมาะสม เช่น 3–5 ปี หรือจนกว่าข้อมูลจะเป็นข้อมูลสาธารณะ (พ.ร.บ. ความลับทางการค้า 2545) |
| กฎหมายที่ใช้บังคับ | ต่ำ | ให้ใช้กฎหมายแห่งราชอาณาจักรไทย และกำหนดศาลไทยที่มีเขตอำนาจพิจารณาคดี (ศาลแรงงานสำหรับข้อพิพาทแรงงาน) |

---

## 🚨 Section 6: Escalation Rules (การยกระดับ)

### 6.1 When to Escalate

| Trigger | Escalate To |
|---------|-------------|
| Risk score 1-5 (🟢 Low) | ไม่ต้อง — ใช้ได้เลย |
| Risk score 6-10 (🟡 Medium) | ผู้จัดการฝ่ายบริหาร (HR Manager) |
| Risk score 11-15 (🟠 High) | ฝ่ายกฎหมายภายใน (Legal Department) |
| Risk score 16-20 (🔴 Very High) | ที่ปรึกษากฎหมายอาวุโส + ผู้บริหาร |
| Risk score 21-25 (⚫ Critical) | **ที่ปรึกษากฎหมายภายนอก (mandatory)** |
| Termination of senior employee | ที่ปรึกษากฎหมายภายนอก |
| Mass termination (≥ 10 คน) | คณะกรรมการบริหาร + ทนาย |
| Labor court case | ทนายแรงงาน (mandatory) |
| Criminal charge against employee | ทนายอาญา (mandatory) |
| Labor inspection (พนักงานตรวจแรงงาน) | ฝ่ายกฎหมาย + HR |
| PDPA breach reported | DPO + ทนาย |

### 6.2 Escalation Workflow

```
[User Request]
   ↓
[Panya-AI Analysis]
   ↓
[Risk Score Calculated]
   ↓
   ├── Score ≤ 10 → Return result to user
   ├── Score 11-15 → Recommend legal review + provide red flags
   ├── Score 16-20 → MANDATORY: refer to senior legal counsel
   └── Score ≥ 21 → MANDATORY: refer to external lawyer + DO NOT proceed without approval
```

### 6.3 Common Risk Patterns (ต้องระวัง)

| Pattern | Severity | Why |
|---------|----------|-----|
| ห้ามลาออก (No resignation allowed) | 5 | ผิด LPA ม.17 |
| ยึดบัตรประชาชน (Confiscate ID card) | 5 | ผิด ป.อ. |
| ปรับลูกจ้าง (Fine employee) | 4 | น่าจะผิด LPA |
| ห้ามแต่งงาน/ตั้งครรภ์ | 5 | เลือกปฏิบัติ |
| Non-compete > 5 ปี | 4 | น่าจะเกินจำเป็น |
| NDA ไม่มีกำหนดเวลา | 3 | ไม่สมเหตุสมผล |
| สละสิทธิ์ลูกจ้างทั้งหมด | 5 | โมฆะตาม LPA |
| ไม่มี PDPA clause | 3 | น่าจะผิด PDPA |
| ไม่มี Force Majeure | 2 | แนะนำ |
| ไม่มี Termination clause | 3 | Default rules apply |
| ค่าเสียหาย > ความเสียหายจริง | 3 | ศาลอาจลด |
| บอกเลิกฝ่ายเดียว (เฉพาะนายจ้าง) | 3 | ไม่เป็นธรรมตาม UCTA |
| ไม่มี PDPA consent | 4 | ผิด PDPA |
| เก็บข้อมูลส่วนบุคคลเกินจำเป็น | 3 | ผิด PDPA principle |
| ไม่แจ้งลูกจ้างเมื่อเก็บข้อมูล | 4 | ผิด PDPA |
| ข้อบังคับไม่ได้แจ้ง สนร. | 4 | ผิด LPA ม.108 |
| ไม่มีหนังสือเตือนก่อนเลิกจ้าง | 4 | เลิกจ้างไม่เป็นธรรม |
| จ่ายค่าชดเชยล่าช้า | 4 | โดนปรับ 6 เท่า (LPA ม.123) |
| ไม่จ่าย OT | 4 | ผิด LPA ม.61 |
| บังคับให้ลาออก | 5 | ผิด LPA ม.17 |

---

## 🗄️ Section 7: Database Schema (Recommended)

### 7.1 Existing Tables (Layer 1)
```sql
sources, laws, law_sections, case_judgments, case_law_links, ingestion_log, rag_chunks
```

### 7.2 New Tables for Knowledge Layer (Layer 2-3)

```sql
-- ========== Layer 2: Knowledge Base ==========

-- Clause Library: 300-500 standard clauses
CREATE TABLE clauses (
  clause_id INTEGER PRIMARY KEY,
  clause_name TEXT NOT NULL,
  clause_name_th TEXT,
  category TEXT,                       -- Employment, NDA, Service, Lease, Loan
  purpose TEXT,
  mandatory INTEGER DEFAULT 0,
  risk_if_missing TEXT,
  related_law_ids TEXT,
  related_section_ids TEXT,
  related_judgment_ids TEXT,
  sample_good TEXT,
  sample_bad TEXT,
  typical_position TEXT,
  alternatives TEXT,
  tags TEXT,
  notes TEXT
);

-- Compliance Checklist: per contract type
CREATE TABLE checklists (
  checklist_id INTEGER PRIMARY KEY,
  contract_type TEXT NOT NULL,
  item_text TEXT NOT NULL,
  item_category TEXT,
  is_required INTEGER DEFAULT 1,
  related_clause_id INTEGER,
  related_law_id INTEGER,
  related_section_id INTEGER,
  risk_level TEXT,
  notes TEXT,
  FOREIGN KEY (related_clause_id) REFERENCES clauses(clause_id),
  FOREIGN KEY (related_law_id) REFERENCES laws(law_id)
);

-- Standard Contract Templates
CREATE TABLE contract_templates (
  template_id INTEGER PRIMARY KEY,
  contract_type TEXT NOT NULL,
  variant TEXT,
  title TEXT,
  content TEXT,
  source TEXT,
  source_url TEXT,
  industry TEXT,
  is_anonymized INTEGER DEFAULT 1,
  version TEXT,
  created_at TEXT
);

-- Legal Terminology Dictionary
CREATE TABLE legal_terms (
  term_id INTEGER PRIMARY KEY,
  term_th TEXT NOT NULL,
  term_en TEXT,
  synonyms TEXT,
  definition TEXT,
  category TEXT,
  related_law_ids TEXT,
  related_section_ids TEXT,
  notes TEXT
);

-- Legal Opinions (from government agencies)
CREATE TABLE legal_opinions (
  opinion_id INTEGER PRIMARY KEY,
  source_agency TEXT,
  title TEXT,
  opinion_text TEXT,
  question TEXT,
  answer TEXT,
  issue_date TEXT,
  source_url TEXT,
  related_law_ids TEXT,
  related_section_ids TEXT,
  tags TEXT
);

-- Industry Rules
CREATE TABLE industry_rules (
  rule_id INTEGER PRIMARY KEY,
  industry TEXT,
  rule_text TEXT,
  related_law_ids TEXT,
  typical_clauses TEXT,
  risk_patterns TEXT,
  notes TEXT
);

-- ========== Layer 3: Decision Rules ==========

-- Risk Matrix: Risk patterns
CREATE TABLE risk_rules (
  rule_id INTEGER PRIMARY KEY,
  rule_name TEXT NOT NULL,
  rule_description TEXT,
  rule_type TEXT,
  pattern TEXT,
  severity INTEGER,
  likelihood INTEGER,
  risk_score INTEGER,
  escalation TEXT,
  related_law_ids TEXT,
  related_section_ids TEXT,
  recommendation TEXT,
  applies_to_contract_types TEXT
);

-- Citation Graph
CREATE TABLE citation_graph (
  citation_id INTEGER PRIMARY KEY,
  source_type TEXT,
  source_id INTEGER,
  target_type TEXT,
  target_id INTEGER,
  relation_type TEXT,
  notes TEXT
);

-- ========== System ==========
CREATE TABLE schema_version (
  version TEXT PRIMARY KEY,
  applied_at TEXT DEFAULT CURRENT_TIMESTAMP,
  notes TEXT
);
```

---

## 📊 Section 8: Data Sources

### 8.1 Statutory Text Sources

| Source | URL | License | Use |
|--------|-----|---------|-----|
| law.go.th (กฤษฎีกา) | https://law.go.th | Public domain | All Thai laws, full text |
| law.go.th API | `https://apig.law.go.th/dga-user-service-phase2/law/detail/{id}` | Public domain | Programmatic fetch |
| Royal Gazette | https://ratchakitcha.soc.go.th | Public domain | Original text |
| Krisdika | https://www.krisdika.go.th | Public domain | Council of State |
| PyThaiNLP/thai-law | https://huggingface.co/datasets/pythainlp/thailaw | Public domain | 42,755 rows |

### 8.2 Case Law Sources

| Source | URL | Coverage | License |
|--------|-----|----------|---------|
| ศาลฎีกา (deka.supremecourt.or.th) | http://deka.supremecourt.or.th/ | ฎีกาทั้งหมด | Public domain (gov) |
| ThaiDeka | https://deka.in.th/ | 5,791+ labor cases | Verify terms |
| กระทรวงแรงงาน | https://ops.mol.go.th/sentence | 4,326 labor pages | Public domain |
| TSCC Dataset | https://github.com/KevinMercury/tscc-dataset | 1,207 criminal | **Academic only** |
| Open Law Data Thailand | https://www.openlawdatathailand.org/ | 1.34M+ documents | Per-document |

### 8.3 Government Opinions & Guidelines

| Source | URL | Use |
|--------|-----|-----|
| คำวินิจฉัย คตร. | https://www.krisdika.go.th | Law interpretation |
| ประกาศกระทรวงแรงงาน | https://www.mol.go.th | Min wage, OT, WFH |
| คำวินิจฉัยกรมสวัสดิการและคุ้มครองแรงงาน | https://www.dlp.go.th | DLP opinions |
| PDPC Guidelines | https://www.pdpc.go.th | PDPA implementation |
| ความเห็นกฤษฎีกา | https://www.krisdika.go.th | Legal interpretation |

### 8.4 Standard Contracts & Templates

| Source | URL | Use |
|--------|-----|-----|
| DBD | https://www.dbd.go.th | Standard contract templates |
| BOI | https://www.boi.go.th | Investment contracts |
| DIPW | https://www.ipthailand.go.th | IP license templates |

---

## 🔍 Section 9: Data Fetch Workflow

### 9.1 Fetch Statutory Texts (Tier 1 — Critical)

For laws on PyThaiNLP (fastest):
```python
from datasets import load_dataset
ds = load_dataset("pythainlp/thailaw", split="train")
# Search by sysid or title
```

For laws NOT on PyThaiNLP, use law.go.th via browser automation:
- Navigate to `https://law.go.th/DetailLawPage?table_of_law_id=XXXX`
- Select latest consolidated version
- Extract all section texts

### 9.2 Fetch Case Law (Tiered)

Priority:
1. **Labor cases (1,000-2,000)** — deka.in.th, ops.mol.go.th
2. **Civil contract cases (2,000-5,000)** — deka.supremecourt.or.th
3. **Criminal contract-related (500-1,000)** — deka.supremecourt.or.th

**Tag by issue:**
- จ้างแรงงาน, ซื้อขาย, เช่า, กู้ยืม, ค้ำประกัน, ตัวแทน, จ้างทำของ
- หุ้นส่วน, บริษัท, ละเมิด, ฉ้อโกง, ยักยอก

### 9.3 Build Knowledge Layer

#### Clause Library (300-500 clauses)
- Termination, Force Majeure, Confidentiality, IP Ownership, Non-Compete
- Non-Solicitation, Payment, Warranty, Indemnity, Limitation of Liability
- Assignment, Severability, Entire Agreement, Jurisdiction, Governing Law
- Notice, Penalty, Liquidated Damage, Inspection, Acceptance
- Change Order, Escrow, Data Protection, PDPA, Security
- Compliance, Audit Right, Arbitration

#### Compliance Checklists
- Employment: Probation, Salary, OT, Leave, Welfare, Confidentiality, PDPA, Termination
- NDA: Confidential Information, Exceptions, Duration, Return
- Lease: Rent, Deposit, Repair, Termination, Handover
- Loan: Principal, Interest, Repayment, Default, Security

#### Risk Rules (50+ patterns)
- IF Penalty > Actual Damage → Critical
- IF No Governing Law → Medium
- IF Waive Employee Rights → Critical
- IF No PDPA → High
- IF Non-compete > 5 years → High

### 9.4 Build RAG Chunks

For each section/judgment/opinion/clause — create 1 chunk in `rag_chunks` table.

---

## 🚀 Section 10: Deployment (Vercel + Turso)

### 10.1 Why Turso?

SQLite files do NOT work on Vercel serverless — no persistent filesystem.

Turso:
- SQLite-compatible (minimal Prisma schema changes)
- Free tier: 500 databases, 9 GB total, 1 billion row reads/month
- Edge network
- Easy migration from local SQLite

### 10.2 Migration Steps

```bash
# 1. Install Turso CLI
powershell -ExecutionPolicy Bypass -c "irm https://github.com/tursodatabase/turso/releases/latest/download/turso_cli-installer.ps1 | iex"

# 2. Login + create database
turso auth login
turso db create panya-ai --location sin

# 3. Get connection + token
turso db show panya-ai --url
turso db tokens create panya-ai

# 4. Import existing SQLite
turso db shell panya-ai < prisma/thai_legal_db.sqlite

# 5. Update .env
DATABASE_URL=libsql://panya-ai-<your-account>.turso.io
TURSO_AUTH_TOKEN=<your-token>

# 6. Switch Prisma to libsql
bun add @prisma/adapter-libsql @libsql/client
```

### 10.3 Vercel Deployment

1. Push code to GitHub
2. Go to vercel.com → Import Project
3. Set Environment Variables:
   - `DATABASE_URL` = libsql://...turso.io
   - `TURSO_AUTH_TOKEN` = ...
   - `Z_AI_API_KEY` = (for AI features)
4. Deploy

### 10.4 Alternative: Supabase (PostgreSQL)

- Free tier: 500 MB database, 50,000 MAU
- Requires Prisma schema migration

---

## 📜 Section 11: License & Compliance

| Source | License | Commercial use? |
|--------|---------|----------------|
| law.go.th content | Public domain | ✅ Yes |
| Supreme Court judgments | Public domain | ✅ Yes |
| PyThaiNLP/thai-law | Public domain | ✅ Yes |
| TSCC Dataset | **Academic only** | ❌ **NO — RAG use only** |
| ThaiDeka | Verify terms | ⚠️ Verify |
| Open Law Data Thailand | Per-document | ⚠️ Verify |
| Standard templates (DBD, BOI) | Public domain | ✅ Yes |

**For commercial deployment:**
- ❌ Do NOT include TSCC data in production
- ✅ Use only deka.in.th / ops.mol.go.th / law.go.th
- ⚠️ Always display source attribution
- ⚠️ Add disclaimer: "AI provides information for educational purposes, not legal advice"

---

## 📅 Section 12: Update & Versioning

- Every record has: `effective_date`, `repealed_date`, `version`, `source_url`
- Run update pipeline monthly
- Tag records with `as_of_date`
- Display "ข้อมูล ณ วันที่ YYYY-MM-DD" in AI responses

---

## 🛣️ Section 13: Roadmap

### Phase 1: Current (✅ Done)
- 14 laws, 4,441 sections, 1,258 judgments
- FTS5 search
- AI RAG with citation
- Next.js web app

### Phase 2: Tier 1 Expansion (2-4 weeks)
- [ ] Add 11 new Tier 1 laws (UCTA, PDPA, Trade Secrets, OSH, etc.)
- [ ] Add 1,000+ more labor judgments
- [ ] Add Labor Court judgments
- [ ] Add 100+ government legal opinions
- [ ] Add 23 employment document templates
- [ ] Add 18 business contract templates

### Phase 3: Knowledge Layer (4-8 weeks)
- [ ] Build Clause Library (300+ clauses)
- [ ] Build Compliance Checklists (10+ contract types)
- [ ] Build Risk Rules (50+ patterns)
- [ ] Build Standard Contract Templates (50+ templates)
- [ ] Build Employer Defense Knowledge Base (20+ tricks)

### Phase 4: Enterprise Features (8-16 weeks)
- [ ] Legal Knowledge Graph
- [ ] Citation Graph
- [ ] Legal Issue Taxonomy with ML classification
- [ ] Industry Rules (5+ industries)
- [ ] Anonymized Contract Dataset (300-500 samples)
- [ ] Risk Assessment Engine
- [ ] Escalation Rules Engine

### Phase 5: Deployment & Scale
- [ ] Turso/Supabase backend
- [ ] Vercel deployment
- [ ] CI/CD with auto-data-update pipeline
- [ ] Monitoring & analytics

---

## 📁 Section 14: File Structure

```
panya-ai/
├── prisma/
│   ├── schema.prisma              # Current (SQLite file)
│   └── schema.turso.prisma        # Vercel variant (libsql)
├── scripts/
│   ├── rebuild_legal_db.py        # Build SQLite from sources
│   ├── import_to_turso.sh         # Migrate to Turso
│   └── fetch_*.py                 # Per-source fetchers
├── src/
│   ├── app/
│   │   ├── api/                   # 7+ API routes
│   │   └── page.tsx               # Main SPA
│   ├── components/
│   └── lib/
│       ├── rag.ts                 # RAG retrieval
│       ├── risk_assessment.ts     # Risk matrix calculator
│       ├── contract_review.ts     # Contract analyzer
│       └── employer_defense.ts    # Anti-trick knowledge
├── data/                          # Generated (gitignored)
│   └── thai_legal_db.sqlite
├── knowledge/                     # Knowledge Layer data (JSON)
│   ├── clauses.json
│   ├── checklists.json
│   ├── risk_rules.json
│   ├── contract_templates/
│   ├── employer_tricks.json
│   └── labor_documents/
├── .env.example
├── .gitignore
├── README.md
├── DEPLOYMENT.md
├── SKILL.md                       # This file
└── package.json
```

---

## 🎓 Section 15: Examples

### Example 1: Review Employment Contract

```text
User: "ตรวจสอบสัญญาจ้างงานนี้"

Panya-AI Output:
# 📋 ผลการตรวจสอบสัญญาจ้างงาน

## สรุประดับความเสี่ยง
| ระดับความเสี่ยง | จำนวน |
|---|---|
| 🔴 สูงมาก (16-25) | 2 |
| 🟠 สูง (11-15) | 1 |
| 🟡 ปานกลาง (6-10) | 2 |
| 🟢 ต่ำ (1-5) | 1 |

[detailed analysis...]

⚠️ ต้องส่งเรื่องถึง: ที่ปรึกษากฎหมายอาวุโส
```

### Example 2: Risk Assessment for Termination

```text
User: "จะเลิกจ้างพนักงานที่ขโมยของบริษัท — ควรทำอย่างไร?"

Panya-AI Output:
# 🎯 การประเมินความเสี่ยง: การเลิกจ้างกรณีขโมย

## คะแนนความเสี่ยง: 8/25 (ปานกลาง)

| ปัจจัย | คะแนน |
|---|---|
| พยานหลักฐานชัดเจน | ✅ มี |
| หนังสือเตือน 3 ครั้ง | ❌ ไม่มี |
| ข้อบังคับเกี่ยวกับการทำงานครอบคลุม | ✅ มี |

## คำแนะนำ:
1. รวบรวมหลักฐานการขโมย (CCTV, พยาน, เอกสาร)
2. สอบสวนเป็นลายลักษณ์อักษร
3. ⚠️ ถ้าไม่มีหนังสือเตือน — แนะนำเตือน 1 ครั้งก่อน + บันทึก
4. เลิกจ้างโดยจ่ายค่าชดเชย (กรณีทำผิด = ไม่ต้องจ่าย ถ้ามีหลักฐานครบ)
5. แจ้ง สนร./สปส. ภายใน 7 วัน

⚠️ ต้องส่งเรื่องถึง: HR Manager + Legal
```

### Example 3: NDA Review

```text
User: "ตรวจสอบ NDA ตามกฎหมายไทย"

Panya-AI Output:
# 📋 ผลการตรวจสอบ NDA

## ความเสี่ยงที่พบ:

| ความเสี่ยง | ระดับ | ข้อเสนอแนะ |
|---|---|---|
| ระยะเวลา NDA ไม่จำกัด | 🟠 สูง | จำกัด 3-5 ปี |
| ไม่มีข้อยกเว้นข้อมูลสาธารณะ | 🟡 ปานกลาง | เพิ่มข้อยกเว้น |
| ไม่มีบทลงโทษชัดเจน | 🟠 สูง | ระบุค่าเสียหาย |
| ไม่อ้าง พ.ร.บ. ความลับทางการค้า | 🟡 ปานกลาง | เพิ่มการอ้างอิง |
```

---

## 🔗 Section 16: Cross-References

- **LPA ม.17** → การบอกเลิกสัญญา (Employee cannot be forced to resign)
- **LPA ม.108** → ข้อบังคับเกี่ยวกับการทำงาน (Work rules must be filed with สนร.)
- **LPA ม.118** → ค่าชดเชย (Severance must be paid on termination day)
- **LPA ม.123** → ค่าชดเชยล่าช้า = โดนปรับ 6 เท่า
- **CCC ม.369** → สัญญาต่างตอบแทน
- **CCC ม.387-394** → การบอกเลิกสัญญา
- **CCC ม.420-452** → ละเมิด
- **CCC ม.458** → ขีดจำกัดความรับผิด
- **CCC ม.575-586** → สัญญาจ้างแรงงาน
- **CCC ม.587-605** → สัญญาจ้างทำของ
- **Penal Code ม.335-336** → ลักทรัพย์
- **Penal Code ม.341-348** → ฉ้อโกง
- **Penal Code ม.352-354** → ยักยอก
- **Penal Code ม.376-377** → ล่วงละเมิดทางเพศ
- **UCTA 2540** → ข้อสัญญาที่ไม่เป็นธรรม
- **PDPA 2562** → คุ้มครองข้อมูลส่วนบุคคล
- **OSH 2554** → ความปลอดภัย อาชีวอนามัย
- **Trade Secrets 2545** → ความลับทางการค้า

---

**📌 Last updated**: 2026-07-27 15:55 (GMT+7)  
**📌 Version**: 3.0 (upgraded from 2.0)  
**📌 Author**: Panya-AI Team  
**📌 License**: MIT

---

## Section 17: Employer-Side Advisory Skills (ฝั่งนายจ้าง) ⭐⭐⭐⭐⭐

### 17.1 Mission Statement
Panya-AI เป็นที่ปรึกษากฎหมายฝั่ง **นายจ้าง/บริษัท/ผู้ประกอบการ** โดยเฉพาะ

**หลักการ:**
1. **ตอบความจริงเท่านั้น** — ผิดคือผิด ถูกคือถูก ห้ามพูดเอาใจ
2. **ถ้านายจ้างผิด** → หาแนวทางช่วยเหลือจาก "หนัก" ให้เป็น "เบา" ลดความเสียหายให้น้อยที่สุด
3. **ถ้านายจ้างถูก** → ประเมินปัญหาที่อาจเกิดขึ้นล่วงหน้า แล้วเตือนเผื่อไว้ก่อน (pre-emptive warning)
4. **ไม่พูดเอาใจ** — ห้ามตอบสองแง่สองง่ามเพื่อไม่ให้ผู้ใช้ไม่พอใจ
5. **บอก "ทุกอย่างขึ้นอยู่กับสถานการณ์" เฉพาะเมื่อจริงๆ** — ถ้ามีคำตอบชัดเจน ให้ตอบชัดเจน

### 17.2 Response Structure (4 ส่วน)
ทุกคำตอบต้องมี 4 ส่วน:

1. **คำตอบโดยตรง** — ตอบสั้นๆ ว่าถูก/ผิด/เสี่ยง อย่างไร
2. **เหตุผลทางกฎหมาย** — อ้างอิงมาตรา/ฎีกา พร้อมเลข [N]
3. **แนวทางปฏิบัติ** — ขั้นตอนที่นายจ้างควรทำ (เฉพาะฝั่งนายจ้าง)
4. **คำเตือนล่วงหน้า** — ปัญหาที่อาจเกิดขึ้น พร้อมวิธีป้องกัน

### 17.3 Common Employer Scenarios

#### สถานการณ์ A: ลูกจ้างหัวหมอ (Employee gaming the system)
- ลูกจ้างแกล้งป่วยเพื่อหลีกเลี่ยงงาน → ต้องเก็บหลักฐาน (ใบรับรองแพทย์, ประวัติการลา)
- ลูกจ้างทำงานช้าลงหลังรู้ว่าจะถูกเลิกจ้าง → ต้องมี KPI และบันทึกผลงาน
- ลูกจ้างกล่าวหานายจ้างเพื่อต่อรอง → ต้องบันทึกทุกการสื่อสาร
- ลูกจ้างใช้สิทธิ์ลาอย่างไม่เหมาะสม → ต้องมีระเบียบการลาชัดเจน

#### สถานการณ์ B: กรมแรงงานเอื้อประโยชน์กับแรงงานเกินไป
- พนักงานตรวจแรงงานตีความกฎหมายเข้าข้างลูกจ้าง → ต้องรู้สิทธิ์ในการโต้แย้ง
- คำสั่งทางปกครองที่ไม่เป็นธรรม → สามารถอุทธรณ์ได้ภายใน 30 วัน
- การไกล่เกลี่ยที่ไม่เป็นธรรม → สามารถปฏิเสธได้ และให้ศาลแรงงานพิจารณา

#### สถานการณ์ C: ลูกจ้างฟ้องศาลแรงงาน
- ลูกจ้างฟ้องเรียกค่าชดเชย → ต้องเตรียมหลักฐาน F5-F7 (หนังสือเตือน)
- ลูกจ้างอ้างการเลิกจ้างไม่เป็นธรรม → ต้องมีเหตุผลที่ชัดเจนตาม ม.119
- ลูกจ้างเรียกค่าเสียหายเกินจริง → ต้องมีหลักฐานค่าจ้างจริง

### 17.4 Employer Defense Knowledge Base

#### 20 Trick ที่ลูกจ้างชอบใช้ + วิธีป้องกัน
| # | Trick ของลูกจ้าง | วิธีป้องกันของนายจ้าง |
|---|----------------|-------------------|
| 1 | แกล้งป่วยเพื่อหลีกเลี่ยงงาน | เก็บใบรับรองแพทย์ + ตรวจสอบความถี่การลา |
| 2 | ทำงานช้าลงหลังรู้ว่าจะถูกเลิกจ้าง | มี KPI รายเดือน + บันทึกผลงาน |
| 3 | กล่าวหานายจ้างละเมิดทางเพศ | มีพยาน + กล้องวงจรปิดในที่ทำงาน |
| 4 | อ้างการเลิกจ้างไม่เป็นธรรม | มี F4 (ระเบียบวินัย) + F5-F7 (หนังสือเตือน) |
| 5 | เรียกค่าชดเชยเกินกว่าที่กฎหมายกำหนด | คำนวณตาม ม.118 + เก็บสลิปเงินเดือน |
| 6 | อ้างว่าทำงานล่วงเวลาแต่ไม่ได้รับค่าจ้าง | มีสมุดลงเวลา (F26) + อนุมัติ OT |
| 7 | ฟ้องหลังลาออกไปแล้ว | อยู่ในอายุความ 2 ปี (ม.193/34 ป.พ.พ.) |
| 8 | อ้างว่าถูกบังคับให้ลาออก | มี F10 (ใบลาออก) ที่ลูกจ้างเซ็นเอง |
| 9 | ไปร้องเรียนกรมแรงงานก่อนฟ้องศาล | ส่งตัวแทนไปชี้แจง + เก็บหลักฐาน |
| 10 | อ้างว่านายจ้างไม่จ่ายเงินสมทบ สปส. | เก็บหลักฐานการส่งเงินสมทบ (F30) |
| 11 | ทำลายเอกสารสำคัญก่อนออก | สำรองเอกสารดิจิทัล + จำกัดสิทธิ์การเข้าถึง |
| 12 | ขโมยข้อมูลลูกค้า/ความลับทางการค้า | มี F14 (NDA) + จำกัดสิทธิ์การเข้าถึงข้อมูล |
| 13 | ไปทำงานกับคู่แข่ง | มี F15 (Non-Compete) — แต่ห้ามเกิน 5 ปี |
| 14 | ยักยอกเงินบริษัท | ตรวจสอบบัญชีเป็นประจำ + มีระบบ audit |
| 15 | ปลอมเอกสารเพื่อขอเงิน | ตรวจสอบเอกสารก่อนจ่าย + มีระบบ approval |
| 16 | อ้างว่าเป็นพนักงานประจำ แต่จริงๆ เป็นชั่วคราว | มีสัญญาจ้างชัดเจน (F1 หรือ F17) |
| 17 | อ้างว่าทำงานเกินเวลาที่กำหนด | มีสัญญาจ้างระบุเวลาทำงานชัดเจน |
| 18 | ฟ้องคดีแพ่งเรียกค่าเสียหายเพิ่ม | อ้าง ม.118 พ.ร.บ.คุ้มครองแรงงาน (จำกัดความรับผิด) |
| 19 | ไปแจ้งความอาญา (ฉ้อโกง/ยักยอก) | เก็บหลักฐานการเงินที่ชัดเจน + มีทนายความ |
| 20 | ใช้สื่อสังคมออนไลน์ทำลายชื่อเสียง | มีหลักฐาน + ฟ้องหมิ่นประมาท (ป.อ. ม.326-328) |

#### 10 Golden Rules สำหรับนายจ้าง
1. **ทุกอย่างต้องเป็นลายลักษณ์อักษร** — ไม่มีสัญญา = แพ้คดี
2. **เตือนก่อนเลิกจ้าง** — F5→F6→F7 ก่อน F8 เสมอ
3. **จ่ายค่าชดเชย ณ วันเลิกจ้าง** — เลยกำหนด = เสียดอกเบี้ย 15%/ปี
4. **เก็บหลักฐานทุกอย่าง** — สลิปเงินเดือน, สมุดลงเวลา, หนังสือเตือน
5. **มีระเบียบวินัยพนักงาน** — F4 ต้องมี ไม่งั้นเลิกจ้างไม่ได้
6. **ยื่น สนร. ภายใน 15 วัน** — เมื่อมีพนักงาน ≥10 คน
7. **ส่งเงินสมทบ สปส. ทุกเดือน** — ไม่ส่ง = โดนปรับ + ฟ้อง
8. **ห้ามยึดบัตรประชาชน** — ผิดกฎหมาย (ป.อ. ม.310 กักขังหน่วงเหนี่ยว)
9. **ห้ามบังคับ OT โดยไม่จ่าย** — ผิดกฎหมาย (ป.อ. ม.312 บังคับให้ทำงาน)
10. **ปรึกษาทนายความก่อนเลิกจ้าง** — ค่าทนายถูกกว่าค่าชดเชยที่ผิด

---

## Section 18: Contract Review & Risk Assessment Skills ⭐⭐⭐⭐⭐

### 18.1 Contract Review Workflow
เมื่อผู้ใช้ส่งสัญญามาตรวจ ให้ทำตามขั้นตอน:

1. **ระบุประเภทสัญญา** — จ้างงาน/ทดลองงาน/NDA/ซื้อขาย/เช่า/กู้ยืม/...
2. **เช็ค Checklist ตามประเภท** — ใช้ Checklist จาก Section 6
3. **หา Clause ที่ขาด** — เปรียบเทียบกับ Clause Library
4. **หา Clause ที่ผิดกฎหมาย** — เช็คกับ Risk Patterns
5. **ประเมิน Risk Score** — Severity × Likelihood (1-25)
6. **แนะนำการแก้ไข** — เฉพาะฝั่งนายจ้าง

### 18.2 Risk Assessment Matrix (5×5)

| Severity ↓ \ Likelihood → | 1 Rare | 2 Unlikely | 3 Possible | 4 Likely | 5 Almost Certain |
|---|---|---|---|---|---|
| **1 Negligible** | 1 ✅ | 2 ✅ | 3 ✅ | 4 ✅ | 5 ⚠️ |
| **2 Minor** | 2 ✅ | 4 ✅ | 6 ⚠️ | 8 ⚠️ | 10 ⚠️ |
| **3 Moderate** | 3 ✅ | 6 ⚠️ | 9 ⚠️ | 12 🔴 | 15 🔴 |
| **4 Major** | 4 ✅ | 8 ⚠️ | 12 🔴 | 16 🔴 | 20 🔴 |
| **5 Critical** | 5 ⚠️ | 10 ⚠️ | 15 🔴 | 20 🔴 | 25 🔴 |

**Risk Score → Action:**
- 1-5: ✅ ใช้งานได้
- 6-10: ⚠️ แจ้งผู้จัดการ — ตรวจสอบเพิ่ม
- 11-15: 🔴 ส่งฝ่ายกฎหมาย
- 16-20: 🔴 ส่งผู้บริหาร + ฝ่ายกฎหมาย
- 21-25: 🔴 **ต้องให้ทนายความตรวจ**

### 18.3 Risk Patterns (Thai Law Specific)

#### 🔴 Critical Risk (Severity 5)
| Pattern | กฎหมายที่ขัด | ผลกระทบ |
|---------|------------|--------|
| ห้ามลาออก | ป.พ.พ. ม.383 (เสรีภาพในการทำงาน) | เป็นโมฆะ + ฟ้องได้ |
| ยึดบัตรประชาชน | ป.อ. ม.310 (กักขังหน่วงเหนี่ยว) | ความผิดอาญา |
| ห้ามแต่งงาน/ตั้งครรภ์ | รัฐธรรมนูญ ม.27 (ความเสมอภาค) | เป็นโมฆะ + ฟ้องได้ |
| ปรับลูกจ้างเกินจริง | พ.ร.บ.คุ้มครองแรงงาน ม.75 | ศาลลดได้ |
| ยกเว้นความรับผิดทั้งหมด | พ.ร.บ.ว่าด้วยข้อสัญญาที่ไม่เป็นธรรม 2540 | เป็นโมฆะ |
| บังคับ OT โดยไม่จ่าย | ป.อ. ม.312 (บังคับให้ทำงาน) | ความผิดอาญา |

#### 🟠 High Risk (Severity 4)
| Pattern | กฎหมายที่เกี่ยวข้อง | ผลกระทบ |
|---------|----------------|--------|
| Non-Compete > 5 ปี | ป.พ.พ. ม.168 (เกินสมควร) | ศาลตัดทอนได้ |
| NDA ตลอดชีวิต | พ.ร.บ.ความลับทางการค้า 2545 | อาจไม่สมเหตุสมผล |
| ไม่มี PDPA clause | พ.ร.บ. PDPA 2562 | ปรับสูงสุด 5 ล้านบาท |
| ทดลองงาน > 119 วัน | พ.ร.บ.คุ้มครองแรงงาน ม.10 | ต้องจ่ายค่าชดเชย |
| ไม่มี Termination Clause | ป.พ.พ. ม.582 | ใช้กฎหมายทั่วไป (ไม่ชัดเจน) |

### 18.4 Contract Template PDF Export
Panya-AI รองรับการส่ง contract template เป็น PDF พร้อมกรอกข้อมูลพนักงาน:

**API:** `GET /api/templates/pdf?id={templateId}&employee={name}&position={pos}&startDate={date}&salary={amount}`

**Features:**
- แปลง Markdown → HTML → PDF (ผ่าน browser print)
- กรอกชื่อพนักงานอัตโนมัติในช่องว่าง
- กรอกตำแหน่ง, วันเริ่มงาน, เงินเดือน
- ปุ่ม "พิมพ์/บันทึกเป็น PDF" ในหน้า HTML

**Workflow:**
1. User ขอ template: "ขอสัญญาจ้างงาน"
2. Agent แสดงรายการ templates (F1-F65)
3. User เลือก template + ระบุชื่อพนักงาน
4. Agent ส่งลิงก์ PDF: `/api/templates/pdf?id=1&employee=นายสมชาย`
5. User เปิดลิงก์ → กดปุ่มพิมพ์ → ได้ PDF

---

## Section 19: Latest Supreme Court Judgments (2565-2568) ⭐⭐⭐⭐

### 19.1 Data Source
ฎีกาล่าสุดดึงจาก **deka.in.th** (เพราะ deka.supremecourt.or.th ถูก WAF บล็อก)

### 19.2 Added Judgments (G503-G514)
12 ฎีกาล่าสุดปี 2565-2568:

| ID | เลขคดี | ปี | ประเด็น |
|----|--------|-----|---------|
| G503 | 8320/2568 | 2568 | ม.118/1 วรรคสอง — คุ้มครองลูกจ้างอายุ 60+ |
| G504 | 3114/2567 | 2567 | (ดูในฐานข้อมูล) |
| G505 | 4468/2566 | 2566 | (ดูในฐานข้อมูล) |
| G506 | 62/2565 | 2565 | (ดูในฐานข้อมูล) |
| G507 | 3805/2566 | 2566 | (ดูในฐานข้อมูล) |
| G508 | 1875/2566 | 2566 | (ดูในฐานข้อมูล) |
| G509 | 3081/2567 | 2567 | (ดูในฐานข้อมูล) |
| G510 | 3113/2567 | 2567 | (ดูในฐานข้อมูล) |
| G511 | 3150/2568 | 2568 | (ดูในฐานข้อมูล) |
| G512 | 3113/2567 | 2567 | (ดูในฐานข้อมูล) |
| G513 | 3116/2567 | 2567 | (ดูในฐานข้อมูล) |
| G514 | 61/2565 | 2565 | คำวินิจฉัย |

### 19.3 Employer-Favorable Classification (Future)
แผนการเพิ่ม field `case_outcome` ในตาราง judgments:
- `employer_won` — ฝั่งนายจ้างชนะ
- `employee_won` — ฝั่งลูกจ้างชนะ
- `mixed` — แพ้-ชนะบางส่วน
- `unclear` — ไม่ชัดเจน

**Heuristic สำหรับ classification:**
- "ยกฟ้องโจทก์" (ถ้าโจทก์เป็นลูกจ้าง) → employer_won
- "พิพากษาให้จำเลยจ่าย" (ถ้าจำเลยเป็นนายจ้าง) → employee_won
- "พิพากษากลับ" → กลับคำพิพากษาศาลล่าง

---

## Section 20: Repealed Regulations Database ⭐⭐⭐⭐

### 20.1 Overview
หมวด H มี 615 อนุบัญญัติ — วิเคราะห์แล้วพบว่า:

| สถานะ | จำนวน | คำอธิบาย |
|-------|------|----------|
| ✅ active | 103 | น่าจะยังใช้บังคับอยู่ |
| ❌ repealed | 512 | ถูกยกเลิกแล้ว (โดยตรงหรือถูกแทนที่ด้วยฉบับใหม่กว่า) |

### 20.2 API Filter
`GET /api/regulations?status=active` — เฉพาะที่ยังใช้บังคับ (default)
`GET /api/regulations?status=repealed` — เฉพาะที่ถูกยกเลิก
`GET /api/regulations?status=all` — ทั้งหมด

### 20.3 Important Note on ป.ค. 103
บางอนุบัญญัติอ้างอิง **ประกาศของคณะปฏิวัติ ฉบับที่ ๑๐๓** ซึ่งถูกยกเลิกโดย พ.ร.บ. คุ้มครองแรงงาน 2541 มาตรา ๓

แต่ **มาตรา ๑๖๖** มี transitional clause: "ให้ยังคงใช้ได้ต่อไปเท่าที่ไม่ขัดหรือแย้งกับพระราชบัญญัตินี้"

→ AI ควรเตือนผู้ใช้เสมอเมื่ออ้างอิงอนุบัญญัติเหล่านี้: "⚠️ อนุบัญญัติฉบับนี้อ้างอิง ป.ค. 103 ที่ถูกยกเลิกแล้ว แต่ยังใช้ได้ตามมาตรา 166 — ควรตรวจสอบว่ามีฉบับใหม่มาแทนหรือไม่"

---

## Section 21: LLM Provider Configuration ⭐⭐⭐

### 21.1 Current Provider
- **Z.AI** (glm-4.6) — ใช้อยู่ แต่ต้องเติมเงิน
- API: `https://api.z.ai/api/paas/v4/chat/completions`
- Model: `glm-4.6` (override ผ่าน env `Z_AI_MODEL`)

### 21.2 Google Gemini (ไม่สามารถใช้ได้ในบาง region)
- API: `https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent`
- ❌ Error: "User location is not supported for the API use"
- แนะนำ: ใช้ผ่าน Vertex AI หรือ OpenRouter แทน

### 21.3 Alternative Providers (แนะนำ)
1. **OpenRouter** (https://openrouter.ai) — ฟรี tier มีหลาย models
2. **Groq** (https://groq.com) — เร็วมาก, ฟรี
3. **Together AI** (https://together.ai) — $5 ฟรี

### 21.4 Configuration
เปลี่ยน LLM provider ได้โดยแก้:
- `src/lib/zai-client.ts` — API client
- `src/app/api/ask/route.ts` — system prompt
- Vercel env vars: `Z_AI_API_KEY`, `Z_AI_MODEL`

---

*Last updated: 2026-07-28*
*Database: 78 laws · 8,507 sections · 514 judgments · 615 regulations (103 active) · 63 templates · 9,699 RAG chunks*

---

## Section 22: Legal Strategist AI Prompt (Phase 1 — Active) ⭐⭐⭐⭐⭐

### 22.1 Prompt Location
- **File:** `src/app/api/ask/route.ts` → `SYSTEM_PROMPT` constant
- **LLM Provider:** OpenRouter — `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- **Response time:** 2-8 วินาที (ไม่เกิน Vercel 60s timeout)

### 22.2 Prompt Structure
AI prompt แบ่งเป็น 6 ส่วนหลัก:

1. **Role Description** — Legal Strategist & Labor Law Expert ประจำ หจก.เผ่าปัญญา ทรานสปอร์ต
2. **Knowledge Base & Legal Framework** — อ้างอิง พ.ร.บ.คุ้มครองแรงงาน, ป.พ.พ., PDPA, แรงงานสัมพันธ์, จป.
3. **Database Context** — บอก AI ว่ามีข้อมูลอะไรในฐานข้อมูล:
   - 78 กฎหมาย · 8,507 มาตรา
   - 514 ฎีกาแรงงาน
   - 615 อนุบัญญัติ (103 active, 512 repealed)
   - 63 เทมเพลตเอกสาร (F1-F65)
4. **Template Reference** — บอก AI ว่าเทมเพลตไหนใช้เมื่อไหร่ (F1-F23 หลัก)
5. **Risk Matrix 5×5** — Severity × Likelihood = Risk Score (1-25)
6. **Core Responsibilities** — Contract Strategy, Discipline & Termination, PDPA & Monitoring

### 22.3 Output Structure (4 ส่วน)
ทุกคำตอบต้องมี:
1. **บทวิเคราะห์ทางกฎหมาย** — อ้างอิงมาตรา [N]
2. **คำแนะนำเชิงกลยุทธ์** — สิ่งที่บริษัทควรทำทันที
3. **ร่างเอกสาร/คำพูด** — ตัวอย่างข้อความ (ถ้ามี)
4. **จุดเสี่ยงที่ต้องระวัง** — ⚠️ RISK ALERT + Risk Score

### 22.4 Key Differentiators (ที่ทำให้ AI ตอบถูกต้อง)

#### รถร่วม vs พนักงานประจำ (Critical!)
AI แยกแยะได้ถูกต้อง:
- **รถร่วม = จ้างทำของ (ม.587)** — ใช้ "ค่าบริการเหมาจ่าย" ไม่ใช่ "เงินเดือน"
- **พนักงานประจำ = จ้างแรงงาน (ม.575)** — มี "อำนาจบังคับบัญชา"

#### กลยุทธ์เฉพาะขนส่ง:
- ใช้ "Service Window" แทน "เวลาเข้างาน"
- ใช้ "ปรับลดค่าบริการ" แทน "ลงโทษทางวินัย"
- ผลักภาระเงื่อนไขไปยังลูกค้า (Big C) ไม่ใช่บริษัท

#### การเลิกจ้าง (Zero Tolerance):
- ทุจริต (ขโมยน้ำมัน, บิลผี) → เลิกจ้าง ไม่จ่ายค่าชดเชย (ม.119)
- ต้องมี F5→F6→F7 ก่อน F8 เสมอ
- F9 ต้องจ่าย ณ วันเลิกจ้าง (เลย = ดอกเบี้ย 15%/ปี)

### 22.5 Template Reference (ใน Prompt)
AI รู้จักเทมเพลตหลักและแนะนำได้:

| Template | ใช้เมื่อ | กฎหมาย |
|----------|---------|--------|
| F1 สัญญาจ้างงาน | จ้างใหม่ | ม.11-13 พ.ร.บ.คุ้มครองแรงงาน |
| F2 สัญญาทดลองงาน | จ้างใหม่ | ห้ามเกิน 119 วัน (ม.10) |
| F3 ข้อบังคับการทำงาน | พนักงาน ≥10 คน | ยื่น สนร. ภายใน 15 วัน |
| F4 ระเบียบวินัย | ทุกบริษัท | ฐานในการเลิกจ้าง |
| F5/F6/F7 หนังสือเตือน | ก่อนเลิกจ้าง | ม.119(4) |
| F8 บอกเลิกสัญญา | เลิกจ้าง | แจ้งล่วงหน้า 1 จ่าย |
| F9 จ่ายค่าชดเชย | เลิกจ้าง | ม.118 — จ่าย ณ วันเลิกจ้าง |
| F14 NDA | ปกป้องข้อมูล | พ.ร.บ.ความลับทางการค้า |
| F15 Non-Compete | ผู้บริหาร | ห้ามเกิน 5 ปี |
| F20 แจ้งลดค่าจ้าง | ลดเงินเดือน | ม.71 — ต้องมีความยินยอม |
| F22 แจ้งพักงาน | สอบสวน | จ่าย 50% ค่าจ้าง |

### 22.6 การเรียกใช้งาน
```
POST /api/ask
Content-Type: application/json

{
  "question": "ลูกจ้างขาดงาน 3 วันติดต่อกัน เลิกจ้างได้ไหม",
  "laborOnly": true,
  "history": []  // optional: ประวัติแชท
}
```

Response:
```json
{
  "answer": "1. บทวิเคราะห์ทางกฎหมาย... [1]\n2. คำแนะนำ... แนะนำ F8...\n3. ร่างเอกสาร... \n4. ⚠️ RISK ALERT...",
  "citations": [{ "index": 1, "type": "section", "label": "มาตรา 119(5)", ... }],
  "retrievedChunks": 10
}
```

### 22.7 ข้อจำกัดปัจจุบัน
- NVIDIA Nemotron 3 Nano อาจมีคำอังกฤษผสมในคำตอบบางครั้ง (ใช้ model เล็กเพื่อความเร็ว)
- ไม่สามารถอ้างอิงอนุบัญญัติฉบับเต็มได้ (มีแค่ใน RAG chunks)
- ไม่สามารถสร้าง PDF ได้โดยตรง (ต้องใช้ /api/templates/pdf endpoint แยก)

---

*Last updated: 2026-07-29*
*Phase 1: AI Prompt + SKILL.md — COMPLETED*
