import sys, re, os, json
sys.path.insert(0,'/tmp/gen')
import gen
from gen import *
from data_alsace import PAGES as AP
from PIL import Image, ImageOps
RDIR['fr']['alsace']='alsace'; RDIR['en']['alsace']='alsace'
RNAME['fr']['alsace']='Alsace'; RNAME['en']['alsace']='Alsace'
TPL['alsace']={'fr':'alpes/megeve','en':'french-alps/megeve'}
L['fr']['autres']['alsace']='Autres marchés de Noël en Alsace'
L['en']['autres']['alsace']='More Christmas markets in Alsace'

IDX = {
 'fr': dict(title='Marchés de Noël en Alsace 2026 : dates et conseils', desc='Strasbourg, Colmar, Kaysersberg, Riquewihr : nos guides des marchés de Noël d’Alsace 2026, avec les dates, les horaires, l’accès en train et nos conseils pour éviter la foule.',
            h1='Les marchés de Noël d’Alsace', lead='Chalets illuminés, vin chaud et villages à colombages : de fin novembre à fin décembre, l’Alsace devient la région de Noël par excellence.',
            alt='Maisons à colombages colorées dans la vieille ville de Colmar',
            prose=['L’Alsace est la région des marchés de Noël en France. Strasbourg, qui se dit capitale de Noël, organise le plus ancien marché du pays, et Colmar et les villages du vignoble, comme Kaysersberg ou Riquewihr, se transforment en décor de conte dès la fin novembre.',
                   'Strasbourg et Colmar sont à une demi-heure l’une de l’autre en train, et des navettes de Noël relient la gare de Colmar aux villages voisins. Chaque guide donne les dates 2026, les horaires, l’accès et nos conseils pour éviter les week-ends les plus chargés.'],
            sec='Marchés de Noël', home='Accueil', crumbs='Fil d’Ariane', photo='Photo : ',
            region_txt='Strasbourg, Colmar et les villages du vignoble : de fin novembre à fin décembre, les plus beaux marchés de Noël de France.'),
 'en': dict(title='Alsace Christmas Markets 2026: Dates and Tips', desc='Strasbourg, Colmar, Kaysersberg, Riquewihr: our guides to the 2026 Alsace Christmas markets, with dates, opening hours, train access and tips to avoid the crowds.',
            h1='The Christmas markets of Alsace', lead='Lit-up stalls, mulled wine and half-timbered villages: from late November to late December, Alsace is France’s Christmas region.',
            alt='Colourful half-timbered houses in Colmar’s old town',
            prose=['Alsace is the Christmas market region of France. Strasbourg, which calls itself the capital of Christmas, holds the country’s oldest market, while Colmar and the wine villages such as Kaysersberg and Riquewihr turn into a fairy-tale setting from late November.',
                   'Strasbourg and Colmar are half an hour apart by train, and Christmas shuttles link Colmar station to the nearby villages. Each guide gives the 2026 dates, opening hours, access and our tips for avoiding the busiest weekends.'],
            sec='Christmas markets', home='Home', crumbs='Breadcrumb', photo='Photo: ',
            region_txt='Strasbourg, Colmar and the wine villages: from late November to late December, the finest Christmas markets in France.'),
}

for lang in ('fr','en'):
    root=ROOT[lang]; o=other(lang); I=IDX[lang]
    for p in AP:
        im=ImageOps.fit(Image.open(f"/tmp/ph/{p['photo']}.jpg").convert('RGB'),(1920,1280))
        im.save(f"{root}/assets/photos/{p['photo']}.jpg",quality=82,optimize=True,progressive=True)
        for w,h in ((960,640),(640,427)): im.resize((w,h),Image.LANCZOS).save(f"{root}/assets/photos/{p['photo']}-{w}.jpg",quality=80,optimize=True,progressive=True)
        ImageOps.fit(im,(1200,630)).save(f"{root}/assets/og/{p['photo']}.jpg",quality=82,optimize=True)
    im=ImageOps.fit(Image.open('/tmp/ph/alsace.jpg').convert('RGB'),(1920,1280))
    im.save(f"{root}/assets/photos/alsace.jpg",quality=82,optimize=True,progressive=True)
    for w,h in ((960,640),(640,427)): im.resize((w,h),Image.LANCZOS).save(f"{root}/assets/photos/alsace-{w}.jpg",quality=80,optimize=True,progressive=True)
    ImageOps.fit(im,(1200,630)).save(f"{root}/assets/og/alsace.jpg",quality=82,optimize=True)
    # pages
    cards={path(lang,p):card_html(lang,p,'PFX') for p in AP}
    for p in AP:
        me=path(lang,p); others=[c for h,c in cards.items() if h!=me]
        out=f"{root}/{me}index.html"; os.makedirs(os.path.dirname(out),exist_ok=True)
        open(out,'w').write(build(lang,p,others))
    # region index from alpes index
    rsrc=f"{root}/{RDIR[lang]['alpes']}/index.html"; s=open(rsrc).read()
    url=f"{BASE[lang]}/alsace/"; ourl=f"{BASE[o]}/alsace/"; en_url=url if lang=='en' else ourl
    head_end=s.index('<script type="application/ld+json">')
    head=s[:head_end]
    head=re.sub(r'<title>.*?</title>',f"<title>{I['title']} | Clic&amp;Site</title>",head)
    head=re.sub(r'(<meta name="description" content=")[^"]*',lambda m:m[1]+ea(I['desc']),head)
    head=re.sub(r'(<meta property="og:description" content=")[^"]*',lambda m:m[1]+ea(I['desc']),head)
    head=re.sub(r'(<meta property="og:title" content=")[^"]*',lambda m:m[1]+f"{I['title']} | Clic&amp;Site",head)
    alp=RDIR[lang]['alpes']; oalp=RDIR[o]['alpes']
    head=head.replace(f"{BASE[lang]}/{alp}/",url).replace(f"{BASE[o]}/{oalp}/",ourl).replace('/assets/og/alpes.jpg','/assets/og/alsace.jpg')
    td={"@context":"https://schema.org","@type":"TouristDestination","name":"Alsace","description":I['desc'],"url":url}
    bc={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":I['home'],"item":f"{BASE[lang]}/"},{"@type":"ListItem","position":2,"name":"Alsace","item":url}]}
    body=s[s.index('</head>'):s.index('<main id="contenu">')]
    body=body.replace(f"{BASE[o]}/{oalp}/",ourl)
    foot=s[s.index('</main>'):]
    main=f'''<main id="contenu">

<header class="post">
  <img class="post__img" src="../assets/photos/alsace.jpg" srcset="../assets/photos/alsace-960.jpg 960w, ../assets/photos/alsace.jpg 1920w" sizes="100vw" alt="{ea(I['alt'])}" fetchpriority="high"><div class="post__shade" aria-hidden="true"></div>
  <div class="wrap post__in">
    <h1 class="post__title">{e(I['h1'])}</h1>
    <p class="post__lead">{e(I['lead'])}</p>
  </div>
  <p class="credit">{I['photo']}<a href="https://unsplash.com/photos/ZeN3Xq9riRU" rel="noopener" target="_blank">Patrick Robert Doyle</a> / Unsplash</p>
</header>
<nav class="crumbs wrap" aria-label="{I['crumbs']}"><ol><li><a href="../">{I['home']}</a></li><li aria-current="page">Alsace</li></ol></nav>
<section class="wrap prose">{''.join(f'<p>{e(x)}</p>' for x in I['prose'])}</section>

<section class="wrap" aria-labelledby="g-noel"><h2 id="g-noel" class="sec-title">{I['sec']}</h2><ul class="cards">{''.join(card_html(lang,p,'../') for p in AP)}</ul></section>

'''
    os.makedirs(f"{root}/alsace",exist_ok=True)
    open(f"{root}/alsace/index.html",'w').write(head+f'<script type="application/ld+json">{json.dumps(td,ensure_ascii=False)}</script>\n<script type="application/ld+json">{json.dumps(bc,ensure_ascii=False)}</script>\n'+body+main+foot)
    # home region card (first)
    f=f"{root}/index.html"; h=open(f).read()
    if 'href="alsace/"' not in h:
        rc=f'''<a class="region-card" href="alsace/">
    <div class="region-card__face">
      <img class="card__img" src="assets/photos/alsace-960.jpg" alt="" loading="lazy" decoding="async"><div class="card__shade" aria-hidden="true"></div>
      <div class="stamp" aria-hidden="true"><span class="stamp__num">67 68</span></div><div class="postmark" aria-hidden="true"><span>Alsace</span></div>
      <span class="region-card__name">Alsace</span>
      <span class="region-card__count">4 guides</span>
    </div>
    <p class="region-card__txt">{e(I['region_txt'])}</p>
  </a>'''
        h=h.replace('<div class="regions"><a class="region-card"','<div class="regions">'+rc+'<a class="region-card"',1)
        open(f,'w').write(h)
    # sitemap
    f=f"{root}/sitemap.xml"; sm=open(f).read()
    add=''.join(f"  <url><loc>{u}</loc><lastmod>2026-11-11</lastmod></url>\n" for u in [url]+[f"{BASE[lang]}/{path(lang,p)}" for p in AP] if u not in sm)
    open(f,'w').write(sm.replace('</urlset>',add+'</urlset>'))
    # nav: add Alsace after Alpes on every page
    lab={'fr':'Alpes','en':'French Alps'}[lang]
    for fp in glob.glob(f"{root}/**/*.html",recursive=True) if False else __import__('glob').glob(f"{root}/**/*.html",recursive=True):
        t=open(fp).read()
        n=re.sub(r'(<a href="([^"]*?)'+alp+r'/">'+lab+r'</a>)(?!<a href="[^"]*alsace/">)',lambda m:m[1]+f'<a href="{m[2]}alsace/">Alsace</a>',t,count=1)
        if n!=t: open(fp,'w').write(n)
    print(lang,'ok')
