import { describe, it, expect } from 'vitest';
import { cn } from '@/lib/utils';

describe('cn (className merge utility)', () => {
  it('should merge multiple class names', () => {
    expect(cn('foo', 'bar')).toBe('foo bar');
  });

  it('should handle conditional classes', () => {
    expect(cn('base', true && 'active', false && 'inactive')).toBe('base active');
  });

  it('should handle undefined and null', () => {
    expect(cn('base', undefined, null, 'end')).toBe('base end');
  });

  it('should deduplicate tailwind classes (twMerge)', () => {
    expect(cn('px-2', 'px-4')).toBe('px-4');
  });

  it('should merge conflicting and non-conflicting classes', () => {
    expect(cn('text-sm', 'text-red-500', 'text-lg')).toBe('text-red-500 text-lg');
  });

  it('should handle empty input', () => {
    expect(cn()).toBe('');
  });
});
