# Close-out report: the money section

_Adopted by owner decision (Minda), **2026-10-10** ("adopt SC-9"). Amendment 53. First run: FC2609 and FC2608,
10 Oct 2026 (Hub AWT-0518). Template: the close-out report approved 10 Oct (AWT-0511), group KB
`Outputs/2026-10-10_Proposal_Fishbone-Close-Out-Report-Template-and-Lessons-Register_v1.md`, section 7.
Procedure: PM-2.3, PM-9.4 to 9.9 (v1.0)._

---

## 0. What it is for

Every job's close-out report has a money section (section 7) written by Rachel. The job lead (Anna for
Construction) writes the rest. The report is internal (PM-9.7). The section states facts from the books and names
each source, so Sarah (compliance officer, no QuickBooks access) can check it against the Document Register and the
source named.

**When:** when the lead asks (a Hub row and a note in Rachel's Raw), after the lead's draft exists.

## 1. Lines of section 7, and where each comes from

Read the project in the company's QuickBooks (Construction: `fishbone-qb2`). Find the project id from the name
(`SELECT ... FROM Customer WHERE Job = true`); a job number can be on two projects (FC2517), so check.

| Line | Source | Query / note |
|---|---|---|
| Basis | The invoice lines | Lump sum on a PO, or day-work (rate per person per day). The basis decides what "cost v quote" means. |
| Quote | Document Register; QuickBooks `Estimate` for the project | No quote → write "GAP" (lump sum) or "None (day-work)", and whether the rates are agreed in writing. |
| PO | Document Register; the invoice line text ("as per PO …") | If the value exists only on the invoices, say so and ask the lead to file the PO. |
| Extras and variations | Invoice lines beyond the PO; the lead's scope section | Goodwill work not charged: say "not charged". |
| Committed (ordered, not invoiced) | Not in QuickBooks (purchase orders are almost never raised) | Closed job: "None known". Live job: the supplier-order line in the job costs sheet. |
| Invoiced | `Invoice WHERE CustomerRef = '<id>'` | Number, date, net amount each. VAT code (Construction to Macdonald: `20.0% RC CIS`, reverse charge, VAT £0). |
| Paid | `LinkedTxn` → `Payment` | Date and amount each; say whether any CIS was deducted. |
| Costs recorded against the job | Every `Bill` and `Purchase` line whose `CustomerRef` is the project (also `JournalEntry`, `VendorCredit`) | Total plus the main groups (accommodation, travel, fuel, materials). Query from about a month before the first invoice. |
| Labour | Payroll, not tagged to jobs | Always a stated GAP until Minda rules how labour is costed (RA-39). Name who worked and the days. |
| Cost v quote | The lines above | No quote → "Not possible". Never state a margin while labour is missing. |
| Final account agreed | Written final account, if any | Usually "Not documented; paid in full". |
| Retention | Payments against invoices | Any shortfall held back, with its release date. |
| Outstanding | Invoice balances | £ and age. |

## 2. Writing it

1. **Only section 7 and Rachel's line in section 13.** The file is the lead's. Check the live md5 equals the copy you
   read, write, then check the md5 after upload (same file id).
2. Head the section with the source (company, project name and id, date read), "all figures net of VAT", and the VAT
   treatment.
3. A table, one row per line in §1, then **Queries** (numbered) for anything that looks wrong.
4. Update the Project Register money columns to match (Quote / PO / Extras / Invoiced / Paid / Invoice status /
   Money notes). Money notes name the source (invoice and payment numbers and dates, Document Register numbers).
5. Rule F: a note in the lead's Raw and the requester's Raw; the Hub row Done with the figures and file ids.

## 3. Traps

1. **Day-work v lump sum.** FC2608 was 15 days at £390 + £340; there is no quote to compare. Do not invent one.
2. **The PO may exist only on the invoices** (FC2609 "PO DM513/001", "1 of 2 payments"). Take the value from them and
   say so.
3. **A billable expense can be marked recharged and not be on the invoice.** `ReimburseCharge` shows
   `HasBeenInvoiced = true` linked to an invoice whose total does not include it (Screwfix £11.66 on FC0232). Check
   the invoice total, not the flag.
4. **Costs tagged to a job may belong to another** (London car parks on a Merry Hill job). Query; do not drop them
   silently.
5. **Untagged costs exist.** Meals and travel during the job often carry no project. Say the cost total is
   incomplete.
6. **Labour is never in job cost.** Wages go through payroll clearing, not the project.
7. **Your own earlier notes can be wrong.** Re-read the register's Money notes against the invoices (9 Oct note said
   FC0232 "includes a rebilled cost"; it does not).

## 4. Run log

| Date | Jobs | By | Notes |
|---|---|---|---|
| 2026-10-10 | FC2609 (long form), FC2608 (short form) | Rachel | AWT-0518. Committed cost not available from QuickBooks; RA-39 opened |
