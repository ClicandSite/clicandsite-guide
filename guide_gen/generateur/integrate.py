import re, json, sys
sys.path.insert(0, '/tmp/g')
from randos_data import H
R = {'fr': ('/home/claude/clicandsite-guide', 'cote-d-azur', 'https://clicandsite.fr', 'mentions-legales'),
     'en': ('/home/claude/clicandsite-guide-en', 'french-riviera', 'https://clicandsite.com', 'legal-notice')}
SEC = {'fr': 'Randonnées et sentiers du littoral', 'en': 'Hikes and coastal paths'}
def esc(t): return t.replace('&', '&amp;')
def typo(t, lang):
    if lang != 'fr': return t
    t = re.sub(r' ([:;?!»])', '\u202f\\1', t)
    return re.sub(r'(\d) (h|km|m|min)\b', '\\1\u00a0\\2', t)
for lang, (root, reg, base, legal) in R.items():
    p = f'{root}/{reg}/index.html'; s = open(p, encoding='utf-8').read()
    # remove mont-gros card from g-nice
    m = re.search(r'</li><li class="card card--pin">\n  <a href="\.\./' + reg + r'/mont-gros/">.*?</li>', s, re.S)
    if m:
        mg = m.group(0)[len('</li>'):]
        s = s.replace(m.group(0), '</li>', 1)
    else:
        mg = re.search(r'<li class="card card--pin">\n  <a href="\.\./' + reg + r'/mont-gros/">.*?</li>', s, re.S).group(0)
    if 'id="g-rando"' not in s:
        tpl = mg
        cards = [mg]
        for h in H:
            d = h[lang]; c = tpl.replace('/mont-gros', '/' + h['slug'])
            c = re.sub(r'<span>[^<]*</span></div><span class="card__name">[^<]*</span>', f'<span>{esc(h["pm"])}</span></div><span class="card__name">{esc(typo(d["crumb"], lang))}</span>', c)
            c = re.sub(r'<p class="card__txt">.*?</p>', f'<p class="card__txt">{esc(typo(d["card"], lang))}</p>', c)
            cards.append(c)
        sec = f'<section class="wrap" aria-labelledby="g-rando"><h2 id="g-rando" class="sec-title">{SEC[lang]}</h2><ul class="cards">' + ''.join(cards) + '</ul></section>'
        i = s.index('<section class="wrap" aria-labelledby="g-fetes">')
        s = s[:i] + sec + s[i:]
    # ld includesAttraction
    for h in H:
        url = f'{base}/{reg}/{h["slug"]}/'
        if url not in s:
            s = s.replace(']}</script>', ', ' + json.dumps({"@type": "TouristAttraction", "name": typo(h[lang]['name'], lang), "url": url}, ensure_ascii=False) + ']}</script>', 1) if '"includesAttraction"' in s else s
    open(p, 'w', encoding='utf-8').write(s)
    # sitemap
    sp = f'{root}/sitemap.xml'; sm = open(sp, encoding='utf-8').read()
    add = ''.join(f'  <url><loc>{base}/{reg}/{h["slug"]}/</loc><lastmod>2026-11-15</lastmod></url>\n' for h in H if f'/{h["slug"]}/' not in sm)
    sm = sm.replace('</urlset>', add + '</urlset>'); open(sp, 'w', encoding='utf-8').write(sm)
    # home counts
    hp = f'{root}/index.html'; hs = open(hp, encoding='utf-8').read()
    n = 56 + len(H)
    hs = hs.replace('<span class="region-card__count">56 guides</span>', f'<span class="region-card__count">{n} guides</span>', 1)
    hs = hs.replace('Voir les 56 guides de la Côte d’Azur', f'Voir les {n} guides de la Côte d’Azur').replace('See all 56 French Riviera guides', f'See all {n} French Riviera guides')
    open(hp, 'w', encoding='utf-8').write(hs)
    # credits
    lp = f'{root}/{legal}/index.html'; ls = open(lp, encoding='utf-8').read()
    anchor = re.search(r'<li>Mont Gros \(Nice\).*?</li>', ls).group(0)
    items = ''
    for h in H:
        a, u, l, lu = h['credit']; nm = h[lang]['crumb']
        sep = ' : ' if lang == 'fr' else ': '
        if l == 'Domaine public':
            items += f'<li>{esc(nm)}{sep}<a href="{u}" rel="noopener" target="_blank">{esc(a)}</a>, {"domaine public" if lang == "fr" else "public domain"}, Wikimedia Commons</li>'
        else:
            items += f'<li>{esc(nm)}{sep}<a href="{u}" rel="noopener" target="_blank">{esc(a)}</a>, <a href="{lu}" rel="noopener license" target="_blank">{l}</a>, Wikimedia Commons</li>'
    if H[0]['credit'][1] not in ls:
        ls = ls.replace(anchor, anchor + items, 1)
    open(lp, 'w', encoding='utf-8').write(ls)
    print(lang, 'ok', n)
