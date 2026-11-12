import re
FR = '/home/claude/clicandsite-guide/paris/'
EN = '/home/claude/clicandsite-guide-en/paris/'
EEE_FR = "visiteurs de l’Espace économique européen (UE, Islande, Liechtenstein, Norvège)"
D = [
('louvre','louvre',"le Louvre","the Louvre",[
"<strong>Tarifs</strong> : 22 € pour les résidents et ressortissants de l’EEE, 32 € pour les autres visiteurs depuis le 14 janvier 2026 ; gratuit pour les moins de 18 ans, quelle que soit la nationalité.",
"<strong>Horaires</strong> : 9 h–18 h, jusqu’à 21 h le mercredi et le vendredi ; fermé le mardi, ainsi que les 1<sup>er</sup> janvier, 1<sup>er</sup> mai et 25 décembre. Dernière entrée une heure avant la fermeture.",
"<strong>Gratuité pour tous</strong> : le premier vendredi du mois après 18 h (sauf juillet et août).",
"<strong>Réservation</strong> : fortement recommandée, y compris pour les visiteurs qui entrent gratuitement.",
],[
"<strong>Prices</strong>: €22 for residents and citizens of the EEA (EU, Iceland, Liechtenstein, Norway), €32 for everyone else since 14 January 2026; free for under-18s of any nationality.",
"<strong>Opening hours</strong>: 9am–6pm, until 9pm on Wednesdays and Fridays; closed on Tuesdays and on 1 January, 1 May and 25 December. Last entry one hour before closing.",
"<strong>Free for everyone</strong>: the first Friday of the month after 6pm (except July and August).",
"<strong>Booking</strong>: strongly recommended, even if you qualify for free entry.",
]),
('tour-eiffel','eiffel-tower',"la tour Eiffel","the Eiffel Tower",[
"<strong>Tarifs adultes 2026</strong> : sommet en ascenseur 36,70 € ; 2<sup>e</sup> étage en ascenseur 23,50 € ; escaliers jusqu’au 2<sup>e</sup> étage 14,80 € ; escaliers jusqu’au 2<sup>e</sup> puis ascenseur jusqu’au sommet 28 €.",
"<strong>Bon à savoir</strong> : le sommet n’est accessible qu’en ascenseur ; les escaliers publics s’arrêtent au 2<sup>e</sup> étage (674 marches).",
"<strong>Nouvelle grille</strong> : l’exploitant applique de nouveaux tarifs à partir du 11 janvier 2027 ; les prix ci-dessus valent jusqu’au 10 janvier 2027.",
"<strong>Réservation</strong> : achetez sur le site officiel avec un créneau horaire, c’est là que les tarifs sont les plus bas.",
],[
"<strong>2026 adult prices</strong>: summit by lift €36.70; 2nd floor by lift €23.50; stairs to the 2nd floor €14.80; stairs to the 2nd floor then lift to the summit €28.",
"<strong>Good to know</strong>: the summit can only be reached by lift; the public stairs stop at the 2nd floor (674 steps).",
"<strong>New prices</strong>: the operator introduces new fares from 11 January 2027; the prices above apply until 10 January 2027.",
"<strong>Booking</strong>: buy on the official website with a time slot, where prices are lowest.",
]),
('versailles','versailles',"Versailles","Versailles",[
"<strong>Billet Passeport</strong> (château, Trianon, jardins) : en basse saison, 22 € pour les visiteurs de l’EEE et 25 € pour les autres ; en haute saison, 32 € et 35 €.",
"<strong>Gratuit</strong> pour les moins de 18 ans et pour les résidents de l’UE de moins de 26 ans ; gratuit pour tous le premier dimanche du mois, de novembre à mars.",
"<strong>Fermé le lundi</strong>, ainsi que le 1<sup>er</sup> janvier, le 1<sup>er</sup> mai et le 25 décembre. Réservation d’un créneau horaire obligatoire pour le château.",
],[
"<strong>Passport ticket</strong> (palace, Trianon, gardens): in low season €22 for EEA visitors and €25 for everyone else; in high season €32 and €35.",
"<strong>Free</strong> for under-18s and EU residents under 26; free for everyone on the first Sunday of the month from November to March.",
"<strong>Closed on Mondays</strong> and on 1 January, 1 May and 25 December. A timed slot is required for the palace.",
]),
('musee-d-orsay','musee-d-orsay',"le musée d’Orsay","the Musée d’Orsay",[
"<strong>Tarifs</strong> : 16 € en ligne avec créneau (14 € sur place, sans garantie d’entrée le jour même) ; nocturne du jeudi 12 € ; gratuit pour les moins de 18 ans.",
"<strong>Horaires</strong> : du mardi au dimanche à partir de 9 h 30, jusqu’à 21 h 45 le jeudi ; fermé le lundi.",
"<strong>40 ans</strong> : le musée fête son 40<sup>e</sup> anniversaire en 2026. L’Orangerie, gérée par le même établissement, est fermée le mardi : faites Orsay le mardi et l’Orangerie un autre jour.",
],[
"<strong>Prices</strong>: €16 online with a time slot (€14 at the desk, with no guaranteed same-day entry); Thursday late opening €12; free for under-18s.",
"<strong>Opening hours</strong>: Tuesday to Sunday from 9:30am, until 9:45pm on Thursdays; closed on Mondays.",
"<strong>40 years</strong>: the museum celebrates its 40th anniversary in 2026. The Orangerie, run by the same body, is closed on Tuesdays: do Orsay on a Tuesday and the Orangerie another day.",
]),
('musee-de-l-orangerie','musee-de-l-orangerie',"le musée de l’Orangerie","the Musée de l’Orangerie",[
"<strong>Tarif</strong> : 12,50 € ; gratuit le premier dimanche du mois, sur réservation. Un créneau horaire est indispensable pour tous les visiteurs, même gratuits.",
"<strong>Horaires</strong> : 9 h–18 h ; fermé le mardi.",
"<strong>Exposition</strong> : « Monet, peindre le temps », pour le centenaire de la mort du peintre, du 30 septembre 2026 au 25 janvier 2027.",
],[
"<strong>Price</strong>: €12.50; free on the first Sunday of the month, with a booking. A time slot is required for every visitor, even free ones.",
"<strong>Opening hours</strong>: 9am–6pm; closed on Tuesdays.",
"<strong>Exhibition</strong>: “Monet, painting time”, marking 100 years since the painter’s death, 30 September 2026 to 25 January 2027.",
]),
('sainte-chapelle','sainte-chapelle',"la Sainte-Chapelle","the Sainte-Chapelle",[
"<strong>Tarifs depuis le 12 janvier 2026</strong> : 16 € pour les visiteurs de l’EEE, 22 € pour les autres.",
"<strong>Billet jumelé Sainte-Chapelle + Conciergerie</strong> : 23 € (EEE) ou 30 € (hors EEE). Les deux monuments sont voisins sur l’île de la Cité.",
"<strong>Fermetures</strong> : 1<sup>er</sup> janvier, 1<sup>er</sup> mai et 25 décembre.",
],[
"<strong>Prices since 12 January 2026</strong>: €16 for EEA visitors, €22 for everyone else.",
"<strong>Sainte-Chapelle + Conciergerie combined ticket</strong>: €23 (EEA) or €30 (non-EEA). The two monuments stand side by side on the Île de la Cité.",
"<strong>Closed</strong>: 1 January, 1 May and 25 December.",
]),
('conciergerie','conciergerie',"la Conciergerie","the Conciergerie",[
"<strong>Tarif</strong> : 13 € ; le HistoPad (tablette de visite) est inclus.",
"<strong>Billet jumelé avec la Sainte-Chapelle</strong> : 23 € pour les visiteurs de l’EEE, 30 € pour les autres.",
"<strong>Fermetures</strong> : 1<sup>er</sup> mai et 25 décembre.",
],[
"<strong>Price</strong>: €13; the HistoPad tablet is included.",
"<strong>Combined ticket with the Sainte-Chapelle</strong>: €23 for EEA visitors, €30 for everyone else.",
"<strong>Closed</strong>: 1 May and 25 December.",
]),
('arc-de-triomphe','arc-de-triomphe',"l’Arc de Triomphe","the Arc de Triomphe",[
"<strong>Tarif</strong> : 16 € en ligne en basse saison (octobre à mars) ; gratuit pour les moins de 18 ans. La terrasse panoramique est à 50 m de haut.",
"<strong>Accès</strong> : uniquement par les passages souterrains depuis les Champs-Élysées ou l’avenue de la Grande-Armée ; ne traversez jamais le rond-point.",
"<strong>Fermetures</strong> : 1<sup>er</sup> janvier, 11 novembre et 25 décembre. Dernier accès 45 minutes avant la fermeture.",
],[
"<strong>Price</strong>: €16 online in low season (October to March); free for under-18s. The panoramic terrace is 50 m up.",
"<strong>Access</strong>: only through the underpasses from the Champs-Élysées or avenue de la Grande-Armée; never try to cross the roundabout.",
"<strong>Closed</strong>: 1 January, 11 November and 25 December. Last entry 45 minutes before closing.",
]),
('pantheon','pantheon',"le Panthéon","the Panthéon",[
"<strong>Tarif</strong> : de 13 à 16 € selon la saison (le tarif bas s’applique d’octobre à mars) ; gratuit pour les moins de 18 ans.",
"<strong>Exposition</strong> : « Vies minuscules », avec le Centre Pompidou, sous la nef du 24 septembre 2026 au 31 janvier 2027.",
],[
"<strong>Price</strong>: €13 to €16 depending on the season (the lower price applies October to March); free for under-18s.",
"<strong>Exhibition</strong>: “Vies minuscules”, with the Centre Pompidou, under the nave from 24 September 2026 to 31 January 2027.",
]),
('notre-dame','notre-dame',"Notre-Dame","Notre-Dame",[
"<strong>Cathédrale</strong> : entrée gratuite. Une réservation gratuite (facultative) ouvre 2 à 3 jours avant sur le site officiel et évite la file.",
"<strong>Horaires</strong> : en semaine de 7 h 45 environ à 19 h, jusqu’à 22 h le jeudi ; le week-end de 8 h 15 à 19 h 30.",
"<strong>Tours</strong> : 16 €, vente uniquement en ligne, aucune entrée sans réservation (gratuit pour les moins de 18 ans, créneau obligatoire). <strong>Trésor</strong> : 12 €. <strong>Crypte archéologique</strong> : 9 €.",
"<strong>Marché de Noël</strong> : square René-Viviani, face à la cathédrale, du 26 novembre au 27 décembre 2026.",
],[
"<strong>Cathedral</strong>: free entry. A free (optional) booking opens 2 to 3 days ahead on the official website and lets you skip the queue.",
"<strong>Opening hours</strong>: weekdays from about 7:45am to 7pm, until 10pm on Thursdays; weekends 8:15am to 7:30pm.",
"<strong>Towers</strong>: €16, sold online only, no entry without a booking (free for under-18s, slot still required). <strong>Treasury</strong>: €12. <strong>Archaeological crypt</strong>: €9.",
"<strong>Christmas market</strong>: square René-Viviani, facing the cathedral, 26 November to 27 December 2026.",
]),
('sacre-coeur','sacre-coeur',"le Sacré-Cœur","the Sacré-Cœur",[
"<strong>Basilique</strong> : entrée libre, tous les jours de 6 h 30 à 22 h 30.",
"<strong>Dôme</strong> : 8 €, 5 € pour les moins de 16 ans ; environ 300 marches, sans ascenseur.",
"<strong>Funiculaire</strong> : un ticket Métro-Train-RER à 2,55 € ; attention, un ticket déjà validé dans le métro ne fonctionne plus pour le funiculaire. Métro Anvers (ligne 2).",
],[
"<strong>Basilica</strong>: free entry, daily 6:30am to 10:30pm.",
"<strong>Dome</strong>: €8, €5 for under-16s; about 300 steps, no lift.",
"<strong>Funicular</strong>: one Métro-Train-RER ticket at €2.55; note that a ticket already validated in the métro no longer works for the funicular. Métro Anvers (line 2).",
]),
('montmartre','montmartre',"Montmartre","Montmartre",[
"<strong>Monter sans effort</strong> : le funiculaire depuis la place Saint-Pierre (ticket Métro-Train-RER à 2,55 €, à valider à nouveau même si vous sortez du métro), ou le Montmartrobus (ligne 40) depuis Pigalle.",
"<strong>Métros</strong> : Anvers (ligne 2) pour le funiculaire et le Sacré-Cœur, Abbesses (ligne 12) pour le cœur du village.",
"<strong>Dôme du Sacré-Cœur</strong> : 8 € (5 € pour les moins de 16 ans), la basilique elle-même est gratuite.",
],[
"<strong>Getting up without effort</strong>: the funicular from place Saint-Pierre (one Métro-Train-RER ticket at €2.55, to be validated again even if you come straight from the métro), or the Montmartrobus (line 40) from Pigalle.",
"<strong>Métro stations</strong>: Anvers (line 2) for the funicular and Sacré-Cœur, Abbesses (line 12) for the heart of the village.",
"<strong>Sacré-Cœur dome</strong>: €8 (€5 for under-16s); the basilica itself is free.",
]),
('moulin-rouge','moulin-rouge',"le Moulin Rouge","the Moulin Rouge",[
"<strong>Revue Féerie</strong> : à 21 h et à 23 h ; spectacle avec une demi-bouteille de champagne à partir de 142 €, dîner-spectacle (19 h) à partir de 255 €.",
"<strong>En hiver</strong> : jusqu’à fin mars, la séance de 23 h n’a lieu que le vendredi et le samedi.",
"<strong>Noël</strong> : dîner-spectacle du 24 décembre 2026 à 290 €, champagne compris. Enfants acceptés à partir de 6 ans. Métro Blanche (ligne 2).",
],[
"<strong>Féerie revue</strong>: at 9pm and 11pm; show with half a bottle of champagne from €142, dinner and show (7pm) from €255.",
"<strong>In winter</strong>: until the end of March, the 11pm show only runs on Fridays and Saturdays.",
"<strong>Christmas</strong>: dinner and show on 24 December 2026 at €290, champagne included. Children admitted from age 6. Métro Blanche (line 2).",
]),
('crazy-horse','crazy-horse',"le Crazy Horse","the Crazy Horse",[
"<strong>Spectacle « Totally Crazy! »</strong> : du dimanche au vendredi à 20 h et 22 h 30 ; le samedi à 19 h, 21 h 30 et 23 h 45.",
"<strong>Tarifs</strong> : de 115 à 295 € selon la formule (revue seule, champagne, dîner, coulisses).",
"<strong>75 ans</strong> : le cabaret fête ses 75 ans en 2026. Adresse : 12 avenue George-V ; parking Alma–George-V au n° 10.",
],[
"<strong>“Totally Crazy!” show</strong>: Sunday to Friday at 8pm and 10:30pm; Saturday at 7pm, 9:30pm and 11:45pm.",
"<strong>Prices</strong>: €115 to €295 depending on the package (show only, champagne, dinner, backstage).",
"<strong>75 years</strong>: the cabaret turns 75 in 2026. Address: 12 avenue George-V; Alma–George-V car park at no. 10.",
]),
('croisiere-sur-la-seine','seine-cruise',"la croisière sur la Seine","your Seine cruise",[
"<strong>Bateaux-Mouches</strong> : embarquement Port de la Conférence, au pied du pont de l’Alma (rive droite) ; croisière promenade d’environ 1 h 10.",
"<strong>Tarifs</strong> : 20 € adulte sur place, 17 € en ligne ; 4-12 ans 10 € sur place, 8 € en ligne ; gratuit avant 4 ans. Parking gratuit sur le quai pendant la croisière.",
"<strong>Accès</strong> : métro Alma-Marceau (ligne 9) ou Franklin-D.-Roosevelt (ligne 1), RER C Pont de l’Alma.",
],[
"<strong>Bateaux-Mouches</strong>: boarding at Port de la Conférence, at the foot of the Pont de l’Alma (right bank); sightseeing cruise of about 1h10.",
"<strong>Fares</strong>: adults €20 at the desk, €17 online; ages 4-12 €10 at the desk, €8 online; free under 4. Free parking on the quay during the cruise.",
"<strong>Getting there</strong>: métro Alma-Marceau (line 9) or Franklin-D.-Roosevelt (line 1), RER C Pont de l’Alma.",
]),
('disneyland-paris','disneyland-paris',"Disneyland Paris","Disneyland Paris",[
"<strong>Noël Enchanté Disney</strong> : du samedi 7 novembre 2026 au mercredi 6 janvier 2027, dans le Parc Disneyland et, pour la première fois, dans le Monde de La Reine des Neiges (Disney Adventure World).",
"<strong>Affluence</strong> : novembre hors vacances scolaires est nettement plus calme que décembre ; évitez les 24, 25, 26 décembre et le 1<sup>er</sup> janvier.",
"<strong>Y aller</strong> : RER A jusqu’à Marne-la-Vallée–Chessy, la gare est à l’entrée des parcs.",
],[
"<strong>Disney’s Enchanted Christmas</strong>: Saturday 7 November 2026 to Wednesday 6 January 2027, in Disneyland Park and, for the first time, in the World of Frozen (Disney Adventure World).",
"<strong>Crowds</strong>: November outside school holidays is much quieter than December; avoid 24, 25, 26 December and 1 January.",
"<strong>Getting there</strong>: RER A to Marne-la-Vallée–Chessy, the station is at the park gates.",
]),
('fondation-louis-vuitton','fondation-louis-vuitton',"la Fondation Louis Vuitton","the Louis Vuitton Foundation",[
"<strong>Exposition</strong> : « Gustave Fayet, collectionneur-créateur », du 9 octobre 2026 au 8 mars 2027, avec l’<em>Autoportrait à l’oreille bandée</em> de Van Gogh.",
"<strong>Tarifs</strong> : 18 € plein tarif, 10 € étudiants, 5 € moins de 18 ans ; le billet donne aussi accès au Jardin d’Acclimatation. Fermé le mardi.",
"<strong>Navette</strong> : départ 44 avenue de Friedland (sortie 2 du métro Charles-de-Gaulle–Étoile), environ toutes les 20 minutes. Sinon métro Les Sablons (ligne 1).",
],[
"<strong>Exhibition</strong>: “Gustave Fayet, collector-creator”, 9 October 2026 to 8 March 2027, including Van Gogh’s <em>Self-Portrait with Bandaged Ear and Pipe</em>.",
"<strong>Prices</strong>: €18 full price, €10 students, €5 under-18s; the ticket also covers the Jardin d’Acclimatation. Closed on Tuesdays.",
"<strong>Shuttle</strong>: from 44 avenue de Friedland (exit 2 of Charles-de-Gaulle–Étoile métro), about every 20 minutes. Otherwise métro Les Sablons (line 1).",
]),
('fontainebleau','fontainebleau',"Fontainebleau","Fontainebleau",[
"<strong>Château</strong> : 17 € plein tarif, 15 € réduit ; gratuit pour les moins de 18 ans et les 18-25 ans de l’UE, et pour tous le premier dimanche du mois (sauf juillet et août).",
"<strong>Horaires</strong> : d’octobre à mars, 9 h 30–17 h (dernier accès 45 minutes avant) ; fermé le mardi, le 1<sup>er</sup> janvier, le 1<sup>er</sup> mai et le 25 décembre. Les cours et les jardins sont gratuits, même le mardi.",
"<strong>Depuis Paris</strong> : Transilien R depuis la gare de Lyon jusqu’à Fontainebleau-Avon, puis bus 1 jusqu’au château.",
],[
"<strong>Palace</strong>: €17 full price, €15 reduced; free for under-18s and EU citizens aged 18-25, and for everyone on the first Sunday of the month (except July and August).",
"<strong>Opening hours</strong>: October to March, 9:30am–5pm (last entry 45 minutes before); closed on Tuesdays, 1 January, 1 May and 25 December. The courtyards and gardens are free, even on Tuesdays.",
"<strong>From Paris</strong>: Transilien line R from Gare de Lyon to Fontainebleau-Avon, then bus 1 to the palace.",
]),
('chantilly','chantilly',"Chantilly","Chantilly",[
"<strong>Billet Domaine</strong> (château et musée Condé, parc, Grandes Écuries, musée du Cheval) : 18 €, 14,50 € en tarif réduit ; gratuit avant 7 ans.",
"<strong>Horaires d’hiver</strong> (novembre à mars) : château 10 h–17 h, Grandes Écuries 12 h–17 h, parc 10 h–18 h ; fermé le mardi, et fermeture annuelle en janvier.",
"<strong>Accès</strong> : TER depuis Paris-Gare du Nord jusqu’à Chantilly-Gouvieux ; en voiture, parking à 5 €.",
],[
"<strong>Estate ticket</strong> (château and Musée Condé, park, Great Stables, Horse Museum): €18, €14.50 reduced; free under 7.",
"<strong>Winter hours</strong> (November to March): château 10am–5pm, Great Stables noon–5pm, park 10am–6pm; closed on Tuesdays, with an annual closure in January.",
"<strong>Getting there</strong>: TER from Paris-Gare du Nord to Chantilly-Gouvieux; by car, parking costs €5.",
]),
('invalides','invalides',"les Invalides","Les Invalides",[
"<strong>Musée de l’Armée</strong> (tombeau de Napoléon inclus) : 17 € plein tarif.",
"<strong>Horaires</strong> : tous les jours de 10 h à 18 h ; fermé les 1<sup>er</sup> janvier, 1<sup>er</sup> mai et 25 décembre.",
"<strong>Billet combiné avec le musée Rodin</strong> voisin : 26 €. Deux entrées : 129 rue de Grenelle ou 2 place Vauban, côté Dôme.",
],[
"<strong>Army Museum</strong> (Napoleon’s tomb included): €17 full price.",
"<strong>Opening hours</strong>: daily 10am to 6pm; closed on 1 January, 1 May and 25 December.",
"<strong>Combined ticket with the nearby Rodin Museum</strong>: €26. Two entrances: 129 rue de Grenelle or 2 place Vauban, on the Dome side.",
]),
('musee-rodin','musee-rodin',"le musée Rodin","the Rodin Museum",[
"<strong>Tarif</strong> : 15 € ; fermé le lundi.",
"<strong>Billet combiné avec le musée de l’Armée</strong> (Invalides, à deux pas) : 26 €.",
"<strong>Accès</strong> : 79 rue de Varenne, métro Varenne (ligne 13) à deux minutes à pied.",
],[
"<strong>Price</strong>: €15; closed on Mondays.",
"<strong>Combined ticket with the Army Museum</strong> (Invalides, next door): €26.",
"<strong>Getting there</strong>: 79 rue de Varenne, métro Varenne (line 13), two minutes on foot.",
]),
('musee-picasso','musee-picasso',"le musée Picasso","the Picasso Museum",[
"<strong>Tarif</strong> : 16 € ; gratuit pour les moins de 18 ans et pour les résidents de l’UE de moins de 26 ans, et pour tous le premier dimanche du mois.",
"<strong>Horaires</strong> : du mardi au dimanche, 9 h 30–18 h (dernier accès 17 h 15) ; fermé le lundi, les 1<sup>er</sup> janvier, 1<sup>er</sup> mai et 25 décembre.",
"<strong>Adresse</strong> : hôtel Salé, 5 rue de Thorigny, dans le Marais.",
],[
"<strong>Price</strong>: €16; free for under-18s and EU residents under 26, and for everyone on the first Sunday of the month.",
"<strong>Opening hours</strong>: Tuesday to Sunday, 9:30am–6pm (last entry 5:15pm); closed on Mondays, 1 January, 1 May and 25 December.",
"<strong>Address</strong>: Hôtel Salé, 5 rue de Thorigny, in the Marais.",
]),
('musee-grevin','musee-grevin',"le musée Grévin","the Grévin",[
"<strong>Tarifs</strong> : billet daté en ligne à partir de 19 € adulte et 16,50 € enfant (5-18 ans) ; nettement plus cher au guichet ; gratuit avant 5 ans.",
"<strong>Horaires</strong> : ouvert tous les jours, 10 h–18 h en semaine, 9 h 30–19 h le week-end, les jours fériés et pendant les vacances scolaires.",
"<strong>Nouveauté</strong> : l’équipage de One Piece a rejoint le musée en juin 2026. Adresse : 10 boulevard Montmartre.",
],[
"<strong>Prices</strong>: dated online ticket from €19 for adults and €16.50 for children (5-18); much more at the desk; free under 5.",
"<strong>Opening hours</strong>: open daily, 10am–6pm on weekdays, 9:30am–7pm at weekends, on public holidays and during school holidays.",
"<strong>New</strong>: the One Piece crew joined the museum in June 2026. Address: 10 boulevard Montmartre.",
]),
('catacombes','catacombs',"les Catacombes","the Catacombs",[
"<strong>Réouverture</strong> : les Catacombes ont rouvert le 8 avril 2026 après plusieurs mois de rénovation.",
"<strong>Tarifs</strong> (audioguide inclus) : 31 € plein tarif, 25 € réduit, 15 € pour les 8-17 ans ; gratuit avant 8 ans.",
"<strong>Réservation obligatoire</strong> en ligne : les créneaux ouvrent 7 jours à l’avance. Ouvert du mardi au dimanche, 9 h 45–20 h 30 (dernière entrée 19 h 30) ; fermé le lundi.",
"<strong>Exposition</strong> : « Nadar : inventer Paris, des profondeurs au ciel », du 29 septembre 2026 au 31 janvier 2027, comprise dans le billet. Métro et RER Denfert-Rochereau.",
],[
"<strong>Reopening</strong>: the Catacombs reopened on 8 April 2026 after several months of renovation.",
"<strong>Prices</strong> (audio guide included): €31 full price, €25 reduced, €15 for ages 8-17; free under 8.",
"<strong>Online booking required</strong>: slots open 7 days ahead. Open Tuesday to Sunday, 9:45am–8:30pm (last entry 7:30pm); closed on Mondays.",
"<strong>Exhibition</strong>: “Nadar: inventing Paris, from the depths to the sky”, 29 September 2026 to 31 January 2027, included in the ticket. Métro and RER Denfert-Rochereau.",
]),
('pere-lachaise','pere-lachaise',"le Père-Lachaise","Père Lachaise",[
"<strong>Entrée</strong> : gratuite, tous les jours.",
"<strong>Horaires d’hiver</strong> (6 novembre – 15 mars) : 8 h–17 h 30 en semaine, 8 h 30–17 h 30 le samedi, 9 h–17 h le dimanche et les jours fériés. Les fontaines sont fermées en hiver.",
"<strong>Accès</strong> : entrée principale boulevard de Ménilmontant (métro Philippe-Auguste, ligne 2) ; porte des Amandiers face au métro Père-Lachaise (lignes 2 et 3) ; porte Gambetta (métro Gambetta, ligne 3).",
],[
"<strong>Entry</strong>: free, every day.",
"<strong>Winter hours</strong> (6 November – 15 March): 8am–5:30pm on weekdays, 8:30am–5:30pm on Saturdays, 9am–5pm on Sundays and public holidays. Fountains are shut in winter.",
"<strong>Access</strong>: main gate on boulevard de Ménilmontant (métro Philippe-Auguste, line 2); Porte des Amandiers opposite Père-Lachaise métro (lines 2 and 3); Porte Gambetta (métro Gambetta, line 3).",
]),
('champs-elysees','champs-elysees',"les Champs-Élysées","the Champs-Élysées",[
"<strong>Illuminations de Noël</strong> : allumage le dimanche 22 novembre 2026, puis tous les soirs jusqu’au 3 janvier 2027.",
"<strong>Marché de Noël</strong> : il revient sur l’avenue après une dizaine d’années d’absence, à partir du 22 novembre 2026, entre la place de la Concorde et le rond-point des Champs-Élysées.",
"<strong>Arc de Triomphe</strong> : 16 € en ligne en basse saison, accès uniquement par les passages souterrains.",
],[
"<strong>Christmas lights</strong>: switched on Sunday 22 November 2026, then every evening until 3 January 2027.",
"<strong>Christmas market</strong>: back on the avenue after about ten years away, from 22 November 2026, between place de la Concorde and the Rond-Point des Champs-Élysées.",
"<strong>Arc de Triomphe</strong>: €16 online in low season, reached only through the underpasses.",
]),
('galeries-lafayette','galeries-lafayette',"les Galeries Lafayette","Galeries Lafayette",[
"<strong>Noël 2026</strong> : vitrines animées et sapin géant sous la coupole à partir du 14 novembre 2026.",
"<strong>Autres vitrines du quartier</strong> : Printemps Haussmann dès le 7 novembre, BHV Marais dès le 6 novembre, Bon Marché et Samaritaine dès le 8 novembre.",
"<strong>Bon à savoir</strong> : venez en semaine en fin de matinée ; les week-ends de décembre, le trottoir du boulevard Haussmann devient difficile à pratiquer.",
],[
"<strong>Christmas 2026</strong>: animated windows and the giant tree under the dome from 14 November 2026.",
"<strong>Other windows nearby</strong>: Printemps Haussmann from 7 November, BHV Marais from 6 November, Bon Marché and Samaritaine from 8 November.",
"<strong>Good to know</strong>: come on a weekday in late morning; on December weekends the boulevard Haussmann pavement gets very crowded.",
]),
('noel-a-paris','christmas-in-paris',"Noël à Paris","Christmas in Paris",[
"<strong>Marché de Noël des Tuileries</strong> : du 14 novembre 2026 au 3 janvier 2027, tous les jours de 11 h à 23 h 30.",
"<strong>Marché de Notre-Dame</strong> : square René-Viviani, du 26 novembre au 27 décembre 2026. <strong>La Défense</strong> : du 12 novembre au 31 décembre 2026.",
"<strong>Champs-Élysées</strong> : illuminations dès le 22 novembre 2026 et retour du marché de Noël sur l’avenue.",
"<strong>Vitrines des grands magasins</strong> : BHV 6 novembre, Printemps 7 novembre, Bon Marché et Samaritaine 8 novembre, Galeries Lafayette 14 novembre.",
],[
"<strong>Tuileries Christmas market</strong>: 14 November 2026 to 3 January 2027, daily 11am to 11:30pm.",
"<strong>Notre-Dame market</strong>: square René-Viviani, 26 November to 27 December 2026. <strong>La Défense</strong>: 12 November to 31 December 2026.",
"<strong>Champs-Élysées</strong>: lights from 22 November 2026, and the Christmas market is back on the avenue.",
"<strong>Department store windows</strong>: BHV 6 November, Printemps 7 November, Bon Marché and Samaritaine 8 November, Galeries Lafayette 14 November.",
]),
('opera-garnier','palais-garnier',"l’Opéra Garnier","the Palais Garnier",[
"<strong>Visite libre</strong> : 15 € pour les adultes de l’EEE, 25 € pour les autres ; 13-25 ans 10 € (EEE) ou 20 € (hors EEE).",
"<strong>Visite guidée</strong> : 35 € ; visite Flash de 45 minutes 25 € (15 € pour l’EEE).",
"<strong>Bon à savoir</strong> : valises et sacs de voyage refusés, pas de vestiaire pendant les visites. Entrée à l’angle des rues Scribe et Auber.",
],[
"<strong>Self-guided visit</strong>: €15 for EEA adults, €25 for everyone else; ages 13-25 €10 (EEA) or €20 (non-EEA).",
"<strong>Guided tour</strong>: €35; 45-minute Flash tour €25 (€15 for EEA visitors).",
"<strong>Good to know</strong>: suitcases and travel bags are refused and there is no cloakroom during visits. Entrance at the corner of rue Scribe and rue Auber.",
]),
('le-marais','le-marais',"le Marais","the Marais",[
"<strong>Musée Picasso</strong> (5 rue de Thorigny) : 16 €, fermé le lundi, gratuit le premier dimanche du mois.",
"<strong>Noël</strong> : vitrines du BHV Marais dès le 6 novembre 2026.",
],[
"<strong>Picasso Museum</strong> (5 rue de Thorigny): €16, closed on Mondays, free on the first Sunday of the month.",
"<strong>Christmas</strong>: BHV Marais windows from 6 November 2026.",
]),
('quartier-latin','latin-quarter',"le Quartier latin","the Latin Quarter",[
"<strong>Panthéon</strong> : de 13 à 16 € selon la saison ; exposition « Vies minuscules » sous la nef jusqu’au 31 janvier 2027.",
"<strong>Marché de Noël de Notre-Dame</strong> : square René-Viviani (5<sup>e</sup>), du 26 novembre au 27 décembre 2026.",
],[
"<strong>Panthéon</strong>: €13 to €16 depending on the season; “Vies minuscules” exhibition under the nave until 31 January 2027.",
"<strong>Notre-Dame Christmas market</strong>: square René-Viviani (5th), 26 November to 27 December 2026.",
]),
('saint-germain-des-pres','saint-germain-des-pres',"Saint-Germain-des-Prés","Saint-Germain-des-Prés",[
"<strong>Noël</strong> : vitrines du Bon Marché Rive Gauche dès le 8 novembre 2026.",
"<strong>À pied</strong> : le musée d’Orsay (16 € en ligne, fermé le lundi) et le musée Rodin (15 €, fermé le lundi) sont à distance de marche.",
],[
"<strong>Christmas</strong>: Bon Marché Rive Gauche windows from 8 November 2026.",
"<strong>On foot</strong>: the Musée d’Orsay (€16 online, closed on Mondays) and the Rodin Museum (€15, closed on Mondays) are within walking distance.",
]),
]
NOTE_FR = "<p class=\"maj\">Tarifs et horaires relevés en novembre 2026 auprès des sites officiels et de l’office de tourisme de Paris ; ils peuvent changer, vérifiez avant de partir.</p>"
NOTE_EN = "<p class=\"maj\">Prices and opening hours checked in November 2026 with the official sites and the Paris tourist office; they can change, so check before you go.</p>"
def nb(s): return ''.join(x if x.startswith('<') else re.sub(r' ([:;?!])', ' \\1', x) for x in re.split(r'(<[^>]+>)', s))
n=0
for sf,se,nf,ne,fr,en in D:
  for path,lang,name,items in ((FR+sf,'fr',nf,fr),(EN+se,'en',ne,en)):
    f=path+'/index.html'; h=open(f,encoding='utf-8').read()
    if 'id="infos-2026"' in h: continue
    if lang=='fr':
      t=name[0].upper()+name[1:]
      sec=nb('<h2 id="infos-2026">Infos pratiques 2026 : '+t+'</h2><ul>'+''.join('<li>'+i+'</li>' for i in items)+'</ul>'+NOTE_FR); key='<h2>Nos conseils'
    else:
      t=name[0].upper()+name[1:]
      sec='<h2 id="infos-2026">Practical info 2026: '+t+'</h2><ul>'+''.join('<li>'+i+'</li>' for i in items)+'</ul>'+NOTE_EN; key='<h2>Tips for'
    assert h.count(key)==1,(f,key)
    h=h.replace(key,sec+'\n    '+key); open(f,'w',encoding='utf-8').write(h); n+=1
print(n)
