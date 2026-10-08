import { NextRequest, NextResponse } from 'next/server';
import { db } from '@/lib/db';
import { parseJsonArray, resolveCategoryFilter, mapJudgmentToList } from '@/lib/api-helpers/judgments';

export const dynamic = 'force-dynamic';

/** Fetch related sections for a judgment via cross_references table. */
async function fetchRelatedSections(judgmentId: number): Promise<any[]> {
  try {
    const refs = await db.crossReference.findMany({
      where: { sourceType: 'judgment', sourceId: judgmentId, targetType: 'law_section' },
      take: 30,
    });
    const sectionIds = refs.map(r => r.targetId).filter(Boolean) as number[];
    if (sectionIds.length === 0) return [];

    const sections = await db.lawSection.findMany({
      where: { sectionId: { in: sectionIds } },
      include: { law: true },
      take: 30,
    });
    return sections.map(s => ({
      sectionId: s.sectionId,
      lawId: s.lawId,
      lawNameTh: s.law.title,
      articleKey: s.sectionNumberThai || `มาตรา ${s.sectionNumber}`,
      sectionNumber: s.sectionNumber,
      sectionText: s.sectionText,
      isLaborRelated: s.isLaborRelated,
      isCancelled: 0,
      chapter: s.chapter,
      notes: s.notes,
    }));
  } catch (e) {
    console.warn('[judgments] cross_references query failed:', e instanceof Error ? e.message : String(e));
    return [];
  }
}

/** Handle GET /api/judgments?id=123 — single judgment detail. */
async function handleDetail(id: string): Promise<NextResponse> {
  const judgmentId = Number.parseInt(id, 10);
  if (Number.isNaN(judgmentId)) return NextResponse.json({ error: 'Invalid id' }, { status: 400 });

  const judgment = await db.judgment.findUnique({
    where: { judgmentId },
    include: { source: true },
  });
  if (!judgment) return NextResponse.json({ error: 'Judgment not found' }, { status: 404 });

  const relatedSections = await fetchRelatedSections(judgmentId);

  return NextResponse.json({
    judgmentId: judgment.judgmentId,
    caseNumber: judgment.dekaNo,
    dekaNo: judgment.dekaNo,
    caseYear: judgment.year,
    year: judgment.year,
    court: 'ศาลฎีกา',
    category: judgment.caseType,
    caseType: judgment.caseType,
    caseTypeGroup: judgment.caseTypeGroup,
    categoryCode: null,
    issueNumber: null,
    lawReferences: judgment.lawsCited,
    lawsCited: judgment.lawsCited,
    lawsCitedList: parseJsonArray(judgment.lawsCited),
    topic: judgment.topic,
    topics: judgment.topics,
    topicsList: parseJsonArray(judgment.topics),
    fact: judgment.fact,
    decision: judgment.ruling,
    ruling: judgment.ruling,
    verdict: judgment.verdict,
    issue: judgment.issue,
    title: judgment.topic,
    sourceId: judgment.sourceId,
    sourceUrl: judgment.sourceUrl,
    sourceName: judgment.source?.sourceName ?? null,
    sourceDescription: judgment.source?.description ?? null,
    licenseNote: judgment.note,
    note: judgment.note,
    fullText: judgment.fullText,
    relatedSections,
  });
}

// GET /api/judgments              — list (filter by case_type, page)
// GET /api/judgments?id=123       — judgment detail + related sections
export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const id = searchParams.get('id');

  // Detail mode
  if (id) return handleDetail(id);

  // List mode
  const category = searchParams.get('category');
  const page = Number.parseInt(searchParams.get('page') || '1', 10);
  const pageSize = Math.min(Number.parseInt(searchParams.get('pageSize') || '30', 10), 100);
  const skip = (page - 1) * pageSize;

  const caseType = resolveCategoryFilter(category);
  const where = caseType ? { caseType } : {};

  const [judgments, total] = await Promise.all([
    db.judgment.findMany({
      where,
      include: { source: true },
      skip,
      take: pageSize,
      orderBy: { judgmentId: 'asc' },
    }),
    db.judgment.count({ where }),
  ]);

  return NextResponse.json({
    data: judgments.map(mapJudgmentToList),
    page,
    pageSize,
    total,
    totalPages: Math.ceil(total / pageSize),
  });
}
