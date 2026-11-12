import glob,re,sys,os
root,lang=sys.argv[1],sys.argv[2]
os.chdir(root)
css=open('assets/style.css').read()
if 'flex-wrap:wrap;gap:.5rem 1.25rem' not in css:
    css=css.replace(".top__nav{display:flex;gap:1.25rem;font-weight:600;font-size:.95rem}",".top__nav{display:flex;flex-wrap:wrap;gap:.5rem 1.25rem;font-weight:600;font-size:.95rem}\n.top__nav a{white-space:nowrap}")
    css=css.replace("  .top__nav{gap:.9rem;font-size:.9rem}","  .top__nav{gap:.55rem 1.1rem;font-size:.9rem}")
css=css.replace("  .top__nav{width:100%;gap:.55rem 1.1rem;font-size:.9rem;padding-bottom:.6rem}","  .top__nav{gap:.55rem 1.1rem;font-size:.9rem}")
css+="""
/* Sélecteur de langue FR / EN */
.langs{display:flex;align-items:center;gap:2px;border:1.5px solid rgba(255,255,255,.75);border-radius:999px;padding:2px;font-weight:700;font-size:.78rem;letter-spacing:.06em;color:#fff}
.langs a,.langs span{display:block;padding:.3rem .65rem;border-radius:999px;line-height:1;text-decoration:none;color:inherit}
.langs span{background:#fff;color:var(--encre)}
.langs a:hover{background:rgba(255,255,255,.18)}
.hero-page .langs{box-shadow:0 1px 8px rgba(0,0,0,.25)}
.plain-page .langs{border-color:var(--encre);color:var(--encre)}
.plain-page .langs span{background:var(--encre);color:#fff}
.plain-page .langs a:hover{background:rgba(19,50,75,.08)}
@media (max-width:900px){
  .langs{order:1}
  .top__nav{order:2;width:100%;padding-bottom:.6rem}
}
"""
open('assets/style.css','w').write(css)
me,other=('FR','EN') if lang=='fr' else ('EN','FR')
olang=other.lower()
for f in glob.glob('**/*.html',recursive=True):
    s=open(f).read()
    m=re.search(r'<a class="lang" href="([^"]*)"[^>]*>[^<]*</a>',s)
    if m:
        href=m[1]; s=s.replace(m[0],'')
    else:
        href='https://clicandsite.com/' if lang=='fr' else 'https://clicandsite.fr/'
    lab='Langue' if lang=='fr' else 'Language'
    sw=f'<div class="langs" aria-label="{lab}"><span aria-current="true" lang="{lang}">{me}</span><a href="{href}" hreflang="{olang}" lang="{olang}">{other}</a></div>'
    if 'class="langs"' in s: continue
    s=re.sub(r'(<nav class="top__nav".*?</nav>)',lambda mm:mm[1]+'\n    '+sw,s,count=1,flags=re.S)
    s=re.sub(r'style\.css\?v=[a-z0-9]+','style.css?v=lang2611',s)
    open(f,'w').write(s)
