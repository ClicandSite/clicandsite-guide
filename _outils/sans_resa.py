"""Pages où ni GetYourGuide ni Viator n'ont rien de propre au lieu (« vraiment rien ») :
on retire les blocs de réservation. Pages où seul Viator a quelque chose : les liens GYG pointent vers Viator.
Usage : python3 _outils/sans_resa.py ../clicandsite-guide ../clicandsite-guide-en"""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from gyg_tours import GT
from viator_picks import P, G, PG, RG, A, PA
PID = 'pid=P00331213&amp;mcid=42383&amp;medium=link&amp;campaign='
def viator_target(fr):
    reg, slug = fr.split('/')
    g = G if reg == 'cote-d-azur' else PG if reg == 'paris' else RG
    a = A if reg == 'cote-d-azur' else PA if reg == 'paris' else {}
    if g.get(slug): return 'tours', P[g[slug][0]][0]
    if a.get(slug): return 'attr', a[slug]
    return None, None
def run(root, lang):
    pre = 'fr-FR/' if lang == 'fr' else ''
    n = {'rien': 0, 'viator': 0}
    for dp, dn, fn in os.walk(root):
        if '/.git' in dp or 'index.html' not in fn: continue
        p = os.path.join(dp, 'index.html'); s = open(p, encoding='utf-8').read()
        rel = os.path.relpath(dp, root).replace(os.sep, '/'); fr = rel
        if lang == 'en':
            h = re.search(r'hreflang="fr" href="https://clicandsite\.fr/([^"]*?)/?"', s)
            if not h: continue
            fr = h.group(1)
        if GT.get(fr) != '-': continue
        kind, path = viator_target(fr)
        o = s
        if kind:
            url = f'https://www.viator.com/{pre}{path}?{PID}clicandsite-{lang}-{rel.replace("/", "-")}'
            def fix(m):
                a = re.sub(r'href="https://www\.getyourguide\.[a-z]+/[^"]*"', f'href="{url}"', m.group(0))
                return a.replace('bk--gyg', 'bk--via')
            s = re.sub(r'<a[^>]*getyourguide\.[a-z]+/[^>]*>', fix, s)
            n['viator'] += 1
        else:
            s = re.sub(r'\s*<aside class="cta-box">.*?</aside>', '', s, flags=re.S)
            s = re.sub(r'\s*<p class="post__cta">.*?</p>', '', s, flags=re.S)
            s = re.sub(r'\s*<section class="book" id="reserver".*?</section>', '', s, flags=re.S)
            s = re.sub(r'\s*<div class="cta-bar" id="cta-bar".*?</div>', '', s, flags=re.S)
            s = re.sub(r'<p>\s*<a class="deep"[^>]*>.*?</a>\s*</p>', '', s, flags=re.S)
            s = re.sub(r'\s*<a class="deep"[^>]*>.*?</a>', '', s, flags=re.S)
            n['rien'] += 1
        left = re.findall(r'href="(https://www\.(?:getyourguide|viator)[^"]*)"', s)
        if left and not kind: print('reste', p, left[:2])
        if s != o: open(p, 'w', encoding='utf-8').write(s)
    print(lang, n)
for r, l in zip(sys.argv[1::1][:2], ('fr', 'en')): run(r, l)
