'use client';

import { useEffect, useState } from 'react';
import { Search, Loader2, ChevronRight, Scale, BookOpen, AlertTriangle, FileText, Gavel } from 'lucide-react';
import { useNavigation } from '@/lib/navigation';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Badge } from '@/components/ui/badge';

type SearchType = 'all' | 'sections' | 'judgments' | 'laws' | 'regulations' | 'templates';

interface SearchResults {
  sections: Array<{
    type: 'section';
    id: number;
    lawId: number;
    lawNameTh: string;
    category: string;
    isLaborLaw: boolean;
    articleKey: string | null;
    sectionNumber: string | null;
    snippet: string;
    isLaborRelated: boolean;
  }>;
  judgments: Array<{
    type: 'judgment';
    id: number;
    caseNumber: string | null;
    caseYear: string | null;
    category: string | null;
    title: string | null;
    snippet: string;
    sourceUrl: string | null;
    licenseNote: string | null;
  }>;
  laws: Array<{
    type: 'law';
    id: number;
    lawNameTh: string;
    lawNameEn: string | null;
    year: string | null;
    category: string;
    isLaborLaw: boolean;
    sectionCount: number;
    hitCount?: number;
  }>;
  regulations: Array<{
    type: 'regulation';
    id: number;
    regulationCode: string;
    title: string;
    category: string | null;
    snippet: string;
    isRepealed?: boolean;
    repealStatus?: string;
    year?: string | null;
  }>;
  templates: Array<{
    type: 'template';
    id: number;
    templateCode: string;
    title: string;
    category: string;
    snippet: string;
  }>;
  total: number;
  q: string;
  type: string;
}

function highlightSnippet(text: string): { __html: string } {
  // The snippet from FTS contains << and >> markers
  // Convert to <mark> with gold highlight
  const escaped = text
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;');
  const html = escaped
    .replaceAll('&lt;&lt;', '<mark class="bg-gold/30 text-gold rounded px-0.5">')
    .replaceAll('&gt;&gt;', '</mark>');
  return { __html: html };
}

export function SearchView({ initialQ, initialType }: { readonly initialQ?: string; readonly initialType?: SearchType }) {
  const { navigate } = useNavigation();
  const [q, setQ] = useState(initialQ || '');
  const [type, setType] = useState<SearchType>(initialType || 'all');
  const [results, setResults] = useState<SearchResults | null>(null);
  const [loading, setLoading] = useState(false);

  const runSearch = (query: string, t: SearchType) => {
    if (!query.trim()) {
      setResults(null);
      return;
    }
    setLoading(true);
    // Update URL
    const params = new URLSearchParams();
    params.set('view', 'search');
    params.set('q', query);
    if (t !== 'all') params.set('type', t);
    window.history.replaceState({}, '', `/?${params.toString()}`);

    fetch(`/api/search?q=${encodeURIComponent(query)}&type=${t}&limit=30`)
      .then(r => r.json())
      .then(setResults)
      .catch(console.error)
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    if (!initialQ) return;
    setQ(initialQ);
    setType(initialType || 'all');
    runSearch(initialQ, initialType || 'all');
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [initialQ, initialType]);

  const onSubmit = (e: React.SyntheticEvent) => {
    e.preventDefault();
    runSearch(q, type);
  };

  return (
    <div className="mx-auto max-w-4xl px-4 sm:px-6 py-8">
      <h1 className="text-2xl sm:text-3xl font-bold mb-2">ค้นหาในฐานข้อมูลกฎหมาย</h1>
      <p className="text-sm text-muted-foreground mb-6">
        ค้นหาในมาตรากฎหมาย คำพิพากษาฎีกา อนุบัญญัติ และเทมเพลตสัญญา
      </p>

      {/* Search form */}
      <form onSubmit={onSubmit} className="mb-6">
        <div className="relative">
          <Search className="absolute left-4 top-1/2 -translate-y-1/2 h-5 w-5 text-muted-foreground" />
          <Input
            type="text"
            value={q}
            onChange={e => setQ(e.target.value)}
            placeholder="เช่น ค่าจ้างล่วงเวลา, เลิกจ้าง, บุริมสิทธิ์, ค่าชดเชย…"
            className="pl-12 h-14 text-base bg-card-soft border-border/60"
            autoFocus
          />
          <Button
            type="submit"
            className="absolute right-2 top-1/2 -translate-y-1/2 bg-gold text-navy hover:bg-gold/90"
            disabled={loading}
          >
            {loading ? <Loader2 className="h-4 w-4 animate-spin" /> : 'ค้นหา'}
          </Button>
        </div>
      </form>

      {/* Type filter */}
      <div className="flex flex-wrap gap-2 mb-6">
        {([
          { v: 'all', label: 'ทั้งหมด' },
          { v: 'sections', label: 'มาตรากฎหมาย' },
          { v: 'judgments', label: 'คำพิพากษา' },
          { v: 'laws', label: 'ชื่อกฎหมาย' },
          { v: 'regulations', label: 'อนุบัญญัติ' },
          { v: 'templates', label: 'เทมเพลตสัญญา' },
        ] as Array<{ v: SearchType; label: string }>).map(opt => (
          <button type="button" key={opt.v} onClick={() => {
              setType(opt.v);
              if (q.trim()) runSearch(q, opt.v);
            }}
            className={`px-3 py-1.5 rounded-full text-xs font-medium transition border ${
              type === opt.v
                ? 'bg-gold text-navy border-gold'
                : 'bg-card-soft text-muted-foreground border-border/50 hover:text-foreground hover:border-gold/30'
            }`}
          >
            {opt.label}
          </button>
        ))}
      </div>

      {/* Results */}
      {results && (
        <div className="space-y-6">
          <div className="text-sm text-muted-foreground">
            พบ <span className="text-gold font-semibold">{results.total}</span> ผลลัพธ์สำหรับ "{results.q}"
          </div>

          {/* Laws */}
          {results.laws.length > 0 && (
            <ResultGroup title="กฎหมาย" icon={BookOpen} count={results.laws.length}>
              {results.laws.map(law => (
                <button type="button" key={law.id} onClick={() => navigate({ name: 'law', lawId: law.id })}
                  className="card-premium rounded-xl p-4 w-full text-left group cursor-pointer"
                >
                  <div className="flex items-start justify-between gap-2 mb-1">
                    <h3 className="text-sm font-semibold text-foreground group-hover:text-gold transition">{law.lawNameTh}</h3>
                    <ChevronRight className="h-4 w-4 text-muted-foreground group-hover:text-gold flex-shrink-0" />
                  </div>
                  <div className="flex flex-wrap items-center gap-2 text-xs text-muted-foreground">
                    {law.isLaborLaw && <Badge variant="outline" className="badge-labor text-[10px]">แรงงาน</Badge>}
                    {law.year && <span>พ.ศ. {law.year}</span>}
                    <span>{law.sectionCount} มาตรา</span>
                    {law.hitCount && <span className="text-gold">{law.hitCount} มาตราตรงกับคำค้น</span>}
                  </div>
                </button>
              ))}
            </ResultGroup>
          )}

          {/* Sections */}
          {results.sections.length > 0 && (
            <ResultGroup title="มาตรากฎหมาย" icon={BookOpen} count={results.sections.length}>
              {results.sections.map(s => (
                <button type="button" key={s.id} onClick={() => navigate({ name: 'section', sectionId: s.id })}
                  className="card-premium rounded-xl p-4 w-full text-left group cursor-pointer"
                >
                  <div className="flex items-start gap-3">
                    <div className="flex-shrink-0">
                      <div className={`flex h-10 min-w-10 px-2 items-center justify-center rounded-lg ${
                        s.isLaborRelated
                          ? 'bg-gold/15 border border-gold/30'
                          : 'bg-card-softer border border-border/40'
                      }`}>
                        <span className={`text-xs font-bold ${s.isLaborRelated ? 'text-gold' : 'text-foreground'}`}>
                          {s.articleKey || s.sectionNumber}
                        </span>
                      </div>
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="text-xs text-muted-foreground mb-1">{s.lawNameTh}</div>
                      <div
                        className="text-sm prose-thai text-foreground/90 line-clamp-3"
                        dangerouslySetInnerHTML={highlightSnippet(s.snippet)}
                      />
                    </div>
                    <ChevronRight className="h-4 w-4 text-muted-foreground group-hover:text-gold flex-shrink-0" />
                  </div>
                </button>
              ))}
            </ResultGroup>
          )}

          {/* Judgments */}
          {results.judgments.length > 0 && (
            <ResultGroup title="คำพิพากษาฎีกา" icon={Scale} count={results.judgments.length}>
              {results.judgments.map(j => (
                <button type="button" key={j.id} onClick={() => navigate({ name: 'judgment', judgmentId: j.id })}
                  className="card-premium rounded-xl p-4 w-full text-left group cursor-pointer"
                >
                  <div className="flex items-start justify-between gap-2 mb-1">
                    <div className="flex flex-wrap items-center gap-2">
                      <Badge variant="outline" className="badge-gold text-[10px]">
                        ฎีกา {j.caseNumber}
                      </Badge>
                      {j.category === 'labor' && (
                        <Badge variant="outline" className="badge-labor text-[10px]">แรงงาน</Badge>
                      )}
                      {j.licenseNote?.includes('TSCC') && (
                        <Badge variant="outline" className="text-[10px] border-amber-500/40 text-amber-500">
                          <AlertTriangle className="h-2.5 w-2.5 mr-1" />TSCC
                        </Badge>
                      )}
                    </div>
                    <ChevronRight className="h-4 w-4 text-muted-foreground group-hover:text-gold flex-shrink-0" />
                  </div>
                  {j.title && (
                    <h3 className="text-sm font-semibold text-foreground group-hover:text-gold transition mb-1 line-clamp-2">
                      {j.title}
                    </h3>
                  )}
                  <div
                    className="text-xs prose-thai text-muted-foreground line-clamp-2"
                    dangerouslySetInnerHTML={highlightSnippet(j.snippet)}
                  />
                </button>
              ))}
            </ResultGroup>
          )}

          {/* Regulations */}
          {results.regulations.length > 0 && (
            <ResultGroup title="อนุบัญญัติ / กฎกระทรวง / ประกาศ" icon={Gavel} count={results.regulations.length}>
              {results.regulations.map(r => {
                const isSuperseded = r.repealStatus === 'superseded';
                return (
                <div key={r.id}
                  className={`card-premium rounded-xl p-4 w-full text-left group cursor-default ${isSuperseded ? 'opacity-75' : ''}`}
                >
                  <div className="flex items-start justify-between gap-2 mb-1">
                    <div className="flex flex-wrap items-center gap-2">
                      <Badge variant="outline" className="badge-gold text-[10px]">{r.regulationCode}</Badge>
                      {r.category && (
                        <Badge variant="outline" className="text-[10px] border-border/60 text-muted-foreground">{r.category}</Badge>
                      )}
                      {r.year && (
                        <span className="text-[10px] text-muted-foreground">พ.ศ. {r.year}</span>
                      )}
                      {r.repealStatus === 'repealed' && (
                        <Badge variant="outline" className="text-[10px] border-red-500/40 text-red-500 bg-red-500/10">
                          ยกเลิกแล้ว
                        </Badge>
                      )}
                      {isSuperseded && (
                        <Badge variant="outline" className="text-[10px] border-amber-500/40 text-amber-500 bg-amber-500/10">
                          ฉบับเก่า — มีฉบับใหม่กว่า
                        </Badge>
                      )}
                      {r.repealStatus === 'active' && (
                        <Badge variant="outline" className="text-[10px] border-green-500/40 text-green-600 bg-green-500/10">
                          ใช้บังคับ
                        </Badge>
                      )}
                    </div>
                  </div>
                  <h3 className={`text-sm font-semibold text-foreground group-hover:text-gold transition mb-1 line-clamp-2 ${isSuperseded ? 'line-through opacity-60' : ''}`}>
                    {r.title}
                  </h3>
                  <div
                    className="text-xs prose-thai text-muted-foreground line-clamp-2"
                    dangerouslySetInnerHTML={highlightSnippet(r.snippet)}
                  />
                </div>
                );
              })}
            </ResultGroup>
          )}

          {/* Contract Templates */}
          {results.templates.length > 0 && (
            <ResultGroup title="เทมเพลตเอกสาร / สัญญา" icon={FileText} count={results.templates.length}>
              {results.templates.map(t => (
                <button type="button" key={t.id} onClick={() => navigate({ name: 'templates' })}
                  className="card-premium rounded-xl p-4 w-full text-left group cursor-pointer"
                >
                  <div className="flex items-start justify-between gap-2 mb-1">
                    <div className="flex flex-wrap items-center gap-2">
                      <Badge variant="outline" className="badge-gold text-[10px]">{t.templateCode}</Badge>
                      <Badge variant="outline" className="text-[10px] border-border/60 text-muted-foreground">{t.category}</Badge>
                    </div>
                    <ChevronRight className="h-4 w-4 text-muted-foreground group-hover:text-gold flex-shrink-0" />
                  </div>
                  <h3 className="text-sm font-semibold text-foreground group-hover:text-gold transition mb-1 line-clamp-2">
                    {t.title}
                  </h3>
                  <div
                    className="text-xs prose-thai text-muted-foreground line-clamp-2"
                    dangerouslySetInnerHTML={highlightSnippet(t.snippet)}
                  />
                </button>
              ))}
            </ResultGroup>
          )}

          {results.total === 0 && (
            <div className="card-premium rounded-xl p-12 text-center">
              <Search className="h-12 w-12 mx-auto mb-4 text-muted-foreground/50" />
              <p className="text-muted-foreground">ไม่พบผลลัพธ์ ลองค้นหาด้วยคำอื่น</p>
            </div>
          )}
        </div>
      )}

      {!results && !loading && (
        <div className="card-premium rounded-xl p-12 text-center">
          <Search className="h-12 w-12 mx-auto mb-4 text-muted-foreground/50" />
          <p className="text-muted-foreground">พิมพ์คำค้นหาด้านบนเพื่อเริ่มต้น</p>
          <p className="text-xs text-muted-foreground/70 mt-2">
            ลอง: ค่าจ้าง · เลิกจ้าง · บุริมสิทธิ์ · ค่าชดเชย · สัญญาจ้าง
          </p>
        </div>
      )}
    </div>
  );
}

function ResultGroup({
  title,
  icon: Icon,
  count,
  children,
}: {
  readonly title: string;
  readonly icon: any;
  readonly count: number;
  readonly children: React.ReactNode;
}) {
  return (
    <div>
      <h2 className="flex items-center gap-2 text-sm font-semibold uppercase tracking-wider text-gold mb-3">
        <Icon className="h-4 w-4" />
        {title}
        <span className="text-xs font-normal text-muted-foreground">({count})</span>
      </h2>
      <div className="space-y-2">{children}</div>
    </div>
  );
}
