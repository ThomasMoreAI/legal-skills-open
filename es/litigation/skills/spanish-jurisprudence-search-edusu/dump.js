async (page) => {
  return JSON.stringify(await page.evaluate(() => window.__log) || 'NO_CAPTURE_GLOBAL', null, 2);
}
