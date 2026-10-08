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
| MW Machinery (Markfield Woodworking Machinery) | invoice PDF by email to Minda; Anna puts it in Rachel's `Raw/` | paid by card via the "Pay Now" link: ask which card (24642 was Minda's personal card) |
| Lathams (James Latham Gateshead) | pro forma first; **VAT invoice only after payment clears** | send the VAT invoice to Dext, not the pro forma |
| Scott+Sargeant (`Www Scosarg.com`) | "A/R Invoice - NNNNNNNNN" PDF email, `ops@` (the order email has no PDF) | pro forma, paid by card; freight on top; total can differ from the bank by 1p |
| Forth England (rent) | Xero invoice email "Invoice INV-NNNN from Forth England Ltd", `ops@`, **link only, no PDF** | **one email per company** (Construction and Furniture by Fishbone): check whose invoice was paid |
| SmartestEnergy | "Your Latest Electricity Invoice" PDF, `ops@`, ~7th | the DD on ~15th pays the **previous** month's invoice; check "Balance brought forward" |
| Starlink | only payment reminder / failed-payment emails | invoice in the Starlink account online |
| Wickes, Wolseley, Radius Telematics | not in the mailboxes (run 2) | in-store or account online: ask Minda |

Save every document found to Drive `QuickBooks/YYYY-MM-DD_Construction_HSBC2819_receipts-for-Dext/`, named
`date_Supplier_doc-no_amount.pdf`, checksum-verified.

---

## 6. Sending to Dext

- **From `ops@`, through Composio only** — the guard checks every send. Payload **inline** (`-d '{...}'`); `@file` or
  stdin is refused.
- `GMAIL_SEND_EMAIL`, `recipient_email` = `mindaugas.gaudiesius@dext.cc`, **one document per email**, attachment = the
  local PDF path. Subject: `Supplier doc-no - amount - HSBC 2819 dd/mm/yyyy`; body: one line with net, VAT, how paid.
- Body ends with `#note <Supplier amount, HSBC 2819 dd/mm/yyyy> #note` (from run 2, §10).
- No PDF (O2): `GMAIL_FORWARD_MESSAGE`, `recipients` = [Dext address], `additional_text` = amount and bank line.
- **Never** `cc`, `bcc` or `extra_recipients` (the guard does not check `extra_recipients`).
- The tool sends the PDF as `application/octet-stream`; **Dext accepts it** (confirmed by Minda, run 1).
- **Paid from a director's personal card** (owner ruling, Minda, 2026-10-08, MW Machinery 24642; Amendment 49): the
  invoice still goes to Dext (it is Construction's cost and VAT), the body says "paid from M Gaudiesius' personal
  card", and when it is published the **payment method is "Directors Loan Account – M Gaudiesius"**, not a bank or
  card. There is **no bank-feed line** to match; the amount stays on the director's loan unless Minda says repay.

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

1. **Count from the file.** Run 1 was quoted as 49 lines; the export had 50. Count with a CSV reader, not `wc -l`: the export has no
   final newline, so `wc -l` is one short (pass 2 of run 2: 34 lines, not 33).
2. **QuickBooks suggestions are wrong where it costs most:** FlexiPay draws suggested as *Insurance*; DVLA with 20% VAT;
   Tower Leasing with no VAT; payroll pensions with the wrong payee.
3. **A charge can appear twice with the same amount** (two Screwfix GBP 40.44 orders, two Anthropic GBP 37.50 charges on
   two cards) — pair explicitly and say which goes with which.
4. **The send tool blocks even a schema lookup** without a Dext-only payload — pass `-d` with the Dext recipient to read
   the schema.
5. **A job name on an invoice names the project, not the company.** JT Dove "ferndale" is 2 Ferndale Avenue: the
   property is Commercial Properties', but the work is **Construction's project FC2610** (Minda, 2026-10-08). Cost to
   Construction, tagged to the project; ask before assuming a recharge.
6. **Read "Total Paid", not the sub total.** Screwfix discounts sit between the two (run 2: sub total 189.99 less 15.00
   = 174.99 paid; 78.96 less 5.00 = 73.96). A "no match" on the sub total is often a discount.
7. **The card on a Screwfix invoice says which account paid.** Card 6941 = HSBC 2819. A Screwfix invoice on another card
   (run 2: 6789) is not for this feed, even when the amount is close.
8. **Re-check QuickBooks for a run-1 document before matching it.** Tower invoice 933575 was sent in run 1 for the 28/09
   line; by run 2 its bill had been closed by a payment dated 10/09. Look at the bill's Balance and linked payments,
   not only whether it exists.
9. **An invoice can be addressed to another group company.** Forth rent GBP 1,800 paid from 2819 on 17/09 was INV-1655
   to Furniture by Fishbone Limited. Read the addressee before sending; if it is not Construction, do not send — ask.
10. **The guard reads the command text.** Even printing a `GMAIL_SEND_EMAIL` command (to review payloads) is blocked
    without a Dext-only `-d`. Generate payloads to a file with a script, read the file, then send with literal `-d`.
11. **Check what Dext published before Minda matches.** Run 2's 13 items published as bills within the hour, and Minda
    matched them. But Dext used supplier **Plumbfix** for Screwfix, category **Purchases** for Hafele and Scott+Sargeant,
    and run 1's Tower bill 933575 went to **Software** with its payment dated 10/09. Read the published bills (supplier,
    account, VAT, date) and list the fixes. Better still, set Dext supplier rules (§10) so they publish right.

---

## 10. What Dext can do — from the help centre (read in full 2026-10-02)

Read from help.dext.com (16 articles) after Minda opened the environment's network to it. **Settings are Minda's to
change** (Admin user); Rachel reads and recommends. Status column: what is set up — update as Minda changes things.

| Feature | What it does | Use for us | Status |
|---|---|---|---|
| **Extract by email** | `name@dext.cc` = one item per file (several files per email fine); `name@multiple.dext.cc` = one item per page. Body-only receipts work. Text between two `#note` tags becomes the item's description. Items appear within ~30 min. A user's address makes that user the document owner. | Our address is Minda's Single address. Add `#note <bank line> #note` to every send so the item says which bank line it is for. | in use |
| **Rejection notices** | Profile > User settings > Bookkeeping email notifications > *On acknowledgement* = Yes: a summary with the rejection reason per file, to the owner's Dext login email. The exact same file sent twice is rejected at upload. | Turn on, so a failed send is visible. | not set |
| **Publish to QuickBooks** | *Bill* = unpaid bill. *Cash / Check / Credit card* = paid expense — the item's **payment method must be linked to a QuickBooks bank account**. Dext attaches the document image to what it publishes. Every item needs a tax rate (set default tax for costs). | Publish **paid**, payment method linked to *Bank current account 2819*: the expense is then waiting in QuickBooks and the bank-feed line offers **Match** — one click. | not set |
| **Payment methods** | The card's last 4 digits, read from the receipt; or created by hand (direct debit, cash, a personal card). Each can carry Auto-publish, Publish to and a linked bank account. | HSBC 2819 debit card(s), HSBC 2819 direct debits; the director cards QuickBooks already has (Andrej, Minda, NatWest). | not set |
| **Supplier rules** | Per supplier: category, tax rate, payment method, paid/unpaid, due date, description, currency, a *workflow note*, duplicate mode, auto-publish. Apply to new items only (tick *Apply to all inbox items* for existing). **QuickBooks vendor defaults sync every 48 h and can overwrite them.** | Fix QuickBooks' wrong defaults at source: Tower Leasing 20% VAT; Anthropic no UK VAT; Screwfix / Hafele / IronmongeryDirect Materials 20%; O2 Telephone. | not set |
| **Rule priority** | AI Assist guidance > user defaults > payment-method rules > supplier rules > account defaults. | Explains surprises. | — |
| **Auto-publish** | Per supplier, payment method or whole account; only items arriving after the rule; exceptions by item type (e.g. supplier statements stay in the inbox). | Only after a supplier's rule has published correctly by hand once or twice. | not set |
| **Duplicate detection** | *Automatic* deletes a suspected duplicate (restorable from Submission history); *Review* flags it amber; *Off*. Receipts: same supplier + date + total + owner; invoices: supplier + total + reference. Per account or per supplier. | **Review**, at least for Screwfix — two genuine GBP 40.44 orders on one day would look like one. | not set |
| **Fetch** | Collects invoices from supplier portals with the login: past documents within 48 h, then weekly. Supported for us: **Microsoft Office365, EDF Energy, Amazon.co.uk (and Amazon Business), o2.co.uk Business, Vodafone UK, Google Play / Payments Center, Spotify, QuickBooks Online UK**, and Travis Perkins, Howdens, British Gas, BT, EE. Not Screwfix, MKM, JT Dove, Hafele, IronmongeryDirect, Tower Leasing, Anthropic, Composio. | Covers most run-1 "Not found" lines. Needs Minda's logins. | not set |
| **Email forwarding rules** | A mailbox rule auto-forwards supplier emails to the Dext address; Gmail sends a verification link to the Dext login email. | A Gmail filter in `ops@` for the PDF suppliers (Screwfix, Hafele, IronmongeryDirect, Tower Leasing). Rachel then checks rather than sends. Minda's filter, not a Rachel send. | not set |
| **Paperwork Match** (works with QuickBooks Online) | Attaches the document **image only** to a transaction already in QuickBooks (same supplier, total, date within 10 days, last 6 months). Publishes nothing. | For bank lines already categorised in QuickBooks without a receipt: send the receipt to Dext, then *Send image to* — **do not publish**, or the cost goes in twice. | — |
| **Bank Match** | Full version (Autofill Payment) only for Xero, Sage, MYOB. | Not for us — the matching file stays. | — |
| **CIS** | QuickBooks CIS must be on; supplier name in Dext must equal the CIS contact name; choose the CIS category. **In QuickBooks Online the *Less CIS* field must be adjusted by hand after publishing.** AI Assist guidance can split labour (gross) and materials. | Sergej Murasov and other subcontractors. | — |
| **Rebillable** | Mark an item rebillable to a QuickBooks customer (billable expenses on in QuickBooks). | JT Dove "ferndale" = Construction project FC2610: tag the cost to the project, so it can be billed on if FC2610 is billed at cost. | — |
| **People's receipts** | Users and submitters can snap receipts in the Dext app; *Request paperwork* asks for a missing one. | Sebastian's materials receipts. | — |

## Run log

| Run | Date | Lines | n/a | Found | Partial | Not found | Sent to Dext | Landed (Minda) | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-10-02 | 50 (21/09–02/10) | 31 | 7 | 2 | 10 | 7 (ops@, 21:05–21:06 UTC) | yes, 02/10 | Learning run; not-found lines left as they are. Tower VAT GBP 47.20 caught. |
| 2 | 2026-10-08 | 50 (14/09–08/10) | 7 | 14 (13 new + Anthropic from run 1) | 9 | 20 | 13 (ops@, 22:43–22:45 UTC) | — | No statement CSV this run (§2 tie not done). Screwfix discounts and card numbers resolved two "no match" lines; Forth rent paid for another company; Tower 933575 already closed by a 10/09 payment; Screwfix 40.44 corrected to A28105872495. |
