import re, sys
FR = '/home/claude/clicandsite-guide/cote-d-azur/'
EN = '/home/claude/clicandsite-guide-en/french-riviera/'
# slug_fr, slug_en, name_fr, name_en, items_fr, items_en
D = [
('eze','eze',"Èze","Èze",[
"<strong>Jardin exotique</strong> : 10 € plein tarif, 6 € pour les 12-17 ans et les étudiants, gratuit avant 12 ans. Ouvert tous les jours, de 9 h à 16 h 30 de novembre à mars.",
"<strong>Bus depuis Nice</strong> : ligne 82 (Lignes d’Azur) depuis Nice Vauban jusqu’à Èze Village ; la ligne Zou! 602 Nice–Monaco passe aussi par Èze.",
"<strong>Depuis la gare d’Èze-sur-Mer</strong> : la ligne 83 monte au village si vous ne voulez pas prendre le chemin de Nietzsche.",
"<strong>Parkings</strong> : places Colette et Figuiera, à moins de 200 m du village ; parking de l’Oppidum au col d’Èze, relié au village par une navette gratuite toutes les 15 minutes.",
],[
"<strong>Exotic garden</strong>: €10 full price, €6 for ages 12-17 and students, free under 12. Open daily, 9am to 4:30pm from November to March.",
"<strong>Bus from Nice</strong>: line 82 (Lignes d’Azur) from Nice Vauban to Èze Village; Zou! line 602 Nice–Monaco also stops in Èze.",
"<strong>From Èze-sur-Mer station</strong>: line 83 climbs to the village if you would rather skip the Nietzsche path.",
"<strong>Parking</strong>: place Colette and place Figuiera, under 200 m from the village; the Oppidum car park at the Col d’Èze has a free shuttle every 15 minutes.",
]),
('monaco','monaco',"Monaco","Monaco",[
"<strong>Palais princier</strong> : 10 € pour les adultes, 5 € pour les enfants et étudiants (tarifs 2026).",
"<strong>Parkings publics</strong> : parking des Pêcheurs pour le Rocher (palais, musée océanographique), parking du Square Beaumarchais pour le Casino.",
"<strong>Bus depuis Nice</strong> : ligne Zou! 602 par la Moyenne Corniche, avec arrêt à Èze. Le TER Nice–Vintimille dessert la gare de Monaco-Monte-Carlo.",
],[
"<strong>Prince’s Palace</strong>: €10 for adults, €5 for children and students (2026 prices).",
"<strong>Public car parks</strong>: Parking des Pêcheurs for the Rock (palace, Oceanographic Museum), Square Beaumarchais for the Casino.",
"<strong>Bus from Nice</strong>: Zou! line 602 along the Middle Corniche, stopping in Èze. TER trains on the Nice–Ventimiglia line stop at Monaco-Monte-Carlo station.",
]),
('menton','menton',"Menton","Menton",[
"<strong>Fête du Citron 2027</strong> (93<sup>e</sup> édition, thème « Douce France ») : du 13 au 28 février 2027.",
"<strong>Corsos</strong> : corsos des fruits d’or les dimanches 14, 21 et 28 février ; corsos nocturnes les 18 et 25 février (30 € en tribune, 16 € debout).",
"<strong>Expositions d’agrumes</strong> aux jardins Biovès : 12 € adultes, 7 € enfants.",
"<strong>Y aller</strong> : le TER Nice–Vintimille s’arrête à Menton ; en février, réservez vos places de corso et évitez la voiture, la ville est saturée.",
],[
"<strong>Lemon Festival 2027</strong> (93rd edition, theme “Douce France”): 13 to 28 February 2027.",
"<strong>Parades</strong>: daytime parades on Sundays 14, 21 and 28 February; night parades on 18 and 25 February (€30 in the stands, €16 standing).",
"<strong>Citrus sculptures</strong> in the Biovès gardens: €12 adults, €7 children.",
"<strong>Getting there</strong>: TER trains on the Nice–Ventimiglia line stop in Menton; in February book parade seats ahead and leave the car behind, the town is packed.",
]),
('nice','nice',"Nice","Nice",[
"<strong>Carnaval de Nice 2027</strong> (« Vive l’Amour ») : du 9 au 28 février 2027, ouverture par un corso illuminé le samedi 13 février à 21 h, place Masséna.",
"<strong>Musée Matisse</strong> (Cimiez) : 12 €, fermé le mardi, gratuit pour les moins de 18 ans et les étudiants.",
"<strong>Musée Chagall</strong> : 10 €, gratuit le premier dimanche du mois. Le bus 5 s’arrête devant (« Musée Chagall ») ; depuis le tram 1, arrêt Gare Thiers puis 15 minutes de marche en montée.",
"<strong>Musée des Beaux-Arts Jules Chéret</strong> : 10 €.",
],[
"<strong>Nice Carnival 2027</strong> (“Vive l’Amour”): 9 to 28 February 2027, opening with an illuminated parade on Saturday 13 February at 9pm, place Masséna.",
"<strong>Matisse Museum</strong> (Cimiez): €12, closed on Tuesdays, free for under-18s and students.",
"<strong>Chagall Museum</strong>: €10, free on the first Sunday of the month. Bus 5 stops right outside (“Musée Chagall”); from tram line 1, get off at Gare Thiers and walk 15 minutes uphill.",
"<strong>Jules Chéret Fine Arts Museum</strong>: €10.",
]),
('cannes','cannes',"Cannes","Cannes",[
"<strong>Bateaux pour les îles de Lérins</strong> : départs au bout du quai Saint-Pierre (Vieux-Port). Riviera Lines dessert Sainte-Marguerite (18,50 € aller-retour adulte en 2026) ; seule la compagnie Planaria, gérée par les moines, va à Saint-Honorat.",
"<strong>Mougins et Grasse sans voiture</strong> : depuis la gare de Cannes, Palm Express B ou ligne Zou! 660 jusqu’à Val de Mougins ; le TER relie aussi Cannes à Grasse.",
"<strong>Dernier bateau</strong> : en hiver, le dernier retour de Sainte-Marguerite part vers 17 h. Ne le manquez pas, il n’y a pas d’hébergement sur l’île.",
],[
"<strong>Boats to the Lérins Islands</strong>: departures from the end of quai Saint-Pierre (Old Port). Riviera Lines serves Sainte-Marguerite (€18.50 adult return in 2026); only Planaria, run by the monks, sails to Saint-Honorat.",
"<strong>Mougins and Grasse without a car</strong>: from Cannes station, Palm Express B or Zou! line 660 to Val de Mougins; TER trains also link Cannes and Grasse.",
"<strong>Last boat</strong>: in winter the last return from Sainte-Marguerite leaves around 5pm. Do not miss it, there is nowhere to stay on the island.",
]),
('iles-de-lerins','lerins-islands',"les îles de Lérins","the Lérins Islands",[
"<strong>Sainte-Marguerite</strong> : Riviera Lines, 18,50 € aller-retour adulte (2026), départ au bout du quai Saint-Pierre à Cannes. Retours vers Cannes jusqu’à 17 h en basse saison.",
"<strong>Saint-Honorat</strong> : uniquement avec Planaria, la compagnie de l’abbaye. En hiver, quatre départs en semaine (10 h, 12 h, 14 h, 16 h la saison passée).",
"<strong>Pas de liaison entre les deux îles</strong> : choisissez votre île avant d’acheter le billet.",
"<strong>Tour-monastère de l’abbaye de Lérins</strong> : visite gratuite du lundi au samedi, de 10 h à 12 h 30 et de 14 h 30 à 17 h ; l’après-midi seulement le dimanche.",
"<strong>Saint-Honorat n’a pas de poubelles</strong> : remportez vos déchets, et prévoyez eau et pique-nique.",
],[
"<strong>Sainte-Marguerite</strong>: Riviera Lines, €18.50 adult return (2026), leaving from the end of quai Saint-Pierre in Cannes. Boats back to Cannes until 5pm in low season.",
"<strong>Saint-Honorat</strong>: only with Planaria, the abbey’s own company. In winter there are four weekday departures (10am, noon, 2pm, 4pm last season).",
"<strong>No boat between the two islands</strong>: pick your island before buying the ticket.",
"<strong>Lérins Abbey fortified monastery</strong>: free visit Monday to Saturday, 10am to 12:30pm and 2:30pm to 5pm; afternoons only on Sundays.",
"<strong>Saint-Honorat has no bins</strong>: take your rubbish back, and bring water and a picnic.",
]),
('antibes','antibes',"Antibes","Antibes",[
"<strong>Musée Picasso</strong> (château Grimaldi) : 12 € plein tarif, 8 € réduit, gratuit pour les moins de 18 ans. Fermé le lundi ; de mi-septembre à mi-juin, 10 h–13 h et 14 h–18 h.",
"<strong>Pass musées d’Antibes</strong> : 15 €, valable 7 jours consécutifs pour les musées municipaux et le Fort Carré.",
"<strong>Exposition en cours</strong> : « Claude Picasso – Une vie en marges », au musée Picasso jusqu’au 10 janvier 2027.",
],[
"<strong>Picasso Museum</strong> (Château Grimaldi): €12 full price, €8 reduced, free for under-18s. Closed on Mondays; from mid-September to mid-June, 10am–1pm and 2pm–6pm.",
"<strong>Antibes museum pass</strong>: €15, valid 7 consecutive days for the municipal museums and Fort Carré.",
"<strong>Current exhibition</strong>: “Claude Picasso – A Life on the Margins”, at the Picasso Museum until 10 January 2027.",
]),
('biot','biot',"Biot","Biot",[
"<strong>Musée national Fernand Léger</strong> : 8 € (10 € pendant les expositions), gratuit pour les moins de 26 ans ressortissants de l’UE. Fermé le mardi ; en hiver, 10 h–17 h.",
"<strong>Exposition</strong> : « Léger – Morellet, Dé-figurer la peinture », du 21 novembre 2026 au 26 avril 2027.",
"<strong>Accès</strong> : parking gratuit au musée ; le TER s’arrête à la gare de Biot, en bas de la commune.",
],[
"<strong>Fernand Léger National Museum</strong>: €8 (€10 during exhibitions), free for EU citizens under 26. Closed on Tuesdays; in winter, 10am–5pm.",
"<strong>Exhibition</strong>: “Léger – Morellet, De-figuring Painting”, 21 November 2026 to 26 April 2027.",
"<strong>Access</strong>: free parking at the museum; TER trains stop at Biot station, at the bottom of the town.",
]),
('grasse','grasse',"Grasse","Grasse",[
"<strong>Musée international de la Parfumerie</strong> : 6 € ; ouvert tous les jours de 10 h à 18 h de septembre à juin, sauf le premier lundi de janvier, février, mars, octobre, novembre et décembre.",
"<strong>Exposition</strong> : « Une nuit au musée – signée Barclay », regard photographique sur les flacons du musée, jusqu’au 7 mars 2027.",
"<strong>En train</strong> : TER jusqu’au terminus Grasse, puis navette vers la gare routière (arrêt Thouron) pour le centre.",
"<strong>Parkings</strong> : cours Honoré-Cresp et La Foux, au plus près du centre historique.",
],[
"<strong>International Perfume Museum</strong>: €6; open daily 10am to 6pm from September to June, except the first Monday of January, February, March, October, November and December.",
"<strong>Exhibition</strong>: “A Night at the Museum – by Barclay”, a photographer’s take on the museum’s bottles, until 7 March 2027.",
"<strong>By train</strong>: TER to the Grasse terminus, then the shuttle to the bus station (Thouron stop) for the centre.",
"<strong>Parking</strong>: cours Honoré-Cresp and La Foux, the closest to the old town.",
]),
('gourdon','gourdon',"Gourdon","Gourdon",[
"<strong>En bus</strong> : la ligne régionale Zou! 651 (Grasse–Vence) dessert la commune et Pont-du-Loup, au pied du village ; vérifiez les horaires sur zou.maregionsud.fr, les passages sont espacés.",
"<strong>En voiture</strong> : c’est le plus simple pour Gourdon ; combinez avec <a href=\"../../cote-d-azur/grasse/\">Grasse</a>, à une vingtaine de minutes.",
],[
"<strong>By bus</strong>: regional Zou! line 651 (Grasse–Vence) serves the area and Pont-du-Loup, at the foot of the village; check times on zou.maregionsud.fr, buses are infrequent.",
"<strong>By car</strong>: the easiest way to reach Gourdon; combine it with <a href=\"../../french-riviera/grasse/\">Grasse</a>, about twenty minutes away.",
]),
('mougins','mougins',"Mougins","Mougins",[
"<strong>En bus depuis Cannes</strong> : Palm Express B ou ligne Zou! 660 depuis la gare jusqu’à Val de Mougins, puis Palm Bus 26 ou 28 jusqu’à l’arrêt Mougins Village.",
"<strong>En voiture</strong> : A8 sortie 42 Cannes-Mougins, direction « Vieux Village » ; parking gratuit à l’entrée du village.",
"<strong>FAMM – Femmes Artistes du Musée de Mougins</strong> : 16 € adultes, 12 € à partir de 64 ans (2026).",
],[
"<strong>By bus from Cannes</strong>: Palm Express B or Zou! line 660 from the station to Val de Mougins, then Palm Bus 26 or 28 to the Mougins Village stop.",
"<strong>By car</strong>: A8 exit 42 Cannes-Mougins, follow “Vieux Village”; free parking at the village entrance.",
"<strong>FAMM – Women Artists Museum of Mougins</strong>: €16 adults, €12 aged 64 and over (2026).",
]),
('saint-paul-de-vence','saint-paul-de-vence',"Saint-Paul-de-Vence","Saint-Paul-de-Vence",[
"<strong>Fondation Maeght</strong> : ouverte tous les jours, de 10 h à 18 h d’octobre à juin ; comptez environ 18 € en plein tarif, gratuit pour les moins de 10 ans.",
"<strong>En bus</strong> : ligne 400 Nice–Vence, arrêt « Fondation Maeght » ou Saint-Paul village.",
],[
"<strong>Fondation Maeght</strong>: open daily, 10am to 6pm from October to June; allow about €18 full price, free for under-10s.",
"<strong>By bus</strong>: line 400 Nice–Vence, “Fondation Maeght” or Saint-Paul village stop.",
]),
('saint-jean-cap-ferrat','saint-jean-cap-ferrat',"Saint-Jean-Cap-Ferrat","Cap Ferrat",[
"<strong>Villa et jardins Ephrussi de Rothschild</strong> : 18 € plein tarif, 12 € pour les 7-17 ans et les étudiants de moins de 25 ans, gratuit avant 7 ans.",
"<strong>Horaires d’hiver</strong> (2 novembre 2026 – 31 janvier 2027) : 10 h–16 h 30 en semaine, 10 h–18 h le week-end et pendant les vacances scolaires. Fermé le 25 décembre.",
"<strong>Accès</strong> : parking gratuit à l’entrée de la villa ; gare TER de Beaulieu-sur-Mer à une vingtaine de minutes à pied.",
],[
"<strong>Villa & Gardens Ephrussi de Rothschild</strong>: €18 full price, €12 for ages 7-17 and students under 25, free under 7.",
"<strong>Winter hours</strong> (2 November 2026 – 31 January 2027): 10am–4:30pm on weekdays, 10am–6pm at weekends and during school holidays. Closed on 25 December.",
"<strong>Access</strong>: free parking at the villa entrance; Beaulieu-sur-Mer TER station is about a 20-minute walk.",
]),
('villefranche-sur-mer','villefranche-sur-mer',"Villefranche-sur-Mer","Villefranche-sur-Mer",[
"<strong>En train</strong> : TER Nice–Menton, moins d’une demi-heure depuis Nice ; la gare est au bord de l’eau, à deux pas de la plage et de la vieille ville.",
"<strong>Citadelle Saint-Elme</strong> : entrée libre ; jardins et courtines visitables en semaine de 10 h à 17 h en hiver. Les salles des musées sont fermées pour rénovation.",
],[
"<strong>By train</strong>: TER Nice–Menton, under half an hour from Nice; the station is by the water, a short walk from the beach and the old town.",
"<strong>Citadelle Saint-Elme</strong>: free entry; gardens and ramparts open on weekdays 10am–5pm in winter. The museum rooms are closed for renovation.",
]),
('roquebrune-cap-martin','roquebrune-cap-martin',"Roquebrune-Cap-Martin","Roquebrune-Cap-Martin",[
"<strong>Cap Moderne</strong> (villa E-1027 d’Eileen Gray, cabanon de Le Corbusier) : <strong>fermé du 1<sup>er</sup> novembre au 31 mars</strong>. Le reste de l’année, visite guidée sur réservation obligatoire : 19 € adultes, 10 € pour les 7-18 ans.",
"<strong>En train</strong> : TER Nice–Vintimille, arrêt Cap-Martin-Roquebrune (gare de Cabbé), à 450 m de l’accueil de Cap Moderne.",
"<strong>En bus</strong> : ligne 100 Nice–Menton, arrêt « Quatre Chemins », puis une vingtaine de minutes à pied.",
],[
"<strong>Cap Moderne</strong> (Eileen Gray’s E-1027 villa, Le Corbusier’s cabanon): <strong>closed from 1 November to 31 March</strong>. The rest of the year, guided tours by compulsory booking: €19 adults, €10 for ages 7-18.",
"<strong>By train</strong>: TER Nice–Ventimiglia, Cap-Martin-Roquebrune stop (Cabbé station), 450 m from the Cap Moderne reception.",
"<strong>By bus</strong>: line 100 Nice–Menton, “Quatre Chemins” stop, then about 20 minutes on foot.",
]),
('saint-tropez','saint-tropez',"Saint-Tropez","Saint-Tropez",[
"<strong>Citadelle et musée d’histoire maritime</strong> : 5 €, 3 € en tarif réduit, gratuit pour les moins de 12 ans. Du 1<sup>er</sup> octobre au 31 mars, 10 h–17 h 30 ; fermé le 25 décembre et le 1<sup>er</sup> janvier.",
"<strong>Musée de la Gendarmerie et du Cinéma</strong> : 5 €, 3 € en tarif réduit.",
"<strong>En bus</strong> : ligne Zou! 876 Saint-Raphaël–Sainte-Maxime–Saint-Tropez, depuis la gare routière située derrière la gare de Saint-Raphaël-Valescure. Les navettes gratuites du village ne roulent que de juin à septembre.",
],[
"<strong>Citadel and Maritime History Museum</strong>: €5, €3 reduced, free for under-12s. From 1 October to 31 March, 10am–5:30pm; closed on 25 December and 1 January.",
"<strong>Gendarmerie and Cinema Museum</strong>: €5, €3 reduced.",
"<strong>By bus</strong>: Zou! line 876 Saint-Raphaël–Sainte-Maxime–Saint-Tropez, from the bus station just behind Saint-Raphaël-Valescure train station. The free village shuttles only run from June to September.",
]),
('porquerolles','porquerolles',"Porquerolles","Porquerolles",[
"<strong>Bateau</strong> : compagnie TLV depuis le port de la Tour Fondue (presqu’île de Giens, Hyères), traversée d’environ 20 minutes.",
"<strong>Tarifs</strong> : aller-retour adulte 17,70 € de novembre à mars, 24 € de mai à septembre ; supplément vélo adulte 17 € aller-retour.",
"<strong>Stationnement</strong> : le parking de la Tour Fondue est payant ; alternative, le parking gratuit Arromanches et le bus 67 (réseau Mistral) jusqu’à l’embarcadère, sans vélo à bord.",
],[
"<strong>Boat</strong>: TLV from La Tour Fondue harbour (Giens peninsula, Hyères), a crossing of about 20 minutes.",
"<strong>Fares</strong>: adult return €17.70 from November to March, €24 from May to September; adult bike supplement €17 return.",
"<strong>Parking</strong>: the Tour Fondue car park is paid; alternatively use the free Arromanches car park and bus 67 (Mistral network) to the pier, no bikes on board.",
]),
('gorges-du-verdon','verdon-gorge',"les gorges du Verdon","the Verdon Gorge",[
"<strong>Route des Crêtes (D23)</strong> : la portion à sens unique entre le Jas d’Aire et La Maline est fermée du 4<sup>e</sup> vendredi de novembre au 4<sup>e</sup> vendredi de mars, soit du 27 novembre 2026 au 26 mars 2027. Départ à 800 m de La Palud-sur-Verdon.",
"<strong>Belvédères</strong> : accès gratuit, sous réserve de météo et d’enneigement en hiver.",
],[
"<strong>Route des Crêtes (D23)</strong>: the one-way section between Jas d’Aire and La Maline is closed from the 4th Friday of November to the 4th Friday of March, i.e. 27 November 2026 to 26 March 2027. It starts 800 m from La Palud-sur-Verdon.",
"<strong>Viewpoints</strong>: free, subject to weather and snow in winter.",
]),
('massif-de-l-esterel','esterel-massif',"le massif de l’Estérel","the Esterel",[
"<strong>En train</strong> : le TER s’arrête à Agay et au Trayas ; une boucle balisée part de la gare du Trayas vers le Pic de l’Ours (492 m).",
"<strong>En voiture</strong> : depuis le rond-point d’Agay, suivez « Massif de l’Estérel » puis « Pic de l’Ours » jusqu’au parking du col Notre-Dame.",
"<strong>Risque incendie</strong> : de fin juin à fin septembre, l’accès au massif dépend chaque jour de la carte de risque de la préfecture ; il peut être interdit. En hiver, pas de restriction habituelle.",
],[
"<strong>By train</strong>: TER trains stop at Agay and Le Trayas; a marked loop leaves Le Trayas station for the Pic de l’Ours (492 m).",
"<strong>By car</strong>: from the Agay roundabout follow “Massif de l’Estérel”, then “Pic de l’Ours” to the Col Notre-Dame car park.",
"<strong>Fire risk</strong>: from late June to late September, access to the massif depends on the prefecture’s daily risk map and can be banned. No usual restriction in winter.",
]),
]
NOTE_FR = "<p class=\"maj\">Tarifs et horaires relevés en novembre 2026 auprès des offices de tourisme et des sites ; ils peuvent changer, vérifiez avant de partir.</p>"
NOTE_EN = "<p class=\"maj\">Prices and opening hours checked in November 2026 with tourist offices and the sites themselves; they can change, so check before you go.</p>"
def nb(s): return ''.join(x if x.startswith('<') else re.sub(r' ([:;?!])', ' \\1', x) for x in re.split(r'(<[^>]+>)', s))
n=0
for sf,se,nf,ne,fr,en in D:
  for path,lang,name,items in ((FR+sf,'fr',nf,fr),(EN+se,'en',ne,en)):
    f=path+'/index.html'; h=open(f,encoding='utf-8').read()
    if 'id="infos-2026"' in h: continue
    if lang=='fr':
      sec='<h2 id="infos-2026">Infos pratiques 2026 : '+name+'</h2><ul>'+''.join('<li>'+i+'</li>' for i in items)+'</ul>'+NOTE_FR
      sec=nb(sec); key='<h2>Nos conseils'
    else:
      sec='<h2 id="infos-2026">Practical info 2026: '+name[0].upper()+name[1:]+'</h2><ul>'+''.join('<li>'+i+'</li>' for i in items)+'</ul>'+NOTE_EN
      key='<h2>Tips for'
    assert h.count(key)==1,(f,key)
    h=h.replace(key,sec+'\n    '+key); open(f,'w',encoding='utf-8').write(h); n+=1
print(n)
