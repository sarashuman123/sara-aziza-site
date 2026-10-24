# Sara Aziza — website

A static website for the artist Sara Aziza, laid out like an independent art
magazine. Five main pages, each an editorial spread: The Cover, The Archive
(with five collection pages and one page per artwork), The Artist, Studio
Notes (with one page per note), Enquiries. Plus Unfinished Business (linked
from the footer) and a 404 page. 49 pages in total, all generated from the
files in this folder.

There is no framework, no Node, no database. Two small Python scripts turn
the source images, the copy and the templates into a folder of plain HTML,
CSS, JPEGs and fonts (`dist/`). That folder is the website. Upload it to any
static host and you are live.

## Quick start (run it on your own computer)

You need Python 3.10 or newer. Unzip, then from this folder:

```
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python3 process_images.py          # signs every painting, writes dist/img/  (about a minute)
python3 build.py                   # renders the pages, writes dist/

cd dist
python3 -m http.server 8000
```

Open http://localhost:8000 in a browser. Stop the server with Ctrl-C.

Whenever you change anything, re-run `python3 build.py` and refresh the
browser. You only need to re-run `process_images.py` if you change the
source images, the signature, or the signature settings in `artworks.json`.

If `python3` is not found, try `python`. If `pip install` fails on Pillow or
numpy, upgrade pip first (`pip install --upgrade pip`).

If you want version control, run `git init && git add -A && git commit -m "Initial site"`
in this folder. The zip ships without a `.git` directory to keep it small.

## What each file is

Everything lives at the top level except the HTML templates and the
original photos.

| File | What it is |
|---|---|
| `build.py` | Renders `templates/` with the data below into `dist/`. |
| `process_images.py` | Finds the canvas in each photo, composites Sara's signature into a corner, exports large (1800px) and small (900px) JPEGs to `dist/img/`. |
| `content.py` | **All the words on the site.** Nav labels, collection titles and straps, the interview, the letter, studio notes, enquiry copy, contact email, form endpoint. |
| `artworks.json` | **The catalogue.** One entry per artwork: id, which source image, which collection, title, medium, size, year, handwritten note, and optional signature overrides. |
| `canvas_boxes.json` | For each source image, the fractional box where the actual painting sits inside the wall photo. Used only to place the signature. |
| `templates/*.html` | Jinja2 templates, one per page type. `base.html` is the shell, `_macros.html` holds shared snippets. |
| `style.css` | All styling. Copied into `dist/static/`. |
| `site.js` | A little JavaScript: fade-in on scroll, gentle parallax, mobile menu, lightbox, enquiry form. Copied into `dist/static/`. |
| `signature.png`, `signature-light.png` | Sara's signature on a transparent background, espresso and cream versions. Also used as the favicon. |
| `fonts/` | Self-hosted web fonts (Cormorant Garamond, Jost, Cedarville Cursive; all SIL Open Font License). No external font requests. |
| `source-images/` | The 31 images from the brief as high-quality JPEGs: 29 artworks (`image1` to `image29`), Sara's photo (`image30`) and the original signature scan (`image31`, PNG). |
| `brief.txt` | The original written brief the site was built from. Reference only. |
| `requirements.txt` | The three Python packages needed: Jinja2, Pillow, numpy. |
| `deploy.sh`, `url-rewrite.js` | Optional helpers for hosting on AWS S3 + CloudFront. See below. |
| `dist/` | **Generated output. Never edit by hand.** Not committed to git. |

## Common edits

- **Change any text**: edit `content.py`, run `python3 build.py`.
- **Rename an artwork, fix a medium or year**: edit `artworks.json`, run `python3 build.py`.
- **Swap in a real email address**: `SITE["contact_email"]` in `content.py`.
- **Make the enquiry form actually send**: set `SITE["form_action"]` in `content.py` to a form endpoint (Formspree, Netlify Forms, Basin, etc.). With it empty, the form opens a pre-filled email instead.
- **Move the signature on one painting**: in `artworks.json` set `sig_corner` (`"br"` or `"bl"`), `sig_ink` (`"dark"` or `"light"`), or `sig_pos` (`[x, y]` fractional centre). Then run both scripts.
- **Add an artwork**: drop the photo into `source-images/` as `imageN.jpg` (or `.png`), add its canvas box to `canvas_boxes.json`, add an entry to `artworks.json`. Run both scripts.
- **Change colours, type, spacing**: `style.css`.

The signature in `signature.png` is already rotated the way Sara wants it.
Do not rotate it again.

## Hosting for real

`dist/` is a plain static site with clean URLs (`/archive/`, `/work/sa-001/`).
Every page is a folder containing an `index.html`, which is the convention
all static hosts understand. Pick whichever is easiest:

**Netlify, Vercel, Cloudflare Pages, GitHub Pages (simplest).** Build
locally, then drag-and-drop the `dist/` folder onto the host's upload page,
or point the host at this repo with build command
`python3 process_images.py && python3 build.py` and publish directory `dist`.
Each of these serves `folder/index.html` for `/folder/` automatically and
will use `404.html` for missing pages.

**AWS S3 + CloudFront.** Create a private S3 bucket, a CloudFront
distribution in front of it, and attach `url-rewrite.js` as a CloudFront
Function on *viewer request* (it maps `/archive/` to `/archive/index.html`).
Set the distribution's custom error response for 404 to `/404.html`. Then:

```
BUCKET=your-bucket-name DIST_ID=your-distribution-id ./deploy.sh
```

The script rebuilds, syncs `dist/` with sensible cache headers (images and
fonts cached for a year, HTML/CSS/JS for five minutes) and invalidates the
CloudFront cache.

**Any other web server (nginx, Apache, shared hosting).** Copy the contents
of `dist/` to the web root. Default directory-index behaviour gives you the
clean URLs. Point the 404 page at `/404.html`.

## Before publishing

- The interview answers, letters and all handwritten annotations are the
  brief's *proposed* copy. Go through them with Sara first.
- Titles, media, dimensions and years in `artworks.json` are placeholders
  written to fit the images. Replace with the real catalogue details.
- Set the real contact email and a form endpoint in `content.py`.
- Set `SITE["year"]` in `content.py` if the footer year needs changing.
