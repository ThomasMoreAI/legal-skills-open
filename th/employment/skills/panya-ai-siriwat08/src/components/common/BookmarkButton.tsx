'use client';

import { useEffect, useState } from 'react';
import { Bookmark, BookmarkCheck } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { useBookmarks } from '@/lib/navigation';
import { toast } from 'sonner';

interface Props {
  readonly type: 'section' | 'judgment' | 'law';
  readonly id: number;
  readonly label: string;
  readonly url: string;
}

export function BookmarkButton({ type, id, label, url }: Props) {
  const { isBookmarked, addBookmark, removeBookmark } = useBookmarks();
  const [bookmarked, setBookmarked] = useState(() => isBookmarked(type, id));

  useEffect(() => {
    const handler = () => setBookmarked(isBookmarked(type, id));
    window.addEventListener('bookmarks-changed', handler);
    return () => window.removeEventListener('bookmarks-changed', handler);
  }, [type, id, isBookmarked]);

  const toggle = (e: React.MouseEvent) => {
    e.stopPropagation();
    e.preventDefault();
    if (bookmarked) {
      removeBookmark(type, id);
      setBookmarked(false);
      toast.success('นำออกจากบันทึกแล้ว');
    } else {
      addBookmark({ type, id, label, url });
      setBookmarked(true);
      toast.success('บันทึกแล้ว');
    }
  };

  return (
    <Button
      variant="ghost"
      size="sm"
      onClick={toggle}
      className={`gap-1 text-xs ${bookmarked ? 'text-gold' : 'text-muted-foreground'}`}
      aria-label={bookmarked ? 'นำออกจากบันทึก' : 'บันทึก'}
    >
      {bookmarked ? <BookmarkCheck className="h-3.5 w-3.5" /> : <Bookmark className="h-3.5 w-3.5" />}
      {bookmarked ? 'บันทึกแล้ว' : 'บันทึก'}
    </Button>
  );
}
