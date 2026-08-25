# Handoff for Claude Code

Two documents govern the TideWave build. Read both before writing code.

| File | What it is | Authority |
|---|---|---|
| `design.md` | TideWave brand system — palette, type, chrome rules, components, page patterns | **Wins on any conflict** |
| `nocturne/nocturne-readme.md` | The base design system TideWave is built on — structure, direction, class list, interaction rules | Governs anything `design.md` doesn't name |
| `nocturne/styles.css` | The base token sheet + component layer. `:root` variables, 100–900 OKLCH ramps, `.btn` `.card` `.table` `.input` `.nav` `.dialog` `.lighten` | Link from every page |
| `nocturne/_ds_bundle.js` | React component build of the same components, for JSX projects | Optional |

## How to use them together

1. Link `styles.css` from every page. Take spacing, radii, shadows, and component classes from it — don't hand-roll parallel CSS.
2. Override the color and font tokens at the top of your own stylesheet with the TideWave values from `design.md` §2 and §3. Nocturne's blurple accent and Inter-only pairing are replaced; everything else stays.
3. Build with Nocturne's classes (`.btn-primary`, `.card`, `.table`, `.lighten`), then apply the TideWave chrome treatments from `design.md` §4 as additive utilities (`.tw-chrome-edge`, `.tw-chrome-text`, the chrome plate).
4. Fonts: Saira Condensed (700 / 500) and Inter (400 / 500) from Google Fonts.
5. Icons: Phosphor.

## Hard constraints

- No pure black, no pure white.
- No chrome, bevel, or glow under 34px.
- Primary buttons are outlined, never filled.
- One accent moment per viewport; one full-bleed moment per page.
- No second accent color. Green is COA status only.
