import sys; sys.path.insert(0,'/tmp/ig')
exec(open('/tmp/pin/make_pins2.py').read().split('PINS=[')[0])
PINS=[('31-paris-noel-jour-de-l-an','notre-dame',.5,'25 DÉCEMBRE ET 1ER JANVIER','Paris à Noël\net au Nouvel An','Ce qui est ouvert :\nmusées, monuments, balades','Photo : Maxime Gilbert / Unsplash')]
exec('for slug'+open('/tmp/pin/make_pins2.py').read().split('for slug',1)[1])
