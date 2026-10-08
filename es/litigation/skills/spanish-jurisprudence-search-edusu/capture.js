async (page) => {
  const fs = await import('fs');
  const path = '/Users/edusu/Obsidian/.playwright-cli/network-log.jsonl';
  try { fs.unlinkSync(path); } catch (e) {}
  const append = (obj) => fs.appendFileSync(path, JSON.stringify(obj) + '\n');
  page.on('request', req => {
    const url = req.url();
    if (url.includes('.action')) {
      append({
        kind: 'req',
        method: req.method(),
        url,
        headers: req.headers(),
        postData: req.postData()
      });
    }
  });
  page.on('response', async resp => {
    const url = resp.url();
    if (url.includes('.action')) {
      let body = null;
      try {
        const buf = await resp.body();
        body = buf.toString('utf8');
      } catch (e) { body = '<' + e.message + '>'; }
      append({
        kind: 'resp',
        url,
        status: resp.status(),
        contentType: resp.headers()['content-type'],
        bodyLen: body ? body.length : 0,
        bodyPreview: body ? body.slice(0, 8000) : null
      });
    }
  });
  return 'listener-attached-to-' + path;
}
