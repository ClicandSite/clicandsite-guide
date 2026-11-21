import sys
sys.path.insert(0,'/tmp/g')
exec(open('/tmp/g/seo_pass_1116.py').read().split("MAJ_FR=")[0])  # charge fr() et add()
R='/home/claude/'
MAJ_FR='Tarifs et dates relevés le 16 novembre 2026 auprès de la station, de l’office de tourisme et des grilles publiées pour 2026-2027 ; ils peuvent changer en cours de saison, vérifiez avant de partir.'
MAJ_EN='Prices and dates checked on 16 November 2026 with the resort, the tourist office and the published 2026-2027 price lists; they can change during the season, so check before you go.'

add(R+'clicandsite-guide/alpes/megeve/index.html','<h2>Nos conseils pour profiter de Megève</h2>','Infos pratiques 2026 : Megève',[
 ('Calendrier','ouverture partielle le week-end des 5 et 6 décembre 2026 (forfait unique à 38 €), puis tous les jours dès le 12 décembre ; ouverture générale le 19 décembre 2026 et fermeture le 4 avril 2027.'),
 ('Forfait Évasion Mont-Blanc','65 € la journée adulte (15-64 ans) du 19 décembre 2026 au 20 mars 2027, 55,50 € pour les 5-14 ans et 58,50 € pour les 65-79 ans.'),
 ('Tarif « première neige »','52 € la journée adulte du 12 au 18 décembre 2026, et de nouveau au printemps, du 21 mars au 4 avril 2027.'),
 ('Piétons','forfait journée à 23 € pour monter aux restaurants et aux points de vue.')],MAJ_FR,
 faq=('Combien coûte le forfait à Megève en 2026-2027 ?','Le forfait Évasion Mont-Blanc coûte 65 € la journée adulte en haute saison et 52 € en début et en fin de saison.'),
 subs=[('jusqu’au début avril 2027, selon l’enneigement','jusqu’au 4 avril 2027, selon l’enneigement'),('<dd>Début avril 2027</dd>','<dd>4 avril 2027</dd>')])
add(R+'clicandsite-guide-en/french-alps/megeve/index.html','<h2>Tips for a ski trip to Megève</h2>','Practical info 2026: Megève',[
 ('Calendar','partial opening on the weekend of 5-6 December 2026 (single €38 pass), then daily from 12 December; full opening on 19 December 2026 and closing on 4 April 2027.'),
 ('Évasion Mont-Blanc pass','€65 a day for an adult (15-64) from 19 December 2026 to 20 March 2027, €55.50 for ages 5-14 and €58.50 for ages 65-79.'),
 ('“First snow” rate','€52 a day for an adult from 12 to 18 December 2026, and again in spring, from 21 March to 4 April 2027.'),
 ('Pedestrians','€23 day pass to ride up to the restaurants and viewpoints.')],MAJ_EN,
 faq=('How much is a lift pass in Megève in 2026-2027?','The Évasion Mont-Blanc pass costs €65 a day for an adult in high season and €52 early and late in the season.'),
 subs=[('until early April 2027, depending on snow','until 4 April 2027, depending on snow'),('<dd>Early April 2027</dd>','<dd>4 April 2027</dd>')])

add(R+'clicandsite-guide/alpes/la-clusaz/index.html','<h2>Nos conseils pour profiter de La Clusaz</h2>','Infos pratiques 2026 : La Clusaz',[
 ('Saison','du 12 décembre 2026 au 25 avril 2027 sur le domaine La Clusaz-Manigod, sous réserve d’enneigement.'),
 ('Forfait journée','56,50 € pour un adulte (15-64 ans) en caisse.'),
 ('Forfait saison','le forfait Intégral La Clusaz-Manigod est à -15 % jusqu’au 21 décembre 2026, plein tarif ensuite.'),
 ('Parking','parking du Salon des Dames à 5 € la journée.')],MAJ_FR,
 faq=('Combien coûte le forfait à La Clusaz en 2026-2027 ?','56,50 € la journée pour un adulte en caisse, sur le domaine La Clusaz-Manigod.'))
add(R+'clicandsite-guide-en/french-alps/la-clusaz/index.html','<h2>Tips for a ski trip to La Clusaz</h2>','Practical info 2026: La Clusaz',[
 ('Season','12 December 2026 to 25 April 2027 on the La Clusaz-Manigod ski area, snow permitting.'),
 ('Day pass','€56.50 for an adult (15-64) at the ticket office.'),
 ('Season pass','the Intégral La Clusaz-Manigod pass is 15% off until 21 December 2026, full price after that.'),
 ('Parking','Salon des Dames car park at €5 a day.')],MAJ_EN,
 faq=('How much is a lift pass in La Clusaz in 2026-2027?','€56.50 a day for an adult at the ticket office, on the La Clusaz-Manigod ski area.'))

add(R+'clicandsite-guide/alpes/avoriaz/index.html','<h2>Nos conseils pour profiter d’Avoriaz</h2>','Infos pratiques 2026 : Avoriaz',[
 ('Saison','domaine ouvert du 11 décembre 2026 au 18 avril 2027 ; les 11, 12 et 13 décembre, pendant le festival Rock on Snow, la journée adulte coûte 27,50 €.'),
 ('Forfait Avoriaz','44,50 € la journée adulte (26-64 ans), 34,50 € pour les 5-15 ans ; 195,50 € les 6 jours adulte.'),
 ('Forfait Portes du Soleil','69 € la journée adulte du 19 décembre 2026 au 19 mars 2027, 62 € du 20 mars au 18 avril 2027.'),
 ('Débutants','forfait débutant à 33 € les 5 heures.')],MAJ_FR,
 faq=('Combien coûte le forfait à Avoriaz en 2026-2027 ?','44,50 € la journée adulte sur le domaine d’Avoriaz, et 69 € sur tout le domaine des Portes du Soleil en haute saison.'),
 subs=[(', avec des week-ends de préouverture fin novembre et début décembre selon l’enneigement.',', sous réserve d’enneigement.'),
       (', avec une préouverture partielle fin novembre et début décembre selon l’enneigement.',', sous réserve d’enneigement.'),
       ('<dd>11 décembre 2026 (préouverture fin novembre)</dd>','<dd>11 décembre 2026</dd>')])
add(R+'clicandsite-guide-en/french-alps/avoriaz/index.html','<h2>Tips for a ski trip to Avoriaz</h2>','Practical info 2026: Avoriaz',[
 ('Season','the ski area is open from 11 December 2026 to 18 April 2027; on 11, 12 and 13 December, during the Rock on Snow festival, an adult day pass costs €27.50.'),
 ('Avoriaz pass','€44.50 a day for an adult (26-64), €34.50 for ages 5-15; €195.50 for 6 days for an adult.'),
 ('Portes du Soleil pass','€69 a day for an adult from 19 December 2026 to 19 March 2027, €62 from 20 March to 18 April 2027.'),
 ('Beginners','beginner pass at €33 for 5 hours.')],MAJ_EN,
 faq=('How much is a lift pass in Avoriaz in 2026-2027?','€44.50 a day for an adult on the Avoriaz ski area, and €69 for the whole Portes du Soleil in high season.'),
 subs=[(', with early-opening weekends in late November and early December depending on snow.',', snow permitting.'),
       (', with a partial early opening in late November and early December depending on snow.',', snow permitting.'),
       ('<dd>11 December 2026 (early opening late November)</dd>','<dd>11 December 2026</dd>')])

add(R+'clicandsite-guide/pyrenees/cauterets/index.html','<h2>Nos conseils pour profiter de Cauterets</h2>','Infos pratiques 2026 : Cauterets',[
 ('Saison','Cirque du Lys ouvert du 27 novembre 2026 au 18 avril 2027, sous réserve d’enneigement.'),
 ('Forfait journée','46 € pour un adulte, 41 € en tarif réduit (5-17 ans) ; en ligne, des journées promo jusqu’à -40 % selon un calendrier.'),
 ('Ski et déjeuner','formule à 60 € : journée de ski, plat, dessert et café au restaurant d’altitude.'),
 ('Forfait saison','699 € pour le forfait Premium adulte.')],MAJ_FR,
 faq=('Combien coûte le forfait à Cauterets en 2026-2027 ?','46 € la journée pour un adulte et 41 € pour les 5-17 ans au Cirque du Lys, avec des journées jusqu’à -40 % en ligne.'))
add(R+'clicandsite-guide-en/pyrenees/cauterets/index.html','<h2>Tips for a ski trip to Cauterets</h2>','Practical info 2026: Cauterets',[
 ('Season','the Cirque du Lys is open from 27 November 2026 to 18 April 2027, snow permitting.'),
 ('Day pass','€46 for an adult, €41 at the reduced rate (ages 5-17); online, promo days up to 40% off on set dates.'),
 ('Ski and lunch','€60 deal: a day’s skiing plus a main course, dessert and coffee at the mountain restaurant.'),
 ('Season pass','€699 for the adult Premium pass.')],MAJ_EN,
 faq=('How much is a lift pass in Cauterets in 2026-2027?','€46 a day for an adult and €41 for ages 5-17 at the Cirque du Lys, with days up to 40% off online.'))
