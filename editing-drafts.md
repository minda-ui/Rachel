# Editing email drafts — Rachel's method for correcting a draft in place

_Adopted by owner decision (Minda), **2026-10-02** ("Based on that create editing draft as a skill"), after the first
in-place edits that day: the Alexey Holdings follow-up in `ops@` (date line) and the RMT request in `minda@` (a
same-text test). Amendment 44._

---

## 0. What this is for, and what it is not

**For:** correcting a draft that is waiting for Minda — a date that has passed, a sentence that changed, a recipient
or subject that was wrong — **in the same draft**, so there is only ever one version in the mailbox.

**Why it matters.** The alternative is to create a replacement and delete the old one. Deleting needs Amendment 37
*and* a settings rule that lets it through; on 2026-10-02 the deny rule `GMAIL_DELETE_*` blocked it, and replaced
drafts piled up for Minda to delete by hand. Two versions of the same email in a mailbox is how the wrong one gets
sent. **Edit in place first; replace only when an edit cannot do the job** (see §4).

**Not for:** sending. Rachel never sends, edited or not. **Not for** drafts someone else wrote — only Rachel's own
unsent drafts, or a draft Minda names.

---

## 1. Which tool, by mailbox

| Mailbox | Tool | Keeps sender name | Notes |
|---|---|---|---|
| `ops@fishboneconstruction.co.uk` | native Gmail connector, `update_draft` | **yes** | Merge semantics: fields left out are kept. **Attachments are removed unless re-supplied.** |
| `minda@fishboneconstruction.co.uk` (`rachel-minda-gmail`) | Composio `GMAIL_UPDATE_DRAFT` | **no** — From drops to the bare address | Fields left out (subject, recipients, thread) are kept. |
| `info@fishboneproperties.co.uk` (`fishbone-properties-info-gmail`) | Composio `GMAIL_UPDATE_DRAFT` | **no** (same tool; not yet used there) | As above. |

**Check which mailbox a tool lands on before relying on it.** On 2026-10-02 the native connector listed only `ops@`
drafts; it does not reach `minda@`.

**Finding the Composio tool:** `composio tools list gmail` did not show `GMAIL_UPDATE_DRAFT`. Search for it instead:
`composio search "update an existing gmail draft" --toolkits gmail`, and read its inputs with
`composio execute GMAIL_UPDATE_DRAFT --get-schema`.

---

## 2. The edit, step by step

1. **Read the whole draft first.** Native: `get_draft` with `FULL_CONTENT`. Composio: `GMAIL_GET_DRAFT` with
   `format: full` (large results land in a file — read `outputFilePath`). Note the recipients, subject, thread,
   **attachments**, and whether the body is HTML with a quoted earlier message underneath.
2. **Change only what needs changing.** Copy the body exactly and alter the one sentence. In a reply draft the quoted
   message below the signature is part of the body — **keep it byte for byte**; dropping it changes what the
   reader sees.
3. **Send HTML back as HTML.** If the body is HTML (a reply with a quote always is), pass it as HTML: `htmlBody`
   (native) or `body` with `is_html: true` (Composio). Plain text with `is_html: false` turns the quote into a
   mess.
4. **Attachments.** Native `update_draft` strips them unless re-supplied — re-attach, or do not edit that draft this
   way. Composio's behaviour with attachments is **untested**: check the size after the edit, and if it is gone,
   re-attach.
5. **Update.** Pass the draft id; leave out fields that must not change.
6. **Read it back.** The draft id must be the same; recipients, subject and thread unchanged; the new sentence present;
   the quote intact; attachment present with its size. Compare against the text you sent, not by eye.
7. **Report** in one line: mailbox, draft, what changed, and — for `minda@` or `info@` — *check the From line shows
   your name before sending.*

---

## 3. Rules that still apply to the words

- **A date in a draft is a promise** (`old-school-finance-writing.md` §7). Moving a date that commits Minda needs a date
  she has confirmed, or is flagged to her as a proposal.
- **Say only what will be true when it is sent.** If an edit says "we have asked RMT", the RMT email must go first —
  tell Minda the order.
- **Signature and salutation unchanged** unless the edit is about them.

---

## 4. When to replace instead of edit

Replace (create a new draft) only when the change is too big to be an edit — a different recipient **and** a different
subject, or a new thread. Then: say so, and either delete the old draft (Amendment 37, if the settings allow it) or
name it to Minda for deletion. Never leave two live versions without telling her.

---

## 5. Traps found on the first run (2026-10-02)

1. **The tool was there all along.** It was missed because the toolkit list was incomplete; the search found it.
2. **The sender name drops in `minda@`.** After a Composio update the From line read `minda@fishboneconstruction.co.uk`
   instead of `Minda Gaudiesius <minda@…>`. Gmail's compose window normally restores the name when Minda opens the
   draft; she checks before sending.
3. **A same-text update is a safe test.** Re-saving a draft with identical content proves the write path without
   changing anything Minda has seen.
