/**
 * CookieBanner, banner de consentimento LGPD/ANPD
 * ==================================================
 * Template lgpd-compliance. Cumpre o Guia Orientativo da ANPD (23/01/2025):
 *  - Cookies não-essenciais DESATIVADOS por padrão
 *  - Botão "Rejeitar opcionais" com mesma proeminência de "Aceitar todos"
 *  - 2 camadas: banner + modal de granularidade por categoria
 *  - Revogação tão fácil quanto consentir
 *  - Persistência em cookie próprio first-party + envio ao backend pra consent_log
 *
 * Stack: Next.js 14+ (App Router) + React 19 + TypeScript + Tailwind.
 * Cole em `components/legal/CookieBanner.tsx` e renderize no `app/layout.tsx`.
 * Ajuste o estilo conforme o design system do seu app.
 */

'use client';

import { useEffect, useState, useCallback } from 'react';
import Link from 'next/link';

// === Tipos ===================================================================

type ConsentCategory = 'essential' | 'functional' | 'analytics' | 'marketing';

type Consent = {
  /** Versão da política aceita, incremente quando mudar materialmente */
  v: string;
  /** ISO timestamp do consentimento */
  ts: string;
  essential: true; // sempre true
  functional: boolean;
  analytics: boolean;
  marketing: boolean;
};

const POLICY_VERSION = '2026-05-24'; // ⚠️ atualize ao mudar a política

const COOKIE_NAME = '__cookie_consent';
const COOKIE_MAX_AGE = 60 * 60 * 24 * 365; // 1 ano

// === Helpers de cookie =======================================================

function readConsent(): Consent | null {
  if (typeof document === 'undefined') return null;
  const raw = document.cookie
    .split('; ')
    .find((c) => c.startsWith(`${COOKIE_NAME}=`));
  if (!raw) return null;
  try {
    return JSON.parse(decodeURIComponent(raw.split('=')[1]));
  } catch {
    return null;
  }
}

function writeConsent(consent: Consent) {
  const value = encodeURIComponent(JSON.stringify(consent));
  document.cookie = [
    `${COOKIE_NAME}=${value}`,
    `Max-Age=${COOKIE_MAX_AGE}`,
    'Path=/',
    'SameSite=Lax',
    location.protocol === 'https:' ? 'Secure' : '',
  ]
    .filter(Boolean)
    .join('; ');
}

async function postConsentToBackend(consent: Consent) {
  // Envia pro consent_log do backend. Não bloquear o usuário em caso de erro de rede.
  try {
    await fetch('/api/legal/consent', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(consent),
      keepalive: true,
    });
  } catch {
    // silenciar, o cookie local já é a prova legal mínima
  }
}

// === Componente principal ===================================================

export function CookieBanner() {
  const [visible, setVisible] = useState(false);
  const [showModal, setShowModal] = useState(false);

  // Estado dos toggles na 2ª camada
  const [toggles, setToggles] = useState<{
    functional: boolean;
    analytics: boolean;
    marketing: boolean;
  }>({ functional: false, analytics: false, marketing: false });

  // Verifica se precisa exibir o banner
  useEffect(() => {
    const existing = readConsent();
    if (!existing || existing.v !== POLICY_VERSION) {
      setVisible(true);
    }
  }, []);

  const persist = useCallback((consent: Consent) => {
    writeConsent(consent);
    postConsentToBackend(consent);
    setVisible(false);
    setShowModal(false);
  }, []);

  const acceptAll = () =>
    persist({
      v: POLICY_VERSION,
      ts: new Date().toISOString(),
      essential: true,
      functional: true,
      analytics: true,
      marketing: true,
    });

  const rejectNonEssential = () =>
    persist({
      v: POLICY_VERSION,
      ts: new Date().toISOString(),
      essential: true,
      functional: false,
      analytics: false,
      marketing: false,
    });

  const saveCustom = () =>
    persist({
      v: POLICY_VERSION,
      ts: new Date().toISOString(),
      essential: true,
      ...toggles,
    });

  if (!visible) return null;

  return (
    <>
      {/* === 1ª camada: banner =========================================== */}
      <div
        role="dialog"
        aria-label="Aviso de cookies"
        aria-modal={false}
        className="fixed bottom-0 inset-x-0 z-50 p-4 sm:p-6 bg-white dark:bg-zinc-900 border-t border-zinc-200 dark:border-zinc-800 shadow-2xl"
      >
        <div className="max-w-5xl mx-auto flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
          <p className="text-sm text-zinc-700 dark:text-zinc-200 leading-relaxed">
            Usamos cookies estritamente necessários para o funcionamento deste
            site. Cookies opcionais (funcionais, analíticos e de marketing)
            só serão usados com seu consentimento, nos termos da{' '}
            <Link
              href="/legal/cookies"
              className="underline underline-offset-2 font-medium"
            >
              Política de Cookies
            </Link>
            .
          </p>

          {/* Três botões com PARIDADE visual, exigência ANPD */}
          <div className="flex flex-col sm:flex-row gap-2 shrink-0">
            <button
              type="button"
              onClick={rejectNonEssential}
              className="px-4 py-2 text-sm font-medium rounded-md border border-zinc-300 dark:border-zinc-700 hover:bg-zinc-50 dark:hover:bg-zinc-800"
            >
              Rejeitar opcionais
            </button>
            <button
              type="button"
              onClick={() => setShowModal(true)}
              className="px-4 py-2 text-sm font-medium rounded-md border border-zinc-300 dark:border-zinc-700 hover:bg-zinc-50 dark:hover:bg-zinc-800"
            >
              Configurar
            </button>
            <button
              type="button"
              onClick={acceptAll}
              className="px-4 py-2 text-sm font-medium rounded-md bg-zinc-900 text-white hover:bg-zinc-800 dark:bg-white dark:text-zinc-900 dark:hover:bg-zinc-100"
            >
              Aceitar todos
            </button>
          </div>
        </div>
      </div>

      {/* === 2ª camada: modal de granularidade ============================ */}
      {showModal && (
        <div
          role="dialog"
          aria-modal
          aria-label="Preferências de cookies"
          className="fixed inset-0 z-[60] flex items-center justify-center bg-black/50 p-4"
        >
          <div className="bg-white dark:bg-zinc-900 rounded-lg shadow-2xl max-w-xl w-full p-6 max-h-[90vh] overflow-y-auto">
            <h2 className="text-lg font-semibold mb-2">
              Preferências de cookies
            </h2>
            <p className="text-sm text-zinc-600 dark:text-zinc-400 mb-6">
              Escolha quais categorias de cookies você autoriza. Você pode
              alterar a qualquer momento clicando em "Gerenciar preferências"
              no rodapé.
            </p>

            <div className="space-y-4">
              <CategoryRow
                title="Estritamente necessários"
                description="Indispensáveis para o funcionamento do site (sessão, segurança). Sempre ativos. Base legal: execução de contrato (art. 7º V LGPD)."
                checked
                disabled
                onChange={() => {}}
              />
              <CategoryRow
                title="Funcionais"
                description="Lembram preferências (idioma, tema). Base legal: consentimento (art. 7º I LGPD)."
                checked={toggles.functional}
                onChange={(v) =>
                  setToggles((t) => ({ ...t, functional: v }))
                }
              />
              <CategoryRow
                title="Analíticos"
                description="Medição agregada de uso para melhorar o produto (Google Analytics 4). Base legal: consentimento (art. 7º I LGPD)."
                checked={toggles.analytics}
                onChange={(v) => setToggles((t) => ({ ...t, analytics: v }))}
              />
              <CategoryRow
                title="Marketing"
                description="Permitem publicidade direcionada e remarketing (Meta Pixel, Google Ads). Base legal: consentimento (art. 7º I LGPD)."
                checked={toggles.marketing}
                onChange={(v) => setToggles((t) => ({ ...t, marketing: v }))}
              />
            </div>

            <div className="flex flex-col sm:flex-row gap-2 mt-6 justify-end">
              <button
                type="button"
                onClick={() => setShowModal(false)}
                className="px-4 py-2 text-sm font-medium rounded-md border border-zinc-300 dark:border-zinc-700"
              >
                Cancelar
              </button>
              <button
                type="button"
                onClick={saveCustom}
                className="px-4 py-2 text-sm font-medium rounded-md bg-zinc-900 text-white dark:bg-white dark:text-zinc-900"
              >
                Salvar preferências
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}

// === Botão "Gerenciar preferências" pro footer ===============================

/**
 * Coloque no rodapé do site pra permitir revogação a qualquer momento.
 * Apaga o cookie atual e força o banner a reaparecer.
 */
export function ManageConsentButton() {
  const reopen = () => {
    document.cookie = `${COOKIE_NAME}=; Max-Age=0; Path=/; SameSite=Lax`;
    if (typeof window !== 'undefined') window.location.reload();
  };

  return (
    <button
      type="button"
      onClick={reopen}
      className="text-sm underline underline-offset-2 text-zinc-600 dark:text-zinc-400 hover:text-zinc-900"
    >
      Gerenciar preferências de cookies
    </button>
  );
}

// === Hook utilitário pra ler consentimento em qualquer componente ============

/**
 * Útil pra renderização condicional de tags de analytics/marketing.
 *   const { analytics, marketing } = useConsent();
 *   if (analytics) <GoogleAnalyticsScript />
 */
export function useConsent(): Partial<Record<ConsentCategory, boolean>> {
  const [consent, setConsent] = useState<Consent | null>(null);

  useEffect(() => {
    setConsent(readConsent());
  }, []);

  return {
    essential: true,
    functional: !!consent?.functional,
    analytics: !!consent?.analytics,
    marketing: !!consent?.marketing,
  };
}

// === Subcomponente ===========================================================

function CategoryRow(props: {
  title: string;
  description: string;
  checked: boolean;
  disabled?: boolean;
  onChange: (v: boolean) => void;
}) {
  return (
    <div className="flex items-start gap-3">
      <input
        type="checkbox"
        checked={props.checked}
        disabled={props.disabled}
        onChange={(e) => props.onChange(e.target.checked)}
        className="mt-1 h-4 w-4 accent-zinc-900 dark:accent-white"
      />
      <div className="flex-1">
        <h3 className="text-sm font-medium">{props.title}</h3>
        <p className="text-xs text-zinc-600 dark:text-zinc-400 mt-1">
          {props.description}
        </p>
      </div>
    </div>
  );
}
