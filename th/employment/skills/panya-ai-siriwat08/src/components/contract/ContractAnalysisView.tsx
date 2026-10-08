'use client';
import { useState, useRef, useCallback } from 'react';
import { Shield, AlertTriangle, CheckCircle, Loader2, FileSearch, Upload, FileText, X, Layers } from 'lucide-react';

import { Button } from '@/components/ui/button';
import { BackButton } from '@/components/common/BackButton';
import { extractPdfPages, formatFileSize, type PDFPagesResult } from '@/lib/pdf-extract';
import { chunkContractPages, formatChunkingSummary, type ChunkingResult, type ContractChunk } from '@/lib/contract-chunker';

interface ChunkResult {
  chunkIndex: number;
  pageRange: string;
  answer: string;
  citations: Array<{ index: number; type: string; id: number; label: string; ref: string; snippet: string; url: string }>;
  error?: string;
}

export function ContractAnalysisView() {
  const [pdfLoading, setPdfLoading] = useState(false);
  const [pdfProgress, setPdfProgress] = useState<string | null>(null);
  const [pdfInfo, setPdfInfo] = useState<PDFPagesResult | null>(null);
  const [chunkingResult, setChunkingResult] = useState<ChunkingResult | null>(null);
  const [analyzing, setAnalyzing] = useState(false);
  const [chunkResults, setChunkResults] = useState<ChunkResult[]>([]);
  const [currentChunk, setCurrentChunk] = useState<number>(-1);
  const [error, setError] = useState<string | null>(null);
  const [dragOver, setDragOver] = useState(false);
  const [manualText, setManualText] = useState('');
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handlePDFFile = useCallback(async (file: File) => {
    setPdfLoading(true);
    setError(null);
    setPdfProgress('กำลังโหลด PDF...');
    setPdfInfo(null);
    setChunkingResult(null);
    setChunkResults([]);
    setManualText('');

    try {
      const result = await extractPdfPages(file, (currentPage, totalPages) => {
        setPdfProgress(`กำลังอ่านหน้า ${currentPage}/${totalPages}...`);
      });

      setPdfInfo(result);
      setPdfProgress(null);

      // Auto-chunk the pages
      const chunked = chunkContractPages(result.pages);
      setChunkingResult(chunked);
    } catch (err: unknown) {
      const message = err instanceof Error ? err.message : 'ไม่สามารถอ่าน PDF ได้';
      setError(message);
      setPdfProgress(null);
    } finally {
      setPdfLoading(false);
    }
  }, []);

  const handleFileSelect = (e: React.SyntheticEvent) => {
    const target = e.target as HTMLInputElement;
    const file = target.files?.[0];
    if (file) handlePDFFile(file);
    target.value = '';
  };

  const handleDrop = (e: React.SyntheticEvent) => {
    e.preventDefault();
    setDragOver(false);
    const dragEvent = e as unknown as DragEvent;
    const file = dragEvent.dataTransfer?.files?.[0];
    if (file) handlePDFFile(file);
  };

  const handleDragOver = (e: React.SyntheticEvent) => {
    e.preventDefault();
    setDragOver(true);
  };

  const handleDragLeave = (e: React.SyntheticEvent) => {
    e.preventDefault();
    setDragOver(false);
  };

  const clearAll = () => {
    setPdfInfo(null);
    setChunkingResult(null);
    setChunkResults([]);
    setError(null);
    setManualText('');
  };

  const analyzeChunk = async (chunk: ContractChunk, totalChunks: number) => {
    try {
      const res = await fetch('/api/contracts/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          chunk: chunk.text,
          chunkIndex: chunk.index,
          totalChunks,
          pageRange: chunk.pageRange,
        }),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      return {
        chunkIndex: chunk.index,
        pageRange: chunk.pageRange,
        answer: data.answer || 'ไม่สามารถวิเคราะห์ได้',
        citations: data.citations || [],
      } as ChunkResult;
    } catch (err: unknown) {
      const message = err instanceof Error ? err.message : 'Unknown error';
      return {
        chunkIndex: chunk.index,
        pageRange: chunk.pageRange,
        answer: '',
        citations: [],
        error: message,
      } as ChunkResult;
    }
  };

  const analyzeAllChunks = async () => {
    if (!chunkingResult || chunkingResult.chunks.length === 0) return;
    setAnalyzing(true);
    setChunkResults([]);
    setError(null);

    const results: ChunkResult[] = [];
    for (let i = 0; i < chunkingResult.chunks.length; i++) {
      setCurrentChunk(i);
      const chunk = chunkingResult.chunks[i];
      const result = await analyzeChunk(chunk, chunkingResult.chunks.length);
      results.push(result);
      setChunkResults([...results]);
    }

    setCurrentChunk(-1);
    setAnalyzing(false);
  };

  const analyzeManualText = async () => {
    if (!manualText.trim()) return;
    setAnalyzing(true);
    setError(null);
    setChunkResults([]);

    // Treat manual text as a single chunk
    const fakeChunk: ContractChunk = {
      index: 0,
      text: manualText,
      charCount: manualText.length,
      pageRange: 'ข้อความที่ป้อน',
      startPage: 1,
      endPage: 1,
    };

    setCurrentChunk(0);
    const result = await analyzeChunk(fakeChunk, 1);
    setChunkResults([result]);
    setCurrentChunk(-1);
    setAnalyzing(false);
  };

  return (
    <div className="mx-auto max-w-3xl px-4 sm:px-6 py-8">
      <BackButton label="ย้อนกลับ" />
      <div className="flex items-center gap-2 mb-2">
        <FileSearch className="h-6 w-6 text-gold" />
        <h1 className="text-2xl sm:text-3xl font-bold" style={{ fontFamily: 'var(--font-ibm-plex-serif)' }}>วิเคราะห์สัญญา</h1>
      </div>
      <p className="text-sm text-muted-foreground mb-4">
        อัปโหลด PDF ขนาดไหนก็ได้ → ระบบแยกข้อความ + กรองหน้าไม่จำเป็น + แบ่งส่วนวิเคราะห์อัตโนมัติ
      </p>

      {/* Privacy notice */}
      <div className="card-premium rounded-lg p-3 mb-4 border-blue-500/20 bg-blue-500/5">
        <p className="text-xs text-muted-foreground flex items-start gap-2">
          <Shield className="h-4 w-4 text-blue-500 flex-shrink-0 mt-0.5" />
          <span>
            <strong>Privacy 100%</strong> — PDF ถูกประมวลผลในเบราว์เซอร์ ไม่ส่งไฟล์ไปเซิร์ฟเวอร์
            ระบบแบ่งเนื้อหาเป็นส่วนๆ แล้วส่งเฉพาะข้อความไปวิเคราะห์
          </span>
        </p>
      </div>

      {/* PDF upload zone (only when no PDF loaded) */}
      {!pdfInfo && !pdfLoading && (
        <div className="card-premium rounded-xl p-6 mb-6">
          <div
            onDrop={handleDrop}
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            className={`border-2 border-dashed rounded-lg p-8 text-center transition-colors mb-4 ${
              dragOver ? 'border-gold bg-gold/5' : 'border-border/50 hover:border-gold/30'
            }`}
          >
            <input ref={fileInputRef} type="file" accept="application/pdf,.pdf" onChange={handleFileSelect} className="hidden" />
            <Upload className={`h-10 w-10 mx-auto mb-3 ${dragOver ? 'text-gold' : 'text-muted-foreground'}`} />
            <p className="text-sm font-medium mb-1">ลากไฟล์ PDF มาวางที่นี่ หรือ</p>
            <button type="button" onClick={() => fileInputRef.current?.click()} className="text-sm text-gold hover:text-gold/80 transition underline">
              เลือกไฟล์จากเครื่อง
            </button>
            <p className="text-xs text-muted-foreground mt-2">ไม่จำกัดขนาดไฟล์ — ระบบแบ่งเนื้อหาอัตโนมัติ</p>
          </div>

          {/* OR manual text input */}
          <div className="border-t border-border/30 pt-4">
            <label htmlFor="manual-text" className="block text-sm font-medium mb-2">หรือวางข้อความสัญญาโดยตรง</label>
            <textarea
              id="manual-text"
              value={manualText}
              onChange={e => setManualText(e.target.value)}
              placeholder="วางข้อความสัญญาที่นี่..."
              rows={4}
              className="w-full px-4 py-3 text-sm rounded-lg border border-border/50 bg-card-soft outline-none focus:border-gold/40 resize-y"
            />
            <div className="flex justify-end mt-3">
              <Button type="button" onClick={analyzeManualText} disabled={analyzing || !manualText.trim()} className="bg-gold text-navy gap-2">
                {analyzing ? <Loader2 className="h-4 w-4 animate-spin" /> : <Shield className="h-4 w-4" />}
                {analyzing ? 'กำลังวิเคราะห์...' : 'วิเคราะห์สัญญา'}
              </Button>
            </div>
          </div>
        </div>
      )}

      {/* PDF loading */}
      {pdfLoading && (
        <div className="card-premium rounded-xl p-8 text-center mb-6">
          <Loader2 className="h-8 w-8 animate-spin text-gold mx-auto mb-4" />
          <p className="text-sm text-muted-foreground">{pdfProgress || 'กำลังประมวลผล...'}</p>
        </div>
      )}

      {/* PDF info + chunking summary */}
      {pdfInfo && chunkingResult && !pdfLoading && (
        <div className="card-premium rounded-xl p-6 mb-6">
          <div className="flex items-center gap-3 mb-4">
            <FileText className="h-5 w-5 text-green-600 flex-shrink-0" />
            <div className="flex-1 min-w-0">
              <p className="text-sm font-medium truncate">{pdfInfo.fileName}</p>
              <p className="text-xs text-muted-foreground">
                {pdfInfo.pageCount} หน้า · {formatFileSize(pdfInfo.fileSize)} · {pdfInfo.totalChars.toLocaleString()} ตัวอักษร
              </p>
            </div>
            <button type="button" onClick={clearAll} className="text-muted-foreground hover:text-red-500 transition flex-shrink-0">
              <X className="h-5 w-5" />
            </button>
          </div>

          {/* Chunking summary */}
          <div className="bg-card-soft rounded-lg p-4 mb-4">
            <div className="flex items-center gap-2 mb-2">
              <Layers className="h-4 w-4 text-gold" />
              <span className="text-sm font-medium">แบ่งเป็น {chunkingResult.totalChunks} ส่วน</span>
            </div>
            <pre className="text-xs text-muted-foreground whitespace-pre-wrap">{formatChunkingSummary(chunkingResult)}</pre>
          </div>

          {/* Analyze button */}
          <Button type="button" onClick={analyzeAllChunks} disabled={analyzing} className="w-full bg-gold text-navy gap-2">
            {analyzing ? <Loader2 className="h-4 w-4 animate-spin" /> : <Shield className="h-4 w-4" />}
            {analyzing
              ? `กำลังวิเคราะห์ส่วน ${currentChunk + 1}/${chunkingResult.totalChunks}...`
              : `เริ่มวิเคราะห์ทั้ง ${chunkingResult.totalChunks} ส่วน`}
          </Button>
        </div>
      )}

      {/* Error */}
      {error && (
        <div className="card-premium rounded-xl p-6 mb-4 border-destructive/30">
          <div className="flex items-center gap-2 mb-2"><AlertTriangle className="h-5 w-5 text-red-500" /><h2 className="text-lg font-semibold">เกิดข้อผิดพลาด</h2></div>
          <p className="text-sm text-muted-foreground">{error}</p>
        </div>
      )}

      {/* Chunk results */}
      {chunkResults.length > 0 && (
        <div className="space-y-4">
          {chunkResults.map((result, i) => (
            <div key={`chunk-${result.chunkIndex}-${result.pageRange}`} className="card-premium rounded-xl p-6">
              <div className="flex items-center gap-2 mb-3">
                <span className="text-xs font-bold px-2 py-1 rounded bg-gold/20 text-gold">
                  ส่วน {result.chunkIndex + 1}
                </span>
                <span className="text-xs text-muted-foreground">{result.pageRange}</span>
                {result.error && <span className="text-xs text-red-500">⚠️ {result.error}</span>}
              </div>

              {/* Citations for this chunk */}
              {result.citations.length > 0 && (
                <div className="mb-3 space-y-1">
                  {result.citations.slice(0, 3).map((c, ci) => (
                    <div key={`cit-${i}-${ci}`} className="text-xs p-2 rounded bg-red-500/5 border border-red-500/10">
                      <span className="text-red-500 font-medium">⚠️ {c.label}</span>
                      <span className="text-muted-foreground ml-2">{c.snippet.slice(0, 100)}...</span>
                    </div>
                  ))}
                </div>
              )}

              {/* AI analysis */}
              {result.answer && (
                <div className="text-sm prose-thai whitespace-pre-wrap leading-relaxed">{result.answer}</div>
              )}
            </div>
          ))}

          {/* Summary recommendation */}
          {!analyzing && chunkResults.length > 1 && (
            <div className="card-premium rounded-xl p-6">
              <div className="flex items-center gap-2 mb-3"><CheckCircle className="h-5 w-5 text-green-600" /><h2 className="text-lg font-semibold">สรุปการวิเคราะห์</h2></div>
              <ul className="space-y-2">
                <li className="flex items-start gap-2 text-sm"><span className="text-gold font-bold">1.</span><span>วิเคราะห์ครบ {chunkResults.length} ส่วน</span></li>
                <li className="flex items-start gap-2 text-sm"><span className="text-gold font-bold">2.</span><span>ตรวจสอบข้อที่ผิดกฎหมายในแต่ละส่วนแล้ว</span></li>
                <li className="flex items-start gap-2 text-sm"><span className="text-gold font-bold">3.</span><span>แก้ไขข้อที่ผิดกฎหมายก่อนลงนาม</span></li>
                <li className="flex items-start gap-2 text-sm"><span className="text-gold font-bold">4.</span><span>ปรึกษาทนายความตรวจสอบขั้นสุดท้าย</span></li>
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
