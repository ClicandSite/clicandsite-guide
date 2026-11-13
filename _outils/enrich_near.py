# Enrichit les pages Paris et Côte d'Azur (FR et EN) : section « À voir à proximité » (distances calculées
# à partir des coordonnées des pages), et 2 questions de FAQ (durée de visite, sites proches), visibles + JSON-LD.
import re,glob,json,math,sys
NB=' '
CONF={'fr':('/home/claude/clicandsite-guide',['paris','cote-d-azur']),'en':('/home/claude/clicandsite-guide-en',['paris','french-riviera'])}
SKIP={'3-jours','3-days','carnaval-de-nice','nice-carnival','fete-du-citron-menton','lemon-festival-menton','noel-cote-d-azur','christmas-french-riviera','noel-a-paris','christmas-in-paris','festival-de-cannes','grand-prix-de-monaco'}
def dist(a,b):
    R=6371;la1,lo1,la2,lo2=map(math.radians,(a[0],a[1],b[0],b[1]))
    d=2*R*math.asin(math.sqrt(math.sin((la2-la1)/2)**2+math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2));return d
def lowart(n):
    return re.sub(r'^(Le|La|Les|L’)\b',lambda m:m.group(1).lower(),n)
def de_from_in(x):
    for a,b in [('dans les ','des '),('dans le ','du '),('dans la ','de la '),('dans l’','de l’'),('à la ','de la '),('à l’','de l’'),('aux ','des '),('au ','du '),('sur la ','de la '),('sur le ','du '),('sur les ','des '),('autour de la ','de la '),('autour du ','du '),('autour des ','des '),('le long du ','du '),('à ','de ')]:
        if x.startswith(a):
            r=b+x[len(a):]
            if r.startswith('de ') and re.match(r'de [AEIOUÉÈÎaeiouéy]',r): r='d’'+r[3:]
            return r
    return None
for lang,(root,regs) in CONF.items():
    pages={}
    for reg in regs:
        for f in glob.glob(f'{root}/{reg}/*/index.html'):
            slug=f.split('/')[-2];h=open(f).read();geo=None
            for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',h,re.S):
                j=json.loads(m)
                if j.get('@type')=='TouristAttraction' and j.get('geo'): geo=(float(j['geo']['latitude']),float(j['geo']['longitude']))
            name=re.search(r'aria-current="page">([^<]*)',h)
            pages[(reg,slug)]=dict(f=f,h=h,geo=geo,name=name.group(1).strip() if name else None)
    n=0
    for (reg,slug),p in pages.items():
        if slug in SKIP or not p['geo'] or 'id="autour"' in p['h']: continue
        h=p['h']
        cands=sorted(((dist(p['geo'],q['geo']),k,q) for k,q in pages.items() if k!=(reg,slug) and k[0]==reg and q['geo'] and k[1] not in SKIP),key=lambda x:x[0])[:3]
        if len(cands)<3: continue
        def how(d):
            if d<1.8:
                m=max(5,int(round(d*1.3/4.5*60/5.0))*5)
                return f'à environ {m}{NB}min à pied' if lang=='fr' else f'about {m} min on foot'
            km=int(round(d*1.25)) or 1
            return f'à environ {km}{NB}km' if lang=='fr' else f'about {km} km away'
        items=[(q['name'],f'../../{k[0]}/{k[1]}/',how(d)) for d,k,q in cands]
        lis=''.join(f'<li><a href="{u}">{nm}</a> <span class="near__d">{w}</span></li>' for nm,u,w in items)
        title='À voir à proximité' if lang=='fr' else 'Nearby'
        sec=f'<h2 id="autour">{title}</h2><ul class="near">{lis}</ul>\n    '
        faqh='<h2>Questions fréquentes</h2>' if lang=='fr' else '<h2>Frequently asked questions</h2>'
        if faqh not in h: continue
        h=h.replace(faqh,sec+faqh,1)
        # FAQ
        a=h.find('<article class="prose">');m=re.search(r'<h2[^>]*>([^<]*)</h2>',h[a:]);t=m.group(1).replace(NB,' ')
        dur=re.search(r'<dt>(?:Durée conseillée|Time needed)</dt><dd>([^<]*)</dd>',h)
        qa=[]
        names=[x[0] for x in items];wh=[x[2] for x in items]
        if lang=='fr':
            mm=re.match(r'Que voir (.+)$',t)
            if mm:
                X=mm.group(1).strip();D=de_from_in(X)
                if dur: qa.append((f'Combien de temps passer {X}{NB}?',f'Comptez {dur.group(1)[0].lower()+dur.group(1)[1:]}{"" if dur.group(1).endswith(".") else "."}'))
                if D:
                    lst=', '.join(f'{lowart(nm) if i else nm} ({w})' for i,(nm,w) in enumerate(zip(names,wh)))
                    qa.append((f'Que voir près {D}{NB}?',f'Dans le guide, les sites les plus proches sont {", ".join(f"{lowart(nm)} ({w})" for nm,w in zip(names,wh))}.'))
        else:
            mm=re.match(r'(?:Things to (?:see|do)|What to see) (in|at|on|around|along) (.+)$',t)
            if mm:
                X=mm.group(1)+' '+mm.group(2);Y=mm.group(2)
                if dur: qa.append((f'How long should you spend {X}?',f'Allow {dur.group(1)[0].lower()+dur.group(1)[1:]}{"" if dur.group(1).endswith(".") else "."}'))
                qa.append((f'What is there to see near {Y}?',f'In this guide, the closest places are {", ".join(f"{nm} ({w})" for nm,w in zip(names,wh))}.'))
        qa=[(q,r) for q,r in qa if q not in h]
        if qa:
            i=h.find('<div class="faq">');j=h.find('</div>',i)
            h=h[:j]+''.join(f'<details><summary>{q}</summary><p>{r}</p></details>' for q,r in qa)+h[j:]
            def addld(m):
                j=json.loads(m.group(1))
                if j.get('@type')!='FAQPage': return m.group(0)
                for q,r in qa: j['mainEntity'].append({"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":re.sub('<[^>]+>','',r)}})
                return '<script type="application/ld+json">'+json.dumps(j,ensure_ascii=False)+'</script>'
            h=re.sub(r'<script type="application/ld\+json">(\{"@context": "https://schema.org", "@type": "FAQPage".*?)</script>',addld,h,count=1,flags=re.S)
        open(p['f'],'w').write(h);n+=1
    print(lang,n)
