/**
 * Contract Chunker — splits contract text into AI-processable chunks.
 *
 * Flow:
 *   1. Takes PdfPageText[] from pdf-extract.ts
 *   2. Filters out skippable pages (cover, TOC, blank, signature-only)
 *   3. Merges remaining pages into a single text stream
 *   4. Splits into chunks of ~3000 characters, respecting paragraph boundaries
 *   5. Returns ContractChunk[] ready for AI analysis
 *
 * The chunk size of 3000 chars is chosen because:
 *   - Thai legal text averages 2 bytes/char → 3000 chars = ~6KB
 *   - AI context window can handle 3000 chars + prompt + citations comfortably
 *   - Smaller chunks = more API calls but more precise analysis
 *   - Larger chunks = fewer calls but AI may miss details
 */

import type { PdfPageText } from './pdf-extract';

const CHUNK_SIZE = 3000; // characters per chunk
const CHUNK_OVERLAP = 200; // overlap between chunks to avoid splitting mid-clause

export interface ContractChunk {
  index: number;           // 0-based chunk index
  text: string;            // chunk text (~3000 chars)
  charCount: number;       // actual char count
  pageRange: string;       // e.g., "หน้า 3-5" — for UI display
  startPage: number;       // first page number in this chunk
  endPage: number;         // last page number in this chunk
}

export interface ChunkingResult {
  chunks: ContractChunk[];
  totalChunks: number;
  totalChars: number;
  skippedPages: Array<{ pageNumber: number; reason: string }>;
  analyzedPages: number;
}

/**
 * Filter skippable pages and split remaining text into chunks.
 *
 * @param pages — PdfPageText[] from extractPdfPages()
 * @returns ChunkingResult with chunks ready for AI analysis
 */
export function chunkContractPages(pages: PdfPageText[]): ChunkingResult {
  const skippedPages: Array<{ pageNumber: number; reason: string }> = [];
  const analyzedPages: PdfPageText[] = [];

  // Step 1: Filter
  for (const page of pages) {
    if (page.isSkippable) {
      skippedPages.push({
        pageNumber: page.pageNumber,
        reason: page.skipReason || 'ไม่ระบุเหตุผล',
      });
    } else {
      analyzedPages.push(page);
    }
  }

  // Step 2: Merge pages into a single text stream with page markers
  let fullText = '';
  const pageBoundaries: Array<{ page: number; offset: number }> = analyzedPages.map(page => {
    const boundary = { page: page.pageNumber, offset: fullText.length };
    fullText += page.text + '\n\n';
    return boundary;
  });

  // Step 3: Split into chunks at paragraph boundaries
  const chunks: ContractChunk[] = [];
  let pos = 0;
  let chunkIndex = 0;
  let iterations = 0;
  const MAX_ITERATIONS = 10000; // safety valve

  while (pos < fullText.length && iterations < MAX_ITERATIONS) {
    iterations++;
    const end = findChunkEnd(fullText, pos, CHUNK_SIZE, CHUNK_OVERLAP);
    const chunkText = fullText.slice(pos, end).trim();

    if (chunkText.length > 0) {
      const pageRange = getPageRange(pos, end, pageBoundaries);
      const startPageStr = pageRange.split('-')[0].replace(/\D/g, '') || '1';
      const endPageStr = pageRange.split('-')[1]?.replace(/\D/g, '') || startPageStr;
      chunks.push({
        index: chunkIndex,
        text: chunkText,
        charCount: chunkText.length,
        pageRange,
        startPage: Number.parseInt(startPageStr, 10) || 1,
        endPage: Number.parseInt(endPageStr, 10) || 1,
      });
      chunkIndex++;
    }

    // Always advance past the chunk — overlap is handled in findChunkEnd
    if (end <= pos) {
      // Safety: if end didn't advance, force advance
      pos += CHUNK_SIZE;
    } else {
      pos = end;
    }
  }

  return {
    chunks,
    totalChunks: chunks.length,
    totalChars: fullText.length,
    skippedPages,
    analyzedPages: analyzedPages.length,
  };
}

/**
 * Find the best end position for a chunk starting at `pos`.
 * Tries to break at a paragraph boundary (double newline) or sentence end.
 * Falls back to hard cut at CHUNK_SIZE if no boundary found.
 */
function findChunkEnd(text: string, pos: number, targetSize: number, overlap: number): number {
  const idealEnd = pos + targetSize;

  // If remaining text is shorter than target, take it all
  if (idealEnd >= text.length) {
    return text.length;
  }

  // Look for paragraph boundary (double newline) within ±overlap chars of idealEnd
  const searchStart = Math.max(pos, idealEnd - overlap);
  const searchEnd = Math.min(text.length, idealEnd + overlap);

  // Try double newline first (paragraph break)
  let boundary = text.lastIndexOf('\n\n', searchEnd);
  if (boundary >= searchStart && boundary < searchEnd) {
    return boundary + 2; // include the double newline
  }

  // Try single newline (line break)
  boundary = text.lastIndexOf('\n', searchEnd);
  if (boundary >= searchStart && boundary < searchEnd) {
    return boundary + 1;
  }

  // Try sentence end (period + space or Thai full stop)
  for (let i = searchEnd; i > searchStart; i--) {
    const char = text[i];
    if (char === '.' || char === 'ฯ') {
      return i + 1;
    }
  }

  // Hard cut — no boundary found
  return idealEnd;
}

/**
 * Get the page range string for a chunk (e.g., "หน้า 3-5").
 */
function getPageRange(startOffset: number, endOffset: number, boundaries: Array<{ page: number; offset: number }>): string {
  if (boundaries.length === 0) return 'หน้า 1';

  let startPage = boundaries[0].page;
  let endPage = boundaries.at(-1)?.page ?? boundaries[0].page;

  for (const b of boundaries) {
    if (b.offset <= startOffset) {
      startPage = b.page;
    }
    if (b.offset <= endOffset) {
      endPage = b.page;
    }
  }

  if (startPage === endPage) {
    return `หน้า ${startPage}`;
  }
  return `หน้า ${startPage}-${endPage}`;
}

/**
 * Format chunking result for UI display.
 */
export function formatChunkingSummary(result: ChunkingResult): string {
  const baseLines = [
    `แบ่งเป็น ${result.totalChunks} ส่วน for AI analysis`,
    `ข้อความรวม: ${result.totalChars.toLocaleString()} ตัวอักษร`,
    `หน้าที่วิเคราะห์: ${result.analyzedPages} หน้า`,
  ];
  if (result.skippedPages.length === 0) {
    return baseLines.join('\n');
  }
  const skipHeader = `ข้าม ${result.skippedPages.length} หน้าที่ไม่จำเป็น:`;
  const skipLines = result.skippedPages.map(sp => `  • หน้า ${sp.pageNumber}: ${sp.reason}`);
  return [...baseLines, skipHeader, ...skipLines].join('\n');
}
