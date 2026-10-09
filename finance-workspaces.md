# Finance workspaces: the month-end fill

_Adopted by owner decision (Minda), **2026-10-09** ("Adopt", skill candidate SC-8). Amendment 52. The workspaces
themselves: Amendment 51 (built 9 Oct 2026, Hub AWT-0503). Workspace and template sheet ids:
`Charter-Locations-and-Connectors.md`._

---

## 0. What it is for

Each company has a Smartsheet workspace, "<Company> - Finance", where Rachel proves every month that the books agree
with the outside world. QuickBooks stays the books. The workspace holds the evidence and the differences. This skill
is how a month is filled.

**Who sees them:** Minda and Rachel only. Alexey read-only is possible later, on Minda's word for that moment.

**When:** by the **20th** of the following month (document-flow schedule A3), for all seven companies. Also after
every bank-feed review, for the lines it touched. First fill: September 2026, by Tue 20 Oct 2026.

## 1. Order of work, per company

Do the companies in the same order each month: Holdings, Construction, Properties, Commercial Properties, Waste,
AMFA, SSAS. Holdings first, because most intercompany pairs start there.

| Step | Sheet | Source | Check |
|---|---|---|---|
| 1 | **2 Bank and cards** | statement closing balance (Drive bank packs, `Raw/` CSVs, the bank's PDF); QuickBooks balance at the month end | Difference must be 0; list each unreconciled item (date, amount, what) |
| 2 | **3 Loans and finance** | lender statement or schedule (`loan-workbook.md`); QuickBooks balance at the month end | Difference 0; rate, payment, end date |
| 3 | **4 Intercompany** | both companies' QuickBooks at the date: loan accounts **and** open invoices and bills (`intercompany-check.md`) | Our books = their books; otherwise the item behind it |
| 4 | **5 Debtors and creditors** | open invoices and bills at the month end | Anything over 90 days or disputed, by name |
| 5 | **6 Tax calendar** | HMRC (VAT, PAYE, CIS, CT), QuickBooks control accounts | Filed and paid by the due date; QuickBooks = HMRC statement |
| 6 | **8 Property finance / Investments** where present | lender statements, rent, share register | As step 2 |
| 7 | **1 Month-end checklist** | the sheets above | Tick each box only when its sheet is complete; done date, by whom |
| 8 | **7 Year-end and adviser queries** | Alexey's questions, our corrections | Status kept current all year, not only at month end |

**Project Register money columns** (Construction workspace, sheet `5250912102778756`, AWT-0494) are
filled in the same pass: invoiced and paid per job from QuickBooks invoices and payments, invoice status, money notes.
Rule F applies to that sheet: it is shared with other assistants, so changes are recorded on the Hub row and noted in
the lead assistant's `Raw/`.

## 2. How to read a balance at a date

- `QUICKBOOKS_GET_GENERAL_LEDGER_REPORT`, `account_ids` as an array, `start_date` = `end_date` = the month end: the
  last running balance in each section is the closing balance. For receivables and payables per counterparty, add
  `customer_ids` / `vendor_ids` with `account_type` AccountsReceivable / AccountsPayable.
- The balance-sheet report ignores the date: do not use it for a past date.
- Liability accounts show positive when owed. Write every figure as a positive amount with a direction.

## 3. Writing to the sheets

- **Every row carries its source** (statement file, QuickBooks report and date, HMRC statement).
- **Read back** after writing: get the rows, check the values and the Difference column.
- **Nothing is posted to QuickBooks from here.** A difference becomes a fix for Minda (`quickbooks-changes-for-minda.md`).
- **New sheet or new company:** copy the template sheet with `create_sheet` → `from_template` (keeps the Difference
  formulas). A sheet built from scratch cannot take a column formula at creation; add it afterwards with
  `update_column`.
- **Copied sheets get new column ids.** Read `get_columns` before writing to any sheet; never reuse ids from another
  company's copy.

## 4. Traps

1. **Point of view.** The same balance is written twice, once in each company's workspace, from its own side: "They
   owe us" in one, "We owe them" in the other, our books and their books swapped.
2. **Cut-off.** Construction's year end is 29 April, the others' 30 April. Movements on 30 April show only in some
   year-end figures (£20,000 in 2025, £5,000 in 2026).
3. **Trade balances hide outside the loan accounts.** Open invoices and bills between group companies are part of
   the balance (FC0035 £30,000; van interest; rent invoice 1811).
4. **An odd account can hold part of a balance.** Properties keeps £2,750 owed to Construction in an Accounts Payable
   account named "Director loan - Mindaugas Gaudiesius".
5. **AMFA and the SSAS keep no QuickBooks.** Their balances are one-sided: fill "their books" from the other company
   and mark One-sided.

## 5. Run log

| Month | Filled | By | Notes |
|---|---|---|---|
| (baseline) | 2026-10-09 | Rachel | Intercompany sheets seeded with the 30/4/25 and 30/4/26 baseline sent to Alexey |
