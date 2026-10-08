# End of day — "Have you documented today's work?"

_Adopted by owner decision (Minda), **2026-09-29**: *"as soon as i write you 'good night' can we trigger skill 'Have you
documented today's work?'"*. Amendment 43. Triggered automatically: a `UserPromptSubmit` hook in the repo's
`.claude/settings.json` sees "good night" / "goodnight" in Minda's message and tells Rachel to run this check before
she replies._

---

## 0. What this is for

A session's work is only safe once it is **written down, in place on Drive, committed and pushed**. The container is
reclaimed after the session; anything left only in chat or the scratchpad is lost. "Good night" is the last moment
to catch it.

**It is a check, not a ritual.** If everything is already done, say so in one line and say good night. Do not redo
work that is already recorded, and do not start new work that Minda has not asked for.

---

## 1. The check, in order

Answer each one **from the files, not from memory** — read the live copy where it matters.

1. **`current-state.md` has today's session row.** It says what was done, what was decided and by whom, and what is
   waiting. If the row was written earlier in the day and more happened since, bring it up to date.
2. **Decisions are recorded where they belong.** A charter-level decision from Minda has its Amendment in
   `CHARTER-amendments.md`, and `Charter-Locations-and-Connectors.md` is updated if a file, mailbox or connector was
   added. Quote her words.
3. **`open-issues.md` is current.** Issues opened, progressed or resolved today say so; resolved rows moved to
   `open-issues-resolved.md`.
4. **The register and the Hub show final status.** Every document registered today has its number and the right
   status (Draft / Issued / Received); every Hub task opened or closed today is set.
5. **Drafts are listed.** Every email draft Rachel left for Minda is named — mailbox, recipient, subject — with the
   date she proposed for any promise in it (`old-school-finance-writing.md` §7).
6. **Outputs are on Drive, not only local.** Anything produced today (xlsx, PDF, review) is in the right Drive folder;
   nothing financial is in git.
7. **Governed files are in place and mirrored.** Each changed governed file was updated **in place** on Drive
   (`put_in_place`: live == git HEAD before upload, verified after, revisions kept forever), then **committed and
   pushed**. `git status` is clean and the branch is not ahead of `origin`.
8. **Skills updated by today's runs.** If a Dext run happened today, `receipts-to-dext.md` has its run-log row and
   any new supplier or trap (Amendment 46).
9. **Skill candidates offered.** `skill-candidates.md` has today's candidates (added during the day, not from
   memory at night), and every row still **Proposed** is listed in the good-night reply for Minda to **adopt or
   delete** (Amendment 48). Rulings given since the last good night are recorded in its §3 and acted on.

Fix what is missing, in that order, then report.

---

## 2. The good-night reply

Short, in the old-school style. One line on whether today is documented (and what was just fixed, if anything). Then
**what is waiting for Minda**, as a numbered list, each with a date where there is one — at most three items at the
top, the rest grouped under "also waiting". Then **skill candidates**: each Proposed row in one line (number, name, why), ending with
"adopt or delete?". Then good night.

Example:

> Today is documented: session row, Amendment 43, register and push all done.
>
> Waiting for you:
> 1. **Alexey drafts** — three in `ops@`, confirm the dates before sending.
> 2. **Bank feed** — export of what is left, for the second pass.
> 3. **Seven answers** — MKM, JT Dove, Tower Leasing ×2, Spotify, Forth England ×2.
>
> Good night, Minda.

---

## 3. If something cannot be finished

Say exactly what is left undone and where it stands (for example: "session row written on Drive, not yet pushed —
the push failed on the network"). Never report a step as done that was not.
