import glob,re,html,sys
SUF=' | Clic&Site'; MAXT=70-len(SUF); MAXD=158
SKIP={'paris/montmartre','cote-d-azur/rocher-de-monaco','french-riviera/rocher-de-monaco','cote-d-azur/saint-jean-cap-ferrat','french-riviera/saint-jean-cap-ferrat','cote-d-azur/eze','french-riviera/eze','cote-d-azur/roquebrune-cap-martin','french-riviera/roquebrune-cap-martin','bretagne/ploumanach','brittany/ploumanach'}
def items(s,lang):
  et=' et ' if lang=='fr' else ' and '
  parts=re.split(r',\s+',s)
  last=parts[-1]
  if et in last: a,b=last.rsplit(et,1); parts=parts[:-1]+[a,b]
  return [p for p in parts if p]
def join(it,lang):
  et=' et ' if lang=='fr' else ' and '
  return it[0] if len(it)==1 else ', '.join(it[:-1])+et+it[-1]
def short_title(t,lang):
  if len(t)<=MAXT: return t
  segs=re.split(r'(\s*\|\s*|\s*[:–—]\s*)',t,maxsplit=1) if False else None
  m=re.match(r'^(.*?)(\s*[  ]?[:|]\s*)(.*)$',t)
  if not m: 
    it=items(t,lang)
    while len(it)>1 and len(join(it,lang))>MAXT: it=it[:-1]
    return join(it,lang)
  head,sep,rest=m.groups()
  rest=re.split(r'\s*\|\s*',rest)[0]
  if len(head)>MAXT: return short_title(head,lang)
  it=items(rest,lang)
  while it and len(head+sep+join(it,lang))>MAXT: it=it[:-1]
  if not it: return head
  return head+sep+join(it,lang)
def short_desc(d):
  if len(d)<=160: return d
  sents=re.split(r'(?<=[.!?])\s+',d); out=''
  for s in sents:
    if len(out+(' ' if out else '')+s)<=MAXD: out=out+(' ' if out else '')+s
    else: break
  if len(out)>=90: return out
  # cut first long sentence at a clause
  s=d[:MAXD]; k=max(s.rfind(', '),s.rfind(' : '),s.rfind(' : '))
  if k<80: k=s.rfind(' ')
  return s[:k].rstrip(' ,: ')+'.'
def esc(x): return html.escape(x,quote=True).replace('&#x27;','’')
dry='--dry' in sys.argv; nt=nd=0; ex=[]
for repo in [a for a in sys.argv[1:] if not a.startswith('--')]:
  lang='en' if repo.endswith('-en') else 'fr'
  for f in glob.glob(repo+'/**/index.html',recursive=True):
    rel=f[len(repo)+1:-len('/index.html')]
    if rel in SKIP: continue
    s=open(f).read(); o=s
    m=re.search(r'<title>(.*?)</title>',s,re.S)
    if m:
      raw=m.group(1); t=html.unescape(raw)
      if t.endswith(SUF) and len(t)>70:
        new=short_title(t[:-len(SUF)],lang)+SUF
        if len(new)>=25:
          newe=esc(new); s=s.replace('<title>'+raw+'</title>','<title>'+newe+'</title>')
          s=s.replace('content="'+raw+'"','content="'+newe+'"'); nt+=1; ex.append(('T',len(new),new))
    m=re.search(r'<meta name="description" content="([^"]*)"',s)
    if m:
      raw=m.group(1); d=html.unescape(raw)
      if len(d)>160:
        nd_=short_desc(d); newe=esc(nd_)
        s=s.replace('content="'+raw+'"','content="'+newe+'"'); nd+=1; ex.append(('D',len(nd_),nd_))
    if s!=o and not dry: open(f,'w').write(s)
print(nt,nd)
import random; random.seed(3)
for e in random.sample(ex,min(30,len(ex))): print(e)
print(max(e[1] for e in ex if e[0]=='T'), min(e[1] for e in ex if e[0]=='D'))
