import sys,os,re
sys.path.insert(0,'/tmp/gen')
from gen import *
from data_chatel import PAGES as NP
from PIL import Image, ImageOps
for lang in ('fr','en'):
    root=ROOT[lang]
    for p in NP:
        im=ImageOps.fit(Image.open(f"/tmp/ph/{p['photo']}.jpg").convert('RGB'),(1920,1280))
        im.save(f"{root}/assets/photos/{p['photo']}.jpg",quality=82,optimize=True,progressive=True)
        for w,h in ((960,640),(640,427)): im.resize((w,h),Image.LANCZOS).save(f"{root}/assets/photos/{p['photo']}-{w}.jpg",quality=80,optimize=True,progressive=True)
        ImageOps.fit(im,(1200,630)).save(f"{root}/assets/og/{p['photo']}.jpg",quality=82,optimize=True)
    existing=region_cards(lang,'alpes')
    newc={path(lang,p):card_html(lang,p,'PFX') for p in NP}
    ex=list(existing.values())
    for i,p in enumerate(NP):
        me=path(lang,p)
        others=[c for h,c in newc.items() if h!=me]+ex[(3*i)%len(ex):][:2]
        out=f"{root}/{me}index.html"; os.makedirs(os.path.dirname(out),exist_ok=True)
        open(out,'w').write(build(lang,p,others))
    f=f"{root}/{RDIR[lang]['alpes']}/index.html"; s=open(f).read()
    for p in NP:
        if f'href="../{path(lang,p)}"' in s: continue
        i=s.index('id="g-stations"'); j=s.index('</li></ul></section>',i)+len('</li>')
        s=s[:j]+card_html(lang,p,'../')+s[j:]
    s=re.sub(r'(cmp|campaign)=clicandsite-'+lang+r'(?=&|")',lambda m:f'{m[1]}=clicandsite-{lang}-{RDIR[lang]["alpes"]}',s)
    open(f,'w').write(s)
    f=f"{root}/index.html"; s=open(f).read()
    s=s.replace('count">15 guides','count">16 guides').replace('Voir les 15 guides des Alpes','Voir les 16 guides des Alpes').replace('15 French Alps guides','16 French Alps guides')
    open(f,'w').write(s)
    f=f"{root}/sitemap.xml"; sm=open(f).read()
    add=''.join(f"  <url><loc>{BASE[lang]}/{path(lang,p)}</loc><lastmod>2026-11-11</lastmod></url>\n" for p in NP if f"{BASE[lang]}/{path(lang,p)}" not in sm)
    open(f,'w').write(sm.replace('</urlset>',add+'</urlset>'))
    print(lang,'ok')
