---
name: deploy-checklist
description: Steps and pitfalls for publishing or updating the TIDElwave COA site on GitHub Pages behind its custom domain. Use when preparing to go live for the first time, or before pushing a change that will affect the production site.
---

# Deploy checklist

The site is static files on GitHub Pages behind a custom domain that a
printed QR code depends on forever. Going through this before a push isn't
optional — a broken deploy here means physical product in the field with a
dead QR code.

## First-time setup (only if not already live)
1. Repo must be public (or Pages must be enabled for a private repo on a
   plan that supports it).
2. GitHub Pages source: deploy from the branch/folder containing
   `index.html` at the repo root — GitHub Pages serves it automatically, no
   configuration needed. This is why the site file is named `index.html`
   and not something else: the QR code encodes the bare domain with no
   path, so the root document must be the library.
3. Add a `CNAME` file at the repo root containing exactly the custom domain,
   nothing else (e.g. `coa.tidelwave.com`).
4. At the DNS provider: add the DNS records GitHub Pages requires (A records
   to GitHub's IPs for an apex domain, or a CNAME record for a subdomain) —
   confirm **auto-renew is ON** for the domain itself, not just correct DNS.
5. In GitHub repo settings → Pages, enter the custom domain and enable
   "Enforce HTTPS" once the certificate provisions.
6. Verify the Google Cloud API key is restricted to this exact domain (HTTP
   referrer restriction) before it's live — an unrestricted key is a real
   liability since it's shipped client-side.

## Every deploy (including updates)
1. Run the `verify-invariants` skill against the diff first — do not deploy
   anything that fails it.
2. Confirm `API_KEY` is set to the real, domain-restricted key in
   **`config.js`** and not left as `"PASTE_API_KEY_HERE"` (that value
   silently activates demo mode in `index.html` and the DEMO-only fixture
   in `viewer.html` — it fails safe, but a real deploy still needs the real
   key). `config.js` is the single source both `index.html` and
   `viewer.html` load — one edit updates both. If `grep -rn API_KEY` ever
   turns up a `var API_KEY = ...` declaration outside `config.js`, that's a
   regression: someone reintroduced a second copy.
3. Confirm the Drive folder (`19tn_iZlmUZBMLmMyw-7G16CY2Mht3eBi`) is still
   shared with "Anyone with the link — Viewer" so the public API key can
   list it. A permissions change here breaks the entire site silently.
4. Load the deployed URL after push and check both tabs (Current COAs, COA
   History) actually fetch and render real files, not the demo set.
5. Confirm the custom domain still resolves and serves over HTTPS with a
   valid cert — GitHub occasionally needs HTTPS re-enforced after a domain
   or DNS change.
6. Spot-check one "View COA (PDF)" link: it should open `viewer.html?id=...`
   in a new tab on the TIDElwave domain, not a raw `drive.google.com` URL.

## If something looks wrong post-deploy
- Blank site / no COAs: almost always either the Drive folder sharing
  permission or the API key restriction — check both before touching code.
- Domain not resolving: check DNS/registrar auto-renew status before
  assuming it's a GitHub Pages problem.
