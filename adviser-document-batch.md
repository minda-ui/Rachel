# Filing a batch of documents from an adviser

_Adopted by owner decision (Minda), **2026-10-08** ("Adopt both", skill candidate SC-6). Amendment 50. Built from RMT's
21 PDFs (8 Oct 2026), Haroon's (Q Accountants) seven PDFs and the Companies House dormant accounts (FM0000022) the
same evening._

---

## 0. What it is for

An adviser sends several papers at once: accounts, CT600s, computations, returns, often re-sent copies of papers we
already hold. This skill sorts each one into **new**, **supersedes** or **duplicate**, files it, registers it, and
reports what is still missing. It is not for reading the papers for their content and replying: that is
`adviser-papers.md`.

**The lesson that made it a skill:** on 8 Oct every one of RMT's 21 checksums differed from the files we held, yet five
were the same returns (unsigned copies of DocuSigned ones), one was the as-filed version of a "For Approval" return and
one the final amended version of draft accounts. **Only the content tells them apart**: not the checksum and not the
filename. A filename's year ("CT600_2025") was not the period.

---

## 1. Capture

1. Download every attachment from the email (`GMAIL_GET_ATTACHMENT`; S3 links expire in about 60 seconds, so
   download at once). Companies House documents: read them with `COMPOSIO_SEARCH_FETCH_URL_CONTENT` (`extras`
   `{"links":60}` lists the document links), or ask Minda to put the PDF in `Raw/` when the link expires.
2. Record for each file: name, size, md5, page count, source (mailbox, message id, sender, date).
3. Count the files from the download, not from the email's list.

## 2. Identify each paper by its content

For each PDF, `pdftotext -layout` and read:
- **company** (name and number on the face, not the email subject);
- **kind**: statutory accounts / CT600 / computation / combined "computation and return" / signed return /
  dormant accounts;
- **period**: the period boxes on a CT600 (box 30–35), the accounts' period end, the computation's heading. A CT600
  covers at most 12 months: a long accounting period gives **two** returns;
- **status**: draft / "For Approval" / signed / as submitted (IRmark, submission receipt) / final amended;
- **key figures**: profit, tax due, turnover, net assets. These are what prove two copies are the same paper.

## 3. Compare with the register

Search the Document Register (`7352854736144260`) for the same company, kind and period. Then decide:

| What you find | Decision | Action |
|---|---|---|
| Nothing for that company, kind and period | **New** | Next number, file, register |
| A draft or "For Approval" copy, and this is the as-filed or final one | **Supersedes** | New number; old row Status → **Superseded**, with a note naming the new number |
| Same text and figures (unsigned v signed, re-print, different scan) | **Duplicate** | Do not register. File to Rachel's `Archive/` named `DUPLICATE of <doc no> - …`; note it on the original row |
| Same period, different figures, both final | **Stop** | Ask Minda: an amended return or an error |

Compare **text and figures**, never checksums. Different md5 with the same content is the normal case.

## 4. File and register

1. **Re-check the high-water number per prefix** (FC, FH, FP, FW, FM) in the register just before numbering. Another
   batch may have taken numbers since you last looked.
2. Name: `<doc no> - Compliance-<Statutory Accounts | Corporation Tax> - <what> <period> [<adviser>].pdf`.
3. Move and rename in **one** call (`GOOGLEDRIVE_UPDATE_FILE_PUT` with `name`, `add_parents`, `remove_parents`) into the
   company's archive `Annual Accounts` folder. Uploads go up with `GOOGLEDRIVE_UPLOAD_FILE`.
4. **Drive rate limits** (HTTP 403 "Quota exceeded") hit mid-batch: pause and retry. Then verify **every** file once:
   name, parent folder, md5.
5. Register row: Doc No, Entity, Direction (Received), Date (of the document), Category, Title, Description (period,
   status, key figures, source email), Status (Received / Superseded), Source key (message id), File link, Location.

## 5. Report to Minda

- What was new, what superseded what, and what was a duplicate, by number.
- **The gaps:** for each company, every period since incorporation, with accounts and CT return held or missing. On
  8 Oct this showed the missing Waste and Commercial Properties periods, which went back to Q Accountants.
- Anything wrongly labelled before, corrected in place, and said so plainly (FM0000019 was titled "period ended 30
  April 2025"; it is one computation for 1/11/23–30/4/25).
- Whether a thank-you or chaser is needed. **Drafts only**, for Minda to send.

## 6. Traps

1. **A different checksum does not mean a different paper** (§0).
2. **The filename's year is not the period.** Read the period boxes.
3. **One computation can cover two returns** (a long period: FM 1/11/23–30/4/25). Ask the adviser before chasing a
   "missing" computation.
4. **A form-field warning from `pdftotext` is not corruption.** FW0000016 was wrongly called "partly corrupt"; it
   renders fine. Open the page before saying a file is damaged.
5. **A dormant company's first accounts may be filed by the directors**, not the adviser: look at Companies House.
