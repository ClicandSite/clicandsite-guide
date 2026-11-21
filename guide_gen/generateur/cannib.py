import re,html
FR='/home/claude/clicandsite-guide/'; EN='/home/claude/clicandsite-guide-en/'
def e(x): return html.escape(x,quote=False)
def fix(path,title,desc,h1=None,subs=()):
  s=open(path).read()
  ot=re.search(r'<title>(.*?)</title>',s).group(1)
  od=re.search(r'<meta name="description" content="([^"]*)"',s).group(1)
  nt=e(title+' | Clic&Site')
  s=s.replace(ot,nt)  # title, og, twitter
  s=s.replace(od,e(desc))  # meta, og, ld
  if h1:
    s=re.sub(r'(<h1[^>]*>)(.*?)(</h1>)',lambda m:m.group(1)+h1+m.group(3),s,count=1)
  for a,b in subs:
    assert a in s,(path,a); s=s.replace(a,b,1)
  open(path,'w').write(s); print('ok',path,len(title)+12,len(desc))
fix(FR+'paris/montmartre/index.html','Visiter Montmartre : place du Tertre, vignes et ruelles',
 'Visiter la butte Montmartre : la place du Tertre, les vignes, le musée de Montmartre, la rue de l’Abreuvoir et le Bateau-Lavoir. Itinéraire à pied et pièges à éviter.',
 'Visiter Montmartre, la butte des artistes')
fix(EN+'paris/montmartre/index.html','Montmartre: Place du Tertre, Vineyard and Lanes',
 'Exploring the Montmartre hill: Place du Tertre, the vineyard, the Montmartre Museum, Rue de l’Abreuvoir and the Bateau-Lavoir. A walking route and scams to avoid.',
 'Visiting Montmartre, the artists’ hill')
fix(FR+'cote-d-azur/rocher-de-monaco/index.html','Le Rocher de Monaco : visiter Monaco-Ville à pied',
 'Visiter le Rocher, la vieille ville de Monaco : ses ruelles, la cathédrale, les jardins Saint-Martin, la place du Palais. Itinéraire à pied et accès depuis le port.',
 subs=[('ouverts à la visite au printemps et en été. ','ouverts à la visite au printemps et en été (voir notre <a href="../palais-princier/">guide du palais princier</a>). '),
       ('que dirigea le commandant Cousteau.','que dirigea le commandant Cousteau (voir notre <a href="../musee-oceanographique/">guide du musée océanographique</a>).')])
fix(EN+'french-riviera/rocher-de-monaco/index.html','The Rock of Monaco: Exploring Monaco-Ville on Foot',
 'Visiting the Rock, Monaco’s old town: its lanes, the cathedral, the Saint-Martin gardens and Palace Square. A walking route and how to get up from the port.',
 subs=[('open to visitors in spring and summer. ','open to visitors in spring and summer (see our <a href="../palais-princier/">Prince’s Palace guide</a>). '),
       ('once run by Jacques Cousteau.','once run by Jacques Cousteau (see our <a href="../musee-oceanographique/">Oceanographic Museum guide</a>).')])
fix(FR+'cote-d-azur/saint-jean-cap-ferrat/index.html','Saint-Jean-Cap-Ferrat : village, port et plage de Paloma',
 'Visiter Saint-Jean-Cap-Ferrat : le village et son port, la plage de Paloma, la pointe Saint-Hospice et sa chapelle. Accès depuis Nice et Villefranche.')
fix(EN+'french-riviera/saint-jean-cap-ferrat/index.html','Saint-Jean-Cap-Ferrat: Village, Harbour and Paloma Beach',
 'Things to do in Saint-Jean-Cap-Ferrat: the village and its harbour, Paloma beach, Pointe Saint-Hospice and its chapel. Getting there from Nice and Villefranche.')
fix(FR+'cote-d-azur/eze/index.html','Visiter Èze : village perché, jardin et parfumeries',
 'Visiter Èze, le village perché entre Nice et Monaco : ses ruelles médiévales, le jardin d’Èze, les parfumeries. Comment y aller et à quelle heure éviter la foule.')
fix(EN+'french-riviera/eze/index.html','Things to Do in Èze: Hilltop Village, Garden, Perfumeries',
 'Things to do in Èze, the hilltop village between Nice and Monaco: medieval lanes, the Jardin d’Èze, the perfumeries. How to get there and when to beat the crowds.')
fix(FR+'cote-d-azur/roquebrune-cap-martin/index.html','Roquebrune-Cap-Martin : village perché et château',
 'Visiter Roquebrune-Cap-Martin : le château médiéval, le village perché et ses passages voûtés, l’olivier millénaire, le Cap Martin. Accès depuis Monaco et Menton.')
fix(EN+'french-riviera/roquebrune-cap-martin/index.html','Roquebrune-Cap-Martin: Hilltop Village and Castle',
 'Visiting Roquebrune-Cap-Martin: the medieval castle, the hilltop village and its vaulted passages, the thousand-year-old olive tree, Cap Martin. Access from Monaco and Menton.')
fix(FR+'bretagne/ploumanach/index.html','Ploumanac’h et la Côte de Granit Rose : que voir',
 'Visiter Ploumanac’h et la Côte de Granit Rose : les chaos de rochers roses, le phare de Mean Ruz, Perros-Guirec, Trégastel et les Sept-Îles.',
 subs=[('au milieu des rochers roses.','au milieu des rochers roses. C’est un tronçon du <a href="../gr34-sentier-des-douaniers/">GR34</a>.')])
fix(EN+'brittany/ploumanach/index.html','Ploumanac’h and the Pink Granite Coast: What to See',
 'Visiting Ploumanac’h and the Pink Granite Coast: the jumbles of pink rocks, the Mean Ruz lighthouse, Perros-Guirec, Trégastel and the Sept-Îles.',
 subs=[('among the pink rocks.','among the pink rocks. It is a stretch of the <a href="../gr34-sentier-des-douaniers/">GR34</a>.')])
