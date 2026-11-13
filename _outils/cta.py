# Ajoute (idempotent) : encadré « À réserver » après l'intro, liens d'action stylés, barre collante mobile.
import re,glob,sys,html
T={'fr':dict(k='À réserver',d='Annulation gratuite sur la plupart des activités · Prix affichés avant de payer',b='Billets',v='ou autres billets',bar='Activités à réserver',barb='Billets'),
   'en':dict(k='Book ahead',d='Free cancellation on most activities · Prices shown before you pay',b='Tickets',v='or more tickets',bar='Things to book',barb='Tickets')}
ARROW='<svg class="cta-arr" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
STAR='<svg class="cta-box__i" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" fill="currentColor"/></svg>'
for root,lang in [('/home/claude/clicandsite-guide','fr'),('/home/claude/clicandsite-guide-en','en')]:
    t=T[lang];n=0
    for f in glob.glob(root+'/*/*/index.html'):
        h=open(f).read();o=h
        b=h.find('id="reserver"');a=h.find('<article class="prose">')
        if b<0 or a<0: continue
        m=re.search(r'<li class="act">\s*<h3 class="act__t">([^<]*)</h3>.*?<a class="bk bk--gyg" href="([^"]+)"',h[b:],re.S)
        if not m: continue
        title,gyg=m.group(1),m.group(2)
        via=re.search(r'<a class="bk bk--via" href="([^"]+)"',h[b:])
        # 1. encadré après l'intro
        if 'class="cta-box"' not in h:
            p=h.find('<h2',a)
            if 0<p<b:
                vl=f'<a class="cta-box__v" href="{via.group(1)}" rel="sponsored nofollow noopener" target="_blank">{t["v"]}</a>' if via else ''
                box=(f'<aside class="cta-box"><p class="cta-box__k">{STAR}{t["k"]}</p><p class="cta-box__t">{title}</p>'
                     f'<p class="cta-box__d">{t["d"]}</p><p class="cta-box__a"><a class="bk bk--gyg cta-box__b" href="{gyg}" rel="sponsored nofollow noopener" target="_blank">{t["b"]}{ARROW}</a>{vl}</p></aside>\n    ')
                h=h[:p]+box+h[p:]
        # 2. liens d'action dans le texte
        b=h.find('id="reserver"')
        seg=h[a:b]
        seg2=re.sub(r'<a href="(https://www\.(?:getyourguide|viator)[^"]+)" rel="sponsored nofollow noopener" target="_blank">([^<]+)</a>\.?',
                    lambda m:f'<a class="deep" href="{m.group(1)}" rel="sponsored nofollow noopener" target="_blank">{m.group(2)}{ARROW}</a>',seg)
        h=h[:a]+seg2+h[b:]
        # 3. barre collante mobile
        if 'class="cta-bar"' not in h:
            bar=(f'<div class="cta-bar" id="cta-bar" hidden><a href="{gyg}" rel="sponsored nofollow noopener" target="_blank">'
                 f'<span class="cta-bar__t">{t["bar"]}</span><span class="cta-bar__b">{t["barb"]}{ARROW}</span></a></div>\n'
                 '<script src="/assets/cta.js?v=1" defer></script>\n')
            h=h.replace('<script src="/assets/stats.js',bar+'<script src="/assets/stats.js',1)
        if h!=o: open(f,'w').write(h);n+=1
    print(lang,n)
