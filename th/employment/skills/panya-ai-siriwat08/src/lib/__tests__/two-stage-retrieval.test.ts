// Tests for src/lib/two-stage-retrieval.ts — Two-Stage Retrieval (REC-006)
import { describe, it, expect } from 'vitest';
import {
  classifyQuestion,
  getCategoryFilters,
  CATEGORIES,
  type LegalCategory,
} from '../two-stage-retrieval';

describe('Two-Stage Retrieval (REC-006)', () => {
  describe('classifyQuestion()', () => {
    it('classifies labor questions correctly', () => {
      const result = classifyQuestion('นายจ้างเลิกจ้างลูกจ้างโดยไม่จ่ายค่าชดเชย ต้องทำอย่างไร');
      expect(result.category).toBe('labor');
      expect(result.categoryCode).toBe('A');
      expect(result.confidence).toBeGreaterThan(0.1);
      expect(result.matchedKeywords.length).toBeGreaterThan(0);
      expect(result.matchedKeywords).toContain('เลิกจ้าง');
      expect(result.matchedKeywords).toContain('ค่าชดเชย');
      expect(result.matchedKeywords).toContain('ลูกจ้าง');
      expect(result.matchedKeywords).toContain('นายจ้าง');
    });

    it('classifies wage questions as labor', () => {
      const result = classifyQuestion('ค่าจ้างขั้นต่ำวันละกี่บาท และค่าล่วงเวลาคิดอย่างไร');
      expect(result.category).toBe('labor');
      expect(result.matchedKeywords).toContain('ค่าจ้าง');
      expect(result.matchedKeywords).toContain('ค่าล่วงเวลา');
    });

    it('classifies leave questions as labor', () => {
      const result = classifyQuestion('ลูกจ้างลาป่วยได้กี่วัน และลาคลอดบุตรได้กี่วัน');
      expect(result.category).toBe('labor');
      expect(result.matchedKeywords).toContain('ลาป่วย');
      expect(result.matchedKeywords).toContain('ลาคลอด');
    });

    it('classifies criminal questions correctly', () => {
      const result = classifyQuestion('การกระทำความผิดอาญาเรื่องคอมพิวเตอร์ มีโทษอย่างไร');
      expect(result.category).toBe('criminal');
      expect(result.categoryCode).toBe('B');
      expect(result.matchedKeywords).toContain('อาญา');
      expect(result.matchedKeywords).toContain('คอมพิวเตอร์');
    });

    it('classifies civil/contract questions correctly', () => {
      const result = classifyQuestion('สัญญากู้ยืมเงิน และการค้ำประกัน ตามป.พ.พ. มีผลอย่างไร');
      expect(result.category).toBe('civil');
      expect(result.categoryCode).toBe('C');
      expect(result.matchedKeywords).toContain('สัญญา');
      expect(result.matchedKeywords).toContain('ป.พ.พ.');
      expect(result.matchedKeywords).toContain('กู้ยืม');
      expect(result.matchedKeywords).toContain('ค้ำประกัน');
    });

    it('classifies tax questions correctly', () => {
      const result = classifyQuestion('อัตราภาษีมูลค่าเพิ่ม VAT และการยื่นภ.ง.ด.');
      expect(result.category).toBe('tax');
      expect(result.categoryCode).toBe('D');
    });

    it('classifies business/corporate questions correctly', () => {
      const result = classifyQuestion('การจัดตั้งบริษัทมหาชน และการออกหลักทรัพย์ในตลาดทุน');
      expect(result.category).toBe('business');
      expect(result.categoryCode).toBe('E');
    });

    it('returns "all" for ambiguous or short questions', () => {
      const result = classifyQuestion('สวัสดีครับ');
      expect(result.category).toBe('all');
      expect(result.categoryCode).toBe('');
      expect(result.confidence).toBeLessThan(0.1);
    });

    it('returns "all" for empty question', () => {
      const result = classifyQuestion('');
      expect(result.category).toBe('all');
      expect(result.confidence).toBe(0);
    });

    it('returns "all" for null/undefined question', () => {
      expect(classifyQuestion(null as unknown as string).category).toBe('all');
      expect(classifyQuestion(undefined as unknown as string).category).toBe('all');
    });

    it('handles English keywords', () => {
      const result = classifyQuestion('What is the minimum wage and overtime rate?');
      expect(result.category).toBe('labor');
      expect(result.matchedKeywords).toContain('wage');
      expect(result.matchedKeywords).toContain('overtime');
    });

    it('handles mixed Thai + English', () => {
      const result = classifyQuestion('employee ลาออก ต้องจ่าย severance ไหม');
      expect(result.category).toBe('labor');
      expect(result.matchedKeywords).toContain('employee');
      expect(result.matchedKeywords).toContain('severance');
    });

    it('returns allScores for all categories', () => {
      const result = classifyQuestion('เลิกจ้างลูกจ้าง');
      expect(result.allScores).toBeDefined();
      expect(result.allScores.labor).toBeGreaterThan(0);
      expect(result.allScores.criminal).toBe(0);
      expect(result.allScores.civil).toBe(0);
      expect(result.allScores.tax).toBe(0);
      expect(result.allScores.business).toBe(0);
    });

    it('picks the highest-scoring category when multiple match', () => {
      // "สัญญาจ้าง" matches both 'civil' (สัญญา) and 'labor' (จ้าง, ลูกจ้าง, นายจ้าง)
      // Labor should win because it has more keyword matches
      const result = classifyQuestion('สัญญาจ้างแรงงาน นายจ้างลูกจ้าง');
      expect(result.category).toBe('labor');
      expect(result.allScores.labor).toBeGreaterThan(result.allScores.civil);
    });
  });

  describe('getCategoryFilters()', () => {
    it('returns labor filters for labor category', () => {
      const filters = getCategoryFilters('labor');
      expect(filters.lawFilter).toContain("l.category = 'labor'");
      expect(filters.judgmentFilter).toContain("j.case_type = 'แรงงาน'");
      expect(filters.regulationFilter).toContain('min_wage');
      expect(filters.regulationFilter).toContain('social_security');
    });

    it('returns criminal filters for criminal category', () => {
      const filters = getCategoryFilters('criminal');
      expect(filters.lawFilter).toContain("l.category = 'criminal'");
      expect(filters.judgmentFilter).toContain('อาญา');
    });

    it('returns civil filters for civil category (includes land)', () => {
      const filters = getCategoryFilters('civil');
      expect(filters.lawFilter).toContain("l.category = 'civil'");
      expect(filters.lawFilter).toContain("l.category = 'land'");
    });

    it('returns empty filters for "all" category (no filtering)', () => {
      const filters = getCategoryFilters('all');
      expect(filters.lawFilter).toBe('');
      expect(filters.judgmentFilter).toBe('');
      expect(filters.regulationFilter).toBe('');
    });

    it('returns empty filters for "other" category', () => {
      const filters = getCategoryFilters('other');
      expect(filters.lawFilter).toBe('');
      expect(filters.judgmentFilter).toBe('');
      expect(filters.regulationFilter).toBe('');
    });

    it('filters do not start with AND for "all" (so they can be safely omitted)', () => {
      const filters = getCategoryFilters('all');
      expect(filters.lawFilter.startsWith('AND')).toBe(false);
    });

    it('filters start with AND for specific categories (so they can be appended to WHERE)', () => {
      const filters = getCategoryFilters('labor');
      expect(filters.lawFilter.startsWith('AND')).toBe(true);
      expect(filters.judgmentFilter.startsWith('AND')).toBe(true);
    });
  });

  describe('CATEGORIES constant', () => {
    it('has 5 categories (A-E)', () => {
      expect(CATEGORIES).toHaveLength(5);
      const codes = CATEGORIES.map(c => c.code);
      expect(codes).toEqual(['A', 'B', 'C', 'D', 'E']);
    });

    it('each category has required fields', () => {
      for (const cat of CATEGORIES) {
        expect(cat.code).toBeDefined();
        expect(cat.name).toBeDefined();
        expect(cat.thaiName).toBeDefined();
        expect(cat.keywords).toBeDefined();
        expect(cat.keywords.length).toBeGreaterThan(5);
      }
    });

    it('labor category has the most keywords (most common use case)', () => {
      const labor = CATEGORIES.find(c => c.name === 'labor');
      expect(labor).toBeDefined();
      expect(labor!.keywords.length).toBeGreaterThan(30);
    });
  });
});
