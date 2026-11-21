import sys; sys.path.insert(0,'/tmp/ig')
exec(open('/tmp/pin/make_pins2.py').read().split('PINS=[')[0])
PINS=[('30-vacances-noel','megeve',.55,'19 DÉC. 2026 - 4 JANV. 2027','Vacances de Noël\nen France','Ski, marchés de Noël\net réveillon : nos idées','Photo : Mat Napo / Unsplash')]
exec('for slug'+open('/tmp/pin/make_pins2.py').read().split('for slug',1)[1])
