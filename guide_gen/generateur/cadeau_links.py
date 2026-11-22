import re
R={'fr':'/home/claude/clicandsite-guide/','en':'/home/claude/clicandsite-guide-en/'}; NB=' '
card={'fr':('idees/cadeau-de-noel-experience','Cadeau de Noël : offrir une sortie','Croisière, cabaret, Versailles, montagne : nos idées.'),
      'en':('ideas/christmas-experience-gifts-france','Experience gifts for Christmas','Cruise, cabaret, Versailles, mountains: our ideas.')}
for l,root in R.items():
    p,name,txt=card[l]; idx=root+p.split('/')[0]+'/index.html'; s=open(idx).read()
    if f'../{p}/' not in s:
        t=re.sub(r' ([:?!])',NB+r'\1',txt) if l=='fr' else txt
        c=f'<li class="card card--encre card--idea">\n  <a href="../{p}/">\n    <div class="card__face"><picture><source type="image/webp" srcset="../assets/photos/versailles-640.webp"><img class="card__img" src="../assets/photos/versailles-640.jpg" alt="" loading="lazy" decoding="async"></picture><div class="card__shade" aria-hidden="true"></div><span class="card__name">{name}</span></div>\n    <p class="card__txt">{t}</p>\n  </a>\n</li>'
        i=s.index('<ul class="cards">')+len('<ul class="cards">'); s=s[:i]+c+s[i:]; open(idx,'w').write(s)
    sm=root+'sitemap.xml'; s=open(sm).read(); dom='https://clicandsite.fr/' if l=='fr' else 'https://clicandsite.com/'
    if p not in s: s=s.replace('</urlset>',f'  <url><loc>{dom}{p}/</loc><lastmod>2026-11-22</lastmod></url>\n</urlset>'); open(sm,'w').write(s)
IN={'fr':[('idees/vacances-de-noel-2026','../cadeau-de-noel-experience/','Envie d’offrir une sortie pour les fêtes ? Voir nos <a href="{u}">idées de cadeaux d’expérience pour Noël</a>.'),
          ('idees/marches-de-noel-france','../cadeau-de-noel-experience/','Pour un cadeau à vivre plutôt qu’à déballer, voir nos <a href="{u}">idées de sorties à offrir à Noël</a>.'),
          ('paris/noel-a-paris','../../idees/cadeau-de-noel-experience/','Dîner sur la Seine, cabaret ou Versailles : voir nos <a href="{u}">idées de cadeaux d’expérience pour Noël 2026</a>.'),
          ('idees/saint-valentin-2027','../cadeau-de-noel-experience/','Un week-end à deux peut aussi s’offrir à Noël : voir nos <a href="{u}">idées de cadeaux d’expérience</a>.')],
    'en':[('ideas/christmas-holidays-2026','../christmas-experience-gifts-france/','Want to give an outing for the holidays? See our <a href="{u}">experience gift ideas for Christmas</a>.'),
          ('ideas/christmas-markets-france','../christmas-experience-gifts-france/','For a gift to live rather than unwrap, see our <a href="{u}">ideas for outings to give at Christmas</a>.'),
          ('paris/christmas-in-paris','../../ideas/christmas-experience-gifts-france/','Seine dinner, cabaret or Versailles: see our <a href="{u}">experience gift ideas for Christmas 2026</a>.'),
          ('ideas/valentines-day-2027','../christmas-experience-gifts-france/','A weekend for two can also be a Christmas gift: see our <a href="{u}">experience gift ideas</a>.')]}
for l,lst in IN.items():
    for p,u,t in lst:
        f=R[l]+p+'/index.html'; s=open(f).read()
        if 'cadeau-de-noel-experience' in s or 'christmas-experience-gifts-france' in s: continue
        t=t.format(u=u)
        if l=='fr': t=re.sub(r' ([:?!])',NB+r'\1',t)
        m=re.search(r'<h2>(Questions fréquentes|Frequently asked questions|FAQ)</h2>',s)
        s=s[:m.start()]+f'<p>{t}</p>\n'+s[m.start():]; open(f,'w').write(s); print('ok',p)
