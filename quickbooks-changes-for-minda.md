# QuickBooks changes Rachel cannot make: steps for Minda, then a check

_Adopted by owner decision (Minda), **2026-10-08** ("Adopt all five", skill candidate SC-4). Amendment 49. Built from
6–8 Oct 2026: pausing the interest templates, voiding Holdings invoice 1137 and a Properties expense, re-pointing the
David Macdonald £1,000 in two companies, matching Holdings payments to invoices._

---

## 0. What the connector can and cannot do (as at 8 Oct 2026)

| Can (Composio, `fishbone-…-qb`) | Cannot |
|---|---|
| Read anything (`QUICKBOOKS_QUERY_ENTITIES`, general ledger, reports) | Pause, edit or delete a **recurring template** |
| Create an invoice (on Minda's word) and a customer | **Void** an invoice or an expense (no void operation) |
| Update an invoice (sparse / full) | Edit or delete an **expense (Purchase)**, a **transfer** or a **deposit** |
| Batch create/update/delete for Bill, Invoice, Payment, Customer, Vendor, Account, Item, SalesReceipt | Match bank-feed lines, or change a bank feed |

The native Intuit connector (`mcp__Intuit_QuickBooks__…`) can pause recurring invoices but needs Minda to sign in
again, and may reach only one company. **Deleting is never Rachel's** (`CHARTER.md` §3): she prefers void, and voiding
is Minda's.

## 1. Writing the steps

1. One block per company, in the order Minda will work: company name as the heading.
2. Each step names **exactly** what to open (menu path, document number, date, amount, memo) and what to change it
   to (account name as it appears in QuickBooks).
3. Say **what it fixes** in one line, and **what the balance will be** after.
4. Put the urgent one first with its date ("Properties' Loan 2 template runs tomorrow").
5. Anything outside QuickBooks (a standing order at the bank) is listed separately: only Minda can do it.

## 2. Recording

The steps go into the working file of the job (matching list, recurring-charges list) with a "Done?" column, and the
decision behind them into the session row.

## 3. Checking after Minda says "done"

Read every item back, one query each:
- templates: `SELECT * FROM RecurringTransaction`, `RecurringInfo.Active` = false;
- voided documents: `TotalAmt` 0 and `PrivateNote` "Voided";
- re-pointed expenses/transfers: the account names on the lines;
- payments applied: the invoice `Balance`, and the `Payment` with its `LinkedTxn`;
- the balances on both sides, as promised in step 1.3.

Report in a table: item, status, and anything not done or done differently. If Minda changed something else at the
same time (a new account, a different treatment), say what you see and ask what it is.
