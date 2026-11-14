"""Ajoute le bloc « À réserver sur place » (widget GetYourGuide + sélection Viator vérifiée) sur une page.
Usage : python3 _outils/activites.py ../clicandsite-guide ../clicandsite-guide-en
Idempotent : le bloc est remplacé entre les marqueurs <!--acts:start--> et <!--acts:end-->.
Chaque activité Viator doit avoir été vérifiée (ouverte, pid conservé, lieu inclus) avant d'être ajoutée ici."""
import re, sys, os, html
PID = 'pid=P00331213&amp;mcid=42383&amp;medium=link&amp;campaign='
PAGES = {
  # clé : (chemin FR, chemin EN)
  'le-suquet': {
    'fr': 'cote-d-azur/le-suquet', 'en': 'french-riviera/le-suquet',
    'gyg_q': 'Le Suquet, Cannes',
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
            f'<div data-gyg-href="https://widget.getyourguide.com/default/activities.frame" data-gyg-locale-code="{t["loc"]}" data-gyg-widget="activities" data-gyg-number-of-items="4" data-gyg-cmp="{camp}" data-gyg-partner-id="XMYSXGR" data-gyg-q="{cfg["gyg_q"]}"></div></div>'
            f'<p class="live__s live__s--via">{t["sel"]}</p><ul class="picks">{rows}</ul>'
            f'<p class="live__all"><a href="https://www.viator.com/{t["pre"]}{cfg["via_all"]}?{PID}{camp}" rel="sponsored nofollow noopener" target="_blank">{t["all"]}{ARR}</a></p>'
            '<script>(function(){var d=document.querySelector(".live__gyg");if(!d)return;function l(){if(window.__gyg)return;window.__gyg=1;var s=document.createElement("script");s.async=1;s.src="https://widget.getyourguide.com/dist/pa.umd.production.min.js";s.setAttribute("data-gyg-partner-id","XMYSXGR");document.body.appendChild(s)}'
            'if("IntersectionObserver"in window){var o=new IntersectionObserver(function(e){if(e[0].isIntersecting){l();o.disconnect()}},{rootMargin:"600px"});o.observe(d)}else l()})();</script>'
            '</div><!--acts:end-->')
def apply(root, lang):
    for key, cfg in PAGES.items():
        p = os.path.join(root, cfg[lang], 'index.html'); s = open(p, encoding='utf-8').read()
        b = block(cfg, lang)
        if '<!--acts:start-->' in s:
            s = re.sub(r'<!--acts:start-->.*?<!--acts:end-->', lambda m: b, s, flags=re.S)
        else:
            s = re.sub(r'(<p class="book__lead">.*?</p>)', lambda m: m.group(1) + '\n      ' + b, s, count=1, flags=re.S)
        if 'activites.css' not in s:
            s = s.replace('/style.css?v=aff1114">', '/style.css?v=aff1114"><link rel="stylesheet" href="../../assets/activites.css?v=1">', 1)
        open(p, 'w', encoding='utf-8').write(s); print('ok', lang, cfg[lang])
if __name__ == '__main__':
    apply(sys.argv[1], 'fr'); apply(sys.argv[2], 'en')
