import re,os
R={'fr':'/home/claude/clicandsite-guide/','en':'/home/claude/clicandsite-guide-en/'}
NB=' '
card={'fr':('idees/marches-de-noel-france','Marchés de Noël en France 2026','Alsace, Paris, Côte d’Azur : toutes les dates 2026.','idees/saint-valentin-2027'),
      'en':('ideas/christmas-markets-france','Christmas markets in France 2026','Alsace, Paris, French Riviera: all the 2026 dates.','ideas/valentines-day-2027')}
for l,root in R.items():
    p,name,txt,after=card[l]; idx=root+p.split('/')[0]+'/index.html'; s=open(idx).read()
    if f'../{p}/' not in s:
        c=f'<li class="card card--encre card--idea">\n  <a href="../{p}/">\n    <div class="card__face"><picture><source type="image/webp" srcset="../assets/photos/noel-a-paris-640.webp"><img class="card__img" src="../assets/photos/noel-a-paris-640.jpg" alt="" loading="lazy" decoding="async"></picture><div class="card__shade" aria-hidden="true"></div><span class="card__name">{name}</span></div>\n    <p class="card__txt">{txt.replace(" :", NB+":") if l=="fr" else txt}</p>\n  </a>\n</li>'
        # en tête de liste (saison)
        i=s.index('<ul class="cards">')+len('<ul class="cards">'); s=s[:i]+c+s[i:]; open(idx,'w').write(s)
    sm=root+'sitemap.xml'; s=open(sm).read(); dom='https://clicandsite.fr/' if l=='fr' else 'https://clicandsite.com/'
    if p not in s: s=s.replace('</urlset>',f'  <url><loc>{dom}{p}/</loc><lastmod>2026-11-20</lastmod></url>\n</urlset>'); open(sm,'w').write(s)
IN={'fr':[('idees/marches-de-noel-alsace','../marches-de-noel-france/','Envie de comparer avec Paris ou la Côte d’Azur ? Voir notre <a href="{u}">calendrier des marchés de Noël en France 2026</a>.'),
          ('paris/noel-a-paris','../../idees/marches-de-noel-france/','Toutes les dates des marchés de Noël 2026, de l’Alsace à la Côte d’Azur : voir notre <a href="{u}">calendrier des marchés de Noël en France</a>.'),
          ('cote-d-azur/noel-cote-d-azur','../../idees/marches-de-noel-france/','Toutes les dates des marchés de Noël 2026, de l’Alsace à Paris : voir notre <a href="{u}">calendrier des marchés de Noël en France</a>.'),
          ('idees/ou-partir-en-hiver','../marches-de-noel-france/','Toutes les dates d’ouverture : voir notre <a href="{u}">calendrier des marchés de Noël en France 2026</a>.')],
    'en':[('ideas/alsace-christmas-markets','../christmas-markets-france/','Want to compare with Paris or the French Riviera? See our <a href="{u}">2026 calendar of Christmas markets in France</a>.'),
          ('paris/christmas-in-paris','../../ideas/christmas-markets-france/','All the 2026 Christmas market dates, from Alsace to the Riviera: see our <a href="{u}">Christmas markets in France calendar</a>.'),
          ('french-riviera/christmas-french-riviera','../../ideas/christmas-markets-france/','All the 2026 Christmas market dates, from Alsace to Paris: see our <a href="{u}">Christmas markets in France calendar</a>.'),
          ('ideas/where-to-go-in-winter','../christmas-markets-france/','All the opening dates: see our <a href="{u}">2026 calendar of Christmas markets in France</a>.')]}
for l,lst in IN.items():
    for p,u,t in lst:
        f=R[l]+p+'/index.html'; s=open(f).read()
        if 'marches-de-noel-france' in s or 'christmas-markets-france' in s: continue
        t=t.format(u=u)
        if l=='fr': t=re.sub(r' ([:?!])',NB+r'\1',t)
        m=re.search(r'<h2>(Questions fréquentes|Frequently asked questions|FAQ)</h2>',s)
        if not m: print('pas de FAQ',f); continue
        s=s[:m.start()]+f'<p>{t}</p>\n'+s[m.start():]; open(f,'w').write(s); print('ok',p)
