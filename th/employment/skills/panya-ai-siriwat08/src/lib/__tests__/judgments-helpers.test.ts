import { describe, it, expect } from 'vitest';
import { parseJsonArray, resolveCategoryFilter, mapJudgmentToList } from '@/lib/api-helpers/judgments';

describe('parseJsonArray', () => {
  it('should return empty array for null', () => {
    expect(parseJsonArray(null)).toEqual([]);
  });

  it('should return empty array for empty string', () => {
    expect(parseJsonArray('')).toEqual([]);
  });

  it('should parse valid JSON array', () => {
    expect(parseJsonArray('["a", "b", "c"]')).toEqual(['a', 'b', 'c']);
  });

  it('should filter falsy values from array', () => {
    expect(parseJsonArray('["a", "", null, "b", false, "c"]')).toEqual(['a', 'b', 'c']);
  });

  it('should return empty array for non-array JSON', () => {
    expect(parseJsonArray('"hello"')).toEqual([]);
    expect(parseJsonArray('{"key": "value"}')).toEqual([]);
    expect(parseJsonArray('42')).toEqual([]);
  });

  it('should return empty array for invalid JSON', () => {
    expect(parseJsonArray('{invalid}')).toEqual([]);
    expect(parseJsonArray('not json')).toEqual([]);
  });

  it('should handle array with Thai text', () => {
    expect(parseJsonArray('["เลิกจ้าง", "ค่าชดเชย"]')).toEqual(['เลิกจ้าง', 'ค่าชดเชย']);
  });
});

describe('resolveCategoryFilter', () => {
  it('should return undefined for null', () => {
    expect(resolveCategoryFilter(null)).toBeUndefined();
  });

  it('should return Thai for "labor"', () => {
    expect(resolveCategoryFilter('labor')).toBe('แรงงาน');
  });

  it('should return Thai for "criminal"', () => {
    expect(resolveCategoryFilter('criminal')).toBe('อาญา');
  });

  it('should pass through unknown categories', () => {
    expect(resolveCategoryFilter('แพ่ง')).toBe('แพ่ง');
    expect(resolveCategoryFilter('custom')).toBe('custom');
  });
});

describe('mapJudgmentToList', () => {
  it('should map judgment with all fields', () => {
    const mock = {
      judgmentId: 10, dekaNo: '1856/2561', year: '2561',
      caseType: 'แรงงาน', caseTypeGroup: 'คดีธุรกิจและเศรษฐกิจ',
      topic: 'เลิกจ้างไม่เป็นธรรม', topics: '["เลิกจ้าง","ค่าชดเชย"]',
      lawsCited: '["พ.ร.บ.แรงงาน มาตรา 118"]',
      fact: 'ข้อเท็จจริง', ruling: 'คำวินิจฉัย',
      sourceUrl: 'https://example.com', note: 'หมายเหตุ',
      source: { sourceName: 'ศาลฎีกา' },
    };
    const result = mapJudgmentToList(mock);
    expect(result.judgmentId).toBe(10);
    expect(result.caseNumber).toBe('1856/2561');
    expect(result.caseYear).toBe('2561');
    expect(result.topicsList).toEqual(['เลิกจ้าง', 'ค่าชดเชย']);
    expect(result.lawsCitedList).toEqual(['พ.ร.บ.แรงงาน มาตรา 118']);
    expect(result.sourceName).toBe('ศาลฎีกา');
  });

  it('should handle null source', () => {
    const mock = { judgmentId: 1, dekaNo: null, year: null, caseType: null, caseTypeGroup: null,
      topic: null, topics: null, lawsCited: null, fact: null, ruling: null,
      sourceUrl: null, note: null, source: null };
    const result = mapJudgmentToList(mock);
    expect(result.sourceName).toBeNull();
    expect(result.topicsList).toEqual([]);
  });
});
