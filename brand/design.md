# TideWave Research Solutions — Design System

The single source of truth for the rebrand. Anything on the site, on a label, or in an ad should be traceable to a rule in this file.

Built on the **Nocturne** design system (attached to this project), re-tinted to the TideWave palette. Nocturne's structure is inherited as-is: dark ground, OKLCH tonal ramps, 0.7× density spacing, 8px radius family, outlined primary buttons, accent-as-line-not-flood, `.lighten` image treatment, Phosphor icons. Where this file names a value, it overrides Nocturne's default. The two deliberate divergences are recorded at the bottom.

---

## 1. Brand in one paragraph

TideWave sells research peptides direct to independent researchers. The buyer is technical, skeptical, and has been burned by vendors who look like supplement brands. So the brand reads as **instrument, not supplement**: black ground, machined chrome, one electric blue, and numbers you can check. The tagline already carries the idea — *Built beneath the surface*. The visual system says the same thing: dark, deep, precise, nothing floating on top for decoration.

**Tone:** flat and factual. State the compound, the mass, the purity, the lot. No hype adjectives, no benefit claims, no second person selling. If a sentence could appear on a certificate of analysis, it's on-brand.

---

## 2. Color

Near-black ground with a blue cast, a chrome-silver neutral ramp, and one electric blue accent. Blue appears as **light** — lines, edges, glows, small fills — never as a large flat field.

### Tokens

```css
:root {
  /* Grounds — deep, blue-cast ink. Never pure #000. */
  --tw-ink-900:      #05070c;  /* page ground */
  --tw-ink-800:      #0a0e16;  /* section ground */
  --tw-ink-700:      #111722;  /* card / surface */
  --tw-ink-600:      #1a2130;  /* raised surface, input fill */
  --tw-ink-500:      #262f41;  /* hairline borders, dividers */

  /* Chrome — the neutral ramp. Text, borders, the metal gradient stops. */
  --tw-chrome-100:   #f4f8fc;  /* highlight stop, headline text */
  --tw-chrome-200:   #dde5ee;  /* body text on ink */
  --tw-chrome-300:   #bcc7d4;  /* secondary text */
  --tw-chrome-400:   #93a1b1;  /* muted text, labels */
  --tw-chrome-500:   #6d7b8c;  /* disabled, meta */
  --tw-chrome-600:   #4c5766;  /* mid gradient stop */
  --tw-chrome-700:   #333c48;  /* shadow gradient stop */

  /* Accent — electric blue. */
  --tw-blue-100:     #e8f2ff;
  --tw-blue-200:     #b9d8ff;
  --tw-blue-300:     #7fb6ff;  /* accent text at paragraph size */
  --tw-blue-400:     #3d92ff;  /* hover / pressed */
  --tw-blue-500:     #0a6be1;  /* THE accent — borders, marks, links */
  --tw-blue-600:     #0654b4;
  --tw-blue-700:     #043d84;
  --tw-blue-800:     #032a5c;  /* tinted fills on dark */
  --tw-blue-900:     #021a3a;

  /* Semantic */
  --tw-verified:     #2fbf8f;  /* COA present / in-spec only */
  --tw-warn:         #e0a13c;  /* low stock, batch notice */

  /* Elevation — edge + ambient darkness, per Nocturne */
  --tw-shadow-sm: 0 0 0 1px var(--tw-ink-500);
  --tw-shadow-md: 0 0 0 1px #313b4c, 0 6px 18px rgba(0,0,0,.55);
  --tw-shadow-lg: 0 0 0 1px #4c5766, 0 16px 40px rgba(0,0,0,.7);
  --tw-glow:      0 0 24px rgba(10,107,225,.35);
}
```

### Ratios (per screen, not per site)

- 70% ink grounds · 22% chrome text and borders · 8% blue.
- Maximum **one** glowing element per viewport. Two glows and it reads as a gaming site.
- Blue at full saturation across an area larger than a button = off-brand. The one licensed exception is the **tide band**: a full-bleed wave-masked blue field at the bottom of the homepage hero, echoing the vial label. Once per page.
- `--tw-verified` green is reserved for COA/in-spec status. Never decorative.

---

## 3. Type

Three roles. Two families.

| Role | Family | Weight | Case | Tracking |
|---|---|---|---|---|
| Display — compound names, hero, big numerals | **Saira Condensed** | 700 | UPPERCASE | −0.01em |
| Body & UI — paragraphs, tables, buttons, nav | **Inter** | 400 / 500 | Sentence | 0 |
| Eyebrow — kickers, section labels, badge text | **Saira Condensed** | 500 | UPPERCASE | 0.22em |

Saira Condensed carries the industrial compression of `RETATRUTIDE` on the label. Inter is inherited from Nocturne and does all the reading work. Nothing else — no third face, no script, no serif.

```css
--tw-font-display: "Saira Condensed", "Arial Narrow", sans-serif;
--tw-font-body:    "Inter", system-ui, sans-serif;
```

### Scale

| Token | Size / line-height | Use |
|---|---|---|
| `display-xl` | 88 / 0.92 | Homepage hero compound or headline |
| `display-l` | 56 / 0.96 | Section headlines, product detail name |
| `display-m` | 34 / 1.05 | Card titles, dose figures |
| `eyebrow` | 12 / 1.2 | Kickers, badges, table headers |
| `body-l` | 18 / 1.6 | Lead paragraph |
| `body` | 15 / 1.65 | Default |
| `body-s` | 13 / 1.5 | Meta, lot numbers, footnotes |
| `mono` | 13 / 1.5 | Lot #, batch ID, CAS, sequence — `ui-monospace, "SF Mono", monospace` |

Rules: headlines flush left. Never center a paragraph. Body copy is never blue — use `--tw-blue-300` if accent text is unavoidable at paragraph size. Compound names always uppercase display; never title case.

---

## 4. Chrome — the signature treatment

Chrome is what makes this brand recognizable, and it is also what breaks a website if overused. It is a **material with three legal forms** and nothing else.

**A. Chrome text** — display sizes 34px and above only. Below that it turns to grey mud.

```css
.tw-chrome-text {
  background: linear-gradient(180deg,
    var(--tw-chrome-100) 0%, var(--tw-chrome-300) 42%,
    var(--tw-chrome-600) 52%, var(--tw-chrome-200) 62%,
    var(--tw-chrome-100) 100%);
  -webkit-background-clip: text; background-clip: text;
  color: transparent;
}
```
Pair with a 1px `--tw-ink-900` text-shadow for edge definition. Never on a paragraph, never on a button label, never on a nav item.

**B. Chrome edge** — a 1px gradient border for cards, badges, and the primary button. This is the workhorse; use it far more than chrome text.

```css
.tw-chrome-edge {
  border: 1px solid transparent;
  background:
    linear-gradient(var(--tw-ink-700), var(--tw-ink-700)) padding-box,
    linear-gradient(160deg, var(--tw-chrome-300), var(--tw-chrome-700) 45%, var(--tw-chrome-200)) border-box;
}
```

**C. Chrome plate** — the label's `20 MG` / `99% PURITY` lozenge, ported to screen: chrome edge + `--tw-ink-800` fill + `radius-sm` + eyebrow or display type inside. Used for dose, purity, and COA badges only.

**Not legal:** bevels, emboss, drop shadows on type, glossy highlights swept across panels, chrome on icons, chrome on body text, chrome on anything under 34px except the plate's border.

---

## 5. The wave

The helix-wave from the mark is the brand's one shape. It appears three ways:

1. **Section divider** — a full-width SVG wave path, 1–2px stroke in `--tw-blue-500`, fading to transparent at both ends (Nocturne's rule for rules). Replaces horizontal rules entirely.
2. **Tide band** — the licensed blue field: a wave-masked block of `--tw-blue-600`→`--tw-blue-800` gradient anchoring the bottom of the homepage hero. Once per page, bottom-anchored, never mid-page.
3. **Mark** — the logo. Use the circular badge lockup only at ≥96px; the horizontal lockup everywhere else; `TW` monogram for favicon, app icon, and watermarks.

Never rotate, recolor, outline, or animate the mark. Wave dividers may animate on scroll-in (a 600ms stroke draw); the logo never moves.

Clear space around any lockup: the height of the `T` on all sides. Minimum horizontal lockup width: 140px.

---

## 6. Layout

Inherited from Nocturne: left-aligned and asymmetric. Content hugs the left, whitespace collects on the right.

- Max content width 1200px; text columns capped at 68ch.
- 12-column grid, 24px gutters. Hero content occupies columns 1–7.
- Spacing from Nocturne's 0.7× scale: `2.8 / 5.6 / 8.4 / 11.2 / 16.8 / 22.4px`. Section rhythm: 96px desktop, 56px mobile.
- Radii: `4px` plates and inputs, `8px` cards and buttons, `14px` modals and the hero panel. No pills, no fully-rounded cards.
- Every screen has one full-bleed moment and one only.

---

## 7. Components

**Buttons** — primary is a chrome-edge outline on transparent (never a blue fill). Hover: `--tw-blue-400` border + `--tw-glow`. Pressed: border `--tw-blue-600`, no glow. Secondary: 1px `--tw-ink-500` border, `--tw-chrome-300` label. Ghost: label only, blue on hover. Height 40px, 15px Inter 500 label, 8px radius.

**Product card (vial)** — chrome-edge, `--tw-ink-700` fill. Order top to bottom: vial photo through `.lighten` (shot on black so the background disappears), eyebrow category, compound name in `display-m` chrome text, a row of two chrome plates (`20 MG` · `99% PURITY`), then price in Inter 500 and a ghost "View COA" link. No star ratings. No badges other than dose, purity, and stock state.

**Chrome plate / purity callout** — see §4C. Dose and purity always appear as a pair, in that order, so they read as spec rather than marketing. Purity is always a number with `%`; never "ultra-pure" or "premium grade".

**COA badge** — chrome plate with a Phosphor `seal-check` icon in `--tw-verified`, label `COA · <LOT>` in eyebrow type. Always a link to the actual document. Never shown without a live COA behind it.

**Table** (COA library) — Nocturne `.table`, header row in eyebrow type / `--tw-chrome-400`, row rules `--tw-ink-500`, lot and batch columns in `mono`. Columns: Compound · Lot · Mass · Purity · Test date · Lab · PDF. Purity cell right-aligned in `mono`; the PDF cell is an icon button.

**Nav** — 64px bar, `--tw-ink-900` with a bottom hairline `--tw-ink-500`, horizontal lockup left, Inter 500 15px links, one primary button right. Sticky, gains `--tw-shadow-md` on scroll. No mega-menu.

**Footer** — `--tw-ink-800`, wave divider above it, `TW` monogram, and the research-use disclaimer in `body-s` / `--tw-chrome-500`.

**States** — Nocturne's rules stand: themed hover on everything interactive, `:focus-visible { outline: 2px solid var(--tw-blue-500); outline-offset: 2px; }`, disabled at 45% opacity. Never a browser default.

**Motion** — 180ms ease-out for state changes, 600ms for scroll reveals. Fades and 8px translations only. No parallax, no bouncing, no liquid effects.

---

## 8. Page patterns

**Homepage** — nav · hero (eyebrow, display-xl headline, one lead paragraph, primary + ghost buttons, tide band anchoring the bottom) · three-up value row, icon + one line each · featured compounds, 3–4 product cards · COA strip: one sentence on third-party testing plus a link to the library · footer. Nothing else. No testimonials, no newsletter interstitial, no stat wall of invented numbers.

**COA library** — nav · display-l title, one line of explanation · filter row (compound select, lot search) using Nocturne `.input` / `.seg` · the table · footer. Dense on purpose. This page is the trust argument, so it stays plain: no cards, no illustrations, no hero.

---

## 9. Do / Don't

**Do**
- Let the ink ground do the work; reach for chrome edges before chrome text.
- Show a real number wherever a claim would go.
- Photograph vials on black and mount them through `.lighten`.
- Keep one accent moment per viewport.
- Use Phosphor icons at 20px, `--tw-chrome-300`, 1.5px stroke.

**Don't**
- No pure black or pure white — every value from the ramps.
- No chrome, bevel, or glow below 34px.
- No large flat blue fields except the single tide band.
- No supplement-industry language: nothing about results, transformation, dosing for people, or before/after.
- No emoji, no gradient-mesh backgrounds, no stock lab photography with blue overlays.
- No second accent color. If something needs to stand out and blue is taken, use space.

---

## 10. Divergences from Nocturne (recorded on purpose)

1. **Accent hue.** Nocturne's blurple `#9184d9` is replaced by `--tw-blue-500 #0a6be1`, and its neutral ramp by the warmer-free chrome ramp. Roles, steps, and contrast intent are unchanged.
2. **Chrome as a material.** Nocturne has no metallic treatment. §4 adds one, bounded to three forms and a 34px floor, plus the tide-band exception to the "no saturated floods" rule — the equivalent of Nocturne's own section-divider and stat-band exceptions.

Everything else — spacing, radii, elevation, outlined primaries, focus rings, `.lighten`, Phosphor, the flush-left asymmetric direction — follows Nocturne unchanged.
