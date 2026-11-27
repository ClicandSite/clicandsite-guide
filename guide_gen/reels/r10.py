import sys; sys.path.insert(0,'/tmp/reel'); from reel import render
S=[
 dict(photo='megeve',focus=0.55,credit='Mat Napo / Unsplash',kicker='19 DÉC. 2026 - 4 JANV. 2027',title='Vacances de Noël : où partir ?',sub='4 idées pour les deux semaines de fêtes.'),
 dict(photo='val-thorens',credit='Joan Oger / Unsplash',kicker='1 · LE SKI',title='Megève ouvre le 19\u00a0décembre',sub='Val Thorens, Tignes et Courchevel tournent déjà.',out=1),
 dict(photo='strasbourg',credit='Alexis Brandner / Unsplash',kicker='2 · LES MARCHÉS DE NOËL',title='Strasbourg : jusqu’au 24 déc.',sub='Colmar jusqu’au 29. Paris, Nice, Cannes et Monaco jusqu’au 3 ou 4 janvier.'),
 dict(photo='champs-elysees',credit='Stephanie LeBlanc / Unsplash',kicker='3 · LE RÉVEILLON',title='Feu d’artifice sur\nles Champs-Élysées',sub='Gratuit, à minuit, le jeudi 31 décembre.',out=1),
 dict(photo='noel-riviera',credit='Gytis Bukauskas / Unsplash',kicker='4 · LE SOLEIL',title='La Côte d’Azur\nsans la foule',sub='Villages perchés et villages de Noël, faciles à relier en train.'),
 dict(photo='noel-a-paris',credit='Pierre Blaché / Unsplash',kicker='LE GUIDE COMPLET',title='Toutes les dates\net nos idées',sub='Lien en bio · clicandsite.fr',end=1,out=1),
]
render(S,'/tmp/ig/out/10-vacances-noel-2026-reel.mp4')
