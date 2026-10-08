'use client';

import { useState } from 'react';
import { ChevronRight, ChevronDown, ChevronUp, BookOpen } from 'lucide-react';
import { useNavigation } from '@/lib/navigation';
import { Badge } from '@/components/ui/badge';
import type { LawSummary } from '@/lib/types';

const CATEGORY_LABEL: Record<string, { th: string; en: string }> = {
  labor: { th: 'กฎหมายแรงงาน', en: 'Labor' },
  civil: { th: 'แพ่งและพาณิชย์', en: 'Civil' },
  criminal: { th: 'อาญา', en: 'Criminal' },
  civil_procedure: { th: 'วิธีพิจารณาแพ่ง', en: 'Civil Procedure' },
  criminal_procedure: { th: 'วิธีพิจารณาอาญา', en: 'Criminal Procedure' },
  land: { th: 'ที่ดิน', en: 'Land' },
  rent: { th: 'เช่าเคหะ', en: 'Rent Control' },
  narcotics: { th: 'ยาเสพติด', en: 'Narcotics' },
  traffic: { th: 'จราจร', en: 'Traffic' },
  other: { th: 'อื่นๆ', en: 'Other' },
};

/** Resolve law status badge className (extracted from nested ternary — SonarCloud S3358). */
function getStatusBadgeClass(status: string): string {
  if (status === 'repealed') return 'border-red-500/40 text-red-500 bg-red-500/10';
  if (status === 'amended') return 'border-blue-500/40 text-blue-500 bg-blue-500/10';
  return 'border-amber-500/40 text-amber-600 bg-amber-500/10';
}

/** Resolve law status label in Thai (extracted from nested ternary — SonarCloud S3358). */
function getStatusLabel(status: string): string {
  if (status === 'repealed') return 'ยกเลิก';
  if (status === 'amended') return 'แก้ไขแล้ว';
  return status;
}

export function LawList({ laws }: { readonly laws: LawSummary[] }) {
  const { navigate } = useNavigation();
  const [filter, setFilter] = useState<string>('all');
  const [expanded, setExpanded] = useState(false);

  // Group by category
  const grouped: Record<string, LawSummary[]> = {};
  for (const l of laws) {
    const cat = l.category || 'other';
    if (!grouped[cat]) grouped[cat] = [];
    grouped[cat].push(l);
  }

  const visibleLaws = filter === 'all' ? laws : (grouped[filter] || []);
  const categories = ['all', ...Object.keys(grouped)];
  const totalLaws = laws.length;

  return (
    <section className="mx-auto max-w-7xl px-4 sm:px-6 py-10">
      <div className="mb-6 flex items-end justify-between flex-wrap gap-4">
        <div>
          <h2 className="text-2xl sm:text-3xl font-bold tracking-tight">
            กฎหมายในระบบ
          </h2>
          <p className="text-sm text-muted-foreground mt-1">
            รวมทั้งหมด {totalLaws} ฉบับ — คลิก &quot;ดูทั้งหมด&quot; เพื่อแสดงรายการ หรือเลือกหมวดเพื่อกรอง
          </p>
        </div>

        {/* Expand / collapse toggle — primary action */}
        <button
          type="button"
          onClick={() => setExpanded(v => !v)}
          className={`inline-flex items-center gap-2 rounded-lg px-4 py-2 text-sm font-semibold transition border ${
            expanded
              ? 'bg-card-soft text-muted-foreground border-border/60 hover:text-foreground hover:border-gold/30'
              : 'bg-gold text-navy border-gold hover:bg-gold/90 shadow-md'
          }`}
        >
          {expanded ? (
            <>
              <ChevronUp className="h-4 w-4" />
              ย่อรายการ
            </>
          ) : (
            <>
              <BookOpen className="h-4 w-4" />
              ดูทั้งหมด {totalLaws} ฉบับ
              <ChevronDown className="h-4 w-4" />
            </>
          )}
        </button>
      </div>

      {/* Filter chips — always visible so user can pre-select a category */}
      {expanded && (
        <div className="mb-5 flex flex-wrap gap-1.5">
          {categories.map(c => (
            <button
              type="button"
              key={c}
              onClick={() => setFilter(c)}
              className={`px-3 py-1 rounded-full text-xs font-medium transition border ${
                filter === c
                  ? 'bg-gold text-navy border-gold'
                  : 'bg-card-soft text-muted-foreground border-border/50 hover:text-foreground hover:border-gold/30'
              }`}
            >
              {c === 'all' ? 'ทั้งหมด' : (CATEGORY_LABEL[c]?.th || c)}
              <span className="ml-1.5 opacity-60">
                {c === 'all' ? totalLaws : (grouped[c]?.length || 0)}
              </span>
            </button>
          ))}
        </div>
      )}

      {/* Laws grid — only render when expanded; otherwise show category teaser cards */}
      {expanded ? (
        <LawsGrid laws={visibleLaws} navigate={navigate} />
      ) : (
        /* Collapsed teaser — show category counts only */
        <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
          {Object.entries(grouped).map(([cat, items]) => {
            const label = CATEGORY_LABEL[cat]?.th || cat;
            return (
              <button
                type="button"
                key={cat}
                onClick={() => { setFilter(cat); setExpanded(true); }}
                className="card-premium rounded-xl p-4 text-left hover:border-gold/40 transition group"
              >
                <div className="flex items-center justify-between mb-1.5">
                  <span className="text-sm font-semibold text-foreground group-hover:text-gold transition">{label}</span>
                  <ChevronRight className="h-4 w-4 text-muted-foreground group-hover:text-gold group-hover:translate-x-1 transition" />
                </div>
                <div className="text-2xl font-bold text-gradient-gold tabular-nums">
                  {items.length}
                  <span className="text-xs font-normal text-muted-foreground ml-1">ฉบับ</span>
                </div>
              </button>
            );
          })}
        </div>
      )}
    </section>
  );
}

/** Renders the grid of law cards, or an empty-state message if no laws match the filter. */
function LawsGrid({ laws, navigate }: { readonly laws: LawSummary[]; readonly navigate: (v: any) => void }) {
  if (laws.length === 0) {
    return <div className="text-center py-10 text-sm text-muted-foreground">ไม่มีกฎหมายในหมวดนี้</div>;
  }
  return (
    <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
      {laws.map(law => (
        <LawCard key={law.lawId} law={law} onClick={() => navigate({ name: 'law', lawId: law.lawId })} />
      ))}
    </div>
  );
}

function LawCard({ law, onClick }: { readonly law: LawSummary; readonly onClick: () => void }) {
  const cat = CATEGORY_LABEL[law.category || 'other'] || { th: law.category, en: '' };
  return (
    <button type="button" onClick={onClick} className="card-premium rounded-xl p-4 text-left hover:border-gold/40 transition group w-full">
      <div className="flex items-start justify-between gap-2 mb-3">
        <div className="flex flex-wrap gap-1.5">
          {law.isLaborLaw === 1 && (
            <Badge variant="outline" className="badge-labor text-[10px]">แรงงาน</Badge>
          )}
          <Badge variant="outline" className="badge-gold text-[10px]">{cat.th}</Badge>
        </div>
        <ChevronRight className="h-4 w-4 text-muted-foreground group-hover:text-gold group-hover:translate-x-1 transition" />
      </div>
      <h3 className="text-sm font-semibold text-foreground leading-snug mb-2 line-clamp-2 group-hover:text-gold transition">
        {law.lawNameTh}
      </h3>
      <div className="flex items-center justify-between text-xs text-muted-foreground">
        <span>{law.year ? `พ.ศ. ${law.year}` : '—'}</span>
        <div className="flex gap-3 items-center">
          <span>{law.sectionCount} มาตรา</span>
          {law.laborSectionCount > 0 && (
            <span className="text-gold">{law.laborSectionCount} แรงงาน</span>
          )}
          {law.status && law.status !== 'complete' && (
            <Badge variant="outline" className={`text-[9px] ${getStatusBadgeClass(law.status)}`}>
              {getStatusLabel(law.status)}
            </Badge>
          )}
        </div>
      </div>
    </button>
  );
}
