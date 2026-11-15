import glob,re,os,math,collections,html
def run(repo,targets,lang):
  P={}
  for f in glob.glob(repo+'/**/index.html',recursive=True):
    rel=os.path.dirname(f)[len(repo)+1:]
    if rel.count('/')!=1: continue
    s=open(f).read()
    g=re.search(r'"geo": \{"@type": "GeoCoordinates", "latitude": ([\d.-]+), "longitude": ([\d.-]+)\}',s)
    n=re.search(r'"@type": "TouristAttraction", "name": "([^"]*)"',s)
    if g: P[rel]=(float(g.group(1)),float(g.group(2)),n.group(1) if n else None,'<ul class="near">' in s,f)
  def km(a,b):
    la1,lo1,la2,lo2=map(math.radians,(a[0],a[1],b[0],b[1]))
    return 6371*2*math.asin(math.sqrt(math.sin((la2-la1)/2)**2+math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2))
  for t in targets:
    if t not in P: print('no geo',t); continue
    cands=sorted((km(P[t],P[s]),s) for s in P if s!=t and P[s][3])
    added=0
    for d,s in cands:
      if added>=3 or d>120: break
      f=P[s][4]; c=open(f).read()
      if f'../../{t}/' in c: continue
      name=html.unescape(P[t][2]); dd=max(1,round(d))
      lab=f'à environ {dd} km' if lang=='fr' else f'about {dd} km away'
      li=f'<li><a href="../../{t}/">{html.escape(name,quote=False)}</a> <span class="near__d">{lab}</span></li>'
      c=re.sub(r'(<ul class="near">.*?)(</ul>)',lambda m:m.group(1)+li+m.group(2),c,count=1,flags=re.S)
      open(f,'w').write(c); added+=1; print(t,'<-',s,dd)
FR=['aquitaine/bergerac','aquitaine/chateau-des-milandes','aquitaine/jardins-de-marqueyssac','aquitaine/lascaux','corse/falaises-de-bonifacio','cote-d-azur/grand-prix-de-monaco','normandie/bayeux','normandie/deauville','paris/pierrefonds','pays-basque/saint-jean-pied-de-port','provence/mont-ventoux']
EN=['aquitaine/bergerac','aquitaine/chateau-des-milandes','aquitaine/jardins-de-marqueyssac','aquitaine/lascaux','basque-country/saint-jean-pied-de-port','corsica/falaises-de-bonifacio','french-riviera/grand-prix-de-monaco','normandy/bayeux','normandy/deauville','paris/pierrefonds','provence/mont-ventoux']

run('/home/claude/clicandsite-guide',['cote-d-azur/fort-carre','cote-d-azur/cours-saleya','cote-d-azur/cap-d-antibes','cote-d-azur/marche-forville'],'fr')
run('/home/claude/clicandsite-guide-en',['french-riviera/fort-carre','french-riviera/cours-saleya','french-riviera/cap-d-antibes','french-riviera/marche-forville'],'en')
