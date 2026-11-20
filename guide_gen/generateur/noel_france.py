import sys; sys.path.insert(0,'/tmp/g')
from winter_gen import build
# (date début, ville, lien FR, lien EN, texte FR, texte EN)
A = [
 ('12 nov.','12 Nov','Paris – La Défense','paris/noel-a-paris','paris/christmas-in-paris',
  'L’un des plus grands marchés de Noël d’Île-de-France, jusqu’au 31 décembre 2026.',
  'One of the largest Christmas markets in the Paris region, until 31 December 2026.'),
 ('14 nov.','14 Nov','Paris – Tuileries','paris/noel-a-paris','paris/christmas-in-paris',
  'Jusqu’au 3 janvier 2027, tous les jours de 11 h à 23 h 30.',
  'Until 3 January 2027, every day from 11 am to 11.30 pm.'),
 ('22 nov.','22 Nov','Paris – Champs-Élysées','paris/noel-a-paris','paris/christmas-in-paris',
  'Les illuminations s’allument le 22 novembre et le marché de Noël revient sur l’avenue, de la Concorde au rond-point, jusqu’au 4 janvier 2027.',
  'The lights are switched on on 22 November and the Christmas market returns to the avenue, from Concorde to the Rond-Point, until 4 January 2027.'),
 ('23 nov.','23 Nov','Colmar','alsace/colmar','alsace/colmar',
  'Six marchés dans la vieille ville jusqu’au 29 décembre ; le marché gourmand et la grande roue jusqu’au 3 janvier 2027.',
  'Six markets in the old town until 29 December; the food market and the big wheel until 3 January 2027.'),
 ('26 nov.','26 Nov','Paris – Notre-Dame','paris/noel-a-paris','paris/christmas-in-paris',
  'Square René-Viviani, face à la cathédrale, jusqu’au 27 décembre 2026.',
  'Square René-Viviani, opposite the cathedral, until 27 December 2026.'),
 ('27 nov.','27 Nov','Strasbourg','alsace/strasbourg','alsace/strasbourg',
  'Le Christkindelsmärik de la place Broglie, le plus ancien de France, jusqu’au 24 décembre 2026.',
  'The Christkindelsmärik on Place Broglie, France’s oldest, until 24 December 2026.'),
 ('27 nov.','27 Nov','Riquewihr et Kaysersberg','idees/marches-de-noel-alsace','ideas/alsace-christmas-markets',
  'Jusqu’au 20 décembre 2026 ; Kaysersberg seulement du vendredi au dimanche. Navettes de Noël depuis la gare de Colmar.',
  'Until 20 December 2026; Kaysersberg from Friday to Sunday only. Christmas shuttles from Colmar station.'),
 ('27 nov.','27 Nov','Nice et Cannes','cote-d-azur/noel-cote-d-azur','french-riviera/christmas-french-riviera',
  'Jusqu’au 3 janvier 2027 : jardin Albert-Ier et place Masséna à Nice, allées de la Liberté à Cannes.',
  'Until 3 January 2027: Jardin Albert-Ier and Place Masséna in Nice, Allées de la Liberté in Cannes.'),
 ('4 déc.','4 Dec','Monaco','cote-d-azur/noel-cote-d-azur','french-riviera/christmas-french-riviera',
  'Le village de Noël du port Hercule, quai Albert-Ier, jusqu’au 3 janvier 2027, avec une patinoire à côté.',
  'The Christmas village on Port Hercule, Quai Albert-Ier, until 3 January 2027, with an ice rink next door.'),
]
def body(lang):
    i = 0 if lang=='fr' else 1
    intro = ('<p>Les marchés de Noël ouvrent en France entre mi-novembre et début décembre 2026. Trois régions sortent du lot : l’Alsace pour l’ambiance traditionnelle, Paris pour les illuminations et les grands magasins, et la Côte d’Azur pour un Noël au soleil. Voici le calendrier 2026, par date d’ouverture, avec un lien vers notre guide détaillé pour chaque destination.</p><p>L’entrée est libre et gratuite sur tous ces marchés.</p>' if lang=='fr' else
             '<p>Christmas markets in France open between mid-November and early December 2026. Three regions stand out: Alsace for the traditional atmosphere, Paris for the lights and the department stores, and the French Riviera for Christmas in the sun. Here is the 2026 calendar, by opening date, with a link to our detailed guide for each destination.</p><p>Entry is free at all these markets.</p>')
    h = '\n<h2>Le calendrier 2026</h2>' if lang=='fr' else '\n<h2>The 2026 calendar</h2>'
    ag = '<ul class="agenda">' + ''.join(f'<li class="ag"><span class="ag__d">{a[i]}</span><div class="ag__b"><strong><a href="../../{a[3+i]}/">{a[2]}</a></strong><p>{a[5+i]}</p></div></li>' for a in A) + '</ul>'
    reg = ('\n<h2>Quelle région choisir ?</h2><h3><a href="../marches-de-noel-alsace/">L’Alsace</a></h3><p>La plus traditionnelle : chalets, vin chaud et villages à colombages. Strasbourg et Colmar se relient en train, et des navettes desservent les villages depuis Colmar.</p><h3><a href="../../paris/noel-a-paris/">Paris</a></h3><p>Pour les illuminations des Champs-Élysées, les vitrines des grands magasins et plusieurs marchés, à combiner avec une croisière sur la Seine.</p><h3><a href="../../cote-d-azur/noel-cote-d-azur/">La Côte d’Azur</a></h3><p>Le Noël le plus doux : Nice, Cannes et Monaco sont à moins d’une heure de train les unes des autres, et les marchés restent ouverts jusqu’au 3 janvier 2027.</p>'
           '\n<h2>Nos conseils</h2><ul><li><strong>Venez en semaine</strong> : le samedi est le jour le plus chargé partout.</li><li><strong>Attention aux dates de fermeture</strong> : Riquewihr et Kaysersberg ferment le 20 décembre, Strasbourg le 24 ; Paris et la Côte d’Azur restent ouverts jusqu’au début janvier.</li><li><strong>Réservez l’hôtel tôt</strong>, surtout à Strasbourg et Colmar pour les week-ends de décembre.</li></ul><p class="maj">Dates relevées en novembre 2026 auprès des villes et des offices de tourisme ; vérifiez avant de partir.</p>'
           if lang=='fr' else
           '\n<h2>Which region to choose?</h2><h3><a href="../alsace-christmas-markets/">Alsace</a></h3><p>The most traditional: wooden chalets, mulled wine and half-timbered villages. Strasbourg and Colmar are linked by train, and shuttles serve the villages from Colmar.</p><h3><a href="../../paris/christmas-in-paris/">Paris</a></h3><p>For the Champs-Élysées lights, the department store windows and several markets, best combined with a Seine cruise.</p><h3><a href="../../french-riviera/christmas-french-riviera/">The French Riviera</a></h3><p>The mildest Christmas: Nice, Cannes and Monaco are less than an hour apart by train, and the markets stay open until 3 January 2027.</p>'
           '\n<h2>Our tips</h2><ul><li><strong>Go on a weekday</strong>: Saturday is the busiest day everywhere.</li><li><strong>Check the closing dates</strong>: Riquewihr and Kaysersberg close on 20 December, Strasbourg on the 24th; Paris and the Riviera stay open until early January.</li><li><strong>Book your hotel early</strong>, especially in Strasbourg and Colmar for December weekends.</li></ul><p class="maj">Dates checked in November 2026 with the cities and tourist offices; check before you go.</p>')
    return intro + h + ag + reg
P = dict(photo='noel-a-paris', og='noel-a-paris', date='2026-11-20',
 acts=[({'fr':'idees/marches-de-noel-alsace','en':'ideas/alsace-christmas-markets'},0), ({'fr':'paris/noel-a-paris','en':'paris/christmas-in-paris'},0)],
 fr=dict(path='idees/marches-de-noel-france', home='Accueil', crumbs=[('Idées','idees/')], crumb_last='Marchés de Noël en France 2026',
  title='Marchés de Noël en France 2026 : dates et lieux',
  desc='Marchés de Noël 2026 en France : dates de Strasbourg, Colmar, Riquewihr, Paris (Tuileries, Champs-Élysées), Nice, Cannes et Monaco, avec nos conseils.',
  h1='Marchés de Noël en France 2026 : le calendrier',
  lead='Alsace, Paris ou Côte d’Azur : les dates d’ouverture et de fermeture des grands marchés de Noël 2026.',
  body=body('fr'), book_lead='Deux visites à réserver pour profiter des marchés de Noël.',
  faq=[('Quand ouvrent les marchés de Noël en 2026 ?','Entre mi-novembre et début décembre : La Défense le 12 novembre, les Tuileries le 14, Colmar le 23, Strasbourg, Riquewihr, Kaysersberg, Nice et Cannes le 27 novembre, Monaco le 4 décembre 2026.'),
       ('Quel est le plus ancien marché de Noël de France ?','Celui de Strasbourg, le Christkindelsmärik, qui existe depuis 1570. En 2026, il est ouvert du 27 novembre au 24 décembre, place Broglie.'),
       ('Quels marchés de Noël sont ouverts après Noël ?','Paris (Tuileries et Champs-Élysées), Nice, Cannes et Monaco restent ouverts jusqu’au 3 ou 4 janvier 2027, et Colmar jusqu’au 29 décembre, avec son marché gourmand jusqu’au 3 janvier.')],
  cards_t='Nos guides de Noël', cards=[dict(href='idees/marches-de-noel-alsace/',photo='strasbourg',name='Alsace',txt='Strasbourg, Colmar, Riquewihr, Kaysersberg.'),dict(href='paris/noel-a-paris/',photo='noel-a-paris',name='Paris',txt='Illuminations, vitrines et marchés.'),dict(href='cote-d-azur/noel-cote-d-azur/',photo='noel-riviera',name='Côte d’Azur',txt='Nice, Cannes et Monaco au soleil.')]),
 en=dict(path='ideas/christmas-markets-france', home='Home', crumbs=[('Ideas','ideas/')], crumb_last='Christmas markets in France 2026',
  title='Christmas markets in France 2026: dates and places',
  desc='Christmas markets 2026 in France: dates for Strasbourg, Colmar, Riquewihr, Paris (Tuileries, Champs-Élysées), Nice, Cannes and Monaco, with our tips.',
  h1='Christmas markets in France 2026: the calendar',
  lead='Alsace, Paris or the French Riviera: opening and closing dates of the main 2026 Christmas markets.',
  body=body('en'), book_lead='Two tours to book to make the most of the Christmas markets.',
  faq=[('When do Christmas markets open in France in 2026?','Between mid-November and early December: La Défense on 12 November, the Tuileries on the 14th, Colmar on the 23rd, Strasbourg, Riquewihr, Kaysersberg, Nice and Cannes on 27 November, and Monaco on 4 December 2026.'),
       ('What is the oldest Christmas market in France?','Strasbourg’s Christkindelsmärik, which dates back to 1570. In 2026 it is open from 27 November to 24 December on Place Broglie.'),
       ('Which Christmas markets are open after Christmas?','Paris (Tuileries and Champs-Élysées), Nice, Cannes and Monaco stay open until 3 or 4 January 2027, and Colmar until 29 December, with its food market until 3 January.')],
  cards_t='Our Christmas guides', cards=[dict(href='ideas/alsace-christmas-markets/',photo='strasbourg',name='Alsace',txt='Strasbourg, Colmar, Riquewihr, Kaysersberg.'),dict(href='paris/christmas-in-paris/',photo='noel-a-paris',name='Paris',txt='Lights, windows and markets.'),dict(href='french-riviera/christmas-french-riviera/',photo='noel-riviera',name='French Riviera',txt='Nice, Cannes and Monaco in the sun.')]))
for l in ('fr','en'):
    assert len(P[l]['title']) <= 58, (l, len(P[l]['title'])); assert len(P[l]['desc']) <= 160, (l, len(P[l]['desc']))
    print(build(P, l))
