import sys, os
sys.path.insert(0,'/tmp/g')
import site_gen as G
import data_new15a as A, data_new15b as B, data_new15c as C
PAGES = A.PAGES + B.PAGES + C.PAGES
DRY = '--dry' in sys.argv
allp = {(p['reg'][l], p['slug']) for p in PAGES for l in ('fr','en')}
for p in PAGES:
    if not DRY: G.photos(p)
    for lang in ('fr','en'):
        out = f"{G.ROOT[lang]}/{p['reg'][lang]}/{p['slug']}/index.html"
        html = G.page(p, lang)
        for s,_,_ in p[lang]['near']:
            assert os.path.exists(f"{G.ROOT[lang]}/{s}/index.html") or tuple(s.split('/')) in allp, (p['slug'], lang, s)
        assert len(p[lang]["title"]) <= 58, (p['slug'], lang, len(p[lang]['title']))
        assert len(p[lang]['desc']) <= 165, (p['slug'], lang, len(p[lang]['desc']))
        if not DRY:
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out,'w',encoding='utf-8').write(html)
    print('ok', p['slug'])
if not DRY: G.integrate(PAGES)
