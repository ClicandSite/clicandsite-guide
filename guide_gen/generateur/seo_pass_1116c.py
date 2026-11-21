exec(open('/tmp/g/seo_pass_1116.py').read().split("MAJ_FR=")[0])
R='/home/claude/'
MAJ_FR='Tarifs et dates relevés le 16 novembre 2026 auprès de la station, de l’office de tourisme et des grilles publiées pour 2026-2027 ; ils peuvent changer en cours de saison, vérifiez avant de partir.'
MAJ_EN='Prices and dates checked on 16 November 2026 with the resort, the tourist office and the published 2026-2027 price lists; they can change during the season, so check before you go.'

add(R+'clicandsite-guide/alpes/les-2-alpes/index.html','<h2>Nos conseils pour profiter des 2 Alpes</h2>','Infos pratiques 2026 : Les 2 Alpes',[
 ('Week-end d’ouverture','les 28 et 29 novembre 2026, la journée coûte 42 € et le forfait 2 jours 84 €.'),
 ('Début de saison','54,50 € la journée adulte du 28 novembre au 4 décembre 2026.'),
 ('Haute saison','68 € la journée adulte du 19 décembre 2026 au 9 avril 2027, 54,50 € pour un enfant ; 333 € les 6 jours adulte.'),
 ('Piétons','accès au domaine piéton, dont le glacier, à partir de 33 € la journée.')],MAJ_FR,
 faq=('Combien coûte le forfait aux 2 Alpes en 2026-2027 ?','68 € la journée adulte en haute saison, 54,50 € en début de saison, et 42 € pendant le week-end d’ouverture des 28 et 29 novembre 2026.'))
add(R+'clicandsite-guide-en/french-alps/les-2-alpes/index.html','<h2>Tips for a ski trip to Les 2 Alpes</h2>','Practical info 2026: Les 2 Alpes',[
 ('Opening weekend','on 28 and 29 November 2026, a day pass costs €42 and a 2-day pass €84.'),
 ('Early season','€54.50 a day for an adult from 28 November to 4 December 2026.'),
 ('High season','€68 a day for an adult from 19 December 2026 to 9 April 2027, €54.50 for a child; €333 for 6 days for an adult.'),
 ('Pedestrians','access to the pedestrian area, including the glacier, from €33 a day.')],MAJ_EN,
 faq=('How much is a lift pass in Les 2 Alpes in 2026-2027?','€68 a day for an adult in high season, €54.50 early in the season, and €42 on the opening weekend of 28 and 29 November 2026.'))

add(R+'clicandsite-guide/alpes/montgenevre/index.html','<h2>Nos conseils pour profiter de Montgenèvre</h2>','Infos pratiques 2026 : Montgenèvre',[
 ('Saison','domaine ouvert du 28 novembre 2026 au 17 avril 2027.'),
 ('Forfait journée Montgenèvre','45,50 € pour un adulte (15-64 ans) jusqu’au 18 décembre 2026 et à partir du 12 avril 2027, 56 € en pleine saison.'),
 ('Domaine transfrontalier','avec les Monts de la Lune, côté italien, la journée coûte 2,50 € de plus ; 301 € les 6 jours adulte.')],MAJ_FR,
 faq=('Combien coûte le forfait à Montgenèvre en 2026-2027 ?','56 € la journée adulte en pleine saison et 45,50 € en début et en fin de saison sur le domaine de Montgenèvre ; ajoutez 2,50 € pour le domaine transfrontalier.'))
add(R+'clicandsite-guide-en/french-alps/montgenevre/index.html','<h2>Tips for a ski trip to Montgenèvre</h2>','Practical info 2026: Montgenèvre',[
 ('Season','the ski area is open from 28 November 2026 to 17 April 2027.'),
 ('Montgenèvre day pass','€45.50 for an adult (15-64) until 18 December 2026 and from 12 April 2027, €56 in the main season.'),
 ('Cross-border area','adding the Monts de la Lune, on the Italian side, costs €2.50 more a day; 6 days for an adult cost €301.')],MAJ_EN,
 faq=('How much is a lift pass in Montgenèvre in 2026-2027?','€56 a day for an adult in the main season and €45.50 early and late in the season on the Montgenèvre area; add €2.50 for the cross-border area.'))

add(R+'clicandsite-guide/pyrenees/saint-lary/index.html','<h2>Nos conseils pour profiter de Saint-Lary</h2>','Infos pratiques 2026 : Saint-Lary',[
 ('Saison','domaine ouvert du 4 décembre 2026 au 29 mars 2027, sous réserve d’enneigement.'),
 ('Forfait journée','54,70 € pour un adulte, 48,70 € au tarif famille.'),
 ('Forfait saison','778 € pour un adulte (18-64 ans).')],MAJ_FR,
 faq=('Combien coûte le forfait à Saint-Lary en 2026-2027 ?','54,70 € la journée pour un adulte et 48,70 € au tarif famille.'),
 subs=[('jusqu’à la fin mars ou au début avril 2027 selon l’enneigement','jusqu’au 29 mars 2027, selon l’enneigement'),('<dd>Fin mars ou début avril 2027</dd>','<dd>29 mars 2027</dd>')])
add(R+'clicandsite-guide-en/pyrenees/saint-lary/index.html','<h2>Tips for a ski trip to Saint-Lary</h2>','Practical info 2026: Saint-Lary',[
 ('Season','the ski area is open from 4 December 2026 to 29 March 2027, snow permitting.'),
 ('Day pass','€54.70 for an adult, €48.70 at the family rate.'),
 ('Season pass','€778 for an adult (18-64).')],MAJ_EN,
 faq=('How much is a lift pass in Saint-Lary in 2026-2027?','€54.70 a day for an adult and €48.70 at the family rate.'),
 subs=[('until late March or early April 2027 depending on snow','until 29 March 2027, depending on snow'),('<dd>Late March or early April 2027</dd>','<dd>29 March 2027</dd>')])

add(R+'clicandsite-guide/pyrenees/peyragudes/index.html','<h2>Nos conseils pour profiter de Peyragudes</h2>','Infos pratiques 2026 : Peyragudes',[
 ('Saison','préouverture du 5 au 9 décembre 2026, puis ouverture du 12 décembre 2026 au 29 mars 2027, de 9 h à 17 h.'),
 ('Forfait journée','51 € pour un adulte en haute saison.'),
 ('Forfait saison','767 € pour un adulte.')],MAJ_FR,
 faq=('Combien coûte le forfait à Peyragudes en 2026-2027 ?','51 € la journée pour un adulte en haute saison, et 767 € le forfait saison adulte.'))
add(R+'clicandsite-guide-en/pyrenees/peyragudes/index.html','<h2>Tips for a ski trip to Peyragudes</h2>','Practical info 2026: Peyragudes',[
 ('Season','early opening from 5 to 9 December 2026, then open from 12 December 2026 to 29 March 2027, 9am to 5pm.'),
 ('Day pass','€51 for an adult in high season.'),
 ('Season pass','€767 for an adult.')],MAJ_EN,
 faq=('How much is a lift pass in Peyragudes in 2026-2027?','€51 a day for an adult in high season, and €767 for an adult season pass.'))
