# Page « Paris le 25 décembre et le 1er janvier : ce qui est ouvert » FR + EN (nuit du 23/11/2026) — modèle winter_gen
# Faits repris uniquement des pages du guide (horaires relevés en novembre 2026) ; rien de nouveau.
import sys; sys.path.insert(0,'/tmp/g')
from winter_gen import build
def body(lang):
    if lang=='fr':
        return ('<p>Noël 2026 et le Jour de l’An 2027 tombent tous les deux un vendredi. Beaucoup de grands musées et monuments de Paris ferment ces jours-là, mais pas tous : voici ce qui reste ouvert, ce qui ferme, et nos idées pour en profiter. Liste établie à partir des horaires de nos guides, relevés en novembre 2026.</p>'
         '\n<h2>Ouvert le 25 décembre et le 1er janvier</h2><ul>'
         '<li><a href="../../paris/tour-eiffel/">La tour Eiffel</a> : ouverte tous les jours, y compris le 25 décembre et le 1er janvier, à partir de 9 h 30 ; le 31 décembre, elle ferme plus tôt, à 21 h.</li>'
         '<li><a href="../../paris/notre-dame/">Notre-Dame</a> : ouverte tous les jours, entrée gratuite (réservation conseillée).</li>'
         '<li><a href="../../paris/sacre-coeur/">Le Sacré-Cœur</a> : la basilique est ouverte tous les jours de 6 h 30 à 22 h 30, entrée libre.</li>'
         '<li><a href="../../paris/musee-grevin/">Le musée Grévin</a> : ouvert tous les jours, de 9 h 30 à 19 h les jours fériés et pendant les vacances scolaires.</li>'
         '<li><a href="../../paris/noel-a-paris/">Les marchés de Noël</a> : celui des Tuileries est ouvert tous les jours de 11 h à 23 h 30 jusqu’au 3 janvier 2027 ; celui des Champs-Élysées dure jusqu’au 4 janvier.</li></ul>'
         '\n<h2>Ouvert le 1er janvier, fermé le 25 décembre</h2><ul>'
         '<li><a href="../../paris/musee-d-orsay/">Le musée d’Orsay</a> : fermé le lundi, le 1er mai et le 25 décembre, il est donc ouvert le vendredi 1er janvier 2027.</li>'
         '<li><a href="../../paris/musee-de-l-orangerie/">Le musée de l’Orangerie</a> : fermé le mardi, le 1er mai, le matin du 14 juillet et le 25 décembre, il est ouvert le 1er janvier.</li>'
         '<li><a href="../../paris/conciergerie/">La Conciergerie</a> : ouverte tous les jours de 9 h 30 à 18 h, sauf le 1er mai et le 25 décembre.</li></ul>'
         '<p>Le 1er janvier, Orsay, l’Orangerie et la Conciergerie font partie des rares grands sites ouverts : réservez un billet à créneau horaire.</p>'
         '\n<h2>Fermé le 25 décembre et le 1er janvier</h2><ul>'
         '<li><a href="../../paris/louvre/">Le Louvre</a>, <a href="../../paris/versailles/">le château de Versailles</a> et <a href="../../paris/fontainebleau/">Fontainebleau</a></li>'
         '<li><a href="../../paris/arc-de-triomphe/">L’Arc de Triomphe</a>, <a href="../../paris/sainte-chapelle/">la Sainte-Chapelle</a>, <a href="../../paris/pantheon/">le Panthéon</a> et <a href="../../paris/chateau-de-vincennes/">le château de Vincennes</a></li>'
         '<li><a href="../../paris/invalides/">Les Invalides</a> (musée de l’Armée et tombeau de Napoléon)</li>'
         '<li><a href="../../paris/musee-picasso/">Le musée Picasso</a>, <a href="../../paris/musee-rodin/">le musée Rodin</a> et <a href="../../paris/catacombes/">les Catacombes</a></li>'
         '<li>La Cité des sciences, à <a href="../../paris/la-villette/">La Villette</a></li></ul>'
         '\n<h2>Nos idées pour ces deux jours</h2><ul>'
         '<li><strong>Une croisière sur la Seine</strong> : Paris illuminé depuis le fleuve, en journée ou avec un dîner ; voir notre <a href="../../paris/croisiere-sur-la-seine/">guide des croisières</a>.</li>'
         '<li><strong>Une balade à pied</strong> dans <a href="../../paris/montmartre/">Montmartre</a>, sur l’<a href="../../paris/ile-saint-louis/">île Saint-Louis</a> ou le long des <a href="../../paris/champs-elysees/">Champs-Élysées</a> illuminés.</li>'
         '<li><strong>Le Panthéon gratuit le dimanche 3 janvier 2027</strong> : il est gratuit pour tous le premier dimanche du mois, de novembre à mars.</li>'
         '<li><strong>La veille au soir</strong>, le 31 décembre, la Ville de Paris organise le feu d’artifice gratuit des Champs-Élysées : voir nos <a href="../reveillon-nouvel-an/">idées de réveillon</a>.</li></ul>'
         '<p>Les 24 et 31 décembre, certains sites ferment plus tôt que d’habitude : vérifiez les horaires sur le site officiel avant de partir. Pour toute la période, voir aussi nos <a href="../vacances-de-noel-2026/">idées pour les vacances de Noël</a> et <a href="../que-faire-a-paris-en-hiver/">que faire à Paris en hiver</a>.</p>'
         '<p class="maj">Horaires relevés en novembre 2026 sur nos pages de chaque lieu ; ils peuvent changer, vérifiez avant de partir.</p>')
    return ('<p>Christmas Day 2026 and New Year’s Day 2027 both fall on a Friday. Many of the big museums and monuments in Paris close on those days, but not all: here is what stays open, what closes, and our ideas to make the most of them. List based on the opening times in our guides, checked in November 2026.</p>'
         '\n<h2>Open on 25 December and 1 January</h2><ul>'
         '<li><a href="../../paris/eiffel-tower/">The Eiffel Tower</a>: open every day, including 25 December and 1 January, from 9.30am; on 31 December it closes earlier, at 9pm.</li>'
         '<li><a href="../../paris/notre-dame/">Notre-Dame</a>: open every day, free entry (booking recommended).</li>'
         '<li><a href="../../paris/sacre-coeur/">The Sacré-Cœur</a>: the basilica is open every day from 6.30am to 10.30pm, free entry.</li>'
         '<li><a href="../../paris/musee-grevin/">The Musée Grévin</a>: open every day, from 9.30am to 7pm on public holidays and during the school holidays.</li>'
         '<li><a href="../../paris/christmas-in-paris/">The Christmas markets</a>: the Tuileries market is open every day from 11am to 11.30pm until 3 January 2027; the Champs-Élysées market runs until 4 January.</li></ul>'
         '\n<h2>Open on 1 January, closed on 25 December</h2><ul>'
         '<li><a href="../../paris/musee-d-orsay/">The Musée d’Orsay</a>: closed on Mondays, 1 May and 25 December, so it is open on Friday 1 January 2027.</li>'
         '<li><a href="../../paris/musee-de-l-orangerie/">The Musée de l’Orangerie</a>: closed on Tuesdays, 1 May, the morning of 14 July and 25 December, so it is open on 1 January.</li>'
         '<li><a href="../../paris/conciergerie/">The Conciergerie</a>: open every day from 9.30am to 6pm, except 1 May and 25 December.</li></ul>'
         '<p>On 1 January, Orsay, the Orangerie and the Conciergerie are among the few major sights open: book a timed ticket.</p>'
         '\n<h2>Closed on 25 December and 1 January</h2><ul>'
         '<li><a href="../../paris/louvre/">The Louvre</a>, <a href="../../paris/versailles/">the Palace of Versailles</a> and <a href="../../paris/fontainebleau/">Fontainebleau</a></li>'
         '<li><a href="../../paris/arc-de-triomphe/">The Arc de Triomphe</a>, <a href="../../paris/sainte-chapelle/">the Sainte-Chapelle</a>, <a href="../../paris/pantheon/">the Panthéon</a> and <a href="../../paris/chateau-de-vincennes/">the Château de Vincennes</a></li>'
         '<li><a href="../../paris/invalides/">Les Invalides</a> (Army Museum and Napoleon’s tomb)</li>'
         '<li><a href="../../paris/musee-picasso/">The Musée Picasso</a>, <a href="../../paris/musee-rodin/">the Musée Rodin</a> and <a href="../../paris/catacombs/">the Catacombs</a></li>'
         '<li>The Cité des sciences at <a href="../../paris/la-villette/">La Villette</a></li></ul>'
         '\n<h2>Our ideas for these two days</h2><ul>'
         '<li><strong>A Seine cruise</strong>: Paris lit up from the river, by day or with dinner; see our <a href="../../paris/seine-cruise/">Seine cruise guide</a>.</li>'
         '<li><strong>A walk</strong> around <a href="../../paris/montmartre/">Montmartre</a>, the <a href="../../paris/ile-saint-louis/">Île Saint-Louis</a> or along the illuminated <a href="../../paris/champs-elysees/">Champs-Élysées</a>.</li>'
         '<li><strong>Free Panthéon on Sunday 3 January 2027</strong>: entry is free for everyone on the first Sunday of the month, from November to March.</li>'
         '<li><strong>The night before</strong>, on 31 December, the City of Paris puts on the free Champs-Élysées fireworks: see our <a href="../new-years-eve-france/">New Year’s Eve ideas</a>.</li></ul>'
         '<p>On 24 and 31 December, some sites close earlier than usual: check the opening times on the official website before you go. For the whole period, see also our <a href="../christmas-holidays-2026/">Christmas holiday ideas</a> and <a href="../things-to-do-in-paris-in-winter/">things to do in Paris in winter</a>.</p>'
         '<p class="maj">Opening times checked in November 2026 on our page for each place; they may change, check before you go.</p>')
P = dict(photo='noel-a-paris', og='noel-a-paris', date='2026-11-23',
 acts=[({'fr':'paris/musee-d-orsay','en':'paris/musee-d-orsay'},0), ({'fr':'paris/noel-a-paris','en':'paris/christmas-in-paris'},0),
       ({'fr':'paris/noel-a-paris','en':'paris/christmas-in-paris'},1), ({'fr':'paris/croisiere-sur-la-seine','en':'paris/seine-cruise'},0)],
 fr=dict(path='idees/paris-25-decembre-1er-janvier', home='Accueil', crumbs=[('Idées','idees/')], crumb_last='Paris le 25 décembre et le 1er janvier',
  title='Paris le 25 décembre et le 1er janvier : ce qui est ouvert',
  desc='Noël et Jour de l’An à Paris : musées et monuments ouverts ou fermés le 25 décembre 2026 et le 1er janvier 2027 (Orsay, Louvre, Notre-Dame…) et sorties.',
  h1='Paris le 25 décembre et le 1er janvier : ce qui est ouvert, ce qui est fermé',
  lead='Orsay ouvert le 1er janvier, Louvre et Versailles fermés, Notre-Dame et le Sacré-Cœur tous les jours : le point pour Noël 2026 et le Jour de l’An 2027.',
  body=body('fr'), book_lead='Quelques idées à réserver pour les fêtes.',
  faq=[('Quels musées sont ouverts le 1er janvier à Paris ?','Parmi les grands musées, le musée d’Orsay et le musée de l’Orangerie sont ouverts le 1er janvier ; le Louvre, Versailles, le musée Picasso et le musée Rodin sont fermés. Notre-Dame, le Sacré-Cœur et le musée Grévin sont ouverts tous les jours.'),
       ('La tour Eiffel est-elle ouverte le 25 décembre et le 1er janvier ?','Oui, la tour Eiffel est ouverte tous les jours, y compris le 25 décembre et le 1er janvier, à partir de 9 h 30. Le 31 décembre 2026, elle ferme plus tôt, à 21 h.'),
       ('Le Louvre est-il ouvert le 25 décembre ?','Non, le Louvre est fermé le 25 décembre, le 1er janvier et le 1er mai, ainsi que tous les mardis.'),
       ('Que faire à Paris le jour de Noël ?','Visiter Notre-Dame ou le Sacré-Cœur, flâner au marché de Noël des Tuileries (ouvert tous les jours jusqu’au 3 janvier 2027), voir les illuminations des Champs-Élysées ou faire une croisière sur la Seine.')],
  cards_t='Nos guides pour les fêtes', cards=[dict(href='idees/reveillon-nouvel-an/',photo='champs-elysees',name='Réveillon du Nouvel An',txt='Feu d’artifice et soirées.'),dict(href='idees/vacances-de-noel-2026/',photo='megeve',name='Vacances de Noël',txt='Du 19 décembre au 4 janvier.'),dict(href='paris/noel-a-paris/',photo='noel-a-paris',name='Noël à Paris',txt='Marchés, vitrines et illuminations.')]),
 en=dict(path='ideas/paris-christmas-day-new-years-day', home='Home', crumbs=[('Ideas','ideas/')], crumb_last='Paris on 25 December and 1 January',
  title='Paris on Christmas Day and New Year’s Day: what’s open',
  desc='Christmas and New Year’s Day in Paris: museums and monuments open or closed on 25 December 2026 and 1 January 2027 (Orsay, Louvre, Notre-Dame…) and ideas.',
  h1='Paris on Christmas Day and New Year’s Day: what’s open and what’s closed',
  lead='Orsay open on 1 January, the Louvre and Versailles closed, Notre-Dame and the Sacré-Cœur every day: the lowdown for Christmas 2026 and New Year’s Day 2027.',
  body=body('en'), book_lead='A few ideas to book for the holidays.',
  faq=[('Which museums are open on 1 January in Paris?','Among the major museums, the Musée d’Orsay and the Musée de l’Orangerie are open on 1 January; the Louvre, Versailles, the Musée Picasso and the Musée Rodin are closed. Notre-Dame, the Sacré-Cœur and the Musée Grévin are open every day.'),
       ('Is the Eiffel Tower open on Christmas Day and New Year’s Day?','Yes, the Eiffel Tower is open every day, including 25 December and 1 January, from 9.30am. On 31 December 2026 it closes earlier, at 9pm.'),
       ('Is the Louvre open on Christmas Day?','No, the Louvre is closed on 25 December, 1 January and 1 May, as well as every Tuesday.'),
       ('What can I do in Paris on Christmas Day?','Visit Notre-Dame or the Sacré-Cœur, stroll around the Tuileries Christmas market (open every day until 3 January 2027), see the Champs-Élysées lights or take a Seine cruise.')],
  cards_t='Our holiday guides', cards=[dict(href='ideas/new-years-eve-france/',photo='champs-elysees',name='New Year’s Eve',txt='Fireworks and parties.'),dict(href='ideas/christmas-holidays-2026/',photo='megeve',name='Christmas holidays',txt='19 December to 4 January.'),dict(href='paris/christmas-in-paris/',photo='noel-a-paris',name='Christmas in Paris',txt='Markets, windows and lights.')]))
for l in ('fr','en'):
    assert len(P[l]['title']) <= 58, (l, len(P[l]['title'])); assert len(P[l]['desc']) <= 160, (l, len(P[l]['desc']))
    print(build(P, l))
