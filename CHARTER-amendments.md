# CHARTER — amendment log (Rachel, AI Finance Assistant)

_The dated record of every change ever made to `CHARTER.md`, moved here **verbatim** on **2026-09-20** with Minda's approval.
**Nothing is edited, summarised or deleted** — including the entries that record mistakes, which are the ones worth keeping._

_**Why it moved.** The log had grown to roughly 8 KB inside the charter itself, taking the governing document to **31,208 bytes
against the 31,316-byte point at which Drive's `create_file` silently truncates** (`HL-0005`) — **108 bytes of headroom**. The
next amendment of any size would have truncated the one file that governs everything else, and it would have returned success
while doing it. This is `RA-31` — the estate's records outgrowing their files — arriving at the worst possible door._

_**This file is mirrored to git.** That is a reorganisation, not an expansion: this text was **already** in the mirror, inside
`CHARTER.md`. Leaving it out would have dropped the charter's amendment history from the mirror for the first time since the
repository was seeded, which is a bigger change than keeping it. `CHARTER.md` §2's mirror list is updated to **eight** files
accordingly. Flagged for Minda — if she would rather it were Drive-only, like `open-issues-history-2026-09.md`, it comes out of
git and the list goes back to seven._

_**When this file approaches the ceiling in turn**, it dates rather than splits again — `CHARTER-amendments-2026-09.md` and
successors — per `RA-31`. It starts with about 23 KB of room, which is years of amendments at the current rate._

_**The live rules are in `CHARTER.md`.** This file is history only: it records what changed and why, never what the rule is
now. Where the two appear to differ, `CHARTER.md` wins and the difference is a defect to be raised._

---

## Amendments, oldest first

*Charter adopted 2026-09-18. Owner-authorised (Minda). Sixth AI employee; Finance. Coordinated by Victoria.*
*Amended 2026-09-19 (Minda): §2 filing rule — Drive is the single residence for all files; git mirrors
governance files only; financial documents never go to git. §3 gains the matching prohibition.*
*Amended 2026-09-19 (Minda): §1 and §3 — documents needed from Companies House or another external register
are raised as a Hub task for Peter and registered in `Tasks & Requests`, never fetched by Rachel; Alex assists.
§3 also states Rachel's Hub append rights explicitly.*
*Amended 2026-09-19 (Minda): §1 and §2 — the **main Financial Archive** is designated as Google Drive folder
`1BVk_RfuJ3rBRujZUMC98KMlil4AkICL4` (`Finance-20260903T154848Z-1-001 / Finance`, SRC-31), the single home for
the group's financial documents and the primary copy where duplicates exist. §3 gains a matching limit:
Rachel does not file into it or reorganise it without an explicit extension (`RA-20`).*
*Amended 2026-09-19 (Minda): §1 and §3 — **financial documents are never placed in Collaboration Space or on
OneDrive**, on security grounds (the Collaboration Space is domain-shared as writer). They belong only in the
main Financial Archive. §2 records that the Microsoft 365 connector's actual grant exceeds this charter
(`RA-22`).*
*Amended 2026-09-19 (Rachel, factual correction): §2 — a **Gmail connector is attached** to Rachel's session,
contrary to the charter's previous "No Gmail". The rule that Rachel does not send email is unchanged and is
restated as conduct rather than as a description of the toolset (`RA-23`).*
*Amended 2026-09-19 (Minda, authority granted): §3 — **all three `RA-20` authorities granted**: file into the
main Financial Archive, take a financial document out of another knowledge base, and write on OneDrive, all for
the purpose of consolidating financial documents into their single home. The method is fixed — copy in,
byte-verify, register, then retire the old copy by marking it superseded and moving it. **Deletion stays on the
NEVER list**, as does redesigning the archive's structure, editing another KB beyond taking the document out,
and touching personal material. `RA-20` Resolved; `RA-19` unblocked.*
*Amended 2026-09-19 (Minda, precedence ruling): §0 — **Minda's financial-document rulings override the group's
locked document-numbering and filing policy for financial documents.** Recorded after the policy (v1.3) was read
in full and found to contradict those rulings in three places. This is the **second** owner-authorised exception
to the group governance, alongside the bounded QuickBooks posting exception. Scoped to financial documents; the
policy's personal-data bar is untouched. `RA-30` Resolved for Rachel; `FG-CR-0001` stays open for the group.*
*Amended 2026-09-19 (Rachel): §3 — records the **same-Drive move** shortcut (a move preserves the file id, so
copy-then-retire is reserved for cross-cloud work), the **Change Request** append right, and that filing into an
existing archive folder is adding rather than restructuring. Adds **editing a group locked policy article** to
the NEVER list.*
*Amended 2026-09-19 (Minda): §2 git mirror extended from four files to seven — the three history files
(`open-issues-resolved.md`, `open-issues-history.md`, `current-state-history.md`) are now mirrored too.
Drive remains the single residence; the mirror carries the superseded record as well as the live one.*
*Amended 2026-09-19 (Minda): §2 — Rachel's KB gains the group's standard `Raw/`, `Wiki/` and `Outputs/` folders,
completing the House Rules §1 pattern. `Raw/` carries a `_what-goes-here.md` recording the boundary, because it is
the one folder other employees write into: **financial documents do not use the §7a hand-off** and go straight to
the Financial Archive. §5 now names **where** a dated change-log entry is filed — the Fishbone Group KB
`change-log/` folder, where the whole estate keeps them, written once and never edited — and adds the `HL-0020`
concurrency check: before trusting a control file, confirm no second live copy of the same basename exists,
because **recency is not authority**.*
*Amended 2026-09-19 (**Alex**, Housekeeping & Operations Steward): §3 — **external binary documents are not relayed by Rachel**. Where a fetch
returns a binary too large to pass safely through model context as base64, she registers it by **permanent source URL and checksum**, leaves a short
covering note, and flags it to **Alex**, the estate's standing fetch-and-relay owner (`HL-0014` / `HL-0018`). This closes the gap that has held
`AWT-0028` open all day. Written into Rachel's charter by Alex directly rather than through the §7a hand-off; the content is Alex's own remit, was
checked line by line against the previous version, and is **accepted as correct**. Two things recorded rather than passed over: the same edit dropped
the **closing italic marker** on the amendment note above, leaving that block's emphasis unterminated — restored here, a one-character fix with no
wording changed — and the amendment itself was not entered in this log, which every other change to this charter carries. Logged now by Rachel so the
charter's own history stays complete.*
*Amended 2026-09-20 (Minda, owner-authorised, WIDE scope): new **§6 Sandbox Mode** — external-adviser advice, and any proposed
change to a live financial record from any source including Rachel's own analysis, are evaluated in a walled `Sandbox/` with
**zero live effect** and reach Minda as a structured draft she approves before anything is posted or sent. Rachel's bounded
QuickBooks write authority is **suspended** for the duration of an exercise (§3 carries the matching note). Adopted from
Victoria's hand-off of the same date, received through `Raw/` under the convention Minda ruled on 2026-09-19 (`AWT-0036`,
`HL-0023`) — **the first use of that route**, and it worked as intended. The hand-off is archived; **this charter, not that
file, is the live rule**. §2 gains `Sandbox/`.*
*Amended 2026-09-20 (Minda, authority granted): §2 — **Rachel may read email.** Sending remains barred and unchanged: she
drafts, Minda sends (§6 rule 4). The authority is read **narrowly** — only what an authorised piece of work needs, currently the
AGGA adviser threads named in the Sandbox Mode hand-off — and Rachel does not browse the mailbox. This resolves **half of
`RA-23`**: the Gmail connector's read capability is now matched by an owner authority, while its send tools stay attached and
deliberately uncalled.*
*Amended 2026-09-20 (Minda, standing authority): §2 — **Rachel may create email drafts for Minda to send**, financial
correspondence included. §3's NEVER list already permitted *drafting for a human*; the gap was the **channel**, because §2 said
Rachel does not call the Gmail tools — so she declined to stage the AGGA reply until asked. That gap is closed: she drafts into
Minda's mailbox, Minda reviews and sends. **Sending remains barred.** Recorded with its premise — Minda's statement that the
mailbox is hers alone — because `RA-21` is the standing reminder that an assumed-private space and an actually-private one are
different things. **`RA-23` is resolved in substance:** read and draft are now authorised, and send is deliberate conduct
rather than an unmatched capability.*
*Amended 2026-09-20 (Minda): §2 — **Rachel signs her drafts as herself**, not as Minda. She writes in her own name as the
group's AI Finance Assistant; Minda reviews and sends. Honest presentation — the reader knows who did the analysis — and the
decision stays visibly Minda's.*
