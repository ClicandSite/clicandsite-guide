import re, json, os, sys
from PIL import Image, ImageOps

SLUG = 'mont-gros'
FR_ROOT, EN_ROOT = '/home/claude/clicandsite-guide', '/home/claude/clicandsite-guide-en'
TPL = {'fr': (FR_ROOT, 'cote-d-azur', 'colline-du-chateau'), 'en': (EN_ROOT, 'french-riviera', 'colline-du-chateau')}
BASE = {'fr': 'https://clicandsite.fr', 'en': 'https://clicandsite.com'}
REG = {'fr': 'cote-d-azur', 'en': 'french-riviera'}
CREDIT = ('Cayambe', 'https://commons.wikimedia.org/wiki/File:Nice_Est_observatoire_01.jpg', 'CC BY-SA 3.0', 'https://creativecommons.org/licenses/by-sa/3.0/')

C = {
'fr': dict(
 name='La randonnée du mont Gros',
 title='Randonnée du mont Gros à Nice : parc du Vinaigrier et Observatoire',
 desc='La randonnée du mont Gros à Nice : boucle de 5 km depuis Saint-Roch par le parc du Vinaigrier, vue sur la baie, Observatoire de Nice, durée, dénivelé, horaires et accès en bus.',
 h1='La randonnée du mont Gros, au-dessus de Nice',
 lead='Une boucle de 5 km depuis le quartier Saint-Roch, à travers le parc du Vinaigrier, sous la grande coupole de l’Observatoire de Nice.',
 alt='Le mont Gros et la coupole de l’Observatoire de Nice au-dessus des immeubles de Nice-Est',
 intro=['Le mont Gros est une colline de 375 mètres à l’est de Nice. À son sommet se dresse l’Observatoire de Nice, dont on aperçoit la grande coupole blanche depuis toute la ville.',
        'Juste en dessous, le parc du Vinaigrier offre des sentiers en pleine nature, à quelques minutes du centre. C’est l’une des plus belles randonnées que l’on puisse faire au départ même de Nice.'],
 hist=['L’Observatoire de Nice est construit au sommet du mont Gros à partir de 1881, à l’initiative du banquier Raphaël Bischoffsheim. Les bâtiments sont dessinés par Charles Garnier, l’architecte de l’Opéra de Paris.',
       'La coupole de la grande lunette est réalisée par les ateliers de Gustave Eiffel et les travaux s’achèvent en 1887. Le site appartient aujourd’hui à l’Observatoire de la Côte d’Azur.'],
 see_h='Que voir pendant la randonnée',
 see=[('Le parc du Vinaigrier','Un espace naturel de 31 hectares, propriété du Conservatoire du littoral, sur les pentes du mont Gros. Les sentiers passent entre oliveraies, pins et anciennes cultures en terrasses.'),
      ('Le belvédère du mont Vinaigrier','Au plateau sommital, à environ 370 mètres, une tourelle en bois sert de belvédère. La vue s’étend sur Nice, la rade de Villefranche, le cap Ferrat et les sommets des Alpes.'),
      ('Les traces du passé','Le parc garde les vestiges d’un mur cyclopéen, reste d’un habitat fortifié, et un ancien système d’irrigation lié aux cultures d’autrefois.'),
      ('L’Observatoire de Nice','La grande coupole blanche domine la randonnée. Le site de l’Observatoire ne se visite qu’avec un guide, sur réservation.')],
 rando_h='L’itinéraire de la randonnée',
 rando=['Départ de l’église Saint-Roch. Montez l’avenue Giacobi et son escalier jusqu’au boulevard Bischoffsheim, sur la Grande Corniche.',
        'Prenez le chemin du Cal du Mont Gros, qui monte entre les villas, puis suivez le balisage jaune et rouge du sentier de grande randonnée de pays de Nice jusqu’à l’entrée du parc du Vinaigrier.',
        'Dans le parc, prenez à droite le sentier du Vinaigrier supérieur jusqu’au plateau sommital et à sa tourelle en bois.',
        'Redescendez par la station d’épuration, puis par le chemin de niveau qui ramène à l’entrée du parc, et revenez à Saint-Roch par le même chemin.'],
 rando_note='Comptez environ 2 h 30 de marche pour 5,2 km et 330 mètres de dénivelé. Le sentier est de difficulté moyenne : la montée depuis Saint-Roch est raide par endroits.',
 go_h='Comment aller au départ',
 go=[('À pied','Le départ se trouve devant l’église Saint-Roch, dans le quartier du même nom, à l’est du centre de Nice.'),
     ('En bus','La ligne 84 des Lignes d’Azur dessert le haut du parc, à l’arrêt « Sainte-Anne ». Pratique pour une balade plus courte, sans la montée depuis la ville.'),
     ('En voiture','Prenez la Grande Corniche puis le boulevard de l’Observatoire : un petit parking se trouve à l’entrée haute du parc, environ 500 mètres après l’Observatoire.')],
 infos_h='Infos pratiques 2026 : le mont Gros',
 infos=[('Parc du Vinaigrier','gratuit, ouvert tous les jours, de 7 h 30 à 20 h d’avril à octobre et de 8 h à 18 h de novembre à mars.'),
        ('Observatoire de Nice','visite guidée uniquement, sur réservation en ligne sur oca.eu : 12 € plein tarif, 10 € tarif réduit, 6 € enfants et étudiants, gratuit pour les moins de 6 ans.'),
        ('Visite','comptez environ 2 heures pour la visite guidée de l’Observatoire.')],
 maj='Tarifs et horaires relevés en novembre 2026 auprès de l’Observatoire de la Côte d’Azur et de l’office de tourisme ; ils peuvent changer, vérifiez avant de partir.',
 tips_h='Nos conseils pour la randonnée',
 tips=['Prenez de bonnes chaussures : certains passages sont escarpés.',
       'Emportez de l’eau : il n’y a ni commerce ni restaurant autour de l’Observatoire.',
       'Partez tôt le matin ou en fin de journée pour la lumière sur la baie et moins de chaleur.',
       'Pour visiter l’Observatoire, réservez votre créneau à l’avance sur le site de l’Observatoire de la Côte d’Azur.',
       'Pour une plus longue randonnée, continuez par le col de Villefranche vers le mont Alban et le mont Boron.'],
 eps_h='Y aller avec un chauffeur privé',
 eps_t='Transfert Côte d’Azur avec chauffeur privé',
 eps_d='Aéroport, gare ou hôtel : un chauffeur vous dépose au départ de la randonnée ou à l’entrée haute du parc, en van ou berline haut de gamme, prix fixe par véhicule.',
 eps_b='Réserver mon transfert', eps_u='https://www.elite-prestige-services.fr/#reservation',
 near=[('port-lympia','Le port Lympia','à environ 10 min en voiture'),('vieux-nice','Le Vieux-Nice','à environ 15 min en voiture'),('villefranche-sur-mer','Villefranche-sur-Mer','à environ 15 min en voiture')],
 faq=[('Combien de temps dure la randonnée du mont Gros ?','Comptez environ 2 h 30 pour la boucle de 5,2 km depuis l’église Saint-Roch, avec 330 mètres de dénivelé.'),
      ('La randonnée est-elle difficile ?','Elle est de difficulté moyenne : la montée depuis Saint-Roch est raide par endroits, le reste du parcours est facile.'),
      ('Peut-on visiter l’Observatoire de Nice ?','Oui, mais uniquement en visite guidée, sur réservation en ligne auprès de l’Observatoire de la Côte d’Azur. Le plein tarif est de 12 €.'),
      ('Le parc du Vinaigrier est-il gratuit ?','Oui, l’entrée est gratuite. Le parc est ouvert tous les jours, jusqu’à 20 h d’avril à octobre et jusqu’à 18 h de novembre à mars.')],
 fiche=[('Distance','5,2 km en boucle'),('Durée','2 h 30 environ'),('Dénivelé','330 m'),('Départ','Église Saint-Roch'),('Prix','Gratuit (parc)')],
 card='Une boucle de 5 km au-dessus de Nice, par le parc du Vinaigrier et sous la coupole de l’Observatoire.',
 credit_lbl='Photo : ', home='Accueil', reg='Côte d’Azur', crumb='Le mont Gros', faq_h='Questions fréquentes', near_h='À voir à proximité', hist_h='Un peu d’histoire', fiche_h='En bref',
 near_q='Que voir près du mont Gros ?',
),
'en': dict(
 name='The Mont Gros hike',
 title='Mont Gros hike in Nice: Parc du Vinaigrier and the Observatory',
 desc='Hiking Mont Gros in Nice: a 5 km loop from Saint-Roch through the Parc du Vinaigrier, views over the bay, the Nice Observatory, time, climb, opening hours and bus access.',
 h1='The Mont Gros hike above Nice',
 lead='A 5 km loop from the Saint-Roch district, through the Parc du Vinaigrier, below the great dome of the Nice Observatory.',
 alt='Mont Gros and the dome of the Nice Observatory above the buildings of eastern Nice',
 intro=['Mont Gros is a 375-metre hill on the east side of Nice. On top stands the Nice Observatory, whose great white dome can be seen from all over the city.',
        'Just below, the Parc du Vinaigrier has trails through real countryside, a few minutes from the centre. It is one of the best hikes you can start right from Nice.'],
 hist=['The Nice Observatory was built on top of Mont Gros from 1881, at the initiative of the banker Raphaël Bischoffsheim. The buildings were designed by Charles Garnier, the architect of the Paris Opera.',
       'The dome of the great telescope was made by Gustave Eiffel’s workshops and the work was completed in 1887. Today the site belongs to the Observatoire de la Côte d’Azur.'],
 see_h='What to see on the hike',
 see=[('The Parc du Vinaigrier','A 31-hectare natural area owned by the Conservatoire du littoral, on the slopes of Mont Gros. The trails wind between olive groves, pines and old terraced fields.'),
      ('The Mont Vinaigrier viewpoint','On the summit plateau, at about 370 metres, a wooden tower serves as a viewpoint. The view takes in Nice, the bay of Villefranche, Cap Ferrat and the peaks of the Alps.'),
      ('Traces of the past','The park keeps the remains of a cyclopean wall from an ancient fortified settlement, and an old irrigation system from the farms of the past.'),
      ('The Nice Observatory','The great white dome towers over the hike. The Observatory site can only be visited with a guide, on booking.')],
 rando_h='The route',
 rando=['Start at the Saint-Roch church. Walk up Avenue Giacobi and its steps to Boulevard Bischoffsheim, on the Grande Corniche.',
        'Take the Chemin du Cal du Mont Gros, which climbs between villas, then follow the yellow and red waymarks of the Nice long-distance trail (GRP) to the entrance of the Parc du Vinaigrier.',
        'In the park, turn right on the upper Vinaigrier trail to the summit plateau and its wooden tower.',
        'Come down past the water treatment station, then along the level path back to the park entrance, and return to Saint-Roch the way you came.'],
 rando_note='Allow about 2 hours 30 minutes for 5.2 km and 330 metres of climb. The trail is of medium difficulty: the climb from Saint-Roch is steep in places.',
 go_h='How to get to the start',
 go=[('On foot','The start is in front of the Saint-Roch church, in the district of the same name, east of central Nice.'),
     ('By bus','Lignes d’Azur bus 84 serves the top of the park, at the “Sainte-Anne” stop. Handy for a shorter walk without the climb from town.'),
     ('By car','Take the Grande Corniche and then Boulevard de l’Observatoire: there is a small car park at the upper entrance of the park, about 500 metres past the Observatory.')],
 infos_h='Practical info 2026: Mont Gros',
 infos=[('Parc du Vinaigrier','free, open every day, 7.30 am to 8 pm from April to October and 8 am to 6 pm from November to March.'),
        ('Nice Observatory','guided visits only, booked online on oca.eu: €12 full price, €10 reduced, €6 children and students, free under 6.'),
        ('Visit','allow about 2 hours for the guided visit of the Observatory.')],
 maj='Prices and opening times checked in November 2026 with the Observatoire de la Côte d’Azur and the tourist office; they may change, so check before you go.',
 tips_h='Tips for the hike',
 tips=['Wear good shoes: some stretches are steep.',
       'Take water: there are no shops or restaurants around the Observatory.',
       'Go early in the morning or late in the day for the light over the bay and less heat.',
       'To visit the Observatory, book your slot in advance on the Observatoire de la Côte d’Azur website.',
       'For a longer hike, carry on past the Col de Villefranche to Mont Alban and Mont Boron.'],
 eps_h='Go there with a private driver',
 eps_t='French Riviera transfer with a private driver',
 eps_d='Airport, station or hotel: a driver drops you at the start of the hike or at the upper entrance of the park, in a premium van or saloon, with a fixed price per vehicle.',
 eps_b='Book my transfer', eps_u='https://www.elite-prestige-services.fr/?lang=en#reservation',
 near=[('port-lympia','Port Lympia','about 10 min by car'),('vieux-nice','Vieux-Nice','about 15 min by car'),('villefranche-sur-mer','Villefranche-sur-Mer','about 15 min by car')],
 faq=[('How long is the Mont Gros hike?','Allow about 2 hours 30 minutes for the 5.2 km loop from the Saint-Roch church, with 330 metres of climb.'),
      ('Is the hike difficult?','It is of medium difficulty: the climb from Saint-Roch is steep in places, the rest is easy.'),
      ('Can you visit the Nice Observatory?','Yes, but only on a guided visit, booked online with the Observatoire de la Côte d’Azur. Full price is €12.'),
      ('Is the Parc du Vinaigrier free?','Yes, entry is free. The park is open every day, until 8 pm from April to October and until 6 pm from November to March.')],
 fiche=[('Distance','5.2 km loop'),('Time','About 2 h 30'),('Climb','330 m'),('Start','Saint-Roch church'),('Price','Free (park)')],
 card='A 5 km loop above Nice, through the Parc du Vinaigrier and below the Observatory dome.',
 credit_lbl='Photo: ', home='Home', reg='French Riviera', crumb='Mont Gros', faq_h='Frequently asked questions', near_h='Nearby', hist_h='A bit of history', fiche_h='At a glance',
 near_q='What is there to see near Mont Gros?',
)}

def fr_typo(t):
    t = re.sub(r' ([:;?!»])', '\u202f\\1', t)
    t = t.replace('« ', '«\u202f')
    t = re.sub(r'(\d) (h|km|m|€|heures|mètres|hectares)\b', '\\1\u00a0\\2', t)
    return t

def esc(t): return t.replace('&', '&amp;')

def page(lang):
    root, reg, tslug = TPL[lang]
    d = C[lang]; T = (fr_typo if lang == 'fr' else (lambda x: x))
    tpl = open(f'{root}/{reg}/{tslug}/index.html', encoding='utf-8').read()
    url = f'{BASE[lang]}/{REG[lang]}/{SLUG}/'
    other = 'en' if lang == 'fr' else 'fr'
    ourl = f'{BASE[other]}/{REG[other]}/{SLUG}/'
    head = tpl[:tpl.index('</head>')]
    head = re.sub(r'<title>.*?</title>', f'<title>{esc(T(d["title"]))} | Clic&amp;Site</title>', head)
    head = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m[1] + esc(T(d['desc'])), head)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m[1] + esc(T(d['title'])) + ' | Clic&amp;Site', head)
    head = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m[1] + esc(T(d['desc'])), head)
    head = head.replace(f'/{tslug}/', f'/{SLUG}/').replace(f'og/{tslug}.jpg', f'og/{SLUG}.jpg')
    head = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', '', head, flags=re.S)
    ld = [
     {"@context": "https://schema.org", "@type": "TouristAttraction", "name": T(d['name']), "description": T(d['desc']), "url": url,
      "image": [f"{BASE[lang]}/assets/photos/{SLUG}.jpg", f"{BASE[lang]}/assets/og/{SLUG}.jpg"],
      "geo": {"@type": "GeoCoordinates", "latitude": 43.7255, "longitude": 7.2997},
      "address": {"@type": "PostalAddress", "addressLocality": "Nice", "addressRegion": "Provence-Alpes-Côte d’Azur", "addressCountry": "FR"},
      "containedInPlace": {"@type": "Place", "name": d['reg']}},
     {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": T(q), "acceptedAnswer": {"@type": "Answer", "text": T(a)}} for q, a in d['faq'] + [(d['near_q'], near_txt(lang))]]},
     {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": d['home'], "item": f"{BASE[lang]}/"},
        {"@type": "ListItem", "position": 2, "name": d['reg'], "item": f"{BASE[lang]}/{REG[lang]}/"},
        {"@type": "ListItem", "position": 3, "name": T(d['crumb']), "item": url}]}]
    head += ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld)
    body = tpl[tpl.index('</head>'):tpl.index('<header class="post')]
    body = body.replace(f'/{tslug}/', f'/{SLUG}/')
    P = '../../assets/photos/' + SLUG
    hero = (f'<header class="post post--pin">\n  <picture><source type="image/webp" srcset="{P}-960.webp 960w, {P}-1280.webp 1280w, {P}.webp 1920w" sizes="100vw">'
            f'<img class="post__img" src="{P}.jpg" srcset="{P}-960.jpg 960w, {P}-1280.jpg 1280w, {P}.jpg 1920w" sizes="100vw" alt="{esc(T(d["alt"]))}" fetchpriority="high"></picture><div class="post__shade" aria-hidden="true"></div>\n'
            f'  <div class="wrap post__in">\n    <div class="stamp" aria-hidden="true"><span class="stamp__num">06</span></div><div class="postmark" aria-hidden="true"><span>Nice</span></div>\n'
            f'    <h1 class="post__title">{esc(T(d["h1"]))}</h1>\n    <p class="post__lead">{esc(T(d["lead"]))}</p>\n  </div>\n'
            f'  <p class="credit">{d["credit_lbl"]}<a href="{CREDIT[1]}" rel="noopener" target="_blank">{CREDIT[0]}</a>, <a href="{CREDIT[3]}" rel="noopener license" target="_blank">{CREDIT[2]}</a>, Wikimedia Commons</p>\n</header>\n')
    crumbs = re.search(r'<nav class="crumbs wrap".*?</p>\n', tpl, re.S).group(0)
    crumbs = re.sub(r'<li aria-current="page">.*?</li>', f'<li aria-current="page">{esc(T(d["crumb"]))}</li>', crumbs)
    crumbs = re.sub(r'(Mis à jour le |Updated )[^<]*', lambda m: m[1] + ('15 novembre 2026' if lang == 'fr' else '15 November 2026'), crumbs)
    h = lambda t: esc(T(t))
    art = '<div class="wrap layout">\n  <article class="prose">\n    ' + ''.join(f'<p>{h(p)}</p>' for p in d['intro']) + '\n'
    art += f'    <h2 id="{"histoire" if lang == "fr" else "history"}">{h(d["hist_h"])}</h2>\n' + '\n'.join(f'<p>{h(p)}</p>' for p in d['hist']) + '\n'
    art += f'<h2 id="itineraire">{h(d["rando_h"])}</h2><ol>' + ''.join(f'<li>{h(x)}</li>' for x in d['rando']) + f'</ol><p>{h(d["rando_note"])}</p>\n'
    art += f'    <h2>{h(d["see_h"])}</h2>' + ''.join(f'<h3>{h(a)}</h3><p>{h(b)}</p>' for a, b in d['see']) + '\n'
    art += f'    <h2>{h(d["go_h"])}</h2>' + ''.join(f'<h3>{h(a)}</h3><p>{h(b)}</p>' for a, b in d['go']) + '\n'
    art += f'    <h2 id="infos-2026">{h(d["infos_h"])}</h2><ul>' + ''.join(f'<li><strong>{h(a)}</strong>{h(" : " if lang == "fr" else ": ")}{h(b)}</li>' for a, b in d['infos']) + f'</ul><p class="maj">{h(d["maj"])}</p>\n'
    art += f'    <h2>{h(d["tips_h"])}</h2><ul>' + ''.join(f'<li>{h(x)}</li>' for x in d['tips']) + '</ul>\n'
    eps_li = re.search(r'<li class="act act--eps">.*?</li>', tpl, re.S).group(0)
    eps_li = re.sub(r'<h3 class="act__t">.*?</h3>', f'<h3 class="act__t">{h(d["eps_t"])}</h3>', eps_li)
    eps_li = re.sub(r'<p class="act__d">.*?</p>', f'<p class="act__d">{h(d["eps_d"])}</p>', eps_li)
    art += (f'    <section class="book" id="chauffeur" aria-labelledby="chauffeur-t">\n      <h2 id="chauffeur-t" class="book__t">{h(d["eps_h"])}</h2>\n'
            f'      <ul class="acts">{eps_li}</ul>\n    </section>\n')
    art += f'    <h2 id="autour">{h(d["near_h"])}</h2><ul class="near">' + ''.join(f'<li><a href="../../{REG[lang]}/{s}/">{h(n)}</a> <span class="near__d">{h(t)}</span></li>' for s, n, t in d['near']) + '</ul>\n'
    art += f'    <h2>{h(d["faq_h"])}</h2>\n    <div class="faq">' + ''.join(f'<details><summary>{h(q)}</summary><p>{h(a)}</p></details>' for q, a in d['faq'] + [(d['near_q'], near_txt(lang))]) + '</div>\n  </article>\n'
    art += (f'  <aside class="fiche" aria-labelledby="fiche-t">\n    <h2 id="fiche-t" class="fiche__t">{h(d["fiche_h"])}</h2>\n    <dl>'
            + ''.join(f'<div><dt>{h(a)}</dt><dd>{h(b)}</dd></div>' for a, b in d['fiche']) + '</dl>\n  </aside>\n</div>\n')
    rest = tpl[tpl.index('<div class="wrap"></div>'):]
    rest = re.sub(r'<div class="cta-bar" id="cta-bar".*?</div>\n?', '', rest, flags=re.S)
    rest = rest.replace(f'/{tslug}/', f'/{SLUG}/')
    # "autres" : colline du Château à la place de la 3e carte
    return head + body + hero + crumbs + art + rest

def near_txt(lang):
    d = C[lang]
    parts = [f'{n} ({t})' for s, n, t in d['near']]
    if lang == 'fr': return 'Dans le guide, les sites les plus proches sont ' + ', '.join(parts[:-1]) + ' et ' + parts[-1] + '.'
    return 'In this guide, the closest places are ' + ', '.join(parts[:-1]) + ' and ' + parts[-1] + '.'

if __name__ == '__main__':
    src = '/home/claude/clicandsite-guide/_photos_brutes/mont-gros-cayambe.jpg'
    for lang, root in (('fr', FR_ROOT), ('en', EN_ROOT)):
        im = ImageOps.fit(Image.open(src).convert('RGB'), (1920, 1280), centering=(0.5, 0.4))
        im.save(f'{root}/assets/photos/{SLUG}.jpg', quality=82, optimize=True, progressive=True)
        for w, hh in ((960, 640), (640, 427)): im.resize((w, hh), Image.LANCZOS).save(f'{root}/assets/photos/{SLUG}-{w}.jpg', quality=80, optimize=True, progressive=True)
        ImageOps.fit(im, (1200, 630), centering=(0.5, 0.35)).save(f'{root}/assets/og/{SLUG}.jpg', quality=82, optimize=True)
        out = f'{root}/{REG[lang]}/{SLUG}/index.html'
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, 'w', encoding='utf-8').write(page(lang))
        print('écrit', out)
