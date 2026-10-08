'use client';

import { useEffect, useState } from 'react';
import { Scale, Loader2, AlertTriangle, ChevronRight } from 'lucide-react';
import { useNavigation } from '@/lib/navigation';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';

interface JudgmentListItem {
  judgmentId: number;
  caseNumber: string | null;
  caseYear: string | null;
  category: string | null;
  caseTypeGroup: string | null;
  title: string | null;
  topic: string | null;
  topicsList?: string[];
  lawsCitedList?: string[];
  fact: string | null;
  decision: string | null;
  sourceUrl: string | null;
  sourceName: string | null;
  licenseNote: string | null;
}

interface ApiResponse {
  data: JudgmentListItem[];
  page: number;
  pageSize: number;
  total: number;
  totalPages: number;
}

export function JudgmentsView() {
  const { navigate } = useNavigation();
  const [data, setData] = useState<ApiResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [category, setCategory] = useState<'labor' | 'criminal' | 'all'>('labor');
  const [page, setPage] = useState(1);

  useEffect(() => {
    setLoading(true);
    const params = new URLSearchParams({
      page: String(page),
      pageSize: '30',
    });
    if (category !== 'all') params.set('category', category);
    fetch(`/api/judgments?${params}`)
      .then(r => r.json())
      .then(setData)
      .catch(console.error)
      .finally(() => setLoading(false));
  }, [category, page]);

  return (
    <div className="mx-auto max-w-4xl px-4 sm:px-6 py-8">
      <div className="mb-6">
        <h1 className="flex items-center gap-2 text-2xl sm:text-3xl font-bold mb-2">
          <Scale className="h-7 w-7 text-gold" />
          คำพิพากษาศาลฎีกา
        </h1>
        <p className="text-sm text-muted-foreground">
          รวบรวมคำพิพากษาฎีกาจาก deka.in.th, ops.mol.go.th และ TSCC Dataset — {data?.total || 0} คดี
        </p>
      </div>

      {/* Latest judgments highlight (page 1 only) */}
      {page === 1 && data && data.data.length > 0 && (
        <div className="mb-6 grid grid-cols-1 sm:grid-cols-3 gap-3">
          {data.data.slice(0, 3).map((j, i) => {
            const isLatest = i === 0;
            return (
              <button
                type="button"
                key={`latest-${j.judgmentId}`}
                onClick={() => navigate({ name: 'judgment', judgmentId: j.judgmentId })}
                className={`card-premium rounded-xl p-4 text-left group cursor-pointer ${isLatest ? 'border-gold/30 bg-gold/5' : ''}`}
              >
                <div className="flex items-center gap-2 mb-2">
                  {isLatest && <span className="text-[9px] font-bold uppercase tracking-wider text-gold bg-gold/10 px-1.5 py-0.5 rounded">ล่าสุด</span>}
                  <Badge variant="outline" className="badge-gold text-[10px]">{j.caseNumber}</Badge>
                  {j.caseYear && <span className="text-[10px] text-muted-foreground">ปี {j.caseYear}</span>}
                </div>
                {(j.topicsList || []).slice(0, 2).map((t: string) => (
                  <span key={t} className="inline-block px-1.5 py-0.5 mr-1 mb-1 rounded bg-gold/10 border border-gold/15 text-[10px] text-gold/90">{t}</span>
                ))}
                <h3 className="text-sm font-semibold text-foreground group-hover:text-gold transition line-clamp-2 mt-1">
                  {j.title || '(ไม่ระบุประเด็น)'}
                </h3>
              </button>
            );
          })}
        </div>
      )}

      {/* Category filter */}
      <div className="flex flex-wrap gap-2 mb-6">
        {([
          { v: 'labor', label: 'คดีแรงงาน' },
          { v: 'criminal', label: 'คดีอาญา (TSCC)' },
          { v: 'all', label: 'ทั้งหมด' },
        ] as const).map(opt => (
          <button type="button" key={opt.v} onClick={() => { setCategory(opt.v); setPage(1); }}
            className={`px-3 py-1.5 rounded-full text-xs font-medium transition border ${
              category === opt.v
                ? 'bg-gold text-navy border-gold'
                : 'bg-card-soft text-muted-foreground border-border/50 hover:text-foreground hover:border-gold/30'
            }`}
          >
            {opt.label}
          </button>
        ))}
      </div>

      {/* List */}
      {loading && (
        <div className="flex justify-center py-20">
          <Loader2 className="h-6 w-6 animate-spin text-gold" />
        </div>
      )}

      {!loading && data && (
        <>
          {category === 'criminal' && (
            <div className="mb-4 p-3 rounded-lg bg-amber-500/10 border border-amber-500/30 flex items-start gap-2">
              <AlertTriangle className="h-4 w-4 text-amber-500 flex-shrink-0 mt-0.5" />
              <div className="text-xs text-amber-100/90">
                คำพิพากษาคดีอาญามาจาก <strong className="text-amber-500">TSCC Dataset</strong>{' '}
                ซึ่งกำหนดให้ใช้เพื่อการวิจัยเท่านั้น (academic use only) ห้ามนำไปใช้เชิงพาณิชย์
              </div>
            </div>
          )}

          <div className="text-sm text-muted-foreground mb-3">
            พบทั้งหมด <span className="text-gold font-semibold">{(data?.total || 0).toLocaleString('th-TH')}</span> เรื่อง
            · หน้า {data.page}/{data.totalPages}
          </div>

          <div className="space-y-3">
            {data.data.map(j => {
              const topics = j.topicsList || [];
              const lawsCited = j.lawsCitedList || [];
              return (
              <button type="button" key={j.judgmentId} onClick={() => navigate({ name: 'judgment', judgmentId: j.judgmentId })}
                className="card-premium rounded-xl p-4 w-full text-left group cursor-pointer"
              >
                <div className="flex items-start justify-between gap-2 mb-2">
                  <div className="flex flex-wrap items-center gap-2">
                    <Badge variant="outline" className="badge-gold text-[10px]">
                      ฎีกา {j.caseNumber}
                    </Badge>
                    {j.caseYear && (
                      <Badge variant="outline" className="text-[10px] border-border/60 text-muted-foreground">
                        ปี {j.caseYear}
                      </Badge>
                    )}
                    {j.category === 'แรงงาน' && (
                      <Badge variant="outline" className="badge-labor text-[10px]">แรงงาน</Badge>
                    )}
                    {j.licenseNote?.includes('TSCC') && (
                      <Badge variant="outline" className="text-[10px] border-amber-500/40 text-amber-500">
                        TSCC
                      </Badge>
                    )}
                    {lawsCited.length > 0 && (
                      <span className="text-[10px] text-muted-foreground/70">
                        · อ้าง {lawsCited.length} มาตรา
                      </span>
                    )}
                  </div>
                  <ChevronRight className="h-4 w-4 text-muted-foreground group-hover:text-gold group-hover:translate-x-1 transition flex-shrink-0" />
                </div>
                {j.title && (
                  <h3 className="text-sm font-semibold text-foreground group-hover:text-gold transition mb-1.5 line-clamp-2">
                    {j.title}
                  </h3>
                )}
                {/* Topic chips (max 3 shown) */}
                {topics.length > 0 && (
                  <div className="flex flex-wrap gap-1 mb-1.5">
                    {topics.slice(0, 3).map((t, i) => (
                      <span key={`${t}-${i}`} className="inline-block px-1.5 py-0.5 rounded bg-gold/10 border border-gold/15 text-[10px] text-gold/90">
                        {t}
                      </span>
                    ))}
                    {topics.length > 3 && (
                      <span className="text-[10px] text-muted-foreground/60 px-1">
                        +{topics.length - 3}
                      </span>
                    )}
                  </div>
                )}
                {j.fact && (
                  <p className="text-xs text-muted-foreground prose-thai line-clamp-2">{j.fact}</p>
                )}
                {j.sourceName && (
                  <p className="text-[10px] text-muted-foreground/70 mt-2">
                    แหล่งที่มา: {j.sourceName}
                  </p>
                )}
              </button>
              );
            })}
          </div>

          {/* Pagination */}
          {data.totalPages > 1 && (
            <div className="flex justify-center items-center gap-2 mt-8">
              <Button
                variant="outline"
                size="sm"
                disabled={page <= 1}
                onClick={() => setPage(p => Math.max(1, p - 1))}
              >
                ก่อนหน้า
              </Button>
              <span className="text-sm text-muted-foreground">
                {page} / {data.totalPages}
              </span>
              <Button
                variant="outline"
                size="sm"
                disabled={page >= data.totalPages}
                onClick={() => setPage(p => Math.min(data.totalPages, p + 1))}
              >
                ถัดไป
              </Button>
            </div>
          )}
        </>
      )}
    </div>
  );
}
