import { NextRequest, NextResponse } from 'next/server';
import { db } from '@/lib/db';
import { Prisma } from '@prisma/client';
import { buildFtsQuery, shouldSearch, mapSectionRow, aggregateLawHit } from '@/lib/api-helpers/search';

export const dynamic = 'force-dynamic';

/** Run a FTS query, returning [] on error (logged). */
async function tryFts(label: string, sql: Prisma.Sql): Promise<any[]> {
  try {
    return await db.$queryRaw<any[]>(sql);
  } catch (e) {
    console.error(`Search ${label} FTS failed:`, e);
    return [];
  }
}

/** Search sections via FTS5 + LIKE fallback. Updates lawsMap with aggregated hits. */
async function searchSections(ftsQuery: string, q: string, limit: number, lawsMap: Map<number, any>): Promise<any[]> {
  const shouldSearch = ftsQuery !== '';
  let sections: any[] = [];

  if (shouldSearch) {
    const rows = await tryFts('section', Prisma.sql`
      SELECT s.section_id, s.law_id, s.section_number, s.section_number_thai,
             s.section_text, s.is_labor_related,
             l.title as law_title, l.law_code, l.category
      FROM law_sections_fts_v2
      JOIN law_sections s ON s.section_id = law_sections_fts_v2.rowid
      JOIN laws l ON l.law_id = s.law_id
      WHERE law_sections_fts_v2 MATCH ${ftsQuery}
      ORDER BY rank
      LIMIT ${limit}
    `);
    sections = rows.map(mapSectionRow);
  }

  // LIKE fallback if FTS returned 0 results (Thai text issue)
  if (sections.length === 0) {
    const likeRows = await db.lawSection.findMany({
      where: { sectionText: { contains: q } },
      take: limit,
      include: { law: true },
    });
    sections = likeRows.map(r => mapSectionRow({
      section_id: r.sectionId, law_id: r.lawId, section_number: r.sectionNumber,
      section_number_thai: r.sectionNumberThai, section_text: r.sectionText,
      is_labor_related: r.isLaborRelated, law_title: r.law.title,
      law_code: r.law.lawCode, category: r.law.category,
    }));
  }

  // Aggregate section hits by law
  for (const s of sections) {
    aggregateLawHit(lawsMap, s);
  }
  return sections;
}

/** Search judgments via FTS5 + LIKE fallback. */
async function searchJudgments(ftsQuery: string, q: string, limit: number): Promise<any[]> {
  let judgments: any[] = [];

  if (ftsQuery) {
    const rows = await tryFts('judgment', Prisma.sql`
      SELECT j.judgment_id, j.deka_no, j.year, j.case_type,
             j.topic, j.fact, j.ruling, j.source_url, j.note,
             s.source_name
      FROM judgments_fts_v2
      JOIN judgments j ON j.judgment_id = judgments_fts_v2.rowid
      LEFT JOIN sources s ON s.source_id = j.source_id
      WHERE judgments_fts_v2 MATCH ${ftsQuery}
      ORDER BY rank
      LIMIT ${limit}
    `);
    judgments = rows.map(r => ({
      type: 'judgment' as const, id: r.judgment_id,
      caseNumber: r.deka_no, dekaNo: r.deka_no,
      caseYear: r.year, year: r.year,
      category: r.case_type, caseType: r.case_type,
      title: r.topic, topic: r.topic,
      snippet: (r.fact || r.ruling || '').slice(0, 200),
      sourceUrl: r.source_url, sourceName: r.source_name,
      licenseNote: r.note, note: r.note,
    }));
  }

  // LIKE fallback
  if (judgments.length === 0) {
    const likeRows = await db.judgment.findMany({
      where: { OR: [{ fact: { contains: q } }, { ruling: { contains: q } }, { topic: { contains: q } }] },
      take: limit,
      include: { source: true },
    });
    judgments = likeRows.map(r => ({
      type: 'judgment' as const, id: r.judgmentId,
      caseNumber: r.dekaNo, dekaNo: r.dekaNo,
      caseYear: r.year, year: r.year,
      category: r.caseType, caseType: r.caseType,
      title: r.topic, topic: r.topic,
      snippet: (r.fact || r.ruling || '').slice(0, 200),
      sourceUrl: r.sourceUrl, sourceName: r.source?.sourceName ?? null,
      licenseNote: r.note, note: r.note,
    }));
  }
  return judgments;
}

/** Search regulations via FTS5 (active only). */
async function searchRegulations(ftsQuery: string, limit: number): Promise<any[]> {
  if (!ftsQuery) return [];
  const rows = await tryFts('regulation', Prisma.sql`
    SELECT r.regulation_id, r.regulation_code, r.title, r.category,
           r.full_text, r.is_repealed, r.repeal_status, r.year
    FROM regulations_fts_v2
    JOIN regulations r ON r.regulation_id = regulations_fts_v2.rowid
    WHERE regulations_fts_v2 MATCH ${ftsQuery}
      AND r.repeal_status = 'active'
    ORDER BY rank
    LIMIT ${Math.max(3, Math.floor(limit / 3))}
  `);
  return rows.map(r => ({
    type: 'regulation' as const, id: r.regulation_id,
    regulationCode: r.regulation_code, title: r.title, category: r.category,
    snippet: r.full_text?.slice(0, 200) || '',
    isRepealed: r.is_repealed === 1, repealStatus: r.repeal_status,
    year: r.year || null,
  }));
}

/** Search contract templates via FTS5. */
async function searchTemplates(ftsQuery: string, limit: number): Promise<any[]> {
  if (!ftsQuery) return [];
  const rows = await tryFts('template', Prisma.sql`
    SELECT t.template_id, t.template_code, t.title, t.category, t.full_text
    FROM contract_templates_fts_v2
    JOIN contract_templates t ON t.template_id = contract_templates_fts_v2.rowid
    WHERE contract_templates_fts_v2 MATCH ${ftsQuery}
    ORDER BY rank
    LIMIT ${Math.max(3, Math.floor(limit / 3))}
  `);
  return rows.map(r => ({
    type: 'template' as const, id: r.template_id,
    templateCode: r.template_code, title: r.title, category: r.category,
    snippet: r.full_text?.slice(0, 200) || '',
  }));
}

/** Search laws by name + merge section-hit aggregated laws. */
async function searchLawsByName(q: string, limit: number, lawsMap: Map<number, any>): Promise<any[]> {
  const lawRows = await db.law.findMany({
    where: { title: { contains: q } },
    take: limit,
    include: { _count: { select: { sections: true } } },
  });
  const laws = lawRows.map(l => ({
    type: 'law' as const, id: l.lawId,
    lawNameTh: l.title, title: l.title, lawCode: l.lawCode, lawNameEn: null,
    year: l.year, category: l.category, isLaborLaw: l.category === 'labor',
    sectionCount: l._count.sections,
  }));

  // Include laws that had section hits but weren't in the name match
  for (const [lawId, info] of lawsMap) {
    if (!laws.some(l => l.id === lawId)) {
      laws.push({
        type: 'law' as const, id: lawId,
        lawNameTh: info.law.lawNameTh || info.law.lawTitle,
        title: info.law.lawTitle || info.law.lawNameTh,
        lawCode: null, lawNameEn: null, year: null,
        category: info.law.category, isLaborLaw: info.law.isLaborLaw,
        sectionCount: 0, hitCount: info.hitCount,
      });
    }
  }
  return laws;
}

// GET /api/search?q=ค่าจ้าง&type=all&limit=20
export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const q = (searchParams.get('q') || '').trim();
  const type = searchParams.get('type') || 'all';
  const limit = Math.min(Number.parseInt(searchParams.get('limit') || '20', 10), 100);

  if (!q) {
    return NextResponse.json({ sections: [], judgments: [], laws: [], regulations: [], templates: [], total: 0 });
  }

  const ftsQuery = buildFtsQuery(q);
  const lawsMap = new Map<number, any>();

  const sections = shouldSearch(type, 'sections') ? await searchSections(ftsQuery, q, limit, lawsMap) : [];
  const judgments = shouldSearch(type, 'judgments') ? await searchJudgments(ftsQuery, q, limit) : [];
  const regulations = shouldSearch(type, 'regulations') ? await searchRegulations(ftsQuery, limit) : [];
  const templates = shouldSearch(type, 'templates') ? await searchTemplates(ftsQuery, limit) : [];
  const laws = shouldSearch(type, 'laws') ? await searchLawsByName(q, limit, lawsMap) : [];

  const total = sections.length + judgments.length + laws.length + regulations.length + templates.length;

  return NextResponse.json({ sections, judgments, laws, regulations, templates, total, q, type });
}
