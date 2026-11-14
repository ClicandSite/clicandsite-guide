"""Remplace les recherches GetYourGuide (s/?q=...) par la page lieu GetYourGuide (slug-lNNNN), partner_id conservé.
Usage : python3 _outils/gyg_fix.py write ../clicandsite-guide ../clicandsite-guide-en  (dry = simulation)"""
import re, os, sys, collections, urllib.parse
L = {}
def m(slug, *qs):
    for q in qs: L[q] = slug
m('bonifacio-l91244', 'bonifacio', 'bonifacio boat', 'lavezzi')
m('porto-vecchio-l91235', 'porto-vecchio', 'porto-vecchio boat')
m('ajaccio-l1535', 'ajaccio', 'ajaccio boat')
m('ajaccio-county-l213076', 'piana', 'scandola')
m('bastia-l1536', 'bastia', 'cap corse')
m('haute-corse-l150371', 'calvi')
m('bordeaux-l287', 'bordeaux', 'cité du vin bordeaux', 'saint-emilion', 'saint-emilion wine tasting')
m('dune-of-pilat-l3438', 'dune du pilat'); m('arcachon-l32338', 'arcachon')
m('sarlat-la-caneda-l1356', 'sarlat', 'lascaux sarlat')
m('dordogne-l39314', 'lascaux', 'beynac', 'castelnaud', 'milandes', 'marqueyssac', 'dordogne', 'dordogne castles',
  'dordogne valley', 'dordogne canoe', 'bergerac', 'bergerac wine', 'périgueux', 'périgord')
m('la-roque-gageac-l139356', 'la roque-gageac')
m('rocamadour-l190520', 'rocamadour', 'padirac', 'rocamadour padirac', 'saint-cirq-lapopie', 'cahors')
pat = re.compile(r'(https://www\.getyourguide\.(?:fr|com)/)s/\?q=([^&"\']+)(&amp;|&)')
st = collections.Counter(); unk = set(); files = 0
for root in sys.argv[2:]:
    for dp, dn, fn in os.walk(root):
        if '/.git' in dp: continue
        for f in fn:
            if not f.endswith(('.html', '.json', '.js', '.xml')): continue
            p = os.path.join(dp, f); s = open(p, encoding='utf-8', errors='ignore').read()
            if 'getyourguide' not in s or '/s/?q=' not in s: continue
            def rep(mo):
                q = urllib.parse.unquote_plus(mo.group(2)).lower()
                if q not in L: unk.add(q); return mo.group(0)
                st['fix'] += 1; return f'{mo.group(1)}{L[q]}/?'
            n = pat.sub(rep, s)
            if n != s:
                files += 1
                if sys.argv[1] == 'write': open(p, 'w', encoding='utf-8').write(n)
print(st, files, 'inconnues:', sorted(unk))
