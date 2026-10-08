'use client';

import { useEffect, useState } from 'react';
import { Scale, AlertTriangle, BookOpen, ChevronRight } from 'lucide-react';
import { useNavigation } from '@/lib/navigation';
import { Badge } from '@/components/ui/badge';
import { BookmarkButton } from '@/components/common/BookmarkButton';
import { BackButton } from '@/components/common/BackButton';

interface SectionData {
  sectionId: number;
  lawId: number;
  lawNameTh: string;
  articleKey: string | null;
  sectionNumber: string | null;
  sectionText: string;
  isLaborRelated: number;
  isCancelled: number;
  chapter: string | null;
  notes: string | null;
  relatedJudgments: Array<{
    judgmentId: number;
    caseNumber: string | null;
    caseYear: string | null;
    category: string | null;
    title: string | null;
    fact: string | null;
    decision: string | null;
    sourceUrl: string | null;
    sourceName: string | null;
    licenseNote: string | null;
  }>;
}

export function SectionView({ sectionId }: { readonly sectionId: number }) {
  const { navigate } = useNavigation();
  const [data, setData] = useState<SectionData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/sections?id=${sectionId}`)
      .then(r => {
        if (!r.ok) throw new Error('Section not found');
        return r.json();
      })
      .then(data => {
        setData(data);
        import('@/lib/recently-viewed').then(({ addRecentlyViewed }) => {
          const label = `${data.lawNameTh} มาตรา ${data.articleKey || data.sectionNumber || ''}`;
          addRecentlyViewed({ type: 'section', id: sectionId, label, url: `/?view=section&id=${sectionId}` });
        });
      })
      .catch(e => setError(e.message))
      .finally(() => setLoading(false));
  }, [sectionId]);

  if (loading) return <div className="mx-auto max-w-4xl px-4 py-20 text-center text-muted-foreground">กำลังโหลด…</div>;
  if (error) return <div className="mx-auto max-w-4xl px-4 py-20 text-center text-destructive">เกิดข้อผิดพลาด: {error}</div>;
  if (!data) return null;

  return (
    <div className="mx-auto max-w-4xl px-4 sm:px-6 py-8">
      <BackButton label="ย้อนกลับ" />

      {/* Section header */}
      <div className="card-premium rounded-2xl p-6 sm:p-8 mb-6">
        <div className="flex items-start justify-between gap-4 mb-4">
          <div>
            <div className="flex flex-wrap items-center gap-2 mb-3">
              {data.isLaborRelated === 1 && (
                <Badge variant="outline" className="badge-labor">มาตราแรงงาน</Badge>
              )}
              {data.isCancelled === 1 && (
                <Badge variant="outline" className="border-destructive/40 text-destructive">ยกเลิกแล้ว</Badge>
              )}
              {data.chapter && (
                <Badge variant="outline" className="border-border/60 text-muted-foreground">{data.chapter}</Badge>
              )}
            </div>
            <h1 className="text-xl sm:text-2xl font-bold text-gold mb-1">
              {data.articleKey || `มาตรา ${data.sectionNumber}`}
            </h1>
            <p className="text-sm text-muted-foreground">{data.lawNameTh}</p>
          </div>
          <BookmarkButton
            type="section"
            id={data.sectionId}
            label={`${data.lawNameTh} ${data.articleKey || ''}`}
            url={`/?view=section&id=${data.sectionId}`}
          />
        </div>

        {/* Section text */}
        <div className="prose-thai text-base leading-loose text-foreground/95 whitespace-pre-wrap">
          {data.sectionText}
        </div>

        {data.notes && (
          <div className="mt-6 pt-4 border-t border-border/40 text-xs text-muted-foreground">
            <strong className="text-gold">หมายเหตุ:</strong> {data.notes}
          </div>
        )}
      </div>

      {/* Related judgments */}
      <div>
        <h2 className="flex items-center gap-2 text-lg font-bold mb-4">
          <Scale className="h-5 w-5 text-gold" />
          คำพิพากษาฎีกาที่อ้างถึงมาตรานี้
          <span className="text-sm font-normal text-muted-foreground">({data.relatedJudgments.length})</span>
        </h2>

        {data.relatedJudgments.length === 0 ? (
          <div className="card-premium rounded-xl p-8 text-center">
            <BookOpen className="h-10 w-10 mx-auto mb-3 text-muted-foreground/50" />
            <p className="text-sm text-muted-foreground">
              ยังไม่มีคำพิพากษาในระบบที่อ้างถึงมาตรานี้โดยตรง
            </p>
          </div>
        ) : (
          <div className="space-y-3">
            {data.relatedJudgments.map(j => (
              <button type="button" key={j.judgmentId} onClick={() => navigate({ name: 'judgment', judgmentId: j.judgmentId })}
                className="card-premium rounded-xl p-4 w-full text-left group cursor-pointer"
              >
                <div className="flex items-start justify-between gap-3 mb-2">
                  <div className="flex flex-wrap items-center gap-2">
                    <Badge variant="outline" className="badge-gold text-[10px]">
                      ฎีกา {j.caseNumber}
                    </Badge>
                    {j.category === 'labor' && (
                      <Badge variant="outline" className="badge-labor text-[10px]">แรงงาน</Badge>
                    )}
                  </div>
                  <ChevronRight className="h-4 w-4 text-muted-foreground group-hover:text-gold group-hover:translate-x-1 transition flex-shrink-0" />
                </div>
                {j.title && (
                  <h3 className="text-sm font-semibold text-foreground group-hover:text-gold transition mb-1 line-clamp-2">
                    {j.title}
                  </h3>
                )}
                {j.fact && (
                  <p className="text-xs text-muted-foreground line-clamp-2 prose-thai">{j.fact}</p>
                )}
                {j.licenseNote?.includes('TSCC') && (
                  <div className="mt-2 flex items-center gap-1 text-[10px] text-amber-500/80">
                    <AlertTriangle className="h-3 w-3" />
                    TSCC academic use only
                  </div>
                )}
              </button>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
