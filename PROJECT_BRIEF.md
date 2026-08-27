# TIDElwave COA Library — Project Brief

## What this is
A public **Certificate of Analysis (COA) library** for TIDElwave peptide products. A QR code printed on product packaging sends customers to a website where they can look up the lab test results for the exact stack and lot they bought.

The QR is printed permanently, so the URL it encodes can never change.

## How it works
```
QR code (printed forever)
  → custom domain (auto-renew ON, must never lapse)
  → GitHub Pages static site
  → reads pdf/manifest.json to render the peptide-stack cards
  → per-batch dedicated route at /pdf/<peptide>/<batch>
     served by 404.html (SPA fallback), which renders the PDF
     at pdf/<peptide>/<batch>.pdf with pdf.js in branded chrome
```

## Repository layout
```
index.html            – library home (search + Current/History tabs)
404.html              – dedicated PDF viewer route
pdf/
  manifest.json       – single source of truth for peptides + batches
  README.md           – naming rules and how to add a batch
  <peptide-slug>/
    <batch-slug>.pdf  – actual COAs
CNAME                 – custom-domain binding
```

`config.js`, `viewer.html`, and the Google Drive listing code that used to power the site have been removed. PDFs now live in the repo, not in Drive.

## Naming
- **Peptide-stack slug** — the folder name under `pdf/`, and the first URL segment. Lowercase, hyphens (`glow70`, `semax`, `tesamorelin-ipamorelin`).
- **Batch slug** — the PDF filename inside the peptide folder, minus `.pdf`, and the second URL segment. Convention: lowercased lot number with any non-alphanumerics turned into hyphens (`20260424-bbg70-1cf1.pdf`).

Each COA is reachable at `/pdf/<peptide-slug>/<batch-slug>`.

## Site structure
Two tabs, both driven by `pdf/manifest.json`:

- **Current COAs** — one card per peptide stack showing `batches[0]` (the newest). Card displays product, description, benefits, lot, and (when available) date and purity. Stacks with no batches yet render with a "COA on the way" placeholder. "View COA (PDF)" opens the dedicated route in a new tab. One COA covers a peptide across all its labeled doses — dose is a packaging detail, not part of the lab test.
- **COA History** — every batch on file, grouped by peptide, newest tagged **CURRENT**. Searchable by lot number.

The dedicated route (`/pdf/<peptide>/<batch>`, served by `404.html`) shows the same peptide info block above the PDF, plus a direct download link.

## Adding a COA
1. Drop the PDF into `pdf/<peptide-slug>/` using the batch-slug convention.
2. Edit `pdf/manifest.json` — either **prepend** a new batch to an existing peptide's `batches` array, or add a new top-level peptide object (see `pdf/README.md` for the full schema).
3. Commit and push. GitHub Pages publishes automatically.

## Hard constraints — do not break these
- **The domain must never change and must never lapse.** Every printed QR code dies with it.
- **The URL scheme `/pdf/<peptide-slug>/<batch-slug>` must remain stable.** Once a QR is printed pointing at a specific batch, that URL is committed forever.
- **No build step, no framework, no server.** Static files on GitHub Pages only.
- **404.html must always be present at the site root** — it's the only thing that makes the `/pdf/<peptide>/<batch>` routes resolve.
- **Batches must stay newest-first in `manifest.json`.** The Current tab reads `batches[0]` blindly; a mis-ordered array will show a stale COA as current.
