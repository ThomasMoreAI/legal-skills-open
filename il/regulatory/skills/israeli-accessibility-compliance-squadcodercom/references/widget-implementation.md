# Accessibility Preferences Widget: Implementation Reference

Copy-pasteable TypeScript/React code for a Regulation 35 / IS 5568 accessibility preferences widget. IS 5568 is anchored to WCAG 2.0 AA (it adds some 2.1-aligned criteria; sources differ).

**Consult this file when** the user wants to ship the widget itself, not just audit an existing site. The main `SKILL.md` covers compliance guidance; this file covers the implementation.

**Scope reminder:** this widget is a user-preference comfort tool. It toggles CSS classes on `<html>`. It does NOT mutate content DOM, inject `alt` text, rewrite ARIA, or auto-remediate anything. See "Avoiding Overlay Anti-Patterns" in `SKILL.md`.

Stack assumptions: Next.js App Router (13+), React 18+, TypeScript, Tailwind (optional but referenced), shadcn/ui Sheet + Button, framer-motion (optional).

---

## 1. Preferences Core (`lib/a11y-prefs/core.ts`)

Pure helpers with no `'use client'` directive, safe to import from Server Components (needed for the FOUC `<script>` injection in the root layout).

```ts
export type ContrastMode = 'off' | 'high' | 'invert' | 'mono';
export type TextSize = 100 | 115 | 130 | 150;
export type LineSpacing = 'normal' | '16' | '20';

export interface A11yPrefs {
  version: number;
  links: boolean;
  contrast: ContrastMode;
  textSize: TextSize;
  lineSpacing: LineSpacing;
  readableFont: boolean;
  headings: boolean;
  cursorBlack: boolean;
  cursorLarge: boolean;
  reduceMotion: boolean;
}

export const A11Y_VERSION = 1;
export const A11Y_STORAGE_KEY = 'site_a11y_prefs_v1';

export const DEFAULT_PREFS: A11yPrefs = Object.freeze({
  version: A11Y_VERSION,
  links: false,
  contrast: 'off',
  textSize: 100,
  lineSpacing: 'normal',
  readableFont: false,
  headings: false,
  cursorBlack: false,
  cursorLarge: false,
  reduceMotion: false,
});

const CONTRAST_CYCLE: ContrastMode[] = ['off', 'high', 'invert', 'mono'];
const TEXT_SIZE_CYCLE: TextSize[] = [100, 115, 130, 150];
const LINE_SPACING_CYCLE: LineSpacing[] = ['normal', '16', '20'];

export function nextContrast(c: ContrastMode): ContrastMode {
  return CONTRAST_CYCLE[(CONTRAST_CYCLE.indexOf(c) + 1) % CONTRAST_CYCLE.length];
}
export function nextTextSize(s: TextSize): TextSize {
  return TEXT_SIZE_CYCLE[(TEXT_SIZE_CYCLE.indexOf(s) + 1) % TEXT_SIZE_CYCLE.length];
}
export function nextLineSpacing(l: LineSpacing): LineSpacing {
  return LINE_SPACING_CYCLE[(LINE_SPACING_CYCLE.indexOf(l) + 1) % LINE_SPACING_CYCLE.length];
}

export function isAnyActive(prefs: A11yPrefs): boolean {
  return (
    prefs.links ||
    prefs.contrast !== 'off' ||
    prefs.textSize !== 100 ||
    prefs.lineSpacing !== 'normal' ||
    prefs.readableFont ||
    prefs.headings ||
    prefs.cursorBlack ||
    prefs.cursorLarge ||
    prefs.reduceMotion
  );
}

// SINGLE SOURCE OF TRUTH: drives both the runtime applyPrefsToElement() and
// the FOUC bootstrap script below. The JS-expression string column is serialized
// into the bootstrap so the two cannot drift.
const CLASS_RULES: ReadonlyArray<[
  className: string,
  predicate: (p: A11yPrefs) => boolean,
  js: string
]> = [
  ['a11y-links',           (p) => p.links,                 '!!p.links'],
  ['a11y-contrast-high',   (p) => p.contrast === 'high',   "p.contrast==='high'"],
  ['a11y-contrast-invert', (p) => p.contrast === 'invert', "p.contrast==='invert'"],
  ['a11y-contrast-mono',   (p) => p.contrast === 'mono',   "p.contrast==='mono'"],
  ['a11y-text-115',        (p) => p.textSize === 115,      'p.textSize===115'],
  ['a11y-text-130',        (p) => p.textSize === 130,      'p.textSize===130'],
  ['a11y-text-150',        (p) => p.textSize === 150,      'p.textSize===150'],
  ['a11y-lines-16',        (p) => p.lineSpacing === '16',  "p.lineSpacing==='16'"],
  ['a11y-lines-20',        (p) => p.lineSpacing === '20',  "p.lineSpacing==='20'"],
  ['a11y-readable-font',   (p) => p.readableFont,          '!!p.readableFont'],
  ['a11y-headings',        (p) => p.headings,              '!!p.headings'],
  ['a11y-cursor-black',    (p) => p.cursorBlack,           '!!p.cursorBlack'],
  ['a11y-cursor-large',    (p) => p.cursorLarge,           '!!p.cursorLarge'],
  ['a11y-reduce-motion',   (p) => p.reduceMotion,          '!!p.reduceMotion'],
];

export function applyPrefsToElement(el: HTMLElement, prefs: A11yPrefs): void {
  for (const [cls, pred] of CLASS_RULES) el.classList.toggle(cls, pred(prefs));
}

// Inline <script> executed in <head> BEFORE React hydrates, so persisted prefs
// are applied synchronously and the user does not see a flash of default styling.
export const A11Y_BOOTSTRAP_SCRIPT: string =
  `(function(){try{var raw=localStorage.getItem(${JSON.stringify(A11Y_STORAGE_KEY)});` +
  `if(!raw)return;var p=JSON.parse(raw);if(p.version!==${A11Y_VERSION})return;` +
  `var c=document.documentElement.classList;` +
  CLASS_RULES.map(([cls, , js]) => `c.toggle(${JSON.stringify(cls)},${js})`).join(';') +
  `}catch(e){}})()`;
```

---

## 2. Pub-Sub Store (`lib/a11y-prefs/store.ts`)

Client-only. Consumed via `useSyncExternalStore` so React can correctly render server, hydration, and client phases.

```ts
'use client';

import { useSyncExternalStore } from 'react';
import {
  A11Y_STORAGE_KEY,
  A11Y_VERSION,
  DEFAULT_PREFS,
  applyPrefsToElement,
  type A11yPrefs,
} from './core';

export * from './core';

function readStorage(): A11yPrefs | null {
  if (typeof window === 'undefined') return null;
  try {
    const raw = localStorage.getItem(A11Y_STORAGE_KEY);
    if (!raw) return null;
    const parsed = JSON.parse(raw) as A11yPrefs;
    if (parsed.version !== A11Y_VERSION) return null;
    return { ...DEFAULT_PREFS, ...parsed, version: A11Y_VERSION };
  } catch {
    return null;
  }
}

const listeners = new Set<() => void>();
let cached: A11yPrefs | undefined;

function notify(next?: A11yPrefs) {
  // Pre-populate the cache so subscribers' getSnapshot() calls don't each
  // trigger a synchronous localStorage re-read during fan-out.
  cached = next ?? readStorage() ?? DEFAULT_PREFS;
  for (const cb of listeners) cb();
}

function writeStorage(prefs: A11yPrefs) {
  try {
    localStorage.setItem(A11Y_STORAGE_KEY, JSON.stringify(prefs));
  } catch {
    // quota / private mode, in-memory state only
  }
}

export const a11yStore = {
  subscribe(cb: () => void) {
    listeners.add(cb);
    return () => { listeners.delete(cb); };
  },
  getSnapshot(): A11yPrefs {
    if (cached === undefined) cached = readStorage() ?? DEFAULT_PREFS;
    return cached;
  },
  getServerSnapshot(): A11yPrefs {
    return DEFAULT_PREFS;
  },
  set(partial: Partial<A11yPrefs>): A11yPrefs {
    const next: A11yPrefs = { ...this.getSnapshot(), ...partial, version: A11Y_VERSION };
    writeStorage(next);
    if (typeof document !== 'undefined') applyPrefsToElement(document.documentElement, next);
    notify(next);
    return next;
  },
  reset(): A11yPrefs {
    try { localStorage.removeItem(A11Y_STORAGE_KEY); } catch {}
    if (typeof document !== 'undefined') applyPrefsToElement(document.documentElement, DEFAULT_PREFS);
    notify(DEFAULT_PREFS);
    return DEFAULT_PREFS;
  },
};

export function useA11yPrefs(): A11yPrefs {
  return useSyncExternalStore(
    a11yStore.subscribe,
    a11yStore.getSnapshot,
    a11yStore.getServerSnapshot,
  );
}
```

---

## 3. Widget Component (`components/accessibility/accessibility-widget.tsx`)

Floating trigger + Radix Sheet panel + 3-column toggle grid + live region + `Alt+A` shortcut.

```tsx
'use client';

import { useCallback, useEffect, useState, type ComponentType } from 'react';
import {
  Accessibility, AlignJustify, CaseSensitive, Contrast, Heading,
  Link2, MousePointer2, MousePointerClick, Pause, RotateCcw, Type,
} from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Sheet, SheetContent, SheetHeader, SheetTitle } from '@/components/ui/sheet';
import { cn } from '@/lib/utils';
import {
  a11yStore, applyPrefsToElement, isAnyActive,
  nextContrast, nextLineSpacing, nextTextSize,
  useA11yPrefs, type A11yPrefs,
} from '@/lib/a11y-prefs/store';

interface Props {
  locale: 'he' | 'en';
  dict: { /* labels, values, etc., see below */ };
}

export function AccessibilityWidget({ locale, dict }: Props) {
  const prefs = useA11yPrefs();
  const [open, setOpen] = useState(false);
  const [announcement, setAnnouncement] = useState('');
  const dir: 'rtl' | 'ltr' = locale === 'he' ? 'rtl' : 'ltr';

  // Safety net: re-apply classes after hydration if the inline FOUC script
  // failed (e.g. localStorage blocked). Don't call a11yStore.set({}), that
  // would write back to storage and notify subscribers on every mount.
  useEffect(() => {
    applyPrefsToElement(document.documentElement, a11yStore.getSnapshot());
  }, []);

  // Alt+A keyboard shortcut. e.code (layout-independent) because macOS
  // produces dead-key 'å' for e.key, which would miss an e.key === 'a' check.
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.altKey && !e.ctrlKey && !e.metaKey && !e.shiftKey && e.code === 'KeyA') {
        e.preventDefault();
        setOpen(prev => !prev);
      }
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, []);

  const toggle = useCallback(
    (feature: keyof A11yPrefs, value: A11yPrefs[keyof A11yPrefs], announce: string) => {
      a11yStore.set({ [feature]: value } as Partial<A11yPrefs>);
      setAnnouncement(`${dict.announceChange}: ${announce}`);
    },
    [dict.announceChange],
  );

  return (
    <>
      {/* Live region OUTSIDE the Sheet portal so announcements aren't lost
          when the portal unmounts. */}
      <div role="status" aria-live="polite" className="sr-only">
        {announcement}
      </div>

      <button
        id="a11y-widget-trigger"
        type="button"
        onClick={() => setOpen(true)}
        aria-label={dict.triggerLabel}
        aria-expanded={open}
        aria-controls="a11y-widget-panel"
        aria-keyshortcuts="Alt+A"
        className={cn(
          'fixed bottom-6 start-6 z-40 flex size-12 items-center justify-center',
          'rounded-full bg-primary text-primary-foreground shadow-lg',
          isAnyActive(prefs) && 'ring-2 ring-white/40',
        )}
      >
        <Accessibility className="size-6" aria-hidden />
      </button>

      <Sheet open={open} onOpenChange={setOpen}>
        <SheetContent
          id="a11y-widget-panel"
          side={dir === 'rtl' ? 'right' : 'left'}
          className="w-3/4 sm:max-w-md"
        >
          <SheetHeader className="border-b">
            <SheetTitle>{dict.title}</SheetTitle>
          </SheetHeader>

          <div className="flex-1 overflow-y-auto p-4">
            <div className="grid grid-cols-3 gap-3">
              {/* Binary toggles: aria-pressed={active} */}
              <ToggleCard icon={Link2} label={dict.labels.links}
                active={prefs.links} onClick={() => toggle('links', !prefs.links, dict.labels.links)} />

              {/* Cycling toggles: OMIT aria-pressed, aria-label carries value */}
              <ToggleCard icon={Contrast} label={dict.labels.contrast}
                active={prefs.contrast !== 'off'}
                valueLabel={prefs.contrast === 'off' ? undefined : dict.values.contrast[prefs.contrast]}
                cycling
                onClick={() => {
                  const next = nextContrast(prefs.contrast);
                  toggle('contrast', next, dict.values.contrast[next]);
                }}
              />
              {/* …text size, line spacing, readable font, headings, cursors, motion */}
            </div>

            <button
              type="button"
              onClick={() => { a11yStore.reset(); setAnnouncement(dict.reset); }}
              className="mt-6 inline-flex items-center gap-1.5 text-sm text-destructive"
            >
              <RotateCcw className="size-4" aria-hidden />
              {dict.reset}
            </button>
          </div>
        </SheetContent>
      </Sheet>
    </>
  );
}

interface ToggleCardProps {
  icon: ComponentType<{ className?: string; 'aria-hidden'?: boolean }>;
  label: string;
  active: boolean;
  valueLabel?: string;
  /** True for cycling controls. When true, aria-pressed is omitted, the
   *  accessible name (aria-label) carries the current value instead. */
  cycling?: boolean;
  onClick: () => void;
}

function ToggleCard({ icon: Icon, label, active, valueLabel, cycling, onClick }: ToggleCardProps) {
  return (
    <Button
      type="button"
      variant="outline"
      onClick={onClick}
      aria-pressed={cycling ? undefined : active}
      aria-label={valueLabel ? `${label}: ${valueLabel}` : label}
      className={cn(
        'flex aspect-square h-auto flex-col items-center justify-center gap-2',
        'whitespace-normal rounded-xl p-3 text-center',
        active && 'ring-1 ring-primary',
      )}
    >
      <Icon className="size-6" aria-hidden />
      <span className="text-xs font-medium">{label}</span>
      {valueLabel && <span className="text-[10px] text-muted-foreground">{valueLabel}</span>}
    </Button>
  );
}
```

---

## 4. framer-motion Reduced-Motion Provider

```tsx
'use client';

import { MotionConfig } from 'framer-motion';
import { useA11yPrefs } from '@/lib/a11y-prefs/store';

export function MotionA11yProvider({ children }: { children: React.ReactNode }) {
  const { reduceMotion } = useA11yPrefs();
  // 'always' → always reduce. 'user' → fall back to prefers-reduced-motion.
  return (
    <MotionConfig reducedMotion={reduceMotion ? 'always' : 'user'}>
      {children}
    </MotionConfig>
  );
}
```

---

## 5. Layout Wiring

### Root layout (Server Component)

Inject the FOUC bootstrap BEFORE React hydrates:

```tsx
// app/layout.tsx
import { A11Y_BOOTSTRAP_SCRIPT } from '@/lib/a11y-prefs/core';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html>
      <head>
        <script dangerouslySetInnerHTML={{ __html: A11Y_BOOTSTRAP_SCRIPT }} />
      </head>
      <body>{children}</body>
    </html>
  );
}
```

### Locale layout

Mount the widget and the framer-motion provider:

```tsx
// app/[locale]/layout.tsx
import { AccessibilityWidget } from '@/components/accessibility/accessibility-widget';
import { MotionA11yProvider } from '@/components/accessibility/motion-a11y-provider';

export default async function LocaleLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: Promise<{ locale: 'he' | 'en' }>;
}) {
  const { locale } = await params;
  const dict = await getDictionary(locale);

  return (
    <MotionA11yProvider>
      {children}
      <AccessibilityWidget locale={locale} dict={dict.accessibility.widget} />
    </MotionA11yProvider>
  );
}
```

---

## 6. CSS Class Reference Table

Each toggle produces one or more CSS classes on `<html>`. Map them in `globals.css` with whatever rules make sense for the site.

| Toggle | Class(es) applied | Suggested CSS rule |
|--------|-------------------|--------------------|
| Highlight links | `.a11y-links` | `.a11y-links a { text-decoration: underline !important; font-weight: 600 !important; outline: 1px solid currentColor !important; outline-offset: 2px !important; }` |
| Contrast high | `.a11y-contrast-high` | `.a11y-contrast-high { filter: contrast(1.3); }` |
| Contrast invert | `.a11y-contrast-invert` | `.a11y-contrast-invert { filter: invert(1) hue-rotate(180deg); }` + counter-invert widget |
| Contrast mono | `.a11y-contrast-mono` | `.a11y-contrast-mono { filter: grayscale(1) contrast(1.1); }` + counter-invert widget |
| Text size | `.a11y-text-115`, `.a11y-text-130`, `.a11y-text-150` | `.a11y-text-150 { font-size: 150%; }` |
| Line spacing | `.a11y-lines-16`, `.a11y-lines-20` | `.a11y-lines-20 { line-height: 2 !important; }` |
| Readable font | `.a11y-readable-font` | `.a11y-readable-font { font-family: system-ui, -apple-system, "Segoe UI", Arial, sans-serif !important; }`, OS stack ONLY, no webfont |
| Highlight headings | `.a11y-headings` | `.a11y-headings h1, .a11y-headings h2, .a11y-headings h3 { outline: 2px dashed currentColor; outline-offset: 4px; }` |
| Black cursor | `.a11y-cursor-black` | `.a11y-cursor-black, .a11y-cursor-black * { cursor: url("data:image/svg+xml,…black cursor SVG…"), auto !important; }` |
| Large cursor | `.a11y-cursor-large` | `.a11y-cursor-large, .a11y-cursor-large * { cursor: url("data:image/svg+xml,…large cursor SVG…"), auto !important; }` |
| Stop animations | `.a11y-reduce-motion` | `.a11y-reduce-motion *, .a11y-reduce-motion *::before, .a11y-reduce-motion *::after { animation-duration: 0.001ms !important; animation-iteration-count: 1 !important; transition-duration: 0.001ms !important; scroll-behavior: auto !important; }` |

### Counter-invert (required)

```css
html.a11y-contrast-invert #a11y-widget-panel,
html.a11y-contrast-invert #a11y-widget-trigger,
html.a11y-contrast-mono #a11y-widget-panel,
html.a11y-contrast-mono #a11y-widget-trigger {
  filter: invert(1) hue-rotate(180deg);
}
```

Without this, users end up with an unreadable widget when invert/mono is active.

### Print reset (required)

```css
@media print {
  html[class*="a11y-"] { filter: none !important; }
  html[class*="a11y-text-"] { font-size: 100% !important; }
  html[class*="a11y-lines-"] { line-height: normal !important; }
  html.a11y-cursor-black, html.a11y-cursor-large { cursor: auto !important; }
}
```

---

## 7. Dictionary Shape

The widget expects this bilingual dictionary shape:

```ts
interface AccessibilityWidgetDict {
  triggerLabel: string;
  title: string;
  close: string;
  reset: string;
  keyboardHint: string;
  announceChange: string;
  footerLink: string;
  labels: {
    links: string;
    contrast: string;
    textSize: string;
    lineSpacing: string;
    readableFont: string;
    headings: string;
    cursorBlack: string;
    cursorLarge: string;
    reduceMotion: string;
  };
  values: {
    contrast: Record<'off' | 'high' | 'invert' | 'mono', string>;
    lineSpacing: Record<'normal' | '16' | '20', string>;
  };
}
```

---

## Testing Checklist

Before shipping:

- [ ] Disable JavaScript → bootstrap script should still apply classes from `localStorage`
- [ ] Clear `localStorage` → widget opens at defaults, no flash
- [ ] Set prefs, reload → no flash of default styling (FOUC test)
- [ ] `Alt+A` on macOS Chrome, Safari, Firefox → panel opens
- [ ] `Alt+A` on Windows / Linux → panel opens
- [ ] Tab through page → widget trigger is reachable by keyboard
- [ ] Enable invert contrast → widget remains readable (counter-invert works)
- [ ] Enable 150% text → no text clipped, no horizontal scroll introduced
- [ ] Print preview → filters removed, text at 100%
- [ ] Enable "Stop animations" → framer-motion animations skip via `MotionConfig`
- [ ] Screen reader (NVDA / VoiceOver) → cycling toggle announces current value, not "pressed"
- [ ] Cross-tab test → preferences persist across tabs (storage event not required; each tab reads from localStorage on load)

## Scope Reminder

This widget must NOT:
- Generate or alter `alt` attributes
- Add, remove, or rewrite ARIA on content elements
- Inject structural DOM changes to fix heading order or landmarks
- Include a "we are compliant" badge or claim
- Load third-party overlay SDKs

The widget is one control surface. Compliance with IS 5568 and WCAG 2.0 AA comes from the site's own HTML, not from the widget. See `SKILL.md` section "Avoiding Overlay Anti-Patterns" and the April 2025 FTC action against accessiBe for why this matters.
