# Journal et file d'attente des guides Clic&Site

## Déjà en ligne (11/11/2026)
- Côte d'Azur : 19 guides + itinéraire 3 jours
- Paris : 15 guides (dont Disneyland Paris, Catacombes, Noël à Paris) + itinéraire 3 jours
- Alpes : Chamonix, Val Thorens, Courchevel, Megève, Val d'Isère, Tignes, Méribel, Alpe d'Huez
- Alsace (depuis le 12/11/2026) : Strasbourg, Colmar

## Pages « Idées » (content_selections_fr.py / _en.py) — À METTRE À JOUR
- 4 pages : où partir cet hiver, que faire à Paris en hiver, Côte d'Azur en hiver, stations de ski ouvertes. Chacune a un agenda daté.
- Le 1er de chaque mois : retirer les événements passés de l'agenda, ajouter ceux du mois suivant (vérifiés le jour même : sites officiels, offices de tourisme, presse), et mettre à jour les dates des expositions parisiennes.
- Selon la saison, ajouter de nouvelles pages idées : « que faire à Paris en février / au printemps », « où partir pour les ponts de mai », « Côte d'Azur en été », etc. Pas plus d'une nouvelle page idée par semaine.

## File d'attente (hiver : priorité ski, Noël et Paris)
1. Alsace : Riquewihr, Kaysersberg, Eguisheim (URGENT, marchés de Noël dès le 27/11 ; dates 2026 sur noel-colmar.com : Riquewihr 27/11-20/12, Kaysersberg ven-sam-dim 27/11-20/12, Eguisheim 27/11-30/12 — à revérifier le jour même)
2. Paris : Invalides et tombeau de Napoléon, musée de l'Orangerie, Saint-Germain-des-Prés, Galeries Lafayette et grands magasins (vérifier les faits du jour)
3. Alpes (stations) : Les Arcs, La Plagne, Les 2 Alpes, Avoriaz, La Clusaz, Serre Chevalier, Les Menuires
5. Alpes (groupe « villes ») : Annecy
6. Pyrénées (stations) : Saint-Lary, Cauterets, Font-Romeu, La Mongie / Grand Tourmalet
7. Ensuite : Provence (prioritaire à partir de mars), Bretagne, Pays basque, Lyon, Bordeaux

## Journal
- 12/11/2026 (routine) : région Alsace créée (Strasbourg, Colmar, FR+EN, photos Unsplash vérifiées : Thomas Dorgler, Aswathy N, Dirk Scheuble pour la région). Dates vérifiées : noel.strasbourg.eu (27/11-24/12/2026), noel-colmar.com (Colmar 23/11-29/12/2026). Enrichi : Menton, FAQ Fête du Citron 2027 (93e, 13-28/02/2027, corsos nocturnes 18 et 25/02). Titres trop longs corrigés (Noël à Paris, Stations de ski). Note : le build demande `npm i --no-save @fontsource/young-serif @fontsource/public-sans` (polices des images OG).
- 11/11/2026 (session manuelle) : région Alpes créée (8 stations), 3 guides Paris ajoutés, boutons partenaires refaits, recherches GetYourGuide/Viator ancrées sur le lieu (fonction anchored dans build.py).
- 11/11/2026 (session manuelle) : 4 pages Idées avec agenda (Carnaval de Nice 9-28 févr. 2027, Fête du Citron 13-28 févr., Mimosa 10-14 févr., cirque de Monte-Carlo 22-31 janv., expos Paris), lien « Idées » dans le menu et section sur l'accueil.

## Search Console (note du 11/11/2026)
- Les propriétés domaine `sc-domain:clicandsite.fr` et `sc-domain:clicandsite.com` sont sur le compte abracadeal@gmail.com. Depuis le 11/11 au soir c'est le seul compte connecté dans le navigateur intégré (`https://search.google.com/search-console/...`, sans /u/1/). Si une page dit « vous n'avez pas accès », vérifier « Connecté en tant que » : ce doit être abracadeal@gmail.com.
- Pour renvoyer un sitemap, saisir l'URL complète (`https://clicandsite.fr/sitemap.xml`), sinon « Adresse de sitemap incorrecte ».
- 11/11 : 10 pages indexées sur 55 (.fr), .com en cours de traitement ; sitemaps renvoyés (55 URL chacun).
