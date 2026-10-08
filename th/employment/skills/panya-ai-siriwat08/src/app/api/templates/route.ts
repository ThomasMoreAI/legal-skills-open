import { NextRequest, NextResponse } from 'next/server';
import { db } from '@/lib/db';

export const dynamic = 'force-dynamic';

// GET /api/templates          — list (with optional category filter)
// GET /api/templates?id=123   — single template detail (full text)
export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const id = searchParams.get('id');
  const category = searchParams.get('category');

  if (id) {
    const templateId = Number.parseInt(id, 10);
    if (Number.isNaN(templateId)) return NextResponse.json({ error: 'Invalid id' }, { status: 400 });
    const template = await db.contractTemplate.findUnique({ where: { templateId } });
    if (!template) return NextResponse.json({ error: 'Not found' }, { status: 404 });
    return NextResponse.json(template);
  }

  const where = category ? { category } : {};
  const items = await db.contractTemplate.findMany({
    where,
    orderBy: { templateId: 'asc' },
    select: {
      templateId: true, templateCode: true, title: true,
      category: true, charsCount: true,
    },
  });

  return NextResponse.json({ data: items, total: items.length });
}
