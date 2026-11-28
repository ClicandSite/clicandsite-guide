import sys; sys.path.insert(0,'/tmp/s')
exec(open('/tmp/s/hubs_1128.py').read().split('# ---------- PYRÉNÉES')[0])
def two(fr_path,en_path,fr_h2,en_h2,fr_head,en_head,rows,fr_note,en_note,fr_txt,en_txt):
    # rows: (slug, fr_name, en_name, [fr cells], [en cells])
    ins(FR,fr_path,f'<h2 id="en-bref">{fr_h2}</h2>'+tbl(fr_head,[[a(f'../{fr_path}/{r[0]}/',r[1])]+r[3] for r in rows])+f'<p>{fr_note}</p>'+fr_txt)
    ins(EN,en_path,f'<h2 id="en-bref">{en_h2}</h2>'+tbl(en_head,[[a(f'../{en_path}/{r[0]}/',r[2])]+r[4] for r in rows])+f'<p>{en_note}</p>'+en_txt)
NF='Prix relevés sur les sites officiels pour 2026 ; chaque guide donne les horaires, l’accès et nos conseils.'
NE='Prices taken from official websites for 2026; each guide gives opening hours, access and our tips.'
# DORDOGNE / AQUITAINE
two('aquitaine','aquitaine','La Dordogne et Bordeaux en un coup d’œil','Dordogne and Bordeaux at a glance',['Lieu','Billet adulte 2026','Depuis Sarlat'],['Place','2026 adult ticket','From Sarlat'],[
 ('lascaux','Lascaux IV','Lascaux IV',[f'23{N}€','30 min'],['€23','30 min']),
 ('chateau-de-beynac','Château de Beynac','Beynac Castle',[f'12,50{N}€','15 min'],['€12.50','15 min']),
 ('chateau-de-castelnaud','Château de Castelnaud','Castelnaud Castle',[f'13,60{N}€','15 min'],['€13.60','15 min']),
 ('jardins-de-marqueyssac','Jardins de Marqueyssac','Marqueyssac Gardens',[f'12,90{N}€ (jumelé avec Castelnaud 24{N}€)','15 min'],['€12.90 (€24 combined with Castelnaud)','15 min']),
 ('chateau-des-milandes','Château des Milandes','Château des Milandes',[f'15{N}€, rapaces compris','25 min'],['€15, birds of prey show included','25 min']),
 ('la-roque-gageac','La Roque-Gageac','La Roque-Gageac',[f'Gabare dès 12,50{N}€ (avril à novembre)','15 min'],['Gabare boat from €12.50 (April to November)','15 min'])],NF,NE,
 f'<h3>Où se baser ?</h3><p>{a("../aquitaine/sarlat-la-caneda/","Sarlat")} est la meilleure base : Beynac, Castelnaud, Marqueyssac et La Roque-Gageac sont à un quart d’heure en voiture, Lascaux à une demi-heure. Il faut une voiture pour circuler entre les sites. Côté Gironde, {a("../aquitaine/bordeaux/","Bordeaux")} se combine avec {a("../aquitaine/saint-emilion/","Saint-Émilion")}, à environ 50 minutes, et la {a("../aquitaine/dune-du-pilat/","dune du Pilat")}, dont l’accès est gratuit (seul le parking est payant).</p>',
 f'<h3>Where to stay?</h3><p>{a("../aquitaine/sarlat-la-caneda/","Sarlat")} is the best base: Beynac, Castelnaud, Marqueyssac and La Roque-Gageac are a quarter of an hour away by car, Lascaux half an hour. You need a car to get between the sites. In the Gironde, {a("../aquitaine/bordeaux/","Bordeaux")} pairs with {a("../aquitaine/saint-emilion/","Saint-Émilion")}, about 50 minutes away, and the {a("../aquitaine/dune-du-pilat/","Dune du Pilat")}, which is free to visit (only parking is charged).</p>')
# CORSE
two('corse','corsica','La Corse en un coup d’œil','Corsica at a glance',['Lieu','À voir','Bon à savoir'],['Place','What to see','Good to know'],[
 ('bonifacio','Bonifacio','Bonifacio',['Haute ville, falaises, escalier du Roi d’Aragon',f'Escalier 5{N}€ ; 30 min de Porto-Vecchio'],['Upper town, cliffs, King of Aragon’s Staircase','Staircase €5; 30 min from Porto-Vecchio']),
 ('porto-vecchio','Porto-Vecchio','Porto-Vecchio',['Citadelle, plages de Palombaggia et Santa Giulia','2 h de Bastia en voiture'],['Citadel, Palombaggia and Santa Giulia beaches','2 h from Bastia by car']),
 ('ajaccio','Ajaccio','Ajaccio',['Maison Bonaparte, palais Fesch, îles Sanguinaires','3 h de Bastia, routes sinueuses'],['Maison Bonaparte, Palais Fesch, Sanguinaires islands','3 h from Bastia, winding roads']),
 ('corte','Corte','Corte',['Citadelle, musée de la Corse, Restonica',f'Musée 4{N}€ (5,50{N}€ avec expositions)'],['Citadel, Museum of Corsica, Restonica','Museum €4 (€5.50 with exhibitions)']),
 ('cap-corse','Cap Corse','Cap Corse',['Erbalunga, Nonza, Centuri, tours génoises','Une journée en voiture depuis Bastia'],['Erbalunga, Nonza, Centuri, Genoese towers','A day’s drive from Bastia']),
 ('calvi','Calvi','Calvi',['Citadelle génoise, plage de la Pinède','2 h de Bastia'],['Genoese citadel, Pinède beach','2 h from Bastia'])],
 'Temps de trajet et prix relevés dans nos guides, à partir des sites officiels.','Journey times and prices from our guides, based on official websites.',
 f'<h3>Comment s’organiser ?</h3><p>Les routes corses sont sinueuses : comptez large entre deux étapes. En une semaine, le plus simple est de choisir une moitié de l’île : le sud autour de {a("../corse/porto-vecchio/","Porto-Vecchio")} et {a("../corse/bonifacio/","Bonifacio")}, ou le nord entre {a("../corse/bastia/","Bastia")}, le {a("../corse/cap-corse/","cap Corse")} et {a("../corse/calvi/","Calvi")}. {a("../corse/corte/","Corte")}, au centre, fait le lien entre les deux.</p>',
 f'<h3>How to plan it?</h3><p>Corsican roads are winding: allow plenty of time between stops. In a week, the easiest plan is to choose half of the island: the south around {a("../corsica/porto-vecchio/","Porto-Vecchio")} and {a("../corsica/bonifacio/","Bonifacio")}, or the north between {a("../corsica/bastia/","Bastia")}, {a("../corsica/cap-corse/","Cap Corse")} and {a("../corsica/calvi/","Calvi")}. {a("../corsica/corte/","Corte")}, in the middle, links the two.</p>')
# PAYS BASQUE
two('pays-basque','basque-country','Le Pays basque en un coup d’œil','The Basque Country at a glance',['Lieu','À voir','Bon à savoir'],['Place','What to see','Good to know'],[
 ('biarritz','Biarritz','Biarritz',['Rocher de la Vierge, Grande Plage, phare','TGV direct depuis Paris, un peu plus de 4 h'],['Rocher de la Vierge, Grande Plage, lighthouse','Direct TGV from Paris, just over 4 h']),
 ('bayonne','Bayonne','Bayonne',['Quais de la Nive, cathédrale, Musée basque','TGV direct depuis Paris, 4 h environ'],['Nive quays, cathedral, Basque Museum','Direct TGV from Paris, about 4 h']),
 ('la-rhune','La Rhune','La Rhune',['Petit train à crémaillère de 1924',f'Aller-retour 26{N}€ (2026)'],['1924 rack railway','Return ticket €26 (2026)']),
 ('sare','Sare','Sare',['Village, grottes, gâteau basque',f'Grottes 10{N}€, réservation obligatoire'],['Village, caves, gâteau basque','Caves €10, booking required']),
 ('hendaye','Hendaye','Hendaye',['Plage, château d’Abbadia',f'Abbadia 12,90{N}€ ; Topo pour Saint-Sébastien'],['Beach, Château d’Abbadia','Abbadia €12.90; Topo train to San Sebastián']),
 ('espelette','Espelette','Espelette',['Façades aux piments, château des Barons','Marché le mercredi matin'],['Chilli-hung façades, Château des Barons','Market on Wednesday mornings'])],NF,NE,
 f'<p>La côte, de {a("../pays-basque/biarritz/","Biarritz")} à {a("../pays-basque/hendaye/","Hendaye")} en passant par {a("../pays-basque/saint-jean-de-luz/","Saint-Jean-de-Luz")}, se parcourt en train ou en voiture ; les villages de l’intérieur ({a("../pays-basque/ainhoa/","Ainhoa")}, {a("../pays-basque/sare/","Sare")}, {a("../pays-basque/espelette/","Espelette")}) demandent une voiture. Comptez deux ou trois jours pour voir l’essentiel.</p>',
 f'<p>The coast, from {a("../basque-country/biarritz/","Biarritz")} to {a("../basque-country/hendaye/","Hendaye")} via {a("../basque-country/saint-jean-de-luz/","Saint-Jean-de-Luz")}, can be done by train or car; the inland villages ({a("../basque-country/ainhoa/","Ainhoa")}, {a("../basque-country/sare/","Sare")}, {a("../basque-country/espelette/","Espelette")}) need a car. Allow two or three days to see the highlights.</p>')
# NORMANDIE
two('normandie','normandy','La Normandie en un coup d’œil','Normandy at a glance',['Lieu','À voir','Bon à savoir'],['Place','What to see','Good to know'],[
 ('mont-saint-michel','Mont-Saint-Michel','Mont-Saint-Michel',['Abbaye, village, marées',f'Abbaye 13{N}€ en basse saison, 16{N}€ en haute saison'],['Abbey, village, tides','Abbey €13 low season, €16 high season']),
 ('etretat','Étretat','Étretat',['Porte d’Aval, Aiguille, Manneporte','Pas de gare : train jusqu’au Havre puis car'],['Porte d’Aval, the Needle, Manneporte','No station: train to Le Havre then coach']),
 ('honfleur','Honfleur','Honfleur',['Vieux Bassin, église Sainte-Catherine',f'Musée Eugène-Boudin 9{N}€, fermé le mardi'],['Old Basin, St Catherine’s church','Eugène Boudin museum €9, closed Tuesdays']),
 ('caen','Caen','Caen',['Mémorial, château, abbayes',f'Mémorial 20,80{N}€'],['Memorial, castle, abbeys','Memorial €20.80']),
 ('rouen','Rouen','Rouen',['Cathédrale de Monet, Gros-Horloge','1 h 20 de Paris en train'],['Monet’s cathedral, Gros-Horloge','1 h 20 from Paris by train']),
 ('bayeux','Bayeux','Bayeux',['Cathédrale, vieille ville','Tapisserie au British Museum jusqu’en juillet 2027'],['Cathedral, old town','Tapestry at the British Museum until July 2027'])],NF,NE,
 f'<p>{a("../normandie/rouen/","Rouen")} se fait facilement dans la journée depuis Paris en train. Pour les {a("../normandie/plages-du-debarquement/","plages du Débarquement")}, {a("../normandie/bayeux/","Bayeux")} est la meilleure base, avec Arromanches et Omaha Beach à une vingtaine de minutes en voiture. {a("../normandie/deauville/","Deauville")} et {a("../normandie/trouville/","Trouville")} partagent la même gare.</p>',
 f'<p>{a("../normandy/rouen/","Rouen")} is an easy day trip from Paris by train. For the {a("../normandy/plages-du-debarquement/","D-Day beaches")}, {a("../normandy/bayeux/","Bayeux")} is the best base, with Arromanches and Omaha Beach about 20 minutes away by car. {a("../normandy/deauville/","Deauville")} and {a("../normandy/trouville/","Trouville")} share the same station.</p>')
# BRETAGNE
two('bretagne','brittany','La Bretagne en un coup d’œil','Brittany at a glance',['Lieu','À voir','Depuis Paris'],['Place','What to see','From Paris'],[
 ('rennes','Rennes','Rennes',['Parlement de Bretagne, marché des Lices','1 h 30 en TGV'],['Brittany Parliament, Lices market','1 h 30 by TGV']),
 ('saint-malo','Saint-Malo','Saint-Malo',['Remparts, Grand Bé à marée basse','2 h 15 en TGV direct'],['Ramparts, Grand Bé at low tide','2 h 15 by direct TGV']),
 ('golfe-du-morbihan','Golfe du Morbihan','Gulf of Morbihan',['Île aux Moines, cairn de Gavrinis','Vannes à 2 h 30 en TGV'],['Île aux Moines, Gavrinis cairn','Vannes 2 h 30 by TGV']),
 ('quimper','Quimper','Quimper',['Cathédrale Saint-Corentin, vieille ville','4 h en TGV direct'],['St Corentin cathedral, old town','4 h by direct TGV']),
 ('carnac','Carnac','Carnac',['Alignements de menhirs','45 min de Vannes en voiture'],['Standing stone alignments','45 min from Vannes by car']),
 ('ploumanach','Ploumanac’h','Ploumanac’h',['Côte de Granit Rose, phare de Mean Ruz','TGV jusqu’à Lannion via Guingamp'],['Pink Granite Coast, Mean Ruz lighthouse','TGV to Lannion via Guingamp'])],
 'Temps de trajet relevés dans nos guides, à partir des horaires SNCF.','Journey times from our guides, based on SNCF timetables.',
 f'<p>Le nord ({a("../bretagne/saint-malo/","Saint-Malo")}, {a("../bretagne/dinan/","Dinan")}, {a("../bretagne/cancale/","Cancale")}) se combine facilement avec le Mont-Saint-Michel. Le sud ({a("../bretagne/golfe-du-morbihan/","golfe du Morbihan")}, {a("../bretagne/carnac/","Carnac")}, {a("../bretagne/quiberon/","Quiberon")}) se visite depuis Vannes, et le Finistère depuis {a("../bretagne/quimper/","Quimper")}. Le {a("../bretagne/gr34-sentier-des-douaniers/","GR34")} longe toute la côte.</p>',
 f'<p>The north ({a("../brittany/saint-malo/","Saint-Malo")}, {a("../brittany/dinan/","Dinan")}, {a("../brittany/cancale/","Cancale")}) combines easily with Mont-Saint-Michel. The south ({a("../brittany/golfe-du-morbihan/","Gulf of Morbihan")}, {a("../brittany/carnac/","Carnac")}, {a("../brittany/quiberon/","Quiberon")}) is best visited from Vannes, and Finistère from {a("../brittany/quimper/","Quimper")}. The {a("../brittany/gr34-sentier-des-douaniers/","GR34")} runs along the whole coast.</p>')
