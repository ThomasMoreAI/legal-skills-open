// RAG helper v3.0 — uses FTS5 + LIKE fallback
// Returns top-K chunks relevant to the user's query.
// Searches across: law_sections, judgments, regulations, contract_templates

import { db } from '@/lib/db';
import { Prisma } from '@prisma/client';

export interface RagHit {
  chunkId: number;
  sourceType: string;  // 'law_section' | 'judgment' | 'regulation' | 'contract_template'
  sourceId: number;
  lawId: number | null;
  sectionId: number | null;
  judgmentId: number | null;
  regulationId: number | null;
  templateId: number | null;
  chunkText: string;
  // Display fields:
  lawTitle?: string | null;
  lawCode?: string | null;
  sectionNumber?: string | null;
  sectionNumberThai?: string | null;
  dekaNo?: string | null;
  caseYear?: string | null;
  caseType?: string | null;
  judgmentTopic?: string | null;
  regulationTitle?: string | null;
  regulationCode?: string | null;
  templateTitle?: string | null;
  templateCode?: string | null;
  templateCategory?: string | null;
  category?: string | null;
}

function buildFtsQuery(query: string): string {
  const safeQ = query.replace(/["']/g, ' ').trim();
  if (!safeQ) return '';
  const tokens = safeQ.split(/\s+/).filter(Boolean);
  return tokens.map(t => `"${t}"`).join(' OR ');
}

const LEGAL_KEYWORDS = [
  'เลิกจ้าง', 'ค่าจ้าง', 'ค่าชดเชย', 'ค่าล่วงเวลา', 'บุริมสิทธิ์', 'ลูกจ้าง', 'นายจ้าง',
  'สัญญาจ้าง', 'แรงงาน', 'วันหยุด', 'วันลา', 'เงินเดือน', 'โบนัส', 'สวัสดิการ',
  'หยุดงาน', 'ปิดงาน', 'ผู้รับเหมา', 'ทดแทน', 'อุทธรณ์', 'ฎีกา', 'คำพิพากษา',
  'อายุความ', 'ศาลแรงงาน', 'ประกันสังคม', 'เงินทดแทน', 'จ้างทำของ', 'จ้างแรงงาน',
  'เจ็บป่วย', 'ทุพพลภาพ', 'คลอดบุตร', 'ลาป่วย', 'ลากิจ', 'ทดลองงาน',
  'สหภาพแรงงาน', 'ต่อรอง', 'นัดหยุดงาน', 'ฉ้อโกง', 'ยักยอก', 'ปลอมเอกสาร',
  'หมิ่นประมาท', 'ละเมิด', 'ค่าเสียหาย', 'ค่าสินไหม', 'จำนอง', 'จำนำ',
  'ค้ำประกัน', 'กู้ยืม', 'เช่า', 'ซื้อขาย', 'ตัวแทน', 'นายหน้า',
  'NDA', 'ความลับ', 'ไม่แข่งขัน', 'Non-compete', 'PDPA', 'ข้อมูลส่วนบุคคล',
  'ค่าจ้างขั้นต่ำ', 'พักงาน', 'ย้ายตำแหน่ง', 'ลดค่าจ้าง', 'ระเบียบวินัย',
  'ข้อบังคับ', 'สนร', 'สปส', 'กองทุนเงินทดแทน', 'อุบัติเหตุ', 'อาชีวอนามัย',
];

function extractKeywords(query: string): string[] {
  const cleaned = query.replace(/[?"'()[\]{}]/g, ' ').trim();
  const tokens = cleaned.split(/\s+/).filter(t => t.length >= 3);
  const found: string[] = [];
  for (const term of LEGAL_KEYWORDS) {
    if (query.includes(term) && !found.includes(term)) found.push(term);
    if (found.length >= 6) break;
  }
  for (const tok of tokens) {
    if (found.length >= 7) break;
    if (tok.length >= 4 && !found.includes(tok)) found.push(tok);
  }
  return found.length > 0 ? found : tokens;
}

/** Run a FTS5 query, returning [] on error (logged). Reduces cognitive complexity. */
async function tryFts(label: string, sql: Prisma.Sql): Promise<any[]> {
  try {
    return await db.$queryRaw<any[]>(sql);
  } catch (e) {
    console.error(`RAG ${label} FTS:`, e);
    return [];
  }
}

/** Run a Prisma findMany as LIKE fallback, returning [] on error. */
async function tryFindMany<T>(label: string, fn: () => Promise<T[]>): Promise<T[]> {
  try {
    return await fn();
  } catch (e) {
    console.error(`RAG ${label} LIKE fallback:`, e);
    return [];
  }
}

export async function retrieveRelevant(
  query: string,
  opts: { topK?: number; laborOnly?: boolean; category?: string } = {}
): Promise<RagHit[]> {
  const topK = opts.topK ?? 10;
  const ftsQuery = buildFtsQuery(query);
  if (!ftsQuery) return [];

  // Two-Stage Retrieval (REC-006): if category is specified, use it to filter.
  // Otherwise fall back to the legacy laborOnly boolean.
  const laborFilter = opts.laborOnly;

  // ============ FTS5 across 4 sources ============
  const sectionHits = await tryFts('section', Prisma.sql`
    SELECT s.section_id as chunk_id, 'law_section' as source_type, s.section_id as source_id,
           s.law_id, s.section_id, NULL as judgment_id, NULL as regulation_id, NULL as template_id,
           s.section_text as chunk_text,
           l.title as law_title, l.law_code, s.section_number, s.section_number_thai,
           NULL as deka_no, NULL as case_year, NULL as case_type, NULL as judgment_topic,
           NULL as regulation_title, NULL as regulation_code,
           NULL as template_title, NULL as template_code, NULL as template_category,
           l.category
    FROM law_sections_fts_v2
    JOIN law_sections s ON s.section_id = law_sections_fts_v2.rowid
    JOIN laws l ON l.law_id = s.law_id
    WHERE law_sections_fts_v2 MATCH ${ftsQuery}
      ${laborFilter ? Prisma.sql`AND (s.is_labor_related = 1 OR l.category = 'labor')` : Prisma.empty}
    ORDER BY rank
    LIMIT ${topK}
  `);

  const judgmentHits = await tryFts('judgment', Prisma.sql`
    SELECT j.judgment_id as chunk_id, 'judgment' as source_type, j.judgment_id as source_id,
           NULL as law_id, NULL as section_id, j.judgment_id, NULL as regulation_id, NULL as template_id,
           (COALESCE(j.fact,'') || ' ' || COALESCE(j.issue,'') || ' ' || COALESCE(j.ruling,'')) as chunk_text,
           NULL as law_title, NULL as law_code, NULL as section_number, NULL as section_number_thai,
           j.deka_no, j.year as case_year, j.case_type, j.topic as judgment_topic,
           NULL as regulation_title, NULL as regulation_code,
           NULL as template_title, NULL as template_code, NULL as template_category,
           NULL as category
    FROM judgments_fts_v2
    JOIN judgments j ON j.judgment_id = judgments_fts_v2.rowid
    WHERE judgments_fts_v2 MATCH ${ftsQuery}
      ${laborFilter ? Prisma.sql`AND j.case_type = 'แรงงาน'` : Prisma.empty}
    ORDER BY rank
    LIMIT ${Math.max(3, Math.floor(topK / 2))}
  `);

  const regulationHits = await tryFts('regulation', Prisma.sql`
    SELECT r.regulation_id as chunk_id, 'regulation' as source_type, r.regulation_id as source_id,
           NULL as law_id, NULL as section_id, NULL as judgment_id, r.regulation_id, NULL as template_id,
           r.full_text as chunk_text,
           NULL as law_title, NULL as law_code, NULL as section_number, NULL as section_number_thai,
           NULL as deka_no, NULL as case_year, NULL as case_type, NULL as judgment_topic,
           r.title as regulation_title, r.regulation_code,
           NULL as template_title, NULL as template_code, NULL as template_category,
           r.category
    FROM regulations_fts_v2
    JOIN regulations r ON r.regulation_id = regulations_fts_v2.rowid
    WHERE regulations_fts_v2 MATCH ${ftsQuery}
    ORDER BY rank
    LIMIT ${Math.max(2, Math.floor(topK / 3))}
  `);

  const templateHits = await tryFts('template', Prisma.sql`
    SELECT t.template_id as chunk_id, 'contract_template' as source_type, t.template_id as source_id,
           NULL as law_id, NULL as section_id, NULL as judgment_id, NULL as regulation_id, t.template_id,
           t.full_text as chunk_text,
           NULL as law_title, NULL as law_code, NULL as section_number, NULL as section_number_thai,
           NULL as deka_no, NULL as case_year, NULL as case_type, NULL as judgment_topic,
           NULL as regulation_title, NULL as regulation_code,
           t.title as template_title, t.template_code, t.category as template_category,
           NULL as category
    FROM contract_templates_fts_v2
    JOIN contract_templates t ON t.template_id = contract_templates_fts_v2.rowid
    WHERE contract_templates_fts_v2 MATCH ${ftsQuery}
    ORDER BY rank
    LIMIT ${Math.max(2, Math.floor(topK / 3))}
  `);

  // ============ LIKE fallback if FTS returned too few ============
  const sectionsFinal = sectionHits.length < 3
    ? await fillSectionsLikeFallback(query, laborFilter, topK, sectionHits)
    : sectionHits;

  const judgmentsFinal = judgmentHits.length < 2
    ? await fillJudgmentsLikeFallback(query, laborFilter, topK, judgmentHits)
    : judgmentHits;

  // ============ Combine + dedupe ============
  return dedupeHits([...sectionsFinal, ...judgmentsFinal, ...regulationHits, ...templateHits], topK);
}

/** LIKE fallback for sections when FTS returns < 3 hits. */
async function fillSectionsLikeFallback(
  query: string,
  laborOnly: boolean | undefined,
  topK: number,
  existing: any[]
): Promise<any[]> {
  const keywords = extractKeywords(query);
  const orClauses = keywords.map(k => ({ sectionText: { contains: k } }));
  if (orClauses.length === 0) return existing;

  const likeHits = await tryFindMany('sections', () => db.lawSection.findMany({
    where: {
      AND: [
        laborOnly
          ? { OR: [{ isLaborRelated: 1 }, { law: { category: 'labor' } }] }
          : {},
        { OR: orClauses as any },
      ],
    } as any,
    take: topK - existing.length,
    include: { law: true },
  }));

  const seen = new Set(existing.map(h => h.chunk_id));
  for (const r of likeHits) {
    if (seen.has(r.sectionId)) continue;
    seen.add(r.sectionId);
    existing.push({
      chunk_id: r.sectionId, source_type: 'law_section', source_id: r.sectionId,
      law_id: r.lawId, section_id: r.sectionId, judgment_id: null, regulation_id: null, template_id: null,
      chunk_text: r.sectionText,
      law_title: r.law.title, law_code: r.law.lawCode,
      section_number: r.sectionNumber, section_number_thai: r.sectionNumberThai,
      category: r.law.category,
    });
  }
  return existing;
}

/** LIKE fallback for judgments when FTS returns < 2 hits. */
async function fillJudgmentsLikeFallback(
  query: string,
  laborOnly: boolean | undefined,
  topK: number,
  existing: any[]
): Promise<any[]> {
  const keywords = extractKeywords(query);
  const orClauses = keywords.map(k => ({ OR: [{ fact: { contains: k } }, { ruling: { contains: k } }] }));
  if (orClauses.length === 0) return existing;

  const likeHits = await tryFindMany('judgments', () => db.judgment.findMany({
    where: {
      AND: [
        laborOnly ? { caseType: 'แรงงาน' } : {},
        { OR: orClauses as any },
      ],
    } as any,
    take: Math.max(3, Math.floor(topK / 2)) - existing.length,
  }));

  const seen = new Set(existing.map(h => h.chunk_id));
  for (const r of likeHits) {
    if (seen.has(r.judgmentId)) continue;
    seen.add(r.judgmentId);
    existing.push({
      chunk_id: r.judgmentId, source_type: 'judgment', source_id: r.judgmentId,
      law_id: null, section_id: null, judgment_id: r.judgmentId, regulation_id: null, template_id: null,
      chunk_text: `${r.fact || ''} ${r.issue || ''} ${r.ruling || ''}`.trim(),
      deka_no: r.dekaNo, case_year: r.year, case_type: r.caseType, judgment_topic: r.topic,
    });
  }
  return existing;
}

/** Dedupe combined hits by chunk_id and map to RagHit[]. Returns up to topK. */
function dedupeHits(all: any[], topK: number): RagHit[] {
  const seen = new Set<number>();
  const deduped: RagHit[] = [];
  for (const h of all) {
    if (seen.has(h.chunk_id)) continue;
    seen.add(h.chunk_id);
    deduped.push({
      chunkId: h.chunk_id,
      sourceType: h.source_type,
      sourceId: h.source_id,
      lawId: h.law_id,
      sectionId: h.section_id,
      judgmentId: h.judgment_id,
      regulationId: h.regulation_id,
      templateId: h.template_id,
      chunkText: h.chunk_text,
      lawTitle: h.law_title,
      lawCode: h.law_code,
      sectionNumber: h.section_number,
      sectionNumberThai: h.section_number_thai,
      dekaNo: h.deka_no,
      caseYear: h.case_year,
      caseType: h.case_type,
      judgmentTopic: h.judgment_topic,
      regulationTitle: h.regulation_title,
      regulationCode: h.regulation_code,
      templateTitle: h.template_title,
      templateCode: h.template_code,
      templateCategory: h.template_category,
      category: h.category,
    });
    if (deduped.length >= topK) break;
  }
  return deduped;
}

export function buildContext(hits: RagHit[]): string {
  if (!hits.length) return '(ไม่พบข้อมูลที่เกี่ยวข้องในฐานข้อมูล)';
  const parts: string[] = [];
  for (let i = 0; i < hits.length; i++) {
    const h = hits[i];
    let ref = '';
    let type = '';
    if (h.sourceType === 'law_section') {
      const sectionLabel = h.sectionNumberThai || (h.sectionNumber ? `มาตรา ${h.sectionNumber}` : '');
      ref = `${h.lawTitle || 'กฎหมาย'} ${sectionLabel}`;
      type = 'มาตรากฎหมาย';
    } else if (h.sourceType === 'judgment') {
      ref = `ฎีกาที่ ${h.dekaNo} (${h.caseType || 'แรงงาน'})${h.judgmentTopic ? ' — ' + h.judgmentTopic : ''}`;
      type = 'คำพิพากษาฎีกา';
    } else if (h.sourceType === 'regulation') {
      ref = `${h.regulationTitle || 'กฎกระทรวง/ประกาศ'} (${h.regulationCode})`;
      type = 'กฎกระทรวง/ประกาศ';
    } else if (h.sourceType === 'contract_template') {
      ref = `${h.templateTitle || 'เทมเพลตสัญญา'} (${h.templateCode})`;
      type = 'เทมเพลตสัญญา';
    }
    const text = h.chunkText.length > 1000 ? h.chunkText.slice(0, 1000) + '…' : h.chunkText;
    parts.push(`[${type} ${i + 1}] ${ref}\n${text}`);
  }
  return parts.join('\n\n---\n\n');
}

export function buildCitations(hits: RagHit[]) {
  return hits.map((h, i) => {
    if (h.sourceType === 'law_section') {
      const secLabel = h.sectionNumberThai || (h.sectionNumber ? `มาตรา ${h.sectionNumber}` : '');
      return {
        index: i + 1,
        type: 'section' as const,
        id: h.sectionId!,
        label: `${h.lawTitle || 'กฎหมาย'} ${secLabel}`.trim(),
        ref: h.sectionNumberThai || h.sectionNumber || '',
        snippet: h.chunkText.slice(0, 180),
        url: `/?view=section&id=${h.sectionId}`,
      };
    } else if (h.sourceType === 'judgment') {
      return {
        index: i + 1,
        type: 'judgment' as const,
        id: h.judgmentId!,
        label: `ฎีกา ${h.dekaNo}${h.judgmentTopic ? ' — ' + h.judgmentTopic : ''}`,
        ref: h.dekaNo || '',
        snippet: h.chunkText.slice(0, 180),
        url: `/?view=judgment&id=${h.judgmentId}`,
      };
    } else if (h.sourceType === 'regulation') {
      return {
        index: i + 1,
        type: 'regulation' as const,
        id: h.regulationId!,
        label: `${h.regulationTitle || 'กฎกระทรวง'} (${h.regulationCode})`,
        ref: h.regulationCode || '',
        snippet: h.chunkText.slice(0, 180),
        url: `/?view=regulation&id=${h.regulationId}`,
      };
    } else {
      return {
        index: i + 1,
        type: 'template' as const,
        id: h.templateId!,
        label: `${h.templateTitle} (${h.templateCode})`,
        ref: h.templateCode || '',
        snippet: h.chunkText.slice(0, 180),
        url: `/?view=template&id=${h.templateId}`,
      };
    }
  });
}
