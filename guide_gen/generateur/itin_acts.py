import re
R='/home/claude/'
def li(root,src,idx):
    s=open(f'{R}{root}/{src}/index.html').read()
    L=re.findall(r'<li class="act">.*?</li>',s,re.S)
    return L[idx]
JOBS=[
 # fr page, en page, FR title, EN title, anchors, sources [(fr src, en src, idx)]
 ('cote-d-azur/3-jours','french-riviera/3-days','Activités à réserver pour ces trois jours','Activities to book for these three days',('<h2>Le rythme de chaque journée</h2>','<h2>The pace of each day</h2>'),
  [('cote-d-azur/villefranche-sur-mer','french-riviera/villefranche-sur-mer',0),('cote-d-azur/monaco','french-riviera/monaco',1),('cote-d-azur/iles-de-lerins','french-riviera/lerins-islands',0)]),
 ('paris/3-jours','paris/3-days','Activités à réserver pour ces trois jours','Activities to book for these three days',('<h2>Le rythme de chaque journée</h2>','<h2>The pace of each day</h2>'),
  [('paris/sainte-chapelle','paris/sainte-chapelle',0),('paris/louvre','paris/louvre',1),('paris/tour-eiffel','paris/eiffel-tower',1)]),
 ('paris/batignolles','paris/batignolles','Activités à réserver aux Batignolles','Activities to book in Batignolles',('<h2>Questions fréquentes</h2>','<h2>Frequently asked questions</h2>'),
  [None,('paris/montmartre','paris/montmartre',0)]),
]
BAT={'fr':('Visite privée des Batignolles',"Trois heures à pied avec un guide dans le quartier, loin de la foule de Montmartre.","Voir l'offre",'https://www.viator.com/fr-FR/'),
     'en':('Private Batignolles walking tour','Three hours on foot with a guide through the neighbourhood, away from the Montmartre crowds.','See the offer','https://www.viator.com/')}
for fr,en,tf,te,anch,srcs in JOBS:
  for k,(lang,root,path) in enumerate((('fr','clicandsite-guide',fr),('en','clicandsite-guide-en',en))):
    camp=f'clicandsite-{lang}-'+path.replace('/','-')
    lis=''
    for s in srcs:
      if s is None:
        t,d,lab,vp=BAT[lang]
        lis+=f'<li class="act">\n  <h3 class="act__t">{t}</h3><p class="act__d">{d}</p>\n  <p class="act__btns"><a class="bk bk--via" href="{vp}tours/Paris/Explore-Batignolles-the-Art-and-Bohemian-Paris-with-a-Local/d479-30791P281?pid=P00331213&amp;mcid=42383&amp;medium=link&amp;campaign={camp}" rel="sponsored nofollow noopener" target="_blank">{lab}</a></p>\n</li>'
        continue
      x=li(root,s[k],s[2])
      assert 'elite-prestige' not in x
      x=re.sub(r'(cmp=|campaign=)clicandsite-[a-z0-9-]+',r'\g<1>'+camp,x)
      lis+=x
    H=tf if lang=='fr' else te
    lead="Réservation en ligne ; les conditions d'annulation sont indiquées sur chaque offre." if lang=='fr' else "Book online; cancellation terms are shown on each offer."
    note='Liens partenaires.' if lang=='fr' else 'Partner links.'
    book=f'<section class="book" id="reserver" aria-labelledby="reserver-t">\n      <h2 id="reserver-t" class="book__t">{H}</h2>\n      <p class="book__lead">{lead}</p>\n      <ul class="acts">{lis}</ul>\n      <p class="aff-note">{note}</p>\n    </section>'
    p=f'{R}{root}/{path}/index.html'; q=open(p).read()
    assert 'class="book"' not in q and anch[k] in q, p
    q=q.replace(anch[k],book+'\n    '+anch[k],1); open(p,'w').write(q); print('ok',p,lis.count('<li'))
