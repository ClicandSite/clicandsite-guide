import sys; sys.path.insert(0,'/tmp/g')
from winter_gen import build
D = [
 ('paris/croisiere-sur-la-seine','paris/seine-cruise','Paris, dîner sur la Seine','Paris, dinner on the Seine',
  'Le grand classique : un dîner croisière sur la Seine, de la formule simple au menu gastronomique, avec la tour Eiffel illuminée. Les bateaux circulent toute l’année, sauf en cas de crue. Le 14 février tombe un dimanche en 2027 : réservez tôt, les créneaux du samedi 13 et du dimanche partent vite.',
  'The great classic: a dinner cruise on the Seine, from a simple menu to a gourmet dinner, with the Eiffel Tower lit up. Boats run all year round, except when the river floods. In 2027, 14 February falls on a Sunday: book early, as Saturday 13 and Sunday slots go fast.'),
 ('paris/montmartre','paris/montmartre','Paris, Montmartre','Paris, Montmartre',
  'Les petites rues pavées, la place du Tertre et la vue depuis le Sacré-Cœur : Montmartre se prête à une longue balade à deux, idéalement tôt le matin avant l’arrivée des groupes.',
  'Cobbled lanes, the Place du Tertre and the view from the Sacré-Cœur: Montmartre is made for a long walk together, ideally early in the morning before the tour groups arrive.'),
 ('cote-d-azur/eze','french-riviera/eze','Èze, le village perché','Èze, the hilltop village',
  'Ruelles médiévales, jardin exotique au sommet et vue plongeante sur la Méditerranée : Èze est l’un des villages les plus romantiques de la Côte d’Azur, à mi-chemin entre Nice et Monaco. En février, il y a beaucoup moins de monde qu’en été.',
  'Medieval lanes, a cactus garden at the top and a sweeping view over the Mediterranean: Èze is one of the most romantic villages on the French Riviera, halfway between Nice and Monaco. In February it is far quieter than in summer.'),
 ('cote-d-azur/saint-paul-de-vence','french-riviera/saint-paul-de-vence','Saint-Paul-de-Vence','Saint-Paul-de-Vence',
  'Les remparts, les galeries d’art et la Fondation Maeght juste à côté : une journée tranquille à deux, à 30 minutes de Nice.',
  'The ramparts, the art galleries and the Fondation Maeght next door: a quiet day for two, 30 minutes from Nice.'),
 ('cote-d-azur/fete-du-citron-menton','french-riviera/lemon-festival-menton','Menton et la Fête du Citron','Menton and the Lemon Festival',
  'La Fête du Citron commence le samedi 13 février 2027, la veille de la Saint-Valentin, et le Carnaval de Nice, sur le thème « Vive l’Amour », bat son plein du 9 au 28 février : de quoi combiner week-end en amoureux et grand spectacle.',
  'The Lemon Festival opens on Saturday 13 February 2027, the day before Valentine’s Day, and the Nice Carnival, themed “Vive l’Amour” (Long live love), is in full swing from 9 to 28 February: a chance to combine a romantic weekend with a big show.'),
 ('alsace/colmar','alsace/colmar','Colmar et la Petite Venise','Colmar and Little Venice',
  'Maisons à colombages, canaux de la Petite Venise et vins d’Alsace : Colmar est une escapade de charme, plus calme en février qu’à Noël. Eguisheim et Riquewihr sont à quelques minutes.',
  'Half-timbered houses, the canals of Little Venice and Alsace wines: Colmar is a charming getaway, quieter in February than at Christmas. Eguisheim and Riquewihr are a few minutes away.'),
 ('normandie/etretat','normandy/etretat','Étretat et Honfleur','Étretat and Honfleur',
  'Les falaises d’Étretat au coucher du soleil, puis le Vieux Bassin de Honfleur à une heure de route : un week-end en Normandie facile depuis Paris.',
  'The Étretat cliffs at sunset, then Honfleur’s Old Harbour an hour’s drive away: an easy Normandy weekend from Paris.'),
 ('bretagne/saint-malo','brittany/saint-malo','Saint-Malo','Saint-Malo',
  'Le tour des remparts face à la mer, les grandes marées d’hiver et une crêperie intra-muros : Saint-Malo garde tout son charme hors saison.',
  'A walk round the ramparts facing the sea, the big winter tides and a crêperie inside the walls: Saint-Malo keeps all its charm out of season.'),
]
def body(lang):
    i = 0 if lang=='fr' else 1
    intro = ('<p>En 2027, la Saint-Valentin tombe un dimanche : le week-end du samedi 13 et du dimanche 14 février est donc idéal pour partir à deux. Voici nos destinations préférées en France pour un week-end en amoureux, de Paris à la Côte d’Azur, avec chaque fois un lien vers notre guide détaillé.</p>' if lang=='fr' else
             '<p>In 2027, Valentine’s Day falls on a Sunday, so the weekend of Saturday 13 and Sunday 14 February is ideal for a trip together. Here are our favourite places in France for a romantic weekend, from Paris to the French Riviera, each with a link to our detailed guide.</p>')
    h = '\n<h2>Nos idées de week-end en amoureux</h2>' if lang=='fr' else '\n<h2>Our romantic weekend ideas</h2>'
    items = ''.join(f'\n<h3><a href="../../{d[i]}/">{d[2+i]}</a></h3><p>{d[4+i]}</p>' for d in D)
    tips = ('\n<h2>Nos conseils pour réserver</h2><ul><li><strong>Réservez tôt</strong> : les dîners croisière et les restaurants du samedi 13 février se remplissent des semaines à l’avance.</li><li><strong>Attention aux vacances de février</strong> : elles commencent le 6 février 2027 pour la zone C (Paris), et les hôtels de montagne et de la Côte d’Azur sont plus chers.</li><li><strong>Pensez au train</strong> : Paris–Nice, Paris–Colmar ou Paris–Saint-Malo se font en TGV, sans voiture sur place.</li></ul><p class="maj">Dates relevées en novembre 2026 ; vérifiez avant de réserver.</p>' if lang=='fr' else
            '\n<h2>Our booking tips</h2><ul><li><strong>Book early</strong>: dinner cruises and restaurants for Saturday 13 February fill up weeks ahead.</li><li><strong>Watch out for the French school holidays</strong>: they start on 6 February 2027 for zone C (Paris), and mountain and Riviera hotels cost more.</li><li><strong>Take the train</strong>: Paris–Nice, Paris–Colmar and Paris–Saint-Malo are all served by TGV, no car needed.</li></ul><p class="maj">Dates checked in November 2026; check before booking.</p>')
    return intro + h + items + tips
P = dict(photo='croisiere-sur-la-seine', og='croisiere-sur-la-seine', date='2026-11-19',
 acts=[({'fr':'paris/croisiere-sur-la-seine','en':'paris/seine-cruise'},1), ({'fr':'cote-d-azur/eze','en':'french-riviera/eze'},0)],
 fr=dict(path='idees/saint-valentin-2027', home='Accueil', crumbs=[('Idées','idees/')], crumb_last='Saint-Valentin 2027',
  title='Saint-Valentin 2027 : où partir en amoureux en France ?',
  desc='Saint-Valentin 2027 (dimanche 14 février) : dîner croisière à Paris, Èze, Menton, Colmar, Étretat, Saint-Malo… nos idées de week-end en amoureux en France.',
  h1='Saint-Valentin 2027 : où partir en amoureux en France ?',
  lead='Le 14 février 2027 tombe un dimanche : nos idées de week-end à deux, de la Seine à la Côte d’Azur.',
  body=body('fr'), book_lead='Deux idées à réserver pour la Saint-Valentin.',
  faq=[('Quel jour tombe la Saint-Valentin 2027 ?','Le dimanche 14 février 2027. Le week-end des 13 et 14 février est donc idéal pour partir à deux.'),
       ('Où partir en amoureux pour la Saint-Valentin en France ?','Paris pour un dîner croisière sur la Seine et Montmartre, la Côte d’Azur pour Èze, Saint-Paul-de-Vence et Menton, l’Alsace pour Colmar, la Normandie pour Étretat et Honfleur, ou la Bretagne pour Saint-Malo.'),
       ('Y a-t-il des événements le week-end de la Saint-Valentin 2027 ?','Oui : la Fête du Citron de Menton commence le samedi 13 février 2027 et le Carnaval de Nice a lieu du 9 au 28 février 2027.')],
  cards_t='Nos coups de cœur', cards=[dict(href='cote-d-azur/eze/',photo='eze',name='Èze',txt='Le village perché entre Nice et Monaco.'),dict(href='alsace/colmar/',photo='colmar',name='Colmar',txt='La Petite Venise, calme en février.'),dict(href='normandie/etretat/',photo='etretat',name='Étretat',txt='Les falaises au coucher du soleil.')]),
 en=dict(path='ideas/valentines-day-2027', home='Home', crumbs=[('Ideas','ideas/')], crumb_last='Valentine’s Day 2027',
  title='Valentine’s Day 2027: romantic weekends in France',
  desc='Valentine’s Day 2027 (Sunday 14 February): Seine dinner cruise in Paris, Èze, Menton, Colmar, Étretat, Saint-Malo… our romantic weekend ideas in France.',
  h1='Valentine’s Day 2027: romantic weekends in France',
  lead='14 February 2027 falls on a Sunday: our ideas for a weekend for two, from the Seine to the French Riviera.',
  body=body('en'), book_lead='Two ideas to book for Valentine’s Day.',
  faq=[('What day is Valentine’s Day 2027?','Sunday 14 February 2027, so the weekend of 13 and 14 February is ideal for a trip together.'),
       ('Where to go for a romantic weekend in France?','Paris for a Seine dinner cruise and Montmartre, the French Riviera for Èze, Saint-Paul-de-Vence and Menton, Alsace for Colmar, Normandy for Étretat and Honfleur, or Brittany for Saint-Malo.'),
       ('Are there events on Valentine’s weekend 2027?','Yes: the Menton Lemon Festival opens on Saturday 13 February 2027 and the Nice Carnival runs from 9 to 28 February 2027.')],
  cards_t='Our favourites', cards=[dict(href='french-riviera/eze/',photo='eze',name='Èze',txt='The hilltop village between Nice and Monaco.'),dict(href='alsace/colmar/',photo='colmar',name='Colmar',txt='Little Venice, quiet in February.'),dict(href='normandy/etretat/',photo='etretat',name='Étretat',txt='The cliffs at sunset.')]))
for l in ('fr','en'):
    assert len(P[l]['title']) <= 58, (l, len(P[l]['title'])); assert len(P[l]['desc']) <= 160, (l, len(P[l]['desc']))
    print(build(P, l))
