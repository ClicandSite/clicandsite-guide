import json, re, os, sys, html, unicodedata
from urllib.parse import quote_plus
sys.path.insert(0, '/tmp/gen')
from data import PAGES

ROOT = {'fr': '/home/claude/clicandsite-guide', 'en': '/home/claude/clicandsite-guide-en'}
BASE = {'fr': 'https://clicandsite.fr', 'en': 'https://clicandsite.com'}
RDIR = {'fr': {'alpes': 'alpes', 'paris': 'paris'}, 'en': {'alpes': 'french-alps', 'paris': 'paris'}}
RNAME = {'fr': {'alpes': 'Alpes', 'paris': 'Paris'}, 'en': {'alpes': 'French Alps', 'paris': 'Paris'}}
TPL = {'alpes': {'fr': 'alpes/megeve', 'en': 'french-alps/megeve'}, 'paris': {'fr': 'paris/sainte-chapelle', 'en': 'paris/sainte-chapelle'}}
L = {
 'fr': dict(cta='Voir les activités à réserver', photo='Photo : ', crumbs='Fil d’Ariane', home='Accueil',
            gyg='Voir les prix sur GetYourGuide', via='Comparer sur Viator',
            lead='Réservation en ligne en quelques minutes, annulation gratuite sur la plupart des activités et avis de voyageurs pour bien choisir.',
            aff='Liens affiliés : si vous réservez, Clic&amp;Site touche une commission, sans surcoût pour vous. Les prix et disponibilités sont ceux de la plateforme.',
            faq='Questions fréquentes', fiche='En bref', autres={'alpes': 'Autres stations des Alpes', 'paris': 'Autres sites à Paris'}, locale='fr_FR'),
 'en': dict(cta='See tours and tickets', photo='Photo: ', crumbs='Breadcrumb', home='Home',
            gyg='Check prices on GetYourGuide', via='Compare on Viator',
            lead='Book online in minutes, with free cancellation on most activities and traveller reviews to help you choose.',
            aff='Affiliate links: if you book, Clic&amp;Site earns a commission at no extra cost to you. Prices and availability are set by the booking platform.',
            faq='Frequently asked questions', fiche='At a glance', autres={'alpes': 'More resorts in the French Alps', 'paris': 'More places in Paris'}, locale='en_GB'),
}
ICON = '<svg class="bk__i" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 8a2 2 0 0 0 2-2h14a2 2 0 0 0 2 2v2a2 2 0 0 0 0 4v2a2 2 0 0 0-2 2H5a2 2 0 0 0-2-2v-2a2 2 0 0 0 0-4z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M14 7v10" stroke="currentColor" stroke-width="2" stroke-dasharray="2 2"/></svg>'

def e(t):  # escape text for HTML
    return html.escape(t, quote=False)
def ea(t):
    return html.escape(t, quote=True)
def strip_acc(t):
    return ''.join(c for c in unicodedata.normalize('NFD', t) if unicodedata.category(c) != 'Mn').replace('’', ' ')

def gyg(lang, q):
    if lang == 'fr':
        return f'https://www.getyourguide.fr/s/?q={quote_plus(q)}&amp;partner_id=XMYSXGR&amp;cmp=clicandsite-fr&amp;utm_medium=online_publisher'
    return f'https://www.getyourguide.com/s/?q={quote_plus(strip_acc(q))}&amp;partner_id=XMYSXGR&amp;cmp=clicandsite-en&amp;utm_medium=online_publisher'
def via(lang, q):
    if lang == 'fr':
        return f'https://www.viator.com/fr-FR/searchResults/all?text={quote_plus(q)}&amp;pid=P00331213&amp;mcid=42383&amp;medium=link&amp;campaign=clicandsite-fr'
    return f'https://www.viator.com/searchResults/all?text={quote_plus(strip_acc(q))}&amp;pid=P00331213&amp;mcid=42383&amp;medium=link&amp;campaign=clicandsite-en'

def path(lang, p):
    return f"{RDIR[lang][p['region']]}/{p['slug']}/"
def other(lang):
    return 'en' if lang == 'fr' else 'fr'

def card_html(lang, p, prefix):
    d = p[lang]
    return f'''<li class="card card--{p['card']}">
  <a href="{prefix}{path(lang,p)}">
    <div class="card__face"><img class="card__img" src="{prefix}assets/photos/{p['photo']}-640.jpg" alt="" loading="lazy" decoding="async"><div class="card__shade" aria-hidden="true"></div><div class="stamp stamp--sm" aria-hidden="true"><span class="stamp__num">{p['num']}</span></div><div class="postmark postmark--sm" aria-hidden="true"><span>{e(p['pm'])}</span></div><span class="card__name">{e(d['name'])}</span></div>
    <p class="card__txt">{e(d['card'])}</p>
  </a>
</li>'''

def region_cards(lang, region):
    """Cards of the region index page, keyed by href (relative to site root)."""
    s = open(f"{ROOT[lang]}/{RDIR[lang][region]}/index.html").read()
    out = {}
    for m in re.finditer(r'<li class="card card--[a-z]+">\n  <a href="\.\./([^"]+)">.*?</li>', s, re.S):
        out[m[1]] = m[0].replace('"../', '"PFX')
    return out

def build(lang, p, others):
    d = p[lang]; Lg = L[lang]; o = other(lang)
    url = f"{BASE[lang]}/{path(lang,p)}"; ourl = f"{BASE[o]}/{path(o,p)}"
    en_url = url if lang == 'en' else ourl
    tpl = open(f"{ROOT[lang]}/{TPL[p['region']][lang]}/index.html").read()
    head_tail = tpl[tpl.index('<meta name="twitter:card"'):tpl.index('<script type="application/ld+json">')]
    top = tpl[tpl.index('<body'):tpl.index('<main id="contenu">')]
    tslug = TPL[p['region']][lang]; tother = TPL[p['region']][o]
    top = top.replace(f"{BASE[o]}/{tother}/", ourl)
    foot = tpl[tpl.index('</main>'):]
    title = f"{d['title']} | Clic&amp;Site"
    ta = {"@context": "https://schema.org", "@type": "TouristAttraction", "name": d['name'], "description": d['desc'], "url": url,
          "image": [f"{BASE[lang]}/assets/photos/{p['photo']}.jpg", f"{BASE[lang]}/assets/og/{p['photo']}.jpg"],
          "geo": {"@type": "GeoCoordinates", "latitude": p['geo'][0], "longitude": p['geo'][1]},
          "address": {"@type": "PostalAddress", "addressLocality": p['locality'], "addressRegion": p['aregion'], "addressCountry": "FR"},
          "containedInPlace": {"@type": "Place", "name": RNAME[lang][p['region']]}}
    fq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d['faq']]}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": Lg['home'], "item": f"{BASE[lang]}/"},
        {"@type": "ListItem", "position": 2, "name": RNAME[lang][p['region']], "item": f"{BASE[lang]}/{RDIR[lang][p['region']]}/"},
        {"@type": "ListItem", "position": 3, "name": d['name'], "item": url}]}
    J = lambda x: json.dumps(x, ensure_ascii=False)
    hreflang = (f'<link rel="alternate" hreflang="fr" href="{url if lang=="fr" else ourl}">\n<link rel="alternate" hreflang="en" href="{en_url}">'
                if lang == 'fr' else f'<link rel="alternate" hreflang="en" href="{url}">\n<link rel="alternate" hreflang="fr" href="{ourl}">')
    head = f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{ea(d['desc'])}">
<link rel="canonical" href="{url}">
{hreflang}
<link rel="alternate" hreflang="x-default" href="{en_url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Clic&amp;Site">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{ea(d['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="{Lg['locale']}">
<meta property="og:image" content="{BASE[lang]}/assets/og/{p['photo']}.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
{head_tail}<script type="application/ld+json">{J(ta)}</script>
<script type="application/ld+json">{J(fq)}</script>
<script type="application/ld+json">{J(bc)}</script>
</head>
'''
    R = '../../'
    rd = RDIR[lang][p['region']]
    see = ''.join(f'<h3>{e(a)}</h3><p>{e(b)}</p>' for a, b in d['see'])
    go = ''.join(f'<h3>{e(a)}</h3><p>{e(b)}</p>' for a, b in d['go'])
    tips = '<ul>' + ''.join(f'<li>{e(t)}</li>' for t in d['tips']) + '</ul>'
    acts = '<ul class="acts">' + ''.join(f'''<li class="act">
  <h3 class="act__t">{e(a)}</h3><p class="act__d">{e(b)}</p>
  <p class="act__btns"><a class="bk bk--gyg" href="{gyg(lang,q)}" rel="sponsored nofollow noopener" target="_blank">{ICON}{Lg['gyg']}</a><a class="bk bk--via" href="{via(lang,q)}" rel="sponsored nofollow noopener" target="_blank">{Lg['via']}</a></p>
</li>''' for a, b, q in d['acts']) + '</ul>'
    faq = '<div class="faq">' + ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in d['faq']) + '</div>'
    fiche = '<dl>' + ''.join(f'<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>' for a, b in d['fiche']) + '</dl>'
    cards = '<ul class="cards">' + ''.join(c.replace('"PFX', f'"{R}') for c in others) + '</ul>'
    main = f'''<main id="contenu">

<header class="post post--{p['post']}">
  <img class="post__img" src="{R}assets/photos/{p['photo']}.jpg" srcset="{R}assets/photos/{p['photo']}-960.jpg 960w, {R}assets/photos/{p['photo']}.jpg 1920w" sizes="100vw" alt="{ea(d['alt'])}" fetchpriority="high"><div class="post__shade" aria-hidden="true"></div>
  <div class="wrap post__in">
    <div class="stamp" aria-hidden="true"><span class="stamp__num">{p['num']}</span></div><div class="postmark" aria-hidden="true"><span>{e(p['pm'])}</span></div>
    <h1 class="post__title">{e(d['h1'])}</h1>
    <p class="post__lead">{e(d['lead'])}</p>
    <p class="post__cta"><a class="bk bk--gyg" href="#reserver">{Lg['cta']}</a></p>
  </div>
  <p class="credit">{Lg['photo']}<a href="https://unsplash.com/photos/{p['credit'][1]}" rel="noopener" target="_blank">{e(p['credit'][0])}</a> / Unsplash</p>
</header>
<nav class="crumbs wrap" aria-label="{Lg['crumbs']}"><ol><li><a href="{R}">{Lg['home']}</a></li><li><a href="{R}{rd}/">{RNAME[lang][p['region']]}</a></li><li aria-current="page">{e(d['name'])}</li></ol></nav><p class="byline wrap">{'Par <a href="'+R+'a-propos/">Anthony</a>, à Cannes · Mis à jour le 12 novembre 2026' if lang=='fr' else 'By <a href="'+R+'about/">Anthony</a>, Cannes · Updated 12 November 2026'}</p>
<div class="wrap layout">
  <article class="prose">
    {''.join(f'<p>{e(x)}</p>' for x in d['intro'])}
    <h2>{e(d['see_h'])}</h2>{see}
    <h2>{e(d['go_h'])}</h2>{go}
    <h2>{e(d['tips_h'])}</h2>{tips}
    <section class="book" id="reserver" aria-labelledby="reserver-t">
      <h2 id="reserver-t" class="book__t">{e(d['book_h'])}</h2>
      <p class="book__lead">{Lg['lead']}</p>
      {acts}
      <p class="aff-note">{Lg['aff']}</p>
    </section>
    <h2>{Lg['faq']}</h2>
    {faq}
  </article>
  <aside class="fiche" aria-labelledby="fiche-t">
    <h2 id="fiche-t" class="fiche__t">{Lg['fiche']}</h2>
    {fiche}
  </aside>
</div>
<div class="wrap"></div>
<section class="wrap" aria-labelledby="autres-t">
  <h2 id="autres-t" class="sec-title">{Lg['autres'][p['region']]}</h2>
  {cards}
</section>

'''
    page = head + top + main + foot
    if lang == 'fr':
        parts = re.split(r'(<[^>]+>)', page)
        page = ''.join(x if x.startswith('<') else re.sub(r' ([:;?!])', '\u00a0\\1', x) for x in parts)
        page = re.sub(r'(content="[^"]*")', lambda m: re.sub(r' ([:;?!])', '\u00a0\\1', m[1]), page)
    tag = path(lang, p).strip('/').replace('/', '-')
    return re.sub(r'(cmp|campaign)=clicandsite-'+lang+r'(?=&|")', lambda m: f'{m[1]}=clicandsite-{lang}-{tag}', page)

if __name__ == '__main__':
    for lang in ('fr', 'en'):
        for region in ('alpes', 'paris'):
            existing = region_cards(lang, region)  # before adding new ones
            new = [p for p in PAGES if p['region'] == region]
            newcards = {path(lang, p): card_html(lang, p, 'PFX') for p in new}
            for i, p in enumerate(new):
                me = path(lang, p)
                nn = [c for h, c in newcards.items() if h != me]
                ex = list(existing.values())
                others = nn[i % len(nn):][:1] + nn[:1] if False else (nn[:2] if i % 2 == 0 else nn[-2:])
                others = others + ex[(2*i) % len(ex):][:2]
                html_ = build(lang, p, others)
                out = f"{ROOT[lang]}/{me}index.html"
                os.makedirs(os.path.dirname(out), exist_ok=True)
                open(out, 'w').write(html_)
                print('wrote', out)
