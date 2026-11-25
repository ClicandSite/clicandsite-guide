"""Nuit du 25-26/11/2026 : pages proches de la 1re page (gsc_cibles.md)."""
import sys, re; sys.path.insert(0,'/tmp/g'); import retitle as R
FR='/home/claude/clicandsite-guide'; EN='/home/claude/clicandsite-guide-en'; NB=' '
def sub(root,path,old,new):
    f=f'{root}/{path}/index.html'; s=open(f).read()
    if new in s: return
    o=old if old in s else old.replace(' :',NB+':')
    assert o in s,(path,old); open(f,'w').write(s.replace(o,new.replace(' :',NB+':') if NB in o else new,1))
def mod(root,path,d='2026-11-25'):
    f=f'{root}/{path}/index.html'; s=open(f).read()
    s=re.sub(r'(dateModified": ")[^"]*', r'\g<1>'+d, s); open(f,'w').write(s)

# 1. Route du Mimosa
p='cote-d-azur/route-du-mimosa'
sub(FR,p,'capitale du mimosa dans le Var, avec plus de 90 espèces.','capitale du mimosa dans le Var, avec plus de 90 espèces. Son corso fleuri a lieu les 20 et 21 février 2027 : marché du mimosa gratuit le samedi, défilé des chars le dimanche (entrée payante, billets sur place).')
R.apply(FR,p,'Route du Mimosa 2027 : dates des fêtes et des corsos','Route du Mimosa 2027 : corso de Sainte-Maxime le 7 février, Fête du Mimosa de Mandelieu du 10 au 14 février, corso de Bormes les 20-21 février. Étapes.','fr')
R.add_faq(FR,p,'Quand a lieu la fête du mimosa de Bormes en 2027 ?','Le corso fleuri de Bormes-les-Mimosas a lieu le week-end des 20 et 21 février 2027 : marché du mimosa le samedi (gratuit), défilé des chars fleuris le dimanche (entrée payante, billets vendus sur place). Dates relevées en novembre 2026.','fr')
R.add_faq(FR,p,'Quand a lieu le corso du mimosa de Sainte-Maxime en 2027 ?','Le dimanche 7 février 2027 à 14 h 30 ; gratuit en promenoir, payant en tribune.','fr')
mod(FR,p)
p='french-riviera/mimosa-route'
sub(EN,p,'the Var’s mimosa capital, with more than 90 species.','the Var’s mimosa capital, with more than 90 species. Its flower parade weekend is 20-21 February 2027: free mimosa market on Saturday, float parade on Sunday (paid entry, tickets sold on site).')
R.apply(EN,p,'Mimosa Route 2027: Festival and Parade Dates','Mimosa Route 2027: Sainte-Maxime parade on 7 February, Mandelieu Mimosa Festival 10-14 February, Bormes flower parade 20-21 February. The stops.','en')
R.add_faq(EN,p,'When is the Bormes-les-Mimosas mimosa festival in 2027?','The Bormes-les-Mimosas flower parade weekend is 20-21 February 2027: mimosa market on Saturday (free), float parade on Sunday (paid entry, tickets sold on site). Dates checked in November 2026.','en')
R.add_faq(EN,p,'When is the Sainte-Maxime mimosa parade in 2027?','Sunday 7 February 2027 at 2.30pm; free standing, paid grandstand seats.','en')
mod(EN,p)

# 2. Festival de Cannes 2027
R.apply(FR,'cote-d-azur/festival-de-cannes','Festival de Cannes 2027 : du 11 au 22 mai, 80e édition','Festival de Cannes 2027 : 80e édition du 11 au 22 mai. Voir la montée des marches depuis la Croisette, le Cinéma de la plage gratuit, les invitations.','fr')
R.add_faq(FR,'cote-d-azur/festival-de-cannes','Le Cinéma de la plage est-il gratuit ?','Oui : les projections en plein air sur la plage Macé sont gratuites, dans la limite des places disponibles.','fr')

# 3. Musée Chagall
p='cote-d-azur/musee-chagall'
R.apply(FR,p,'Musée Chagall Nice : tarif 2026 (10 €) et horaires','Musée Chagall à Nice : 10 € (12 € pendant les expositions), gratuit le 1er dimanche du mois. Ouvert de 10 h à 17 h, fermé le mardi. Le Message biblique.','fr')
R.add_faq(FR,p,'Quels sont les horaires du musée Chagall ?','Tous les jours sauf le mardi, de 10 h à 13 h et de 14 h 30 à 17 h (18 h de mai à octobre). Vente des billets jusqu’à 30 minutes avant la fermeture. Horaires relevés en novembre 2026.','fr')
p='french-riviera/musee-chagall'
R.apply(EN,p,'Chagall Museum Nice: €10 Ticket (2026), Opening Times','Chagall Museum in Nice: €10 (€12 during exhibitions), free on the first Sunday of the month. Open 10am to 5pm, closed Tuesdays. The Biblical Message.','en')

# 4. Villa Ephrussi
p='cote-d-azur/villa-ephrussi-de-rothschild'
R.apply(FR,p,'Villa Ephrussi de Rothschild : tarif 2026 (18 €), horaires','Villa Ephrussi de Rothschild à Saint-Jean-Cap-Ferrat : 18 € (12 € réduit, gratuit moins de 7 ans), de 10 h à 18 h en saison. Le palais rose et ses 9 jardins.','fr')
p='french-riviera/villa-ephrussi-de-rothschild'
R.apply(EN,p,'Villa Ephrussi de Rothschild: €18 Ticket (2026), Hours','Villa Ephrussi de Rothschild in Saint-Jean-Cap-Ferrat: €18 (€12 reduced, free under 7), 10am-6pm in season. The pink Belle Époque palace and its gardens.','en')
R.add_faq(EN,'french-riviera/musee-chagall','What are the Chagall Museum opening times?','Daily except Tuesdays, 10am to 1pm and 2.30pm to 5pm (6pm from May to October). Tickets sold until 30 minutes before closing. Times checked in November 2026.','en')
print('ok')
