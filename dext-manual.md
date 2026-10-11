# Dext manual for Fishbone

_Written by Rachel on 11 October 2026, at Minda's request ("write the Dext manual from online help center"). The source
is Dext's help centre (help.dext.com): 56 articles read on 11 October 2026. Each section names the articles it comes
from. Our own procedure for sending documents is `receipts-to-dext.md`; this manual explains Dext itself and how we
should set it up._

**Who can change what.** Dext settings, rules, payment methods, suppliers, duplicates and auto-publish are
**Admin-only** (Business Admin or User Admin). Minda is the Admin. Rachel has **no Dext login**: she sends documents by
email only, and cannot see the inbox, the settings or the rules. Anything below marked "Minda" is a click in Dext.

**What Rachel cannot reach.** Dext has no connection in Composio, and `api.dext.com` is blocked from Rachel's
environment. The **Dext AI Connector** (Claude, ChatGPT, Copilot) is in beta for **accounting practices on Practice
Advanced only**, is read-only, and covers practice data (clients, time, aged balances, journals). It does not show a
business account's rules or settings. It is not for us (§9).

---

## 1. How a document travels

1. **In:** email to our Dext address, Fetch from a supplier portal, the mobile app, or upload (§2).
2. **Extraction:** Dext reads supplier, date, totals, VAT and the card's last 4 digits, usually **within 30 minutes**.
3. **Rules run** in a fixed order (§5): AI Assist guidance, user rules, payment method rules, supplier rules,
   account defaults.
4. **Inbox:** each item is **To review** (something missing or wrong; hover over the badge to see what) or **Ready**
   (green = fine; yellow = an earlier publish attempt failed).
5. **Publish to QuickBooks Online** (§4): as a **Bill** (unpaid) or as **Cash / Check / Credit card** (paid, against a
   bank or card account). Dext attaches the document image to what it creates.
6. **In QuickBooks:** the bank feed line offers **Match** to the published expense or bill payment.

_Sources: Rules and automation in Dext; What do "To review" and "Ready" mean; How to publish documents from Dext to
QuickBooks Online._

---

## 2. Getting documents in

### 2.1 Extract by email (what we use)

- Each user and the account itself have their own addresses, for Costs and for Sales, in two modes:
  **Single** `name@dext.cc` (each file = one item, even with several pages; several files per email are fine) and
  **Multiple** `name@multiple.dext.cc` (each page = one item; PDFs up to 200 pages).
- **Ownership:** a user's address makes that user the document owner; the account address leaves the owner blank.
  Ours is **Minda's Single address**, `mindaugas.gaudiesius@dext.cc`.
- **File types:** PDF, DOC/DOCX, ODT, RTF, JPG, PNG, GIF, BMP, TIFF, ZIP of images. **Body-only** receipts work (give
  supplier, date, total, currency). Dext cannot read password-protected files or follow links.
- **Description:** text between two `#note` tags becomes the item's description. We use it for the bank line or the
  payment route.
- **The original email** is kept: open the item, **Email** tab.
- **Rejection notices** (Minda): Profile > User settings > Bookkeeping email notifications > **On acknowledgement =
  Yes**. Dext then emails the reason for each rejected file to the owner's login email.
- **Block senders** (Minda): Business settings > Extraction > Blocked emails > Manage. `*@domain.com` blocks a domain.
- **Find or rename the address:** Profile > User settings > Extract by Email (own); Business settings > Extraction >
  Extract by email (account address).

### 2.2 Email forwarding rules (no hand-sending)

A mailbox rule forwards supplier emails to the Dext address. Gmail sends a **verification link to the Dext login
email** (Minda's) before forwarding starts. If the account-level address is used, first choose a user in Business
settings > Extraction > Email notifications > "When a document doesn't have an owner", or the verification never
arrives. Use rule conditions on the sender address and words like invoice, receipt, bill.

**For us:** a Gmail filter in `ops@` for the suppliers that email PDFs (Screwfix, Hafele, IronmongeryDirect, Tower
Leasing, RMT Technology, SmartestEnergy). It is Minda's filter to set; Rachel would then check rather than send.

### 2.3 Fetch from supplier portals

Business settings > Connections > Cost Connections > **Connect** > Add connection > choose the supplier portal (check
the region) > Document owner > "Load the transactions since" date > enter the portal login. Dext collects what is
already there within 48 hours, then checks **every 7 days**. Business settings > Connections > Cost Connections >
**Manage** shows each connection's status. **Force Document Fetch** syncs now (up to 24 hours; may trigger 2FA).
Fetched documents go through the same rules.

**Our suppliers on Dext's Fetch list:** Amazon.co.uk, Microsoft Office365.com, o2.co.uk, Spotify, Audible.co.uk,
Google Payments Center / Google Apps, Apple Store UK, Adobe, OpenAI, Zoom, Dropbox, BT Business, EE, EDF Energy,
Sky.com, Vodafone UK, QuickBooks Online UK, **Travis Perkins, Howdens, Wolseley**. Not on it: Screwfix, MKM, JT Dove,
Hafele, IronmongeryDirect, Tower Leasing, Anthropic, Starlink, SmartestEnergy, Lathams, Bytestock, Renewtech.

**Amazon:** there is an ordinary Amazon.co.uk Fetch portal, and a separate **Amazon Business** connection (daily, up to
7 days back, Amazon Business accounts only; personal accounts not supported; no invoice number extracted). Our orders
are on a personal account in Minda's name, so it is the Amazon.co.uk portal, or moving business buying to Amazon
Business.

### 2.4 Other routes

- **Mobile app:** photograph and submit; a category chosen in the app before submitting beats supplier rules.
- **Upload:** + Add documents.
- **Supplier statements:** upload through + Add documents > Supplier statements tab (not by email). Dext matches each
  line to invoices by supplier and reference (then total and date). Each plan has a free allowance; extra
  statements are charged. A statement emailed in arrives as a normal Costs item; Move to > Supplier statements runs
  the matching and is charged.

_Sources: How to submit documents to Dext via email; How to find and edit your Extract by Email address; Set up email
forwarding rules to Dext; How to block unwanted email addresses or domains; How to set up / manage a Fetch connection;
List of suppliers for Invoice Fetch; How to connect your Amazon Business account; How to upload and manage supplier
statements._

---

## 3. The inbox

### 3.1 Duplicates — two different checks

- **File rejection:** the *exact same file* sent twice is refused at upload ("This item already exists in your
  account"). No item, nothing in Submission history. Always on.
- **Duplicate detection** (Costs only), set in Business settings > Extraction > **Duplicate items**, or per supplier
  in Costs > Suppliers > supplier > Duplicate cost items:
  - **Automatic:** a suspected duplicate is deleted at once and only appears in Submission history as "Confirmed
    duplicate". It can be restored.
  - **Review:** it stays in the inbox as To review with an amber dot, for an Admin to decide.
  - **Off:** not recommended.
- **How Dext decides:** same document type, same supplier record, same non-zero total, plus:
  - **receipts:** same date and same document owner, and printed times less than 10 minutes apart. **Receipt
    numbers are not compared**, so two genuine Screwfix orders of £40.44 on one day count as duplicates.
  - **invoices and credit notes:** same reference (spaces ignored); the date is used only when neither has a
    reference.
  - **not checked at all:** supplier statements, delivery notes, mileage, "Other" and some other types.

**For us:** **Review** for the whole account, or at least for Screwfix and B&Q.

### 3.2 Finding things

- **Submission history** (bottom of the left sidebar): everything ever submitted (inbox, archive, deleted, merged,
  confirmed duplicates), with view, download, history and **Restore**. Search is by supplier name; Advanced filters by
  submitter, method, dates and amount. Exports to CSV. Rejected files are not there.
- To review and Ready can be shown as separate tabs: Business settings > Extraction > Inbox tabs.

### 3.3 Editing an item

- **Split:** one document into two items with different categories and amounts (Split at the top of the item).
- **Line Item Extraction:** each line read separately. Uses **credits** from the plan (they reset each period and do
  not roll over). Turn it on per supplier (Costs > Suppliers > Extract line items) or for one item.
- **Suppliers:** merge duplicates (Costs > Suppliers > Supplier duplicates > Merge; cannot be undone, merge in
  QuickBooks too); add **aliases** (e.g. "Www Scosarg.com" → Scott+Sargeant). A new supplier created in Dext is also
  created in QuickBooks when published; turn on **Warn me when creating a new supplier** (Connections > Manage >
  Settings > General).

_Sources: How Dext handles duplicate Cost documents; How does Dext decide two Cost items are duplicates; How to use the
Submission history; How to split an item; How to use Line Item Extraction; How to manage suppliers in Dext._

---

## 4. Publishing to QuickBooks Online

**Settings** (Minda): Business settings > Connections > **Manage** (next to QuickBooks Online) > Settings, with tabs
General, Tax and Automatic publishing.

### 4.1 Publish to

- **Bill:** unpaid; appears in QuickBooks as a bill to be paid (e.g. RMT Technology, paid later by direct debit).
- **Cash / Check / Credit card:** paid; appears as an expense against the **bank or card account linked to the
  item's payment method**. Without a linked payment method a paid item cannot publish.
- **Credit note:** required for a negative total; QuickBooks rejects negatives published any other way.
- **Default "Publish to" for costs:** in the General settings; can be overridden per supplier (supplier rule) or per
  item.

### 4.2 Payment methods

- A payment method is a card's **last 4 digits**. When Dext reads new digits it creates a method called **"New"**.
  **Rename it** (e.g. "HSBC 2819 debit – Minda"), or Dext keeps creating new ones.
- **Link each to a QuickBooks account:** Business settings > Lists > **Payment methods** > Bank account column. The
  list shows **bank and card accounts synced from QuickBooks** (Reload if one is missing).
- Methods can also be created by hand for a personal card, cash or petty cash.
- If the QuickBooks connection is ever disabled and reconnected, **the links are lost** and must be made again.

### 4.3 Tax

Settings > Tax: **Use tax list** on; **Default tax for costs**; **Default tax for sales**; **default tax code if no
tax amount extracted** (an exempt/0% code). Without these, items publish with errors ("Please select a tax rate…" or
"Dext is unable to find a 0% tax rate"). Dext sends amounts **tax-exclusive** and QuickBooks works out the gross.

### 4.4 Construction specifics

- **CIS:** CIS must be on in QuickBooks; the supplier name in Dext must match the CIS contact exactly; choose the CIS
  category. **In QuickBooks Online the "Less CIS" field must be adjusted by hand after publishing.** Labour and
  materials should be split (line items or Smart Split).
- **Domestic reverse charge:** the help centre describes choosing DRC VAT rates in Dext for Sage 50 and Xero only.
  Construction's QuickBooks has the codes **20.0% RC CIS** and **5.0% RC CIS**. Choose one of these in Dext's tax list
  for a subcontractor's reverse-charge invoice, and check the first one in QuickBooks before relying on it.
- **Rebillable:** choose a QuickBooks **customer** on the item and Mark as rebillable = Yes (billable expenses must be on
  in QuickBooks). For example, JT Dove "ferndale" → customer project FC2610.

### 4.5 Matching what is already in QuickBooks

- **Paperwork Match:** for a transaction already in QuickBooks (same supplier and total, date up to 10 days later,
  within 6 months), **Send image to** attaches only the image. **Do not also publish**, or the cost goes in twice.
- **Bank Match:** the full version with Autofill Payment is for Xero, Sage and MYOB only. For QuickBooks it only flags
  possible matches.

### 4.6 Common QuickBooks errors

| Error | Fix |
|---|---|
| Publish to empty / Bill not offered | choose Bill or a paid type; Bill is missing on QuickBooks Simple Start |
| No tax rate / no 0% rate | set the default tax codes (§4.3) |
| Duplicate document number | change the reference, or publish as Bill |
| Duplicate supplier name | a customer or employee has the same name in QuickBooks; rename one |
| Object not found | a supplier or category was deleted in QuickBooks; Refresh integration data; relink payment methods if reconnected |
| Something went wrong | the connection expired; reconnect |
| Stale object | clear the item's publishing data and republish, after checking QuickBooks for a duplicate |

**Refresh:** Dext pulls QuickBooks lists **every 48 hours**. To pull at once: Business settings > Connections > Manage >
**Refresh integration data**, or Reload on any list page.

_Sources: How to publish documents from Dext to QuickBooks Online; How to set up tax settings for QuickBooks Online;
What is a Payment method; Manage Payment methods; How to link a payment method to a bank account; How does CIS work in
Dext; How does DRC work in Dext; How to use Paperwork Match; How does Bank Match work; QuickBooks Online publishing
error messages; How to refresh your accounting software data._

---

## 5. Rules and automation

### 5.1 The order (highest first)

1. **Dext AI Assist guidance**
2. **User rules** (per uploader: default payment method or project)
3. **Payment method rules** (auto-publish, publish to, bank account)
4. **Supplier rules**
5. **Account defaults**

Auto-categorisation fills the category only where no supplier rule set one. Rules apply **to new items only**. Coding
rules can be pushed to existing inbox items with **Apply to all inbox items**; auto-publish and line items never are.
**QuickBooks supplier defaults sync every 48 hours and can overwrite Dext supplier rules**, so fix wrong defaults in
QuickBooks too.

### 5.2 Supplier rules

Costs > **Suppliers** > click the supplier (or **Set supplier rules** on an item). Fields:
- category, tax rate, payment method, Paid/Unpaid, due date, description, currency, Publish to;
- auto-publish, duplicate mode, Extract line items, Smart Split;
- a **Specific workflow** note, shown at the top of every item from that supplier (e.g. "Lathams: VAT invoice
  only, not the pro forma").

Several suppliers at once: tick them, then **Bulk Edit**.

### 5.3 Payment method rules

Business settings > Lists > Payment methods. Per method:
- **Auto-publish** = Always / Never / None;
- **Publish to**;
- **Bank account**.

They beat supplier rules for the same field. A supplier rule can choose the payment method, and the payment method's
rule then decides publishing. **Never** blocks auto-publish for everything on that card.

### 5.4 User rules

Business settings > Lists > Payment methods > **Set user defaults**: a default payment method per user, either
"Always use default" or "Use default if blank". The same is possible for a default project (QuickBooks Classes or
Locations).

### 5.5 Auto-categorisation

Business settings > Automation > Categorisation:
- **Always:** machine learning from past coding;
- **Supplier rules:** only when a supplier rule sets the category;
- **Never.**

With Never, items without a category cannot publish.

### 5.6 Auto-publish

Four levels:
- supplier (Costs > Suppliers > Auto-publish toggle);
- payment method;
- account (Connections > Manage > Settings > Automatic publishing > Auto-publish all items, with **Cost item
  exceptions** such as supplier statements and credit notes);
- AI Assist guidance.

Dext's own advice:
- start with suppliers whose documents never vary, and only after their rules publish correctly by hand;
- **avoid account-wide** auto-publish;
- leave out Amazon-type suppliers whose category changes with what was bought;
- check the History tab ("published via autopublish");
- published items cannot be unpublished; correcting means clearing publishing data and republishing.

Dext marks suggested suppliers with a sparkle (Suppliers > Auto-publish: Suggested) once they have published three
months without edits. An item still To review, held by an approval workflow, or on an exception list is not
auto-published.

### 5.7 Dext AI Assist

Written "guidance" rules, up to 1,500 characters each, set to **Manual review** or **Auto-apply**. They can:
- set category, tax, description, payment method, Publish to and line items;
- flag, publish or archive;
- read the **email body** (only when the guidance says so);
- use the uploader or owner as a condition.

They rank above every other rule. Guidance should be written as "publish if…"; there is no "don't publish" action.
**Free trial: 50 applied suggestions per client**, then a paid option. Example for CIS: "If an invoice refers to CIS,
group labour lines to CIS labour at gross, materials to Materials, and do not extract the CIS deduction."

### 5.8 Expense claims

Expense claims group a person's own-money purchases for reimbursement. **Auto Expense claims** (Business settings >
Automation) put every item a chosen user submits into a weekly, fortnightly or monthly claim, **ahead of auto-publish**.
It is a possible route for Minda's personal-card purchases, but how a claim posts in QuickBooks was not covered in the
articles read. **Not recommended until tested on one claim.**

_Sources: Rules and automation in Dext; How to use supplier and customer rules; How to set up payment method rules; How
to set up user rules; How Dext auto-categorises your Costs items; How to use auto-publish; Auto-publish best practices;
What is Dext AI Assist; Dext AI Assist: Account guidance; What are expense claims; How to set up Auto Expense claims._

---

## 6. Roles

- **Business Admin:** everything, including subscription.
- **User Admin:** all documents and most settings, but not Business Admins or the subscription.
- **Standard user:** own items only; can be given "Access all documents", "Create expense claims" and publishing
  rights.

Supplier rules, payment methods, duplicates, Fetch and AI Assist guidance are Admin-only. If Rachel were ever given a
login, **Standard user without publishing** would match her charter (she reads and recommends; QuickBooks stays
read-only).

_Source: Roles and permissions in Dext._

---

## 7. Recommended set-up for Fishbone Construction

Check first: what is already set. Minda's screenshots of **Payment methods** and **Suppliers** into Rachel's `Raw/`
let Rachel tick off this list.

**What is set today** (Minda's screenshots, 11/10/2026, 12:45):
- **Suppliers:** 709 in the list (Showing 50 of 709). Auto-publish **No** and Extract line items **No** on every
  supplier seen; Extract supplier statements **Yes** (the default). The **Category column is empty**: no supplier
  rules yet.
- **Costs inbox:** 4 items, all **To review**: E.H. Booth & Co 09/10 £116.97; RMT Technology £358.80; Bytestock
  £468.00 (2 issues); Anthropic Ireland £135.50. On every item the tax rate shows **"Extracted…" with a warning**, so
  a default tax code is probably not set (#2 below).
- **Expense claims, Supplier statements:** empty. **AI Assist:** present in the menu. **Payments:** locked (not on
  our plan).
- **Business profile:** CRN 7211420054 (Dext's own customer reference, not the Companies House number — Minda, 11/10/2026); base currency GBP; industry Construction and trades. VAT registration no. **GB190175216**, reporting cycle **Quarterly**, starting month **May** (entered by Minda 11/10, 14:36).
- **Connections:** QuickBooks Online (Fishbone Construction Ltd) **connected**. **Cost connections (Fetch): none.**
  Back up: **Google Drive, connected 11/10/2026 ~12:05** by Minda: folder **"Dext Prepare Backups"** in Minda's My Drive
  (`1Y07oPVFf34wZZZkdWCULS7QZct3wk3Qw`) > "Fishbone Construction Ltd - 7211420054" > **Costs** (`194du0OiSasR5kiMDioif_Az9Tb-sQtfm`)
  and **Sales**, one folder per month "YYYY - MM" from 2018 - 10; files named "Supplier - DextItemId.pdf/.jpg" (2025 - 04
  holds 67). Rachel can read every Dext document here.
- **Extraction:** account address `mindaugas.gaudiesius343@dext.cc` (Single), `…343@multiple.dext.cc`; Sales
  `…343+sales@dext.cc`. Our sends go to Minda's **user** address `mindaugas.gaudiesius@dext.cc`, which makes Minda
  the owner (items show "Mindaugas Ga…"). **Duplicate cost items: Automatic.** Extract tax: Yes. Due-date defaults:
  blank. Inbox tabs: off.
- **Lists > Categories:** 154, synced from QuickBooks, no codes, **all visible**, including balance-sheet accounts
  (Andrej Credit Card, Bank current account 2819, AT UK Interiors, Accruals…), which can be chosen by mistake as a
  cost category. **List visibility:** no groups.
- **Automation:** Auto-categorisation **Always**; Default category blank; Smart Suggestions shown, auto-apply off;
  Auto Expense claims not set; Archive after publishing Yes.
- **QuickBooks Online settings (14:34):** General: Default publish to costs **Bill**; Notify me when creating a new
  supplier **Yes**; Default prepayments category Prepayments. Tax: Use tax list **Yes**; Default tax for costs
  **20.0% S**; no-tax default (costs) **No VAT**; Default tax for sales **20.0% S**; no-tax default (sales) **No VAT**.
  Automatic publishing: Auto-publish all items **No**; exceptions ticked: Statements/remittance advice, Expense
  statements, Supplier statements. (Checklist rows 2–5 done.)
- **Not yet seen:** Lists > **Payment methods** and **Tax rates**; Profile > notifications.

### 7.1 Account settings (once)

| # | Where | Set to | Why |
|---|---|---|---|
| 1 | Profile > User settings > Bookkeeping email notifications | On acknowledgement = **Yes** | a rejected file is reported, not lost |
| 2 | Connections > QuickBooks Online > Settings > Tax | Use tax list on; default tax for costs **20.0% S**; default code when no tax is extracted **No VAT** | publishing does not fail on tax (codes as named in Construction's QuickBooks) |
| 3 | same > General | Warn me when creating a new supplier = **Yes** | stops "Www Scosarg.com"-type suppliers being created in QuickBooks |
| 4 | Business settings > Extraction > Duplicate items | **Review** | two genuine identical orders on one day are kept |
| 5 | Business settings > Automation > Categorisation | **Supplier rules** at first; Always later | no surprise categories while rules are set up |
| 6 | Automatic publishing (account level) | **Off** | Dext's own advice |

### 7.2 Payment methods (Business settings > Lists > Payment methods)

| Card | Name it | Link to QuickBooks account | Auto-publish |
|---|---|---|---|
| HSBC 2819 debit card(s) | "HSBC 2819 debit" | **Bank current account 2819** (Id 128) | None |
| Company credit card **6789** (Visa, in Minda's name) | "Company Visa 6789 – Minda" | **Minda Credit Card** (Id 130, a card account) | None |
| Andrej's card | "Andrej card" | **Andrej Credit Card** (Id 131) | None |
| "Company Credit Card" (Id 209) | which card this is: to confirm with Minda (few entries since June, paid from 2819) | Company Credit Card (Id 209) | None |
| Minda's **personal** card (when used for the company) | "Minda personal card" (digits to confirm) | none: publish as **Bill**, then clear against "Directors Loan Account – M Gaudiesius" (Id 16) | Never |

**Card 6789 is the company credit card** (Minda, 11/10/2026: "It is company credit card, not my personal"). Its
spend is booked to **"Minda Credit Card"** (Id 130) in QuickBooks: Anthropic, Adobe, Google, B&Q, LNER, the £32
annual fee. Link it there; items paid with it publish as **Credit card** against that account.

**Minda's personal card** is different: purchases on it are a director's loan (ruling of 8/10/2026, MW Machinery).
Dext can only publish a paid item to a bank or card account, and the director's loan (Id 16) is a liability account,
so personal-card items go in as a **Bill**, and the bill is cleared against the director's loan.

### 7.3 Supplier rules (Costs > Suppliers)

| Supplier | Category | Tax | Publish to | Other |
|---|---|---|---|---|
| Screwfix | Materials | 20.0% S | by payment method | duplicates Review |
| B&Q | Materials | 20.0% S | by payment method | duplicates Review |
| Hafele, IronmongeryDirect, Plumbfix | Materials | 20.0% S | by payment method | |
| JT Dove, Lathams, MKM | Materials | 20.0% S | by payment method | workflow note: "tag the job; rebillable if the job is charged at cost"; Lathams: "VAT invoice only, never the pro forma" |
| Tower Leasing | Software | **20.0% S** (QuickBooks default says none — fix it there too) | by payment method | |
| Anthropic | Subscriptions | 20.0% S (UK VAT on the receipt since October) | Credit card (company card 6789 → Minda Credit Card) | |
| RMT Technology (leased line) | Telephone | 20.0% S | **Bill** | paid by direct debit |
| SmartestEnergy | Electricity and Gas | per invoice | Bill | the direct debit pays the previous month's invoice |
| O2 | Telephone | 20.0% S | by payment method | Fetch |
| Bytestock, Renewtech, Amazon (IT parts) | Computer running costs, or an asset over the capitalisation limit | per invoice | by payment method | no auto-publish: the category depends on what was bought |
| Spotify, Audible | waits for Minda's answer (Entertaining or personal) | | | |

Auto-publish: **none at first.** After a month without edits, turn it on for Screwfix and Anthropic only.

### 7.4 Fetch

**Minda** connects Amazon.co.uk, O2, Spotify, Audible, Google, Microsoft Office365 and Wolseley, with the portal
logins; Travis Perkins and Howdens only if we have trade accounts. Document owner: Minda.

### 7.5 Not now

- Auto Expense claims (§5.8), until tested.
- AI Assist beyond the free trial; worth trying on the 50 free suggestions for CIS invoices.
- The AI Connector (§9).

---

## 8. Checks Rachel can do without a login

- **Sent:** every send is in `ops@` Sent (`to:mindaugas.gaudiesius@dext.cc`).
- **Bounces:** none from the Dext address.
- **Rejection notices:** these arrive in Minda's mailbox once §7.1 #1 is on.
- **QuickBooks after publishing:** the bill or expense exists with the document attached, under the right account and
  VAT code, and the bank feed line shows Match.

## 9. The Dext AI Connector — why it is not for us

It is a beta for **accounting practices on the Practice Advanced plan**, connected at **firm workspace** level, using
each person's Dext login. It is **read-only** and answers practice questions: client lists, time tracking, aged
balances, journals, UK tax estimates, many needing Dext's Data Health & Insights add-on. It does not expose a business
account's supplier rules, payment methods or inbox. If AGGA ever runs Dext as a practice with our account as a
client, Alexey's firm could use it; Fishbone cannot on its own.

_Sources: How do I add the Dext AI Connector to my workspace; How do I connect my Dext account to Claude, ChatGPT or
Copilot; What can I ask Dext through Claude, ChatGPT or Copilot; How does the Dext AI Connector keep your data secure._

---

## Changes

| Date | Change |
|---|---|
| 2026-10-11 | Written from 56 help-centre articles (Minda's request). |
| 2026-10-11 | §7: current state recorded from Minda's screenshots (two sets, 12:45 and 12:58). |
| 2026-10-11 | Google Drive backup connected ("Dext Prepare Backups"). |
| 2026-10-11 | §7.2 corrected: card 6789 is the company credit card (Minda), linked to "Minda Credit Card"; personal card = Bill cleared to the director's loan. |
