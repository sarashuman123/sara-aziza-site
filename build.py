"""Static site generator. Renders templates/ + content.py + artworks.json into dist/.

Usage: python3 build.py            (run process_images.py first to create dist/img/)

The finished site is dist/. Upload that folder to any static host as-is.
"""
import json
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

import content

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
# Files copied verbatim into dist/static/ (templates reference them as /static/...).
STATIC_FILES = ["style.css", "site.js", "signature.png", "signature-light.png"]
STATIC_DIRS = ["fonts"]


def load_artworks():
    works = json.load(open(ROOT / "artworks.json"))
    by_id = {w["id"]: w for w in works}
    for w in works:
        for opt in ("note", "subtitle", "feature", "overlap", "cover"):
            w.setdefault(opt, None)
        w["slug"] = w["id"].lower()
        w["url"] = f"/work/{w['slug']}/"
        w["img"] = f"/img/{w['id']}.jpg"
        w["img_s"] = f"/img/{w['id']}-s.jpg"
        w["number"] = w["id"].replace("SA-", "SA—")
        w["collection_obj"] = next(c for c in content.COLLECTIONS if c["number"] == w["collection"])
    return works, by_id


def main():
    works, by_id = load_artworks()
    collections = []
    for c in content.COLLECTIONS:
        c = dict(c)
        c.setdefault("fig", None)
        c["url"] = f"/archive/{c['slug']}/"
        c["works"] = [w for w in works if w["collection"] == c["number"]]
        c["feature"] = next((w for w in c["works"] if w.get("feature")), c["works"][0])
        c["overlap"] = next((w for w in c["works"] if w.get("overlap")), None)
        c["others"] = [w for w in c["works"] if w is not c["feature"]]
        c["num"] = f"{c['number']:02d}"
        collections.append(c)
    cols_by_num = {c["number"]: c for c in collections}
    for w in works:
        w["collection_obj"] = cols_by_num[w["collection"]]
    notes = []
    for n in content.NOTES:
        n = dict(n)
        for opt in ("image", "postscript", "margin", "featured", "size"):
            n.setdefault(opt, None)
        n["url"] = f"/notes/{n['slug']}/"
        n["num"] = f"{n['number']:03d}"
        n["image_obj"] = by_id[n["image"]] if n.get("image") else None
        n["gallery_objs"] = [by_id[g] for g in n.get("gallery", [])]
        notes.append(n)
    cover = next(w for w in works if w.get("cover"))
    obsessions = [by_id[i] for i in ("SA-009", "SA-026", "SA-013", "SA-021")]

    env = Environment(loader=FileSystemLoader(ROOT / "templates"), undefined=StrictUndefined,
                      autoescape=True, trim_blocks=True, lstrip_blocks=True)
    base_ctx = dict(site=content.SITE, collections=collections, works=works, notes=notes,
                    intro=content.INTRO, eye=content.EYE, interview=content.INTERVIEW,
                    letter=content.LETTER, note_kinds=content.NOTE_KINDS, enq=content.ENQUIRIES,
                    cover=cover, obsessions=obsessions)

    def render(template, path, **ctx):
        out = DIST / path.lstrip("/")
        out.mkdir(parents=True, exist_ok=True)
        html = env.get_template(template).render(**base_ctx, page_path=path, **ctx)
        (out / "index.html").write_text(html)

    if not (DIST / "img").exists():
        raise SystemExit("dist/img/ is missing: run `python3 process_images.py` first")
    # Fresh dist, but keep processed images.
    for p in DIST.iterdir():
        if p.name != "img":
            shutil.rmtree(p) if p.is_dir() else p.unlink()
    static = DIST / "static"
    static.mkdir()
    for name in STATIC_FILES:
        shutil.copy2(ROOT / name, static / name)
    for name in STATIC_DIRS:
        shutil.copytree(ROOT / name, static / name)

    render("cover.html", "/", title=None)
    render("archive.html", "/archive/", title="The Archive")
    for c in collections:
        render("collection.html", c["url"], title=c["title"].title(), collection=c)
    for i, w in enumerate(works):
        render("artwork.html", w["url"], title=w["title"], work=w,
               prev=works[i - 1], next=works[(i + 1) % len(works)])
    render("artist.html", "/artist/", title="The Artist")
    render("notes.html", "/notes/", title="Studio Notes",
           featured=next(n for n in notes if n.get("featured")),
           entries=[n for n in notes if not n.get("featured")])
    for n in notes:
        render("note.html", n["url"], title=n["title"].rstrip(".").title(), note=n)
    render("enquiries.html", "/enquiries/", title="Enquiries")
    render("unfinished.html", "/unfinished/", title="Unfinished Business")
    html404 = env.get_template("404.html").render(**base_ctx, page_path="/404", title="Lost")
    (DIST / "404.html").write_text(html404)
    pages = sum(1 for _ in DIST.rglob("index.html"))
    print(f"built {pages} pages into {DIST}")


if __name__ == "__main__":
    main()
