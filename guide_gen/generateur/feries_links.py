import re
R={'fr':'/home/claude/clicandsite-guide/','en':'/home/claude/clicandsite-guide-en/'}; NB=' '
card={'fr':('idees/paris-25-decembre-1er-janvier','Paris le 25 décembre et le 1er janvier','Ce qui est ouvert, ce qui est fermé.'),
      'en':('ideas/paris-christmas-day-new-years-day','Paris on 25 December and 1 January','What’s open, what’s closed.')}
for l,root in R.items():
    p,name,txt=card[l]; idx=root+p.split('/')[0]+'/index.html'; s=open(idx).read()
    if f'../{p}/' not in s:
        t=re.sub(r' ([:?!])',NB+r'\1',txt) if l=='fr' else txt
        c=f'<li class="card card--encre card--idea">\n  <a href="../{p}/">\n    <div class="card__face"><picture><source type="image/webp" srcset="../assets/photos/noel-a-paris-640.webp"><img class="card__img" src="../assets/photos/noel-a-paris-640.jpg" alt="" loading="lazy" decoding="async"></picture><div class="card__shade" aria-hidden="true"></div><span class="card__name">{name}</span></div>\n    <p class="card__txt">{t}</p>\n  </a>\n</li>'
        i=s.index('<ul class="cards">')+len('<ul class="cards">'); s=s[:i]+c+s[i:]; open(idx,'w').write(s)
    sm=root+'sitemap.xml'; s=open(sm).read(); dom='https://clicandsite.fr/' if l=='fr' else 'https://clicandsite.com/'
    if p not in s: s=s.replace('</urlset>',f'  <url><loc>{dom}{p}/</loc><lastmod>2026-11-23</lastmod></url>\n</urlset>'); open(sm,'w').write(s)
IN={'fr':[('paris/noel-a-paris','../../idees/paris-25-decembre-1er-janvier/','Musées ouverts ou fermés le jour de Noël et le Jour de l’An : voir <a href="{u}">Paris le 25 décembre et le 1er janvier</a>.'),
          ('idees/reveillon-nouvel-an','../paris-25-decembre-1er-janvier/','Et le lendemain ? Voir <a href="{u}">ce qui est ouvert à Paris le 1er janvier</a>.'),
          ('idees/vacances-de-noel-2026','../paris-25-decembre-1er-janvier/','À Paris pendant les fêtes, voir <a href="{u}">les musées et monuments ouverts le 25 décembre et le 1er janvier</a>.'),
          ('idees/que-faire-a-paris-en-hiver','../paris-25-decembre-1er-janvier/','Le 25 décembre et le 1er janvier, beaucoup de musées ferment : voir <a href="{u}">ce qui reste ouvert ces jours-là</a>.')],
    'en':[('paris/christmas-in-paris','../../ideas/paris-christmas-day-new-years-day/','Museums open or closed on Christmas Day and New Year’s Day: see <a href="{u}">Paris on 25 December and 1 January</a>.'),
          ('ideas/new-years-eve-france','../paris-christmas-day-new-years-day/','And the day after? See <a href="{u}">what’s open in Paris on 1 January</a>.'),
          ('ideas/christmas-holidays-2026','../paris-christmas-day-new-years-day/','In Paris over the holidays, see <a href="{u}">the museums and monuments open on 25 December and 1 January</a>.'),
          ('ideas/things-to-do-in-paris-in-winter','../paris-christmas-day-new-years-day/','On 25 December and 1 January many museums close: see <a href="{u}">what stays open on those days</a>.')]}
for l,lst in IN.items():
    for p,u,t in lst:
        f=R[l]+p+'/index.html'; s=open(f).read()
        if 'paris-25-decembre-1er-janvier' in s or 'paris-christmas-day-new-years-day' in s: continue
        t=t.format(u=u)
        if l=='fr': t=re.sub(r' ([:?!])',NB+r'\1',t)
        m=re.search(r'<h2>(Questions fréquentes|Frequently asked questions|FAQ)</h2>',s)
        s=s[:m.start()]+f'<p>{t}</p>\n'+s[m.start():]; open(f,'w').write(s); print('ok',p)
