# TIDElwave COA Library — Project Brief

## What this is
A public **Certificate of Analysis (COA) library** for TIDElwave peptide products. A QR code printed on product packaging sends customers to a website where they can look up the lab test results for the exact product and lot they bought.

The QR is printed permanently, so the URL it encodes can never change.

## How it works
```
QR code (printed forever)
  → custom domain (auto-renew ON, must never lapse)
  → GitHub Pages static site
  → JS lists a public Google Drive folder via Drive API v3 (domain-restricted API key)
  → PDFs shown to the customer through an on-domain viewer
```

The whole point of the design: **Damian drags a COA PDF into the Drive folder and the site updates itself.** No rebuilds, no deploys, no code changes, no developer involved. Ever.

Customers never see Google Drive — no Drive branding, no Drive URLs.

## File naming convention
COAs in the Drive folder are named:

```
Product Name - Lot Number.pdf
```

Everything before the first ` - ` is the product name and determines which card the PDF groups under. Malformed names must not crash anything — they render as their own standalone card.

## Site structure
Two tabs:

- **Current COAs** — newest lot per product, shown as "LAB TESTED" cards.
- **COA History** — every lot ever, grouped by product, newest tagged "Current", searchable by lot number.

Clicking a peptide card opens its detail view, which offers a clear **"View COA (PDF)"** link. That link opens in a **new browser tab** (`target="_blank" rel="noopener"`) so the library stays open behind it.

The new tab goes to a **same-origin `viewer.html?id={fileId}`** page that renders the PDF with pdf.js. This was chosen over linking directly to `drive.google.com/file/d/{id}/view` specifically so the URL stays on the TIDElwave domain and customers never see Google branding. A raw Drive link is acceptable only as a fallback if `viewer.html` fails to load the file.

## Drive folder
Drive folder already exists: **"TIDElwave COAs"**, id `19tn_iZlmUZBMLmMyw-7G16CY2Mht3eBi`.

## Hard constraints — do not break these
- **The domain must never change and must never lapse.** Every printed QR code dies with it.
- **The Drive folder must never be deleted or trashed.** The folder ID is hardcoded and must live forever.
- **The API key is safe to embed in client-side code** — it only reads public data and is locked to the domain. Don't refactor it into a backend or env var; there is no backend by design.
- **No build step, no framework, no server.** Static files on GitHub Pages only.
- **Adding a new COA must never require touching the code.** If a proposed change would mean Damian has to edit a file, update a list, or redeploy to publish a COA, it's the wrong change.
