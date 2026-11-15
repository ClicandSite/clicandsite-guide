import re, sys, html
sys.path.insert(0, '/tmp/g')
from rando_gen import fr_typo
N = {
'mont-gros': ('Mont Gros à Nice : randonnée jusqu’à l’Observatoire', 'Boucle de 5 km au mont Gros, à Nice : parc du Vinaigrier, vue sur la baie et coupole de l’Observatoire. Durée, dénivelé, horaires et bus.',
              'Mont Gros hike in Nice: up to the Observatory', 'A 5 km loop up Mont Gros in Nice: Parc du Vinaigrier, bay views and the Observatory dome. Time, climb, opening hours and bus access.'),
'tete-de-chien': ('Tête de Chien (La Turbie) : randonnée vue sur Monaco', 'Tour de la Tête de Chien depuis La Turbie : boucle de 7,5 km au-dessus de Monaco, falaises et vue sur la côte. Durée, dénivelé, bus et conseils.',
              'Tête de Chien hike (La Turbie): view over Monaco', 'The Tête de Chien loop from La Turbie: 7.5 km above Monaco, white cliffs and coast views. Time, climb, bus access and tips.'),
'promenade-le-corbusier': ('Promenade Le Corbusier : sentier du cap Martin', 'Promenade Le Corbusier : 4,7 km au bord de l’eau autour du cap Martin, de gare à gare, jusqu’au cabanon de Le Corbusier. Accès et infos 2026.',
              'Promenade Le Corbusier: Cap Martin coastal path', 'Promenade Le Corbusier: 4.7 km at the water’s edge around Cap Martin, station to station, to Le Corbusier’s cabin. Access and 2026 info.'),
'lac-de-trecolpas': ('Lac de Trécolpas : randonnée depuis le Boréon', 'Lac de Trécolpas (2 150 m) dans le Mercantour : boucle de 8 km depuis le Boréon, bouquetins et chamois. Durée, dénivelé, saison et navette.',
              'Lac de Trécolpas hike from Le Boréon', 'Lac de Trécolpas (2,150 m) in the Mercantour: an 8 km loop from Le Boréon, ibex and chamois. Time, climb, season and shuttle.'),
'val-de-siagne': ('Val de Siagne au Tignet : la randonnée en boucle', 'Circuit du Val de Siagne au Tignet, près de Grasse : boucle de 7 km à l’ombre, au bord de la Siagne. Durée, départ, parking et conseils.',
              'Val de Siagne loop hike at Le Tignet', 'The Val de Siagne loop at Le Tignet near Grasse: a shady 7 km walk along the Siagne river. Time, start, parking and tips.'),
'pic-de-courmettes': ('Pic de Courmettes : randonnée et épave d’avion', 'Pic de Courmettes (1 248 m) au-dessus de Vence : vue sur toute la côte, épave d’avion sur la crête. Distance, dénivelé, départ et conseils.',
              'Pic de Courmettes hike and plane wreck', 'Pic de Courmettes (1,248 m) above Vence: views over the whole coast and a plane wreck on the ridge. Distance, climb, start and tips.'),
'vieil-aspremont': ('Ruines du Vieil Aspremont : randonnée près de Nice', 'Ruines du Vieil Aspremont, village abandonné en 1426 au-dessus de Nice : 3,6 km aller-retour, vue sur le Var et le Mercantour. Infos et conseils.',
              'Vieil Aspremont ruins: a hike near Nice', 'The ruins of Vieil Aspremont, a village abandoned in 1426 above Nice: 3.6 km out and back, views over the Var and the Mercantour.'),
'sentier-nietzsche': ('Sentier Nietzsche : d’Èze-sur-Mer au village d’Èze', 'Sentier Nietzsche : 2,1 km et 400 m de montée entre la gare d’Èze-sur-Mer et le village perché d’Èze. Durée, départ, train et conseils.',
              'Nietzsche Path: Èze-sur-Mer to Èze village', 'The Nietzsche Path: 2.1 km and a 400 m climb from Èze-sur-Mer station to the hilltop village of Èze. Time, start, train and tips.'),
'cascade-de-vescagne': ('Cascade de Vescagne : randonnée au col de Vence', 'Cascade de Vescagne depuis le col de Vence : 5 km aller-retour, ancienne mine de lignite et gué sur la Cagne. Durée, parking et conseils.',
              'Cascade de Vescagne hike from the Col de Vence', 'The Cascade de Vescagne from the Col de Vence: 5 km out and back, an old lignite mine and a ford over the Cagne. Time, parking and tips.'),
'cime-de-la-forna': ('Cime de la Forna : randonnée en boucle à La Turbie', 'Circuit de la cime de la Forna depuis La Turbie : boucle de 6,8 km sur les crêtes, table d’orientation et vue sur Monaco. Durée et accès.',
              'Cime de la Forna loop hike from La Turbie', 'The Cime de la Forna loop from La Turbie: 6.8 km on the ridges, a viewpoint table and views over Monaco. Time, climb and access.'),
'sentier-de-la-brague': ('Sentier de la Brague : de Biot à Valbonne à pied', 'Sentier de la Brague : 10 km faciles à l’ombre au bord de la rivière, de Biot à Valbonne, retour en bus. Durée, départs et conseils.',
              'Brague trail: Biot to Valbonne on foot', 'The Brague trail: an easy, shady 10 km along the river from Biot to Valbonne, back by bus. Time, start points and tips.'),
'sentier-du-cap-ferrat': ('Sentier du littoral du cap Ferrat : le tour à pied', 'Sentier du littoral de Saint-Jean-Cap-Ferrat : tour du cap (4,8 km), pointe Saint-Hospice et plage de la Paloma. Durées, départs et accès.',
              'Cap Ferrat coastal path: walk around the cape', 'The Saint-Jean-Cap-Ferrat coastal path: the cape loop (4.8 km), Pointe Saint-Hospice and Paloma beach. Times, start points and access.'),
'plage-de-la-mala': ('Plage de la Mala à Cap-d’Ail : accès et sentier', 'Plage de la Mala à Cap-d’Ail, crique turquoise près de Monaco : accès par les escaliers ou le sentier du littoral (3,6 km). Gare et parking.',
              'Plage de la Mala (Cap-d’Ail): access and path', 'Plage de la Mala in Cap-d’Ail, a turquoise cove near Monaco: reach it by the steps or the 3.6 km coastal path. Station and parking.'),
}
R = {'fr': ('/home/claude/clicandsite-guide', 'cote-d-azur'), 'en': ('/home/claude/clicandsite-guide-en', 'french-riviera')}
for slug, (tf, df, te, de) in N.items():
    for lang, (root, reg) in R.items():
        p = f'{root}/{reg}/{slug}/index.html'; s = open(p, encoding='utf-8').read()
        nt, nd = (fr_typo(tf), fr_typo(df)) if lang == 'fr' else (te, de)
        assert len(nt) <= 52 and len(nd) <= 156, (slug, lang, len(nt), len(nd))
        ot = html.unescape(re.search(r'<title>(.*?) \| Clic&amp;Site</title>', s).group(1))
        od = html.unescape(re.search(r'name="description" content="(.*?)"', s).group(1))
        for o, n in ((ot, nt), (od, nd)):
            for f in (lambda x: x, lambda x: html.escape(x, quote=True), lambda x: html.escape(x, quote=False)):
                s = s.replace(f(o), f(n))
        assert ot not in s and od not in s
        open(p, 'w', encoding='utf-8').write(s)
print('ok')
