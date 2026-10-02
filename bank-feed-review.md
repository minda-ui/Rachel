# Bank-feed review — Rachel's method for QuickBooks "For review" transactions

_Adopted by owner decision (Minda), **2026-09-29** ("Yes, go ahead"), from the first full review that day of
Fishbone Construction's HSBC 2819 feed (137 lines). Amendment 41._

---

## 0. What this is for, and what it is not

**For:** turning the list of bank transactions waiting in QuickBooks' Banking tab ("For review") into a
checklist Minda can work through in one sitting: **accept as suggested / change the category / match to an
existing bill / needs Minda's answer**, then a second pass on whatever is left.

**Not for:** posting. **Rachel does not accept, match, categorise or exclude anything in the bank feed.**
QuickBooks is read-only for her until the routine-posting rule set is agreed (`RA-3`). Minda posts. Rachel
prepares the list and checks the result. The rules in §4 are a draft of that rule set, not an authority to use it.

**Not a reconciliation.** It clears the feed. Whether the bank account then agrees with the statement is a
separate step, done afterwards with the statement.

---

## 1. First rule: ask for the export, not screenshots

**Ask Minda to export the list.** On the Banking → Bank transactions page there is an export icon at the top
right of the list, between the print icon and the gear. It downloads every line on the tab in one file.

**Why this is the first rule.** The 2026-09-29 review ran on eight phone photos of the screen. It worked, but:
- nine new transactions downloaded while we worked, so every row shifted down nine places and the same nine
  rows appeared on two "pages" — easy to count twice;
- rows at page breaks were missed (about 22 of 137 were never seen);
- amounts had to be read off a photographed monitor.

An export has none of those problems. **Screenshots are the fallback**, and if they are used: note the
"1–50 of N" counter on each page, and if N changes between photos, assume rows have shifted.

---

## 2. Before classifying anything

1. **Which company file, and which bank account is this feed?** Confirm both. Select the QuickBooks alias by
   company (`fishbone-qb2` is Construction; the others are in `Charter-Locations-and-Connectors.md`). A tell
   that you have the account wrong: QuickBooks suggests the feed's own account as the category.
2. **Read the chart of accounts live**, not from memory or screenshots:
   `QUICKBOOKS_QUERY_ENTITIES` — `SELECT Id, Name, FullyQualifiedName, AccountType, CurrentBalance FROM Account MAXRESULTS 400`.
   Look at the balance-sheet side first: bank, loan, intercompany and control accounts are where the costly
   mistakes land.
3. **Read how each payee was booked before.** Pull Purchases and Bills for the last six to twelve months
   (`SELECT * FROM Purchase WHERE TxnDate >= '…' MAXRESULTS 1000`; the API caps at 1,000, so query in date
   slices) and group by payee. **Consistency with past bookings is the default**; depart from it only for a reason
   stated in the list.
4. **Read the account's detail type when a name misleads.** In Construction's file "Storage" is set up as *Rent or
   Lease of Buildings* — it is the rent account.

---

## 3. Classify every line

| Action | Meaning | Colour in the sheet |
|---|---|---|
| **Accept** | QuickBooks' suggestion is right; tick and post | green |
| **Change** | Post to a different account (named) | orange |
| **Match** | Match to an existing bill or transaction (named) | blue |
| **Your answer** | Only Minda knows; one short question each | yellow |

**Output, every time:**
- an `.xlsx`, one row per line (date, description, spent, received, QuickBooks' suggestion, action, post to, note),
  colour-coded, filterable, with a summary tab (lines per action; money being re-pointed, by account);
  saved to Rachel's Drive `QuickBooks/` folder — **never to git**;
- a **phone-friendly ready list** in chat, in three steps — post as suggested, change then post, match — with the
  questions held back to a short "left for after" list. Group Step 1 by type, not line by line; list Step 2 line by
  line with date and amount, grouped by the account to post to.

Then Minda works the Banking tab, sends what is left (export again), and the second pass covers only that.

---

## 4. Mapping rules — Fishbone Construction, HSBC 2819 (established 2026-09-29)

Established with Minda on 2026-09-29. The "source" column says which rows she stated and which Rachel derived
from the chart or past bookings and put in the ready list she worked from. **They apply to Construction's file only**; each other company's rules are
built the same way (§2) and added here as they are agreed.

| Bank description (feed) | QuickBooks tended to suggest | Post to | Source of the rule |
|---|---|---|---|
| Holdings Loan (receipt) | Bank current account 2819 | **Fishbone Holdings** (other current asset) | chart; in the ready list Minda worked from, 29/09 |
| Fishbone Commercial loan payback | Bank current account 2819 | **Fishbone Commercial Property Ltd** | chart + Minda |
| Income Acnt / Expense Acnt Loan Payback | 2819 or Fishbone Holdings | **Fishbone Properties** — both are Properties' accounts | Minda, 29/09 |
| Fishbone Properties payback / loan (payment) | Fishbone Properties or match | **Fishbone Properties** | chart |
| Fishbone Drylining flexipay (receipt) | **Insurance** (wrong) | **Loan Funding Circle current** — FlexiPay draw | chart: "current" is the revolving facility |
| Funding Circle, small repayments | Loan Funding Circle current | Accept | — |
| Funding Circle £2,593.93 monthly | Loan Funding Circle current | **Loan Funding Circle 20112023** (term loan, schedule FC0000030), interest split | schedule; confirm account |
| Funding Circle payment + "Reversal … Funding Circle" + re-presentment | split across two accounts | **all to the same account** (Loan Funding Circle 30092024 on 14–18/09) | a bounced DD must net to nil |
| HM Revenue & Customs (receipt) | VAT Suspense **with 20% VAT** | **VAT Control, No VAT** — or record as the refund in the VAT section | a VAT repayment carries no VAT |
| Forth England Ltd | Storage | Accept — rent, Units 30 and 31 | Minda; detail type |
| Target | Software | **Advertising** — website/marketing agency | past bookings |
| Svetlana Berdysheva | Match | Match to **one** bill — Accountancy (bookkeeper) | Minda; past bills |
| Tower Leasing / Towerleasing | Subscriptions or Lease finance | **Lease finance charges – paid**, consistently | ask if several a month |
| Fishbone SSAS [name] (pension) | Pension, payee sometimes Fishbone Waste | Payroll Clearing old: Pension, **payee Fishbone SSAS** | — |
| NCFF Collections | Nucleus Loan | Accept (interest not split since May — year-end true-up) | past bookings |
| Salaries, suppliers, utilities, phones, subscriptions | as suggested | Accept, after a glance | — |

**QuickBooks' own bank rules.** The best fix is at source: Minda can set the first four rows above as rules in
QuickBooks (Banking → Rules), so the next feed arrives right. Recommend it after any review where the same wrong
suggestion recurs.

---

## 5. Traps found on the first run

1. **QuickBooks' suggestions were wrong on about a quarter of the lines**, and the wrong ones were the expensive
   ones: £18,450 of Holdings money suggested as a transfer between own accounts; £9,700 of FlexiPay draws suggested
   as *Insurance*, which would have shown as negative insurance cost.
2. **"2 matches found" can mean a duplicate bill.** Svetlana's August bill was entered twice (and July twice).
   Match to one; report the duplicate for deletion. **Look for duplicates whenever a match offers more than one.**
3. **A match can carry the wrong supplier** — a Screwfix payment matched a bill entered under Plumbfix. Accept the
   match if amount and reference agree; note the supplier.
4. **The same description can be booked two ways.** "Loan Payback" receipts from Properties were suggested to 2819
   once and to Fishbone Holdings once; past receipts from Properties had been posted to the *Holdings* account.
   Intercompany errors of this kind are what make the group's balances disagree.
5. **Loans with the wrong sign are worth a line.** Iwoca showed +£23,828.66 and the Company Credit Card
   +£21,505.47 in credit. Not feed items — report them, don't chase them mid-review.
6. **Counts go stale.** The tab said 128 at the start and 137 half an hour later. State the count with its time.

---

## 6. Afterwards

- Keep the `.xlsx` as the record of what was recommended; note in `current-state.md` what Minda posted.
- Add any new payee rule to §4 **only once Minda has agreed it**, with the date.
- If the same questions recur (who is this payee?), put the answer in §4 so the next review does not ask again.

---

## 7. Receipts to Dext — Construction only (Amendment 45, first run 2026-10-02)

Minda's design (2026-10-02): the bank feed is matched to **bills that Dext creates** from the invoices and receipts.

1. **Two files in Rachel's `Raw/`:** the QuickBooks For Review export and the HSBC statement CSV for the same account.
   Tie every QuickBooks line to its statement line (exact amount, date within 3 days); report any that do not tie.
2. **One matching file** (`QuickBooks/YYYY-MM-DD_Construction_HSBC2819_matching-and-receipts.xlsx`): per line, the
   posting (§4), VAT, and an **Invoice / receipt** column — **Found**, **Partial** (statement or chaser only),
   **Not found**, or **n/a** (salaries, pensions, loans, intercompany, FlexiPay, HP, vehicle tax — no invoice exists).
3. **Before anything goes to Dext,** query QuickBooks Bills and Purchases for the period: a supplier with a bill
   already would be entered twice.
4. **Search `ops@` and `minda@`** by supplier for the period; open each candidate and tie it by **amount** (and order
   number where two orders share an amount). Read the PDF total, not the email subject.
5. **Save** each document to Drive `QuickBooks/YYYY-MM-DD_..._receipts-for-Dext/` (never git), checksum-verified.
6. **Send from `ops@` through Composio only** (the PR #4 recipient guard checks every send): `GMAIL_SEND_EMAIL` to
   `mindaugas.gaudiesius@dext.cc`, **one document per email**, payload inline (`-d '{...}'`, never `@file`), subject
   `Supplier doc-no - amount - HSBC 2819 dd/mm/yyyy`. An email with no PDF (an O2 bill) goes by `GMAIL_FORWARD_MESSAGE`.
   Where the supplier email carries **two PDFs of the same charge** (Anthropic invoice + receipt), send one — Dext
   would create two bills.
7. **Log** each send in the file's "Sent to Dext" column (time, message id), confirm it in `ops@` Sent, and look for a
   bounce.

**Traps from the first run:** the export line count was 50, not the 49 first quoted — count from the file. The
attachment goes as `application/octet-stream` (the tool takes a path only); Dext reads it by extension: **confirmed by
Minda on 2026-10-02 — all seven of the first batch landed in Dext**, so no workaround is needed. The guard does not check `extra_recipients` — never use that field.
