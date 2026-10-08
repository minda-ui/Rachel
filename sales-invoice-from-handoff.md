# Sales invoice from a hand-off

_Adopted by owner decision (Minda), **2026-10-08** ("Adopt all five", skill candidate SC-2). Amendment 49. Built from
FC0237 (131 Goathland Avenue, 29 Sep 2026) and FC0238 (Macdonald Joinery, FC2612, 5 Oct 2026)._

---

## 0. When

A colleague (usually Anna) or Minda asks for a sales invoice: a hand-off note in Rachel's `Raw/` and a Hub row.
**Rachel creates a sales invoice only on Minda's explicit word for that invoice** ("yes, create FC0238"); Minda sends
it. Payments, credit notes and anything to a customer are Minda's.

## 1. Before creating

1. **Read the hand-off and its sources**: the purchase order, the quote, what was done and when, any photos or
   measurements. Note anything not charged (return visits, materials still to come).
2. **Customer record.** Construction bills each job as a **project** under the main customer (FC2606, FC2609, FC2612
   under Macdonald Joinery and Construction). **CIS items are refused on a plain sub-customer** ("You cannot select
   CIS accounts/items for a non-CIS supplier/customer"): if the job is not a project yet, Minda creates it in the
   QuickBooks UI (the connector cannot), then Rachel uses the project's Id.
3. **Tax treatment from the precedent.** Find the last invoice to the same customer and copy its item and tax code.
   Construction labour for a contractor: item "CIS labour gross (0%)", tax code "20% RC CIS" (domestic reverse
   charge, VAT £0). Work for a group company or a private client: standard VAT. If the hand-off asks "does reverse
   charge apply?", answer from the precedent and say so.
4. **Number.** Next `DocNumber` after the highest in QuickBooks (`FC0237` → `FC0238`). Terms, bill address and
   email from the precedent.
5. **Show Minda** the lines, amounts, tax and dates in one short table, and wait for "yes, create".

## 2. Create and read back

1. `QUICKBOOKS_CREATE_INVOICE` from a JSON payload, with a `requestid` and a `private_note` saying who asked and on
   whose instruction.
2. **Read it back** (`SELECT * FROM Invoice WHERE DocNumber = …`): customer, lines, item, tax code, VAT, total,
   dates, email, and **EmailStatus = NotSet** (not sent).
3. If QuickBooks refuses, **nothing is created**: fix the cause (usually the customer record) and try again with a
   fresh `requestid`.

## 3. Record

1. **Document Register**: next number for the company (find the highest first), Direction Outgoing, Category
   Invoice, Status **Draft**, Source key = "QuickBooks … Invoice Id …". The QuickBooks PDF carries bank details:
   no copy on Drive.
2. **Hub row**: In Progress, with the invoice number, amount and due date.
3. When Minda says it is sent: read back **EmailStatus = EmailSent**, set the register row **Issued**, the Hub row
   Done.

## 4. Traps

1. A project created to fix the CIS refusal can clash by name with the plain record: make the old record inactive
   before renaming (FC2612 "…Merry Hill 2").
2. A PO number field may not exist on the invoice form: put the PO in the line description.
3. Never invoice from a quote alone: the PO or Minda's word decides the amount.
