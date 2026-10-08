// Chat Session Storage — saves chat conversations to localStorage
// so users can resume previous conversations.

export interface SavedChatMessage {
  role: 'user' | 'assistant';
  content: string;
  uid: string;
  citations?: Array<{
    index: number;
    type: string;
    id: number;
    label: string;
    ref: string;
    snippet: string;
    url: string;
  }>;
  retrievedChunks?: number;
  error?: boolean;
}

export interface ChatSession {
  id: string;
  title: string; // First user question (truncated)
  messages: SavedChatMessage[];
  persona?: string | null;
  createdAt: string;
  updatedAt: string;
}

const STORAGE_KEY = 'panya_chat_sessions';
const MAX_SESSIONS = 10;

export function getChatSessions(): ChatSession[] {
  if (typeof window === 'undefined') return [];
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return [];
    const sessions = JSON.parse(raw) as ChatSession[];
    return Array.isArray(sessions) ? sessions : [];
  } catch {
    return [];
  }
}

export function saveChatSession(session: ChatSession): void {
  if (typeof window === 'undefined') return;
  try {
    const sessions = getChatSessions();
    // Remove existing session with same id
    const filtered = sessions.filter(s => s.id !== session.id);
    // Add/update session at front
    filtered.unshift({ ...session, updatedAt: new Date().toISOString() });
    // Trim to max
    const trimmed = filtered.slice(0, MAX_SESSIONS);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(trimmed));
    window.dispatchEvent(new Event('panya-chat-sessions-changed'));
  } catch {
    // localStorage might be full
  }
}

export function deleteChatSession(id: string): void {
  if (typeof window === 'undefined') return;
  try {
    const sessions = getChatSessions();
    const filtered = sessions.filter(s => s.id !== id);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(filtered));
    window.dispatchEvent(new Event('panya-chat-sessions-changed'));
  } catch {
    // ignore
  }
}

export function clearAllChatSessions(): void {
  if (typeof window === 'undefined') return;
  localStorage.removeItem(STORAGE_KEY);
  window.dispatchEvent(new Event('panya-chat-sessions-changed'));
}

/** Create a new chat session from messages. */
export function createChatSession(
  messages: SavedChatMessage[],
  persona?: string | null
): ChatSession {
  const firstUserMsg = messages.find(m => m.role === 'user');
  let title = 'การสนทนาใหม่';
  if (firstUserMsg) {
    const truncated = firstUserMsg.content.slice(0, 60);
    title = firstUserMsg.content.length > 60 ? truncated + '...' : truncated;
  }

  return {
    id: `chat-${Date.now()}`,
    title,
    messages,
    persona,
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
  };
}
