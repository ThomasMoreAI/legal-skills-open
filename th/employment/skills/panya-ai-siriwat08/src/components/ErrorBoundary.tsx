'use client';

import React from 'react';

interface State {
  hasError: boolean;
  error: Error | null;
}

export class ErrorBoundary extends React.Component<{ children: React.ReactNode }, State> {
  constructor(props: { children: React.ReactNode }) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
    console.error('ErrorBoundary caught:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div style={{ padding: '20px', fontFamily: 'monospace', fontSize: '14px' }}>
          <h2 style={{ color: 'red' }}>⚠️ เกิดข้อผิดพลาด</h2>
          <pre style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-all', marginTop: '10px' }}>
            {this.state.error?.message || 'Unknown error'}
          </pre>
          <pre style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-all', marginTop: '10px', fontSize: '12px', color: '#666' }}>
            {this.state.error?.stack?.slice(0, 1000)}
          </pre>
          <button type="button" onClick={() => this.setState({ hasError: false, error: null })}
            style={{ marginTop: '10px', padding: '5px 15px', cursor: 'pointer' }}
          >
            ลองใหม่
          </button>
        </div>
      );
    }
    return this.props.children;
  }
}
