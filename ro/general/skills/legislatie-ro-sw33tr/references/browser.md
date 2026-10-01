# Ruta prin browser (Claude in Chrome sau browserul integrat)

Folosește-o când nici mediul curent, nici calculatorul utilizatorului nu pot rula scripturile.
Browserul utilizatorului trece de blocaje pentru că folosește IP-ul lui.

Instrumente: Claude in Chrome (`mcp__claude-in-chrome__*`, preferat) sau browserul integrat al aplicației, dacă există.
Încarcă-le într-un singur apel ToolSearch, de ex.:
`select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__tabs_close_mcp`

## Pași

1. Află id-ul actului (căutarea prin API merge aproape oriunde: `legislatie_search.py "OUG 57/2019"`).
   Dacă nici API-ul nu merge, folosește în browser formularul de căutare de pe `https://legislatie.just.ro`.
2. `navigate` la `https://legislatie.just.ro/Public/DetaliiDocument/<id>`: această rută afișează
   ULTIMA consolidare. (`DetaliiDocumentAfis/<id>` afișează forma publicată inițial, deci nu o folosi.)
3. Rulează cu `javascript_tool` fragmentul de mai jos (setează `ART`). Rezultatul poate fi:
   - `Consolidarea din DD.MM.YYYY | … | len=N`: articolul e în `window.__a`.
   - `AMBALAJ: deschide DetaliiDocument/<id2>`: actul e un „ambalaj” (ex. Legea 53/2003 → Codul
     muncii, 309240). Navighează la id2 și rulează din nou.
   - `len=0`: articolul nu există în forma în vigoare (abrogat/renumerotat?). Verifică cu `grep`-ul JS de mai jos.
   - Dacă „alte consolidări, cea mai recentă” are o dată MAI NOUĂ decât forma afișată, navighează la acel id.
4. Citește textul pe bucăți: `window.__a.substring(0, 700)`, `(700, 1400)`, … `javascript_tool` din
   Chrome trunchiază răspunsul la ~800 de caractere pe apel, indiferent cât returnează expresia.
5. Închide tab-ul (`tabs_close_mcp`).

Nu apela `get_page_text` / `read_page` pe acte mari: Codul administrativ are 1,5 milioane de caractere.

## Fragment de extragere

```js
await new Promise(r => { const f = () => document.readyState === 'complete' ? r() : setTimeout(f, 300); f(); });
(() => {
  const ART = '485^1';   // <- articolul: '12', '485^1', 'XLIX', 'unic'
  const cur = document.querySelector('#istoric_fa a:not([href])');
  const other = [...document.querySelectorAll('#istoric_fa a[href]')]
    .map(a => a.textContent.trim() + '=' + (a.getAttribute('href').match(/\d+/g) || []).pop())[0];
  const t = document.body.innerText;
  const lead = (t.match(/^\s*Articolul\s/gm) || []).length >= (t.match(/^\s*Art\.\s/gm) || []).length ? 'Articolul' : 'Art\\.';
  if (!new RegExp('^\\s*' + lead + '\\s+\\S', 'm').test(t)) {
    const w = document.querySelector('#div_Formaconsolidata a[href*="DetaliiDocument"]');
    return (cur ? cur.title : '-') + ' | AMBALAJ: deschide DetaliiDocument/' + (w ? (w.getAttribute('href').match(/\d+/g) || []).pop() : '?');
  }
  const esc = ART.replace(/[\^.]/g, c => '\\' + c);
  const start = new RegExp('^\\s*' + lead + '\\s+' + esc + '(?![\\d^])', 'gm');   // 56 nu prinde 560 sau 56^1
  const next = new RegExp('^\\s*' + lead + '\\s+(?:\\d+(?:\\^\\d+)?|[IVXLCDM]+|unic)(?![\\w^])', 'gm');
  let best = null, m;
  while ((m = start.exec(t))) {           // prima apariție e de obicei cuprinsul: păstrăm corpul cel mai lung
    next.lastIndex = m.index + m[0].length;
    const n = next.exec(t), end = n ? n.index : t.length;
    if (!best || end - m.index > best[1] - best[0]) best = [m.index, end];
  }
  window.__a = best ? t.slice(best[0], best[1]).trim() : '';
  return (cur ? cur.title : 'FĂRĂ CONSOLIDĂRI (forma publicată)') +
         ' | alte consolidări, cea mai recentă: ' + (other || '-') + ' | len=' + window.__a.length;
})()
```

Căutare de text în pagină (echivalentul `--grep`):

```js
(() => { const q = /concediu de odihn/i;
  return document.body.innerText.split('\n').filter(l => q.test(l)).slice(0, 8).map(l => l.slice(0, 90)).join('\n'); })()
```
