# Weekly payment list: every Friday

_Adopted by owner decision (Minda), **2026-10-16** ("Adopt", skill candidate SC-11). Amendment 58. Built from the first
run, 15/10/2026 for Friday 16/10 (Budgets, Drive `1pQ1SFEdmhZW7SfcBDTaFVazIHdMz5BOB`). Part of Minda's 90-day plan,
Phase 1 (Hub AWT-0767, item 1). Day: Minda, 15/10, "Ideally Friday"._

---

## 0. What it is for

Once a week Minda approves the payments in **one sitting**, from one list, instead of one at a time as they come up.
Rachel prepares the list; **Minda approves and pays**. Payments stay with Minda (owner ruling 15/10): there is **no
spending limit** for any assistant and nothing on this list moves money.

**Not for:** paying, scheduling a payment, or marking a bill paid in QuickBooks (read-only for Rachel, `RA-3`);
filing or paying CIS or VAT (Minda's, 15/10).

**When:** ready by **Friday morning**; built Thursday evening if possible, so wages can be paid before Friday's direct
debits. **Company:** Fishbone Construction Ltd first; add the others once Minda asks.

## 1. Sources, read fresh every week

1. **Open bills:** `SELECT * FROM Bill WHERE Balance > '0' MAXRESULTS 1000` in `fishbone-qb2`. Keep vendor, number,
   date, due date, balance, and per line the account, item and `CustomerRef` (the job).
2. **The budget** for the month (`bud/build.py` lines): wages, loans, leases, FlexiPay, rent, HMRC.
3. **The FlexiPay register** and Funding Circle / GoCardless emails: what is due, what failed, when it is retried.
4. **The mailboxes** (ops@, info@fishboneconstruction, minda@): supplier statements, overdue notices, remittances.
5. **Minda's rule for the week** (for example 14/10: "FlexiPay and salaries only until 131 Goathland money arrives").
6. **The HSBC 2819 balance**, from Minda (the QuickBooks figure is not reconciled and means nothing).

## 2. The four sections

Every open bill goes in exactly one section. **The open bills, wherever they sit, must add back to the QuickBooks open-bills total**; the other lines (wages, direct debits, money in) are listed beside them but are not bills.

| Section | What goes in it |
|---|---|
| **A. Pay this week** | Due by next Friday and allowed by the week's rule. Wages. Direct debits listed too (marked "automatic") so the balance is right, and money expected in. |
| **B. Held** | Due, but held by the week's rule or until money arrives; each with the date it can be paid. |
| **C. Do not pay: paid, not matched** | Bills that the evidence shows are paid: card receipts published by Dext as bills, a bill paid by card (find the Dext email or the bank line), old subcontractor bills now paid through payroll. These are QuickBooks clean-up items (`RA-41`), not money owed. |
| **D. Needs Minda's answer** | Anything Rachel cannot prove either way: no statement, no chaser, no matching payment. Ask "paid or owed?". |

## 3. For each line

- **Pay to, what** (invoice number and date).
- **Order checked (PM-14.9):** the order, quote, lease or contract it should match. For suppliers that do not raise
  orders (JT Dove, Screwfix, MKM), check against the **supplier's statement** instead and say so.
- **Job number** (FC…). If the bill is not coded to the job, say which job it belongs to and that it is not coded.
- **CIS:** labour from a subcontractor → CIS applies (deduction is Minda's to verify); materials or a limited company
  supplying goods → not CIS. Say which.
- **Due date, amount, how it goes** (Minda pays / direct debit / card).
- **Rachel suggests** (pay, hold to a date, do not pay, ask), plus a **"Minda: approve? (Y/N)"** column left blank.

## 4. Summary page

One line per section with its total; then **what Section A needs** net of money in, with and without any direct debit
that may or may not go through; then **the bank balance after**, from Minda's figure. If Minda has not given the
balance, write "?" and ask: never use the QuickBooks balance.

## 5. Checks before it goes to Minda

1. The open bills across the sections add back to the QuickBooks open-bills total, to the penny (run 1: C £49,683.69 + D £15,879.21 + JT Dove £862.41 in B = £66,425.31).
2. Every Section A and B amount is traced to its source (bill, budget line, statement, email).
3. Nothing is in Section C on a guess: each has its evidence in the Notes column.
4. No bank details from supplier emails are copied into the list.
5. Saved to `Budgets/` as `YYYY-MM-DD_Fishbone-Construction_Weekly-payment-list.xlsx`, verified on Drive; the
   session row says where it is and the four totals.

## 6. After Minda approves

Record her Y/N per line in the session row. When she says what she paid, check it against the bank feed the next
week. Section D answers go to `RA-41` (clean-up through Sandbox or `quickbooks-changes-for-minda.md`); items Minda
says are owed move to A or B next week.

## 7. Traps found so far

- **A same-amount search in QuickBooks cannot see bank-feed lines still waiting in "For review".** No match does not
  prove a bill is unpaid. That is why Section D exists. (First run, 15/10.)
- **£49.7k of the £66.4k open bills on the first run were paid but not matched**, mostly weekly subcontractor bills from
  2025. Read open bills with suspicion. (15/10.)
- **Markfield £2,060.88 was paid by card on 08/10** and still showed as an open bill due 07/11. The Dext email from
  ops@ ("card 08/10/2026") was the proof. (15/10.)
- **JT Dove's 30/09 statement proved the £862.41 bill** (two invoices for Ferndale, FC2610), while the earlier overdue
  notice (£429.19, 22/09) was no longer on it. Use the latest statement. (15/10.)
- **Direct debits that cannot be stopped compete with the payments Minda chooses.** On 16/10 the term loan 94631B
  (£2,593.93) was due the same day as FlexiPay. Show the total with and without it.

## 8. Run log

| Run | For | Open bills (QuickBooks) | A / B / C / D | Notes |
|---|---|---|---|---|
| 1 | Fri 16/10/2026 | 64, £66,425.31 | £10,012.12 (A, incl. direct debits, net of Macdonald £2,243.50) / £11,637.41 / £49,683.69 / £15,879.21 | Rule: FlexiPay and wages only until Goathland money (20/10). Bank balance awaited from Minda. |
