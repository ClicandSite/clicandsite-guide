import sys,os,re,json
sys.path.insert(0,'/tmp/gen')
import gen
from gen import *
from data_events import PAGES as NP
from urllib.parse import quote_plus
from PIL import Image, ImageOps
R='cote'
RDIR['fr'][R]='cote-d-azur'; RDIR['en'][R]='french-riviera'
RNAME['fr'][R]='Côte d’Azur'; RNAME['en'][R]='French Riviera'
TPL[R]={'fr':'alpes/megeve','en':'french-alps/megeve'}
L['fr']['autres'][R]='Autres sites de la Côte d’Azur'
L['en']['autres'][R]='More places on the French Riviera'
def path2(lang,p):
    return f"{RDIR[lang][p['region']]}/{p.get('slug_'+lang,p['slug'])}/"
gen.path=path2; path=path2
RIDE={'fr':'''<div class="wrap"><aside class="ride">
  <h2 class="ride__t">Y aller avec un chauffeur privé</h2>
  <p>Pour un aéroport, une famille avec bagages ou plusieurs sites dans la même journée, un chauffeur vous évite parkings et correspondances. Notre partenaire Elite Prestige Services, basé à Cannes, assure les transferts sur toute la Côte d’Azur.</p>
  <p><a class="btn btn--light" href="https://elite-prestige-services.fr/" rel="noopener" target="_blank">Réserver un transfert</a></p>
</aside></div>''','en':'''<div class="wrap"><aside class="ride">
  <h2 class="ride__t">Go there with a private driver</h2>
  <p>For an airport transfer, a family with luggage or several places in one day, a driver saves you parking and connections. Our partner Elite Prestige Services, based in Cannes, covers the whole French Riviera.</p>
  <p><a class="btn btn--light" href="https://elite-prestige-services.fr/" rel="noopener" target="_blank">Book a transfer</a></p>
</aside></div>'''}
SEC={'fr':'Fêtes et événements','en':'Festivals and events'}
def fixlinks(s,lang,p):
    tag=path(lang,p).strip('/').replace('/','-')
    host='https://www.getyourguide.fr/' if lang=='fr' else 'https://www.getyourguide.com/'
    vh='https://www.viator.com/fr-FR/searchResults/all' if lang=='fr' else 'https://www.viator.com/searchResults/all'
    i=[0]; j=[0]
    def rg(m):
        g=p['gyg'][min(i[0],len(p['gyg'])-1)]; i[0]+=1
        return f'class="bk bk--gyg" href="{host}{g}?partner_id=XMYSXGR&amp;cmp=clicandsite-{lang}-{tag}&amp;utm_medium=online_publisher"'
    def rv(m):
        vt=p[lang]['acts'][min(j[0],len(p[lang]['acts'])-1)][2]; j[0]+=1
        return f'class="bk bk--via" href="{vh}?text={quote_plus(vt)}&amp;pid=P00331213&amp;mcid=42383&amp;medium=link&amp;campaign=clicandsite-{lang}-{tag}"'
    s=re.sub(r'class="bk bk--gyg" href="https://www\.getyourguide[^"]*"',rg,s)
    s=re.sub(r'class="bk bk--via" href="https://www\.viator[^"]*"',rv,s)
    return s
for lang in ('fr','en'):
    root=ROOT[lang]
    for p in NP:
        im=ImageOps.fit(Image.open(f"/tmp/ph/{p['photo']}.jpg").convert('RGB'),(1920,1280),centering=(0.5,0.55))
        im.save(f"{root}/assets/photos/{p['photo']}.jpg",quality=82,optimize=True,progressive=True)
        for w,h in ((960,640),(640,427)): im.resize((w,h),Image.LANCZOS).save(f"{root}/assets/photos/{p['photo']}-{w}.jpg",quality=80,optimize=True,progressive=True)
        ImageOps.fit(im,(1200,630)).save(f"{root}/assets/og/{p['photo']}.jpg",quality=82,optimize=True)
    existing=region_cards(lang,R)
    ex=list(existing.values())
    newc={path(lang,p):card_html(lang,p,'PFX') for p in NP}
    for i,p in enumerate(NP):
        me=path(lang,p)
        nn=[c for h,c in newc.items() if h!=me]
        others=nn+ex[(3*i)%len(ex):][:2]
        html_=build(lang,p,others).replace('<div class="wrap"></div>',RIDE[lang],1)
        out=f"{root}/{me}index.html"; os.makedirs(os.path.dirname(out),exist_ok=True)
        open(out,'w').write(fixlinks(html_,lang,p))
    f=f"{root}/{RDIR[lang][R]}/index.html"; s=open(f).read()
    if 'id="g-fetes"' not in s:
        i=s.index('id="g-nature"'); j=s.index('</li></ul></section>',i)+len('</li></ul></section>')
        sec=f'<section class="wrap" aria-labelledby="g-fetes"><h2 id="g-fetes" class="sec-title">{SEC[lang]}</h2><ul class="cards">'+'\n'.join(card_html(lang,p,'../') for p in NP)+'</ul></section>'
        if lang=='fr': sec=''.join(x if x.startswith('<') else re.sub(r' ([:;?!])',' \\1',x) for x in re.split(r'(<[^>]+>)',sec))
        s=s[:j]+sec+s[j:]
    m=re.search(r'"includesAttraction": (\[.*?\])\}</script>',s)
    if m:
        arr=json.loads(m[1])
        for p in NP:
            u=f"{BASE[lang]}/{path(lang,p)}"
            if not any(a['url']==u for a in arr): arr.append({"@type":"TouristAttraction","name":p[lang]['name'],"url":u})
        s=s[:m.start(1)]+json.dumps(arr,ensure_ascii=False)+s[m.end(1):]
    open(f,'w').write(s)
    f=f"{root}/index.html"; s=open(f).read()
    s=s.replace('Voir les 19 guides de la Côte d’Azur','Voir les 22 guides de la Côte d’Azur').replace('See all 19 French Riviera guides','See all 22 French Riviera guides')
    s=re.sub(r'(region-card__name">(?:Côte d’Azur|French Riviera)</span>\s*<span class="region-card__count">)19',lambda m:m[1]+'22',s)
    open(f,'w').write(s)
    f=f"{root}/sitemap.xml"; sm=open(f).read()
    add=''.join(f"  <url><loc>{BASE[lang]}/{path(lang,p)}</loc><lastmod>2026-11-12</lastmod></url>\n" for p in NP if f"{BASE[lang]}/{path(lang,p)}" not in sm)
    open(f,'w').write(sm.replace('</urlset>',add+'</urlset>'))
    print(lang,'ok',len(ex))
