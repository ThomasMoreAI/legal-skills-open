'use client';

import { useEffect, useState } from 'react';
import { PERSONAS, getPersona, type PersonaId } from '@/lib/persona';

/**
 * usePersona — React hook that subscribes to persona changes.
 * Returns the current Persona object (or null if not set) + the raw id.
 */
export function usePersona() {
  const [personaId, setPersonaId] = useState<PersonaId | null>(null);

  useEffect(() => {
    setPersonaId(getPersona());
    const onChange = () => setPersonaId(getPersona());
    window.addEventListener('panya-persona-changed', onChange);
    window.addEventListener('storage', onChange);
    return () => {
      window.removeEventListener('panya-persona-changed', onChange);
      window.removeEventListener('storage', onChange);
    };
  }, []);

  const persona = personaId ? PERSONAS[personaId] : null;
  return { persona, personaId };
}
