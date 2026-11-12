import sys, os, re, json, glob
sys.path.insert(0, '/tmp/gen')
import gen
from gen import *
from data_pyrenees import PAGES as NP, GYG, VIA
from PIL import Image, ImageOps

RDIR['fr']['pyrenees'] = 'pyrenees'; RDIR['en']['pyrenees'] = 'pyrenees'
RNAME['fr']['pyrenees'] = 'Pyrénées'; RNAME['en']['pyrenees'] = 'Pyrenees'
TPL['pyrenees'] = {'fr': 'alpes/megeve', 'en': 'french-alps/megeve'}
L['fr']['autres']['pyrenees'] = 'Autres stations des Pyrénées'
L['en']['autres']['pyrenees'] = 'More resorts in the Pyrenees'

def gyg_loc(lang, key):
    host = 'fr' if lang == 'fr' else 'com'
    return f'https://www.getyourguide.{host}/{GYG[key]}?partner_id=XMYSXGR&amp;cmp=clicandsite-{lang}&amp;utm_medium=online_publisher'
def via_loc(lang, key):
    base = 'https://www.viator.com/fr-FR/searchResults/all' if lang == 'fr' else 'https://www.viator.com/searchResults/all'
    return f'{base}?text={VIA[key]}&amp;pid=P00331213&amp;mcid=42383&amp;medium=link&amp;campaign=clicandsite-{lang}'
gen.gyg = gyg_loc; gen.via = via_loc

CENTER = {'grand-tourmalet': (0.5, 0.3), 'cauterets': (0.5, 0.45)}
def photo(root, name):
    im = ImageOps.fit(Image.open(f"/tmp/ph/{name}.jpg").convert('RGB'), (1920, 1280), centering=CENTER.get(name, (0.5, 0.5)))
    im.save(f"{root}/assets/photos/{name}.jpg", quality=82, optimize=True, progressive=True)
    for w, h in ((960, 640), (640, 427)):
        im.resize((w, h), Image.LANCZOS).save(f"{root}/assets/photos/{name}-{w}.jpg", quality=80, optimize=True, progressive=True)
    ImageOps.fit(im, (1200, 630)).save(f"{root}/assets/og/{name}.jpg", quality=82, optimize=True)

IDX = {
 'fr': dict(title='Stations de ski des Pyrénées : ouvertures 2026-2027', desc='Font-Romeu, Saint-Lary, Grand Tourmalet, Cauterets, Peyragudes : nos guides des stations de ski des Pyrénées pour 2026-2027, avec les dates d’ouverture, l’accès et nos conseils.',
            h1='Les stations de ski des Pyrénées', lead='Du soleil de la Cerdagne aux grands domaines des Hautes-Pyrénées : des stations souvent moins chères que dans les Alpes, à deux heures de Toulouse.',
            alt='Le pic du Midi d’Ossau enneigé, dans les Pyrénées',
            prose=['Les Pyrénées françaises comptent une quarantaine de stations, entre l’Atlantique et la Méditerranée. Les plus grandes, comme Saint-Lary ou le Grand Tourmalet, dépassent les 100 kilomètres de pistes, et les forfaits y sont souvent plus abordables que dans les grandes stations alpines.',
                   'Pour la saison 2026-2027, Cauterets ouvre parmi les premières, dès le 27 novembre, puis Font-Romeu et Saint-Lary le 4 décembre, le Grand Tourmalet le 5 décembre et Peyragudes le 12 décembre. Chaque guide donne les dates, l’accès en train ou en voiture et nos conseils.'],
            sec='Stations de ski', home='Accueil', crumbs='Fil d’Ariane', photo='Photo : ',
            region_txt='Font-Romeu, Saint-Lary, le Grand Tourmalet : des stations ensoleillées et plus abordables, ouvertes dès fin novembre 2026.'),
 'en': dict(title='Pyrenees Ski Resorts: 2026-2027 Opening Dates', desc='Font-Romeu, Saint-Lary, Grand Tourmalet, Cauterets, Peyragudes: our guides to the French Pyrenees ski resorts for 2026-2027, with opening dates, access and tips.',
            h1='Ski resorts in the Pyrenees', lead='From the Cerdagne sunshine to the big ski areas of the Hautes-Pyrénées: resorts often cheaper than the Alps, two hours from Toulouse.',
            alt='The snowy Pic du Midi d’Ossau in the Pyrenees',
            prose=['The French Pyrenees have around forty ski resorts between the Atlantic and the Mediterranean. The biggest, such as Saint-Lary and the Grand Tourmalet, have more than 100 kilometres of runs, and lift passes are often more affordable than in the big Alpine resorts.',
                   'For the 2026-2027 season, Cauterets is among the first to open, on 27 November, followed by Font-Romeu and Saint-Lary on 4 December, the Grand Tourmalet on 5 December and Peyragudes on 12 December. Each guide gives the dates, access by train or car, and our tips.'],
            sec='Ski resorts', home='Home', crumbs='Breadcrumb', photo='Photo: ',
            region_txt='Font-Romeu, Saint-Lary, the Grand Tourmalet: sunny, more affordable resorts, open from late November 2026.'),
}

# agenda entries for the ski-opening idea page: (sort key, label fr, label en, slug path, text fr, text en)
AG = [
 (1127, '27 nov.', '27 Nov', 'pyrenees/cauterets/', 'Cirque du Lys, jusqu’au 18 avril 2027.', 'Cirque du Lys, until 18 April 2027.'),
 (1203, '3 déc.', '3 Dec', 'ALP/isola-2000/', 'La station de ski la plus proche de Nice, jusqu’au 19 avril 2027.', 'The closest ski resort to Nice, until 19 April 2027.'),
 (1204, '4 déc.', '4 Dec', 'pyrenees/font-romeu/', 'Le soleil de la Cerdagne, accès en train jaune.', 'Cerdagne sunshine, reached by the Little Yellow Train.'),
 (1204, '4 déc.', '4 Dec', 'pyrenees/saint-lary/', 'Environ 100 km de pistes dans la vallée d’Aure.', 'About 100 km of runs in the Aure valley.'),
 (1205, '5 déc.', '5 Dec', 'pyrenees/grand-tourmalet/', 'La Mongie et Barèges, jusqu’au 29 mars 2027.', 'La Mongie and Barèges, until 29 March 2027.'),
 (1205, '5 déc.', '5 Dec', 'ALP/auron/', 'Station village à 1 h 30 de Nice.', 'Village resort 90 minutes from Nice.'),
 (1212, '12 déc.', '12 Dec', 'pyrenees/peyragudes/', 'Ouverture complète après une préouverture du 5 au 9 décembre.', 'Full opening after an early opening from 5 to 9 December.'),
]
def agkey(lbl):
    l = lbl.lower()
    if l.startswith(('fin nov', 'late nov')): return 1130
    m = re.match(r'(\d+)\s*(\S+)', l)
    if not m: return 9999
    mo = {'nov': 1100, 'déc': 1200, 'dec': 1200, 'jan': 1300}[m[2][:3]]
    return mo + int(m[1])

for lang in ('fr', 'en'):
    root = ROOT[lang]; o = other(lang); I = IDX[lang]
    for p in NP: photo(root, p['photo'])
    photo(root, 'pyrenees')
    alp = RDIR[lang]['alpes']; oalp = RDIR[o]['alpes']
    # --- Alpes : Isola 2000, Auron
    AP = [p for p in NP if p['region'] == 'alpes']
    existing = region_cards(lang, 'alpes'); ex = list(existing.values())
    newc = {path(lang, p): card_html(lang, p, 'PFX') for p in AP}
    for i, p in enumerate(AP):
        me = path(lang, p)
        others = [c for h, c in newc.items() if h != me] + ex[(5 * i) % len(ex):][:3]
        out = f"{root}/{me}index.html"; os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, 'w').write(build(lang, p, others))
    f = f"{root}/{alp}/index.html"; s = open(f).read()
    for p in AP:
        if f'href="../{path(lang,p)}"' in s: continue
        i = s.index('id="g-stations"'); j = s.index('</li></ul></section>', i) + len('</li>')
        s = s[:j] + card_html(lang, p, '../') + s[j:]
    open(f, 'w').write(s)
    # --- Pyrénées : pages
    PP = [p for p in NP if p['region'] == 'pyrenees']
    cards = {path(lang, p): card_html(lang, p, 'PFX') for p in PP}
    for p in PP:
        me = path(lang, p); others = [c for h, c in cards.items() if h != me]
        out = f"{root}/{me}index.html"; os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, 'w').write(build(lang, p, others))
    # --- Pyrénées : index de région (gabarit : index Alpes)
    s = open(f"{root}/{alp}/index.html").read()
    url = f"{BASE[lang]}/pyrenees/"; ourl = f"{BASE[o]}/pyrenees/"
    head = s[:s.index('<script type="application/ld+json">')]
    head = re.sub(r'<title>.*?</title>', f"<title>{e(I['title'])} | Clic&amp;Site</title>", head)
    for k in ('name="description"', 'property="og:description"'):
        head = re.sub(r'(<meta ' + k + r' content=")[^"]*', lambda m: m[1] + ea(I['desc']), head)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m[1] + f"{e(I['title'])} | Clic&amp;Site", head)
    head = head.replace(f"{BASE[lang]}/{alp}/", url).replace(f"{BASE[o]}/{oalp}/", ourl).replace('/assets/og/alpes.jpg', '/assets/og/pyrenees.jpg')
    td = {"@context": "https://schema.org", "@type": "TouristDestination", "name": RNAME[lang]['pyrenees'], "description": I['desc'], "url": url}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": I['home'], "item": f"{BASE[lang]}/"}, {"@type": "ListItem", "position": 2, "name": RNAME[lang]['pyrenees'], "item": url}]}
    body = s[s.index('</head>'):s.index('<main id="contenu">')].replace(f"{BASE[o]}/{oalp}/", ourl)
    foot = s[s.index('</main>'):]
    main = f'''<main id="contenu">

<header class="post">
  <img class="post__img" src="../assets/photos/pyrenees.jpg" srcset="../assets/photos/pyrenees-960.jpg 960w, ../assets/photos/pyrenees.jpg 1920w" sizes="100vw" alt="{ea(I['alt'])}" fetchpriority="high"><div class="post__shade" aria-hidden="true"></div>
  <div class="wrap post__in">
    <h1 class="post__title">{e(I['h1'])}</h1>
    <p class="post__lead">{e(I['lead'])}</p>
  </div>
  <p class="credit">{I['photo']}<a href="https://unsplash.com/photos/Oy_0XywezgE" rel="noopener" target="_blank">Oihan Brière</a> / Unsplash</p>
</header>
<nav class="crumbs wrap" aria-label="{I['crumbs']}"><ol><li><a href="../">{I['home']}</a></li><li aria-current="page">{RNAME[lang]['pyrenees']}</li></ol></nav>
<section class="wrap prose">{''.join(f'<p>{e(x)}</p>' for x in I['prose'])}</section>

<section class="wrap" aria-labelledby="g-stations"><h2 id="g-stations" class="sec-title">{I['sec']}</h2><ul class="cards">{''.join(card_html(lang, p, '../') for p in PP)}</ul></section>

'''
    page = head + f'<script type="application/ld+json">{json.dumps(td, ensure_ascii=False)}</script>\n<script type="application/ld+json">{json.dumps(bc, ensure_ascii=False)}</script>\n' + body + main + foot
    if lang == 'fr':
        parts = re.split(r'(<[^>]+>)', page)
        page = ''.join(x if x.startswith('<') else re.sub(r' ([:;?!])', ' \\1', x) for x in parts)
    os.makedirs(f"{root}/pyrenees", exist_ok=True)
    open(f"{root}/pyrenees/index.html", 'w').write(page)
    # --- accueil : carte région après les Alpes + compteur Alpes 16 -> 18
    f = f"{root}/index.html"; h = open(f).read()
    if 'href="pyrenees/"' not in h:
        rc = f'''<a class="region-card" href="pyrenees/">
    <div class="region-card__face">
      <img class="card__img" src="assets/photos/pyrenees-960.jpg" alt="" loading="lazy" decoding="async"><div class="card__shade" aria-hidden="true"></div>
      <div class="stamp" aria-hidden="true"><span class="stamp__num">65 66</span></div><div class="postmark" aria-hidden="true"><span>{'Pyrénées' if lang=='fr' else 'Pyrenees'}</span></div>
      <span class="region-card__name">{RNAME[lang]['pyrenees']}</span>
      <span class="region-card__count">{len(PP)} guides</span>
    </div>
    <p class="region-card__txt">{e(I['region_txt'])}</p>
  </a>'''
        k = h.index(f'<a class="region-card" href="{alp}/">'); k = h.index('</a>', k) + 4
        h = h[:k] + rc + h[k:]
    h = h.replace('count">16 guides', 'count">18 guides').replace('Voir les 16 guides des Alpes', 'Voir les 18 guides des Alpes').replace('16 French Alps guides', '18 French Alps guides')
    if lang == 'fr':
        parts = re.split(r'(<[^>]+>)', h)
        h = ''.join(x if x.startswith('<') else re.sub(r' ([:;?!])', ' \\1', x) for x in parts)
    open(f, 'w').write(h)
    # --- sitemap
    f = f"{root}/sitemap.xml"; sm = open(f).read()
    add = ''.join(f"  <url><loc>{u}</loc><lastmod>2026-11-12</lastmod></url>\n" for u in [url] + [f"{BASE[lang]}/{path(lang,p)}" for p in NP] if u not in sm)
    open(f, 'w').write(sm.replace('</urlset>', add + '</urlset>'))
    # --- menu : Pyrénées après Alpes sur toutes les pages
    lab = {'fr': 'Alpes', 'en': 'French Alps'}[lang]; nl = RNAME[lang]['pyrenees']
    for fp in glob.glob(f"{root}/**/*.html", recursive=True):
        t = open(fp).read()
        n = re.sub(r'(<a href="([^"]*?)' + alp + r'/">' + lab + r'</a>)(?!<a href="[^"]*pyrenees/">)', lambda m: m[1] + f'<a href="{m[2]}pyrenees/">{nl}</a>', t, count=1)
        if n != t: open(fp, 'w').write(n)
    # --- page idée « stations ouvertes » : agenda
    idp = {'fr': 'idees/stations-de-ski-ouvertes', 'en': 'ideas/ski-resort-opening-dates'}[lang]
    f = f"{root}/{idp}/index.html"; s = open(f).read()
    a = s.index('<ol class="agenda">'); b = s.index('</ol>', a)
    lis = re.findall(r'<li class="ag">.*?</li>', s[a:b], re.S)
    items = [(agkey(re.search(r'ag__d">([^<]*)', x)[1]), i, x) for i, x in enumerate(lis)]
    for k, (key, lf, le, pth, tf, te) in enumerate(AG):
        pth = pth.replace('ALP/', alp + '/')
        if f'href="../../{pth}"' in s[a:b]: continue
        nm = next(p[lang]['name'] for p in NP if path(lang, p) == pth)
        items.append((key, 100 + k, f'<li class="ag"><span class="ag__d">{lf if lang=="fr" else le}</span><div class="ag__b"><strong><a href="../../{pth}">{e(nm)}</a></strong><p>{e(tf if lang=="fr" else te)}</p></div></li>'))
    items.sort(key=lambda x: (x[0], x[1]))
    newol = '<ol class="agenda">' + ''.join(x[2] for x in items)
    if lang == 'fr':
        newol = re.sub(r'>([^<]*)<', lambda m: '>' + re.sub(r' ([:;?!])', ' \\1', m[1]) + '<', newol)
    s = s[:a] + newol + s[b:]
    s = s.replace('annoncées par les grandes stations des Alpes', 'annoncées par les grandes stations des Alpes et des Pyrénées').replace('announced by the big Alpine resorts', 'announced by the big resorts in the Alps and the Pyrenees')
    open(f, 'w').write(s)
    print(lang, 'ok', [x[0] for x in items])
