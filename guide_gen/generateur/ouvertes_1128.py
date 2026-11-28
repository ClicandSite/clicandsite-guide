import sys; sys.path.insert(0,'/tmp/g'); import retitle as R, re
FR='/home/claude/clicandsite-guide'; EN='/home/claude/clicandsite-guide-en'
N=' '
def edit(f,fn):
    s=open(f).read(); t=fn(s); assert t!=s, f; open(f,'w').write(t)
fr=FR+'/idees/stations-de-ski-ouvertes/index.html'; en=EN+'/ideas/ski-resort-opening-dates/index.html'
secfr=(f'<h2 id="deja-ouvertes">Déjà ouvertes au 28 novembre 2026</h2><ul>'
 f'<li><a href="../../alpes/val-thorens/"><strong>Val Thorens</strong></a> : ouverte depuis le 21 novembre, jusqu’au 2 mai 2027 (dates confirmées par le site officiel de la station).</li>'
 f'<li><a href="../../alpes/tignes/"><strong>Tignes</strong></a> : ouverte depuis le 21 novembre, jusqu’au 2 mai 2027 (site officiel de la station).</li>'
 f'<li><a href="../../pyrenees/cauterets/"><strong>Cauterets</strong></a> : ouverture annoncée le 27 novembre au cirque du Lys, la première des Pyrénées.</li>'
 f'<li><strong>Val d’Isère</strong> et <a href="../../alpes/montgenevre/"><strong>Montgenèvre</strong></a> : ouverture annoncée ce samedi 28 novembre.</li></ul>'
 f'<p>La semaine prochaine, Isola 2000 (3 décembre), Courchevel, Font-Romeu et Saint-Lary (4 décembre), puis Méribel, l’Alpe d’Huez, le Grand Tourmalet et Auron (5 décembre) ouvrent à leur tour. Le nombre de pistes ouvertes change chaque jour selon la neige : consultez la page « ouvertures en temps réel » de la station avant de partir.</p>')
secen=(f'<h2 id="deja-ouvertes">Already open on 28 November 2026</h2><ul>'
 f'<li><a href="../../french-alps/val-thorens/"><strong>Val Thorens</strong></a>: open since 21 November, until 2 May 2027 (dates confirmed on the resort’s official website).</li>'
 f'<li><a href="../../french-alps/tignes/"><strong>Tignes</strong></a>: open since 21 November, until 2 May 2027 (resort’s official website).</li>'
 f'<li><a href="../../pyrenees/cauterets/"><strong>Cauterets</strong></a>: opening announced for 27 November at the Cirque du Lys, the first in the Pyrenees.</li>'
 f'<li><strong>Val d’Isère</strong> and <a href="../../french-alps/montgenevre/"><strong>Montgenèvre</strong></a>: opening announced for Saturday 28 November.</li></ul>'
 f'<p>Next week, Isola 2000 (3 December), Courchevel, Font-Romeu and Saint-Lary (4 December), then Méribel, Alpe d’Huez, Grand Tourmalet and Auron (5 December) follow. The number of open runs changes daily with the snow: check the resort’s live opening page before you go.</p>')
for f,k,sec in [(fr,'vérifiez les pistes ouvertes juste avant de partir.</p>',secfr),(en,'check which runs are open just before you go.</p>',secen)]:
    edit(f,lambda s:s.replace(k,k+sec,1) if 'id="deja-ouvertes"' not in s else s)
edit(fr,lambda s:s.replace('jusqu’au début mai 2027','jusqu’au 2 mai 2027'))
edit(en,lambda s:s.replace('until early May 2027','until 2 May 2027'))
R.apply(FR,'idees/stations-de-ski-ouvertes',"Stations de ski ouvertes : Val Thorens, Tignes et dates 2026","Déjà ouvertes : Val Thorens et Tignes depuis le 21 novembre, Cauterets, Val d’Isère et Montgenèvre fin novembre. Toutes les dates d’ouverture 2026-2027.")
R.apply(EN,'ideas/ski-resort-opening-dates',"Ski Resorts Open Now: Val Thorens, Tignes, 2026 Dates","Already open: Val Thorens and Tignes since 21 November, Cauterets, Val d’Isère and Montgenèvre at the end of November. All 2026-2027 opening dates.",lang='en')
for root,p,fq in [(FR,'idees/stations-de-ski-ouvertes',('Quelles stations de ski sont déjà ouvertes ?','Au 28 novembre 2026, Val Thorens et Tignes sont ouvertes depuis le 21 novembre (jusqu’au 2 mai 2027), et Cauterets, Val d’Isère et Montgenèvre ont annoncé leur ouverture pour les 27 et 28 novembre, sous réserve d’enneigement.','fr')),
 (EN,'ideas/ski-resort-opening-dates',('Which ski resorts are already open?','On 28 November 2026, Val Thorens and Tignes have been open since 21 November (until 2 May 2027), and Cauterets, Val d’Isère and Montgenèvre announced their opening for 27 and 28 November, depending on snow.','en'))]:
    R.add_faq(root,p,fq[0],fq[1],lang=fq[2],after_first=False)
for f in (fr,en):
    edit(f,lambda s:re.sub(r'("dateModified": ")[0-9-]+',r'\g<1>2026-11-28',s) if '"dateModified"' in s else s+' ')
print('ok')
