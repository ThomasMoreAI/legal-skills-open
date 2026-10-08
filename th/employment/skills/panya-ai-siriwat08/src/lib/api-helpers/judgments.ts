// Shared API helper functions — extracted from route files for testability.
// These are pure functions that don't depend on Prisma/db.

/** Parse a JSON array stored as TEXT in DB. Returns [] if invalid. */
export function parseJsonArray(raw: string | null): string[] {
  if (!raw) return [];
  try {
    const arr = JSON.parse(raw);
    return Array.isArray(arr) ? arr.filter(Boolean) : [];
  } catch {
    return [];
  }
}

/** Resolve category query param to Thai case_type. Returns undefined if no filter. */
export function resolveCategoryFilter(category: string | null): string | undefined {
  if (!category) return undefined;
  if (category === 'labor') return 'แรงงาน';
  if (category === 'criminal') return 'อาญา';
  return category;
}

/** Map judgment DB row to list response object. */
export function mapJudgmentToList(j: any) {
  return {
    judgmentId: j.judgmentId,
    caseNumber: j.dekaNo,
    dekaNo: j.dekaNo,
    caseYear: j.year,
    year: j.year,
    category: j.caseType,
    caseType: j.caseType,
    caseTypeGroup: j.caseTypeGroup,
    title: j.topic,
    topic: j.topic,
    topicsList: parseJsonArray(j.topics),
    lawsCitedList: parseJsonArray(j.lawsCited),
    fact: j.fact,
    decision: j.ruling,
    ruling: j.ruling,
    sourceUrl: j.sourceUrl,
    sourceName: j.source?.sourceName ?? null,
    licenseNote: j.note,
    note: j.note,
  };
}
