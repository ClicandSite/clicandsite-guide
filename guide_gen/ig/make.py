from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

PH = '/home/claude/clicandsite-guide/assets/photos/'
F = '/tmp/ig/fonts/'
OUT = '/tmp/ig/out/'
os.makedirs(OUT, exist_ok=True)
ENCRE = (19, 50, 75); OCRE = (224, 162, 67); BLANC = (255, 255, 255)
NB = ' '

def font(n, s): return ImageFont.truetype(F + n + '.ttf', s)
SERIF = 'young-serif-latin-400-normal'; SANS = 'public-sans-latin-400-normal'
SANS6 = 'public-sans-latin-600-normal'; SANS7 = 'public-sans-latin-700-normal'

POSTS = [
    dict(slug='01-tignes-val-thorens', photo='tignes', focus=0.5, credit='Valentin de Brabandère / Unsplash',
         kicker='OUVERTURE · 21 NOV. 2026', title='La saison de ski\ncommence ce samedi',
         sub=f'Tignes et Val Thorens ouvrent{NB}les premiers, le 21 novembre.',
         story=['Tignes · 21 novembre', 'Val Thorens · 21 novembre', 'Val d’Isère · 28 novembre'],
         story_title='Les stations\nqui ouvrent en premier'),
    dict(slug='02-champs-elysees', photo='noel-a-paris', focus=0.5, credit='Pierre Blaché / Unsplash',
         kicker='PARIS · 22 NOV. 2026', title='Les Champs-Élysées\ns’illuminent',
         sub='Lancement des illuminations le dimanche 22 novembre, avenue piétonne.',
         story=['Dimanche 22 novembre', 'Avenue entièrement piétonne', 'Gratuit, en plein air'],
         story_title='Noël à Paris\ncommence ici'),
    dict(slug='03-strasbourg', photo='strasbourg', focus=0.5, credit='Alexis Brandner / Unsplash',
         kicker='ALSACE · DÈS LE 27 NOV.', title='Le plus ancien\nmarché de Noël',
         sub='Le Christkindelsmärik de Strasbourg existe depuis 1570.',
         story=['Du 27 novembre au 24 décembre', 'De 11 h 30 à 21 h environ', 'Entrée libre'],
         story_title='Strasbourg,\ncapitale de Noël'),
    dict(slug='04-ski-pres-de-nice', photo='auron', focus=0.55, credit='Tom Coomer / Unsplash',
         kicker='CÔTE D’AZUR · DÉCEMBRE', title='Skier à 1 h 30\nde Nice',
         sub='Isola 2000 ouvre le 3 décembre, Auron le 5 décembre.',
         story=['Isola 2000 · dès le 3 décembre', 'Auron · dès le 5 décembre', 'Forfait journée adulte : 44 €'],
         story_title='La neige,\nà côté de la mer'),
    dict(slug='05-eze', photo='eze', focus=0.45, credit='Anatoly Volochay / Unsplash',
         kicker='CÔTE D’AZUR', title='Èze, le village\nsuspendu',
         sub='Entre Nice et Monaco, à plus de 400 mètres au-dessus de la mer.',
         story=['Ruelles médiévales', 'Jardin exotique : 10 €', 'Venez tôt le matin'],
         story_title='Èze, la vue\nla plus folle'),
    dict(slug='06-fete-du-citron', photo='fete-du-citron', focus=0.45, credit='Anatoli Nicolae / Unsplash',
         kicker='MENTON · 13-28 FÉV. 2027', title='La Fête du Citron\nrevient',
         sub='93e édition sur le thème « Douce France ».',
         story=['Du 13 au 28 février 2027', 'Corsos le dimanche après-midi', 'Corsos de nuit les 18 et 25 février'],
         story_title='Des chars\nen citrons'),
]

def cover(im, W, H, focus=0.5):
    r = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    x = (im.width - W) * focus if im.width > W else 0
    y = (im.height - H) / 2
    return im.crop((int(x), int(y), int(x) + W, int(y) + H))

def gradient(W, H, start, alpha_top=0, alpha_bot=235):
    g = Image.new('L', (1, H), 0)
    for y in range(H):
        t = max(0, (y - start) / (H - start)) if y > start else 0
        g.putpixel((0, y), int(alpha_top + (alpha_bot - alpha_top) * (t ** 0.75)))
    g = g.resize((W, H))
    layer = Image.new('RGBA', (W, H), ENCRE + (0,)); layer.putalpha(g)
    return layer

def top_shade(W, H, h=260, a=150):
    g = Image.new('L', (1, H), 0)
    for y in range(h): g.putpixel((0, y), int(a * (1 - y / h)))
    g = g.resize((W, H)); layer = Image.new('RGBA', (W, H), ENCRE + (0,)); layer.putalpha(g); return layer

def brand(d, x, y, size):
    f = font(SERIF, size)
    d.text((x, y), 'Clic', font=f, fill=BLANC)
    w = d.textlength('Clic', font=f)
    d.text((x + w, y), '&', font=f, fill=OCRE)
    w2 = d.textlength('&', font=f)
    d.text((x + w + w2, y), 'Site', font=f, fill=BLANC)

def pill(d, x, y, text, size):
    f = font(SANS7, size)
    w = d.textlength(text, font=f)
    pad = size * 0.7
    d.rounded_rectangle((x, y, x + w + 2 * pad, y + size * 2), radius=size, fill=OCRE)
    d.text((x + pad, y + size * 0.42), text, font=f, fill=ENCRE)
    return y + size * 2

def wrap(d, text, f, maxw):
    out = []
    for para in text.split('\n'):
        line = ''
        for wd in para.split(' '):
            t = (line + ' ' + wd).strip()
            if d.textlength(t, font=f) <= maxw: line = t
            else: out.append(line); line = wd
        out.append(line)
    return out

def post(p):
    W, H = 1080, 1350
    im = cover(Image.open(PH + p['photo'] + '.jpg').convert('RGB'), W, H, p['focus'])
    im = Image.alpha_composite(im.convert('RGBA'), gradient(W, H, int(H * 0.30), 0, 245))
    im = Image.alpha_composite(im, top_shade(W, H, 220, 120))
    d = ImageDraw.Draw(im)
    M = 80
    brand(d, M, 60, 46)
    ft = font(SERIF, 96); fs = font(SANS, 38)
    title = wrap(d, p['title'], ft, W - 2 * M)
    sub = wrap(d, p['sub'], fs, W - 2 * M)
    y = H - 110 - len(sub) * 52 - 36 - len(title) * 108 - 30 - 64
    y = pill(d, M, y, p['kicker'], 30) + 34
    for l in title: d.text((M, y), l, font=ft, fill=BLANC); y += 108
    y += 18
    for l in sub: d.text((M, y), l, font=fs, fill=(225, 233, 240)); y += 52
    d.text((M, H - 74), 'clicandsite.fr', font=font(SANS6, 30), fill=OCRE)
    fc = font(SANS, 20); c = 'Photo : ' + p['credit']
    d.text((W - M - d.textlength(c, font=fc), H - 68), c, font=fc, fill=(200, 210, 220))
    im.convert('RGB').save(OUT + p['slug'] + '-post.jpg', quality=92)

def story(p):
    W, H = 1080, 1920
    im = cover(Image.open(PH + p['photo'] + '.jpg').convert('RGB'), W, H, p['focus'])
    im = Image.alpha_composite(im.convert('RGBA'), gradient(W, H, int(H * 0.22), 0, 250))
    im = Image.alpha_composite(im, top_shade(W, H, 380, 150))
    d = ImageDraw.Draw(im)
    M = 90
    brand(d, M, 230, 52)
    ft = font(SERIF, 104); fi = font(SANS6, 44)
    title = wrap(d, p['story_title'], ft, W - 2 * M)
    # bloc infos
    items = p['story']
    y = 1960 - 420 - len(items) * 92 - 50 - len(title) * 118 - 40 - 64
    y = pill(d, M, y, p['kicker'], 32) + 40
    for l in title: d.text((M, y), l, font=ft, fill=BLANC); y += 118
    y += 40
    for it in items:
        d.ellipse((M, y + 18, M + 16, y + 34), fill=OCRE)
        d.text((M + 40, y), it, font=fi, fill=BLANC); y += 92
    # zone du sticker lien
    y += 30
    f = font(SANS7, 38); t = 'Le guide complet sur clicandsite.fr'
    w = d.textlength(t, font=f)
    d.rounded_rectangle((M, y, M + w + 70, y + 92), radius=46, fill=BLANC)
    d.text((M + 35, y + 24), t, font=f, fill=ENCRE)
    fc = font(SANS, 22); c = 'Photo : ' + p['credit']
    d.text((W - M - d.textlength(c, font=fc), H - 200), c, font=fc, fill=(200, 210, 220))
    im.convert('RGB').save(OUT + p['slug'] + '-story.jpg', quality=92)

for p in POSTS:
    post(p); story(p)
print('ok')
