#!/usr/bin/env bash
# Rachel (AI Finance Assistant) — PreToolUse recipient guard (wrapper).
#
# Permits GMAIL_SEND_EMAIL / GMAIL_FORWARD_MESSAGE only when every recipient is
# the Dext inbound address (mindaugas.gaudiesius@dext.cc); denies all other
# recipients. The real logic is in gmail-recipient-guard.py.
#
# Fail-closed: if python3 is unavailable, the gated send/forward actions are
# DENIED rather than let through. Non-gated commands always pass (exit 0, no
# output => normal permission system applies).
set -uo pipefail

INPUT="$(cat)"

PY="$(command -v python3 || true)"
if [ -z "$PY" ]; then
  if printf '%s' "$INPUT" | grep -qE 'GMAIL_SEND_EMAIL|GMAIL_FORWARD_MESSAGE'; then
    printf '%s' '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"gmail-recipient-guard: python3 unavailable, cannot verify recipient; blocking send/forward (fail-closed). Rachel drafts, Minda sends."}}'
  fi
  exit 0
fi

GUARD="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/../.." && pwd)}/.claude/hooks/gmail-recipient-guard.py"
if [ ! -f "$GUARD" ]; then
  GUARD="$(dirname "$0")/gmail-recipient-guard.py"
fi

printf '%s' "$INPUT" | "$PY" "$GUARD"
