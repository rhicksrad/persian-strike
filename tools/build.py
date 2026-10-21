#!/usr/bin/env python3
"""Generate the persianstrike.com pages. Run: build.py <site-dir>"""
import json, sys, html
from pathlib import Path

SITE = Path(sys.argv[1])
BUY = "https://reformatgames.itch.io/persian-strike-retribution"
RAW = "https://raw.githubusercontent.com/rhicksrad/persian-strike/main/media/"
ORIGIN = "https://persianstrike.com/"
FONTS = ("https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700"
         "&family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@400;500;600&display=swap")
DISCLAIMER = ("PERSIAN STRIKE: RETRIBUTION is a work of fiction set in an alternate-history 1990s. "
              "All names, places, factions, and events are fictional; any resemblance to real states "
              "or persons is coincidental.")

# Every image the pages use. Swapping a capture means editing one line here.
IMG = json.loads((Path(__file__).parent / "images.json").read_text())

NAV = [("index.html", "Home"), ("c1.html", "Tondbad"), ("c2.html", "Tangeh"),
       ("c3.html", "Shahin"), ("c4.html", "Azadi"), ("about.html", "About")]


def img(key, cls="", lazy=True):
    src, alt = IMG[key]
    c = f' class="{cls}"' if cls else ""
    l = ' loading="lazy"' if lazy else ' fetchpriority="high"'
    return f'<img{c} src="media/{src}" alt="{html.escape(alt)}"{l}>'


def page(fname, title, desc, og_key, body, ld=None):
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{h}"{cur if h == fname else ""}>{t}</a>' for h, t in NAV)
    ogimg = ORIGIN + "media/" + IMG[og_key][0]
    url = ORIGIN if fname == "index.html" else ORIGIN + fname
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in (ld or []))
    out = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#0b0a08">
<meta property="og:type" content="website">
<meta property="og:site_name" content="PERSIAN STRIKE: RETRIBUTION">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{ogimg}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{ogimg}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><rect width=%22100%22 height=%2233%22 fill=%22%23b8261e%22/><rect y=%2233%22 width=%22100%22 height=%2234%22 fill=%22%23050505%22/><rect y=%2267%22 width=%22100%22 height=%2233%22 fill=%22%23efe9dd%22/></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
{lds}</head>
<body>
<header class="nav"><div class="wrap">
  <a class="brand" href="index.html">Persian Strike <span>Retribution</span></a>
  <nav class="links">{nav}<a class="buy" href="{BUY}" target="_blank" rel="noopener">Buy · Early access</a></nav>
</div></header>
{body}
<footer><div class="wrap">
  <div><div class="studio">Reformat Games</div><div class="fnav">{nav}</div></div>
  <div><p>© 2026 Reformat Games LLC. {DISCLAIMER}</p>
  <p>In early access for Windows and Linux PC on <a href="{BUY}" target="_blank" rel="noopener">itch.io</a>. Built with the Godot Engine. Every image and film on this site is captured in-engine.</p></div>
</div></footer>
</body>
</html>
"""
    (SITE / fname).write_text(out)


def film(src, poster_key, t, m, d):
    return f"""<figure class="film">
  <video controls preload="none" poster="media/{IMG[poster_key][0]}"><source src="{RAW}{src}" type="video/mp4"></video>
  <figcaption><span class="t">{t}</span><span class="m">{m}</span><span class="d">{d}</span></figcaption>
</figure>"""


def video_ld(name, desc, src, poster_key):
    return {"@context": "https://schema.org", "@type": "VideoObject", "name": name, "description": desc,
            "thumbnailUrl": ORIGIN + "media/" + IMG[poster_key][0], "uploadDate": "2026-10-21",
            "contentUrl": RAW + src}


def cards(items, cls="g3", orders=False):
    oc = " orders" if orders else ""
    out = [f'<div class="grid {cls}{oc}">']
    for key, k, h, p in items:
        out.append(f'<article class="card">{img(key)}<span class="k">{k}</span><h3>{h}</h3><p>{p}</p></article>')
    out.append("</div>")
    return "\n".join(out)


def split(key, label, h, paras, flip=False):
    ps = "".join(f"<p>{p}</p>" for p in paras)
    return f'<div class="split{" flip" if flip else ""}">{img(key)}<div><span class="label">{label}</span><h3>{h}</h3>{ps}</div></div>'


def gallery(items):
    out = ['<div class="gallery">']
    for key, cap, size in items:
        cls = f' class="{size}"' if size else ""
        out.append(f'<figure{cls}><a href="media/{IMG[key][0]}" target="_blank" rel="noopener">{img(key)}</a><figcaption>{cap}</figcaption></figure>')
    out.append("</div>")
    return "\n".join(out)


def block(inner, cls="", sid=""):
    i = f' id="{sid}"' if sid else ""
    return f'<section class="block {cls}"{i}><div class="wrap">\n{inner}\n</div></section>'


def head(label, h2, lede=""):
    l = f'<p class="lede">{lede}</p>' if lede else "<div></div>"
    return f'<div class="head"><div><span class="label">{label}</span><h2>{h2}</h2></div>{l}</div>'


def campaign_head(num, name, lede, hero_key, dossier):
    dd = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in dossier)
    return f"""<section class="page-head"><div class="wrap">
  <div class="num">{num}</div><h1>{name}</h1><p class="lede">{lede}</p>
</div></section>
<div class="hero-frame">{img(hero_key, lazy=False)}</div>
<div class="rule"></div>
<dl class="dossier">{dd}</dl>"""


def pager(prev, nxt):
    p = f'<a class="prev" href="{prev[0]}"><span class="k">← Previous</span><span class="t">{prev[1]}</span></a>' if prev else "<span></span>"
    n = f'<a class="next" href="{nxt[0]}"><span class="k">Next →</span><span class="t">{nxt[1]}</span></a>' if nxt else "<span></span>"
    return f'<nav class="pager">{p}{n}</nav>'


def closer(h, lede):
    return f"""<section class="closer"><div class="wrap">
  <h2>{h}</h2><p class="lede">{lede}</p>
  <div class="cta"><a class="btn primary" href="{BUY}" target="_blank" rel="noopener">Buy on itch.io</a><a class="btn" href="{BUY}" target="_blank" rel="noopener">Play the free demo</a></div>
</div></section>"""


exec((Path(__file__).parent / "pages.py").read_text())
