'use client';

import { useEffect, useState } from 'react';
import { Users, Scale, Crown, ChevronDown, Settings2, Check } from 'lucide-react';
import { PERSONAS, getPersona, setPersona, type PersonaId } from '@/lib/persona';
import { cn } from '@/lib/utils';

const ICONS: Record<string, typeof Users> = { Users, Scale, Crown };

/**
 * PersonaSwitcher — compact dropdown shown in the Sidebar user info area.
 * Click → expands menu with all 3 personas + a "Manage / เปลี่ยนบทบาท" hint.
 */
export function PersonaSwitcher() {
  const [personaId, setPersonaId] = useState<PersonaId | null>(null);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    setPersonaId(getPersona());
    const onChange = () => setPersonaId(getPersona());
    window.addEventListener('panya-persona-changed', onChange);
    window.addEventListener('storage', onChange);
    return () => {
      window.removeEventListener('panya-persona-changed', onChange);
      window.removeEventListener('storage', onChange);
    };
  }, []);

  // Close on outside click
  useEffect(() => {
    if (!open) return;
    const handler = (e: MouseEvent) => {
      const target = e.target as HTMLElement;
      if (!target.closest('[data-persona-switcher]')) setOpen(false);
    };
    document.addEventListener('click', handler);
    return () => document.removeEventListener('click', handler);
  }, [open]);

  const current = personaId ? PERSONAS[personaId] : null;
  const CurrentIcon = current ? (ICONS[current.icon] || Users) : Settings2;

  return (
    <div data-persona-switcher className="relative">
      {/* Trigger button */}
      <button
        type="button"
        onClick={() => setOpen(!open)}
        className={cn(
          'flex w-full items-center gap-2 rounded-lg border px-2.5 py-1.5 text-[11px] transition-colors',
          current
            ? cn('border-transparent', current.color)
            : 'border-border/40 bg-white/5 text-muted-foreground hover:text-foreground hover:bg-accent/30'
        )}
        title={current ? `บทบาท: ${current.label}` : 'เลือกบทบาท'}
      >
        <CurrentIcon className="h-3.5 w-3.5 flex-shrink-0" />
        <span className="flex-1 text-left truncate font-medium">
          {current ? current.label : 'เลือกบทบาท'}
        </span>
        <ChevronDown className={cn('h-3 w-3 transition-transform', open && 'rotate-180')} />
      </button>

      {/* Dropdown menu */}
      {open && (
        <div className="absolute bottom-full mb-1 left-0 right-0 z-50 rounded-lg border border-border/60 bg-popover shadow-xl overflow-hidden">
          <div className="px-2 py-1.5 text-[10px] uppercase tracking-wider text-muted-foreground border-b border-border/40">
            เปลี่ยนบทบาท
          </div>
          <div className="p-1.5 space-y-0.5">
            {Object.values(PERSONAS).map((p) => {
              const Icon = ICONS[p.icon] || Users;
              const isActive = personaId === p.id;
              return (
                <button
                  type="button"
                  key={p.id}
                  onClick={() => {
                    setPersona(p.id);
                    setOpen(false);
                  }}
                  className={cn(
                    'flex w-full items-center gap-2 rounded-md px-2 py-1.5 text-[11px] transition-colors text-left',
                    isActive
                      ? 'bg-gold/10 text-gold'
                      : 'text-foreground/80 hover:bg-accent/40 hover:text-foreground'
                  )}
                >
                  <Icon className="h-3.5 w-3.5 flex-shrink-0" />
                  <div className="flex-1 min-w-0">
                    <div className="font-medium truncate">{p.label}</div>
                    <div className="text-[9px] text-muted-foreground truncate">{p.labelEn}</div>
                  </div>
                  {isActive && <Check className="h-3 w-3 flex-shrink-0" />}
                </button>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
}
