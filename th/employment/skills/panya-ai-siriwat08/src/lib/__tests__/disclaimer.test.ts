// Tests for src/lib/disclaimer.ts — Disclaimer Layer (REC-005)
import { describe, it, expect } from 'vitest';
import {
  DISCLAIMER_TEXT,
  DISCLAIMER_SHORT,
  withDisclaimer,
  shouldShowDisclaimer,
} from '../disclaimer';

describe('Disclaimer Layer (REC-005)', () => {
  describe('DISCLAIMER_TEXT', () => {
    it('contains the key legal warning phrases', () => {
      expect(DISCLAIMER_TEXT).toContain('คำเตือนทางกฎหมาย');
      expect(DISCLAIMER_TEXT).toContain('ไม่ใช่คำแนะนำทางกฎหมายอย่างเป็นทางการ');
      expect(DISCLAIMER_TEXT).toContain('ปรึกษาทนายความ');
      expect(DISCLAIMER_TEXT).toContain('ตัวบทกฎหมายฉบับเต็ม');
    });

    it('mentions that laws may change (legal currency warning)', () => {
      expect(DISCLAIMER_TEXT).toContain('แก้ไขเพิ่มเติม');
      expect(DISCLAIMER_TEXT).toContain('คำพิพากษาฎีกาใหม่');
    });

    it('starts with a separator so it visually separates from the answer', () => {
      expect(DISCLAIMER_TEXT.startsWith('\n\n---\n\n')).toBe(true);
    });
  });

  describe('DISCLAIMER_SHORT', () => {
    it('is a concise version suitable for chat UI badges', () => {
      expect(DISCLAIMER_SHORT.length).toBeLessThan(DISCLAIMER_TEXT.length);
      expect(DISCLAIMER_SHORT).toContain('ข้อมูลเพื่อการอ้างอิงเท่านั้น');
      expect(DISCLAIMER_SHORT).toContain('ปรึกษาทนายความ');
    });

    it('starts with warning emoji for visual prominence', () => {
      expect(DISCLAIMER_SHORT.startsWith('⚠️')).toBe(true);
    });
  });

  describe('withDisclaimer()', () => {
    it('appends DISCLAIMER_TEXT to the answer field', () => {
      const input = { answer: 'นายจ้างต้องจ่ายค่าชดเชยตามมาตรา 118' };
      const result = withDisclaimer(input);
      expect(result.answer).toBe(input.answer + DISCLAIMER_TEXT);
    });

    it('adds a top-level disclaimer field with the short version', () => {
      const input = { answer: 'some answer', citations: [] };
      const result = withDisclaimer(input);
      expect(result.disclaimer).toBe(DISCLAIMER_SHORT);
    });

    it('preserves other fields in the response object', () => {
      const input = {
        answer: 'test',
        citations: [{ index: 1, type: 'section' as const, id: 1, label: 'L1 ม.118', ref: '118', snippet: '...', url: '/' }],
        retrievedChunks: 5,
        skill: 'legal-qa',
        persona: 'hr',
      };
      const result = withDisclaimer(input);
      expect(result.citations).toEqual(input.citations);
      expect(result.retrievedChunks).toBe(5);
      expect(result.skill).toBe('legal-qa');
      expect(result.persona).toBe('hr');
    });

    it('handles empty answer gracefully', () => {
      const input = { answer: '' };
      const result = withDisclaimer(input);
      // Empty answer + disclaimer text (since the conditional appends only if answer exists)
      expect(result.answer).toBe('');
      expect(result.disclaimer).toBe(DISCLAIMER_SHORT);
    });

    it('handles missing answer field gracefully', () => {
      const input = { citations: [] };
      const result = withDisclaimer(input);
      expect(result.answer).toBeUndefined();
      expect(result.disclaimer).toBe(DISCLAIMER_SHORT);
    });

    it('does not mutate the original input object', () => {
      const input = { answer: 'original' };
      const result = withDisclaimer(input);
      expect(input.answer).toBe('original'); // unchanged
      expect(result.answer).toBe('original' + DISCLAIMER_TEXT);
    });
  });

  describe('shouldShowDisclaimer()', () => {
    it('returns true for legal answers with มาตรา', () => {
      expect(shouldShowDisclaimer('ตามมาตรา 118 นายจ้างต้องจ่ายค่าชดเชย')).toBe(true);
    });

    it('returns true for answers mentioning พ.ร.บ.', () => {
      expect(shouldShowDisclaimer('พ.ร.บ.คุ้มครองแรงงาน พ.ศ. 2541')).toBe(true);
    });

    it('returns true for answers about เลิกจ้าง', () => {
      expect(shouldShowDisclaimer('การเลิกจ้างต้องบอกล่วงหน้า')).toBe(true);
    });

    it('returns true for answers citing ฎีกา', () => {
      expect(shouldShowDisclaimer('ตามคำพิพากษาฎีกาที่ 587/2563')).toBe(true);
    });

    it('returns false for short non-legal responses', () => {
      expect(shouldShowDisclaimer('สวัสดี')).toBe(false);
      expect(shouldShowDisclaimer('ขอบคุณครับ')).toBe(false);
    });

    it('returns false for empty or very short answers', () => {
      expect(shouldShowDisclaimer('')).toBe(false);
      expect(shouldShowDisclaimer('hi')).toBe(false);
    });

    it('returns false for non-legal technical content', () => {
      expect(shouldShowDisclaimer('The database connection failed due to timeout. Please check your network settings and try again.')).toBe(false);
    });
  });
});
