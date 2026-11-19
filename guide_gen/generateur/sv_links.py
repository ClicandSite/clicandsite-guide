import re
R={'fr':'/home/claude/clicandsite-guide/','en':'/home/claude/clicandsite-guide-en/'}
card={'fr':('idees/saint-valentin-2027','Saint-Valentin 2027','Le 14 février tombe un dimanche : nos idées de week-end à deux.','idees/ou-partir-en-france-en-2027'),
      'en':('ideas/valentines-day-2027','Valentine’s Day 2027','14 February falls on a Sunday: our ideas for a weekend for two.','ideas/where-to-go-in-france-in-2027')}
for l,root in R.items():
    p,name,txt,after=card[l]; idx=root+p.split('/')[0]+'/index.html'; s=open(idx).read()
    if p not in s:
        c=f'<li class="card card--encre card--idea">\n  <a href="../{p}/">\n    <div class="card__face"><picture><source type="image/webp" srcset="../assets/photos/croisiere-sur-la-seine-640.webp"><img class="card__img" src="../assets/photos/croisiere-sur-la-seine-640.jpg" alt="" loading="lazy" decoding="async"></picture><div class="card__shade" aria-hidden="true"></div><span class="card__name">{name}</span></div>\n    <p class="card__txt">{txt}</p>\n  </a>\n</li>'
        i=s.index(f'<a href="../{after}/">'); j=s.index('</li>',i)+5; s=s[:j]+c+s[j:]; open(idx,'w').write(s)
    sm=root+'sitemap.xml'; s=open(sm).read(); dom='https://clicandsite.fr/' if l=='fr' else 'https://clicandsite.com/'
    if p not in s:
        s=s.replace('</urlset>',f'  <url><loc>{dom}{p}/</loc><lastmod>2026-11-19</lastmod></url>\n</urlset>'); open(sm,'w').write(s)
# liens entrants
IN={'fr':[('idees/vacances-de-fevrier-2027','Pour un week-end à deux le 13 et 14 février, voir aussi nos <a href="../saint-valentin-2027/">idées pour la Saint-Valentin 2027</a>.'),
          ('paris/croisiere-sur-la-seine','Un dîner croisière pour le 14 février ? Voir nos <a href="../../idees/saint-valentin-2027/">idées de week-end pour la Saint-Valentin 2027</a>.'),
          ('cote-d-azur/eze','Èze fait partie de nos <a href="../../idees/saint-valentin-2027/">idées de week-end en amoureux pour la Saint-Valentin 2027</a>.')],
    'en':[('ideas/february-half-term-2027',None),
          ('paris/seine-cruise','A dinner cruise for 14 February? See our <a href="../../ideas/valentines-day-2027/">romantic weekend ideas for Valentine’s Day 2027</a>.'),
          ('french-riviera/eze','Èze is one of our <a href="../../ideas/valentines-day-2027/">romantic weekend ideas for Valentine’s Day 2027</a>.')]}
import os
for l,lst in IN.items():
    for p,t in lst:
        f=R[l]+p+'/index.html'
        if not os.path.exists(f): print('absent',f); continue
        s=open(f).read()
        if 'saint-valentin-2027' in s or 'valentines-day-2027' in s: continue
        if t is None: continue
        m=re.search(r'<h2>(Questions fréquentes|Frequently asked questions|FAQ)</h2>',s)
        if not m: print('pas de FAQ',f); continue
        if l=='fr': t=t.replace(' ?',' ?')
        s=s[:m.start()]+f'<p>{t}</p>\n'+s[m.start():]; open(f,'w').write(s); print('ok',f)
