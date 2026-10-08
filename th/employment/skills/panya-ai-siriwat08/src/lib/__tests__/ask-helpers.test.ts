import { describe, it, expect } from 'vitest';
import { parseRequestBody, resolvePersona, selectSkill, type AskBody } from '@/lib/api-helpers/ask';

const MOCK_SKILLS = [
  { name: 'contract-review', keywords: ['สัญญา', 'clause'], topK: 12, laborOnly: true },
  { name: 'risk-assessment', keywords: ['เสี่ยง', 'ฟ้อง'], topK: 10, laborOnly: true },
  { name: 'document-drafting', keywords: ['ร่าง', 'เขียน'], topK: 8, laborOnly: true },
  { name: 'legal-qa', keywords: [], topK: 10, laborOnly: true },
];

describe('parseRequestBody', () => {
  it('should return question for valid input', () => {
    const result = parseRequestBody({ question: 'ค่าจ้าง OT คำนวณอย่างไร?' });
    expect('question' in result).toBe(true);
    if ('question' in result) expect(result.question).toBe('ค่าจ้าง OT คำนวณอย่างไร?');
  });

  it('should return error for empty question', () => {
    const result = parseRequestBody({ question: '' });
    expect('error' in result).toBe(true);
    if ('error' in result) { expect(result.error).toBe('question required'); expect(result.status).toBe(400); }
  });

  it('should return error for whitespace-only question', () => {
    const result = parseRequestBody({ question: '   ' });
    expect('error' in result).toBe(true);
  });

  it('should return error for question over 2000 chars', () => {
    const result = parseRequestBody({ question: 'a'.repeat(2001) });
    expect('error' in result).toBe(true);
    if ('error' in result) expect(result.error).toBe('too long');
  });

  it('should accept question exactly 2000 chars', () => {
    const result = parseRequestBody({ question: 'a'.repeat(2000) });
    expect('question' in result).toBe(true);
  });
});

describe('resolvePersona', () => {
  it('should return null when persona is not set', () => {
    expect(resolvePersona({} as AskBody)).toBeNull();
  });

  it('should return null for invalid persona id', () => {
    expect(resolvePersona({ persona: 'invalid' as any } as AskBody)).toBeNull();
  });

  it('should return persona for valid "hr"', () => {
    const result = resolvePersona({ persona: 'hr' } as AskBody);
    expect(result).not.toBeNull();
    expect(result!.id).toBe('hr');
    expect(result!.persona.laborOnly).toBe(true);
  });

  it('should return persona for valid "legal"', () => {
    const result = resolvePersona({ persona: 'legal' } as AskBody);
    expect(result!.id).toBe('legal');
    expect(result!.persona.laborOnly).toBe(false);
  });

  it('should return persona for valid "owner"', () => {
    const result = resolvePersona({ persona: 'owner' } as AskBody);
    expect(result!.id).toBe('owner');
  });

  it('should return null for null persona', () => {
    expect(resolvePersona({ persona: null } as AskBody)).toBeNull();
  });
});

describe('selectSkill', () => {
  it('should return legal-qa (default) when no keywords match', () => {
    const result = selectSkill('สวัสดีครับ', MOCK_SKILLS);
    expect(result.name).toBe('legal-qa');
  });

  it('should return contract-review for "สัญญา" keyword', () => {
    const result = selectSkill('วิเคราะห์สัญญาจ้างนี้', MOCK_SKILLS);
    expect(result.name).toBe('contract-review');
  });

  it('should return risk-assessment for "เสี่ยง" keyword', () => {
    const result = selectSkill('ประเมินความเสี่ยง', MOCK_SKILLS);
    expect(result.name).toBe('risk-assessment');
  });

  it('should return document-drafting for "ร่าง" keyword', () => {
    const result = selectSkill('ร่างหนังสือเตือน', MOCK_SKILLS);
    expect(result.name).toBe('document-drafting');
  });

  it('should weight longer keywords higher', () => {
    const result = selectSkill('ร่างสัญญาจ้าง', MOCK_SKILLS);
    expect(result.name).toBe('contract-review');
  });
});
