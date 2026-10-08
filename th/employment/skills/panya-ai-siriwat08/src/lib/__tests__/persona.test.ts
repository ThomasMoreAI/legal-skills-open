import { describe, it, expect, beforeEach, vi } from 'vitest';
import { PERSONAS, type PersonaId } from '@/lib/persona';

// Mock localStorage
const localStorageMock = (() => {
  let store: Record<string, string> = {};
  return {
    getItem: (key: string) => store[key] || null,
    setItem: (key: string, value: string) => { store[key] = value; },
    removeItem: (key: string) => { delete store[key]; },
    clear: () => { store = {}; },
  };
})();

Object.defineProperty(globalThis, 'localStorage', { value: localStorageMock });
Object.defineProperty(globalThis, 'window', {
  value: {
    ...globalThis,
    localStorage: localStorageMock,
    dispatchEvent: vi.fn(),
  },
  writable: true,
});

describe('PERSONAS', () => {
  it('should have exactly 3 personas: hr, legal, owner', () => {
    const keys = Object.keys(PERSONAS);
    expect(keys).toHaveLength(3);
    expect(keys).toContain('hr');
    expect(keys).toContain('legal');
    expect(keys).toContain('owner');
  });

  it('each persona should have all required fields', () => {
    for (const [id, persona] of Object.entries(PERSONAS)) {
      expect(persona.id).toBe(id as PersonaId);
      expect(persona.label).toBeTruthy();
      expect(persona.labelEn).toBeTruthy();
      expect(persona.icon).toBeTruthy();
      expect(persona.color).toBeTruthy();
      expect(persona.description).toBeTruthy();
      expect(persona.promptPrefix).toBeTruthy();
      expect(typeof persona.laborOnly).toBe('boolean');
      expect(persona.skillPriority).toHaveLength(4);
      expect(persona.sampleQuestions.length).toBeGreaterThanOrEqual(3);
      expect(persona.quickActions.length).toBeGreaterThanOrEqual(3);
    }
  });

  it('hr persona should have laborOnly=true', () => {
    expect(PERSONAS.hr.laborOnly).toBe(true);
  });

  it('legal persona should have laborOnly=false', () => {
    expect(PERSONAS.legal.laborOnly).toBe(false);
  });

  it('owner persona should have laborOnly=true', () => {
    expect(PERSONAS.owner.laborOnly).toBe(true);
  });

  it('each persona promptPrefix should contain org name', () => {
    for (const persona of Object.values(PERSONAS)) {
      expect(persona.promptPrefix).toContain('หจก.เผ่าปัญญา ทรานสปอร์ต');
    }
  });

  it('each persona promptPrefix should contain "ความต้องการหลัก:"', () => {
    for (const persona of Object.values(PERSONAS)) {
      expect(persona.promptPrefix).toContain('ความต้องการหลัก:');
    }
  });

  it('each persona should have unique skillPriority ordering', () => {
    const priorities = Object.values(PERSONAS).map(p => p.skillPriority.join(','));
    const unique = new Set(priorities);
    expect(unique.size).toBe(3);
  });
});

describe('Persona storage helpers', () => {
  beforeEach(() => {
    localStorageMock.clear();
    vi.clearAllMocks();
  });

  it('getPersona should return null when not set', async () => {
    const { getPersona } = await import('@/lib/persona');
    expect(getPersona()).toBeNull();
  });

  it('setPersona should store persona id and dispatch event', async () => {
    const { setPersona, getPersona } = await import('@/lib/persona');
    setPersona('hr');
    expect(getPersona()).toBe('hr');
    expect(globalThis.window.dispatchEvent).toHaveBeenCalled();
  });

  it('getPersona should return null for invalid id', async () => {
    localStorageMock.setItem('panya_persona_v1', JSON.stringify({ id: 'invalid' }));
    const { getPersona } = await import('@/lib/persona');
    expect(getPersona()).toBeNull();
  });

  it('clearPersona should remove stored persona', async () => {
    const { setPersona, clearPersona, getPersona } = await import('@/lib/persona');
    setPersona('legal');
    expect(getPersona()).toBe('legal');
    clearPersona();
    expect(getPersona()).toBeNull();
  });

  it('isOnboarded should return false initially', async () => {
    const { isOnboarded } = await import('@/lib/persona');
    expect(isOnboarded()).toBe(false);
  });

  it('markOnboarded should set flag and dispatch event', async () => {
    const { markOnboarded, isOnboarded } = await import('@/lib/persona');
    markOnboarded();
    expect(isOnboarded()).toBe(true);
    expect(globalThis.window.dispatchEvent).toHaveBeenCalled();
  });
});
