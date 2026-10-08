// Tests for src/lib/contract-chunker.ts — contract text chunking
import { describe, it, expect } from 'vitest';
import { chunkContractPages, formatChunkingSummary } from '../contract-chunker';
import type { PdfPageText } from '../pdf-extract';

function makePage(pageNum: number, text: string, skippable = false, reason?: string): PdfPageText {
  return {
    pageNumber: pageNum,
    text,
    charCount: text.length,
    isSkippable: skippable,
    skipReason: reason,
  };
}

describe('Contract Chunker', () => {
  describe('chunkContractPages()', () => {
    it('returns empty chunks for empty input', () => {
      const result = chunkContractPages([]);
      expect(result.chunks).toEqual([]);
      expect(result.totalChunks).toBe(0);
      expect(result.totalChars).toBe(0);
    });

    it('returns single chunk for short text', () => {
      const pages = [makePage(1, 'สัญญาจ้างแรงงาน ข้อ 1 นายจ้างตกลงจ้าง')];
      const result = chunkContractPages(pages);
      expect(result.totalChunks).toBe(1);
      expect(result.chunks[0].text).toContain('สัญญาจ้างแรงงาน');
      expect(result.chunks[0].pageRange).toContain('หน้า 1');
    });

    it('filters out skippable pages', () => {
      const pages = [
        makePage(1, 'สัญญาจ้าง', true, 'หน้าปกสัญญา'),
        makePage(2, 'ข้อ 1 นายจ้างตกลงจ้างลูกจ้าง'),
        makePage(3, '', true, 'หน้าว่าง'),
        makePage(4, 'ข้อ 2 ลูกจ้างตกลงทำงาน'),
      ];
      const result = chunkContractPages(pages);
      expect(result.skippedPages).toHaveLength(2);
      expect(result.skippedPages[0].pageNumber).toBe(1);
      expect(result.skippedPages[0].reason).toBe('หน้าปกสัญญา');
      expect(result.analyzedPages).toBe(2);
    });

    it('splits long text into multiple chunks', () => {
      // Create a page with 7000 chars (should produce ~3 chunks)
      const longText = 'นายจ้างตกลงจ่ายค่าจ้าง '.repeat(300);
      const pages = [makePage(1, longText)];
      const result = chunkContractPages(pages);
      expect(result.totalChunks).toBeGreaterThan(1);
      // Each chunk should be roughly 3000 chars
      for (const chunk of result.chunks) {
        expect(chunk.charCount).toBeLessThanOrEqual(3500);
        expect(chunk.charCount).toBeGreaterThan(100);
      }
    });

    it('preserves page range in chunks', () => {
      const pages = [
        makePage(3, 'ข้อ 1 เนื้อหาสัญญา '),
        makePage(4, 'ข้อ 2 เนื้อหาต่อ '),
        makePage(5, 'ข้อ 3 สิ้นสุด'),
      ];
      const result = chunkContractPages(pages);
      expect(result.chunks.length).toBeGreaterThanOrEqual(1);
      const firstChunk = result.chunks[0];
      expect(firstChunk.pageRange).toContain('หน้า 3');
    });

    it('handles multiple pages that merge into one chunk', () => {
      const pages = [
        makePage(1, 'ข้อ 1 สั้นๆ'),
        makePage(2, 'ข้อ 2 สั้นๆ'),
        makePage(3, 'ข้อ 3 สั้นๆ'),
      ];
      const result = chunkContractPages(pages);
      expect(result.totalChunks).toBe(1);
      expect(result.chunks[0].text).toContain('ข้อ 1');
      expect(result.chunks[0].text).toContain('ข้อ 2');
      expect(result.chunks[0].text).toContain('ข้อ 3');
    });

    it('respects paragraph boundaries when splitting', () => {
      // Create text with clear paragraph breaks
      const para1 = 'ข้อ 1 '.repeat(100); // ~500 chars
      const para2 = 'ข้อ 2 '.repeat(100); // ~500 chars
      const para3 = 'ข้อ 3 '.repeat(1000); // ~5000 chars
      const text = `${para1}\n\n${para2}\n\n${para3}`;
      const pages = [makePage(1, text)];
      const result = chunkContractPages(pages);

      // Should produce multiple chunks
      expect(result.totalChunks).toBeGreaterThan(1);
      // Each chunk should be ≤3500 chars
      for (const chunk of result.chunks) {
        expect(chunk.charCount).toBeLessThanOrEqual(3500);
      }
    });
  });

  describe('formatChunkingSummary()', () => {
    it('formats basic summary', () => {
      const result = chunkContractPages([makePage(1, 'สัญญาจ้าง')]);
      const summary = formatChunkingSummary(result);
      expect(summary).toContain('ส่วน');
      expect(summary).toContain('ตัวอักษร');
    });

    it('includes skipped pages in summary', () => {
      const pages = [
        makePage(1, 'หน้าปก', true, 'หน้าปกสัญญา'),
        makePage(2, 'เนื้อหาสัญญาจ้าง'),
      ];
      const result = chunkContractPages(pages);
      const summary = formatChunkingSummary(result);
      expect(summary).toContain('ข้าม');
      expect(summary).toContain('หน้าปกสัญญา');
    });

    it('does not include skipped section when no pages skipped', () => {
      const result = chunkContractPages([makePage(1, 'เนื้อหาสัญญา')]);
      const summary = formatChunkingSummary(result);
      expect(summary).not.toContain('ข้าม');
    });
  });
});
