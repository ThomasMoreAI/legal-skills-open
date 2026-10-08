'use client';

import { useEffect, useState } from 'react';
import { Search, BookOpen, ExternalLink, Filter, Scale, ChevronRight, Building2, FileText } from 'lucide-react';
import { useNavigation } from '@/lib/navigation';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Badge } from '@/components/ui/badge';
import { BackButton } from '@/components/common/BackButton';
import { BookmarkButton } from '@/components/common/BookmarkButton';

interface LawDetailData {
  lawId: number;
  lawNameTh: string;
  lawNameEn: string | null;
  year: string | null;
  category: string | null;
  isLaborLaw: number;
  status: string | null;
  fullText: string | null;
  sourceUrl: string | null;
  notes: string | null;
  krisdikaSysid: string | null;
  lawType: string | null;
  lawGroup: string | null;
  lawGoThId: string | null;
  sections: Array<{
    sectionId: number;
    articleKey: string | null;
    sectionNumber: string | null;
    sectionText: string;
    isLaborRelated: number;
    isCancelled: number;
    chapter: string | null;
    notes: string | null;
  }>;
  relatedJudgments?: Array<{
    judgmentId: number;
    judgmentCode: string;
    dekaNo: string | null;
    year: string | null;
    topic: string | null;
  }>;
}

export function LawView({ lawId }: { readonly lawId: number }) {
  const { navigate } = useNavigation();
  const [law, setLaw] = useState<LawDetailData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [searchQ, setSearchQ] = useState('');
  const [laborOnly, setLaborOnly] = useState(false);

  useEffect(() => {
    setLoading(true);
    setError(null);
    const q = searchQ.trim();
    const params = new URLSearchParams({ id: String(lawId) });
    if (q) params.set('q', q);
    const url = `/api/laws?${params.toString()}`;
    fetch(url)
      .then(r => {
        if (!r.ok) throw new Error('Law not found');
        return r.json();
      })
      .then(data => {
        setLaw(data);
        // Track in recently viewed
        import('@/lib/recently-viewed').then(({ addRecentlyViewed }) => {
          addRecentlyViewed({ type: 'law', id: lawId, label: data.lawNameTh || data.title || `กฎหมาย #${lawId}`, url: `/?view=law&id=${lawId}` });
        });
      })
      .catch(e => setError(e.message))
      .finally(() => setLoading(false));
  }, [lawId, searchQ]);

  const visibleSections = (law?.sections || []).filter(s => !laborOnly || s.isLaborRelated === 1);

  return (
    <div className="mx-auto max-w-5xl px-4 sm:px-6 py-8">
      <BackButton label="ย้อนกลับ" />

      {loading && <div className="text-center py-20 text-muted-foreground">กำลังโหลด…</div>}
      {error && <div className="text-center py-20 text-destructive">เกิดข้อผิดพลาด: {error}</div>}

      {law && !loading && (
        <>
          {/* Header */}
          <div className="card-premium rounded-2xl p-6 sm:p-8 mb-6">
            <div className="flex items-start justify-between gap-4 mb-4">
              <div className="flex-1">
                <div className="flex flex-wrap items-center gap-2 mb-3">
                  {law.isLaborLaw === 1 && (
                    <Badge variant="outline" className="badge-labor">กฎหมายแรงงาน</Badge>
                  )}
                  {law.lawType && (
                    <Badge variant="outline" className="border-border/60 text-muted-foreground">
                      <FileText className="h-2.5 w-2.5 mr-1" />
                      {law.lawType}
                    </Badge>
                  )}
                  {law.lawGroup && (
                    <Badge variant="outline" className="border-border/60 text-muted-foreground">
                      <Building2 className="h-2.5 w-2.5 mr-1" />
                      {law.lawGroup}
                    </Badge>
                  )}
                  {law.year && <Badge variant="outline" className="badge-gold">พ.ศ. {law.year}</Badge>}
                  <Badge variant="outline" className="border-border/60 text-muted-foreground">
                    {law.category}
                  </Badge>
                  <BookmarkButton
                    type="law"
                    id={law.lawId}
                    label={law.lawNameTh}
                    url={`/?view=law&id=${law.lawId}`}
                  />
                </div>
                <h1 className="text-2xl sm:text-3xl font-bold leading-tight text-foreground">
                  {law.lawNameTh}
                </h1>
                {law.lawNameEn && (
                  <p className="text-sm text-muted-foreground mt-1">{law.lawNameEn}</p>
                )}
              </div>
            </div>
            <div className="flex flex-wrap items-center gap-4 pt-4 border-t border-border/40 text-sm">
              <div>
                <span className="text-muted-foreground">มาตรา:</span>{' '}
                <span className="font-semibold text-gold">{law.sections.length}</span>
              </div>
              <div>
                <span className="text-muted-foreground">มาตราแรงงาน:</span>{' '}
                <span className="font-semibold text-gold">
                  {law.sections.filter(s => s.isLaborRelated === 1).length}
                </span>
              </div>
              {law.krisdikaSysid && (
                <a
                  href={`https://www.krisdika.go.th/librarian/get?sysid=${law.krisdikaSysid}&ext=htm`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="ml-auto inline-flex items-center gap-1 text-xs text-gold hover:underline"
                >
                  ดูที่กฤษฎีกา <ExternalLink className="h-3 w-3" />
                </a>
              )}
              {!law.krisdikaSysid && law.sourceUrl && (
                <a
                  href={law.sourceUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="ml-auto inline-flex items-center gap-1 text-xs text-gold hover:underline"
                >
                  ดูที่ law.go.th <ExternalLink className="h-3 w-3" />
                </a>
              )}
            </div>
          </div>

          {/* Search + filter */}
          <div className="flex flex-col sm:flex-row gap-3 mb-6">
            <div className="relative flex-1">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
              <Input
                placeholder="ค้นหาในมาตราของกฎหมายนี้…"
                value={searchQ}
                onChange={e => setSearchQ(e.target.value)}
                className="pl-10 bg-card-soft border-border/60"
              />
            </div>
            <Button
              variant={laborOnly ? 'default' : 'outline'}
              onClick={() => setLaborOnly(v => !v)}
              className={laborOnly ? 'bg-gold text-navy hover:bg-gold/90' : ''}
            >
              <Filter className="h-4 w-4" />
              {laborOnly ? 'แสดงเฉพาะมาตราแรงงาน' : 'ทั้งหมด'}
            </Button>
          </div>

          {/* Sections list */}
          {visibleSections.length === 0 ? (
            <div className="text-center py-12 text-muted-foreground">
              <BookOpen className="h-12 w-12 mx-auto mb-3 opacity-50" />
              <p>ไม่พบมาตราที่ตรงกับเงื่อนไข</p>
            </div>
          ) : (
            <div className="space-y-3">
              {visibleSections.map(s => (
                <SectionCard key={s.sectionId} section={s} lawNameTh={law.lawNameTh} />
              ))}
            </div>
          )}

          {/* Related Judgments (via cross_references — judgments that cite this law via templates) */}
          {law.relatedJudgments && law.relatedJudgments.length > 0 && (
            <div className="mt-10">
              <h2 className="flex items-center gap-2 text-lg font-bold mb-4">
                <Scale className="h-5 w-5 text-gold" />
                คำพิพากษาฎีกาที่เกี่ยวข้อง
                <span className="text-sm font-normal text-muted-foreground">
                  ({law.relatedJudgments.length})
                </span>
              </h2>
              <p className="text-xs text-muted-foreground mb-4">
                ฎีกาที่อ้างอิงกฎหมายนี้ผ่านเทมเพลตเอกสาร (cross-references)
              </p>
              <div className="space-y-3">
                {law.relatedJudgments.map(j => (
                  <button
                    type="button"
                    key={j.judgmentId}
                    onClick={() => navigate({ name: 'judgment', judgmentId: j.judgmentId })}
                    className="card-premium rounded-xl p-4 w-full text-left group cursor-pointer"
                  >
                    <div className="flex items-start gap-3">
                      <div className="flex-shrink-0">
                        <div className="flex h-10 min-w-10 px-2 items-center justify-center rounded-lg bg-gold/10 border border-gold/20">
                          <Scale className="h-4 w-4 text-gold" />
                        </div>
                      </div>
                      <div className="flex-1 min-w-0">
                        <div className="flex flex-wrap items-center gap-2 mb-1">
                          <span className="text-xs font-semibold text-gold">{j.dekaNo || j.judgmentCode}</span>
                          {j.year && (
                            <span className="text-[10px] text-muted-foreground">ปี {j.year}</span>
                          )}
                        </div>
                        <p className="text-sm prose-thai text-foreground/90 line-clamp-2">
                          {j.topic || '(ไม่ระบุประเด็น)'}
                        </p>
                      </div>
                      <ChevronRight className="h-4 w-4 text-muted-foreground group-hover:text-gold group-hover:translate-x-1 transition flex-shrink-0" />
                    </div>
                  </button>
                ))}
              </div>
            </div>
          )}
        </>
      )}
    </div>
  );
}

function SectionCard({
  section,
  lawNameTh,
}: {
  readonly section: LawDetailData['sections'][number];
  readonly lawNameTh: string;
}) {
  const { navigate } = useNavigation();
  return (
    <button type="button" onClick={() => navigate({ name: 'section', sectionId: section.sectionId })}
      className="card-premium rounded-xl p-5 w-full text-left group cursor-pointer"
    >
      <div className="flex items-start gap-4">
        <div className="flex-shrink-0">
          <div className={`flex h-12 min-w-12 px-3 items-center justify-center rounded-lg ${
            section.isLaborRelated === 1
              ? 'bg-gold/15 border border-gold/30'
              : 'bg-card-softer border border-border/40'
          }`}>
            <span className={`text-sm font-bold ${section.isLaborRelated === 1 ? 'text-gold' : 'text-foreground'}`}>
              {section.articleKey || `มาตรา ${section.sectionNumber || '?'}`}
            </span>
          </div>
        </div>
        <div className="flex-1 min-w-0">
          <p className="text-sm leading-relaxed prose-thai text-foreground/90 line-clamp-3 group-hover:text-foreground transition">
            {section.sectionText}
          </p>
          {section.isLaborRelated === 1 && (
            <Badge variant="outline" className="badge-labor mt-2 text-[10px]">แรงงาน</Badge>
          )}
          {section.isCancelled === 1 && (
            <Badge variant="outline" className="mt-2 ml-1 text-[10px] border-destructive/40 text-destructive">
              ยกเลิก
            </Badge>
          )}
        </div>
      </div>
    </button>
  );
}
