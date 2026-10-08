import { NextRequest, NextResponse } from 'next/server';
import { db } from '@/lib/db';
import { markdownToHtml, fillEmployeeName, fillPosition, fillStartDate, fillSalary } from '@/lib/api-helpers/pdf';

export const dynamic = 'force-dynamic';

/** Parse and validate request params. Returns null if invalid (with response). */
function parseRequest(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const id = searchParams.get('id');
  if (!id) return { error: NextResponse.json({ error: 'id required' }, { status: 400 }) };
  const templateId = Number.parseInt(id, 10);
  if (Number.isNaN(templateId)) return { error: NextResponse.json({ error: 'Invalid id' }, { status: 400 }) };
  return {
    templateId,
    employeeName: searchParams.get('employee') || '',
    position: searchParams.get('position') || '',
    startDate: searchParams.get('startDate') || '',
    salary: searchParams.get('salary') || '',
  };
}

/** Build the full HTML page with styles. */
function buildFullHtml(html: string, template: { title: string; templateCode: string; charsCount: number }): string {
  return `<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<title>${template.title} — Panya-AI</title>
<style>
  @page { size: A4; margin: 2cm; }
  body { font-family: 'TH Sarabun New', 'Sukhumvit Set', 'Noto Sans Thai', sans-serif; font-size: 16px; line-height: 1.8; color: #1a1a1a; max-width: 800px; margin: 0 auto; padding: 20px; }
  h1 { font-size: 24px; text-align: center; margin: 20px 0; }
  h2 { font-size: 20px; margin-top: 30px; }
  h3 { font-size: 18px; margin-top: 25px; }
  p { margin: 10px 0; }
  ul { margin: 10px 0; padding-left: 30px; }
  li { margin: 5px 0; }
  hr { border: none; border-top: 1px dashed #ccc; margin: 20px 0; }
  strong { font-weight: bold; }
  u { text-decoration: underline; }
  .print-btn { position: fixed; top: 10px; right: 10px; padding: 10px 20px; background: #E8541A; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 14px; z-index: 9999; }
  .print-btn:hover { background: #c7421a; }
  @media print { .print-btn { display: none; } body { padding: 0; } }
  .footer { margin-top: 50px; padding-top: 20px; border-top: 1px solid #eee; font-size: 12px; color: #888; text-align: center; }
</style>
</head>
<body>
<button class="print-btn" onclick="window.print()">🖨️ พิมพ์ / บันทึกเป็น PDF</button>
${html}
<div class="footer">
  เอกสารนี้สร้างโดย Panya-AI — ฝั่งนายจ้าง/บริษัท<br/>
  Template: ${template.templateCode} | ขนาด: ${template.charsCount} ตัวอักษร<br/>
  ⚠️ ควรให้ทนายความตรวจทานก่อนใช้งานจริง
</div>
</body>
</html>`;
}

// GET /api/templates/pdf?id=123&employee=นาย+สมชาย+ใจดี
export async function GET(req: NextRequest) {
  const parsed = parseRequest(req);
  if ('error' in parsed) return parsed.error;

  const template = await db.contractTemplate.findUnique({ where: { templateId: parsed.templateId } });
  if (!template) return NextResponse.json({ error: 'Not found' }, { status: 404 });

  let html = markdownToHtml(template.fullText || '');
  html = fillEmployeeName(html, parsed.employeeName);
  html = fillPosition(html, parsed.position);
  html = fillStartDate(html, parsed.startDate);
  html = fillSalary(html, parsed.salary);

  const fullHtml = buildFullHtml(html, template);
  return new NextResponse(fullHtml, {
    headers: { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store' },
  });
}
