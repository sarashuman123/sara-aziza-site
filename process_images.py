"""Prepare artwork images: apply Sara's signature to a corner of every painting,
then export web-sized JPEGs (large + small) into dist/img/.

Usage: python3 process_images.py
"""
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

ROOT = Path(__file__).parent
SRC = ROOT / "source-images"
OUT = ROOT / "dist" / "img"
SIG_DARK = Image.open(ROOT / "signature.png").convert("RGBA")
SIG_LIGHT = Image.open(ROOT / "signature-light.png").convert("RGBA")
BOXES = json.load(open(ROOT / "canvas_boxes.json"))  # where the canvas sits in each wall photo
ARTWORKS = json.load(open(ROOT / "artworks.json"))

LARGE_W = 1800
SMALL_W = 900


def source_path(n):
    for ext in ("png", "jpeg", "jpg"):
        p = SRC / f"image{n}.{ext}"
        if p.exists():
            return p
    raise FileNotFoundError(n)


def artwork_box(n, w, h):
    """Fractional box of the actual artwork inside the photo."""
    x0, y0, x1, y1 = BOXES[str(n)]
    area = (x1 - x0) * (y1 - y0)
    if area < 0.6:
        # Drawing on paper or full-bleed canvas: the whole image is the work.
        return 0, 0, w, h
    # Hung canvas: trim a little for drop shadows.
    pad_x, pad_y = (x1 - x0) * 0.025, (y1 - y0) * 0.025
    return int((x0 + pad_x) * w), int((y0 + pad_y) * h), int((x1 - pad_x) * w), int((y1 - pad_y) * h)


def corner_stats(img, box, corner, sig_w, sig_h, inset):
    x0, y0, x1, y1 = box
    if corner == "br":
        cx, cy = x1 - inset - sig_w, y1 - inset - sig_h
    else:
        cx, cy = x0 + inset, y1 - inset - sig_h
    patch = np.array(img.crop((cx, cy, cx + sig_w, cy + sig_h)).convert("L")).astype(float)
    return (cx, cy), patch.mean(), patch.std()


def sign(img, n, art):
    w, h = img.size
    box = artwork_box(n, w, h)
    bw, bh = box[2] - box[0], box[3] - box[1]
    # The signature is a wide mark (rotated 90° clockwise from Sara's original
    # scan), so size it by width: about a sixth of the shorter canvas side.
    sig_w = int(min(bw, bh) * 0.17)
    sig_h = int(SIG_DARK.height * sig_w / SIG_DARK.width)
    inset = int(min(bw, bh) * 0.035)

    if art.get("sig_pos"):
        # Explicit fractional centre for awkward shapes (e.g. a round record).
        fx, fy = art["sig_pos"]
        cx, cy = int(fx * w - sig_w / 2), int(fy * h - sig_h / 2)
        patch = np.array(img.crop((cx, cy, cx + sig_w, cy + sig_h)).convert("L"))
        mean, corner = patch.mean(), "custom"
    else:
        forced = art.get("sig_corner")
        candidates = [forced] if forced else ["br", "bl"]
        best = None
        for c in candidates:
            pos, mean, std = corner_stats(img, box, c, sig_w, sig_h, inset)
            if best is None or std < best[2]:
                best = (pos, mean, std, c)
        (cx, cy), mean, _, corner = best
    ink = art.get("sig_ink") or ("dark" if mean > 110 else "light")
    sig = (SIG_DARK if ink == "dark" else SIG_LIGHT).resize((sig_w, sig_h), Image.LANCZOS)
    # Soften very slightly so it sits in the paint rather than on top of it.
    alpha = sig.getchannel("A").filter(ImageFilter.GaussianBlur(0.4))
    alpha = alpha.point(lambda a: int(a * 0.82))
    sig.putalpha(alpha)
    img = img.convert("RGBA")
    img.alpha_composite(sig, (cx, cy))
    return img.convert("RGB"), corner, ink


def export(img, stem):
    for suffix, width in (("", LARGE_W), ("-s", SMALL_W)):
        im = img.copy()
        if im.width > width:
            im = im.resize((width, int(im.height * width / im.width)), Image.LANCZOS)
        im.save(OUT / f"{stem}{suffix}.jpg", quality=84, optimize=True, progressive=True)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for art in ARTWORKS:
        n = art["source"]
        img = Image.open(source_path(n)).convert("RGB")
        signed, corner, ink = sign(img, n, art)
        export(signed, art["id"])
        print(art["id"], art["title"], corner, ink)
    # Non-artwork images: the artist's photo, unsigned.
    export(Image.open(source_path(30)).convert("RGB"), "portrait")
    print(f"wrote {len(ARTWORKS) * 2 + 2} images to {OUT}")


if __name__ == "__main__":
    main()
