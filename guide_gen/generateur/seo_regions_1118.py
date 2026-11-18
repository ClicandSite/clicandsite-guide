import sys; sys.argv=['x']
exec(open('/tmp/g/seo_pass_1116.py').read().split('MAJ_FR=')[0])   # imports fr(), add()
import re, json, html
R='/home/claude/'
F=R+'clicandsite-guide/'; EN=R+'clicandsite-guide-en/'
MF='Informations relevées le 18 novembre 2026 auprès des sites officiels et des offices de tourisme ; horaires et tarifs peuvent changer, vérifiez avant de partir.'
ME='Information checked on 18 November 2026 with the official websites and tourist offices; opening times and prices can change, so check before you go.'

def append(path, items, faq=None, subs=()):
    s=open(path).read()
    en='-en/' in path
    m=re.search(r'(<h2 id="infos-2026">.*?)(</ul>)', s, re.S); assert m, path
    lis=''.join((f'<li><strong>{a}</strong>: {b}</li>' if en else fr(f'<li><strong>{a}</strong> : {b}</li>')) for a,b in items)
    s=s[:m.end(1)]+lis+s[m.end(1):]
    s=re.sub(r'(id="infos-2026".*?<p class="maj">)[^<]*', lambda x: x.group(1)+(ME if en else MF), s, count=1, flags=re.S)
    for a,b in subs:
        assert a in s, (path,a); s=s.replace(a,b)
    open(path,'w').write(s)
    if faq:
        # reuse add()'s FAQ logic via a tiny trick: temporarily remove marker
        t=open(path).read().replace('id="infos-2026"','id="infos-2026-tmp"',1); open(path,'w').write(t)
        add(path,'<div class="faq">','',[],'',faq=faq) if False else None
        s=open(path).read()
        q,a=faq
        if not en: q,a=fr(q),fr(a)
        s=s.replace('<div class="faq">', f'<div class="faq"><details><summary>{html.escape(q,quote=False)}</summary><p>{html.escape(a,quote=False)}</p></details>',1)
        def addld(m):
            j=json.loads(m.group(1)); its=j if isinstance(j,list) else j.get('@graph',[j])
            for x in its:
                if isinstance(x,dict) and x.get('@type')=='FAQPage':
                    x['mainEntity'].insert(0,{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}})
            return '<script type="application/ld+json">'+json.dumps(j,ensure_ascii=False)+'</script>'
        s=re.sub(r'<script type="application/ld\+json">(.*?)</script>',lambda m: addld(m) if 'FAQPage' in m.group(1) else m.group(0),s,flags=re.S)
        s=s.replace('id="infos-2026-tmp"','id="infos-2026"',1)
        open(path,'w').write(s)
    print('ok+',path)

# ---------------- Mont-Saint-Michel
add(F+'normandie/mont-saint-michel/index.html','<h2>Nos conseils pour visiter le Mont-Saint-Michel</h2>','Infos pratiques 2026 : Mont-Saint-Michel',[
 ('Abbaye','ouverte tous les jours de 9 h 30 à 18 h du 1er septembre au 30 avril (dernière entrée à 17 h), et de 9 h à 19 h du 2 mai au 31 août (dernière entrée à 18 h).'),
 ('Jours de fermeture','le 1er janvier, le 1er mai et le 25 décembre.'),
 ('Billets','billet daté à réserver sur le site de l’abbaye, ou billet non daté aux bureaux d’information ; le parcours commenté de 45 minutes se réserve obligatoirement en ligne.'),
 ('Navette Le Passeur','gratuite, du parking au pied du Mont en une douzaine de minutes ; elle circule au moins de 7 h 30 à 23 h et vous dépose à environ 350 mètres de l’entrée.')],MF,
 faq=('Quels sont les horaires de l’abbaye du Mont-Saint-Michel en hiver ?','Du 1er septembre au 30 avril, l’abbaye ouvre tous les jours de 9 h 30 à 18 h, avec une dernière entrée à 17 h. Elle est fermée le 1er janvier, le 1er mai et le 25 décembre.'))
add(EN+'normandy/mont-saint-michel/index.html','<h2>Tips for visiting Mont-Saint-Michel</h2>','Practical info 2026: Mont-Saint-Michel',[
 ('Abbey','open daily from 9.30am to 6pm from 1 September to 30 April (last entry 5pm), and from 9am to 7pm from 2 May to 31 August (last entry 6pm).'),
 ('Closed','on 1 January, 1 May and 25 December.'),
 ('Tickets','a timed ticket can be booked on the abbey’s website, or an open ticket bought at the information offices; the 45-minute guided tour must be booked online.'),
 ('Le Passeur shuttle','free, from the car park to the foot of the Mont in about twelve minutes; it runs at least from 7.30am to 11pm and drops you about 350 metres from the entrance.')],ME,
 faq=('What are the abbey’s opening hours in winter?','From 1 September to 30 April, the abbey is open daily from 9.30am to 6pm, with last entry at 5pm. It is closed on 1 January, 1 May and 25 December.'))

# ---------------- Étretat
add(F+'normandie/etretat/index.html','<h2>Nos conseils pour visiter Étretat</h2>','Infos pratiques 2026 : Étretat',[
 ('Sites interdits','depuis le 28 avril 2025, un arrêté municipal interdit l’accès à plusieurs sites menacés d’éboulement : le tunnel du Trou à l’Homme, la Descente au Chaudron, la Chambre des Demoiselles et les tunnels qui traversent les falaises.'),
 ('Sommet des falaises','accès libre toute l’année par les sentiers ; il n’y a pas de barrière, restez sur le chemin balisé et loin du bord.'),
 ('Marées','à marée montante, le passage au pied de la falaise d’Aval vers la Manneporte peut être coupé en quelques minutes : consultez l’horaire des marées avant de descendre sur l’estran.'),
 ('Sans voiture','Étretat n’a pas de gare ; on vient en train jusqu’au Havre, puis en car.')],MF,
 faq=('Peut-on passer par le Trou à l’Homme à Étretat ?','Non, l’accès est interdit depuis le 28 avril 2025 par arrêté municipal, comme la Descente au Chaudron, la Chambre des Demoiselles et les tunnels des falaises, à cause du risque d’éboulement.'))
add(EN+'normandy/etretat/index.html','<h2>Tips for visiting Étretat</h2>','Practical info 2026: Étretat',[
 ('Closed spots','since 28 April 2025, a town by-law bans access to several spots at risk of rockfall: the Trou à l’Homme tunnel, the Descente au Chaudron, the Chambre des Demoiselles and the tunnels through the cliffs.'),
 ('Clifftops','free access all year along the paths; there is no barrier, so stay on the marked trail and well away from the edge.'),
 ('Tides','on a rising tide, the way along the foot of the Falaise d’Aval towards the Manneporte can be cut off within minutes: check the tide times before heading onto the shore.'),
 ('Without a car','Étretat has no train station; take the train to Le Havre, then the bus.')],ME,
 faq=('Can you go through the Trou à l’Homme in Étretat?','No, access has been banned since 28 April 2025 by a town by-law, along with the Descente au Chaudron, the Chambre des Demoiselles and the cliff tunnels, because of the risk of rockfall.'))

# ---------------- Honfleur
add(F+'normandie/honfleur/index.html','<h2>Nos conseils pour visiter Honfleur</h2>','Infos pratiques 2026 : Honfleur',[
 ('Musée Eugène-Boudin','9 € en plein tarif, gratuit pour les moins de 16 ans ; fermé le mardi. Il réunit les peintres de l’estuaire autour de Boudin, de Courbet à Monet.'),
 ('Autres musées','les Maisons Satie, le musée de la Marine, le musée d’ethnographie et la Lieutenance coûtent 7 € chacun.'),
 ('Pass','le Multi-Pass, à 18 €, donne accès aux cinq musées pendant un an ; le Pass Duo, à 12 €, à deux sites au choix.')],MF,
 faq=('Combien coûte le musée Eugène-Boudin à Honfleur ?','9 € en plein tarif, et c’est gratuit pour les moins de 16 ans. Le Multi-Pass à 18 € donne accès à cinq musées de Honfleur pendant un an.'))
add(EN+'normandy/honfleur/index.html','<h2>Tips for visiting Honfleur</h2>','Practical info 2026: Honfleur',[
 ('Musée Eugène-Boudin','€9 full price, free for under-16s; closed on Tuesdays. It gathers the painters of the estuary around Boudin, from Courbet to Monet.'),
 ('Other museums','the Maisons Satie, the maritime museum, the ethnography museum and the Lieutenance cost €7 each.'),
 ('Passes','the Multi-Pass, at €18, covers all five museums for a year; the Pass Duo, at €12, covers two sites of your choice.')],ME,
 faq=('How much is the Musée Eugène-Boudin in Honfleur?','€9 full price, and free for under-16s. The €18 Multi-Pass gives access to five Honfleur museums for a year.'))

# ---------------- Rouen
add(F+'normandie/rouen/index.html','<h2>Nos conseils pour visiter Rouen</h2>','Infos pratiques 2026 : Rouen',[
 ('Armada 2027','la 9e édition du grand rassemblement de voiliers se tient du 17 au 27 juin 2027 sur les quais de Seine, avec plus de 40 navires ; on visite gratuitement de nombreux bateaux.'),
 ('Gros-Horloge','7,70 € en plein tarif, 3,90 € en tarif réduit, gratuit avant 6 ans ; d’octobre à mars, ouvert de 14 h à 18 h, sauf le lundi.'),
 ('Musée des Beaux-Arts','collection permanente en accès gratuit, avec ses toiles impressionnistes, dont une cathédrale de Rouen de Monet.')],MF,
 faq=('Quand a lieu l’Armada de Rouen 2027 ?','Du 17 au 27 juin 2027, sur les quais de Seine. C’est la 9e édition, avec plus de 40 grands voiliers, et la visite de nombreux bateaux est gratuite.'))
add(EN+'normandy/rouen/index.html','<h2>Tips for visiting Rouen</h2>','Practical info 2026: Rouen',[
 ('Armada 2027','the 9th edition of the great tall ships gathering runs from 17 to 27 June 2027 on the banks of the Seine, with more than 40 ships; many of them can be boarded for free.'),
 ('Gros-Horloge','€7.70 full price, €3.90 reduced, free under 6; from October to March, open from 2pm to 6pm, except Mondays.'),
 ('Musée des Beaux-Arts','free entry to the permanent collection, with its Impressionist paintings, including one of Monet’s Rouen Cathedral series.')],ME,
 faq=('When is the 2027 Rouen Armada?','From 17 to 27 June 2027, on the banks of the Seine. It is the 9th edition, with more than 40 tall ships, and many of them can be visited for free.'))

# ---------------- Plages du Débarquement
add(F+'normandie/plages-du-debarquement/index.html','<h2>Nos conseils pour les plages du Débarquement</h2>','Infos pratiques 2026 : plages du Débarquement',[
 ('Mémorial de Caen','20,80 € en plein tarif, 18,50 € en tarif réduit, gratuit jusqu’à 9 ans ; prévoyez au moins trois heures de visite. Le musée ferme trois semaines en janvier.'),
 ('Cimetière américain de Colleville','entrée gratuite, ouvert tous les jours ; 9 389 soldats américains y reposent, au-dessus d’Omaha Beach.'),
 ('En hiver','les jours sont courts : commencez tôt et gardez les sites en plein air pour le milieu de journée.')],MF,
 faq=('Le cimetière américain de Colleville-sur-Mer est-il gratuit ?','Oui, l’entrée est gratuite et le cimetière est ouvert tous les jours. Comptez une à deux heures de visite.'))
add(EN+'normandy/plages-du-debarquement/index.html','<h2>Tips for the D-Day beaches</h2>','Practical info 2026: the D-Day beaches',[
 ('Mémorial de Caen','€20.80 full price, €18.50 reduced, free up to age 9; allow at least three hours. The museum closes for three weeks in January.'),
 ('Normandy American Cemetery, Colleville','free entry, open every day; 9,389 American soldiers are buried here, above Omaha Beach.'),
 ('In winter','days are short: start early and keep the open-air sites for the middle of the day.')],ME,
 faq=('Is the Normandy American Cemetery at Colleville-sur-Mer free?','Yes, entry is free and the cemetery is open every day. Allow one to two hours.'))

# ---------------- Strasbourg
add(F+'alsace/strasbourg/index.html','<h2>Nos conseils pour le marché de Noël de Strasbourg</h2>','Infos pratiques 2026 : Strasbourg',[
 ('Cathédrale','entrée libre en dehors des offices et de la présentation de l’horloge astronomique.'),
 ('Horloge astronomique','film de présentation à 12 h, puis défilé des apôtres à 12 h 30 ; 2 € en plein tarif, 1,50 € pour les 6-18 ans.'),
 ('Plateforme de la cathédrale','330 marches jusqu’à 66 m de haut, avec vue sur les Vosges et la Forêt-Noire ; 10 € en plein tarif, 6 € pour les 6-18 ans et les étudiants. Elle n’est pas accessible aux personnes à mobilité réduite.')],MF,
 faq=('Combien coûte la montée à la plateforme de la cathédrale de Strasbourg ?','10 € en plein tarif et 6 € pour les 6-18 ans et les étudiants, pour 330 marches jusqu’à 66 mètres de haut.'))
add(EN+'alsace/strasbourg/index.html','<h2>Tips for the Strasbourg Christmas market</h2>','Practical info 2026: Strasbourg',[
 ('Cathedral','free entry outside services and the astronomical clock show.'),
 ('Astronomical clock','an introductory film at noon, then the procession of the apostles at 12.30pm; €2 full price, €1.50 for ages 6-18.'),
 ('Cathedral platform','330 steps up to 66 metres, with views of the Vosges and the Black Forest; €10 full price, €6 for ages 6-18 and students. It is not accessible to people with reduced mobility.')],ME,
 faq=('How much is it to climb to the Strasbourg Cathedral platform?','€10 full price and €6 for ages 6-18 and students, for 330 steps up to 66 metres.'))

# ---------------- Colmar
add(F+'alsace/colmar/index.html','<h2>Nos conseils pour les marchés de Noël de Colmar</h2>','Infos pratiques 2026 : Colmar',[
 ('Musée Unterlinden','le musée du retable d’Issenheim est ouvert du mercredi au lundi de 9 h à 18 h (dernière entrée à 17 h 30), fermé le mardi ; il ferme à 16 h les 24 et 31 décembre.'),
 ('Jours de fermeture','le musée est fermé le 1er janvier, le 1er mai, le 1er novembre et le 25 décembre.'),
 ('Haut-Koenigsbourg','à 26 km de Colmar, le château se pare de décors de Noël du 22 novembre 2026 au 3 janvier 2027 ; entrée à 12 €, 8 € pour les 6-17 ans. Il est fermé les 25 et 26 décembre et le 1er janvier.')],MF,
 faq=('Le musée Unterlinden est-il ouvert pendant les marchés de Noël ?','Oui, du mercredi au lundi de 9 h à 18 h ; il est fermé le mardi et le 25 décembre, et ferme à 16 h les 24 et 31 décembre.'))
add(EN+'alsace/colmar/index.html','<h2>Tips for the Colmar Christmas markets</h2>','Practical info 2026: Colmar',[
 ('Musée Unterlinden','the home of the Isenheim Altarpiece is open Wednesday to Monday from 9am to 6pm (last entry 5.30pm), closed on Tuesdays; it closes at 4pm on 24 and 31 December.'),
 ('Closed','the museum is closed on 1 January, 1 May, 1 November and 25 December.'),
 ('Haut-Koenigsbourg','26 km from Colmar, the castle has Christmas decorations from 22 November 2026 to 3 January 2027; entry €12, €8 for ages 6-17. It is closed on 25 and 26 December and 1 January.')],ME,
 faq=('Is the Musée Unterlinden open during the Christmas markets?','Yes, Wednesday to Monday from 9am to 6pm; it is closed on Tuesdays and on 25 December, and closes at 4pm on 24 and 31 December.'))

# ---------------- Riquewihr
add(F+'alsace/riquewihr/index.html','<h2>Nos conseils pour le marché de Noël de Riquewihr</h2>','Infos pratiques 2026 : Riquewihr',[
 ('Ouverture du marché','un feu d’artifice lance le marché de Noël le vendredi 27 novembre 2026.'),
 ('Concerts','le Chœur d’hommes de Riquewihr chante le 4 décembre et le soir du 24 décembre 2026.'),
 ('Musée du Dolder','la tour-porte de 1291, classée Musée de France, raconte l’histoire de la cité fortifiée ; 3 € l’entrée, 7 € avec la Tour des Voleurs, gratuit pour les moins de 15 ans accompagnés.'),
 ('Tour des Voleurs','l’ancienne prison et une maison de vigneron se visitent d’avril à fin octobre (en 2026, du 3 avril au 31 octobre) ; 5 € l’entrée.')],MF,
 faq=('Y a-t-il un feu d’artifice pour l’ouverture du marché de Noël de Riquewihr ?','Oui, un feu d’artifice lance le marché le vendredi 27 novembre 2026.'))
add(EN+'alsace/riquewihr/index.html','<h2>Tips for the Riquewihr Christmas market</h2>','Practical info 2026: Riquewihr',[
 ('Market opening','fireworks open the Christmas market on Friday 27 November 2026.'),
 ('Concerts','the Riquewihr men’s choir sings on 4 December and on the evening of 24 December 2026.'),
 ('Musée du Dolder','the 1291 gate tower, a listed Musée de France, tells the story of the walled town; €3 entry, €7 with the Thieves’ Tower, free for accompanied under-15s.'),
 ('Thieves’ Tower','the old prison and a winegrower’s house are open from April to the end of October (in 2026, from 3 April to 31 October); €5 entry.')],ME,
 faq=('Are there fireworks for the opening of the Riquewihr Christmas market?','Yes, fireworks open the market on Friday 27 November 2026.'))

# ---------------- Kaysersberg
add(F+'alsace/kaysersberg/index.html','<h2>Nos conseils pour le marché de Noël de Kaysersberg</h2>','Infos pratiques 2026 : Kaysersberg',[
 ('Centre Schweitzer','la maison natale d’Albert Schweitzer, prix Nobel de la paix en 1952, est devenue un centre d’interprétation ; ouvert le lundi et du mercredi au dimanche, de 10 h 30 à 13 h et de 14 h à 17 h 30, jusqu’au 24 décembre, puis du 27 au 31 décembre 2026.'),
 ('Gratuit au Centre Schweitzer','les expositions temporaires, la boutique et la librairie.'),
 ('Château','un escalier d’une centaine de marches mène en haut du donjon, avec la vue sur le village et le vignoble.')],MF,
 faq=('Le Centre Schweitzer de Kaysersberg est-il ouvert en décembre ?','Oui, le lundi et du mercredi au dimanche, de 10 h 30 à 13 h et de 14 h à 17 h 30, jusqu’au 24 décembre, puis du 27 au 31 décembre 2026.'))
add(EN+'alsace/kaysersberg/index.html','<h2>Tips for the Kaysersberg Christmas market</h2>','Practical info 2026: Kaysersberg',[
 ('Centre Schweitzer','the birthplace of Albert Schweitzer, winner of the 1952 Nobel Peace Prize, is now an interpretation centre; open on Mondays and Wednesday to Sunday, from 10.30am to 1pm and 2pm to 5.30pm, until 24 December, then from 27 to 31 December 2026.'),
 ('Free at the Centre Schweitzer','the temporary exhibitions, the shop and the bookshop.'),
 ('Castle','a staircase of about a hundred steps leads to the top of the keep, with views over the village and the vineyards.')],ME,
 faq=('Is the Centre Schweitzer in Kaysersberg open in December?','Yes, on Mondays and Wednesday to Sunday, from 10.30am to 1pm and 2pm to 5.30pm, until 24 December, then from 27 to 31 December 2026.'))

# ---------------- Quimper (ajout)
append(F+'bretagne/quimper/index.html',[
 ('Musée des Beaux-Arts','fermé pour travaux depuis octobre 2024 ; sa réouverture est annoncée pour 2027, à une date encore provisoire.'),
 ('Musée de la Faïence','6 € pour un adulte, ouvert du lundi au samedi de 10 h à 18 h pendant sa saison d’ouverture.')],
 faq=('Le musée des Beaux-Arts de Quimper est-il ouvert ?','Non, il est fermé pour travaux depuis octobre 2024 ; sa réouverture est annoncée pour 2027, à une date encore provisoire.'),
 subs=[('<h3>Le musée des Beaux-Arts</h3><p>Une belle collection de peinture, dont des œuvres de l’école de Pont-Aven.</p>','<h3>Le musée des Beaux-Arts</h3><p>Une belle collection de peinture, dont des œuvres de l’école de Pont-Aven. Il est fermé pour travaux jusqu’à sa réouverture, annoncée pour 2027.</p>'),
       ('le musée des Beaux-Arts et les ateliers de faïence.','le musée de la Faïence et les ateliers de faïence ; le musée des Beaux-Arts est fermé pour travaux jusqu’en 2027.')])
append(EN+'brittany/quimper/index.html',[
 ('Musée des Beaux-Arts','closed for works since October 2024; it is due to reopen in 2027, on a date not yet confirmed.'),
 ('Faience Museum','€6 for an adult, open Monday to Saturday from 10am to 6pm during its opening season.')],
 faq=('Is the Musée des Beaux-Arts in Quimper open?','No, it has been closed for works since October 2024; it is due to reopen in 2027, on a date not yet confirmed.'),
 subs=[('<h3>The Musée des Beaux-Arts</h3><p>A fine painting collection, including works from the Pont-Aven school.</p>','<h3>The Musée des Beaux-Arts</h3><p>A fine painting collection, including works from the Pont-Aven school. It is closed for works until it reopens, planned for 2027.</p>'),
       ('the Musée des Beaux-Arts and the faience workshops.','the Faience Museum and the faience workshops; the Musée des Beaux-Arts is closed for works until 2027.')])

# ---------------- Ploumanac'h (ajout)
append(F+'bretagne/ploumanach/index.html',[
 ('Parkings','le grand parking de Ploumanac’h, chemin du Ranolien, est gratuit (172 places) ; les parkings de Pors Kamor et du Sémaphore sont payants du 28 mars au 1er novembre, celui de Saint-Guirec en juillet et août.'),
 ('Navette d’été','une navette gratuite relie le parking de Ploumanac’h à la plage Saint-Guirec et au port, en juillet et août.'),
 ('Maison du Littoral','face au phare de Men Ruz, elle présente le site et propose des balades guidées.')],
 faq=('Le parking de Ploumanac’h est-il gratuit ?','Oui, le grand parking de Ploumanac’h, chemin du Ranolien, est gratuit. Les parkings de Pors Kamor et du Sémaphore, au départ du sentier, sont payants du 28 mars au 1er novembre.'))
append(EN+'brittany/ploumanach/index.html',[
 ('Car parks','the large Ploumanac’h car park on chemin du Ranolien is free (172 spaces); the Pors Kamor and Sémaphore car parks charge from 28 March to 1 November, and Saint-Guirec in July and August.'),
 ('Summer shuttle','a free shuttle links the Ploumanac’h car park to Saint-Guirec beach and the harbour in July and August.'),
 ('Maison du Littoral','opposite the Men Ruz lighthouse, it presents the site and runs guided walks.')],
 faq=('Is parking free in Ploumanac’h?','Yes, the large Ploumanac’h car park on chemin du Ranolien is free. The Pors Kamor and Sémaphore car parks, at the start of the trail, charge from 28 March to 1 November.'))

# ---------------- Espelette (ajout)
append(F+'pays-basque/espelette/index.html',[
 ('Marché','tous les mercredis matin, toute l’année.'),
 ('Château des Barons d’Ezpeleta','il abrite la mairie et des expositions sur le piment, à voir en une demi-heure.'),
 ('Fêtes du village','au début du mois d’août ; en 2026, elles ont eu lieu du 1er au 5 août.')],
 faq=('Quel jour a lieu le marché d’Espelette ?','Le mercredi matin, toute l’année.'),
 subs=[('chaque année à la fin du mois d’octobre, avec marché et animations.','chaque année le dernier week-end d’octobre, avec marché et animations ; la fête, créée en 1967, a eu lieu les 24 et 25 octobre en 2026.')])
append(EN+'basque-country/espelette/index.html',[
 ('Market','every Wednesday morning, all year round.'),
 ('Château des Barons d’Ezpeleta','it houses the town hall and exhibitions on the pepper, which take about half an hour.'),
 ('Village festival','in early August; in 2026 it ran from 1 to 5 August.')],
 faq=('What day is the Espelette market?','Wednesday morning, all year round.'))
