import { NextRequest, NextResponse } from 'next/server';
import { db } from '@/lib/db';

export const dynamic = 'force-dynamic';

// GET /api/sections?id=123 — section detail + related judgments (via laws_cited in judgments)
export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const id = searchParams.get('id');
  if (!id) return NextResponse.json({ error: 'id required' }, { status: 400 });
  const sectionId = Number.parseInt(id, 10);
  if (Number.isNaN(sectionId)) return NextResponse.json({ error: 'Invalid id' }, { status: 400 });

  const section = await db.lawSection.findUnique({
    where: { sectionId },
    include: { law: true },
  });
  if (!section) return NextResponse.json({ error: 'Section not found' }, { status: 404 });

  // Find related judgments via cross_references table
  let relatedJudgments: any[] = []
  try {
    const refs = await db.crossReference.findMany({
      where: { sourceType: 'law_section', sourceId: sectionId, targetType: 'judgment' },
      take: 30,
    })
    const judgmentIds = refs.map(r => r.targetId).filter(Boolean) as number[]
    if (judgmentIds.length > 0) {
      const judgments = await db.judgment.findMany({
        where: { judgmentId: { in: judgmentIds } },
        include: { source: true },
        take: 30,
      })
      relatedJudgments = judgments.map(j => ({
        judgmentId: j.judgmentId,
        caseNumber: j.dekaNo,
        caseYear: j.year,
        year: j.year,
        category: j.caseType,
        title: j.topic,
        fact: j.fact,
        decision: j.ruling,
        sourceUrl: j.sourceUrl,
        sourceName: j.source?.sourceName ?? null,
        licenseNote: j.note,
      }))
    }
  } catch (e) {
    // cross_references table might be empty — log and continue
    console.warn('[sections] cross_references query failed:', e instanceof Error ? e.message : String(e));
  }

  // Also try: find judgments that cite this law's section number in laws_cited
  if (relatedJudgments.length === 0 && section.sectionNumber) {
    try {
      const lawTitle = section.law.title || ''
      const sectionRef = section.sectionNumber
      // Search judgments where laws_cited contains this law + section
      const judgments = await db.judgment.findMany({
        where: {
          AND: [
            { lawsCited: { contains: lawTitle.slice(0, 20) } },
            { lawsCited: { contains: `มาตรา ${sectionRef}` } },
          ],
        },
        include: { source: true },
        take: 10,
      })
      relatedJudgments = judgments.map(j => ({
        judgmentId: j.judgmentId,
        caseNumber: j.dekaNo,
        caseYear: j.year,
        year: j.year,
        category: j.caseType,
        title: j.topic,
        fact: j.fact,
        decision: j.ruling,
        sourceUrl: j.sourceUrl,
        sourceName: j.source?.sourceName ?? null,
        licenseNote: j.note,
      }))
    } catch (e) {
      // ignore — log so we can debug if it becomes a real failure
      console.warn('[sections] laws_cited fallback query failed:', e instanceof Error ? e.message : String(e));
    }
  }

  return NextResponse.json({
    sectionId: section.sectionId,
    lawId: section.lawId,
    lawNameTh: section.law.title,  // legacy alias
    title: section.law.title,
    lawCode: section.law.lawCode,
    articleKey: section.sectionNumberThai || `มาตรา ${section.sectionNumber}`,  // legacy alias
    sectionNumber: section.sectionNumber,
    sectionNumberThai: section.sectionNumberThai,
    sectionText: section.sectionText,
    isLaborRelated: section.isLaborRelated,
    isCancelled: 0,
    chapter: section.chapter,
    notes: section.notes,
    relatedJudgments,
  });
}
