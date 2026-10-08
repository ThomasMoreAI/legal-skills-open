'use client';

import { useState } from 'react';
import { Users, Scale, Crown, Check, Sparkles, X, ArrowRight } from 'lucide-react';
import { PERSONAS, setPersona, markOnboarded, type PersonaId } from '@/lib/persona';
import { cn } from '@/lib/utils';

interface PersonaOnboardingProps {
  /** Called when user picks a persona OR skips */
  readonly onClose: () => void;
}

const ICONS: Record<string, typeof Users> = { Users, Scale, Crown };

/** Resolve persona card className based on selected/hovered state (extracted from nested ternary). */
function getCardClass(isSelected: boolean, isHovered: boolean): string {
  if (isSelected) return 'border-gold bg-gold/8 shadow-lg shadow-gold/10';
  if (isHovered) return 'border-border/80 bg-accent/30';
  return 'border-border/40 bg-card/30 hover:bg-accent/20';
}

export function PersonaOnboarding({ onClose }: PersonaOnboardingProps) {
  const [selected, setSelected] = useState<PersonaId | null>(null);
  const [hovered, setHovered] = useState<PersonaId | null>(null);

  const handleConfirm = () => {
    if (selected) {
      setPersona(selected);
    }
    markOnboarded();
    onClose();
  };

  const handleSkip = () => {
    markOnboarded();
    onClose();
  };

  const personaList = Object.values(PERSONAS);

  return (
    <div className="fixed inset-0 z-[100] flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm">
      <div
        className="relative w-full max-w-3xl rounded-2xl border border-gold/30 shadow-2xl max-h-[92vh] overflow-y-auto"
        style={{ background: 'linear-gradient(180deg, #0E1F45 0%, #0A1633 100%)' }}
      >
        {/* Header */}
        <div className="flex items-start justify-between p-6 border-b border-border/40">
          <div className="flex items-start gap-3">
            <img src="/mascot/mascot-front.png" alt="" className="h-12 w-12 object-contain" />
            <div>
              <h2 className="text-xl font-bold text-foreground flex items-center gap-2">
                เลือกบทบาทของคุณ
                <Sparkles className="h-4 w-4 text-gold" />
              </h2>
              <p className="text-sm text-muted-foreground mt-0.5">
                Panya-AI จะปรับคำตอบ เทมเพลต และคำแนะนำให้เหมาะกับงานของคุณ
              </p>
            </div>
          </div>
          <button
            type="button"
            onClick={handleSkip}
            className="text-muted-foreground hover:text-foreground p-1 rounded-md hover:bg-accent/40"
            aria-label="ปิด"
          >
            <X className="h-5 w-5" />
          </button>
        </div>

        {/* Persona cards */}
        <div className="p-6 grid gap-4 md:grid-cols-3">
          {personaList.map((p) => {
            const Icon = ICONS[p.icon] || Users;
            const isSelected = selected === p.id;
            const isHovered = hovered === p.id;
            return (
              <button
                type="button"
                key={p.id}
                onClick={() => setSelected(p.id)}
                onMouseEnter={() => setHovered(p.id)}
                onMouseLeave={() => setHovered(null)}
                className={cn(
                  'group relative text-left rounded-xl border p-5 transition-all duration-200',
                  getCardClass(isSelected, isHovered)
                )}
              >
                {/* Selected check badge */}
                {isSelected && (
                  <div className="absolute top-3 right-3 flex h-6 w-6 items-center justify-center rounded-full bg-gold text-navy">
                    <Check className="h-3.5 w-3.5" strokeWidth={3} />
                  </div>
                )}

                {/* Icon + label */}
                <div className="flex items-center gap-3 mb-3">
                  <div className={cn('flex h-10 w-10 items-center justify-center rounded-lg border', p.color)}>
                    <Icon className="h-5 w-5" />
                  </div>
                  <div>
                    <div className="font-bold text-foreground">{p.label}</div>
                    <div className="text-[10px] uppercase tracking-wider text-muted-foreground">{p.labelEn}</div>
                  </div>
                </div>

                {/* Description */}
                <p className="text-xs text-muted-foreground leading-relaxed mb-4">
                  {p.description}
                </p>

                {/* Focus tags */}
                <div className="flex flex-wrap gap-1.5">
                  {p.skillPriority.slice(0, 2).map((s) => (
                    <span key={s} className="rounded-md bg-white/5 border border-border/40 px-2 py-0.5 text-[10px] text-muted-foreground">
                      {s === 'contract-review' && '🔍 ตรวจสัญญา'}
                      {s === 'risk-assessment' && '⚠️ ประเมินความเสี่ยง'}
                      {s === 'document-drafting' && '📝 ร่างเอกสาร'}
                      {s === 'legal-qa' && '💬 ถามตอบ'}
                    </span>
                  ))}
                  <span className="rounded-md bg-white/5 border border-border/40 px-2 py-0.5 text-[10px] text-muted-foreground">
                    {p.laborOnly ? '⚡ เน้นแรงงาน' : '🌐 ทุกกฎหมาย'}
                  </span>
                </div>
              </button>
            );
          })}
        </div>

        {/* Selected persona preview — show sample questions */}
        {selected && (
          <div className="px-6 pb-2">
            <div className="rounded-lg border border-gold/20 bg-gold/5 p-4">
              <div className="text-xs font-semibold text-gold mb-2 flex items-center gap-1.5">
                <Sparkles className="h-3 w-3" />
                ตัวอย่างคำถามสำหรับ {PERSONAS[selected].label}
              </div>
              <ul className="space-y-1.5">
                {PERSONAS[selected].sampleQuestions.slice(0, 3).map((q) => (
                  <li key={q} className="text-xs text-foreground/80 flex items-start gap-2">
                    <span className="text-gold mt-0.5">▸</span>
                    <span>{q}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        )}

        {/* Footer */}
        <div className="flex items-center justify-between gap-3 p-6 border-t border-border/40">
          <button
            type="button"
            onClick={handleSkip}
            className="text-sm text-muted-foreground hover:text-foreground px-3 py-2 rounded-md hover:bg-accent/30"
          >
            ข้าม — ใช้ค่าเริ่มต้น
          </button>
          <button
            type="button"
            onClick={handleConfirm}
            disabled={!selected}
            className={cn(
              'inline-flex items-center gap-2 rounded-lg px-5 py-2.5 text-sm font-semibold transition-all',
              selected
                ? 'bg-gradient-to-r from-gold to-gold/80 text-navy hover:from-gold/90 hover:to-gold/70 shadow-md shadow-gold/20'
                : 'bg-white/5 text-muted-foreground cursor-not-allowed'
            )}
          >
            เริ่มใช้งาน
            <ArrowRight className="h-4 w-4" />
          </button>
        </div>
      </div>
    </div>
  );
}
