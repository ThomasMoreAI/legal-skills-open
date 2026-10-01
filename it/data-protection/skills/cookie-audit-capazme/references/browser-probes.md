# Browser probes — frammenti JavaScript

Da incollare nel tool «evaluate script in page» del browser MCP (chrome-devtools: `evaluate_script({function: ...})`; claude-in-chrome: `javascript_tool`). Ogni frammento è una funzione/espressione che ritorna JSON serializzabile.

---

## §1 — Probe pre-consenso (e riusabile post-consenso)
Legge cookie, storage e globali dei tracker. Eseguila in Fase 1 (prima di toccare il banner) e di nuovo in Fase 3.

```js
() => {
  const parse = s => (s||'').split(';').map(c=>c.trim()).filter(Boolean).map(c=>{
    const i=c.indexOf('='); return {name:i>=0?c.slice(0,i):c, value:i>=0?c.slice(i+1).slice(0,80):''};
  });
  const out = { url: location.href, title: document.title };
  out.cookies = parse(document.cookie);
  out.cookieCount = out.cookies.length;
  out.localStorage = {}; try { for (let i=0;i<localStorage.length;i++){const k=localStorage.key(i);out.localStorage[k]=(localStorage.getItem(k)||'').slice(0,160);} } catch(e){}
  out.sessionStorage = {}; try { for (let i=0;i<sessionStorage.length;i++){const k=sessionStorage.key(i);out.sessionStorage[k]=(sessionStorage.getItem(k)||'').slice(0,160);} } catch(e){}
  out.trackerGlobals = {
    gtag:typeof window.gtag, ga:typeof window.ga, fbq:typeof window.fbq,
    _linkedin:typeof window._linkedin_data_partner_ids, lintrk:typeof window.lintrk,
    hj:typeof window.hj, clarity:typeof window.clarity, _hsq:typeof window._hsq,
    Cookiebot:typeof window.Cookiebot, OneTrust:typeof window.OneTrust,
    _iub:typeof window._iub, cmplz:typeof window.cmplz, Usercentrics:typeof window.UC_UI
  };
  out.dataLayer = (window.dataLayer||[]).map(x=>{try{return JSON.stringify(x).slice(0,200);}catch(e){return String(x).slice(0,120);}});
  return out;
}
```

Poi lista le **richieste di rete** (chrome-devtools `list_network_requests`) e individua i domini di terze parti (tutto ciò che non è il dominio del sito): `googletagmanager.com`, `google-analytics.com`, `*.g.doubleclick.net`, `connect.facebook.net`, `*.linkedin.com`, `static.hotjar.com`, `*.clarity.ms`, `*.hs-scripts.com`, ecc.

## §2 — Struttura del banner (funziona anche se l'ad-blocker lo nasconde)
Legge i pulsanti e le categorie dal DOM, con gli stili calcolati per valutare la **parità Accetta/Rifiuta**.

```js
() => {
  const sel = '.cmplz-cookiebanner, #CybotCookiebotDialog, #onetrust-banner-sdk, #iubenda-cs-banner, [id*="usercentrics"], [class*="cookie"][class*="banner"], [id*="cookie"][id*="consent"]';
  const banner = document.querySelector(sel);
  const out = { bannerFound: !!banner };
  if (!banner) return out;
  const cs = getComputedStyle(banner);
  out.visibility = { display: cs.display, visibility: cs.visibility, opacity: cs.opacity };
  const btns = banner.querySelectorAll('button, a[role="button"], .cmplz-btn, [class*="accept"], [class*="deny"], [class*="reject"]');
  out.buttons = Array.from(btns).slice(0,20).map(b=>{const s=getComputedStyle(b);return{
    text:(b.innerText||b.textContent||'').trim().slice(0,50), cls:b.className.toString().slice(0,60),
    bg:s.backgroundColor, color:s.color, fontSize:s.fontSize, border:s.borderStyle
  };});
  out.categories = Array.from(document.querySelectorAll('[class*="categor"], input[type="checkbox"][name*="consent"], input[type="checkbox"][class*="cmplz"]'))
    .map(c=>(c.getAttribute('data-category')||c.name||c.value||c.className||'').toString().slice(0,50)).filter(Boolean).slice(0,15);
  out.policyLinks = Array.from(banner.querySelectorAll('a[href]')).map(a=>({t:(a.innerText||'').trim().slice(0,40),href:a.href})).slice(0,10);
  return out;
}
```

## §3 — Concessione del consenso (per CMP)
Prima identifica la CMP (§ fingerprints), poi usa il frammento giusto. In caso di dubbio, prova tutti — quelli non applicabili sono no-op.

```js
() => {
  const done = [];
  // Complianz
  try { if (typeof window.cmplz_set_consent==='function'){cmplz_set_consent('allow');done.push('complianz');} } catch(e){}
  // Cookiebot
  try { if (window.Cookiebot && Cookiebot.submitCustomConsent){Cookiebot.submitCustomConsent(true,true,true);done.push('cookiebot');} } catch(e){}
  try { if (window.Cookiebot && Cookiebot.dialog && document.getElementById('CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')){document.getElementById('CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click();done.push('cookiebot-click');} } catch(e){}
  // OneTrust
  try { if (window.OneTrust && OneTrust.AllowAll){OneTrust.AllowAll();done.push('onetrust');} } catch(e){}
  // iubenda
  try { if (window._iub && _iub.cs && _iub.cs.api && _iub.cs.api.consent){_iub.cs.api.consent();done.push('iubenda');} } catch(e){}
  // fallback generico: click su qualsiasi pulsante "accetta"
  try {
    const b = document.querySelector('.cmplz-accept, #onetrust-accept-btn-handler, #CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll, .iubenda-cs-accept-btn, [class*="accept-all"], [id*="accept"]');
    if (b){ b.click(); done.push('generic-click:'+b.className); }
  } catch(e){}
  return { granted: done };
}
```

Dopo aver concesso il consenso: **attendi ~2s** (i tag si iniettano in modo asincrono), poi ri-esegui §1 e ri-lista la rete. Cerca il cookie `*_consent_mode` (Complianz) o equivalenti che riportino i segnali Consent Mode v2.

## §4 — Enumerazione script bloccati dalla CMP
Alcune CMP «congelano» gli script di tracciamento come `type="text/plain"` con `data-category`/`data-service` finché manca il consenso. Enumerarli dà l'inventario **senza** doverli far scattare (immune all'ad-blocker), ma **non** rivela i tag iniettati da GTM a runtime (per quelli serve la Fase 3-bis).

```js
() => {
  const blocked = document.querySelectorAll('script[type="text/plain"], script[data-category], script[data-service]');
  return Array.from(blocked).map(s=>({
    category: s.getAttribute('data-category')||'', service: s.getAttribute('data-service')||'',
    src: s.getAttribute('data-src')||s.src||'(inline)',
    hint: (!s.src && !s.getAttribute('data-src')) ? (s.textContent||'').replace(/\s+/g,' ').slice(0,100):''
  }));
}
```
