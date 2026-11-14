"""Optimise les photos : versions WebP + taille 1280, et balises <picture> dans les pages. Idempotent."""
import os,re,glob,sys
from PIL import Image
for root in ('/home/claude/clicandsite-guide','/home/claude/clicandsite-guide-en'):
    ph=f'{root}/assets/photos'
    made=0
    for f in glob.glob(ph+'/*.jpg'):
        b=os.path.basename(f)
        if b.startswith('og-'): continue
        base=f[:-4]
        if not re.search(r'-(640|960|1280)$',base):
            j=base+'-1280.jpg'
            if not os.path.exists(j) or os.path.getmtime(j)<os.path.getmtime(f):
                im=Image.open(f).convert('RGB'); im=im.resize((1280,round(im.height*1280/im.width)),Image.LANCZOS)
                im.save(j,quality=80,optimize=True,progressive=True); made+=1
        for src in (f,):
            w=src[:-4]+'.webp'
            if not os.path.exists(w) or os.path.getmtime(w)<os.path.getmtime(src):
                Image.open(src).convert('RGB').save(w,'WEBP',quality=76,method=6); made+=1
    for f in glob.glob(ph+'/*-1280.jpg'):
        w=f[:-4]+'.webp'
        if not os.path.exists(w) or os.path.getmtime(w)<os.path.getmtime(f):
            Image.open(f).convert('RGB').save(w,'WEBP',quality=76,method=6); made+=1
    pages=0
    hero=re.compile(r'(?<!</source>)(?<!">)<img class="post__img" src="([^"]*?assets/photos/[^"/]+?)\.jpg" srcset="[^"]*" sizes="100vw"([^>]*)>')
    small=re.compile(r'<img ([^>]*?)src="([^"]*?assets/photos/[^"/]+?-(?:640|960))\.jpg"([^>]*)>')
    for p in glob.glob(root+'/**/*.html',recursive=True):
        t=open(p).read(); u=t
        def H(m):
            P=m.group(1)
            if not os.path.exists(os.path.join(os.path.dirname(p),P+'-1280.webp')): return m.group(0)
            return (f'<picture><source type="image/webp" srcset="{P}-960.webp 960w, {P}-1280.webp 1280w, {P}.webp 1920w" sizes="100vw">'
                    f'<img class="post__img" src="{P}.jpg" srcset="{P}-960.jpg 960w, {P}-1280.jpg 1280w, {P}.jpg 1920w" sizes="100vw"{m.group(2)}></picture>')
        u=hero.sub(H,u)
        out=[];last=0
        for m in small.finditer(u):
            pre=u[max(0,m.start()-200):m.start()]
            if pre.endswith('.webp">'): continue
            P=m.group(2)
            if not os.path.exists(os.path.join(os.path.dirname(p),P+'.webp')): continue
            out.append(u[last:m.start()]+f'<picture><source type="image/webp" srcset="{P}.webp">{m.group(0)}</picture>'); last=m.end()
        u=''.join(out)+u[last:]
        if u!=t: open(p,'w').write(u); pages+=1
    print(root,'fichiers',made,'pages',pages)
