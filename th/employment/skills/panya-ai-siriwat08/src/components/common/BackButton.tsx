'use client';

import { ArrowLeft } from 'lucide-react';
import { useNavigation } from '@/lib/navigation';
import { Button } from '@/components/ui/button';

/**
 * Reusable back button — uses browser history to go back.
 * Falls back to home page if no history.
 */
export function BackButton({ label = 'ย้อนกลับ' }: { readonly label?: string }) {
  const { navigate } = useNavigation();

  const handleBack = () => {
    if (typeof window !== 'undefined' && window.history.length > 1) {
      window.history.back();
    } else {
      navigate({ name: 'home' });
    }
  };

  return (
    <Button
      type="button"
      variant="ghost"
      size="sm"
      onClick={handleBack}
      className="mb-4 gap-1 text-muted-foreground hover:text-foreground"
    >
      <ArrowLeft className="h-4 w-4" />
      {label}
    </Button>
  );
}
