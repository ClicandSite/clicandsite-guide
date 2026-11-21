import sys; sys.path.insert(0,'/tmp/ig')
from make import font, SERIF, SANS, SANS6, SANS7, ENCRE, OCRE, BLANC, cover, gradient, top_shade, brand
from PIL import Image, ImageDraw
PH='/home/claude/clicandsite-guide/assets/photos/'
W,H=1000,1500
PINS=[
 ('01-prix-forfaits-ski','courchevel',.5,'SKI · SAISON 2026-2027','Prix des forfaits\nde ski 2026-2027','De 44 € à 84,20 € la journée :\n24 stations comparées','Photo : Piotr Figlarz / Unsplash'),
 ('02-marches-noel-alsace','strasbourg',.5,'ALSACE · DÈS LE 23 NOV.','Marchés de Noël\nen Alsace 2026','Strasbourg, Colmar, Riquewihr,\nKaysersberg : dates et itinéraire','Photo : Alexis Brandner / Unsplash'),
 ('03-reveillon-nouvel-an','champs-elysees',.5,'31 DÉCEMBRE 2026','Où fêter\nle Nouvel An ?','Feu d’artifice des Champs-Élysées,\nParis et Côte d’Azur','Photo : Stephanie LeBlanc / Unsplash'),
 ('04-vacances-fevrier-2027','les-arcs',.5,'ZONES A, B ET C','Vacances de\nfévrier 2027','Les dates par zone\net où partir','Photo : Tomas Yates / Unsplash'),
 ('05-rallye-monte-carlo','monaco',.5,'MONACO · 21-24 JANV. 2027','Rallye\nMonte-Carlo 2027','Dates, parcours\net où voir les voitures','Photo : Victor He / Unsplash'),
 ('06-route-du-mimosa','mandelieu-la-napoule',.5,'CÔTE D’AZUR · FÉVRIER 2027','La Route\ndu Mimosa','130 km de Bormes à Grasse\net la Fête du Mimosa','Photo : Yves Tennevin / Wikimedia Commons, CC BY 4.0'),
]
for slug,ph,fo,kick,title,sub,cred in PINS:
    im=cover(Image.open(PH+ph+'.jpg').convert('RGB'),W,H,fo).convert('RGBA')
    im=Image.alpha_composite(im,gradient(W,H,int(H*.30),0,250)); im=Image.alpha_composite(im,gradient(W,H,int(H*.50),0,170))
    im=Image.alpha_composite(im,top_shade(W,H,300,170))
    d=ImageDraw.Draw(im)
    brand(d,60,58,54)
    fk=font(SANS7,30); tw=d.textlength(kick,font=fk)
    d.rounded_rectangle((60,860,60+tw+44,860+58),radius=29,fill=OCRE)
    d.text((82,872),kick,font=fk,fill=ENCRE)
    ft=font(SERIF,92); y=950
    for line in title.split('\n'):
        d.text((60,y),line,font=ft,fill=BLANC); y+=106
    fs=font(SANS6,40); y+=20
    for line in sub.split('\n'):
        d.text((60,y),line,font=fs,fill=BLANC); y+=52
    d.text((60,H-70),'clicandsite.fr',font=font(SANS7,34),fill=OCRE)
    fc=font(SANS,20); cw=d.textlength(cred,font=fc)
    d.text((W-60-cw,H-60),cred,font=fc,fill=(255,255,255,190))
    im.convert('RGB').save(f'/tmp/pin/out/{slug}.jpg',quality=90)
print('ok')
