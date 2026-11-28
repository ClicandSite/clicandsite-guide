import sys; sys.path.insert(0,'/tmp/reel'); from reel import render
N=' '
S=[
 dict(photo='pyrenees',credit='Oihan Brière / Unsplash',kicker='SAISON 2026-2027',title='Skier dans\nles Pyrénées',sub=f'Cauterets ouvre dès le 27{N}novembre. Des forfaits souvent moins chers que dans les Alpes.'),
 dict(photo='font-romeu',credit='Quentin Rey / Unsplash',kicker='LE SOLEIL',title='Font-Romeu',sub=f'Ouverture le 4{N}décembre. Accès en train jaune, forfait 49,50{N}€.'),
 dict(photo='saint-lary',credit='Marek Piwnicki / Unsplash',kicker='LE VILLAGE',title='Saint-Lary',sub=f'100{N}km de pistes au-dessus d’un vrai village. Dès le 4{N}décembre.',out=1),
 dict(photo='grand-tourmalet',credit='mathieu gauzy / Unsplash',kicker='LE PLUS GRAND',title='Grand Tourmalet',sub=f'La Mongie, Barèges et le Pic du Midi. Dès le 5{N}décembre.'),
 dict(photo='peyragudes',credit='Erwan Hesry / Unsplash',kicker='LE GUIDE COMPLET',title='Dates, forfaits\net accès',sub=f'Peyragudes ouvre le 12{N}décembre. Lien en bio · clicandsite.fr',end=1,out=1),
]
render(S,'/tmp/ig/out/13-pyrenees-ski-reel.mp4')
