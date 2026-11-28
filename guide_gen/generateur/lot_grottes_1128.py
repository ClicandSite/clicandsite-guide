"""Nuit du 28/11/2026 : hub Lot étoffé (« grottes du lot » pos 6, page < 600 mots) + saison 2027 Pech Merle.
Sources : fiches CRT Occitanie (tourisme-occitanie.com) Pech Merle, Cougnac, Lacave lues le 28/11/2026 ; Padirac repris de la page du guide."""
import sys, re; sys.path.insert(0,'/tmp/g'); import retitle as R
FR='/home/claude/clicandsite-guide'; EN='/home/claude/clicandsite-guide-en'

SEC_FR='''<section class="wrap prose" aria-labelledby="g-grottes"><h2 id="g-grottes" class="sec-title">Les grottes du Lot</h2><p>Le Lot est l’un des départements les plus riches de France en grottes : rivières souterraines, salles de concrétions et grottes ornées de peintures préhistoriques. Presque toutes ferment l’hiver et se visitent du printemps à l’automne, souvent avec un guide. Prévoyez un pull : il fait frais sous terre, même en été.</p><ul><li><strong><a href="../lot/gouffre-de-padirac/">Le gouffre de Padirac</a></strong> : la rivière souterraine à 103 mètres sous terre, parcourue en barque ; environ 1 h 30 de visite, sur créneau. Saison 2026 : du 28 mars au 1er novembre. À 25 minutes de Rocamadour.</li><li><strong><a href="../lot/grotte-du-pech-merle/">La grotte du Pech Merle</a></strong>, à Cabrerets : une vraie grotte ornée (chevaux ponctués, mammouths, mains), en visite guidée uniquement, réservation fortement conseillée. Saison 2027 annoncée du 27 mars au 14 novembre ; à partir de 17 € adulte et 9 € de 5 à 14 ans.</li><li><strong>Les grottes de Lacave</strong> : un petit train électrique s’enfonce sur 400 mètres sous terre, puis la visite guidée à pied (environ 1 h 15) mène à la salle des Merveilles, dont les concrétions brillent sous la lumière noire. Pas de réservation nécessaire ; à partir de 12,50 €.</li><li><strong>Les grottes de Cougnac</strong>, à Payrignac près de Gourdon : peintures préhistoriques (bouquetins, mammouths, grands cervidés) et plafonds couverts de concrétions. Saison 2027 annoncée du 4 avril au 31 octobre ; site non accessible aux personnes à mobilité réduite.</li></ul><p>Padirac et Rocamadour se combinent dans la même journée ; le Pech Merle, dans la vallée du Célé, se combine facilement avec <a href="../lot/saint-cirq-lapopie/">Saint-Cirq-Lapopie</a>, tout proche dans la vallée du Lot. Dates et tarifs relevés en novembre 2026 sur les fiches du Comité régional du tourisme d’Occitanie ; vérifiez sur le site de chaque grotte avant de partir.</p></section>
'''
SEC_EN='''<section class="wrap prose" aria-labelledby="g-grottes"><h2 id="g-grottes" class="sec-title">The caves of the Lot</h2><p>The Lot is one of the richest departments in France for caves: underground rivers, halls of rock formations and caves decorated with prehistoric paintings. Almost all of them close in winter and open from spring to autumn, often with a guide. Bring a jumper: it is cool underground, even in summer.</p><ul><li><strong><a href="../lot/gouffre-de-padirac/">The Gouffre de Padirac</a></strong>: an underground river 103 metres below ground, explored by boat; about 1.5 hours, with timed entry. 2026 season: 28 March to 1 November. 25 minutes from Rocamadour.</li><li><strong><a href="../lot/grotte-du-pech-merle/">Pech Merle cave</a></strong>, in Cabrerets: a real painted cave (spotted horses, mammoths, hands), guided visits only, booking strongly advised. 2027 season announced from 27 March to 14 November; from €17 for adults and €9 for ages 5 to 14.</li><li><strong>The Lacave caves</strong>: a small electric train runs 400 metres underground, then a guided walk (about 1 hour 15) leads to the Hall of Wonders, where the formations glow under black light. No booking needed; from €12.50.</li><li><strong>The Cougnac caves</strong>, in Payrignac near Gourdon: prehistoric paintings (ibex, mammoths, giant deer) and ceilings covered in rock formations. 2027 season announced from 4 April to 31 October; not accessible to people with reduced mobility.</li></ul><p>Padirac and Rocamadour fit into the same day; Pech Merle, in the Célé valley, pairs easily with <a href="../lot/saint-cirq-lapopie/">Saint-Cirq-Lapopie</a>, close by in the Lot valley. Dates and prices checked in November 2026 on the Occitanie regional tourist board listings; check each cave's website before you go.</p></section>
'''
for root, sec, lang in ((FR, SEC_FR, 'fr'), (EN, SEC_EN, 'en')):
    f=f'{root}/lot/index.html'; s=open(f).read()
    if 'g-grottes' not in s:
        if lang=='fr': sec=R.fr_typo(sec)
        s=s.replace('\n</main>', '\n'+sec+'\n</main>',1); assert 'g-grottes' in s
        open(f,'w').write(s)
R.apply(FR,'lot',"Visiter le Lot : grottes, Padirac, Rocamadour, Saint-Cirq",
 "Visiter le Lot : les grottes (Padirac, Pech Merle, Lacave, Cougnac) et leurs saisons 2027, Rocamadour, Saint-Cirq-Lapopie, Cahors et Figeac.",'fr')
R.apply(EN,'lot',"Visiting the Lot: Caves, Padirac, Rocamadour",
 "Visiting the Lot: the caves (Padirac, Pech Merle, Lacave, Cougnac) and their 2027 seasons, Rocamadour, Saint-Cirq-Lapopie, Cahors and Figeac.",'en')

# Pech Merle : saison 2027 + tarifs (fiche CRT Occitanie)
def rep(root, path, a, b):
    f=f'{root}/{path}/index.html'; s=open(f).read()
    rx='[   ]+'.join(map(re.escape, re.split('[   ]', a)))
    if root==FR: b=R.fr_typo(b)
    s,c=re.subn(rx, lambda m: b, s); assert c>=1,(path,a); open(f,'w').write(s)
rep(FR,'lot/grotte-du-pech-merle','En 2026, d’avril à début novembre. Vérifiez les dates sur pechmerle.com.',
 'Elle est fermée l’hiver. La saison 2027 est annoncée du 27 mars au 14 novembre 2027 (en 2026, d’avril à début novembre). Vérifiez les dates sur pechmerle.com.')
R.add_faq(FR,'lot/grotte-du-pech-merle',"Combien coûte la visite de la grotte du Pech Merle ?",
 "À partir de 17 € pour un adulte, 14 € de 15 à 17 ans et 9 € de 5 à 14 ans ; le billet comprend la grotte et le musée. Tarifs relevés en novembre 2026 sur la fiche du Comité régional du tourisme d’Occitanie.",'fr')
rep(EN,'lot/grotte-du-pech-merle','In 2026, from April to early November. Check the dates on pechmerle.com.',
 'It is closed in winter. The 2027 season is announced from 27 March to 14 November 2027 (in 2026, April to early November). Check the dates on pechmerle.com.')
R.add_faq(EN,'lot/grotte-du-pech-merle',"How much does it cost to visit Pech Merle cave?",
 "From €17 for an adult, €14 for ages 15 to 17 and €9 for ages 5 to 14; the ticket covers the cave and the museum. Prices checked in November 2026 on the Occitanie regional tourist board listing.",'en')
for root,a,b in ((FR,'Mis à jour le 15 novembre 2026','Mis à jour le 28 novembre 2026'),(EN,'Updated 15 November 2026','Updated 28 November 2026')):
    f=f'{root}/lot/grotte-du-pech-merle/index.html'; s=open(f).read(); assert a in s; open(f,'w').write(s.replace(a,b))
print('ok lot')
