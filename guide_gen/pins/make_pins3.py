import sys; sys.path.insert(0,'/tmp/ig')
exec(open('/tmp/pin/make_pins2.py').read().split('PINS=[')[0])
PINS=[
 ('13-ou-partir-2027','mont-saint-michel',.5,'IDÉES · 2027','Où partir\nen France en 2027 ?','Une destination\npour chaque mois','Photo : Andrej A / Unsplash'),
 ('14-bordeaux','bordeaux',.5,'NOUVELLE-AQUITAINE','Bordeaux\nen 1 jour','Place de la Bourse, miroir d’eau\net quais de la Garonne','Photo : Maxime Kirschner / Unsplash'),
 ('15-marseille','marseille',.5,'PROVENCE','Marseille :\nles incontournables','Notre-Dame de la Garde,\nVieux-Port et MuCEM','Photo : Kamilla Isalieva / Unsplash'),
 ('16-monaco','monaco',.5,'CÔTE D’AZUR','Monaco\nen une journée','Le Rocher, Monte-Carlo\net le port Hercule','Photo : Victor He / Unsplash'),
 ('17-eguisheim','eguisheim',.5,'ALSACE · ROUTE DES VINS','Eguisheim,\nle village en cercles','Ruelles fleuries\nprès de Colmar','Photo : Pug Girl / Wikimedia Commons, CC BY 2.0'),
]
exec('for slug'+open('/tmp/pin/make_pins2.py').read().split('for slug',1)[1])
