import re,glob,os
T={'fr':('/home/claude/clicandsite-guide','a-propos','Par <a href="{R}a-propos/">Anthony</a>, à Cannes · Mis à jour le 12 novembre 2026'),
   'en':('/home/claude/clicandsite-guide-en','about','By <a href="{R}about/">Anthony</a>, Cannes · Updated 12 November 2026')}
for lang,(root,ab,tpl) in T.items():
    n=0
    for f in glob.glob(root+'/**/index.html',recursive=True):
        s=open(f).read()
        if 'class="fiche"' not in s or 'class="byline' in s: continue
        depth=os.path.relpath(f,root).count('/')
        R='../'*depth
        b=f'<p class="byline wrap">{tpl.format(R=R)}</p>'
        t=re.sub(r'(<nav class="crumbs wrap"[^>]*>.*?</nav>)',lambda m:m[1]+b,s,count=1,flags=re.S)
        if t!=s: open(f,'w').write(t); n+=1
    css=root+'/assets/style.css'; c=open(css).read()
    if '.byline' not in c:
        open(css,'a').write('\n.byline{font-size:.8125rem;color:var(--doux);margin:.35rem auto 0}\n.byline a{color:var(--doux)}\n')
    print(lang,n)
