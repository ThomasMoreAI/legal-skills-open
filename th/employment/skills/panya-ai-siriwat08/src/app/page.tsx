import { ErrorBoundary } from '@/components/ErrorBoundary';
import { AppShell } from '@/components/AppShell';

export default function Home() {
  return (
    <ErrorBoundary>
      <AppShell />
    </ErrorBoundary>
  );
}
