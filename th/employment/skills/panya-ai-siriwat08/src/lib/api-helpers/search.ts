// Shared API helper functions for search route — extracted for testability.

/** Build FTS5 query string from user input. */
export function buildFtsQuery(q: string): string {
  const safeQ = q.replace(/["']/g, ' ').trim();
  const tokens = safeQ.split(/\s+/).filter(Boolean);
  if (tokens.length === 0) return '';
  return tokens.length === 1
    ? `"${tokens[0]}"`
    : tokens.map(t => `"${t}"`).join(' OR ');
}

/** Check if a search type should be included. */
export function shouldSearch(type: string, target: string): boolean {
  return type === 'all' || type === target;
}

/** Map a DB section row to API response object. */
export function mapSectionRow(r: any) {
  return {
    type: 'section' as const,
    id: r.section_id,
    lawId: r.law_id,
    lawNameTh: r.law_title,
    lawTitle: r.law_title,
    lawCode: r.law_code,
    category: r.category,
    isLaborLaw: r.category === 'labor',
    articleKey: r.section_number_thai || `มาตรา ${r.section_number}`,
    sectionNumber: r.section_number,
    sectionNumberThai: r.section_number_thai,
    snippet: r.section_text?.slice(0, 200) || '',
    isLaborRelated: r.is_labor_related === 1,
  };
}

/** Add a section hit to the laws aggregation map. */
export function aggregateLawHit(lawsMap: Map<number, any>, s: any) {
  if (!lawsMap.has(s.lawId)) {
    lawsMap.set(s.lawId, {
      law: { lawId: s.lawId, lawNameTh: s.lawNameTh, lawTitle: s.lawTitle, category: s.category, isLaborLaw: s.isLaborLaw },
      hitCount: 0,
    });
  }
  lawsMap.get(s.lawId)!.hitCount += 1;
}
