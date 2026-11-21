import re
R={'fr':'/home/claude/clicandsite-guide/','en':'/home/claude/clicandsite-guide-en/'}; NB=' '
card={'fr':('idees/vacances-de-noel-2026','Vacances de Noël 2026','Du 19 décembre au 4 janvier : ski, marchés, réveillon.'),
      'en':('ideas/christmas-holidays-2026','Christmas holidays 2026','19 December to 4 January: skiing, markets, New Year.')}
for l,root in R.items():
    p,name,txt=card[l]; idx=root+p.split('/')[0]+'/index.html'; s=open(idx).read()
    if f'../{p}/' not in s:
        t=re.sub(r' ([:?!])',NB+r'\1',txt) if l=='fr' else txt
        c=f'<li class="card card--encre card--idea">\n  <a href="../{p}/">\n    <div class="card__face"><picture><source type="image/webp" srcset="../assets/photos/megeve-640.webp"><img class="card__img" src="../assets/photos/megeve-640.jpg" alt="" loading="lazy" decoding="async"></picture><div class="card__shade" aria-hidden="true"></div><span class="card__name">{name}</span></div>\n    <p class="card__txt">{t}</p>\n  </a>\n</li>'
        i=s.index('<ul class="cards">')+len('<ul class="cards">'); s=s[:i]+c+s[i:]; open(idx,'w').write(s)
    sm=root+'sitemap.xml'; s=open(sm).read(); dom='https://clicandsite.fr/' if l=='fr' else 'https://clicandsite.com/'
    if p not in s: s=s.replace('</urlset>',f'  <url><loc>{dom}{p}/</loc><lastmod>2026-11-21</lastmod></url>\n</urlset>'); open(sm,'w').write(s)
IN={'fr':[('idees/stations-de-ski-ouvertes','../vacances-de-noel-2026/','Vous partez pendant les fêtes ? Voir notre <a href="{u}">calendrier des vacances de Noël 2026</a>.'),
          ('idees/marches-de-noel-france','../vacances-de-noel-2026/','Quels marchés restent ouverts pendant les vacances scolaires ? Voir notre <a href="{u}">calendrier des vacances de Noël 2026</a>.'),
          ('idees/reveillon-nouvel-an','../vacances-de-noel-2026/','Pour organiser toutes les fêtes, voir notre <a href="{u}">calendrier des vacances de Noël 2026</a>.'),
          ('idees/ou-partir-en-hiver','../vacances-de-noel-2026/','Pour les fêtes de fin d’année, voir notre <a href="{u}">guide des vacances de Noël 2026</a>.')],
    'en':[('ideas/ski-resort-opening-dates','../christmas-holidays-2026/','Going over the festive season? See our <a href="{u}">Christmas holidays 2026 calendar</a>.'),
          ('ideas/christmas-markets-france','../christmas-holidays-2026/','Which markets stay open during the school holidays? See our <a href="{u}">Christmas holidays 2026 calendar</a>.'),
          ('ideas/new-years-eve-france','../christmas-holidays-2026/','To plan the whole festive season, see our <a href="{u}">Christmas holidays 2026 calendar</a>.'),
          ('ideas/where-to-go-in-winter','../christmas-holidays-2026/','For the end-of-year holidays, see our <a href="{u}">Christmas holidays 2026 guide</a>.')]}
for l,lst in IN.items():
    for p,u,t in lst:
        f=R[l]+p+'/index.html'; s=open(f).read()
        if 'vacances-de-noel-2026' in s or 'christmas-holidays-2026' in s: continue
        t=t.format(u=u)
        if l=='fr': t=re.sub(r' ([:?!])',NB+r'\1',t)
        m=re.search(r'<h2>(Questions fréquentes|Frequently asked questions|FAQ)</h2>',s)
        s=s[:m.start()]+f'<p>{t}</p>\n'+s[m.start():]; open(f,'w').write(s); print('ok',p)
