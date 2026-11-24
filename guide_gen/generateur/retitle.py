"""Réécrit titre + description (title, og:title, meta description, og:description, JSON-LD description) d'une page.
Usage : import retitle; retitle.apply(root, path, title, desc)"""
import re, html, json
NB=' '
def esc(s): return html.escape(s, quote=True)
def fr_typo(s): return re.sub(r' ([:;?!])', NB+r'\1', s)
def apply(root, path, title, desc, lang='fr'):
    f=f'{root}/{path}/index.html'; s=open(f).read()
    if lang=='fr': title, desc = fr_typo(title), fr_typo(desc)
    assert len(title.replace(NB,' '))<=58, (path, len(title)); assert len(desc)<=160, (path, len(desc))
    old_t=html.unescape(re.search(r'<title>(.*?)</title>',s).group(1))
    old_d=html.unescape(re.search(r'name="description" content="([^"]*)"',s).group(1))
    full=title+' | Clic&Site'
    s=re.sub(r'<title>.*?</title>', '<title>'+esc(full).replace('&#x27;',"'")+'</title>', s, 1)
    s=re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1)+esc(full).replace('&#x27;',"'"), s, 1)
    s=re.sub(r'(<meta name="twitter:title" content=")[^"]*', lambda m: m.group(1)+esc(full).replace('&#x27;',"'"), s, 1)
    for k in ('name="description"','property="og:description"','name="twitter:description"'):
        s=re.sub(r'(<meta '+re.escape(k)+r' content=")[^"]*', lambda m: m.group(1)+esc(desc).replace('&#x27;',"'"), s, 1)
    # JSON-LD : remplace l'ancienne description exacte
    s=s.replace(json.dumps(old_d, ensure_ascii=False)[1:-1], json.dumps(desc, ensure_ascii=False)[1:-1])
    open(f,'w').write(s)
    return old_t, old_d

def add_faq(root, path, q, a, lang='fr', after_first=True):
    """Ajoute une question à la FAQ visible et au JSON-LD FAQPage (après la 1re question)."""
    f=f'{root}/{path}/index.html'; s=open(f).read()
    if lang=='fr': q,a=fr_typo(q),fr_typo(a)
    if q in s: return False
    det=f'<details><summary>{q}</summary><p>{a}</p></details>'
    i=s.index('<div class="faq">')+len('<div class="faq">')
    if after_first: i=s.index('</details>',i)+len('</details>')
    s=s[:i]+det+s[i:]
    j=s.index('"@type": "FAQPage", "mainEntity": [')+len('"@type": "FAQPage", "mainEntity": [')
    item=json.dumps({"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}},ensure_ascii=False)
    if after_first:
        # fin du premier objet Question : chercher '}}, ' après j
        k=s.index('}}, {"@type": "Question"',j)+3
        s=s[:k]+item+', '+s[k:]
    else:
        s=s[:j]+item+', '+s[j:]
    open(f,'w').write(s); return True
