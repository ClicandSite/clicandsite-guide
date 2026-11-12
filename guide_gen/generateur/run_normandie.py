import sys, re, os, json, glob
sys.path.insert(0,'/tmp/gen')
from gen import *
from data_normandie import PAGES as AP
from urllib.parse import quote_plus
from PIL import Image, ImageOps
R='normandie'
RDIR['fr'][R]='normandie'; RDIR['en'][R]='normandy'
RNAME['fr'][R]='Normandie'; RNAME['en'][R]='Normandy'
TPL[R]={'fr':'alpes/megeve','en':'french-alps/megeve'}
L['fr']['autres'][R]='Autres sites en Normandie'
L['en']['autres'][R]='More places in Normandy'
REG_PHOTO=('normandie','Alexander Van Steenberge','NTnxLdMX0Ao')
IDX = {
 'fr': dict(title='Normandie : Mont-Saint-Michel, Étretat, Honfleur, plages du Débarquement', desc='Nos guides pour visiter la Normandie : le Mont-Saint-Michel, les falaises d’Étretat, Honfleur, les plages du Débarquement et Rouen, avec les horaires, les prix 2026 et l’accès depuis Paris.',
   h1='Visiter la Normandie', lead='Le Mont-Saint-Michel, les falaises d’Étretat, le port de Honfleur et les plages du 6 juin 1944 : la Normandie est la grande escapade à quelques heures de Paris.',
   alt='Le Mont-Saint-Michel au crépuscule au-dessus des prés salés',
   prose=['La Normandie concentre quelques-uns des sites les plus visités de France : le Mont-Saint-Michel, les falaises de craie d’Étretat, le Vieux Bassin de Honfleur et les plages du Débarquement. Rouen, sa capitale, est à 1 h 20 de Paris en train.',
          'La région se visite toute l’année. L’hiver est la saison idéale pour éviter la foule au Mont-Saint-Michel, et Rouen accueille un marché de Noël au pied de sa cathédrale. Chaque guide donne les horaires, les prix 2026, l’accès et nos conseils.'],
   sec='Que voir en Normandie', home='Accueil', crumbs='Fil d’Ariane', photo='Photo : ',
   region_txt='Le Mont-Saint-Michel, les falaises d’Étretat, Honfleur et les plages du Débarquement : la grande escapade à quelques heures de Paris.'),
 'en': dict(title='Normandy: Mont-Saint-Michel, Étretat, Honfleur, D-Day Beaches', desc='Our guides to visiting Normandy: Mont-Saint-Michel, the Étretat cliffs, Honfleur, the D-Day beaches and Rouen, with opening hours, 2026 prices and access from Paris.',
   h1='Visiting Normandy', lead='Mont-Saint-Michel, the cliffs of Étretat, Honfleur harbour and the beaches of 6 June 1944: Normandy is the great getaway a few hours from Paris.',
   alt='Mont-Saint-Michel at dusk above the salt meadows',
   prose=['Normandy is home to some of the most visited sites in France: Mont-Saint-Michel, the chalk cliffs of Étretat, Honfleur’s Vieux Bassin and the D-Day beaches. Rouen, its capital, is 1 hour 20 from Paris by train.',
          'The region can be visited all year round. Winter is the ideal season to avoid the crowds at Mont-Saint-Michel, and Rouen holds a Christmas market beneath its cathedral. Each guide gives opening hours, 2026 prices, access and our tips.'],
   sec='What to see in Normandy', home='Home', crumbs='Breadcrumb', photo='Photo: ',
   region_txt='Mont-Saint-Michel, the Étretat cliffs, Honfleur and the D-Day beaches: the great getaway a few hours from Paris.'),
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
      <div class="stamp" aria-hidden="true"><span class="stamp__num">14 50 76</span></div><div class="postmark" aria-hidden="true"><span>{RNAME[lang][R]}</span></div>
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
    lab={'fr':'Alpes','en':'French Alps'}[lang]
    for fp in glob.glob(f"{root}/**/*.html",recursive=True):
        t=open(fp).read()
        n=re.sub(r'(<a href="([^"]*?)'+alp+r'/">'+lab+r'</a>)(?!<a href="[^"]*'+rd+r'/">)',lambda m:m[1]+f'<a href="{m[2]}{rd}/">{RNAME[lang][R]}</a>',t,count=1)
        if n!=t: open(fp,'w').write(n)
    print(lang,'ok')
