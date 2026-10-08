/**
 * LLM client — supports multiple providers via env vars.
 *
 * Provider selection (in priority order):
 * 1. OPENROUTER_API_KEY + OPENROUTER_MODEL → OpenRouter (recommended)
 * 2. Z_AI_API_KEY + Z_AI_MODEL → Z.AI (legacy)
 *
 * OpenRouter: https://openrouter.ai — supports free models like
 *   - inclusionai/ling-3.0-flash:free
 *   - meta-llama/llama-3.3-70b-instruct
 *   - qwen/qwen3.7-flash
 *
 * Z.AI: https://z.ai — requires paid balance
 *   - glm-4.6, glm-4.5-flash
 */

export interface ChatMessage {
  role: 'system' | 'user' | 'assistant';
  content: string;
}

export async function createChatCompletion(
  messages: ChatMessage[],
  options: { stream?: boolean; model?: string } = {}
): Promise<{ content: string; raw: any }> {
  // ============ Provider 1: OpenRouter (recommended) ============
  if (process.env.OPENROUTER_API_KEY) {
    return await callOpenRouter(messages, options);
  }

  // ============ Provider 2: Z.AI (legacy) ============
  if (process.env.Z_AI_API_KEY) {
    return await callZai(messages, options);
  }

  throw new Error('No LLM API key configured. Set OPENROUTER_API_KEY or Z_AI_API_KEY env var.');
}

// ============ OpenRouter ============
async function callOpenRouter(
  messages: ChatMessage[],
  options: { stream?: boolean; model?: string }
): Promise<{ content: string; raw: any }> {
  const url = 'https://openrouter.ai/api/v1/chat/completions';
  // Default: NVIDIA Nemotron 3 Ultra (free) — override via OPENROUTER_MODEL env
  const model = options.model || process.env.OPENROUTER_MODEL || 'inclusionai/ling-3.0-flash:free';

  const body: any = {
    model,
    messages,
    stream: false,
    ...options,
  };

  console.log('[llm] OpenRouter model:', model, 'messages:', messages.length);

  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${process.env.OPENROUTER_API_KEY}`,
      'HTTP-Referer': 'https://panya-ai.vercel.app',
      'X-Title': 'Panya-AI',
    },
    body: JSON.stringify(body),
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`OpenRouter API HTTP ${response.status}: ${errorText.slice(0, 500)}`);
  }

  const raw: any = await response.json();

  if (raw?.error) {
    const errMsg = typeof raw.error === 'string' ? raw.error : (raw.error.message || JSON.stringify(raw.error));
    throw new Error(`OpenRouter API body error: ${errMsg.slice(0, 300)}`);
  }

  const content =
    raw?.choices?.[0]?.message?.content ??
    raw?.choices?.[0]?.delta?.content ??
    raw?.content ??
    null;

  if (!content) {
    console.error('[llm] OpenRouter unexpected response:', JSON.stringify(raw).slice(0, 500));
  }

  return { content: content || '', raw };
}

// ============ Z.AI (legacy) ============
async function callZai(
  messages: ChatMessage[],
  options: { stream?: boolean; model?: string }
): Promise<{ content: string; raw: any }> {
  const url = 'https://api.z.ai/api/paas/v4/chat/completions';
  const model = options.model || process.env.Z_AI_MODEL || 'glm-4.6';

  const body: any = {
    model,
    messages,
    stream: false,
    ...options,
  };

  console.log('[llm] Z.AI model:', model, 'messages:', messages.length);

  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${process.env.Z_AI_API_KEY}`,
      'X-Z-AI-From': 'Z',
    },
    body: JSON.stringify(body),
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`Z.AI API HTTP ${response.status}: ${errorText.slice(0, 500)}`);
  }

  const raw: any = await response.json();

  if (raw?.error) {
    const errMsg = typeof raw.error === 'string' ? raw.error : (raw.error.message || JSON.stringify(raw.error));
    throw new Error(`Z.AI API body error: ${errMsg.slice(0, 300)}`);
  }

  const content =
    raw?.choices?.[0]?.message?.content ??
    raw?.choices?.[0]?.delta?.content ??
    raw?.content ??
    raw?.result?.content ??
    raw?.choices?.[0]?.text ??
    null;

  if (!content) {
    console.error('[llm] Z.AI unexpected response:', JSON.stringify(raw).slice(0, 500));
  }

  return { content: content || '', raw };
}
