import sys,os,re,json
sys.path.insert(0,'/tmp/gen')
from gen import *
from data_paris4 import PAGES as NP
from urllib.parse import quote_plus
from PIL import Image, ImageOps
N_OLD,N_NEW=29,29+len(NP)
def fixlinks(s,lang,p):
    tag=f"paris-{p['slug']}"
    host='https://www.getyourguide.fr/' if lang=='fr' else 'https://www.getyourguide.com/'
    vh='https://www.viator.com/fr-FR/searchResults/all' if lang=='fr' else 'https://www.viator.com/searchResults/all'
    vt=p['vtx'][0 if lang=='fr' else 1]; i=[0]
    def rg(m):
        g=p['gyg'][min(i[0],len(p['gyg'])-1)]; i[0]+=1
        return f'class="bk bk--gyg" href="{host}{g}?partner_id=XMYSXGR&amp;cmp=clicandsite-{lang}-{tag}&amp;utm_medium=online_publisher"'
    s=re.sub(r'class="bk bk--gyg" href="https://www\.getyourguide[^"]*"',rg,s)
    s=re.sub(r'class="bk bk--via" href="https://www\.viator[^"]*"',lambda m:f'class="bk bk--via" href="{vh}?text={quote_plus(vt)}&amp;pid=P00331213&amp;mcid=42383&amp;medium=link&amp;campaign=clicandsite-{lang}-{tag}"',s)
    return s
for lang in ('fr','en'):
    root=ROOT[lang]
    for p in NP:
        im=ImageOps.fit(Image.open(f"/tmp/ph/{p['photo']}.jpg").convert('RGB'),(1920,1280))
        im.save(f"{root}/assets/photos/{p['photo']}.jpg",quality=82,optimize=True,progressive=True)
        for w,h in ((960,640),(640,427)): im.resize((w,h),Image.LANCZOS).save(f"{root}/assets/photos/{p['photo']}-{w}.jpg",quality=80,optimize=True,progressive=True)
        ImageOps.fit(im,(1200,630)).save(f"{root}/assets/og/{p['photo']}.jpg",quality=82,optimize=True)
    existing=region_cards(lang,'paris')
    newc={path(lang,p):card_html(lang,p,'PFX') for p in NP}
    ex=list(existing.values())
    for i,p in enumerate(NP):
        me=path(lang,p)
        nn=[c for h,c in newc.items() if h!=me]
        others=nn[i%len(nn):][:2]+ex[(3*i)%len(ex):][:2]
        out=f"{root}/{me}index.html"; os.makedirs(os.path.dirname(out),exist_ok=True)
        open(out,'w').write(fixlinks(build(lang,p,others),lang,p))
    f=f"{root}/paris/index.html"; s=open(f).read()
    for p in NP:
        if f'href="../{path(lang,p)}"' in s: continue
        i=s.index(f'id="{p["group"]}"'); j=s.index('</li></ul></section>',i)+len('</li>')
        s=s[:j]+'\n'+card_html(lang,p,'../')+s[j:]
    m=re.search(r'"includesAttraction": (\[.*?\])\}</script>',s)
    arr=json.loads(m[1])
    for p in NP:
        u=f"{BASE[lang]}/{path(lang,p)}"
        if not any(a['url']==u for a in arr): arr.append({"@type":"TouristAttraction","name":p[lang]['name'],"url":u})
    s=s[:m.start(1)]+json.dumps(arr,ensure_ascii=False)+s[m.end(1):]
    open(f,'w').write(s)
    f=f"{root}/index.html"; s=open(f).read()
    s=re.sub(r'(region-card__name">Paris</span>\s*<span class="region-card__count">)'+str(N_OLD),lambda m:m[1]+str(N_NEW),s)
    s=s.replace(f'Voir les {N_OLD} guides de Paris',f'Voir les {N_NEW} guides de Paris').replace(f'See all {N_OLD} Paris guides',f'See all {N_NEW} Paris guides')
    open(f,'w').write(s)
    f=f"{root}/sitemap.xml"; sm=open(f).read()
    add=''.join(f"  <url><loc>{BASE[lang]}/{path(lang,p)}</loc><lastmod>2026-11-11</lastmod></url>\n" for p in NP if f"{BASE[lang]}/{path(lang,p)}" not in sm)
    open(f,'w').write(sm.replace('</urlset>',add+'</urlset>'))
    print(lang,'ok')
