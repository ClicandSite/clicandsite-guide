# Mise à jour Carnaval de Nice 2027 (programme dévoilé le 12/11/2026) — nuit du 22/11/2026
import sys
NB=' '
FR='/home/claude/clicandsite-guide/cote-d-azur/carnaval-de-nice/index.html'
EN='/home/claude/clicandsite-guide-en/french-riviera/nice-carnival/index.html'
fr=[
('les mercredis 10, 17 et 24 et les samedis 13, 20 et 27 février 2027, de 14 h 30 à 16 h. Gratuit pour les moins de 6 ans.',
 'les mercredis 17 et 24 et les samedis 20 et 27 février 2027, à 14 h 30. Nouveau parcours en 2027 : depuis la place Masséna, les chars rejoignent la promenade des Anglais et le quai des États-Unis. Places debout (promenoirs) gratuites sur réservation.'),
('Le premier a lieu le samedi 13 février à 21 h.',
 'Le corso d’ouverture a lieu le samedi 13 février à 21 h ; le corso de clôture, le samedi 27 février à 20 h 30, se termine par l’incinération du Roi et un feu d’artifice.'),
('mercredis 10, 17 et 24 et samedis 13, 20 et 27 février 2027, sous réserve',
 'mercredis 17 et 24 et samedis 20 et 27 février 2027 à 14 h 30, avec plus de 2'+NB+'000 places supplémentaires sur le quai des États-Unis, sous réserve'),
('place Masséna ; les fiches 2027 du comité régional du tourisme indiquent 20 h 30 les mardis 16 et 23 et le samedi 20 février. Programme complet sur nicecarnaval.com.',
 'place Masséna : ouverture le samedi 13 février à 21 h, puis 20 h 30 les mardis 16 et 23 et le samedi 20 février, et clôture le samedi 27 février à 20 h 30 (incinération du Roi et feu d’artifice). Programme complet sur nicecarnaval.com.'),
('<li><strong>Billets</strong> : tarifs 2027 « non communiqués » à la mi-novembre 2026. Toute entrée gratuite nécessite quand même un billet ;',
 '<li><strong>Billets</strong> : nouveauté 2027, les promenoirs (places debout) des corsos et des batailles de fleurs deviennent gratuits, sur réservation préalable ; l’ouverture des réservations grand public est annoncée pour début janvier 2027. Les tribunes restent payantes (légère hausse annoncée, tarifs pas encore publiés). Toute entrée gratuite nécessite quand même un billet ;'),
('Dates et horaires relevés le 15 novembre 2026 sur les fiches de Côte d’Azur France (comité régional du tourisme) ; le site officiel du carnaval n’a pas pu être consulté ce jour-là, vérifiez avant de réserver.',
 'Programme relevé en novembre 2026 sur le site de l’Office de tourisme Nice Côte d’Azur (annonce de la Ville du 12 novembre 2026) et les fiches de Côte d’Azur France ; vérifiez sur nicecarnaval.com avant de réserver.'),
('Les mercredis 10, 17 et 24 et les samedis 13, 20 et 27 février 2027, de 14 h 30 à 16 h, place Masséna.',
 'Les mercredis 17 et 24 et les samedis 20 et 27 février 2027 à 14 h 30, au départ de la place Masséna, sur la promenade des Anglais et le quai des États-Unis.'),
('Les tarifs grand public 2027 n’étaient pas encore publiés en novembre 2026. Les places en tribune sont plus chères que les places debout en promenoir ; l’entrée est gratuite pour les moins de 6 ans.',
 'En 2027, les places debout en promenoir sont gratuites, sur réservation préalable (ouverture annoncée début janvier 2027). Les tribunes restent payantes ; leurs tarifs 2027 n’étaient pas encore publiés en novembre 2026.'),
('Mis à jour le 15 novembre 2026','Mis à jour le 22 novembre 2026'),
('du 9 au 28 février : batailles de fleurs, corsos illuminés et corso d’Aqui place Masséna, billets et accès.',
 'du 9 au 28 février : batailles de fleurs, corsos illuminés, promenoirs gratuits sur réservation, billets et accès.'),
]
en=[
('on Wednesdays 10, 17 and 24 and Saturdays 13, 20 and 27 February 2027, from 2:30 to 4pm. Free for under-6s.',
 'on Wednesdays 17 and 24 and Saturdays 20 and 27 February 2027, at 2:30pm. New route in 2027: from Place Masséna, the floats head along the Promenade des Anglais and the Quai des États-Unis. Standing places are free with advance booking.'),
('The first is on Saturday 13 February at 9pm.',
 'The opening parade is on Saturday 13 February at 9pm; the closing parade, on Saturday 27 February at 8:30pm, ends with the burning of the King and fireworks.'),
('Wednesdays 10, 17 and 24 and Saturdays 13, 20 and 27 February 2027, weather permitting',
 'Wednesdays 17 and 24 and Saturdays 20 and 27 February 2027 at 2:30pm, with over 2,000 extra places on the Quai des États-Unis, weather permitting'),
('on Place Masséna; the regional tourist board’s 2027 listings give 8:30pm on Tuesdays 16 and 23 and Saturday 20 February. Full programme on nicecarnaval.com.',
 'on Place Masséna: opening on Saturday 13 February at 9pm, then 8:30pm on Tuesdays 16 and 23 and Saturday 20 February, and closing on Saturday 27 February at 8:30pm (burning of the King and fireworks). Full programme on nicecarnaval.com.'),
('<li><strong>Tickets</strong>: 2027 prices were still “not announced” in mid-November 2026. Free entry still requires a ticket;',
 '<li><strong>Tickets</strong>: new for 2027, the standing areas (promenoirs) for the parades and flower battles are free, with advance booking; public bookings are announced to open in early January 2027. Grandstand seats remain paid (a small increase has been announced, prices not yet published). Free entry still requires a ticket;'),
('from 2:30 to 4pm on Place Masséna.',
 'at 2:30pm, starting from Place Masséna along the Promenade des Anglais and the Quai des États-Unis.'),
('Public prices for 2027 had not been published in November 2026. Grandstand seats cost more than standing places; entry is free for under-6s.',
 'In 2027, standing places are free with advance booking (bookings announced to open in early January 2027). Grandstand seats remain paid; their 2027 prices had not been published in November 2026.'),
('Updated 15 November 2026','Updated 22 November 2026'),
('flower parades, illuminated parades and Corso d’Aqui on Place Masséna, tickets and access.',
 'flower parades, illuminated parades, free standing places with booking, tickets and access.'),
]
import re
def nb(x):
    for c in ':;?!':
        x=x.replace(' '+c,NB+c)
    return x.replace('« ','«'+NB).replace(' »',NB+'»')
fr=[(nb(a),nb(b)) for a,b in fr]
def apply(path,reps,maj_new=None):
    t=open(path).read()
    for a,b in reps:
        n=t.count(a)
        if n==0: sys.exit(f'ABSENT {path}: {a[:60]}')
        t=t.replace(a,b)
    if maj_new:
        t=re.sub(r'class="maj">Dates and times checked on 15 November 2026[^<]*', 'class="maj">'+maj_new, t)
    open(path,'w').write(t)
apply(FR,fr)
apply(EN,en,'Programme checked in November 2026 on the Nice Côte d’Azur tourist office website (City announcement of 12 November 2026) and the Côte d’Azur France listings; check nicecarnaval.com before you book.')
print('ok')
# + EN FAQ : sed 's/On Wednesdays 10, 17 and 24 and Saturdays 13, 20 and 27 February 2027, at 2:30pm/On Wednesdays 17 and 24 and Saturdays 20 and 27 February 2027, at 2:30pm/g'
