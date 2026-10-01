# Framework integration

Authoritative basis: Next.js documentation for `next/script` and `@next/third-parties`; Nuxt Scripts documentation for `useScriptTriggerConsent`; SvelteKit documentation for `csp` config and the `handle` hook. Status as at 2026-08-05. Verify against the installed version — these APIs move.

## The SSR trap

On the server, consent state is unknown unless it arrives in the request. That produces three failure modes, in ascending order of how long they take to find:

1. **Rendering the banner into the HTML for a user who already decided.** Cosmetic flicker, annoying, harmless.
2. **Rendering the tag into the HTML because a build-time flag said analytics is on.** The tag is in the served markup and fires before any client code runs. This is the failure the whole skill exists to prevent.
3. **A CDN caching a page rendered for a consenting user and serving it to everyone.** The gate is bypassed for every subsequent visitor and the network trace looks clean in the developer's own browser, because their consent is stored.

Rules:

- **Never let server-rendered output contain an unblocked third-party tag.** The tag is injected client-side, always, or shipped as `type="text/plain"` for the unblocker.
- **Read state from the request or not at all.** A cookie is readable server-side; `localStorage` is not. If you need server-side awareness, put the decision in a first-party cookie as well as in `localStorage`.
- **Vary or do not cache.** If any part of the HTML depends on consent, either add `Vary` on the consent cookie or move that part to the client.
- **Render the banner client-side after hydration**, or render it server-side only when the request carries no consent cookie.

## Next.js App Router

`next/script` strategies, from the documentation:

| Strategy | Behaviour | Use for consent work |
|---|---|---|
| `beforeInteractive` | Injected into the initial HTML from the server, downloaded before any Next.js module, executed in order before hydration; must be placed in the root layout; always injected into `<head>` | The consent manager itself and the Consent Mode `default` call — the documentation names cookie consent managers as an intended case |
| `afterInteractive` | Default; loads client-side after some hydration | Tags that are already gated by your own logic |
| `lazyOnload` | Loads during browser idle time after page load | Low-priority gated widgets |
| `worker` | Partytown web worker; **not supported in the app directory** | Not usable here |

`onLoad`, `onReady` and `onError` do not work in Server Components. Any component using them must carry `'use client'`.

Correct ordering in `app/layout.tsx`:

```tsx
import Script from 'next/script';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="[[LOCALE]]">
      <head>
        {/* 1. Consent Mode defaults — inline, executes first */}
        <Script id="consent-default" strategy="beforeInteractive">{`
          window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}
          gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',
            ad_personalization:'denied',analytics_storage:'denied',
            functionality_storage:'denied',personalization_storage:'denied',
            security_storage:'granted',wait_for_update:500});
        `}</Script>
      </head>
      <body>
        {children}
        {/* 2. Banner is a client component; it injects tags itself after the choice */}
        <ConsentBanner />
      </body>
    </html>
  );
}
```

**`@next/third-parties` is not a gate.** `<GoogleTagManager gtmId="GTM-XYZ" />` in the root layout loads the container unconditionally. Render it conditionally from a client component that has already read the stored consent:

```tsx
'use client';
import { GoogleTagManager } from '@next/third-parties/google';
import { useConsent } from '@/lib/consent';

export function Analytics() {
  const consent = useConsent();           // null until read from storage on the client
  if (!consent?.categories.analytics) return null;
  return <GoogleTagManager gtmId="[[GTM_ID]]" />;
}
```

`sendGTMEvent` and `sendGAEvent` queue into `dataLayer`; calling them before the container loads is harmless, but do not treat a queued event as evidence the gate held.

Streaming adds one wrinkle: a Suspense boundary that resolves later can inject markup after the banner rendered. Gate inside the streamed component too, not only at the top.

## Nuxt

Nuxt Scripts has a first-class consent trigger. Verified API:

```vue
<script setup lang="ts">
const trigger = useScriptTriggerConsent()

useScriptGoogleTagManager({
  id: '[[GTM_ID]]',
  scriptOptions: { trigger }
})
</script>
```

`trigger.accept()` loads the script, `trigger.revoke()` signals it to unload, `trigger.consented` is a `Ref<boolean>`. It also accepts an external reactive source, which is how you bind a third-party CMP:

```vue
<script setup lang="ts">
const hasAnalyticsConsent = ref(false)

useScriptGoogleAnalytics({
  id: '[[GA_ID]]',
  scriptOptions: { trigger: useScriptTriggerConsent({ consent: hasAnalyticsConsent }) }
})
</script>
```

Share one trigger across the app rather than creating one per component, so a single decision drives every script:

```ts
// composables/consent.ts
export const scriptsConsent = useScriptTriggerConsent()
```

## SvelteKit

No script abstraction is needed; the pieces are the `handle` hook, `csp` config and client-side injection.

```js
// src/hooks.server.js — read GPC and the consent cookie before rendering
export async function handle({ event, resolve }) {
  event.locals.gpc = event.request.headers.get('sec-gpc') === '1';
  event.locals.consent = event.cookies.get('consent') ?? null;
  return resolve(event);
}
```

```js
// svelte.config.js — CSP as the backstop
export default {
  kit: {
    csp: {
      mode: 'auto',                       // hashes for prerendered, nonces for dynamic
      directives: {
        'script-src': ['self'],
        'connect-src': ['self'],
        'frame-src': ['none'],
        'font-src': ['self']
      },
      reportOnly: {
        'script-src': ['self'],
        'report-uri': ['/csp-report']
      }
    }
  }
};
```

Tags are injected from `onMount` in a layout component, behind the consent store. Never place a third-party `<script>` in `src/app.html`.

## Plain static sites

The simplest case and the one most often got wrong, because the tag sits in a shared header include.

1. Convert every third-party tag in the template to `type="text/plain"` with `data-src` and `data-consent-category` (`blocking-layer.md`).
2. Ship one first-party `consent.js`: store, banner, unblocker.
3. Put the Consent Mode `default` call inline in `<head>`, above everything.
4. Remove `preconnect`/`dns-prefetch` for third parties from the template.
5. Verify with `audit.md` — static sites are the easiest to assert against because there is no hydration timing.

CMS-hosted platforms (WordPress plugins, Shopify apps) inject tags outside your template. Assume nothing from the plugin's settings screen; the network trace is the only evidence.

## Checkpoints

- [ ] No server-rendered HTML contains an unblocked third-party tag
- [ ] Consent readable server-side only via a first-party cookie, never assumed
- [ ] CDN caching keyed or bypassed for consent-dependent HTML
- [ ] Next.js: consent defaults in `beforeInteractive` in the root layout
- [ ] Next.js: `@next/third-parties` components rendered conditionally from a client component
- [ ] Next.js: `onLoad`/`onReady` only in `'use client'` components
- [ ] Streamed/Suspense boundaries gated independently
- [ ] Nuxt: one shared `useScriptTriggerConsent` trigger drives all scripts
- [ ] SvelteKit: `handle` hook reads `sec-gpc` and the consent cookie; CSP configured
- [ ] Static: template includes converted; resource hints removed
- [ ] Platform plugins verified against a network trace, not their settings UI
