'use client';

import { useEffect, useState, useMemo } from 'react';
import { Button } from '@/components/ui/button';
import { ArrowRight, Sparkles, BookOpen, Shield, Check, FileText, FileSearch } from 'lucide-react';
import { useNavigation } from '@/lib/navigation';
import { usePersona } from '@/components/onboarding/usePersona';
import type { DashboardStats } from '@/lib/types';

const TYPEWRITER_QUESTIONS = [
  'ลูกจ้างขาดงาน 3 วันติดต่อกัน เลิกจ้างได้ไหม?',
  'ค่าจ้างล่วงเวลาคำนวณอย่างไร?',
  'พนักงานทดลองงาน 119 วัน เลิกจ้างต้องจ่ายค่าชดเชยไหม?',
  'ลูกจ้างเอาข้อมูลลูกค้าไปให้คู่แข่ง ฟ้องอาญาได้ไหม?',
  'ลดค่าจ้างเพราะบริษัทขาดทุน ต้องขอความยินยอมไหม?',
  'นายจ้างหยุดกิจการ ต้องจ่ายค่าชดเชยอย่างไร?',
  'ลูกจ้างลาป่วยเกิน 30 วัน หักเงินเดือนได้ไหม?',
  'รถร่วมเป็นลูกจ้างหรือไม่ ต้องจ่ายค่าชดเชยไหม?',
  'ลูกจ้างเมาแล้วขับรถบรรทุก ฟ้องไล่ออกได้ไหม?',
  'พนักงานลาออกแล้วฟ้องเรียก OT ย้อนหลัง ต้องจ่ายไหม?',
];

const EMPLOYER_DEFENSE_CARDS = [
  { t: 'เลิกจ้างโดยไม่ต้องจ่ายค่าชดเชย', d: 'มาตรา 119 · 6 กรณีที่เลิกจ้างได้ทันที', ref: 'พ.ร.บ.แรงงาน' },
  { t: 'หนังสือเตือน 3 ครั้ง = เลิกจ้างได้', d: 'วิธีเขียนให้ศาลรับฟังได้', ref: 'ฎีกา 2567/8103' },
  { t: 'ทดลองงาน 119 วัน', d: 'เลิกจ้างก่อนครบ 120 วัน = ไม่ต้องชดเชย', ref: 'มาตรา 118' },
  { t: 'ลูกจ้างเอาข้อมูลไปให้คู่แข่ง', d: 'ฟ้องอาญา + เรียกค่าเสียหาย', ref: 'ป.อ. 323 + NDA' },
  { t: 'ลาป่วยเท็จ / เกินสิทธิ', d: 'ตรวจใบรับรองแพทย์ · หักค่าจ้างได้', ref: 'มาตรา 32' },
  { t: 'ฟ้องเรียก OT ย้อนหลัง', d: 'อายุความ 2 ปี · ต้องมีหลักฐาน', ref: 'มาตรา 193/34' },
];

export function Hero({ stats }: { readonly stats: DashboardStats | null }) {
  const { navigate } = useNavigation();
  const { persona } = usePersona();

  // Persona-aware question pool — fall back to defaults if no persona
  const questions = useMemo(() => {
    if (persona && persona.sampleQuestions.length >= 3) return persona.sampleQuestions;
    return TYPEWRITER_QUESTIONS;
  }, [persona]);

  const [typedQ, setTypedQ] = useState('');
  const [startIdx] = useState(() => {
    // Cryptographically secure random — satisfies SonarCloud S2245
    const arr = new Uint8Array(1);
    crypto.getRandomValues(arr);
    return arr[0] % questions.length;
  });
  const [qIdx, setQIdx] = useState(startIdx);

  // Reset qIdx if questions array changes (persona switch)
  useEffect(() => {
    if (qIdx >= questions.length) setQIdx(0);
  }, [questions, qIdx]);

  // Typewriter effect — cycle through example questions (randomized start)
  useEffect(() => {
    const q = questions[qIdx];
    let i = 0;
    setTypedQ('');
    const typeInt = setInterval(() => {
      i++;
      setTypedQ(q.slice(0, i));
      if (i >= q.length) {
        clearInterval(typeInt);
        setTimeout(() => setQIdx((qIdx + 1) % questions.length), 4000);
      }
    }, 120);
    return () => clearInterval(typeInt);
  }, [qIdx]);

  return (
    <>
      <section className="relative overflow-hidden">
        {/* Decorative glow + floating mascot */}
        <div className="absolute inset-0 -z-10 overflow-hidden">
          <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-gold/10 rounded-full blur-[120px]" />
          <div className="absolute top-20 right-10 w-[300px] h-[300px] bg-primary/5 rounded-full blur-[100px]" />
          {/* Floating mascot — large, semi-transparent */}
          <img
            src="/mascot/mascot-front.png"
            alt=""
            aria-hidden="true"
            className="absolute right-4 bottom-0 w-64 h-64 object-contain opacity-[0.06] pointer-events-none hidden lg:block"
            style={{ animation: 'floatMascot 5s ease-in-out infinite' }}
          />
        </div>

        <div className="mx-auto max-w-7xl px-4 sm:px-6 pt-16 pb-12 sm:pt-20 sm:pb-16">
          {/* Badge */}
          <div className="flex justify-center mb-6">
            <div className="inline-flex items-center gap-2 rounded-full border border-gold/30 bg-gold-soft px-4 py-1.5">
              <Shield className="h-3.5 w-3.5 text-gold" />
              <span className="text-xs font-medium text-gold tracking-wide">
                AI ที่ยืนข้างนายจ้าง · Employer-Side Legal AI
              </span>
            </div>
          </div>

          {/* Headline */}
          <h1 className="text-center text-4xl sm:text-5xl md:text-6xl font-bold tracking-tight leading-[1.1]" style={{ fontFamily: 'var(--font-ibm-plex-serif)' }}>
            <span className="text-gradient-gold">ที่สุดแห่งปัญญาประดิษฐ์</span>
            <br />
            <span className="text-foreground">ครบเครื่องมือกฎหมายไทย</span>
            <br />
            <span className="text-foreground italic font-medium opacity-85 text-3xl sm:text-4xl md:text-5xl">
              เพื่อปกป้องบริษัทคุณ
            </span>
          </h1>

          <p className="mx-auto mt-6 max-w-2xl text-center text-base sm:text-lg text-muted-foreground leading-relaxed">
            AI ที่ค้นและตอบข้อกฎหมายไทย{' '}
            <span className="text-gold font-medium">พร้อมอ้างอิงมาตรา ฎีกา และคำพิพากษาศาลจริง</span>{' '}
            ครอบคลุมกฎหมายแรงงาน อาญา แพ่ง — ไม่ประดิษฐ์มาตราที่ไม่มีอยู่จริง
          </p>

          {/* CTA */}
          <div className="mt-8 flex flex-col sm:flex-row gap-3 justify-center items-center">
            <Button
              size="lg"
              onClick={() => navigate({ name: 'ask' })}
              className="btn-glow bg-gradient-to-r from-gold to-gold/80 text-navy hover:from-gold/90 hover:to-gold/70 font-semibold gap-2"
            >
              <Sparkles className="h-4 w-4" />
              เริ่มถาม Panya-AI
              <ArrowRight className="h-4 w-4" />
            </Button>
            <Button
              size="lg"
              variant="outline"
              onClick={() => navigate({ name: 'templates' })}
              className="border-border/60 bg-card/50 backdrop-blur-sm hover:bg-accent/50 gap-2"
            >
              <FileText className="h-4 w-4" />
              สร้างเอกสาร (63 เทมเพลต)
            </Button>
          </div>

          {/* Trust chips */}
          <div className="mt-8 flex flex-wrap gap-4 justify-center text-xs text-muted-foreground">
            <span className="inline-flex gap-1.5 items-center">
              <Check className="h-3.5 w-3.5 text-gold" />
              <span>ข้อมูลจาก law.go.th (กฤษฎีกา)</span>
            </span>
            <span className="inline-flex gap-1.5 items-center">
              <Check className="h-3.5 w-3.5 text-gold" />
              <span>คำพิพากษาศาลฎีกา 502 คดี</span>
            </span>
            <span className="inline-flex gap-1.5 items-center">
              <Check className="h-3.5 w-3.5 text-gold" />
              <span>อ้างอิงตรวจสอบได้ทุกคำตอบ</span>
            </span>
          </div>

          {/* Live chat demo card with typewriter */}
          <div className="mt-12 max-w-2xl mx-auto">
            <LiveChatDemo typedQ={typedQ} qIdx={qIdx} onAskClick={() => navigate({ name: 'ask' })} />
          </div>

          {/* Stats Strip */}
          {stats && <StatsStrip stats={stats} />}

          {/* Gold rule */}
          <div className="mt-16 h-px bg-gradient-to-r from-transparent via-gold/50 to-transparent" />

          {/* 4 Action Buttons — "วันนี้คุณต้องการอะไร?" */}
          <ActionButtons onNav={navigate} />
        </div>
      </section>

      {/* Employer Section */}
      <EmployerSection />
    </>
  );
}

/* ---------- Live Chat Demo (animated preview) ---------- */
function LiveChatDemo({ typedQ, qIdx, onAskClick }: { readonly typedQ: string; readonly qIdx: number; readonly onAskClick: () => void }) {
  // Randomize demo content based on typedQ hash
  const demoVariants = [
    {
      verdict: 'เลิกจ้างได้ · ไม่ต้องจ่ายค่าชดเชย',
      verdictColor: 'bg-green-500/20 text-green-300',
      answer: 'หากลูกจ้างขาดงานติดต่อกันครบ 3 วันทำงานโดยไม่มีเหตุอันสมควร ถือเป็น "การละทิ้งหน้าที่" ตาม',
      law: 'พ.ร.บ.คุ้มครองแรงงาน มาตรา 119(5)',
      steps: [
        { label: 'ค้นในกฎหมายแรงงาน 2541', done: true },
        { label: 'พบมาตรา 119(5), 118', done: true },
        { label: 'ตรวจสอบคำพิพากษาฎีกา 4 คดี', done: true },
        { label: 'เรียบเรียงคำตอบพร้อมอ้างอิง', done: false },
      ],
    },
    {
      verdict: 'ต้องจ่าย · 1.5 เท่าค่าจ้างปกติ',
      verdictColor: 'bg-blue-500/20 text-blue-300',
      answer: 'การทำงานล่วงเวลา นายจ้างต้องจ่ายค่าจ้างไม่น้อยกว่า 1.5 เท่าของอัตราค่าจ้างปกติ สำหรับชั่วโมงแรก และ 3 เท่า สำหรับชั่วโมงถัดไปในวันหยุด ตาม',
      law: 'พ.ร.บ.คุ้มครองแรงงาน มาตรา 61',
      steps: [
        { label: 'ค้นในกฎหมายแรงงาน 2541', done: true },
        { label: 'พบมาตรา 61, 62 (OT rate)', done: true },
        { label: 'ตรวจอนุบัญญัติค่าจ้าง OT', done: true },
        { label: 'คำนวณอัตราตามประเภทงาน', done: false },
      ],
    },
    {
      verdict: 'เสี่ยงสูง · ต้องจ่ายค่าชดเชย',
      verdictColor: 'bg-red-500/20 text-red-300',
      answer: 'การลดค่าจ้างฝ่ายเดียวโดยไม่ได้ความยินยอมจากลูกจ้าง ถือเป็นการเปลี่ยนสภาพการจ้างโดยมิชอบ ตาม',
      law: 'พ.ร.บ.คุ้มครองแรงงาน มาตรา 53',
      steps: [
        { label: 'ค้นในกฎหมายแรงงาน 2541', done: true },
        { label: 'พบมาตรา 53 (ห้ามลดค่าจ้าง)', done: true },
        { label: 'ตรวจฎีกา 2566/9876', done: true },
        { label: 'ประเมินความเสี่ยงฝั่งนายจ้าง', done: false },
      ],
    },
  ];
  // Use qIdx (question index) for variant — NOT typedQ.length
  // This way demo content only changes when the QUESTION changes, not every keystroke
  const variantIdx = qIdx % demoVariants.length;
  const demo = demoVariants[variantIdx];
  return (
    <div
      className="rounded-2xl p-1 border border-gold/30 shadow-2xl"
      style={{ background: 'linear-gradient(180deg, rgba(15,33,73,1), rgba(11,27,59,1))' }}
    >
      <div className="rounded-xl overflow-hidden" style={{ background: '#0A1633' }}>
        {/* Header */}
        <div className="px-4 py-3 border-b border-gold/15 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <img src="/mascot/mascot-front.png" alt="Panya-AI" className="h-6 w-6 rounded object-contain" />
            <span className="text-xs font-semibold text-gold">Panya-AI</span>
            <span className="text-[10px] px-2 py-0.5 rounded-full bg-green-500/20 text-green-300">
              ● พร้อมตอบ
            </span>
          </div>
          <div className="flex gap-1">
            {[1, 2, 3].map(dotNum => (
              <div key={`dot-${dotNum}`} className="h-2 w-2 rounded-full bg-white/15" />
            ))}
          </div>
        </div>

        {/* Question bubble with typewriter */}
        <div className="px-4 pt-4 pb-2">
          <div className="text-[10px] uppercase tracking-wider text-navy-300 mb-2">คำถาม</div>
          <div className="bg-gold/8 border border-gold/20 rounded-lg px-3 py-2.5 text-sm leading-relaxed text-white min-h-[48px]">
            {typedQ}
            <span
              className="inline-block w-1.5 h-4 bg-gold ml-0.5 align-middle"
              style={{ animation: 'blink 1s infinite' }}
            />
          </div>
        </div>

        {/* Agent steps preview */}
        <div className="px-4 py-3">
          <div className="text-[10px] uppercase tracking-wider text-navy-300 mb-2">AI กำลังทำงาน</div>
          {demo.steps.map((s, i) => (
            <div
              key={`step-${s.label}`}
              className="flex items-center gap-2.5 py-1.5 text-[12px]"
              style={{ color: s.done ? 'rgba(200,210,235,0.8)' : '#c9a961' }}
            >
              <div
                className={`h-4 w-4 rounded-full flex items-center justify-center flex-shrink-0 ${
                  s.done ? 'bg-green-500' : 'border-2 border-gold'
                }`}
                style={{ animation: s.done ? 'none' : 'spin 1.5s linear infinite' }}
              >
                {s.done && (
                  <svg className="h-2.5 w-2.5 text-white" fill="none" stroke="currentColor" strokeWidth={3} viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                  </svg>
                )}
              </div>
              <span>{s.label}</span>
              {s.done && <span className="ml-auto text-green-500 text-[10px]">✓</span>}
            </div>
          ))}
        </div>

        {/* Preview answer */}
        <div className="px-4 py-3 border-t border-gold/15 bg-black/20">
          <div className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded text-[11px] font-semibold ${demo.verdictColor} mb-2`}>
            <Check className="h-3 w-3" /> {demo.verdict}
          </div>
          <div className="text-[13px] leading-relaxed text-white/85">
            {demo.answer}
            <span className="text-gold font-medium mx-1">{demo.law}</span>
            <sup className="text-gold" style={{ fontFamily: 'var(--font-ibm-plex-serif)' }}>[1]</sup>
            {' '}นายจ้างมีสิทธิดำเนินการ...
          </div>
        </div>
      </div>

      <style>{`
        @keyframes blink { 50% { opacity: 0; } }
        @keyframes spin { to { transform: rotate(360deg); } }
        @keyframes floatMascot { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
      `}</style>

      {/* CTA below demo */}
      <div className="text-center mt-4">
        <button
          type="button"
          onClick={onAskClick}
          className="text-xs text-gold hover:text-gold/80 transition inline-flex items-center gap-1"
        >
          ลองถามด้วยตัวเอง <ArrowRight className="h-3 w-3" />
        </button>
      </div>
    </div>
  );
}

/* ---------- Stats Strip ---------- */
function StatsStrip({ stats }: { readonly stats: DashboardStats }) {
  const items = [
    { n: '78', label: 'กฎหมายไทยในระบบ', sub: 'แรงงาน · อาญา · แพ่ง · ภาษี' },
    { n: (stats.totalSections || 12936).toLocaleString('th-TH'), label: 'มาตราให้ค้นหา', sub: 'FTS5 + LIKE fallback' },
    { n: (stats.totalLaborJudgments || 502).toLocaleString('th-TH'), label: 'คำพิพากษาฎีกา', sub: 'พร้อมสรุปประเด็น' },
    { n: '63', label: 'เทมเพลตเอกสาร PDF', sub: 'ครอบคลุม 5 หมวด' },
  ];
  return (
    <div className="mt-16 grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-4">
      {items.map((it, i) => (
        <div
          key={it.label}
          className={`p-4 ${i === 0 ? 'border-l-2 border-gold' : 'border-l border-border/40'}`}
        >
          <div
            className="text-3xl sm:text-4xl font-medium text-gradient-gold tabular-nums"
            style={{ fontFamily: 'var(--font-ibm-plex-serif)' }}
          >
            {it.n}
          </div>
          <div className="text-xs sm:text-sm font-medium text-foreground mt-1">{it.label}</div>
          <div className="text-[10px] text-muted-foreground mt-0.5">{it.sub}</div>
        </div>
      ))}
    </div>
  );
}

/* ---------- Employer Section (defense cards) ---------- */
function EmployerSection() {
  const { navigate } = useNavigation();

  return (
    <section className="bg-card-soft/30 border-y border-border/40">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 py-16 sm:py-20">
        <div className="grid grid-cols-1 lg:grid-cols-[1fr_1.4fr] gap-12 items-start">
          {/* Left: pitch */}
          <div>
            <div className="inline-flex items-center gap-2 mb-4">
              <Shield className="h-4 w-4 text-red-600" />
              <span className="text-[11px] uppercase tracking-wider text-red-600 font-semibold">
                Employer-Side · ฝั่งนายจ้าง
              </span>
            </div>
            <h2
              className="text-3xl sm:text-4xl font-semibold leading-tight tracking-tight"
              style={{ fontFamily: 'var(--font-ibm-plex-serif)' }}
            >
              ป้องกัน<span className="text-red-600">ลูกจ้างหัวหมอ</span>
              <br />
              โดยไม่ทำผิดกฎหมาย
            </h2>
            <p className="mt-5 text-base text-muted-foreground leading-relaxed max-w-md">
              AI ทั่วไปตอบเข้าข้างลูกจ้าง — Panya-AI ออกแบบมาเพื่อรู้{' '}
              <span className="font-semibold text-foreground">กลอุบายและช่องโหว่</span>{' '}
              ที่ลูกจ้างมักใช้ฟ้องนายจ้าง แล้วชี้แนวป้องกันที่
              <span className="font-semibold text-foreground">ถูกต้องตามกฎหมาย 100%</span>
            </p>

            {/* Gold rule */}
            <div className="my-6 h-px bg-gradient-to-r from-gold/60 to-transparent max-w-[200px]" />

            <p className="text-sm text-muted-foreground italic">
              &quot;รู้กฎ ยิ่งกว่าอีกฝ่าย = ไม่ต้องกลัวถูกฟ้อง&quot;
            </p>

            <Button
              onClick={() => navigate({ name: 'ask' })}
              className="mt-6 bg-navy text-gold hover:bg-navy/90 gap-2"
            >
              <Shield className="h-4 w-4" />
              เริ่มปรึกษาฝั่งนายจ้าง
            </Button>
          </div>

          {/* Right: 6 defense cards */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {EMPLOYER_DEFENSE_CARDS.map((c, i) => (
              <div
                key={c.t}
                className="card-premium rounded-xl p-4 relative group cursor-pointer hover:border-gold/40 transition"
              >
                <div
                  className="absolute top-3 right-4 text-xl font-semibold text-gold/50"
                  style={{ fontFamily: 'var(--font-ibm-plex-serif)' }}
                >
                  0{i + 1}
                </div>
                <div className="text-sm font-semibold text-foreground pr-8">{c.t}</div>
                <div className="text-xs text-muted-foreground mt-1.5 leading-relaxed">{c.d}</div>
                <div className="mt-3 pt-2 border-t border-dashed border-border/40 text-[11px] text-gold font-medium flex items-center gap-1.5">
                  <BookOpen className="h-3 w-3" />
                  {c.ref}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}

/* ---------- 4 Action Buttons ---------- */
function ActionButtons({ onNav }: { readonly onNav: (v: any) => void }) {
  const actions = [
    {
      label: 'ถาม AI',
      desc: 'คำถามกฎหมายแรงงาน พร้อมอ้างอิงมาตรา/ฎีกา',
      icon: Sparkles,
      view: { name: 'ask' as const },
      color: 'from-gold/15 to-gold/5 border-gold/30 hover:border-gold/50',
      iconColor: 'text-gold',
    },
    {
      label: 'ตรวจสัญญา',
      desc: 'วางข้อความสัญญา → AI หาข้อผิดกฎหมาย',
      icon: FileSearch,
      view: { name: 'contract-analysis' as const },
      color: 'from-red-500/10 to-red-500/5 border-red-500/20 hover:border-red-500/40',
      iconColor: 'text-red-500',
    },
    {
      label: 'สร้างเอกสาร',
      desc: '63 เทมเพลตพร้อมกรอก + ดาวน์โหลด PDF',
      icon: FileText,
      view: { name: 'pdf-builder' as const },
      color: 'from-blue-500/10 to-blue-500/5 border-blue-500/20 hover:border-blue-500/40',
      iconColor: 'text-blue-500',
    },
    {
      label: 'ประเมินความเสี่ยง',
      desc: 'Risk Matrix 5×5 สำหรับนายจ้าง',
      icon: Shield,
      view: { name: 'risk-matrix' as const },
      color: 'from-orange-500/10 to-orange-500/5 border-orange-500/20 hover:border-orange-500/40',
      iconColor: 'text-orange-500',
    },
  ];

  return (
    <div className="mt-12">
      <h2 className="text-center text-xl sm:text-2xl font-bold mb-2" style={{ fontFamily: 'var(--font-ibm-plex-serif)' }}>
        วันนี้คุณต้องการอะไร?
      </h2>
      <p className="text-center text-sm text-muted-foreground mb-6">
        เลือกงานที่ต้องการ — Panya-AI พร้อมช่วยทันที
      </p>
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-3 sm:gap-4 max-w-4xl mx-auto">
        {actions.map((a) => {
          const Icon = a.icon;
          return (
            <button
              type="button"
              key={a.label}
              onClick={() => onNav(a.view)}
              className={`group relative overflow-hidden rounded-xl border bg-gradient-to-br ${a.color} p-5 sm:p-6 text-left transition-all hover:shadow-lg hover:-translate-y-0.5`}
            >
              <div className="flex flex-col gap-3">
                <div className={`h-10 w-10 rounded-lg flex items-center justify-center bg-background/50 ${a.iconColor}`}>
                  <Icon className="h-5 w-5" />
                </div>
                <div>
                  <div className="text-sm sm:text-base font-bold text-foreground">
                    {a.label}
                  </div>
                  <div className="text-[11px] sm:text-xs text-muted-foreground mt-1 leading-snug">
                    {a.desc}
                  </div>
                </div>
              </div>
              <ArrowRight className="absolute bottom-3 right-3 h-4 w-4 text-muted-foreground opacity-0 group-hover:opacity-100 group-hover:translate-x-1 transition-all" />
            </button>
          );
        })}
      </div>
    </div>
  );
}
