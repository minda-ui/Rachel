# Skill candidates: collected through the day, offered at "good night"

_Adopted by owner decision (Minda), **2026-10-08**: *"We need to add candidates for skill in every trigger 'Good Night'. You
collect candidates through a day and then you offer them to adopt or to delete."* Amendment 48._

---

## 0. What this is

A **skill** here is a written method Rachel follows every time a kind of work comes round (`end-of-day.md`,
`editing-drafts.md`, `receipts-to-dext.md`, `loan-workbook.md`). This file is where **candidates** wait until Minda
rules on them.

- **Collect during the day.** When work repeats, or a method had to be worked out the hard way, or a trap was found
  that will catch the next run, Rachel adds a candidate row **at the time**, not from memory at night.
- **Offer at "good night".** The end-of-day check (`end-of-day.md` §1 point 9) lists the day's new candidates in the
  good-night reply, each with one line on why, and asks: **adopt or delete?**
- **Minda rules.** *Adopt* → Rachel writes the skill file (or the update to an existing one), records the Amendment,
  mirrors it to git, and marks the row Adopted. *Delete* → the row is marked Deleted with the date and stays here as
  the record (nothing is removed). *No answer* → the row stays Proposed and is offered again next time, at most three
  times, then Rachel asks once whether to drop it.

## 1. What makes a good candidate

1. **It will come round again**: monthly, per supplier, per invoice, per adviser paper. A one-off is not a skill.
2. **The method was not obvious**: a step was missed, a tool refused, a figure was wrong the first time.
3. **Someone else could follow it from the page**: the steps, the checks, the traps, and what Minda decides.
4. **It is not already a skill.** If an existing skill covers it, the candidate is an **update** to that skill.

Not a candidate: a one-off decision (that goes to `current-state.md` or an Amendment), an open problem (that is an
`open-issues.md` row), or a preference about wording (that goes in `old-school-finance-writing.md`).

## 2. Candidates

Status: **Proposed** (waiting for Minda) · **Adopted** (date, skill file) · **Deleted** (date).

| # | Date | Candidate | Why (evidence) | Would cover | Status |
|---|---|---|---|---|---|
| SC-1 | 2026-10-06 | **Intercompany both-sides check** (new skill) | Done three times in a week: ITC matrix v five QuickBooks files (6 Oct), Holdings feed matching lists (6–7 Oct), monthly A3 recurring charges. Traps found: interest booked as loan repayment, receipts booked straight to income with no invoice, a waiver missed (FH0000012), cut-off 29 v 30 April | Pull loan and trade balances for every pair from each company's QuickBooks (general ledger at a date, open invoices and bills), tie them, trace differences to the transaction, list fixes for Minda, recheck after | Adopted 2026-10-08 → `intercompany-check.md` |
| SC-2 | 2026-10-05 | **Sales invoice from a hand-off** (new skill) | FC0237 (29 Sep) and FC0238 (5 Oct): Anna's request → check PO and quote → create in QuickBooks → read back → register → Hub. Trap: a plain sub-customer is refused for CIS items; the job must be a **project** | Checks before creating (PO, CIS / reverse charge, customer is a project, next number), creation on Minda's word, read-back, register `Draft` → `Issued` when sent, Hub close | Adopted 2026-10-08 → `sales-invoice-from-handoff.md` |
| SC-3 | 2026-10-07 | **Adviser paper: summary, meeting brief, reply** (new skill) | Alexey's archiving note (6 Oct), ITC matrix (6 Oct), fee proposal (7–8 Oct): read the attachment, compare with our books, a one-page summary for Minda, questions to settle, a brief before a meeting, then the reply draft. Rule kept: Minda's private view never goes in anything the adviser sees | Sandbox Mode steps made routine: capture to Raw/Finance, summary, brief, minutes from a transcript, reply draft for Minda | Adopted 2026-10-08 → `adviser-papers.md` |
| SC-4 | 2026-10-06 | **QuickBooks change Rachel cannot make** (new skill) | 6–8 Oct: pausing recurring templates, voiding an invoice and an expense, re-pointing expenses and transfers: the connector cannot do them. What worked: exact click-by-click steps for Minda, then a read-back of every item | Which changes the connector can and cannot make; the step list format; the verification after Minda says "done" | Adopted 2026-10-08 → `quickbooks-changes-for-minda.md` |
| SC-5 | 2026-10-08 | **Update to `receipts-to-dext.md`: purchases paid personally** | MW Machinery invoice 24642 (8 Oct) paid from Minda's personal card: no bank line to match; Minda's ruling: leave it on her director's loan | A rule in §6 and the supplier table: personal-card purchases go to Dext with the payment method = Directors Loan Account – M Gaudiesius; no feed line expected | Adopted 2026-10-08 → `receipts-to-dext.md` §5–6 |
| SC-6 | 2026-10-08 | **Filing a batch of documents from an adviser** (new skill) | RMT's 21 PDFs (8 Oct): every md5 differed from the registered files, yet five were the same returns (unsigned copies of DocuSigned ones), one was the as-filed version of a "For Approval" return, one the final amended version of draft accounts. Only a text and figures comparison told them apart; a filename's year ("CT600_2025") was not the period. A Drive rate limit failed one move mid-batch | Capture and checksum; compare each item with the register by content (page count, text, key figures, period boxes), not by checksum or filename; decide new row / supersedes / duplicate; re-check the high-water numbers; move and rename in one call, pause on rate limits, verify name, folder and checksum; duplicates to `Archive/` labelled, noted on the original row; report gaps | Adopted 2026-10-08 → `adviser-document-batch.md` |
| SC-7 | 2026-10-08 | **Update to `bank-feed-review.md`: QuickBooks bank rules from a feed** | Built 8 Oct for Construction (43 rules). Traps: the rule must use **Bank text**, not Description (QuickBooks shortens "AVIVA LIFE PENS" to "Aviva"); several Funding Circle loans share one bank text and can only be told apart by amount; a rule needs Minda's decision where past bookings disagree | A section on building the rule set per company: read the export and past bookings, one rule per payee, order, the condition to use, a "no rule — why" list, the decisions for Minda, and checking the next feed that the rules fired right | Adopted 2026-10-08 → `bank-feed-review.md` §4A |
| SC-8 | 2026-10-09 | **Finance workspaces: the month-end fill** (new skill) | Seven "<Company> - Finance" workspaces built 9 Oct (Amendment 51, AWT-0503); the monthly fill is due by the 20th for every company, plus the Project Register money columns (AWT-0494). Traps found building them: Smartsheet refuses a formula column at sheet creation (create, then add the formula; or copy a template sheet with from_template, which keeps formulas); copied sheets get new column ids; the baseline must be written from each company's own point of view | Order of work per company (bank and cards, loans, intercompany both sides, debtors and creditors, tax calendar, month-end row), where each figure comes from (QuickBooks general ledger at the date, statements, HMRC), the Project Register money columns from invoices and payments, read-back, and the fixes list for Minda | Proposed |

## 3. Log of rulings

| Date | Candidate | Ruling (Minda's words) | Result |
|---|---|---|---|
| 2026-10-08 | SC-1 to SC-5 | "Adopt all five" | Four new skill files and the Dext update written the same day; Amendment 49 |
| 2026-10-08 | SC-6, SC-7 | "Adopt both" | `adviser-document-batch.md` written and `bank-feed-review.md` §4A added the same night; Amendment 50 |
