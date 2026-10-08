import { describe, it, expect } from 'vitest';
import { buildFtsQuery, shouldSearch, mapSectionRow, aggregateLawHit } from '@/lib/api-helpers/search';

describe('buildFtsQuery', () => {
  it('should return empty string for empty input', () => {
    expect(buildFtsQuery('')).toBe('');
    expect(buildFtsQuery('   ')).toBe('');
  });

  it('should wrap single token in quotes', () => {
    expect(buildFtsQuery('ค่าจ้าง')).toBe('"ค่าจ้าง"');
  });

  it('should join multiple tokens with OR', () => {
    expect(buildFtsQuery('ค่าจ้าง ล่วงเวลา')).toBe('"ค่าจ้าง" OR "ล่วงเวลา"');
  });

  it('should strip quotes from input', () => {
    expect(buildFtsQuery('"ค่าจ้าง"')).toBe('"ค่าจ้าง"');
    expect(buildFtsQuery("'ค่าจ้าง'")).toBe('"ค่าจ้าง"');
  });

  it('should handle mixed Thai and English', () => {
    expect(buildFtsQuery('ค่าจ้าง overtime')).toBe('"ค่าจ้าง" OR "overtime"');
  });

  it('should handle multiple spaces between tokens', () => {
    expect(buildFtsQuery('ค่าจ้าง    ล่วงเวลา')).toBe('"ค่าจ้าง" OR "ล่วงเวลา"');
  });
});

describe('shouldSearch', () => {
  it('should return true when type is "all"', () => {
    expect(shouldSearch('all', 'sections')).toBe(true);
    expect(shouldSearch('all', 'judgments')).toBe(true);
  });

  it('should return true when type matches target', () => {
    expect(shouldSearch('sections', 'sections')).toBe(true);
  });

  it('should return false when type does not match target', () => {
    expect(shouldSearch('sections', 'judgments')).toBe(false);
  });
});

describe('mapSectionRow', () => {
  it('should map section row correctly', () => {
    const row = {
      section_id: 1, law_id: 5, section_number: '118', section_number_thai: 'มาตรา ๑๑๘',
      section_text: 'นายจ้างต้องจ่ายค่าชดเชย', is_labor_related: 1,
      law_title: 'พ.ร.บ.แรงงาน', law_code: 'A1', category: 'labor',
    };
    const result = mapSectionRow(row);
    expect(result.id).toBe(1);
    expect(result.lawId).toBe(5);
    expect(result.sectionNumber).toBe('118');
    expect(result.articleKey).toBe('มาตรา ๑๑๘');
    expect(result.isLaborRelated).toBe(true);
    expect(result.isLaborLaw).toBe(true);
  });

  it('should use section_number for articleKey when thai is null', () => {
    const row = {
      section_id: 2, law_id: 5, section_number: '20', section_number_thai: null,
      section_text: 'text', is_labor_related: 0,
      law_title: 'law', law_code: 'X1', category: 'civil',
    };
    const result = mapSectionRow(row);
    expect(result.articleKey).toBe('มาตรา 20');
  });
});

describe('aggregateLawHit', () => {
  it('should create new entry for unseen law', () => {
    const map = new Map<number, any>();
    aggregateLawHit(map, { lawId: 1, lawNameTh: 'Law A', lawTitle: 'Law A', category: 'labor', isLaborLaw: true });
    expect(map.has(1)).toBe(true);
    expect(map.get(1).hitCount).toBe(1);
  });

  it('should increment hitCount for existing law', () => {
    const map = new Map<number, any>();
    aggregateLawHit(map, { lawId: 1, lawNameTh: 'Law A', lawTitle: 'Law A', category: 'labor', isLaborLaw: true });
    aggregateLawHit(map, { lawId: 1, lawNameTh: 'Law A', lawTitle: 'Law A', category: 'labor', isLaborLaw: true });
    expect(map.get(1).hitCount).toBe(2);
  });

  it('should track multiple laws independently', () => {
    const map = new Map<number, any>();
    aggregateLawHit(map, { lawId: 1, lawNameTh: 'A', lawTitle: 'A', category: 'labor', isLaborLaw: true });
    aggregateLawHit(map, { lawId: 2, lawNameTh: 'B', lawTitle: 'B', category: 'civil', isLaborLaw: false });
    aggregateLawHit(map, { lawId: 1, lawNameTh: 'A', lawTitle: 'A', category: 'labor', isLaborLaw: true });
    expect(map.size).toBe(2);
    expect(map.get(1).hitCount).toBe(2);
    expect(map.get(2).hitCount).toBe(1);
  });
});
