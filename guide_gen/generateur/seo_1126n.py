# Nuit du 26/11/2026 : pages proches de la 1re page (gsc_cibles.md)
import sys; sys.path.insert(0,'/tmp/g'); import retitle as R
FR='/home/claude/clicandsite-guide'; EN='/home/claude/clicandsite-guide-en'
NB=' '
def rep(root,path,old,new):
    f=f'{root}/{path}/index.html'; s=open(f).read()
    assert s.count(old)==1,(path,old[:40]); open(f,'w').write(s.replace(old,new))

# --- Palm Beach Cannes (FR pos 17,5 ; EN 14,4 ; EN « pointe croisette » 6)
R.apply(FR,'cote-d-azur/palm-beach','Palm Beach Cannes : casino Royal Palm, plage, Croisette',
 "Le Palm Beach de Cannes, casino de 1929 rouvert en 2024 à la pointe Croisette : casino Royal Palm (entrée gratuite, majeurs), restaurants, plage, accès.")
R.apply(EN,'french-riviera/palm-beach','Palm Beach Cannes: Royal Palm Casino, Pointe Croisette',
 "Palm Beach in Cannes, the 1929 casino on Pointe Croisette reopened in 2024: Casino Royal Palm (free entry, adults only), restaurants, beach, getting there.",'en')
rep(FR,'cote-d-azur/palm-beach','le casino est réservé aux majeurs avec pièce d’identité.</li>',
 'le casino est réservé aux majeurs avec pièce d’identité.</li><li><strong>Casino Royal Palm</strong> : c’est le nom du casino du Palm Beach (place Franklin-Roosevelt). Entrée gratuite, réservée aux majeurs non interdits de jeux avec une pièce d’identité ; tenue élégante demandée. Ouvert tous les soirs, avec des horaires qui changent selon la saison : vérifiez avant de venir.</li>')
rep(EN,'french-riviera/palm-beach','the casino is adults-only with photo ID.</li>',
 'the casino is adults-only with photo ID.</li><li><strong>Casino Royal Palm</strong>: this is the name of the Palm Beach casino (place Franklin-Roosevelt). Free entry, adults only (photo ID required); smart dress is expected. It opens every evening, with hours that change with the season: check before you go.</li>')
rep(FR,'cote-d-azur/palm-beach','Mis à jour le 12 novembre 2026','Mis à jour le 26 novembre 2026')
rep(EN,'french-riviera/palm-beach','Updated 12 November 2026','Updated 26 November 2026')
R.add_faq(FR,'cote-d-azur/palm-beach','Comment s’appelle le casino du Palm Beach à Cannes ?',
 'Le casino Royal Palm, place Franklin-Roosevelt, à la pointe Croisette. L’entrée est gratuite, réservée aux majeurs avec une pièce d’identité, et une tenue élégante est demandée. Il ouvre le soir, avec des horaires qui varient selon la saison.')
R.add_faq(EN,'french-riviera/palm-beach','What is the casino at Palm Beach Cannes called?',
 'Casino Royal Palm, on place Franklin-Roosevelt at Pointe Croisette. Entry is free for adults with photo ID, and smart dress is expected. It opens in the evening, with hours that vary by season.','en')
R.add_faq(EN,'french-riviera/palm-beach','What is there to see at Pointe Croisette?',
 'The restored Palm Beach and its Art Deco façade, the Port Pierre-Canto marina, beaches, and a panorama from Cap d’Antibes to the Esterel with the Lérins Islands just opposite.','en')

# --- Mont Gros (FR « le mont gros nice » pos 8,8)
R.apply(FR,'cote-d-azur/mont-gros','Mont Gros à Nice : randonnée de 5 km et Observatoire',
 "Le mont Gros à Nice : boucle de 5,2 km (2 h 30, 330 m) depuis Saint-Roch par le parc du Vinaigrier, gratuit. Observatoire en visite guidée, 12 €.")
R.apply(EN,'french-riviera/mont-gros','Mont Gros in Nice: 5 km Hike and the Observatory',
 "Mont Gros in Nice: a 5.2 km loop (2.5 hours, 330 m climb) from Saint-Roch through the free Parc du Vinaigrier. Observatory by guided tour only, €12.",'en')
R.add_faq(FR,'cote-d-azur/mont-gros','Où se trouve le mont Gros à Nice ?',
 'À l’est de Nice : c’est la colline de 375 mètres que couronne la coupole de l’Observatoire. On y monte à pied depuis l’église Saint-Roch, ou en bus avec la ligne 84 des Lignes d’Azur jusqu’à l’arrêt « Sainte-Anne », en haut du parc du Vinaigrier.')
R.add_faq(EN,'french-riviera/mont-gros','Where is Mont Gros in Nice?',
 'On the east side of Nice: it is the 375-metre hill topped by the Observatory dome. Walk up from the Saint-Roch church, or take Lignes d’Azur bus 84 to the “Sainte-Anne” stop at the top of the Parc du Vinaigrier.','en')

# --- Espelette (FR « que voir à espelette » 10,2 ; « combien de temps pour visiter espelette » 17,7)
R.apply(FR,'pays-basque/espelette','Espelette : que voir en 2 heures, piment et marché',
 "Que voir à Espelette : façades aux piments, château des Barons, église Saint-Étienne. Comptez 2 heures ; marché le mercredi matin, fête du piment fin octobre.")
R.apply(EN,'basque-country/espelette','Espelette: What to See in 2 Hours, Peppers, Market',
 "What to see in Espelette: pepper-hung house fronts, the Château des Barons, Saint-Étienne church. Allow 2 hours; market on Wednesday mornings.",'en')
R.add_faq(FR,'pays-basque/espelette','Combien de temps pour visiter Espelette ?',
 'Comptez environ deux heures pour le village : les façades aux piments, le château des Barons (une demi-heure), l’église Saint-Étienne et les boutiques. Prévoyez une demi-journée en enchaînant avec Ainhoa ou Sare, à moins de vingt minutes.',after_first=False)
R.add_faq(FR,'pays-basque/espelette','Que voir à Espelette ?',
 'Les façades décorées de guirlandes de piments (de la fin de l’été à l’automne), le château des Barons d’Ezpeleta avec la mairie et des expositions sur le piment, l’église Saint-Étienne et ses stèles discoïdales, et les boutiques de produits au piment.')
R.add_faq(EN,'basque-country/espelette','How long do you need to visit Espelette?',
 'Allow about two hours for the village: the pepper-hung house fronts, the Château des Barons (half an hour), Saint-Étienne church and the shops. Make it half a day by adding Ainhoa or Sare, less than twenty minutes away.','en',after_first=False)
print('ok')
