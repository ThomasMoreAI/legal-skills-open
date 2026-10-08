import { NextRequest, NextResponse } from 'next/server';
import { db } from '@/lib/db';

export const dynamic = 'force-dynamic';

export async function GET(_req: NextRequest) {
  const [
    totalLaws,
    totalSections,
    totalJudgments,
    totalRegulations,
    totalTemplates,
    totalRagChunks,
    totalCrossRefs,
    totalLaborSections,
    laborLawCount,
    totalLaborJudgments,
    totalCriminalJudgments,
  ] = await Promise.all([
    db.law.count(),
    db.lawSection.count(),
    db.judgment.count(),
    db.regulation.count(),
    db.contractTemplate.count(),
    db.ragChunk.count(),
    db.crossReference.count(),
    db.lawSection.count({ where: { isLaborRelated: 1 } }),
    db.law.count({ where: { category: 'labor' } }),
    db.judgment.count({ where: { caseType: 'แรงงาน' } }),
    db.judgment.count({ where: { caseType: 'อาญา' } }),
  ]);

  // Laws by category with section counts
  const laws = await db.law.findMany({
    select: {
      lawId: true,
      category: true,
      sections: { select: { sectionId: true, isLaborRelated: true } },
    },
  });
  const byCat: Record<string, { count: number; sectionCount: number; laborSectionCount: number }> = {};
  for (const l of laws) {
    const cat = l.category || 'other';
    if (!byCat[cat]) byCat[cat] = { count: 0, sectionCount: 0, laborSectionCount: 0 };
    byCat[cat].count += 1;
    byCat[cat].sectionCount += l.sections.length;
    byCat[cat].laborSectionCount += l.sections.filter(s => s.isLaborRelated).length;
  }
  const lawsByCategory = Object.entries(byCat).map(([category, v]) => ({
    category,
    count: v.count,
    sectionCount: v.sectionCount,
    laborSectionCount: v.laborSectionCount,
  }));

  // Templates by category
  const templates = await db.contractTemplate.findMany({
    select: { category: true },
  });
  const templatesByCat: Record<string, number> = {};
  for (const t of templates) {
    const c = t.category || 'other';
    templatesByCat[c] = (templatesByCat[c] || 0) + 1;
  }

  return NextResponse.json({
    totalLaws,
    totalSections,
    totalJudgments,
    totalLaborJudgments,
    totalCriminalJudgments,
    totalRegulations,
    totalTemplates,
    totalRagChunks,
    totalCrossRefs,
    totalLaborSections,
    laborLawCount,
    lawsByCategory,
    templatesByCategory: Object.entries(templatesByCat).map(([category, count]) => ({ category, count })),
    regulationStatus: { active: 48, superseded: 567 },
    latestJudgmentYear: '2563',
    version: '3.0',
    lastUpdated: '2026-08-02',
  });
}
