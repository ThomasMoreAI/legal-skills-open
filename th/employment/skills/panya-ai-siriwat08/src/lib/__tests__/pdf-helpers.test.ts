import { describe, it, expect } from 'vitest';
import { markdownToHtml, fillEmployeeName, fillPosition, fillStartDate, fillSalary } from '@/lib/api-helpers/pdf';

describe('markdownToHtml', () => {
  it('should convert headers', () => {
    expect(markdownToHtml('# Title')).toContain('<h1>Title</h1>');
    expect(markdownToHtml('## Section')).toContain('<h2>Section</h2>');
    expect(markdownToHtml('### Sub')).toContain('<h3>Sub</h3>');
  });

  it('should convert bold and italic', () => {
    expect(markdownToHtml('**bold**')).toContain('<strong>bold</strong>');
    expect(markdownToHtml('*italic*')).toContain('<em>italic</em>');
  });

  it('should convert lists', () => {
    const result = markdownToHtml('- item 1\n- item 2');
    expect(result).toContain('<li>item 1</li>');
    expect(result).toContain('<li>item 2</li>');
    expect(result).toContain('<ul>');
  });

  it('should convert horizontal rules', () => {
    expect(markdownToHtml('---')).toContain('<hr/>');
  });

  it('should escape HTML', () => {
    expect(markdownToHtml('<script>')).toContain('&lt;script&gt;');
    expect(markdownToHtml('a & b')).toContain('a &amp; b');
  });

  it('should wrap in paragraph tags', () => {
    expect(markdownToHtml('text')).toMatch(/^<p>/);
    expect(markdownToHtml('text')).toMatch(/<\/p>$/);
  });
});

describe('fillEmployeeName', () => {
  it('should return unchanged if no name provided', () => {
    expect(fillEmployeeName('___', '')).toBe('___');
  });

  it('should fill first 5 blank fields', () => {
    const html = '___ ___ ___ ___ ___ ___';
    const result = fillEmployeeName(html, 'สมชาย');
    const filled = (result.match(/สมชาย/g) || []).length;
    expect(filled).toBe(5);
  });

  it('should not fill more than 5 fields', () => {
    const html = '___ ___ ___ ___ ___ ___ ___';
    const result = fillEmployeeName(html, 'สมชาย');
    const filled = (result.match(/สมชาย/g) || []).length;
    expect(filled).toBe(5);
  });
});

describe('fillPosition', () => {
  it('should return unchanged if no position provided', () => {
    expect(fillPosition('ตำแหน่ง: ___', '')).toBe('ตำแหน่ง: ___');
  });

  it('should fill first 2 position fields', () => {
    const html = 'ตำแหน่ง: ___ และ ตำแหน่ง: ___ และ ตำแหน่ง: ___';
    const result = fillPosition(html, 'พนักงานขับรถ');
    const filled = (result.match(/พนักงานขับรถ/g) || []).length;
    expect(filled).toBe(2);
  });
});

describe('fillStartDate', () => {
  it('should return unchanged if no date provided', () => {
    expect(fillStartDate('วันที่ __ เดือน __ พ.ศ. __', '')).toBe('วันที่ __ เดือน __ พ.ศ. __');
  });

  it('should fill date field', () => {
    const html = 'วันที่ __ เดือน __ พ.ศ. __';
    const result = fillStartDate(html, '1 มกราคม');
    expect(result).toContain('1 มกราคม');
  });
});

describe('fillSalary', () => {
  it('should return unchanged if no salary provided', () => {
    expect(fillSalary('500 บาท', '')).toBe('500 บาท');
  });

  it('should replace first 2 amounts under 1000', () => {
    const html = 'ค่าจ้าง 500 บาท และ 800 บาท และ 200 บาท';
    const result = fillSalary(html, '15000');
    expect(result).toContain('15000');
    expect(result).not.toContain('500 บาท');
  });

  it('should not replace amounts >= 1000', () => {
    const html = 'เงินเดือน 5000 บาท';
    const result = fillSalary(html, '15000');
    expect(result).toContain('5000 บาท');
    expect(result).not.toContain('15000');
  });

  it('should only replace first 2 matches', () => {
    const html = '100 บาท 200 บาท 300 บาท 400 บาท';
    const result = fillSalary(html, '999');
    const filled = (result.match(/999/g) || []).length;
    expect(filled).toBe(2);
  });
});
