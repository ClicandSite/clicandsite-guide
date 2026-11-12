import sys, re, os, json, glob
sys.path.insert(0,'/tmp/gen')
from gen import *
from data_loire import PAGES as AP
from urllib.parse import quote_plus
from PIL import Image, ImageOps
RDIR['fr']['normandie']='normandie'; RDIR['en']['normandie']='normandy'
R='loire'
RDIR['fr'][R]='chateaux-de-la-loire'; RDIR['en'][R]='loire-valley'
RNAME['fr'][R]='Châteaux de la Loire'; RNAME['en'][R]='Loire Valley'
TPL[R]={'fr':'alpes/megeve','en':'french-alps/megeve'}
L['fr']['autres'][R]='Autres châteaux de la Loire'
L['en']['autres'][R]='More Loire Valley châteaux'
REG_PHOTO=('loire','Colin Watts','nSO236rmK8s')
IDX = {
 'fr': dict(title='Châteaux de la Loire : Chambord, Chenonceau, Amboise, Villandry', desc='Nos guides pour visiter les châteaux de la Loire : Chambord, Chenonceau, Amboise et le Clos Lucé, Villandry, avec les horaires, les prix 2026, Noël dans les châteaux et l’accès depuis Paris.',
   h1='Visiter les châteaux de la Loire', lead='Chambord, Chenonceau, Amboise et Villandry : les grands châteaux de la Renaissance, à deux heures de Paris.',
   alt='Le château de Chenonceau et ses arches au-dessus du Cher',
   prose=['La vallée de la Loire, inscrite au patrimoine mondial de l’Unesco, rassemble les plus beaux châteaux de la Renaissance : Chambord, le plus grand, Chenonceau bâti sur le Cher, Amboise et le Clos Lucé de Léonard de Vinci, Villandry et ses jardins. Tours, Amboise et Blois sont à 1 h à 2 h de Paris en train.',
          'En hiver, la plupart des châteaux restent ouverts et se parent de décors de Noël de fin novembre à début janvier. Chaque guide donne les horaires, les prix 2026, l’accès et nos conseils.'],
   sec='Que voir dans la vallée de la Loire', home='Accueil', crumbs='Fil d’Ariane', photo='Photo : ',
   region_txt='Chambord, Chenonceau, Amboise et Villandry : les grands châteaux de la Renaissance, à deux heures de Paris.'),
 'en': dict(title='Loire Valley Châteaux: Chambord, Chenonceau, Amboise, Villandry', desc='Our guides to visiting the Loire Valley châteaux: Chambord, Chenonceau, Amboise and Clos Lucé, Villandry, with opening hours, 2026 prices, Christmas at the châteaux and access from Paris.',
   h1='Visiting the Loire Valley châteaux', lead='Chambord, Chenonceau, Amboise and Villandry: the great Renaissance châteaux, two hours from Paris.',
   alt='Château de Chenonceau and its arches over the river Cher',
   prose=['The Loire Valley, a Unesco World Heritage site, is home to the finest Renaissance châteaux: Chambord, the largest, Chenonceau built across the Cher, Amboise and Leonardo da Vinci’s Clos Lucé, and Villandry with its gardens. Tours, Amboise and Blois are 1 to 2 hours from Paris by train.',
          'In winter most châteaux stay open and put up Christmas decorations from late November to early January. Each guide gives opening hours, 2026 prices, access and our tips.'],
   sec='What to see in the Loire Valley', home='Home', crumbs='Breadcrumb', photo='Photo: ',
   region_txt='Chambord, Chenonceau, Amboise and Villandry: the great Renaissance châteaux, two hours from Paris.'),
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
      <div class="stamp" aria-hidden="true"><span class="stamp__num">37 41</span></div><div class="postmark" aria-hidden="true"><span>{RNAME[lang][R]}</span></div>
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
    lab={'fr':'Normandie','en':'Normandy'}[lang]; alp=RDIR[lang]['normandie']
    for fp in glob.glob(f"{root}/**/*.html",recursive=True):
        t=open(fp).read()
        n=re.sub(r'(<a href="([^"]*?)'+alp+r'/">'+lab+r'</a>)(?!<a href="[^"]*'+rd+r'/">)',lambda m:m[1]+f'<a href="{m[2]}{rd}/">{RNAME[lang][R]}</a>',t,count=1)
        if n!=t: open(fp,'w').write(n)
    print(lang,'ok')
