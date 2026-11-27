import sys,re; sys.path.insert(0,'/tmp/g'); import retitle as R
FR='/home/claude/clicandsite-guide'; EN='/home/claude/clicandsite-guide-en'
N=' '
def add_li(root,path,li):
    f=f'{root}/{path}/index.html'; s=open(f).read()
    if li in s: return
    i=s.index('<h2 id="infos-2026">'); j=s.index('<ul>',i)+4
    s=s[:j]+li+s[j:]; open(f,'w').write(s)
def bump(root,path,fr):
    f=f'{root}/{path}/index.html'; s=open(f).read()
    s=re.sub(r'("dateModified": ")[0-9-]+',r'\g<1>2026-11-27',s)
    s=re.sub(r'Mis à jour le \d+ \w+ 2026','Mis à jour le 27 novembre 2026',s) if fr else re.sub(r'Updated (on )?\d+ \w+ 2026',lambda m:'Updated '+(m.group(1) or '')+'27 November 2026',s)
    open(f,'w').write(s)
# Disneyland FR
p='paris/disneyland-paris'
R.apply(FR,p,"Disneyland Paris : prix d’entrée dès 62 €, billets, RER",
 "Entrée Disneyland Paris : billet daté 1 jour, 1 parc, de 62 à 100 € par adulte selon la date, gratuit avant 3 ans, à acheter avant. Accès en RER A.")
add_li(FR,p,f'<li><strong>Prix d’entrée</strong> : billet daté 1 jour pour 1 parc de 62{N}€ à 100{N}€ environ par adulte selon la date (tarifs relevés le 27 novembre 2026 sur le site officiel), moins cher pour les 3-11 ans, gratuit avant 3 ans. Les billets ne se vendent pas à l’entrée des parcs, sauf exceptions : achetez-les avant.</li>')
R.add_faq(FR,p,"Combien coûte l’entrée à Disneyland Paris ?",f"Un billet daté 1 jour pour 1 parc coûte de 62{N}€ à 100{N}€ environ par adulte selon la date (tarifs relevés le 27 novembre 2026), un peu moins pour les enfants de 3 à 11 ans ; l’entrée est gratuite avant 3 ans. Les billets s’achètent à l’avance, pas à l’entrée des parcs.",after_first=False)
bump(FR,p,1)
# Disneyland EN
R.apply(EN,p,"Disneyland Paris: Tickets from €62, Getting There, Tips",
 "Disneyland Paris entry: a dated 1-day, 1-park ticket costs €62 to €100 per adult depending on the date, free under 3, buy in advance. RER A access.",lang='en')
add_li(EN,p,'<li><strong>Ticket prices</strong>: a dated 1-day, 1-park ticket costs about €62 to €100 per adult depending on the date (prices checked on the official website on 27 November 2026), less for ages 3-11, free under 3. Tickets are not sold at the park gates except in special cases, so buy them in advance.</li>')
R.add_faq(EN,p,"How much is a ticket to Disneyland Paris?","A dated 1-day ticket for one park costs about €62 to €100 per adult depending on the date (prices checked on 27 November 2026), slightly less for children aged 3 to 11; under-3s go in free. Buy tickets in advance: they are not sold at the park gates.",lang='en',after_first=False)
bump(EN,p,0)
# Méribel EN
p='french-alps/meribel'
R.apply(EN,p,"Méribel 2026-2027: Opens 5 December, 3 Valleys Pass",
 "Méribel opens 5 December 2026 to 18 April 2027. 3 Valleys pass €84.20 a day, €421 for 6 days; pedestrian pass €31.40 a day, €284.30 a season.",lang='en')
add_li(EN,p,'<li><strong>Pedestrian pass</strong>: €31.40 a day or €284.30 for the season (single rate from age 5), single lift rides from €12.80, from 5 December 2026 to 18 April 2027. It gives non-skiers access to viewpoints such as the Saulire (2,740 m) and the Col de la Loze.</li>')
R.add_faq(EN,p,"How much is the Méribel pedestrian pass?","In winter 2026-2027 the 3 Valleys pedestrian pass bought from Méribel costs €31.40 a day or €284.30 for the season (single rate from age 5); single lift rides start at €12.80. It covers the lifts that take walkers to viewpoints such as the Saulire and the Col de la Loze.",lang='en',after_first=False)
bump(EN,p,0)
print('ok')
