"""Générateur de pages « site » pour les régions (hors Côte d'Azur), sur le modèle d'une page existante de la région."""
import re, json, os, sys, html
from PIL import Image, ImageOps
sys.path.insert(0, '/tmp/g')
from rando_gen import fr_typo

ROOT = {'fr': '/home/claude/clicandsite-guide', 'en': '/home/claude/clicandsite-guide-en'}
BASE = {'fr': 'https://clicandsite.fr', 'en': 'https://clicandsite.com'}
GHOST = {'fr': 'https://www.getyourguide.fr/', 'en': 'https://www.getyourguide.com/'}
VPRE = {'fr': 'fr-FR/', 'en': ''}
PID = 'pid=P00331213&amp;mcid=42383&amp;medium=link&amp;campaign='
L = {'fr': dict(credit='Photo : ', pd='domaine public', faq='Questions fréquentes', fiche='En bref', home='Accueil', near_h='À voir à proximité',
                hist='Un peu d’histoire', bk='Billets', bkv='Autres billets', cta_k='À réserver', cta_v='ou autres billets', date='15 novembre 2026',
                lead='Réservation en ligne en quelques minutes, annulation gratuite sur la plupart des activités et avis de voyageurs pour bien choisir.'),
     'en': dict(credit='Photo: ', pd='public domain', faq='Frequently asked questions', fiche='At a glance', home='Home', near_h='Nearby',
                hist='A bit of history', bk='Tickets', bkv='More tickets', cta_k='Book ahead', cta_v='or more tickets', date='15 November 2026',
                lead='Book online in minutes, with free cancellation on most activities and traveller reviews to help you choose.')}

def esc(t): return html.escape(t, quote=False)
def ea(t): return html.escape(t, quote=True)

def links(p, lang):
    rel = f"{p['reg'][lang]}/{p['slug']}"
    camp = f"clicandsite-{lang}-{rel.replace('/', '-')}"
    g = f"{GHOST[lang]}{p['gyg']}/?partner_id=XMYSXGR&amp;cmp={camp}&amp;utm_medium=online_publisher" if p.get('gyg') else None
    v = f"https://www.viator.com/{VPRE[lang]}{p['via']}?{PID}{camp}"
    return g, v

def page(p, lang):
    o = 'en' if lang == 'fr' else 'fr'
    T = fr_typo if lang == 'fr' else (lambda x: x)
    h = lambda t: esc(T(t))
    d = p[lang]; Lg = L[lang]
    root = ROOT[lang]; reg = p['reg'][lang]
    tpl_rel = f"{reg}/{p['tpl']}"
    tpl = open(f'{root}/{tpl_rel}/index.html', encoding='utf-8').read()
    url = f"{BASE[lang]}/{reg}/{p['slug']}/"; ourl = f"{BASE[o]}/{p['reg'][o]}/{p['slug']}/"
    turl = f"{BASE[lang]}/{tpl_rel}/"; tourl = f"{BASE[o]}/{p['reg'][o]}/{p['tpl']}/"
    head = tpl[:tpl.index('</head>')]
    head = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', '', head, flags=re.S)
    head = re.sub(r'<title>.*?</title>', f'<title>{h(d["title"])} | Clic&amp;Site</title>', head)
    head = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m[1] + ea(T(d['desc'])), head)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m[1] + ea(T(d['title'])) + ' | Clic&amp;Site', head)
    head = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m[1] + ea(T(d['desc'])), head)
    head = head.replace(turl, url).replace(tourl, ourl).replace(f"og/{p['tpl']}.jpg", f"og/{p['slug']}.jpg")
    ld = [{"@context": "https://schema.org", "@type": "TouristAttraction", "name": T(d['name']), "description": T(d['desc']), "url": url,
           "image": [f"{BASE[lang]}/assets/photos/{p['slug']}.jpg", f"{BASE[lang]}/assets/og/{p['slug']}.jpg"],
           "geo": {"@type": "GeoCoordinates", "latitude": p['geo'][0], "longitude": p['geo'][1]},
           "address": {"@type": "PostalAddress", "addressLocality": p['loc'], "addressRegion": p['aregion'], "addressCountry": "FR"},
           "containedInPlace": {"@type": "Place", "name": p['rname'][lang]}},
          {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": T(q), "acceptedAnswer": {"@type": "Answer", "text": T(a)}} for q, a in d['faq']]},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": Lg['home'], "item": f"{BASE[lang]}/"},
              {"@type": "ListItem", "position": 2, "name": p['rname'][lang], "item": f"{BASE[lang]}/{reg}/"},
              {"@type": "ListItem", "position": 3, "name": T(d['crumb']), "item": url}]}]
    head += ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld)
    body = tpl[tpl.index('</head>'):tpl.index('<header class="post')].replace(turl, url).replace(tourl, ourl)
    P = '../../assets/photos/' + p['slug']
    a, u, li, lu = p['credit']
    cred = (f'{Lg["credit"]}<a href="{u}" rel="noopener" target="_blank">{esc(a)}</a>, {Lg["pd"]}, Wikimedia Commons' if li == 'PD' else
            f'{Lg["credit"]}<a href="{u}" rel="noopener" target="_blank">{esc(a)}</a>, <a href="{lu}" rel="noopener license" target="_blank">{li}</a>, Wikimedia Commons')
    ref = open(f"{root}/{'normandie' if lang == 'fr' else 'normandy'}/etretat/index.html", encoding='utf-8').read()
    def grab(rx):
        m = re.search(rx, tpl, re.S) or re.search(rx, ref, re.S)
        return m
    cta_btn = grab(r'<p class="post__cta">.*?</p>').group(0)
    hero = (f'<header class="post post--{p["post"]}">\n  <picture><source type="image/webp" srcset="{P}-960.webp 960w, {P}-1280.webp 1280w, {P}.webp 1920w" sizes="100vw">'
            f'<img class="post__img" src="{P}.jpg" srcset="{P}-960.jpg 960w, {P}-1280.jpg 1280w, {P}.jpg 1920w" sizes="100vw" alt="{ea(T(d["alt"]))}" fetchpriority="high"></picture><div class="post__shade" aria-hidden="true"></div>\n'
            f'  <div class="wrap post__in">\n    <div class="stamp" aria-hidden="true"><span class="stamp__num">{p["num"]}</span></div><div class="postmark" aria-hidden="true"><span>{esc(p["pm"])}</span></div>\n'
            f'    <h1 class="post__title">{h(d["h1"])}</h1>\n    <p class="post__lead">{h(d["lead"])}</p>\n    {cta_btn}\n  </div>\n'
            f'  <p class="credit">{cred}</p>\n</header>\n')
    crumbs = re.search(r'<nav class="crumbs wrap".*?</p>\n', tpl, re.S).group(0)
    crumbs = re.sub(r'<li aria-current="page">.*?</li>', f'<li aria-current="page">{h(d["crumb"])}</li>', crumbs)
    crumbs = re.sub(r'(Mis à jour le |Updated )[^<]*', lambda m: m[1] + Lg['date'], crumbs)
    g, v = links(p, lang)
    arr = grab(r'<svg class="cta-arr".*?</svg>').group(0)
    tick = grab(r'<svg class="bk__i".*?</svg>').group(0)
    star = grab(r'<p class="cta-box__k">(<svg.*?</svg>)')
    star = star.group(1) if star else ''
    R = 'rel="sponsored nofollow noopener" target="_blank"'
    if g:
        cbtn = f'<a class="bk bk--gyg cta-box__b" href="{g}" {R}>{Lg["bk"]}{arr}</a><a class="cta-box__v" href="{v}" {R}>{Lg["cta_v"]}</a>'
        abtn = f'<a class="bk bk--gyg" href="{g}" {R}>{tick}{Lg["bk"]}</a><a class="bk bk--via" href="{v}" {R}>{Lg["bkv"]}</a>'
    else:
        cbtn = f'<a class="bk bk--via cta-box__b" href="{v}" {R}>{Lg["bk"]}{arr}</a>'
        abtn = f'<a class="bk bk--via" href="{v}" {R}>{tick}{Lg["bk"]}</a>'
    cta = (f'<aside class="cta-box"><p class="cta-box__k">{star}{Lg["cta_k"]}</p><p class="cta-box__t">{h(d["acts"][0][0])}</p>'
           f'<p class="cta-box__d">{"Annulation gratuite sur la plupart des activités · Prix affichés avant de payer" if lang == "fr" else "Free cancellation on most activities · Prices shown before you pay"}</p>'
           f'<p class="cta-box__a">{cbtn}</p></aside>')
    art = '<div class="wrap layout">\n  <article class="prose">\n    ' + ''.join(f'<p>{h(x)}</p>' for x in d['intro']) + '\n    ' + cta + '\n'
    if d.get('hist'): art += f'    <h2 id="{"histoire" if lang == "fr" else "history"}">{Lg["hist"]}</h2>' + ''.join(f'<p>{h(x)}</p>' for x in d['hist']) + '\n'
    art += f'    <h2>{h(d["see_h"])}</h2>' + ''.join(f'<h3>{h(x)}</h3><p>{h(y)}</p>' for x, y in d['see']) + '\n'
    art += f'    <h2>{h(d["go_h"])}</h2>' + ''.join(f'<h3>{h(x)}</h3><p>{h(y)}</p>' for x, y in d['go']) + '\n'
    art += f'    <h2 id="infos-2026">{h(d["infos_h"])}</h2><ul>' + ''.join(f'<li><strong>{h(x)}</strong>{" : " if lang == "fr" else ": "}{h(y)}</li>' for x, y in d['infos']) + f'</ul><p class="maj">{h(d["maj"])}</p>\n'
    art += f'    <h2>{h(d["tips_h"])}</h2><ul>' + ''.join(f'<li>{h(x)}</li>' for x in d['tips']) + '</ul>\n'
    acts = ''.join(f'<li class="act">\n  <h3 class="act__t">{h(x)}</h3><p class="act__d">{h(y)}</p>\n  <p class="act__btns">{abtn}</p>\n</li>' for x, y in d['acts'])
    art += (f'    <section class="book" id="reserver" aria-labelledby="reserver-t">\n      <h2 id="reserver-t" class="book__t">{h(d["book_h"])}</h2>\n'
            f'      <p class="book__lead">{Lg["lead"]}</p>\n      <ul class="acts">{acts}</ul>\n      <p class="aff-note">{"Liens partenaires." if lang == "fr" else "Partner links."}</p>\n    </section>\n')
    if d.get('near'):
        art += f'    <h2 id="{"autour" if lang == "fr" else "nearby"}">{Lg["near_h"]}</h2><ul class="near">' + ''.join(
            f'<li><a href="../../{s}/">{h(n)}</a> <span class="near__d">{h(t)}</span></li>' for s, n, t in d['near']) + '</ul>\n'
    art += f'    <h2>{Lg["faq"]}</h2>\n    <div class="faq">' + ''.join(f'<details><summary>{h(q)}</summary><p>{h(a_)}</p></details>' for q, a_ in d['faq']) + '</div>\n  </article>\n'
    art += (f'  <aside class="fiche" aria-labelledby="fiche-t">\n    <h2 id="fiche-t" class="fiche__t">{Lg["fiche"]}</h2>\n    <dl>'
            + ''.join(f'<div><dt>{h(x)}</dt><dd>{h(y)}</dd></div>' for x, y in d['fiche']) + '</dl>\n  </aside>\n</div>\n')
    k = tpl.find('<div class="wrap"></div>')
    if k < 0: k = tpl.index('<div class="wrap"><aside class="ride">')
    rest = tpl[k:]
    # autres : cartes de l'index de la région (sauf la page elle-même), 4 max
    idx = open(f'{root}/{reg}/index.html', encoding='utf-8').read()
    cards = [c for c in re.findall(r'<li class="card card--[a-z]+">\n  <a href="\.\./[^"]+">.*?</li>', idx, re.S) if f'/{p["slug"]}/' not in c]
    cards = [c.replace('"../', '"../../').replace("srcset=\"../assets", "srcset=\"../../assets") for c in cards][:4]
    rest = re.sub(r'(<section class="wrap" aria-labelledby="autres-t">.*?<ul class="cards">).*?(</ul>\s*</section>)', lambda m: m[1] + ''.join(cards) + m[2], rest, count=1, flags=re.S)
    rest = re.sub(r'<div class="cta-bar" id="cta-bar".*?</div>\n?', '', rest, flags=re.S)
    out = head + body + hero + crumbs + art + rest
    return out

def card(p, lang, prefix='../'):
    d = p[lang]; T = fr_typo if lang == 'fr' else (lambda x: x)
    P = f'{prefix}assets/photos/{p["slug"]}-640'
    return (f'<li class="card card--{p["card"]}">\n  <a href="{prefix}{p["reg"][lang]}/{p["slug"]}/">\n    <div class="card__face"><picture><source type="image/webp" srcset="{P}.webp">'
            f'<img class="card__img" src="{P}.jpg" alt="" loading="lazy" decoding="async"></picture><div class="card__shade" aria-hidden="true"></div>'
            f'<div class="stamp stamp--sm" aria-hidden="true"><span class="stamp__num">{p["num"]}</span></div><div class="postmark postmark--sm" aria-hidden="true"><span>{esc(p["pm"])}</span></div>'
            f'<span class="card__name">{esc(T(d["name"]))}</span></div>\n    <p class="card__txt">{esc(T(d["card"]))}</p>\n  </a>\n</li>')

def photos(p):
    src = f'/home/claude/clicandsite-guide/_photos_brutes/{p["photo"]}.jpg'
    for lang in ('fr', 'en'):
        r = ROOT[lang]
        im = ImageOps.fit(Image.open(src).convert('RGB'), (1920, 1280), centering=p.get('center', (0.5, 0.5)))
        im.save(f'{r}/assets/photos/{p["slug"]}.jpg', quality=82, optimize=True, progressive=True)
        for w, hh in ((960, 640), (640, 427)): im.resize((w, hh), Image.LANCZOS).save(f'{r}/assets/photos/{p["slug"]}-{w}.jpg', quality=80, optimize=True, progressive=True)
        ImageOps.fit(im, (1200, 630), centering=(0.5, 0.45)).save(f'{r}/assets/og/{p["slug"]}.jpg', quality=82, optimize=True)

def integrate(pages):
    """Cartes dans l'index de région, ld, sitemap, compteur accueil, crédits."""
    for lang in ('fr', 'en'):
        r = ROOT[lang]; T = fr_typo if lang == 'fr' else (lambda x: x)
        by = {}
        for p in pages: by.setdefault(p['reg'][lang], []).append(p)
        for reg, ps in by.items():
            f = f'{r}/{reg}/index.html'; s = open(f, encoding='utf-8').read()
            for p in ps:
                if f'href="../{reg}/{p["slug"]}/"' in s: continue
                sec = p['sec']
                m = re.search(r'(aria-labelledby="' + sec + r'">.*?<ul class="cards">.*?)(</ul></section>)', s, re.S)
                s = s[:m.end(1)] + card(p, lang) + s[m.end(1):]
                u = f"{BASE[lang]}/{reg}/{p['slug']}/"
                item = json.dumps({"@type": "TouristAttraction", "name": T(p[lang]['name']), "url": u}, ensure_ascii=False)
                s = re.sub(r'("includesAttraction": \[.*?)(\]\})', lambda m: m[1] + ', ' + item + m[2], s, count=1, flags=re.S)
            open(f, 'w', encoding='utf-8').write(s)
            # compteur accueil
            hp = f'{r}/index.html'; hs = open(hp, encoding='utf-8').read()
            n = len(re.findall(r'<li class="card card--', s))
            hs = re.sub(r'(<a class="region-card" href="' + reg + r'/">.*?<span class="region-card__count">)\d+( guides</span>)', lambda m: f'{m[1]}{n}{m[2]}', hs, count=1, flags=re.S)
            open(hp, 'w', encoding='utf-8').write(hs)
        sp = f'{r}/sitemap.xml'; sm = open(sp, encoding='utf-8').read()
        add = ''.join(f"  <url><loc>{BASE[lang]}/{p['reg'][lang]}/{p['slug']}/</loc><lastmod>2026-11-15</lastmod></url>\n" for p in pages if f"/{p['reg'][lang]}/{p['slug']}/<" not in sm)
        open(sp, 'w', encoding='utf-8').write(sm.replace('</urlset>', add + '</urlset>'))
        lp = f"{r}/{'mentions-legales' if lang == 'fr' else 'legal-notice'}/index.html"; ls = open(lp, encoding='utf-8').read()
        items = ''
        for p in pages:
            a, u, li, lu = p['credit']
            if u in ls: continue
            nm = esc(T(p[lang]['name'])); sep = ' : ' if lang == 'fr' else ': '
            items += (f'<li>{nm}{sep}<a href="{u}" rel="noopener" target="_blank">{esc(a)}</a>, {L[lang]["pd"]}, Wikimedia Commons</li>' if li == 'PD' else
                      f'<li>{nm}{sep}<a href="{u}" rel="noopener" target="_blank">{esc(a)}</a>, <a href="{lu}" rel="noopener license" target="_blank">{li}</a>, Wikimedia Commons</li>')
        ls = re.sub(r'(<li>Fort Carré.*?</li>)', lambda m: m[1] + items, ls, count=1)
        open(lp, 'w', encoding='utf-8').write(ls)

if __name__ == '__main__':
    mod = __import__(sys.argv[1])
    for p in mod.PAGES:
        photos(p)
        for lang in ('fr', 'en'):
            out = f"{ROOT[lang]}/{p['reg'][lang]}/{p['slug']}/index.html"
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, 'w', encoding='utf-8').write(page(p, lang))
        print('ok', p['slug'])
    integrate(mod.PAGES)
