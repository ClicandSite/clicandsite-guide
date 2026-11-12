# Région Alsace (marchés de Noël) — édition française (12/11/2026).
# Dates des marchés de Noël 2026 vérifiées le 12/11/2026 : noel.strasbourg.eu (27 nov.-24 déc.)
# et noel-colmar.com (Colmar 23 nov.-29 déc.). Pas de prix, pas d'horaires.

REGION = {
    "slug": "alsace",
    "nom": "Alsace",
    "h1": "Visiter l'Alsace et ses marchés de Noël",
    "de": "d'Alsace",
    "autres": "Autres sites d'Alsace",
    "couleur": "ocre",
    "timbre": "Alsace",
    "photo": "alsace",
    "photo_alt": "Une église fortifiée au milieu des vignes d'Alsace",
    "address_region": "Grand Est",
    "description": "Strasbourg, Colmar : nos guides de l'Alsace pour les marchés de Noël 2026, les vieilles villes à colombages, l'accès en train et quoi réserver.",
    "accroche": "Maisons à colombages, vignobles et vieilles villes illuminées : en décembre, l'Alsace devient la région de Noël par excellence.",
    "intro": [
        "Entre les Vosges et le Rhin, l'Alsace aligne des villes et des villages parmi les mieux conservés de France : la cathédrale et la Petite France à Strasbourg, les canaux de Colmar, les villages fleuris de la route des vins. Chaque guide indique quoi voir, comment y aller et ce qu'il vaut la peine de réserver.",
        "De fin novembre à fin décembre, la région vit au rythme de ses marchés de Noël, dont celui de Strasbourg, organisé depuis 1570. Le train relie facilement Strasbourg, Colmar et la plupart des villages : on peut tout à fait visiter l'Alsace sans voiture.",
    ],
    "departements": ["67", "68"],
}

GROUPES = [
    ("villes", "Villes et marchés de Noël"),
]

VEDETTES = ["strasbourg", "colmar"]

def _d(**k):
    k.setdefault("region", "alsace")
    return k

DESTINATIONS = [
    _d(slug="strasbourg", groupe="villes", nom="Strasbourg", dept="67", cachet="Bas-Rhin", couleur="encre", h1="Strasbourg : marché de Noël, cathédrale et Petite France",
       description="Visiter Strasbourg : le marché de Noël 2026 (27 novembre-24 décembre), la cathédrale, la Petite France, la Neustadt et l'accès en train depuis Paris.",
       accroche="Une cathédrale de grès rose, des quais à colombages et le plus célèbre marché de Noël de France : Strasbourg se visite à pied, en un ou deux jours.",
       intro=[
           "Le centre historique de Strasbourg, la Grande Île, est entouré par les bras de l'Ill. On y passe en quelques minutes de la cathédrale aux maisons de tanneurs de la Petite France, puis aux larges avenues de la Neustadt, le quartier construit à l'époque allemande. L'ensemble est inscrit au patrimoine mondial de l'Unesco.",
           "Pour l'édition 2026, le marché de Noël, le Christkindelsmärik, se tient du 27 novembre au 24 décembre. Les chalets se répartissent sur plusieurs places de la Grande Île, avec le Grand Sapin place Kléber et une patinoire installée dans la cour du palais Rohan.",
       ],
       a_voir=[
           ("La cathédrale Notre-Dame", "Chef-d'œuvre gothique en grès rose des Vosges, avec sa flèche unique et son horloge astronomique. Une plateforme, accessible par un long escalier, offre une vue sur les toits de la ville et, par temps clair, sur la Forêt-Noire."),
           ("La Petite France", "L'ancien quartier des meuniers et des tanneurs, ses maisons à colombages au bord de l'eau et ses ponts tournants. C'est le plus beau coin de la ville pour une promenade à la tombée de la nuit."),
           ("Les Ponts couverts et le barrage Vauban", "Les tours médiévales qui gardaient l'entrée de la ville, puis le barrage Vauban, dont la terrasse sur le toit offre une belle vue sur la Petite France."),
           ("Le Christkindelsmärik et le Grand Sapin", "Le marché historique place Broglie et l'immense sapin décoré de la place Kléber, deux étapes incontournables entre fin novembre et Noël."),
           ("Le palais Rohan", "L'ancienne résidence des princes-évêques, à deux pas de la cathédrale, abrite trois musées : beaux-arts, arts décoratifs et archéologie."),
           ("La Neustadt", "Les grands bâtiments de la place de la République, l'université et les rues de style néo-renaissance et Art nouveau montrent un tout autre visage de Strasbourg."),
       ],
       y_aller=[
           ("En train", "Le TGV relie Paris-Est à Strasbourg en moins de deux heures. De la gare, la cathédrale est à une vingtaine de minutes à pied, ou quelques arrêts en tram."),
           ("En avion", "L'aéroport de Strasbourg-Entzheim est relié à la gare centrale par un train régional. L'EuroAirport Bâle-Mulhouse est une autre option, plus au sud."),
           ("En voiture", "Pendant le marché de Noël, la circulation est très restreinte dans la Grande Île : garez-vous dans un parking-relais P+R en périphérie et finissez en tram."),
       ],
       fiche=[("Marché de Noël 2026", "Du 27 novembre au 24 décembre"), ("Pour qui", "Familles, couples, amateurs de patrimoine"), ("À ne pas manquer", "Cathédrale, Petite France"), ("Accès", "TGV depuis Paris, puis à pied ou en tram")],
       conseils=[
           "Le week-end en décembre, le centre est très fréquenté : visitez les marchés en semaine ou en fin de matinée si vous pouvez.",
           "Montez à la plateforme de la cathédrale en début de journée, puis gardez la Petite France pour la fin d'après-midi, quand les illuminations s'allument.",
           "Réservez votre hébergement très tôt pour les week-ends de l'Avent, ou logez à Colmar ou à Kehl, de l'autre côté du Rhin, reliés par le train et le tram.",
       ],
       activites=[
           ("Visites guidées du marché de Noël", "Balades commentées dans la Grande Île illuminée, avec dégustations de spécialités alsaciennes.", "marché de Noël visite guidée"),
           ("Croisière sur l'Ill", "Une promenade en bateau autour de la Grande Île, de la Petite France au quartier européen.", "croisière bateau"),
       ],
       faq=[
           ("Quand a lieu le marché de Noël de Strasbourg en 2026 ?", "Du vendredi 27 novembre au jeudi 24 décembre 2026, sur plusieurs places de la Grande Île, autour de la cathédrale et de la place Kléber."),
           ("Combien de temps faut-il pour visiter Strasbourg ?", "Une journée suffit pour la cathédrale, la Petite France et les marchés. Comptez deux jours pour ajouter les musées, la Neustadt et une croisière sur l'Ill."),
           ("Peut-on visiter Strasbourg sans voiture ?", "Oui, c'est même conseillé : la ville est à moins de deux heures de Paris en TGV et le centre se parcourt à pied ou en tram."),
       ]),

    _d(slug="colmar", groupe="villes", nom="Colmar", dept="68", cachet="Haut-Rhin", couleur="ocre", h1="Colmar : Petite Venise, vieille ville et marchés de Noël",
       description="Visiter Colmar : la Petite Venise, la maison Pfister, le musée Unterlinden et les 6 marchés de Noël 2026 (23 novembre-29 décembre). Accès en train.",
       accroche="Des canaux bordés de maisons colorées, une vieille ville presque entièrement piétonne et six marchés de Noël : Colmar est la carte postale de l'Alsace.",
       intro=[
           "Colmar est la capitale des vins d'Alsace, au pied des Vosges. Sa vieille ville a traversé les siècles presque intacte : maisons à colombages aux couleurs vives, façades Renaissance, ruelles pavées et le quartier de la Petite Venise, où la Lauch coule entre les maisons de maraîchers.",
           "Pour Noël 2026, la ville installe six marchés de Noël du 23 novembre au 29 décembre, dont un marché dédié aux enfants. Les illuminations mettent en valeur le patrimoine chaque soir, et Colmar sert de point de départ idéal vers les villages de la route des vins.",
       ],
       a_voir=[
           ("La Petite Venise", "Le quartier le plus photographié de Colmar : maisons colorées au bord de la Lauch, vues depuis le pont de la rue de Turenne. Des barques à fond plat y proposent de courtes promenades."),
           ("Le musée Unterlinden", "Installé dans un ancien couvent, il abrite le célèbre retable d'Issenheim, l'un des chefs-d'œuvre de la peinture du début du XVIe siècle."),
           ("La maison Pfister et la maison des Têtes", "Deux façades emblématiques de la Renaissance colmarienne : la première avec sa galerie de bois et ses fresques, la seconde ornée de dizaines de visages sculptés."),
           ("Le Koïfhus et la place de l'Ancienne Douane", "L'ancien bâtiment des douanes, au toit de tuiles vernissées, domine une place animée qui accueille l'un des marchés de Noël."),
           ("Le quartier des Tanneurs", "De hautes maisons à colombages restaurées, aux greniers ouverts où l'on faisait sécher les peaux, à deux pas de la Petite Venise."),
       ],
       y_aller=[
           ("En train", "Colmar est desservie par le TGV depuis Paris et par de fréquents trains régionaux depuis Strasbourg et Mulhouse. La vieille ville est à environ quinze minutes à pied de la gare."),
           ("En avion", "Les aéroports les plus proches sont l'EuroAirport Bâle-Mulhouse et Strasbourg-Entzheim, tous deux reliés à Colmar par la route ou le train."),
           ("Vers les villages", "Pendant la période de Noël, des navettes relient Colmar aux villages voisins comme Eguisheim, Kaysersberg ou Riquewihr : consultez le guide des navettes de l'office de tourisme."),
       ],
       fiche=[("Marchés de Noël 2026", "Du 23 novembre au 29 décembre"), ("Pour qui", "Couples, familles, amateurs de vins"), ("À ne pas manquer", "Petite Venise, retable d'Issenheim"), ("Accès", "TGV ou train régional depuis Strasbourg")],
       conseils=[
           "Le samedi en décembre, la vieille ville est bondée : l'office de tourisme publie un calendrier des affluences prévues, utile pour choisir son jour.",
           "Revenez à la Petite Venise à la nuit tombée : les reflets des illuminations sur l'eau valent la deuxième visite.",
           "Logez à Colmar plutôt qu'à Strasbourg si vous voulez aussi voir les villages de la route des vins : ils sont à quelques kilomètres.",
       ],
       activites=[
           ("Visites guidées de Colmar", "Découverte de la vieille ville et de la Petite Venise avec un guide, de jour ou à la lumière des illuminations.", "visite guidée"),
           ("Route des vins d'Alsace", "Excursions vers Eguisheim, Kaysersberg et Riquewihr, avec dégustation chez un vigneron.", "route des vins d'Alsace excursion"),
       ],
       faq=[
           ("Quand ont lieu les marchés de Noël de Colmar en 2026 ?", "Les six marchés de Noël de Colmar sont ouverts du lundi 23 novembre au mardi 29 décembre 2026, dans la vieille ville."),
           ("Colmar ou Strasbourg pour les marchés de Noël ?", "Strasbourg est plus grande et plus animée, Colmar plus intime et plus proche des villages de la route des vins. À une demi-heure de train l'une de l'autre, les deux se combinent facilement."),
           ("Combien de temps faut-il pour visiter Colmar ?", "Une journée suffit pour la vieille ville, la Petite Venise et le musée Unterlinden. Ajoutez une journée pour les villages voisins."),
       ]),
]

TITRES = {
    "strasbourg": "Strasbourg : marché de Noël 2026, cathédrale, accès",
    "colmar": "Colmar : marchés de Noël 2026, Petite Venise, accès",
}
TITRE_REGION = "Alsace : marchés de Noël 2026, Strasbourg, Colmar"

LIEU_VOIR = {"strasbourg": "à Strasbourg", "colmar": "à Colmar"}
LIEU_ALLER = {"strasbourg": "à Strasbourg", "colmar": "à Colmar"}

GEO = {"strasbourg": (48.5818, 7.7509), "colmar": (48.0772, 7.3570)}

ALIAS = {"strasbourg": ["Strasbourg"], "colmar": ["Colmar"]}
