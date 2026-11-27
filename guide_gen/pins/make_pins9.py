import sys; sys.path.insert(0,'/tmp/ig')
exec(open('/tmp/pin/make_pins2.py').read().split('PINS=[')[0])
PINS=[('32-janvier-2027','alpe-d-huez',.5,'JANVIER 2027','Où partir\nen janvier ?','Ski hors vacances, Rallye\nMonte-Carlo, cirque de Monaco','Photo : yelr / Unsplash'),
('33-disneyland-paris','disneyland-paris',.5,'MARNE-LA-VALLÉE','Disneyland Paris','Billets, accès en RER\net Noël Enchanté','Photo : Thomas Evraert / Unsplash')]
exec('for slug'+open('/tmp/pin/make_pins2.py').read().split('for slug',1)[1])
