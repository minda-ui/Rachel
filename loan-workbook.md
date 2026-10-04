# Loan workbook — Rachel's method for keeping the group's loan plan current

_Adopted by owner decision (Minda), **2026-10-04**: "you need to take over this loan spreadsheet and keep updating it
from bank statements or by your request I can upload statements from lenders if available". Amendment 47._

**The workbook:** `Loans/Outputs/Fishbone_Loan_Repayment_Plan.xlsx` on Drive (`17JiFHokAPOnlfk-PZZPFmOcK-8xWIcRM`). It
is a financial working paper: **Drive only, never git**. Rachel owns it from 2026-10-04.

---

## 1. The rules that do not change

- **Three layers, never one combined group total** (OI-6): (a) business, related-party and hire-purchase debt;
  (b) property mortgages (Fishbone Properties, from the Property Register); (c) intercompany loans (internal).
- **Every balance says what it rests on**: lender-stated (with date), rolled forward from statements (estimate), or a
  **proxy** (payments still to make, which overstates principal). The *Update Status* sheet holds this per facility.
- **Nothing is removed.** Corrections are added as dated notes; superseded notes stay for the audit trail.
- **Decision aid only.** No repayment, no lender contact, nothing signed: Minda's.

## 2. Each update

1. **Inputs:** the bank statement CSVs Minda puts in Rachel's `Raw/` — Construction HSBC 2819 (most facilities);
   Properties (Funding Circle 0874BD, Sebastian, mortgages); Commercial Properties (SSAS loanback); the HSBC loan account.
   Lender statements when Minda uploads them.
2. **Payment Log sheet:** one row per instalment seen: date, facility number, amount, which month it pays, the
   statement line, the source file. A bounce and its re-presentment are recorded as they happened; count one instalment.
3. **Update Status sheet:** last instalment seen per facility; flag any instalment **not seen** when due.
4. **Balances:** roll forward only on evidence. A lender statement replaces the figure (note the date). Without one,
   an estimate (payment less a month's interest at the stated rate) is marked *estimate* and never replaces a
   lender-stated figure.
5. **Revolving FlexiPay book:** its draws and repayments are visible on the bank statement, its balance is not —
   use the Funding Circle FlexiPay statement.
6. **Before saving:** compare every existing sheet cell by cell with the version downloaded; only the intended
   cells may change. Check the live file is unchanged since download, update in place, verify the checksum, keep
   every revision forever.
7. **Report to Minda:** what moved, what was not seen, which statements are needed next (one short list).

## 3. Traps

1. A Funding Circle direct debit can bounce and be re-presented days later (9406CF, 14/09 → 18/09/2026).
2. Many small Funding Circle debits are FlexiPay repayments, not term-loan instalments: match term loans by their
   exact instalment amount.
3. Weekly "FISHBONE SSAS …" £50.08 standing orders are pension contributions, **not** the SSAS loanback.
4. Saving with a spreadsheet library drops cached formula results; Excel and Google Sheets recalculate on opening.
   Check the workbook has no charts or images first (an automated save can lose them).

## Update log

| Date | Inputs | What changed |
|---|---|---|
| 2026-10-04 | HSBC 2819 statement 02/09–02/10/2026 | Ownership taken. Added *Payment Log* (11 instalments) and *Update Status* sheets; no existing cell changed. Not seen: HSBC director loan (none since June), Eugene's interest. Balances still as at 21/08/2026 pending the August statement and lender statements. |
