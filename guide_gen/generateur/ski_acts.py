import re
R='/home/claude/'
TICK=open('/tmp/g/quimper_acts.py').read().split("TICK='")[1].split("'\n")[0]
SNOW=('auvergne-rhone-alpes-l132103/snow-winter-sports-tc113/','Rhone-Alpes/d24268-ttd')
SNOWT=('Activités de neige dans les Alpes','Raquettes, cours de ski et sorties guidées dans les stations des Alpes du Nord.','Snow activities in the Alps','Snowshoeing, ski lessons and guided outings in the northern Alps resorts.')
RA='Rhone-Alpes/d24268-ttd'; DORD='Bergerac/d24181-ttd'; LOURDES='Lourdes/d24041-ttd'
GAV='tours/Lourdes/Discovery-of-the-Circus-of-Gavarnie-half-day-afternoon/d24041-417001P7'
# page: (fr path, en path, fr title, en title, acts[(frT,frD,enT,enD,gyg,via)])
P=[
('alpes/tignes','french-alps/tignes','à Tignes','in Tignes',[
 ("Transfert privé vers l'aéroport de Genève","Le trajet du retour en voiture privée, de Tignes ou Val d'Isère jusqu'à l'aéroport de Genève.","Private transfer to Geneva airport","The return trip by private car, from Tignes or Val d'Isère to Geneva airport.",None,'tours/France/Private-Transfer-From-Val-D-Isere-or-Tignes-to-Geneva/d51-378737P13'),
 SNOWT+SNOW]),
('alpes/val-d-isere','french-alps/val-d-isere',"à Val d'Isère","in Val d'Isère",[
 ("Transfert depuis l'aéroport de Genève","Voiture privée de l'aéroport de Genève jusqu'à votre hébergement à Val d'Isère.","Transfer from Geneva airport","Private car from Geneva airport to your accommodation in Val d'Isère.",None,'tours/Geneva/Geneva-Airport-GVA-to-Val-dIsere-FR-Arrival-Private-Car-Transfer/d578-128285P1374'),
 SNOWT+SNOW]),
('alpes/val-thorens','french-alps/val-thorens','à Val Thorens','in Val Thorens',[
 ("Transfert depuis l'aéroport de Genève","Transfert privé de l'aéroport de Genève jusqu'à Val Thorens, skis compris.","Transfer from Geneva airport","Private transfer from Geneva airport to Val Thorens, skis included.",None,'tours/Geneva/Geneva-Airport-GVA-to-Val-Thorens-Private-Ski-Transfer/d578-5618417P26'),
 ("Transfert depuis Lyon","Trajet privé entre Lyon et Val Thorens.","Transfer from Lyon","Private ride between Lyon and Val Thorens.",None,'tours/Lyon/Private-Lyon-Val-Thorens-Ride/d829-214567P39'),
 SNOWT+SNOW]),
('alpes/meribel','french-alps/meribel','à Méribel','in Méribel',[
 ("Activités dans les 3 Vallées","Raquettes et parapente à Courchevel, reliée à Méribel par les pistes.","Activities in the 3 Valleys","Snowshoeing and paragliding in Courchevel, linked to Méribel by the slopes.",'courchevel-l201172/',RA),
 ("Transfert depuis l'aéroport de Lyon","Voiture privée de l'aéroport de Lyon-Saint-Exupéry jusqu'à Méribel.","Transfer from Lyon airport","Private car from Lyon-Saint-Exupéry airport to Méribel.",None,'tours/Lyon/Private-Transfer-Lyon-Airport-to-Meribel/d829-214567P40')]),
('alpes/les-menuires','french-alps/les-menuires','aux Menuires','in Les Menuires',[
 ("Activités dans les 3 Vallées","Raquettes et parapente à Courchevel, à l'autre bout du domaine des 3 Vallées.","Activities in the 3 Valleys","Snowshoeing and paragliding in Courchevel, at the other end of the 3 Valleys ski area.",'courchevel-l201172/',RA),
 SNOWT+SNOW]),
('alpes/les-arcs','french-alps/les-arcs','aux Arcs','in Les Arcs',[
 ("Transfert vers Arc 1950 ou Arc 2000","Voiture privée de l'aéroport de Lyon jusqu'à Arc 1950 ou Arc 2000.","Transfer to Arc 1950 or Arc 2000","Private car from Lyon airport to Arc 1950 or Arc 2000.",None,'tours/Lyon/Private-Transfer-from-Lyon-Airport-to-Les-Arcs-1950-2000/d829-214567P44'),
 ("Transfert vers Arc 1600 ou Arc 1800","Voiture privée de l'aéroport de Lyon jusqu'à Arc 1600 ou Arc 1800.","Transfer to Arc 1600 or Arc 1800","Private car from Lyon airport to Arc 1600 or Arc 1800.",None,'tours/Lyon/Private-Transfer-from-Lyon-Airport-to-Les-Arcs-1600-1800/d829-214567P45'),
 SNOWT+SNOW]),
('alpes/avoriaz','french-alps/avoriaz','à Avoriaz','in Avoriaz',[
 ("Transfert depuis Genève","Navette de l'aéroport de Genève à Morzine, ou voiture privée jusqu'à Avoriaz.","Transfer from Geneva","Shuttle from Geneva airport to Morzine, or a private car up to Avoriaz.",'canton-de-geneve-l54/depuis-geneve-transfert-aller-simple-de-l-aeroport-de-geneve-a-morzine-t565388/','tours/Geneva/Geneva-to-Morzine-Avoriaz-or-Les-Gets-Private-Transfer/d578-5577630P11'),
 ("Jeu d'évasion dans Avoriaz","Jeu de piste en extérieur sur téléphone, dans les rues de la station.","Escape game in Avoriaz","Outdoor phone-based trail game through the resort's streets.",None,'tours/France/Curse-of-the-Doomed-Passage-Escape-Game-in-Avoriaz/d51-378394P167'),
 SNOWT+SNOW]),
('alpes/la-clusaz','french-alps/la-clusaz','à La Clusaz','in La Clusaz',[
 ("Activités à La Clusaz","Parapente biplace et sorties en montagne autour de la station.","Activities in La Clusaz","Tandem paragliding and mountain outings around the resort.",'la-clusaz-l255105/','tours/France/Baptism-in-Paragliding-in-La-Clusaz/d51-5591796P1'),
 ("Transfert depuis l'aéroport de Genève","Voiture privée de l'aéroport de Genève jusqu'à La Clusaz.","Transfer from Geneva airport","Private car from Geneva airport to La Clusaz.",None,'tours/Geneva/Geneva-Int-Airport-GVA-to-La-Clusaz-Arrival-Private-Transfer/d578-350808P739')]),
('lot/gouffre-de-padirac','lot/gouffre-de-padirac','autour de Padirac','around Padirac',[
 ("Visites à Rocamadour","Visites guidées de la cité, à une quinzaine de kilomètres du gouffre.","Tours in Rocamadour","Guided tours of the village, about fifteen kilometres from the chasm.",'rocamadour-l190520/',None),
 ("Rocamadour et Padirac depuis Toulouse","Transfert privé depuis Toulouse pour voir les deux sites dans la journée.","Rocamadour and Padirac from Toulouse","Private transfer from Toulouse to see both sites in a day.",None,'tours/Toulouse/Rocamadour-and-Padirac-Chasm-Private-Tour-from-Toulouse/d812-5703615P4')]),
('aquitaine/jardins-de-marqueyssac','aquitaine/jardins-de-marqueyssac','à Marqueyssac','at Marqueyssac',[
 ("Billets et visites à Marqueyssac","Les offres disponibles pour les jardins et leurs environs.","Marqueyssac tickets and tours","Offers available for the gardens and the surrounding area.",'the-marqueyssac-gardens-l139346/',DORD),
 ("La Dordogne en canoë","Descente de la rivière au pied des châteaux de la vallée.","The Dordogne by canoe","Paddle down the river below the valley's castles.",'domme-l100749/sarlat-la-caneda-la-vallee-de-la-dordogne-en-canoe-t431922/','tours/Bergerac/Private-guided-tour-of-Beynac-castle-and-La-Roque-Gageac/d24181-69161P15')]),
('aquitaine/chateau-des-milandes','aquitaine/chateau-des-milandes','autour des Milandes','around Les Milandes',[
 ("Château de Castelnaud","Le château voisin, sur la même commune, et son musée de la guerre au Moyen Âge.","Château de Castelnaud","The neighbouring castle, in the same village, with its museum of medieval warfare.",'castelnaud-la-chapelle-l139351/chateau-de-castelnaud-musee-de-la-guerre-au-moyen-age-billet-d-entree-t1079053/',DORD),
 ("Canoë et vallée des châteaux","Canoë sur la Dordogne et circuits entre les châteaux du Périgord noir.","Canoeing and the valley of castles","Canoeing on the Dordogne and tours of the Périgord Noir castles.",'castelnaud-la-chapelle-l139351/','tours/Bergerac/La-vallee-des-5-chateaux/d24181-67850P3')]),
('pyrenees/cauterets','pyrenees/cauterets','autour de Cauterets','around Cauterets',[
 ("Cirque de Gavarnie","Demi-journée guidée au cirque, à environ une heure de route de Cauterets.","Cirque de Gavarnie","Guided half-day at the cirque, about an hour's drive from Cauterets.",None,GAV),
 ("Activités autour de Lourdes","Visites et sorties en eaux vives au départ de Lourdes, à une demi-heure de Cauterets.","Activities around Lourdes","Tours and white-water outings from Lourdes, half an hour from Cauterets.",None,LOURDES)]),
('pyrenees/grand-tourmalet','pyrenees/grand-tourmalet','autour du Grand Tourmalet','around Grand Tourmalet',[
 ("Cirque de Gavarnie","Demi-journée guidée au cirque, à moins d'une heure de Barèges.","Cirque de Gavarnie","Guided half-day at the cirque, less than an hour from Barèges.",None,GAV),
 ("Activités autour de Lourdes","Visites et sorties en eaux vives au départ de Lourdes.","Activities around Lourdes","Tours and white-water outings from Lourdes.",None,LOURDES)]),
]
for fr,en,tf,te,acts in P:
  for lang,root,path in (('fr','clicandsite-guide',fr),('en','clicandsite-guide-en',en)):
    camp=f'clicandsite-{lang}-'+path.replace('/','-')
    gd='getyourguide.fr' if lang=='fr' else 'getyourguide.com'
    vp='https://www.viator.com/fr-FR/' if lang=='fr' else 'https://www.viator.com/'
    lis=''
    for a in acts:
      t,d=(a[0],a[1]) if lang=='fr' else (a[2],a[3]); g,v=a[4],a[5]
      btn=''
      if g: btn+=f'<a class="bk bk--gyg" href="https://www.{gd}/{g}?partner_id=XMYSXGR&amp;cmp={camp}&amp;utm_medium=online_publisher" rel="sponsored nofollow noopener" target="_blank">{TICK}{"Billets" if lang=="fr" else "Tickets"}</a>'
      if v:
        lab=("Autres billets" if lang=='fr' else "More tickets") if g else ("Voir l'offre" if lang=='fr' else "See the offer")
        btn+=f'<a class="bk bk--via" href="{vp}{v}?pid=P00331213&amp;mcid=42383&amp;medium=link&amp;campaign={camp}" rel="sponsored nofollow noopener" target="_blank">{lab}</a>'
      lis+=f'<li class="act">\n  <h3 class="act__t">{t}</h3><p class="act__d">{d}</p>\n  <p class="act__btns">{btn}</p>\n</li>'
    H=('Activités à réserver '+tf) if lang=='fr' else ('Activities to book '+te)
    lead="Réservation en ligne ; les conditions d'annulation sont indiquées sur chaque offre." if lang=='fr' else "Book online; cancellation terms are shown on each offer."
    note='Liens partenaires.' if lang=='fr' else 'Partner links.'
    book=f'<section class="book" id="reserver" aria-labelledby="reserver-t">\n      <h2 id="reserver-t" class="book__t">{H}</h2>\n      <p class="book__lead">{lead}</p>\n      <ul class="acts">{lis}</ul>\n      <p class="aff-note">{note}</p>\n    </section>'
    p=f'{R}{root}/{path}/index.html'; q=open(p).read()
    assert 'class="book"' not in q, p
    anchor='<h2>Questions fréquentes</h2>' if lang=='fr' else '<h2>Frequently asked questions</h2>'
    assert anchor in q, p
    q=q.replace(anchor,book+'\n    '+anchor,1)
    open(p,'w').write(q); print('ok',p)
