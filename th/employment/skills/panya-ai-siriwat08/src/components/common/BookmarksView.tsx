'use client';

import { useEffect, useState } from 'react';
import { Bookmark, Trash2, ChevronRight, Scale, BookOpen } from 'lucide-react';
import { useBookmarks } from '@/lib/navigation';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';

interface BookmarkItem {
  type: 'section' | 'judgment' | 'law';
  id: number;
  label: string;
  url: string;
  savedAt: string;
}

export function BookmarksView() {
  const { navigate, getBookmarks, removeBookmark } = useBookmarks() as any;
  const [items, setItems] = useState<BookmarkItem[]>([]);

  const refresh = () => setItems(getBookmarks());
  useEffect(() => {
    refresh();
    window.addEventListener('bookmarks-changed', refresh);
    return () => window.removeEventListener('bookmarks-changed', refresh);
  }, [getBookmarks]);

  const handleRemove = (type: string, id: number) => {
    removeBookmark(type, id);
    refresh();
  };

  const handleNavigate = (item: BookmarkItem) => {
    const params = new URLSearchParams(item.url.split('?')[1] || '');
    const view = params.get('view');
    const id = params.get('id');
    if (view === 'law' && id) navigate({ name: 'law', lawId: Number.parseInt(id, 10) });
    else if (view === 'section' && id) navigate({ name: 'section', sectionId: Number.parseInt(id, 10) });
    else if (view === 'judgment' && id) navigate({ name: 'judgment', judgmentId: Number.parseInt(id, 10) });
  };

  return (
    <div className="mx-auto max-w-3xl px-4 sm:px-6 py-8">
      <div className="mb-6">
        <h1 className="flex items-center gap-2 text-2xl sm:text-3xl font-bold mb-2">
          <Bookmark className="h-7 w-7 text-gold" />
          รายการบันทึก
        </h1>
        <p className="text-sm text-muted-foreground">
          มาตรา/ฎีกา/กฎหมายที่คุณบันทึกไว้ (เก็บในเบราว์เซอร์ของคุณ)
        </p>
      </div>

      {items.length === 0 ? (
        <div className="card-premium rounded-xl p-12 text-center">
          <Bookmark className="h-12 w-12 mx-auto mb-4 text-muted-foreground/50" />
          <p className="text-muted-foreground mb-2">ยังไม่มีรายการบันทึก</p>
          <p className="text-xs text-muted-foreground/70 mb-6">
            คลิกปุ่ม "บันทึก" ที่มาตราหรือฎีกาเพื่อเพิ่มลงรายการนี้
          </p>
          <Button
            onClick={() => navigate({ name: 'laws' })}
            className="bg-gold text-navy hover:bg-gold/90"
          >
            สำรวจกฎหมาย
          </Button>
        </div>
      ) : (
        <div className="space-y-3">
          {items.map(item => (
            <div key={`${item.type}-${item.id}`} className="card-premium rounded-xl p-4 flex items-center gap-3">
              <div className="flex-shrink-0">
                <div className={`flex h-10 w-10 items-center justify-center rounded-lg ${
                  item.type === 'judgment'
                    ? 'bg-gold/15 border border-gold/30'
                    : 'bg-card-softer border border-border/40'
                }`}>
                  {item.type === 'judgment' ? (
                    <Scale className="h-5 w-5 text-gold" />
                  ) : (
                    <BookOpen className="h-5 w-5 text-foreground" />
                  )}
                </div>
              </div>
              <button type="button" onClick={() => handleNavigate(item)}
                className="flex-1 text-left group min-w-0"
              >
                <div className="flex items-center gap-2 mb-1">
                  <Badge variant="outline" className="text-[10px]">
                    {getBookmarkTypeLabel(item.type)}
                  </Badge>
                  <span className="text-[10px] text-muted-foreground">
                    {new Date(item.savedAt).toLocaleDateString('th-TH', {
                      year: 'numeric', month: 'short', day: 'numeric',
                    })}
                  </span>
                </div>
                <div className="text-sm font-medium text-foreground group-hover:text-gold transition truncate">
                  {item.label}
                </div>
              </button>
              <ChevronRight className="h-4 w-4 text-muted-foreground" />
              <Button
                variant="ghost"
                size="sm"
                onClick={() => handleRemove(item.type, item.id)}
                className="text-muted-foreground hover:text-destructive"
              >
                <Trash2 className="h-3.5 w-3.5" />
              </Button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

/** Resolves the Thai label for a bookmark type — extracted to satisfy S3358 (no nested ternary). */
function getBookmarkTypeLabel(type: 'section' | 'judgment' | 'law'): string {
  if (type === 'judgment') return 'ฎีกา';
  if (type === 'law') return 'กฎหมาย';
  return 'มาตรา';
}
