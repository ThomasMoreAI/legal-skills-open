'use strict';

/**
 * regulatory-compliance post-execute hook
 * Emits observability event via send-event.cjs per Iron Law III.
 * Events are appended to .claude/context/runtime/tool-events.jsonl
 */

const path = require('path');

function postExecute(context = {}) {
  try {
    const sendEventPath = path.resolve(__dirname, '../../../../tools/observability/send-event.cjs');

    let sendEvent;
    try {
      sendEvent = require(sendEventPath).sendEvent;
    } catch (_) {
      // Fail-open: observability is non-blocking
      process.stderr.write(
        '[regulatory-compliance/post-execute] send-event.cjs not found — skipping event\n'
      );
      return;
    }

    sendEvent({
      tool_name: 'regulatory-compliance',
      agent_id: context.agentId || process.env.AGENT_ID || 'unknown',
      session_id: context.sessionId || process.env.SESSION_ID || 'unknown',
      outcome: context.success !== false ? 'success' : 'failure',
      metadata: {
        subject: context.subject || 'unknown',
        decision: context.decision || 'unknown',
        regulationsAssessed: context.regulationsAssessed || [],
        findingCount: context.findingCount || 0,
      },
    });

    process.stderr.write('[regulatory-compliance/post-execute] Observability event emitted\n');
  } catch (err) {
    // Fail-open: post hooks must not block workflow
    process.stderr.write(`[regulatory-compliance/post-execute] Error (ignoring): ${err.message}\n`);
  }
}

module.exports = { postExecute };
