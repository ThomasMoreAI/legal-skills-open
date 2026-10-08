// Shared API helper functions for laws route — extracted for testability.

/** Build Prisma where clause for section keyword filter. */
export function buildSectionFilter(q: string | undefined) {
  if (!q) return undefined;
  return {
    OR: [
      { sectionText: { contains: q } },
      { sectionNumber: { contains: q } },
      { sectionNumberThai: { contains: q } },
    ],
  };
}

/** Map law DB row to list response object. */
export function mapLawToList(l: any) {
  return {
    lawId: l.lawId,
    lawCode: l.lawCode,
    title: l.title,
    lawNameTh: l.title,
    lawNameEn: null,
    year: l.year,
    category: l.category,
    isLaborLaw: l.category === 'labor' ? 1 : 0,
    status: l.status,
    sourceUrl: l.sourceUrl,
    sectionCount: l._count.sections,
    laborSectionCount: l.sections.length,
  };
}
