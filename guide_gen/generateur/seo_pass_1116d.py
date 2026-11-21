exec(open('/tmp/g/seo_pass_1116.py').read().split("MAJ_FR=")[0])
R='/home/claude/'
MAJ_FR='Tarifs et dates relevés le 16 novembre 2026 auprès de la station, de l’office de tourisme et des grilles publiées pour 2026-2027 ; ils peuvent changer en cours de saison, vérifiez avant de partir.'
MAJ_EN='Prices and dates checked on 16 November 2026 with the resort, the tourist office and the published 2026-2027 price lists; they can change during the season, so check before you go.'
def rep(path, pairs):
    s=open(path).read()
    for a,b in pairs:
        assert a in s,(path,a); s=s.replace(a,b)
    open(path,'w').write(s); print('rep',path)

add(R+'clicandsite-guide/alpes/la-grave/index.html','<h2>Nos conseils pour profiter de La Grave</h2>','Infos pratiques 2026 : La Grave',[
 ('Saison','téléphériques ouverts du 19 décembre 2026 au 2 mai 2027, de 8 h 30 (première montée) à 16 h (dernière descente depuis 3 200 m).'),
 ('Forfait journée','68 € pour les téléphériques et le téléski ; le téléski sommital dépend de la météo et n’est pas garanti.'),
 ('Piétons','aller-retour panorama jusqu’à 3 200 m pour 37 €.')],
 'Tarifs et horaires relevés le 16 novembre 2026 auprès de l’office de tourisme des Hautes Vallées ; ils peuvent changer, vérifiez avant de partir.',
 faq=('Combien coûte le téléphérique de La Grave en 2026-2027 ?','68 € la journée pour skier (téléphériques et téléski), 37 € l’aller-retour piéton jusqu’à 3 200 m.'),
 subs=[('du 20 décembre 2026 au 3 mai 2027','du 19 décembre 2026 au 2 mai 2027'),('<dd>20 décembre 2026</dd>','<dd>19 décembre 2026</dd>'),('<dd>3 mai 2027</dd>','<dd>2 mai 2027</dd>')])
add(R+'clicandsite-guide-en/french-alps/la-grave/index.html','<h2>Tips for a ski trip to La Grave</h2>','Practical info 2026: La Grave',[
 ('Season','the cable cars run from 19 December 2026 to 2 May 2027, from 8.30am (first ride up) to 4pm (last ride down from 3,200 m).'),
 ('Day pass','€68 for the cable cars and the drag lift; the summit drag lift depends on the weather and is not guaranteed.'),
 ('Pedestrians','panorama return trip to 3,200 m for €37.')],
 'Prices and times checked on 16 November 2026 with the Hautes Vallées tourist office; they can change, so check before you go.',
 faq=('How much is the La Grave cable car in 2026-2027?','€68 a day for skiing (cable cars and drag lift), €37 for a pedestrian return trip to 3,200 m.'),
 subs=[('from 20 December 2026 to 3 May 2027','from 19 December 2026 to 2 May 2027'),('<dd>20 December 2026</dd>','<dd>19 December 2026</dd>'),('<dd>3 May 2027</dd>','<dd>2 May 2027</dd>')])
rep(R+'clicandsite-guide/idees/stations-de-ski-ouvertes/index.html',[('<span class="ag__d">20 déc.</span><div class="ag__b"><strong><a href="../../alpes/la-grave/">La Grave</a></strong><p>Téléphérique et freeride, jusqu’au 3 mai 2027.</p>','<span class="ag__d">19 déc.</span><div class="ag__b"><strong><a href="../../alpes/la-grave/">La Grave</a></strong><p>Téléphérique et freeride, jusqu’au 2 mai 2027.</p>')])
rep(R+'clicandsite-guide-en/ideas/ski-resort-opening-dates/index.html',[('<span class="ag__d">20 Dec</span><div class="ag__b"><strong><a href="../../french-alps/la-grave/">La Grave</a></strong><p>Cable car and freeride, until 3 May 2027.</p>','<span class="ag__d">19 Dec</span><div class="ag__b"><strong><a href="../../french-alps/la-grave/">La Grave</a></strong><p>Cable car and freeride, until 2 May 2027.</p>')])

add(R+'clicandsite-guide/alpes/superdevoluy/index.html','<h2>Nos conseils pour profiter du Dévoluy</h2>','Infos pratiques 2026 : Dévoluy',[
 ('Saison','domaine de SuperDévoluy et de La Joue du Loup ouvert en continu du 12 décembre 2026 au 11 avril 2027.'),
 ('Forfait journée','46 € pour un adulte, 39 € pour les enfants, les seniors et les étudiants de 18 à 25 ans.'),
 ('Forfait 6 jours','226 € pour un adulte.')],MAJ_FR,
 faq=('Combien coûte le forfait au Dévoluy en 2026-2027 ?','46 € la journée pour un adulte, 39 € en tarif réduit, et 226 € les 6 jours adulte.'))
add(R+'clicandsite-guide-en/french-alps/superdevoluy/index.html','<h2>Tips for a ski trip to the Dévoluy</h2>','Practical info 2026: the Dévoluy',[
 ('Season','the SuperDévoluy and La Joue du Loup ski area is open daily from 12 December 2026 to 11 April 2027.'),
 ('Day pass','€46 for an adult, €39 for children, seniors and students aged 18 to 25.'),
 ('6-day pass','€226 for an adult.')],MAJ_EN,
 faq=('How much is a lift pass in the Dévoluy in 2026-2027?','€46 a day for an adult, €39 at the reduced rate, and €226 for 6 days for an adult.'))

add(R+'clicandsite-guide/alpes/chatel/index.html','<h2>Nos conseils pour profiter de Châtel</h2>','Infos pratiques 2026 : Châtel',[
 ('Forfait Espace Liberté','55 € la journée adulte (26-64 ans) en ligne, 41 € pour les 5-15 ans, 50 € pour les 16-25 ans et les 65 ans et plus.'),
 ('Le samedi','forfait Espace Liberté à 44 € la journée pour un adulte.'),
 ('Forfait Portes du Soleil','à partir de 69 € la journée adulte en ligne avant le 19 décembre 2026, pour les 600 km de pistes du domaine franco-suisse.'),
 ('Snowpark','forfait journée à 33 € en ligne.')],MAJ_FR,
 faq=('Combien coûte le forfait à Châtel en 2026-2027 ?','55 € la journée adulte sur l’Espace Liberté (44 € le samedi), et à partir de 69 € pour les Portes du Soleil.'))
add(R+'clicandsite-guide-en/french-alps/chatel/index.html','<h2>Tips for a ski trip to Châtel</h2>','Practical info 2026: Châtel',[
 ('Espace Liberté pass','€55 a day for an adult (26-64) online, €41 for ages 5-15, €50 for ages 16-25 and 65 and over.'),
 ('On Saturdays','Espace Liberté pass at €44 a day for an adult.'),
 ('Portes du Soleil pass','from €69 a day for an adult online before 19 December 2026, for the 600 km of runs across France and Switzerland.'),
 ('Snowpark','day pass at €33 online.')],MAJ_EN,
 faq=('How much is a lift pass in Châtel in 2026-2027?','€55 a day for an adult on the Espace Liberté (€44 on Saturdays), and from €69 for the Portes du Soleil.'))

add(R+'clicandsite-guide/pyrenees/grand-tourmalet/index.html','<h2>Nos conseils pour profiter du Grand Tourmalet</h2>','Infos pratiques 2026 : Grand Tourmalet',[
 ('Saison','domaine de Barèges et La Mongie ouvert du 5 décembre 2026 au 29 mars 2027.'),
 ('Forfait journée','55 € pour un adulte (18-74 ans), 50 € pour les 5-17 ans ; assurance en option à 4 € par jour.'),
 ('Carte No Souci','la journée adulte descend à 38,50 € hors vacances et 46,80 € en vacances et le week-end.'),
 ('FastPass','60 € la journée adulte, avec passage prioritaire aux principales remontées.')],MAJ_FR,
 faq=('Combien coûte le forfait au Grand Tourmalet en 2026-2027 ?','55 € la journée pour un adulte et 50 € pour les 5-17 ans, moins avec la carte No Souci.'))
add(R+'clicandsite-guide-en/pyrenees/grand-tourmalet/index.html','<h2>Tips for a ski trip to the Grand Tourmalet</h2>','Practical info 2026: Grand Tourmalet',[
 ('Season','the Barèges and La Mongie ski area is open from 5 December 2026 to 29 March 2027.'),
 ('Day pass','€55 for an adult (18-74), €50 for ages 5-17; optional insurance at €4 a day.'),
 ('No Souci card','an adult day drops to €38.50 outside school holidays and €46.80 during holidays and at weekends.'),
 ('FastPass','€60 a day for an adult, with priority access to the main lifts.')],MAJ_EN,
 faq=('How much is a lift pass at the Grand Tourmalet in 2026-2027?','€55 a day for an adult and €50 for ages 5-17, less with the No Souci card.'))
