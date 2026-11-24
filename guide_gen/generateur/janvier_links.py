import re
R={'fr':'/home/claude/clicandsite-guide/','en':'/home/claude/clicandsite-guide-en/'}; NB=' '
card={'fr':('idees/ou-partir-en-janvier-2027','Où partir en janvier 2027','Ski au calme, Monaco, soleil et expositions.'),
      'en':('ideas/where-to-go-in-france-in-january-2027','Where to go in January 2027','Quiet skiing, Monaco, sunshine and exhibitions.')}
for l,root in R.items():
    p,name,txt=card[l]; idx=root+p.split('/')[0]+'/index.html'; s=open(idx).read()
    if f'../{p}/' not in s:
        t=re.sub(r' ([:?!])',NB+r'\1',txt) if l=='fr' else txt
        c=f'<li class="card card--encre card--idea">\n  <a href="../{p}/">\n    <div class="card__face"><picture><source type="image/webp" srcset="../assets/photos/alpe-d-huez-640.webp"><img class="card__img" src="../assets/photos/alpe-d-huez-640.jpg" alt="" loading="lazy" decoding="async"></picture><div class="card__shade" aria-hidden="true"></div><span class="card__name">{name}</span></div>\n    <p class="card__txt">{t}</p>\n  </a>\n</li>'
        i=s.index('<ul class="cards">')+len('<ul class="cards">'); s=s[:i]+c+s[i:]; open(idx,'w').write(s)
    sm=root+'sitemap.xml'; s=open(sm).read(); dom='https://clicandsite.fr/' if l=='fr' else 'https://clicandsite.com/'
    if p not in s: s=s.replace('</urlset>',f'  <url><loc>{dom}{p}/</loc><lastmod>2026-11-24</lastmod></url>\n</urlset>'); open(sm,'w').write(s)
IN={'fr':[('idees/vacances-de-noel-2026','../ou-partir-en-janvier-2027/','Et après les fêtes ? Voir <a href="{u}">où partir en janvier 2027</a>.'),
          ('idees/vacances-de-fevrier-2027','../ou-partir-en-janvier-2027/','Pour skier avant les vacances, voir <a href="{u}">où partir en janvier 2027</a>.'),
          ('cote-d-azur/rallye-monte-carlo','../../idees/ou-partir-en-janvier-2027/','Les autres rendez-vous du mois : voir <a href="{u}">où partir en janvier 2027</a>.'),
          ('idees/ou-partir-en-hiver','../ou-partir-en-janvier-2027/','Mois par mois : voir aussi <a href="{u}">où partir en janvier 2027</a>.')],
    'en':[('ideas/christmas-holidays-2026','../where-to-go-in-france-in-january-2027/','And after the holidays? See <a href="{u}">where to go in France in January 2027</a>.'),
          ('ideas/february-school-holidays-2027','../where-to-go-in-france-in-january-2027/','To ski before the holidays, see <a href="{u}">where to go in France in January 2027</a>.'),
          ('french-riviera/monte-carlo-rally','../../ideas/where-to-go-in-france-in-january-2027/','The month’s other events: see <a href="{u}">where to go in France in January 2027</a>.'),
          ('ideas/where-to-go-in-winter','../where-to-go-in-france-in-january-2027/','Month by month: see also <a href="{u}">where to go in France in January 2027</a>.')]}
for l,lst in IN.items():
    for p,u,t in lst:
        f=R[l]+p+'/index.html'; s=open(f).read()
        if 'ou-partir-en-janvier-2027' in s or 'where-to-go-in-france-in-january-2027' in s: continue
        t=t.format(u=u)
        if l=='fr': t=re.sub(r' ([:?!])',NB+r'\1',t)
        m=re.search(r'<h2>(Questions fréquentes|Frequently asked questions|FAQ)</h2>',s)
        s=s[:m.start()]+f'<p>{t}</p>\n'+s[m.start():]; open(f,'w').write(s); print('ok',p)
