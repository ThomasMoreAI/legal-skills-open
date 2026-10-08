import { describe, it, expect } from 'vitest';
import { buildSectionFilter, mapLawToList } from '@/lib/api-helpers/laws';

describe('buildSectionFilter', () => {
  it('should return undefined for empty query', () => {
    expect(buildSectionFilter(undefined)).toBeUndefined();
    expect(buildSectionFilter('')).toBeUndefined();
  });

  it('should return OR clause for non-empty query', () => {
    const result = buildSectionFilter('ค่าจ้าง');
    expect(result).toBeDefined();
    expect(result!.OR).toHaveLength(3);
    expect(result!.OR[0]).toEqual({ sectionText: { contains: 'ค่าจ้าง' } });
    expect(result!.OR[1]).toEqual({ sectionNumber: { contains: 'ค่าจ้าง' } });
    expect(result!.OR[2]).toEqual({ sectionNumberThai: { contains: 'ค่าจ้าง' } });
  });

  it('should handle English keywords', () => {
    const result = buildSectionFilter('overtime');
    expect(result!.OR[0]).toEqual({ sectionText: { contains: 'overtime' } });
  });
});

describe('mapLawToList', () => {
  it('should map law with all fields correctly', () => {
    const mockLaw = {
      lawId: 1, lawCode: 'A1', title: 'พ.ร.บ.คุ้มครองแรงงาน 2541',
      year: '2541', category: 'labor', status: 'complete',
      sourceUrl: 'https://example.com',
      _count: { sections: 182 },
      sections: [{ sectionId: 1 }, { sectionId: 2 }],
    };
    const result = mapLawToList(mockLaw);
    expect(result.lawId).toBe(1);
    expect(result.lawCode).toBe('A1');
    expect(result.title).toBe('พ.ร.บ.คุ้มครองแรงงาน 2541');
    expect(result.lawNameTh).toBe('พ.ร.บ.คุ้มครองแรงงาน 2541');
    expect(result.lawNameEn).toBeNull();
    expect(result.isLaborLaw).toBe(1);
    expect(result.sectionCount).toBe(182);
    expect(result.laborSectionCount).toBe(2);
  });

  it('should set isLaborLaw=0 for non-labor category', () => {
    const mockLaw = {
      lawId: 5, lawCode: 'C1', title: 'ป.พ.พ.', year: '2535',
      category: 'civil', status: 'complete', sourceUrl: null,
      _count: { sections: 100 }, sections: [],
    };
    const result = mapLawToList(mockLaw);
    expect(result.isLaborLaw).toBe(0);
    expect(result.laborSectionCount).toBe(0);
  });
});
