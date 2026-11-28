import re
FR='/home/claude/clicandsite-guide/'; EN='/home/claude/clicandsite-guide-en/'
N=' '
def ins(root,path,before,html_,sid):
    f=root+path+'/index.html'; s=open(f).read()
    if f'id="{sid}"' in s: return print('déjà',path)
    i=s.index(before); j=s.rfind('<',0,i)
    # remonter au début de la balise <h2 ...>
    j=s.rfind('<h2',0,i+1)
    s=s[:j]+html_+s[j:]; open(f,'w').write(s); print('ok',root[-4:],path)
def tbl(head,rows):
    return '<div class="tbl"><table><thead><tr>'+''.join(f'<th>{h}</th>' for h in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)+'</tbody></table></div>'
# SAINT-LARY
ins(FR,'pyrenees/saint-lary','Nos conseils pour profiter',
 '<h2 id="domaine">Le domaine en chiffres et pour quel niveau</h2>'+tbl(['Pistes','Vertes','Bleues','Rouges','Noires'],[['59 pistes, environ 100 km','7','26','15','11']])+
 f'<p>Le domaine s’étage de 1 700 à 2 515 mètres, sur trois secteurs. <strong>Débutants et enfants</strong> : le Pla d’Adet (1 700 m) a un front de neige skis aux pieds, un jardin des neiges et un Kidpark réservé aux 6-12 ans ; la télécabine depuis le village y monte en 8 minutes environ. <strong>Bons skieurs</strong> : Espiaube et surtout le Vallon du Portet, le versant haute montagne de la station, avec de longues rouges et noires comme la Mirabelle ou Terranère (environ 800 mètres de dénivelé).</p><p>Chiffres du domaine publiés pour la saison (plan des pistes et fiches station) ; le nombre de pistes ouvertes varie chaque jour selon l’enneigement.</p>','domaine')
ins(EN,'pyrenees/saint-lary','Tips for a ski trip',
 '<h2 id="domaine">The ski area in numbers, and which level it suits</h2>'+tbl(['Runs','Green','Blue','Red','Black'],[['59 runs, about 100 km','7','26','15','11']])+
 '<p>The area runs from 1,700 to 2,515 metres across three sectors. <strong>Beginners and children</strong>: Pla d’Adet (1,700 m) has a ski-in, ski-out snow front, a snow garden and a Kidpark for 6 to 12-year-olds; the gondola from the village gets there in about 8 minutes. <strong>Good skiers</strong>: Espiaube and above all the Vallon du Portet, the high-mountain side of the resort, with long reds and blacks such as the Mirabelle or Terranère (about 800 metres of vertical).</p><p>Figures published for the season (piste map and resort fact sheets); the number of open runs changes daily with the snow.</p>','domaine')
# PEYRAGUDES
ins(FR,'pyrenees/peyragudes','Nos conseils pour profiter',
 '<h2 id="domaine">Le domaine en chiffres et pour quel niveau</h2>'+tbl(['Pistes','Vertes','Bleues','Rouges','Noires'],[['Une cinquantaine, environ 60 km','7','21','16','7']])+
 '<p>Les pistes s’étagent de 1 600 à 2 400 mètres, entre les deux fronts de neige de Peyresourde et des Agudes, reliés en altitude. <strong>Débutants</strong> : chaque versant a son espace d’apprentissage, au pied des pistes. <strong>Skieurs moyens</strong> : la Vallée Blanche, une rouge d’environ 5 km qui s’éloigne des remontées. <strong>Sans voiture</strong> : la télécabine Skyvall monte de Loudenvielle (900 m) à Peyresourde (1 600 m), ce qui permet de loger au bord du lac et de rejoindre les pistes directement.</p><p>Répartition des pistes selon le plan publié par la station ; les fiches spécialisées donnent entre 49 et 53 pistes selon le décompte, et l’ouverture dépend chaque jour de l’enneigement.</p>','domaine')
ins(EN,'pyrenees/peyragudes','Tips for a ski trip',
 '<h2 id="domaine">The ski area in numbers, and which level it suits</h2>'+tbl(['Runs','Green','Blue','Red','Black'],[['About fifty, around 60 km','7','21','16','7']])+
 '<p>The runs go from 1,600 to 2,400 metres, between the two snow fronts of Peyresourde and Les Agudes, linked at altitude. <strong>Beginners</strong>: each side has its own learning area at the foot of the slopes. <strong>Intermediates</strong>: the Vallée Blanche, a red run of about 5 km away from the lifts. <strong>Without a car</strong>: the Skyvall gondola climbs from Loudenvielle (900 m) to Peyresourde (1,600 m), so you can stay by the lake and reach the slopes directly.</p><p>Run breakdown from the resort’s published piste map; specialist sites give between 49 and 53 runs depending on how they count, and openings depend on daily snow conditions.</p>','domaine')
# CHÂTEL
ins(FR,'alpes/chatel','Nos conseils pour profiter',
 '<h2 id="domaine">Le domaine en chiffres et pour quel niveau</h2>'+tbl(['Forfait','Domaine','Pistes','Remontées'],[['Espace Liberté','Environ 120 km, de 1 100 à 2 200 m','69','56'],['Portes du Soleil','Environ 600 km, 12 stations franco-suisses','—','—']])+
 '<p>Le forfait Espace Liberté couvre Châtel, La Chapelle-d’Abondance, Torgon et le secteur du Corbeau à Morgins, côté suisse. <strong>Familles et débutants</strong> : Super-Châtel, avec ses pentes douces et son snowpark. <strong>Bons skieurs</strong> : le secteur du Linga et ses noires. Le forfait Portes du Soleil, plus cher, ouvre tout le domaine franco-suisse, avec Avoriaz et Morzine : il vaut surtout le coup pour une semaine. L’aéroport de Genève est à environ 1 h 30 de route.</p><p>Chiffres publiés par l’office de tourisme Haute-Savoie Mont-Blanc et les fiches de la station ; ils varient un peu selon les sources et l’enneigement.</p>','domaine')
ins(EN,'french-alps/chatel','Tips for a ski trip',
 '<h2 id="domaine">The ski area in numbers, and which level it suits</h2>'+tbl(['Lift pass','Area','Runs','Lifts'],[['Espace Liberté','About 120 km, from 1,100 to 2,200 m','69','56'],['Portes du Soleil','About 600 km, 12 French and Swiss resorts','—','—']])+
 '<p>The Espace Liberté pass covers Châtel, La Chapelle-d’Abondance, Torgon and the Corbeau sector of Morgins in Switzerland. <strong>Families and beginners</strong>: Super-Châtel, with gentle slopes and a snowpark. <strong>Good skiers</strong>: the Linga sector and its black runs. The more expensive Portes du Soleil pass opens the whole French-Swiss area, including Avoriaz and Morzine: it is mostly worth it for a full week. Geneva airport is about 1 h 30 by road.</p><p>Figures published by the Haute-Savoie Mont-Blanc tourist office and the resort’s fact sheets; they vary slightly between sources and with snow conditions.</p>','domaine')
