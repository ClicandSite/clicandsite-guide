import sys, re, os, json, glob
sys.path.insert(0,'/tmp/gen')
from gen import *
from data_provence import PAGES as AP
from urllib.parse import quote_plus
from PIL import Image, ImageOps
RDIR['fr']['normandie']='normandie'; RDIR['en']['normandie']='normandy'
RDIR['fr']['loire']='chateaux-de-la-loire'; RDIR['en']['loire']='loire-valley'
R='provence'
RDIR['fr'][R]='provence'; RDIR['en'][R]='provence'
RNAME['fr'][R]='Provence'; RNAME['en'][R]='Provence'
TPL[R]={'fr':'alpes/megeve','en':'french-alps/megeve'}
L['fr']['autres'][R]='Autres sites en Provence'
L['en']['autres'][R]='More places in Provence'
REG_PHOTO=('provence','Chelsea Essig','qdAVQuYQ74U')
IDX = {
 'fr': dict(title='Provence : Avignon, Aix, Marseille, calanques, Luberon, Baux-de-Provence', desc='Nos guides pour visiter la Provence : Avignon et le palais des Papes, Aix-en-Provence, Marseille, les calanques de Cassis, Gordes et le Luberon, les Baux-de-Provence, avec les horaires et les prix 2026.',
   h1='Visiter la Provence', lead='Le palais des Papes, la Bonne Mère, les calanques, les villages perchés du Luberon et les Carrières des Lumières : la Provence se visite toute l’année.',
   alt='Le village ocre de Roussillon au milieu des arbres, dans le Luberon',
   prose=['La Provence s’étend des remparts d’Avignon aux falaises des calanques. Avignon, Aix-en-Provence et Marseille sont à 2 h 40 à 3 h 15 de Paris en TGV, et chacune sert de base pour rayonner vers le Luberon, les Alpilles ou la côte.',
          'L’hiver y est souvent ensoleillé : c’est la saison des marchés de Noël, des foires aux santons et des randonnées au calme dans les calanques. Chaque guide donne les horaires, les prix 2026, l’accès et nos conseils.'],
   sec='Que voir en Provence', home='Accueil', crumbs='Fil d’Ariane', photo='Photo : ',
   region_txt='Avignon, Aix, Marseille, les calanques et les villages perchés : la Provence se visite toute l’année.'),
 'en': dict(title='Provence: Avignon, Aix, Marseille, Calanques, Luberon, Les Baux', desc='Our guides to visiting Provence: Avignon and the Palais des Papes, Aix-en-Provence, Marseille, the calanques of Cassis, Gordes and the Luberon, and Les Baux-de-Provence, with 2026 opening hours and prices.',
   h1='Visiting Provence', lead='The Palais des Papes, the Bonne Mère, the calanques, the Luberon hilltop villages and the Carrières des Lumières: Provence is worth visiting all year round.',
   alt='The ochre village of Roussillon among the trees in the Luberon',
   prose=['Provence stretches from the ramparts of Avignon to the cliffs of the calanques. Avignon, Aix-en-Provence and Marseille are 2 h 40 to 3 h 15 from Paris by TGV, and each makes a base for the Luberon, the Alpilles or the coast.',
          'Winter is often sunny: it is the season of Christmas markets, santon fairs and quiet hikes in the calanques. Each guide gives opening hours, 2026 prices, access and our tips.'],
   sec='What to see in Provence', home='Home', crumbs='Breadcrumb', photo='Photo: ',
   region_txt='Avignon, Aix, Marseille, the calanques and the hilltop villages: Provence all year round.'),
}
def fixlinks(s,lang,p):
    tag=path(lang,p).strip('/').replace('/','-')
    host='https://www.getyourguide.fr/' if lang=='fr' else 'https://www.getyourguide.com/'
    vh='https://www.viator.com/fr-FR/searchResults/all' if lang=='fr' else 'https://www.viator.com/searchResults/all'
    vt=p['vtx'][0 if lang=='fr' else 1]; i=[0]
    def rg(m):
        g=p['gyg'][min(i[0],len(p['gyg'])-1)]; i[0]+=1
        return f'class="bk bk--gyg" href="{host}{g}?partner_id=XMYSXGR&amp;cmp=clicandsite-{lang}-{tag}&amp;utm_medium=online_publisher"'
    s=re.sub(r'class="bk bk--gyg" href="https://www\.getyourguide[^"]*"',rg,s)
    s=re.sub(r'class="bk bk--via" href="https://www\.viator[^"]*"',lambda m:f'class="bk bk--via" href="{vh}?text={quote_plus(vt)}&amp;pid=P00331213&amp;mcid=42383&amp;medium=link&amp;campaign=clicandsite-{lang}-{tag}"',s)
    return s
def save_photo(root,name):
    im=ImageOps.fit(Image.open(f"/tmp/ph/{name}.jpg").convert('RGB'),(1920,1280))
    im.save(f"{root}/assets/photos/{name}.jpg",quality=82,optimize=True,progressive=True)
    for w,h in ((960,640),(640,427)): im.resize((w,h),Image.LANCZOS).save(f"{root}/assets/photos/{name}-{w}.jpg",quality=80,optimize=True,progressive=True)
    ImageOps.fit(im,(1200,630)).save(f"{root}/assets/og/{name}.jpg",quality=82,optimize=True)
for lang in ('fr','en'):
    root=ROOT[lang]; o=other(lang); I=IDX[lang]; rd=RDIR[lang][R]; ord_=RDIR[o][R]
    for p in AP: save_photo(root,p['photo'])
    save_photo(root,REG_PHOTO[0])
    cards={path(lang,p):card_html(lang,p,'PFX') for p in AP}
    for p in AP:
        me=path(lang,p); others=[c for h,c in cards.items() if h!=me]
        out=f"{root}/{me}index.html"; os.makedirs(os.path.dirname(out),exist_ok=True)
        open(out,'w').write(fixlinks(build(lang,p,others),lang,p))
    rsrc=f"{root}/{RDIR[lang]['alpes']}/index.html"; s=open(rsrc).read()
    url=f"{BASE[lang]}/{rd}/"; ourl=f"{BASE[o]}/{ord_}/"
    head=s[:s.index('<script type="application/ld+json">')]
    head=re.sub(r'<title>.*?</title>',f"<title>{I['title']} | Clic&amp;Site</title>",head)
    head=re.sub(r'(<meta name="description" content=")[^"]*',lambda m:m[1]+ea(I['desc']),head)
    head=re.sub(r'(<meta property="og:description" content=")[^"]*',lambda m:m[1]+ea(I['desc']),head)
    head=re.sub(r'(<meta property="og:title" content=")[^"]*',lambda m:m[1]+f"{I['title']} | Clic&amp;Site",head)
    alp=RDIR[lang]['alpes']; oalp=RDIR[o]['alpes']
    head=head.replace(f"{BASE[lang]}/{alp}/",url).replace(f"{BASE[o]}/{oalp}/",ourl).replace('/assets/og/alpes.jpg',f'/assets/og/{REG_PHOTO[0]}.jpg')
    td={"@context":"https://schema.org","@type":"TouristDestination","name":RNAME[lang][R],"description":I['desc'],"url":url,
        "includesAttraction":[{"@type":"TouristAttraction","name":p[lang]['name'],"url":f"{BASE[lang]}/{path(lang,p)}"} for p in AP]}
    bc={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":I['home'],"item":f"{BASE[lang]}/"},{"@type":"ListItem","position":2,"name":RNAME[lang][R],"item":url}]}
    body=s[s.index('</head>'):s.index('<main id="contenu">')].replace(f"{BASE[o]}/{oalp}/",ourl)
    foot=s[s.index('</main>'):]
    main=f'''<main id="contenu">

<header class="post">
  <img class="post__img" src="../assets/photos/{REG_PHOTO[0]}.jpg" srcset="../assets/photos/{REG_PHOTO[0]}-960.jpg 960w, ../assets/photos/{REG_PHOTO[0]}.jpg 1920w" sizes="100vw" alt="{ea(I['alt'])}" fetchpriority="high"><div class="post__shade" aria-hidden="true"></div>
  <div class="wrap post__in">
    <h1 class="post__title">{e(I['h1'])}</h1>
    <p class="post__lead">{e(I['lead'])}</p>
  </div>
  <p class="credit">{I['photo']}<a href="https://unsplash.com/photos/{REG_PHOTO[2]}" rel="noopener" target="_blank">{REG_PHOTO[1]}</a> / Unsplash</p>
</header>
<nav class="crumbs wrap" aria-label="{I['crumbs']}"><ol><li><a href="../">{I['home']}</a></li><li aria-current="page">{RNAME[lang][R]}</li></ol></nav>
<section class="wrap prose">{''.join(f'<p>{e(x)}</p>' for x in I['prose'])}</section>

<section class="wrap" aria-labelledby="g-sites"><h2 id="g-sites" class="sec-title">{I['sec']}</h2><ul class="cards">{''.join(card_html(lang,p,'../') for p in AP)}</ul></section>

'''
    page=head+f'<script type="application/ld+json">{json.dumps(td,ensure_ascii=False)}</script>\n<script type="application/ld+json">{json.dumps(bc,ensure_ascii=False)}</script>\n'+body+main+foot
    if lang=='fr':
        parts=re.split(r'(<[^>]+>)',page)
        page=''.join(x if x.startswith('<') else re.sub(r' ([:;?!])',' \\1',x) for x in parts)
    os.makedirs(f"{root}/{rd}",exist_ok=True)
    open(f"{root}/{rd}/index.html",'w').write(page)
    # home card after the Alps card
    f=f"{root}/index.html"; h=open(f).read()
    if f'href="{rd}/"' not in h.split('class="regions"')[1].split('</div>\n  <p class="next">')[0]:
        rc=f'''<a class="region-card" href="{rd}/">
    <div class="region-card__face">
      <img class="card__img" src="assets/photos/{REG_PHOTO[0]}-960.jpg" alt="" loading="lazy" decoding="async"><div class="card__shade" aria-hidden="true"></div>
      <div class="stamp" aria-hidden="true"><span class="stamp__num">13 84</span></div><div class="postmark" aria-hidden="true"><span>{RNAME[lang][R]}</span></div>
      <span class="region-card__name">{RNAME[lang][R]}</span>
      <span class="region-card__count">{len(AP)} guides</span>
    </div>
    <p class="region-card__txt">{e(I['region_txt'])}</p>
  </a>'''
        h=h.replace('<a class="region-card" href="alsace/">',rc+'<a class="region-card" href="alsace/">',1)
        open(f,'w').write(h)
    f=f"{root}/sitemap.xml"; sm=open(f).read()
    add=''.join(f"  <url><loc>{u}</loc><lastmod>2026-11-12</lastmod></url>\n" for u in [url]+[f"{BASE[lang]}/{path(lang,p)}" for p in AP] if u not in sm)
    open(f,'w').write(sm.replace('</urlset>',add+'</urlset>'))
    # nav: insert after Alps link on every page
    lab={'fr':'Châteaux de la Loire','en':'Loire Valley'}[lang]; alp=RDIR[lang]['loire']
    for fp in glob.glob(f"{root}/**/*.html",recursive=True):
        t=open(fp).read()
        n=re.sub(r'(<a href="([^"]*?)'+alp+r'/">'+lab+r'</a>)(?!<a href="[^"]*'+rd+r'/">)',lambda m:m[1]+f'<a href="{m[2]}{rd}/">{RNAME[lang][R]}</a>',t,count=1)
        if n!=t: open(fp,'w').write(n)
    print(lang,'ok')
