'use client';

import { useEffect, useState } from 'react';
import { Database, BookOpen, Scale, FileText, Link2, Boxes, TrendingUp, Calendar } from 'lucide-react';
import { BackButton } from '@/components/common/BackButton';

interface Stats {
  totalLaws: number;
  totalSections: number;
  totalJudgments: number;
  totalRegulations: number;
  totalTemplates: number;
  totalRagChunks: number;
  totalCrossRefs: number;
  totalLaborSections: number;
  lawsByCategory: Array<{ category: string; count: number; sectionCount: number; laborSectionCount: number }>;
  templatesByCategory: Array<{ category: string; count: number }>;
  regulationStatus: { active: number; superseded: number };
  latestJudgmentYear: string | null;
  version: string;
}

const CATEGORY_LABELS: Record<string, string> = {
  labor: 'แรงงาน',
  civil: 'แพ่งและพาณิชย์',
  criminal: 'อาญา',
  business: 'ธุรกิจ',
  other: 'อื่นๆ',
};

export function DataDashboardView() {
  const [stats, setStats] = useState<Stats | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/stats')
      .then(r => r.json())
      .then(data => {
        setStats(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <div className="mx-auto max-w-5xl px-4 py-8">
        <BackButton label="ย้อนกลับ" />
        <div className="text-center py-20 text-muted-foreground">กำลังโหลด...</div>
      </div>
    );
  }

  if (!stats) return null;

  const cards = [
    { icon: BookOpen, label: 'กฎหมาย', value: stats.totalLaws, color: 'text-blue-400', sub: `${stats.totalSections.toLocaleString()} มาตรา` },
    { icon: Scale, label: 'คำพิพากษาฎีกา', value: stats.totalJudgments, color: 'text-purple-400', sub: `ล่าสุดปี ${stats.latestJudgmentYear || '-'}` },
    { icon: FileText, label: 'อนุบัญญัติ/กฎกระทรัฐมนตรี', value: stats.totalRegulations, color: 'text-amber-400', sub: `${stats.regulationStatus?.active || 0} ใช้บังคับ` },
    { icon: FileText, label: 'เทมเพลตเอกสาร', value: stats.totalTemplates, color: 'text-green-400', sub: 'พร้อมใช้งาน' },
    { icon: Boxes, label: 'RAG Chunks', value: stats.totalRagChunks.toLocaleString(), color: 'text-cyan-400', sub: 'สำหรับ AI ค้นข้อมูล' },
    { icon: Link2, label: 'Cross-references', value: stats.totalCrossRefs.toLocaleString(), color: 'text-pink-400', sub: 'เชื่อมโยงข้อมูล' },
  ];

  return (
    <div className="mx-auto max-w-5xl px-4 sm:px-6 py-8">
      <BackButton label="ย้อนกลับ" />
      <div className="flex items-center gap-2 mb-2">
        <Database className="h-6 w-6 text-gold" />
        <h1 className="text-2xl sm:text-3xl font-bold">สถานะข้อมูลระบบ</h1>
      </div>
      <p className="text-sm text-muted-foreground mb-6">
        ภาพรวมข้อมูลทั้งหมดในฐานข้อมูล Panya-AI — อัปเดตล่าสุด: {new Date().toLocaleDateString('th-TH')}
      </p>

      {/* Stats cards */}
      <div className="grid grid-cols-2 sm:grid-cols-3 gap-4 mb-8">
        {cards.map((card) => {
          const Icon = card.icon;
          return (
            <div key={card.label} className="card-premium rounded-xl p-4">
              <div className="flex items-center gap-2 mb-2">
                <Icon className={`h-5 w-5 ${card.color}`} />
                <span className="text-xs font-medium text-muted-foreground">{card.label}</span>
              </div>
              <div className="text-2xl font-bold text-foreground">{card.value}</div>
              <div className="text-[10px] text-muted-foreground mt-1">{card.sub}</div>
            </div>
          );
        })}
      </div>

      {/* Laws by category */}
      <div className="card-premium rounded-xl p-6 mb-6">
        <h2 className="flex items-center gap-2 text-lg font-semibold mb-4">
          <BookOpen className="h-5 w-5 text-gold" />
          กฎหมายแยกตามหมวด
        </h2>
        <div className="space-y-3">
          {stats.lawsByCategory?.map((cat) => {
            const label = CATEGORY_LABELS[cat.category] || cat.category;
            const maxSections = Math.max(...stats.lawsByCategory.map(c => c.sectionCount));
            const pct = maxSections > 0 ? (cat.sectionCount / maxSections) * 100 : 0;
            return (
              <div key={cat.category}>
                <div className="flex items-center justify-between text-sm mb-1">
                  <span className="font-medium">{label}</span>
                  <span className="text-muted-foreground">
                    {cat.count} ฉบับ · {cat.sectionCount.toLocaleString()} มาตรา
                    {cat.laborSectionCount > 0 && <span className="text-gold ml-1">({cat.laborSectionCount} แรงงาน)</span>}
                  </span>
                </div>
                <div className="h-2 bg-card-soft rounded-full overflow-hidden">
                  <div className="h-full bg-gold/60 rounded-full" style={{ width: `${pct}%` }} />
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Regulation status */}
      {stats.regulationStatus && (
        <div className="card-premium rounded-xl p-6 mb-6">
          <h2 className="flex items-center gap-2 text-lg font-semibold mb-4">
            <FileText className="h-5 w-5 text-gold" />
            สถานะอนุบัญญัติ
          </h2>
          <div className="grid grid-cols-2 gap-4">
            <div className="rounded-lg border border-green-500/30 bg-green-500/5 p-4">
              <div className="text-2xl font-bold text-green-400">{stats.regulationStatus.active}</div>
              <div className="text-xs text-muted-foreground">ใช้บังคับ (ฉบับรวมล่าสุด)</div>
            </div>
            <div className="rounded-lg border border-amber-500/30 bg-amber-500/5 p-4">
              <div className="text-2xl font-bold text-amber-400">{stats.regulationStatus.superseded}</div>
              <div className="text-xs text-muted-foreground">ฉบับเก่า (ถูกแทนที่)</div>
            </div>
          </div>
        </div>
      )}

      {/* Data freshness */}
      <div className="card-premium rounded-xl p-6">
        <h2 className="flex items-center gap-2 text-lg font-semibold mb-4">
          <Calendar className="h-5 w-5 text-gold" />
          ความสดของข้อมูล
        </h2>
        <div className="space-y-2 text-sm">
          <div className="flex items-center justify-between">
            <span className="text-muted-foreground">ฎีกาล่าสุดในระบบ:</span>
            <span className="font-semibold text-foreground">ปี {stats.latestJudgmentYear || 'ไม่ทราบ'}</span>
          </div>
          <div className="flex items-center justify-between">
            <span className="text-muted-foreground">ปีปัจจุบัน (พ.ศ.):</span>
            <span className="font-semibold text-foreground">{new Date().getFullYear() + 543}</span>
          </div>
          <div className="flex items-center justify-between">
            <span className="text-muted-foreground">ระบบตรวจสอบกฎหมายใหม่:</span>
            <span className="font-semibold text-green-400 flex items-center gap-1">
              <TrendingUp className="h-3 w-3" /> เปิดใช้งาน (รายวัน)
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}
