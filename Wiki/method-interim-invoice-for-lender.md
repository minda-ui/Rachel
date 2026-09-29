# Method — interim invoice between group companies, when a lender asks for invoices

_Written 2026-09-29 on Minda's decision ("Yes, go ahead"), from invoice FC0237: Fishbone Construction to Fishbone
Properties, 131 Goathland Avenue, sent to PLS Solicitors for Landbay condition OC80. A Wiki method, not a skill:
the pattern will repeat for FC0237's later applications and the final account, and for any refurbishment a lender
asks about._

---

## 1. When it applies

A lender (usually through the conveyancing solicitor) asks for **invoices for works done** at a property, and
the works were carried out by a group company — in practice Fishbone Construction for Fishbone Properties or
Commercial Properties. Check first what the lender actually needs: on 131 Goathland it was offer condition
**OC80** — "an invoice and photographs" for one specific item (the rear door), with the whole refurbishment
invoiced around it.

**Look for an existing invoice first.** Construction had never invoiced Properties; the QuickBooks job
("FC2603 131 Goathland Avenue", a sub-customer of Fishbone Properties Ltd) already existed and held the costs.

---

## 2. Decisions that are Minda's, asked in one message

1. **Who did the work** named by the lender, and how many days (this is what the invoice line must describe).
2. **Scope:** only the item the lender named, or the whole job.
3. **Basis:** the job budget's **commercial** rates or its **internal** (cost) rates. Show both totals side by
   side before she chooses — the difference on 131 Goathland was about £11,000.
4. **How much now:** a percentage (75% was first proposed) or a target amount (the answer was "around
   £35,000 including VAT").
5. **VAT:** Construction charges 20% to Properties; Properties cannot reclaim it on a residential let. Flag the
   5% renovation rate once as a question for RMT (a home empty two years or more); do not advise.
6. **Billing address** if QuickBooks has none.

Ask them as numbered questions and wait. **Do not price before 1–4 are answered.** On FC0237, running ahead
produced a 75% draft that was then replaced; and one answer ("normal cost") was read the wrong way before it
was pinned down.

---

## 3. Pricing the application

- **Contract value** = the job budget's plan total at the chosen rates, **less every item marked not done**,
  **plus additional works** that were never in the plan (on FC0237: the rear opening and the decking, labour at
  the budget's commercial day rate of £400 per man-day, materials at cost).
- **This application** = additional works that are complete, claimed in full, **plus** a percentage of the
  main works chosen to reach the target. State the percentage on the invoice.
- **Anything not yet invoiced by the supplier** (on FC0237: the door and the decking materials from MKM) goes
  on the final account, said so on the invoice, **never estimated**.
- **Later applications** show "less previously invoiced", so no work is billed twice.

---

## 4. Wording — describe what was built

The invoice line for the lender's item must match the photographs. On 131 Goathland the condition assumed a door
matching the original opening; the opening had been a large window, deliberately reduced. The line reads
exactly that: *existing large window opening reduced; new external door fitted; remainder clad in anthracite
composite cladding*. **Never word an invoice to fit a lender's condition that the works do not literally meet** —
say what was done, and let the covering email explain.

The covering email says plainly that the contractor is a **group company under the same directors**. The lender
will see it anyway; better it comes from us.

---

## 5. Creating it

1. **Draft first** as a PDF (marked DRAFT) in Rachel's `Outputs/`, from the job budget; show Minda.
2. **Create in QuickBooks only on Minda's explicit instruction for that invoice** — the charter's NEVER list
   allows it only on a human decision, and it is **not** the `RA-3` posting authority. Use the company's own item
   ("Construction Services") and the **standard 20% VAT code**, not the domestic reverse charge Construction uses
   with trade clients. Pass an idempotency key (`requestid`). Do not email it from QuickBooks.
3. **Read it back** from QuickBooks and check the totals and VAT against the draft. QuickBooks' PDF prints the
   company's VAT number — the draft's placeholder is filled by that — **and the bank details**, so the QuickBooks
   PDF is sent but **not stored on Drive** (no sort codes stored).
4. **Register it** (Outgoing, `Invoice`) after a fresh high-water check — two numbers were taken overnight before
   FC0237 was registered. Status **Draft** until sent, **Issued** once the Sent folder confirms it.

---

## 6. Sending it

- **Draft the reply in the correspondent's own thread, in the mailbox the correspondence actually uses.** For
  Properties' lender and solicitor correspondence that is **`info@fishboneproperties.co.uk`** (connected
  2026-09-29, Amendment 40), not `ops@fishboneconstruction.co.uk`, which would reach the solicitor from the
  wrong company.
- Attach the invoice **and the photographs again**, even if sent before — the lender assembles one file.
- **Photo and document numbers from the register, not from the property's Wiki page**: the page still carries the
  pre-migration numbers, one lower (on 131 Goathland the completion photos are **FP0000029**, the page says
  FP0000028).
- Minda sends. Then confirm it in the Sent folder, with the attachments, before marking the register row Issued.

---

## 7. Left open by FC0237 (for the next application)

The door and decking materials (MKM, not yet invoiced); the remaining main works (£31,530.07 at commercial
rates, on the plan as it stood on 2026-09-29); Anna's pending budget updates, which change actual costs but not
the contract value.
