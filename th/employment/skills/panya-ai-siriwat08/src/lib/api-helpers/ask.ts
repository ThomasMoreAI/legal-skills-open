// Shared API helper functions for ask route — extracted for testability.
import { PERSONAS, type PersonaId, type Persona } from '@/lib/persona';

export interface AskBody {
  question: string;
  history?: { role: 'user' | 'assistant'; content: string }[];
  laborOnly?: boolean;
  persona?: PersonaId | null;
}

/** Parse and validate the request body. */
export function parseRequestBody(body: AskBody): { question: string } | { error: string; status: number } {
  const question = (body.question || '').trim();
  if (!question) return { error: 'question required', status: 400 };
  if (question.length > 2000) return { error: 'too long', status: 400 };
  return { question };
}

/** Resolve persona from request body. Returns null if not set or invalid. */
export function resolvePersona(body: AskBody): { id: PersonaId; persona: Persona } | null {
  const personaId = body.persona && body.persona in PERSONAS ? body.persona : null;
  if (!personaId) return null;
  return { id: personaId, persona: PERSONAS[personaId] };
}

interface SubSkill {
  name: string;
  keywords: string[];
  topK: number;
  laborOnly: boolean;
}

/** Select the best matching sub-skill based on keyword scoring. */
export function selectSkill(question: string, SKILLS: SubSkill[]): SubSkill {
  const q = question.toLowerCase();
  let bestSkill = SKILLS.at(-1) as SubSkill;
  let bestScore = 0;

  for (const skill of SKILLS) {
    if (skill.keywords.length === 0) continue;
    let score = 0;
    for (const kw of skill.keywords) {
      if (q.includes(kw.toLowerCase())) {
        score += kw.length > 3 ? 2 : 1;
      }
    }
    if (score > bestScore) {
      bestScore = score;
      bestSkill = skill;
    }
  }

  if (bestScore === 0) {
    bestSkill = SKILLS.at(-1) as SubSkill;
  }

  return bestSkill;
}
