/**
 * NutritionLabel, visão rápida no estilo Apple Privacy Nutrition Labels
 * =====================================================================
 * Skill: lgpd-compliance (Parte 3)
 * Cole em: components/transparencia/NutritionLabel.tsx
 *
 * Renderiza grid 3×N com buckets:
 *  - Dados Não Vinculados a Você (anônimos)
 *  - Dados Vinculados a Você (PII)
 *  - Dados Sensíveis LGPD (art. 11)
 *
 * Cada bucket lista as categorias que o app coleta. Se vazio, mostra
 * checkmark verde "Nada coletado aqui", diferencial competitivo.
 */

'use client';

import { CheckCircle2, ChevronRight } from 'lucide-react';
import Link from 'next/link';

// =========================================================================
// Tipos (espelham o schema do inventario.yaml)
// =========================================================================

type SensibilidadeNivel = 'baixa' | 'media' | 'alta' | 'critica' | 'variavel' | 'alta_inferencia';

type CategoriaItem = {
  nome_publico: string;
  finalidade: string[];
  base_legal_lgpd: string;
};

type Categoria = {
  id: string;
  nome_publico: string;
  sensibilidade: SensibilidadeNivel;
  pii?: boolean;
  aplicavel?: boolean;
  itens: CategoriaItem[];
  declaracao_publica?: string;
};

type Inventario = {
  meta: { versao: string; data_atualizacao: string };
  categorias: Categoria[];
};

// =========================================================================
// Classificação por bucket
// =========================================================================

function classificarBucket(c: Categoria): 'nao_vinculado' | 'vinculado' | 'sensivel' | null {
  // Sensíveis (art. 11) sempre no bucket próprio
  if (c.id === 'sensiveis') return c.aplicavel === false ? 'sensivel' : 'sensivel';

  // Identificáveis = vinculado
  if (c.pii === true) return 'vinculado';

  // Anônimos = não vinculado
  return 'nao_vinculado';
}

const ICONES_POR_CATEGORIA: Record<string, string> = {
  identidade: '👤',
  autenticacao: '🔑',
  financeiros: '💳',
  identificadores_tecnicos: '🖥️',
  geolocalizacao: '📍',
  midia_arquivos: '🖼️',
  ugc: '✍️',
  comportamentais: '📊',
  sensiveis: '⚠️',
  inferidos: '🧮',
  metadados_comunicacao: '💬',
  terceiros: '👥',
};

const CORES_SENSIBILIDADE: Record<SensibilidadeNivel, string> = {
  baixa: 'text-emerald-600 dark:text-emerald-400',
  media: 'text-amber-600 dark:text-amber-400',
  alta: 'text-orange-600 dark:text-orange-400',
  critica: 'text-red-600 dark:text-red-400',
  variavel: 'text-zinc-500',
  alta_inferencia: 'text-orange-600 dark:text-orange-400',
};

// =========================================================================
// Componente
// =========================================================================

export function NutritionLabel({ inventario }: { inventario: Inventario }) {
  const buckets = {
    sensivel: [] as Categoria[],
    vinculado: [] as Categoria[],
    nao_vinculado: [] as Categoria[],
  };

  for (const c of inventario.categorias) {
    const b = classificarBucket(c);
    if (b) buckets[b].push(c);
  }

  return (
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
      <Bucket
        titulo="Dados Sensíveis (LGPD art. 11)"
        descricao="Saúde, religião, política, biometria. Exigem consentimento específico e destacado."
        categorias={buckets.sensivel}
        corHeader="bg-red-50 dark:bg-red-950/30 border-red-200 dark:border-red-900"
      />
      <Bucket
        titulo="Dados Vinculados a Você"
        descricao="Identificam você como pessoa. Tratados conforme base legal e seu consentimento."
        categorias={buckets.vinculado}
        corHeader="bg-amber-50 dark:bg-amber-950/30 border-amber-200 dark:border-amber-900"
      />
      <Bucket
        titulo="Dados Não Vinculados a Você"
        descricao="Coletados de forma agregada ou anônima. Não permitem identificação direta."
        categorias={buckets.nao_vinculado}
        corHeader="bg-emerald-50 dark:bg-emerald-950/30 border-emerald-200 dark:border-emerald-900"
      />
    </div>
  );
}

// =========================================================================
// Subcomponente: Bucket
// =========================================================================

function Bucket({
  titulo,
  descricao,
  categorias,
  corHeader,
}: {
  titulo: string;
  descricao: string;
  categorias: Categoria[];
  corHeader: string;
}) {
  const aplicaveis = categorias.filter((c) => c.aplicavel !== false && c.itens.length > 0);
  const naoAplicaveis = categorias.filter((c) => c.aplicavel === false || c.itens.length === 0);

  return (
    <div className="rounded-lg border border-zinc-200 dark:border-zinc-800 overflow-hidden">
      <div className={`p-4 border-b ${corHeader}`}>
        <h3 className="font-semibold text-zinc-900 dark:text-zinc-100">{titulo}</h3>
        <p className="mt-1 text-xs text-zinc-600 dark:text-zinc-400">{descricao}</p>
      </div>

      <div className="p-4 space-y-3">
        {aplicaveis.length === 0 && naoAplicaveis.every((c) => c.aplicavel === false) && (
          <div className="flex items-start gap-2 text-emerald-700 dark:text-emerald-400">
            <CheckCircle2 className="h-5 w-5 flex-shrink-0 mt-0.5" />
            <div>
              <p className="text-sm font-medium">Nada coletado aqui</p>
              <p className="text-xs text-zinc-500 mt-1">
                Não tratamos nenhum dado dessa categoria.
              </p>
            </div>
          </div>
        )}

        {aplicaveis.map((c) => (
          <CategoriaRow key={c.id} categoria={c} />
        ))}

        {naoAplicaveis.length > 0 && aplicaveis.length > 0 && (
          <div className="pt-2 border-t border-zinc-100 dark:border-zinc-800">
            <p className="text-xs text-zinc-500 mb-2">Não coletados:</p>
            {naoAplicaveis.map((c) => (
              <div key={c.id} className="text-xs text-zinc-400 flex items-center gap-2">
                <CheckCircle2 className="h-3 w-3 text-emerald-500" />
                {c.nome_publico}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

// =========================================================================
// Subcomponente: CategoriaRow
// =========================================================================

function CategoriaRow({ categoria }: { categoria: Categoria }) {
  const icone = ICONES_POR_CATEGORIA[categoria.id] ?? '📦';
  const corSens = CORES_SENSIBILIDADE[categoria.sensibilidade];

  return (
    <Link
      href={`/transparencia/inventario#${categoria.id}`}
      className="flex items-start gap-3 group hover:bg-zinc-50 dark:hover:bg-zinc-900 -mx-2 px-2 py-1 rounded"
    >
      <span className="text-xl flex-shrink-0">{icone}</span>
      <div className="flex-1 min-w-0">
        <p className="text-sm font-medium text-zinc-900 dark:text-zinc-100">
          {categoria.nome_publico}
        </p>
        <p className={`text-xs ${corSens} mt-0.5`}>
          {categoria.itens.length} item{categoria.itens.length !== 1 ? 's' : ''} ·{' '}
          sensibilidade {categoria.sensibilidade}
        </p>
      </div>
      <ChevronRight className="h-4 w-4 text-zinc-400 group-hover:text-zinc-900 dark:group-hover:text-zinc-100 flex-shrink-0 mt-1" />
    </Link>
  );
}
