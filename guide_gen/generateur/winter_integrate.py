import re,os,datetime
D='2026-11-16'
IDEA=[('prix-forfaits-ski-2026-2027','ski-pass-prices-2026-2027','courchevel','Prix des forfaits de ski 2026-2027','Ski pass prices 2026-2027','De 44 € à 84,20 € la journée : le comparatif de 24 stations des Alpes et des Pyrénées.','From €44 to €84.20 a day: 24 resorts in the Alps and the Pyrenees compared.'),
 ('marches-de-noel-alsace','alsace-christmas-markets','strasbourg','Marchés de Noël en Alsace 2026','Alsace Christmas markets 2026','Strasbourg, Colmar, Riquewihr et Kaysersberg : les dates 2026 et un itinéraire en deux jours.','Strasbourg, Colmar, Riquewihr and Kaysersberg: the 2026 dates and a two-day itinerary.'),
 ('reveillon-nouvel-an','new-years-eve-france','champs-elysees','Réveillon du Nouvel An 2026','New Year’s Eve 2026','Le feu d’artifice des Champs-Élysées, les dîners sur la Seine et les soirées de la Côte d’Azur.','The Champs-Élysées fireworks, Seine dinner cruises and parties on the French Riviera.'),
 ('vacances-de-fevrier-2027','february-school-holidays-2027','les-arcs','Vacances de février 2027','February holidays 2027','Les dates des zones A, B et C, la semaine la plus chargée et où partir.','The dates for zones A, B and C, the busiest week and where to go.')]
REG=[('rallye-monte-carlo','monte-carlo-rally','monaco','Monaco','Rallye Monte-Carlo 2027','Monte-Carlo Rally 2027','La 95e édition du 21 au 24 janvier 2027, arrivée sur le port Hercule.','The 95th edition from 21 to 24 January 2027, finishing on Port Hercule.','encre'),
 ('route-du-mimosa','mimosa-route','mandelieu-la-napoule','Mandelieu','Route du Mimosa et Fête du Mimosa 2027','Mimosa Route and Mimosa Festival 2027','130 km de Bormes à Grasse ; la fête de Mandelieu du 10 au 14 février 2027.','130 km from Bormes to Grasse; the Mandelieu festival from 10 to 14 February 2027.','ocre')]
CSS='\n.tbl{overflow-x:auto;margin:1rem 0 1.5rem}.tbl table{width:100%;border-collapse:collapse;font-size:.95rem}.tbl th,.tbl td{text-align:left;padding:.55rem .6rem;border-bottom:1px solid rgba(19,50,75,.12);vertical-align:top}.tbl thead th{background:var(--encre);color:#fff;font-weight:600}.tbl tbody tr:nth-child(even){background:rgba(224,162,67,.08)}.tbl__s{display:block;font-size:.8rem;opacity:.7}\n'
for lang,root,dom,idx,reg,regname in (('fr','clicandsite-guide','https://clicandsite.fr','idees','cote-d-azur','Côte d’Azur'),('en','clicandsite-guide-en','https://clicandsite.com','ideas','french-riviera','French Riviera')):
    i=0 if lang=='fr' else 1
    f=f'{root}/{idx}/index.html'; s=open(f).read()
    for it in IDEA:
        slug=it[i]
        if f'/{idx}/{slug}/' in s: continue
        card=f'<li class="card card--encre card--idea">\n  <a href="../{idx}/{slug}/">\n    <div class="card__face"><picture><source type="image/webp" srcset="../assets/photos/{it[2]}-640.webp"><img class="card__img" src="../assets/photos/{it[2]}-640.jpg" alt="" loading="lazy" decoding="async"></picture><div class="card__shade" aria-hidden="true"></div><span class="card__name">{it[3+i]}</span></div>\n    <p class="card__txt">{it[5+i]}</p>\n  </a>\n</li>'
        k=s.index('</ul></section>', s.index('card--idea')); s=s[:k]+card+s[k:]
    open(f,'w').write(s)
    f=f'{root}/{reg}/index.html'; s=open(f).read()
    anchor='carnaval-de-nice/' if lang=='fr' else 'nice-carnival/'
    for it in REG:
        slug=it[i]
        if f'/{reg}/{slug}/' in s: continue
        card=f'<li class="card card--{it[8]}">\n  <a href="../{reg}/{slug}/">\n    <div class="card__face"><picture><source type="image/webp" srcset="../assets/photos/{it[2]}-640.webp"><img class="card__img" src="../assets/photos/{it[2]}-640.jpg" alt="" loading="lazy" decoding="async"></picture><div class="card__shade" aria-hidden="true"></div><div class="stamp stamp--sm" aria-hidden="true"><span class="stamp__num">06</span></div><div class="postmark postmark--sm" aria-hidden="true"><span>{it[3]}</span></div><span class="card__name">{it[4+i]}</span></div>\n    <p class="card__txt">{it[6+i]}</p>\n  </a>\n</li>'
        a=s.index(f'<a href="../{reg}/{anchor}"'); k=s.index('</li>',a)+5; s=s[:k]+card+s[k:]
        # ld includesAttraction
        s=s.replace('"includesAttraction": [', f'"includesAttraction": [{{"@type": "TouristAttraction", "name": "{it[4+i]}", "url": "{dom}/{reg}/{slug}/"}}, ',1)
    open(f,'w').write(s)
    f=f'{root}/sitemap.xml'; s=open(f).read()
    for p in [f'{idx}/{it[i]}' for it in IDEA]+[f'{reg}/{it[i]}' for it in REG]:
        if f'{dom}/{p}/<' not in s: s=s.replace('</urlset>',f'  <url><loc>{dom}/{p}/</loc><lastmod>{D}</lastmod></url>\n</urlset>')
    open(f,'w').write(s)
    c=f'{root}/assets/style.css'; cs=open(c).read()
    if '.tbl{' not in cs: open(c,'a').write(CSS)
print('ok')
