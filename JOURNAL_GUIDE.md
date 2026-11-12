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
