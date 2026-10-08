# Intercompany check: both sides, every pair

_Adopted by owner decision (Minda), **2026-10-08** ("Adopt all five", skill candidate SC-1). Amendment 49. Built from the
FY2026 ITC check (6 Oct 2026), the Holdings bank-feed matching lists (6–7 Oct) and the recurring-charges list (6 Oct)._

---

## 0. What it is for

Every balance between two group companies sits in **two** sets of books. They must agree. This skill finds where they
do not, traces each difference to the transaction, and gives Minda a list of fixes. It is used:
- **monthly**, by the 20th (document-flow schedule A3, FG-CR-0003);
- **at each year end**, against the adviser's matrix (ITC);
- **after any bank-feed review** that touches an intercompany account.

It changes nothing in QuickBooks by itself: fixes go to Minda (`quickbooks-changes-for-minda.md`).

## 1. The pairs and where they live

| Company | Alias | Loan accounts to the others (QuickBooks Id) |
|---|---|---|
| Construction | `fishbone-qb2` | Holdings 197 · Properties 183 · Commercial 225 · Waste 220 · Investments (Amfa) 204 · David Macdonald Loan 222 (external) |
| Holdings | `fishbone-holdings-qb` | Construction 58 · Properties 56 · Waste 70 · Commercial 1150040000 · Investments 59 |
| Properties | `fishbone-properties-qb` | Holdings 83 · Construction ("Fishbone Construction Ltd.") 145 · Commercial 142 |
| Commercial Properties | `fishbone-commercial-properties-qb` | Construction ("Fishbone Drylining Ltd") 69 · Holdings 1150040002 · Properties 1150040001 |
| Waste | `fishbone-waste-qb` | Construction 79 · Holdings 90 |

Amfa and SSAS keep no QuickBooks: their balances are one-sided. **Check this table against the chart of accounts
each time**; accounts get added (Holdings' "David Macdonald Loan" appeared on 6 Oct 2026).

## 2. Steps

1. **Balance at the date, both sides.** Use `QUICKBOOKS_GET_GENERAL_LEDGER_REPORT` with `account_ids` as an **array**
   and `start_date` = `end_date` = the date: the "Beginning Balance" row plus that day's lines give the closing
   balance. (`QUICKBOOKS_GET_BALANCE_SHEET_REPORT` ignores `report_date` and returns the current year to date: do not use
   it for a past date.) For today, `CurrentBalance` from a `SELECT … FROM Account` query is enough.
2. **Sign.** An asset account shows the other company owing; a liability account shows this company owing. In the
   general ledger a liability balance shows positive. Write every pair as "X owes Y £n" before comparing.
3. **Trade balances too.** Open invoices and bills between group companies (customers and vendors named
   Fishbone…, Furniture by Fishbone, Fishbone Drylining) sit outside the loan accounts. The adviser's matrix nets them
   in. Query `Invoice` / `Bill` with `Balance > '0'` and `TxnDate` ≤ the date.
4. **Recurring charges.** Interest and recharges (the list in `QuickBooks/2026-10-06_Group_recurring-intercompany-charges_DRAFT.xlsx`):
   the charging company's invoice and the paying company's bill must both exist and both be paid or open.
5. **Trace every difference.** Pull both general ledgers over the period and match line by line (same amount, dates
   within a few days). What is left on one side only is the difference. Read the transaction in full (memo, journal
   note, who created it and when).
6. **Report.** One table per pair: each side's figure, the difference, the transaction behind it, the fix and who
   makes it. Matching lists for a bank-feed review go in `QuickBooks/YYYY-MM-DD_…_matching-lists.xlsx`.
7. **Recheck after Minda says done.** Read every item back (`quickbooks-changes-for-minda.md` §3).

## 3. Traps found so far

1. **Cut-off.** Construction's year end is **29 April**; the others' is 30 April. A transfer on 30 April is in one
   company's year and not the other's (£5,000 on 30/4/2026).
2. **Interest booked as a loan repayment** on one side and as interest on the other (£896 and £100, Sept 2026).
3. **Receipts booked straight to income** with no invoice (Holdings, van interest and loan interest, May–Dec 2025);
   months then go missing without anyone noticing (Sep–Nov 2025).
4. **A year-end journal mirrored on one side only** (RMT journal 2020-433, £900, Properties only).
5. **An old invoice open on one side** (Construction 1443, 77 Martin Road, 2020, £1,200).
6. **Waivers and agreements.** Before listing a charge as due, check the Document Register and `open-issues.md` for
   a waiver or variation (FH0000012 waives the Properties loan interest from 1 Oct 2026). Rachel missed it once.
7. **Recurring templates keep running** after a waiver or change; check `RecurringTransaction` on both sides.
8. **Bank feeds behind.** A difference may only be one company's feed not yet reviewed: check the last date entered
   on each bank account before calling it an error.
9. **Money passing through Holdings**: a repayment from Properties and an advance to Construction on the same day
   are two pairs, not one.

## 4. Run log

| Date | What | Result |
|---|---|---|
| 2026-10-06 | FY2026 ITC matrix v five QuickBooks files at 30/4/26 | All agree; £2,100 and £30,000 explained; cut-off and interest points to Alexey |
| 2026-10-06/07 | Holdings feed reviewed by Minda; Properties and Construction compared | Holdings fixes 1–2 done; matching lists for Properties (12 lines) and Construction (12 lines + re-point) |
