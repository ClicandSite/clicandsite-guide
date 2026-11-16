import sys; sys.path.insert(0, '/tmp/g')
from winter_gen import build

# ---------------------------------------------------------------- A. Prix des forfaits
SKI = [  # (nom FR, nom EN, chemin FR, chemin EN, massif FR, massif EN, prix, domaine FR, domaine EN, ouverture FR, ouverture EN)
 ('Isola 2000','Isola 2000','alpes/isola-2000','french-alps/isola-2000','Alpes du Sud','Southern Alps','44 €','Isola 2000','Isola 2000','3 déc.','3 Dec'),
 ('Auron','Auron','alpes/auron','french-alps/auron','Alpes du Sud','Southern Alps','44 €','Auron','Auron','5 déc.','5 Dec'),
 ('Avoriaz','Avoriaz','alpes/avoriaz','french-alps/avoriaz','Haute-Savoie','Haute-Savoie','44,50 €','Avoriaz','Avoriaz','11 déc.','11 Dec'),
 ('Cauterets','Cauterets','pyrenees/cauterets','pyrenees/cauterets','Pyrénées','Pyrenees','46 €','Cirque du Lys','Cirque du Lys','27 nov.','27 Nov'),
 ('SuperDévoluy','SuperDévoluy','alpes/superdevoluy','french-alps/superdevoluy','Alpes du Sud','Southern Alps','46 €','Dévoluy','Dévoluy','12 déc.','12 Dec'),
 ('Font-Romeu','Font-Romeu','pyrenees/font-romeu','pyrenees/font-romeu','Pyrénées','Pyrenees','49,50 €','Pyrénées 2000','Pyrénées 2000','4 déc.','4 Dec'),
 ('Peyragudes','Peyragudes','pyrenees/peyragudes','pyrenees/peyragudes','Pyrénées','Pyrenees','51 €','Peyragudes','Peyragudes','12 déc.','12 Dec'),
 ('Saint-Lary','Saint-Lary','pyrenees/saint-lary','pyrenees/saint-lary','Pyrénées','Pyrenees','54,70 €','Saint-Lary','Saint-Lary','4 déc.','4 Dec'),
 ('Grand Tourmalet','Grand Tourmalet','pyrenees/grand-tourmalet','pyrenees/grand-tourmalet','Pyrénées','Pyrenees','55 €','Barèges-La Mongie','Barèges-La Mongie','5 déc.','5 Dec'),
 ('Châtel','Châtel','alpes/chatel','french-alps/chatel','Haute-Savoie','Haute-Savoie','55 € en ligne','Espace Liberté','Espace Liberté','—','—'),
 ('Montgenèvre','Montgenèvre','alpes/montgenevre','french-alps/montgenevre','Hautes-Alpes','Hautes-Alpes','56 €','Montgenèvre','Montgenèvre','28 nov.','28 Nov'),
 ('La Clusaz','La Clusaz','alpes/la-clusaz','french-alps/la-clusaz','Haute-Savoie','Haute-Savoie','56,50 €','La Clusaz-Manigod','La Clusaz-Manigod','12 déc.','12 Dec'),
 ('Megève','Megève','alpes/megeve','french-alps/megeve','Haute-Savoie','Haute-Savoie','65 €','Évasion Mont-Blanc','Évasion Mont-Blanc','19 déc.','19 Dec'),
 ('Les 2 Alpes','Les 2 Alpes','alpes/les-2-alpes','french-alps/les-2-alpes','Isère','Isère','68 €','Les 2 Alpes','Les 2 Alpes','28 nov.','28 Nov'),
 ('La Grave','La Grave','alpes/la-grave','french-alps/la-grave','Hautes-Alpes','Hautes-Alpes','68 €','Téléphériques de la Meije','Meije cable cars','19 déc.','19 Dec'),
 ('Tignes','Tignes','alpes/tignes','french-alps/tignes','Savoie','Savoie','70 €','Tignes seul','Tignes only','21 nov.','21 Nov'),
 ('Val d’Isère','Val d’Isère','alpes/val-d-isere','french-alps/val-d-isere','Savoie','Savoie','70 €','Val d’Isère seul','Val d’Isère only','28 nov.','28 Nov'),
 ('Les Menuires','Les Menuires','alpes/les-menuires','french-alps/les-menuires','Savoie','Savoie','70 €','Menuires-Saint-Martin','Menuires-Saint-Martin','5 déc.','5 Dec'),
 ('Les Arcs','Les Arcs','alpes/les-arcs','french-alps/les-arcs','Savoie','Savoie','71 €','Pass Classique','Pass Classique','12 déc.','12 Dec'),
 ('La Plagne','La Plagne','alpes/la-plagne','french-alps/la-plagne','Savoie','Savoie','72 €','La Plagne','La Plagne','12 déc.','12 Dec'),
 ('Val Thorens','Val Thorens','alpes/val-thorens','french-alps/val-thorens','Savoie','Savoie','73,50 €','Val Thorens-Orelle','Val Thorens-Orelle','21 nov.','21 Nov'),
 ('Chamonix','Chamonix','alpes/chamonix','french-alps/chamonix','Haute-Savoie','Haute-Savoie','76,50 €','Chamonix Le Pass','Chamonix Le Pass','fin nov.','late Nov'),
 ('Tignes-Val d’Isère','Tignes-Val d’Isère','alpes/val-d-isere','french-alps/val-d-isere','Savoie','Savoie','78 €','Tignes-Val d’Isère','Tignes-Val d’Isère','28 nov.','28 Nov'),
 ('Courchevel, Méribel','Courchevel, Méribel','alpes/courchevel','french-alps/courchevel','Savoie','Savoie','84,20 €','3 Vallées','3 Vallées','4-5 déc.','4-5 Dec'),
]
def ski_table(lang):
    i = 0 if lang == 'fr' else 1
    pre = '../../'
    eur = (lambda x: x) if lang == 'fr' else (lambda x: '€' + x.replace(' €', '').replace(',', '.').replace(' en ligne', ' online') if x[0].isdigit() else x)
    head = ('<tr><th>Station</th><th>Domaine</th><th>Journée adulte</th><th>Ouverture</th></tr>' if lang == 'fr'
            else '<tr><th>Resort</th><th>Ski area</th><th>Adult day pass</th><th>Opening</th></tr>')
    rows = ''.join(f'<tr><td><a href="{pre}{r[2+i]}/">{r[i]}</a> <span class="tbl__s">{r[4+i]}</span></td><td>{r[7+i]}</td><td><strong>{eur(r[6])}</strong></td><td>{r[9+i]}</td></tr>' for r in SKI)
    return f'<div class="tbl"><table><thead>{head}</thead><tbody>{rows}</tbody></table></div>'

A = dict(photo='courchevel', og='courchevel', acts=[({'fr':'idees/stations-de-ski-ouvertes','en':'ideas/ski-resort-opening-dates'},0),({'fr':'idees/stations-de-ski-ouvertes','en':'ideas/ski-resort-opening-dates'},1)],
 fr=dict(path='idees/prix-forfaits-ski-2026-2027', home='Accueil', crumbs=[('Idées','idees/')], crumb_last='Prix des forfaits de ski 2026-2027',
  title='Prix des forfaits de ski 2026-2027 : le comparatif',
  desc='Combien coûte un forfait de ski en 2026-2027 ? Prix de la journée adulte dans 24 stations des Alpes et des Pyrénées, de la moins chère à la plus chère.',
  h1='Prix des forfaits de ski 2026-2027 : le comparatif des stations',
  lead='De 44 € à Isola 2000 à 84,20 € dans les 3 Vallées : le prix d’une journée de ski varie du simple au double selon la station.',
  body='<p>Voici le prix de la journée de ski pour un adulte en pleine saison, dans les stations de notre guide, de la moins chère à la plus chère. Les tarifs ont été relevés en novembre 2026 sur les grilles publiées par les stations pour l’hiver 2026-2027. Chaque nom renvoie vers notre guide de la station, avec les tarifs enfants, les forfaits 6 jours et l’accès.</p>\n<h2>Le comparatif, de la moins chère à la plus chère</h2>\n' + ski_table('fr') +
   '\n<p class="maj">Prix de la journée adulte en haute saison, à la caisse sauf mention contraire. Tarifs relevés le 16 novembre 2026 ; ils peuvent changer en cours de saison.</p>'
   '\n<h2>Comment payer son forfait moins cher</h2><ul>'
   '<li><strong>Acheter en ligne à l’avance</strong> : à Chamonix, la journée démarre à 49 € en ligne au lieu de 76,50 € ; à Cauterets, certaines journées sont jusqu’à 40 % moins chères en ligne.</li>'
   '<li><strong>Skier le samedi</strong> : c’est le jour des départs, donc des réductions. Dans les 3 Vallées, la journée est à -20 % le samedi en ligne ; à Châtel, elle descend à 44 € ; aux Menuires, à 41 €.</li>'
   '<li><strong>Venir en début ou en fin de saison</strong> : 52 € à Megève au lieu de 65 €, 54,50 € aux 2 Alpes au lieu de 68 €, 66,10 € à Val Thorens au lieu de 73,50 €.</li>'
   '<li><strong>Prendre une carte de station</strong> : au Grand Tourmalet, la carte No Souci fait descendre la journée à 38,50 € hors vacances.</li>'
   '<li><strong>Commencer sur les pistes débutants</strong> : à Isola 2000, le forfait du front de neige est gratuit.</li></ul>'
   '\n<h2>Les Pyrénées, moins chères que les Alpes</h2><p>Les cinq stations des Pyrénées du comparatif sont toutes entre 46 € et 55 € la journée. Dans les Alpes, il faut aller dans les petites stations ou dans les Alpes du Sud, comme Isola 2000, Auron ou le Dévoluy, pour trouver ces prix. Les grandes stations de Savoie dépassent 70 €.</p>'
   '\n<h2>Les grands domaines reliés</h2><p>Les forfaits qui ouvrent plusieurs stations sont les plus chers : 84,20 € pour les 3 Vallées (Courchevel, Méribel, Les Menuires, Val Thorens), 78 € pour Tignes-Val d’Isère, 78 € pour Paradiski (La Plagne et Les Arcs) et 69 € pour les Portes du Soleil depuis Avoriaz ou Châtel. Si vous skiez peu, le forfait d’une seule station suffit souvent.</p>',
  book_lead='Cours de ski, sorties en raquettes ou excursion au mont Blanc : quelques activités à réserver pour votre séjour.',
  faq=[('Quelle est la station de ski la moins chère en 2026-2027 ?','Dans notre comparatif, Isola 2000 et Auron, à 44 € la journée adulte, puis Avoriaz à 44,50 € sur son seul domaine. Dans les Pyrénées, Cauterets est à 46 €.'),
       ('Combien coûte un forfait aux 3 Vallées en 2026-2027 ?','84,20 € la journée adulte en haute saison, 75,70 € en début et en fin de saison, et 421 € les 6 jours.'),
       ('Le forfait est-il gratuit pour les enfants ?','Dans la plupart des grandes stations, le forfait est gratuit avant 5 ans, par exemple aux Arcs, à La Plagne et aux Menuires ; à Tignes et Val d’Isère, il est gratuit avant 8 ans.')],
  cards_t='Les stations les moins chères', cards=[dict(href='alpes/isola-2000/',photo='isola-2000',name='Isola 2000',txt='44 € la journée, à 1 h 30 de Nice.'),dict(href='alpes/auron/',photo='auron',name='Auron',txt='44 € la journée, 135 km de pistes.'),dict(href='pyrenees/cauterets/',photo='cauterets',name='Cauterets',txt='46 € la journée au Cirque du Lys.')]),
 en=dict(path='ideas/ski-pass-prices-2026-2027', home='Home', crumbs=[('Ideas','ideas/')], crumb_last='Ski pass prices 2026-2027',
  title='Ski Pass Prices 2026-2027: French Resorts Compared',
  desc='How much is a ski pass in France in 2026-2027? Adult day pass prices at 24 resorts in the Alps and the Pyrenees, from the cheapest to the most expensive.',
  h1='Ski pass prices 2026-2027: French resorts compared',
  lead='From €44 at Isola 2000 to €84.20 in the 3 Vallées: the price of a ski day can double from one resort to another.',
  body='<p>Here is the price of an adult day pass in high season at the resorts in our guide, from the cheapest to the most expensive. Prices were checked in November 2026 against the lists published by the resorts for winter 2026-2027. Each name links to our resort guide, with child prices, 6-day passes and how to get there.</p>\n<h2>The comparison, from cheapest to most expensive</h2>\n' + ski_table('en') +
   '\n<p class="maj">Adult day pass price in high season, at the ticket office unless stated. Prices checked on 16 November 2026; they can change during the season.</p>'
   '\n<h2>How to pay less for your lift pass</h2><ul>'
   '<li><strong>Buy online in advance</strong>: in Chamonix, a day starts at €49 online instead of €76.50; in Cauterets, some days are up to 40% cheaper online.</li>'
   '<li><strong>Ski on Saturday</strong>: it is changeover day, so passes are cheaper. In the 3 Vallées, a day is 20% off on Saturdays online; in Châtel it drops to €44; in Les Menuires, to €41.</li>'
   '<li><strong>Go early or late in the season</strong>: €52 in Megève instead of €65, €54.50 in Les 2 Alpes instead of €68, €66.10 in Val Thorens instead of €73.50.</li>'
   '<li><strong>Get a resort card</strong>: at the Grand Tourmalet, the No Souci card brings a day down to €38.50 outside school holidays.</li>'
   '<li><strong>Start on the beginner slopes</strong>: at Isola 2000, the front de neige pass is free.</li></ul>'
   '\n<h2>The Pyrenees are cheaper than the Alps</h2><p>The five Pyrenees resorts in the comparison all cost between €46 and €55 a day. In the Alps, you need to head to smaller resorts or the Southern Alps, such as Isola 2000, Auron or the Dévoluy, to find these prices. The big Savoie resorts go above €70.</p>'
   '\n<h2>The big linked ski areas</h2><p>Passes covering several resorts cost the most: €84.20 for the 3 Vallées (Courchevel, Méribel, Les Menuires, Val Thorens), €78 for Tignes-Val d’Isère, €78 for Paradiski (La Plagne and Les Arcs) and €69 for the Portes du Soleil from Avoriaz or Châtel. If you only ski a little, a single-resort pass is often enough.</p>',
  book_lead='Ski lessons, snowshoe outings or a trip to Mont Blanc: a few activities to book for your stay.',
  faq=[('Which is the cheapest ski resort in France in 2026-2027?','In our comparison, Isola 2000 and Auron, at €44 for an adult day pass, then Avoriaz at €44.50 on its own ski area. In the Pyrenees, Cauterets costs €46.'),
       ('How much is a 3 Vallées lift pass in 2026-2027?','€84.20 a day for an adult in high season, €75.70 early and late in the season, and €421 for 6 days.'),
       ('Are lift passes free for children?','At most big resorts the pass is free for under-5s, for example in Les Arcs, La Plagne and Les Menuires; in Tignes and Val d’Isère it is free for under-8s.')],
  cards_t='The cheapest resorts', cards=[dict(href='french-alps/isola-2000/',photo='isola-2000',name='Isola 2000',txt='€44 a day, 1 hour 30 from Nice.'),dict(href='french-alps/auron/',photo='auron',name='Auron',txt='€44 a day, 135 km of runs.'),dict(href='pyrenees/cauterets/',photo='cauterets',name='Cauterets',txt='€46 a day at the Cirque du Lys.')]))

# ---------------------------------------------------------------- B. Marchés de Noël en Alsace
B = dict(photo='strasbourg', og='strasbourg', acts=[({'fr':'alsace/strasbourg','en':'alsace/strasbourg'},0),({'fr':'alsace/colmar','en':'alsace/colmar'},1)],
 fr=dict(path='idees/marches-de-noel-alsace', home='Accueil', crumbs=[('Idées','idees/')], crumb_last='Marchés de Noël en Alsace 2026',
  title='Marchés de Noël en Alsace 2026 : dates et itinéraire',
  desc='Les dates 2026 des marchés de Noël de Strasbourg, Colmar, Riquewihr et Kaysersberg, les navettes depuis Colmar et un itinéraire pour tout voir en deux jours.',
  h1='Marchés de Noël en Alsace 2026 : dates et itinéraire',
  lead='Strasbourg, Colmar, Riquewihr et Kaysersberg : quatre marchés, des dates différentes et des navettes pour passer de l’un à l’autre sans voiture.',
  body='<p>L’Alsace est la région des marchés de Noël en France. Le plus ancien, à Strasbourg, existe depuis 1570. Mais les dates ne sont pas les mêmes partout : certains marchés ferment dès le 20 décembre, d’autres ne sont ouverts que le week-end. Voici le calendrier 2026 pour bien organiser votre séjour.</p>'
   '\n<h2>Les dates 2026</h2><ol class="agenda">'
   '<li class="ag"><span class="ag__d">23 nov.</span><div class="ag__b"><strong><a href="../../alsace/colmar/">Colmar</a></strong><p>Six marchés dans la vieille ville, jusqu’au 29 décembre ; le marché gourmand et la grande roue jusqu’au 3 janvier 2027.</p></div></li>'
   '<li class="ag"><span class="ag__d">27 nov.</span><div class="ag__b"><strong><a href="../../alsace/strasbourg/">Strasbourg</a></strong><p>Le Christkindelsmärik de la place Broglie, jusqu’au 24 décembre, de 11 h 30 à 21 h environ.</p></div></li>'
   '<li class="ag"><span class="ag__d">27 nov.</span><div class="ag__b"><strong><a href="../../alsace/riquewihr/">Riquewihr</a></strong><p>Tous les jours jusqu’au 20 décembre, à partir de 10 h.</p></div></li>'
   '<li class="ag"><span class="ag__d">27 nov.</span><div class="ag__b"><strong><a href="../../alsace/kaysersberg/">Kaysersberg</a></strong><p>Seulement du vendredi au dimanche, quatre week-ends jusqu’au 20 décembre, de 10 h à 20 h.</p></div></li></ol>'
   '\n<p>L’entrée est libre et gratuite sur tous ces marchés.</p>'
   '\n<h2>Sans voiture : les navettes de Noël</h2><p>Du 27 novembre au 20 décembre 2026, des navettes de Noël partent de la gare de Colmar vers les marchés des villages voisins, dont Kaysersberg et Riquewihr. C’est la solution la plus simple : les parkings des villages sont saturés le week-end.</p>'
   '\n<h2>Notre itinéraire en deux jours</h2><ul>'
   '<li><strong>Jour 1, Strasbourg</strong> : le marché de la place Broglie et le grand sapin de la place Kléber le matin, avant la foule, puis la cathédrale et la Petite France. Prenez le train pour Colmar en fin de journée.</li>'
   '<li><strong>Jour 2, Colmar et les villages</strong> : la navette de Noël le matin pour Riquewihr, puis Kaysersberg si c’est un vendredi, un samedi ou un dimanche. Retour à Colmar pour voir la Petite Venise illuminée le soir.</li></ul>'
   '\n<h2>Nos conseils</h2><ul><li><strong>Évitez les samedis</strong> : c’est le jour le plus chargé partout. Venez en semaine si vous pouvez.</li><li><strong>Réservez l’hôtel très tôt</strong> : à Strasbourg, les chambres des week-ends de décembre partent dès l’été.</li><li><strong>Ne visez pas la dernière semaine</strong> à la campagne : Riquewihr et Kaysersberg ferment le 20 décembre.</li></ul>',
  book_lead='Visites guidées des marchés, croisière sur l’Ill ou barque dans la Petite Venise : à réserver avant de partir.',
  faq=[('Quand ouvrent les marchés de Noël en Alsace en 2026 ?','Colmar ouvre le lundi 23 novembre 2026 ; Strasbourg, Riquewihr et Kaysersberg le vendredi 27 novembre.'),
       ('Quel marché de Noël reste ouvert le plus longtemps ?','Colmar : ses marchés ferment le 29 décembre 2026, mais le marché gourmand et la grande roue restent ouverts jusqu’au 3 janvier 2027.'),
       ('Peut-on faire les marchés de Noël d’Alsace sans voiture ?','Oui : le train relie Strasbourg et Colmar, et des navettes de Noël partent de la gare de Colmar vers les villages du 27 novembre au 20 décembre 2026.')],
  cards_t='Nos guides des marchés', cards=[dict(href='alsace/strasbourg/',photo='strasbourg',name='Strasbourg',txt='Le plus ancien marché de Noël de France.'),dict(href='alsace/colmar/',photo='colmar',name='Colmar',txt='Six marchés et la Petite Venise illuminée.'),dict(href='alsace/riquewihr/',photo='riquewihr',name='Riquewihr',txt='Un village fortifié au milieu des vignes.'),dict(href='alsace/kaysersberg/',photo='kaysersberg',name='Kaysersberg',txt='Un marché d’artisans, quatre week-ends.')]),
 en=dict(path='ideas/alsace-christmas-markets', home='Home', crumbs=[('Ideas','ideas/')], crumb_last='Alsace Christmas markets 2026',
  title='Alsace Christmas Markets 2026: Dates and Itinerary',
  desc='The 2026 dates of the Christmas markets in Strasbourg, Colmar, Riquewihr and Kaysersberg, the shuttle buses from Colmar and a two-day itinerary.',
  h1='Alsace Christmas markets 2026: dates and itinerary',
  lead='Strasbourg, Colmar, Riquewihr and Kaysersberg: four markets, different dates, and shuttle buses to go from one to the next without a car.',
  body='<p>Alsace is France’s Christmas market region. The oldest, in Strasbourg, dates back to 1570. But the dates are not the same everywhere: some markets close on 20 December, others only open at weekends. Here is the 2026 calendar to plan your trip.</p>'
   '\n<h2>The 2026 dates</h2><ol class="agenda">'
   '<li class="ag"><span class="ag__d">23 Nov</span><div class="ag__b"><strong><a href="../../alsace/colmar/">Colmar</a></strong><p>Six markets in the old town, until 29 December; the food market and the big wheel until 3 January 2027.</p></div></li>'
   '<li class="ag"><span class="ag__d">27 Nov</span><div class="ag__b"><strong><a href="../../alsace/strasbourg/">Strasbourg</a></strong><p>The Christkindelsmärik on Place Broglie, until 24 December, from about 11.30am to 9pm.</p></div></li>'
   '<li class="ag"><span class="ag__d">27 Nov</span><div class="ag__b"><strong><a href="../../alsace/riquewihr/">Riquewihr</a></strong><p>Every day until 20 December, from 10am.</p></div></li>'
   '<li class="ag"><span class="ag__d">27 Nov</span><div class="ag__b"><strong><a href="../../alsace/kaysersberg/">Kaysersberg</a></strong><p>Friday to Sunday only, four weekends until 20 December, 10am to 8pm.</p></div></li></ol>'
   '\n<p>Entry is free at all these markets.</p>'
   '\n<h2>Without a car: the Christmas shuttles</h2><p>From 27 November to 20 December 2026, Christmas shuttle buses leave Colmar station for the markets in the nearby villages, including Kaysersberg and Riquewihr. It is the easiest option: village car parks are full at weekends.</p>'
   '\n<h2>Our two-day itinerary</h2><ul>'
   '<li><strong>Day 1, Strasbourg</strong>: the Place Broglie market and the giant tree on Place Kléber in the morning, before the crowds, then the cathedral and La Petite France. Take the train to Colmar in the late afternoon.</li>'
   '<li><strong>Day 2, Colmar and the villages</strong>: the Christmas shuttle to Riquewihr in the morning, then Kaysersberg if it is a Friday, Saturday or Sunday. Back in Colmar to see Little Venice lit up in the evening.</li></ul>'
   '\n<h2>Our tips</h2><ul><li><strong>Avoid Saturdays</strong>: it is the busiest day everywhere. Come on a weekday if you can.</li><li><strong>Book your hotel very early</strong>: in Strasbourg, rooms for December weekends go in the summer.</li><li><strong>Do not aim for the last week</strong> in the villages: Riquewihr and Kaysersberg close on 20 December.</li></ul>',
  book_lead='Guided tours of the markets, a cruise on the Ill or a boat ride in Little Venice: book before you go.',
  faq=[('When do the Alsace Christmas markets open in 2026?','Colmar opens on Monday 23 November 2026; Strasbourg, Riquewihr and Kaysersberg on Friday 27 November.'),
       ('Which Christmas market stays open the longest?','Colmar: its markets close on 29 December 2026, but the food market and the big wheel stay open until 3 January 2027.'),
       ('Can you visit the Alsace Christmas markets without a car?','Yes: trains link Strasbourg and Colmar, and Christmas shuttle buses run from Colmar station to the villages from 27 November to 20 December 2026.')],
  cards_t='Our market guides', cards=[dict(href='alsace/strasbourg/',photo='strasbourg',name='Strasbourg',txt='France’s oldest Christmas market.'),dict(href='alsace/colmar/',photo='colmar',name='Colmar',txt='Six markets and Little Venice lit up.'),dict(href='alsace/riquewihr/',photo='riquewihr',name='Riquewihr',txt='A walled village among the vineyards.'),dict(href='alsace/kaysersberg/',photo='kaysersberg',name='Kaysersberg',txt='A craft market over four weekends.')]))

# ---------------------------------------------------------------- C. Réveillon du Nouvel An
C = dict(photo='champs-elysees', og='champs-elysees', acts=[({'fr':'paris/croisiere-sur-la-seine','en':'paris/seine-cruise'},1),({'fr':'paris/moulin-rouge','en':'paris/moulin-rouge'},1),({'fr':'cote-d-azur/nice','en':'french-riviera/nice'},0)],
 event={'fr':{"name":"Nouvel An 2027 sur les Champs-Élysées","startDate":"2026-12-31T23:50:00+01:00","endDate":"2027-01-01T00:20:00+01:00","location":{"@type":"Place","name":"Avenue des Champs-Élysées","address":"Avenue des Champs-Élysées, 75008 Paris, France"},"isAccessibleForFree":True,"description":"Vidéo-mapping sur l’Arc de Triomphe à 23 h 50, puis feu d’artifice à minuit."},
        'en':{"name":"New Year’s Eve 2027 on the Champs-Élysées","startDate":"2026-12-31T23:50:00+01:00","endDate":"2027-01-01T00:20:00+01:00","location":{"@type":"Place","name":"Avenue des Champs-Élysées","address":"Avenue des Champs-Élysées, 75008 Paris, France"},"isAccessibleForFree":True,"description":"Video mapping on the Arc de Triomphe at 11.50pm, then fireworks at midnight."}},
 fr=dict(path='idees/reveillon-nouvel-an', home='Accueil', crumbs=[('Idées','idees/')], crumb_last='Réveillon du Nouvel An 2026',
  title='Réveillon du Nouvel An 2026 : Paris et Côte d’Azur',
  desc='Où passer le réveillon du 31 décembre 2026 ? Le feu d’artifice gratuit des Champs-Élysées, les croisières-dîners sur la Seine et les soirées de la Côte d’Azur.',
  h1='Réveillon du Nouvel An 2026 : où le fêter à Paris et sur la Côte d’Azur',
  lead='Le feu d’artifice gratuit des Champs-Élysées, un dîner sur la Seine ou une soirée à la montagne au-dessus de Nice : nos idées pour passer à 2027.',
  body='<p>Le 31 décembre tombe un jeudi en 2026. Que vous cherchiez une fête gratuite en plein air ou un dîner à réserver, voici ce qui est prévu à Paris et sur la Côte d’Azur, avec les horaires annoncés.</p>'
   '\n<h2>À Paris : le feu d’artifice des Champs-Élysées</h2><p>La Ville de Paris organise une soirée gratuite sur les Champs-Élysées, de l’Arc de Triomphe à la place de la Concorde. À partir de 23 h 50, un spectacle de vidéo-mapping est projeté sur l’Arc de Triomphe, suivi du compte à rebours. À minuit, un feu d’artifice d’une dizaine de minutes est tiré, en musique. La fête se termine vers 0 h 20.</p>'
   '<ul><li><strong>Arrivez tôt</strong> : pour être dans l’axe de l’Arc de Triomphe, il faut être là bien avant 23 h.</li><li><strong>Accès contrôlés</strong> : fouilles à l’entrée ; verre, pétards et feux d’artifice personnels sont interdits.</li><li><strong>Pour rentrer</strong> : prévoyez que les stations de métro les plus proches soient fermées ou saturées, et marchez quelques stations.</li></ul>'
   '\n<h2>À Paris : dîner sur la Seine ou au cabaret</h2><p>Pour un réveillon assis, les croisières-dîners sur la Seine et les cabarets comme le <a href="../../paris/moulin-rouge/">Moulin Rouge</a> proposent des soirées spéciales le 31 décembre. Ce sont les places qui partent les premières : réservez dès maintenant. Voir notre guide des <a href="../../paris/croisiere-sur-la-seine/">croisières sur la Seine</a>.</p>'
   '\n<h2>Sur la Côte d’Azur</h2><ul>'
   '<li><strong>Nice</strong> : la ville fête le Nouvel An sur la Promenade des Anglais et dans le Vieux-Nice, où les restaurants proposent des menus de réveillon. Le programme officiel de la Ville n’est pas encore publié ; nous le mettrons à jour dès sa sortie. Au Théâtre de la Cité, le cabaret Burlesque Follies propose un réveillon à 22 h, à 80 € avec deux coupes et la soirée dansante.</li>'
   '<li><strong>Isola 2000</strong> : à 1 h 30 de Nice, la station fête le Nouvel An à partir de 18 h, gratuitement, avec bal, descente aux flambeaux des moniteurs et feu d’artifice. Voir notre <a href="../../alpes/isola-2000/">guide d’Isola 2000</a>.</li>'
   '<li><strong>Auron</strong> : soirée du Nouvel An gratuite sur la place centrale de la station. Voir notre <a href="../../alpes/auron/">guide d’Auron</a>.</li></ul>'
   '\n<h2>Nos conseils</h2><ul><li><strong>Réservez tôt</strong> : dîners, croisières et hôtels sont souvent complets début décembre.</li><li><strong>Pensez au retour</strong> : taxis et VTC sont rares et chers après minuit ; réservez votre trajet à l’avance.</li></ul>',
  book_lead='Croisière-dîner du réveillon, soirée au cabaret ou visite de Nice : à réserver avant que les places partent.',
  faq=[('À quelle heure est le feu d’artifice des Champs-Élysées ?','À minuit, après un spectacle de vidéo-mapping sur l’Arc de Triomphe qui commence à 23 h 50. Le feu dure une dizaine de minutes et la soirée se termine vers 0 h 20.'),
       ('Le réveillon des Champs-Élysées est-il gratuit ?','Oui, la soirée organisée par la Ville de Paris est gratuite, avec des accès contrôlés et des fouilles.'),
       ('Y a-t-il un feu d’artifice à Nice le 31 décembre 2026 ?','Le programme officiel de la Ville de Nice n’est pas encore publié. À Isola 2000, à 1 h 30 de Nice, un feu d’artifice est annoncé lors de la soirée gratuite du 31 décembre.')],
  cards_t='À lire aussi', cards=[dict(href='paris/noel-a-paris/',photo='noel-a-paris',name='Noël à Paris',txt='Illuminations, vitrines et marchés de Noël.'),dict(href='idees/cote-d-azur-en-hiver/',photo='menton',name='Côte d’Azur en hiver',txt='Le soleil et les grandes fêtes de février.'),dict(href='paris/croisiere-sur-la-seine/',photo='croisiere-sur-la-seine',name='Croisières sur la Seine',txt='Bateaux-promenades et dîners sur l’eau.')]),
 en=dict(path='ideas/new-years-eve-france', home='Home', crumbs=[('Ideas','ideas/')], crumb_last='New Year’s Eve 2026',
  title='New Year’s Eve 2026 in Paris and on the French Riviera',
  desc='Where to spend New Year’s Eve 2026? The free fireworks on the Champs-Élysées, dinner cruises on the Seine and parties on the French Riviera.',
  h1='New Year’s Eve 2026: where to celebrate in Paris and on the French Riviera',
  lead='Free fireworks on the Champs-Élysées, dinner on the Seine or a party in the mountains above Nice: our ideas for welcoming 2027.',
  body='<p>31 December falls on a Thursday in 2026. Whether you want a free open-air party or a dinner to book, here is what is planned in Paris and on the French Riviera, with the announced times.</p>'
   '\n<h2>In Paris: the Champs-Élysées fireworks</h2><p>The City of Paris holds a free event on the Champs-Élysées, from the Arc de Triomphe to Place de la Concorde. From 11.50pm, a video-mapping show is projected onto the Arc de Triomphe, followed by the countdown. At midnight, a fireworks display of about ten minutes is set off to music. The party ends at around 12.20am.</p>'
   '<ul><li><strong>Arrive early</strong>: to be in line with the Arc de Triomphe, get there well before 11pm.</li><li><strong>Security checks</strong>: bags are searched; glass, bangers and private fireworks are banned.</li><li><strong>Getting home</strong>: expect the nearest metro stations to be closed or packed, and walk a few stops.</li></ul>'
   '\n<h2>In Paris: dinner on the Seine or at a cabaret</h2><p>For a sit-down New Year’s Eve, dinner cruises on the Seine and cabarets such as the <a href="../../paris/moulin-rouge/">Moulin Rouge</a> hold special evenings on 31 December. These are the first seats to sell out: book now. See our guide to <a href="../../paris/seine-cruise/">Seine cruises</a>.</p>'
   '\n<h2>On the French Riviera</h2><ul>'
   '<li><strong>Nice</strong>: the city celebrates on the Promenade des Anglais and in Old Nice, where restaurants serve New Year’s Eve menus. The city’s official programme is not out yet; we will update this page as soon as it is. At the Théâtre de la Cité, the Burlesque Follies cabaret holds a New Year’s Eve show at 10pm, €80 with two glasses of champagne and the dance party.</li>'
   '<li><strong>Isola 2000</strong>: 1 hour 30 from Nice, the resort celebrates from 6pm, free of charge, with a ball, a torchlight descent by the ski instructors and fireworks. See our <a href="../../french-alps/isola-2000/">Isola 2000 guide</a>.</li>'
   '<li><strong>Auron</strong>: free New Year’s Eve party on the resort’s main square. See our <a href="../../french-alps/auron/">Auron guide</a>.</li></ul>'
   '\n<h2>Our tips</h2><ul><li><strong>Book early</strong>: dinners, cruises and hotels are often full by early December.</li><li><strong>Plan your way back</strong>: taxis and ride-hailing cars are scarce and expensive after midnight; book your ride in advance.</li></ul>',
  book_lead='New Year’s Eve dinner cruise, a cabaret night or a tour of Nice: book before the seats go.',
  faq=[('What time are the Champs-Élysées fireworks?','At midnight, after a video-mapping show on the Arc de Triomphe that starts at 11.50pm. The fireworks last about ten minutes and the event ends at around 12.20am.'),
       ('Is the Champs-Élysées New Year’s Eve party free?','Yes, the event run by the City of Paris is free, with controlled access and bag searches.'),
       ('Are there fireworks in Nice on 31 December 2026?','The City of Nice has not yet published its official programme. At Isola 2000, 1 hour 30 from Nice, fireworks are announced at the free New Year’s Eve party.')],
  cards_t='Read next', cards=[dict(href='paris/christmas-in-paris/',photo='noel-a-paris',name='Christmas in Paris',txt='Lights, shop windows and Christmas markets.'),dict(href='ideas/french-riviera-in-winter/',photo='menton',name='French Riviera in winter',txt='Sunshine and the big February festivals.'),dict(href='paris/seine-cruise/',photo='croisiere-sur-la-seine',name='Seine cruises',txt='Sightseeing boats and dinners on the water.')]))

# ---------------------------------------------------------------- D. Vacances de février 2027
D = dict(photo='les-arcs', og='les-arcs', acts=[({'fr':'idees/stations-de-ski-ouvertes','en':'ideas/ski-resort-opening-dates'},0),({'fr':'cote-d-azur/carnaval-de-nice','en':'french-riviera/nice-carnival'},0)],
 fr=dict(path='idees/vacances-de-fevrier-2027', home='Accueil', crumbs=[('Idées','idees/')], crumb_last='Vacances de février 2027',
  title='Vacances de février 2027 : dates par zone et où partir',
  desc='Les dates des vacances d’hiver 2027 pour les zones A, B et C, et où partir chaque semaine : stations de ski, Carnaval de Nice, Fête du Citron.',
  h1='Vacances de février 2027 : les dates par zone et où partir',
  lead='Du 6 février au 8 mars 2027, les trois zones partent l’une après l’autre. Voici quelle semaine choisir pour le ski ou pour le soleil de la Côte d’Azur.',
  body='<p>Les vacances d’hiver 2027 durent deux semaines dans chaque zone et s’étalent sur un mois. La zone C part la première, la zone B la dernière. Les vacances commencent le samedi après la classe et la reprise a lieu le lundi matin.</p>'
   '\n<h2>Les dates par zone</h2><div class="tbl"><table><thead><tr><th>Zone</th><th>Départ</th><th>Reprise</th></tr></thead><tbody>'
   '<tr><td><strong>Zone C</strong> <span class="tbl__s">Paris, Créteil, Versailles, Montpellier, Toulouse</span></td><td>samedi 6 février 2027</td><td>lundi 22 février 2027</td></tr>'
   '<tr><td><strong>Zone A</strong> <span class="tbl__s">Lyon, Grenoble, Bordeaux, Clermont-Ferrand, Dijon, Besançon, Limoges, Poitiers</span></td><td>samedi 13 février 2027</td><td>lundi 1er mars 2027</td></tr>'
   '<tr><td><strong>Zone B</strong> <span class="tbl__s">Aix-Marseille, Nice, Lille, Nantes, Rennes, Strasbourg, Normandie, Nancy-Metz, Orléans-Tours, Reims, Amiens</span></td><td>samedi 20 février 2027</td><td>lundi 8 mars 2027</td></tr>'
   '</tbody></table></div><p>La Corse suit le calendrier de la zone A.</p>'
   '\n<h2>La semaine la plus chargée</h2><p>Du 13 au 22 février 2027, les zones C et A sont en vacances en même temps : c’est la période la plus chère et la plus fréquentée dans les stations de ski, avec les bouchons du samedi sur les routes des Alpes. Si vous avez le choix, visez la première semaine de la zone C (6 au 13 février) ou la dernière semaine de la zone B (27 février au 8 mars).</p>'
   '\n<h2>Où partir au ski</h2><p>Toutes les stations sont ouvertes en février. Pour comparer les prix des forfaits, voir notre <a href="../prix-forfaits-ski-2026-2027/">comparatif 2026-2027</a> : de 44 € la journée à Isola 2000 ou Auron à 84,20 € dans les 3 Vallées. Les Pyrénées, entre 46 € et 55 €, sont souvent moins chargées que les grandes stations de Savoie.</p>'
   '\n<h2>Ou le soleil de la Côte d’Azur</h2><p>Février est le mois des grandes fêtes de la Riviera : le <a href="../../cote-d-azur/carnaval-de-nice/">Carnaval de Nice</a>, la <a href="../../cote-d-azur/fete-du-citron-menton/">Fête du Citron de Menton</a> du 13 au 28 février 2027, et la <a href="../../cote-d-azur/route-du-mimosa/">Fête du Mimosa de Mandelieu</a> du 10 au 14 février. La zone A, en vacances du 13 février au 1er mars, peut tout voir.</p>',
  book_lead='Cours de ski en station ou places en tribune au Carnaval de Nice : à réserver avant février.',
  faq=[('Quelles sont les dates des vacances de février 2027 ?','Zone C : du 6 au 22 février 2027. Zone A : du 13 février au 1er mars 2027. Zone B : du 20 février au 8 mars 2027.'),
       ('Quelle zone part en premier en février 2027 ?','La zone C (Paris, Créteil, Versailles, Montpellier, Toulouse), dès le samedi 6 février 2027.'),
       ('Quelle est la semaine la plus chargée au ski en février 2027 ?','Du 13 au 22 février 2027, quand les zones C et A sont en vacances en même temps.')],
  cards_t='Pour préparer le séjour', cards=[dict(href='idees/prix-forfaits-ski-2026-2027/',photo='courchevel',name='Prix des forfaits',txt='Le comparatif 2026-2027 des stations.'),dict(href='cote-d-azur/carnaval-de-nice/',photo='carnaval-nice',name='Carnaval de Nice',txt='Corsos et bataille de fleurs en février.'),dict(href='cote-d-azur/fete-du-citron-menton/',photo='fete-du-citron',name='Fête du Citron',txt='Du 13 au 28 février 2027 à Menton.')]),
 en=dict(path='ideas/february-school-holidays-2027', home='Home', crumbs=[('Ideas','ideas/')], crumb_last='February holidays 2027',
  title='France February Holidays 2027: Dates and Where to Go',
  desc='The dates of the 2027 French winter school holidays for zones A, B and C, and where to go each week: ski resorts, the Nice Carnival, the Lemon Festival.',
  h1='February school holidays 2027 in France: dates by zone and where to go',
  lead='From 6 February to 8 March 2027, the three zones go on holiday one after the other. Here is which week to choose for skiing or for Riviera sunshine.',
  body='<p>French winter school holidays in 2027 last two weeks in each zone and span a month. Zone C goes first, zone B last. The holidays start on Saturday after school and children go back on Monday morning. If you are travelling from abroad, these are the weeks when French families crowd the ski resorts.</p>'
   '\n<h2>Dates by zone</h2><div class="tbl"><table><thead><tr><th>Zone</th><th>Start</th><th>Back to school</th></tr></thead><tbody>'
   '<tr><td><strong>Zone C</strong> <span class="tbl__s">Paris, Créteil, Versailles, Montpellier, Toulouse</span></td><td>Saturday 6 February 2027</td><td>Monday 22 February 2027</td></tr>'
   '<tr><td><strong>Zone A</strong> <span class="tbl__s">Lyon, Grenoble, Bordeaux, Clermont-Ferrand, Dijon, Besançon, Limoges, Poitiers</span></td><td>Saturday 13 February 2027</td><td>Monday 1 March 2027</td></tr>'
   '<tr><td><strong>Zone B</strong> <span class="tbl__s">Aix-Marseille, Nice, Lille, Nantes, Rennes, Strasbourg, Normandy, Nancy-Metz, Orléans-Tours, Reims, Amiens</span></td><td>Saturday 20 February 2027</td><td>Monday 8 March 2027</td></tr>'
   '</tbody></table></div><p>Corsica follows the zone A calendar.</p>'
   '\n<h2>The busiest week</h2><p>From 13 to 22 February 2027, zones C and A are on holiday at the same time: it is the most expensive and crowded period in the ski resorts, with Saturday traffic jams on the Alpine roads. If you can choose, aim for the first week of zone C (6 to 13 February) or the last week of zone B (27 February to 8 March).</p>'
   '\n<h2>Where to go skiing</h2><p>All resorts are open in February. To compare lift pass prices, see our <a href="../ski-pass-prices-2026-2027/">2026-2027 comparison</a>: from €44 a day at Isola 2000 or Auron to €84.20 in the 3 Vallées. The Pyrenees, between €46 and €55, are often less crowded than the big Savoie resorts.</p>'
   '\n<h2>Or French Riviera sunshine</h2><p>February is the month of the Riviera’s big festivals: the <a href="../../french-riviera/nice-carnival/">Nice Carnival</a>, the <a href="../../french-riviera/lemon-festival-menton/">Menton Lemon Festival</a> from 13 to 28 February 2027, and the <a href="../../french-riviera/mimosa-route/">Mandelieu Mimosa Festival</a> from 10 to 14 February. Zone A, on holiday from 13 February to 1 March, can see them all.</p>',
  book_lead='Ski lessons at the resort or grandstand seats at the Nice Carnival: book before February.',
  faq=[('When are the February school holidays in France in 2027?','Zone C: 6 to 22 February 2027. Zone A: 13 February to 1 March 2027. Zone B: 20 February to 8 March 2027.'),
       ('Which zone goes first in February 2027?','Zone C (Paris, Créteil, Versailles, Montpellier, Toulouse), from Saturday 6 February 2027.'),
       ('Which is the busiest ski week in February 2027?','13 to 22 February 2027, when zones C and A are on holiday at the same time.')],
  cards_t='Plan your trip', cards=[dict(href='ideas/ski-pass-prices-2026-2027/',photo='courchevel',name='Ski pass prices',txt='The 2026-2027 resort comparison.'),dict(href='french-riviera/nice-carnival/',photo='carnaval-nice',name='Nice Carnival',txt='Parades and flower battles in February.'),dict(href='french-riviera/lemon-festival-menton/',photo='fete-du-citron',name='Lemon Festival',txt='13 to 28 February 2027 in Menton.')]))

# ---------------------------------------------------------------- E. Rallye Monte-Carlo 2027
E = dict(photo='monaco', og='monaco', acts=[({'fr':'cote-d-azur/monaco','en':'french-riviera/monaco'},0),({'fr':'cote-d-azur/monaco','en':'french-riviera/monaco'},1),({'fr':'cote-d-azur/nice','en':'french-riviera/nice'},1)],
 event={'fr':{"name":"95e Rallye Automobile Monte-Carlo","startDate":"2027-01-21","endDate":"2027-01-24","location":{"@type":"Place","name":"Port Hercule, Monaco","address":"Quai Albert 1er, 98000 Monaco"},"organizer":{"@type":"Organization","name":"Automobile Club de Monaco","url":"https://acm.mc/"},"description":"Manche d’ouverture du championnat du monde des rallyes (WRC) 2027, entre Gap et Monaco."},
        'en':{"name":"95th Rallye Automobile Monte-Carlo","startDate":"2027-01-21","endDate":"2027-01-24","location":{"@type":"Place","name":"Port Hercule, Monaco","address":"Quai Albert 1er, 98000 Monaco"},"organizer":{"@type":"Organization","name":"Automobile Club de Monaco","url":"https://acm.mc/"},"description":"Opening round of the 2027 FIA World Rally Championship (WRC), between Gap and Monaco."}},
 fr=dict(path='cote-d-azur/rallye-monte-carlo', home='Accueil', crumbs=[('Côte d’Azur','cote-d-azur/')], crumb_last='Rallye Monte-Carlo 2027',
  title='Rallye Monte-Carlo 2027 : dates, parcours, où le voir',
  desc='Le 95e Rallye Monte-Carlo se court du 21 au 24 janvier 2027 entre Gap et Monaco. Dates, programme, où voir les voitures et le Rallye Historique.',
  h1='Rallye Monte-Carlo 2027 : dates, parcours et où le voir',
  lead='Du 21 au 24 janvier 2027, la 95e édition ouvre le championnat du monde des rallyes, sur les routes de montagne entre Gap et Monaco.',
  body='<p>Le Rallye Automobile Monte-Carlo est la première manche du championnat du monde des rallyes (WRC). Organisé par l’Automobile Club de Monaco, il se court en plein hiver sur les petites routes des Alpes du Sud, où la neige et le verglas changent tout d’une spéciale à l’autre.</p>'
   '\n<h2>Les dates 2027</h2><ul><li><strong>Compétition</strong> : du jeudi 21 au dimanche 24 janvier 2027.</li><li><strong>Semaine du rallye</strong> : les reconnaissances et les animations commencent dès le lundi 18 janvier à Monaco.</li><li><strong>Parc d’assistance</strong> : à Gap, dans les Hautes-Alpes, comme les années précédentes.</li><li><strong>Arrivée</strong> : sur le port Hercule, à Monaco, le dimanche 24 janvier.</li></ul>'
   '\n<h2>Où voir les voitures</h2><p>À Monaco, le plus simple est de venir sur le port Hercule, où sont installés le départ, l’arrivée et le podium, quai Albert-Ier. Pour voir les voitures en course, il faut monter dans les spéciales des Alpes du Sud : prévoyez des vêtements chauds, arrivez tôt et respectez les zones réservées au public. Le parcours détaillé est publié par l’Automobile Club de Monaco.</p>'
   '\n<h2>Venir à Monaco pendant le rallye</h2><ul><li><strong>En train</strong> : le TER Nice–Vintimille dessert la gare de Monaco-Monte-Carlo, à quelques minutes à pied du port Hercule.</li><li><strong>En bus depuis Nice</strong> : la ligne Zou! 602 passe par la Moyenne Corniche, avec un arrêt à Èze.</li><li><strong>En voiture</strong> : les parkings publics de Monaco, comme celui des Pêcheurs sous le Rocher, sont très demandés pendant la semaine du rallye.</li><li><strong>Pour repartir</strong> : Uber ne peut pas prendre de course au départ de Monaco ; prévoyez le train, le bus, un taxi monégasque ou un chauffeur réservé à l’avance.</li></ul>\n<h2>Le Rallye Monte-Carlo Historique</h2><p>Une semaine plus tard, du 27 janvier au 3 février 2027, la 29e édition du Rallye Monte-Carlo Historique fait rouler des voitures anciennes, avec des départs de plusieurs villes d’Europe et une arrivée à Monaco.</p>'
   '\n<h2>Nos conseils</h2><ul><li><strong>Réservez votre hôtel tôt</strong> : Monaco et les villes voisines se remplissent pendant la semaine du rallye.</li><li><strong>Venez en train</strong> : la gare de Monaco est reliée à Nice et à Menton par les TER, plus simple que de chercher à se garer.</li><li><strong>Profitez du séjour</strong> : le <a href="../rocher-de-monaco/">Rocher</a>, le <a href="../musee-oceanographique/">Musée océanographique</a> et le <a href="../jardin-exotique-monaco/">Jardin exotique</a> sont ouverts en janvier.</li></ul>',
  book_lead='Visites de Monaco et excursions sur la Riviera : à réserver pour la semaine du rallye.',
  faq=[('Quand a lieu le Rallye Monte-Carlo 2027 ?','La 95e édition se court du jeudi 21 au dimanche 24 janvier 2027, avec l’arrivée sur le port Hercule à Monaco.'),
       ('Où se trouve le parc d’assistance du Rallye Monte-Carlo ?','À Gap, dans les Hautes-Alpes.'),
       ('Quand a lieu le Rallye Monte-Carlo Historique 2027 ?','Du 27 janvier au 3 février 2027, pour sa 29e édition.')],
  cards_t='À voir à Monaco', cards=[dict(href='cote-d-azur/monaco/',photo='monaco',name='Monaco',txt='Le guide complet de la Principauté.'),dict(href='cote-d-azur/grand-prix-de-monaco/',photo='grand-prix-de-monaco',name='Grand Prix de Monaco',txt='La Formule 1 en mai, dans les rues.'),dict(href='cote-d-azur/rocher-de-monaco/',photo='rocher-de-monaco',name='Le Rocher',txt='La vieille ville de Monaco à pied.')]),
 en=dict(path='french-riviera/monte-carlo-rally', home='Home', crumbs=[('French Riviera','french-riviera/')], crumb_last='Monte-Carlo Rally 2027',
  title='Monte-Carlo Rally 2027: Dates, Route, Where to Watch',
  desc='The 95th Monte-Carlo Rally runs from 21 to 24 January 2027 between Gap and Monaco. Dates, programme, where to see the cars and the Historic Rally.',
  h1='Monte-Carlo Rally 2027: dates, route and where to watch',
  lead='From 21 to 24 January 2027, the 95th edition opens the World Rally Championship on the mountain roads between Gap and Monaco.',
  body='<p>The Rallye Automobile Monte-Carlo is the opening round of the World Rally Championship (WRC). Run by the Automobile Club de Monaco, it takes place in midwinter on the narrow roads of the Southern Alps, where snow and ice change everything from one stage to the next.</p>'
   '\n<h2>The 2027 dates</h2><ul><li><strong>Competition</strong>: Thursday 21 to Sunday 24 January 2027.</li><li><strong>Rally week</strong>: reconnaissance and events start on Monday 18 January in Monaco.</li><li><strong>Service park</strong>: in Gap, in the Hautes-Alpes, as in previous years.</li><li><strong>Finish</strong>: on Port Hercule in Monaco on Sunday 24 January.</li></ul>'
   '\n<h2>Where to see the cars</h2><p>In Monaco, the easiest place is Port Hercule, home to the start, the finish and the podium on Quai Albert Ier. To see the cars racing, you need to head up to the stages in the Southern Alps: bring warm clothes, arrive early and stay in the spectator areas. The detailed route is published by the Automobile Club de Monaco.</p>'
   '\n<h2>Getting to Monaco during the rally</h2><ul><li><strong>By train</strong>: TER trains on the Nice–Ventimiglia line stop at Monaco-Monte-Carlo station, a few minutes’ walk from Port Hercule.</li><li><strong>By bus from Nice</strong>: Zou! line 602 runs along the Middle Corniche, stopping in Èze.</li><li><strong>By car</strong>: Monaco’s public car parks, such as the Parking des Pêcheurs below the Rock, are in high demand during rally week.</li><li><strong>Getting back</strong>: Uber rides cannot be booked from Monaco; plan for the train, the bus, a Monaco taxi or a driver booked in advance.</li></ul>\n<h2>The Monte-Carlo Historic Rally</h2><p>A week later, from 27 January to 3 February 2027, the 29th Rallye Monte-Carlo Historique sees classic cars set off from several European cities and finish in Monaco.</p>'
   '\n<h2>Our tips</h2><ul><li><strong>Book your hotel early</strong>: Monaco and the nearby towns fill up during rally week.</li><li><strong>Come by train</strong>: Monaco station is linked to Nice and Menton by TER trains, easier than looking for parking.</li><li><strong>Make the most of your stay</strong>: <a href="../rocher-de-monaco/">the Rock</a>, the <a href="../musee-oceanographique/">Oceanographic Museum</a> and the <a href="../jardin-exotique-monaco/">Exotic Garden</a> are open in January.</li></ul>',
  book_lead='Monaco tours and Riviera day trips: book for rally week.',
  faq=[('When is the Monte-Carlo Rally 2027?','The 95th edition runs from Thursday 21 to Sunday 24 January 2027, finishing on Port Hercule in Monaco.'),
       ('Where is the Monte-Carlo Rally service park?','In Gap, in the Hautes-Alpes.'),
       ('When is the 2027 Monte-Carlo Historic Rally?','From 27 January to 3 February 2027, for its 29th edition.')],
  cards_t='What to see in Monaco', cards=[dict(href='french-riviera/monaco/',photo='monaco',name='Monaco',txt='Our full guide to the Principality.'),dict(href='french-riviera/grand-prix-de-monaco/',photo='grand-prix-de-monaco',name='Monaco Grand Prix',txt='Formula 1 in May, through the streets.'),dict(href='french-riviera/rocher-de-monaco/',photo='rocher-de-monaco',name='The Rock',txt='Monaco’s old town on foot.')]))

# ---------------------------------------------------------------- F. Route du Mimosa
F = dict(photo='mandelieu-la-napoule', og='mandelieu-la-napoule', acts=[({'fr':'cote-d-azur/grasse','en':'french-riviera/grasse'},0),({'fr':'cote-d-azur/grasse','en':'french-riviera/grasse'},1),({'fr':'cote-d-azur/mandelieu-la-napoule','en':'french-riviera/mandelieu-la-napoule'},0)],
 event={'fr':{"name":"Fête du Mimosa 2027 à Mandelieu-La Napoule","startDate":"2027-02-10","endDate":"2027-02-14","location":{"@type":"Place","name":"Mandelieu-La Napoule","address":"06210 Mandelieu-La Napoule, France"},"description":"Corsos fleuris, défilés et feu d’artifice ; thème 2027 : « Le mimosa entre en jeu »."},
        'en':{"name":"Mimosa Festival 2027 in Mandelieu-La Napoule","startDate":"2027-02-10","endDate":"2027-02-14","location":{"@type":"Place","name":"Mandelieu-La Napoule","address":"06210 Mandelieu-La Napoule, France"},"description":"Flower parades, processions and fireworks; 2027 theme: “Le mimosa entre en jeu”."}},
 fr=dict(path='cote-d-azur/route-du-mimosa', home='Accueil', crumbs=[('Côte d’Azur','cote-d-azur/')], crumb_last='Route du Mimosa et Fête du Mimosa 2027',
  title='Route du Mimosa et Fête du Mimosa 2027 : dates et étapes',
  desc='La Route du Mimosa relie Bormes-les-Mimosas à Grasse sur 130 km, de janvier à mars. Les étapes, la Fête du Mimosa de Mandelieu (10-14 février 2027) et les corsos.',
  h1='Route du Mimosa et Fête du Mimosa 2027',
  lead='De janvier à mars, le mimosa fleurit sur 130 km entre Bormes-les-Mimosas et Grasse. Les étapes, les corsos et la Fête du Mimosa de Mandelieu, du 10 au 14 février 2027.',
  body='<p>En plein hiver, quand le reste de l’Europe est gris, les collines entre le Var et les Alpes-Maritimes se couvrent de pompons jaunes. La Route du Mimosa suit cette floraison sur 130 kilomètres, de Bormes-les-Mimosas à Grasse. La meilleure période va de janvier à mars, avec un pic en février.</p>'
   '\n<h2>Les 8 étapes de la route</h2><ol class="agenda">'
   '<li class="ag"><span class="ag__d">km 0</span><div class="ag__b"><strong>Bormes-les-Mimosas</strong><p>Le point de départ : un village médiéval perché, capitale du mimosa dans le Var, avec plus de 90 espèces.</p></div></li>'
   '<li class="ag"><span class="ag__d">km 17</span><div class="ag__b"><strong>Rayol-Canadel-sur-Mer</strong><p>Un village de la corniche des Maures, en direction de Saint-Tropez.</p></div></li>'
   '<li class="ag"><span class="ag__d"></span><div class="ag__b"><strong>Sainte-Maxime</strong><p>Son corso du mimosa défile le dimanche 7 février 2027 à 14 h 30 ; gratuit en promenoir, payant en tribune.</p></div></li>'
   '<li class="ag"><span class="ag__d">km 59</span><div class="ag__b"><strong><a href="../frejus-saint-raphael/">Saint-Raphaël</a></strong><p>Au pied du <a href="../massif-de-l-esterel/">massif de l’Estérel</a> et de ses roches rouges.</p></div></li>'
   '<li class="ag"><span class="ag__d"></span><div class="ag__b"><strong><a href="../mandelieu-la-napoule/">Mandelieu-La Napoule</a></strong><p>La capitale du mimosa, avec sa grande fête de février.</p></div></li>'
   '<li class="ag"><span class="ag__d">km 122</span><div class="ag__b"><strong>Tanneron</strong><p>Le massif où les collines de mimosa sont les plus spectaculaires.</p></div></li>'
   '<li class="ag"><span class="ag__d"></span><div class="ag__b"><strong>Pégomas</strong><p>Un village entre mimosas et eucalyptus, au bord de la Siagne.</p></div></li>'
   '<li class="ag"><span class="ag__d">km 130</span><div class="ag__b"><strong><a href="../grasse/">Grasse</a></strong><p>L’arrivée, dans la capitale mondiale du parfum.</p></div></li></ol>'
   '\n<h2>La Fête du Mimosa de Mandelieu 2027</h2><p>Elle a lieu du mercredi 10 au dimanche 14 février 2027, sur le thème « Le mimosa entre en jeu ». Au programme : défilés, animations, distributions de mimosa et feu d’artifice. Le temps fort est le grand corso fleuri du dimanche après-midi, avec des chars couverts de mimosa, entre les plages, le port et le château de La Napoule. La fête existe depuis 1931.</p>'
   '\n<h2>Nos conseils</h2><ul><li><strong>Prenez deux ou trois jours</strong> : la route se fait en voiture, avec des arrêts dans chaque village.</li><li><strong>Finissez avant la nuit</strong> : en février, le soleil se couche tôt derrière l’Estérel ; prévoyez vos dernières étapes avant 17 h 30.</li><li><strong>Couplez avec les autres fêtes</strong> : le Carnaval de Nice et la Fête du Citron de Menton ont lieu au même moment.</li></ul>',
  book_lead='Atelier de création de parfum à Grasse ou excursion dans les villages perchés : à réserver pour février.',
  faq=[('Quand a lieu la Fête du Mimosa 2027 à Mandelieu ?','Du mercredi 10 au dimanche 14 février 2027, avec le grand corso fleuri le dimanche après-midi.'),
       ('Quelle est la meilleure période pour la Route du Mimosa ?','De janvier à mars, avec la floraison la plus forte en février.'),
       ('Quelle est la longueur de la Route du Mimosa ?','130 kilomètres, de Bormes-les-Mimosas à Grasse, en huit étapes.')],
  cards_t='Sur la route', cards=[dict(href='cote-d-azur/mandelieu-la-napoule/',photo='mandelieu-la-napoule',name='Mandelieu-La Napoule',txt='La capitale du mimosa et son château.'),dict(href='cote-d-azur/grasse/',photo='grasse',name='Grasse',txt='La capitale mondiale du parfum.'),dict(href='cote-d-azur/frejus-saint-raphael/',photo='frejus-saint-raphael',name='Fréjus et Saint-Raphaël',txt='Une étape de la route, au pied de l’Estérel.')]),
 en=dict(path='french-riviera/mimosa-route', home='Home', crumbs=[('French Riviera','french-riviera/')], crumb_last='Mimosa Route and Mimosa Festival 2027',
  title='Mimosa Route and Mimosa Festival 2027: Dates and Stops',
  desc='The Mimosa Route runs 130 km from Bormes-les-Mimosas to Grasse, January to March. The stops, the Mandelieu Mimosa Festival (10-14 February 2027) and the parades.',
  h1='Mimosa Route and Mimosa Festival 2027',
  lead='From January to March, mimosa blooms along 130 km between Bormes-les-Mimosas and Grasse. The stops, the parades and the Mandelieu Mimosa Festival, 10 to 14 February 2027.',
  body='<p>In midwinter, while the rest of Europe is grey, the hills between the Var and the Alpes-Maritimes turn yellow with mimosa. The Mimosa Route follows the blossom for 130 kilometres, from Bormes-les-Mimosas to Grasse. The best time is January to March, peaking in February.</p>'
   '\n<h2>The 8 stops on the route</h2><ol class="agenda">'
   '<li class="ag"><span class="ag__d">km 0</span><div class="ag__b"><strong>Bormes-les-Mimosas</strong><p>The starting point: a hilltop medieval village, the Var’s mimosa capital, with more than 90 species.</p></div></li>'
   '<li class="ag"><span class="ag__d">km 17</span><div class="ag__b"><strong>Rayol-Canadel-sur-Mer</strong><p>A village on the Corniche des Maures, towards Saint-Tropez.</p></div></li>'
   '<li class="ag"><span class="ag__d"></span><div class="ag__b"><strong>Sainte-Maxime</strong><p>Its mimosa parade takes place on Sunday 7 February 2027 at 2.30pm; free standing, paid grandstand seats.</p></div></li>'
   '<li class="ag"><span class="ag__d">km 59</span><div class="ag__b"><strong><a href="../frejus-saint-raphael/">Saint-Raphaël</a></strong><p>At the foot of the <a href="../esterel-massif/">Esterel massif</a> and its red rocks.</p></div></li>'
   '<li class="ag"><span class="ag__d"></span><div class="ag__b"><strong><a href="../mandelieu-la-napoule/">Mandelieu-La Napoule</a></strong><p>The mimosa capital, with its big February festival.</p></div></li>'
   '<li class="ag"><span class="ag__d">km 122</span><div class="ag__b"><strong>Tanneron</strong><p>The massif where the mimosa-covered hills are most spectacular.</p></div></li>'
   '<li class="ag"><span class="ag__d"></span><div class="ag__b"><strong>Pégomas</strong><p>A village among mimosa and eucalyptus, on the river Siagne.</p></div></li>'
   '<li class="ag"><span class="ag__d">km 130</span><div class="ag__b"><strong><a href="../grasse/">Grasse</a></strong><p>The finish, in the world capital of perfume.</p></div></li></ol>'
   '\n<h2>The 2027 Mandelieu Mimosa Festival</h2><p>It runs from Wednesday 10 to Sunday 14 February 2027, on the theme “Le mimosa entre en jeu”. The programme includes parades, street entertainment, mimosa giveaways and fireworks. The highlight is the big flower parade on Sunday afternoon, with floats covered in mimosa, between the beaches, the port and the Château de La Napoule. The festival dates back to 1931.</p>'
   '\n<h2>Our tips</h2><ul><li><strong>Take two or three days</strong>: the route is done by car, stopping in each village.</li><li><strong>Finish before dark</strong>: in February, the sun sets early behind the Esterel; plan your last stops before 5.30pm.</li><li><strong>Combine it with the other festivals</strong>: the Nice Carnival and the Menton Lemon Festival take place at the same time.</li></ul>',
  book_lead='A perfume-making workshop in Grasse or a hilltop village tour: book for February.',
  faq=[('When is the 2027 Mimosa Festival in Mandelieu?','From Wednesday 10 to Sunday 14 February 2027, with the big flower parade on Sunday afternoon.'),
       ('When is the best time for the Mimosa Route?','January to March, with the strongest blossom in February.'),
       ('How long is the Mimosa Route?','130 kilometres, from Bormes-les-Mimosas to Grasse, in eight stops.')],
  cards_t='Along the route', cards=[dict(href='french-riviera/mandelieu-la-napoule/',photo='mandelieu-la-napoule',name='Mandelieu-La Napoule',txt='The mimosa capital and its castle.'),dict(href='french-riviera/grasse/',photo='grasse',name='Grasse',txt='The world capital of perfume.'),dict(href='french-riviera/frejus-saint-raphael/',photo='frejus-saint-raphael',name='Fréjus and Saint-Raphaël',txt='A stop on the route, below the Esterel.')]))

PAGES = [A, B, C, D, E, F]
if __name__ == '__main__':
    for p in PAGES:
        for lang in ('fr', 'en'):
            print(build(p, lang))
