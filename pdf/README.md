# pdf/

The site's data lives here. `manifest.json` is the single source of
truth; every stack has its own folder for the actual COA PDFs.

One COA covers a peptide across all its labeled doses — the lab
tests the peptide, not each dose. So each stack has a single line
of batches over time (never a per-dose subhistory).

## Folder layout

```
pdf/
  manifest.json
  README.md
  <stack-slug>/
    <YYYY-MM-DD>-<lab-short>-<tail>.pdf
    <YYYY-MM-DD>-<lab-short>-<tail>.pdf
```

- **stack-slug** — folder name and first URL segment. Matches the
  `slug` field in `manifest.json`.
- **filename** — see the *Filename convention* section below.

Each PDF is reachable at `/pdf/<stack-slug>/<filename-minus-.pdf>` —
the site's dedicated route page renders it in branded chrome.

## Filename convention

```
<YYYY-MM-DD>-<lab-short>-<tail>.pdf
```

- **YYYY-MM-DD** — the COA date. For ILS use *Analysis Date*, for
  Freedom use *Reported*. Whatever field the lab treats as "COA
  finalized on". Lets the folder sort chronologically.
- **lab-short** — a short tag identifying the lab: `ils`, `freedom`,
  etc. (Match the existing tags in the folder if there are any.)
- **tail** — whatever the lab gives you that is unique for this batch.
  For ILS that's the lot number lowercased (`20260424-bbg70-1cf1`).
  For Freedom, which doesn't issue structured lot numbers, use the
  Accession # (`2608120389`).

Examples:
```
pdf/glow/2026-07-16-ils-20260424-bbg70-1cf1.pdf
pdf/tirzepatide/2026-08-14-freedom-2608120389.pdf
```

## Adding a new batch (existing stack)

1. Save the PDF into `pdf/<stack-slug>/` using the filename convention
   above.
2. Open `manifest.json`, find that stack's entry, and **prepend** a
   new object to its `batches` array (newest-first is what the
   Current tab relies on).
3. Commit and push. GitHub Pages publishes automatically.

## Adding a new stack

1. Create `pdf/<stack-slug>/` and save the first batch PDF in.
2. Add a new top-level object to `manifest.json` (see field reference
   below).
3. Commit and push.

## Field reference

Per stack:

| field | required | notes |
|---|---|---|
| `slug` | yes | Must match the folder name under `pdf/`. |
| `product` | yes | Display name shown on the card and viewer. |
| `description` | no | One-sentence blurb rendered on card and viewer. |
| `benefits` | no | Array of strings, rendered as bullets. |
| `batches` | yes | Array (may be empty). Newest first. |

Per batch:

| field | required | notes |
|---|---|---|
| `file` | yes | Filename inside the stack folder. |
| `date` | yes | ISO `YYYY-MM-DD`. The COA's finalized date. |
| `purity` | yes | Display string, e.g. `"99.79%"`. |
| `lab` | no (recommended) | Lab name as displayed, e.g. `"ILS Labs"` or `"Freedom Diagnostics"`. Shown on card and viewer. |
| `lot` | no | Lot as printed. May be a formal number (`20260424-BBG70-1CF1`) or an informal tag (`"Green Cap"` — Freedom uses cap-color labels). Omit if the lab doesn't provide one. |
| `reference` | no | Lab-assigned identifier: COA #, Accession #, Search Code, etc. Shown on the viewer detail page. |

**Why `date` and `purity` are the only required batch fields:** they're
the only things every lab we've seen so far always provides in the
same conceptual form. Lot number is unreliable (Freedom uses cap
colors, not structured lots); COA #/Accession is lab-specific.

A stack with an empty `batches: []` renders on the Current tab with a
"COA on the way" state and is omitted from the History tab.

## Adding batches with Claude

When you have new COA PDFs to place, drop them in the repo root (or
tell Claude where they are) and say something like *"sort these into
`pdf/`"*. Claude will run the workflow below. This section exists so
Claude can re-read it and stay consistent across sessions.

### Workflow

1. **Locate the PDFs.** Check the repo root first, then wherever the
   user pointed. `ls <path>/*.pdf`.
2. **Read every PDF with the `Read` tool** to extract per-batch
   metadata. Do this in parallel — one `Read` call per file in a
   single message.
3. **Extract these fields per PDF:**
   - **Product / peptide name** → maps to a stack slug in
     `manifest.json`. If a match is ambiguous, ask.
   - **Lab** → `"ILS Labs"` or `"Freedom Diagnostics"` (or ask for the
     display name if it's a new lab).
   - **COA date** → for ILS use *Analysis Date*, for Freedom use
     *Reported*. Always output ISO `YYYY-MM-DD`.
   - **Purity %** → verbatim display string, e.g. `"99.79%"`.
   - **Lot** → the *Lot Number* field. For Freedom this is often an
     informal tag like `"Green Cap"` — that's fine, store it as-is.
     Omit the field if the COA has no lot at all.
   - **Reference** → *COA #* (ILS) or *Accession #* (Freedom) or the
     equivalent lab identifier.
4. **Detect duplicates.** If two PDFs share the same reference #, lot,
   and date, treat them as duplicates: place one, leave the other in
   place, and flag it for the user to confirm delete.
5. **Build the new filename** per the *Filename convention* section
   above:
   - `lab-short` = `ils` for ILS Labs, `freedom` for Freedom
     Diagnostics, or a short lowercase tag for a new lab (confirm
     with the user).
   - `tail` for ILS = lot number lowercased with non-alphanumerics
     turned into hyphens (`20260424-BBG70-1CF1` → `20260424-bbg70-1cf1`).
   - `tail` for Freedom = the Accession # as-is
     (e.g. `2608120389`).
6. **Move the PDF** with `mv` from its source path to
   `pdf/<stack-slug>/<new-filename>.pdf`. Delete the folder's
   `.gitkeep` if present (folder is no longer empty).
7. **Update `manifest.json`:** prepend a new batch object to the
   target stack's `batches` array. Required fields: `file`, `date`,
   `purity`. Include `lab`, `lot`, `reference` whenever available.
8. **Verify:**
   - `python3 -c "import json; json.load(open('pdf/manifest.json'))"` — JSON parses.
   - Serve locally with `python3 serve.py` (the repo's dev server —
     mirrors GH Pages' 404.html fallback so pretty routes work), then
     `curl -I` each new PDF URL — all should return 200.
9. **Report back** with a summary table: which stack got which
   batch, plus any duplicates or missing fields.

### Adding a brand-new lab

If a PDF comes from a lab that isn't ILS or Freedom, before
proceeding:
1. Confirm the display name for the `lab` field (how it should appear
   as "Tested by …" on the site).
2. Confirm the `lab-short` tag for filenames (2–8 lowercase chars).
3. Confirm which date field to use (Analysis Date / Reported /
   Issued / etc.).
4. Update this section with the mapping so future sessions have it.

