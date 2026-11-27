import sys, subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFont
PH='/home/claude/clicandsite-guide/assets/photos/'; F='/tmp/ig/fonts/'
ENCRE=(19,50,75); OCRE=(224,162,67); BLANC=(255,255,255)
W,H,FPS=1080,1920,30
def font(n,s): return ImageFont.truetype(F+n+'.ttf',s)
SERIF='young-serif-latin-400-normal'; SANS='public-sans-latin-400-normal'; SANS7='public-sans-latin-700-normal'
def wrap(d,text,f,maxw):
    out=[]
    for para in text.split('\n'):
        line=''
        for w in para.split(' '):
            t=(line+' '+w).strip()
            if d.textlength(t,font=f)<=maxw: line=t
            else: out.append(line); line=w
        out.append(line)
    return out
def overlay(s):
    L=Image.new('RGBA',(W,H),(0,0,0,0))
    # shades
    a=np.zeros((H,),np.float32)
    for y in range(H):
        if y<300: a[y]=150*(1-y/300)
        if y>H*0.45: a[y]=max(a[y],235*((y-H*0.45)/(H*0.55))**0.8)
    g=Image.fromarray(np.repeat(a.astype(np.uint8)[:,None],W,1),'L')
    sh=Image.new('RGBA',(W,H),ENCRE+(0,)); sh.putalpha(g); L=Image.alpha_composite(L,sh)
    d=ImageDraw.Draw(L)
    f=font(SERIF,56); x,y=70,90
    for t,c in (('Clic',BLANC),('&',OCRE),('Site',BLANC)):
        d.text((x,y),t,font=f,fill=c); x+=d.textlength(t,font=f)
    y=1180 if not s.get('end') else 820
    fk=font(SANS7,38); w=d.textlength(s['kicker'],font=fk)
    d.rounded_rectangle((70,y,70+w+56,y+76),radius=38,fill=OCRE); d.text((98,y+16),s['kicker'],font=fk,fill=ENCRE)
    y+=120; ft=font(SERIF,92)
    for ln in wrap(d,s['title'],ft,W-140): d.text((70,y),ln,font=ft,fill=BLANC); y+=112
    y+=20; fs=font(SANS,46)
    for ln in wrap(d,s['sub'],fs,W-140): d.text((70,y),ln,font=fs,fill=BLANC); y+=62
    fc=font(SANS,26); d.text((70,H-90),'Photo : '+s['credit'],font=fc,fill=(255,255,255,190))
    return L
def base(name,focus):
    im=Image.open(PH+name+'.jpg').convert('RGB')
    S=1.15; Wb,Hb=int(W*S),int(H*S)
    r=max(Wb/im.width,Hb/im.height); im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS)
    x=int((im.width-Wb)*focus); y=(im.height-Hb)//2
    return im.crop((x,y,x+Wb,y+Hb))
def frames(s,n):
    b=base(s['photo'],s.get('focus',0.5)); ov=overlay(s)
    if s.get('end'):
        dk=Image.new('RGB',b.size,ENCRE); b=Image.blend(b,dk,0.45)
    for i in range(n):
        t=i/(n-1); z=1.15-0.15*t if s.get('out') else 1.0+0.15*t
        cw,ch=int(b.width/z*1.0/1.15*1.15/1.15*1.15) ,0
        cw=int(W*1.15/z); ch=int(H*1.15/z)
        cx=(b.width-cw)//2; cy=(b.height-ch)//2
        fr=b.crop((cx,cy,cx+cw,cy+ch)).resize((W,H),Image.BILINEAR).convert('RGBA')
        yield np.asarray(Image.alpha_composite(fr,ov).convert('RGB'))
def render(slides,out,dur=2.6,xf=0.4):
    n=int(dur*FPS); nx=int(xf*FPS)
    p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
        '-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-shortest',
        '-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-movflags','+faststart','-c:a','aac',out],stdin=subprocess.PIPE)
    prev=None
    for k,s in enumerate(slides):
        fl=list(frames(s,n+(nx if k<len(slides)-1 else 0)))
        start=0
        if prev is not None:
            for j in range(nx):
                a=(j+1)/(nx+1); p.stdin.write((prev[j]*(1-a)+fl[j]*a).astype(np.uint8).tobytes())
            start=nx
        last=len(fl)-(nx if k<len(slides)-1 else 0)
        for fr in fl[start:last]: p.stdin.write(fr.tobytes())
        prev=fl[last:]
    p.stdin.close(); p.wait()
