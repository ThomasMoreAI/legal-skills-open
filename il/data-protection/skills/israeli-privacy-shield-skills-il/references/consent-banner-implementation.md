# Consent Banner: Implementation Reference

Copy-pasteable TypeScript/React code for a Privacy Protection Law Amendment 13 + GDPR compliant consent surface.

**Consult this file when** the user wants to ship the consent UI itself, not just audit the law. The main `SKILL.md` covers legal requirements and compliance guidance; this file covers the implementation.

**Scope reminder:** this surface is a consent elicitation tool. It must gate non-essential trackers, persist the user's choice, support withdrawal, and emit audit events. It must NOT pre-check boxes, hide the Reject button, style Accept more prominently than Reject, or condition service on consent (cookie walls).

Stack assumptions: Next.js App Router (13+), React 18+, TypeScript, shadcn/ui Dialog + Switch + Button, Sentry (optional), Vercel Analytics or equivalent (optional).

---

## 1. Core Store (`lib/consent/store.ts`)

No `'use client'` directive (safe to import from `instrumentation-client.ts`). Exports the pub-sub store, types, constants, and the `SSR_SENTINEL`.

```ts
export type ConsentCategory = 'analytics' | 'session_replay' | 'error_monitoring';
export type ConsentChoice = 'accepted' | 'rejected' | 'customized';

export interface ConsentCategories {
  analytics: boolean;
  session_replay: boolean;
  error_monitoring: boolean;
}

export interface ConsentState {
  version: number;
  categories: ConsentCategories;
  timestamp: string;
}

export const CONSENT_VERSION = 1;
export const CONSENT_STORAGE_KEY = 'site_consent_v1';
export const CONSENT_COOKIE_NAME = 'site_consent';
export const CONSENT_REPROMPT_MS = 365 * 24 * 60 * 60 * 1000;

export const ALL_CATEGORIES_OFF: ConsentCategories = {
  analytics: false,
  session_replay: false,
  error_monitoring: false,
};

export const ALL_CATEGORIES_ON: ConsentCategories = {
  analytics: true,
  session_replay: true,
  error_monitoring: true,
};

export const OPTIONAL_CATEGORIES = Object.keys(ALL_CATEGORIES_OFF) as ConsentCategory[];

// Identity-compared by the provider to detect the server/hydration render.
// Frozen so identity stays stable across re-renders.
export const SSR_SENTINEL: ConsentState = Object.freeze({
  version: -1,
  categories: ALL_CATEGORIES_OFF,
  timestamp: '1970-01-01T00:00:00.000Z',
});

export function deriveChoice(categories: ConsentCategories): ConsentChoice {
  const on = OPTIONAL_CATEGORIES.filter((k) => categories[k]).length;
  if (on === OPTIONAL_CATEGORIES.length) return 'accepted';
  if (on === 0) return 'rejected';
  return 'customized';
}

declare global {
  interface Window {
    __consent?: ConsentCategories;
  }
}

const listeners = new Set<() => void>();
let cached: ConsentState | null | undefined;

function readStorage(): ConsentState | null {
  if (typeof window === 'undefined') return null;
  try {
    const raw = localStorage.getItem(CONSENT_STORAGE_KEY);
    if (!raw) return null;
    const parsed = JSON.parse(raw) as ConsentState;
    if (parsed.version !== CONSENT_VERSION) return null;
    const ts = Date.parse(parsed.timestamp);
    if (!Number.isFinite(ts) || Date.now() - ts > CONSENT_REPROMPT_MS) return null;
    return parsed;
  } catch {
    return null;
  }
}

function notify() {
  cached = undefined;
  for (const cb of listeners) cb();
}

function writeCookie(state: ConsentState | null) {
  if (typeof document === 'undefined') return;
  const maxAge = Math.floor(CONSENT_REPROMPT_MS / 1000);
  const secure = location.protocol === 'https:' ? '; Secure' : '';
  if (!state) {
    document.cookie = `${CONSENT_COOKIE_NAME}=; Path=/; Max-Age=0; SameSite=Lax${secure}`;
    return;
  }
  const value = state.categories.analytics ? '1' : '0';
  document.cookie = `${CONSENT_COOKIE_NAME}=${value}; Path=/; Max-Age=${maxAge}; SameSite=Lax${secure}`;
}

function syncWindow(state: ConsentState | null) {
  if (typeof window === 'undefined') return;
  window.__consent = state?.categories ?? ALL_CATEGORIES_OFF;
}

function onStorageEvent(e: StorageEvent) {
  // Fires when another tab changes localStorage; drop our cache + re-notify.
  if (e.key === null || e.key === CONSENT_STORAGE_KEY) notify();
}

export const consentStore = {
  subscribe(cb: () => void) {
    listeners.add(cb);
    if (listeners.size === 1 && typeof window !== 'undefined') {
      window.addEventListener('storage', onStorageEvent);
    }
    return () => {
      listeners.delete(cb);
      if (listeners.size === 0 && typeof window !== 'undefined') {
        window.removeEventListener('storage', onStorageEvent);
      }
    };
  },

  getSnapshot(): ConsentState | null {
    if (cached === undefined) cached = readStorage();
    return cached ?? null;
  },

  getServerSnapshot(): ConsentState {
    return SSR_SENTINEL;
  },

  save(categories: ConsentCategories): ConsentState {
    const state: ConsentState = {
      version: CONSENT_VERSION,
      categories,
      timestamp: new Date().toISOString(),
    };
    try {
      localStorage.setItem(CONSENT_STORAGE_KEY, JSON.stringify(state));
    } catch {
      // storage quota / private mode, in-memory state still applies
    }
    writeCookie(state);
    syncWindow(state);
    notify();
    return state;
  },

  clear() {
    try { localStorage.removeItem(CONSENT_STORAGE_KEY); } catch {}
    writeCookie(null);
    syncWindow(null);
    notify();
  },

  isAllowed(category: ConsentCategory): boolean {
    const state = this.getSnapshot();
    return state?.categories[category] ?? false;
  },
};

// Called from instrumentation-client.ts BEFORE Sentry.init()
export function hydrateWindowFromStorage() {
  if (typeof window === 'undefined') return;
  syncWindow(readStorage());
}
```

---

## 2. Provider (`lib/consent/provider.tsx`)

```tsx
'use client';

import {
  createContext, useCallback, useContext, useEffect, useMemo, useState,
  useSyncExternalStore, type ReactNode,
} from 'react';
import { trackEvent } from '@/lib/analytics/client';
import {
  ALL_CATEGORIES_OFF, ALL_CATEGORIES_ON, CONSENT_VERSION, SSR_SENTINEL,
  consentStore, deriveChoice,
  type ConsentCategories, type ConsentCategory, type ConsentState,
} from './store';

interface ConsentContextValue {
  state: ConsentState | null;
  needsPrompt: boolean;
  promptOpen: boolean;
  prefsOpen: boolean;
  isAllowed(category: ConsentCategory): boolean;
  acceptAll(): void;
  rejectAll(): void;
  customize(categories: ConsentCategories): void;
  /** First-time users see the banner; returning users jump to the toggle dialog. */
  reopen(): void;
  openPreferences(): void;
  closePreferences(): void;
}

const ConsentContext = createContext<ConsentContextValue | null>(null);

export function useConsent(): ConsentContextValue {
  const ctx = useContext(ConsentContext);
  if (!ctx) throw new Error('useConsent must be used within ConsentProvider');
  return ctx;
}

export function ConsentProvider({ children, locale }: { children: ReactNode; locale: string }) {
  const rawState = useSyncExternalStore(
    consentStore.subscribe,
    consentStore.getSnapshot,
    consentStore.getServerSnapshot,
  );

  const [manualOpen, setManualOpen] = useState(false);
  const [prefsOpen, setPrefsOpen] = useState(false);

  // SSR_SENTINEL identity signals the server/hydration render; treat it as
  // "not yet hydrated" so the banner stays out of SSR HTML.
  const isHydrated = rawState !== SSR_SENTINEL;
  const state = isHydrated ? rawState : null;

  // Mirror client snapshot to window.__consent for non-React consumers (Sentry).
  useEffect(() => {
    if (typeof window !== 'undefined') {
      window.__consent = state?.categories ?? undefined;
    }
  }, [state]);

  // Attach Sentry Replay the first time session_replay consent is granted.
  // Dynamic import keeps Replay off the initial bundle when consent is denied.
  useEffect(() => {
    if (state?.categories.session_replay) {
      import('./sentry-gate').then((m) => m.enableSentryReplay());
    }
  }, [state?.categories.session_replay]);

  const save = useCallback(
    (categories: ConsentCategories) => {
      consentStore.save(categories);
      setManualOpen(false);
      setPrefsOpen(false);
      trackEvent(`consent_${deriveChoice(categories)}`, {
        categories, version: CONSENT_VERSION, locale,
      });
    },
    [locale],
  );

  const acceptAll = useCallback(() => save(ALL_CATEGORIES_ON), [save]);
  const rejectAll = useCallback(() => save(ALL_CATEGORIES_OFF), [save]);
  const customize = useCallback((cats: ConsentCategories) => save(cats), [save]);

  const openPreferences = useCallback(() => setPrefsOpen(true), []);
  const closePreferences = useCallback(() => setPrefsOpen(false), []);

  // First-time users (no stored choice) see the banner; returning users jump
  // straight to the toggle dialog since they already understand the choice.
  const reopen = useCallback(() => {
    trackEvent('consent_reopened', { locale });
    if (state === null) setManualOpen(true);
    else setPrefsOpen(true);
  }, [locale, state]);

  const isAllowed = useCallback(
    (category: ConsentCategory): boolean => state?.categories[category] ?? false,
    [state],
  );

  const needsPrompt = isHydrated && state === null;
  const promptOpen = needsPrompt || manualOpen;

  const value = useMemo<ConsentContextValue>(
    () => ({
      state, needsPrompt, promptOpen, prefsOpen,
      isAllowed, acceptAll, rejectAll, customize,
      openPreferences, closePreferences, reopen,
    }),
    [state, needsPrompt, promptOpen, prefsOpen,
     isAllowed, acceptAll, rejectAll, customize,
     openPreferences, closePreferences, reopen],
  );

  return <ConsentContext.Provider value={value}>{children}</ConsentContext.Provider>;
}
```

---

## 3. Banner (`components/consent/cookie-banner.tsx`)

```tsx
'use client';

import { useEffect } from 'react';
import Link from 'next/link';
import { X } from 'lucide-react';
import { useConsent } from '@/lib/consent/provider';
import { Button } from '@/components/ui/button';
import { trackEvent } from '@/lib/analytics/client';

interface Props {
  locale: string;
  dict: { /* see section 7 */ };
}

export function CookieBanner({ locale, dict }: Props) {
  const { promptOpen, needsPrompt, acceptAll, rejectAll, openPreferences } = useConsent();

  // Fire only on first-show (no stored choice). Re-opens are tracked separately.
  useEffect(() => {
    if (needsPrompt) trackEvent('consent_banner_shown', { locale });
  }, [needsPrompt, locale]);

  // ESC mirrors the X button, both reject (dismissing = refusing, per GDPR).
  useEffect(() => {
    if (!promptOpen) return;
    function onKey(e: KeyboardEvent) {
      if (e.key === 'Escape') rejectAll();
    }
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [promptOpen, rejectAll]);

  if (!promptOpen) return null;

  return (
    <div
      role="dialog"
      aria-modal="false"
      aria-labelledby="consent-banner-title"
      aria-describedby="consent-banner-body"
      className="fixed inset-x-0 bottom-0 z-[60] px-4 pb-4 sm:inset-x-auto sm:end-4 sm:max-w-md"
    >
      <div className="relative rounded-xl border bg-background/95 p-5 shadow-xl backdrop-blur">
        <button
          type="button"
          onClick={rejectAll}
          className="absolute end-3 top-3 rounded-full p-1 text-muted-foreground hover:bg-foreground/10"
          aria-label={dict.close}
        >
          <X className="size-4" />
        </button>
        <h2 id="consent-banner-title" className="pe-6 text-base font-semibold">{dict.title}</h2>
        <p id="consent-banner-body" className="mt-2 text-sm text-muted-foreground">{dict.body}</p>
        <p className="mt-2 text-xs text-muted-foreground">
          <Link href={`/${locale}/privacy`} className="underline">
            {dict.policyLink}
          </Link>
        </p>
        {/* GDPR requires equal visual weight for Reject and Accept. */}
        <div className="mt-4 grid grid-cols-3 gap-2">
          <Button size="sm" variant="outline" onClick={rejectAll}>{dict.rejectAll}</Button>
          <Button size="sm" variant="outline" onClick={openPreferences}>{dict.customize}</Button>
          <Button size="sm" onClick={acceptAll}>{dict.acceptAll}</Button>
        </div>
        <p className="mt-3 text-xs text-muted-foreground">{dict.manageLater}</p>
      </div>
    </div>
  );
}
```

---

## 4. Preferences Dialog (`components/consent/preferences-dialog.tsx`)

```tsx
'use client';

import { useState } from 'react';
import { Lock } from 'lucide-react';
import {
  Dialog, DialogContent, DialogDescription, DialogFooter,
  DialogHeader, DialogTitle,
} from '@/components/ui/dialog';
import { Button } from '@/components/ui/button';
import { Switch } from '@/components/ui/switch';
import { useConsent } from '@/lib/consent/provider';
import {
  ALL_CATEGORIES_OFF, OPTIONAL_CATEGORIES, type ConsentCategories,
} from '@/lib/consent/store';

export function PreferencesDialog({ dict }: { dict: any }) {
  const { prefsOpen, closePreferences } = useConsent();
  return (
    <Dialog open={prefsOpen} onOpenChange={(o) => (o ? null : closePreferences())}>
      {/* DialogContent unmounts on close, so draft resets naturally on reopen. */}
      {prefsOpen && <PreferencesContent dict={dict} />}
    </Dialog>
  );
}

function PreferencesContent({ dict }: { dict: any }) {
  const { state, customize, acceptAll, rejectAll, closePreferences } = useConsent();
  const [draft, setDraft] = useState<ConsentCategories>(
    () => state?.categories ?? ALL_CATEGORIES_OFF,
  );

  const allOn = OPTIONAL_CATEGORIES.every((k) => draft[k]);
  const allOff = OPTIONAL_CATEGORIES.every((k) => !draft[k]);

  return (
    <DialogContent className="max-w-lg">
      <DialogHeader>
        <DialogTitle>{dict.categoriesHeading}</DialogTitle>
        <DialogDescription>{dict.body}</DialogDescription>
      </DialogHeader>
      <div className="space-y-4">
        {/* Essential: always on, disabled switch + lock icon. */}
        <div className="flex items-start justify-between gap-4 rounded-lg border bg-muted/40 p-4">
          <div className="flex-1">
            <div className="flex items-center gap-2">
              <span className="font-semibold">{dict.categories.essential.title}</span>
              <Lock className="size-3.5 text-muted-foreground" aria-hidden />
            </div>
            <p className="mt-1 text-sm text-muted-foreground">
              {dict.categories.essential.description}
            </p>
          </div>
          <Switch checked disabled aria-label={dict.categories.essential.title} />
        </div>
        {OPTIONAL_CATEGORIES.map((key) => {
          const cat = dict.categories[key];
          return (
            <div key={key} className="flex items-start justify-between gap-4 rounded-lg border p-4">
              <div className="flex-1">
                <span className="font-semibold">{cat.title}</span>
                <p className="mt-1 text-sm text-muted-foreground">{cat.description}</p>
              </div>
              <Switch
                checked={draft[key]}
                onCheckedChange={(checked) => setDraft((prev) => ({ ...prev, [key]: checked }))}
                aria-label={cat.title}
              />
            </div>
          );
        })}
      </div>
      <DialogFooter className="flex flex-col gap-2 sm:flex-row sm:justify-between">
        <div className="flex flex-wrap gap-2">
          <Button variant="outline" size="sm" onClick={rejectAll} disabled={allOff}>
            {dict.rejectAll}
          </Button>
          <Button variant="outline" size="sm" onClick={acceptAll} disabled={allOn}>
            {dict.acceptAll}
          </Button>
        </div>
        <div className="flex flex-wrap gap-2">
          <Button variant="ghost" size="sm" onClick={closePreferences}>{dict.close}</Button>
          <Button size="sm" onClick={() => customize(draft)}>{dict.savePreferences}</Button>
        </div>
      </DialogFooter>
    </DialogContent>
  );
}
```

---

## 5. Tracker Gate (`components/consent/consent-gated-trackers.tsx`)

```tsx
'use client';

import Script from 'next/script';
import { Analytics } from '@vercel/analytics/next';
import { SpeedInsights } from '@vercel/speed-insights/next';
import { useConsent } from '@/lib/consent/provider';

const CLARITY_ID = process.env.NEXT_PUBLIC_CLARITY_ID?.trim();

// Clarity enforces its own consent signal in EEA/UK/CH. Since we only load the
// script after session_replay consent is granted, signal full consent so
// Clarity does not stay in restricted-preview mode.
const CLARITY_SNIPPET = CLARITY_ID
  ? `(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};` +
    `t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;` +
    `y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);})` +
    `(window,document,"clarity","script","${CLARITY_ID}");` +
    `window.clarity("consent",true);`
  : '';

export function ConsentGatedTrackers() {
  const { isAllowed } = useConsent();
  const analyticsOk = isAllowed('analytics');
  const sessionReplayOk = isAllowed('session_replay');

  return (
    <>
      {analyticsOk && <Analytics />}
      {analyticsOk && <SpeedInsights />}
      {sessionReplayOk && CLARITY_SNIPPET && (
        <Script
          id="clarity-script"
          strategy="afterInteractive"
          dangerouslySetInnerHTML={{ __html: CLARITY_SNIPPET }}
        />
      )}
    </>
  );
}
```

---

## 6. Sentry Gate (`lib/consent/sentry-gate.ts` + `instrumentation-client.ts`)

**`lib/consent/sentry-gate.ts`**, mid-session attach, kept separate so React components don't re-run `Sentry.init`:

```ts
'use client';

import * as Sentry from '@sentry/nextjs';

export function enableSentryReplay() {
  if (typeof window === 'undefined') return;
  const client = Sentry.getClient();
  if (!client) return;
  if (client.getIntegrationByName?.('Replay')) return;
  Sentry.addIntegration(Sentry.replayIntegration());
}
```

**`instrumentation-client.ts`**, hydrate BEFORE `Sentry.init`:

```ts
import * as Sentry from '@sentry/nextjs';
import { hydrateWindowFromStorage } from '@/lib/consent/store';

// CRITICAL: runs before Sentry.init so early hydration errors respect consent.
hydrateWindowFromStorage();

Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  // Replay only loaded when consent was granted in a previous session.
  // Mid-session grants attach via sentry-gate.ts.
  replaysSessionSampleRate: window.__consent?.session_replay ? 0.1 : 0,
  replaysOnErrorSampleRate: window.__consent?.session_replay ? 1.0 : 0,
  integrations: window.__consent?.session_replay ? [Sentry.replayIntegration()] : [],
  beforeSend(event) {
    return window.__consent?.error_monitoring ? event : null;
  },
});
```

---

## 7. Dictionary Shape

```ts
interface ConsentDict {
  title: string;
  body: string;
  acceptAll: string;
  rejectAll: string;
  customize: string;
  close: string;
  savePreferences: string;
  policyLink: string;
  manageLater: string;
  categoriesHeading: string;
  categories: {
    essential: { title: string; description: string };
    analytics: { title: string; description: string };
    session_replay: { title: string; description: string };
    error_monitoring: { title: string; description: string };
  };
}
```

Hebrew copy must be natural Israeli Hebrew (plural imperative, avoid literal EN translations). Keep technical terms (analytics, session replay, Sentry) in English in Hebrew copy where they are proper nouns.

---

## 8. Layout Wiring

```tsx
// app/[locale]/layout.tsx
import { ConsentProvider } from '@/lib/consent/provider';
import { CookieBanner } from '@/components/consent/cookie-banner';
import { PreferencesDialog } from '@/components/consent/preferences-dialog';
import { ConsentGatedTrackers } from '@/components/consent/consent-gated-trackers';

export default async function LocaleLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  const dict = await getDictionary(locale);

  return (
    <ConsentProvider locale={locale}>
      {children}
      <ConsentGatedTrackers />
      <CookieBanner locale={locale} dict={dict.consent} />
      <PreferencesDialog dict={dict.consent} />
    </ConsentProvider>
  );
}
```

---

## 9. Footer "Manage Consent" Link

```tsx
'use client';
import { useConsent } from '@/lib/consent/provider';

export function ManageConsentLink({ label, className }: { label: string; className?: string }) {
  const { reopen } = useConsent();
  return (
    <button type="button" onClick={reopen} className={className}>
      {label}
    </button>
  );
}
```

Place under "Privacy" in the footer. `reopen()` branches: first-time users (no stored state) see the banner; returning users jump straight to the preferences dialog.

---

## 10. Server Component Gating (`lib/consent/server.ts`)

```ts
import { cookies } from 'next/headers';
import { CONSENT_COOKIE_NAME } from './store';

export async function isAnalyticsAllowedServerSide(): Promise<boolean> {
  try {
    const store = await cookies();
    return store.get(CONSENT_COOKIE_NAME)?.value === '1';
  } catch {
    return false;
  }
}
```

Use it inside `after()`:

```tsx
import { after } from 'next/server';
import { isAnalyticsAllowedServerSide } from '@/lib/consent/server';

export default async function BundlePage({ params }) {
  const { slug } = await params;
  if (await isAnalyticsAllowedServerSide()) {
    after(() => incrementBundleViews(slug));
  }
  // ...render
}
```

---

## 11. Essential-Event Allowlist

```ts
// lib/analytics/client.ts
export const CONSENT_EVENT_TYPES = [
  'consent_banner_shown',
  'consent_accepted',
  'consent_rejected',
  'consent_customized',
  'consent_reopened',
] as const;

const ESSENTIAL_EVENTS = new Set<string>([
  ...CONSENT_EVENT_TYPES,
  'auth_sign_in',   // legally transactional
]);

export function trackEvent(event: string, data?: Record<string, unknown>) {
  if (!ESSENTIAL_EVENTS.has(event) && !window.__consent?.analytics) return;
  // ...send to analytics backend
}
```

Do NOT add marketing / retargeting events to `ESSENTIAL_EVENTS`. The allowlist is for legally transactional events only, the consent choice itself and auth, because without those events you can't prove consent or prove the user authenticated.

---

## Testing Checklist

Before shipping:

- [ ] SSR HTML does NOT contain the banner. `curl https://yoursite/en | grep consent-banner-title` should return nothing.
- [ ] First visit: banner appears, trackers (Analytics, Clarity, Sentry Replay) not loaded.
- [ ] Reject all: banner dismisses, no tracker scripts load, `localStorage[site_consent_v1]` has `categories` all `false`, cookie value is `0`.
- [ ] Accept all: banner dismisses, trackers load, cookie value is `1`.
- [ ] ESC key on banner: acts as Reject all.
- [ ] X button: acts as Reject all.
- [ ] Customize → toggle analytics only → Save: cookie value is `1`, session_replay script not loaded.
- [ ] Open two tabs, accept in one: the other re-renders to hide the banner within one tick.
- [ ] Footer "Privacy preferences" link: first-time opens banner, returning opens preferences dialog.
- [ ] Set `CONSENT_VERSION = 2` in code, reload: banner re-appears even though a choice was stored.
- [ ] Advance system clock 13 months, reload: banner re-appears (TTL expiry).
- [ ] Error thrown during hydration with error_monitoring rejected: NOT sent to Sentry.
- [ ] Error thrown after consent granted mid-session: Sentry picks it up AND Replay starts attaching.
- [ ] Print preview: banner does not appear on paper.
- [ ] No pre-checked boxes in preferences dialog on a fresh visit.
- [ ] Reject + Accept have identical button width, padding, and visual prominence.

## Scope Reminder

This surface MUST:
- Default every optional category to `false`
- Treat ESC and X as Reject all (dismissal-as-refusal)
- Give Reject and Accept equal visual weight
- Re-prompt when `CONSENT_VERSION` bumps or after 12 months
- Emit an audit event for every choice
- Stop trackers from loading when the relevant category is `false`

This surface MUST NOT:
- Pre-check any optional category
- Hide Reject behind Customize
- Condition service on accepting non-essential categories (no cookie walls)
- Re-prompt every session
- Load tracker SDKs and then pass `consent=denied` to them (gate the `<script>` itself)
- Treat scrolling, closing, or inactivity as consent

The consent surface is one layer. Privacy policy, DPO appointment, data subject request process, breach response plan, and (for public bodies + data brokers) database registration all have to exist independently. See `SKILL.md` and `references/privacy-law-requirements.md` for the law side.

## Engineering detail moved from SKILL.md

### Persistence

Store the state in **both** `localStorage` and a companion cookie. `localStorage` is the source of truth for the client; the cookie exists so Server Components can gate SSR work (e.g. `incrementBundleViews` inside `after()`) without a client round-trip. The cookie only needs a single bit (`0` or `1`) because Server Components rarely distinguish individual categories.

```ts
// lib/consent/store.ts
export const CONSENT_VERSION = 1;
export const CONSENT_STORAGE_KEY = 'site_consent_v1';
export const CONSENT_COOKIE_NAME = 'site_consent';
export const CONSENT_REPROMPT_MS = 365 * 24 * 60 * 60 * 1000;

function writeCookie(state: ConsentState | null) {
  const maxAge = Math.floor(CONSENT_REPROMPT_MS / 1000);
  const secure = location.protocol === 'https:' ? '; Secure' : '';
  if (!state) {
    document.cookie = `${CONSENT_COOKIE_NAME}=; Path=/; Max-Age=0; SameSite=Lax${secure}`;
    return;
  }
  const value = state.categories.analytics ? '1' : '0';
  document.cookie = `${CONSENT_COOKIE_NAME}=${value}; Path=/; Max-Age=${maxAge}; SameSite=Lax${secure}`;
}
```

**Re-prompt rules.** `readStorage()` returns `null` if the stored `version` mismatches `CONSENT_VERSION` or the timestamp is older than 12 months. Bumping `CONSENT_VERSION` when adding a new tracker category forces a fresh prompt, this is how you stay compliant when you add a new analytics vendor.


### SSR Safety: The SSR_SENTINEL Pattern

Naive `useSyncExternalStore` with a `null` server snapshot renders the banner in the initial SSR HTML, which means a) the banner is visible for a moment before hydration replaces it, and b) search engines index pages with the consent dialog overlaying the content. The fix is a sentinel object that is identity-compared to distinguish the server/hydration render from "user hasn't decided yet":

```ts
export const SSR_SENTINEL: ConsentState = Object.freeze({
  version: -1,
  categories: ALL_CATEGORIES_OFF,
  timestamp: '1970-01-01T00:00:00.000Z',
});

// In the provider:
const rawState = useSyncExternalStore(
  consentStore.subscribe,
  consentStore.getSnapshot,
  consentStore.getServerSnapshot,  // returns SSR_SENTINEL
);
const isHydrated = rawState !== SSR_SENTINEL;
const state = isHydrated ? rawState : null;

const needsPrompt = isHydrated && state === null;
```

Only when `isHydrated` is true AND `state` is `null` does the banner render. The sentinel is identity-compared with `!==`, which is why it is frozen and exported as a module constant.


### Sentry Integration: Two Pieces

Sentry is unusual because `Sentry.init()` runs in `instrumentation-client.ts` **before** React hydrates, which is before `useConsent()` can tell you what the user wants. Two pieces:

**1. Hydrate `window.__consent` from storage BEFORE `Sentry.init()`.** Without this, any errors thrown during early hydration are captured even if the user previously rejected consent.

```ts
// instrumentation-client.ts
import { hydrateWindowFromStorage } from '@/lib/consent/store';

hydrateWindowFromStorage();  // sets window.__consent from localStorage

Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  integrations: window.__consent?.session_replay ? [Sentry.replayIntegration()] : [],
  beforeSend(event) {
    return window.__consent?.error_monitoring ? event : null;
  },
});
```

**2. Attach Replay mid-session when the user later grants consent.** Don't re-run `Sentry.init()`, that breaks the existing client. Use `Sentry.addIntegration()`:

```ts
// lib/consent/sentry-gate.ts
import * as Sentry from '@sentry/nextjs';

export function enableSentryReplay() {
  const client = Sentry.getClient();
  if (!client) return;
  if (client.getIntegrationByName?.('Replay')) return;  // idempotent
  Sentry.addIntegration(Sentry.replayIntegration());
}
```

The React provider calls `enableSentryReplay()` the first time `state.categories.session_replay` flips to true. Dynamic-import it so the Replay bundle is not shipped to users who rejected it:

```ts
useEffect(() => {
  if (state?.categories.session_replay) {
    import('./sentry-gate').then((m) => m.enableSentryReplay());
  }
}, [state?.categories.session_replay]);
```

## Hebrew engineering detail moved from SKILL_HE.md

### בטיחות SSR: דפוס ה-SSR_SENTINEL

שימוש נאיבי ב-`useSyncExternalStore` עם server snapshot של `null` מרנדר את הבאנר ב-HTML של SSR, כלומר (א) הבאנר גלוי לרגע לפני שההידרציה מחליפה אותו, ו(ב) מנועי חיפוש מאנדקסים דפים עם דיאלוג ההסכמה מכסה את התוכן. הפתרון הוא אובייקט sentinel שנבדק בזהות כדי להפריד בין רינדור השרת / ההידרציה לבין "המשתמש עדיין לא החליט":

```ts
export const SSR_SENTINEL: ConsentState = Object.freeze({
  version: -1,
  categories: ALL_CATEGORIES_OFF,
  timestamp: '1970-01-01T00:00:00.000Z',
});

// בתוך ה-provider:
const rawState = useSyncExternalStore(
  consentStore.subscribe,
  consentStore.getSnapshot,
  consentStore.getServerSnapshot,  // מחזיר SSR_SENTINEL
);
const isHydrated = rawState !== SSR_SENTINEL;
const state = isHydrated ? rawState : null;

const needsPrompt = isHydrated && state === null;
```

רק כש-`isHydrated` הוא true וגם `state` הוא `null`, הבאנר מורנדר. ה-sentinel נבדק בזהות עם `!==`, ולכן הוא מוקפא ומיוצא כקבוע של מודול.


### אינטגרציה עם Sentry: שני חלקים

Sentry חריג כי `Sentry.init()` רץ ב-`instrumentation-client.ts` **לפני** ש-React נהידרר, שזה לפני ש-`useConsent()` יכול להגיד לכם מה המשתמש רוצה. שני חלקים:

**1. הידרוט של `window.__consent` מהאחסון לפני `Sentry.init()`.** בלי זה, כל שגיאה שנזרקת במהלך ההידרציה המוקדמת נתפסת גם אם המשתמש דחה הסכמה קודם.

```ts
// instrumentation-client.ts
import { hydrateWindowFromStorage } from '@/lib/consent/store';

hydrateWindowFromStorage();  // קובע את window.__consent מ-localStorage

Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  integrations: window.__consent?.session_replay ? [Sentry.replayIntegration()] : [],
  beforeSend(event) {
    return window.__consent?.error_monitoring ? event : null;
  },
});
```

**2. לחבר את Replay באמצע הסשן כשהמשתמש מאשר אחר כך.** אל תריצו `Sentry.init()` שוב, זה שובר את הלקוח הקיים. תשתמשו ב-`Sentry.addIntegration()`:

```ts
// lib/consent/sentry-gate.ts
import * as Sentry from '@sentry/nextjs';

export function enableSentryReplay() {
  const client = Sentry.getClient();
  if (!client) return;
  if (client.getIntegrationByName?.('Replay')) return;  // idempotent
  Sentry.addIntegration(Sentry.replayIntegration());
}
```

ה-provider של React קורא ל-`enableSentryReplay()` בפעם הראשונה ש-`state.categories.session_replay` הופך ל-true. תטענו אותו בצורה דינמית כדי ש-bundle של Replay לא ישלח למשתמשים שדחו:

```ts
useEffect(() => {
  if (state?.categories.session_replay) {
    import('./sentry-gate').then((m) => m.enableSentryReplay());
  }
}, [state?.categories.session_replay]);
```


### שמירה

תשמרו את המצב **גם** ב-`localStorage` **וגם** בעוגייה נלווית. `localStorage` הוא מקור האמת ללקוח; העוגייה קיימת כדי ש-Server Components יוכלו לחסום עבודת SSR (למשל `incrementBundleViews` בתוך `after()`) בלי round-trip ללקוח. העוגייה צריכה רק ביט יחיד (`0` או `1`) כי Server Components בדרך כלל לא מבדילים בין קטגוריות בודדות.

```ts
// lib/consent/store.ts
export const CONSENT_VERSION = 1;
export const CONSENT_STORAGE_KEY = 'site_consent_v1';
export const CONSENT_COOKIE_NAME = 'site_consent';
export const CONSENT_REPROMPT_MS = 365 * 24 * 60 * 60 * 1000;

function writeCookie(state: ConsentState | null) {
  const maxAge = Math.floor(CONSENT_REPROMPT_MS / 1000);
  const secure = location.protocol === 'https:' ? '; Secure' : '';
  if (!state) {
    document.cookie = `${CONSENT_COOKIE_NAME}=; Path=/; Max-Age=0; SameSite=Lax${secure}`;
    return;
  }
  const value = state.categories.analytics ? '1' : '0';
  document.cookie = `${CONSENT_COOKIE_NAME}=${value}; Path=/; Max-Age=${maxAge}; SameSite=Lax${secure}`;
}
```

**כללי שאילתה חוזרת.** `readStorage()` מחזיר `null` אם ה-`version` השמור לא תואם ל-`CONSENT_VERSION` או אם ה-timestamp ישן מ-12 חודשים. העלאת `CONSENT_VERSION` כשמוסיפים קטגוריית מעקב חדשה מאלצת שאילתה טריה, ככה נשארים תואמים כשמוסיפים ספק ניתוח חדש.

