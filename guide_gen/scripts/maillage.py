import re,glob,os,sys
DRY='--dry' in sys.argv
SKIP={'Croisière sur la Seine','Noël à Paris','Plages du Débarquement','Seine river cruise','Christmas in Paris','D-Day Beaches'}
def variants(name):
    if name in SKIP: return []
    n=re.sub(r'^(Château de |Château du |Cimetière du |The |Le (?=Marais|Sacré)|La (?=Conciergerie)|Les (?=Invalides|calanques)|Les (?=Baux))','',name)
    n=re.sub(r' (et|and) .*$','',n)
    n=re.sub(r'^calanques de ','',n); n=re.sub(r'^Calanques of ','',n)
    n=re.sub(r' Cemetery$','',n)
    return [n] if len(n)>=4 else []
for root in ('/home/claude/clicandsite-guide','/home/claude/clicandsite-guide-en'):
    pages={}
    for f in glob.glob(root+'/*/*/index.html'):
        s=open(f).read()
        if 'class="fiche"' not in s: continue
        m=re.search(r'<li aria-current="page">([^<]*)',s); pages[os.path.relpath(os.path.dirname(f),root)+'/']=(f,m[1].replace('&amp;','&'))
    kws=[]
    for p,(f,name) in pages.items():
        for v in variants(name): kws.append((v,p))
    kws.sort(key=lambda x:-len(x[0]))
    total=0
    for p,(f,name) in pages.items():
        s=open(f).read()
        a0=s.index('<article'); a1=s.index('</article>')
        art=s[a0:a1]
        b0=art.find('<section class="book"'); b1=art.find('</section>',b0)+10 if b0>=0 else -1
        linked=set(re.findall(r'href="(?:\.\./)+([a-z0-9-]+/[a-z0-9-]+/)"',art))
        st=[0]
        def proc(seg):

            out=[];inside_a=0
            for tok in re.split(r'(<[^>]+>)',seg):
                if tok.startswith('<'):
                    if tok.startswith('<a '): inside_a+=1
                    elif tok=='</a>': inside_a-=1
                    out.append(tok); continue
                if inside_a or st[0]>=3: out.append(tok); continue
                for kw,tp in kws:
                    if st[0]>=3: break
                    if tp==p or tp in linked or tp.split('/')[0]!=p.split('/')[0] or 'seine' in tp: continue
                    pat=r'(?<![\w’\'-])'+re.escape(kw)+r'(?![\w-])'+(r'(?! de)' if kw=='Notre-Dame' else '')+(r'(?! Cathedral of)' if False else '')
                    mm=re.search(pat,tok)
                    if mm:
                        tok=tok[:mm.start()]+f'<a href="../../{tp}">{mm[0]}</a>'+tok[mm.end():]
                        linked.add(tp); st[0]+=1
                        # rest of tok is after link; stop processing this tok further to keep it simple
                        break
                out.append(tok)
            return ''.join(out)
        def blocks(txt):
            return re.sub(r'(<(p|li)>)(.*?)(</\2>)',lambda m:m[1]+proc(m[3])+m[4],txt,flags=re.S)
        if b0>=0: new=blocks(art[:b0])+art[b0:b1]+blocks(art[b1:])
        else: new=blocks(art)
        added=st[0]
        if added:
            total+=added
            if DRY: print(p,added,re.findall(r'<a href="\.\./\.\./([^"]+)">([^<]+)</a>',new)[-added:])
            else: open(f,'w').write(s[:a0]+new+s[a1:])
    print(root,total)
