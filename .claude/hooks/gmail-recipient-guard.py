#!/usr/bin/env python3
"""
Rachel (AI Finance Assistant) — PreToolUse recipient guard for Gmail sends.

Rachel's charter bars her from sending email: "Rachel drafts, Minda sends"
(CHARTER.md §2 / §6 rule 4, owner ruling resolving RA-23). The ONE
owner-authorised exception (Minda, direct instruction 2026-10-02) is that she
may send/forward invoices and receipts to the Dext inbound address so Dext can
extract them into QuickBooks — a mechanical bookkeeping step, not external
correspondence.

A text-match permission rule can pre-approve "composio execute GMAIL_SEND_EMAIL"
but cannot pin the *recipient*, so it would allow a send to anyone. This hook
closes that gap: it inspects the actual command and permits GMAIL_SEND_EMAIL /
GMAIL_FORWARD_MESSAGE ONLY when every recipient (to/recipient_email, cc, bcc,
recipients) is exactly the Dext address, and denies everything else.

Fail-closed: if the gated action is present but the recipient cannot be
verified (payload via @file / stdin, or unparseable), the call is DENIED.
Non-gated commands pass straight through untouched. GMAIL_SEND_DRAFT and
GMAIL_REPLY_TO_THREAD stay hard-denied in settings.json (Minda sends those),
so this hook deliberately does not touch them.
"""
import sys
import json
import re
import shlex

DEXT = "mindaugas.gaudiesius@dext.cc"
GATED = ("GMAIL_SEND_EMAIL", "GMAIL_FORWARD_MESSAGE")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
RECIPIENT_KEYS = ("recipient_email", "to", "recipients", "cc", "bcc")


def decide(decision, reason):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": decision,
        "permissionDecisionReason": reason,
    }}))
    sys.exit(0)


def passthrough():
    # No output + exit 0 => defer to the normal permission system.
    sys.exit(0)


def recipients_from(payload):
    """Return (set_of_lowercased_emails, parsed_structured?)."""
    obj = None
    try:
        obj = json.loads(payload)
    except Exception:
        # Composio also accepts JS-style objects (unquoted keys). Lightly
        # normalise {key: -> {"key": then retry.
        norm = re.sub(r'([{,]\s*)([A-Za-z_][A-Za-z0-9_]*)\s*:', r'\1"\2":', payload)
        try:
            obj = json.loads(norm)
        except Exception:
            obj = None

    emails = set()
    if isinstance(obj, dict):
        for key in RECIPIENT_KEYS:
            v = obj.get(key)
            if isinstance(v, str):
                emails.update(e.lower() for e in EMAIL_RE.findall(v))
            elif isinstance(v, list):
                for x in v:
                    if isinstance(x, str):
                        emails.update(e.lower() for e in EMAIL_RE.findall(x))
        return emails, True

    # Fallback: cannot parse the object — take EVERY email in the payload
    # (fail-closed; an address in the body will block the send).
    emails.update(e.lower() for e in EMAIL_RE.findall(payload))
    return emails, False


def main():
    raw = sys.stdin.read()
    try:
        env = json.loads(raw)
    except Exception:
        # Unreadable envelope: only intervene (deny) if it names a gated action.
        if any(g in raw for g in GATED):
            decide("deny", "gmail-recipient-guard: unparseable hook input; blocking "
                           "send/forward (fail-closed). Rachel drafts, Minda sends.")
        passthrough()

    if env.get("tool_name") != "Bash":
        passthrough()
    cmd = ((env.get("tool_input") or {}).get("command") or "")
    if "composio" not in cmd or "execute" not in cmd:
        passthrough()

    action = next((g for g in GATED if re.search(r"\b" + g + r"\b", cmd)), None)
    if not action:
        passthrough()

    try:
        toks = shlex.split(cmd)
    except Exception:
        decide("deny", f"gmail-recipient-guard: {action} command could not be parsed; "
                       "blocking (fail-closed).")

    payloads = [toks[i + 1] for i, t in enumerate(toks)
                if t in ("-d", "--data") and i + 1 < len(toks)]
    if not payloads:
        decide("deny", f"gmail-recipient-guard: {action} has no -d/--data payload to "
                       "verify the recipient; blocking (fail-closed).")
    for p in payloads:
        if p.startswith("@") or p == "-":
            decide("deny", f"gmail-recipient-guard: {action} payload comes via @file or "
                           "stdin; recipient cannot be verified; blocking (fail-closed).")

    all_emails = set()
    structured_all = True
    for p in payloads:
        em, structured = recipients_from(p)
        all_emails |= em
        structured_all = structured_all and structured

    if not all_emails:
        decide("deny", f"gmail-recipient-guard: no recipient found on {action}; blocking "
                       f"(fail-closed). Only {DEXT} is permitted.")

    bad = sorted(e for e in all_emails if e != DEXT.lower())
    if bad:
        decide("deny", f"gmail-recipient-guard: {action} may only go to {DEXT}; blocked "
                       f"recipient(s): {', '.join(bad)}. Rachel drafts, Minda sends "
                       "(CHARTER §2 / §6 rule 4); Dext-only send is the one owner-authorised "
                       "exception (Minda, 2026-10-02).")

    note = "" if structured_all else (" (recipients inferred from payload text — keep other "
                                      "email addresses out of the subject/body)")
    decide("allow", f"gmail-recipient-guard: {action} to {DEXT} only — permitted bookkeeping "
                    f"forward to Dext{note}.")


if __name__ == "__main__":
    main()
