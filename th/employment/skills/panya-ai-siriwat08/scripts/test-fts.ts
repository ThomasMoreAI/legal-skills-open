import { PrismaClient } from '@prisma/client';
import { Prisma } from '@prisma/client';
const db = new PrismaClient();
try {
  const q = 'ค่าจ้าง';
  const ftsQuery = `"${q}"`;
  console.log('FTS query:', ftsQuery);
  const rows = await db.$queryRaw<any[]>(Prisma.sql`
    SELECT s.section_id, s.law_id, s.article_key, snippet(law_sections_fts_v2, 0, '<<', '>>', '...', 24) as snippet
    FROM law_sections_fts_v2
    JOIN law_sections s ON s.section_id = law_sections_fts_v2.rowid
    WHERE law_sections_fts_v2 MATCH ${ftsQuery}
    LIMIT 5
  `);
  console.log('Rows:', rows.length);
  console.log('First:', rows[0]);
} catch (e: any) {
  console.error('ERR:', e.message);
} finally {
  await db.$disconnect();
}
