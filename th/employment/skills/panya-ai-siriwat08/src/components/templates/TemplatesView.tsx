'use client';

import { useEffect, useState } from 'react';
import { FileText, ChevronRight, Download, Search } from 'lucide-react';
import { Input } from '@/components/ui/input';
import { Badge } from '@/components/ui/badge';

interface Template {
  templateId: number;
  templateCode: string;
  title: string;
  category: string;
  charsCount: number;
}

const CATEGORY_LABELS: Record<string, string> = {
  labor: 'เอกสารแรงงาน',
  accounting: 'บัญชี/เงินเดือน',
  contracts: 'สัญญาธุรกิจ',
  court: 'เอกสารศาล',
  sso: 'เอกสาร สปส.',
};

export function TemplatesView() {
  const [templates, setTemplates] = useState<Template[]>([]);
  const [loading, setLoading] = useState(true);
  const [filter, setFilter] = useState<string>('all');
  const [searchQ, setSearchQ] = useState('');

  useEffect(() => {
    fetch('/api/templates')
      .then(r => r.json())
      .then(d => setTemplates(d.data || []))
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  const visible = templates.filter(t => {
    if (filter !== 'all' && t.category !== filter) return false;
    if (searchQ && !t.title.includes(searchQ)) return false;
    return true;
  });

  const categories = ['all', ...Array.from(new Set(templates.map(t => t.category)))];

  return (
    <div className="mx-auto max-w-5xl px-4 sm:px-6 py-8">
      <div className="mb-6">
        <h1 className="flex items-center gap-2 text-2xl sm:text-3xl font-bold mb-2">
          <FileText className="h-7 w-7 text-gold" />
          เอกสารและสัญญา (หมวด F)
        </h1>
        <p className="text-sm text-muted-foreground">
          65 เทมเพลตเอกสารพร้อมใช้ — คลิกเพื่อดู + ดาวน์โหลด PDF พร้อมกรอกชื่อพนักงาน
        </p>
      </div>

      {/* Search */}
      <div className="relative mb-4">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
        <Input
          placeholder="ค้นหาเอกสาร..."
          value={searchQ}
          onChange={e => setSearchQ(e.target.value)}
          className="pl-10 bg-card-soft border-border/60"
        />
      </div>

      {/* Category filter */}
      <div className="flex flex-wrap gap-1.5 mb-6">
        {categories.map(c => (
          <button type="button" key={c} onClick={() => setFilter(c)}
            className={`px-3 py-1 rounded-full text-xs font-medium transition border ${
              filter === c
                ? 'bg-gold text-navy border-gold'
                : 'bg-card-soft text-muted-foreground border-border/50 hover:text-foreground hover:border-gold/30'
            }`}
          >
            {c === 'all' ? 'ทั้งหมด' : (CATEGORY_LABELS[c] || c)}
          </button>
        ))}
      </div>

      {/* Templates grid */}
      {renderTemplatesList(loading, visible)}
    </div>
  );
}

/** Renders the templates list — extracted to satisfy S3358 (no nested ternary). */
function renderTemplatesList(loading: boolean, visible: Template[]) {
  if (loading) {
    return <div className="text-center py-20 text-muted-foreground">กำลังโหลด…</div>;
  }
  if (visible.length === 0) {
    return (
      <div className="text-center py-12 text-muted-foreground">
        <FileText className="h-12 w-12 mx-auto mb-4 opacity-50" />
        ไม่พบเอกสารที่ตรงกับเงื่อนไข
      </div>
    );
  }
  return (
    <div className="grid gap-3 sm:grid-cols-2">
      {visible.map(t => (
        <TemplateCard key={t.templateId} template={t} />
      ))}
    </div>
  );
}

function TemplateCard({ template }: { readonly template: Template }) {
  const catLabel = CATEGORY_LABELS[template.category] || template.category;
  return (
    <div className="card-premium rounded-xl p-4 group">
      <div className="flex items-start justify-between gap-2 mb-2">
        <div className="flex flex-wrap items-center gap-2">
          <Badge variant="outline" className="badge-gold text-[10px]">{template.templateCode}</Badge>
          <Badge variant="outline" className="border-border/60 text-muted-foreground text-[10px]">{catLabel}</Badge>
        </div>
        <ChevronRight className="h-4 w-4 text-muted-foreground group-hover:text-gold transition" />
      </div>
      <h3 className="text-sm font-semibold text-foreground group-hover:text-gold transition mb-2">
        {template.title}
      </h3>
      <div className="flex items-center justify-between">
        <span className="text-xs text-muted-foreground">{template.charsCount} ตัวอักษร</span>
        <a
          href={`/api/templates/pdf?id=${template.templateId}`}
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center gap-1 text-xs text-gold hover:underline"
        >
          <Download className="h-3 w-3" />
          ดู/ดาวน์โหลด PDF
        </a>
      </div>
    </div>
  );
}
