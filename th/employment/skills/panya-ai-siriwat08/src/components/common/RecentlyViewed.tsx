'use client';

import { useEffect, useState } from 'react';
import { Clock, BookOpen, Scale, FileText } from 'lucide-react';
import { useNavigation } from '@/lib/navigation';
import { getRecentlyViewed, clearRecentlyViewed, type RecentlyViewedItem } from '@/lib/recently-viewed';

export function RecentlyViewed() {
  const { navigate } = useNavigation();
  const [items, setItems] = useState<RecentlyViewedItem[]>([]);

  useEffect(() => {
    const update = () => setItems(getRecentlyViewed());
    update();
    window.addEventListener('panya-recently-viewed-changed', update);
    return () => window.removeEventListener('panya-recently-viewed-changed', update);
  }, []);

  if (items.length === 0) return null;

  const getIcon = (type: string) => {
    if (type === 'law') return BookOpen;
    if (type === 'judgment') return Scale;
    return FileText;
  };

  const handleClick = (item: RecentlyViewedItem) => {
    if (item.type === 'law') navigate({ name: 'law', lawId: item.id });
    else if (item.type === 'section') navigate({ name: 'section', sectionId: item.id });
    else if (item.type === 'judgment') navigate({ name: 'judgment', judgmentId: item.id });
  };

  return (
    <div className="px-3 py-2">
      <div className="flex items-center justify-between mb-2">
        <span className="text-[10px] font-semibold uppercase tracking-wider text-muted-foreground flex items-center gap-1">
          <Clock className="h-3 w-3" />
          ดูล่าสุด
        </span>
        <button
          type="button"
          onClick={() => { clearRecentlyViewed(); }}
          className="text-[10px] text-muted-foreground hover:text-foreground"
          aria-label="ล้างประวัติ"
        >
          ล้าง
        </button>
      </div>
      <div className="space-y-0.5 max-h-48 overflow-y-auto">
        {items.slice(0, 8).map((item, i) => {
          const Icon = getIcon(item.type);
          return (
            <button
              type="button"
              key={`${item.type}-${item.id}-${i}`}
              onClick={() => handleClick(item)}
              className="flex w-full items-center gap-2 rounded-lg border-l-2 border-transparent px-2 py-1.5 text-xs text-muted-foreground hover:bg-accent/50 hover:text-foreground transition text-left"
            >
              <Icon className="h-3 w-3 flex-shrink-0" />
              <span className="flex-1 truncate">{item.label}</span>
            </button>
          );
        })}
      </div>
    </div>
  );
}
