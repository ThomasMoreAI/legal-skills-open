/**
 * AIDisclosure, selo "Gerado por IA" + canal de contestação (art. 20 LGPD)
 * =====================================================================
 * Skill: lgpd-compliance (Parte 3)
 * Cole em: components/transparencia/AIDisclosure.tsx
 *
 * Usar SEMPRE que o app exibir output de IA ao usuário.
 *  - Variante <AIBadge>, selo compacto inline
 *  - Variante <AICard>, card completo com modelo, disclaimer, feedback, contestação
 *
 * Cumpre:
 *  - EU AI Act Article 50 (transparência de chatbot/synthetic)
 *  - PL 2338 (Marco Legal IA, quando virar lei)
 *  - LGPD art. 20 (direito de revisão de decisão automatizada)
 */

'use client';

import { useState } from 'react';
import { Sparkles, AlertCircle, ThumbsUp, ThumbsDown, MessageSquare } from 'lucide-react';
import Link from 'next/link';

// =========================================================================
// Tipos
// =========================================================================

type AIModelo = {
  provedor: 'anthropic' | 'openai' | 'google' | 'mistral' | 'proprio' | string;
  modelo: string;
  versao?: string;
};

type AIDisclosureProps = {
  modelo: AIModelo;
  /** Indica que esta é uma decisão que afeta o usuário (art. 20 LGPD) */
  decisaoAutomatizada?: boolean;
  /** ID da decisão pra log de contestação */
  decisaoId?: string;
  /** Texto do disclaimer customizado (override do default) */
  disclaimer?: string;
};

// =========================================================================
// Variante 1: Badge compacto inline
// =========================================================================

export function AIBadge({ modelo }: { modelo: AIModelo }) {
  return (
    <span
      className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium bg-violet-50 dark:bg-violet-950/40 text-violet-700 dark:text-violet-300 border border-violet-200 dark:border-violet-900"
      title={`Conteúdo gerado por ${modelo.provedor} ${modelo.modelo}. Pode conter imprecisões.`}
    >
      <Sparkles className="h-3 w-3" />
      Gerado por IA
    </span>
  );
}

// =========================================================================
// Variante 2: Card completo
// =========================================================================

export function AIDisclosure({
  modelo,
  decisaoAutomatizada = false,
  decisaoId,
  disclaimer,
}: AIDisclosureProps) {
  const [feedback, setFeedback] = useState<'up' | 'down' | null>(null);

  const disclaimerText =
    disclaimer ??
    'Esta resposta foi gerada automaticamente e pode conter imprecisões. Confirme informações importantes em fontes oficiais.';

  return (
    <div className="mt-3 rounded-lg border border-violet-200 dark:border-violet-900 bg-violet-50/50 dark:bg-violet-950/20 p-3 text-sm">
      {/* Linha de identificação */}
      <div className="flex items-center justify-between flex-wrap gap-2">
        <div className="flex items-center gap-2 text-violet-700 dark:text-violet-300">
          <Sparkles className="h-4 w-4" />
          <span className="font-medium">
            Gerado por IA · {modelo.provedor} {modelo.modelo}
            {modelo.versao ? ` (${modelo.versao})` : ''}
          </span>
        </div>

        <Link
          href="/transparencia/ia"
          className="text-xs underline underline-offset-2 text-violet-600 dark:text-violet-400 hover:text-violet-900"
        >
          Como funciona?
        </Link>
      </div>

      {/* Disclaimer */}
      <div className="mt-2 flex items-start gap-2 text-violet-700 dark:text-violet-300">
        <AlertCircle className="h-4 w-4 flex-shrink-0 mt-0.5" />
        <p className="text-xs">{disclaimerText}</p>
      </div>

      {/* Feedback */}
      <div className="mt-3 flex items-center gap-2 text-xs">
        <span className="text-violet-600 dark:text-violet-400">Esta resposta foi útil?</span>
        <button
          type="button"
          onClick={() => {
            setFeedback('up');
            postFeedback({ rating: 'up', decisaoId });
          }}
          className={`p-1 rounded ${
            feedback === 'up'
              ? 'bg-violet-200 dark:bg-violet-800'
              : 'hover:bg-violet-100 dark:hover:bg-violet-900'
          }`}
          aria-label="Útil"
        >
          <ThumbsUp className="h-3.5 w-3.5" />
        </button>
        <button
          type="button"
          onClick={() => {
            setFeedback('down');
            postFeedback({ rating: 'down', decisaoId });
          }}
          className={`p-1 rounded ${
            feedback === 'down'
              ? 'bg-violet-200 dark:bg-violet-800'
              : 'hover:bg-violet-100 dark:hover:bg-violet-900'
          }`}
          aria-label="Não útil"
        >
          <ThumbsDown className="h-3.5 w-3.5" />
        </button>

        {/* Decisão automatizada, botão de contestação (art. 20 LGPD) */}
        {decisaoAutomatizada && decisaoId && (
          <Link
            href={`/decisoes/${decisaoId}/contestar`}
            className="ml-auto inline-flex items-center gap-1 px-2 py-1 rounded bg-violet-100 dark:bg-violet-900 hover:bg-violet-200 dark:hover:bg-violet-800 font-medium"
          >
            <MessageSquare className="h-3.5 w-3.5" />
            Contestar esta decisão
          </Link>
        )}
      </div>
    </div>
  );
}

// =========================================================================
// Helpers
// =========================================================================

async function postFeedback(payload: { rating: 'up' | 'down'; decisaoId?: string }) {
  try {
    await fetch('/api/ai/feedback', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
      keepalive: true,
    });
  } catch {
    // silencioso, feedback não é crítico
  }
}
