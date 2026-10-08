'use client';

import { useEffect, useState } from 'react';
import { BookOpen, ChevronRight } from 'lucide-react';
import { useNavigation } from '@/lib/navigation';
import { Badge } from '@/components/ui/badge';
import type { LawSummary } from '@/lib/types';

const CATEGORY_LABEL: Record<string, string> = {
  labor: 'กฎหมายแรงงาน',
  civil: 'แพ่งและพาณิชย์',
  criminal: 'อาญา',
  civil_procedure: 'วิธีพิจารณาแพ่ง',
  criminal_procedure: 'วิธีพิจารณาอาญา',
  land: 'ที่ดิน',
  rent: 'เช่าเคหะ',
  narcotics: 'ยาเสพติด',
  traffic: 'จราจร',
  other: 'อื่นๆ',
};

export function LawsView() {
  const { navigate } = useNavigation();
  const [laws, setLaws] = useState<LawSummary[]>([]);
  const [loading, setLoading] = useState(true);
  const [filter, setFilter] = useState<string>('all');

  useEffect(() => {
    fetch('/api/laws')
      .then(r => r.json())
      .then(setLaws)
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  const grouped: Record<string, LawSummary[]> = {};
  for (const l of laws) {
    const cat = l.category || 'other';
    if (!grouped[cat]) grouped[cat] = [];
    grouped[cat].push(l);
  }
  const categories = Object.keys(grouped);
  const visible = filter === 'all' ? laws : (grouped[filter] || []);

  return (
    <div className="mx-auto max-w-7xl px-4 sm:px-6 py-8">
      <div className="mb-6">
        <h1 className="flex items-center gap-2 text-2xl sm:text-3xl font-bold mb-2">
          <BookOpen className="h-7 w-7 text-gold" />
          กฎหมายทั้งหมด
        </h1>
        <p className="text-sm text-muted-foreground">
          รวบรวมกฎหมายไทยทุกหมวด · คลิกที่กฎหมายเพื่อดูมาตราทั้งหมด
        </p>
      </div>

      <div className="flex flex-wrap gap-1.5 mb-6">
        <button type="button" onClick={() => setFilter('all')}
          className={`px-3 py-1 rounded-full text-xs font-medium transition border ${
            filter === 'all'
              ? 'bg-gold text-navy border-gold'
              : 'bg-card-soft text-muted-foreground border-border/50 hover:text-foreground hover:border-gold/30'
          }`}
        >
          ทั้งหมด
        </button>
        {categories.map(c => (
          <button type="button" key={c} onClick={() => setFilter(c)}
            className={`px-3 py-1 rounded-full text-xs font-medium transition border ${
              filter === c
                ? 'bg-gold text-navy border-gold'
                : 'bg-card-soft text-muted-foreground border-border/50 hover:text-foreground hover:border-gold/30'
            }`}
          >
            {CATEGORY_LABEL[c] || c} ({grouped[c].length})
          </button>
        ))}
      </div>

      {loading ? (
        <div className="text-center py-20 text-muted-foreground">กำลังโหลด…</div>
      ) : (
        <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {visible.map(law => (
            <button type="button" key={law.lawId} onClick={() => navigate({ name: 'law', lawId: law.lawId })}
              className="card-premium rounded-xl p-5 text-left group cursor-pointer"
            >
              <div className="flex items-start justify-between gap-2 mb-3">
                <div className="flex flex-wrap gap-1.5">
                  {law.isLaborLaw === 1 && (
                    <Badge variant="outline" className="badge-labor text-[10px]">แรงงาน</Badge>
                  )}
                  <Badge variant="outline" className="badge-gold text-[10px]">
                    {CATEGORY_LABEL[law.category || 'other'] || law.category}
                  </Badge>
                </div>
                <ChevronRight className="h-4 w-4 text-muted-foreground group-hover:text-gold group-hover:translate-x-1 transition" />
              </div>
              <h3 className="text-sm font-semibold text-foreground leading-snug mb-2 line-clamp-2 group-hover:text-gold transition">
                {law.lawNameTh}
              </h3>
              <div className="flex items-center justify-between text-xs text-muted-foreground">
                <span>{law.year ? `พ.ศ. ${law.year}` : '—'}</span>
                <div className="flex gap-3">
                  <span>{law.sectionCount} มาตรา</span>
                  {law.laborSectionCount > 0 && (
                    <span className="text-gold">{law.laborSectionCount} แรงงาน</span>
                  )}
                </div>
              </div>
            </button>
          ))}
        </div>
      )}
    </div>
  );
}
