// Persona definitions for Panya-AI
// Three personas: HR / Legal / Owner — each tailors AI prompt, default sample questions,
// skill routing priority, and quick actions.

export type PersonaId = 'hr' | 'legal' | 'owner';

export interface Persona {
  id: PersonaId;
  label: string;           // Thai label
  labelEn: string;         // English subtitle
  icon: string;            // lucide icon name (resolved in component)
  color: string;           // tailwind color class for badge
  description: string;     // 1-2 sentence what this persona focuses on
  /** AI prompt prefix — injected before the sub-skill prompt */
  promptPrefix: string;
  /** Default laborOnly flag for RAG */
  laborOnly: boolean;
  /** Skill routing priority — which sub-skill to prefer when ambiguous */
  skillPriority: Array<'contract-review' | 'risk-assessment' | 'document-drafting' | 'legal-qa'>;
  /** Sample questions shown in chat empty state */
  sampleQuestions: string[];
  /** Sidebar quick actions (top 3-4) */
  quickActions: Array<{ view: string; label: string; icon: string }>;
}

// ============================
// Shared helpers (reduce code duplication)
// ============================

/** Build a persona prompt prefix from structured parts. All personas share the same
 *  boilerplate (org name, section headers) — this helper centralizes it. */
function buildPromptPrefix(opts: {
  emoji: string;
  title: string;
  role: string;
  needs: string[];
  focus: string[];
  avoid?: string[];
  footer?: string;
}): string {
  const lines = [
    `# ${opts.emoji} PERSONA: ${opts.title}`,
    `ผู้ใช้คือ${opts.role}ของ หจก.เผ่าปัญญา ทรานสปอร์ต`,
    `ความต้องการหลัก:`,
    ...opts.needs.map(n => `- ${n}`),
    ``,
    `เน้น:`,
    ...opts.focus.map(f => `- ${f}`),
  ];
  if (opts.avoid && opts.avoid.length > 0) {
    lines.push(``, `หลีกเลี่ยง:`, ...opts.avoid.map(a => `- ${a}`));
  }
  if (opts.footer) {
    lines.push(``, opts.footer);
  }
  return lines.join('\n');
}

/** Common quick action shortcuts reused across personas. */
const QA = {
  ask: { view: 'ask', label: 'ถาม AI', icon: 'MessageSquare' },
  pdfBuilder: { view: 'pdf-builder', label: 'สร้างเอกสาร', icon: 'Wand2' },
  contractAnalysis: { view: 'contract-analysis', label: 'วิเคราะห์สัญญา', icon: 'FileSearch' },
  riskMatrix: { view: 'risk-matrix', label: 'Risk Matrix', icon: 'Grid3x3' },
};

export const PERSONAS: Record<PersonaId, Persona> = {
  // ============================
  // HR — ฝ่ายบุคคล
  // ============================
  hr: {
    id: 'hr',
    label: 'ฝ่ายบุคคล',
    labelEn: 'HR / People Operations',
    icon: 'Users',
    color: 'bg-blue-500/15 text-blue-300 border-blue-500/30',
    description: 'เน้นการจัดการพนักงานรายวัน — สัญญาจ้าง, หนังสือเตือน, ค่าจ้าง/OT, การลา, วินัย',
    promptPrefix: buildPromptPrefix({
      emoji: '👤',
      title: 'HR (ฝ่ายบุคคล)',
      role: 'เจ้าหน้าที่ฝ่ายบุคคล',
      needs: [
        'ร่างเอกสารประจำวัน: สัญญาจ้าง, หนังสือเตือน, ใบลา, ใบรับรองเงินเดือน',
        'คำนวณสิทธิ: ค่าจ้าง OT, ค่าชดเชย, เงินประกันสังคม, เงินทดแทน',
        'จัดการวินัย: หนังสือเตือน 3 ครั้ง → เลิกจ้าง (ม.119(4))',
        'ตอบคำถามพนักงานเกี่ยวกับสิทธิ/หน้าที่',
      ],
      focus: [
        'ขั้นตอนที่ "ปฏิบัติได้จริง" ทันที (พร้อมเทมเพลต)',
        'ระบุเอกสารที่ต้องใช้ + มาตราอ้างอิง',
        'เตือนความเสี่ยงที่อาจเกิดจากการทำผิดขั้นตอน',
      ],
      avoid: [
        'คำแนะนำเชิงนโยบายระดับสูง (ให้ Owner ตัดสินใจ)',
        'การวิเคราะห์คดีฎีกาโดยไม่จำเป็น',
      ],
    }),
    laborOnly: true,
    skillPriority: ['document-drafting', 'contract-review', 'risk-assessment', 'legal-qa'],
    sampleQuestions: [
      'จะร่างหนังสือเตือนครั้งที่ 2 ให้ลูกจ้างที่มาสายบ่อย ต้องระบุอะไรบ้าง?',
      'พนักงานทดลองงาน 119 วัน เลิกจ้างต้องจ่ายค่าชดเชียไหม?',
      'ค่าจ้าง OT วันหยุดปกติคิดกี่เท่า? ยกตัวอย่างคำนวณ',
      'ลูกจ้างลาป่วย 45 วัน ปีนี้ หักเงินเดือนได้กี่วัน?',
      'ต้องการร่างสัญญาจ้างงานพนักงานขับรถ — เน้นเรื่องใด?',
    ],
    quickActions: [
      QA.pdfBuilder,
      QA.ask,
      { view: 'templates', label: 'เทมเพลต', icon: 'FileText' },
      { view: 'laws', label: 'กฎหมายแรงงาน', icon: 'BookOpen' },
    ],
  },

  // ============================
  // Legal — ฝ่ายกฎหมาย
  // ============================
  legal: {
    id: 'legal',
    label: 'ฝ่ายกฎหมาย',
    labelEn: 'Legal Counsel / In-house Lawyer',
    icon: 'Scale',
    color: 'bg-purple-500/15 text-purple-300 border-purple-500/30',
    description: 'เน้นการวิเคราะห์เชิงลึก — ฎีกา, ความเสี่ยงคดี, ตรวจสัญญา, กลยุทธ์ฟ้อง/ต่อสู้คดี',
    promptPrefix: buildPromptPrefix({
      emoji: '⚖️',
      title: 'Legal Counsel (ฝ่ายกฎหมาย)',
      role: 'ทนายความ/ที่ปรึกษากฎหมายในองค์กร',
      needs: [
        'วิเคราะห์สัญญา/เงื่อนไขอย่างละเอียด — หาข้อที่ผิดกฎหมาย + ระบุมาตรา',
        'ศึกษาคำพิพากษาฎีกาที่เกี่ยวข้อง + อัตราความสำเร็จ',
        'ประเมินความเสี่ยงคดี (Risk Matrix 5×5) + แนวป้องกันเชิงกลยุทธ์',
        'เตรียมเอกสารสำหรับฟ้อง/ต่อสู้คดี — คำฟ้อง, คำให้การ, หนังสือนำสืบ',
      ],
      focus: [
        'ความแม่นยำทางกฎหมาย — ระบุมาตรา, ข้อความฎีกา, หลักกฎหมาย',
        'วิเคราะห์หลายมุมมอง — ฝั่งเรา vs ฝั่งคู่กรณี',
        'ระบุความเสี่ยงที่อาจเกิดจากจังหวะเวลา, หลักฐาน, อายุความ',
        'เสนอทางเลือกหลายแบบ + ข้อดี-ข้อเสียแต่ละทาง',
      ],
      footer: 'ใช้ศัพท์กฎหมายเฉพาะทางได้ — แต่ต้องอธิบายให้ HR/Owner เข้าใจได้',
    }),
    laborOnly: false, // Legal needs ALL law categories
    skillPriority: ['contract-review', 'risk-assessment', 'legal-qa', 'document-drafting'],
    sampleQuestions: [
      'วิเคราะห์สัญญาจ้างนี้ — ข้อใดผิดกฎหมายและเสี่ยงฟ้องที่สุด?',
      'ฎีกาล่าสุดว่าด้วย "การเลิกจ้างเพราะลดค่าจ้าง" วินิจฉัยอย่างไร?',
      'ลูกจ้างฟ้องเรียก OT ย้อนหลัง 2 ปี — อายุความขัดข้องไหม?',
      'ประเมินความเสี่ยง: ปลดพนักงานที่ร้องเรียน ความเสี่ยงคดีกี่/25?',
      'จะร่าง "หนังสือแจ้งเลิกสัญญาจ้าง" ที่ทนายฝั่งตรงข้ามเอาไม่ได้ — เน้นอะไร?',
    ],
    quickActions: [
      QA.contractAnalysis,
      QA.riskMatrix,
      QA.ask,
      { view: 'judgments', label: 'คำพิพากษา', icon: 'Scale' },
    ],
  },

  // ============================
  // Owner — เจ้าของกิจการ
  // ============================
  owner: {
    id: 'owner',
    label: 'เจ้าของกิจการ',
    labelEn: 'Business Owner / Executive',
    icon: 'Crown',
    color: 'bg-gold/15 text-gold border-gold/30',
    description: 'มุมมองระดับนโยบาย — ความเสี่ยงรวม, การตัดสินใจใหญ่, ต้นทุน-ผลตอบแทน, กลยุทธ์',
    promptPrefix: buildPromptPrefix({
      emoji: '👑',
      title: 'Owner (เจ้าของกิจการ)',
      role: 'เจ้าของกิจการ',
      needs: [
        'ภาพรวมความเสี่ยง — ไม่ลงรายละเอียดเทคนิค',
        'การตัดสินใจระดับนโยบาย: เปิด/ปิดสาขา, จ้าง/เลิกจ้างรวม, ลดต้นทุน',
        'ตัวเลขธุรกิจ: ต้นทุนค่าชดเชย, ค่าปรับ, ค่าทนาย, เวลาคดี',
        'ความเสี่ยงต่อแบรนด์/ชื่อเสียง — ไม่ใช่แค่ตัวเลข',
      ],
      focus: [
        'สรุปคำแนะนำเป็น "ทำ / ไม่ทำ / รอดู" ใน 3 บรรทัดแรก',
        'เปรียบเทียบทางเลือก: ต้นทุน vs ผลตอบแทน vs ความเสี่ยง',
        'ระบุความเสี่ยงเชิงธุรกิจ (reputational, financial, operational)',
        'ใช้ภาษาธุรกิจ — ไม่ใช่ศัพท์กฎหมายเฉพาะทาง',
      ],
      avoid: [
        'รายละเอียดมาตรา/ฎีกาในส่วนสรุป (ย้ายไป appendix)',
        'คำแนะนำที่ต้องการการดำเนินการทันที (ให้ HR/Legal execute)',
      ],
    }),
    laborOnly: true,
    skillPriority: ['risk-assessment', 'legal-qa', 'document-drafting', 'contract-review'],
    sampleQuestions: [
      'ถ้าเลิกจ้าง 20 คนพร้อมกันเพราะขาดทุน — ต้นทุนรวมประมาณเท่าไหร่?',
      'ความเสี่ยงสูงสุดของบริษัทขนส่งเราตอนนี้คืออะไร? จัดลำดับให้',
      'จะเปิดสาขาใหม่ — ต้องเตรียมกฎหมายแรงงานอะไรบ้าง?',
      'พนักงานขับรถเมาแล้วขับ บริษัทต้องรับผิดไหม? จำคุกไหม?',
      'เปรียบเทียบ: จ้างพนักงานประจำ vs จ้างเหมา — ต้นทุน/ความเสี่ยงต่างอย่างไร?',
    ],
    quickActions: [
      QA.riskMatrix,
      QA.ask,
      QA.contractAnalysis,
      QA.pdfBuilder,
    ],
  },
};

// ============================
// Storage helpers (localStorage)
// ============================
const STORAGE_KEY = 'panya_persona_v1';

export function getPersona(): PersonaId | null {
  if (typeof window === 'undefined') return null;
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return null;
    const parsed = JSON.parse(raw) as { id?: PersonaId };
    if (parsed?.id && parsed.id in PERSONAS) return parsed.id;
    return null;
  } catch {
    return null;
  }
}

export function setPersona(id: PersonaId): void {
  if (typeof window === 'undefined') return;
  localStorage.setItem(STORAGE_KEY, JSON.stringify({ id, setAt: new Date().toISOString() }));
  // Dispatch event so React components re-render
  window.dispatchEvent(new Event('panya-persona-changed'));
}

export function clearPersona(): void {
  if (typeof window === 'undefined') return;
  localStorage.removeItem(STORAGE_KEY);
  window.dispatchEvent(new Event('panya-persona-changed'));
}

/** Returns true if onboarding has been completed (either chosen or skipped) */
const ONBOARDED_KEY = 'panya_onboarded_v1';
export function isOnboarded(): boolean {
  if (typeof window === 'undefined') return false;
  return localStorage.getItem(ONBOARDED_KEY) === '1';
}
export function markOnboarded(): void {
  if (typeof window === 'undefined') return;
  localStorage.setItem(ONBOARDED_KEY, '1');
  window.dispatchEvent(new Event('panya-persona-changed'));
}
