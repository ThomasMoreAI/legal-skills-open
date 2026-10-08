'use client';
import { useEffect, useState } from 'react';
import { ArrowLeft, ArrowRight, Check, Download, Wand2 } from 'lucide-react';
import { useNavigation } from '@/lib/navigation';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { BackButton } from '@/components/common/BackButton';

interface Template { templateId: number; templateCode: string; title: string; category: string; }
const CATS: Record<string,string> = { labor:'แรงงาน', accounting:'บัญชี', contracts:'สัญญา', court:'ศาล', sso:'สปส.' };
const STEPS = [{n:1,label:'เลือกเทมเพลต'},{n:2,label:'กรอกข้อมูล'},{n:3,label:'ตรวจดู'},{n:4,label:'ดาวน์โหลด'}];
const DF = { company:'ห้างหุ้นส่วนจำกัด เผ่าปัญญา ทรานสปอร์ต', empName:'', empPosition:'', reason:'', date:new Date().toLocaleDateString('th-TH'), signerName:'', signerTitle:'' };

/** Resolve step badge class (extracted from nested ternary — SonarCloud S3358). */
function getStepBadgeClass(done: boolean, active: boolean): string {
  if (done) return 'bg-green-600 text-white';
  if (active) return 'bg-navy text-white';
  return 'bg-card-soft text-muted-foreground border border-border/60';
}

export function PdfBuilderView({ initialTemplateId }: { readonly initialTemplateId?: number }) {
  const { navigate } = useNavigation();
  const [step, setStep] = useState(initialTemplateId ? 2 : 1);
  const [templates, setTemplates] = useState<Template[]>([]);
  const [loading, setLoading] = useState(true);
  const [selectedId, setSelectedId] = useState<number | null>(initialTemplateId || null);
  const [category, setCategory] = useState('all');
  const [form, setForm] = useState(DF);
  const [pdfUrl, setPdfUrl] = useState<string | null>(null);

  useEffect(() => {
    fetch('/api/templates')
      .then(r => r.json())
      .then(d => {
        const data = d.data || [];
        // Map API fields to our interface (handle both camelCase and snake_case)
        const mapped = data.map((t: any) => ({
          templateId: t.templateId || t.template_id,
          templateCode: t.templateCode || t.template_code,
          title: t.title,
          category: t.category,
        }));
        setTemplates(mapped);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  const sf = (k: string, v: string) => setForm(f => ({ ...f, [k]: v }));
  const selected = templates.find(t => t.templateId === selectedId);
  const filtered = templates.filter(t => category === 'all' || t.category === category);

  return (
    <div className="min-h-screen bg-background">
      {/* Header + Stepper */}
      <div className="bg-card-soft/30 border-b border-border/60">
        <div className="mx-auto max-w-6xl px-4 sm:px-6 pt-5">
          <div className="flex items-center justify-between mb-4">
            <div>
              <div className="text-[10px] uppercase tracking-wider text-gold mb-1">PDF Builder</div>
              <h1 className="text-2xl font-bold" style={{ fontFamily: 'var(--font-ibm-plex-serif)' }}>สร้างเอกสารกฎหมาย</h1>
            </div>
            <BackButton label="กลับ" />
          </div>
          {/* Stepper */}
          <div className="flex items-center pb-5">
            {STEPS.map((s, i) => {
              const a = step === s.n;
              const d = step > s.n;
              return (
                <div key={s.n} className="flex items-center flex-1 last:flex-none">
                  <div className="flex items-center gap-2.5">
                    <div className={`h-8 w-8 rounded-full flex items-center justify-center font-semibold text-sm ${getStepBadgeClass(d, a)}`}>
                      {d ? <Check className="h-4 w-4" strokeWidth={2.5} /> : s.n}
                    </div>
                    <span className={`text-sm ${a || d ? 'font-medium' : 'text-muted-foreground'}`}>{s.label}</span>
                  </div>
                  {i < STEPS.length - 1 && <div className={`flex-1 h-px mx-4 ${d ? 'bg-green-600' : 'bg-border/60'}`} />}
                </div>
              );
            })}
          </div>
        </div>
      </div>

      <div className="mx-auto max-w-6xl px-4 sm:px-6 py-8">
        {/* Step 1: Template Picker */}
        {step === 1 && (
          <div>
            <div className="flex flex-wrap gap-2 mb-5">
              {['all', ...Object.keys(CATS)].map(c => (
                <button type="button" key={c} onClick={() => setCategory(c)} className={`px-3 py-1.5 rounded-full text-xs font-medium border ${category === c ? 'bg-navy text-white border-navy' : 'bg-card-soft text-muted-foreground border-border/50'}`}>{c === 'all' ? 'ทั้งหมด' : CATS[c]}</button>
              ))}
            </div>
            {loading ? (
              <div className="text-center py-20 text-muted-foreground">กำลังโหลด...</div>
            ) : (
              <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
                {filtered.map(t => (
                  <button type="button" key={t.templateId} onClick={() => { setSelectedId(t.templateId); setStep(2); }} className="card-premium rounded-xl p-4 text-left hover:border-gold/40 transition">
                    <div className="h-8 w-10 rounded border border-border/60 bg-card-soft flex items-center justify-center text-[9px] font-bold text-gold mb-3">{t.templateCode}</div>
                    <div className="text-sm font-semibold mb-3 line-clamp-2">{t.title}</div>
                    <div className="text-[11px] text-muted-foreground pt-2 border-t border-border/40">{CATS[t.category] || t.category}</div>
                  </button>
                ))}
              </div>
            )}
          </div>
        )}

        {/* Step 2: Fill Form */}
        {step === 2 && selected && (
          <div className="max-w-2xl mx-auto">
            <div className="card-premium rounded-xl p-6">
              <h2 className="text-lg font-semibold mb-1">กรอกข้อมูล</h2>
              <p className="text-sm text-muted-foreground mb-6"><span className="text-gold font-semibold">{selected.templateCode}</span> — {selected.title}</p>
              <div className="grid gap-4 sm:grid-cols-2">
                <div><label htmlFor="pdf-company" className="block text-xs font-medium text-muted-foreground mb-1.5">ชื่อบริษัท</label><input id="pdf-company" type="text" value={form.company} onChange={e => sf('company', e.target.value)} className="w-full px-3 py-2 text-sm rounded-lg border border-border/50 bg-card-soft outline-none focus:border-gold/40" /></div>
                <div><label htmlFor="pdf-date" className="block text-xs font-medium text-muted-foreground mb-1.5">วันที่</label><input id="pdf-date" type="text" value={form.date} onChange={e => sf('date', e.target.value)} className="w-full px-3 py-2 text-sm rounded-lg border border-border/50 bg-card-soft outline-none focus:border-gold/40" /></div>
                <div><label htmlFor="pdf-emp-name" className="block text-xs font-medium text-muted-foreground mb-1.5">ชื่อพนักงาน</label><input id="pdf-emp-name" type="text" value={form.empName} onChange={e => sf('empName', e.target.value)} placeholder="นาย ก." className="w-full px-3 py-2 text-sm rounded-lg border border-border/50 bg-card-soft outline-none focus:border-gold/40" /></div>
                <div><label htmlFor="pdf-emp-position" className="block text-xs font-medium text-muted-foreground mb-1.5">ตำแหน่ง</label><input id="pdf-emp-position" type="text" value={form.empPosition} onChange={e => sf('empPosition', e.target.value)} className="w-full px-3 py-2 text-sm rounded-lg border border-border/50 bg-card-soft outline-none focus:border-gold/40" /></div>
                <div className="sm:col-span-2"><label htmlFor="pdf-reason" className="block text-xs font-medium text-muted-foreground mb-1.5">เหตุผล/หมายเหตุ</label><input id="pdf-reason" type="text" value={form.reason} onChange={e => sf('reason', e.target.value)} className="w-full px-3 py-2 text-sm rounded-lg border border-border/50 bg-card-soft outline-none focus:border-gold/40" /></div>
                <div><label htmlFor="pdf-signer-name" className="block text-xs font-medium text-muted-foreground mb-1.5">ชื่อผู้ลงนาม</label><input id="pdf-signer-name" type="text" value={form.signerName} onChange={e => sf('signerName', e.target.value)} className="w-full px-3 py-2 text-sm rounded-lg border border-border/50 bg-card-soft outline-none focus:border-gold/40" /></div>
                <div><label htmlFor="pdf-signer-title" className="block text-xs font-medium text-muted-foreground mb-1.5">ตำแหน่งผู้ลงนาม</label><input id="pdf-signer-title" type="text" value={form.signerTitle} onChange={e => sf('signerTitle', e.target.value)} className="w-full px-3 py-2 text-sm rounded-lg border border-border/50 bg-card-soft outline-none focus:border-gold/40" /></div>
              </div>
              <div className="flex justify-between mt-6">
                <Button type="button" variant="ghost" onClick={() => setStep(1)}><ArrowLeft className="h-4 w-4" /> ย้อนกลับ</Button>
                <Button type="button" onClick={() => setStep(3)} className="bg-navy text-white">ตรวจดู <ArrowRight className="h-4 w-4" /></Button>
              </div>
            </div>
          </div>
        )}

        {/* Step 3: Preview */}
        {step === 3 && selected && (
          <div className="max-w-3xl mx-auto">
            <div className="card-premium rounded-xl p-6">
              <h2 className="text-lg font-semibold mb-4">ตรวจสอบก่อนดาวน์โหลด</h2>
              <div className="bg-card-soft/50 rounded-lg p-6 border border-border/40 mb-6">
                <div className="text-center mb-4">
                  <div className="font-bold text-lg">{form.company}</div>
                  <Badge variant="outline" className="badge-gold text-xs mt-2">{selected.templateCode}</Badge>
                  <h3 className="text-xl font-bold mt-2">{selected.title}</h3>
                </div>
                <div className="text-sm space-y-1.5">
                  <div><span className="text-muted-foreground">วันที่:</span> {form.date}</div>
                  {form.empName && <div><span className="text-muted-foreground">พนักงาน:</span> {form.empName}</div>}
                  {form.empPosition && <div><span className="text-muted-foreground">ตำแหน่ง:</span> {form.empPosition}</div>}
                  {form.reason && <div><span className="text-muted-foreground">เหตุผล:</span> {form.reason}</div>}
                </div>
                <div className="mt-6 text-right text-sm">
                  <div className="text-muted-foreground">ผู้ลงนาม</div>
                  <div className="font-semibold mt-1">{form.signerName}</div>
                  <div className="text-xs text-muted-foreground">{form.signerTitle}</div>
                </div>
              </div>
              <div className="flex justify-between">
                <Button type="button" variant="ghost" onClick={() => setStep(2)}><ArrowLeft className="h-4 w-4" /> แก้ไข</Button>
                <Button type="button" onClick={() => { setStep(4); setPdfUrl(`/api/templates/pdf?id=${selected.templateId}&employee=${encodeURIComponent(form.empName)}&position=${encodeURIComponent(form.empPosition)}&startDate=${encodeURIComponent(form.date)}`); }} className="bg-gold text-navy">ดาวน์โหลด PDF <Download className="h-4 w-4" /></Button>
              </div>
            </div>
          </div>
        )}

        {/* Step 4: Download */}
        {step === 4 && selected && (
          <div className="max-w-2xl mx-auto text-center py-12">
            <div className="card-premium rounded-xl p-10">
              <div className="h-16 w-16 rounded-full bg-green-500/15 flex items-center justify-center mx-auto mb-4"><Check className="h-8 w-8 text-green-600" strokeWidth={2.5} /></div>
              <h2 className="text-xl font-bold mb-2">เอกสารพร้อมดาวน์โหลด!</h2>
              <p className="text-sm text-muted-foreground mb-6">{selected.templateCode} — {selected.title}</p>
              {pdfUrl && <a href={pdfUrl} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-2 px-6 py-3 bg-gold text-navy font-semibold rounded-lg hover:bg-gold/90"><Download className="h-5 w-5" /> ดาวน์โหลด PDF</a>}
              <div className="mt-6 flex justify-center gap-3">
                <Button type="button" variant="ghost" onClick={() => setStep(1)}><Wand2 className="h-4 w-4" /> สร้างใหม่</Button>
                <Button type="button" variant="ghost" onClick={() => navigate({ name: 'home' })}>กลับหน้าแรก</Button>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
