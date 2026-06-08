# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static HTML/CSS/JS website for **Tim MacDonough Painting Company** — a luxury residential and commercial painting contractor based in Metro Detroit, Michigan. There is no build system, framework, or package manager. Open any `.html` file directly in a browser to preview.

## File Structure

- `index.html` — Homepage (hero, services, gallery, process, reviews, contact form)
- `residential.html`, `commercial.html`, `exterior.html`, `interior.html` — Service-specific landing pages
- `service-areas.html` — Geographic coverage page
- `contact.html` — Standalone contact/estimate page
- `style.css` — All styles (single file, no preprocessor)
- `script.js` — All JavaScript (single file): mobile nav, smooth scroll, animated counters, scroll-fade, contact form
- `brand-guidelines.md` — Canonical brand reference — **read this before making any visual changes**

## Brand Rules (Non-Negotiable)

### Colors (CSS custom properties in `style.css :root`)
| Variable | Hex | Usage |
|---|---|---|
| `--navy` | `#0E1D3A` | Dark backgrounds, headings |
| `--gold` | `#F2B322` | Accent only — CTAs, labels, icons |
| `--cream` | `#F7F3E9` | Page/section backgrounds (preferred over white) |
| `--charcoal` | `#2B2B2B` | Body text |
| `--taupe` | `#A79B8B` | Muted/secondary text |
| `--stone` | `#6E7277` | Captions, placeholders |

Gold is an **accent only** — never a large background fill. Warm Cream is preferred over pure white for section backgrounds.

### Typography
- **Cormorant Garamond** (`var(--font-display)`) — headlines and display text only. Never body copy.
- **Montserrat** (`var(--font-body)`) — all body, nav, buttons, labels.
- Section labels (e.g. "OUR SERVICES"): Montserrat, uppercase, `letter-spacing: 0.22em+`, gold color.
- `h2` inside `.section-header` uses `font-display` with `<em>` for the italic, lighter second line.

### Layout
- Max content width: `1200px` (`--max-width`)
- Section padding: `96px 0` desktop (`.section` class)
- Card border-radius: `4px`–`8px` (`--radius-sm`, `--radius-md`) — no large rounded corners
- Standard shadow: `0 2px 12px rgba(14,29,58,0.08)`

## Multi-Page Architecture

All pages share the same header and footer HTML — **duplicated manually, not templated**. When updating nav links, the logo, phone number, footer content, or anything in the shared chrome, you must edit every `.html` file. The logo `href` differs by context: `#top` on `index.html`, `index.html` on inner pages.

Each inner page (`residential.html`, `commercial.html`, `exterior.html`, `interior.html`, `service-areas.html`, `contact.html`) loads the same `style.css` and `script.js`. There is no page-specific CSS or JS.

## JavaScript Patterns

`script.js` uses vanilla JS with no dependencies. Key patterns:
- **IntersectionObserver** for scroll-triggered counter animation (`.stat-num[data-target]`) and card fade-in (`.service-card`, `.review-card`, etc.)
- Contact form (`#contactForm`) currently uses a `setTimeout` mock — the comment says to replace with a real endpoint (Netlify/Formspree)
- Smooth scroll offsets by `80px` to account for the sticky header height
- Mobile nav: `#navToggle` toggles `.open` on `#mobileNav` with ARIA attribute updates

## Copy & Tone

Refer to `brand-guidelines.md` for approved vocabulary. Key rules:
- Lead with outcome, not process
- Avoid: cheap, affordable, budget, deal, fast, best (without proof)
- Use: craftsmanship, distinguished, elevated, refined, flawless, white-glove
- CTAs are invitations: "Request Your Complimentary Estimate" not "Click Here"
- Be specific and local — name neighborhoods (Oakland Township, Lake Orion, Rochester Hills, Shelby Township, Metamora, Oxford, Auburn Hills, Clarkston, Troy, Bloomfield Hills, Birmingham)

## Business Details

- **Phone:** (248) 978-2946 (`tel:+12489782946`)
- **Email:** timmacdonoughpainting@gmail.com
- **Domain:** timmacdonoughpainting.com
- **Based:** Oakland Township, MI
- **Hours:** Mon–Fri 7am–6pm, Sat 8am–3pm
- **Founded:** 2006 | **30+ years experience** | **500+ projects** | **Zero subcontractors**
