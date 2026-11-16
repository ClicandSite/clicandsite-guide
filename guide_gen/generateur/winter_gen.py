"""Génère les pages d'hiver (FR + EN) à partir du modèle Idées de stations-de-ski-ouvertes."""
import re, json, html, os

FR = '/home/claude/clicandsite-guide/'
EN = '/home/claude/clicandsite-guide-en/'
TPL = {'fr': FR + 'idees/stations-de-ski-ouvertes/index.html', 'en': EN + 'ideas/ski-resort-opening-dates/index.html'}
DOM = {'fr': 'https://clicandsite.fr/', 'en': 'https://clicandsite.com/'}
NB = ' '

def fr_typo(s):
    # espace insécable avant : ; ? ! dans le texte (pas dans les balises ni les URL)
    out = []
    for part in re.split(r'(<[^>]+>)', s):
        if part.startswith('<'): out.append(part); continue
        out.append(re.sub(r' ([:;?!])(?=\s|$|<)', NB + r'\1', part))
    return ''.join(out)

def credit_for(photo, root):
    import glob
    for f in glob.glob(root + '**/index.html', recursive=True):
        s = open(f).read()
        if f'assets/photos/{photo}.jpg" srcset' in s and 'class="post__img"' in s:
            m = re.search(r'<p class="credit">.*?</p>', s)
            if m: return m.group(0)
    raise SystemExit('pas de crédit pour ' + photo)

def acts_from(root, path, idx, tag, lang):
    s = open(root + path + '/index.html').read()
    lis = re.findall(r'<li class="act">.*?</li>', s, re.S)
    li = lis[idx]
    li = re.sub(r'cmp=clicandsite-(fr|en)-[a-z0-9-]+', f'cmp=clicandsite-{lang}-{tag}', li)
    li = re.sub(r'campaign=clicandsite-(fr|en)-[a-z0-9-]+', f'campaign=clicandsite-{lang}-{tag}', li)
    return li

def faq_html(faq, lang):
    return '<div class="faq">' + ''.join(f'<details><summary>{html.escape(q, quote=False)}</summary><p>{html.escape(a, quote=False)}</p></details>' for q, a in faq) + '</div>'

def build(p, lang):
    L = p[lang]
    root = FR if lang == 'fr' else EN
    other = 'en' if lang == 'fr' else 'fr'
    url = DOM[lang] + L['path'] + '/'
    url_other = DOM[other] + p[other]['path'] + '/'
    url_fr = DOM['fr'] + p['fr']['path'] + '/'; url_en = DOM['en'] + p['en']['path'] + '/'
    s = open(TPL[lang]).read()
    depth = L['path'].count('/') + 1
    pre = '../' * depth
    assert depth == 2
    tx = fr_typo if lang == 'fr' else (lambda x: x)
    title = tx(L['title']) + ' | Clic&Site'
    desc = tx(L['desc'])
    e = lambda x: html.escape(x, quote=True).replace('&#x27;', '’')
    # head
    s = re.sub(r'<title>.*?</title>', '<title>' + e(title).replace('&quot;', '"') + '</title>', s, 1)
    s = re.sub(r'(<meta (?:name="description"|property="og:description") content=")[^"]*"', lambda m: m.group(1) + e(desc) + '"', s)
    s = re.sub(r'(<meta property="og:title" content=")[^"]*"', lambda m: m.group(1) + e(title) + '"', s)
    old_url = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
    old_other = re.search(r'hreflang="' + other + r'" href="([^"]*)"', s).group(1)
    s = s.replace(old_url, url).replace(old_other, url_other)
    s = re.sub(r'(<meta property="og:image" content=")[^"]*"', lambda m: m.group(1) + DOM[lang] + 'assets/og/' + p['og'] + '.jpg"', s)
    # JSON-LD
    lds = []
    crumbs = [(L['home'], DOM[lang])] + [(n, DOM[lang] + u) for n, u in L['crumbs']] + [(tx(L['h1']), url)]
    art = {"@context": "https://schema.org", "@type": "Article", "headline": tx(L['h1']), "description": desc, "inLanguage": 'fr-FR' if lang == 'fr' else 'en-GB',
           "author": {"@type": "Organization", "name": "Clic&Site"}, "dateModified": "2026-11-16", "image": DOM[lang] + 'assets/photos/' + p['photo'] + '.jpg'}
    lds.append(art)
    if p.get('event'):
        ev = dict(p['event'][lang]); ev.update({"@context": "https://schema.org", "@type": "Event", "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode", "eventStatus": "https://schema.org/EventScheduled", "image": DOM[lang] + 'assets/photos/' + p['photo'] + '.jpg'})
        lds.append(ev)
    faq = [(tx(q), tx(a)) for q, a in L['faq']]
    lds.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})
    lds.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]})
    ldtxt = ''.join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False) + '</script>\n' for x in lds)
    s = re.sub(r'(<script type="application/ld\+json">.*?</script>\s*)+', ldtxt, s, 1, flags=re.S)
    # langues
    s = re.sub(r'(<div class="langs"[^>]*>.*?<a href=")[^"]*(")', lambda m: m.group(1) + url_other + m.group(2), s, 1, flags=re.S)
    # hero
    ph = p['photo']
    pic = (f'<picture><source type="image/webp" srcset="{pre}assets/photos/{ph}-960.webp 960w, {pre}assets/photos/{ph}-1280.webp 1280w, {pre}assets/photos/{ph}.webp 1920w" sizes="100vw">'
           f'<img class="post__img" src="{pre}assets/photos/{ph}.jpg" srcset="{pre}assets/photos/{ph}-960.jpg 960w, {pre}assets/photos/{ph}-1280.jpg 1280w, {pre}assets/photos/{ph}.jpg 1920w" sizes="100vw" alt="{e(tx(L["h1"]))}" fetchpriority="high"></picture>')
    s = re.sub(r'<picture>.*?</picture>(?=<div class="post__shade")', pic, s, 1, flags=re.S)
    s = re.sub(r'<h1 class="post__title">.*?</h1>', f'<h1 class="post__title">{tx(L["h1"])}</h1>', s, 1, flags=re.S)
    s = re.sub(r'<p class="post__lead">.*?</p>', f'<p class="post__lead">{tx(L["lead"])}</p>', s, 1, flags=re.S)
    s = re.sub(r'<p class="credit">.*?</p>', credit_for(ph, root), s, 1)
    # fil d'Ariane visible
    cr = f'<li><a href="{pre}">{L["home"]}</a></li>' + ''.join(f'<li><a href="{pre}{u}">{n}</a></li>' for n, u in L['crumbs']) + f'<li aria-current="page">{tx(L["crumb_last"])}</li>'
    s = re.sub(r'(<nav class="crumbs wrap"[^>]*><ol>).*?(</ol>)', lambda m: m.group(1) + cr + m.group(2), s, 1, flags=re.S)
    # corps : du premier prose jusqu'à la section réserver
    i0 = s.index('<div class="wrap prose prose--wide">')
    i1 = s.index('<div class="wrap prose prose--wide">\n  <section class="book"')
    body = '<div class="wrap prose prose--wide">\n' + tx(L['body']) + '\n</div>\n'
    if L.get('cards'):
        cards = ''.join(f'<li class="card card--{c.get("col", "encre")} card--idea">\n  <a href="{pre}{c["href"]}">\n    <div class="card__face"><picture><source type="image/webp" srcset="{pre}assets/photos/{c["photo"]}-640.webp"><img class="card__img" src="{pre}assets/photos/{c["photo"]}-640.jpg" alt="" loading="lazy" decoding="async"></picture><div class="card__shade" aria-hidden="true"></div><span class="card__name">{c["name"]}</span></div>\n    <p class="card__txt">{tx(c["txt"])}</p>\n  </a>\n</li>' for c in L['cards'])
        body += f'<section class="wrap" aria-label="{L["cards_t"]}"><h2 class="sec-title">{L["cards_t"]}</h2><ul class="cards">{cards}</ul></section>\n'
    s = s[:i0] + body + s[i1:]
    # réserver
    acts = ''.join(acts_from(root, a[0][lang], a[1], L['path'].replace('/', '-'), lang) for a in p['acts'])
    s = re.sub(r'<p class="book__lead">.*?</p>', f'<p class="book__lead">{tx(L["book_lead"])}</p>', s, 1, flags=re.S)
    s = re.sub(r'<!--acts:start-->.*?<!--acts:end-->\s*', '', s, 1, flags=re.S)
    s = re.sub(r'<ul class="acts">.*?</ul>', '<ul class="acts">' + acts + '</ul>', s, 1, flags=re.S)
    # FAQ
    s = re.sub(r'<div class="faq">.*?</div>\n', faq_html(faq, lang) + '\n', s, 1, flags=re.S)
    out = root + L['path'] + '/index.html'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(s)
    return out
