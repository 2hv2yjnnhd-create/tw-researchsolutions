---
name: verify-invariants
description: Check a proposed or just-made change to the TIDElwave COA site against the project's hard constraints (domain, Drive folder, no backend, no build step, zero-touch publishing). Use before finishing any code change, before committing, and before deploy.
---

# Verify invariants

This site is reached by a QR code printed permanently on physical product
packaging. The URL can never change. That one fact drives every constraint
below — treat all of them as non-negotiable unless the user explicitly says
otherwise in this conversation.

Run through this checklist against the diff (or the full file, if unsure)
before calling any change finished.

## 1. The domain never changes
- No change should alter, remove, or make conditional the custom domain the
  site is served from (the `CNAME` file for GitHub Pages, any hardcoded
  domain references).
- If a change touches DNS, GitHub Pages settings, or the `CNAME` file, stop
  and flag it explicitly — auto-renew must stay on and the domain must never
  lapse.

## 2. The Drive folder ID never changes
- The folder ID `19tn_iZlmUZBMLmMyw-7G16CY2Mht3eBi` must stay hardcoded and
  unchanged. `grep` for it after any edit near the Drive API calls to confirm
  it's still present verbatim.
- No change should ever call a delete/trash operation on this folder, or on
  files inside it — the site only ever *reads* Drive, never writes.

## 3. No backend, no build step
- All logic stays in static HTML/CSS/JS served directly from GitHub Pages.
- Reject any change that introduces a server, a build tool, a package
  manager, a framework, or an env-var/secrets-management layer for the API
  key. The API key is meant to be embedded client-side (it's domain-locked
  and read-only) — do not "fix" this by moving it server-side.
- `FOLDER_ID` and `API_KEY` are declared exactly once, in `config.js`,
  which both `index.html` and `viewer.html` load via `<script src=
  "config.js">` before their own script runs. Never reintroduce a `var
  API_KEY = ...` declaration inside either HTML file — that's the two-file
  drift risk `config.js` exists specifically to remove. `grep -rn "var
  API_KEY"` should match exactly once, in `config.js`.

## 4. Publishing a COA must never require a code change
- The only supported way to add a COA is: Damian drags a PDF into the Drive
  folder, named `Product Name - Lot Number.pdf`.
- Any change that would require editing a list of products, a mapping file,
  or redeploying the site in order for a new COA to appear is wrong — reject
  it or redesign it so the site continues to derive everything from the live
  Drive folder listing at request time.
- Malformed filenames (missing ` - `, no lot number, etc.) must render as
  their own standalone card, never throw or break the rest of the page.

## 5. Customers never see Google Drive
- No visible Drive branding, no `drive.google.com` URLs in the normal path.
- PDF links go to the same-origin `viewer.html?id={fileId}`, opened via
  `target="_blank" rel="noopener"` so the library stays open behind it.
- A raw Drive link (`drive.google.com/file/d/{id}/view`) is acceptable **only**
  as a fallback shown when `viewer.html` fails to load the file — never as
  the primary link.
- `viewer.html` loads pdf.js from a version-pinned CDN URL (currently
  `3.11.174`), never `@latest` — an unpinned version can change out from
  under a page nobody will ever redeploy to fix.

## 6. Demo mode stays intact — and exercises the real customer path
- The site must keep working in demo mode (`API_KEY === "PASTE_API_KEY_HERE"`)
  showing sample COAs, so it can be tested and previewed without live
  credentials. Don't remove or silently break `renderDemo()` /
  `demoHistoryGroups()` while changing the live-data path.
- Demo mode must include `DEMO_VIEWER_FIXTURE` (fileId `"DEMO"`) in the
  Current COAs render, so the new-tab `viewer.html?id=...` path — the one
  real customers actually hit — gets exercised without a real key, not just
  the in-page sample-COA modal. `viewer.html` special-cases `id === "DEMO"`
  to render a placeholder instead of attempting a live Drive fetch. Don't
  let a future change silently drop this fixture back to modal-only demo
  coverage.

## How to report
List each of the 6 items with a one-line pass/fail/n-a and, for anything
that fails, the exact line(s) responsible. If everything passes, say so
briefly — don't pad it out.
