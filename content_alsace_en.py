# Alsace region (Christmas markets) — English edition (12/11/2026). Same facts as the French edition.

REGION = {
    "slug": "alsace", "path": "alsace", "nom": "Alsace",
    "h1": "Visiting Alsace and its Christmas markets",
    "de": "Alsace",
    "autres": "More places in Alsace",
    "couleur": "ocre",
    "timbre": "Alsace",
    "photo": "alsace",
    "photo_alt": "A fortified church among the vineyards of Alsace",
    "address_region": "Grand Est",
    "description": "Strasbourg and Colmar: our Alsace guides to the 2026 Christmas markets, half-timbered old towns, getting there by train and what to book.",
    "accroche": "Half-timbered houses, vineyards and old towns lit up for the season: in December, Alsace is France's Christmas region.",
    "intro": [
        "Between the Vosges mountains and the Rhine, Alsace has some of the best-preserved towns and villages in France: the cathedral and Petite France in Strasbourg, the canals of Colmar, the flower-decked villages of the wine route. Each guide covers what to see, how to get there and what is worth booking.",
        "From late November to late December the region revolves around its Christmas markets, including Strasbourg's, held since 1570. Trains link Strasbourg, Colmar and most villages easily, so Alsace is perfectly manageable without a car.",
    ],
    "departements": ["67", "68"],
}

GROUPES = [
    ("villes", "Towns and Christmas markets"),
]

VEDETTES = ["strasbourg", "colmar"]

def _d(**k):
    k.setdefault("region", "alsace")
    return k

DESTINATIONS = [
    _d(slug="strasbourg", path="strasbourg", groupe="villes", nom="Strasbourg", dept="67", cachet="Bas-Rhin", couleur="encre", h1="Strasbourg: Christmas market, cathedral and Petite France",
       **{"in": "in Strasbourg", "to": "to Strasbourg", "tips_for": "a trip to Strasbourg"},
       description="Visiting Strasbourg: the 2026 Christmas market (27 November to 24 December), the cathedral, Petite France, the Neustadt and the train from Paris.",
       accroche="A pink sandstone cathedral, half-timbered quaysides and France's most famous Christmas market: Strasbourg is best explored on foot over one or two days.",
       intro=[
           "Strasbourg's historic centre, the Grande Île, is ringed by the arms of the River Ill. Within minutes you walk from the cathedral to the old tanners' houses of Petite France, then on to the broad avenues of the Neustadt, the district built during the German period. The whole ensemble is a UNESCO World Heritage Site.",
           "For 2026 the Christmas market, the Christkindelsmärik, runs from 27 November to 24 December. The stalls are spread across several squares of the Grande Île, with the Great Christmas Tree on Place Kléber and an ice rink in the courtyard of the Palais Rohan.",
       ],
       a_voir=[
           ("Strasbourg Cathedral", "A Gothic masterpiece in pink Vosges sandstone, with its single spire and astronomical clock. A platform, reached by a long staircase, looks out over the rooftops and, on a clear day, the Black Forest."),
           ("Petite France", "The old millers' and tanners' quarter, with half-timbered houses on the water and swing bridges. It is the loveliest part of town for a walk at dusk."),
           ("The Ponts Couverts and the Vauban Dam", "The medieval towers that once guarded the city's entrance, then the Vauban Dam, whose rooftop terrace has a fine view over Petite France."),
           ("The Christkindelsmärik and the Great Tree", "The historic market on Place Broglie and the huge decorated tree on Place Kléber, two essential stops between late November and Christmas."),
           ("Palais Rohan", "The former palace of the prince-bishops, next to the cathedral, houses three museums: fine arts, decorative arts and archaeology."),
           ("The Neustadt", "The grand buildings of Place de la République, the university and streets of neo-Renaissance and Art Nouveau houses show a very different side of Strasbourg."),
       ],
       y_aller=[
           ("By train", "The TGV links Paris Gare de l'Est with Strasbourg in under two hours. From the station, the cathedral is about twenty minutes on foot or a few stops by tram."),
           ("By air", "Strasbourg-Entzheim airport has a regional train link to the main station. EuroAirport Basel-Mulhouse, further south, is another option."),
           ("By car", "During the Christmas market, traffic is heavily restricted on the Grande Île: park at a Park and Ride (P+R) on the outskirts and finish by tram."),
       ],
       fiche=[("Christmas market 2026", "27 November to 24 December"), ("Good for", "Families, couples, heritage lovers"), ("Don't miss", "Cathedral, Petite France"), ("Access", "TGV from Paris, then walk or tram")],
       conseils=[
           "December weekends are very busy in the centre: visit the markets on a weekday or late in the morning if you can.",
           "Climb the cathedral platform early in the day and save Petite France for late afternoon, when the lights come on.",
           "Book accommodation very early for Advent weekends, or stay in Colmar or in Kehl, across the Rhine, both linked by train or tram.",
       ],
       activites=[
           ("Christmas market guided tours", "Guided walks through the illuminated Grande Île, with tastings of Alsatian specialities.", "Christmas market guided tour"),
           ("River Ill cruise", "A boat trip around the Grande Île, from Petite France to the European quarter.", "boat cruise"),
       ],
       faq=[
           ("When is the Strasbourg Christmas market in 2026?", "From Friday 27 November to Thursday 24 December 2026, across several squares of the Grande Île around the cathedral and Place Kléber."),
           ("How long do you need in Strasbourg?", "One day is enough for the cathedral, Petite France and the markets. Allow two days to add the museums, the Neustadt and a river cruise."),
           ("Can you visit Strasbourg without a car?", "Yes, and it is the best way: the city is under two hours from Paris by TGV and the centre is easy to explore on foot or by tram."),
       ]),

    _d(slug="colmar", path="colmar", groupe="villes", nom="Colmar", dept="68", cachet="Haut-Rhin", couleur="ocre", h1="Colmar: Little Venice, the old town and Christmas markets",
       **{"in": "in Colmar", "to": "to Colmar", "tips_for": "a trip to Colmar"},
       description="Visiting Colmar: Little Venice, Maison Pfister, the Unterlinden Museum and the six 2026 Christmas markets (23 November to 29 December). Getting there by train.",
       accroche="Canals lined with colourful houses, a largely pedestrian old town and six Christmas markets: Colmar is Alsace's picture postcard.",
       intro=[
           "Colmar is the capital of Alsace wine, at the foot of the Vosges. Its old town has come through the centuries almost untouched: brightly painted half-timbered houses, Renaissance façades, cobbled lanes and the Little Venice district, where the River Lauch flows between the old market gardeners' houses.",
           "For Christmas 2026 the town sets up six Christmas markets from 23 November to 29 December, including one just for children. Every evening the lights bring out the old buildings, and Colmar makes an ideal base for the villages of the wine route.",
       ],
       a_voir=[
           ("Little Venice", "Colmar's most photographed spot: colourful houses along the Lauch, best seen from the bridge on Rue de Turenne. Flat-bottomed boats offer short trips on the river."),
           ("The Unterlinden Museum", "Set in a former convent, it holds the famous Isenheim Altarpiece, one of the great masterpieces of early sixteenth-century painting."),
           ("Maison Pfister and Maison des Têtes", "Two emblematic Renaissance façades: the first with its wooden gallery and painted panels, the second decorated with dozens of carved faces."),
           ("The Koïfhus and Place de l'Ancienne Douane", "The old customs house, with its glazed tile roof, overlooks a lively square that hosts one of the Christmas markets."),
           ("The Tanners' Quarter", "Tall restored half-timbered houses with open lofts where hides were once dried, a few steps from Little Venice."),
       ],
       y_aller=[
           ("By train", "Colmar has TGV services from Paris and frequent regional trains from Strasbourg and Mulhouse. The old town is about fifteen minutes' walk from the station."),
           ("By air", "The nearest airports are EuroAirport Basel-Mulhouse and Strasbourg-Entzheim, both linked to Colmar by road or rail."),
           ("To the villages", "During the Christmas season, shuttles link Colmar with nearby villages such as Eguisheim, Kaysersberg and Riquewihr: check the tourist office's shuttle guide."),
       ],
       fiche=[("Christmas markets 2026", "23 November to 29 December"), ("Good for", "Couples, families, wine lovers"), ("Don't miss", "Little Venice, Isenheim Altarpiece"), ("Access", "TGV or regional train from Strasbourg")],
       conseils=[
           "On December Saturdays the old town is packed: the tourist office publishes a calendar of expected crowds, handy for choosing your day.",
           "Go back to Little Venice after dark: the reflections of the lights on the water are worth a second visit.",
           "Stay in Colmar rather than Strasbourg if you also want to see the wine-route villages: they are just a few kilometres away.",
       ],
       activites=[
           ("Guided tours of Colmar", "Explore the old town and Little Venice with a guide, by day or under the Christmas lights.", "guided tour"),
           ("Alsace Wine Route", "Trips to Eguisheim, Kaysersberg and Riquewihr, with a tasting at a winemaker's.", "Alsace wine route tour"),
       ],
       faq=[
           ("When are the Colmar Christmas markets in 2026?", "Colmar's six Christmas markets are open from Monday 23 November to Tuesday 29 December 2026, in the old town."),
           ("Colmar or Strasbourg for the Christmas markets?", "Strasbourg is bigger and busier; Colmar is more intimate and closer to the wine-route villages. Half an hour apart by train, the two are easy to combine."),
           ("How long do you need in Colmar?", "One day covers the old town, Little Venice and the Unterlinden Museum. Add a day for the nearby villages."),
       ]),
]

TITRES = {
    "strasbourg": "Strasbourg: 2026 Christmas Market, Cathedral, Access",
    "colmar": "Colmar: 2026 Christmas Markets, Little Venice, Access",
}
TITRE_REGION = "Alsace: 2026 Christmas Markets, Strasbourg, Colmar"

ALIAS = {"strasbourg": ["Strasbourg"], "colmar": ["Colmar"]}
