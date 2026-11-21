import sys; sys.path.insert(0,'/tmp/g')
from winter_gen import build
def S(fr, en): return {'fr': fr, 'en': en}
# (mois FR, mois EN, titre FR, titre EN, lien FR, lien EN, texte FR, texte EN)
M = [
 ('Janvier','January','Le Rallye Monte-Carlo','The Monte-Carlo Rally','cote-d-azur/rallye-monte-carlo','french-riviera/monte-carlo-rally',
  'La 95e édition se court du 21 au 24 janvier 2027, avec l’arrivée sur le port Hercule de Monaco. Une bonne occasion de voir la Côte d’Azur sans la foule de l’été.',
  'The 95th edition runs from 21 to 24 January 2027, finishing on Port Hercule in Monaco. A good chance to see the French Riviera without the summer crowds.'),
 ('Février','February','Le Carnaval de Nice et la Fête du Citron','The Nice Carnival and the Lemon Festival','cote-d-azur/carnaval-de-nice','french-riviera/nice-carnival',
  'Le Carnaval de Nice a lieu du 9 au 28 février 2027 et la Fête du Citron de Menton du 13 au 28 février 2027 : deux grands rendez-vous à une demi-heure l’un de l’autre. C’est aussi le mois des vacances au ski.',
  'The Nice Carnival runs from 9 to 28 February 2027 and the Menton Lemon Festival from 13 to 28 February 2027: two big events half an hour apart. It is also the month of the ski holidays.'),
 ('Avril','April','Giverny et les jardins de Monet','Giverny and Monet’s gardens','paris/giverny','paris/giverny',
  'Les jardins de Monet rouvrent chaque printemps, début avril, et sont fermés en hiver. Avril et mai, avec les tulipes puis les glycines, sont les plus beaux mois pour y aller depuis Paris.',
  'Monet’s gardens reopen every spring, in early April, and close for the winter. April and May, with the tulips and then the wisteria, are the best months to go from Paris.'),
 ('Mai','May','Les châteaux de la Loire','The Loire Valley châteaux','chateaux-de-la-loire/chenonceau','loire-valley/chenonceau',
  'Avant la foule de l’été, mai est idéal pour Chenonceau, Chambord, Villandry et ses jardins, à vélo ou en voiture, avec les longs week-ends de l’Ascension et de la Pentecôte.',
  'Before the summer crowds, May is ideal for Chenonceau, Chambord and the gardens of Villandry, by bike or by car, with the long bank-holiday weekends.'),
 ('Juin','June','L’Armada de Rouen','The Rouen Armada','normandie/rouen','normandy/rouen',
  'Du 17 au 27 juin 2027, la 9e Armada réunit de grands voiliers venus du monde entier sur les quais de Seine. L’entrée est libre et c’est l’un des grands événements de 2027.',
  'From 17 to 27 June 2027, the 9th Armada brings tall ships from around the world to the banks of the Seine in Rouen. Entry is free and it is one of the big events of 2027.'),
 ('Juillet','July','La lavande en Provence','Lavender in Provence','provence/gordes','provence/gordes',
  'La lavande fleurit en général de fin juin à mi-juillet autour de Gordes, de l’abbaye de Sénanque et du plateau de Valensole. Venez tôt le matin pour la lumière et le calme.',
  'Lavender usually blooms from late June to mid-July around Gordes, Sénanque Abbey and the Valensole plateau. Come early in the morning for the light and the calm.'),
 ('Août','August','Le Festival interceltique de Lorient et la Bretagne','The Lorient Interceltic Festival and Brittany','bretagne/','brittany/',
  'Le Festival interceltique de Lorient est annoncé du 30 juillet au 8 août 2027. Profitez-en pour Belle-Île, le golfe du Morbihan et Carnac, tout proches.',
  'The Lorient Interceltic Festival is scheduled from 30 July to 8 August 2027. Combine it with Belle-Île, the Gulf of Morbihan and Carnac, all close by.'),
 ('Septembre','September','La Corse','Corsica','corse/','corsica/',
  'La mer est encore chaude, les randonnées redeviennent agréables et les prix baissent après le 15 août : septembre est le meilleur mois pour la Corse, de Bonifacio au cap Corse.',
  'The sea is still warm, hiking becomes pleasant again and prices drop after mid-August: September is the best month for Corsica, from Bonifacio to Cap Corse.'),
 ('Octobre','October','La Dordogne et le Périgord','The Dordogne and Périgord','aquitaine/sarlat-la-caneda','aquitaine/sarlat-la-caneda',
  'Les couleurs d’automne sur la vallée de la Dordogne, les marchés de Sarlat et les châteaux de Beynac et de Castelnaud, sans les embouteillages de l’été.',
  'Autumn colours over the Dordogne valley, the Sarlat markets and the castles of Beynac and Castelnaud, without the summer traffic jams.'),
 ('Décembre','December','Les marchés de Noël d’Alsace','The Alsace Christmas markets','idees/marches-de-noel-alsace','ideas/alsace-christmas-markets',
  'Strasbourg, Colmar, Riquewihr, Kaysersberg et Eguisheim : l’Alsace reste la destination de Noël la plus recherchée de France.',
  'Strasbourg, Colmar, Riquewihr, Kaysersberg and Eguisheim: Alsace remains France’s most popular Christmas destination.'),
]
def body(lang):
    i = 0 if lang == 'fr' else 1
    intro = ('<p>Pour bien choisir ses vacances en France en 2027, le plus simple est de partir de la saison. Voici, mois par mois, les destinations et les événements que nous conseillons, avec les dates déjà annoncées pour 2027. Chaque titre renvoie vers notre guide détaillé.</p>'
             if lang == 'fr' else
             '<p>The easiest way to plan a holiday in France in 2027 is to start from the season. Here, month by month, are the destinations and events we recommend, with the dates already announced for 2027. Each heading links to our detailed guide.</p>')
    h = '\n<h2>Où partir en France en 2027, mois par mois</h2>' if lang == 'fr' else '\n<h2>Where to go in France in 2027, month by month</h2>'
    items = ''.join(f'\n<h3>{m[i]} : <a href="../../{m[4+i]}{"" if m[4+i].endswith("/") else "/"}">{m[2+i]}</a></h3><p>{m[6+i]}</p>'.replace(' : ', ': ' if lang == 'en' else ' : ') for m in M)
    tips = ('\n<h2>Nos conseils pour réserver</h2><ul><li><strong>Réservez tôt pour les grands événements</strong> : les hôtels de Nice, Menton et Rouen se remplissent des mois à l’avance pour le Carnaval, la Fête du Citron et l’Armada.</li><li><strong>Préférez les ailes de saison</strong> : mai, juin et septembre offrent le beau temps sans la foule ni les prix de juillet-août.</li><li><strong>Combinez les régions proches</strong> : la Côte d’Azur et la Provence, la Normandie et la Bretagne, ou le Pays basque et les Pyrénées se visitent facilement dans le même séjour.</li></ul><p class="maj">Dates relevées en novembre 2026 auprès des organisateurs ; elles peuvent encore changer, vérifiez avant de réserver.</p>'
            if lang == 'fr' else
            '\n<h2>Our booking tips</h2><ul><li><strong>Book early for the big events</strong>: hotels in Nice, Menton and Rouen fill up months ahead for the Carnival, the Lemon Festival and the Armada.</li><li><strong>Go in the shoulder seasons</strong>: May, June and September bring good weather without the crowds or the July-August prices.</li><li><strong>Combine nearby regions</strong>: the French Riviera and Provence, Normandy and Brittany, or the Basque Country and the Pyrenees are easy to visit in one trip.</li></ul><p class="maj">Dates checked in November 2026 with the organisers; they may still change, check before booking.</p>')
    return intro + h + items + tips
P = dict(photo='mont-saint-michel', og='mont-saint-michel',
 acts=[({'fr':'cote-d-azur/carnaval-de-nice','en':'french-riviera/nice-carnival'},0), ({'fr':'paris/giverny','en':'paris/giverny'},0)],
 fr=dict(path='idees/ou-partir-en-france-en-2027', home='Accueil', crumbs=[('Idées','idees/')], crumb_last='Où partir en France en 2027',
  title='Où partir en France en 2027 ? Nos idées mois par mois',
  desc='Où partir en France en 2027 ? Carnaval de Nice, Armada de Rouen, lavande, Lorient, Corse, marchés de Noël : nos idées mois par mois, avec les dates 2027.',
  h1='Où partir en France en 2027 ? Nos idées mois par mois',
  lead='Du Rallye Monte-Carlo en janvier aux marchés de Noël d’Alsace en décembre : une destination et un rendez-vous pour chaque mois de 2027.',
  body=body('fr'), book_lead='Quelques activités à réserver dès maintenant pour les grands rendez-vous de 2027.',
  faq=[('Quels sont les grands événements en France en 2027 ?','Le Rallye Monte-Carlo du 21 au 24 janvier, le Carnaval de Nice du 9 au 28 février, la Fête du Citron de Menton du 13 au 28 février, l’Armada de Rouen du 17 au 27 juin et le Festival interceltique de Lorient du 30 juillet au 8 août 2027.'),
       ('Quel est le meilleur mois pour partir en France ?','Mai, juin et septembre : il fait beau dans la plupart des régions, et il y a moins de monde et des prix plus bas qu’en juillet-août.'),
       ('Où partir en France en hiver 2027 ?','Sur la Côte d’Azur pour le Carnaval de Nice et la Fête du Citron en février, à la montagne pour le ski, ou en Alsace pour les marchés de Noël en décembre.')],
  cards_t='Les rendez-vous à ne pas manquer', cards=[dict(href='normandie/rouen/',photo='rouen',name='Armada de Rouen',txt='Du 17 au 27 juin 2027.'),dict(href='cote-d-azur/carnaval-de-nice/',photo='carnaval-nice',name='Carnaval de Nice',txt='Du 9 au 28 février 2027.'),dict(href='idees/marches-de-noel-alsace/',photo='riquewihr',name='Noël en Alsace',txt='Strasbourg, Colmar, Riquewihr.')]),
 en=dict(path='ideas/where-to-go-in-france-in-2027', home='Home', crumbs=[('Ideas','ideas/')], crumb_last='Where to go in France in 2027',
  title='Where to go in France in 2027: month-by-month ideas',
  desc='Where to go in France in 2027? Nice Carnival, Rouen Armada, lavender, Lorient festival, Corsica, Christmas markets: our month-by-month ideas with 2027 dates.',
  h1='Where to go in France in 2027: month-by-month ideas',
  lead='From the Monte-Carlo Rally in January to the Alsace Christmas markets in December: a destination and an event for every month of 2027.',
  body=body('en'), book_lead='A few activities to book now for the big events of 2027.',
  faq=[('What are the big events in France in 2027?','The Monte-Carlo Rally from 21 to 24 January, the Nice Carnival from 9 to 28 February, the Menton Lemon Festival from 13 to 28 February, the Rouen Armada from 17 to 27 June and the Lorient Interceltic Festival from 30 July to 8 August 2027.'),
       ('What is the best month to visit France?','May, June and September: the weather is good in most regions, with fewer crowds and lower prices than in July and August.'),
       ('Where to go in France in winter 2027?','The French Riviera for the Nice Carnival and the Lemon Festival in February, the mountains for skiing, or Alsace for the Christmas markets in December.')],
  cards_t='Events not to miss', cards=[dict(href='normandy/rouen/',photo='rouen',name='Rouen Armada',txt='From 17 to 27 June 2027.'),dict(href='french-riviera/nice-carnival/',photo='carnaval-nice',name='Nice Carnival',txt='From 9 to 28 February 2027.'),dict(href='ideas/alsace-christmas-markets/',photo='riquewihr',name='Christmas in Alsace',txt='Strasbourg, Colmar, Riquewihr.')]))
for l in ('fr','en'):
    assert len(P[l]['title']) <= 58, (l, len(P[l]['title'])); assert len(P[l]['desc']) <= 165, (l, len(P[l]['desc']))
    print(build(P, l))
