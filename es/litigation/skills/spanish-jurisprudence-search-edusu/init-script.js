async (page) => {
  await page.addInitScript(() => {
    window.__log = [];
    const origFetch = window.fetch;
    window.fetch = async function(...args) {
      const [url, opts={}] = args;
      const entry = { kind: 'fetch', url: String(url), method: opts?.method || 'GET', body: opts?.body ? String(opts.body) : null, ts: Date.now() };
      try {
        const resp = await origFetch.apply(this, args);
        entry.status = resp.status;
        entry.respCT = resp.headers.get('content-type');
        window.__log.push(entry);
        return resp;
      } catch (e) { entry.err = String(e); window.__log.push(entry); throw e; }
    };
    const OrigXHR = window.XMLHttpRequest;
    function PatchedXHR() {
      const xhr = new OrigXHR();
      let _url, _method, _body, _hdrs = {};
      const origOpen = xhr.open;
      xhr.open = function(m, u) { _method = m; _url = u; return origOpen.apply(xhr, arguments); };
      const origSetH = xhr.setRequestHeader;
      xhr.setRequestHeader = function(k, v) { _hdrs[k] = v; return origSetH.apply(xhr, arguments); };
      const origSend = xhr.send;
      xhr.send = function(b) {
        _body = b;
        xhr.addEventListener('loadend', () => {
          window.__log.push({
            kind: 'xhr',
            url: _url, method: _method,
            body: _body ? String(_body) : null,
            reqHeaders: _hdrs,
            status: xhr.status,
            respCT: xhr.getResponseHeader('content-type'),
            respLen: (xhr.responseText||'').length
          });
        });
        return origSend.apply(xhr, arguments);
      };
      return xhr;
    }
    PatchedXHR.prototype = OrigXHR.prototype;
    window.XMLHttpRequest = PatchedXHR;
  });
  return 'init-script-set';
}
