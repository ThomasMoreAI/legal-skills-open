// Replicate exact logic from search route
import { PrismaClient, Prisma } from '@prisma/client';
const db = new PrismaClient();
try {
  const q = 'ค่าจ้าง';
  const safeQ = q.replace(/["']/g, ' ').trim();
  const ftsQuery = safeQ.split(/\s+/).filter(Boolean).map(t => `"${t}"`).join(' OR ');
  console.log('ftsQuery:', JSON.stringify(ftsQuery));
  const limit = 3;
  
  const rows = await db.$queryRaw<any[]>(Prisma.sql`
    SELECT s.section_id, s.law_id, s.article_key, s.section_number,
           s.section_text, s.is_labor_related, s.is_cancelled,
           l.law_name_th, l.category, l.is_labor_law,
           snippet(law_sections_fts_v2, 0, '<<', '>>', '...', 24) as snippet
    FROM law_sections_fts_v2
    JOIN law_sections s ON s.section_id = law_sections_fts_v2.rowid
    JOIN laws l ON l.law_id = s.law_id
    WHERE law_sections_fts_v2 MATCH ${ftsQuery}
    ORDER BY rank
    LIMIT ${limit}
  `);
  console.log('Rows:', rows.length);
  if (rows.length > 0) console.log('First row snippet:', rows[0].snippet?.slice(0, 100));
} catch (e: any) {
  console.error('ERR:', e.message);
  console.error('CODE:', e.code);
} finally {
  await db.$disconnect();
}
