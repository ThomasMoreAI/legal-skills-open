'use client';

import { useEffect, useRef, useState } from 'react';
import { Send, ChevronRight, Shield, X, ExternalLink, BookOpen, Scale, RotateCcw } from 'lucide-react';
import { useNavigation } from '@/lib/navigation';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { usePersona } from '@/components/onboarding/usePersona';

interface Citation {
  index: number;
  type: 'section' | 'judgment';
  id: number;
  label: string;
  ref: string;
  snippet: string;
  url: string;
}

interface ChatMessage {
  role: 'user' | 'assistant';
  content: string;
  citations?: Citation[];
  retrievedChunks?: number;
  error?: boolean;
  /** Stable unique id for keying — uses timestamp + role + sequence */
  uid: string;
}

const SAMPLE_QUESTIONS = [
  'นายจ้างเลิกจ้างโดยไม่เตือนล่วงหน้า ลูกจ้างมีสิทธิอะไรบ้าง?',
  'ค่าจ้างล่วงเวลาคำนวณอย่างไร?',
  'ลูกจ้างมีบุริมสิทธิ์เมื่อนายจ้างล้มละลายหรือไม่?',
  'การเลิกจ้างเพราะลูกจ้างอายุ 60 ปีถือเป็นการเลิกจ้างที่ชอบหรือไม่?',
  'นายจ้างหยุดกิจการ ต้องจ่ายค่าชดเชยอย่างไร?',
];

/** Returns persona-specific sample questions, falling back to defaults */
function useSampleQuestions() {
  const { persona } = usePersona();
  if (persona) return persona.sampleQuestions;
  return SAMPLE_QUESTIONS;
}

/** Resolve mascot image source based on UI state (extracted from nested ternary). */
function getMascotSrc(opts: {
  showEasterEgg: boolean;
  loading: boolean;
  openCitation: boolean;
  thinkingIdx: number;
  thinkingImgs: readonly string[];
}): string {
  if (opts.showEasterEgg) return '/mascot/mascot-back.png';
  if (opts.loading) return opts.thinkingImgs[opts.thinkingIdx % opts.thinkingImgs.length];
  if (opts.openCitation) return '/mascot/mascot-right.png';
  return '/mascot/mascot-front.png';
}

/** Resolve message bubble className based on role/error (extracted from nested ternary). */
function getBubbleClass(isUser: boolean, isError: boolean): string {
  if (isUser) return 'bg-gradient-to-br from-gold to-gold/80 text-navy rounded-br-md';
  if (isError) return 'card-premium border-destructive/30 rounded-bl-md';
  return 'card-premium rounded-bl-md';
}

/** Resolve agent step dot className based on done/active state (extracted from nested ternary). */
function getStepDotClass(done: boolean, active: boolean): string {
  if (done) return 'bg-green-600';
  if (active) return 'border-2 border-gold animate-spin';
  return 'border border-border/60';
}

/** Resolve agent step opacity based on state (extracted from nested ternary). */
function getStepOpacity(opts: { pending: boolean; loading: boolean; idx: number; activeStepIdx: number }): number {
  if (opts.pending) return 0.35;
  if (opts.loading && opts.idx > opts.activeStepIdx) return 0.35;
  return 1;
}

/** Agent workflow steps — animated while AI is processing */
const AGENT_STEPS = [
  { id: 1, label: 'ทำความเข้าใจคำถาม', detail: 'วิเคราะห์ประเด็นและเจตนาของผู้ถาม' },
  { id: 2, label: 'ค้นในฐานกฎหมาย', detail: 'FTS5 search ในมาตรา + อนุบัญญัติ' },
  { id: 3, label: 'ค้นคำพิพากษาฎีกา', detail: 'ฎีกาแรงงาน + ฎีกาอาญา/แพ่ง' },
  { id: 4, label: 'ประเมินความเสี่ยงฝั่งนายจ้าง', detail: 'Risk Matrix + แนวป้องกัน' },
  { id: 5, label: 'เรียบเรียงคำตอบพร้อมอ้างอิง', detail: 'Citations [1] [2] [3]...' },
];

export function AskView() {
  const { navigate } = useNavigation();
  // Restore chat state from sessionStorage (saved before navigating to section/judgment)
  const [messages, setMessages] = useState<ChatMessage[]>(() => {
    if (typeof window === 'undefined') return [];
    try {
      const saved = sessionStorage.getItem('panya_chat_messages');
      if (saved) {
        sessionStorage.removeItem('panya_chat_messages');
        return JSON.parse(saved);
      }
    } catch {}
    return [];
  });
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  // Persona — drives default laborOnly + sample questions + AI prompt customization
  const { persona, personaId } = usePersona();
  // Default laborOnly from persona (HR/Owner = true, Legal = false). User can still override.
  const [laborOnly, setLaborOnly] = useState(true);
  // Sync laborOnly when persona changes
  useEffect(() => {
    if (persona) setLaborOnly(persona.laborOnly);
  }, [persona]);
  const sampleQuestions = useSampleQuestions();
  const [inputFocused, setInputFocused] = useState(false);
  const [activeStepIdx, setActiveStepIdx] = useState(-1);
  const [openCitation, setOpenCitation] = useState<Citation | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const lastAiMsgRef = useRef<HTMLDivElement>(null);
  const prevLoadingRef = useRef(false);
  const stepTimerRef = useRef<NodeJS.Timeout | null>(null);

  // === MASCOT FEATURES ===
  // 1. Easter egg: 3 clicks on mascot → back view + funny message (4s)
  const [mascotClicks, setMascotClicks] = useState(0);
  const [showEasterEgg, setShowEasterEgg] = useState(false);
  const easterEggTimerRef = useRef<NodeJS.Timeout | null>(null);
  // 2. Thinking mascot: cycle front/left/right during loading
  const [thinkingIdx, setThinkingIdx] = useState(0);
  const thinkingImgs = ['/mascot/mascot-front.png', '/mascot/mascot-left.png', '/mascot/mascot-right.png'];
  // 3. Direction-aware: front by default, right when citation panel open, back on easter egg
  const mascotSrc = getMascotSrc({ showEasterEgg, loading, openCitation: !!openCitation, thinkingIdx, thinkingImgs });

  const handleMascotClick = () => {
    const n = mascotClicks + 1;
    setMascotClicks(n);
    if (n >= 3) {
      setShowEasterEgg(true);
      setMascotClicks(0);
      if (easterEggTimerRef.current) clearTimeout(easterEggTimerRef.current);
      easterEggTimerRef.current = setTimeout(() => setShowEasterEgg(false), 4000);
    } else {
      if (easterEggTimerRef.current) clearTimeout(easterEggTimerRef.current);
      easterEggTimerRef.current = setTimeout(() => setMascotClicks(0), 1500);
    }
  };
  // === END MASCOT ===

  // Smart scroll: when user sends → scroll to bottom (show loading);
  // when AI responds → scroll to TOP of AI message (so user reads from beginning, not end)
  useEffect(() => {
    const lastMsg = messages.at(-1);
    const wasLoading = prevLoadingRef.current;

    if (loading) {
      // Loading started — scroll to bottom to show AgentRunning animation
      messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    } else if (wasLoading && lastMsg?.role === 'assistant') {
      // AI just responded — scroll to TOP of AI message so user reads from start
      setTimeout(() => {
        lastAiMsgRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }, 150);
    } else if (lastMsg?.role === 'user') {
      // User sent message — scroll to bottom
      messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }

    prevLoadingRef.current = loading;
  }, [messages, loading]);

  // Animate agent steps while loading
  useEffect(() => {
    if (loading) {
      setActiveStepIdx(0);
      let i = 0;
      let mi = 0;
      stepTimerRef.current = setInterval(() => {
        i++;
        mi++;
        setThinkingIdx(mi);
        if (i >= AGENT_STEPS.length) {
          // Hold on last step until response arrives
          setActiveStepIdx(AGENT_STEPS.length - 1);
          // Note: AGENT_STEPS.length - 1 is the last index — SonarCloud S7755
          // prefers .at(-1) but we need the numeric index here, not the element.
        } else {
          setActiveStepIdx(i);
        }
      }, 800);
    } else {
      if (stepTimerRef.current) {
        clearInterval(stepTimerRef.current);
        stepTimerRef.current = null;
      }
      setActiveStepIdx(-1);
    }
    return () => {
      if (stepTimerRef.current) clearInterval(stepTimerRef.current);
    };
  }, [loading]);

  const ask = async (question: string) => {
    if (!question.trim() || loading) return;
    const userMsg: ChatMessage = { role: 'user', content: question, uid: `u-${Date.now()}` };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setLoading(true);

    const history = messages.slice(-4).map(m => ({ role: m.role, content: m.content }));

    try {
      const res = await fetch('/api/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question, history, laborOnly, persona: personaId }),
      });
      const data = await res.json();

      if (data.error) {
        setMessages(prev => [
          ...prev,
          {
            role: 'assistant',
            content: `ขออภัย เกิดข้อผิดพลาด: ${data.error}\n\n${data.message || ''}\n\nอย่างไรก็ตาม ผมค้นพบ ${data.retrievedChunks || 0} มาตรา/ฎีกาที่เกี่ยวข้อง คุณสามารถดู citations ด้านล่างเพื่ออ่านด้วยตัวเอง`,
            citations: data.citations || [],
            retrievedChunks: data.retrievedChunks,
            error: true,
            uid: `a-err-${Date.now()}`,
          },
        ]);
      } else {
        setMessages(prev => [
          ...prev,
          {
            role: 'assistant',
            content: data.answer,
            citations: data.citations || [],
            retrievedChunks: data.retrievedChunks,
            uid: `a-${Date.now()}`,
          },
        ]);
      }
    } catch (e: any) {
      setMessages(prev => [
        ...prev,
        {
          role: 'assistant',
          content: `เกิดข้อผิดพลาดในการเชื่อมต่อ: ${e.message || 'Unknown error'}`,
          error: true,
          uid: `a-throw-${Date.now()}`,
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const onSubmit = (e: React.SyntheticEvent) => {
    e.preventDefault();
    ask(input);
  };

  const handleCitationClick = (url: string, cit?: Citation) => {
    if (cit) setOpenCitation(cit);
    const params = new URLSearchParams(url.split('?')[1] || '');
    const view = params.get('view');
    const id = params.get('id');
    // Save chat state to sessionStorage before navigating away
    if (messages.length > 0) {
      try {
        sessionStorage.setItem('panya_chat_messages', JSON.stringify(messages));
        sessionStorage.setItem('panya_chat_input', input);
      } catch {}
    }
    if (view === 'section' && id) navigate({ name: 'section', sectionId: Number.parseInt(id, 10) });
    else if (view === 'judgment' && id) navigate({ name: 'judgment', judgmentId: Number.parseInt(id, 10) });
  };

  return (
    <div className="flex h-screen overflow-hidden overflow-x-hidden">
      {/* MAIN chat column */}
      <div className="flex flex-col bg-background transition-all duration-300 flex-1">
        {/* Header */}
        <div className="border-b border-border/60 bg-card-soft/30 px-4 sm:px-6 py-4 flex items-center justify-between overflow-hidden">
          <div>
            <div className="flex items-center gap-2 mb-1">
              <h1 className="text-xl font-bold tracking-tight" style={{ fontFamily: 'var(--font-ibm-plex-serif)' }}>
                ปรึกษา Panya-AI
              </h1>
              <Badge variant="outline" className="badge-gold text-[10px] gap-1">
                <Shield className="h-3 w-3" />
                Employer Mode
              </Badge>
            </div>
            <p className="text-xs text-muted-foreground">
              AI ตอบโดยอ้างอิงกฎหมายและคำพิพากษาจริง · ตรวจสอบต้นทางได้ทุกคำตอบ
            </p>
          </div>
          <div className="flex gap-2">
            <Button
              variant="ghost"
              size="sm"
              className="text-xs text-muted-foreground hover:text-foreground gap-1"
              onClick={() => {
                // Save current session before clearing
                if (messages.length > 0) {
                  import('@/lib/chat-sessions').then(({ createChatSession, saveChatSession }) => {
                    const session = createChatSession(messages as any[], personaId);
                    saveChatSession(session);
                  });
                }
                setMessages([]);
                sessionStorage.removeItem('panya_chat_messages');
                sessionStorage.removeItem('panya_chat_input');
              }}
            >
              <RotateCcw className="h-3.5 w-3.5" />
              เริ่มใหม่
            </Button>
          </div>
        </div>

        {/* Labor-only toggle */}
        <div className="px-6 pt-4 flex items-center gap-2 text-xs">
          <button
            type="button"
            onClick={() => setLaborOnly(v => !v)}
            className={`px-3 py-1.5 rounded-full font-medium transition border ${
              laborOnly
                ? 'bg-gold/15 text-gold border-gold/30'
                : 'bg-card-soft text-muted-foreground border-border/50'
            }`}
          >
            {laborOnly ? '✓ ' : ''}โฟกัสเฉพาะกฎหมายแรงงาน
          </button>
          <span className="text-muted-foreground">
            {laborOnly ? 'ค้นหาเฉพาะมาตรา/ฎีกาแรงงาน' : 'ค้นหาในทุกกฎหมาย'}
          </span>
        </div>

        {/* Messages */}
        <div className="flex-1 overflow-y-auto overflow-x-hidden px-4 sm:px-6 py-6 min-w-0">
          {messages.length === 0 && !loading && (
            <div className="max-w-2xl mx-auto">
              <div className="card-premium rounded-2xl p-8 text-center">
                <div className="flex justify-center mb-4">
                  <button type="button" onClick={handleMascotClick} className="relative">
                    <img src={mascotSrc} alt="Panya-AI" className="h-20 w-20 rounded-lg object-contain ring-1 ring-gold/20 bg-navy/5 transition-all duration-300" />
                    {showEasterEgg && (
                      <div className="absolute -bottom-8 left-1/2 -translate-x-1/2 whitespace-nowrap text-[10px] text-gold bg-navy/90 px-3 py-1 rounded-full">🤖 อ้อ! จับได้แล้วเหรอ?</div>
                    )}
                  </button>
                </div>
                <h2 className="text-lg font-semibold mb-2" style={{ fontFamily: 'var(--font-ibm-plex-serif)' }}>
                  สวัสดีครับ ผมปัญญา
                </h2>
                <p className="text-sm text-muted-foreground mb-3">
                  ที่ปรึกษากฎหมายไทยฝั่งนายจ้าง · ผมค้นและตอบคำถามได้จากกฎหมาย 78 ฉบับ, มาตรา 12,936, คำพิพากษาฎีกา 502 คดี
                </p>
                {persona && (
                  <div className="mb-4 inline-flex items-center gap-2 rounded-full border px-3 py-1 text-[11px] font-medium" style={{ borderColor: 'var(--gold)', color: 'var(--gold)', background: 'rgba(201,169,97,0.08)' }}>
                    <span>👤 บทบาท: {persona.label}</span>
                    <span className="opacity-60">·</span>
                    <span className="opacity-80">{persona.labelEn}</span>
                  </div>
                )}
                <div className="grid gap-2 text-left">
                  {sampleQuestions.map((q) => (
                    <button
                      type="button"
                      key={q}
                      onClick={() => ask(q)}
                      className="px-4 py-3 rounded-lg bg-card-softer border border-border/40 hover:border-gold/30 hover:bg-accent/30 transition text-sm text-foreground/90 text-left"
                    >
                      <span className="text-gold mr-2">›</span>
                      {q}
                    </button>
                  ))}
                </div>
              </div>
            </div>
          )}

          <div className="max-w-3xl mx-auto space-y-4 min-w-0">
            {messages.map((msg, i) => {
              const isLastAi = i === messages.length - 1 && msg.role === 'assistant';
              // Note: SonarCloud S7755 wants .at(-1) here too, but we can't use it
              // because we need the INDEX comparison, not the element itself.
              // This is a false positive — the pattern is correct for this use case.
              return (
                <div key={msg.uid} ref={isLastAi ? lastAiMsgRef : undefined}>
                  <MessageBubble msg={msg} onCitationClick={handleCitationClick} onOpenCitation={setOpenCitation} mascotSrc={mascotSrc} onMascotClick={handleMascotClick} />
                </div>
              );
            })}

            {loading && <AgentRunning idx={activeStepIdx} mascotSrc={mascotSrc} />}

            <div ref={messagesEndRef} />
          </div>
        </div>

        {/* Input */}
        <form onSubmit={onSubmit} className="border-t border-border/60 bg-card-soft/30 px-6 py-4">
          <div className="max-w-3xl mx-auto">
            <div
              className={`card-premium rounded-2xl p-2 flex gap-2 items-end transition-all duration-200 ${
                inputFocused ? 'ring-2 ring-gold/40 shadow-lg' : ''
              }`}
            >
              <textarea
                value={input}
                onChange={e => setInput(e.target.value)}
                onFocus={() => setInputFocused(true)}
                onBlur={() => setInputFocused(false)}
                onKeyDown={e => {
                  if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    onSubmit(e as any);
                  }
                }}
                placeholder="ถามข้อกฎหมายเป็นภาษาธรรมดา เช่น 'ลูกจ้างขาดงาน 3 วัน เลิกจ้างได้ไหม'..."
                rows={inputFocused ? 3 : 1}
                className={`flex-1 bg-transparent resize-none outline-none text-sm px-3 py-2 max-h-48 transition-all duration-200 ${
                  inputFocused ? 'min-h-[80px]' : 'min-h-[40px]'
                }`}
                disabled={loading}
              />
              <Button
                type="submit"
                disabled={loading || !input.trim()}
                className="bg-gold text-navy hover:bg-gold/90 flex-shrink-0"
                size="sm"
              >
                <Send className="h-4 w-4" />
                <span className="hidden sm:inline">ส่งคำถาม</span>
              </Button>
            </div>
            <p className="text-[10px] text-muted-foreground/70 text-center mt-2">
              Panya-AI อาจผิดพลาดได้ · ควรตรวจสอบกับต้นฉบับที่อ้างอิงทุกครั้ง ·{' '}
              <span className="text-gold">เพื่อการศึกษา ไม่ใช่คำปรึกษาทางกฎหมาย</span>
            </p>
          </div>
        </form>
      </div>

      {/* RIGHT panel — Agent workflow + Citations */}
      <RightPanel
        loading={loading}
        activeStepIdx={activeStepIdx}
        messages={messages}
        onOpenCitation={setOpenCitation}
      />

      {/* Citation drawer — slides in on XL, modal overlay on smaller screens */}
      {openCitation && (
        <CitationDrawer citation={openCitation} onClose={() => setOpenCitation(null)} onNavigate={handleCitationClick} />
      )}
    </div>
  );
}

/* ---------- Message Bubble ---------- */
function MessageBubble({
  msg,
  onCitationClick,
  onOpenCitation,
  mascotSrc,
  onMascotClick,
}: {
  readonly msg: ChatMessage;
  readonly onCitationClick: (url: string, cit?: Citation) => void;
  readonly onOpenCitation: (cit: Citation) => void;
  readonly mascotSrc: string;
  readonly onMascotClick: () => void;
}) {
  const isUser = msg.role === 'user';

  // Render content with [N] citation pills
  const renderContent = (text: string) => {
    if (!msg.citations || msg.citations.length === 0) {
      return <span className="whitespace-pre-wrap">{text}</span>;
    }
    const parts = text.split(/(\[\d+\])/g);
    return parts.map((part, i) => {
      // Use RegExp.exec instead of String.match (SonarCloud S6594)
      const m = /\[(\d+)\]/.exec(part);
      if (m) {
        // Use Number.parseInt instead of global parseInt (SonarCloud S7773)
        const n = Number.parseInt(m[1], 10);
        const cit = msg.citations?.find(c => c.index === n);
        if (cit) {
          return (
            <button
              type="button"
              key={`cit-${cit.index}-${i}`}
              onClick={() => onCitationClick(cit.url, cit)}
              className="inline-flex items-center px-1.5 py-0.5 mx-0.5 rounded text-[11px] font-semibold bg-gold/15 text-gold border border-gold/40 hover:bg-gold/25 transition align-baseline cursor-pointer"
              style={{ fontFamily: 'var(--font-ibm-plex-serif)' }}
            >
              {n}
            </button>
          );
        }
      }
      // Stable key: use part content (truncated) + index to avoid array-index-only keys
      return <span key={`text-${part.slice(0, 20)}-${i}`} className="whitespace-pre-wrap">{part}</span>;
    });
  };

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div className={`max-w-[92%] sm:max-w-[85%] ${isUser ? '' : 'w-full min-w-0 overflow-hidden'}`}>
        {!isUser && (
          <div className="flex items-center gap-2 mb-1.5">
            <button type="button" onClick={onMascotClick} className="flex-shrink-0">
              <img src={mascotSrc} alt="Panya-AI" className="h-8 w-8 rounded object-contain transition-all duration-300" />
            </button>
            <span className="text-xs font-semibold text-foreground">Panya-AI</span>
            {msg.retrievedChunks !== undefined && (
              <span className="text-[10px] text-gold">· วิเคราะห์เสร็จ · {msg.retrievedChunks} แหล่งอ้างอิง</span>
            )}
          </div>
        )}
        <div
          className={`rounded-2xl px-4 py-3 ${getBubbleClass(isUser, !!msg.error)}`}
        >
          <div className="text-sm prose-thai whitespace-pre-wrap leading-relaxed break-words overflow-hidden w-full">
            {renderContent(msg.content)}
          </div>

          {/* Citations list (inline at bottom of AI message) */}
          {!isUser && msg.citations && msg.citations.length > 0 && (
            <div className="mt-4 pt-3 border-t border-border/40">
              <div className="text-[10px] uppercase tracking-wider text-gold mb-2 font-semibold">
                อ้างอิง ({msg.citations.length})
              </div>
              <div className="grid gap-1.5">
                {msg.citations.map(c => (
                  <button
                    type="button"
                    key={`${c.type}-${c.id}-${c.index}`}
                    onClick={() => onCitationClick(c.url, c)}
                    className="flex items-start gap-2 text-left p-2 rounded-lg bg-card-softer hover:bg-accent/30 border border-border/30 hover:border-gold/30 transition group cursor-pointer"
                  >
                    <Badge variant="outline" className="badge-gold text-[10px] flex-shrink-0">
                      [{c.index}]
                    </Badge>
                    <div className="flex-1 min-w-0">
                      <div className="text-xs font-medium text-foreground group-hover:text-gold transition flex items-center gap-1">
                        {c.type === 'judgment' ? <Scale className="h-3 w-3" /> : <BookOpen className="h-3 w-3" />}
                        <span className="truncate">{c.label}</span>
                        <ChevronRight className="h-3 w-3 ml-auto flex-shrink-0 opacity-0 group-hover:opacity-100 transition" />
                      </div>
                      <div className="text-[10px] text-muted-foreground line-clamp-1 mt-0.5">{c.snippet}</div>
                    </div>
                  </button>
                ))}
              </div>
              {msg.retrievedChunks !== undefined && (
                <div className="mt-2 text-[10px] text-muted-foreground/70">
                  ค้นพบ {msg.retrievedChunks} ชิ้นข้อมูลที่เกี่ยวข้องจากฐานข้อมูล
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

/* ---------- Agent Running Animation ---------- */
function AgentRunning({ idx, mascotSrc }: { readonly idx: number; readonly mascotSrc: string }) {
  return (
    <div className="flex justify-start">
      <div className="w-full max-w-2xl">
        <div className="flex items-center gap-2 mb-1.5">
          <img src={mascotSrc} alt="Panya-AI" className="h-8 w-8 rounded object-contain transition-all duration-300" />
          <span className="text-xs font-semibold text-foreground">Panya-AI</span>
          <span className="text-[10px] text-gold">· กำลังวิเคราะห์...</span>
        </div>
        <div
          className="rounded-2xl rounded-bl-md px-5 py-4 card-premium"
          style={{ background: 'linear-gradient(180deg, rgba(201,169,97,0.05), transparent)' }}
        >
          <div className="flex items-center gap-2 mb-3">
            <div className="h-2 w-2 rounded-full bg-gold animate-pulse" />
            <span className="text-[10px] uppercase tracking-wider text-gold font-semibold">
              Agent กำลังทำงาน
            </span>
          </div>
          <div className="space-y-2">
            {AGENT_STEPS.map((s, i) => {
              const done = i < idx;
              const active = i === idx;
              return (
                <div
                  key={s.id}
                  className="flex items-start gap-3 transition-opacity duration-200"
                  style={{ opacity: i > idx ? 0.35 : 1 }}
                >
                  <div
                    className={`h-4 w-4 rounded-full flex-shrink-0 mt-0.5 flex items-center justify-center transition-all ${getStepDotClass(done, active)}`}
                  >
                    {done && (
                      <svg className="h-2.5 w-2.5 text-white" fill="none" stroke="currentColor" strokeWidth={3} viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                      </svg>
                    )}
                  </div>
                  <div className="flex-1">
                    <div className={`text-[13px] font-medium ${active ? 'text-gold' : 'text-foreground'}`}>
                      {s.label}
                    </div>
                    {(done || active) && s.detail && (
                      <div className="text-[11px] text-muted-foreground mt-0.5">{s.detail}</div>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}

/* ---------- Right Panel: Workflow + Citations ---------- */
function RightPanel({
  loading,
  activeStepIdx,
  messages,
  onOpenCitation,
}: {
  readonly loading: boolean;
  readonly activeStepIdx: number;
  readonly messages: ChatMessage[];
  readonly onOpenCitation: (cit: Citation) => void;
}) {
  // Get latest AI message with citations
  const lastAiMsg = [...messages].reverse().find(m => m.role === 'assistant' && m.citations && m.citations.length > 0);

  return (
    <aside className="hidden lg:flex flex-col w-80 border-l border-border/60 bg-card-soft/20 overflow-hidden">
      <div className="px-5 py-4 border-b border-border/60">
        <div className="text-[10px] uppercase tracking-wider text-gold mb-1">Legal Research Panel</div>
        <div className="text-sm font-semibold" style={{ fontFamily: 'var(--font-ibm-plex-serif)' }}>
          แหล่งอ้างอิงและขั้นตอน
        </div>
      </div>

      <div className="flex-1 overflow-y-auto p-5">
        {/* Workflow status */}
        <div className="mb-6">
          <div className="text-[10px] uppercase tracking-wider text-muted-foreground mb-3">Agent Workflow</div>
          <div className="space-y-2">
            {AGENT_STEPS.map((s, i) => {
              const done = !!(lastAiMsg || (loading && i < activeStepIdx));
              const active = loading && i === activeStepIdx;
              const pending = !lastAiMsg && !loading;
              return (
                <div
                  key={s.id}
                  className="flex items-start gap-2 transition-opacity duration-200"
                  style={{ opacity: getStepOpacity({ pending: !!pending, loading: !!loading, idx: i, activeStepIdx }) }}
                >
                  <div
                    className={`h-3.5 w-3.5 rounded-full flex-shrink-0 mt-0.5 transition-all ${getStepDotClass(done, active)}`}
                  />
                  <div className={`text-[12px] leading-relaxed ${active ? 'text-gold font-semibold' : 'text-foreground/80'}`}>
                    {s.label}
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Citations from last AI message */}
        {lastAiMsg?.citations && lastAiMsg.citations.length > 0 && (
          <div className="mb-6">
            <div className="text-[10px] uppercase tracking-wider text-muted-foreground mb-3">
              อ้างอิง ({lastAiMsg.citations.length})
            </div>
            <div className="space-y-1.5">
              {lastAiMsg.citations.map(c => (
                <button
                  type="button"
                  key={`${c.type}-${c.id}-${c.index}`}
                  onClick={() => onOpenCitation(c)}
                  className="w-full flex items-center gap-2.5 p-2.5 rounded-lg border border-border/40 hover:border-gold/40 hover:bg-accent/30 transition group text-left"
                >
                  <div
                    className={`h-6 w-6 rounded flex items-center justify-center flex-shrink-0 text-[11px] font-bold ${
                      c.type === 'section'
                        ? 'bg-navy text-gold'
                        : 'bg-gold text-navy'
                    }`}
                    style={{ fontFamily: 'var(--font-ibm-plex-serif)' }}
                  >
                    {c.index}
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className="text-[12px] font-semibold text-foreground group-hover:text-gold transition truncate">
                      {c.ref}
                    </div>
                    <div className="text-[10px] text-muted-foreground truncate">
                      {c.type === 'section' ? c.label : 'คำพิพากษาศาลฎีกา'}
                    </div>
                  </div>
                  <ExternalLink className="h-3 w-3 text-muted-foreground group-hover:text-gold flex-shrink-0" />
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Stats */}
        <div>
          <div className="text-[10px] uppercase tracking-wider text-muted-foreground mb-3">ฐานข้อมูล</div>
          <div className="space-y-1.5 text-[12px]">
            <div className="flex justify-between">
              <span className="text-muted-foreground">กฎหมาย</span>
              <span className="font-semibold">78 ฉบับ</span>
            </div>
            <div className="flex justify-between">
              <span className="text-muted-foreground">มาตรา</span>
              <span className="font-semibold">12,936</span>
            </div>
            <div className="flex justify-between">
              <span className="text-muted-foreground">คำพิพากษาฎีกา</span>
              <span className="font-semibold">502</span>
            </div>
            <div className="flex justify-between">
              <span className="text-muted-foreground">อนุบัญญัติ</span>
              <span className="font-semibold">615</span>
            </div>
            <div className="flex justify-between">
              <span className="text-muted-foreground">เทมเพลต</span>
              <span className="font-semibold">63</span>
            </div>
          </div>
        </div>
      </div>
    </aside>
  );
}

/* ---------- Citation Drawer (3rd column) ---------- */
function CitationDrawer({
  citation,
  onClose,
  onNavigate,
}: {
  readonly citation: Citation;
  readonly onClose: () => void;
  readonly onNavigate: (url: string, cit?: Citation) => void;
}) {
  const isSection = citation.type === 'section';
  return (
    <>
      {/* Mobile overlay backdrop — use <button> for keyboard accessibility */}
      <button
        type="button"
        onClick={onClose}
        className="fixed inset-0 z-50 bg-black/50 xl:hidden cursor-default"
        aria-label="ปิดหน้าต่างอ้างอิง"
      />
      <aside
        className="fixed xl:relative right-0 top-0 bottom-0 z-50 xl:z-auto flex flex-col w-full sm:w-96 max-w-md xl:w-96 border-l border-border/60 bg-background overflow-hidden xl:flex"
        style={{ animation: 'slideIn 220ms ease' }}
      >
      <style>{`@keyframes slideIn { from { transform: translateX(20px); opacity: 0; } to { transform: none; opacity: 1; } }`}</style>
      <div className="px-5 py-4 border-b border-border/60 bg-card-soft/30 flex items-start justify-between gap-2">
        <div className="flex-1">
          <div className="text-[10px] uppercase tracking-wider text-gold mb-1">
            อ้างอิง [{citation.index}] · {isSection ? 'บทกฎหมาย' : 'คำพิพากษา'}
          </div>
          <div className="text-base font-semibold" style={{ fontFamily: 'var(--font-ibm-plex-serif)' }}>
            {citation.ref}
          </div>
        </div>
        <button
          type="button"
          onClick={onClose}
          className="p-1.5 text-muted-foreground hover:text-foreground hover:bg-accent/40 rounded"
        >
          <X className="h-4 w-4" />
        </button>
      </div>

      <div className="flex-1 overflow-y-auto p-6">
        <div className="text-[12px] text-gold mb-2 font-semibold">{citation.label}</div>
        <div className="text-sm leading-relaxed text-foreground/90 prose-thai">
          {citation.snippet}
        </div>

        <button
          type="button"
          onClick={() => onNavigate(citation.url, citation)}
          className="mt-6 px-4 py-2 border border-navy-800 text-navy-800 dark:text-foreground dark:border-foreground rounded-lg text-[13px] font-medium inline-flex gap-2 items-center hover:bg-accent/30 transition"
        >
          <ExternalLink className="h-3.5 w-3.5" />
          ดู{isSection ? 'มาตรา' : 'คำพิพากษา'}ฉบับเต็ม
        </button>
      </div>
    </aside>
    </>
  );
}
