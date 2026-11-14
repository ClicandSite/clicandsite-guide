"""Ajoute le bloc « À réserver sur place » (widget GetYourGuide + sélection Viator vérifiée) sur une page.
Usage : python3 _outils/activites.py ../clicandsite-guide ../clicandsite-guide-en
Idempotent : le bloc est remplacé entre les marqueurs <!--acts:start--> et <!--acts:end-->.
Chaque activité Viator doit avoir été vérifiée (ouverte, pid conservé, lieu inclus) avant d'être ajoutée ici."""
import re, sys, os, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from viator_picks import P as VP, G as VG, A as VA, PG as VPG, PA as VPA, RG as VRG  # sélection Viator vérifiée (Côte d'Azur, 14/11/2026)
PID = 'pid=P00331213&amp;mcid=42383&amp;medium=link&amp;campaign='
# Lieux GYG trop larges remplacés (testé 14/11/2026) : 132103 = Auvergne-Rhône-Alpes → Lyon en tête
# Activités GYG choisies (ordre gardé ; les 2 premières sur mobile)
GYG_TOURS = {'cote-d-azur/cannes': '95337,243442,65370,641064', 'french-riviera/cannes': '95337,243442,65370,641064',
             'paris/arc-de-triomphe': '66157,344326',
             'paris/tour-eiffel': '62484,403497,983435,403969', 'paris/eiffel-tower': '62484,403497,983435,403969',
             'paris/notre-dame': '1156458,778850,525225,1239537',
             'paris/sainte-chapelle': '828673,525225,233477',
             'paris/pantheon': '70680,1428204,497728',
             'paris/invalides': '70627,1148557,463678,1501481',
             'paris/conciergerie': '222147,525225'}
LOC_OVERRIDE = {'132103': '201172'}
PAGES = {
  # clé : (chemin FR, chemin EN)
  'le-suquet': {
    'fr': 'cote-d-azur/le-suquet', 'en': 'french-riviera/le-suquet',
    
    'via_all': 'Cannes-attractions/Le-Suquet/d786-a1817',
    'via': [  # vérifiées le 14/11/2026
      ('tours/Cannes/Guided-Tour-in-Cannes-History-Glamour-and-Cinema/d786-183050P4',
       'Visite guidée de Cannes par une scénariste', '2 h 40 · vieille ville, marché et Croisette',
       'Cannes guided tour by a screenwriter', '2 h 40 · old town, market and Croisette'),
      ('tours/Cannes/Cannes-Beyond-The-Red-Carpet-Walking-Tour/d786-14737P19',
       'Cannes, au-delà du tapis rouge', '3 h · colline du Suquet, marché et Croisette',
       'Cannes beyond the red carpet', '3 h · Suquet hill, market and Croisette'),
    ],
  },
}
T = {'fr': dict(h='À réserver sur place', sub='Activités en direct', sel='Notre sélection Viator',
                all='Toutes les activités sur Viator', loc='fr-FR', pre='fr-FR/', note='Liens partenaires.'),
     'en': dict(h='Book on the spot', sub='Live activities', sel='Our Viator picks',
                all='All activities on Viator', loc='en-US', pre='', note='Partner links.')}
ARR = '<svg class="cta-arr" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def block(cfg, lang):
    t = T[lang]; path = cfg[lang]
    camp = f"clicandsite-{lang}-{path.replace('/', '-')}"
    rows = ''
    for u, tfr, dfr, ten, den in cfg['via']:
        tt, dd = (tfr, dfr) if lang == 'fr' else (ten, den)
        rows += (f'<li><a class="pick" href="https://www.viator.com/{t["pre"]}{u}?{PID}{camp}" rel="sponsored nofollow noopener" target="_blank">'
                 f'<span class="pick__t">{html.escape(tt)}</span><span class="pick__d">{html.escape(dd)}</span>{ARR}</a></li>')
    return (f'<!--acts:start--><div class="live" id="sur-place"><h3 class="live__t">{t["h"]}</h3>'
            f'<div class="live__gyg"><p class="live__s">{t["sub"]} · GetYourGuide</p>'
            f'<div data-gyg-href="https://widget.getyourguide.com/default/activities.frame" data-gyg-locale-code="{t["loc"]}" data-gyg-widget="activities" data-gyg-number-of-items="{min(4, len(cfg["gyg_tours"].split(","))) if cfg.get("gyg_tours") else 4}" data-gyg-cmp="{camp}" data-gyg-partner-id="XMYSXGR" '+(f'data-gyg-tour-ids="{cfg["gyg_tours"]}"' if cfg.get("gyg_tours") else f'data-gyg-location-id="{cfg["gyg_loc"]}"')+'></div></div>'
            + (f'<p class="live__s live__s--via">{t["sel"]}</p><ul class="picks">{rows}</ul>' if rows else '') +
            f'<p class="live__all"><a href="{cfg["via_all_url"]}" rel="sponsored nofollow noopener" target="_blank">{t["all"]}{ARR}</a></p>'
            '<script>(function(){var d=document.querySelector(".live__gyg");if(!d)return;function l(){if(window.__gyg)return;window.__gyg=1;var w=d.querySelector("[data-gyg-widget]"),ti=w.getAttribute("data-gyg-tour-ids");if(innerWidth<700){w.setAttribute("data-gyg-number-of-items","2");if(ti)w.setAttribute("data-gyg-tour-ids",ti.split(",").slice(0,2).join(","))}var s=document.createElement("script");s.async=1;s.src="https://widget.getyourguide.com/dist/pa.umd.production.min.js";s.setAttribute("data-gyg-partner-id","XMYSXGR");document.body.appendChild(s)}'
            'if("IntersectionObserver"in window){var o=new IntersectionObserver(function(e){if(e[0].isIntersecting){l();o.disconnect()}},{rootMargin:"600px"});o.observe(d)}else l()})();</script>'
            '</div><!--acts:end-->')
def apply(root, lang):
    n = 0
    for dp, dn, fn in os.walk(root):
        if '/.git' in dp or 'index.html' not in fn: continue
        p = os.path.join(dp, 'index.html'); s = open(p, encoding='utf-8').read()
        if 'class="book__lead"' not in s: continue
        rel = os.path.relpath(dp, root).replace(os.sep, '/')
        cfg = next((dict(c) for c in PAGES.values() if c[lang] == rel), {'via': []})
        slug = rel.split('/')[-1]
        if rel.startswith(('cote-d-azur/', 'french-riviera/')): g, a = VG, VA
        elif rel.startswith('paris/'): g, a = VPG, VPA
        elif rel.startswith(('idees/', 'ideas/')): g, a = {}, {}
        else: g, a = VRG, {}
        if not cfg['via'] and slug in g: cfg['via'] = [VP[k] for k in g[slug]]
        if not cfg.get('via_all') and slug in a: cfg['via_all'] = a[slug]
        cfg[lang] = rel
        m = re.search(r'getyourguide\.(?:fr|com)/[^"?]*?-l(\d+)/', s)
        if not m: print('sans lieu GYG', p); continue
        cfg['gyg_loc'] = LOC_OVERRIDE.get(m.group(1), m.group(1))
        if rel in GYG_TOURS: cfg['gyg_tours'] = GYG_TOURS[rel]
        if cfg.get('via_all'):
            camp = f"clicandsite-{lang}-{rel.replace('/', '-')}"
            cfg['via_all_url'] = f"https://www.viator.com/{T[lang]['pre']}{cfg['via_all']}?{PID}{camp}"
        else:
            v = re.search(r'href="(https://www\.viator\.com/[^"]+)"', s)
            if not v: print('sans Viator', p); continue
            cfg['via_all_url'] = v.group(1)
        b = block(cfg, lang)
        if '<!--acts:start-->' in s:
            s = re.sub(r'<!--acts:start-->.*?<!--acts:end-->', lambda m: b, s, flags=re.S)
        else:
            s = re.sub(r'(<p class="book__lead">.*?</p>)', lambda m: m.group(1) + '\n      ' + b, s, count=1, flags=re.S)
        if 'activites.css' not in s:
            depth = rel.count('/') + 1
            s = re.sub(r'(<link[^>]+assets/style\.css\?v=[^"]*">)', lambda m: m.group(1) + f'<link rel="stylesheet" href="{"../"*depth}assets/activites.css?v=1">', s, count=1)
        open(p, 'w', encoding='utf-8').write(s); n += 1
    print(lang, n, 'pages')
if __name__ == '__main__':
    apply(sys.argv[1], 'fr'); apply(sys.argv[2], 'en')
