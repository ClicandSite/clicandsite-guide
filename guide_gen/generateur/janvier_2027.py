import sys; sys.path.insert(0,'/tmp/g')
from winter_gen import build
# Faits repris des pages du guide (vérifiées) + festival du cirque (CRT Côte d'Azur, cotedazurfrance.fr, relevé en novembre 2026)
A = [
 ('3 janv.','3 Jan','Derniers jours des marchés de Noël','Last days of the Christmas markets','idees/marches-de-noel-france','ideas/christmas-markets-france',
  'Nice, Cannes, Monaco et les Tuileries ferment le 3 janvier 2027 ; le marché des Champs-Élysées dure jusqu’au 4.','Nice, Cannes, Monaco and the Tuileries close on 3 January 2027; the Champs-Élysées market runs until the 4th.'),
 ('4 janv.','4 Jan','Fin des vacances de Noël','End of the Christmas school holidays','idees/vacances-de-noel-2026','ideas/christmas-holidays-2026',
  'Reprise des cours dans toute la France. Jusqu’au 6 février 2027, aucune zone n’est en vacances scolaires.','School resumes across France. Until 6 February 2027, no zone is on school holiday.'),
 ('10 janv.','10 Jan','Fin de l’exposition Warhol','Warhol exhibition ends','idees/que-faire-a-paris-en-hiver','ideas/things-to-do-in-paris-in-winter',
  'Au musée du Luxembourg, à Paris. Cezanne au Grand Palais dure jusqu’au 17 janvier.','At the Musée du Luxembourg in Paris. Cezanne at the Grand Palais runs until 17 January.'),
 ('18 janv.','18 Jan','Semaine du Rallye Monte-Carlo','Monte-Carlo Rally week','cote-d-azur/rallye-monte-carlo','french-riviera/monte-carlo-rally',
  'Reconnaissances et animations à Monaco, puis la course du jeudi 21 au dimanche 24 janvier 2027, arrivée sur le port Hercule.','Reconnaissance and events in Monaco, then the race from Thursday 21 to Sunday 24 January 2027, finishing at Port Hercule.'),
 ('22 janv.','22 Jan','Festival international du cirque de Monte-Carlo','Monte-Carlo International Circus Festival','cote-d-azur/monaco','french-riviera/monaco',
  '49e édition, du 22 au 31 janvier 2027 à Monaco.','49th edition, from 22 to 31 January 2027 in Monaco.'),
 ('24 janv.','24 Jan','Fin de l’exposition Marie-Antoinette','Marie-Antoinette exhibition ends','paris/versailles','paris/versailles',
  'Au château de Versailles.','At the Palace of Versailles.'),
 ('fin janv.','late Jan','Premiers mimosas','First mimosa blossom','cote-d-azur/route-du-mimosa','french-riviera/mimosa-route',
  'Le mimosa fleurit de janvier à mars entre Bormes-les-Mimosas et Grasse, avec un pic en février.','Mimosa blooms from January to March between Bormes-les-Mimosas and Grasse, peaking in February.'),
]
def body(lang):
    i = 0 if lang=='fr' else 1
    def li(a):
        t = f'<a href="../../{a[4+i]}/">{a[2+i]}</a>' if a[4] else a[2+i]
        return f'<li class="ag"><span class="ag__d">{a[i]}</span><div class="ag__b"><strong>{t}</strong><p>{a[6+i]}</p></div></li>'
    ag = '<ul class="agenda">' + ''.join(li(a) for a in A) + '</ul>'
    if lang=='fr':
        return ('<p>Janvier est le mois creux de l’hiver : les fêtes sont passées, les vacances de février n’ont pas commencé et les trains comme les stations sont moins chargés. C’est le bon moment pour skier au calme, chercher le soleil sur la Côte d’Azur ou voir les grandes expositions de Paris avant leur fermeture.</p>'
         '\n<h2>L’agenda de janvier 2027</h2>' + ag +
         '\n<h2>Nos idées pour janvier</h2>'
         '<h3><a href="../stations-de-ski-ouvertes/">Skier hors vacances scolaires</a></h3><p>Du lundi 4 janvier au samedi 6 février 2027, aucune zone n’est en vacances : c’est la période la plus calme de la saison dans les stations des Alpes et des Pyrénées. Pour comparer les prix, voir notre comparatif des <a href="../prix-forfaits-ski-2026-2027/">forfaits 2026-2027</a> : de 44 € la journée à Isola 2000 ou Auron à 84,20 € dans les 3 Vallées.</p>'
         '<h3><a href="../../cote-d-azur/rallye-monte-carlo/">Le Rallye et le cirque à Monaco</a></h3><p>Deux grands rendez-vous se suivent à Monaco : le <a href="../../cote-d-azur/rallye-monte-carlo/">Rallye Monte-Carlo</a> du 21 au 24 janvier, puis le festival du cirque du 22 au 31 janvier. Le TER Nice–Vintimille dessert la gare de Monaco-Monte-Carlo.</p>'
         '<h3><a href="../cote-d-azur-en-hiver/">Le soleil de la Côte d’Azur</a></h3><p>Balades au bord de l’eau, villages perchés sans la foule et premiers mimosas sur la <a href="../../cote-d-azur/route-du-mimosa/">Route du Mimosa</a>. Les grandes fêtes (Carnaval de Nice, Fête du Citron) arrivent en février.</p>'
         '<h3><a href="../que-faire-a-paris-en-hiver/">Les expositions de Paris</a></h3><p>Dernières semaines pour Warhol au musée du Luxembourg (10 janvier), Cezanne au Grand Palais (17 janvier) et Marie-Antoinette à Versailles (24 janvier 2027).</p>'
         '\n<h2>Nos conseils</h2><ul><li><strong>Vérifiez l’enneigement</strong> avant de partir : en début de saison, les stations les plus hautes sont les plus sûres.</li><li><strong>Au ski, réservez avant le 6 février</strong> : ensuite, les <a href="../vacances-de-fevrier-2027/">vacances de février</a> commencent pour la zone C.</li><li><strong>Pour Monaco pendant le Rallye</strong>, venez en train : les parkings sont très demandés.</li></ul><p class="maj">Dates relevées en novembre 2026 (Automobile Club de Monaco, Comité régional du tourisme Côte d’Azur, sites des musées) ; vérifiez avant de partir.</p>')
    return ('<p>January is the quiet month of winter: the holidays are over, the February school break has not started and trains and ski resorts are less busy. It is a good time to ski in peace, find the sun on the French Riviera or catch the big Paris exhibitions before they close.</p>'
         '\n<h2>January 2027 events</h2>' + ag +
         '\n<h2>Our ideas for January</h2>'
         '<h3><a href="../ski-resort-opening-dates/">Ski outside the school holidays</a></h3><p>From Monday 4 January to Saturday 6 February 2027, no French school zone is on holiday: it is the quietest part of the season in the Alps and the Pyrenees. To compare prices, see our <a href="../ski-pass-prices-2026-2027/">2026-2027 lift pass comparison</a>: from €44 a day at Isola 2000 or Auron to €84.20 in the 3 Vallées.</p>'
         '<h3><a href="../../french-riviera/monte-carlo-rally/">The Rally and the circus in Monaco</a></h3><p>Two big events follow each other in Monaco: the <a href="../../french-riviera/monte-carlo-rally/">Monte-Carlo Rally</a> from 21 to 24 January, then the circus festival from 22 to 31 January. The Nice–Ventimiglia TER train stops at Monaco-Monte-Carlo station.</p>'
         '<h3><a href="../french-riviera-in-winter/">Riviera sunshine</a></h3><p>Seaside walks, hilltop villages without the crowds and the first mimosa on the <a href="../../french-riviera/mimosa-route/">Mimosa Route</a>. The big festivals (Nice Carnival, Menton Lemon Festival) come in February.</p>'
         '<h3><a href="../things-to-do-in-paris-in-winter/">Paris exhibitions</a></h3><p>Last weeks for Warhol at the Musée du Luxembourg (10 January), Cezanne at the Grand Palais (17 January) and Marie-Antoinette at Versailles (24 January 2027).</p>'
         '\n<h2>Our tips</h2><ul><li><strong>Check snow conditions</strong> before you go: early in the season, the highest resorts are the safest bet.</li><li><strong>For skiing, go before 6 February</strong>: then the <a href="../february-school-holidays-2027/">February school holidays</a> start for zone C.</li><li><strong>For Monaco during the Rally</strong>, come by train: car parks are in high demand.</li></ul><p class="maj">Dates checked in November 2026 (Automobile Club de Monaco, Côte d’Azur regional tourist board, museum websites); check before you go.</p>')
P = dict(photo='alpe-d-huez', og='alpe-d-huez', date='2026-11-24',
 acts=[({'fr':'idees/stations-de-ski-ouvertes','en':'ideas/ski-resort-opening-dates'},0), ({'fr':'cote-d-azur/rallye-monte-carlo','en':'french-riviera/monte-carlo-rally'},0)],
 fr=dict(path='idees/ou-partir-en-janvier-2027', home='Accueil', crumbs=[('Idées','idees/')], crumb_last='Où partir en janvier 2027',
  title='Où partir en janvier 2027 en France : idées et agenda',
  desc='Où partir en janvier 2027 : ski hors vacances scolaires, Rallye Monte-Carlo, festival du cirque de Monaco, Côte d’Azur et expositions à Paris.',
  h1='Où partir en janvier 2027 en France : nos idées et l’agenda',
  lead='Le mois le plus calme de l’hiver : ski sans la foule, Monaco en fête, soleil sur la Riviera et dernières grandes expositions à Paris.',
  body=body('fr'), book_lead='Deux idées à réserver pour janvier.',
  faq=[('Où partir en France en janvier ?','Au ski hors vacances scolaires (du 4 janvier au 6 février 2027), sur la Côte d’Azur pour le soleil et les premiers mimosas, à Monaco pour le Rallye Monte-Carlo (21-24 janvier) et le festival du cirque (22-31 janvier), ou à Paris pour les grandes expositions.'),
       ('Quand a lieu le festival du cirque de Monte-Carlo 2027 ?','La 49e édition du Festival international du cirque de Monte-Carlo a lieu du 22 au 31 janvier 2027, à Monaco.'),
       ('Janvier est-il un bon mois pour skier ?','Oui : entre la fin des vacances de Noël (4 janvier 2027) et le début des vacances de février (6 février pour la zone C), aucune zone n’est en vacances, les pistes et les hébergements sont moins chargés.')],
  cards_t='Nos guides pour l’hiver', cards=[dict(href='idees/stations-de-ski-ouvertes/',photo='val-thorens',name='Ski',txt='Les dates d’ouverture des stations.'),dict(href='cote-d-azur/rallye-monte-carlo/',photo='monaco',name='Rallye Monte-Carlo',txt='Du 21 au 24 janvier 2027.'),dict(href='idees/cote-d-azur-en-hiver/',photo='menton',name='Côte d’Azur',txt='Que faire au soleil en hiver.')]),
 en=dict(path='ideas/where-to-go-in-france-in-january-2027', home='Home', crumbs=[('Ideas','ideas/')], crumb_last='Where to go in January 2027',
  title='Where to go in France in January 2027: ideas & events',
  desc='Where to go in France in January 2027: skiing outside school holidays, the Monte-Carlo Rally, the Monaco circus festival, the Riviera and Paris exhibitions.',
  h1='Where to go in France in January 2027: ideas and events',
  lead='The quietest month of winter: uncrowded skiing, Monaco in party mode, Riviera sunshine and the last big exhibitions in Paris.',
  body=body('en'), book_lead='Two ideas to book for January.',
  faq=[('Where should I go in France in January?','Skiing outside the school holidays (4 January to 6 February 2027), the French Riviera for sunshine and the first mimosa, Monaco for the Monte-Carlo Rally (21-24 January) and the circus festival (22-31 January), or Paris for the big exhibitions.'),
       ('When is the 2027 Monte-Carlo Circus Festival?','The 49th Monte-Carlo International Circus Festival runs from 22 to 31 January 2027, in Monaco.'),
       ('Is January a good month for skiing in France?','Yes: between the end of the Christmas holidays (4 January 2027) and the start of the February holidays (6 February for zone C), no school zone is on holiday, so slopes and accommodation are less busy.')],
  cards_t='Our winter guides', cards=[dict(href='ideas/ski-resort-opening-dates/',photo='val-thorens',name='Skiing',txt='Resort opening dates.'),dict(href='french-riviera/monte-carlo-rally/',photo='monaco',name='Monte-Carlo Rally',txt='21 to 24 January 2027.'),dict(href='ideas/french-riviera-in-winter/',photo='menton',name='French Riviera',txt='Things to do in the winter sun.')]))
for l in ('fr','en'):
    assert len(P[l]['title']) <= 58, (l, len(P[l]['title'])); assert len(P[l]['desc']) <= 160, (l, len(P[l]['desc']))
    print(build(P, l))
