import re, json, os, sys
from PIL import Image, ImageOps

SLUG = 'mont-gros'
FR_ROOT, EN_ROOT = '/home/claude/clicandsite-guide', '/home/claude/clicandsite-guide-en'
TPL = {'fr': (FR_ROOT, 'cote-d-azur', 'colline-du-chateau'), 'en': (EN_ROOT, 'french-riviera', 'colline-du-chateau')}
BASE = {'fr': 'https://clicandsite.fr', 'en': 'https://clicandsite.com'}
REG = {'fr': 'cote-d-azur', 'en': 'french-riviera'}
CREDIT = ('Cayambe', 'https://commons.wikimedia.org/wiki/File:Nice_Est_observatoire_01.jpg', 'CC BY-SA 3.0', 'https://creativecommons.org/licenses/by-sa/3.0/')

from randos_data import H as HIKES, EPS_FR, EPS_EN, COM_FR, COM_EN
C=None; SLUG=None; CREDIT=None; HK=None
def fr_typo(t):
    t = re.sub(r' ([:;?!»])', '\u202f\\1', t)
    t = t.replace('« ', '«\u202f')
    t = re.sub(r'(\d) (h|km|m|€|heures|mètres|hectares|min|minutes|marches)\b', '\\1\u00a0\\2', t)
    return t

def esc(t): return t.replace('&', '&amp;')

def page(lang):
    root, reg, tslug = TPL[lang]
    d = C[lang]; T = (fr_typo if lang == 'fr' else (lambda x: x))
    tpl = open(f'{root}/{reg}/{tslug}/index.html', encoding='utf-8').read()
    url = f'{BASE[lang]}/{REG[lang]}/{SLUG}/'
    other = 'en' if lang == 'fr' else 'fr'
    ourl = f'{BASE[other]}/{REG[other]}/{SLUG}/'
    head = tpl[:tpl.index('</head>')]
    head = re.sub(r'<title>.*?</title>', f'<title>{esc(T(d["title"]))} | Clic&amp;Site</title>', head)
    head = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m[1] + esc(T(d['desc'])), head)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m[1] + esc(T(d['title'])) + ' | Clic&amp;Site', head)
    head = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m[1] + esc(T(d['desc'])), head)
    head = head.replace(f'/{tslug}/', f'/{SLUG}/').replace(f'og/{tslug}.jpg', f'og/{SLUG}.jpg')
    head = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', '', head, flags=re.S)
    ld = [
     {"@context": "https://schema.org", "@type": "TouristAttraction", "name": T(d['name']), "description": T(d['desc']), "url": url,
      "image": [f"{BASE[lang]}/assets/photos/{SLUG}.jpg", f"{BASE[lang]}/assets/og/{SLUG}.jpg"],
      "geo": {"@type": "GeoCoordinates", "latitude": HK["geo"][0], "longitude": HK["geo"][1]},
      "address": {"@type": "PostalAddress", "addressLocality": HK["loc"], "addressRegion": "Provence-Alpes-Côte d’Azur", "addressCountry": "FR"},
      "containedInPlace": {"@type": "Place", "name": d['reg']}},
     {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": T(q), "acceptedAnswer": {"@type": "Answer", "text": T(a)}} for q, a in d['faq'] + [(d['near_q'], near_txt(lang))]]},
     {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": d['home'], "item": f"{BASE[lang]}/"},
        {"@type": "ListItem", "position": 2, "name": d['reg'], "item": f"{BASE[lang]}/{REG[lang]}/"},
        {"@type": "ListItem", "position": 3, "name": T(d['crumb']), "item": url}]}]
    head += ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld)
    body = tpl[tpl.index('</head>'):tpl.index('<header class="post')]
    body = body.replace(f'/{tslug}/', f'/{SLUG}/')
    P = '../../assets/photos/' + SLUG
    hero = (f'<header class="post post--pin">\n  <picture><source type="image/webp" srcset="{P}-960.webp 960w, {P}-1280.webp 1280w, {P}.webp 1920w" sizes="100vw">'
            f'<img class="post__img" src="{P}.jpg" srcset="{P}-960.jpg 960w, {P}-1280.jpg 1280w, {P}.jpg 1920w" sizes="100vw" alt="{esc(T(d["alt"]))}" fetchpriority="high"></picture><div class="post__shade" aria-hidden="true"></div>\n'
            f'  <div class="wrap post__in">\n    <div class="stamp" aria-hidden="true"><span class="stamp__num">06</span></div><div class="postmark" aria-hidden="true"><span>{HK["pm"]}</span></div>\n'
            f'    <h1 class="post__title">{esc(T(d["h1"]))}</h1>\n    <p class="post__lead">{esc(T(d["lead"]))}</p>\n  </div>\n'
            f'  <p class="credit">{credit_html(lang)}</p>\n</header>\n')
    crumbs = re.search(r'<nav class="crumbs wrap".*?</p>\n', tpl, re.S).group(0)
    crumbs = re.sub(r'<li aria-current="page">.*?</li>', f'<li aria-current="page">{esc(T(d["crumb"]))}</li>', crumbs)
    crumbs = re.sub(r'(Mis à jour le |Updated )[^<]*', lambda m: m[1] + ('15 novembre 2026' if lang == 'fr' else '15 November 2026'), crumbs)
    h = lambda t: esc(T(t))
    art = '<div class="wrap layout">\n  <article class="prose">\n    ' + ''.join(f'<p>{h(p)}</p>' for p in d['intro']) + '\n'
    if d.get('hist'): art += f'    <h2 id="{"histoire" if lang == "fr" else "history"}">{h(d["hist_h"])}</h2>\n' + '\n'.join(f'<p>{h(p)}</p>' for p in d['hist']) + '\n'
    art += f'<h2 id="itineraire">{h(d["rando_h"])}</h2><ol>' + ''.join(f'<li>{h(x)}</li>' for x in d['rando']) + f'</ol><p>{h(d["rando_note"])}</p>\n'
    art += f'    <h2>{h(d["see_h"])}</h2>' + ''.join(f'<h3>{h(a)}</h3><p>{h(b)}</p>' for a, b in d['see']) + '\n'
    art += f'    <h2>{h(d["go_h"])}</h2>' + ''.join(f'<h3>{h(a)}</h3><p>{h(b)}</p>' for a, b in d['go']) + '\n'
    art += f'    <h2 id="infos-2026">{h(d["infos_h"])}</h2><ul>' + ''.join(f'<li><strong>{h(a)}</strong>{h(" : " if lang == "fr" else ": ")}{h(b)}</li>' for a, b in d['infos']) + f'</ul><p class="maj">{h(d["maj"])}</p>\n'
    art += f'    <h2>{h(d["tips_h"])}</h2><ul>' + ''.join(f'<li>{h(x)}</li>' for x in d['tips']) + '</ul>\n'
    eps_li = re.search(r'<li class="act act--eps">.*?</li>', tpl, re.S).group(0)
    eps_li = re.sub(r'<h3 class="act__t">.*?</h3>', f'<h3 class="act__t">{h(d["eps_t"])}</h3>', eps_li)
    eps_li = re.sub(r'<p class="act__d">.*?</p>', f'<p class="act__d">{h(d["eps_d"])}</p>', eps_li)
    art += (f'    <section class="book" id="chauffeur" aria-labelledby="chauffeur-t">\n      <h2 id="chauffeur-t" class="book__t">{h(d["eps_h"])}</h2>\n'
            f'      <ul class="acts">{eps_li}</ul>\n    </section>\n')
    art += f'    <h2 id="autour">{h(d["near_h"])}</h2><ul class="near">' + ''.join(f'<li><a href="../../{REG[lang]}/{s}/">{h(n)}</a> <span class="near__d">{h(t)}</span></li>' for s, n, t in d['near']) + '</ul>\n'
    art += f'    <h2>{h(d["faq_h"])}</h2>\n    <div class="faq">' + ''.join(f'<details><summary>{h(q)}</summary><p>{h(a)}</p></details>' for q, a in d['faq'] + [(d['near_q'], near_txt(lang))]) + '</div>\n  </article>\n'
    art += (f'  <aside class="fiche" aria-labelledby="fiche-t">\n    <h2 id="fiche-t" class="fiche__t">{h(d["fiche_h"])}</h2>\n    <dl>'
            + ''.join(f'<div><dt>{h(a)}</dt><dd>{h(b)}</dd></div>' for a, b in d['fiche']) + '</dl>\n  </aside>\n</div>\n')
    rest = tpl[tpl.index('<div class="wrap"></div>'):]
    rest = re.sub(r'<div class="cta-bar" id="cta-bar".*?</div>\n?', '', rest, flags=re.S)
    rest = rest.replace(f'/{tslug}/', f'/{SLUG}/')
    # "autres" : colline du Château à la place de la 3e carte
    return head + body + hero + crumbs + art + rest

def near_txt(lang):
    d = C[lang]
    parts = [f'{n} ({t})' for s, n, t in d['near']]
    if lang == 'fr': return 'Dans le guide, les sites les plus proches sont ' + ', '.join(parts[:-1]) + ' et ' + parts[-1] + '.'
    return 'In this guide, the closest places are ' + ', '.join(parts[:-1]) + ' and ' + parts[-1] + '.'

def credit_html(lang):
    d = C[lang]; a, u, l, lu = CREDIT
    if l == 'Domaine public':
        return f'{d["credit_lbl"]}<a href="{u}" rel="noopener" target="_blank">{a}</a>, {"domaine public" if lang == "fr" else "public domain"}, Wikimedia Commons'
    return f'{d["credit_lbl"]}<a href="{u}" rel="noopener" target="_blank">{a}</a>, <a href="{lu}" rel="noopener license" target="_blank">{l}</a>, Wikimedia Commons'

def setup(hk):
    global C, SLUG, CREDIT, HK
    HK = hk; SLUG = hk['slug']; CREDIT = hk['credit']
    C = {'fr': {**COM_FR, **EPS_FR, **hk['fr']}, 'en': {**COM_EN, **EPS_EN, **hk['en']}}

if __name__ == '__main__':
    only = sys.argv[1:]
    for hk in HIKES:
        if only and hk['slug'] not in only: continue
        setup(hk)
        src = f'/home/claude/clicandsite-guide/_photos_brutes/{hk["photo"]}.jpg'
        for lang, root in (('fr', FR_ROOT), ('en', EN_ROOT)):
            im = ImageOps.fit(Image.open(src).convert('RGB'), (1920, 1280), centering=hk.get('center', (0.5, 0.5)))
            im.save(f'{root}/assets/photos/{SLUG}.jpg', quality=82, optimize=True, progressive=True)
            for w, hh in ((960, 640), (640, 427)): im.resize((w, hh), Image.LANCZOS).save(f'{root}/assets/photos/{SLUG}-{w}.jpg', quality=80, optimize=True, progressive=True)
            ImageOps.fit(im, (1200, 630), centering=(0.5, 0.45)).save(f'{root}/assets/og/{SLUG}.jpg', quality=82, optimize=True)
            out = f'{root}/{REG[lang]}/{SLUG}/index.html'
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, 'w', encoding='utf-8').write(page(lang))
            print('écrit', out)
