# TIDElwave COA Library — Design Brief

## What we're building

A public **Certificate of Analysis (COA) library** for TIDElwave Research Solutions. Customers scan a QR code on their peptide vial, land here, and verify that what they bought is real, third-party-tested, and matches the batch on their label. Live at **tw-researchsolutions.com**.

This is not a store, not a marketing site, not a product catalog. It exists for one job: **compliance-grade verification of what a customer already owns.**

## Who this is for

The primary user is a customer who just bought a research peptide from us. They may have never been to the site before. They're checking one thing: *is this legitimate?* Trust is the whole product.

Peptides are an industry with real trust issues — customers are used to being skeptical. Our advantage is that we actually test everything and can prove it. The site is where that proof lives.

## The one flow that has to be excellent

1. **Arrive** — usually from a QR code on packaging (phone, first time), sometimes typed URL
2. **Find** their peptide (by name) OR their specific batch (by lot number)
3. **See PASS** — immediate visual reassurance
4. **Confirm the batch matches** their vial (lot + date + testing lab)
5. **Optionally open the actual COA PDF** for the deep-inspection user

Under 15 seconds end-to-end for the common case. Everything else in the design is secondary.

## Current state

A working prototype is deployed at tw-researchsolutions.com. It's functional but generic — a clinical-light theme with report-style cards. It works; it doesn't yet *feel* trustworthy the way it should.

- **33 peptide stacks** in the catalog (single peptides like Semax, blends like CJC-1295 + Ipamorelin)
- Each stack has 0+ batches over time; newest is "current"
- Stacks with no COA yet are hidden
- Search filters by peptide name OR lot number
- Cards collapsed by default (name + PASS pill); tap to expand for metadata + PDF link
- Dedicated route per batch: `/pdf/<stack>/<batch>` renders the PDF inline with pdf.js, plus a batch selector for the stack's history

## Design requirements

- **Mobile-first.** Most traffic is a phone right after unboxing. Design for that first. Desktop should feel intentional, not scaled-up.
- **Trust and clarity above novelty.** Read "medical lab report," not "consumer brand." Restraint is a feature.
- **PASS is the emotional payoff.** Make it decisive.
- **Purity % is the data payoff.** Present it confidently — it's the number that answers "did this pass".
- **Lot numbers are gnarly.** They can be long alphanumeric (`20260424-BBG70-1CF1`) OR short informal (`Green Cap` — some labs don't issue structured lot numbers). Design must handle both without breaking.
- **Search is a first-class action.** Sticky, always accessible. Someone with a lot number on their vial should be one paste + one tap away from confirmation.
- **The site handles multiple labs.** Currently ILS Laboratories and Freedom Diagnostics; more likely in future. Design cannot hard-couple to any single lab's branding.

## Content per stack (the "report card")

- Peptide name (short or long — e.g. "Glow" vs "CJC-1295 + Ipamorelin (No DAC)")
- PASS status
- Batch metadata: lot, COA date, purity %, testing lab, lab's own reference number
- Full COA PDF link
- Batch history — older batches of the same peptide, each with its own PDF

## Page types

1. **Library / home** — searchable list of stacks that have a COA.
2. **Batch viewer** (`/pdf/<stack>/<batch>`) — inline PDF render with the same metadata card + a "batch history" selector so a customer viewing an older batch can jump to the current one. Includes a warning banner when viewing a non-latest batch.

## Constraints

- **Static site.** Vanilla HTML/CSS/JS only. No frameworks, no build step, no backend. Design has to be implementable in a single `<style>` block per page.
- **GitHub Pages hosting.** No server-side logic. Pretty URLs work via GH Pages' `404.html` fallback.
- **pdf.js renders each PDF page as a full-width canvas** — the viewer page needs to accommodate a variable-height inline PDF below (or beside) the metadata block.
- **All data lives in `pdf/manifest.json`** (schema in `pdf/README.md` in the repo). No CMS.
- **Zero brand system exists today.** This project is your chance to define one for the compliance surface.

## Deliverables we're looking for

- **Mobile and desktop mockups for both page types** (home + viewer)
- **Component states:** collapsed card, expanded card, search focus, no-results, "viewing older batch" banner, empty catalog, PDF loading, PDF failed
- **Design tokens:** color, type, spacing, radius — as a system we can wire into CSS variables
- **Interaction notes** for expansion, search behavior, batch selection on the viewer
- **A one-page rationale** covering major design choices

## Brand notes

- **TIDElwave Research Solutions** — the "TIDE" is the anchor, "lwave" is currently rendered as a secondary accent. Feel free to keep, evolve, or replace the wordmark treatment.
- No formal identity system yet. Treat this project as the seed for a compliance/verification brand surface.
- Prior aesthetic direction on the site was a dark "instrument / lab equipment" feel, which we moved away from. Current direction is clinical/medical minimalism. Push it further if you have a better read.

## Out of scope

- E-commerce, cart, checkout
- User accounts, login, saved-search
- Vial photography (we have none)
- Anything requiring a backend

## Repo & handoff

Repo: `github.com/2hv2yjnnhd-create/tw-researchsolutions`
Live: `tw-researchsolutions.com`
Local preview: `python3 serve.py` at repo root, then http://localhost:8000

Read `PROJECT_BRIEF.md` and `pdf/README.md` for how the data model works. `index.html` and `404.html` are the two pages to redesign.
