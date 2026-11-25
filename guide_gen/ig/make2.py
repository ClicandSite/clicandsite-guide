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

NB='\u00a0'
POSTS = [
    dict(slug='10-vacances-noel-2026', photo='megeve', focus=0.55, credit='Mat Napo / Unsplash',
         kicker='19 DÉC. 2026 - 4 JANV. 2027', title='Vacances de Noël :\noù partir ?',
         sub='Ski, marchés de Noël encore ouverts, réveillon ou soleil sur la Côte d’Azur.'),
    dict(slug='11-paris-25-decembre', photo='notre-dame', focus=0.5, credit='Maxime Gilbert / Unsplash',
         kicker='PARIS · 25 DÉC. ET 1ER JANV.', title='Qu’est-ce qui est\nouvert à Paris ?',
         sub='Tour Eiffel, Notre-Dame, Sacré-Cœur : ouverts. Orsay rouvre le 1er janvier.'),
    dict(slug='12-carnaval-nice-2027', photo='carnaval-nice', focus=0.5, credit='Pierre Goiffon / Unsplash',
         kicker='NICE · 9-28 FÉV. 2027', title='Carnaval de Nice :\n« Vive l’Amour »',
         sub='Batailles de fleurs et corsos illuminés place Masséna.'),
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
    post(p)
