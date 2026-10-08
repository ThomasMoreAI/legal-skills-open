// POST /api/contracts/analyze
// Analyzes a single contract chunk for legal violations.
// Called by the client for each chunk after PDF extraction + chunking.
//
// Body: { chunk: string, chunkIndex: number, totalChunks: number, pageRange: string }
// Returns: { findings: Array<{ clause, issue, legalBasis, severity, suggestion }>, chunkIndex }
//
// Uses the existing /api/ask infrastructure (RAG + LLM + disclaimer) but with
// a specialized contract-analysis prompt.

import { NextRequest, NextResponse } from 'next/server';
import { retrieveRelevant, buildContext, buildCitations } from '@/lib/rag';
import { createChatCompletion } from '@/lib/zai-client';
import { withDisclaimer } from '@/lib/disclaimer';

export const dynamic = 'force-dynamic';
export const maxDuration = 60;

const CONTRACT_ANALYSIS_PROMPT = `คุณคือ "Panya-AI" — Legal Strategist & Labor Law Expert ประจำ หจก.เผ่าปัญญา ทรานสปอร์ต

# 📋 SKILL: Contract Chunk Analysis
คุณกำลังวิเคราะห์ส่วนหนึ่งของสัญญาจ้างแรงงาน (chunk) เพื่อหาข้อที่ผิดกฎหมาย

## ขั้นตอนวิเคราะห์
1. อ่านข้อความใน chunk นี้
2. ระบุข้อความที่ผิดกฎหมายแรงงาน (ถ้ามี)
3. อ้างอิงมาตราที่เกี่ยวข้อง
4. เสนอแนะการแก้ไข

## กฎหมายที่ต้องเช็ค
- พ.ร.บ.คุ้มครองแรงงาน 2541: ม.118(ค่าชดเชย) ม.119(เลิกจ้างไม่ชดเชย) ม.76(หักค่าจ้าง)
  ม.27(ชั่วโมงทำงาน) ม.28(วันหยุด) ม.57(ลาป่วย) ม.41(ลาคลอด) ม.61(OT)
- ป.พ.พ.: ม.575 vs ม.587 — แยกลูกจ้าง vs รถร่วม
- ห้าม: เลิกจ้างได้ทุกเวลา, หักเงินเป็นค่าปรับ, ลดค่าจ้างฝ่ายเดียว, ห้ามลาออก

## รูปแบบคำตอบ
หากพบข้อผิดกฎหมาย:
⚠️ พบปัญหา:
- [ข้อความในสัญญา] → ผิด [มาตรา] เพราะ [เหตุผล]
- ความรุนแรง: ร้ายแรง/ปานกลาง/ต่ำ
✅ แนะนำ: [ข้อความที่ควรแก้เป็น]

หากไม่พบปัญหา:
✅ ส่วนนี้ไม่พบข้อที่ผิดกฎหมาย

อ้างอิง [N] จาก context เท่านั้น ตอบภาษาไทย กระชับ`;

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { chunk, chunkIndex, totalChunks, pageRange } = body;

    if (!chunk || typeof chunk !== 'string') {
      return NextResponse.json(
        { error: 'Missing required field: chunk (string)' },
        { status: 400 }
      );
    }

    // Retrieve relevant law sections for context
    const hits = await retrieveRelevant(chunk, { topK: 8, laborOnly: true });
    const context = buildContext(hits);
    const citations = buildCitations(hits);

    // Build messages for LLM
    const question = `วิเคราะห์สัญญาส่วนที่ ${chunkIndex + 1}/${totalChunks} (${pageRange}):\n\n${chunk}`;
    const messages = [
      { role: 'assistant' as const, content: CONTRACT_ANALYSIS_PROMPT },
      { role: 'user' as const, content: `Context กฎหมาย:\n${context}\n\n---\n\nคำถาม: ${question}` },
    ];

    const { content: aiContent } = await createChatCompletion(messages);

    return NextResponse.json(withDisclaimer({
      answer: aiContent || 'ไม่สามารถวิเคราะห์ได้',
      citations,
      chunkIndex,
      totalChunks,
      pageRange,
    }));
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : 'Unknown error';
    return NextResponse.json(
      withDisclaimer({ answer: `เกิดข้อผิดพลาด: ${message}` }),
      { status: 500 }
    );
  }
}
