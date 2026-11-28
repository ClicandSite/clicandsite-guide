FR='/home/claude/clicandsite-guide/'; EN='/home/claude/clicandsite-guide-en/'
def tbl(head,rows):
    return '<div class="tbl"><table><thead><tr>'+''.join(f'<th>{h}</th>' for h in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)+'</tbody></table></div>'
def a(h,t): return f'<a href="{h}">{t}</a>'
def put(root,path,html_):
    f=root+path+'/index.html'; s=open(f).read()
    if 'id="agenda-hiver"' in s: return print('déjà')
    i=s.index('<section class="wrap"><ul class="cards">'); j=s.index('</ul></section>',i)+len('</ul></section>')
    s=s[:j]+'\n<section class="wrap prose" aria-labelledby="agenda-hiver">'+html_+'</section>'+s[j:]; open(f,'w').write(s); print('ok',path)
put(FR,'idees','<h2 id="agenda-hiver">L’hiver 2026-2027 en un coup d’œil</h2>'+tbl(['Quand','Quoi','Où'],[
 ['Depuis le 21 novembre',a('stations-de-ski-ouvertes/','Premières stations de ski ouvertes'),'Val Thorens, Tignes'],
 ['Du 27 novembre au 24 décembre',a('marches-de-noel-france/','Marchés de Noël'),'Strasbourg, Colmar, Paris, Côte d’Azur'],
 ['Du 19 décembre au 4 janvier',a('vacances-de-noel-2026/','Vacances de Noël'),'Toutes les zones'],
 ['31 décembre',a('reveillon-nouvel-an/','Réveillon et feu d’artifice'),'Champs-Élysées, Seine, Riviera'],
 ['Du 21 au 24 janvier',a('../cote-d-azur/rallye-monte-carlo/','Rallye Monte-Carlo'),'Monaco, col de Turini'],
 ['Du 6 février au 8 mars',a('vacances-de-fevrier-2027/','Vacances d’hiver (zones C, A puis B)'),'Stations de ski, Riviera'],
 ['Du 7 au 21 février',a('../cote-d-azur/route-du-mimosa/','Route du Mimosa'),'Sainte-Maxime, Mandelieu, Bormes'],
 ['Du 9 au 28 février',a('../cote-d-azur/carnaval-de-nice/','Carnaval de Nice'),'Nice'],
 ['Du 13 au 28 février',a('../cote-d-azur/fete-du-citron-menton/','Fête du Citron'),'Menton'],
 ['Dimanche 14 février',a('saint-valentin-2027/','Saint-Valentin'),'Week-ends à deux']])+
 '<p>Chaque ligne renvoie au guide complet, avec les dates vérifiées sur les sites officiels, les prix et l’accès. Les stations de ski et les grands événements publient parfois leurs horaires détaillés quelques semaines seulement avant : nos pages sont mises à jour au fur et à mesure.</p>')
put(EN,'ideas','<h2 id="agenda-hiver">Winter 2026-2027 at a glance</h2>'+tbl(['When','What','Where'],[
 ['Since 21 November',a('ski-resort-opening-dates/','First ski resorts open'),'Val Thorens, Tignes'],
 ['27 November to 24 December',a('christmas-markets-france/','Christmas markets'),'Strasbourg, Colmar, Paris, French Riviera'],
 ['19 December to 4 January',a('christmas-holidays-2026/','Christmas school holidays'),'All zones'],
 ['31 December',a('new-years-eve-france/','New Year’s Eve and fireworks'),'Champs-Élysées, Seine, Riviera'],
 ['21 to 24 January',a('../french-riviera/monte-carlo-rally/','Monte-Carlo Rally'),'Monaco, Col de Turini'],
 ['6 February to 8 March',a('february-school-holidays-2027/','Winter school holidays (zones C, A then B)'),'Ski resorts, Riviera'],
 ['7 to 21 February','Mimosa Route','Sainte-Maxime, Mandelieu, Bormes'],
 ['9 to 28 February','Nice Carnival','Nice'],
 ['13 to 28 February','Lemon Festival','Menton'],
 ['Sunday 14 February',a('valentines-day-2027/','Valentine’s Day'),'Weekends for two']])+
 '<p>Each line links to the full guide, with dates checked on official websites, prices and access. Ski resorts and big events sometimes publish detailed times only a few weeks ahead: our pages are updated as they do.</p>')
