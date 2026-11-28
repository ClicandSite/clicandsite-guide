import re
FR='/home/claude/clicandsite-guide/'; EN='/home/claude/clicandsite-guide-en/'
N=' '
def tbl(head,rows):
    return '<div class="tbl"><table><thead><tr>'+''.join(f'<th>{h}</th>' for h in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)+'</tbody></table></div>'
def ins(root,path,html_):
    f=root+path+'/index.html'; s=open(f).read()
    if 'id="en-bref"' in s: return print('déjà',path)
    i=s.index('<section class="wrap prose">'); j=s.index('</section>',i)+10
    s=s[:j]+'\n\n<section class="wrap prose" aria-labelledby="en-bref">'+html_+'</section>'+s[j:]
    open(f,'w').write(s); print('ok',root[-4:],path)
def a(href,t): return f'<a href="{href}">{t}</a>'
# ---------- PYRÉNÉES
ins(FR,'pyrenees','<h2 id="en-bref">Les stations des Pyrénées en un coup d’œil</h2>'+tbl(['Station','Saison 2026-2027','Forfait journée adulte','Le point fort'],[
 [a('../pyrenees/cauterets/','Cauterets'),'27 nov. – 18 avr.',f'46{N}€','La plus précoce, neige du cirque du Lys'],
 [a('../pyrenees/font-romeu/','Font-Romeu'),'4 déc. – 29 mars',f'49,50{N}€','Soleil de Cerdagne, accès en train jaune'],
 [a('../pyrenees/saint-lary/','Saint-Lary'),'4 déc. – 29 mars',f'54,70{N}€','100 km de pistes et un vrai village'],
 [a('../pyrenees/grand-tourmalet/','Grand Tourmalet'),'5 déc. – 29 mars',f'55{N}€','Le plus grand domaine, Pic du Midi'],
 [a('../pyrenees/peyragudes/','Peyragudes'),'12 déc. – 29 mars',f'51{N}€','Piste 007, télécabine de Loudenvielle']])+
 f'<p>Tarifs adultes 2026-2027 relevés sur les sites officiels des stations ; les forfaits en ligne sont souvent moins chers, surtout hors vacances.</p><h3>Laquelle choisir ?</h3><p>Pour skier le plus tôt possible, Cauterets ouvre dès le 27 novembre et reste ouvert jusqu’au 18 avril. Pour un grand domaine, le Grand Tourmalet relie La Mongie et Barèges au pied du Pic du Midi. Pour dormir dans un village de vallée plutôt qu’en station, Saint-Lary est le meilleur choix. Et pour venir sans voiture, Font-Romeu se rejoint par le train jaune depuis Villefranche-de-Conflent.</p><p>Hors des pistes, {a("../pyrenees/lourdes/","Lourdes")} est la porte d’entrée des Hautes-Pyrénées, et la {a("../pyrenees/cote-vermeille/","Côte Vermeille")}, avec {a("../pyrenees/collioure/","Collioure")}, se visite toute l’année au bord de la Méditerranée.</p>')
ins(EN,'pyrenees','<h2 id="en-bref">Pyrenees ski resorts at a glance</h2>'+tbl(['Resort','2026-2027 season','Adult day pass','Best for'],[
 [a('../pyrenees/cauterets/','Cauterets'),'27 Nov – 18 Apr','€46','Earliest opening, snowy Cirque du Lys'],
 [a('../pyrenees/font-romeu/','Font-Romeu'),'4 Dec – 29 Mar','€49.50','Cerdagne sunshine, Yellow Train access'],
 [a('../pyrenees/saint-lary/','Saint-Lary'),'4 Dec – 29 Mar','€54.70','100 km of runs and a real village'],
 [a('../pyrenees/grand-tourmalet/','Grand Tourmalet'),'5 Dec – 29 Mar','€55','The biggest area, Pic du Midi'],
 [a('../pyrenees/peyragudes/','Peyragudes'),'12 Dec – 29 Mar','€51','The 007 run, Loudenvielle gondola']])+
 f'<p>2026-2027 adult prices taken from the resorts’ official websites; passes bought online are often cheaper, especially outside school holidays.</p><h3>Which one to choose?</h3><p>To ski as early as possible, Cauterets opens on 27 November and stays open until 18 April. For a big area, the Grand Tourmalet links La Mongie and Barèges below the Pic du Midi. To stay in a valley village rather than a purpose-built resort, Saint-Lary is the best pick. And to arrive without a car, Font-Romeu is reached by the Yellow Train from Villefranche-de-Conflent.</p><p>Away from the slopes, {a("../pyrenees/lourdes/","Lourdes")} is the gateway to the Hautes-Pyrénées, and the {a("../pyrenees/cote-vermeille/","Côte Vermeille")} with {a("../pyrenees/collioure/","Collioure")} can be visited all year on the Mediterranean.</p>')
# ---------- LOIRE
ins(FR,'chateaux-de-la-loire','<h2 id="en-bref">Les châteaux de la Loire en un coup d’œil</h2>'+tbl(['Château','Billet adulte 2026','À ne pas manquer'],[
 [a('../chateaux-de-la-loire/chambord/','Chambord'),f'21{N}€ (résidents EEE), 31{N}€ (autres)','L’escalier à double révolution, les terrasses'],
 [a('../chateaux-de-la-loire/chenonceau/','Chenonceau'),f'15{N}€ (19{N}€ avec audioguide)','La galerie au-dessus du Cher'],
 [a('../chateaux-de-la-loire/amboise/','Amboise'),f'17,50{N}€ ; Clos Lucé 20{N}€','La tombe de Léonard de Vinci'],
 [a('../chateaux-de-la-loire/villandry/','Villandry'),f'14{N}€ (jardins seuls 8,50{N}€)','Le potager décoratif'],
 [a('../chateaux-de-la-loire/chaumont-sur-loire/','Chaumont-sur-Loire'),'Selon la saison','Noël « Rêves d’antan » jusqu’au 10 janvier 2027'],
 [a('../chateaux-de-la-loire/cheverny/','Cheverny'),'Selon la formule','Ouvert tous les jours, même le 25 décembre et le 1er janvier'],
 [a('../chateaux-de-la-loire/blois/','Blois'),'Selon la formule','L’escalier de François Ier, le son et lumière']])+
 f'<p>Prix relevés sur les sites officiels pour 2026 ; chaque guide détaille les tarifs réduits et les horaires.</p><h3>Combien de jours prévoir ?</h3><p>En une journée depuis Paris, le plus simple est de choisir un secteur : Amboise et Chenonceau depuis Tours, ou Chambord, Blois et Cheverny autour de Blois. Avec deux ou trois jours, on enchaîne les deux secteurs et on ajoute Villandry. Amboise est à environ 2 h de Paris en train, et la gare de Chenonceaux est à quelques minutes à pied du château ; pour Chambord, il faut une voiture ou la navette depuis Blois.</p>')
ins(EN,'loire-valley','<h2 id="en-bref">The Loire châteaux at a glance</h2>'+tbl(['Château','2026 adult ticket','Don’t miss'],[
 [a('../loire-valley/chambord/','Chambord'),'€21 (EEA residents), €31 (others)','The double-helix staircase, the rooftop terraces'],
 [a('../loire-valley/chenonceau/','Chenonceau'),'€15 (€19 with audio guide)','The gallery spanning the Cher'],
 [a('../loire-valley/amboise/','Amboise'),'€17.50; Clos Lucé €20','Leonardo da Vinci’s tomb'],
 [a('../loire-valley/villandry/','Villandry'),'€14 (gardens only €8.50)','The ornamental kitchen garden'],
 [a('../loire-valley/chaumont-sur-loire/','Chaumont-sur-Loire'),'Depends on season','Christmas “Rêves d’antan” until 10 January 2027'],
 [a('../loire-valley/cheverny/','Cheverny'),'Depends on ticket','Open every day, even 25 December and 1 January'],
 [a('../loire-valley/blois/','Blois'),'Depends on ticket','François I staircase, the sound and light show']])+
 '<p>Prices taken from the official websites for 2026; each guide lists reduced rates and opening hours.</p><h3>How many days?</h3><p>On a day trip from Paris, pick one area: Amboise and Chenonceau from Tours, or Chambord, Blois and Cheverny around Blois. With two or three days you can combine both areas and add Villandry. Amboise is about 2 hours from Paris by train, and Chenonceaux station is a few minutes’ walk from the château; Chambord needs a car or the shuttle from Blois.</p>')
# ---------- PROVENCE
ins(FR,'provence','<h2 id="en-bref">La Provence en un coup d’œil</h2>'+tbl(['Lieu','Depuis Paris','À voir, prix 2026'],[
 [a('../provence/avignon/','Avignon'),'2 h 40 en TGV',f'Palais des Papes, 16{N}€'],
 [a('../provence/aix-en-provence/','Aix-en-Provence'),'3 h en TGV','Cours Mirabeau, atelier de Cézanne'],
 [a('../provence/marseille/','Marseille'),'3 h 15 en TGV','Notre-Dame de la Garde, Vieux-Port, MuCEM'],
 [a('../provence/baux-de-provence/','Les Baux-de-Provence'),'Depuis Avignon ou Arles',f'Carrières des Lumières, 16,50{N}€'],
 [a('../provence/gordes/','Gordes'),'Depuis Avignon',f'Abbaye de Sénanque, 8{N}€'],
 [a('../provence/roussillon/','Roussillon'),'Depuis Avignon',f'Sentier des ocres, 3,50{N}€']])+
 f'<p>Temps de trajet et prix relevés sur les sites officiels ; chaque guide donne les horaires et nos conseils.</p><h3>Où se baser ?</h3><p>Avignon est la meilleure base pour le Luberon ({a("../provence/gordes/","Gordes")}, {a("../provence/roussillon/","Roussillon")}, {a("../provence/isle-sur-la-sorgue/","L’Isle-sur-la-Sorgue")}) et les Alpilles. Marseille et Aix sont mieux placées pour la côte et {a("../provence/calanques/","les calanques")}, et {a("../provence/arles/","Arles")} pour {a("../provence/camargue/","la Camargue")}. En hiver, beaucoup de sites gardent des horaires réduits mais restent ouverts, et la route du sommet du {a("../provence/mont-ventoux/","mont Ventoux")} est fermée jusqu’au printemps.</p>')
ins(EN,'provence','<h2 id="en-bref">Provence at a glance</h2>'+tbl(['Place','From Paris','What to see, 2026 prices'],[
 [a('../provence/avignon/','Avignon'),'2 h 40 by TGV','Palais des Papes, €16'],
 [a('../provence/aix-en-provence/','Aix-en-Provence'),'3 h by TGV','Cours Mirabeau, Cézanne’s studio'],
 [a('../provence/marseille/','Marseille'),'3 h 15 by TGV','Notre-Dame de la Garde, Old Port, MuCEM'],
 [a('../provence/baux-de-provence/','Les Baux-de-Provence'),'From Avignon or Arles','Carrières des Lumières, €16.50'],
 [a('../provence/gordes/','Gordes'),'From Avignon','Sénanque Abbey, €8'],
 [a('../provence/roussillon/','Roussillon'),'From Avignon','Ochre trail, €3.50']])+
 f'<p>Journey times and prices taken from official websites; each guide gives opening hours and our tips.</p><h3>Where to stay?</h3><p>Avignon is the best base for the Luberon ({a("../provence/gordes/","Gordes")}, {a("../provence/roussillon/","Roussillon")}, {a("../provence/isle-sur-la-sorgue/","L’Isle-sur-la-Sorgue")}) and the Alpilles. Marseille and Aix suit the coast and {a("../provence/calanques/","the calanques")}, and {a("../provence/arles/","Arles")} suits {a("../provence/camargue/","the Camargue")}. In winter many sites keep shorter hours but stay open, and the summit road of {a("../provence/mont-ventoux/","Mont Ventoux")} is closed until spring.</p>')
# ---------- ALSACE
ins(FR,'alsace','<h2 id="en-bref">L’Alsace en un coup d’œil</h2>'+tbl(['Lieu','Marché de Noël 2026','À voir aussi'],[
 [a('../alsace/strasbourg/','Strasbourg'),'Dès le 27 novembre, jusqu’au 24 décembre',f'Plateforme de la cathédrale, 10{N}€'],
 [a('../alsace/colmar/','Colmar'),'23 novembre – 29 décembre','Petite Venise, musée Unterlinden'],
 [a('../alsace/riquewihr/','Riquewihr'),'Tous les jours du 27 novembre au 20 décembre',f'Musée du Dolder, 3{N}€'],
 [a('../alsace/kaysersberg/','Kaysersberg'),'Les week-ends de l’Avent, 10 h – 20 h','Centre Schweitzer, château'],
 [a('../alsace/eguisheim/','Eguisheim'),'Pendant l’Avent','Ruelles en cercles, accès libre'],
 [a('../alsace/haut-koenigsbourg/','Haut-Kœnigsbourg'),'Décors du 22 novembre au 3 janvier',f'Château fort, 12{N}€']])+
 f'<p>Dates et prix relevés sur les sites officiels ; chaque guide donne les horaires et l’accès.</p><h3>Comment s’organiser ?</h3><p>Strasbourg est à environ 1 h 50 de Paris en TGV, et Colmar à une trentaine de minutes de Strasbourg en TER. Le plus pratique est de dormir à Colmar et de rayonner vers les villages du vignoble ; évitez si possible les samedis de décembre, les plus chargés. Pour une visite au calme, {a("../alsace/obernai/","Obernai")} a son propre marché de Noël, et {a("../alsace/mulhouse/","Mulhouse")} offre le musée de l’Automobile et la Cité du Train.</p>')
ins(EN,'alsace','<h2 id="en-bref">Alsace at a glance</h2>'+tbl(['Place','Christmas market 2026','Also worth seeing'],[
 [a('../alsace/strasbourg/','Strasbourg'),'From 27 November to 24 December','Cathedral platform, €10'],
 [a('../alsace/colmar/','Colmar'),'23 November – 29 December','Little Venice, Unterlinden museum'],
 [a('../alsace/riquewihr/','Riquewihr'),'Daily from 27 November to 20 December','Dolder museum, €3'],
 [a('../alsace/kaysersberg/','Kaysersberg'),'Advent weekends, 10 am – 8 pm','Schweitzer Centre, castle'],
 [a('../alsace/eguisheim/','Eguisheim'),'During Advent','Circular lanes, free access'],
 [a('../alsace/haut-koenigsbourg/','Haut-Kœnigsbourg'),'Decorations 22 November – 3 January','Castle, €12']])+
 f'<p>Dates and prices taken from official websites; each guide gives opening hours and access.</p><h3>How to plan it?</h3><p>Strasbourg is about 1 h 50 from Paris by TGV, and Colmar about 30 minutes from Strasbourg by TER. The easiest plan is to stay in Colmar and visit the wine villages from there; avoid December Saturdays if you can, as they are the busiest. For a quieter visit, {a("../alsace/obernai/","Obernai")} has its own Christmas market, and {a("../alsace/mulhouse/","Mulhouse")} offers the Car Museum and the Railway Museum.</p>')
