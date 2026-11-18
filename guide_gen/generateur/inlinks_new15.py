import re, sys
sys.path.insert(0,'/tmp/g')
from rando_gen import fr_typo
REG={'alsace':'alsace','normandie':'normandy','bretagne':'brittany','pays-basque':'basque-country','corse':'corsica','pyrenees':'pyrenees'}
N={'eguisheim':('Eguisheim','Eguisheim'),'haut-koenigsbourg':('Le Haut-Kœnigsbourg','Haut-Kœnigsbourg'),'obernai':('Obernai','Obernai'),'mulhouse':('Mulhouse','Mulhouse'),
   'caen':('Caen et le Mémorial','Caen and the Memorial'),'trouville':('Trouville-sur-Mer','Trouville-sur-Mer'),'rennes':('Rennes','Rennes'),'belle-ile':('Belle-Île-en-Mer','Belle-Île-en-Mer'),
   'golfe-du-morbihan':('Le golfe du Morbihan','The Gulf of Morbihan'),'cancale':('Cancale','Cancale'),'hendaye':('Hendaye','Hendaye'),'sare':('Sare','Sare'),
   'corte':('Corte','Corte'),'cap-corse':('Le cap Corse','Cap Corse'),'lourdes':('Lourdes','Lourdes')}
D={'qq':('à quelques kilomètres','a few kilometres away'),'30':('à environ 30 minutes','about 30 minutes away'),'20':('à environ 20 minutes','about 20 minutes away'),
   '50':('à environ 50 minutes','about 50 minutes away'),'train':('à une vingtaine de minutes en train','about twenty minutes by train'),'30km':('à 30 km','30 km away'),
   'pont':('de l’autre côté du pont','across the bridge'),'15km':('à 15 km','15 km away'),'1h':('à environ une heure','about an hour away'),
   'bateau':('en bateau depuis Quiberon','by ferry from Quiberon'),'45':('à environ 45 minutes','about 45 minutes away'),'25':('à environ 25 minutes','about 25 minutes away'),
   'nord':('au nord de Bastia','north of Bastia'),'1h15':('à environ 1 h 15','about 1 hour 15 away'),'voisin':('village voisin','neighbouring village')}
M={'alsace/colmar':[('eguisheim','qq'),('haut-koenigsbourg','30'),('mulhouse','train')],
   'alsace/strasbourg':[('obernai','30km'),('haut-koenigsbourg','50')],
   'alsace/riquewihr':[('haut-koenigsbourg','20'),('eguisheim','20')],
   'alsace/kaysersberg':[('eguisheim','20')],
   'normandie/bayeux':[('caen','30km')],'normandie/plages-du-debarquement':[('caen','30')],
   'normandie/deauville':[('trouville','pont')],'normandie/honfleur':[('trouville','15km')],
   'normandie/mont-saint-michel':[('cancale','50'),('rennes','1h')],
   'bretagne/saint-malo':[('cancale','15km'),('rennes','1h')],'bretagne/dinan':[('rennes','1h')],
   'bretagne/quiberon':[('belle-ile','bateau'),('golfe-du-morbihan','45')],'bretagne/carnac':[('golfe-du-morbihan','30'),('belle-ile','bateau')],
   'pays-basque/saint-jean-de-luz':[('hendaye','15km'),('sare','25')],'pays-basque/la-rhune':[('sare','voisin')],'pays-basque/ainhoa':[('sare','voisin')],
   'corse/bastia':[('cap-corse','nord'),('corte','1h15')],
   'pyrenees/cauterets':[('lourdes','30')],'pyrenees/grand-tourmalet':[('lourdes','45')]}
R={'fr':'/home/claude/clicandsite-guide','en':'/home/claude/clicandsite-guide-en'}
for src, tg in M.items():
    reg, slug = src.split('/')
    for i, lang in enumerate(('fr','en')):
        r = reg if lang=='fr' else REG[reg]
        p = f'{R[lang]}/{r}/{slug}/index.html'; s = open(p, encoding='utf-8').read()
        T = fr_typo if lang=='fr' else (lambda x: x)
        lis = ''.join(f'<li><a href="../../{r}/{t}/">{T(N[t][i])}</a> <span class="near__d">{T(D[d][i])}</span></li>' for t,d in tg if f'../../{r}/{t}/' not in s)
        if not lis: continue
        m = re.search(r'(<h2 id="(?:autour|nearby)">[^<]*</h2><ul class="near">)(.*?)(</ul>)', s)
        if m:
            s = s.replace(m.group(0), m.group(1)+m.group(2)+lis+m.group(3), 1)
        else:
            faq = '<h2>Questions fréquentes</h2>' if lang=='fr' else '<h2>Frequently asked questions</h2>'
            assert faq in s, p
            h = '<h2 id="autour">À voir à proximité</h2>' if lang=='fr' else '<h2 id="nearby">Nearby</h2>'
            s = s.replace(faq, f'{h}<ul class="near">{lis}</ul>\n    {faq}', 1)
        open(p,'w',encoding='utf-8').write(s); print('ok', lang, src)
