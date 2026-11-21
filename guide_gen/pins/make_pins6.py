import sys; sys.path.insert(0,'/tmp/ig')
exec(open('/tmp/pin/make_pins2.py').read().split('PINS=[')[0])
PINS=[('29-marches-noel-france','noel-a-paris',.5,'NOV. 2026 - JANV. 2027','Marchés de Noël\nen France','Alsace, Paris, Côte d’Azur :\nles dates 2026','Photo : Pierre Blaché / Unsplash')]
exec('for slug'+open('/tmp/pin/make_pins2.py').read().split('for slug',1)[1])
