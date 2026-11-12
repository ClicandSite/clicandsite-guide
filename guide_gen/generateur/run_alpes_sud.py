import sys, os, re, glob
sys.path.insert(0, '/tmp/gen')
import gen
from gen import *
from data_alpes_sud import PAGES as NP, GYG, VIA
from data_pyrenees import PAGES as PY
from PIL import Image, ImageOps
def gyg_loc(lang, key):
    host = 'fr' if lang == 'fr' else 'com'
    return f'https://www.getyourguide.{host}/{GYG[key]}?partner_id=XMYSXGR&amp;cmp=clicandsite-{lang}&amp;utm_medium=online_publisher'
def via_loc(lang, key):
    base = 'https://www.viator.com/fr-FR/searchResults/all' if lang == 'fr' else 'https://www.viator.com/searchResults/all'
    return f'{base}?text={VIA[key]}&amp;pid=P00331213&amp;mcid=42383&amp;medium=link&amp;campaign=clicandsite-{lang}'
gen.gyg = gyg_loc; gen.via = via_loc

CENTER = {'la-grave': (0.5, 0.78)}
def photo(root, name):
    im = ImageOps.fit(Image.open(f"/tmp/ph/{name}.jpg").convert('RGB'), (1920, 1280), centering=CENTER.get(name, (0.5, 0.5)))
    im.save(f"{root}/assets/photos/{name}.jpg", quality=82, optimize=True, progressive=True)
    for w, h in ((960, 640), (640, 427)):
        im.resize((w, h), Image.LANCZOS).save(f"{root}/assets/photos/{name}-{w}.jpg", quality=80, optimize=True, progressive=True)
    ImageOps.fit(im, (1200, 630)).save(f"{root}/assets/og/{name}.jpg", quality=82, optimize=True)


def agkey(lbl):
    l = lbl.lower()
    if l.startswith(('fin nov', 'late nov')): return 1130
    m = re.match(r'(\d+)\s*(\S+)', l)
    if not m: return 9999
    mo = {'nov': 1100, 'déc': 1200, 'dec': 1200, 'jan': 1300}[m[2][:3]]
    return mo + int(m[1])


AG = [(1128, '28 nov.', '28 Nov', 'montgenevre', 'Ouverture en continu, reliée à l’Italie.', 'Open continuously, linked to Italy.'),
      (1212, '12 déc.', '12 Dec', 'superdevoluy', 'Le grand domaine familial du Dévoluy.', 'The Dévoluy’s big family ski area.'),
      (1220, '20 déc.', '20 Dec', 'la-grave', 'Téléphérique et freeride, jusqu’au 3 mai 2027.', 'Cable car and freeride, until 3 May 2027.')]
HIVER = {'fr': ('idees/cote-d-azur-en-hiver', 'Le ski à 1 h 30 de la mer', 'Isola 2000 et Auron, les stations des Alpes-Maritimes, ouvrent début décembre : une journée de ski depuis Nice ou Cannes.'),
          'en': ('ideas/french-riviera-in-winter', 'Skiing 90 minutes from the sea', 'Isola 2000 and Auron, the Alpes-Maritimes resorts, open in early December: a ski day out from Nice or Cannes.')}
for lang in ('fr', 'en'):
    root = ROOT[lang]; alp = RDIR[lang]['alpes']
    for p in NP: photo(root, p['photo'])
    existing = region_cards(lang, 'alpes')
    sc = existing.get(f'{alp}/serre-chevalier/'); dalp = existing.get(f'{alp}/les-2-alpes/') or list(existing.values())[0]
    newc = {path(lang, p): card_html(lang, p, 'PFX') for p in NP}
    for p in NP:
        me = path(lang, p)
        others = [c for h, c in newc.items() if h != me] + [c for c in (sc, dalp) if c]
        out = f"{root}/{me}index.html"; os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, 'w').write(build(lang, p, others))
    f = f"{root}/{alp}/index.html"; s = open(f).read()
    for p in NP:
        if f'href="../{path(lang,p)}"' in s: continue
        i = s.index('id="g-stations"'); j = s.index('</li></ul></section>', i) + len('</li>')
        s = s[:j] + card_html(lang, p, '../') + s[j:]
    open(f, 'w').write(s)
    f = f"{root}/index.html"; h = open(f).read()
    h = h.replace('count">18 guides', 'count">21 guides').replace('Voir les 18 guides des Alpes', 'Voir les 21 guides des Alpes').replace('18 French Alps guides', '21 French Alps guides')
    open(f, 'w').write(h)
    f = f"{root}/sitemap.xml"; sm = open(f).read()
    add = ''.join(f"  <url><loc>{BASE[lang]}/{path(lang,p)}</loc><lastmod>2026-11-12</lastmod></url>\n" for p in NP if f"{BASE[lang]}/{path(lang,p)}" not in sm)
    open(f, 'w').write(sm.replace('</urlset>', add + '</urlset>'))
    # agenda stations ouvertes
    idp = {'fr': 'idees/stations-de-ski-ouvertes', 'en': 'ideas/ski-resort-opening-dates'}[lang]
    f = f"{root}/{idp}/index.html"; s = open(f).read()
    a = s.index('<ol class="agenda">'); b = s.index('</ol>', a)
    lis = re.findall(r'<li class="ag">.*?</li>', s[a:b], re.S)
    items = [(agkey(re.search(r'ag__d">([^<]*)', x)[1]), i, x) for i, x in enumerate(lis)]
    for k, (key, lf, le, slug, tf, te) in enumerate(AG):
        pth = f'{alp}/{slug}/'
        if f'href="../../{pth}"' in s[a:b]: continue
        nm = next(p[lang]['name'] for p in NP if p['slug'] == slug)
        items.append((key, 100 + k, f'<li class="ag"><span class="ag__d">{lf if lang=="fr" else le}</span><div class="ag__b"><strong><a href="../../{pth}">{e(nm)}</a></strong><p>{e(tf if lang=="fr" else te)}</p></div></li>'))
    items.sort(key=lambda x: (x[0], x[1]))
    newol = '<ol class="agenda">' + ''.join(x[2] for x in items)
    if lang == 'fr': newol = re.sub(r'>([^<]*)<', lambda m: '>' + re.sub(r' ([:;?!])', '\u00a0\\1', m[1]) + '<', newol)
    open(f, 'w').write(s[:a] + newol + s[b:])
    # Côte d'Azur en hiver : section ski
    pth, t, lead = HIVER[lang]; f = f"{root}/{pth}/index.html"; s = open(f).read()
    if f'{alp}/isola-2000/' not in s:
        al = re.findall(r'<li class="card card--[a-z]+">\n  <a href="\.\./\.\./' + alp + r'/(?:isola-2000|auron)/">.*?</li>', open(f"{root}/{alp}/isola-2000/index.html").read() + open(f"{root}/{alp}/auron/index.html").read(), re.S)
        cards = ''.join(dict.fromkeys(al))
        sec = f'<section class="wrap" aria-label="{ea(t)}"><h2 class="sec-title">{e(t)}</h2><p class="sec-lead">{e(lead)}</p><ul class="cards">{cards}</ul></section>'
        if lang == 'fr': sec = re.sub(r'>([^<]*)<', lambda m: '>' + re.sub(r' ([:;?!])', '\u00a0\\1', m[1]) + '<', sec)
        k = s.index('<div class="wrap prose prose--wide">\n  <section class="book"')
        s = s[:k] + sec + '\n' + s[k:]
        open(f, 'w').write(s)
    print(lang, 'ok')
