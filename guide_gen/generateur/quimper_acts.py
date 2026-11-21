import re
R='/home/claude/'
TICK='<svg class="bk__i" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 8a2 2 0 0 0 2-2h14a2 2 0 0 0 2 2v2a2 2 0 0 0 0 4v2a2 2 0 0 0-2 2H5a2 2 0 0 0-2-2v-2a2 2 0 0 0 0-4z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M14 7v10" stroke="currentColor" stroke-width="2" stroke-dasharray="2 2"/></svg>'
for lang,root,src,dst,camp in (('fr','clicandsite-guide','bretagne/concarneau','bretagne/quimper','clicandsite-fr-bretagne-quimper'),('en','clicandsite-guide-en','brittany/concarneau','brittany/quimper','clicandsite-en-brittany-quimper')):
    s=open(f'{R}{root}/{src}/index.html').read()
    i=s.index('<section class="book"'); j=s.index('</section>',i)+len('</section>')
    book=s[i:j]
    oldcamp=re.search(r'data-gyg-cmp="([^"]+)"',book).group(1)
    book=book.replace(oldcamp,camp)
    book=re.sub(r'data-gyg-tour-ids="[^"]*"','data-gyg-tour-ids="606317,677349"',book)
    book=re.sub(r'(class="book__t">)[^<]*',r'\1'+('Activités à réserver autour de Quimper' if lang=='fr' else 'Activities to book around Quimper'),book)
    gyg='getyourguide.fr' if lang=='fr' else 'getyourguide.com'
    vloc='fr-FR' if lang=='fr' else 'en-GB'
    vm=re.search(r'href="(https://www\.viator\.com/[^"]+)"',book).group(1)
    acts=[ (('Activités autour de Quimper','Surf à la pointe de la Torche et sorties en mer en Cornouaille.') if lang=='fr' else ('Activities around Quimper','Surfing at the Pointe de la Torche and boat trips in Cornouaille.'),
            f'https://www.{gyg}/quimper-l99276/?partner_id=XMYSXGR&amp;cmp={camp}&amp;utm_medium=online_publisher'),
           (('Croisière aux îles des Glénan','Une journée en mer au départ de Concarneau, à une demi-heure de Quimper.') if lang=='fr' else ('Glénan islands cruise','A day at sea from Concarneau, half an hour from Quimper.'),
            f'https://www.{gyg}/concarneau-l101238/bretagne-journee-de-croisiere-dans-l-archipel-des-glenan-t606317/?partner_id=XMYSXGR&amp;cmp={camp}&amp;utm_medium=online_publisher')]
    b1,b2=('Billets','Autres billets') if lang=='fr' else (None,None)
    m=re.search(r'<a class="bk bk--gyg"[^>]*>(?:<svg.*?</svg>)?([^<]*)</a><a class="bk bk--via"[^>]*>([^<]*)</a>',book,re.S)
    b1,b2=m.group(1),m.group(2)
    lis=''.join(f'<li class="act">\n  <h3 class="act__t">{t}</h3><p class="act__d">{d}</p>\n  <p class="act__btns"><a class="bk bk--gyg" href="{g}" rel="sponsored nofollow noopener" target="_blank">{TICK}{b1}</a><a class="bk bk--via" href="{vm}" rel="sponsored nofollow noopener" target="_blank">{b2}</a></p>\n</li>' for (t,d),g in acts)
    book=re.sub(r'<ul class="acts">.*?</ul>','<ul class="acts">'+lis+'</ul>',book,flags=re.S)
    p=f'{R}{root}/{dst}/index.html'; q=open(p).read()
    assert 'class="book"' not in q
    anchor='<h2>Questions fréquentes</h2>' if lang=='fr' else '<h2>Frequently asked questions</h2>'
    assert anchor in q, p
    q=q.replace('    '+anchor, '    '+book+'\n    '+anchor,1) if '    '+anchor in q else q.replace(anchor,book+'\n'+anchor,1)
    open(p,'w').write(q); print('ok',p, vm[:70])
