# Tanya C — portfolio package

Two deliverables, one visual identity (press-proof: paper stock, ink, CMYK control strip).

| File | What it is |
|---|---|
| `index.html` | Single-file portfolio website. No build step — double-click to open, or drop on Netlify / GitHub Pages / Vercel as-is. |
| `Tanya_C_Portfolio_Deck.pdf` | 12-slide 16:9 portfolio deck for emailing or presenting. |

## Before this goes out — 3 things to replace

**1. Contact details.** Both files carry placeholders:
`hello@example.com`, `+1 (000) 000-0000`, `tanya-c.example.com`, and an empty LinkedIn link.
In `index.html` they're in the section marked `<!-- ══ CONTACT ══ -->`.

**2. Artwork.** Every image slot is empty — the site has 6, the deck has 6.
In `index.html`, find a block like this and replace the inner `<div class="ph">…</div>`:

```html
<div class="proof">
  <img src="images/01-pitch-book.jpg" alt="Executive deck for a product launch">
</div>
```

Put the files in an `images/` folder next to `index.html`. Slot ratios are labelled
on-screen (16:9, 4:5, 1:1) — crop to those and nothing shifts.

**3. Résumé download.** The site links to `Tanya_C_Resume.pdf` — drop that file
next to `index.html`.

## Notes

- Six work categories were derived from the résumé: presentations & pitch books,
  infographics & data viz, brochures & editorial, brand systems & collateral, icons &
  illustration, event & signage. Rename any of them to match the real pieces.
- Case-study copy beats category copy. If real project detail can be shared
  (constraint → approach → outcome), swap the descriptions for that.
- Fonts load from Google Fonts (Big Shoulders Display, Instrument Sans, IBM Plex Mono),
  with system fallbacks if offline.
- The deck source is `deck.html` + `build.py` if slides need editing; regenerate with
  `wkhtmltopdf --page-width 338.667mm --page-height 190.5mm`.
