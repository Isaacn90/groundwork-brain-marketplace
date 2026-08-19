---
name: web-design
description: Design anything visual for the business and make it look professionally made. Use when the user asks for a website, landing page, or web page, a logo, a flyer, poster, or menu, a social media image, banner, or cover photo, a presentation or slides, or says make this look better, prettier, or more professional.
---

# Web & Visual Design

The owner asks for an outcome: "a flyer for the winter special", "a page for the
new service", "something for Instagram". Deliver the finished piece. Design
decisions are yours to make well, not theirs to configure.

## The design library

This skill's `data/` folder is a curated design library (derived from
ui-ux-pro-max, MIT licence, see `LICENSE` in this folder):

| File | What it holds | Search it by |
|---|---|---|
| `ui-reasoning.csv` | 162 decision rules: which style, colors, and type fit a kind of interface | kind of thing being built |
| `styles.csv` | 85 UI style recipes with keywords, Best For / Do Not Use For, implementation checklist | mood words: clean, warm, luxury, playful, trades |
| `colors.csv` | 162 complete palettes keyed by product type, every color with its on-color pair | business or product type |
| `typography.csv` | 74 font pairings with Google Fonts URL and CSS import | mood and Best For |
| `ux-guidelines.csv` | 100 UX rules with Do / Don't and severity | platform or issue |
| `app-interface.csv` | 31 app-screen UX rules | keywords |
| `landing.csv` | 35 landing-page patterns: section order, CTA placement, conversion notes | pattern keywords |

Rows are long. Never read a whole file. Grep for keywords first, then read only
the matching rows, e.g. `grep -i "cafe\|coffee\|hospitality" data/colors.csv`.

## Workflow

1. Understand the job in business terms: what it is for, who sees it, where it
   lives (web, print, a specific platform). One round of questions at most, and
   only if the answer would change the design.
2. Pick from the library, in order: a decision row from `ui-reasoning.csv`, a
   style from `styles.csv`, a palette from `colors.csv`, a pairing from
   `typography.csv`. If the business already has brand colors, fonts, or a
   logo (in its brain or in the conversation), those win; the library fills
   gaps, it never overrides a real brand.
3. Build the piece as a self-contained HTML/CSS file unless the surrounding
   project already uses something else. Real words, never lorem ipsum: pull
   facts, prices, and phrasing from the business's brain when one is present,
   and ask rather than invent anything the business would be held to.
4. Check the result against the relevant `ux-guidelines.csv` rows and, for
   social or banner work, the exact sizes below.
5. Show the finished piece. Offer at most two alternatives. Iterate on
   feedback rather than asking for a brief up front.

Logo requests: build clean typographic or geometric lockups as SVG, three
options, each on a white background. No image-generation service is assumed to
exist on this machine.

## Sizes that must be exact (px)

| Platform | Type | Size |
|---|---|---|
| Facebook | Cover | 820 x 312 |
| Facebook | Post | 1200 x 630 |
| Instagram | Post | 1080 x 1080 |
| Instagram | Story | 1080 x 1920 |
| Twitter/X | Header | 1500 x 500 |
| LinkedIn | Post | 1200 x 627 |
| YouTube | Thumbnail | 1280 x 720 |
| Website | Hero | 1920 x 600-1080 |

## Design rules

- Critical content in the central 70-80% of a banner; edges get cropped.
- One call to action per piece, minimum 44px tall.
- Two fonts maximum. Body at least 16px, headlines at least 32px.
- Ads: keep text under 20% of the image area.
- Print: 300 DPI, CMYK, 3-5mm bleed, fonts embedded not linked.

## Rules

- Talk outcomes, never machinery: no CSS, file formats, or design jargon in
  what the owner reads, unless they ask how it works.
- Never invent claims, prices, or offers. They come from the brain, the
  conversation, or a question.
- A piece is not done until it has been looked at (screenshot or preview),
  not just written.
