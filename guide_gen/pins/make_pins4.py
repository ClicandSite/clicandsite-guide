import sys; sys.path.insert(0,'/tmp/ig')
exec(open('/tmp/pin/make_pins2.py').read().split('PINS=[')[0])
PINS=[
 ('18-strasbourg-noel','strasbourg',.5,'ALSACE · DÈS LE 27 NOV. 2026','Marché de Noël\nde Strasbourg','Dates, horaires et\nplus beaux chalets','Photo : Alexis Brandner / Unsplash'),
 ('19-colmar-noel','colmar',.5,'ALSACE · 23 NOV.-29 DÉC. 2026','Marchés de Noël\nde Colmar','Canaux, colombages\net illuminations','Photo : Sascha Sturm / Unsplash'),
 ('20-riquewihr-noel','riquewihr',.5,'ALSACE · 27 NOV.-20 DÉC. 2026','Noël\nà Riquewihr','Le marché de Noël\nd’un village de conte','Photo : Thomas Bormans / Unsplash'),
 ('21-chamonix','chamonix',.5,'ALPES · HIVER 2026-2027','Chamonix\nface au mont Blanc','Ski, forfaits\net Aiguille du Midi','Photo : Chris Biron / Unsplash'),
 ('22-courchevel','courchevel',.5,'ALPES · 3 VALLÉES','Courchevel\n2026-2027','Forfaits, ouverture\net villages','Photo : Piotr Figlarz / Unsplash'),
 ('23-tour-eiffel','tour-eiffel',.5,'PARIS','Visiter\nla tour Eiffel','Billets, sommet\net nos conseils','Photo : Anthony Delanoix / Unsplash'),
 ('24-mont-saint-michel','mont-saint-michel',.5,'NORMANDIE','Le Mont-\nSaint-Michel','Abbaye, marées,\nhoraires et prix','Photo : Andrej A / Unsplash'),
 ('25-nice','nice',.5,'CÔTE D’AZUR','Nice :\nque voir ?','Vieux-Nice, promenade\ndes Anglais et musées','Photo : Constantin / Unsplash'),
 ('26-cannes','cannes',.5,'CÔTE D’AZUR','Visiter\nCannes','La Croisette, le Suquet\net les îles de Lérins','Photo : Jannis Lucas / Unsplash'),
 ('27-versailles','versailles',.5,'DEPUIS PARIS','Versailles\nen une journée','Galerie des Glaces,\njardins et réservation','Photo : Mathias Reding / Unsplash'),
]
exec('for slug'+open('/tmp/pin/make_pins2.py').read().split('for slug',1)[1])
