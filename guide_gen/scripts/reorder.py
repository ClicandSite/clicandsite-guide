import re,glob
for root,rv in (('/home/claude/clicandsite-guide','cote-d-azur'),('/home/claude/clicandsite-guide-en','french-riviera')):
    # nav: swap Riviera and Paris on every page
    n=0
    for f in glob.glob(root+'/**/*.html',recursive=True):
        s=open(f).read()
        s2=re.sub(r'(<nav class="top__nav"[^>]*>)(<a href="[^"]*'+rv+r'/">[^<]*</a>)(<a href="[^"]*paris/">Paris</a>)',r'\1\3\2',s)
        if s2!=s: open(f,'w').write(s2); n+=1
    print(root,'nav',n)
    f=root+'/index.html'; s=open(f).read()
    # region cards
    i=s.index('<div class="regions">')+len('<div class="regions">'); j=s.index('</a></div>',i)+len('</a>')
    cards=re.findall(r'<a class="region-card" href="([^"]+)">.*?</a>(?=<a class="region-card"|$)',s[i:j],re.S)
    blocks={m[1]:m[0] for m in re.finditer(r'<a class="region-card" href="([^"]+)">.*?</a>(?=<a class="region-card"|$)',s[i:j],re.S)}
    order=['paris/',rv+'/','alpes/' if 'alpes/' in blocks else 'french-alps/','alsace/']
    assert set(order)==set(blocks),blocks.keys()
    s=s[:i]+''.join(blocks[k] for k in order)+s[j:]
    # region sections
    secs=list(re.finditer(r'<section class="wrap" aria-labelledby="inc-([a-z-]+)">.*?</section>\n?',s,re.S))
    by={m[1]:m[0] for m in secs}
    print(list(by))
    a,b=secs[0].start(),secs[-1].end()
    assert s[a:b]==''.join(m[0] for m in secs)
    so=['paris',rv,'alpes' if 'alpes' in by else 'french-alps']+[k for k in by if k not in ('paris',rv,'alpes','french-alps')]
    s=s[:a]+''.join(by[k] for k in so)+s[b:]
    open(f,'w').write(s)
