import sys; sys.path.insert(0,'/tmp/ig')
exec(open('/tmp/pin/make_pins2.py').read().split('PINS=[')[0])
PINS=[('28-saint-valentin','croisiere-sur-la-seine',.5,'DIMANCHE 14 FÉVRIER 2027','Saint-Valentin\nen amoureux','Paris, Èze, Colmar :\nnos idées de week-end','Photo : Bastien Nvs / Unsplash')]
exec('for slug'+open('/tmp/pin/make_pins2.py').read().split('for slug',1)[1])
