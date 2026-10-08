/**
 * Portal de Transparência, página hub
 * =====================================================================
 * Skill: lgpd-compliance (Parte 3)
 * Rota: app/(transparencia)/page.tsx
 * URL: /transparencia
 *
 * Hub do portal. Renderiza Nutrition Label no topo + grade de sub-páginas.
 * Stack: Next.js 14+ App Router + TypeScript + Tailwind.
 * Ajuste paleta/tipografia pra alinhar com o design system do seu app.
 */

import Link from 'next/link';
import { NutritionLabel } from '@/components/transparencia/NutritionLabel';
import inventario from '@/transparencia/inventario.yaml';

export const metadata = {
  title: 'Portal de Transparência | {{APP_NOME}}',
  description:
    'Tudo que tratamos sobre você, em formato navegável e auditável. Atualizado continuamente a partir do código.',
};

// =========================================================================
// Sub-páginas (ajustar quais existem no projeto)
// =========================================================================

const SECTIONS: {
  slug: string;
  titulo: string;
  descricao: string;
  icone: string;
  habilitado: boolean;
}[] = [
  {
    slug: 'inventario',
    titulo: 'Dicionário de Dados',
    descricao: 'Cada dado que tratamos, finalidade, base legal e retenção.',
    icone: '📚',
    habilitado: true,
  },
  {
    slug: 'terceiros',
    titulo: 'Quem mais tem acesso',
    descricao: 'Lista completa dos prestadores que processam dados em nosso nome.',
    icone: '🤝',
    habilitado: true,
  },
  {
    slug: 'cookies',
    titulo: 'Cookies e tracking',
    descricao: 'Categorias usadas e como gerenciar suas preferências.',
    icone: '🍪',
    habilitado: true,
  },
  {
    slug: 'ia',
    titulo: 'Inteligência Artificial',
    descricao: 'Modelos usados, o que enviamos a eles, model cards.',
    icone: '🤖',
    habilitado: false, // mudar pra true se o app usa IA
  },
  {
    slug: 'retencao',
    titulo: 'Tempo de retenção',
    descricao: 'Quanto tempo guardamos cada categoria de dado e por qual fundamento legal.',
    icone: '⏱️',
    habilitado: true,
  },
  {
    slug: 'incidentes',
    titulo: 'Histórico de incidentes',
    descricao: 'Comunicamos publicamente todo incidente, mesmo os não-notificáveis à ANPD.',
    icone: '🚨',
    habilitado: true,
  },
  {
    slug: 'seguranca',
    titulo: 'Práticas de segurança',
    descricao: 'Criptografia, controle de acesso, auditoria, backups, certificações.',
    icone: '🔒',
    habilitado: true,
  },
  {
    slug: 'dados-abertos',
    titulo: 'Dados abertos',
    descricao: 'Datasets publicados em formato FAIR (DCAT + Schema.org).',
    icone: '📊',
    habilitado: false, // mudar pra true se publica dados
  },
  {
    slug: 'relatorio/2026',
    titulo: 'Relatório anual',
    descricao: 'Métricas agregadas de requisições, direitos exercidos, incidentes.',
    icone: '📈',
    habilitado: false, // mudar pra true após primeiro ano
  },
  {
    slug: 'direitos',
    titulo: 'Seus direitos',
    descricao: 'Como exercer os 9 direitos do art. 18 LGPD aqui mesmo, em até 1 clique.',
    icone: '⚖️',
    habilitado: true,
  },
  {
    slug: 'governanca',
    titulo: 'Governança',
    descricao: 'Encarregado (DPO), organograma de privacidade, comitê.',
    icone: '👥',
    habilitado: true,
  },
  {
    slug: 'mudancas',
    titulo: 'Histórico de mudanças',
    descricao: 'Changelog de todas as alterações nesta página, desde o primeiro dia.',
    icone: '📝',
    habilitado: true,
  },
];

// =========================================================================
// Page
// =========================================================================

export default function PortalTransparenciaPage() {
  return (
    <main className="max-w-5xl mx-auto px-4 py-12 md:py-16">
      {/* Header */}
      <header className="mb-12">
        <p className="text-sm font-medium text-zinc-500 uppercase tracking-wide mb-2">
          Portal de Transparência
        </p>
        <h1 className="text-4xl md:text-5xl font-semibold tracking-tight text-zinc-900 dark:text-zinc-100">
          Tudo que tratamos sobre você
        </h1>
        <p className="mt-4 text-lg text-zinc-600 dark:text-zinc-400 max-w-2xl">
          Este portal é nosso compromisso público com transparência radical.
          Diferente da{' '}
          <Link href="/legal/privacidade" className="underline underline-offset-2">
            Política de Privacidade
          </Link>{' '}
          (documento jurídico), aqui você navega por categorias, vê números,
          baixa o JSON canônico, audita. Atualizado continuamente a partir do
          código, com validação automatizada de drift.
        </p>
        <div className="mt-6 flex flex-wrap gap-3 text-sm">
          <span className="px-3 py-1 rounded-full bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300">
            Versão: {inventario.meta.versao}
          </span>
          <span className="px-3 py-1 rounded-full bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300">
            Atualizado em: {inventario.meta.data_atualizacao}
          </span>
          <a
            href="/api/transparencia/inventario.json"
            className="px-3 py-1 rounded-full bg-emerald-50 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300 hover:underline"
          >
            Inventário em JSON ↗
          </a>
        </div>
      </header>

      {/* Nutrition Label */}
      <section className="mb-16">
        <h2 className="text-2xl font-semibold mb-6">Visão rápida</h2>
        <NutritionLabel inventario={inventario} />
      </section>

      {/* Grade de sub-páginas */}
      <section>
        <h2 className="text-2xl font-semibold mb-6">Explore em profundidade</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {SECTIONS.filter((s) => s.habilitado).map((s) => (
            <Link
              key={s.slug}
              href={`/transparencia/${s.slug}`}
              className="group p-5 rounded-lg border border-zinc-200 dark:border-zinc-800 hover:border-zinc-900 dark:hover:border-zinc-100 transition-colors"
            >
              <div className="text-2xl mb-3">{s.icone}</div>
              <h3 className="font-medium text-zinc-900 dark:text-zinc-100 group-hover:underline">
                {s.titulo}
              </h3>
              <p className="mt-1 text-sm text-zinc-600 dark:text-zinc-400">
                {s.descricao}
              </p>
            </Link>
          ))}
        </div>
      </section>

      {/* Como reportar / DPO */}
      <section className="mt-16 p-6 rounded-lg bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800">
        <h2 className="text-xl font-semibold mb-2">Encontrou algo errado?</h2>
        <p className="text-zinc-600 dark:text-zinc-400">
          Fale com nosso Encarregado de Dados:{' '}
          <a
            href={`mailto:${inventario.meta.dpo_contato}`}
            className="underline underline-offset-2 font-medium"
          >
            {inventario.meta.dpo_contato}
          </a>
        </p>
        <p className="mt-3 text-sm text-zinc-500">
          Você também pode reclamar diretamente à{' '}
          <a
            href="https://www.gov.br/anpd/pt-br/canais_atendimento/cidadao/peticao-de-titular"
            className="underline underline-offset-2"
            target="_blank"
            rel="noreferrer"
          >
            ANPD
          </a>
          .
        </p>
      </section>
    </main>
  );
}
