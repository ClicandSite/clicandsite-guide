import sys; sys.path.insert(0,'/tmp/g')
from winter_gen import build
A = [
 ('19 déc.','19 Dec','Début des vacances de Noël','Christmas school holidays begin',None,None,
  'Pour les trois zones et la Corse, jusqu’au lundi 4 janvier 2027 (reprise des cours).','For all three zones and Corsica, until Monday 4 January 2027 (back to school).'),
 ('19 déc.','19 Dec','Ouverture de Megève et de La Grave','Megève and La Grave open','alpes/megeve','french-alps/megeve',
  'Le jour même des vacances. Val Thorens, Tignes, Courchevel ou l’Alpe d’Huez sont ouvertes depuis fin novembre ou début décembre.','On the first day of the holidays. Val Thorens, Tignes, Courchevel and Alpe d’Huez have been open since late November or early December.'),
 ('20 déc.','20 Dec','Fermeture de Riquewihr et Kaysersberg','Riquewihr and Kaysersberg close','idees/marches-de-noel-alsace','ideas/alsace-christmas-markets',
  'Seul le premier week-end des vacances permet de les voir.','Only the first weekend of the holidays lets you see them.'),
 ('24 déc.','24 Dec','Dernier jour du marché de Strasbourg','Last day of the Strasbourg market','alsace/strasbourg','alsace/strasbourg',
  'Le Christkindelsmärik de la place Broglie ferme le soir de Noël.','The Christkindelsmärik on Place Broglie closes on Christmas Eve.'),
 ('29 déc.','29 Dec','Fin des marchés de Colmar','Colmar markets end','alsace/colmar','alsace/colmar',
  'Le marché gourmand et la grande roue restent jusqu’au 3 janvier 2027.','The food market and the big wheel stay until 3 January 2027.'),
 ('31 déc.','31 Dec','Réveillon du Nouvel An','New Year’s Eve','idees/reveillon-nouvel-an','ideas/new-years-eve-france',
  'Un jeudi soir : feu d’artifice gratuit sur les Champs-Élysées à minuit, dîners sur la Seine, fête à Nice.','A Thursday night: free fireworks on the Champs-Élysées at midnight, dinners on the Seine, celebrations in Nice.'),
 ('3 janv.','3 Jan','Fin des marchés de Nice, Cannes, Monaco et des Tuileries','Nice, Cannes, Monaco and Tuileries markets end','idees/marches-de-noel-france','ideas/christmas-markets-france',
  'Le marché des Champs-Élysées dure jusqu’au 4 janvier 2027.','The Champs-Élysées market runs until 4 January 2027.'),
]
def body(lang):
    i = 0 if lang=='fr' else 1
    intro = ('<p>Les vacances de Noël 2026 vont du samedi 19 décembre 2026 au lundi 4 janvier 2027, aux mêmes dates pour toute la France. Ski, marchés de Noël, réveillon à Paris ou soleil sur la Côte d’Azur : voici le calendrier des vacances et nos idées pour en profiter, avec un lien vers notre guide détaillé à chaque fois.</p>' if lang=='fr' else
             '<p>The French Christmas school holidays run from Saturday 19 December 2026 to Monday 4 January 2027, on the same dates across France. Skiing, Christmas markets, New Year’s Eve in Paris or sunshine on the Riviera: here is the holiday calendar and our ideas to make the most of it, each with a link to our detailed guide.</p>')
    h = '\n<h2>Le calendrier des vacances</h2>' if lang=='fr' else '\n<h2>The holiday calendar</h2>'
    def li(a):
        t = f'<a href="../../{a[4+i]}/">{a[2+i]}</a>' if a[4] else a[2+i]
        return f'<li class="ag"><span class="ag__d">{a[i]}</span><div class="ag__b"><strong>{t}</strong><p>{a[6+i]}</p></div></li>'
    ag = '<ul class="agenda">' + ''.join(li(a) for a in A) + '</ul>'
    if lang=='fr':
        rest = ('\n<h2>Nos idées pour les vacances de Noël</h2>'
         '<h3><a href="../stations-de-ski-ouvertes/">Partir au ski</a></h3><p>Pendant les vacances de Noël, les grandes stations des Alpes et des Pyrénées sont ouvertes. Les plus hautes, comme Val Thorens et Tignes, sont les plus sûres côté neige. C’est aussi la période la plus chère : voir notre comparatif des <a href="../prix-forfaits-ski-2026-2027/">prix des forfaits 2026-2027</a>.</p>'
         '<h3><a href="../marches-de-noel-france/">Faire les marchés de Noël</a></h3><p>Attention aux dates : en Alsace, Riquewihr et Kaysersberg ferment le 20 décembre et Strasbourg le 24. Pendant toute la durée des vacances, ce sont Paris, Nice, Cannes et Monaco qui restent ouverts, jusqu’au 3 ou 4 janvier 2027.</p>'
         '<h3><a href="../reveillon-nouvel-an/">Fêter le Nouvel An</a></h3><p>Le feu d’artifice gratuit des Champs-Élysées, un dîner croisière sur la Seine ou une fête au bord de la mer à Nice.</p>'
         '<h3><a href="../cote-d-azur-en-hiver/">Chercher le soleil sur la Côte d’Azur</a></h3><p>Des balades au bord de l’eau, les villages perchés sans la foule et les villages de Noël de Nice, Cannes et Monaco, faciles à relier en train.</p>'
         '<h3><a href="../que-faire-a-paris-en-hiver/">Profiter de Paris en hiver</a></h3><p>Illuminations, patinoires et musées : notre sélection pour les journées courtes de décembre.</p>'
         '\n<h2>Nos conseils</h2><ul><li><strong>Réservez vos trains tôt</strong> : les premiers et les derniers jours des vacances sont les plus demandés.</li><li><strong>Au ski, les deux semaines sont en haute saison</strong> : réservez l’hébergement et le matériel dès maintenant.</li><li><strong>Pour les marchés d’Alsace</strong>, partez dès le premier week-end des vacances.</li></ul><p class="maj">Dates des vacances : arrêté du 22 octobre 2025 (Journal officiel du 23 octobre 2025). Autres dates relevées en novembre 2026 ; vérifiez avant de partir.</p>')
    else:
        rest = ('\n<h2>Our ideas for the Christmas holidays</h2>'
         '<h3><a href="../ski-resort-opening-dates/">Go skiing</a></h3><p>During the Christmas holidays, the big resorts in the Alps and the Pyrenees are open. The highest ones, such as Val Thorens and Tignes, are the safest bet for snow. It is also the most expensive period: see our comparison of <a href="../ski-pass-prices-2026-2027/">2026-2027 lift pass prices</a>.</p>'
         '<h3><a href="../christmas-markets-france/">Visit the Christmas markets</a></h3><p>Check the dates: in Alsace, Riquewihr and Kaysersberg close on 20 December and Strasbourg on the 24th. For the whole holiday, Paris, Nice, Cannes and Monaco stay open, until 3 or 4 January 2027.</p>'
         '<h3><a href="../new-years-eve-france/">Celebrate New Year’s Eve</a></h3><p>The free fireworks on the Champs-Élysées, a dinner cruise on the Seine or a seaside party in Nice.</p>'
         '<h3><a href="../french-riviera-in-winter/">Find the sun on the French Riviera</a></h3><p>Seaside walks, hilltop villages without the crowds and the Christmas villages of Nice, Cannes and Monaco, easy to link by train.</p>'
         '<h3><a href="../things-to-do-in-paris-in-winter/">Enjoy Paris in winter</a></h3><p>Lights, ice rinks and museums: our pick for the short days of December.</p>'
         '\n<h2>Our tips</h2><ul><li><strong>Book your trains early</strong>: the first and last days of the holidays are the busiest.</li><li><strong>On the slopes, both weeks are peak season</strong>: book accommodation and equipment now.</li><li><strong>For the Alsace markets</strong>, go on the first weekend of the holidays.</li></ul><p class="maj">Holiday dates: decree of 22 October 2025 (Journal officiel, 23 October 2025). Other dates checked in November 2026; check before you go.</p>')
    return intro + h + ag + rest
P = dict(photo='megeve', og='megeve', date='2026-11-21',
 acts=[({'fr':'idees/stations-de-ski-ouvertes','en':'ideas/ski-resort-opening-dates'},0), ({'fr':'idees/reveillon-nouvel-an','en':'ideas/new-years-eve-france'},0)],
 fr=dict(path='idees/vacances-de-noel-2026', home='Accueil', crumbs=[('Idées','idees/')], crumb_last='Vacances de Noël 2026',
  title='Vacances de Noël 2026 : dates et où partir',
  desc='Vacances de Noël 2026 : du 19 décembre au 4 janvier 2027. Ski, marchés de Noël encore ouverts, réveillon, Côte d’Azur : le calendrier et nos idées.',
  h1='Vacances de Noël 2026 : les dates et où partir en France',
  lead='Du samedi 19 décembre 2026 au lundi 4 janvier 2027 : ski, marchés de Noël, réveillon ou soleil, notre calendrier des vacances.',
  body=body('fr'), book_lead='Deux idées à réserver pour les vacances de Noël.',
  faq=[('Quelles sont les dates des vacances de Noël 2026 ?','Du samedi 19 décembre 2026 au lundi 4 janvier 2027, jour de la reprise des cours. Les dates sont les mêmes pour les zones A, B et C et pour la Corse.'),
       ('Quels marchés de Noël sont ouverts pendant les vacances ?','Paris (Tuileries jusqu’au 3 janvier, Champs-Élysées jusqu’au 4 janvier), Nice, Cannes et Monaco jusqu’au 3 janvier 2027, Colmar jusqu’au 29 décembre et Strasbourg jusqu’au 24 décembre. Riquewihr et Kaysersberg ferment le 20 décembre.'),
       ('Les stations de ski sont-elles ouvertes pour les vacances de Noël ?','Oui : les grandes stations ouvrent entre fin novembre et le 19 décembre. Megève (ouverture générale) et La Grave ouvrent le 19 décembre, le premier jour des vacances. Tout reste sous réserve d’enneigement.')],
  cards_t='Nos guides pour les fêtes', cards=[dict(href='idees/stations-de-ski-ouvertes/',photo='val-thorens',name='Ski',txt='Les dates d’ouverture des stations.'),dict(href='idees/marches-de-noel-france/',photo='noel-a-paris',name='Marchés de Noël',txt='Le calendrier 2026 en France.'),dict(href='idees/reveillon-nouvel-an/',photo='noel-riviera',name='Nouvel An',txt='Paris et la Côte d’Azur.')]),
 en=dict(path='ideas/christmas-holidays-2026', home='Home', crumbs=[('Ideas','ideas/')], crumb_last='Christmas holidays 2026',
  title='Christmas holidays 2026 in France: dates and ideas',
  desc='French Christmas school holidays 2026: 19 December to 4 January 2027. Skiing, Christmas markets still open, New Year’s Eve, the Riviera: calendar and ideas.',
  h1='Christmas holidays 2026 in France: dates and where to go',
  lead='From Saturday 19 December 2026 to Monday 4 January 2027: skiing, Christmas markets, New Year’s Eve or sunshine, our holiday calendar.',
  body=body('en'), book_lead='Two ideas to book for the Christmas holidays.',
  faq=[('What are the French Christmas school holiday dates in 2026?','From Saturday 19 December 2026 to Monday 4 January 2027, when school resumes. The dates are the same for zones A, B and C and for Corsica.'),
       ('Which Christmas markets are open during the holidays?','Paris (Tuileries until 3 January, Champs-Élysées until 4 January), Nice, Cannes and Monaco until 3 January 2027, Colmar until 29 December and Strasbourg until 24 December. Riquewihr and Kaysersberg close on 20 December.'),
       ('Are ski resorts open for the Christmas holidays?','Yes: the big resorts open between late November and 19 December. Megève (full opening) and La Grave open on 19 December, the first day of the holidays. Everything depends on snow conditions.')],
  cards_t='Our holiday guides', cards=[dict(href='ideas/ski-resort-opening-dates/',photo='val-thorens',name='Skiing',txt='Resort opening dates.'),dict(href='ideas/christmas-markets-france/',photo='noel-a-paris',name='Christmas markets',txt='The 2026 calendar in France.'),dict(href='ideas/new-years-eve-france/',photo='noel-riviera',name='New Year’s Eve',txt='Paris and the French Riviera.')]))
for l in ('fr','en'):
    assert len(P[l]['title']) <= 58, (l, len(P[l]['title'])); assert len(P[l]['desc']) <= 160, (l, len(P[l]['desc']))
    print(build(P, l))
