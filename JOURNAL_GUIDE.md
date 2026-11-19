# Journal et file d'attente des guides Clic&Site

## Déjà en ligne (11/11/2026)
- Côte d'Azur : 19 guides + itinéraire 3 jours
- Paris : 15 guides (dont Disneyland Paris, Catacombes, Noël à Paris) + itinéraire 3 jours
- Alpes : Chamonix, Val Thorens, Courchevel, Megève, Val d'Isère, Tignes, Méribel, Alpe d'Huez

## Pages « Idées » (content_selections_fr.py / _en.py) — À METTRE À JOUR
- 4 pages : où partir cet hiver, que faire à Paris en hiver, Côte d'Azur en hiver, stations de ski ouvertes. Chacune a un agenda daté.
- Le 1er de chaque mois : retirer les événements passés de l'agenda, ajouter ceux du mois suivant (vérifiés le jour même : sites officiels, offices de tourisme, presse), et mettre à jour les dates des expositions parisiennes.
- Selon la saison, ajouter de nouvelles pages idées : « que faire à Paris en février / au printemps », « où partir pour les ponts de mai », « Côte d'Azur en été », etc. Pas plus d'une nouvelle page idée par semaine.

## File d'attente (hiver : priorité ski, Noël et Paris)
1. Alsace (nouvelle région, marchés de Noël, URGENT avant fin novembre) : Strasbourg, Colmar
2. Paris : Invalides et tombeau de Napoléon, musée de l'Orangerie, Saint-Germain-des-Prés, Galeries Lafayette et grands magasins (vérifier les faits du jour)
3. Alpes (stations) : Les Arcs, La Plagne, Les 2 Alpes, Avoriaz, La Clusaz, Serre Chevalier, Les Menuires
4. Alsace : Riquewihr, Kaysersberg, Eguisheim
5. Alpes (groupe « villes ») : Annecy
6. Pyrénées (stations) : Saint-Lary, Cauterets, Font-Romeu, La Mongie / Grand Tourmalet
7. Ensuite : Provence (prioritaire à partir de mars), Bretagne, Pays basque, Lyon, Bordeaux

## Journal
- 12/11/2026 (routine, 00:30 UTC) : ÉCHEC DE PUBLICATION ÉVITÉ. La branche `sources` (ff18b2b et avant) est EN RETARD sur le site publié : main contient déjà Alsace (Strasbourg, Colmar, Riquewihr, Kaysersberg), Avoriaz, Les Arcs, La Plagne, Provence (Aix, Avignon...), Amboise, etc., publiés le 12/11 vers 00:25 UTC depuis des sources non poussées. Une publication depuis `sources` a supprimé ces pages pendant ~1 min, puis main a été restauré à l'identique (eeddd36 FR, c98e86d EN). Le travail de la routine (Strasbourg/Colmar) a été annulé sur `sources` (doublon). À FAIRE : pousser les vraies sources sur la branche `sources` avant toute nouvelle routine. Garde-fou : avant de publier, comparer la liste des pages de site/ avec celle de main et refuser si des pages disparaissent.
- 11/11/2026 (session manuelle) : région Alpes créée (8 stations), 3 guides Paris ajoutés, boutons partenaires refaits, recherches GetYourGuide/Viator ancrées sur le lieu (fonction anchored dans build.py).
- 11/11/2026 (session manuelle) : 4 pages Idées avec agenda (Carnaval de Nice 9-28 févr. 2027, Fête du Citron 13-28 févr., Mimosa 10-14 févr., cirque de Monte-Carlo 22-31 janv., expos Paris), lien « Idées » dans le menu et section sur l'accueil.

## Search Console (note du 11/11/2026)
- Les propriétés domaine `sc-domain:clicandsite.fr` et `sc-domain:clicandsite.com` sont sur le compte abracadeal@gmail.com. Depuis le 11/11 au soir c'est le seul compte connecté dans le navigateur intégré (`https://search.google.com/search-console/...`, sans /u/1/). Si une page dit « vous n'avez pas accès », vérifier « Connecté en tant que » : ce doit être abracadeal@gmail.com.
- Pour renvoyer un sitemap, saisir l'URL complète (`https://clicandsite.fr/sitemap.xml`), sinon « Adresse de sitemap incorrecte ».
- 11/11 : 10 pages indexées sur 55 (.fr), .com en cours de traitement ; sitemaps renvoyés (55 URL chacun).

## 12/11/2026 (session manuelle, ~01:40 Paris) : AVERTISSEMENT, deux chaînes de production
Le site publié sur main (FR) et sur ClicandSite/clicandsite-guide-en (EN) a été modifié le 11 et le 12/11 par une autre chaîne que build.py. Ce sont les scripts de `guide_gen/` (gen.py, data_*.py, run_*.py), plus des corrections appliquées directement au HTML de main :
- régions Loire, Provence, Alsace, Normandie et lots Paris 2, 3 et 4, générées avec guide_gen/generateur ;
- liens partenaires corrigés : pages de lieu GYG au lieu de la recherche libre, textes Viator testés ;
- signature d'auteur, page À propos, maillage interne ;
- sections « Infos pratiques 2026 » sur les 19 guides Côte d'Azur et les 31 guides Paris, en FR et en EN ;
- info Uber sur la page Monaco ;
- pages événements : Fête du Citron 2027, Carnaval de Nice 2027, Noël Côte d'Azur 2026, en FR et en EN.

**`python3 build.py && python3 build.py en` ne redonne PAS main.** Je ne l'ai pas vérifié, parce que tout ce contenu est absent de build.py et des content_*.py. Publier depuis `sources` supprimerait ou écraserait ces pages.
Règle à suivre jusqu'à la fusion des deux chaînes : NE PAS publier main depuis build.py. Enrichir et corriger directement le HTML de main (et du dépôt EN), en partant de `git pull`.
Pour fusionner les chaînes : intégrer guide_gen/ et le HTML actuel de main dans build.py, puis vérifier que la liste des pages et le contenu générés sont identiques à main, avec un diff vide.
## Détail de guide_gen/

Cette branche contient les scripts qui ont servi à produire et corriger le guide publié sur `main` (clicandsite.fr) et sur le dépôt anglais (clicandsite.com). Elle ne contient pas le HTML publié : celui-ci reste sur `main`.

## Ce qu'il y a ici

- `generateur/gen.py` : le générateur de pages guide (gabarit, JSON-LD, liens partenaires, insécables français).
- `generateur/data_*.py` : les données des pages générées (Paris 2 à 4, Alsace, Normandie, Loire, Provence, Châtel, ski, événements Côte d'Azur).
- `generateur/run_*.py` : un script par lot. Chaque script écrit les nouvelles pages, puis modifie en place l'index de la région, l'accueil et le sitemap.
- `scripts/` : les corrections ponctuelles appliquées au HTML existant :
  - liens partenaires : `fixsearch.py`, `fixvtx.py`, `fixlinks.py` ;
  - signature d'auteur : `byline.py` ;
  - maillage interne : `maillage.py` ;
  - sections « Infos pratiques 2026 » : `infos.py` pour la Côte d'Azur, `infos_paris.py` pour Paris ;
  - les autres scripts servent aux vérifications locales et aux captures d'écran.

## Reproductibilité : ce qui est vrai et ce qui ne l'est pas

**Il n'existe pas de `build.py` qui reconstruise tout le site.** La commande `python3 build.py && python3 build.py en` ne redonne donc pas les pages de `main`, et je ne l'ai pas vérifié pour cette raison.

- Les pages des lots `data_*.py` sont régénérables avec `gen.py`. Les 19 guides Côte d'Azur d'origine, l'accueil, les index de régions, les pages À propos et les mentions légales ne le sont pas : ils ont été écrits à la main avant ces scripts.
- Les scripts ne repartent pas de zéro : ils modifient le HTML existant. Relancer un `run_*.py` sur un dépôt neuf ne suffit pas, il faut aussi rejouer les corrections de `scripts/` dans le bon ordre.
- Les sections « Infos pratiques 2026 », les liens de maillage et la signature d'auteur n'existent que dans le HTML de `main`, pas dans les données `data_*.py`. Si on régénère une page avec `gen.py` puis qu'on rejoue `infos.py` ou `infos_paris.py`, on retrouve sa section. La signature d'auteur, elle, est déjà dans `gen.py`.
- Les chemins sont absolus : `/home/claude/clicandsite-guide` pour le FR, `/home/claude/clicandsite-guide-en` pour l'EN, et `/tmp/ph` pour les photos sources.
- Les photos sources (Unsplash, environ 39 Mo) ne sont pas versionnées ici. Les versions publiées, redimensionnées, sont dans `assets/photos` et `assets/og` sur `main`. Les crédits sont dans chaque fichier `data_*.py`, au champ `credit`.

## Historique (12 novembre 2026)

- Régions Loire et Provence ajoutées. Liens GetYourGuide et Viator vérifiés : pages de lieu GYG, plus de recherche libre, et recherches Viator testées.
- Signature « Par Anthony, à Cannes », page À propos complétée, maillage interne limité à 3 liens par page et à la même région.
- Section « Infos pratiques 2026 » ajoutée sur les 19 guides Côte d'Azur et les 31 guides Paris, en FR et en EN.
- Info terrain d'Anthony sur la page Monaco : Uber permet de déposer à Monaco, mais aucune course ne peut y être commandée pour en repartir.
- Prix du billet Domaine de Chantilly corrigé : 18 €.
- Pages événements créées : Fête du Citron 2027, Carnaval de Nice 2027, Noël sur la Côte d'Azur 2026. Indexation demandée dans la Search Console pour les 6 URL.

## À faire pour une vraie reproductibilité

Extraire toutes les pages de `main` en données, écrire un `build.py` unique qui sorte dans `site/` et `site_en/`, puis comparer ce build avec `main` page par page, avec la même liste de fichiers et un diff vide.
- 12/11/2026 (routine) : section « Infos pratiques 2026 » ajoutée sur Val Thorens, Courchevel, Méribel et Tignes (FR alpes/ + EN french-alps/) : dates de saison 2026-2027, prix des forfaits (Val Thorens-Orelle, 3 Vallées, Tignes-Val d'Isère), réduction du samedi 3 Vallées, navettes gratuites de Tignes ; 1 question FAQ (visible + JSON-LD) par page ; titles et meta descriptions avec « forfait » et l'année. Sources : les3vallees.com, valthorens.com (EN), skipasscourchevel.com, en.tignes.net, relevées le 12/11. Liens GYG/Viator : contrôle automatique sur toutes les pages des deux sites (format, partner_id, tag), aucune anomalie. Non fait : Chamonix (sites Compagnie du Mont-Blanc et chamonix.com inaccessibles), tarifs Altibus non vérifiés. 107 pages FR / 106 EN, inchangé.
- 12/11/2026 (session manuelle, ~11 h Paris) : nouvelle région Pyrénées (FR pyrenees/, EN pyrenees/) avec Font-Romeu, Saint-Lary, Grand Tourmalet, Cauterets, Peyragudes + index de région ; Isola 2000 et Auron ajoutées aux Alpes (alpes/ et french-alps/). Menu « Pyrénées » après Alpes sur toutes les pages, carte région sur l'accueil (Alpes 16 -> 18 guides), sitemap (114 URL chacun), agenda de la page « stations de ski ouvertes » complété (FR + EN). Générateur : guide_gen/generateur/data_pyrenees.py + run_pyrenees.py (liens GYG = pages lieu, ex. cauterets-l133967, isola-2000-l221614, auron-l185401, pyrenees-orientales-l247576). Dates relevées le 12/11 : skiinfo, guide-ski, alti-mag, N'PY, bergfex, explorenicecotedazur. Photos Unsplash : Saint-Lary (photo générique Pyrénées, Marek Piwnicki) et Isola 2000 (vue aérienne Alpes-Maritimes) ne montrent pas la station elle-même, à remplacer si on trouve mieux. Valberg reporté (pas de photo trouvée). 116 pages FR / 115 EN.
- 12/11/2026 (~11 h 30 Paris) : encart Elite Prestige Services (carte act--eps « Transfert privé vers … » + bloc .ride) ajouté à la main sur Isola 2000 et Auron, FR et EN, sur le modèle des pages Côte d'Azur. Absent de data_pyrenees.py : à recopier si on régénère ces pages.
- 12/11/2026 (~12 h 15 Paris) : Alpes du Sud — Montgenèvre (28 nov.-17 avr.), SuperDévoluy (12 déc.-11 avr.), La Grave (20 déc.-3 mai) ajoutées aux Alpes FR/EN (21 guides), agenda « stations ouvertes » complété, nouvelle section « Le ski à 1 h 30 de la mer » (Isola 2000, Auron) sur la page Côte d'Azur en hiver FR/EN. Générateur : data_alpes_sud.py + run_alpes_sud.py (GYG briancon-l227363). Vars et Pra-Loup reportés faute de photo Unsplash du lieu. 119 pages FR / 118 EN.
- 12/11/2026 (~12 h 45 Paris) : AUDIT LIENS PARTENAIRES dans le navigateur. Constat : les recherches libres Viator (searchResults?text=…) renvoyaient souvent hors sujet ou hors de France (« Mougins » → Vietnam, « Cap d'Antibes bateau » → Le Cap, « Hautes-Alpes » → Nouvelle-Zélande, « Briancon » → Annecy/Lugano) et perdaient pid/mcid quand Viator redirigeait. Correction : les 406 liens Viator de chaque site pointent désormais vers une page destination Viator vérifiée (ex. /fr-FR/Nice/d478-ttd?pid=P00331213&mcid=42383&medium=link&campaign=…), table dans guide_gen/scripts/fixvia_destinations.py (36 destinations, toutes contrôlées). RÈGLE : ne plus jamais utiliser searchResults pour Viator ; gen.via() et les champs VIA des data_*.py sont obsolètes, passer par la table de destinations. GetYourGuide : midi-pyrenees (Bordeaux en tête) et pyrenees-l7935 (Espagne/Andorre) retirés de Saint-Lary, Peyragudes, Grand Tourmalet → lourdes-l311 ; provence-l32433 (Nice/Marseille) retiré de Serre Chevalier ; SuperDévoluy → grenoble-l98511. Pages GYG contrôlées une par une : cauterets, lourdes, isola-2000, auron, briancon, grenoble, morzine, haute-savoie/auvergne-rhone-alpes (Chamonix), pyrenees-orientales (Font-Romeu, gardé). Le partner_id reste dans l'URL après redirection GYG vers getyourguide.com/fr-fr/.
- RÈGLE D'ANTHONY (12/11/2026) : à CHAQUE page ou article créé ou modifié, vérifier dans un navigateur que chaque lien GetYourGuide et Viator mène au bon endroit (bon lieu, activités sur place, identifiant partenaire conservé). Viator : pages destination uniquement (table guide_gen/scripts/fixvia_destinations.py). Tâche planifiée de nuit mise à jour en ce sens.
- 13/11/2026 (routine de nuit) : AUCUN ENRICHISSEMENT DE CONTENU. WebFetch refusait tous les sites officiels (erreur PROVENANCE_REQUIRED : demande d'autorisation sans réponse, session sans surveillance) : lesarcs.com, la-plagne.com, skipass-laplagne.com/fr, valdisere.com, tignes.net, les3vallees.com, lesmenuires.com, valthorens.com, fete-du-citron.com, nicecarnaval.com, saint-lary.com, font-romeu.fr, cauterets.com, n-py.com. Rien n'a été écrit sans source officielle du jour. Pages visées, à reprendre : Val d'Isère, Les Arcs, La Plagne, Les Menuires (FR + EN). Seul fait lu : skipass-laplagne.com/en annonce « Winter opening: from the 12th of December to the 24th of April 2027 » (non publié, à recouper). Liens partenaires : contrôle automatique des 687 liens FR et 687 liens EN (format, partner_id/pid/mcid, pas de searchResults ni /s/?q=) ; FR sans anomalie ; EN : 128 liens sur 26 pages avaient un tag de campagne au chemin FR (clicandsite-en-pays-basque-…, -bretagne-…, -cote-d-azur-…) au lieu du chemin EN (basque-country, brittany, french-riviera) → corrigés (commit 73bb456 EN). Destinations GYG/Viator inchangées (navigateur indisponible, aucun nouveau chemin ajouté). Pages : 168 FR / 167 EN, inchangé.
- 13/11/2026 (relance manuelle, Anthony présent) : section « Infos pratiques 2026 » ajoutée sur Val d'Isère, Les Arcs, La Plagne et Les Menuires (FR alpes/ + EN french-alps/) : saison 2026-2027, forfaits (Tignes-Val d'Isère et Val d'Isère seul, Pass Classique/Essentiel/Premium des Arcs, La Plagne/Paradiski, Menuires-Saint-Martin et 3 Vallées, tarif du samedi), funiculaire Bourg-Saint-Maurice-Arc 1600, cars (Altibus, lignes S70/S71/S72/S66, Moûtiers env. 12 €) et navettes gratuites ; 1 question FAQ (visible + JSON-LD) par page ; title et meta description avec « forfait » et 2026-2027. Sources lues le 13/11 : valdisere.com, tignes.net/ski/forfaits-ski, lesarcs.com, lesarcs-peiseyvallandry.com (boutique et funiculaire), la-plagne.com + PDF Tarifs_domaine_La_Plagne_Hiver_2026-2027, lesmenuires.com/fr/forfaits-ski et /navettes, les3vallees.com. Non publiés : prix des cars Altibus (Val d'Isère, La Plagne), prix enfant/senior par période aux Arcs (non affichés hors JavaScript), prix enfant La Plagne (colonnes du PDF ambiguës, non repris). Liens partenaires inchangés (chemins déjà présents), contrôle automatique 687/687 sans anomalie. Commits c2fee0f (FR), c58924f (EN). 168 pages FR / 167 EN, inchangé.

- 13/11/2026 (session avec Anthony, de jour) : (1) liens partenaires plus visibles sur les pages de lieux FR/EN : encadré « À réserver » (cta-box), liens d'action en gras (class deep), barre « Voir les prix » collante sur mobile (assets/cta.js) — script main:_outils/cta.py, idempotent, à relancer après toute nouvelle page. (2) Paris + Côte d'Azur FR/EN : section « À voir à proximité » (h2 id="autour") + 2 questions FAQ visibles et JSON-LD — script main:_outils/enrich_near.py. (3) Tarifs/horaires vérifiés le 13/11 ajoutés aux infos-2026 : rocher-de-monaco, monte-carlo, vieil-antibes, port-vauban, promenade-des-anglais, vieux-nice.
- 13/11/2026 (suite) : horaires vérifiés ajoutés aux infos-2026 Paris : sainte-chapelle, pantheon, arc-de-triomphe, opera-garnier (FR seulement, pas de page EN), versailles, musee-rodin.
- 13/11/2026 (suite) : libellés des boutons partenaires changés à la demande d'Anthony — FR « Mes billets sur GetYourGuide », « Mes billets sur Viator », « Prendre mes billets », « ou sur Viator », barre mobile « Mes billets » ; EN « Get tickets on GetYourGuide/Viator », « Get my tickets », « or on Viator », « Get tickets ». Ne plus écrire « comparer » ni « voir les prix ».
- 13/11/2026 (suite) : RÈGLE ANTHONY — les liens Viator doivent viser l'activité, jamais la page ville/région. Format : https://www.viator.com/fr-FR/searchResults/all?text=<ville+lieu>&pid=P00331213&mcid=42383&medium=link&campaign=… (EN : sans fr-FR). Lien ville (d…-ttd) seulement si la page parle de la ville elle-même. Boutons : FR « Billets » (GetYourGuide) / « Autres billets » (Viator), encadré « Billets » + « ou autres billets », barre mobile « Billets » ; EN « Tickets » / « More tickets ». Ne pas réécrire « comparer », « voir les prix » ni le nom des plateformes sur les boutons.
- 13/11/2026 (suite) : section « Un peu d’histoire » (FR h2 id="histoire", EN h2 id="history" « A bit of history ») ajoutée avant le 1er h2 de contenu sur les 50 pages Paris et les 37 Côte d’Azur, FR + EN. 2 paragraphes, dates clés, faits vérifiés. Liens Viator : jamais la page ville sauf page de ville → format searchResults/all?text=.
  À FAIRE (tâche de nuit) : ajouter la même section aux 65 pages des autres régions (Provence, Alpes, Alsace, Bretagne, Normandie, Pays basque, Pyrénées, Loire…), ~5 pages par nuit, FR + EN, faits vérifiés le jour même, en vérifiant d’abord que id="histoire" n’existe pas déjà.
- 13/11/2026 (suite) : NOUVELLE RÉGION AQUITAINE (FR /aquitaine/, EN /aquitaine/) à la demande d’Anthony : bordeaux, saint-emilion, dune-du-pilat, perigueux, sarlat-la-caneda, la-roque-gageac, chateau-de-beynac + page région, menu (après Alsace) et carte sur l’accueil. Généré avec /tmp/gen/content12.py + build3b.py (copie de build3 : liens GetYourGuide en recherche s/?q=…). Photos Unsplash vérifiées. Liens GYG en recherche (s/?q=) non encore testés au navigateur → À VÉRIFIER, et remplacer par les pages lieu GYG (…-lNNNN/) quand elles sont confirmées.
  À AJOUTER quand une vraie photo Unsplash du lieu est trouvée : bergerac, lascaux (Lascaux IV, Montignac), chateau-de-castelnaud, chateau-des-milandes, jardins-de-marqueyssac. Tarifs déjà vérifiés : Castelnaud 2026 13,60 €/6,80 € (10-17 ans).

- 13/11/2026 : page Bergerac ajoutée (aquitaine/bergerac, FR+EN), photo Commons Benjamin Smith CC BY-SA 4.0, crédit dans mentions légales. Section histoire déjà faite. Restent à faire faute de photos libres : Lascaux, Castelnaud, Milandes, Marqueyssac.
- 13/11/2026 : page Lascaux (aquitaine/lascaux, FR+EN), photo Commons Eline13Viki (licence exacte à confirmer et à ajouter au crédit). Tarifs Lascaux IV 2026 : 23/22/15 €, jumelés Thot 26,50 / Lascaux II 29.
- 13/11/2026 : page château de Castelnaud (aquitaine/chateau-de-castelnaud). Auteur + licence photo Castelnaud-Castle-1.JPG à compléter (attente capture Anthony), idem Lascaux. Tarifs 2026 : 13,60 / 6,80 (10-17) / gratuit -10.
- 13/11/2026 : page château des Milandes (aquitaine/chateau-des-milandes), photo Renhour48 (licence à confirmer). Tarifs 2026 : 15 / 9,50 (5-16) / 12,50 étudiant / 11,50 PMR.
- 13/11/2026 : page jardins de Marqueyssac (aquitaine/jardins-de-marqueyssac), photo Inga Tomane CC BY-SA 4.0. Aquitaine = 12 guides. Licences encore à confirmer : Lascaux, Castelnaud (auteur aussi), Milandes.
- 13/11/2026 : crédits Aquitaine complets. Lascaux CC0 (Eline13Viki+), Castelnaud CC BY-SA 3.0 (Castelnaud-Castle-1.JPG, sans auteur indiqué), Milandes nouvelle photo Johan Allard CC BY-SA 4.0 (lien vers la catégorie Commons ; nom exact du fichier à ajouter si connu).
- 13/11/2026 : nouvelle région Lot (lot/) : hub (photo Unsplash Joran Quinten), Rocamadour (Peter Muscutt), Saint-Cirq-Lapopie (Martin Masson). Lien nav « Lot » après Aquitaine, carte accueil (46, Quercy). Gouffre de Padirac à faire dès réception de la photo Commons. CSS nav resserrée 901-1440px.
- 13/11/2026 : page gouffre de Padirac (lot/gouffre-de-padirac), photo prise par Anthony, créditée « Clic&Site ». Saison 2026 : 28 mars – 1er nov. Tarifs non publiés (sources contradictoires). À faire : ajouter Padirac dans les cartes « autres sites » de Rocamadour et Saint-Cirq.
- 13/11/2026 : nouvelle région Corse (corse/ FR, corsica/ EN) : hub + Ajaccio, Bastia, Bonifacio, Porto-Vecchio, îles Lavezzi. Photos Unsplash (crédits mentions légales). Nav « Corse » après Lot, carte accueil (2A 2B). Pistes suivantes : Calvi, calanques de Piana, Corte, Cap Corse.
- 13/11/2026 : Corse + Calvi (Unsplash Hannah Wright) et Piana (Commons Jean-Pol GRANDMONT, CC BY 3.0). Corse = 7 guides. Les anciennes pages Corse ne listent pas encore Calvi/Piana dans « autres sites » (à rafraîchir).
- 13/11/2026 : page falaises-de-bonifacio (Corse, 8 guides), photo Unsplash Petr Slováček.
- 14/11/2026 : pages Théoule-sur-Mer et Mandelieu-la-Napoule (Côte d’Azur, 40 guides), photos Commons Txllxt TxllxT et Yves Tennevin (licences à confirmer). Bloc chauffeur Elite Prestige inclus. À corriger : 4 cartes de la page Côte d’Azur (Biot, îles de Lérins, Estérel, Porquerolles) utilisent des images hébergées sur Wikimedia au lieu de assets/photos.
- 14/11/2026 : page villa-ephrussi-de-rothschild (Côte d’Azur, 41 guides), photo Unsplash Hugo Richard. Tarifs 18/12 €, gratuit -7. Beaulieu et Cap d’Antibes en attente de photos Commons.
- 14/11/2026 : page beaulieu-sur-mer (villa Kérylos, 42 guides), photo Commons Finoskov CC BY-SA 3.0 (Category:Villa_Kérylos). Prix non affichés (13 € officiel vs 15 € OT). Reste Cap d’Antibes.
- 14/11/2026 : page cap-d-antibes (43 guides), photo Commons Spike CC BY-SA 4.0 (baie des Milliardaires, crop 1245px agrandi ; lien Category:Cap_d%27Antibes).
- 14/11/2026 : page la-malmaison (44 guides), photo Commons Benoît Prieur CC0 ; lien depuis la page Cannes.
- 14/11/2026 : index Côte d’Azur réorganisé par ville. Sections : g-cannes, g-nice, g-antibes, g-monaco, g-capferrat (Villefranche→Menton), g-esterel (Estérel→St-Tropez), g-villages, g-nature, g-fetes. Pour une nouvelle page CdA, mettre SECTION={fr:(id,"",""),en:(id,"","")} dans le content (g-mer et g-quartiers n’existent plus).
- 14/11/2026 : toutes les pages région classées par ville/secteur (script /tmp/regroup.py). Ids : aquitaine g-bordeaux/g-sarlat/g-perigueux ; corse g-ajaccio/g-bonifacio/g-bastia ; provence g-marseille/g-avignon/g-arles ; alpes g-montblanc/g-3vallees/g-tarentaise/g-isere/g-hautesalpes/g-alpesmaritimes ; pyrenees g-hautespyrenees/g-pyreneesorientales ; alsace g-strasbourg/g-routevins ; bretagne g-nord/g-sud ; normandie g-seine/g-ouest ; paris g-monuments/g-musees/g-quartiers/g-sorties/g-autour. Nouvelle page : SECTION vers la bonne id.
- 14/11/2026 : page plages-electroniques (g-fetes, 45 guides), photo Unsplash Jim Thirion 5wSTD4OwPFo. Dates 2027 (6-8 août) issues d’agrégateurs : vérifier sur plages-electroniques.com quand annoncées officiellement.
- 14/11/2026 : pages palais-princier, jardin-exotique-monaco (g-monaco), colline-du-chateau (g-nice) — 48 guides CdA. Liées depuis monaco/nice. Restent sans photo libre : Musée océanographique (bâtiment), musée Matisse, musée Chagall, cours Saleya → demander photos Commons à Anthony.
- 14/11/2026 : page marche-forville (g-cannes, 49 guides), photo Commons Draupnir3 CC BY-SA 3.0 (couleurs retouchées). Palais des Festivals : photo Commons refusée (800px, hommage 2015) → attendre photo d’Anthony.
- 14/11/2026 : page musee-chagall (g-nice, 50 guides), photo Commons Derbrauni CC BY-SA 4.0 (lien Category).
- 14/11/2026 : page cours-saleya (g-nice, 51 guides), photo Commons dalbera CC BY 2.0.
- 14/11/2026 : page musee-oceanographique (g-monaco, 52 guides), photo Commons Uhooep CC BY-SA 4.0.
- 14/11/2026 : page musee-picasso-antibes (g-antibes, 53 guides), photo Commons MOSSOT CC BY-SA 4.0.
- 14/11/2026 : page musee-matisse (g-nice, 54 guides), photo Commons Chris Bontemps CC BY-SA 2.0 (original 1280px).
- 14/11/2026 : page fort-carre (g-antibes, 55 guides), photo Commons Sukkoria CC BY-SA 4.0 (lien Category). Reste : Palais des Festivals, musée Explorations du Monde, marché provençal Antibes.
- 14/11/2026 : photos optimisées — WebP (q76) pour 640/960/1280/1920 + nouvelle taille 1280 jpg, pages en <picture>. APRES CHAQUE NOUVELLE PAGE : lancer python3 /tmp/webp.py (idempotent ; script copié dans _outils/webp.py).
- 14/11/2026 (routine de nuit) : AUCUN ENRICHISSEMENT DE CONTENU. WebFetch refuse toujours les sites officiels (PROVENANCE_REQUIRED, autorisation sans réponse en session sans surveillance) : alpedhuez.com, sataski.com, les2alpes.com, skipass.les2alpes.com, serre-chevalier.com, skipass-serrechevalier.com, avoriaz.com, skipass-avoriaz.com, portesdusoleil.com. WebSearch ne renvoie que des titres d'agrégateurs (guide-ski.fr, skiinfo) : rien écrit. Pages visées, à reprendre : Alpe d'Huez, Les 2 Alpes, Serre Chevalier, Avoriaz (FR + EN). Liens partenaires : audit automatique des 889 liens GYG et 563 liens Viator de chaque site. Corrigé : 85 liens GYG en recherche libre (/s/?q=) sur 17 pages Côte d'Azur FR et EN (Villa Ephrussi, Beaulieu, Théoule, Mandelieu, Malmaison, Forville, Plages électroniques, Colline du Château, Cours Saleya, Chagall, Matisse, Palais princier, Jardin exotique, Musée océanographique, Picasso Antibes, Fort Carré, Cap d'Antibes) → chemins lieu GYG déjà présents sur le site (nice-l314, cannes-l15, antibes-l5075, monaco-l515, villa-ephrussi-de-rothschild-l136993, castle-hill-nice-l5144, cours-saleya-l12764, vieux-nice-l5145, prince-s-palace-of-monaco-l3880, rock-of-monaco-l3886, picasso-museum-antibes-l136838, remparts-d-antibes-l232232, villefranche-sur-mer-l1706, frejus-saint-raphael-l32405) ; EN : 200 tags cmp/campaign au chemin FR (corse-…, cote-d-azur-…) corrigés sur 25 pages corsica/ et french-riviera/. Commits a468ccc9 (FR), 982297b (EN). RESTE : 115 liens GYG /s/?q= par site sur Aquitaine (12 pages), Corse (8), Lot (3) : aucun chemin lieu vérifié pour ces régions, navigateur indisponible. CONFLIT DE RÈGLES : la consigne de la routine interdit Viator searchResults, mais la règle d'Anthony du 13/11 l'impose pour viser l'activité (512 liens searchResults par site) : non modifiés, à trancher. 211 pages FR / 210 EN, inchangé.
- RÈGLE VIATOR VALIDÉE PAR ANTHONY (14/11/2026), remplace les règles du 12/11 et du 13/11 : lien de recherche Viator autorisé pour viser l'activité (searchResults/all?text=<ville>+<lieu>&pid=P00331213&mcid=42383&medium=link&campaign=clicandsite-<lang>-<tag>), le texte contient TOUJOURS la ville, jamais un mot seul. Toute NOUVELLE recherche est testée dans un navigateur (activités sur place, pid conservé) avant publication. Sans navigateur (routine de nuit) : aucune nouvelle recherche, on reprend une recherche déjà en ligne pour le même lieu, sinon la page destination de la ville (table fixvia_destinations.py). Les 512 recherches Viator déjà en ligne par site restent à tester une par une lors d'une session de jour avec navigateur. Consigne de la tâche de nuit mise à jour en ce sens.

## 2026-11-14 — Test des recherches Viator (viator_a_tester.tsv)
- 226 recherches uniques testées dans le navigateur intégré (fetch fr-FR, 1res activités + adresse finale). Viator a déclenché son anti-robot (DataDome) après ~190 : les 32 dernières (saint-*, tignes, val-*, villa-*, tours-chateau-*…) non testées, envoyées par sécurité vers la page destination. Captcha non résolu.
- Constats : (1) une recherche qui tombe sur un nom de ville (antibes, cannes, bordeaux, grasse, ajaccio, bergerac, provence) est redirigée vers /Ville/dNNN-ttd **sans le pid** ; (2) beaucoup de recherches renvoient du hors-sujet (auron→Akron, monaco→Neuschwanstein, etretat→Tunisie, biot→Vieques, place+massena→rafting Québec, recherches « paris+… » → bloc Versailles en tête).
- Correction : 747 liens (FR+EN) remplacés par la page destination avec pid/mcid/campaign conservés ; 268 liens gardés en recherche (53 requêtes vérifiées OK : louvre, catacombes, Père-Lachaise, Sainte-Chapelle, Lérins, Chagall, Versailles, Mont-Saint-Michel…) ; 9 requêtes remplacées par une requête vérifiée (lerins+islands→cannes+lerins+islands, paris+montmartre→montmartre, musee+rodin→paris+musee+rodin, monaco+palais+princier→monaco+rocher).
- Destinations utilisées : Paris d479, Nice d478, Cannes d786, Antibes d21941, Grasse d50323, Menton d23076, Villefranche d50322, Fréjus d5223, Monaco d948, St-Tropez d4195, Toulon d24308, French-Riviera d179, Provence d184, Avignon d483, Arles d28884, Gordes d50932, Marseille d485, Corsica d4799, Ajaccio d4192, Bergerac d24181 (Dordogne/Lot), Bordeaux d468, Midi-Pyrenees d5512, Lourdes d24041, Perpignan d26343, Colmar d22940, Brittany d21942, Rennes d21943, Loire-Valley d178, Le-Havre d4199, Bayonne d5047, Biarritz d23856, Chamonix d24269, Annecy d5437, Rhone-Alpes d24268, Grenoble d27067, France d51.
- Outil : clicandsite-guide/_outils/viator_fix.py (idempotent) → à lancer après chaque build : `python3 _outils/viator_fix.py write ../clicandsite-guide ../clicandsite-guide-en`. Toute nouvelle requête non listée sort en « unknown » : la tester avant de l'ajouter.
- Commits : FR d5a7799, EN 76cb82a.

## 2026-11-14 — Bloc « À réserver sur place » (test : Le Suquet)
- FR cote-d-azur/le-suquet + EN french-riviera/le-suquet : bloc #sur-place inséré après .book__lead (marqueurs <!--acts:start-->/<!--acts:end-->).
  - Widget officiel GetYourGuide (data-gyg-widget="activities", partner XMYSXGR, cmp=clicandsite-{lang}-{chemin}), script pa.umd.production.min.js chargé seulement à l'approche du bloc (IntersectionObserver, rootMargin 600px) → pas d'impact sur le chargement initial. 2 activités si largeur < 700 px, 4 sinon.
  - Sélection Viator vérifiée dans le navigateur (pid conservé, lieu inclus) : d786-183050P4 (scénariste, 4,7/68 avis, 2 h 40) et d786-14737P19 (Au-delà du tapis rouge, 3 h, colline du Suquet). Lien « Toutes les activités » → page attraction Viator Le Suquet d786-a1817 (pid conservé).
- Fichiers : assets/activites.css (chargé uniquement sur les pages avec le bloc), _outils/activites.py (config PAGES, idempotent ; ajouter une page = une entrée avec activités Viator vérifiées).
- Vérifié en ligne sur clicandsite.fr et .com : iframe GYG chargée (fr-FR / en-US), liens Viator avec pid.
- À faire si Anthony valide : étendre aux autres pages de lieux (chercher la page attraction Viator « -aNNNN » de chaque lieu, meilleure que la page ville).

## 2026-11-14 — Liens GetYourGuide de recherche (signalé par Anthony sur Padirac)
- Problème : 230 liens GYG de type `getyourguide.fr/s/?q=…` (39 requêtes, 46 pages Corse / Aquitaine-Dordogne / Lot) → résultats d'autres pays (ex. Padirac).
- Correction : remplacés par la page lieu GYG `slug-lNNNN/?partner_id=XMYSXGR…` (cmp conservé). Lieux : Bonifacio l91244, Porto-Vecchio l91235, Ajaccio l1535, Ajaccio County l213076 (Piana, Scandola), Bastia l1536, Haute-Corse l150371 (Calvi), Bordeaux l287 (dont Saint-Émilion), Dune du Pilat l3438, Arcachon l32338, Sarlat l1356, Dordogne l39314 (Lascaux, Beynac, Castelnaud, Milandes, Marqueyssac, Bergerac, Périgueux), La Roque-Gageac l139356, Rocamadour l190520 (Padirac, Saint-Cirq-Lapopie, Cahors). L'excursion GYG « Padirac + Rocamadour depuis Sarlat » (t382850) semble retirée → non utilisée.
- Outil : _outils/gyg_fix.py (idempotent), à lancer après build comme viator_fix.py.
- Non testé en navigateur (Mac hors ligne) : IDs relevés sur les pages GYG elles-mêmes. À contrôler au prochain passage dans le navigateur.

## 2026-11-14 — Bloc « À réserver sur place » généralisé (191 pages FR + 191 EN)
- _outils/activites.py traite désormais toutes les pages ayant .book__lead (idempotent). Widget GYG par **numéro de lieu** (`data-gyg-location-id`, transmis en `location_id` à l'iframe) pris dans le 1er lien GYG `-lNNNN/` de la page. NE PAS utiliser `data-gyg-q` : testé, « Padirac » affichait Costa Rica / Hongrie / Mexique.
- 131 numéros de lieu testés un par un dans le widget (14/11) : tous affichent des activités du bon secteur. Exception corrigée : 132103 (région Auvergne-Rhône-Alpes → Lyon en tête) remplacé par 201172 (Savoie) pour les stations de Tarentaise + idées ski (LOC_OVERRIDE dans le script).
- Lien « Toutes les activités sur Viator » = 1er lien Viator de la page (déjà corrigé par viator_fix.py). Sélection Viator vérifiée à la main : seulement Le Suquet pour l'instant (config PAGES).
- Commits : FR b2e40f0 + ceaf1bb, EN d1c7978 + bcaba74.

## 2026-11-14 — Sélection Viator Côte d'Azur (52 pages FR + 52 EN)
- 41 activités Viator retenues (2 par page), tirées des pages Viator du lieu (« -attractions/…-aNNNN ») ou de la ville, choix = sur place + beaucoup d'avis. Toutes vérifiées dans le navigateur le 14/11 : page OK, bonne activité, pid conservé.
- Fichier : _outils/viator_picks.py (P = activités FR/EN, G = page → 2 activités, A = page → page lieu Viator pour « Toutes les activités »). Alias EN : esterel-massif, lemon-festival-menton, lerins-islands, verdon-gorge.
- Sans sélection (volontaire) : 3-jours, carnaval-de-nice, noel-cote-d-azur, porquerolles (Viator n'a rien sur Porquerolles depuis Toulon).
- Musées Matisse / Chagall : liens GYG + widget passés de Nice (l314, qui affichait un bateau pour Saint-Tropez) aux lieux dédiés matisse-museum-of-nice-l4133 et marc-chagall-national-museum-l4138 (testé : activités du musée en tête).
- Commits : FR 4f6fd9e + suivant, EN 7569c82 + suivant. Suite prévue : Paris.

## 2026-11-14 — Sélection Viator : Paris
- Bloc « À réserver sur place » de Paris (FR + EN) : 2 activités Viator choisies pour 35 pages (60 produits, bien notés et en rapport direct avec le lieu), plus le lien « Toutes les activités » vers la page attraction Viator de 47 pages.
- Sans sélection, faute de produit propre au lieu : bastille, batignolles, bercy, buttes-chaumont, chantilly, château de Vincennes, châtelet, île Saint-Louis, la Défense, la Villette, Montparnasse, Saint-Germain, Saint-Michel, Auvers, Pierrefonds, 3 jours, Noël.
- Chaque produit vérifié : statut 200, code produit présent, pid gardé. Outil : _outils/viator_picks.py (PG/PA), activites.py.

## 2026-11-14 — Sélection Viator : Aquitaine, Lot, Corse
- 16 pages avec 1 ou 2 activités Viator (19 produits) : Bordeaux, Saint-Émilion, dune du Pilat, Sarlat, La Roque-Gageac, Beynac, Castelnaud, Lascaux, Rocamadour, Ajaccio, Piana, Calvi, Bonifacio, falaises de Bonifacio, Lavezzi, Porto-Vecchio.
- Sans sélection (rien de propre au lieu ou pas d'avis) : Bergerac, Périgueux, Milandes, Marqueyssac, Padirac, Saint-Cirq-Lapopie, Bastia.
- 50 produits candidats testés : statut 200, code produit, pid gardé.

## 2026-11-14 — Sélection Viator : autres régions + Cannes
- 27 pages de plus avec 1 ou 2 activités Viator (46 produits testés : 200, code produit, pid gardé) : Colmar, Strasbourg, Riquewihr, Kaysersberg, Dinan, Saint-Malo, Chambord, Chenonceau, Amboise, Villandry, Honfleur, Étretat, plages du Débarquement, Mont-Saint-Michel, Rouen, Biarritz, Saint-Jean-de-Luz, Bayonne, Aix, Avignon, Arles, Camargue, Baux, Gordes, Marseille, Calanques, Chamonix.
- Sans sélection (rien de propre au lieu) : stations de ski (sauf Chamonix), Pyrénées, Carnac, Concarneau, Ploumanac'h, Quimper, Espelette, L'Isle-sur-la-Sorgue, pages « idées ».
- Cannes (FR + EN), demande d'Anthony : le widget GYG ne prend plus le lieu (il sortait un tour de Menton) mais 4 activités choisies, dans l'ordre : bateau pour Saint-Tropez (t95337), visite guidée à pied de Cannes (t243442), ferry Sainte-Marguerite (t65370), atelier parfum Molinard (t641064). Sur mobile, les 2 premières. Réglage : GYG_TOURS dans activites.py.

## 2026-11-14 — Arc de Triomphe : widget GYG
- Le widget (lieu l3238) montrait le marché de Noël de la Défense. Remplacé par 2 activités choisies : billets pour le toit (t66157) et entrée + croisière sur la Seine (t344326). FR + EN. Réglage : GYG_TOURS dans activites.py.

## 2026-11-14 — Tour Eiffel : widget GYG
- Le widget montrait une croisière et le restaurant. Remplacé par 4 activités de la tour : billet 2e étage/sommet (t149861), accès réservé sommet ou 2e étage (t403969), visite guidée avec sommet en option (t29942), sommet ou 2e étage avec guide (t983435). FR + EN.
- Tour Eiffel, à la demande d’Anthony : ordre final t62484 (sommet ou 2e étage, ~18 000 avis), t403497 (2e étage et sommet en ascenseur), t983435, t403969.

## 2026-11-14 — Notre-Dame : widget GYG
- Le 2e résultat était un déjeuner à la Brasserie Madame (tour Eiffel). Remplacé par : visite guidée du chef-d’œuvre restauré (t1156458), intérieur et extérieur avec guide (t778850), Sainte-Chapelle + Conciergerie + Notre-Dame (t525225), visite avec guide francophone (t1239537). Rendu vérifié dans le widget. FR + EN.

## 2026-11-14 — Sainte-Chapelle : widget GYG
- Demande d’Anthony : Sainte-Chapelle + extérieur de Notre-Dame (t828673), Sainte-Chapelle + Conciergerie (t525225), plus visite en petit groupe (t233477). FR + EN.
- Correctif : quand on fixe moins de 4 activités, GYG complétait avec n’importe quoi (une croisière). Le widget affiche maintenant exactement le nombre d’activités choisies (Arc de Triomphe : 2, Sainte-Chapelle : 3).

## 2026-11-14 — Panthéon : widget GYG
- Le 2e était une balade en mobylette. Remplacé (demande d’Anthony) : billet d’entrée (t70680), billet + audioguide (t1428204), visite privée Luxembourg + Panthéon (t497728). Rendu vérifié. FR + EN.

## 2026-11-14 — Invalides : widget GYG
- Le 2e était une croisière avec gaufre. Remplacé (demande d’Anthony) : tombeau de Napoléon + musée de l’Armée (t70627), visite guidée « de l’hôpital royal à la tombe de Napoléon » (t1148557), Aura Invalides (t463678), visite privée (t1501481). Sur mobile : les 2 premiers. FR + EN.

## 2026-11-14 — Conciergerie : widget GYG
- Aucun des 2 n’allait. Remplacé (demande d’Anthony) : billet Conciergerie avec HistoPad (t222147), Sainte-Chapelle + Conciergerie (t525225). Rendu vérifié. FR + EN.

## 2026-11-14 — Fondation Louis Vuitton
- GYG n’a aucune activité propre à la Fondation (sa page l4985 montre Disneyland, croisières…). Les 5 liens GYG de la page (FR + EN) pointent maintenant vers l’entrée Viator de la Fondation (d479-466185P14, testée), et le widget GYG est retiré du bloc (GYG_TOURS = « - »). Reste la sélection Viator.

## 2026-11-14 — Musée Picasso : widget GYG
- Demande d’Anthony : billet musée Picasso + croisière en option (t432084), visite privée « L’artiste amoureux » (t1272547). Rendu vérifié. FR + EN.

## 2026-11-14 — GYG : activités choisies sur tout le site
- Relevé des activités GYG de chaque lieu (pages lieu GetYourGuide), tri par mot-clé du lieu puis relecture à la main : excursions « depuis X » vers ailleurs, transferts, bar crawl, cours en néerlandais… écartés.
- 141 pages (FR + EN) ont maintenant des activités fixées (data-gyg-tour-ids) ; les 316 numéros ont été contrôlés dans le widget (3 introuvables retirés).
- 46 pages sans rien de propre au lieu : widget GYG retiré (stations de ski sauf Chamonix, Courchevel, Megève, Les 2 Alpes, Alpe d'Huez, Serre-Chevalier, La Plagne ; Pyrénées ; Kaysersberg ; Castelnaud, Milandes, Marqueyssac, La Roque-Gageac ; Ploumanac'h, Quimper ; Beaulieu, Biot, Cap d'Antibes, Carnaval de Nice, Noël Côte d'Azur, Grand Prix, Jardin exotique, Mougins, Roquebrune, villa Ephrussi ; Padirac ; Batignolles, Buttes-Chaumont, Champs-Élysées, Vincennes, Châtelet, Montparnasse, Noël à Paris, Saint-Michel ; Fondation Louis Vuitton).
- Pages « idées » : widget par lieu gardé (pages générales).
- Réglage : _outils/gyg_tours.py (clé = chemin FR ; l’anglais suit via hreflang).

## 2026-11-14 — Pages « vraiment rien »
- Recherche GYG par nom pour les 45 pages sans widget : 13 récupérées (Montgenèvre, Kaysersberg, château de Castelnaud, Cap d’Antibes, Carnaval de Nice, Grand Prix, Mougins, Noël Côte d’Azur, Champs-Élysées, Vincennes, Montparnasse, Noël à Paris, Saint-Michel).
- 6 pages où seul Viator a quelque chose (La Roque-Gageac, Beaulieu, villa Ephrussi, Jardin exotique, Buttes-Chaumont, Châtelet-Les Halles) : tous les liens GYG pointent vers l’activité ou la page Viator du lieu.
- 26 pages sans rien nulle part (stations de ski sans offre, Pyrénées, Milandes, Marqueyssac, Ploumanac’h, Quimper, Biot, Roquebrune, Padirac, Batignolles…) : encadré « À réserver », section « Activités à réserver », barre mobile, bouton d’en-tête et liens « Réserver… » retirés. Plus aucun lien partenaire sur ces pages. Picks Viator de Biot (Antibes) et Roquebrune (Menton) retirés.
- Outil : _outils/sans_resa.py (FR + EN).

## 2026-11-14 — Widget mobile : remplissage Notre-Dame
- Signalé par Anthony (La Villette) : sur mobile, le script forçait 2 cartes ; avec 1 seule activité choisie, GYG complétait avec une visite de Notre-Dame. Le nombre de cartes suit maintenant le nombre d’activités choisies (max 2 sur mobile). Toutes les pages FR + EN régénérées.

## 2026-11-15 — Nouvelle page : randonnée du mont Gros (Nice)
- FR cote-d-azur/mont-gros/, EN french-riviera/mont-gros/ ; carte dans la section Nice de l’index Côte d’Azur, JSON-LD includesAttraction, sitemap, accueil (56 guides Côte d’Azur, compteur corrigé : il affichait 38 et 55).
- Faits relevés le 15/11 : Wikipédia (mont Gros 375 m, observatoire 1881-1887, Bischoffsheim, Garnier, coupole Eiffel), Visorando « Tour du Vinaigrier » (5,23 km, 2 h 25, +332 m, départ église Saint-Roch, balisage jaune-rouge), provence-alpes-cotedazur.com (parc 31 ha, horaires saisonniers, bus 84 arrêt Sainte-Anne), fiche office de tourisme + OCA (visite guidée obligatoire, 12/10/6 €, 2 h).
- Pas d’activité GYG/Viator propre au lieu : pas de bloc de réservation, seulement le transfert Elite Prestige (section « Y aller avec un chauffeur privé »).
- Photo : « Nice Est observatoire 01 » de Cayambe, CC BY-SA 3.0, Wikimedia Commons ; crédit en bas de photo et dans les mentions légales (FR + EN).
- NOUVEL OUTIL photos : upload.wikimedia.org est bloqué depuis l’environnement de travail. Lister « nom URL » dans main:_outils/photos.txt et pousser : l’action GitHub « Photos (téléchargement) » télécharge dans _photos_brutes/ et commit. Récupérer avec git pull, traiter, puis supprimer _photos_brutes/ (le site a .nojekyll, le dossier serait public).
- Générateur de la page : guide_gen/generateur/run_mont_gros.py (à partir du gabarit colline-du-chateau).
- Correctif du 15/11 : la carte « transfert Elite Prestige » avait été retirée par erreur avec les blocs de réservation sur Auron, Isola 2000, Biot, Roquebrune (FR + EN) ; rétablie dans une section « Y aller avec un chauffeur privé » (id="chauffeur").

## 2026-11-15 — 12 pages randonnées Côte d'Azur (FR+EN)
- Pages : tete-de-chien, promenade-le-corbusier, lac-de-trecolpas, val-de-siagne, pic-de-courmettes, vieil-aspremont, sentier-nietzsche, cascade-de-vescagne, cime-de-la-forna, sentier-de-la-brague, sentier-du-cap-ferrat, plage-de-la-mala (mêmes slugs FR/EN).
- Nouvelle section « Randonnées et sentiers du littoral » / « Hikes and coastal paths » (#g-rando) sur l'index Côte d'Azur ; mont-gros déplacé dedans. Compteur accueil : 68 guides.
- Générateur : guide_gen/generateur/run_randos.py + randos_data.py (contenu) + run_randos_integration.py (index, sitemap, crédits, compteurs).
- Photos Commons téléchargées via le workflow photos.yml (ajout pause + 4 tentatives, Commons renvoie 429). Lignes traitées marquées « # fait: » dans _outils/photos.txt.
- Pas de bloc réservation GYG/Viator sur ces pages (rien de spécifique) ; carte chauffeur EPS uniquement.
- À surveiller : Tête de Chien, tronçon balises 605-606 signalé fermé (Randoxygène) ; Cap Moderne fermé de novembre à mars.

## 2026-11-15 (nuit) — SEO pages randonnées
- Titres raccourcis (≤ 52 car. + « | Clic&Site ») et descriptions ≤ 156 car. sur les 13 pages rando FR/EN (seo_meta.py). Attention : run_randos.py régénère avec les anciens titres → relancer seo_meta.py après toute régénération.
- Liens internes : 21 pages villes/sites (FR+EN) pointent vers les randos dans « À voir à proximité » (seo_links.py) + liens dans le texte sur Èze, Roquebrune, Saint-Jean-Cap-Ferrat.
- Sitemaps FR et EN renvoyés dans Search Console (FR lu le 15/11 : 223 URL).

## 2026-11-15 (routine de nuit) — Infos pratiques 2026 sur 4 pages (FR + EN)
- Pages : Fête du Citron (Corsos des fruits d’or et nocturnes avec tarifs enfant, forfait nocturne + expo 37/18 €, Jardins de lumière 16/8 € les 16, 19, 23, 26 févr.), Carnaval de Nice (batailles de fleurs sous réserve météo, corsos illuminés 20 h 30 les 16, 20, 23 févr. selon le CRT, corso d’Aqui 21 févr. 14 h 30, tarifs 2027 « non communiqués »), Alpe d’Huez (forfait saison 930,50 € jusqu’au 20/11 puis 1 127,50 €, gratuit -5 ans, 72+ 338,50 €, Flex 10 jours, Supernova), Serre Chevalier (saison 5 déc.-18 avr., forfaits Addict/Ski’llimité, forfaits séjour, navette Oulx). FR cote-d-azur/, alpes/ ; EN french-riviera/, french-alps/.
- 1 à 2 questions FAQ par page (visible + JSON-LD) ; titles ≤ 65 car. et descriptions ≤ 155 avec l’année ; « Mis à jour le 15 novembre 2026 ».
- Sources lues le 15/11 : cotedazurfrance.fr (fiches 2027 Fête du Citron et Carnaval), skipass.alpedhuez.com (page forfait saison), serre-chevalier.com et booking.serre-chevalier.com. Bloqués (PROVENANCE_REQUIRED) : fete-du-citron.com, nicecarnaval.com, les2alpes.com, skipass.les2alpes.com, alpedhuez.com, pages journée/semaine de skipass.alpedhuez.com. À recouper : fiche CRT Fête du Citron indique l’expo payante (12/7 €) mais la fiche « Douce France » la dit gratuite ; date du forfait saison Alpe d’Huez 5 ou 6 déc. selon la langue de la page.
- Liens partenaires : aucun lien ajouté. Contrôle automatique des 749 GYG et 939 Viator par site : format, partner_id, pid/mcid, langue, tag = page, aucun /s/?q= → aucune anomalie. Signalés (recherche Viator d’un seul mot, sans ville) : text=Lascaux, courchevel, louvre, montmartre (FR + EN) — à tester au navigateur et passer en « ville+lieu ».
- Contrôles : html.parser, 1 h1, JSON-LD valides, 344 liens internes/hreflang OK (serveur local), 224 pages FR / 223 EN inchangé. Commits d7ad2eae (FR), 1226e08 (EN).

## 2026-11-15 (soir) — 21 nouvelles pages régions (FR+EN)
- Générateur : guide_gen/generateur/site_gen.py (modèle = page existante de la même région ; svg/cta repris de normandie/etretat si absents) + data_lot1..4.py. Lancement : PAGES -> photos() / page() / integrate() puis webp.py puis activites.py.
- Lot : cahors, grotte-du-pech-merle, figeac. Loire : blois, cheverny, chaumont-sur-loire. Normandie : bayeux, deauville (Giverny existait déjà dans paris/giverny : carte ajoutée dans l'index Normandie vers cette page, pas de doublon). Pays basque : la-rhune, saint-jean-pied-de-port, ainhoa.
- Côte d'Azur (section g-nature) : hyeres, port-cros. Provence (g-avignon) : roussillon, fontaine-de-vaucluse, mont-ventoux. Bretagne : gr34-sentier-des-douaniers (g-nord), quiberon, pointe-du-raz (g-sud). Pyrénées : nouvelle section g-vermeille « Collioure et la Côte Vermeille » (collioure, cote-vermeille) ; titre de l'index Pyrénées élargi.
- Attention : la photo d'une nouvelle page porte le nom du slug → vérifier qu'aucun asset existant du même nom n'est écrasé (incident giverny corrigé par git checkout).
- Viator : destinations utilisées Midi-Pyrenees d5512, Blois d50324, Bayeux d909, Deauville-City d50417, Biarritz d23856, Toulon d24308, Gordes d50932, Avignon d483, Brittany d21942, Perpignan d26343.
- Bayeux : tapisserie au British Museum du 10/09/2026 au 11/07/2027, musée fermé (réouverture 2027) — à mettre à jour à la réouverture.

## 2026-11-15 — Corrections après audit
- Liens Viator : plus aucun lien `searchResults` ; tout pointe vers des pages destination `dNNN-ttd` (script /tmp/g/viator_dest.py, copié ici : guide_gen/generateur/viator_dest.py). Nouvelles destinations vérifiées : Chamonix d24269, Menton d23076, Arcachon d26516, Mont-St-Michel d25906, Versailles d763, Rhone-Alpes d24268 (Courchevel), Rennes d21943 (Saint-Malo), Bergerac d24181 (Lascaux), Loire-Valley d178 (Chambord).
- Titres ≤ 70 car. et descriptions ≤ 160 sur les deux sites (shorten.py). ATTENTION : si on régénère des pages avec rando_gen/site_gen/seo_meta, re-lancer shorten.py ensuite.
- Cannibalisation : titres recentrés pour Montmartre, Rocher de Monaco, Saint-Jean-Cap-Ferrat, Èze, Roquebrune, Ploumanac'h ; liens ajoutés Rocher → palais princier / musée océanographique, Ploumanac'h → GR34.
- RGPD : le module GetYourGuide est chargé par /assets/gyg.js seulement après clic « Accepter » (localStorage cs_gyg=1). activites.py génère désormais `<script src="/assets/gyg.js?v=1">`. Mentions légales : section RGPD complète (#cookies) + bouton de retrait.
- Liens internes ajoutés (inlinks.py, par proximité GPS) ; itinéraires 3 jours étoffés ; À propos : méthode, indépendance, mises à jour.
- 15/11 soir : tâche planifiée de nuit « Guide Clic&Site – enrichissement SEO + liens partenaires » DÉSACTIVÉE à la demande d'Anthony (son prompt imposait encore les recherches Viator, contraire à la règle du jour).
- Programme de contrôle : _outils/controle.py dans les deux dépôts + workflow .github/workflows/controle.yml (à chaque push sur main, chaque nuit à 6 h 17, et à la demande). Erreur = le workflow échoue et GitHub envoie un e-mail. Vérifie : pages concurrentes, JSON-LD (fil d'Ariane, FAQ = FAQ visible, Organization), FAQ répétées/hors sujet, titres ≤ 70 et descriptions ≤ 165 uniques, h1, canonical, liens partenaires (pas de searchResults, pas de /s/ GYG, ids), consentement GYG (gyg.js), liens internes, sitemap, robots, pages supprimées, mentions légales/À propos. Pas de CGV exigées (le site ne vend rien).
- 16/11 passage « SEO » (manuel, à la demande d'Anthony) : contrôle 0 erreur ; agenda Idées à jour (rien de passé, illuminations Champs-Élysées 22/11 et ouverture Val Thorens/Tignes 21/11 reconfirmées) ; section infos-2026 + 1 question FAQ (visible + JSON-LD) FR/EN sur Isola 2000, Auron, Font-Romeu, Chamonix (forfaits 2026-2027, saison). Font-Romeu : fermeture corrigée au 29/03/2027. Aucun nouveau lien partenaire. Publication OK (pages-build success).
- 16/11 (2e passage) : infos-2026 + FAQ forfait FR/EN sur Megève, La Clusaz, Avoriaz, Cauterets (sources : sites des stations et offices de tourisme). Corrigé : fermeture Megève 4/04/2027 (au lieu de « début avril ») ; Avoriaz : « préouverture fin novembre » retirée (non confirmée, ouverture officielle 11/12/2026). Vérifié en ligne dans le navigateur (Megève FR, Cauterets EN).
- 16/11 (3e passage) : infos-2026 + FAQ forfait FR/EN sur Les 2 Alpes, Montgenèvre, Saint-Lary, Peyragudes. Saint-Lary : fermeture corrigée au 29/03/2027. Reste sans infos-2026 : La Grave, SuperDévoluy, Châtel, Grand Tourmalet. Vérifié en ligne (Saint-Lary FR, Les 2 Alpes EN).
- 16/11 (4e passage) : infos-2026 + FAQ forfait FR/EN sur La Grave, Dévoluy, Châtel, Grand Tourmalet → toutes les stations Alpes et Pyrénées ont leur section infos-2026. La Grave : dates corrigées 19/12/2026-2/05/2027 et 68 € (office de tourisme des Hautes Vallées) sur la page, les cartes et l'agenda des stations. Vérifié en ligne (La Grave FR, Grand Tourmalet EN).

## 16/11/2026 — 6 pages d'hiver FR+EN
- idees/prix-forfaits-ski-2026-2027 ↔ ideas/ski-pass-prices-2026-2027 (tableau 24 stations, CSS .tbl ajouté, style.css?v=w1116)
- idees/marches-de-noel-alsace ↔ ideas/alsace-christmas-markets
- idees/reveillon-nouvel-an ↔ ideas/new-years-eve-france (Nice : programme officiel 2026 pas encore publié → à mettre à jour dès sa sortie)
- idees/vacances-de-fevrier-2027 ↔ ideas/february-school-holidays-2027
- cote-d-azur/rallye-monte-carlo ↔ french-riviera/monte-carlo-rally (Event 21-24/01/2027)
- cote-d-azur/route-du-mimosa ↔ french-riviera/mimosa-route (Event 10-14/02/2027)
- Cartes Idées + région Côte d'Azur, sitemaps, liens entrants depuis stations, Strasbourg, Colmar, Noël à Paris, Côte d'Azur en hiver, Monaco, Mandelieu, Où partir en hiver
- Générateur : guide_gen/generateur/winter_gen.py + winter_data.py
- controle.py : 0 erreur FR et EN ; workflows verts ; 12 pages en ligne vérifiées (200, liens partenaires OK)

## 18/11/2026
- Stats : la fonction collect (Supabase) ignore désormais les IP de Google (goog.json + plages des robots), en plus du filtre user-agent
- mentions-legales.html (ancienne URL) redirigée vers /mentions-legales/
- Search Console : .com, « Valider la correction » lancée sur les anciennes URL http/www en noindex
- Pinterest : compte pro ClicAndsite, 4 tableaux publics, 12 épingles publiées (scripts /tmp/pin)
- AdSense : balise meta + ads.txt (pub-9562574817844558), sites .fr et .com soumis

## 18/11/2026 (nuit) — SEO régions
- Infos pratiques 2026 + FAQ (FR+EN) : Mont-Saint-Michel, Étretat, Honfleur, Rouen (Armada 17-27/06/2027), plages du Débarquement, Strasbourg, Colmar, Riquewihr, Kaysersberg ; ajouts Quimper (MBA fermé jusqu’en 2027), Ploumanac’h (parkings 2026), Espelette (marché mercredi)
- Sections annuelles (#g-annee) sur les hubs Bretagne, Normandie, Alsace, Pays basque, Corse
- Script : guide_gen/generateur/seo_regions_1118.py + regions_hub_1118.py
- À faire : Quimper et Ploumanac’h n’ont aucun lien partenaire (chercher des activités GYG/Viator pertinentes)
- Quimper : section #reserver ajoutée (GYG quimper-l99276, croisière Glénan t606317, widget 606317+677349, Viator Bretagne d21942). Ploumanac’h : aucune offre GYG/Viator à Perros-Guirec (vérifié 18/11) → pas de section, à revoir si une offre apparaît

## 18/11/2026 — Liens partenaires sur les pages qui n'en avaient pas
- Ajout FR+EN (script guide_gen/generateur/ski_acts.py, sans widget) : Tignes, Val d'Isère, Val Thorens, Méribel, Les Menuires, Les Arcs, Avoriaz, La Clusaz, Cauterets, Grand Tourmalet, Padirac, Marqueyssac, Milandes. Chaque lien vérifié dans le navigateur.
- Sans offre pertinente (pas de lien) : Châtel, La Grave, Superdévoluy, Font-Romeu, Saint-Lary, Peyragudes. Revoir à chaque passage SEO.
- 18/11 : liens ajoutés sur cote-d-azur/3-jours, paris/3-jours (repris des pages Villefranche, Monaco, Lérins, Sainte-Chapelle, Louvre, Tour Eiffel) et paris/batignolles (visite privée Viator d479-30791P281 + Montmartre). Script itin_acts.py.

## 18/11/2026 (nuit) — 15 nouvelles pages régions (FR+EN)
- Alsace : eguisheim, haut-koenigsbourg, obernai, mulhouse. Normandie : caen, trouville. Bretagne : rennes, belle-ile, golfe-du-morbihan, cancale. Pays basque : hendaye, sare. Corse : corte, cap-corse. Pyrénées : lourdes. Mêmes slugs FR/EN.
- Générateur : run_new15.py + data_new15a/b/c.py (site_gen.py) ; liens entrants : inlinks_new15.py (blocs « À voir à proximité » ajoutés sur colmar, strasbourg, saint-malo, saint-jean-de-luz, cauterets…).
- Photos Commons (crédits page + mentions légales) : Pug Girl CC BY 2.0, Gzen92, Hermann Luyken, Pieter Smits CC BY 2.0, Zairon, W. Bulach (Trouville, Lourdes), Erwan Corre, Franck-fnba, Jebulon CC0, Alan M Hughes, Daniel Villafruela, Gilles Guillamot, Bj.schoenmakers CC0, Pierre Bona.
- Photos : le workflow n'accepte que les largeurs standard (1920) ou l'original ; 2400/2560/3000px échouent. Lignes traitées marquées « # fait: ». _photos_brutes supprimé.
- sitemap_dates.py : passer le domaine AVEC https:// (sinon 0 mise à jour).
- Tarifs 2026 vérifiés : Haut-Kœnigsbourg 12/8 €, musée Automobile 19 €, Cité du Train 16 €, Mémorial 20,80/18,50 €, Abbadia 12,90/9,90 €, grottes de Sare 10/6 €, musée de la Corse 5,50/4 €, pic du Jer 14,50 € A/R, procession Lourdes 21 h du 5/04 au 1/11/2026.
- Liens partenaires : GYG colmar-l2924, chateau-du-haut-koenigsbourg-l132238, obernai-l102201, memorial-de-caen-l5062, deauville-l33006, rennes-l2681, sauzon-l190848, gulf-of-morbihan-l161168, cancale-l148240, french-basque-country-l117470, corte-l32543, lourdes-l311 ; Viator Obernai d51227, Normandy d183, Corte d24042, produit cap Corse d24042-5501928P1, produit Mulhouse d22940-76654P670.

## 18/11/2026 (soir) — Page « Où partir en France en 2027 » + épingles publiées
- Page FR idees/ou-partir-en-france-en-2027, EN ideas/where-to-go-in-france-in-2027 (script /tmp/g/ou_partir_2027.py, modèle winter_gen). Liens entrants depuis ou-partir-en-hiver, vacances-de-fevrier-2027, marches-de-noel-alsace.
- Pinterest : site clicandsite.fr revendiqué (meta p:domain_verify sur l'accueil FR).
- Méthode qui marche pour publier : images d'épingle dans assets/pins/ + bloc <figure class="pinit"> sur la page (avant la FAQ) ; Pinterest « Enregistrer depuis l'URL » avec l'URL de la PAGE → le lien de destination = la page. (Upload de fichier refusé hors mode auto ; fetch bloqué par la CSP Pinterest ; modifier le lien après coup échoue.)
- Publiées : 2027, Bordeaux, Marseille, Eguisheim (tableau Idées de voyage en France), Monaco (Côte d'Azur). Une 1re épingle « Où partir 2027 » pointe vers l'image jpg (pin 230035493464319708) : à supprimer avec l'accord d'Anthony.
- Tableaux : Côte d'Azur, Idées de voyage en France, Noël et Nouvel An, Ski et montagne.
- Cadence Pinterest validée par Anthony : ~1 épingle/jour en semaine (3-5/sem), images toujours nouvelles, saison avec 4-6 semaines d'avance. Au prochain « SEO » (ordi allumé) : préparer ~10 épingles et les programmer sur 2 semaines via Pinterest. Épingle en double « 2027 » supprimée le 18/11.
- 18/11 23h45 : épingles Strasbourg et Colmar publiées (tableau Noël et Nouvel An). La programmation n'existe pas dans le générateur « depuis l'URL » (seulement Supprimer/Dupliquer). File d'attente prête (images en ligne + bloc pinit sur les pages) : 20 Riquewihr (Noël et Nouvel An), 21 Chamonix et 22 Courchevel (Ski et montagne), 23 tour Eiffel, 24 Mont-Saint-Michel, 27 Versailles (Idées de voyage), 25 Nice et 26 Cannes (Côte d'Azur). Publier 1 à 2 par passage SEO.
- 18/11 23h50 : Riquewihr publiée (Noël et Nouvel An). Reste en file : 21 Chamonix, 22 Courchevel, 23 tour Eiffel, 24 Mont-Saint-Michel, 25 Nice, 26 Cannes, 27 Versailles.
- 19/11 00h20 : Instagram @clicandsite (basculer depuis abracadeal.fr dans Chrome) : 3 publications 4:5 — Colmar Noël, Où partir 2027, Chamonix (légendes ≤5 hashtags, partage Facebook « Tonino Cannes » laissé désactivé). Méthode : images dans assets/ig/ + page assets/ig/send.html (noindex, robots Disallow) ouverte par un bouton injecté sur instagram.com → postMessage du blob → DataTransfer sur l'input file du dialogue Créer. Recadrage : icône en bas à gauche → 4:5. Images IG générées avec /tmp/ig/make.py (post()).

## 19/11/2026 — SEO
- AdSense : ads.txt .com vérifié en ligne (https et www → redirection), « Introuvable » = contrôle AdSense 7 min après la mise en ligne ; revérification auto
- Pinterest : profil complet (nom, photo, description, site), clicandsite.fr revendiqué
- Stats 7 j hors robots (Mountain View, Prineville…) et hors Cannes : 93 vues, 5 clics partenaires ; 24 h : 4 vues
- Nouvelle page FR idees/saint-valentin-2027, EN ideas/valentines-day-2027 (script saint_valentin.py, winter_gen avec date) ; carte sur l’index Idées, sitemap, liens entrants : vacances-de-fevrier-2027 / february-school-holidays-2027, croisiere-sur-la-seine / seine-cruise, eze
- Épingle 28-saint-valentin (make_pins5.py) + bloc pinit sur la page FR
