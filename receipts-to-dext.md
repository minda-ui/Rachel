# Receipts to Dext — Rachel's method for matching Construction's bank feed

_Adopted by owner decision (Minda), **2026-10-02**: "save this process as skill and keep updating it with every run".
Sending authority: **Amendment 45** (Dext only, from `ops@`, Fishbone Construction Ltd only), enforced by the recipient
guard in `.claude/hooks/` (PR minda-ui/Rachel#4). Skill: Amendment 46. Companion: `bank-feed-review.md` (the posting
rules in its §4)._

**This file is a living record. After every run, update it before the run is called done** (§8). The end-of-day check
asks for it.

---

## 0. What this is for

Minda's design: **a bank-feed line in QuickBooks is matched to a bill, and the bill comes from Dext.** So for every
Construction bank line that needs one, Rachel finds the invoice or receipt in the mailboxes, saves it, sends it to Dext
(`mindaugas.gaudiesius@dext.cc`), and logs it. Dext extracts it and publishes a bill to QuickBooks; **Minda matches**.

**Not for:** posting or matching in QuickBooks (read-only for Rachel until `RA-3`); any company but Fishbone
Construction Ltd; any recipient but the Dext address; anything that is not an invoice or receipt backing a bank line.

---

## 1. Inputs — two files in Rachel's `Raw/`

1. **QuickBooks export** of Banking → For Review, Construction HSBC 2819 (e.g. `HSBC_Bank (UK) - transactions to match
   DDMMYYYY.csv`: Date, Bank description, Spent, Received, VAT, From/To, Match/Categorise).
2. **HSBC statement CSV** for the same account (e.g. `RT_YYYYMMDD_04212819.csv`: Date, Type, Description, Amount, Balance).

**Count the lines from the file** — never quote a count from memory.

---

## 2. Tie every QuickBooks line to the statement

Exact amount, date within 3 days, each statement line used once. The statement gives the fuller description (card
reference, supplier town, order or account number) — keep it. **Every line must tie**; report any that do not.
Statement lines from the same period that are not in the export: check QuickBooks before assuming anything (on run 1
Minda had matched them herself; card payments can sit under an earlier transaction date).

---

## 3. The matching file

`QuickBooks/YYYY-MM-DD_Construction_HSBC2819_matching-and-receipts.xlsx` on Drive (never git). Sheet **Matching**, one
row per QuickBooks line:

Date · Bank description (QuickBooks) · Statement line · Spent · Received · QuickBooks suggests · Post to (Rachel) · VAT ·
**Invoice / receipt** · Document · Found in · Drive file · **Sent to Dext** · Note.

**Invoice / receipt** is one of:

| Value | Meaning | Colour |
|---|---|---|
| **Found** | document downloaded, total checked to the penny | green |
| **Partial** | only a statement, chaser or overdue letter — not an invoice | amber |
| **Not found** | not in `ops@` or `minda@` | red |
| **n/a** | no invoice exists for this kind of line | grey |

**n/a lines** (no invoice): salaries (Net Pay) · SSAS pensions · intercompany loans and paybacks (Holdings, Income /
Expense Acnt = Properties) · Funding Circle repayments and FlexiPay draws · HP and loans (MotoNovo, Haydock, NCFF) ·
director's loan account · DVLA vehicle tax (statutory, **no VAT**).

Sheet **Summary**: counts per value, totals, what was sent, where the documents are.

---

## 4. Before sending — no duplicates

Query QuickBooks (`fishbone-qb2`) for **Bill**, **Purchase** and **BillPayment** from a fortnight before the period:
a supplier that already has a bill for the amount is **not** sent again. (`Purchase` has no `VendorRef` — use `EntityRef`.)

---

## 5. Finding the documents

Search `ops@` (`fishbone-ops-gmail-v2`, which also receives `info@fishboneconstruction.co.uk` mail) and `minda@`
(`rachel-minda-gmail`), per supplier, from about ten days before the period. **Open each candidate and tie it by
amount** — read the PDF total, not the subject. Where two orders share an amount, pair each with one payment and note it.

**Where each supplier's documents are** — add to this table on every run:

| Supplier | Where the document is | Notes |
|---|---|---|
| Screwfix | order confirmation email with PDF invoice, `ops@` and `minda@` (some orders only in one) | card payment posts 1–3 days after the order |
| Tower Leasing | monthly invoice email ~18th, `ops@`, PDF (`Invoice_NNNNNN.pdf`) | **carries 20% VAT** — QuickBooks suggests none |
| IronmongeryDirect | "Invoice NNNNNNN, Sales Order NNNNNNN" email, `ops@`, PDF | |
| Hafele | "Hafele Billing Document-NNNNNNNN" email, `ops@`, PDF | the "Confirmation" email is the order, not the invoice |
| Anthropic | "Your receipt from Anthropic Ireland" email, **two PDFs** (invoice + receipt) | send the receipt only; two cards = two charges, second receipt elsewhere |
| O2 | "Your O2 bill is ready", `ops@`, **no PDF** | forward the email itself; two accounts, two bills |
| JT Dove | only a monthly statement email (lists invoices) | invoices not emailed — ask JT Dove |
| MKM | only an "Overdue account" letter | invoices not emailed — ask MKM |
| Microsoft | only payment notices by email | invoice in the Microsoft 365 admin centre |
| Composio, EDF, Amazon, Sanef (tolls), Google Play | not in the mailboxes | supplier account online — needs the login |
| Sebastian Pabis (materials), Sergej Murasov (CIS) | not in the mailboxes | ask the person |

Save every document found to Drive `QuickBooks/YYYY-MM-DD_Construction_HSBC2819_receipts-for-Dext/`, named
`date_Supplier_doc-no_amount.pdf`, checksum-verified.

---

## 6. Sending to Dext

- **From `ops@`, through Composio only** — the guard checks every send. Payload **inline** (`-d '{...}'`); `@file` or
  stdin is refused.
- `GMAIL_SEND_EMAIL`, `recipient_email` = `mindaugas.gaudiesius@dext.cc`, **one document per email**, attachment = the
  local PDF path. Subject: `Supplier doc-no - amount - HSBC 2819 dd/mm/yyyy`; body: one line with net, VAT, how paid.
- No PDF (O2): `GMAIL_FORWARD_MESSAGE`, `recipients` = [Dext address], `additional_text` = amount and bank line.
- **Never** `cc`, `bcc` or `extra_recipients` (the guard does not check `extra_recipients`).
- The tool sends the PDF as `application/octet-stream`; **Dext accepts it** (confirmed by Minda, run 1).

---

## 7. After sending

1. Confirm every send in `ops@` Sent (`in:sent to:mindaugas.gaudiesius@dext.cc`) — recipient, subject, attachment.
2. Look for a bounce or a Dext reply.
3. Fill **Sent to Dext** (time UTC, message id) and the Summary; update the Drive file in place, checksum-verified.
4. Tell Minda what went, what is Partial or Not found and where it probably is; she confirms the batch landed in Dext
   and matches the bills.

---

## 8. Updating this skill — every run

Before the run is called done:
1. Add a row to the **run log** below.
2. Add any **new supplier** or a better location to the §5 table.
3. Add any **new trap** to §9, and any new n/a kind to §3.
4. Put the file in place on Drive (live == git HEAD), commit and push.

---

## 9. Traps

1. **Count from the file.** Run 1 was quoted as 49 lines; the export had 50.
2. **QuickBooks suggestions are wrong where it costs most:** FlexiPay draws suggested as *Insurance*; DVLA with 20% VAT;
   Tower Leasing with no VAT; payroll pensions with the wrong payee.
3. **A charge can appear twice with the same amount** (two Screwfix GBP 40.44 orders, two Anthropic GBP 37.50 charges on
   two cards) — pair explicitly and say which goes with which.
4. **The send tool blocks even a schema lookup** without a Dext-only payload — pass `-d` with the Dext recipient to read
   the schema.
5. **A job name on an invoice can point to another company** — JT Dove "ferndale" is 2 Ferndale Avenue, a Commercial
   Properties job: flag for recharge.

---

## Run log

| Run | Date | Lines | n/a | Found | Partial | Not found | Sent to Dext | Landed (Minda) | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-10-02 | 50 (21/09–02/10) | 31 | 7 | 2 | 10 | 7 (ops@, 21:05–21:06 UTC) | yes, 02/10 | Learning run; not-found lines left as they are. Tower VAT GBP 47.20 caught. |
