import re, sys
sys.path.insert(0, '/tmp/g')
from rando_gen import fr_typo
from randos_data import H
NAME = {h['slug']: (h['fr']['crumb'], h['en']['crumb']) for h in H}
NAME['mont-gros'] = ('Le mont Gros', 'Mont Gros')
FRN = {'tete-de-chien':'La Tête de Chien','promenade-le-corbusier':'La promenade Le Corbusier','lac-de-trecolpas':'Le lac de Trécolpas','val-de-siagne':'Le circuit du Val de Siagne','pic-de-courmettes':'Le pic de Courmettes','vieil-aspremont':'Les ruines du Vieil Aspremont','sentier-nietzsche':'Le sentier Nietzsche','cascade-de-vescagne':'La cascade de Vescagne','cime-de-la-forna':'La cime de la Forna','sentier-de-la-brague':'Le sentier de la Brague','sentier-du-cap-ferrat':'Le sentier du littoral du cap Ferrat','plage-de-la-mala':'La plage de la Mala','mont-gros':'Le mont Gros'}
ENN = {'tete-de-chien':'The Tête de Chien loop','promenade-le-corbusier':'The Promenade Le Corbusier','lac-de-trecolpas':'Lac de Trécolpas','val-de-siagne':'The Val de Siagne loop','pic-de-courmettes':'Pic de Courmettes','vieil-aspremont':'The Vieil Aspremont ruins','sentier-nietzsche':'The Nietzsche Path','cascade-de-vescagne':'Cascade de Vescagne','cime-de-la-forna':'Cime de la Forna','sentier-de-la-brague':'The Brague trail','sentier-du-cap-ferrat':'The Cap Ferrat coastal path','plage-de-la-mala':'Plage de la Mala','mont-gros':'Mont Gros'}
LBL = ('randonnée', 'hike')
M = {
 'eze': ['sentier-nietzsche', 'plage-de-la-mala', 'cime-de-la-forna'],
 'monaco': ['tete-de-chien', 'plage-de-la-mala'],
 'rocher-de-monaco': ['tete-de-chien'], 'jardin-exotique-monaco': ['tete-de-chien'], 'monte-carlo': ['tete-de-chien'],
 'roquebrune-cap-martin': ['promenade-le-corbusier'], 'menton': ['promenade-le-corbusier'],
 'saint-jean-cap-ferrat': ['sentier-du-cap-ferrat'], 'villa-ephrussi-de-rothschild': ['sentier-du-cap-ferrat'],
 'beaulieu-sur-mer': ['sentier-du-cap-ferrat', 'sentier-nietzsche'], 'villefranche-sur-mer': ['sentier-du-cap-ferrat'],
 'biot': ['sentier-de-la-brague'], 'antibes': ['sentier-de-la-brague'],
 'grasse': ['val-de-siagne'], 'mandelieu-la-napoule': ['val-de-siagne'], 'mougins': ['val-de-siagne'],
 'saint-paul-de-vence': ['pic-de-courmettes', 'cascade-de-vescagne'], 'gourdon': ['pic-de-courmettes'],
 'nice': ['mont-gros', 'vieil-aspremont', 'lac-de-trecolpas'], 'colline-du-chateau': ['mont-gros'], 'musee-chagall': ['mont-gros'],
}
R = {'fr': ('/home/claude/clicandsite-guide', 'cote-d-azur', FRN, 'sentier'), 'en': ('/home/claude/clicandsite-guide-en', 'french-riviera', ENN, 'trail')}
n = 0
for lang, (root, reg, NM, _) in R.items():
    for page, targets in M.items():
        p = f'{root}/{reg}/{page}/index.html'
        try: s = open(p, encoding='utf-8').read()
        except FileNotFoundError: print('absent', p); continue
        m = re.search(r'(<h2 id="autour">[^<]*</h2><ul class="near">)(.*?)(</ul>)', s) or re.search(r'(<h2 id="nearby">[^<]*</h2><ul class="near">)(.*?)(</ul>)', s)
        if not m: print('pas de bloc near', p); continue
        add = ''
        for t in targets:
            if f'/{t}/' in m.group(2): continue
            d = 'randonnée' if lang == 'fr' else 'hike'
            if t in ('plage-de-la-mala',): d = 'plage et sentier du littoral' if lang == 'fr' else 'beach and coastal path'
            if t in ('promenade-le-corbusier', 'sentier-du-cap-ferrat'): d = 'sentier du littoral' if lang == 'fr' else 'coastal path'
            add += f'<li><a href="../../{reg}/{t}/">{NM[t]}</a> <span class="near__d">{d}</span></li>'
        if add:
            s = s.replace(m.group(0), m.group(1) + m.group(2) + add + m.group(3), 1); n += 1
            open(p, 'w', encoding='utf-8').write(s)
print('pages modifiées', n)
