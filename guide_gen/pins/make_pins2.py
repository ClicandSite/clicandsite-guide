import sys; sys.path.insert(0,'/tmp/ig')
from make import font, SERIF, SANS, SANS6, SANS7, ENCRE, OCRE, BLANC, cover, gradient, top_shade, brand
from PIL import Image, ImageDraw
PH='/home/claude/clicandsite-guide/assets/photos/'
W,H=1000,1500
PINS=[
 ('07-carnaval-de-nice','carnaval-nice',.5,'NICE · 9-28 FÉV. 2027','Carnaval\nde Nice 2027','Batailles de fleurs et corsos\nilluminés place Masséna','Photo : Pierre Goiffon / Unsplash'),
 ('08-fete-du-citron','fete-du-citron',.45,'MENTON · 13-28 FÉV. 2027','Fête du Citron\n2027 à Menton','Corsos, nocturnes\net Jardins de lumière','Photo : Anatoli Nicolae / Unsplash'),
 ('09-noel-a-paris','noel-a-paris',.5,'PARIS · NOËL 2026','Noël à Paris','Illuminations, marchés de Noël,\npatinoires et vitrines','Photo : Pierre Blaché / Unsplash'),
 ('10-stations-ski-ouvertes','val-thorens',.5,'SKI · 2026-2027','Stations de ski\nouvertes','Le calendrier d’ouverture\ndes grandes stations','Photo : Joan Oger / Unsplash'),
 ('11-eze','eze',.45,'CÔTE D’AZUR','Visiter Èze,\nle village perché','Entre Nice et Monaco :\nruelles, jardin et vue','Photo : Anatoly Volochay / Unsplash'),
 ('12-cote-d-azur-hiver','menton',.5,'CÔTE D’AZUR · HIVER','La Côte d’Azur\nen hiver','Carnaval, citrons, mimosa\net sorties au soleil','Photo : Slim Mars / Unsplash'),
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
