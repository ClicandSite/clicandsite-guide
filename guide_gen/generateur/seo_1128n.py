"""Nuit du 28/11/2026 : pages proches de la 1re page (gsc_cibles.md) + étoffage hub Lot."""
import sys, re, json; sys.path.insert(0,'/tmp/g'); import retitle as R
FR='/home/claude/clicandsite-guide'; EN='/home/claude/clicandsite-guide-en'
NB=' '

def rep(root, path, pairs, n_min=1):
    f=f'{root}/{path}/index.html'; s=open(f).read()
    for a,b in pairs:
        rx='[ \u00a0\u202f]+'.join(map(re.escape, re.split('[ \u00a0\u202f]', a)))
        if root==FR: b=R.fr_typo(b)
        s,c=re.subn(rx, lambda m: b, s); assert c>=n_min, (path, a[:60], c)
    open(f,'w').write(s)

def maj(root, path, lang):
    if lang=='fr': rep(root,path,[('Mis à jour le 12 novembre 2026','Mis à jour le 28 novembre 2026')])
    else: rep(root,path,[('Updated 12 November 2026','Updated 28 November 2026')])

# ---------- 1. Musée Grévin (« musée grévin » 27,2 ; « réservation » 17,3 ; « code promo » 20,8)
# Prix guichet 28 € / 19,80 € (tarifs.org vérifié 27/11/2026 + cometoparis) ; billet daté en ligne : prix variable (21 à 23 € selon les sources) -> pas de chiffre.
rep(FR,'paris/musee-grevin',[
 ('billet daté en ligne à partir de 19 € adulte et 16,50 € enfant (5-18 ans) ; nettement plus cher au guichet ; gratuit avant 5 ans.',
  'au guichet, 28 € adulte et 19,80 € enfant (5-18 ans) ; billet daté en ligne moins cher, prix variable selon la date ; gratuit avant 5 ans ; tarif réduit au guichet sur justificatif.'),
 ('Le billet daté acheté en ligne coûte environ 19 € pour un adulte, contre environ 28 € au guichet.',
  'Au guichet, 28 € pour un adulte et 19,80 € pour un enfant de 5 à 18 ans ; gratuit avant 5 ans. Le billet daté acheté en ligne quelques jours avant est moins cher, avec un prix qui varie selon la date (relevé en novembre 2026).'),
 ('<dd>Environ 19 € en ligne</dd>','<dd>28 € au guichet, moins en ligne</dd>')])
R.apply(FR,'paris/musee-grevin',"Musée Grévin : réservation, prix et horaires 2026",
 "Musée Grévin à Paris : billet daté en ligne moins cher que les 28 € du guichet, gratuit avant 5 ans, ouvert tous les jours de 10 h à 18 h (19 h le week-end).",'fr')
R.add_faq(FR,'paris/musee-grevin',"Comment réserver le musée Grévin moins cher ?",
 "Réservez un billet daté sur le site officiel du musée quelques jours avant la visite : il coûte moins cher que le billet non daté vendu 28 € (adulte) au guichet. Des billets combinés, par exemple avec une croisière sur la Seine, existent aussi. Le tarif réduit se demande au guichet, sur justificatif. Relevé en novembre 2026.",'fr')
maj(FR,'paris/musee-grevin','fr')

rep(EN,'paris/musee-grevin',[
 ('dated online ticket from €19 for adults and €16.50 for children (5-18); much more at the desk; free under 5.',
  'at the desk, €28 for adults and €19.80 for children (5-18); dated online tickets are cheaper, with prices varying by date; free under 5; reduced rate at the desk with proof.'),
 ('A dated ticket bought online costs about €19 for an adult, compared with about €28 at the desk.',
  'At the desk, €28 for an adult and €19.80 for a child aged 5 to 18; free under 5. A dated ticket bought online a few days ahead is cheaper, with a price that varies by date (checked in November 2026).'),
 ('<dd>About €19 online</dd>','<dd>€28 at the desk, less online</dd>')])
R.apply(EN,'paris/musee-grevin',"Grévin Museum Paris: Tickets, Prices and Opening Hours",
 "Grévin wax museum in Paris: dated online tickets cost less than the €28 desk price, free under 5, open daily 10am to 6pm (7pm at weekends).",'en')
R.add_faq(EN,'paris/musee-grevin',"How do I book Grévin tickets for less?",
 "Book a dated ticket on the museum's official website a few days before your visit: it costs less than the undated €28 adult ticket sold at the desk. Combined tickets, for example with a Seine cruise, are also available. Reduced rates are given at the desk with proof. Checked in November 2026.",'en')
maj(EN,'paris/musee-grevin','en')

# ---------- 2. Musée d'Orsay (« nocturne orsay jeudi » 15,7 ; « nocturne orsay » 28) — faits déjà dans la page (relevés en novembre 2026)
rep(FR,'paris/musee-d-orsay',[('Le jeudi, le musée reste ouvert jusqu’en soirée, avec une dernière entrée environ 45 minutes avant la fermeture.',
  'Le jeudi, le musée reste ouvert jusqu’à 21 h 45, avec une dernière entrée environ 45 minutes avant la fermeture.')])
R.apply(FR,'paris/musee-d-orsay',"Musée d’Orsay : nocturne du jeudi jusqu’à 21 h 45, tarifs",
 "Musée d’Orsay : nocturne le jeudi jusqu’à 21 h 45 (12 €), 16 € en ligne avec créneau, gratuit avant 18 ans, fermé le lundi. Que voir et conseils de visite.",'fr')
R.add_faq(FR,'paris/musee-d-orsay',"Combien coûte la nocturne du jeudi au musée d’Orsay ?",
 "Le tarif de la nocturne du jeudi soir est de 12 €, contre 16 € pour un billet en ligne avec créneau en journée ; l’entrée reste gratuite pour les moins de 18 ans. Le musée ferme à 21 h 45 ce jour-là. Tarifs relevés en novembre 2026.",'fr')
maj(FR,'paris/musee-d-orsay','fr')
rep(EN,'paris/musee-d-orsay',[('On Thursdays the museum stays open into the evening, with last entry about 45 minutes before closing.',
  'On Thursdays the museum stays open until 9:45pm, with last entry about 45 minutes before closing.')])
R.apply(EN,'paris/musee-d-orsay',"Musée d’Orsay: Thursday Late Opening to 9:45pm, Prices",
 "Musée d’Orsay: open late on Thursdays until 9:45pm (€12), €16 online with a time slot, free for under-18s, closed on Mondays. Highlights and visiting tips.",'en')
R.add_faq(EN,'paris/musee-d-orsay',"How much is the Thursday late opening at the Musée d’Orsay?",
 "The Thursday evening rate is €12, compared with €16 for a daytime online ticket with a time slot; entry is free for under-18s. The museum closes at 9:45pm that day. Prices checked in November 2026.",'en')
maj(EN,'paris/musee-d-orsay','en')

# ---------- 3. Estérel (« criques estérel » 16,7 ; « corniche d or » 13,8) — faits déjà dans la page
R.apply(FR,'cote-d-azur/massif-de-l-esterel',"Estérel : corniche d’Or, criques rouges et randonnées",
 "Massif de l’Estérel : la corniche d’Or de Mandelieu à Saint-Raphaël, les criques d’Anthéor et du Trayas, le pic de l’Ours, le Cap Roux et l’accès en été.",'fr')
R.add_faq(FR,'cote-d-azur/massif-de-l-esterel',"Où sont les plus belles criques de l’Estérel ?",
 "Les petites calanques d’Anthéor et du Trayas, entre les rochers rouges, ont l’eau la plus claire ; la baie d’Agay, au pied du Rastel, est plus abritée. Les criques se voient le mieux depuis la mer : des sorties en bateau partent d’Agay, de Saint-Raphaël et de Cannes. En été, l’accès au massif dépend du risque d’incendie du jour.",'fr')
R.add_faq(FR,'cote-d-azur/massif-de-l-esterel',"Où commence la corniche d’Or ?",
 "La corniche d’Or est la route côtière qui relie Mandelieu-la-Napoule à Saint-Raphaël en longeant les roches rouges de l’Estérel. Ouverte en 1903, elle se parcourt en voiture avec de nombreux points d’arrêt : comptez une heure depuis Cannes avec les pauses.",'fr')
maj(FR,'cote-d-azur/massif-de-l-esterel','fr')
R.apply(EN,'french-riviera/esterel-massif',"Esterel: Corniche d’Or, Red Rock Coves and Hikes",
 "Esterel Massif: the Corniche d’Or from Mandelieu to Saint-Raphaël, the coves of Anthéor and Le Trayas, Pic de l’Ours, Cap Roux and summer access rules.",'en')
R.add_faq(EN,'french-riviera/esterel-massif',"Where are the best coves in the Esterel?",
 "The small calanques of Anthéor and Le Trayas, between the red rocks, have the clearest water; the bay of Agay, below the Rastel, is more sheltered. The coves are best seen from the sea: boat trips leave from Agay, Saint-Raphaël and Cannes. In summer, access to the massif depends on the day's fire risk.",'en')
R.add_faq(EN,'french-riviera/esterel-massif',"Where does the Corniche d’Or start?",
 "The Corniche d’Or is the coast road linking Mandelieu-la-Napoule to Saint-Raphaël along the Esterel's red rocks. Opened in 1903, it is best driven with plenty of stops: allow an hour from Cannes including breaks.",'en')
maj(EN,'french-riviera/esterel-massif','en')
print('ok 1-3')
