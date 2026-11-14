"""Remplace les recherches Viator qui partent ailleurs (ou perdent le pid) par la page destination.
Usage : python3 _outils/viator_fix.py write ../clicandsite-guide ../clicandsite-guide-en"""
import re, os, sys, collections
# Recherches Viator testées le 14/11/2026 : premiers résultats sur place -> on garde la recherche
KEEP=set(['arles+amphitheatre', 'avignon+palais+des+papes', 'bayeux+d+day+landing+beaches', 'bayeux+omaha+beach', 'biarritz+aquarium', 'blois+chateau+de+chambord', 'cannes+lerins+islands', 'cap+d+antibes', 'casino+monte+carlo', 'castle+hill+nice', 'chamonix+aiguille+du+midi', 'chamonix+mont+blanc', 'courchevel', 'dune+du+pilat', 'festival+de+cannes', 'fete+du+citron+menton', 'grand+prix+de+monaco', 'lascaux', 'lemon+festival+menton', 'louis+vuitton+foundation', 'louvre', 'marseille+notre+dame+de+la+garde', 'monaco+rocher', 'mont+saint+michel', 'montmartre', 'musee+chagall+nice', 'nice+castle+hill', 'nice+food+tour', 'nice+promenade+des+anglais', 'palace+of+versailles', 'palais+des+papes', 'pantheon+paris', 'paris+arc+de+triomphe', 'paris+belleville', 'paris+canal+saint+martin', 'paris+catacombs', 'paris+champs+elysees', 'paris+conciergerie', 'paris+eiffel+tower', 'paris+louis+vuitton+foundation', 'paris+moulin+rouge', 'paris+musee+de+l+orangerie', 'paris+musee+rodin', 'paris+notre+dame+cathedral', 'paris+pere+lachaise+cemetery', 'paris+sacre+coeur+basilica', 'paris+saint+germain+des+pres', 'paris+sainte+chapelle', 'paris+seine+river', 'pere+lachaise+cemetery', 'picasso+museum+paris', 'remparts+d+antibes', 'rennes+saint+malo+ramparts'])
SUBST={'lerins+islands':'cannes+lerins+islands','paris+montmartre':'montmartre','musee+rodin':'paris+musee+rodin',
       'monaco+palais+princier':'monaco+rocher','pantheon':'pantheon+paris'}
D={'paris':'Paris/d479','nice':'Nice/d478','cannes':'Cannes/d786','antibes':'Antibes/d21941','grasse':'Grasse/d50323',
'menton':'Menton/d23076','villef':'Villefranche-sur-Mer/d50322','frejus':'Frejus-Saint-Raphael/d5223','monaco':'Monaco/d948',
'tropez':'St-Tropez/d4195','toulon':'Toulon/d24308','riviera':'French-Riviera/d179','provence':'Provence/d184',
'avignon':'Avignon/d483','arles':'Arles/d28884','gordes':'Gordes/d50932','marseille':'Marseille/d485','corsica':'Corsica/d4799',
'ajaccio':'Ajaccio/d4192','bergerac':'Bergerac/d24181','bordeaux':'Bordeaux/d468','midipy':'Midi-Pyrenees/d5512',
'lourdes':'Lourdes/d24041','perpignan':'Perpignan/d26343','colmar':'Colmar/d22940','brittany':'Brittany/d21942',
'rennes':'Rennes/d21943','loire':'Loire-Valley/d178','lehavre':'Le-Havre/d4199','bayonne':'Bayonne/d5047',
'biarritz':'Biarritz/d23856','chamonix':'Chamonix/d24269','annecy':'Annecy/d5437','rhone':'Rhone-Alpes/d24268',
'grenoble':'Grenoble/d27067','france':'France/d51'}
M={}
def m(dest,*ks):
    for k in ks: M[k]=dest
m('grenoble','alpe+d+huez','les+2+alpes','briancon','superdevoluy')
m('nice','auron','isola+2000','carnaval+de+nice','nice+carnival','place+massena','nice+place+massena','promenade+des+anglais','port+lympia','musee+matisse+nice','vieux+nice','nice+cours+saleya','saint+paul+de+vence','eze')
m('rhone','avoriaz','morzine','chatel','la+plagne','les+arcs','les+menuires','meribel','tignes','val+d+isere','val+thorens','stations+de+ski+ouvertes','ski+resort+opening+dates')
m('annecy','la+clusaz','haute+savoie'); m('chamonix','megeve')
m('colmar','kaysersberg','riquewihr')
m('bergerac','bergerac','beynac','castelnaud','milandes','marqueyssac','la+roque-gageac','perigueux','sarlat','padirac','rocamadour')
m('bordeaux','bordeaux','saint-emilion'); m('midipy','saint-cirq-lapopie')
m('brittany','carnac','rennes+gulf+of+morbihan','concarneau','concarneau+musee+de+la+peche','concarneau+fishing+museum','quimper','brittany')
m('rennes','saint+malo','dinan')
m('loire','tours+chateau+du+clos+luce','tours+chateau+d+amboise','chateau+de+chambord','chateau+de+chenonceau','tours+chateau+de+chenonceau','chateau+de+villandry','tours+chateau+de+villandry')
m('ajaccio','ajaccio'); m('corsica','bastia','bonifacio','calvi','bonifacio+cliffs+boat','lavezzi','piana+calanques','porto-vecchio')
m('villef','villa+kerylos','villa+ephrussi+de+rothschild','villefranche+sur+mer+villa+ephrussi+de+rothschild')
m('antibes','biot','antibes','juan+les+pins','picasso+museum+antibes','port+vauban','vieil+antibes')
m('cannes','cannes','la+croisette','cannes+la+croisette','le+suquet','cannes+le+suquet','mandelieu','cannes+food+tour','palm+beach','theoule-sur-mer','mougins')
m('frejus','frejus','massif+de+l+esterel','esterel+massif'); m('grasse','gourdon','grasse')
m('monaco','monaco','jardin+exotique+monaco','oceanographic+museum+monaco','prince+palace+monaco','monaco+prince+palace','monaco+port+hercule','port+hercules+monaco','monaco+rock')
m('provence','moustiers+sainte+marie+verdon+gorge','provence'); m('toulon','toulon+ile+de+porquerolles')
m('menton','roquebrune+cap+martin'); m('tropez','saint+tropez'); m('riviera','cote+d+azur+en+hiver','french+riviera+in+winter')
m('france','ou+partir+en+hiver','where+to+go+in+winter')
m('lehavre','etretat'); m('bayonne','bayonne+cathedral','espelette','french+basque+country'); m('biarritz','saint+jean+de+luz')
m('avignon','les+baux+de+provence','l+isle+sur+la+sorgue'); m('gordes','luberon'); m('arles','the+camargue','arles+the+camargue')
m('marseille','calanques+national+park','cassis+calanques+national+park','notre+dame+de+la+garde')
m('lourdes','cauterets','grand+tourmalet','peyragudes','saint+lary'); m('perpignan','font+romeu','pyrenees+orientales')
PAR=['paris+','bastille+paris','batignolles','champs+elysees','chateau+de+chantilly','chateau+de+fontainebleau','compiegne','disneyland+paris','galeries+lafayette+paris','grevin+wax+museum','le+crazy+horse+de+paris','le+marais','les+halles+de+paris','les+invalides','auvers+sur+oise','saint+germain+des+pres','villette+paris','que+faire+a+paris+en+hiver','things+to+do+in+paris+in+winter']
def dest(t):
    if t in M: return D[M[t]]
    if any(t.startswith(p) if p.endswith('+') else t==p for p in PAR): return D['paris']
    return None
pat=re.compile(r'https://www\.viator\.com/(fr-FR/)?searchResults/all\?text=([^&"\']+)(&amp;|&)')
stats=collections.Counter(); unk=set(); files=0
for root in sys.argv[2:]:
  for dp,dn,fn in os.walk(root):
    if '/.git' in dp: continue
    for f in fn:
      if not f.endswith(('.html','.json','.js','.xml')): continue
      p=os.path.join(dp,f); s=open(p,encoding='utf-8',errors='ignore').read()
      if 'searchResults' not in s: continue
      def rep(mo):
        loc,t,amp=mo.group(1) or '',mo.group(2),mo.group(3); tl=t.lower()
        if tl in KEEP: stats['keep']+=1; return mo.group(0)
        if tl in SUBST: stats['subst']+=1; return f'https://www.viator.com/{loc}searchResults/all?text={SUBST[tl]}{amp}'
        d=dest(tl)
        if not d: unk.add(tl); return mo.group(0)
        stats['dest']+=1; return f'https://www.viator.com/{loc}{d}-ttd?'
      n=pat.sub(rep,s)
      if n!=s:
        files+=1
        if sys.argv[1]=='write': open(p,'w',encoding='utf-8').write(n)
print(stats,files,'unknown:',sorted(unk))
